// THIR periodic failover auditor (Tool 39)
// tools/39_failover_auditor_live.go
// NOTE ON NAME: originally scoped as two tools — "Tool 39 node_healthcheck"
// and "Tool 40 failover_notifier". Merged into one here per request. Named
// "auditor" rather than "notifier" deliberately: this runs on the same 2h
// pipeline.yml cadence as everything else, NOT a tight VM2 cron. HAProxy
// failover resolves in 30-60s (per HA Runbooks RB-04); this tool can only
// ever report what HAProxy's state looks like at the moment the 2h pipeline
// happens to run, so a failover that starts and ends between runs may be
// missed or only seen after the fact. That's an accepted, documented
// tradeoff — "auditor" reflects what this actually is. "Notifier" would
// overpromise real-time behavior this tool does not have.
//
// COVERS TWO INDEPENDENT HAPROXY BACKENDS, confirmed against the live
// /etc/haproxy/haproxy.cfg on VM2 (not assumed from docs):
//   cowrie_backend: vm1 10.0.0.53:2222 <-> vm2_backup 127.0.0.1:4222
//   telnet_backend: vm1_telnet 10.0.0.53:2223 <-> vm2_telnet_backup 127.0.0.1:4223
// These are SEPARATE failover states in HAProxy — SSH can fail over while
// telnet stays up, or vice versa. Originally only cowrie_backend was
// checked here; that left telnet failovers completely silent, same blind
// spot DEBT-4 was about, just relocated to a second backend. Both are now
// checked with identical correlation logic, distinct event types.
//
// HTTP backend (http_honeypot) is commented out in the live cfg pending
// Tool 41 — deliberately not checked here; nothing to correlate against
// yet, and adding a check for a backend that doesn't exist would just be
// noise. Revisit once Tool 41 ships and config/haproxy.cfg's HTTP blocks
// are uncommented.
//
// WHAT THIS DOES:
//   1. Two-state VM1 health check, via SSH relay through VM2 (same
//      mechanism as Tool 05's checkServiceViaSSH — VM1's private VCN IP
//      is not reachable from the GitHub Actions runner directly):
//        - port 22222 (VM1 admin SSH) reachable? — shared across both
//          backends, since it's the same VM1 host being asked twice
//        - the relevant SERVICE port reachable? — 2222 for cowrie_backend,
//          2223 for telnet_backend, checked independently per backend
//      Two states per backend, not three: VM1_UNREACHABLE (admin port
//      closed — applies to both backends identically, since it means the
//      whole host is down) or SERVICE_DOWN (admin port open, that one
//      backend's service port closed). If both ports are open for a given
//      backend, that's just "healthy" — not a distinct alertable state.
//   2. Queries VM2's local HAProxy admin socket (same idiom as Tool 05/
//      Tool 38) for BOTH cowrie_backend and telnet_backend vm1 row status
//      (UP/DOWN), in the same `show stat` call.
//   3. Correlates each backend independently: only fires an event for a
//      given backend when HAProxy reports THAT backend's vm1 row DOWN.
//      When HAProxy says vm1 is UP for both backends, no events are
//      written regardless of node state — this avoids double-alerting
//      alongside Tool 05's own posture.json DEGRADED signal, which
//      already covers "VM1 health, full stop" for the dashboard. This
//      tool is specifically about the FAILOVER correlation, not general
//      VM1 health (that's already Tool 05's job).
//   4. Writes data/failover_events.json — a new Tool-37-consumable input,
//      same pattern as every other data/*.json the alert engine reads.
//      Now a LIST of 0-2 events (one per backend with something to
//      report), not a single object — see schema note below.
//      Does NOT alert directly — Tool 37 owns all alerting (per project
//      convention, confirmed for Tools 38/39/40 alike).
//
// Standard library only — matches every other Go tool in this pipeline.

package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

var (
	sshHost    string
	sshUser    string
	sshPort    int
	sshKey     string
	vm1Host    string // private VCN IP, e.g. 10.0.0.53
	adminPort  int    // VM1 admin SSH port, default 22222 — shared across backends
	cowriePort int    // VM1 Cowrie service port, default 2222
	telnetPort int    // VM1 telnet service port, default 2223
	haproxySock string
	outputFile string
	timeoutSec int
	verboseMode bool
)

func init() {
	flag.StringVar(&sshHost, "ssh-host", "", "VM2 public IP/host to SSH through (jump host).")
	flag.StringVar(&sshUser, "ssh-user", "ubuntu", "SSH user for the VM2 jump host.")
	flag.IntVar(&sshPort, "ssh-port", 22222, "SSH port on VM2 (admin port).")
	flag.StringVar(&sshKey, "ssh-key", "", "Path to private key file for VM2 SSH access.")
	flag.StringVar(&vm1Host, "vm1-host", "10.0.0.53", "VM1 private VCN IP.")
	flag.IntVar(&adminPort, "vm1-admin-port", 22222, "VM1 admin SSH port — proves VM1 itself is alive, shared check for both backends.")
	flag.IntVar(&cowriePort, "vm1-cowrie-port", 2222, "VM1 Cowrie SSH port — cowrie_backend service check.")
	flag.IntVar(&telnetPort, "vm1-telnet-port", 2223, "VM1 Cowrie telnet port — telnet_backend service check.")
	flag.StringVar(&haproxySock, "haproxy-sock", "/var/run/haproxy/admin.sock", "HAProxy admin socket path on VM2.")
	flag.StringVar(&outputFile, "output", "data/failover_events.json", "Path to write failover_events.json.")
	flag.IntVar(&timeoutSec, "timeout", 5, "Per-check timeout in seconds.")
	flag.BoolVar(&verboseMode, "v", false, "Verbose logging to stderr.")
}

// sshRemoteCommand runs a single command on the VM2 jump host and returns
// trimmed stdout. Mirrors checkServiceViaSSH's exec.Command("ssh", ...)
// pattern from Tool 05 — same dependency footprint (none new), same
// reasoning for why a subprocess shell-out is preferred over a Go SSH
// client library for this project.
func sshRemoteCommand(remoteCmd string, timeout time.Duration) (string, error) {
	timeoutSecs := int(timeout.Seconds())
	if timeoutSecs < 1 {
		timeoutSecs = 1
	}
	args := []string{
		"-i", sshKey,
		"-p", strconv.Itoa(sshPort),
		"-o", "StrictHostKeyChecking=no",
		"-o", fmt.Sprintf("ConnectTimeout=%d", timeoutSecs+5),
		"-o", "BatchMode=yes",
		fmt.Sprintf("%s@%s", sshUser, sshHost),
		remoteCmd,
	}
	cmd := exec.Command("ssh", args...)
	var out, errBuf strings.Builder
	cmd.Stdout = &out
	cmd.Stderr = &errBuf
	if err := cmd.Start(); err != nil {
		return "", fmt.Errorf("failed to start ssh: %w", err)
	}
	done := make(chan error, 1)
	go func() { done <- cmd.Wait() }()
	select {
	case err := <-done:
		if err != nil {
			return "", fmt.Errorf("ssh failed: %w (stderr: %s)", err, strings.TrimSpace(errBuf.String()))
		}
		return strings.TrimSpace(out.String()), nil
	case <-time.After(timeout + 10*time.Second):
		_ = cmd.Process.Kill()
		return "", fmt.Errorf("ssh relay timed out")
	}
}

// checkVM1TwoState performs the two TCP checks against VM1 for a given
// service port, both relayed through VM2 since the runner has no route to
// VM1's private VCN IP. servicePort is 2222 for cowrie_backend or 2223 for
// telnet_backend — adminPort (22222) is the same check either way, since
// it's testing the same VM1 host, just asked once per backend for
// independence (no shared state between the two calls).
// Returns one of: "HEALTHY", "SERVICE_DOWN", "VM1_UNREACHABLE", "UNKNOWN".
func checkVM1TwoState(servicePort int, timeout time.Duration) (state string, detail string, err error) {
	remoteCmd := fmt.Sprintf(
		`A=$(timeout %d bash -c 'echo > /dev/tcp/%s/%d' 2>/dev/null && echo UP || echo DOWN); `+
			`S=$(timeout %d bash -c 'echo > /dev/tcp/%s/%d' 2>/dev/null && echo UP || echo DOWN); `+
			`echo "admin=$A service=$S"`,
		int(timeout.Seconds()), vm1Host, adminPort,
		int(timeout.Seconds()), vm1Host, servicePort,
	)
	out, sshErr := sshRemoteCommand(remoteCmd, timeout)
	if sshErr != nil {
		// Can't even reach VM2 to ask — treat conservatively as unknown,
		// not as a VM1 failure (this is a VM2/relay problem, not VM1's).
		return "UNKNOWN", fmt.Sprintf("ssh relay to VM2 failed: %v", sshErr), sshErr
	}

	adminUp := strings.Contains(out, "admin=UP")
	serviceUp := strings.Contains(out, "service=UP")

	switch {
	case adminUp && serviceUp:
		return "HEALTHY", fmt.Sprintf("both admin (22222) and service (%d) reachable", servicePort), nil
	case adminUp && !serviceUp:
		return "SERVICE_DOWN", fmt.Sprintf("VM1 admin port reachable but service port %d closed — likely crashed", servicePort), nil
	default:
		// admin port closed regardless of service state — VM1 itself
		// appears unreachable (network/instance level, not just a
		// single service).
		return "VM1_UNREACHABLE", "VM1 admin port (22222) unreachable — host or network down", nil
	}
}

// checkHAProxyBackends queries VM2's local HAProxy admin socket ONCE for
// both cowrie_backend and telnet_backend vm1 row statuses, parsing both
// out of the same `show stat` response rather than querying twice — same
// socat/show-stat idiom already used in Tool 38 and referenced in HA
// Runbooks RB-04/RB-05. Returns a map keyed by backend name.
func checkHAProxyBackends(timeout time.Duration) (map[string]string, error) {
	remoteCmd := fmt.Sprintf(
		`echo 'show stat' | sudo socat stdio %s 2>/dev/null | `+
			`awk -F',' '$2=="vm1" || $2=="vm1_telnet" {print $1","$18}'`,
		haproxySock,
	)
	out, sshErr := sshRemoteCommand(remoteCmd, timeout)
	results := map[string]string{
		"cowrie_backend": "UNKNOWN",
		"telnet_backend": "UNKNOWN",
	}
	if sshErr != nil {
		return results, sshErr
	}
	for _, line := range strings.Split(strings.TrimSpace(out), "\n") {
		parts := strings.SplitN(line, ",", 2)
		if len(parts) != 2 {
			continue
		}
		backendName, status := strings.TrimSpace(parts[0]), strings.TrimSpace(parts[1])
		if backendName == "" || status == "" {
			continue
		}
		results[backendName] = status
	}
	return results, nil
}

// FailoverEvent is the schema written to data/failover_events.json.
// Deliberately small and flat — matches the simplicity of this project's
// other small status/event files (integrity_status.json, etc.) rather
// than over-modeling something a portfolio dashboard doesn't need.
//
// One event struct per BACKEND now (cowrie + telnet are independent
// failover states) — the output file is a list, not a single object, so
// each gets its own row when something is worth reporting.
type FailoverEvent struct {
	GeneratedAt      time.Time `json:"generated_at"`
	Backend          string    `json:"backend"`            // "cowrie_backend" or "telnet_backend"
	HAProxyVM1Status string    `json:"haproxy_vm1_status"` // UP / DOWN / UNKNOWN
	VM1NodeState     string    `json:"vm1_node_state"`     // HEALTHY / SERVICE_DOWN / VM1_UNREACHABLE / UNKNOWN
	Correlated       bool      `json:"correlated"`         // true if HAProxy DOWN and node check agrees
	EventType        string    `json:"event_type"`         // "" if no event, else one of the types below
	Severity         string    `json:"severity,omitempty"`
	Detail           string    `json:"detail,omitempty"`
	DetectionLagNote string    `json:"detection_lag_note"`
}

// buildEvent runs the correlation logic for ONE backend and returns the
// resulting event. event.EventType is "" when HAProxy reports that
// backend's vm1 row UP — caller decides whether to include empty events
// in the output (we don't, see main()).
func buildEvent(backend string, servicePort int, haproxyStatus string, timeout time.Duration) FailoverEvent {
	nodeState, nodeDetail, nodeErr := checkVM1TwoState(servicePort, timeout)
	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] [%s] VM1 node state: %s (%s)\n", backend, nodeState, nodeDetail)
		fmt.Fprintf(os.Stderr, "[INFO] [%s] HAProxy status: %s\n", backend, haproxyStatus)
	}
	if nodeErr != nil && nodeState == "UNKNOWN" {
		fmt.Fprintf(os.Stderr, "[WARN] [%s] Could not reach VM2 to check VM1: %v\n", backend, nodeErr)
	}

	event := FailoverEvent{
		GeneratedAt:      time.Now().UTC(),
		Backend:          backend,
		HAProxyVM1Status: haproxyStatus,
		VM1NodeState:     nodeState,
		DetectionLagNote: "Checked on the 2h pipeline cadence, not real-time. A failover that starts and resolves between runs may be missed or only visible after the fact (HA Runbooks RB-04: HAProxy itself detects/fails over in 30-60s — this tool does not run that fast).",
	}

	// Correlation logic — see file header for the full rationale.
	// Only emit an event when HAProxy itself reports this backend's vm1
	// row DOWN. If HAProxy says UP, stay silent regardless of node
	// state — Tool 05's posture.json/DEGRADED signal already covers
	// general VM1 health; this tool is specifically about the
	// HAProxy-failover correlation, per backend.
	if haproxyStatus == "DOWN" {
		switch nodeState {
		case "VM1_UNREACHABLE":
			event.Correlated = true
			event.EventType = fmt.Sprintf("failover_confirmed_vm1_unreachable_%s", backend)
			event.Severity = "HIGH"
			event.Detail = fmt.Sprintf("HAProxy (%s) shifted traffic away from VM1, and VM1 is independently confirmed unreachable — real incident, not a flapping health check.", backend)
		case "SERVICE_DOWN":
			event.Correlated = true
			event.EventType = fmt.Sprintf("failover_confirmed_service_down_%s", backend)
			event.Severity = "HIGH"
			event.Detail = fmt.Sprintf("HAProxy (%s) shifted traffic away from VM1. VM1 host is reachable (admin SSH up) but the %s service itself is down — service-level failure, not a host/network failure.", backend, backend)
		case "HEALTHY":
			event.Correlated = false
			event.EventType = fmt.Sprintf("failover_uncorrelated_vm1_appears_healthy_%s", backend)
			event.Severity = "MEDIUM"
			event.Detail = fmt.Sprintf("HAProxy (%s) reports the vm1 backend DOWN, but an independent check right now shows VM1 fully reachable. Possible flapping/transient health-check failure rather than a sustained outage — worth a lower-confidence flag rather than a HIGH-severity incident alert.", backend)
		default: // UNKNOWN — couldn't reach VM2 at all to check
			event.Correlated = false
			event.EventType = fmt.Sprintf("failover_unconfirmed_check_failed_%s", backend)
			event.Severity = "MEDIUM"
			event.Detail = fmt.Sprintf("HAProxy (%s) reports the vm1 backend DOWN, but this tool could not independently verify VM1's state (SSH relay to VM2 itself failed). Treat as a possible incident pending manual check.", backend)
		}
	}

	return event
}

func main() {
	flag.Parse()

	if sshHost == "" || sshKey == "" {
		fmt.Fprintln(os.Stderr, "[ERROR] --ssh-host and --ssh-key are required (this tool only runs via SSH relay through VM2).")
		os.Exit(1)
	}

	timeout := time.Duration(timeoutSec) * time.Second

	haproxyStatuses, hapErr := checkHAProxyBackends(timeout)
	if hapErr != nil {
		fmt.Fprintf(os.Stderr, "[WARN] Could not read HAProxy backend status: %v\n", hapErr)
	}
	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] HAProxy backend statuses: cowrie_backend=%s telnet_backend=%s\n",
			haproxyStatuses["cowrie_backend"], haproxyStatuses["telnet_backend"])
	}

	cowrieEvent := buildEvent("cowrie_backend", cowriePort, haproxyStatuses["cowrie_backend"], timeout)
	telnetEvent := buildEvent("telnet_backend", telnetPort, haproxyStatuses["telnet_backend"], timeout)

	// Only include events that actually have something to report — a
	// quiet run (both backends UP) writes an empty list, same "nothing
	// to see here" convention as Tool 37's own check_* functions
	// returning [] on a quiet run.
	var events []FailoverEvent
	for _, e := range []FailoverEvent{cowrieEvent, telnetEvent} {
		if e.EventType != "" {
			events = append(events, e)
		}
	}
	if events == nil {
		events = []FailoverEvent{} // marshal as [] not null
	}

	data, err := json.MarshalIndent(events, "", "  ")
	if err != nil {
		fmt.Fprintf(os.Stderr, "[ERROR] Failed to marshal failover_events.json: %v\n", err)
		os.Exit(1)
	}
	if err := os.WriteFile(outputFile, data, 0644); err != nil {
		fmt.Fprintf(os.Stderr, "[ERROR] Failed to write %s: %v\n", outputFile, err)
		os.Exit(1)
	}

	if verboseMode {
		if len(events) == 0 {
			fmt.Fprintln(os.Stderr, "[INFO] No failover events — both backends report vm1 UP (or unknown), nothing to report.")
		} else {
			for _, e := range events {
				fmt.Fprintf(os.Stderr, "[INFO] Event written: %s (severity %s)\n", e.EventType, e.Severity)
			}
		}
	}
}

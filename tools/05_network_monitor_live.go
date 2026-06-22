/*
Tool_05 network_monitor (honeypot_liveness_and_asset_inventory)
THIR LIVE PIPELINE — PRODUCTION TOOL
Adapted from: CybersecurityPortfolio/05_network_service_monitor.go

CHANGES FROM ORIGINAL:
  1. Added JSON output mode (encoding/json import)
  2. Added --json flag to write machine-readable posture data
  3. Added CheckedAt timestamp to results
  4. Added ErrorMsg string field (JSON-serialisable, Error interface is not)
  5. writeJSONReport() replaces writeReport() when --json flag is set
  6. All original CLI flags and text-report behaviour preserved

v2 ADDITIONS (ID.AM-1 — Asset Inventory):
  7. Added --assets flag to write data/assets.json alongside posture.json
  8. AssetRecord struct covers: asset_id, hostname, ip, port, role,
     classification, owner, status, first_seen, last_seen
  9. writeAssetsJSON() writes the asset register
 10. Assets file is append-aware: if assets.json exists, first_seen is
     preserved from the existing record so asset age is tracked correctly

NIST CSF COVERAGE:
  posture.json → DE.CM-1  (Honeypot Liveness Monitoring)
  assets.json  → ID.AM-1  (Asset Inventory)

ROLE IN THIR PIPELINE:
  Checks Cowrie honeypot port 2222 on Oracle Cloud VM2 (HAProxy) every 2 hours.
  Writes data/posture.json → portfolio posture dashboard reads it live.
  Writes data/assets.json  → asset inventory for ID.AM-1 coverage.

GITHUB ACTIONS USAGE:
  go run tools/05_network_monitor_live.go \
    -h $ORACLE_VPS_IP -p 2222 \
    --json -o data/posture.json \
    --assets data/assets.json \
    -v
*/

package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
	"os/exec"
	"strconv"
	"strings"
	"time"
)

// Global variables for CLI flags
var (
	host        string
	port        int
	inputFile   string
	outputFile  string
	assetsFile  string // NEW: path for assets.json
	timeoutSec  int
	verboseMode bool
	jsonMode    bool

	// v3 ADDITIONS (DEBT-4 — VM1 visibility via SSH relay through VM2)
	sshHost   string // VM2 public IP/host — the jump host
	sshUser   string // SSH user on VM2, default "ubuntu"
	sshPort   int    // VM2 admin SSH port, default 22222
	sshKey    string // path to private key file for VM2 SSH
	vm1Target string // "10.0.0.53:2222" — host:port to check FROM VM2's side
)

// ServiceCheckResult stores the result of a single service check.
type ServiceCheckResult struct {
	Address   string    `json:"address"`
	Status    string    `json:"status"`
	ErrorMsg  string    `json:"error,omitempty"`
	CheckedAt time.Time `json:"checked_at"`
	Error     error     `json:"-"`
}

// PostureReport is the JSON structure written to data/posture.json
type PostureReport struct {
	GeneratedAt time.Time            `json:"generated_at"`
	Services    []ServiceCheckResult `json:"services"`
	Summary     PostureSummary       `json:"summary"`
    Controls    []CISControl         `json:"cis_controls"`   // ADD THIS LINE
}

type PostureSummary struct {
	Total   int    `json:"total"`
	Up      int    `json:"up"`
	Down    int    `json:"down"`
	Overall string `json:"overall"` // "HEALTHY" | "DEGRADED" | "DOWN"
}

// CISControl represents a single CIS Critical Security Control status.
type CISControl struct {
    ID          string `json:"id"`           // "CIS-1"
    Name        string `json:"name"`         // "Asset Inventory"
    Status      string `json:"status"`       // "ACTIVE" | "MONITORING" | "PLANNED"
    Evidence    string `json:"evidence"`     // brief source description
}

// PostureReport is the JSON structure written to data/posture.json
// Extended: CISControls block added for dashboard Section 05.

// AssetRecord represents a single known asset in the inventory.
// Covers NIST CSF ID.AM-1: Physical devices and systems are inventoried.
type AssetRecord struct {
	AssetID        string    `json:"asset_id"`        // stable identifier, e.g. "thir-honeypot-01"
	Hostname       string    `json:"hostname"`        // DNS name or label
	IPAddress      string    `json:"ip_address"`      // observed IP
	Port           int       `json:"port"`            // monitored port
	Role           string    `json:"role"`            // e.g. "Cowrie SSH Honeypot"
	Classification string    `json:"classification"`  // "PUBLIC" | "INTERNAL" | "SENSITIVE"
	Owner          string    `json:"owner"`           // asset owner / operator
	Platform       string    `json:"platform"`        // "AWS EC2 Ubuntu"
	Status         string    `json:"status"`          // "UP" | "DOWN" | "UNKNOWN"
	FirstSeen      time.Time `json:"first_seen"`      // preserved across runs
	LastSeen       time.Time `json:"last_seen"`       // updated every run
	LastChecked    time.Time `json:"last_checked"`    // timestamp of this check
	NistControl    string    `json:"nist_control"`    // "ID.AM-1"
	NistFunction   string    `json:"nist_function"`   // "IDENTIFY"
}

// AssetInventory is the top-level structure for data/assets.json
type AssetInventory struct {
	GeneratedAt   time.Time     `json:"generated_at"`
	NistControl   string        `json:"nist_control"`   // "ID.AM-1"
	NistFunction  string        `json:"nist_function"`  // "IDENTIFY"
	Description   string        `json:"description"`
	TotalAssets   int           `json:"total_assets"`
	AssetsOnline  int           `json:"assets_online"`
	AssetsOffline int           `json:"assets_offline"`
	Assets        []AssetRecord `json:"assets"`
}

func init() {
	flag.StringVar(&host, "host", "", "Host IP address or hostname to monitor.")
	flag.StringVar(&host, "h", "", "Host IP address or hostname to monitor (shorthand).")
	flag.IntVar(&port, "port", 0, "Port number to monitor.")
	flag.IntVar(&port, "p", 0, "Port number to monitor (shorthand).")
	flag.StringVar(&inputFile, "input", "", "Path to a file containing services to monitor (host:port per line).")
	flag.StringVar(&inputFile, "i", "", "Path to services file (shorthand).")
	flag.StringVar(&outputFile, "output", "", "Path to save posture report. Prints to stdout if not provided.")
	flag.StringVar(&outputFile, "o", "", "Output file path (shorthand).")
	flag.StringVar(&assetsFile, "assets", "", "Path to write asset inventory JSON (data/assets.json). Enables ID.AM-1 coverage.")
	flag.IntVar(&timeoutSec, "timeout", 3, "Connection timeout in seconds.")
	flag.IntVar(&timeoutSec, "t", 3, "Connection timeout in seconds (shorthand).")
	flag.BoolVar(&verboseMode, "verbose", false, "Enable verbose output.")
	flag.BoolVar(&verboseMode, "v", false, "Enable verbose output (shorthand).")
	flag.BoolVar(&jsonMode, "json", false, "Write JSON output for THIR pipeline (posture dashboard).")

	// v3 — VM1 visibility via SSH relay through VM2 (closes DEBT-4)
	flag.StringVar(&sshHost, "ssh-host", "", "VM2 public IP/host to SSH through, to reach VM1's private VCN IP. Leave empty to skip the VM1 check entirely.")
	flag.StringVar(&sshUser, "ssh-user", "ubuntu", "SSH user for the VM2 jump host.")
	flag.IntVar(&sshPort, "ssh-port", 22222, "SSH port on VM2 (admin port — NOT 22, which is Cowrie).")
	flag.StringVar(&sshKey, "ssh-key", "", "Path to private key file for VM2 SSH access.")
	flag.StringVar(&vm1Target, "vm1-target", "", "host:port to check FROM VM2's side over the private VCN, e.g. 10.0.0.53:2222. Requires --ssh-host and --ssh-key.")

	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  Monitors network services. Writes posture + asset inventory for THIR pipeline.\n")
		fmt.Fprintf(os.Stderr, "  Example (pipeline):\n")
		fmt.Fprintf(os.Stderr, "    %s -h $VPS_IP -p 2222 --json -o data/posture.json --assets data/assets.json -v\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  Example (text only):\n")
		fmt.Fprintf(os.Stderr, "    %s -h 192.168.1.1 -p 80\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "Flags:\n")
		flag.PrintDefaults()
	}
}

// checkService attempts TCP connection to the given address.
func checkService(address string, timeout time.Duration) ServiceCheckResult {
	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Checking service: %s\n", address)
	}
	checkedAt := time.Now().UTC()
	conn, err := net.DialTimeout("tcp", address, timeout)
	if err != nil {
		return ServiceCheckResult{
			Address:   address,
			Status:    "DOWN",
			ErrorMsg:  err.Error(),
			Error:     err,
			CheckedAt: checkedAt,
		}
	}
	defer conn.Close()
	return ServiceCheckResult{
		Address:   address,
		Status:    "UP",
		CheckedAt: checkedAt,
	}
}

// checkServiceViaSSH checks a host:port that is only reachable from inside
// the Oracle VCN (e.g. VM1's private IP) by SSHing into a jump host (VM2,
// which IS on the VCN) and running a remote TCP-dial one-liner there.
//
// This exists because GitHub Actions runners have no route to Oracle's
// private VCN (10.0.0.0/24) — they can only reach VM2's public IP directly.
// VM1 is checked BY VM2, not by the runner, using the same internal network
// path the rsync pull already relies on (Master Transition Doc Part 4.7).
//
// Deliberately minimal: a single `timeout N bash -c '</dev/tcp/...'` remote
// command, mirroring the bash TCP-check idiom already used elsewhere in this
// pipeline (e.g. the VCN connectivity checks in the baseline inventory) —
// no new dependency, no Go SSH library, just exec.Command("ssh", ...).
func checkServiceViaSSH(jumpHost, jumpUser string, jumpPort int, keyPath, target string, timeout time.Duration) ServiceCheckResult {
	checkedAt := time.Now().UTC()
	address := target // reported address is the VM1-side target, not the jump host

	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Checking service via SSH relay: %s (through %s@%s:%d)\n", target, jumpUser, jumpHost, jumpPort)
	}

	tcpHost, tcpPort, err := net.SplitHostPort(target)
	if err != nil {
		return ServiceCheckResult{
			Address:   address,
			Status:    "DOWN",
			ErrorMsg:  fmt.Sprintf("invalid --vm1-target %q: %v", target, err),
			CheckedAt: checkedAt,
		}
	}

	timeoutSecs := int(timeout.Seconds())
	if timeoutSecs < 1 {
		timeoutSecs = 1
	}
	remoteCmd := fmt.Sprintf(
		"timeout %d bash -c 'echo > /dev/tcp/%s/%s' 2>/dev/null && echo UP || echo DOWN",
		timeoutSecs, tcpHost, tcpPort,
	)

	args := []string{
		"-i", keyPath,
		"-p", strconv.Itoa(jumpPort),
		"-o", "StrictHostKeyChecking=no",
		"-o", fmt.Sprintf("ConnectTimeout=%d", timeoutSecs+5),
		"-o", "BatchMode=yes",
		fmt.Sprintf("%s@%s", jumpUser, jumpHost),
		remoteCmd,
	}

	cmd := exec.Command("ssh", args...)
	// Hard ceiling so a hung jump-host SSH session can't stall the whole
	// pipeline step beyond the per-check timeout plus connection overhead.
	cmdDone := make(chan error, 1)
	var outBuf, errBuf strings.Builder
	cmd.Stdout = &outBuf
	cmd.Stderr = &errBuf

	if err := cmd.Start(); err != nil {
		return ServiceCheckResult{
			Address:   address,
			Status:    "DOWN",
			ErrorMsg:  fmt.Sprintf("failed to start ssh relay: %v", err),
			CheckedAt: checkedAt,
		}
	}
	go func() { cmdDone <- cmd.Wait() }()

	select {
	case err := <-cmdDone:
		out := strings.TrimSpace(outBuf.String())
		if err != nil {
			// ssh itself failed (jump host unreachable, auth failure, etc.)
			// — distinct from the remote check legitimately reporting DOWN.
			return ServiceCheckResult{
				Address:   address,
				Status:    "DOWN",
				ErrorMsg:  fmt.Sprintf("ssh relay failed: %v (stderr: %s)", err, strings.TrimSpace(errBuf.String())),
				CheckedAt: checkedAt,
			}
		}
		if out == "UP" {
			return ServiceCheckResult{Address: address, Status: "UP", CheckedAt: checkedAt}
		}
		return ServiceCheckResult{
			Address:   address,
			Status:    "DOWN",
			ErrorMsg:  "remote TCP dial from VM2 to VM1 target failed (port closed or VM1 unreachable)",
			CheckedAt: checkedAt,
		}
	case <-time.After(timeout + 10*time.Second):
		_ = cmd.Process.Kill()
		return ServiceCheckResult{
			Address:   address,
			Status:    "DOWN",
			ErrorMsg:  "ssh relay timed out (jump host may be unreachable)",
			CheckedAt: checkedAt,
		}
	}
}


func loadServicesFromFile(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("[ERROR] Failed to open input file %s: %w", filePath, err)
	}
	defer file.Close()

	var services []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			services = append(services, line)
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("[ERROR] Error reading input file %s: %w", filePath, err)
	}
	return services, nil
}

// writeTextReport — original text report, preserved unchanged.
func writeTextReport(results []ServiceCheckResult, output *os.File) {
	fmt.Fprintf(output, "--- Network Service Monitor Report ---\n\n")
	if len(results) == 0 {
		fmt.Fprintln(output, "No services were monitored or no results to report.")
		return
	}
	for _, result := range results {
		fmt.Fprintf(output, "Service: %s\n", result.Address)
		fmt.Fprintf(output, "Status:  %s\n", result.Status)
		if result.ErrorMsg != "" {
			fmt.Fprintf(output, "Error:   %s\n", result.ErrorMsg)
		}
		fmt.Fprintln(output, "------------------------------")
	}
}

// buildCISControls returns the CIS control statuses derived from known
// infrastructure facts. States are static for controls that don't vary
// per run. CIS-1 (asset count) is set dynamically from the service check result.
func buildCISControls(overallStatus string) []CISControl {
    active := "ACTIVE"
    monitoring := "MONITORING"
    planned := "PLANNED"

    controls := []CISControl{
        {ID: "CIS-1",  Name: "Asset Inventory",          Status: active,     Evidence: "assets.json updated every pipeline run by Tool 05 — covers VM2 directly and VM1 via SSH relay"},
        {ID: "CIS-2",  Name: "Software Inventory",       Status: monitoring, Evidence: "data/tool_manifest.json auto-generated from pipeline.yml each run — tracks all active tools, languages, and I/O paths"},
        {ID: "CIS-3",  Name: "Data Protection",          Status: active,     Evidence: "R2 archive encrypted at rest — thirha-raw-archive"},
        {ID: "CIS-4",  Name: "Secure Configuration",     Status: active,     Evidence: "haproxy.cfg, cowrie.cfg, VCN rules in config/"},
        {ID: "CIS-5",  Name: "Account Management",       Status: active,     Evidence: "Two key pairs, dedicated cowrie user, no shared credentials"},
        {ID: "CIS-6",  Name: "Access Control",           Status: active,     Evidence: "Pipeline key vs personal key separation, GitHub Secrets"},
        {ID: "CIS-7",  Name: "Vulnerability Management", Status: monitoring, Evidence: "Oracle security patches — pending regular cadence"},
        {ID: "CIS-8",  Name: "Audit Log Management",     Status: active,     Evidence: "cowrie.json + cowrie.log dual streams, 59-day corpus"},
        {ID: "CIS-9",  Name: "Email/Web Protection",     Status: planned,    Evidence: "cloudflared tunnels planned — direct IP exposure currently"},
        {ID: "CIS-10", Name: "Malware Defence",          Status: active,     Evidence: "Tool 31 malware analysis + Tool 33 YARA classification"},
        {ID: "CIS-11", Name: "Data Recovery",            Status: active,     Evidence: "R2 archive, EBS snapshots, runbook recovery procedures"},
        {ID: "CIS-12", Name: "Network Infrastructure",   Status: active,     Evidence: "VCN private networking, HAProxy TCP LB, Cloudflare DNS"},
    }

    // CIS-1 status reflects current honeypot health
    if overallStatus == "DOWN" {
        controls[0].Status = "MONITORING"
        controls[0].Evidence = "Honeypot DOWN — asset unreachable at check time"
    }

    return controls
}

// writeJSONReport — writes posture.json for the portfolio dashboard.
func writeJSONReport(results []ServiceCheckResult, output *os.File) error {
	up, down := 0, 0
	for _, r := range results {
		if r.Status == "UP" {
			up++
		} else {
			down++
		}
	}

	overall := "HEALTHY"
	if down > 0 && up > 0 {
		overall = "DEGRADED"
	} else if down > 0 {
		overall = "DOWN"
	}

	report := PostureReport{
		GeneratedAt: time.Now().UTC(),
		Services:    results,
		Summary: PostureSummary{
			Total:   len(results),
			Up:      up,
			Down:    down,
			Overall: overall,
		},
	    Controls: buildCISControls(overall),   // ADD THIS LINE
	}

	enc := json.NewEncoder(output)
	enc.SetIndent("", "  ")
	if err := enc.Encode(report); err != nil {
		return fmt.Errorf("[ERROR] Failed to encode JSON: %w", err)
	}
	return nil
}

// loadExistingAssets reads the current assets.json to preserve first_seen timestamps.
// Returns a map of asset_id → AssetRecord. Returns empty map if file doesn't exist.
func loadExistingAssets(filePath string) map[string]AssetRecord {
	existing := make(map[string]AssetRecord)
	data, err := os.ReadFile(filePath)
	if err != nil {
		return existing // file doesn't exist yet — that's fine
	}
	var inv AssetInventory
	if err := json.Unmarshal(data, &inv); err != nil {
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[WARN] Could not parse existing assets.json: %v — will rebuild\n", err)
		}
		return existing
	}
	for _, a := range inv.Assets {
		existing[a.AssetID] = a
	}
	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Loaded %d existing asset record(s) from %s\n", len(existing), filePath)
	}
	return existing
}

// buildAssetRecord constructs an AssetRecord from a ServiceCheckResult.
// Preserves first_seen from existing record if available.
//
// v3: role/classification/platform are now parameters, not hardcoded —
// VM2 (public, HAProxy/pipeline brain) and VM1 (private, sensor node,
// only reachable via the VM2 SSH relay) are different assets with
// different roles and must not share VM2's hardcoded label.
func buildAssetRecord(result ServiceCheckResult, existing map[string]AssetRecord, role, classification, platform string) AssetRecord {
	// Parse host and port from result.Address ("ip:port")
	h, p, err := net.SplitHostPort(result.Address)
	if err != nil {
		h = result.Address
		p = "0"
	}
	portNum := 0
	fmt.Sscanf(p, "%d", &portNum)

	assetID := fmt.Sprintf("thir-honeypot-%s-%s", h, p)

	now := time.Now().UTC()
	firstSeen := now

	// Preserve first_seen if this asset was seen before
	if prev, ok := existing[assetID]; ok {
		firstSeen = prev.FirstSeen
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] Asset %s: preserving first_seen = %s\n", assetID, firstSeen.Format(time.RFC3339))
		}
	} else {
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] Asset %s: new asset, setting first_seen = %s\n", assetID, firstSeen.Format(time.RFC3339))
		}
	}

	lastSeen := now
	if result.Status != "UP" {
		// Don't update last_seen if asset is down — preserve last known-good time
		if prev, ok := existing[assetID]; ok {
			lastSeen = prev.LastSeen
		}
	}

	return AssetRecord{
		AssetID:        assetID,
		Hostname:       h,
		IPAddress:      h,
		Port:           portNum,
		Role:           role,
		Classification: classification,
		Owner:          "aegispub — THIR Project",
		Platform:       platform,
		Status:         result.Status,
		FirstSeen:      firstSeen,
		LastSeen:       lastSeen,
		LastChecked:    now,
		NistControl:    "ID.AM-1",
		NistFunction:   "IDENTIFY",
	}
}

// writeAssetsJSON builds and writes data/assets.json. Covers NIST ID.AM-1.
// AssetMeta carries the per-result labelling that buildAssetRecord needs.
// Passed explicitly by the caller (main) rather than inferred from the
// address (e.g. "private IP => VM1") — inference here would silently
// mislabel any future third asset that doesn't fit the VM1/VM2 pattern.
type AssetMeta struct {
	Role           string
	Classification string
	Platform       string
}

// writeAssetsJSON builds and writes data/assets.json. Covers NIST ID.AM-1.
//
// v3: results and meta are parallel slices — meta[i] describes results[i].
// This is what allows VM1 (sensor, INTERNAL, checked via SSH relay) and
// VM2 (brain, PUBLIC, checked directly) to coexist in the same file with
// correct, distinct labels instead of VM2's role being applied to both.
func writeAssetsJSON(results []ServiceCheckResult, meta []AssetMeta, filePath string) error {
	existing := loadExistingAssets(filePath)

	var assets []AssetRecord
	online, offline := 0, 0

	for i, r := range results {
		asset := buildAssetRecord(r, existing, meta[i].Role, meta[i].Classification, meta[i].Platform)
		assets = append(assets, asset)
		if asset.Status == "UP" {
			online++
		} else {
			offline++
		}
	}

	inventory := AssetInventory{
		GeneratedAt:   time.Now().UTC(),
		NistControl:   "ID.AM-1",
		NistFunction:  "IDENTIFY",
		Description:   "Physical devices and systems within the THIR honeypot infrastructure are inventoried. Updated hourly by Tool 05.",
		TotalAssets:   len(assets),
		AssetsOnline:  online,
		AssetsOffline: offline,
		Assets:        assets,
	}

	data, err := json.MarshalIndent(inventory, "", "  ")
	if err != nil {
		return fmt.Errorf("[ERROR] Failed to marshal assets JSON: %w", err)
	}

	if err := os.WriteFile(filePath, data, 0644); err != nil {
		return fmt.Errorf("[ERROR] Failed to write assets file %s: %w", filePath, err)
	}

	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Asset inventory written to %s (%d asset(s), %d online)\n",
			filePath, len(assets), online)
	}
	return nil
}

func main() {
	flag.Parse()

	if inputFile == "" && (host == "" || port == 0) {
		flag.Usage()
		fmt.Fprintln(os.Stderr, "\n[ERROR] Either an input file (-i) or a host (-h) and port (-p) must be provided.")
		os.Exit(1)
	}
	if inputFile != "" && (host != "" || port != 0) {
		fmt.Fprintln(os.Stderr, "[WARNING] Input file (-i) provided. -host and -port flags will be ignored.")
	}

	var servicesToMonitor []string
	if inputFile != "" {
		loaded, err := loadServicesFromFile(inputFile)
		if err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
		servicesToMonitor = loaded
	} else {
		servicesToMonitor = []string{net.JoinHostPort(host, fmt.Sprintf("%d", port))}
	}

	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Monitoring %d service(s)...\n", len(servicesToMonitor))
	}

	results := make(chan ServiceCheckResult, len(servicesToMonitor))
	timeout := time.Duration(timeoutSec) * time.Second

	for _, svc := range servicesToMonitor {
		go func(s string) {
			results <- checkService(s, timeout)
		}(svc)
	}

	var allResults []ServiceCheckResult
	for range servicesToMonitor {
		allResults = append(allResults, <-results)
	}

	// Every entry in allResults so far came from a direct dial — all VM2
	// (or whatever --host/--input pointed at). Track that for the meta
	// slice below before VM1's SSH-relayed result (if any) gets appended.
	directResultCount := len(allResults)

	// ── v3: VM1 check via SSH relay through VM2 (closes DEBT-4) ───────
	// Only runs if --vm1-target is set. VM1's private VCN IP is not
	// reachable from the GitHub Actions runner directly, so this check
	// is performed BY VM2 (the jump host), not by the runner — see
	// checkServiceViaSSH for the full rationale.
	vm1Checked := false
	if vm1Target != "" {
		if sshHost == "" || sshKey == "" {
			fmt.Fprintln(os.Stderr, "[WARN] --vm1-target given without --ssh-host/--ssh-key — skipping VM1 check")
		} else {
			vm1Result := checkServiceViaSSH(sshHost, sshUser, sshPort, sshKey, vm1Target, timeout)
			allResults = append(allResults, vm1Result)
			vm1Checked = true
			if verboseMode {
				fmt.Fprintf(os.Stderr, "[INFO] VM1 (%s) status: %s\n", vm1Target, vm1Result.Status)
			}
		}
	}

	// ── Write posture.json (DE.CM-1) ──────────────────────────────────
	output := os.Stdout
	if outputFile != "" {
		var err error
		output, err = os.Create(outputFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "[ERROR] Failed to create output file %s: %v\n", outputFile, err)
			os.Exit(1)
		}
		defer output.Close()
	}

	if jsonMode {
		if err := writeJSONReport(allResults, output); err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] posture.json written (DE.CM-1)\n")
		}
	} else {
		writeTextReport(allResults, output)
	}

	// ── Write assets.json (ID.AM-1) ───────────────────────────────────
	if assetsFile != "" {
		// Build per-result metadata: direct-dial results are labelled as
		// the brain node (today this is always VM2 in pipeline.yml usage);
		// the SSH-relayed result, if present, is labelled as the sensor
		// node (VM1) since it's a fundamentally different role/exposure.
		meta := make([]AssetMeta, len(allResults))
		for i := 0; i < directResultCount; i++ {
			meta[i] = AssetMeta{
				Role:           "HAProxy Load Balancer · Pipeline Brain (Oracle VM2)",
				Classification: "PUBLIC",
				Platform:       "Oracle Cloud VM.Standard.E2.1.Micro (Always Free)",
			}
		}
		if vm1Checked {
			meta[len(allResults)-1] = AssetMeta{
				Role:           "Cowrie SSH Honeypot · Sensor Node (Oracle VM1, private VCN)",
				Classification: "INTERNAL",
				Platform:       "Oracle Cloud VM.Standard.E2.1.Micro (Always Free)",
			}
		}

		if err := writeAssetsJSON(allResults, meta, assetsFile); err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] assets.json written (ID.AM-1)\n")
		}
	}

	if verboseMode {
		fmt.Fprintln(os.Stderr, "[INFO] Tool 05 complete.")
	}
	os.Exit(0)
}

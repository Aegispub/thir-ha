# THIR HA — Architecture Reference

*Two-node Oracle Cloud Always Free deployment. Confirmed live as of June 2026.*

---

## Design Principles

**Separation of concerns.** VM1 is the attack surface — exposed to the internet, running honeypots, accepting attacker connections. VM2 is the brain — running the pipeline, hosting HAProxy, never directly exposed to attacker traffic. A compromise of VM1 does not give an attacker access to VM2 or the pipeline.

**Independent failure domains.** VM1 and VM2 are separate Oracle compute instances in the same VCN. Either can be lost without the other going down. VM1 loss triggers HAProxy failover to VM2 standby Cowrie — data capture continues. VM2 loss means the pipeline pauses but VM1 keeps capturing independently.

**Pipeline never touches VM1.** GitHub Actions SSHes to VM2 only. VM1 public IP is never in any GitHub secret. VM2 rsync pulls logs from VM1 via private VCN before the pipeline runs. This keeps the public-facing attack surface isolated from the automation layer.

**Zero external cost.** Oracle Always Free tier (2 VMs), GitHub Pages (dashboard), Cloudflare free tier (DNS, DDoS, health checks), Cloudflare R2 (two buckets — AWS corpus archive and Oracle ongoing archive, zero egress).

---

## Node Specifications

| Property | VM1 — Sensor | VM2 — Brain |
|---|---|---|
| Oracle shape | VM.Standard.E2.1.Micro | VM.Standard.E2.1.Micro |
| vCPU | 1 AMD (full core, not burstable) | 1 AMD (full core, not burstable) |
| RAM | 1GB | 1GB |
| Cost | Always Free | Always Free |
| Public IP | 129.80.119.236 | 150.230.174.199 |
| Private IP | 10.0.0.53 | 10.0.0.73 |
| OS | Ubuntu 22.04.5 LTS | Ubuntu 22.04.5 LTS |
| Kernel | 6.8.0-1054-oracle | 6.8.0-1054-oracle |
| Admin port | 22222 | 22222 |

---

## Services Per Node

### VM1 — Sensor Node

| Service | Port | Binding | Purpose |
|---|---|---|---|
| Cowrie SSH honeypot | 2222 | 0.0.0.0 | Primary SSH attack surface |
| Cowrie Telnet honeypot | 2223 | 0.0.0.0 | Telnet attack surface |
| Cowrie Telnet alt | 2323 | 0.0.0.0 | Alternate telnet port |
| Admin SSH (sshd) | 22222 | 0.0.0.0 | Real management access |
| HTTP honeypot (planned) | 8080 | 127.0.0.1 | Pending Tool 41 — localhost only until HAProxy frontend uncommented |

Port 22 on VM1 redirects to Cowrie port 2222 via iptables. Attackers connecting to port 22 land in the honeypot. Admin access always uses port 22222.

**iptables NAT rules (VM1):**

| Rule | Packets (baseline) | Status |
|---|---|---|
| 22 → 2222 (Cowrie SSH) | Active | ✓ Live |
| 23 → 2223 (Cowrie Telnet) | Active | ✓ Live |
| 80 → 8080 (HTTP honeypot) | 0 packets | Pending Tool 41 |

Rules persist across reboot via `netfilter-persistent`.

### VM2 — Brain Node

| Service | Port | Binding | Purpose |
|---|---|---|---|
| HAProxy SSH frontend | 2222 | 0.0.0.0 | Proxies to VM1 Cowrie; failover to VM2 standby |
| HAProxy Telnet frontend | 2223 | 0.0.0.0 | Proxies to VM1 Cowrie telnet; failover to VM2 standby |
| Admin SSH (sshd) | 22222 | 0.0.0.0 | Real management access |
| Cowrie SSH backup | 4222 | 127.0.0.1 | HAProxy failover target — never public-facing |
| Cowrie Telnet backup | 4223 | 127.0.0.1 | HAProxy failover target — never public-facing |
| Cowrie Telnet alt backup | 4323 | 127.0.0.1 | HAProxy failover target — never public-facing |
| Cowrie pool | 6415 | 127.0.0.1 | Internal Cowrie port — never public-facing |

Port 22 on VM2 is unused. No iptables redirect. Admin access always uses port 22222.

---

## Network Configuration

### Oracle VCN

| Property | Value |
|---|---|
| VCN CIDR | 10.0.0.0/24 |
| Internal MTU | 9000 (Oracle jumbo frames) |
| Internal bandwidth | Up to 10Gbps |
| Cross-VM traffic | Stays on private VCN — never hits public internet |

### VCN Subnet Security List — Required Ingress Rules

| Source | Protocol | Port(s) | Applied To | Purpose |
|---|---|---|---|---|
| 0.0.0.0/0 | TCP | 2222 | Both VMs | Cowrie SSH honeypot (attacker-facing) |
| 0.0.0.0/0 | TCP | 2223 | Both VMs | Cowrie Telnet honeypot (attacker-facing) |
| 0.0.0.0/0 | TCP | 80, 443 | Both VMs | HTTP honeypot (pending Tool 41) |
| Your IP only | TCP | 22222 | Both VMs | Admin SSH — PuTTY access |
| 10.0.0.0/24 | All | All | Both VMs | Internal VCN — rsync, HAProxy backends |

> **Critical Oracle note:** Security rules must be set at the Subnet Security List level, not just instance firewall (iptables/ufw). Both layers must allow traffic. This is the most common Oracle setup mistake.

---

## HAProxy Configuration (VM2)

HAProxy provides TCP-level automatic failover. If VM1 fails two consecutive health checks (60 seconds), SSH and Telnet traffic shifts automatically to VM2 standby Cowrie instances — which listen on localhost-only ports and are never directly reachable from the internet.

Reference config: `config/haproxy.cfg`

| Backend | Primary | Failover | Check interval |
|---|---|---|---|
| `cowrie_backend` | VM1 10.0.0.53:2222 | VM2 127.0.0.1:4222 | 30s, fall 2, rise 2 |
| `telnet_backend` | VM1 10.0.0.53:2223 | VM2 127.0.0.1:4223 | 30s, fall 2, rise 2 |
| `http_honeypot` | VM1 10.0.0.53:8080 | VM2 127.0.0.1:8080 | Commented out — pending Tool 41 |

HAProxy health check fingerprints show in VM1's sshd journal as `kex_exchange_identification` errors from `10.0.0.73`. This is expected behaviour — HAProxy is probing VM1's real sshd on port 22222 as part of the TCP check. Not a security event.

---

## HA Failover Stack

| Layer | Technology | Scope | Failover Time |
|---|---|---|---|
| DNS | Cloudflare health checks | Full VM outage | 60–120 seconds |
| TCP | HAProxy on VM2 | Service crash (Cowrie down, VM up) | 30–60 seconds |
| Tunnel | cloudflared on both VMs | Network blip | 10–30 seconds |
| Data | Rsync over VCN | Log continuity | No real-time gap |

### Failover State Matrix

| VM1 State | VM2 State | Traffic Routing | Action Required |
|---|---|---|---|
| UP | UP | VM1 primary — HAProxy active | None — normal operations |
| DOWN | UP | HAProxy shifts to VM2 standby | Investigate VM1 — RB-02 |
| UP | DOWN | Direct to VM1 — pipeline offline | Restore VM2 — RB-03 |
| DOWN | DOWN | No capture — full outage | Full rebuild — RB-06 |

---

## Data Flow — End to End

```
Attacker connects to thirha.aegispub.com honeypot IP
        │
        ▼
Cloudflare (DNS + DDoS protection)
        │
        ▼
VM2 HAProxy :2222 or :2223
        │  TCP proxy via Oracle VCN private network
        ▼
VM1 Cowrie (10.0.0.53:2222 or :2223)
        │  Captures session, credentials, commands, downloads
        │  Writes to /home/cowrie/cowrie/var/log/cowrie/cowrie.json
        ▼
VM2 rsync cron (runs at :55 every 2 hours)
        │  rsync cowrie@10.0.0.53:/home/cowrie/.../cowrie.json
        │  Destination: /opt/thir/logs/cowrie.json
        ▼
GitHub Actions pipeline (triggers at :00 every 2 hours)
        │  SSHes to VM2 150.230.174.199 port 22222
        │  Reads /opt/thir/logs/cowrie.json from watermark
        │  Runs Tools 05, 26, 34, 35, 36, 27, 29, 30, 30b
        │  Conditional: Tools 31, 33 if downloads present
        │  Runs Tools 28, 37, 32, 07
        │  git push data/ + reports/
        ▼
GitHub Pages → thirha.aegispub.com
```

---

## SSH Key Architecture

| Key | File | Fingerprint | Used By |
|---|---|---|---|
| Personal access | `thir-pipeline-key.ppk` / `.pem` | `SHA256:0Xko5IkOIR5n3oSNER34aXPBbV7bJuERM4FYESrEriw` | PuTTY admin SSH to both VMs (port 22222) |
| Pipeline access | `thir_pipeline_key` | `SHA256:csenfxiT4p6AvVKwjTTV35EGpJ8ZkVdeyen2LfsoBA8` | GitHub Actions secret `ORACLE_VPS_SSH_KEY` |
| Internal rsync | `thir_internal` (VM2 only) | `SHA256:t5zmp2Dmw0wPBlp8aKM62buYg3vZJ6pFIHxKxmENvg8` | VM2 rsync pulls from VM1 cowrie user |

Both public keys (personal + pipeline) are in `authorized_keys` on both VMs for the `ubuntu` user. The internal rsync key public half is in `authorized_keys` on VM1 for the `cowrie` user only — VM2 cowrie user has no authorized keys.

---

## Raw Log Archival

Raw Cowrie logs are archived to Cloudflare R2 — they are never stored in the GitHub repo. Two separate buckets exist for two distinct corpora.

### AWS Corpus — `thir-raw-archive`

| Property | Value |
|---|---|
| Bucket | `thir-raw-archive` (Cloudflare R2) |
| Coverage | March 7 2026 – AWS EC2 retirement (~Sep 2026) |
| Status | Complete — all 59+ days uploaded before AWS retires |
| Format | Compressed: `cowrie.json.YYYY-MM-DD.gz` (~90% reduction) |
| Structure | `cowrie-json/YYYY-MM/` and `cowrie-log/YYYY-MM/` |
| Purpose | Historical corpus — source data for Tool 00 historical processor |

This bucket captures everything from the AWS single-node deployment. It is a one-time archive — no ongoing sync after AWS EC2 is terminated.

### Oracle Corpus — `thirha-raw-archive`

| Property | Value |
|---|---|
| Bucket | `thirha-raw-archive` (Cloudflare R2) |
| Coverage | June 2026 onwards — Oracle VM1 production logs |
| Status | Active — daily sync running |
| Format | Compressed: `cowrie.json.YYYY-MM-DD.gz` (~90% reduction) |
| Structure | `cowrie-json/YYYY-MM/` and `cowrie-log/YYYY-MM/` |
| Sync script | `/home/ubuntu/sync_to_r2.sh` (VM2) |
| Cron schedule | Daily at 01:00 UTC — previous day's logs |
| Tool | rclone v1.74.3 — configured for ubuntu user |
| Purpose | Ongoing Oracle corpus — permanent raw log backup |

---

## Tool Architecture

### Tool 05 vs Tool 39 — Health Check Separation

Tool 05 (`05_network_monitor_live.go`) checks VM2's HAProxy port 2222. It confirms the full HAProxy→Cowrie path is functioning and writes `data/posture.json` and `data/assets.json`. It runs via GitHub Actions and sees the system from the outside.

Tool 39 (`39_node_healthcheck.go`) — **planned** — checks VM1 directly at `10.0.0.53` via the private VCN. It detects degraded VM1 states that HAProxy hasn't failed yet (Cowrie process slowing, disk pressure, high session load). It writes `data/node_health.json` — a separate file that does not conflict with Tool 05's output.

This separation means:
- Tool 05 output: "Can GitHub Actions reach a working honeypot via VM2?" — answers the pipeline question
- Tool 39 output: "Is VM1 itself healthy?" — answers the infrastructure question

Both run every pipeline cycle. Tool 05 runs first (step 4). Tool 39 runs after the log fetch (planned position: after Tool 26, before Tool 27 — so node health context is available to enrichment tools).

### Tool 38 — Structured Rsync Collector

The current rsync mechanism is a shell script (`/home/ubuntu/rsync_from_vm1.sh`) running as a VM2 cron job. Tool 38 (`38_rsync_collector.py`) replaces this with a Python-managed process that adds:
- Structured JSON logging of every sync operation
- Line count verification (VM1 source vs VM2 destination)
- Download directory sync with ownership handling
- Error reporting to a file the pipeline can read

When Tool 38 is deployed, the shell cron job is retired. Tool 38 runs as a VM2 cron job at the same `:55` schedule.

---

## Resource Profile

Captured June 2026 — typical operational state:

| Metric | VM1 | VM2 | Notes |
|---|---|---|---|
| RAM used | 315MB / 956MB | 277MB / 956MB | Both well within 1GB limit |
| CPU | 0% | 0% | Idle between pipeline runs |
| Load average | 0.00 | 0.07 | Flat |
| Swap | None | None | Not configured |
| Disk used | 4.0GB / 45GB (9%) | 4.1GB / 45GB (9%) | Ample headroom |

---

## Recovery Runbooks

Full recovery procedures for all failure scenarios are in `docs/THIR_HA_Runbooks_v2.docx`.

| Runbook | Scenario | RTO |
|---|---|---|
| RB-01 | Architecture reference | — |
| RB-02 | VM1 sensor failure | < 45 min |
| RB-03 | VM2 brain failure | < 30 min |
| RB-04 | Failover procedure | < 5 min (auto) |
| RB-05 | HAProxy + Cloudflare recovery | < 15 min |
| RB-06 | Full stack rebuild | < 90 min |

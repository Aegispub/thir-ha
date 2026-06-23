# THIR — Threat Hunter Intelligence Range
## OPERATIONS & RECOVERY RUNBOOK SET
### Oracle Cloud HA Architecture · Two-Node Deployment

| Field | Value |
|---|---|
| Document Version | v2.1 — June 2026 |
| Supersedes | v2.0 (May 2026) — corrected private IPs, HAProxy backup ports, telnet backend, iptables restore, cloudflared status |
| Architecture | Oracle Cloud Always Free — 2× VM.Standard.E2.1.Micro |
| Replaces | `docs/runbook_rc_rp_1.md` (AWS EC2 single node) |
| Owner | Joy Dane |
| Classification | Internal — THIR Project |
| Live dashboard | thirha.aegispub.com |

---

## Runbook Index

| ID | Runbook | Scenario | NIST CSF |
|---|---|---|---|
| RB-01 | Architecture Overview | Reference — system design and data flow | ID.AM |
| RB-02 | VM1 Sensor Failure | Cowrie node down or compromised | RC.RP-1 |
| RB-03 | VM2 Brain Failure | Pipeline node down, data at risk | RC.RP-1 |
| RB-04 | Failover Procedure | Manual and automatic failover steps | RS.RP-1 |
| RB-05 | HAProxy & Cloudflare | Load balancer recovery and config | PR.IP-1 |
| RB-06 | Full Stack Rebuild | Both nodes lost — start from zero | RC.RP-1 |

## Recovery Time Objectives

| Scenario | RTO Target | RPO Target | Runbook |
|---|---|---|---|
| VM1 (Cowrie) failure | < 5 min (auto) | 0 — HAProxy shifts traffic | RB-02, RB-04 |
| VM2 (pipeline) failure | < 30 min manual | < 2h — last rsync | RB-03 |
| Cloudflare/HAProxy failure | < 15 min | 0 — config restore | RB-05 |
| Full stack loss | < 90 min | Last git push to GitHub | RB-06 |

---

# RB-01 — Architecture Overview

| Field | Value |
|---|---|
| Document ID | THIR-RB-01 |
| Type | Reference |
| NIST CSF | ID.AM-1 — Asset Management |
| Last Reviewed | June 2026 |

## Confirmed Live Node Specifications

| Property | VM1 — Sensor | VM2 — Brain |
|---|---|---|
| Name | thir-honeypot-vm1 | thir-pipeline-vm2 |
| Oracle shape | VM.Standard.E2.1.Micro | VM.Standard.E2.1.Micro |
| vCPU | 1 AMD (full core) | 1 AMD (full core) |
| RAM | 1GB | 1GB |
| OS | Ubuntu 22.04.5 LTS | Ubuntu 22.04.5 LTS |
| Kernel | 6.8.0-1054-oracle | 6.8.0-1054-oracle |
| Public IP | 129.80.119.236 | 150.230.174.199 |
| Private IP | **10.0.0.53** | **10.0.0.73** |
| Admin SSH port | 22222 | 22222 |
| Live since | 2026-06-08 05:50 UTC | 2026-06-08 05:50 UTC |

> **Private IP note:** Oracle assigned `10.0.0.53` (VM1) and `10.0.0.73` (VM2) at provisioning. The planned values `10.0.0.1` / `10.0.0.2` were not available. All configs, commands, and runbook procedures use the actual assigned values.

## Services Per Node

### VM1 — Sensor Node

| Service | Port | Binding | Status |
|---|---|---|---|
| Cowrie SSH honeypot | 2222 | 0.0.0.0 | ✓ Live |
| Cowrie Telnet honeypot | 2223 | 0.0.0.0 | ✓ Live |
| Cowrie Telnet alt | 2323 | 0.0.0.0 | ✓ Live |
| Admin SSH (sshd) | 22222 | 0.0.0.0 | ✓ Live |
| HTTP honeypot | 8080 | 127.0.0.1 | → Planned (Tool 41, gate July 8 2026) |

**iptables NAT rules (VM1):**

| Rule | Confirmed Status |
|---|---|
| Port 22 → 2222 (Cowrie SSH) | ✓ Active — 3,899 packets at baseline |
| Port 23 → 2223 (Cowrie Telnet) | ✓ Active — 3,199 packets at baseline |
| Port 80 → 8080 (HTTP honeypot) | → In place, 0 packets — waiting for Tool 41 |

Rules persist across reboot via `netfilter-persistent.service` (enabled ✓).

### VM2 — Brain Node

| Service | Port | Binding | Status |
|---|---|---|---|
| HAProxy SSH frontend | 2222 | 0.0.0.0 | ✓ Live |
| HAProxy Telnet frontend | 2223 | 0.0.0.0 | ✓ Live |
| Admin SSH (sshd) | 22222 | 0.0.0.0 | ✓ Live |
| Cowrie SSH backup | 4222 | 127.0.0.1 | ✓ Live (standby — HAProxy failover target) |
| Cowrie Telnet backup | 4223 | 127.0.0.1 | ✓ Live (standby — HAProxy failover target) |
| Cowrie Telnet alt backup | 4323 | 127.0.0.1 | ✓ Live (standby) |
| Cowrie pool port | 6415 | 127.0.0.1 | ✓ Live (internal) |
| HTTP honeypot (planned) | 8080 | 127.0.0.1 | → Planned (Tool 41) |

> VM2 Cowrie is the **standby** instance only. Its logs are always 0 bytes unless a failover has occurred. A non-empty VM2 Cowrie log means failover happened. Check HAProxy stats and investigate VM1.

## Network Configuration

| Property | Value |
|---|---|
| VCN CIDR | 10.0.0.0/24 |
| Internal MTU | 9000 (Oracle jumbo frames) |
| Internal bandwidth | Up to 10Gbps |
| VM1 gateway | 10.0.0.1 |
| VM2 gateway | 10.0.0.1 |
| DNS | 127.0.0.53 (systemd-resolved) |

## Data Flow

1. Attackers hit VM2 public IP (`150.230.174.199`) on ports 2222 and 2223
2. HAProxy proxies connections through Oracle VCN to VM1 (`10.0.0.53:2222`, `10.0.0.53:2223`)
3. Cloudflare DNS health-checks VM1; if VM1 unreachable, DNS shifts to VM2 public IP
4. HAProxy TCP health check (30s × 2 failures) shifts traffic to VM2 backup Cowrie automatically
5. VM2 cron runs `rsync_from_vm1.sh` at `:55` of each even hour, pulling logs from `cowrie@10.0.0.53` via private VCN
6. GitHub Actions runs at `:00` — SSHes to VM2 port 22222 only, reads `/opt/thir/logs/cowrie.json`
7. Pipeline processes logs, pushes `data/` to GitHub Pages
8. `thirha.aegispub.com` dashboard fetches from GitHub Pages

> **VM1 is never touched by GitHub Actions.** VM1 public IP is not in any GitHub Secret. All pipeline access is through VM2.

## Key Management

| Key | File | Fingerprint | Used By |
|---|---|---|---|
| Personal access | thir-pipeline-key.ppk / .pem | `SHA256:0Xko5IkOIR5n3oSNER34aXPBbV7bJuERM4FYESrEriw` | PuTTY — admin SSH to both VMs |
| Pipeline key | thir_pipeline_key | `SHA256:csenfxiT4p6AvVKwjTTV35EGpJ8ZkVdeyen2LfsoBA8` | GitHub Actions — ORACLE_VPS_SSH_KEY |
| Internal rsync key | thir_internal (VM2 only) | `SHA256:t5zmp2Dmw0wPBlp8aKM62buYg3vZJ6pFIHxKxmENvg8` | VM2 rsync pulls from VM1 as cowrie user |

## GitHub Secrets Reference

### Required Secrets

| Secret | Value |
|---|---|
| `ORACLE_VPS_SSH_KEY` | Contents of `thir_pipeline_key` private key |
| `ORACLE_VPS_IP` | `150.230.174.199` (VM2 public IP — pipeline target only) |
| `ABUSEIPDB_API_KEY` | AbuseIPDB free key |
| `OTX_API_KEY` | AlienVault OTX free key |

### Optional Secrets

| Secret | Value |
|---|---|
| `VIRUSTOTAL_API_KEY` | VirusTotal free key — enables Tool 31 hash lookups |
| `ALERT_CHANNEL` | `slack` \| `email` \| `both` \| `dry-run` (default: `dry-run`) |
| `SLACK_WEBHOOK_URL` | Required if ALERT_CHANNEL includes `slack` |
| `SMTP_HOST` / `SMTP_USER` / `SMTP_PASS` | Required if ALERT_CHANNEL includes `email` |
| `CLOUDFLARE_R2_KEY` / `CLOUDFLARE_R2_SECRET` | R2 API credentials for log archival |

## Cloudflare R2 Archive

| Bucket | Purpose | Status |
|---|---|---|
| `thir-raw-archive` | AWS corpus (Mar–[retirement] 2026) | One-time write — source for Tool 00 |
| `thirha-raw-archive` | Oracle corpus (Jun 2026 → ongoing) | Daily via `sync_to_r2.sh` cron on VM2 |

## Planned Components (Not Yet Deployed)

| Component | Target | Gate |
|---|---|---|
| HTTP honeypot (Tool 41) | VM1 port 8080 | July 8 2026 (30-day SSH stability window) |
| HTTP log parser (Tool 42) | VM2 pipeline | After Tool 41 |
| cloudflared tunnels | Both VMs | After Tool 41 |

> **cloudflared is not currently deployed.** Any runbook section referring to `systemctl status cloudflared` will fail until tunnels are set up post-Tool 41 gate. HAProxy TCP health checks provide failover coverage in the interim.

---

# RB-02 — VM1 Sensor Node Failure

| Field | Value |
|---|---|
| Document ID | THIR-RB-02 |
| NIST CSF | RC.RP-1 — Recovery plan executed during/after incident |
| Asset | VM1 — `thir-honeypot-vm1` (`129.80.119.236` / `10.0.0.53`) |
| RTO | < 5 min automatic / < 45 min full rebuild |
| RPO | 0 — HAProxy shifts SSH/Telnet traffic automatically |

## Trigger Conditions

| Condition | How You Know |
|---|---|
| VM1 unreachable | Tool 05 reports DOWN in `posture.json` for 2+ consecutive runs; `assets.json` shows VM1 status OFFLINE |
| Cowrie process crashed | No new sessions in `ir_cases.json` but VM1 is up (HAProxy backend shows UP but no new events) |
| VM1 host compromised | Cowrie logs show `/proc`, `/etc/shadow`, `iptables` commands from an attacker session |
| Unexpected outbound traffic | AbuseIPDB reports VM1 public IP (`129.80.119.236`) as a threat actor |
| Oracle instance terminated | Oracle console shows instance state as TERMINATED |

> **WARNING — Evidence first. Do not rebuild before preserving logs. A honeypot compromise is the data, not a failure.**

## Phase 1 — Automatic Failover (0–5 minutes)

HAProxy on VM2 detects VM1 down via TCP health check (30s interval, 2 failures = 60s detection). SSH and Telnet traffic automatically routes to VM2 standby Cowrie on `127.0.0.1:4222` and `127.0.0.1:4223`. No manual action required.

**Verify automatic failover worked (from your machine):**

```bash
ssh -i thir-pipeline-key.pem ubuntu@150.230.174.199 -p 22222

# Check HAProxy stats — columns: pxname, svname, status
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | cut -d',' -f1,2,18

# Look for:
# cowrie_backend,vm1,DOWN          ← VM1 marked down
# cowrie_backend,vm2_backup,UP     ← backup active
# telnet_backend,vm1_telnet,DOWN
# telnet_backend,vm2_telnet_backup,UP
```

## Phase 2 — Evidence Preservation (5–15 minutes)

Only if VM1 is still accessible:

```bash
# From your local machine — copy all logs and auth records
mkdir -p ./evidence/vm1_$(date +%Y%m%d_%H%M%S)
cd ./evidence/vm1_*/

scp -i thir-pipeline-key.pem -P 22222 \
  ubuntu@129.80.119.236:/home/cowrie/cowrie/var/log/cowrie/* .

scp -i thir-pipeline-key.pem -P 22222 \
  ubuntu@129.80.119.236:/var/log/auth.log .

scp -i thir-pipeline-key.pem -P 22222 \
  ubuntu@129.80.119.236:/var/log/syslog .
```

**Take Oracle boot volume backup before any rebuild:**

Oracle Console → Compute → Instances → `thir-honeypot-vm1` → Boot Volume → Create Manual Backup

Label: `thir-vm1-evidence-YYYY-MM-DD`

> Keep the backup for at least 30 days. This is your forensic image.

## Phase 3 — Rebuild VM1 (15–45 minutes)

**Step 1 — Provision new VM1:**

Oracle Console → Compute → Instances → Create Instance

| Field | Value |
|---|---|
| Name | `thir-honeypot-vm1` |
| Shape | VM.Standard.E2.1.Micro (Always Free) |
| Image | Ubuntu 22.04 (Canonical) |
| VCN | Same VCN as VM2 |
| Subnet | Public subnet |
| Public IP | Assign — attempt to recover `129.80.119.236` if possible |
| Private IP | Advanced networking → request `10.0.0.53` |
| SSH keys | Paste both public keys (personal + pipeline), one per line |

Note the new public IP. If different from `129.80.119.236`, update Cloudflare DNS A record.

**Step 2 — Install dependencies:**

```bash
ssh -i thir-pipeline-key.pem ubuntu@NEW_VM1_IP -p 22222

sudo apt update && sudo apt install -y \
  python3-virtualenv git libssl-dev libffi-dev \
  build-essential libpython3-dev iptables-persistent
```

**Step 3 — Create Cowrie user:**

```bash
sudo adduser --disabled-password --gecos "" cowrie
```

**Step 4 — Install Cowrie:**

```bash
sudo su - cowrie
git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg
```

**Step 5 — Configure Cowrie (`etc/cowrie.cfg`):**

```ini
[honeypot]
hostname = nas-storage-01

[ssh]
listen_endpoints = tcp:2222:interface=0.0.0.0

[telnet]
enabled = true
listen_endpoints = tcp:2223:interface=0.0.0.0 tcp:2323:interface=0.0.0.0

[output_jsonlog]
enabled = true
logfile = ${honeypot:log_path}/cowrie.json
```

**Step 6 — Add VM2 internal key to Cowrie authorized_keys:**

```bash
exit  # back to ubuntu

sudo mkdir -p /home/cowrie/.ssh
# Paste the VM2 thir_internal public key:
sudo tee /home/cowrie/.ssh/authorized_keys << 'EOF'
PASTE_VM2_THIR_INTERNAL_PUBLIC_KEY_HERE
EOF
sudo chown -R cowrie:cowrie /home/cowrie/.ssh
sudo chmod 700 /home/cowrie/.ssh
sudo chmod 600 /home/cowrie/.ssh/authorized_keys
```

Get the VM2 internal public key from VM2:

```bash
# On VM2
cat /home/ubuntu/.ssh/thir_internal.pub
```

**Step 7 — Configure Cowrie as systemd service:**

```bash
sudo nano /etc/systemd/system/cowrie.service
```

```ini
[Unit]
Description=Cowrie SSH/Telnet Honeypot
After=network.target

[Service]
Type=simple
User=cowrie
WorkingDirectory=/home/cowrie/cowrie
ExecStart=/home/cowrie/cowrie/cowrie-env/bin/twistd \
  --nodaemon --pidfile=/home/cowrie/cowrie/var/run/cowrie.pid \
  -l /home/cowrie/cowrie/var/log/cowrie/cowrie.log cowrie
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable cowrie
sudo systemctl start cowrie
```

**Step 8 — Restore iptables NAT rules:**

> **This step is mandatory.** Without it, port 22 connects to the real admin sshd, not Cowrie — defeating the honeypot design and creating a direct exposure.

```bash
# Redirect port 22 → Cowrie port 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222

# Redirect port 23 → Cowrie port 2223
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223

# Redirect port 80 → HTTP honeypot port 8080 (0 packets until Tool 41 deployed)
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080

# Save rules — survive reboot
sudo netfilter-persistent save

# Verify
sudo iptables -t nat -L PREROUTING -n --line-numbers
# Expected: 3 REDIRECT rules — 22→2222, 23→2223, 80→8080
```

**Step 9 — Configure Admin SSH on port 22222:**

```bash
sudo nano /etc/ssh/sshd_config
# Confirm or add: Port 22222
# Confirm: PasswordAuthentication no
# Confirm: PubkeyAuthentication yes
sudo systemctl restart ssh
```

## Phase 4 — Restore VCN Internal Access (5 minutes)

VM2 rsync needs passwordless SSH access to VM1 as the `cowrie` user:

```bash
# From VM2
ssh-copy-id -i /home/ubuntu/.ssh/thir_internal.pub cowrie@10.0.0.53

# Test internal rsync
rsync -avzn cowrie@10.0.0.53:/home/cowrie/cowrie/var/log/cowrie/cowrie.json /tmp/test_sync.json
# Expected: dry-run shows file stats, 0 errors
```

## Phase 5 — Restore HAProxy Backend (2 minutes)

```bash
# On VM2
sudo nano /etc/haproxy/haproxy.cfg

# Confirm backend entries:
#   server vm1        10.0.0.53:2222  check inter 30s fall 2 rise 2
#   server vm1_telnet 10.0.0.53:2223  check inter 30s fall 2 rise 2

sudo systemctl reload haproxy

# Verify vm1 backends show UP
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | cut -d',' -f1,2,18
```

## Phase 6 — Verify Recovery

| | Check |
|---|---|
| ☐ | Tool 05 reports both VMs UP in `posture.json` |
| ☐ | `assets.json` shows VM1 (`10.0.0.53`) status ONLINE |
| ☐ | Cowrie log file growing on VM1 — `tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.json` shows new sessions |
| ☐ | HAProxy `cowrie_backend,vm1` shows UP in stats |
| ☐ | HAProxy `telnet_backend,vm1_telnet` shows UP in stats |
| ☐ | Rsync from VM1 to VM2 completes without error |
| ☐ | GitHub Actions pipeline completes successfully |
| ☐ | `thirha.aegispub.com` dashboard shows live data — no `[cached]` labels |
| ☐ | iptables NAT rules confirmed: `iptables -t nat -L PREROUTING -n` shows 3 REDIRECT rules |
| ☐ | Compromise documented as IR case in THIR dashboard if applicable |

---

# RB-03 — VM2 Brain Node Failure

| Field | Value |
|---|---|
| Document ID | THIR-RB-03 |
| NIST CSF | RC.RP-1 — Recovery plan executed during/after incident |
| Asset | VM2 — `thir-pipeline-vm2` (`150.230.174.199` / `10.0.0.73`) |
| RTO | < 30 min manual recovery |
| RPO | < 2 hours — last successful rsync to VM2 |

VM2 failure is lower urgency than VM1. Cowrie on VM1 keeps capturing attacks independently — no data is lost. The only impact is GitHub Actions cannot push updates to the dashboard until VM2 is restored.

## Trigger Conditions

| Condition | How You Know |
|---|---|
| GitHub Actions pipeline fails | SSH step times out — cannot reach VM2 on port 22222 |
| Dashboard stale | `thirha.aegispub.com` shows `[cached HH:MM UTC]` labels > 6h |
| HAProxy down | Cloudflare health check fails — DNS may shift to VM1 direct |
| VM2 terminated | Oracle console shows instance state as TERMINATED |

## Phase 1 — Cowrie Continuity Check (2 minutes)

Confirm VM1 is still capturing. Data queues on VM1 until VM2 recovers — nothing is lost.

```bash
ssh -i thir-pipeline-key.pem ubuntu@129.80.119.236 -p 22222

tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.json
# New lines = VM1 healthy. Ctrl+C and proceed to restore VM2.
```

## Phase 2 — Restore VM2 (20 minutes)

Oracle Console → Compute → Instances → Create Instance

| Field | Value |
|---|---|
| Name | `thir-pipeline-vm2` |
| Shape | VM.Standard.E2.1.Micro (Always Free) |
| Image | Ubuntu 22.04 (Canonical) |
| VCN | Same VCN as VM1 |
| Subnet | Public subnet |
| Public IP | Assign — note the IP |
| Private IP | Advanced networking → request `10.0.0.73` |
| SSH keys | Paste both public keys (personal + pipeline), one per line |

```bash
ssh -i thir-pipeline-key.pem ubuntu@NEW_VM2_IP -p 22222

sudo apt update && sudo apt install -y haproxy python3-pip rsync socat
```

> `socat` is required for HAProxy stats socket queries. Do not omit it.

## Phase 3 — Restore HAProxy (5 minutes)

```bash
sudo tee /etc/haproxy/haproxy.cfg << 'EOF'
global
    log /dev/log local0
    log /dev/log local1 notice
    stats socket /var/run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    maxconn 50

defaults
    log     global
    mode    tcp
    option  tcplog
    option  dontlognull
    timeout connect 5s
    timeout client  30s
    timeout server  30s

# SSH honeypot — primary VM1, failover to VM2 standby Cowrie
frontend ssh_front
    bind *:2222
    default_backend cowrie_backend

backend cowrie_backend
    option  tcp-check
    server  vm1        10.0.0.53:2222  check inter 30s fall 2 rise 2
    server  vm2_backup 127.0.0.1:4222  check inter 30s backup

# Telnet honeypot — primary VM1, failover to VM2 standby Cowrie
frontend telnet_front
    bind *:2223
    default_backend telnet_backend

backend telnet_backend
    option  tcp-check
    server  vm1_telnet        10.0.0.53:2223  check inter 30s fall 2 rise 2
    server  vm2_telnet_backup 127.0.0.1:4223  check inter 30s backup

# HTTP honeypot — commented out until Tool 41 is deployed
#frontend http_front
#    bind *:80
#    default_backend http_honeypot
#
#backend http_honeypot
#    option  tcp-check
#    server  vm1_http        10.0.0.53:8080  check inter 30s fall 2 rise 2
#    server  vm2_http_backup 127.0.0.1:8080  check inter 30s backup
EOF

sudo haproxy -c -f /etc/haproxy/haproxy.cfg
# Expected: Configuration file is valid

sudo systemctl enable haproxy
sudo systemctl start haproxy
sudo systemctl status haproxy
```

## Phase 4 — Restore VM2 Cowrie Standby (10 minutes)

HAProxy needs a local backup target. Without VM2 Cowrie running on `127.0.0.1:4222` and `127.0.0.1:4223`, the backup servers are DOWN and failover has no target.

```bash
sudo adduser --disabled-password --gecos "" cowrie

sudo su - cowrie
git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg
```

Configure VM2 Cowrie for localhost-only on offset ports (`etc/cowrie.cfg`):

```ini
[honeypot]
hostname = nas-storage-01

[ssh]
listen_endpoints = tcp:4222:interface=127.0.0.1

[telnet]
enabled = true
listen_endpoints = tcp:4223:interface=127.0.0.1 tcp:4323:interface=127.0.0.1

[output_jsonlog]
enabled = true
logfile = ${honeypot:log_path}/cowrie.json
```

```bash
bin/cowrie start

# Verify localhost-only binding
ss -tlnp | grep -E '4222|4223|4323'
# Expected: 127.0.0.1:4222, 127.0.0.1:4223, 127.0.0.1:4323 (twistd)
```

Configure as systemd service (same unit file as VM1 but runs as cowrie):

```bash
exit  # back to ubuntu

sudo nano /etc/systemd/system/cowrie.service
# Same unit content as RB-02 Phase 3 Step 7
sudo systemctl daemon-reload
sudo systemctl enable cowrie
sudo systemctl start cowrie
```

## Phase 5 — Restore Internal SSH Key for Rsync (3 minutes)

```bash
ssh-keygen -t ed25519 -C 'thir-internal-vm2' \
  -f /home/ubuntu/.ssh/thir_internal -N ''

# Display new public key
cat /home/ubuntu/.ssh/thir_internal.pub
```

Add this new public key to VM1 `cowrie` authorized_keys:

```bash
# On VM1
sudo nano /home/cowrie/.ssh/authorized_keys
# Replace old VM2 internal key with new one
# File should contain exactly 1 key after this change
```

Test rsync from VM2:

```bash
# On VM2
rsync -avz cowrie@10.0.0.53:/home/cowrie/cowrie/var/log/cowrie/cowrie.json /tmp/test.json
# Expected: transfer completes, no permission errors
```

## Phase 6 — Restore Pipeline Directory (2 minutes)

```bash
sudo mkdir -p /opt/thir/logs/downloads
sudo chown -R ubuntu:ubuntu /opt/thir/logs
sudo chown cowrie:cowrie /opt/thir/logs/downloads
sudo chmod 775 /opt/thir/logs
```

## Phase 7 — Update GitHub Secret if IP Changed

If VM2 public IP is different from `150.230.174.199`:

GitHub → Repository Settings → Secrets → `ORACLE_VPS_IP` → update to new VM2 public IP

Trigger pipeline manually — Actions → THIR Live Pipeline → Run workflow

## Phase 8 — Restore VM2 Cron Jobs

```bash
crontab -e
```

Add:

```cron
# rsync logs from VM1 — at :55 before GitHub Actions runs at :00
55 */2 * * * /home/ubuntu/rsync_from_vm1.sh >> /home/ubuntu/var/log/thir_rsync.log 2>&1

# Daily R2 archive sync — at 01:00 UTC after Cowrie log rotation at midnight
0 1 * * * /home/ubuntu/sync_to_r2.sh >> /home/ubuntu/var/log/r2_upload.log 2>&1
```

> `sync_to_r2.sh` must be at `/home/ubuntu/sync_to_r2.sh`. Do not use `/home/cowrie/sync_to_r2.sh` — that path does not exist and the cron will silently fail.

## Verify Recovery

| | Check |
|---|---|
| ☐ | HAProxy running — `systemctl status haproxy` shows active |
| ☐ | HAProxy config valid — `sudo haproxy -c -f /etc/haproxy/haproxy.cfg` |
| ☐ | VM2 Cowrie backup ports bound to localhost — `ss -tlnp \| grep -E '4222\|4223'` |
| ☐ | HAProxy backends show both VM1 and VM2 UP |
| ☐ | Rsync from VM1 completes without permission errors |
| ☐ | GitHub Actions pipeline completes successfully |
| ☐ | `thirha.aegispub.com` removes `[cached]` labels — fresh data showing |
| ☐ | Cron jobs active — `crontab -l` shows both entries with correct paths |

---

# RB-04 — Failover Procedure

| Field | Value |
|---|---|
| Document ID | THIR-RB-04 |
| NIST CSF | RS.RP-1 — Response plan executed during incident |
| Covers | Automatic HAProxy failover + Manual Cloudflare DNS failover |

## Automatic Failover — HAProxy (SSH and Telnet Traffic)

HAProxy on VM2 monitors VM1 via TCP health check every 30 seconds. Two consecutive failures (60 seconds) triggers failover. **No manual action required.**

THIR has two independent failover backends:

| Backend | Primary | Backup | Note |
|---|---|---|---|
| `cowrie_backend` | `vm1 10.0.0.53:2222` | `vm2_backup 127.0.0.1:4222` | SSH traffic |
| `telnet_backend` | `vm1_telnet 10.0.0.53:2223` | `vm2_telnet_backup 127.0.0.1:4223` | Telnet traffic |

These are independent states. SSH can fail over while telnet stays healthy, or vice versa. Tool 39 (failover auditor) monitors and reports both backends independently in `data/failover_events.json`.

**Check current backend status:**

```bash
# On VM2
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | cut -d',' -f1,2,18,19
# Columns: pxname, svname, status, act

# Check both backends explicitly
echo 'show servers state' | sudo socat stdio /var/run/haproxy/admin.sock
```

**Failover state reference:**

| VM1 State | VM2 State | Traffic Routing | Action Required |
|---|---|---|---|
| UP | UP | VM1 primary — normal operations | None |
| DOWN | UP | HAProxy → VM2 backup Cowrie | Investigate VM1 — RB-02 |
| UP | DOWN | No pipeline updates — VM1 still capturing | Restore VM2 — RB-03 |
| DOWN | DOWN | Full outage — no capture | Full rebuild — RB-06 |

**HAProxy failover events:**

| Event | What Happens |
|---|---|
| VM1 health check fails ×2 | HAProxy marks `vm1` DOWN; shifts SSH to `vm2_backup`, Telnet to `vm2_telnet_backup` |
| VM1 recovers | HAProxy detects UP after 2 successful checks; shifts traffic back automatically |
| VM2 HAProxy fails | Cloudflare DNS failover activates — attacker traffic routes to VM1 public IP directly |

## Manual Failover — Cloudflare DNS

Use when VM1 public IP is unreachable **and** HAProxy is also down (VM2 lost). Cloudflare automatic health checks handle this, but manual override is faster if you already know VM1 is down.

Cloudflare Dashboard → aegispub.com → DNS

- Find the A record pointing to VM1 public IP (`129.80.119.236`)
- Change IP to VM2 public IP (`150.230.174.199`)
- Set TTL to 60 seconds for fast propagation
- Verify propagation:

```bash
dig thirha.aegispub.com @1.1.1.1
dig thirha.aegispub.com @8.8.8.8
```

> Cloudflare free tier health checks have ~60–120 second detection lag. Manual DNS change is faster if you already know VM1 is down.

## Cloudflare Automatic Health Check Setup

One-time configuration — Cloudflare monitors VM1 continuously after this.

> **Note:** The HTTP `/health` endpoint requires Tool 41 (HTTP honeypot) to be deployed. Until then, configure health checks as TCP connect on port 2222 to confirm the HAProxy frontend is answering.

Cloudflare Dashboard → Traffic → Health Checks → Create Health Check

**VM1 health check:**

| Field | Value |
|---|---|
| Name | `thir-vm1-health` |
| URL | `http://129.80.119.236/health` (post-Tool 41) |
| Type | HTTP (TCP connect until Tool 41 deployed) |
| Interval | 60 seconds |
| Retries | 2 |
| Notification | Alert on status change |

**VM2 health check:**

| Field | Value |
|---|---|
| Name | `thir-vm2-health` |
| URL | `http://150.230.174.199/health` |
| Interval | 60 seconds |
| Retries | 2 |

**DNS Failover:** Primary = `129.80.119.236` (VM1) / Fallback = `150.230.174.199` (VM2)

---

# RB-05 — HAProxy & Cloudflare Recovery

| Field | Value |
|---|---|
| Document ID | THIR-RB-05 |
| NIST CSF | PR.IP-1 — Baseline configuration maintained |
| Assets | HAProxy on VM2, Cloudflare DNS |

## HAProxy Recovery

### Check Status

```bash
sudo systemctl status haproxy
sudo journalctl -u haproxy -n 50
```

### Restart HAProxy

```bash
sudo systemctl restart haproxy

# Verify all backends
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | cut -d',' -f1,2,18

# Check connection rates
echo 'show info' | sudo socat stdio /var/run/haproxy/admin.sock | grep -E 'ConnRate|MaxConnRate|Uptime'
```

### Full HAProxy Config Restore (Authoritative)

This is the confirmed live configuration. Use this as the authoritative restore source.

```bash
sudo tee /etc/haproxy/haproxy.cfg << 'EOF'
global
    log /dev/log local0
    log /dev/log local1 notice
    stats socket /var/run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    maxconn 50

defaults
    log     global
    mode    tcp
    option  tcplog
    option  dontlognull
    timeout connect 5s
    timeout client  30s
    timeout server  30s

# SSH honeypot — primary VM1, failover to VM2 standby Cowrie
frontend ssh_front
    bind *:2222
    default_backend cowrie_backend

backend cowrie_backend
    option  tcp-check
    server  vm1        10.0.0.53:2222  check inter 30s fall 2 rise 2
    server  vm2_backup 127.0.0.1:4222  check inter 30s backup

# Telnet honeypot — primary VM1, failover to VM2 standby Cowrie
frontend telnet_front
    bind *:2223
    default_backend telnet_backend

backend telnet_backend
    option  tcp-check
    server  vm1_telnet        10.0.0.53:2223  check inter 30s fall 2 rise 2
    server  vm2_telnet_backup 127.0.0.1:4223  check inter 30s backup

# HTTP honeypot — commented out until Tool 41 is deployed
#frontend http_front
#    bind *:80
#    default_backend http_honeypot
#
#backend http_honeypot
#    option  tcp-check
#    server  vm1_http        10.0.0.53:8080  check inter 30s fall 2 rise 2
#    server  vm2_http_backup 127.0.0.1:8080  check inter 30s backup
EOF

sudo haproxy -c -f /etc/haproxy/haproxy.cfg
# Expected: Configuration file is valid

sudo systemctl reload haproxy
```

**Reference hash for the live config:**
`6160bc94ccfea91349a34685ab18735eac9b7c0ef1e6dfc55b4b43a32da070e7`

Any deviation from this hash after a restore means the config was modified.

## Cloudflare DNS Reference

| Record | Type | Current Value | Notes |
|---|---|---|---|
| `thirha.aegispub.com` | CNAME | `[github-user].github.io` | Dashboard — GitHub Pages |
| Honeypot A record | A | `129.80.119.236` (VM1) | Primary — attacker-facing |
| Failover record | A | `150.230.174.199` (VM2) | Activated by health check or manually |

**DNS failover TTL guidance:**

| State | TTL Setting |
|---|---|
| Normal operations | 300 seconds (5 minutes) |
| Before any failover or IP change | Reduce to 60 seconds — wait one full TTL cycle first |
| After new IP confirmed stable (30+ min) | Restore to 300 seconds |

## Cloudflare Tunnel Recovery

> **cloudflared is not currently deployed on either VM.** This section describes the planned procedure for when tunnels are set up (post-Tool 41, gate July 8 2026).

```bash
# These commands will fail until cloudflared is installed:
# sudo systemctl status cloudflared     # Unit not found
# cloudflared tunnel list               # Command not found

# When deployed, restore procedure will be:
# sudo systemctl restart cloudflared
# cloudflared tunnel list               # Confirm tunnel connected
# cloudflared tunnel info thir-vm1      # or thir-vm2
```

---

# RB-06 — Full Stack Rebuild

| Field | Value |
|---|---|
| Document ID | THIR-RB-06 |
| NIST CSF | RC.RP-1 — Recovery plan executed |
| Scenario | Both VM1 and VM2 lost simultaneously |
| RTO Target | < 90 minutes |
| RPO | Last git push to GitHub Pages — all processed data safe |

> **GitHub Pages data is safe regardless of VM loss.** All processed data in `data/` and `reports/` is already committed to GitHub. Only raw Cowrie logs on VM1 since the last rsync (up to 2 hours) are at risk.

## Pre-Rebuild Checklist

| | Check |
|---|---|
| ☐ | Confirm `thirha.aegispub.com` is serving — confirms GitHub Pages unaffected |
| ☐ | Confirm GitHub repo `data/` has recent commits — this is the recovery baseline |
| ☐ | Locate SSH key files: `thir-pipeline-key.pem` (personal) + `thir_pipeline_key` (pipeline) |
| ☐ | Have both key fingerprints noted (see RB-01 Key Management) |
| ☐ | Have GitHub repo URL, AbuseIPDB, OTX API keys ready |
| ☐ | Note Oracle compartment and VCN details from last working setup |

## Phase 1 — Provision Both VMs (20 minutes)

> **Always provision VM2 (brain) before VM1 (sensor).** HAProxy must be running before VM1 starts receiving traffic.

### Provision VM2 — Brain Node

Oracle Console → Compute → Instances → Create Instance

| Field | Value |
|---|---|
| Name | `thir-pipeline-vm2` |
| Shape | VM.Standard.E2.1.Micro (Always Free) |
| Image | Ubuntu 22.04 (Canonical) |
| VCN | Create new VCN or use existing |
| Subnet | Public subnet |
| Public IP | Assign |
| Private IP | Advanced networking → request `10.0.0.73` |
| SSH keys | Paste both public keys (personal + pipeline), one per line |

Note VM2 public IP. If different from `150.230.174.199`, GitHub Secret and Cloudflare DNS will need updating.

### Provision VM1 — Sensor Node

| Field | Value |
|---|---|
| Name | `thir-honeypot-vm1` |
| Shape | VM.Standard.E2.1.Micro (Always Free) |
| Image | Ubuntu 22.04 (Canonical) |
| VCN | Same VCN as VM2 |
| Subnet | Public subnet |
| Public IP | Assign |
| Private IP | Advanced networking → request `10.0.0.53` |
| SSH keys | Same two public keys |

### Oracle VCN Security List — Required Ingress Rules

Apply at the Subnet Security List level (Oracle Console → Networking → VCN → Subnets → Security List). **This is separate from instance-level iptables — both layers must allow traffic.**

| Source CIDR | Protocol | Port(s) | Purpose |
|---|---|---|---|
| 0.0.0.0/0 | TCP | 2222 | Cowrie SSH honeypot |
| 0.0.0.0/0 | TCP | 2223 | Cowrie Telnet honeypot |
| 0.0.0.0/0 | TCP | 80, 443 | HTTP honeypot — pending Tool 41 |
| Your IP only | TCP | 22222 | Admin SSH — restrict to your IP, not 0.0.0.0/0 |
| 10.0.0.0/24 | All | All | Internal VCN — rsync, HAProxy backends |

## Phase 2 — Install VM2 Stack (15 minutes)

```bash
ssh -i thir-pipeline-key.pem ubuntu@VM2_IP -p 22222

sudo apt update && sudo apt install -y haproxy python3-pip rsync socat

# Configure HAProxy — use RB-05 full config above
# (both IP values confirmed: 10.0.0.53 for VM1, 10.0.0.73 for VM2 private)

sudo systemctl enable haproxy && sudo systemctl start haproxy

# Generate internal rsync key
ssh-keygen -t ed25519 -C 'thir-internal-vm2' \
  -f /home/ubuntu/.ssh/thir_internal -N ''

# Copy this — needed for VM1 setup
cat /home/ubuntu/.ssh/thir_internal.pub
```

## Phase 3 — Install VM1 Stack (25 minutes)

```bash
ssh -i thir-pipeline-key.pem ubuntu@VM1_IP -p 22222

sudo apt update && sudo apt install -y \
  python3-virtualenv git libssl-dev libffi-dev \
  build-essential libpython3-dev iptables-persistent

sudo adduser --disabled-password --gecos "" cowrie

# Add VM2 internal public key to cowrie authorized_keys
sudo mkdir -p /home/cowrie/.ssh
echo 'PASTE_VM2_THIR_INTERNAL_PUBLIC_KEY_HERE' | \
  sudo tee /home/cowrie/.ssh/authorized_keys
sudo chown -R cowrie:cowrie /home/cowrie/.ssh
sudo chmod 700 /home/cowrie/.ssh
sudo chmod 600 /home/cowrie/.ssh/authorized_keys

# Install Cowrie
sudo su - cowrie
git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg

# Configure cowrie.cfg — see RB-02 Phase 3 Step 5 for content
nano etc/cowrie.cfg

# Start Cowrie
bin/cowrie start
```

Exit back to ubuntu user and restore iptables:

```bash
exit  # back to ubuntu

# MANDATORY — restore iptables NAT rules
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080

# Save — survive reboot
sudo netfilter-persistent save

# Verify
sudo iptables -t nat -L PREROUTING -n --line-numbers
```

Configure Admin SSH on port 22222:

```bash
sudo nano /etc/ssh/sshd_config
# Port 22222
# PasswordAuthentication no
# PubkeyAuthentication yes
sudo systemctl restart ssh
```

Install VM2 Cowrie standby (follow RB-03 Phase 4 procedure).

## Phase 4 — Restore Pipeline (10 minutes)

```bash
# On VM2 — restore pipeline directory
sudo mkdir -p /opt/thir/logs/downloads
sudo chown -R ubuntu:ubuntu /opt/thir/logs
sudo chown cowrie:cowrie /opt/thir/logs/downloads

# Restore rsync script (copy from repo or restore from backup)
# Verify the cron path is correct
crontab -e
# Add both cron entries from RB-03 Phase 8
# CRITICAL: sync_to_r2.sh must be /home/ubuntu/sync_to_r2.sh — not /home/cowrie/
```

Update GitHub Secret if VM2 public IP changed:

GitHub → Repository Settings → Secrets → `ORACLE_VPS_IP` → new VM2 public IP

Update Cloudflare DNS A record to VM1 public IP.

Trigger pipeline manually:

Actions → THIR Live Pipeline → Run workflow

## Phase 5 — Verify Full Stack

| | Check |
|---|---|
| ☐ | VM1 Cowrie running — `bin/cowrie status` shows running |
| ☐ | VM1 Cowrie ports bound — `ss -tlnp \| grep -E '2222\|2223\|2323'` shows `0.0.0.0` binding |
| ☐ | VM1 iptables NAT rules present — `sudo iptables -t nat -L PREROUTING -n` shows 3 REDIRECT rules |
| ☐ | HAProxy on VM2 — `systemctl status haproxy` shows active |
| ☐ | HAProxy shows all 4 backends UP — `vm1`, `vm2_backup`, `vm1_telnet`, `vm2_telnet_backup` |
| ☐ | VM2 Cowrie standby bound to localhost — `ss -tlnp \| grep -E '4222\|4223'` |
| ☐ | Rsync from VM1 to VM2 works — `rsync -avzn cowrie@10.0.0.53:.../cowrie.json /tmp/` |
| ☐ | GitHub Actions pipeline completes without errors |
| ☐ | `thirha.aegispub.com` shows live data — no `[cached]` labels |
| ☐ | Cloudflare DNS resolves to VM1 public IP — `dig thirha.aegispub.com @1.1.1.1` |
| ☐ | Both VMs accessible via PuTTY using `thir-pipeline-key.ppk` on port 22222 |
| ☐ | Post-rebuild incident documented in THIR IR archive |

---

# NIST CSF Control Alignment

| Control | Function | Coverage | Runbook |
|---|---|---|---|
| ID.AM-1 | IDENTIFY | Asset inventory — both VMs, keys, services documented. Tool 05 writes `assets.json` per run covering VM1 and VM2. | RB-01 |
| PR.IP-1 | PROTECT | Baseline config maintained: `haproxy.cfg`, `cowrie.cfg`, VCN rules in `config/`. Full restore in RB-05. | RB-05 |
| PR.IP-4 | PROTECT | Oracle Boot Volume Backup before any rebuild — evidence preserved before modification. | RB-02, RB-06 |
| RS.RP-1 | RESPOND | Failover procedure documented and executable — both HAProxy backends and Cloudflare DNS covered. | RB-04 |
| RS.AN-1 | RESPOND | Evidence preservation is mandatory Phase 2 of RB-02 before any rebuild action. | RB-02 |
| RC.RP-1 | RECOVER | Recovery plan exists, version-controlled, covers all four failure modes (VM1, VM2, HAProxy, full stack). | RB-02, RB-03, RB-06 |
| RC.CO-3 | RECOVER | Dashboard recovery comms — `[cached HH:MM UTC]` labels show staleness visibly to any visitor. | RB-01 (architecture) |

---

## Version History

| Version | Date | Changes |
|---|---|---|
| v2.0 | May 2026 | Initial HA runbook set — planned private IPs `10.0.0.1`/`10.0.0.2` |
| v2.1 | June 2026 | Corrected private IPs to `10.0.0.53`/`10.0.0.73` (Oracle-assigned). Fixed HAProxy backup port `2223→4222`. Added telnet backend throughout. Added iptables restore to RB-02 and RB-06 (critical missing step). Added VM2 Cowrie standby install to RB-03. Marked cloudflared as not yet deployed. Corrected dashboard URL to `thirha.aegispub.com`. Added socat to RB-03 install list. Added correct cron paths. Corrected R2 bucket name to `thirha-raw-archive`. Added RTO phase breakdown for RB-03. |

---

*// The feed runs whether or not you're reading.*
*thirha.aegispub.com ●LIVE*

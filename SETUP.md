# THIR HA — Setup Guide

*Oracle Cloud Always Free — Two-Node HA Deployment*

This guide covers provisioning and configuring the full Oracle HA architecture from scratch. It uses confirmed values from the live deployment — IPs, ports, paths, and key fingerprints are real, not placeholders.

For recovery procedures after the system is running, see `docs/THIR_HA_Runbooks_v2.docx`.

---

## Prerequisites

- Oracle Cloud account (Always Free tier — no credit card charges if you stay within free limits)
- Cloudflare account (free tier) — for DNS, DDoS protection, health checks, R2 storage
- GitHub account — for the repo, Actions pipeline, and Pages dashboard
- SSH key pair already generated — see Section 1.3

---

## Section 1 — Before Touching Oracle

### 1.1 Set Up Cloudflare R2 — Two Buckets

THIR uses two separate R2 buckets. Create both before provisioning VMs.

**Bucket 1 — AWS corpus archive (one-time, if migrating)**

1. Cloudflare Dashboard → R2 → Create Bucket → Name: `thir-raw-archive`
2. R2 → Manage R2 API Tokens → Create Token → Object Read & Write → `thir-raw-archive`
3. Note: Account ID, Access Key ID, Secret Access Key

This bucket receives the full AWS log corpus (March–[retirement] 2026). It is written once and never updated after AWS EC2 is terminated. It is the source data for Tool 00 historical processor.

**Bucket 2 — Oracle corpus archive (ongoing)**

1. Cloudflare Dashboard → R2 → Create Bucket → Name: `thirha-raw-archive`
2. R2 → Manage R2 API Tokens → Create Token → Object Read & Write → `thirha-raw-archive`
3. Note: Account ID, Access Key ID, Secret Access Key

This bucket receives daily compressed logs from Oracle VM1 via the `sync_to_r2.sh` cron on VM2. It grows continuously for the life of the Oracle deployment.

### 1.2 Compress and Upload AWS Logs to `thir-raw-archive`

```bash
# On AWS EC2 — compress all rotated logs
cd /home/cowrie/cowrie/var/log/cowrie/
for f in cowrie.json.2026-*; do gzip -k "$f" && echo "Compressed: $f"; done
for f in cowrie.log.2026-*;  do gzip -k "$f" && echo "Compressed: $f"; done

# Install rclone
curl https://rclone.org/install.sh | sudo bash

# Configure rclone for R2 (using thir-raw-archive credentials from Section 1.1)
rclone config
# n → new remote → name: r2-aws → type: s3 → provider: Cloudflare
# Access Key ID and Secret from thir-raw-archive token
# Endpoint: https://[ACCOUNT_ID].r2.cloudflarestorage.com

# Upload all compressed logs by month — destination is thir-raw-archive
for f in cowrie.json.*.gz; do
  month=$(echo $f | grep -o '[0-9]\{4\}-[0-9]\{2\}')
  rclone copy $f r2-aws:thir-raw-archive/cowrie-json/$month/
done
for f in cowrie.log.*.gz; do
  month=$(echo $f | grep -o '[0-9]\{4\}-[0-9]\{2\}')
  rclone copy $f r2-aws:thir-raw-archive/cowrie-log/$month/
done

# Verify
rclone ls r2-aws:thir-raw-archive | wc -l
```

### 1.3 SSH Keys Required

Two key pairs are needed. Both public keys go into every Oracle VM during provisioning.

| Key | Purpose | Format needed for Oracle |
|---|---|---|
| Personal access key | PuTTY admin SSH to both VMs | OpenSSH public key |
| Pipeline key | GitHub Actions `ORACLE_VPS_SSH_KEY` secret | OpenSSH public key |

Oracle's VM creation UI accepts one public key per paste field — paste both keys one per line in the SSH key field, or add the second after provisioning via `~/.ssh/authorized_keys`.

Generate the internal rsync key after VM2 is provisioned (Section 4.2).

---

## Section 2 — Oracle VM Provisioning

> **Always provision VM2 (brain) before VM1 (sensor).** The brain node hosts HAProxy and the pipeline. Building it first means you can configure VM1 as a backend immediately.

### 2.1 Oracle Console Navigation

Oracle Cloud Console → Compute → Instances → Create Instance

### 2.2 Provision VM2 — Brain Node

| Field | Value |
|---|---|
| Name | `thir-pipeline-vm2` |
| Shape | VM.Standard.E2.1.Micro (Always Free) |
| Image | Ubuntu 22.04 (Canonical) |
| VCN | Create new VCN or use existing |
| Subnet | Public subnet |
| Public IP | Assign — note the IP assigned |
| Private IP | Advanced networking options → request `10.0.0.73` |
| SSH keys | Paste both public keys (personal + pipeline), one per line |

After launch: note VM2 public IP. This becomes `ORACLE_VPS_IP` in GitHub Secrets.

### 2.3 Provision VM1 — Sensor Node

| Field | Value |
|---|---|
| Name | `thir-honeypot-vm1` |
| Shape | VM.Standard.E2.1.Micro (Always Free) |
| Image | Ubuntu 22.04 (Canonical) |
| VCN | Same VCN as VM2 |
| Subnet | Same public subnet |
| Public IP | Assign — note the IP assigned |
| Private IP | Advanced networking options → request `10.0.0.53` |
| SSH keys | Same both public keys |

### 2.4 VCN Subnet Security List — Critical Step

> **Oracle requires security rules at the Subnet Security List level in addition to instance-level firewall rules. iptables/ufw alone is not sufficient. This is the most common Oracle setup mistake.**

Oracle Console → Networking → Virtual Cloud Networks → [your VCN] → Subnets → [your subnet] → Security List → Add Ingress Rules:

| Source CIDR | Protocol | Port(s) | Purpose |
|---|---|---|---|
| 0.0.0.0/0 | TCP | 2222 | Cowrie SSH honeypot — attacker-facing |
| 0.0.0.0/0 | TCP | 2223 | Cowrie Telnet honeypot — attacker-facing |
| 0.0.0.0/0 | TCP | 80, 443 | HTTP honeypot — pending Tool 41 |
| Your IP only | TCP | 22222 | Admin SSH — PuTTY access |
| 10.0.0.0/24 | All | All | Internal VCN — rsync, HAProxy backends |

### 2.5 Verify Both VMs Reachable

```bash
# Test personal key access to both VMs (from your machine)
# PuTTY: connect to VM1_PUBLIC_IP port 22222 using thir-pipeline-key.ppk
# PuTTY: connect to VM2_PUBLIC_IP port 22222 using thir-pipeline-key.ppk
# Expected: ubuntu@thir-honeypot-vm1 and ubuntu@thir-pipeline-vm2
```

---

## Section 3 — VM1 Setup (Sensor Node)

```bash
ssh -i thir-pipeline-key.pem -p 22222 ubuntu@VM1_PUBLIC_IP
```

### 3.1 Install Dependencies

```bash
sudo apt update && sudo apt install -y \
  python3-virtualenv git libssl-dev libffi-dev \
  build-essential libpython3-dev iptables-persistent
```

### 3.2 Create Cowrie User

```bash
sudo adduser --disabled-password --gecos "" cowrie
```

### 3.3 Install Cowrie

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

### 3.4 Configure Cowrie

```bash
nano etc/cowrie.cfg
```

Key settings to confirm or set:

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

### 3.5 Start Cowrie

```bash
bin/cowrie start
bin/cowrie status
# Expected: twistd running, PID file present
```

### 3.6 Configure iptables Port Redirects

```bash
# Run as ubuntu user (sudo)
exit  # back to ubuntu if still as cowrie

# Redirect port 22 → Cowrie port 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222

# Redirect port 23 → Cowrie port 2223
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223

# Redirect port 80 → HTTP honeypot port 8080 (pending Tool 41)
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080

# Save rules (survives reboot)
sudo netfilter-persistent save

# Verify
sudo iptables -t nat -L PREROUTING -n --line-numbers
```

### 3.7 Configure Admin SSH on Port 22222

```bash
sudo nano /etc/ssh/sshd_config
# Add or confirm: Port 22222
sudo systemctl reload ssh
```

Verify admin SSH still works on 22222 before closing the session.

### 3.8 Add VM2 Internal Rsync Key to cowrie User

After completing VM2 Section 4.2 (internal key generation), come back here:

```bash
sudo mkdir -p /home/cowrie/.ssh
echo 'PASTE_VM2_THIR_INTERNAL_PUBLIC_KEY_HERE' | \
  sudo tee /home/cowrie/.ssh/authorized_keys
sudo chown -R cowrie:cowrie /home/cowrie/.ssh
sudo chmod 700 /home/cowrie/.ssh
sudo chmod 600 /home/cowrie/.ssh/authorized_keys
```

### 3.9 Configure Cowrie as systemd Service

```bash
sudo nano /etc/systemd/system/cowrie.service
```

```ini
[Unit]
Description=Cowrie SSH/Telnet Honeypot
After=network.target

[Service]
Type=forking
User=cowrie
WorkingDirectory=/home/cowrie/cowrie
ExecStart=/home/cowrie/cowrie/bin/cowrie start
ExecStop=/home/cowrie/cowrie/bin/cowrie stop
PIDFile=/home/cowrie/cowrie/var/run/cowrie.pid
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable cowrie
sudo systemctl start cowrie
sudo systemctl status cowrie
```

### 3.10 Verify VM1 Cowrie Running

```bash
# Log file should be growing
tail -f /home/cowrie/cowrie/var/log/cowrie/cowrie.json

# Port 2222 listening and public-facing
ss -tlnp | grep 2222
# Expected: 0.0.0.0:2222 (twistd)

# Port 22222 listening for admin
ss -tlnp | grep 22222
# Expected: 0.0.0.0:22222 (sshd)
```

---

## Section 4 — VM2 Setup (Brain Node)

```bash
ssh -i thir-pipeline-key.pem -p 22222 ubuntu@VM2_PUBLIC_IP
```

### 4.1 Install Dependencies

```bash
sudo apt update && sudo apt install -y haproxy rsync socat python3-pip
```

### 4.2 Generate Internal Rsync Key

```bash
ssh-keygen -t ed25519 -C 'thir-internal-vm2' \
  -f /home/ubuntu/.ssh/thir_internal -N ''

# Display public key — copy this for VM1 Section 3.8
cat /home/ubuntu/.ssh/thir_internal.pub
```

### 4.3 Configure HAProxy

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

### 4.4 Install VM2 Cowrie (Standby Instance)

VM2 runs a standby Cowrie instance listening only on localhost. It never receives attacker traffic unless HAProxy fails over.

```bash
sudo adduser --disabled-password --gecos "" cowrie

sudo -u cowrie bash << 'EOF'
cd /home/cowrie
git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv cowrie-env
source cowrie-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg
EOF
```

Configure VM2 Cowrie for localhost-only on offset ports:

```bash
sudo nano /home/cowrie/cowrie/etc/cowrie.cfg
```

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
sudo -u cowrie /home/cowrie/cowrie/bin/cowrie start

# Verify localhost-only binding
ss -tlnp | grep -E '4222|4223'
# Expected: 127.0.0.1:4222 and 127.0.0.1:4223 (twistd)
# Must NOT show 0.0.0.0 — backup Cowrie must never be public-facing
```

Configure as systemd service (same unit file as VM1 — cowrie.service).

### 4.5 Create Pipeline Directory

```bash
sudo mkdir -p /opt/thir/logs/downloads
sudo chown -R ubuntu:ubuntu /opt/thir
sudo chmod 775 /opt/thir/logs
```

### 4.6 Configure Admin SSH on Port 22222

Same as VM1 Section 3.7.

### 4.7 Configure rclone for Oracle R2 (`thirha-raw-archive`)

```bash
# Install rclone (binary — not apt)
curl https://rclone.org/install.sh | sudo bash

# Configure as ubuntu user — using thirha-raw-archive credentials from Section 1.1
rclone config
# n → new remote → name: r2 → type: s3 → provider: Cloudflare
# Access Key ID and Secret from thirha-raw-archive token
# Endpoint: https://[ACCOUNT_ID].r2.cloudflarestorage.com

# Verify — this is the Oracle ongoing corpus bucket
rclone lsd r2:thirha-raw-archive
```

> **Note:** If rclone was also configured on AWS EC2 for the AWS corpus upload (Section 1.2), that used remote name `r2-aws` pointing at `thir-raw-archive`. The VM2 rclone config uses remote name `r2` pointing at `thirha-raw-archive`. These are separate remotes for separate buckets.

### 4.8 Set Up Rsync Cron (Temporary — Until Tool 38 Is Built)

```bash
# Create rsync script
nano /home/ubuntu/rsync_from_vm1.sh
```

```bash
#!/bin/bash
# rsync_from_vm1.sh — Pull Cowrie logs from VM1 to VM2 via private VCN
# Runs at :55 every 2 hours — before GitHub Actions at :00

SSH_KEY="/home/ubuntu/.ssh/thir_internal"
VM1_IP="10.0.0.53"
VM1_LOG="/home/cowrie/cowrie/var/log/cowrie/"
LOCAL_LOG="/opt/thir/logs/"
LOG_FILE="/home/ubuntu/var/log/thir_rsync.log"

mkdir -p /home/ubuntu/var/log

echo "$(date -u): rsync start" >> "$LOG_FILE"

rsync -az --append \
  -e "ssh -i $SSH_KEY -o StrictHostKeyChecking=accept-new" \
  cowrie@${VM1_IP}:${VM1_LOG} \
  ${LOCAL_LOG} \
  >> "$LOG_FILE" 2>&1

echo "$(date -u): rsync complete — exit $?" >> "$LOG_FILE"
```

```bash
chmod +x /home/ubuntu/rsync_from_vm1.sh

# Add to crontab
crontab -e
# Add line:
# 55 */2 * * * /home/ubuntu/rsync_from_vm1.sh
```

### 4.9 Set Up R2 Sync Cron

```bash
# R2 sync runs daily at 01:00 UTC
# sync_to_r2.sh should already be present at /home/ubuntu/sync_to_r2.sh
# Verify:
ls -la /home/ubuntu/sync_to_r2.sh

# Confirm crontab has correct path:
crontab -l | grep r2
# Expected: 0 1 * * * /home/ubuntu/sync_to_r2.sh
```

---

## Section 5 — Connectivity Verification

### 5.1 Verify VCN Internal Connectivity (from VM2)

```bash
# Ping VM1 private IP
ping -c 4 10.0.0.53
# Expected: 0% loss, RTT < 5ms

# TCP check VM1 Cowrie
timeout 5 bash -c 'echo > /dev/tcp/10.0.0.53/2222' && echo 'OK' || echo 'FAIL'
# Expected: OK

# TCP check VM1 admin SSH
timeout 5 bash -c 'echo > /dev/tcp/10.0.0.53/22222' && echo 'OK' || echo 'FAIL'
# Expected: OK
```

### 5.2 Verify Rsync Works

```bash
# Test rsync with dry-run first
rsync -avzn \
  -e "ssh -i /home/ubuntu/.ssh/thir_internal -o StrictHostKeyChecking=accept-new" \
  cowrie@10.0.0.53:/home/cowrie/cowrie/var/log/cowrie/ \
  /opt/thir/logs/
# Expected: file list without errors

# Run actual sync
/home/ubuntu/rsync_from_vm1.sh

# Verify cowrie.json arrived
ls -lh /opt/thir/logs/cowrie.json
# Expected: file present, size > 0
```

### 5.3 Verify HAProxy Backends

```bash
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | \
  cut -d',' -f1,2,18 | grep -v "^#"
# Expected:
# cowrie_backend,vm1,UP
# cowrie_backend,vm2_backup,UP
# telnet_backend,vm1_telnet,UP
# telnet_backend,vm2_telnet_backup,UP
```

---

## Section 6 — GitHub Actions Pipeline

### 6.1 Fork thir-live → thir-ha

1. GitHub → thir-live → Fork → Name: `thir-ha`
2. Default branch: `oracle-ha`
3. Initial commits: `MIGRATION.md`, `ARCHITECTURE.md`, `config/haproxy.cfg`
4. Tag: `git tag v2.0-ha-architecture-baseline`

### 6.2 Update GitHub Secrets

| Secret | Value | Action |
|---|---|---|
| `ORACLE_VPS_SSH_KEY` | Contents of `thir_pipeline_key` private key | Unchanged from thir-live |
| `ORACLE_VPS_IP` | VM2 public IP (150.230.174.199) | **UPDATE** — was AWS EC2 IP |
| `ABUSEIPDB_API_KEY` | AbuseIPDB key | Unchanged |
| `OTX_API_KEY` | AlienVault OTX key | Unchanged |
| `CLOUDFLARE_R2_KEY` | R2 Access Key ID | **ADD NEW** |
| `CLOUDFLARE_R2_SECRET` | R2 Secret Access Key | **ADD NEW** |

### 6.3 Confirm Pipeline reads from Oracle VM2

The pipeline fetch step must read from `/opt/thir/logs/cowrie.json` on VM2 (not the old AWS Cowrie path). Verify in `pipeline.yml`:

```yaml
ssh -p 22222 ubuntu@${{ secrets.ORACLE_VPS_IP }} \
  "tail -n +$LINE /opt/thir/logs/cowrie.json"
```

### 6.4 Run Pipeline Manually

GitHub → thir-ha → Actions → THIR Live Pipeline → Run workflow

Expected: All steps pass, `data/posture.json` updates, dashboard at `thirha.aegispub.com` shows live data.

---

## Section 7 — Parallel Run and Cutover

### 7.1 Parallel Run

Run both pipelines simultaneously for 72 hours. Compare `data/` output. Confirm Oracle output matches AWS before cutover.

### 7.2 Cutover

Single action: update `ORACLE_VPS_IP` secret from AWS EC2 IP to Oracle VM2 IP (`150.230.174.199`).

Monitor `thirha.aegispub.com` for 30 minutes after cutover. Data should update normally on the next pipeline run.

### 7.3 Wrap-Up

After 72h+ Oracle stability:

```bash
# Final AWS corpus sync — ensure all remaining AWS logs are in thir-raw-archive
ssh -i thir-pipeline-key.pem -p 22222 ubuntu@AWS_EC2_IP

# Compress any logs not yet compressed
cd /home/cowrie/cowrie/var/log/cowrie/
for f in cowrie.json.2026-* cowrie.log.2026-*; do
  [ -f "${f}.gz" ] || gzip -k "$f"
done

# Upload to AWS corpus bucket (thir-raw-archive)
for f in cowrie.json.*.gz; do
  month=$(echo $f | grep -o '[0-9]\{4\}-[0-9]\{2\}')
  rclone copy $f r2-aws:thir-raw-archive/cowrie-json/$month/
done

# Verify completeness
rclone ls r2-aws:thir-raw-archive | wc -l
```

Then:
- Run Tool 00 historical processor against `thir-raw-archive` (AWS corpus)
- Commit `historical_data/` to thir-ha
- Update thir-live README.md with archive notice and link to both R2 buckets
- GitHub → thir-live → Settings → Archive this repository
- Cancel AWS EC2 before billing resumes (~Sep 2026)

---

## Section 8 — Troubleshooting

### Pipeline fails — SSH timeout on VM2

```bash
# Verify ORACLE_VPS_IP points to VM2 (150.230.174.199), not VM1
# Verify port 22222 is open in Oracle VCN security list
# Test from your machine:
ssh -p 22222 ubuntu@150.230.174.199 echo OK
```

### cowrie.json stale on VM2 (>2.5 hours old)

```bash
# Check rsync log
tail -20 /home/ubuntu/var/log/thir_rsync.log

# Check cron is running
systemctl is-active cron

# Run rsync manually
/home/ubuntu/rsync_from_vm1.sh
```

### HAProxy backend DOWN

```bash
# Check HAProxy status
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | cut -d',' -f1,2,18

# Check VM1 Cowrie is running
ssh -i thir-pipeline-key.pem -p 22222 ubuntu@10.0.0.53
sudo -u cowrie /home/cowrie/cowrie/bin/cowrie status
```

### Tool 05 reports OFFLINE but HAProxy shows UP

This means HAProxy is up but Cowrie on VM1 has crashed. HAProxy will have already failed over to VM2 standby. Restart Cowrie on VM1 — traffic automatically shifts back once HAProxy sees two consecutive UP checks (60 seconds).

```bash
sudo systemctl restart cowrie   # on VM1
```

### Downloads missing from VM2

```bash
# Check downloads directory ownership — must be ubuntu:ubuntu
ls -la /opt/thir/logs/downloads/
# If cowrie:cowrie, fix:
sudo chown ubuntu:ubuntu /opt/thir/logs/downloads/
```

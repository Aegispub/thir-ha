# Cloudflare — DNS Failover, Health Checks & Tunnel Setup

*Reference for all Cloudflare configuration in the THIR HA deployment. Covers DNS records, health check failover, DDoS protection, cloudflared tunnel setup, and Cloudflare R2 archive integration.*

---

## Overview

Cloudflare sits in front of the THIR HA infrastructure at two levels:

1. **DNS + DDoS protection** — all traffic to `thirha.aegispub.com` and the honeypot IPs passes through Cloudflare. Provides DDoS mitigation at no cost on the free tier.
2. **Health check failover** — Cloudflare monitors VM1 public IP. If VM1 goes down, DNS automatically switches the A record to VM2 public IP within ~60–120 seconds. This is the outer failover layer above HAProxy.
3. **Cloudflared tunnels** (planned) — secure outbound-only tunnels from both VMs, eliminating the need for any inbound port exposure. Not yet deployed.
4. **Cloudflare R2** — object storage for raw log archival. Two buckets: `thir-raw-archive` (AWS corpus) and `thirha-raw-archive` (Oracle corpus).

---

## Section 1 — DNS Records

### Current DNS Configuration

| Record | Type | Value | Proxied | Purpose |
|---|---|---|---|---|
| `thirha.aegispub.com` | CNAME | `[github-user].github.io` | Yes | Dashboard — GitHub Pages |
| Honeypot A record | A | VM1 public IP (129.80.119.236) | Yes | Attacker-facing honeypot traffic |
| Failover A record | A | VM2 public IP (150.230.174.199) | Yes | Standby — activated by health check |

### DNS Failover TTL

During steady state: TTL 300 seconds (5 minutes) — balances propagation speed with DNS caching.

During migration or failover: Reduce to 60 seconds before making IP changes. Restore to 300 after the new IP is confirmed stable for 30+ minutes.

```
# Verify DNS propagation
dig thirha.aegispub.com @1.1.1.1
dig thirha.aegispub.com @8.8.8.8
```

---

## Section 2 — Health Check Configuration

Cloudflare free tier health checks allow automatic DNS failover. Configure once — Cloudflare monitors continuously.

### Health Check Setup

Cloudflare Dashboard → Traffic → Health Checks → Create Health Check

**VM1 health check:**

| Field | Value |
|---|---|
| Name | `thir-vm1-health` |
| URL | `http://129.80.119.236/health` |
| Type | HTTP |
| Interval | 60 seconds |
| Retries | 2 |
| Expected status code | 200 (or TCP connect if no HTTP endpoint yet) |
| Notification | Alert on status change |

**VM2 health check:**

| Field | Value |
|---|---|
| Name | `thir-vm2-health` |
| URL | `http://150.230.174.199/health` |
| Type | HTTP |
| Interval | 60 seconds |
| Retries | 2 |
| Expected status code | 200 |
| Notification | Alert on status change |

> **Note:** The `/health` endpoint requires Tool 41 (HTTP honeypot) to be deployed — it will expose this endpoint on port 8080, proxied by HAProxy on port 80. Until Tool 41 is live, configure health checks as TCP type against port 2222 instead.

### DNS Failover Record

Cloudflare Dashboard → DNS → Add Record:

- Primary A record: points to VM1 (129.80.119.236) — active under normal operation
- Create a second A record pointing to VM2 (150.230.174.199) — linked to `thir-vm1-health`
- When `thir-vm1-health` transitions to DOWN, Cloudflare activates the VM2 record

### Failover Timing

| Event | Detection | DNS Switch | Propagation | Total |
|---|---|---|---|---|
| VM1 goes DOWN | ~60 seconds (2 failed checks × 30s interval) | Immediate on detection | 60 seconds (TTL) | ~2 minutes |
| VM1 comes back UP | ~60 seconds (2 passed checks) | Immediate on detection | 60 seconds | ~2 minutes |

This is the outer layer. HAProxy on VM2 provides inner-layer TCP failover in 30–60 seconds for service-level failures (Cowrie crash while VM1 is up).

---

## Section 3 — Manual DNS Failover

Use when you know VM1 is down and want faster failover than the health check detection window.

```
Cloudflare Dashboard → DNS → honeypot A record
→ Edit → Change IP from 129.80.119.236 to 150.230.174.199
→ Set TTL to 60 seconds
→ Save
```

Verify propagation:

```bash
dig honeypot.aegispub.com @1.1.1.1
# Expected: 150.230.174.199 within ~60 seconds
```

Restore VM1 as primary after rebuild:

```
→ Change IP back to 129.80.119.236
→ Restore TTL to 300 seconds after confirming stable
```

---

## Section 4 — Cloudflared Tunnel Setup (Planned)

Cloudflared tunnels replace public port exposure with secure outbound-only connections from each VM to Cloudflare's edge. When deployed, external traffic reaches the VM through the tunnel rather than direct TCP — eliminating the need for public IP exposure on honeypot ports.

**Status:** Not yet deployed. The sections below document the intended setup for when cloudflared is added.

### Prerequisites

- Cloudflare account with the `aegispub.com` zone active
- `cloudflared` binary installed on both VMs

### Install cloudflared

```bash
# On both VM1 and VM2
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 \
  -o /usr/local/bin/cloudflared
chmod +x /usr/local/bin/cloudflared
cloudflared --version
```

### Authenticate

```bash
# Run once per VM — opens browser auth
cloudflared tunnel login
# This creates ~/.cloudflared/cert.pem
```

### Create Tunnels

```bash
# On VM1
cloudflared tunnel create thir-vm1
# Note the tunnel UUID returned

# On VM2
cloudflared tunnel create thir-vm2
# Note the tunnel UUID returned
```

### Configure Tunnels

VM1 — `/etc/cloudflared/config.yml`:

```yaml
tunnel: <VM1_TUNNEL_UUID>
credentials-file: /root/.cloudflared/<VM1_TUNNEL_UUID>.json

ingress:
  - hostname: honeypot.aegispub.com
    service: tcp://localhost:2222
  - service: http_status:404
```

VM2 — `/etc/cloudflared/config.yml`:

```yaml
tunnel: <VM2_TUNNEL_UUID>
credentials-file: /root/.cloudflared/<VM2_TUNNEL_UUID>.json

ingress:
  - hostname: pipeline.aegispub.com
    service: tcp://localhost:22222
  - service: http_status:404
```

### Run as systemd Service

```bash
cloudflared service install
sudo systemctl enable cloudflared
sudo systemctl start cloudflared
sudo systemctl status cloudflared
```

### DNS Records for Tunnels

```bash
# Create CNAME records pointing to tunnel
cloudflared tunnel route dns thir-vm1 honeypot.aegispub.com
cloudflared tunnel route dns thir-vm2 pipeline.aegispub.com
```

### Recovery

```bash
# Check tunnel status
sudo systemctl status cloudflared
cloudflared tunnel list
cloudflared tunnel info <TUNNEL_UUID>

# Restart
sudo systemctl restart cloudflared

# Re-authenticate if credentials lost
cloudflared tunnel login
cloudflared tunnel create thir-vm1   # recreate if needed
```

---

## Section 5 — Cloudflare R2 Archive

Two separate buckets serve two distinct corpora. See `config/haproxy.cfg` comments and `ARCHITECTURE.md` for full context.

| Bucket | Corpus | Period | Access |
|---|---|---|---|
| `thir-raw-archive` | AWS EC2 logs | March–[retirement] 2026 | Read-only after AWS retires |
| `thirha-raw-archive` | Oracle VM1 logs | June 2026+ | Active — daily writes |

### R2 Token Management

Each bucket has its own API token with Object Read & Write scope scoped to that bucket only. Token credentials are stored in:

- VM2 ubuntu user rclone config (`~/.config/rclone/rclone.conf`) — `thirha-raw-archive` token for ongoing sync
- GitHub Secrets `CLOUDFLARE_R2_KEY` and `CLOUDFLARE_R2_SECRET` — for any pipeline-triggered R2 operations

Never share the two bucket tokens. The AWS corpus bucket token can be downgraded to Read Only after AWS EC2 is terminated.

### Verify R2 Connectivity

```bash
# On VM2 — as ubuntu user
rclone lsd r2:thirha-raw-archive
rclone ls r2:thirha-raw-archive | wc -l

# Check most recent upload
rclone lsl r2:thirha-raw-archive --max-depth 3 | sort -k2,3 | tail -5
```

### Manual Sync Trigger

```bash
# On VM2 — force an immediate R2 sync outside the daily cron
sudo -u ubuntu /home/ubuntu/sync_to_r2.sh

# Check result
tail -20 /home/ubuntu/var/log/r2_upload.log
```

---

## Section 6 — DDoS Protection

Cloudflare's free tier provides automatic DDoS mitigation for all proxied traffic. Both the dashboard (`thirha.aegispub.com`) and any Cloudflare-proxied honeypot subdomains benefit from this automatically.

No configuration is required. Cloudflare's network absorbs volumetric attacks before they reach VM1 or VM2.

**Note on honeypot traffic:** Cowrie captures connections from real attackers. Cloudflare DDoS protection may rate-limit or block sustained campaigns that exceed free tier thresholds. If you observe a campaign being filtered before reaching Cowrie, this is expected Cloudflare behaviour — not a system fault. The raw Cowrie logs on VM1 will still capture whatever gets through.

---

## Section 7 — Failover State Reference

| VM1 | VM2 | Cloudflare DNS | HAProxy | Action |
|---|---|---|---|---|
| UP | UP | VM1 primary | VM1 primary | None — normal operations |
| DOWN | UP | Failover to VM2 (~2 min) | Already shifted (<60s) | Investigate VM1 — RB-02 |
| UP | DOWN | VM1 primary (unchanged) | N/A — HAProxy is on VM2 | Restore VM2 — RB-03 |
| DOWN | DOWN | VM2 (failed) | N/A | Full rebuild — RB-06 |

The HAProxy layer (inner) is faster than the Cloudflare DNS layer (outer). In most VM1 failure scenarios, HAProxy has already shifted SSH/Telnet traffic to VM2 standby Cowrie before Cloudflare has even detected the failure. Cloudflare failover matters for the HTTP honeypot (Tool 41) and any future services that are DNS-fronted directly.

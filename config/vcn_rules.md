# Oracle VCN — Subnet Security List Rules

*Reference for the Oracle Virtual Cloud Network ingress rules required by the THIR HA two-node deployment.*

---

## Critical Oracle Note

Security rules must be configured at **two independent layers**:

1. **Oracle VCN Subnet Security List** — network-level, controls traffic reaching the VM's network interface
2. **Instance firewall** — OS-level, iptables/ufw on each VM

Both layers must allow traffic. The VCN Security List is the outer gate — if it blocks a port, no traffic reaches the instance regardless of what iptables allows. This is the most common Oracle setup mistake: iptables is configured correctly but the VCN Security List was never updated.

---

## Navigation

Oracle Cloud Console → Networking → Virtual Cloud Networks → [your VCN] → Subnets → [your subnet] → Security Lists → Default Security List → Add Ingress Rules

---

## Required Ingress Rules

### Applied to Both VM1 and VM2

| Rule | Source CIDR | Protocol | Destination Port | Purpose |
|---|---|---|---|---|
| 1 | 0.0.0.0/0 | TCP | 2222 | Cowrie SSH honeypot — attacker-facing |
| 2 | 0.0.0.0/0 | TCP | 2223 | Cowrie Telnet honeypot — attacker-facing |
| 3 | 0.0.0.0/0 | TCP | 80, 443 | HTTP honeypot — pending Tool 41 deployment |
| 4 | Your IP only | TCP | 22222 | Admin SSH — PuTTY access to both VMs |
| 5 | 10.0.0.0/24 | All protocols | All ports | Internal VCN — rsync, HAProxy health checks, VCN-internal traffic |

### Rule Notes

**Rule 1 (port 2222):** On VM2, port 2222 is HAProxy fronting Cowrie on VM1. On VM1, port 2222 is Cowrie directly. Attacker traffic hits VM2 HAProxy first via Cloudflare DNS, which proxies to VM1 via private VCN. Both VMs need this rule open to allow HAProxy health checks and failover.

**Rule 2 (port 2223):** Same pattern as Rule 1 for Telnet. VM2 HAProxy binds `*:2223` and proxies to VM1 `10.0.0.53:2223`.

**Rule 3 (ports 80, 443):** Commented out in HAProxy config until Tool 41 (HTTP honeypot) is deployed on VM1. Add the VCN rule now so no console intervention is needed when Tool 41 goes live.

**Rule 4 (port 22222):** Restrict source CIDR to your specific IP address — not 0.0.0.0/0. This is the only real management path into both VMs. Keeping it IP-restricted is the single most important hardening step. If your IP changes, update this rule before attempting to SSH.

**Rule 5 (10.0.0.0/24):** Allows all traffic between VM1 and VM2 on the private VCN. Required for:
- HAProxy health checks (VM2 → VM1 on ports 2222, 2223)
- rsync log collection (VM2 → VM1 on port 22 / cowrie user)
- Any future inter-VM communication

---

## Current Live State

Confirmed from baseline run June 2026:

| Rule | Status | Notes |
|---|---|---|
| Port 2222 (TCP) | ✓ Active | Cowrie SSH receiving attacker connections |
| Port 2223 (TCP) | ✓ Active | Cowrie Telnet receiving attacker connections |
| Port 80, 443 (TCP) | ✓ Active | Rule present — 0 packets until Tool 41 deployed |
| Port 22222 (TCP) | ✓ Active | Admin SSH restricted to owner IP |
| 10.0.0.0/24 (All) | ✓ Active | rsync and HAProxy health checks working |

---

## Default Egress Rule

Oracle VCN default security list includes a permissive egress rule (0.0.0.0/0, All protocols, All ports). This allows:
- VM1 Cowrie to make outbound connections (normal honeypot operation — attackers may initiate outbound from within Cowrie)
- VM2 pipeline to reach GitHub Actions, AbuseIPDB, OTX, Cloudflare R2
- rclone uploads from VM2 to R2
- Oracle Cloud Agent phone-home traffic

No changes to egress rules are required.

---

## Verification Commands

After setting rules, verify from each VM:

```bash
# From VM2 — confirm VM1 ports reachable over VCN
timeout 5 bash -c 'echo > /dev/tcp/10.0.0.53/2222' && echo 'VM1:2222 OK' || echo 'VM1:2222 FAIL'
timeout 5 bash -c 'echo > /dev/tcp/10.0.0.53/2223' && echo 'VM1:2223 OK' || echo 'VM1:2223 FAIL'
timeout 5 bash -c 'echo > /dev/tcp/10.0.0.53/22222' && echo 'VM1:22222 OK' || echo 'VM1:22222 FAIL'

# From your machine — confirm public ports reachable on VM2
nc -zv 150.230.174.199 2222
nc -zv 150.230.174.199 2223
nc -zv 150.230.174.199 22222

# HAProxy backend status (on VM2)
echo 'show stat' | sudo socat stdio /var/run/haproxy/admin.sock | cut -d',' -f1,2,18
```

---

## Recovery Reference

If VCN rules are lost (e.g. VCN deleted and recreated during RB-06 full stack rebuild), re-apply all five rules above before attempting any SSH or pipeline connectivity. Rules 1–3 are required for HAProxy to pass traffic and health check VM1. Rule 4 is required for admin access. Rule 5 is required for rsync and HAProxy backends.

See `docs/THIR_HA_Runbooks_v2.docx` RB-06 Phase 1 for the full VM rebuild sequence including VCN rule restoration.

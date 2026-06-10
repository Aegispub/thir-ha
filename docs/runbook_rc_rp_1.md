# THIR-RC-RP-1 — Legacy Runbook (AWS EC2 Single Node)

> **SUPERSEDED — This runbook covers the original AWS EC2 single-node deployment (thir-live).**
>
> It is retained here for historical reference only. The THIR infrastructure migrated to Oracle Cloud Always Free two-node HA architecture in June 2026.
>
> **For current recovery procedures, use `docs/THIR_HA_Runbooks_v2.docx (planned)`:**
>
> | Scenario | Runbook |
> |---|---|
> | VM1 sensor failure | RB-02 |
> | VM2 brain failure | RB-03 |
> | Manual / automatic failover | RB-04 |
> | HAProxy + Cloudflare recovery | RB-05 |
> | Full stack rebuild from zero | RB-06 |
> | Architecture reference | RB-01 |
>
> **Legacy reference dates:** Operational March 7 2026 – September 6 2026
> **AWS corpus:** Raw logs archived to Cloudflare R2 `thir-raw-archive`

---

# THIR Recovery Runbook
## RC.RP-1 — Recovery Planning
### If the AWS EC2 Honeypot Is Compromised or Lost

---

**Document ID:** THIR-RC-RP-1
**NIST CSF Control:** RC.RP-1 — Recovery plan is executed during or after a cybersecurity incident
**NIST Function:** RECOVER
**Asset Covered:** AWS EC2 Ubuntu — Cowrie SSH Honeypot (`thir-honeypot-01`)
**Owner:** nikhilsalunkemumbai
**Last Reviewed:** 2025-03-08
**Status:** LEGACY — superseded by THIR_HA_Runbooks_v2.docx

---

## 1. Purpose

This runbook documents the step-by-step procedure to recover the THIR honeypot infrastructure if the AWS EC2 instance is compromised, corrupted, terminated, or otherwise unavailable. It exists so recovery can begin immediately without making decisions under pressure.

A honeypot getting compromised is not a failure. It is the expected outcome of intentional exposure. The goal is to restore the sensor quickly, cleanly, and from a known-good state.

---

## 2. Recovery Trigger Conditions

Execute this runbook if any of the following are true:

| Condition | How You Know |
|---|---|
| EC2 instance unreachable | Tool 05 reports `DOWN` in `data/posture.json` for 2+ consecutive hourly runs |
| Cowrie process crashed | No new sessions in `ir_cases.json` — but EC2 is still reachable via SSH |
| EC2 host appears compromised | Cowrie logs show `iptables`, `/proc`, `/etc/shadow` commands — attacker escalated |
| Unexpected outbound traffic | AbuseIPDB or OTX flags your EC2 IP as a threat actor |
| EC2 terminated unexpectedly | AWS Console shows instance as Terminated |

---

## 3. Before You Rebuild — Evidence First

> **Do not rebuild until evidence is preserved. A honeypot compromise is intelligence, not a crisis.**

### 3.1 Preserve Logs

If the EC2 is still accessible:

```bash
# From your local machine
scp -P 22222 -i thir-pipeline-key.pem \
  ubuntu@EC2_IP:/home/cowrie/cowrie/var/log/cowrie/* \
  ./evidence/

scp -P 22222 -i thir-pipeline-key.pem \
  ubuntu@EC2_IP:/var/log/auth.log \
  ubuntu@EC2_IP:/var/log/syslog \
  ./evidence/
```

### 3.2 Take EBS Snapshot

AWS Console → EC2 → Instances → [instance] → Storage → [volume] → Actions → Create Snapshot

Label: `thir-compromise-evidence-YYYY-MM-DD`

### 3.3 Document the Incident

Before terminating the instance, note:
- Last known good time (last clean pipeline run)
- First anomaly indicator
- Any attacker commands that targeted the host OS (not just Cowrie)
- Whether the pipeline key was exposed

---

## 4. Recovery Steps

### 4.1 Launch New EC2 Instance

- AWS Console → EC2 → Launch Instance
- AMI: Ubuntu Server 22.04 LTS
- Type: t2.micro (free tier)
- Key pair: use existing `thir-pipeline-key`
- Security group: ports 2222, 22222, 80/443 inbound; restrict port 22222 to your IP

### 4.2 Assign Elastic IP

- EC2 → Elastic IPs → Allocate → Associate with new instance
- Update GitHub secret `ORACLE_VPS_IP` with new public IP if Elastic IP changed

### 4.3 Install Cowrie

```bash
ssh -i thir-pipeline-key.pem -p 22222 ubuntu@NEW_EC2_IP

sudo apt update && sudo apt install -y \
  python3-virtualenv git libssl-dev libffi-dev build-essential

sudo adduser --disabled-password cowrie
sudo su - cowrie

git clone https://github.com/cowrie/cowrie.git
cd cowrie
virtualenv cowrie-env && source cowrie-env/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
cp etc/cowrie.cfg.dist etc/cowrie.cfg
# Edit: listen_port = 2222, output_jsonlog = true

bin/cowrie start
```

### 4.4 Restore iptables

```bash
# Port redirect 22 → 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sudo netfilter-persistent save
```

### 4.5 Add Pipeline Key

```bash
# Ensure pipeline public key is in ubuntu authorized_keys
# (Should already be there from EC2 launch — verify)
cat ~/.ssh/authorized_keys | grep pipeline
```

### 4.6 Trigger Pipeline

GitHub → thir-live → Actions → THIR Live Pipeline → Run workflow

Verify `data/posture.json` shows UP and `threats.aegispub.com` updates.

---

## 5. Post-Recovery

- Open an IR case in the THIR dashboard documenting the incident
- Review the evidence files — attacker commands inside Cowrie vs host OS escalation
- Update `data/posture.json` CIS control statuses if any controls were affected
- Consider whether the compromise yielded any new IOCs worth enriching

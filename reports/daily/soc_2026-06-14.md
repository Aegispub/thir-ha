# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T17:23:38Z |
| **Shift Time** | 17:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **73** |
| Confirmed Threats | **62** |
| False Positives Filtered | **11** (15.1%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **8** |
| High Severity Cases | **26** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **47** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **5** |
| Unique Usernames | **2** |
| Unique Passwords | **5** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 12 |
| `123@@@` | 6 |
| `smo@@kkklss` | 6 |
| `` | 2 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 12 |
| `root` | `123@@@` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `root` | `` | 2 |
| `admin` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-14T14:56:14 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-14T14:56:14 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-14T14:56:21 |
| `root` | `LeitboGi0ro` | `40.233.83.131` | 2026-06-14T15:16:39 |
| `root` | `123@@@` | `40.233.83.131` | 2026-06-14T15:16:39 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-14T15:34:08 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-14T15:34:09 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-14T15:34:16 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-14T15:56:45 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-14T15:56:47 |
| `root` | `123@@@` | `168.156.171.11` | 2026-06-14T16:46:50 |
| `root` | `LeitboGi0ro` | `168.156.171.11` | 2026-06-14T16:46:50 |
| `admin` | `admin` | `5.175.169.118` | 2026-06-14T16:54:25 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-14T16:54:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **73** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 24 |
| libssh | 9 |
| Go SSH scanner | 3 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 16 | 3 |
| `6372ee695756...` | Modern SSH client | 8 | 2 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 16 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 8 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 2 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **19** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS10430` | Washington State K-20 Telecommunications Network | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS398019` | Dynu Systems Incorporated | 1 | HIGH |
| `AS208476` | Badr Ouseffar trading as Rootlink | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-572f21b73251

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 14:56 |
| **Last Seen** | 2026-06-14 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:56:13` | `cowrie.session.connect` |
| `2026-06-14 14:56:13` | `cowrie.client.version` |
| `2026-06-14 14:56:13` | `cowrie.client.kex` |
| `2026-06-14 14:56:14` | `cowrie.login.success` |
| `2026-06-14 14:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e5c7cc9e0a6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 14:56 |
| **Last Seen** | 2026-06-14 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:56:14` | `cowrie.session.connect` |
| `2026-06-14 14:56:14` | `cowrie.client.version` |
| `2026-06-14 14:56:14` | `cowrie.client.kex` |
| `2026-06-14 14:56:14` | `cowrie.login.success` |
| `2026-06-14 14:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-041d13c55419

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 14:56 |
| **Last Seen** | 2026-06-14 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:56:20` | `cowrie.session.connect` |
| `2026-06-14 14:56:20` | `cowrie.client.version` |
| `2026-06-14 14:56:21` | `cowrie.client.kex` |
| `2026-06-14 14:56:21` | `cowrie.login.success` |
| `2026-06-14 14:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-025c2556a36d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-14 14:56 |
| **Last Seen** | 2026-06-14 14:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 14:56:21` | `cowrie.session.connect` |
| `2026-06-14 14:56:21` | `cowrie.client.version` |
| `2026-06-14 14:56:22` | `cowrie.client.kex` |
| `2026-06-14 14:56:22` | `cowrie.login.success` |
| `2026-06-14 14:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139a6372b02b

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 15:16 |
| **Last Seen** | 2026-06-14 15:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:16:39` | `cowrie.session.connect` |
| `2026-06-14 15:16:39` | `cowrie.client.version` |
| `2026-06-14 15:16:39` | `cowrie.client.kex` |
| `2026-06-14 15:16:39` | `cowrie.login.success` |
| `2026-06-14 15:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07240fd8186

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 15:16 |
| **Last Seen** | 2026-06-14 15:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:16:39` | `cowrie.session.connect` |
| `2026-06-14 15:16:39` | `cowrie.client.version` |
| `2026-06-14 15:16:39` | `cowrie.client.kex` |
| `2026-06-14 15:16:39` | `cowrie.login.success` |
| `2026-06-14 15:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f97a549cea

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 15:17 |
| **Last Seen** | 2026-06-14 15:19 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:17:03` | `cowrie.session.connect` |
| `2026-06-14 15:17:03` | `cowrie.client.version` |
| `2026-06-14 15:17:03` | `cowrie.client.kex` |
| `2026-06-14 15:17:03` | `cowrie.login.success` |
| `2026-06-14 15:17:04` | `cowrie.session.file_upload` |
| `2026-06-14 15:17:05` | `cowrie.session.params` |
| `2026-06-14 15:17:05` | `cowrie.command.input` |
| `2026-06-14 15:17:05` | `cowrie.command.input` |
| `2026-06-14 15:17:05` | `cowrie.command.input` |
| `2026-06-14 15:17:05` | `cowrie.command.failed` |
| `2026-06-14 15:17:05` | `cowrie.log.closed` |
| `2026-06-14 15:17:06` | `cowrie.session.params` |
| `2026-06-14 15:17:06` | `cowrie.command.input` |
| `2026-06-14 15:17:06` | `cowrie.log.closed` |
| `2026-06-14 15:17:06` | `cowrie.session.params` |
| `2026-06-14 15:17:06` | `cowrie.command.input` |
| `2026-06-14 15:17:06` | `cowrie.log.closed` |
| `2026-06-14 15:17:07` | `cowrie.session.params` |
| `2026-06-14 15:17:07` | `cowrie.command.input` |
| `2026-06-14 15:17:07` | `cowrie.command.failed` |
| `2026-06-14 15:17:07` | `cowrie.command.failed` |
| `2026-06-14 15:18:08` | `cowrie.session.params` |
| `2026-06-14 15:18:08` | `cowrie.command.input` |
| `2026-06-14 15:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868586fc19a1

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-14 15:19 |
| **Last Seen** | 2026-06-14 15:21 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:19:23` | `cowrie.session.connect` |
| `2026-06-14 15:19:23` | `cowrie.client.version` |
| `2026-06-14 15:19:23` | `cowrie.client.kex` |
| `2026-06-14 15:19:23` | `cowrie.login.success` |
| `2026-06-14 15:19:24` | `cowrie.session.file_upload` |
| `2026-06-14 15:19:25` | `cowrie.session.params` |
| `2026-06-14 15:19:25` | `cowrie.command.input` |
| `2026-06-14 15:19:25` | `cowrie.command.input` |
| `2026-06-14 15:19:25` | `cowrie.command.input` |
| `2026-06-14 15:19:25` | `cowrie.command.failed` |
| `2026-06-14 15:19:25` | `cowrie.log.closed` |
| `2026-06-14 15:19:26` | `cowrie.session.params` |
| `2026-06-14 15:19:26` | `cowrie.command.input` |
| `2026-06-14 15:19:26` | `cowrie.log.closed` |
| `2026-06-14 15:19:26` | `cowrie.session.params` |
| `2026-06-14 15:19:26` | `cowrie.command.input` |
| `2026-06-14 15:19:26` | `cowrie.log.closed` |
| `2026-06-14 15:19:27` | `cowrie.session.params` |
| `2026-06-14 15:19:27` | `cowrie.command.input` |
| `2026-06-14 15:19:27` | `cowrie.command.failed` |
| `2026-06-14 15:19:27` | `cowrie.command.failed` |
| `2026-06-14 15:20:28` | `cowrie.session.params` |
| `2026-06-14 15:20:28` | `cowrie.command.input` |
| `2026-06-14 15:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b11cbb608811

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 15:34 |
| **Last Seen** | 2026-06-14 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:34:08` | `cowrie.session.connect` |
| `2026-06-14 15:34:08` | `cowrie.client.version` |
| `2026-06-14 15:34:08` | `cowrie.client.kex` |
| `2026-06-14 15:34:08` | `cowrie.login.success` |
| `2026-06-14 15:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38192c56340f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 15:34 |
| **Last Seen** | 2026-06-14 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:34:09` | `cowrie.session.connect` |
| `2026-06-14 15:34:09` | `cowrie.client.version` |
| `2026-06-14 15:34:09` | `cowrie.client.kex` |
| `2026-06-14 15:34:09` | `cowrie.login.success` |
| `2026-06-14 15:34:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fb7f7e40d1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 15:34 |
| **Last Seen** | 2026-06-14 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:34:16` | `cowrie.session.connect` |
| `2026-06-14 15:34:16` | `cowrie.client.version` |
| `2026-06-14 15:34:16` | `cowrie.client.kex` |
| `2026-06-14 15:34:16` | `cowrie.login.success` |
| `2026-06-14 15:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a2b41fd231

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 15:34 |
| **Last Seen** | 2026-06-14 15:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:34:16` | `cowrie.session.connect` |
| `2026-06-14 15:34:16` | `cowrie.client.version` |
| `2026-06-14 15:34:16` | `cowrie.client.kex` |
| `2026-06-14 15:34:16` | `cowrie.login.success` |
| `2026-06-14 15:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563f79296655

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-14 15:56 |
| **Last Seen** | 2026-06-14 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:56:44` | `cowrie.session.connect` |
| `2026-06-14 15:56:44` | `cowrie.client.version` |
| `2026-06-14 15:56:44` | `cowrie.client.kex` |
| `2026-06-14 15:56:45` | `cowrie.login.success` |
| `2026-06-14 15:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc94cbefa1c4

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-14 15:56 |
| **Last Seen** | 2026-06-14 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:56:45` | `cowrie.session.connect` |
| `2026-06-14 15:56:45` | `cowrie.client.version` |
| `2026-06-14 15:56:46` | `cowrie.client.kex` |
| `2026-06-14 15:56:47` | `cowrie.login.success` |
| `2026-06-14 15:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b61f2f2d23a

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-14 15:57 |
| **Last Seen** | 2026-06-14 15:59 |
| **Session Duration** | 133s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:57:10` | `cowrie.session.connect` |
| `2026-06-14 15:57:10` | `cowrie.client.version` |
| `2026-06-14 15:57:10` | `cowrie.client.kex` |
| `2026-06-14 15:57:11` | `cowrie.login.success` |
| `2026-06-14 15:57:13` | `cowrie.session.file_upload` |
| `2026-06-14 15:57:14` | `cowrie.session.params` |
| `2026-06-14 15:57:14` | `cowrie.command.input` |
| `2026-06-14 15:57:14` | `cowrie.command.input` |
| `2026-06-14 15:57:14` | `cowrie.command.input` |
| `2026-06-14 15:57:14` | `cowrie.command.failed` |
| `2026-06-14 15:57:15` | `cowrie.log.closed` |
| `2026-06-14 15:57:16` | `cowrie.session.params` |
| `2026-06-14 15:57:16` | `cowrie.command.input` |
| `2026-06-14 15:57:16` | `cowrie.log.closed` |
| `2026-06-14 15:57:17` | `cowrie.session.params` |
| `2026-06-14 15:57:17` | `cowrie.command.input` |
| `2026-06-14 15:57:18` | `cowrie.log.closed` |
| `2026-06-14 15:57:19` | `cowrie.session.params` |
| `2026-06-14 15:57:19` | `cowrie.command.input` |
| `2026-06-14 15:57:19` | `cowrie.command.failed` |
| `2026-06-14 15:57:19` | `cowrie.command.failed` |
| `2026-06-14 15:58:20` | `cowrie.session.params` |
| `2026-06-14 15:58:20` | `cowrie.command.input` |
| `2026-06-14 15:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b4ff35ecb7e

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-14 15:59 |
| **Last Seen** | 2026-06-14 16:01 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 15:59:38` | `cowrie.session.connect` |
| `2026-06-14 15:59:38` | `cowrie.client.version` |
| `2026-06-14 15:59:38` | `cowrie.client.kex` |
| `2026-06-14 15:59:39` | `cowrie.login.success` |
| `2026-06-14 15:59:42` | `cowrie.session.file_upload` |
| `2026-06-14 15:59:43` | `cowrie.session.params` |
| `2026-06-14 15:59:43` | `cowrie.command.input` |
| `2026-06-14 15:59:43` | `cowrie.command.input` |
| `2026-06-14 15:59:43` | `cowrie.command.input` |
| `2026-06-14 15:59:43` | `cowrie.command.failed` |
| `2026-06-14 15:59:43` | `cowrie.log.closed` |
| `2026-06-14 15:59:44` | `cowrie.session.params` |
| `2026-06-14 15:59:44` | `cowrie.command.input` |
| `2026-06-14 15:59:44` | `cowrie.log.closed` |
| `2026-06-14 15:59:45` | `cowrie.session.params` |
| `2026-06-14 15:59:45` | `cowrie.command.input` |
| `2026-06-14 15:59:46` | `cowrie.log.closed` |
| `2026-06-14 15:59:47` | `cowrie.session.params` |
| `2026-06-14 15:59:47` | `cowrie.command.input` |
| `2026-06-14 15:59:47` | `cowrie.command.failed` |
| `2026-06-14 15:59:47` | `cowrie.command.failed` |
| `2026-06-14 16:00:48` | `cowrie.session.params` |
| `2026-06-14 16:00:48` | `cowrie.command.input` |
| `2026-06-14 16:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059a0f95ed56

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 16:20 |
| **Last Seen** | 2026-06-14 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:20:20` | `cowrie.session.connect` |
| `2026-06-14 16:20:20` | `cowrie.client.version` |
| `2026-06-14 16:20:20` | `cowrie.client.kex` |
| `2026-06-14 16:20:20` | `cowrie.login.success` |
| `2026-06-14 16:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb0da935937

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 16:20 |
| **Last Seen** | 2026-06-14 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:20:20` | `cowrie.session.connect` |
| `2026-06-14 16:20:20` | `cowrie.client.version` |
| `2026-06-14 16:20:20` | `cowrie.client.kex` |
| `2026-06-14 16:20:20` | `cowrie.login.success` |
| `2026-06-14 16:20:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e24bfe1a173

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 16:20 |
| **Last Seen** | 2026-06-14 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:20:25` | `cowrie.session.connect` |
| `2026-06-14 16:20:25` | `cowrie.client.version` |
| `2026-06-14 16:20:25` | `cowrie.client.kex` |
| `2026-06-14 16:20:26` | `cowrie.login.success` |
| `2026-06-14 16:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13eac14f619

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-14 16:20 |
| **Last Seen** | 2026-06-14 16:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:20:26` | `cowrie.session.connect` |
| `2026-06-14 16:20:26` | `cowrie.client.version` |
| `2026-06-14 16:20:26` | `cowrie.client.kex` |
| `2026-06-14 16:20:26` | `cowrie.login.success` |
| `2026-06-14 16:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca887f719b10

| Field | Detail |
|---|---|
| **Source IP** | `168.156.171[.]11` |
| **First Seen** | 2026-06-14 16:46 |
| **Last Seen** | 2026-06-14 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:46:49` | `cowrie.session.connect` |
| `2026-06-14 16:46:49` | `cowrie.client.version` |
| `2026-06-14 16:46:49` | `cowrie.client.kex` |
| `2026-06-14 16:46:50` | `cowrie.login.success` |
| `2026-06-14 16:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.156.171[.]11` to AbuseIPDB if not already reported
- [ ] Block `168.156.171[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80852fcca77f

| Field | Detail |
|---|---|
| **Source IP** | `168.156.171[.]11` |
| **First Seen** | 2026-06-14 16:46 |
| **Last Seen** | 2026-06-14 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:46:49` | `cowrie.session.connect` |
| `2026-06-14 16:46:49` | `cowrie.client.version` |
| `2026-06-14 16:46:49` | `cowrie.client.kex` |
| `2026-06-14 16:46:50` | `cowrie.login.success` |
| `2026-06-14 16:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.156.171[.]11` to AbuseIPDB if not already reported
- [ ] Block `168.156.171[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7763d96ebf

| Field | Detail |
|---|---|
| **Source IP** | `168.156.171[.]11` |
| **First Seen** | 2026-06-14 16:47 |
| **Last Seen** | 2026-06-14 16:49 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:47:13` | `cowrie.session.connect` |
| `2026-06-14 16:47:13` | `cowrie.client.version` |
| `2026-06-14 16:47:13` | `cowrie.client.kex` |
| `2026-06-14 16:47:13` | `cowrie.login.success` |
| `2026-06-14 16:47:15` | `cowrie.session.file_upload` |
| `2026-06-14 16:47:15` | `cowrie.session.params` |
| `2026-06-14 16:47:15` | `cowrie.command.input` |
| `2026-06-14 16:47:15` | `cowrie.command.input` |
| `2026-06-14 16:47:15` | `cowrie.command.input` |
| `2026-06-14 16:47:15` | `cowrie.command.failed` |
| `2026-06-14 16:47:15` | `cowrie.log.closed` |
| `2026-06-14 16:47:16` | `cowrie.session.params` |
| `2026-06-14 16:47:16` | `cowrie.command.input` |
| `2026-06-14 16:47:16` | `cowrie.log.closed` |
| `2026-06-14 16:47:17` | `cowrie.session.params` |
| `2026-06-14 16:47:17` | `cowrie.command.input` |
| `2026-06-14 16:47:17` | `cowrie.log.closed` |
| `2026-06-14 16:47:18` | `cowrie.session.params` |
| `2026-06-14 16:47:18` | `cowrie.command.input` |
| `2026-06-14 16:47:18` | `cowrie.command.failed` |
| `2026-06-14 16:47:18` | `cowrie.command.failed` |
| `2026-06-14 16:48:19` | `cowrie.session.params` |
| `2026-06-14 16:48:19` | `cowrie.command.input` |
| `2026-06-14 16:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.156.171[.]11` to AbuseIPDB if not already reported
- [ ] Block `168.156.171[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3f6ac08fb1

| Field | Detail |
|---|---|
| **Source IP** | `168.156.171[.]11` |
| **First Seen** | 2026-06-14 16:49 |
| **Last Seen** | 2026-06-14 16:51 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:49:34` | `cowrie.session.connect` |
| `2026-06-14 16:49:35` | `cowrie.client.version` |
| `2026-06-14 16:49:35` | `cowrie.client.kex` |
| `2026-06-14 16:49:35` | `cowrie.login.success` |
| `2026-06-14 16:49:36` | `cowrie.session.file_upload` |
| `2026-06-14 16:49:37` | `cowrie.session.params` |
| `2026-06-14 16:49:37` | `cowrie.command.input` |
| `2026-06-14 16:49:37` | `cowrie.command.input` |
| `2026-06-14 16:49:37` | `cowrie.command.input` |
| `2026-06-14 16:49:37` | `cowrie.command.failed` |
| `2026-06-14 16:49:37` | `cowrie.log.closed` |
| `2026-06-14 16:49:38` | `cowrie.session.params` |
| `2026-06-14 16:49:38` | `cowrie.command.input` |
| `2026-06-14 16:49:38` | `cowrie.log.closed` |
| `2026-06-14 16:49:38` | `cowrie.session.params` |
| `2026-06-14 16:49:38` | `cowrie.command.input` |
| `2026-06-14 16:49:38` | `cowrie.log.closed` |
| `2026-06-14 16:49:39` | `cowrie.session.params` |
| `2026-06-14 16:49:39` | `cowrie.command.input` |
| `2026-06-14 16:49:39` | `cowrie.command.failed` |
| `2026-06-14 16:49:39` | `cowrie.command.failed` |
| `2026-06-14 16:50:40` | `cowrie.session.params` |
| `2026-06-14 16:50:40` | `cowrie.command.input` |
| `2026-06-14 16:51:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.156.171[.]11` to AbuseIPDB if not already reported
- [ ] Block `168.156.171[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e27045b988

| Field | Detail |
|---|---|
| **Source IP** | `5.175.169[.]118` |
| **First Seen** | 2026-06-14 16:54 |
| **Last Seen** | 2026-06-14 16:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:54:24` | `cowrie.session.connect` |
| `2026-06-14 16:54:24` | `cowrie.client.version` |
| `2026-06-14 16:54:24` | `cowrie.client.kex` |
| `2026-06-14 16:54:25` | `cowrie.login.success` |
| `2026-06-14 16:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.175.169[.]118` to AbuseIPDB if not already reported
- [ ] Block `5.175.169[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d622652db7e3

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-14 16:54 |
| **Last Seen** | 2026-06-14 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 16:54:25` | `cowrie.session.connect` |
| `2026-06-14 16:54:25` | `cowrie.client.version` |
| `2026-06-14 16:54:25` | `cowrie.client.kex` |
| `2026-06-14 16:54:25` | `cowrie.login.success` |
| `2026-06-14 16:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.166.223[.]22` | **12** | 2026-06-14 14:59 | 2026-06-14 16:45 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **5** | 2026-06-14 14:55 | 2026-06-14 16:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **5** | 2026-06-14 15:04 | 2026-06-14 16:17 | 4m | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]161` | **2** | 2026-06-14 16:35 | 2026-06-14 16:37 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.163.26[.]91` | **2** | 2026-06-14 16:51 | 2026-06-14 16:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `69.11.71[.]166` | **2** | 2026-06-14 15:15 | 2026-06-14 15:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.93[.]206` | 1 | 2026-06-14 15:23 | 2026-06-14 15:23 | 5s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-06-14 16:23 | 2026-06-14 16:24 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-06-14 15:24 | 2026-06-14 15:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `172.81.62[.]90` | 1 | 2026-06-14 16:12 | 2026-06-14 16:13 | 38s | 0 | `T1592` | 🟢 LOW |
| `177.130.50[.]21` | 1 | 2026-06-14 16:11 | 2026-06-14 16:11 | 29s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-14 16:09 | 2026-06-14 16:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-14 16:22 | 2026-06-14 16:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]119` | 1 | 2026-06-14 16:34 | 2026-06-14 16:34 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 3 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 2 |
| `168.156.171[.]11` | US | Washington State Board for Community & Technical Colleges | **100** ⚠️ | 2 |
| `172.81.62[.]90` | US | Dynu Systems Incorporated | **100** ⚠️ | 8 |
| `40.233.83[.]131` | CA | Oracle Corporation | **100** ⚠️ | 2 |
| `69.11.71[.]166` | CA | SaskTel Wide Area Network Engineering Center | **100** ⚠️ | 2 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 26 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 73 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (15.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 26 priority case(s) shown individually · 14 recon entry/entries in table (6 group(s) consolidating 28 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `Aegispub/thir-ha · Oracle Cloud HA_  
_Report time: 2026-06-14T17:23:38Z_

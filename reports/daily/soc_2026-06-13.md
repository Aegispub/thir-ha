# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T17:26:51Z |
| **Shift Time** | 17:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **164** |
| Confirmed Threats | **151** |
| False Positives Filtered | **13** (7.9%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **13** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **140** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **3** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `admin` | 5 |
| `1234` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 8 |
| `LeitboGi0ro` | 7 |
| `123@@@` | 5 |
| `admin` | 5 |
| `smo@@kkklss` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 8 |
| `root` | `LeitboGi0ro` | 7 |
| `root` | `123@@@` | 5 |
| `admin` | `admin` | 5 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@@@` | `129.153.145.135` | 2026-06-13T13:08:05 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-13T13:08:06 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-13T13:19:21 |
| `1234` | `1234` | `176.65.139.130` | 2026-06-13T13:24:50 |
| `root` | `---fuck_you----` | `101.126.4.215` | 2026-06-13T13:40:58 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-13T13:54:23 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-13T13:54:23 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-13T13:57:15 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-13T14:10:55 |
| `admin` | `admin` | `47.79.37.117` | 2026-06-13T14:24:09 |
| `admin` | `admin` | `43.110.37.217` | 2026-06-13T14:51:14 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-13T14:51:15 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-13T15:03:40 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-13T15:03:41 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-13T16:35:53 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-13T16:35:53 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-13T16:36:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **164** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 18 |
| Paramiko (Python) | 16 |
| libssh | 4 |
| PuTTY | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 16 | 4 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 4 | 1 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |
| `5bd26477da54...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 16 | 4 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `5bd26477da54...` | PuTTY | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **23** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS132124` | Information and Communication Technology Agency of Sri Lanka | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bf2fb29b9631

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 13:08 |
| **Last Seen** | 2026-06-13 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:08:05` | `cowrie.session.connect` |
| `2026-06-13 13:08:05` | `cowrie.client.version` |
| `2026-06-13 13:08:05` | `cowrie.client.kex` |
| `2026-06-13 13:08:05` | `cowrie.login.success` |
| `2026-06-13 13:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261b126cc2d6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 13:08 |
| **Last Seen** | 2026-06-13 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:08:05` | `cowrie.session.connect` |
| `2026-06-13 13:08:05` | `cowrie.client.version` |
| `2026-06-13 13:08:05` | `cowrie.client.kex` |
| `2026-06-13 13:08:06` | `cowrie.login.success` |
| `2026-06-13 13:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02969b952eb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-13 13:24 |
| **Last Seen** | 2026-06-13 13:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:24:44` | `cowrie.session.connect` |
| `2026-06-13 13:24:45` | `cowrie.client.version` |
| `2026-06-13 13:24:45` | `cowrie.client.kex` |
| `2026-06-13 13:24:50` | `cowrie.login.success` |
| `2026-06-13 13:24:51` | `cowrie.direct-tcpip.request` |
| `2026-06-13 13:24:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-13 13:24:53` | `cowrie.direct-tcpip.data` |
| `2026-06-13 13:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30980ef63985

| Field | Detail |
|---|---|
| **Source IP** | `101.126.4[.]215` |
| **First Seen** | 2026-06-13 13:40 |
| **Last Seen** | 2026-06-13 13:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:40:57` | `cowrie.session.connect` |
| `2026-06-13 13:40:57` | `cowrie.client.version` |
| `2026-06-13 13:40:58` | `cowrie.client.kex` |
| `2026-06-13 13:40:58` | `cowrie.login.success` |
| `2026-06-13 13:41:00` | `cowrie.session.params` |
| `2026-06-13 13:41:00` | `cowrie.command.input` |
| `2026-06-13 13:41:00` | `cowrie.log.closed` |
| `2026-06-13 13:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.4[.]215` to AbuseIPDB if not already reported
- [ ] Block `101.126.4[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67cab968aaed

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 13:54 |
| **Last Seen** | 2026-06-13 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:54:21` | `cowrie.session.connect` |
| `2026-06-13 13:54:21` | `cowrie.client.version` |
| `2026-06-13 13:54:22` | `cowrie.client.kex` |
| `2026-06-13 13:54:23` | `cowrie.login.success` |
| `2026-06-13 13:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964f3fc72dcd

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 13:54 |
| **Last Seen** | 2026-06-13 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:54:22` | `cowrie.session.connect` |
| `2026-06-13 13:54:22` | `cowrie.client.version` |
| `2026-06-13 13:54:22` | `cowrie.client.kex` |
| `2026-06-13 13:54:23` | `cowrie.login.success` |
| `2026-06-13 13:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3185ef42f5f0

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 13:54 |
| **Last Seen** | 2026-06-13 13:56 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:54:45` | `cowrie.session.connect` |
| `2026-06-13 13:54:45` | `cowrie.client.version` |
| `2026-06-13 13:54:45` | `cowrie.client.kex` |
| `2026-06-13 13:54:46` | `cowrie.login.success` |
| `2026-06-13 13:54:48` | `cowrie.session.file_upload` |
| `2026-06-13 13:54:50` | `cowrie.session.params` |
| `2026-06-13 13:54:50` | `cowrie.command.input` |
| `2026-06-13 13:54:50` | `cowrie.command.input` |
| `2026-06-13 13:54:50` | `cowrie.command.input` |
| `2026-06-13 13:54:50` | `cowrie.command.failed` |
| `2026-06-13 13:54:50` | `cowrie.log.closed` |
| `2026-06-13 13:54:51` | `cowrie.session.params` |
| `2026-06-13 13:54:51` | `cowrie.command.input` |
| `2026-06-13 13:54:51` | `cowrie.log.closed` |
| `2026-06-13 13:54:52` | `cowrie.session.params` |
| `2026-06-13 13:54:52` | `cowrie.command.input` |
| `2026-06-13 13:54:53` | `cowrie.log.closed` |
| `2026-06-13 13:54:54` | `cowrie.session.params` |
| `2026-06-13 13:54:54` | `cowrie.command.input` |
| `2026-06-13 13:54:54` | `cowrie.command.failed` |
| `2026-06-13 13:54:54` | `cowrie.command.failed` |
| `2026-06-13 13:55:55` | `cowrie.session.params` |
| `2026-06-13 13:55:55` | `cowrie.command.input` |
| `2026-06-13 13:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e1812b4b9a3

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-13 13:57 |
| **Last Seen** | 2026-06-13 13:59 |
| **Session Duration** | 133s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 13:57:11` | `cowrie.session.connect` |
| `2026-06-13 13:57:11` | `cowrie.client.version` |
| `2026-06-13 13:57:12` | `cowrie.client.kex` |
| `2026-06-13 13:57:13` | `cowrie.login.success` |
| `2026-06-13 13:57:15` | `cowrie.session.file_upload` |
| `2026-06-13 13:57:16` | `cowrie.session.params` |
| `2026-06-13 13:57:16` | `cowrie.command.input` |
| `2026-06-13 13:57:16` | `cowrie.command.input` |
| `2026-06-13 13:57:16` | `cowrie.command.input` |
| `2026-06-13 13:57:16` | `cowrie.command.failed` |
| `2026-06-13 13:57:17` | `cowrie.log.closed` |
| `2026-06-13 13:57:18` | `cowrie.session.params` |
| `2026-06-13 13:57:18` | `cowrie.command.input` |
| `2026-06-13 13:57:18` | `cowrie.log.closed` |
| `2026-06-13 13:57:19` | `cowrie.session.params` |
| `2026-06-13 13:57:19` | `cowrie.command.input` |
| `2026-06-13 13:57:20` | `cowrie.log.closed` |
| `2026-06-13 13:57:21` | `cowrie.session.params` |
| `2026-06-13 13:57:21` | `cowrie.command.input` |
| `2026-06-13 13:57:21` | `cowrie.command.failed` |
| `2026-06-13 13:57:21` | `cowrie.command.failed` |
| `2026-06-13 13:58:22` | `cowrie.session.params` |
| `2026-06-13 13:58:22` | `cowrie.command.input` |
| `2026-06-13 13:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f98e6e7fcc11

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 14:10 |
| **Last Seen** | 2026-06-13 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:10:54` | `cowrie.session.connect` |
| `2026-06-13 14:10:54` | `cowrie.client.version` |
| `2026-06-13 14:10:54` | `cowrie.client.kex` |
| `2026-06-13 14:10:55` | `cowrie.login.success` |
| `2026-06-13 14:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-994d5b79d0d3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 14:10 |
| **Last Seen** | 2026-06-13 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:10:55` | `cowrie.session.connect` |
| `2026-06-13 14:10:55` | `cowrie.client.version` |
| `2026-06-13 14:10:55` | `cowrie.client.kex` |
| `2026-06-13 14:10:55` | `cowrie.login.success` |
| `2026-06-13 14:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95ed6009c24

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 14:10 |
| **Last Seen** | 2026-06-13 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:10:55` | `cowrie.session.connect` |
| `2026-06-13 14:10:55` | `cowrie.client.version` |
| `2026-06-13 14:10:55` | `cowrie.client.kex` |
| `2026-06-13 14:10:55` | `cowrie.login.success` |
| `2026-06-13 14:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a7255408f00

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-13 14:10 |
| **Last Seen** | 2026-06-13 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:10:55` | `cowrie.session.connect` |
| `2026-06-13 14:10:55` | `cowrie.client.version` |
| `2026-06-13 14:10:55` | `cowrie.client.kex` |
| `2026-06-13 14:10:55` | `cowrie.login.success` |
| `2026-06-13 14:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cfdca5fc48b

| Field | Detail |
|---|---|
| **Source IP** | `47.79.37[.]117` |
| **First Seen** | 2026-06-13 14:23 |
| **Last Seen** | 2026-06-13 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:23:07` | `cowrie.session.connect` |
| `2026-06-13 14:23:08` | `cowrie.telnet.option` |
| `2026-06-13 14:23:09` | `cowrie.telnet.option` |
| `2026-06-13 14:24:09` | `cowrie.login.success` |
| `2026-06-13 14:24:10` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.79.37[.]117` to AbuseIPDB if not already reported
- [ ] Block `47.79.37[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160ff7d59324

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-06-13 14:51 |
| **Last Seen** | 2026-06-13 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:51:14` | `cowrie.session.connect` |
| `2026-06-13 14:51:14` | `cowrie.client.version` |
| `2026-06-13 14:51:14` | `cowrie.client.kex` |
| `2026-06-13 14:51:14` | `cowrie.login.success` |
| `2026-06-13 14:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fdf6d7ba195

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-13 14:51 |
| **Last Seen** | 2026-06-13 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 14:51:15` | `cowrie.session.connect` |
| `2026-06-13 14:51:15` | `cowrie.client.version` |
| `2026-06-13 14:51:15` | `cowrie.client.kex` |
| `2026-06-13 14:51:15` | `cowrie.login.success` |
| `2026-06-13 14:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9bd98040ecc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-13 15:03 |
| **Last Seen** | 2026-06-13 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:03:39` | `cowrie.session.connect` |
| `2026-06-13 15:03:39` | `cowrie.client.version` |
| `2026-06-13 15:03:39` | `cowrie.client.kex` |
| `2026-06-13 15:03:40` | `cowrie.login.success` |
| `2026-06-13 15:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164266465b7e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-13 15:03 |
| **Last Seen** | 2026-06-13 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 15:03:40` | `cowrie.session.connect` |
| `2026-06-13 15:03:40` | `cowrie.client.version` |
| `2026-06-13 15:03:40` | `cowrie.client.kex` |
| `2026-06-13 15:03:41` | `cowrie.login.success` |
| `2026-06-13 15:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088ca2e93843

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-13 16:35 |
| **Last Seen** | 2026-06-13 16:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:35:52` | `cowrie.session.connect` |
| `2026-06-13 16:35:52` | `cowrie.client.version` |
| `2026-06-13 16:35:52` | `cowrie.client.kex` |
| `2026-06-13 16:35:53` | `cowrie.login.success` |
| `2026-06-13 16:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d088950db8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-13 16:35 |
| **Last Seen** | 2026-06-13 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:35:53` | `cowrie.session.connect` |
| `2026-06-13 16:35:53` | `cowrie.client.version` |
| `2026-06-13 16:35:53` | `cowrie.client.kex` |
| `2026-06-13 16:35:53` | `cowrie.login.success` |
| `2026-06-13 16:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e518ddf7fbb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-13 16:36 |
| **Last Seen** | 2026-06-13 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:36:03` | `cowrie.session.connect` |
| `2026-06-13 16:36:03` | `cowrie.client.version` |
| `2026-06-13 16:36:03` | `cowrie.client.kex` |
| `2026-06-13 16:36:04` | `cowrie.login.success` |
| `2026-06-13 16:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5f84677b01

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-13 16:36 |
| **Last Seen** | 2026-06-13 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 16:36:04` | `cowrie.session.connect` |
| `2026-06-13 16:36:04` | `cowrie.client.version` |
| `2026-06-13 16:36:04` | `cowrie.client.kex` |
| `2026-06-13 16:36:05` | `cowrie.login.success` |
| `2026-06-13 16:36:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `154.16.146[.]65` | **64** | 2026-06-13 12:57 | 2026-06-13 16:51 | 41m | 0 | `T1592` | 🟠 MEDIUM |
| `188.166.223[.]22` | **31** | 2026-06-13 12:55 | 2026-06-13 16:52 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **4** | 2026-06-13 13:36 | 2026-06-13 16:36 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.228[.]229` | **3** | 2026-06-13 14:34 | 2026-06-13 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]39` | **3** | 2026-06-13 13:43 | 2026-06-13 13:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.121[.]200` | **2** | 2026-06-13 14:38 | 2026-06-13 14:40 | 4m | 0 | `T1592` | 🟢 LOW |
| `117.50.218[.]37` | **2** | 2026-06-13 15:13 | 2026-06-13 15:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `43.224.126[.]107` | **2** | 2026-06-13 14:31 | 2026-06-13 15:22 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.126.4[.]215` | 1 | 2026-06-13 13:40 | 2026-06-13 13:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.245.138[.]229` | 1 | 2026-06-13 15:41 | 2026-06-13 15:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `134.209.93[.]206` | 1 | 2026-06-13 14:51 | 2026-06-13 14:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-13 16:13 | 2026-06-13 16:14 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-06-13 16:04 | 2026-06-13 16:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `188.214.144[.]172` | 1 | 2026-06-13 15:51 | 2026-06-13 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-06-13 16:21 | 2026-06-13 16:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.15.246[.]7` | 1 | 2026-06-13 16:23 | 2026-06-13 16:25 | 124s | 0 | `T1592` | 🟢 LOW |
| `36.49.40[.]185` | 1 | 2026-06-13 14:55 | 2026-06-13 14:56 | 31s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-06-13 13:07 | 2026-06-13 13:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-13 16:08 | 2026-06-13 16:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-13 15:35 | 2026-06-13 15:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-06-13 14:34 | 2026-06-13 14:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `58.253.129[.]91` | 1 | 2026-06-13 15:12 | 2026-06-13 15:12 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-13 13:37 | 2026-06-13 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]132` | 1 | 2026-06-13 15:32 | 2026-06-13 15:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-13 13:37 | 2026-06-13 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.219.249[.]135` | 1 | 2026-06-13 13:48 | 2026-06-13 13:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]121` | 1 | 2026-06-13 13:36 | 2026-06-13 13:36 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `154.16.146[.]65` | US | OC1-HostForWeb, LLC | **100** ⚠️ | 2 |
| `117.245.138[.]229` | IN | BSNL GSM North Zone, O/o Sr GM (CMTS), NC, Chandigarh | **100** ⚠️ | 0 |
| `188.166.223[.]22` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `176.65.139[.]130` | NL | Storm Industries | **100** ⚠️ | 50 |
| `138.2.98[.]41` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `172.236.228[.]229` | US | Linode | **100** ⚠️ | 50 |
| `134.209.93[.]206` | NL | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `106.13.121[.]200` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 42 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 164 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 27 recon entry/entries in table (8 group(s) consolidating 111 session(s)).

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
_Report time: 2026-06-13T17:26:51Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-08 |
| **Generated At** | 2026-06-08T18:32:50Z |
| **Shift Time** | 18:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **160** |
| Confirmed Threats | **149** |
| False Positives Filtered | **11** (6.9%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **8** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **145** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **6** |
| Unique Usernames | **2** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 5 |
| `123@@@` | 3 |
| `smo@@kkklss` | 2 |
| `admin` | 2 |
| `ubuntu` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `root` | `123@@@` | 3 |
| `root` | `smo@@kkklss` | 2 |
| `admin` | `admin` | 2 |
| `root` | `ubuntu` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-08T15:14:50 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-08T15:14:51 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-08T15:14:58 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-08T15:26:56 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-08T15:26:56 |
| `root` | `` | `176.65.139.174` | 2026-06-08T16:12:04 |
| `admin` | `admin` | `147.139.136.75` | 2026-06-08T16:12:44 |
| `admin` | `admin` | `176.65.139.130` | 2026-06-08T16:22:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-08T16:34:27 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-08T16:34:28 |
| `root` | `ubuntu` | `43.226.38.130` | 2026-06-08T16:38:52 |
| `root` | `ubuntu` | `36.103.204.54` | 2026-06-08T16:47:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **160** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 10 |
| Go SSH scanner | 6 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 2 | 2 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `4c20a8895324...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `95420f9d932d...` | Go SSH scanner | 3 | 2 | — |
| `98ddc5604ef6...` | Go SSH scanner | 2 | 2 | Modern SSH client |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `4c20a8895324...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **14** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS214472` | Offshore LC | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS134762` | CHINANET Liaoning province Dalian MAN network | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS134761` | CHINANET NINGXIA province ZHONGWEI IDC network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-580021104eea

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-08 15:14 |
| **Last Seen** | 2026-06-08 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:14:50` | `cowrie.session.connect` |
| `2026-06-08 15:14:50` | `cowrie.client.version` |
| `2026-06-08 15:14:50` | `cowrie.client.kex` |
| `2026-06-08 15:14:50` | `cowrie.login.success` |
| `2026-06-08 15:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7af49a43a1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-08 15:14 |
| **Last Seen** | 2026-06-08 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:14:50` | `cowrie.session.connect` |
| `2026-06-08 15:14:51` | `cowrie.client.version` |
| `2026-06-08 15:14:51` | `cowrie.client.kex` |
| `2026-06-08 15:14:51` | `cowrie.login.success` |
| `2026-06-08 15:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a55295250a9e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-08 15:14 |
| **Last Seen** | 2026-06-08 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:14:58` | `cowrie.session.connect` |
| `2026-06-08 15:14:58` | `cowrie.client.version` |
| `2026-06-08 15:14:58` | `cowrie.client.kex` |
| `2026-06-08 15:14:58` | `cowrie.login.success` |
| `2026-06-08 15:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498c4d6cb17a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-08 15:14 |
| **Last Seen** | 2026-06-08 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:14:58` | `cowrie.session.connect` |
| `2026-06-08 15:14:58` | `cowrie.client.version` |
| `2026-06-08 15:14:58` | `cowrie.client.kex` |
| `2026-06-08 15:14:58` | `cowrie.login.success` |
| `2026-06-08 15:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f65730ae19

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-08 15:26 |
| **Last Seen** | 2026-06-08 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:26:55` | `cowrie.session.connect` |
| `2026-06-08 15:26:55` | `cowrie.client.version` |
| `2026-06-08 15:26:55` | `cowrie.client.kex` |
| `2026-06-08 15:26:56` | `cowrie.login.success` |
| `2026-06-08 15:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339d655b4f2d

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-08 15:26 |
| **Last Seen** | 2026-06-08 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:26:56` | `cowrie.session.connect` |
| `2026-06-08 15:26:56` | `cowrie.client.version` |
| `2026-06-08 15:26:56` | `cowrie.client.kex` |
| `2026-06-08 15:26:56` | `cowrie.login.success` |
| `2026-06-08 15:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3bbb9aa77e

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-08 15:27 |
| **Last Seen** | 2026-06-08 15:29 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:27:21` | `cowrie.session.connect` |
| `2026-06-08 15:27:21` | `cowrie.client.version` |
| `2026-06-08 15:27:21` | `cowrie.client.kex` |
| `2026-06-08 15:27:21` | `cowrie.login.success` |
| `2026-06-08 15:27:23` | `cowrie.session.file_upload` |
| `2026-06-08 15:27:23` | `cowrie.session.params` |
| `2026-06-08 15:27:23` | `cowrie.command.input` |
| `2026-06-08 15:27:23` | `cowrie.command.input` |
| `2026-06-08 15:27:23` | `cowrie.command.input` |
| `2026-06-08 15:27:23` | `cowrie.command.failed` |
| `2026-06-08 15:27:23` | `cowrie.log.closed` |
| `2026-06-08 15:27:24` | `cowrie.session.params` |
| `2026-06-08 15:27:24` | `cowrie.command.input` |
| `2026-06-08 15:27:24` | `cowrie.log.closed` |
| `2026-06-08 15:27:25` | `cowrie.session.params` |
| `2026-06-08 15:27:25` | `cowrie.command.input` |
| `2026-06-08 15:27:25` | `cowrie.log.closed` |
| `2026-06-08 15:27:26` | `cowrie.session.params` |
| `2026-06-08 15:27:26` | `cowrie.command.input` |
| `2026-06-08 15:27:26` | `cowrie.command.failed` |
| `2026-06-08 15:27:26` | `cowrie.command.failed` |
| `2026-06-08 15:28:27` | `cowrie.session.params` |
| `2026-06-08 15:28:27` | `cowrie.command.input` |
| `2026-06-08 15:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff649ff2904

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-08 15:29 |
| **Last Seen** | 2026-06-08 15:32 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:29:53` | `cowrie.session.connect` |
| `2026-06-08 15:29:53` | `cowrie.client.version` |
| `2026-06-08 15:29:53` | `cowrie.client.kex` |
| `2026-06-08 15:29:53` | `cowrie.login.success` |
| `2026-06-08 15:29:55` | `cowrie.session.file_upload` |
| `2026-06-08 15:29:55` | `cowrie.session.params` |
| `2026-06-08 15:29:55` | `cowrie.command.input` |
| `2026-06-08 15:29:55` | `cowrie.command.input` |
| `2026-06-08 15:29:55` | `cowrie.command.input` |
| `2026-06-08 15:29:55` | `cowrie.command.failed` |
| `2026-06-08 15:29:56` | `cowrie.log.closed` |
| `2026-06-08 15:29:56` | `cowrie.session.params` |
| `2026-06-08 15:29:56` | `cowrie.command.input` |
| `2026-06-08 15:29:56` | `cowrie.log.closed` |
| `2026-06-08 15:29:57` | `cowrie.session.params` |
| `2026-06-08 15:29:57` | `cowrie.command.input` |
| `2026-06-08 15:29:57` | `cowrie.log.closed` |
| `2026-06-08 15:29:58` | `cowrie.session.params` |
| `2026-06-08 15:29:58` | `cowrie.command.input` |
| `2026-06-08 15:29:58` | `cowrie.command.failed` |
| `2026-06-08 15:29:58` | `cowrie.command.failed` |
| `2026-06-08 15:30:59` | `cowrie.session.params` |
| `2026-06-08 15:30:59` | `cowrie.command.input` |
| `2026-06-08 15:32:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d279b61e57ff

| Field | Detail |
|---|---|
| **Source IP** | `147.139.136[.]75` |
| **First Seen** | 2026-06-08 16:11 |
| **Last Seen** | 2026-06-08 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:11:43` | `cowrie.session.connect` |
| `2026-06-08 16:11:44` | `cowrie.telnet.option` |
| `2026-06-08 16:11:44` | `cowrie.telnet.option` |
| `2026-06-08 16:12:44` | `cowrie.login.success` |
| `2026-06-08 16:12:45` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `147.139.136[.]75` to AbuseIPDB if not already reported
- [ ] Block `147.139.136[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cb1ba94a08

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]174` |
| **First Seen** | 2026-06-08 16:12 |
| **Last Seen** | 2026-06-08 16:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:12:04` | `cowrie.session.connect` |
| `2026-06-08 16:12:04` | `cowrie.login.success` |
| `2026-06-08 16:12:05` | `cowrie.session.params` |
| `2026-06-08 16:12:05` | `cowrie.command.input` |
| `2026-06-08 16:12:06` | `cowrie.command.input` |
| `2026-06-08 16:12:07` | `cowrie.command.input` |
| `2026-06-08 16:12:08` | `cowrie.command.input` |
| `2026-06-08 16:12:08` | `cowrie.command.failed` |
| `2026-06-08 16:12:09` | `cowrie.log.closed` |
| `2026-06-08 16:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]174` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed3c3c1f2b9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]130` |
| **First Seen** | 2026-06-08 16:22 |
| **Last Seen** | 2026-06-08 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:22:17` | `cowrie.session.connect` |
| `2026-06-08 16:22:17` | `cowrie.client.version` |
| `2026-06-08 16:22:17` | `cowrie.client.kex` |
| `2026-06-08 16:22:17` | `cowrie.login.success` |
| `2026-06-08 16:22:17` | `cowrie.direct-tcpip.request` |
| `2026-06-08 16:22:17` | `cowrie.direct-tcpip.ja4` |
| `2026-06-08 16:22:17` | `cowrie.direct-tcpip.data` |
| `2026-06-08 16:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]130` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211e089d37ad

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-08 16:34 |
| **Last Seen** | 2026-06-08 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:34:26` | `cowrie.session.connect` |
| `2026-06-08 16:34:26` | `cowrie.client.version` |
| `2026-06-08 16:34:27` | `cowrie.client.kex` |
| `2026-06-08 16:34:27` | `cowrie.login.success` |
| `2026-06-08 16:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3b11e43ad0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-08 16:34 |
| **Last Seen** | 2026-06-08 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:34:27` | `cowrie.session.connect` |
| `2026-06-08 16:34:27` | `cowrie.client.version` |
| `2026-06-08 16:34:27` | `cowrie.client.kex` |
| `2026-06-08 16:34:28` | `cowrie.login.success` |
| `2026-06-08 16:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4273d7ee57

| Field | Detail |
|---|---|
| **Source IP** | `43.226.38[.]130` |
| **First Seen** | 2026-06-08 16:38 |
| **Last Seen** | 2026-06-08 16:43 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:38:48` | `cowrie.session.connect` |
| `2026-06-08 16:38:49` | `cowrie.client.version` |
| `2026-06-08 16:38:49` | `cowrie.client.kex` |
| `2026-06-08 16:38:52` | `cowrie.login.success` |
| `2026-06-08 16:43:52` | `cowrie.session.file_upload` |
| `2026-06-08 16:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.226.38[.]130` to AbuseIPDB if not already reported
- [ ] Block `43.226.38[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01a75421921d

| Field | Detail |
|---|---|
| **Source IP** | `36.103.204[.]54` |
| **First Seen** | 2026-06-08 16:47 |
| **Last Seen** | 2026-06-08 16:49 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 16:47:40` | `cowrie.session.connect` |
| `2026-06-08 16:47:40` | `cowrie.client.version` |
| `2026-06-08 16:47:40` | `cowrie.client.kex` |
| `2026-06-08 16:47:41` | `cowrie.login.success` |
| `2026-06-08 16:49:06` | `cowrie.session.file_upload` |
| `2026-06-08 16:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.103.204[.]54` to AbuseIPDB if not already reported
- [ ] Block `36.103.204[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **121** | 2026-06-08 14:55 | 2026-06-08 16:54 | 67m | 0 | `T1592` | 🟠 MEDIUM |
| `107.174.155[.]67` | **5** | 2026-06-08 15:02 | 2026-06-08 16:25 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.14.81[.]42` | **2** | 2026-06-08 15:07 | 2026-06-08 15:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-08 16:40 | 2026-06-08 16:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]174` | 1 | 2026-06-08 16:12 | 2026-06-08 16:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-08 16:06 | 2026-06-08 16:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.79.20[.]59` | 1 | 2026-06-08 16:34 | 2026-06-08 16:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.231.70[.]13` | 1 | 2026-06-08 15:57 | 2026-06-08 15:57 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `107.174.155[.]67` | US | sally wang | **100** ⚠️ | 0 |
| `43.226.38[.]130` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 1 |
| `5.231.70[.]13` | DE | Myps | **100** ⚠️ | 3 |
| `176.65.139[.]174` | NL | Storm Industries | **100** ⚠️ | 29 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `47.79.20[.]59` | HK | Alibaba Cloud LLC | **100** ⚠️ | 19 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `20.14.81[.]42` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `176.65.139[.]130` | NL | Storm Industries | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 6 |
| AbuseIPDB score 21 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 160 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (6.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 8 recon entry/entries in table (4 group(s) consolidating 130 session(s)).

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
_Report time: 2026-06-08T18:32:50Z_

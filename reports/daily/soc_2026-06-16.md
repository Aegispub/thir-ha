# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-16 |
| **Generated At** | 2026-06-16T23:26:24Z |
| **Shift Time** | 23:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **89** |
| Confirmed Threats | **50** |
| False Positives Filtered | **39** (43.8%) |
| Unique Attacker IPs | **67** |
| Countries of Origin | **16** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **79** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **3** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `pi` | 1 |
| `vyatta` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 3 |
| `123@@@` | 2 |
| `vyatta` | 2 |
| `prIN6262@ce` | 1 |
| `raspberry` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 3 |
| `root` | `123@@@` | 2 |
| `root` | `prIN6262@ce` | 1 |
| `pi` | `raspberry` | 1 |
| `root` | `vyatta` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-16T20:57:41 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-16T20:57:47 |
| `root` | `prIN6262@ce` | `185.93.89.95` | 2026-06-16T21:15:20 |
| `pi` | `raspberry` | `185.93.89.95` | 2026-06-16T21:47:08 |
| `root` | `vyatta` | `185.93.89.95` | 2026-06-16T22:19:05 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-16T22:35:43 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-16T22:35:43 |
| `root` | `ubuntu` | `58.23.69.251` | 2026-06-16T22:49:10 |
| `vyatta` | `vyatta` | `185.93.89.95` | 2026-06-16T22:51:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **89** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 8 |
| Paramiko (Python) | 5 |
| libssh | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 5 | 2 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `e37f354a101a...` | Mirai/variant | 2 | 2 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 5 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `e37f354a101a...` | libssh | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **67** |
| Unique ASNs | **47** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 8 | HIGH |
| `AS16509` | Amazon.com, Inc. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS40065` | CNSERVERS LLC | 3 | MEDIUM |
| `AS35916` | MULTACOM CORPORATION | 2 | HIGH |
| `AS43515` | Google Ireland Limited | 2 | HIGH |
| `AS54801` | Zillion Network Inc. | 2 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4678dc42e6c8

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-16 20:57 |
| **Last Seen** | 2026-06-16 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 20:57:41` | `cowrie.session.connect` |
| `2026-06-16 20:57:41` | `cowrie.client.version` |
| `2026-06-16 20:57:41` | `cowrie.client.kex` |
| `2026-06-16 20:57:41` | `cowrie.login.success` |
| `2026-06-16 20:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f7012b403a5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-16 20:57 |
| **Last Seen** | 2026-06-16 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 20:57:47` | `cowrie.session.connect` |
| `2026-06-16 20:57:47` | `cowrie.client.version` |
| `2026-06-16 20:57:47` | `cowrie.client.kex` |
| `2026-06-16 20:57:47` | `cowrie.login.success` |
| `2026-06-16 20:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e325c0101f

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-16 20:58 |
| **Last Seen** | 2026-06-16 21:00 |
| **Session Duration** | 127s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 20:58:36` | `cowrie.session.connect` |
| `2026-06-16 20:58:36` | `cowrie.client.version` |
| `2026-06-16 20:58:36` | `cowrie.client.kex` |
| `2026-06-16 20:58:36` | `cowrie.login.success` |
| `2026-06-16 20:58:37` | `cowrie.session.file_upload` |
| `2026-06-16 20:58:38` | `cowrie.session.params` |
| `2026-06-16 20:58:38` | `cowrie.command.input` |
| `2026-06-16 20:58:38` | `cowrie.command.input` |
| `2026-06-16 20:58:38` | `cowrie.command.input` |
| `2026-06-16 20:58:38` | `cowrie.command.failed` |
| `2026-06-16 20:58:38` | `cowrie.log.closed` |
| `2026-06-16 20:58:39` | `cowrie.session.params` |
| `2026-06-16 20:58:39` | `cowrie.command.input` |
| `2026-06-16 20:58:39` | `cowrie.log.closed` |
| `2026-06-16 20:58:39` | `cowrie.session.params` |
| `2026-06-16 20:58:39` | `cowrie.command.input` |
| `2026-06-16 20:58:39` | `cowrie.log.closed` |
| `2026-06-16 20:58:40` | `cowrie.session.params` |
| `2026-06-16 20:58:40` | `cowrie.command.input` |
| `2026-06-16 20:58:40` | `cowrie.command.failed` |
| `2026-06-16 20:58:40` | `cowrie.command.failed` |
| `2026-06-16 20:59:41` | `cowrie.session.params` |
| `2026-06-16 20:59:41` | `cowrie.command.input` |
| `2026-06-16 21:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b523d020fe

| Field | Detail |
|---|---|
| **Source IP** | `185.93.89[.]95` |
| **First Seen** | 2026-06-16 21:15 |
| **Last Seen** | 2026-06-16 21:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;w` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 21:15:19` | `cowrie.session.connect` |
| `2026-06-16 21:15:19` | `cowrie.client.version` |
| `2026-06-16 21:15:19` | `cowrie.client.kex` |
| `2026-06-16 21:15:20` | `cowrie.login.success` |
| `2026-06-16 21:15:21` | `cowrie.session.params` |
| `2026-06-16 21:15:21` | `cowrie.command.input` |
| `2026-06-16 21:15:21` | `cowrie.log.closed` |
| `2026-06-16 21:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.93.89[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.93.89[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5ca0479386

| Field | Detail |
|---|---|
| **Source IP** | `185.93.89[.]95` |
| **First Seen** | 2026-06-16 21:47 |
| **Last Seen** | 2026-06-16 21:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;w` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 21:47:07` | `cowrie.session.connect` |
| `2026-06-16 21:47:07` | `cowrie.client.version` |
| `2026-06-16 21:47:08` | `cowrie.client.kex` |
| `2026-06-16 21:47:08` | `cowrie.login.success` |
| `2026-06-16 21:47:09` | `cowrie.session.params` |
| `2026-06-16 21:47:09` | `cowrie.command.input` |
| `2026-06-16 21:47:10` | `cowrie.log.closed` |
| `2026-06-16 21:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.93.89[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.93.89[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55d4f0f523e4

| Field | Detail |
|---|---|
| **Source IP** | `185.93.89[.]95` |
| **First Seen** | 2026-06-16 22:19 |
| **Last Seen** | 2026-06-16 22:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;w` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:19:04` | `cowrie.session.connect` |
| `2026-06-16 22:19:04` | `cowrie.client.version` |
| `2026-06-16 22:19:05` | `cowrie.client.kex` |
| `2026-06-16 22:19:05` | `cowrie.login.success` |
| `2026-06-16 22:19:06` | `cowrie.session.params` |
| `2026-06-16 22:19:06` | `cowrie.command.input` |
| `2026-06-16 22:19:07` | `cowrie.log.closed` |
| `2026-06-16 22:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.93.89[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.93.89[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11aa8622c349

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-16 22:35 |
| **Last Seen** | 2026-06-16 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:35:42` | `cowrie.session.connect` |
| `2026-06-16 22:35:42` | `cowrie.client.version` |
| `2026-06-16 22:35:42` | `cowrie.client.kex` |
| `2026-06-16 22:35:43` | `cowrie.login.success` |
| `2026-06-16 22:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e840a554519

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-16 22:35 |
| **Last Seen** | 2026-06-16 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:35:42` | `cowrie.session.connect` |
| `2026-06-16 22:35:42` | `cowrie.client.version` |
| `2026-06-16 22:35:42` | `cowrie.client.kex` |
| `2026-06-16 22:35:43` | `cowrie.login.success` |
| `2026-06-16 22:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a76d874a697

| Field | Detail |
|---|---|
| **Source IP** | `58.23.69[.]251` |
| **First Seen** | 2026-06-16 22:49 |
| **Last Seen** | 2026-06-16 22:50 |
| **Session Duration** | 74s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:49:09` | `cowrie.session.connect` |
| `2026-06-16 22:49:09` | `cowrie.client.version` |
| `2026-06-16 22:49:09` | `cowrie.client.kex` |
| `2026-06-16 22:49:10` | `cowrie.login.success` |
| `2026-06-16 22:50:23` | `cowrie.session.file_upload` |
| `2026-06-16 22:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.23.69[.]251` to AbuseIPDB if not already reported
- [ ] Block `58.23.69[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf6fb54fef3

| Field | Detail |
|---|---|
| **Source IP** | `185.93.89[.]95` |
| **First Seen** | 2026-06-16 22:51 |
| **Last Seen** | 2026-06-16 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a;w` |
| **TTPs (MITRE)** | T1057 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 22:51:08` | `cowrie.session.connect` |
| `2026-06-16 22:51:08` | `cowrie.client.version` |
| `2026-06-16 22:51:08` | `cowrie.client.kex` |
| `2026-06-16 22:51:08` | `cowrie.login.success` |
| `2026-06-16 22:51:09` | `cowrie.session.params` |
| `2026-06-16 22:51:09` | `cowrie.command.input` |
| `2026-06-16 22:51:09` | `cowrie.log.closed` |
| `2026-06-16 22:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.93.89[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.93.89[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `188.166.223[.]22` | **11** | 2026-06-16 21:04 | 2026-06-16 22:11 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `192.155.90[.]220` | **3** | 2026-06-16 21:36 | 2026-06-16 21:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.42.204[.]29` | **2** | 2026-06-16 21:59 | 2026-06-16 21:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.91.31[.]94` | 1 | 2026-06-16 21:28 | 2026-06-16 21:29 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.28.135[.]84` | 1 | 2026-06-16 21:29 | 2026-06-16 21:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `122.200.86[.]145` | 1 | 2026-06-16 20:58 | 2026-06-16 20:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `140.238.180[.]92` | 1 | 2026-06-16 22:27 | 2026-06-16 22:27 | 31s | 0 | `T1592` | 🟢 LOW |
| `144.24.90[.]1` | 1 | 2026-06-16 22:09 | 2026-06-16 22:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `156.251.176[.]28` | 1 | 2026-06-16 22:27 | 2026-06-16 22:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `16.162.188[.]118` | 1 | 2026-06-16 21:22 | 2026-06-16 21:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `163.47.43[.]17` | 1 | 2026-06-16 21:41 | 2026-06-16 21:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `18.162.112[.]209` | 1 | 2026-06-16 21:22 | 2026-06-16 21:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `185.194.143[.]239` | 1 | 2026-06-16 21:53 | 2026-06-16 21:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `190.115.189[.]194` | 1 | 2026-06-16 22:39 | 2026-06-16 22:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]199` | 1 | 2026-06-16 22:47 | 2026-06-16 22:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `202.73.4[.]102` | 1 | 2026-06-16 21:23 | 2026-06-16 21:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `202.95.14[.]10` | 1 | 2026-06-16 21:23 | 2026-06-16 21:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.141.52[.]222` | 1 | 2026-06-16 22:17 | 2026-06-16 22:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `31.59.129[.]147` | 1 | 2026-06-16 22:09 | 2026-06-16 22:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.209.18[.]80` | 1 | 2026-06-16 21:19 | 2026-06-16 21:20 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.212.190[.]168` | 1 | 2026-06-16 21:04 | 2026-06-16 21:04 | 34s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-06-16 22:10 | 2026-06-16 22:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-16 21:35 | 2026-06-16 21:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `5.181.48[.]45` | 1 | 2026-06-16 22:31 | 2026-06-16 22:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.23.69[.]251` | 1 | 2026-06-16 22:03 | 2026-06-16 22:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `82.40.35[.]179` | 1 | 2026-06-16 20:57 | 2026-06-16 20:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-06-16 22:45 | 2026-06-16 22:45 | 29s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (17 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `195.96.139[.]199` | GB | Driftnet Ltd | **100** ⚠️ | 5 |
| `202.73.4[.]102` | HK | ACCESSTEL-ISP | **100** ⚠️ | 0 |
| `45.33.12[.]122` | US | Linode | **100** ⚠️ | 50 |
| `16.162.188[.]118` | HK | Amazon Data Services Hong Kong | **100** ⚠️ | 0 |
| `35.209.18[.]80` | US | Google LLC | **100** ⚠️ | 1 |
| `58.23.69[.]251` | CN | Quanzhou city, fujian provincial network of CNCGROUP | **100** ⚠️ | 19 |
| `190.115.189[.]194` | HT | Télécommunications de Haití (Teleco) | **100** ⚠️ | 9 |
| `5.181.48[.]45` | DE | netcup GmbH | **100** ⚠️ | 0 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `85.217.149[.]20` | CA | NL MODAT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (39 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 32 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 89 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 67 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 39 filtered (43.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 27 recon entry/entries in table (3 group(s) consolidating 16 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

## 🛡️ CIS Controls Snapshot

| Control | Name | Status | Evidence |
|---|---|---|---|
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 |
| CIS-2 | Software Inventory | MONITORING | tool_manifest.yaml tracks pipeline tools |
| CIS-3 | Data Protection | ACTIVE | R2 archive encrypted at rest — thirha-raw-archive |
| CIS-4 | Secure Configuration | ACTIVE | haproxy.cfg, cowrie.cfg, VCN rules in config/ |
| CIS-5 | Account Management | ACTIVE | Two key pairs, dedicated cowrie user, no shared credentials |
| CIS-6 | Access Control | ACTIVE | Pipeline key vs personal key separation, GitHub Secrets |
| CIS-7 | Vulnerability Management | MONITORING | Oracle security patches — pending regular cadence |
| CIS-8 | Audit Log Management | ACTIVE | cowrie.json + cowrie.log dual streams, 59-day corpus |
| CIS-9 | Email/Web Protection | PLANNED | cloudflared tunnels planned — direct IP exposure currently |
| CIS-10 | Malware Defence | ACTIVE | Tool 31 malware analysis + Tool 33 YARA classification |
| CIS-11 | Data Recovery | ACTIVE | R2 archive, EBS snapshots, runbook recovery procedures |
| CIS-12 | Network Infrastructure | ACTIVE | VCN private networking, HAProxy TCP LB, Cloudflare DNS |

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `Aegispub/thir-ha · Oracle Cloud HA_  
_Report time: 2026-06-16T23:26:24Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-19 |
| **Generated At** | 2026-06-19T23:02:16Z |
| **Shift Time** | 23:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **652** |
| Confirmed Threats | **622** |
| False Positives Filtered | **30** (4.6%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **14** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **623** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **9** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **23** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `admin` | 5 |
| `ubuntu` | 3 |
| `GET / HTTP/1.1` | 1 |
| `hostmaster` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 6 |
| `LeitboGi0ro` | 4 |
| `123@@@` | 2 |
| `smo@@kkklss` | 2 |
| `123qweasd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 5 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 2 |
| `root` | `smo@@kkklss` | 2 |
| `root` | `123qweasd` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123qweasd` | `45.198.224.120` | 2026-06-19T21:01:56 |
| `root` | `epf6QxCw2K` | `10.0.0.73` | 2026-06-19T21:05:19 |
| `root` | `Oracle123!@#` | `45.198.224.120` | 2026-06-19T21:09:37 |
| `root` | `123@@@` | `137.131.9.65` | 2026-06-19T21:10:42 |
| `root` | `LeitboGi0ro` | `137.131.9.65` | 2026-06-19T21:10:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.133.199` | 2026-06-19T21:14:33 |
| `root` | `pass7` | `45.198.224.120` | 2026-06-19T21:17:38 |
| `root` | `admin` | `185.220.101.97` | 2026-06-19T21:28:58 |
| `ubuntu` | `111111111` | `45.198.224.120` | 2026-06-19T21:33:23 |
| `ubuntu` | `zaq1@WSX` | `45.198.224.120` | 2026-06-19T21:41:38 |
| `root` | `qazxcvbnm` | `45.198.224.120` | 2026-06-19T21:49:37 |
| `hostmaster` | `hostmaster` | `45.198.224.120` | 2026-06-19T21:57:21 |
| `root` | `ubuntu` | `5.202.4.64` | 2026-06-19T22:01:33 |
| `postgres` | `postgres` | `45.198.224.120` | 2026-06-19T22:05:15 |
| `ubuntu` | `user12345678` | `45.198.224.120` | 2026-06-19T22:12:39 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-19T22:15:51 |
| `chris` | `chris` | `45.198.224.120` | 2026-06-19T22:28:47 |
| `www-data` | `1q2w3e` | `45.198.224.120` | 2026-06-19T22:36:40 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-19T22:40:04 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-19T22:40:05 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-19T22:40:10 |
| `admin` | `admin` | `167.233.68.137` | 2026-06-19T22:45:11 |
| `atendimento` | `atendimento` | `45.198.224.120` | 2026-06-19T22:52:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **652** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 18 |
| libssh | 15 |
| Paramiko (Python) | 8 |
| Unknown | 3 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 12 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 13 | 4 | — |
| `16443846184e...` | Go SSH scanner | 12 | 1 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **20** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 8 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS0` |  | 1 | LOW |
| `AS45903` | CMC Telecom Infrastructure Company | 1 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 1 | HIGH |
| `AS4618` | Internet Thailand Company Limited | 1 | HIGH |
| `AS34918` | Pishgaman Toseeh Ertebatat Company (Private Joint Stock) | 1 | MEDIUM |
| `AS17858` | LG POWERCOMM | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-720aa4bf8c2a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:01 |
| **Last Seen** | 2026-06-19 21:02 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:01:36` | `cowrie.session.connect` |
| `2026-06-19 21:01:40` | `cowrie.client.version` |
| `2026-06-19 21:01:40` | `cowrie.client.kex` |
| `2026-06-19 21:01:56` | `cowrie.login.success` |
| `2026-06-19 21:02:08` | `cowrie.session.params` |
| `2026-06-19 21:02:08` | `cowrie.command.input` |
| `2026-06-19 21:02:11` | `cowrie.log.closed` |
| `2026-06-19 21:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36febc403406

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:09 |
| **Last Seen** | 2026-06-19 21:09 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:09:19` | `cowrie.session.connect` |
| `2026-06-19 21:09:23` | `cowrie.client.version` |
| `2026-06-19 21:09:23` | `cowrie.client.kex` |
| `2026-06-19 21:09:37` | `cowrie.login.success` |
| `2026-06-19 21:09:46` | `cowrie.session.params` |
| `2026-06-19 21:09:46` | `cowrie.command.input` |
| `2026-06-19 21:09:49` | `cowrie.log.closed` |
| `2026-06-19 21:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7dd5639da9

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-19 21:10 |
| **Last Seen** | 2026-06-19 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:10:41` | `cowrie.session.connect` |
| `2026-06-19 21:10:41` | `cowrie.client.version` |
| `2026-06-19 21:10:41` | `cowrie.client.kex` |
| `2026-06-19 21:10:42` | `cowrie.login.success` |
| `2026-06-19 21:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f199f3388e7

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-19 21:10 |
| **Last Seen** | 2026-06-19 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:10:54` | `cowrie.session.connect` |
| `2026-06-19 21:10:54` | `cowrie.client.version` |
| `2026-06-19 21:10:54` | `cowrie.client.kex` |
| `2026-06-19 21:10:54` | `cowrie.login.success` |
| `2026-06-19 21:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1c100f4be3

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-19 21:11 |
| **Last Seen** | 2026-06-19 21:13 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:11:02` | `cowrie.session.connect` |
| `2026-06-19 21:11:02` | `cowrie.client.version` |
| `2026-06-19 21:11:02` | `cowrie.client.kex` |
| `2026-06-19 21:11:03` | `cowrie.login.success` |
| `2026-06-19 21:11:04` | `cowrie.session.file_upload` |
| `2026-06-19 21:11:05` | `cowrie.session.params` |
| `2026-06-19 21:11:05` | `cowrie.command.input` |
| `2026-06-19 21:11:05` | `cowrie.command.input` |
| `2026-06-19 21:11:05` | `cowrie.command.input` |
| `2026-06-19 21:11:05` | `cowrie.command.failed` |
| `2026-06-19 21:11:05` | `cowrie.log.closed` |
| `2026-06-19 21:11:06` | `cowrie.session.params` |
| `2026-06-19 21:11:06` | `cowrie.command.input` |
| `2026-06-19 21:11:06` | `cowrie.log.closed` |
| `2026-06-19 21:11:07` | `cowrie.session.params` |
| `2026-06-19 21:11:07` | `cowrie.command.input` |
| `2026-06-19 21:11:07` | `cowrie.log.closed` |
| `2026-06-19 21:11:08` | `cowrie.session.params` |
| `2026-06-19 21:11:08` | `cowrie.command.input` |
| `2026-06-19 21:11:08` | `cowrie.command.failed` |
| `2026-06-19 21:11:08` | `cowrie.command.failed` |
| `2026-06-19 21:12:09` | `cowrie.session.params` |
| `2026-06-19 21:12:09` | `cowrie.command.input` |
| `2026-06-19 21:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296bc6679471

| Field | Detail |
|---|---|
| **Source IP** | `137.131.9[.]65` |
| **First Seen** | 2026-06-19 21:13 |
| **Last Seen** | 2026-06-19 21:16 |
| **Session Duration** | 137s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:13:45` | `cowrie.session.connect` |
| `2026-06-19 21:13:45` | `cowrie.client.version` |
| `2026-06-19 21:13:45` | `cowrie.client.kex` |
| `2026-06-19 21:13:45` | `cowrie.login.success` |
| `2026-06-19 21:13:46` | `cowrie.session.file_upload` |
| `2026-06-19 21:13:47` | `cowrie.session.params` |
| `2026-06-19 21:13:47` | `cowrie.command.input` |
| `2026-06-19 21:13:47` | `cowrie.command.input` |
| `2026-06-19 21:13:47` | `cowrie.command.input` |
| `2026-06-19 21:13:47` | `cowrie.command.failed` |
| `2026-06-19 21:13:47` | `cowrie.log.closed` |
| `2026-06-19 21:13:48` | `cowrie.session.params` |
| `2026-06-19 21:13:48` | `cowrie.command.input` |
| `2026-06-19 21:13:48` | `cowrie.log.closed` |
| `2026-06-19 21:13:49` | `cowrie.session.params` |
| `2026-06-19 21:13:49` | `cowrie.command.input` |
| `2026-06-19 21:13:49` | `cowrie.log.closed` |
| `2026-06-19 21:13:50` | `cowrie.session.params` |
| `2026-06-19 21:13:50` | `cowrie.command.input` |
| `2026-06-19 21:13:50` | `cowrie.command.failed` |
| `2026-06-19 21:13:50` | `cowrie.command.failed` |
| `2026-06-19 21:14:51` | `cowrie.session.params` |
| `2026-06-19 21:14:51` | `cowrie.command.input` |
| `2026-06-19 21:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `137.131.9[.]65` to AbuseIPDB if not already reported
- [ ] Block `137.131.9[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082a09dc7583

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:17 |
| **Last Seen** | 2026-06-19 21:17 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:17:19` | `cowrie.session.connect` |
| `2026-06-19 21:17:22` | `cowrie.client.version` |
| `2026-06-19 21:17:22` | `cowrie.client.kex` |
| `2026-06-19 21:17:38` | `cowrie.login.success` |
| `2026-06-19 21:17:49` | `cowrie.session.params` |
| `2026-06-19 21:17:49` | `cowrie.command.input` |
| `2026-06-19 21:17:52` | `cowrie.log.closed` |
| `2026-06-19 21:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a4d6014cf68

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]97` |
| **First Seen** | 2026-06-19 21:28 |
| **Last Seen** | 2026-06-19 21:29 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:28:56` | `cowrie.session.connect` |
| `2026-06-19 21:28:56` | `cowrie.client.version` |
| `2026-06-19 21:28:56` | `cowrie.client.kex` |
| `2026-06-19 21:28:58` | `cowrie.client.fingerprint` |
| `2026-06-19 21:28:58` | `cowrie.login.failed` |
| `2026-06-19 21:28:58` | `cowrie.login.success` |
| `2026-06-19 21:29:16` | `cowrie.direct-tcpip.request` |
| `2026-06-19 21:29:16` | `cowrie.direct-tcpip.ja4` |
| `2026-06-19 21:29:16` | `cowrie.direct-tcpip.data` |
| `2026-06-19 21:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]97` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372938119824

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:33 |
| **Last Seen** | 2026-06-19 21:33 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:33:03` | `cowrie.session.connect` |
| `2026-06-19 21:33:07` | `cowrie.client.version` |
| `2026-06-19 21:33:07` | `cowrie.client.kex` |
| `2026-06-19 21:33:23` | `cowrie.login.success` |
| `2026-06-19 21:33:33` | `cowrie.session.params` |
| `2026-06-19 21:33:33` | `cowrie.command.input` |
| `2026-06-19 21:33:36` | `cowrie.log.closed` |
| `2026-06-19 21:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4528ce1f8508

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:41 |
| **Last Seen** | 2026-06-19 21:41 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:41:14` | `cowrie.session.connect` |
| `2026-06-19 21:41:18` | `cowrie.client.version` |
| `2026-06-19 21:41:18` | `cowrie.client.kex` |
| `2026-06-19 21:41:38` | `cowrie.login.success` |
| `2026-06-19 21:41:47` | `cowrie.session.params` |
| `2026-06-19 21:41:47` | `cowrie.command.input` |
| `2026-06-19 21:41:53` | `cowrie.log.closed` |
| `2026-06-19 21:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dce24223656

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:49 |
| **Last Seen** | 2026-06-19 21:49 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:49:16` | `cowrie.session.connect` |
| `2026-06-19 21:49:20` | `cowrie.client.version` |
| `2026-06-19 21:49:20` | `cowrie.client.kex` |
| `2026-06-19 21:49:37` | `cowrie.login.success` |
| `2026-06-19 21:49:49` | `cowrie.session.params` |
| `2026-06-19 21:49:49` | `cowrie.command.input` |
| `2026-06-19 21:49:52` | `cowrie.log.closed` |
| `2026-06-19 21:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb708d37461

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 21:56 |
| **Last Seen** | 2026-06-19 21:57 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 21:56:57` | `cowrie.session.connect` |
| `2026-06-19 21:57:01` | `cowrie.client.version` |
| `2026-06-19 21:57:01` | `cowrie.client.kex` |
| `2026-06-19 21:57:21` | `cowrie.login.success` |
| `2026-06-19 21:57:31` | `cowrie.session.params` |
| `2026-06-19 21:57:31` | `cowrie.command.input` |
| `2026-06-19 21:57:35` | `cowrie.log.closed` |
| `2026-06-19 21:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fed1b312806

| Field | Detail |
|---|---|
| **Source IP** | `5.202.4[.]64` |
| **First Seen** | 2026-06-19 22:01 |
| **Last Seen** | 2026-06-19 22:06 |
| **Session Duration** | 311s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:01:21` | `cowrie.session.connect` |
| `2026-06-19 22:01:24` | `cowrie.client.version` |
| `2026-06-19 22:01:24` | `cowrie.client.kex` |
| `2026-06-19 22:01:33` | `cowrie.login.success` |
| `2026-06-19 22:06:33` | `cowrie.session.file_upload` |
| `2026-06-19 22:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.202.4[.]64` to AbuseIPDB if not already reported
- [ ] Block `5.202.4[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c14e973e36

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 22:04 |
| **Last Seen** | 2026-06-19 22:05 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:04:53` | `cowrie.session.connect` |
| `2026-06-19 22:04:56` | `cowrie.client.version` |
| `2026-06-19 22:04:56` | `cowrie.client.kex` |
| `2026-06-19 22:05:15` | `cowrie.login.success` |
| `2026-06-19 22:05:26` | `cowrie.session.params` |
| `2026-06-19 22:05:26` | `cowrie.command.input` |
| `2026-06-19 22:05:29` | `cowrie.log.closed` |
| `2026-06-19 22:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241b76e28648

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 22:12 |
| **Last Seen** | 2026-06-19 22:12 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:12:19` | `cowrie.session.connect` |
| `2026-06-19 22:12:22` | `cowrie.client.version` |
| `2026-06-19 22:12:22` | `cowrie.client.kex` |
| `2026-06-19 22:12:39` | `cowrie.login.success` |
| `2026-06-19 22:12:49` | `cowrie.session.params` |
| `2026-06-19 22:12:49` | `cowrie.command.input` |
| `2026-06-19 22:12:52` | `cowrie.log.closed` |
| `2026-06-19 22:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c88e99e1411

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 22:28 |
| **Last Seen** | 2026-06-19 22:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:28:27` | `cowrie.session.connect` |
| `2026-06-19 22:28:30` | `cowrie.client.version` |
| `2026-06-19 22:28:30` | `cowrie.client.kex` |
| `2026-06-19 22:28:47` | `cowrie.login.success` |
| `2026-06-19 22:28:57` | `cowrie.session.params` |
| `2026-06-19 22:28:57` | `cowrie.command.input` |
| `2026-06-19 22:29:00` | `cowrie.log.closed` |
| `2026-06-19 22:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a8528e67cb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 22:36 |
| **Last Seen** | 2026-06-19 22:36 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:36:15` | `cowrie.session.connect` |
| `2026-06-19 22:36:19` | `cowrie.client.version` |
| `2026-06-19 22:36:19` | `cowrie.client.kex` |
| `2026-06-19 22:36:40` | `cowrie.login.success` |
| `2026-06-19 22:36:50` | `cowrie.session.params` |
| `2026-06-19 22:36:50` | `cowrie.command.input` |
| `2026-06-19 22:36:54` | `cowrie.log.closed` |
| `2026-06-19 22:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df962ce66e27

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-19 22:40 |
| **Last Seen** | 2026-06-19 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:40:03` | `cowrie.session.connect` |
| `2026-06-19 22:40:03` | `cowrie.client.version` |
| `2026-06-19 22:40:03` | `cowrie.client.kex` |
| `2026-06-19 22:40:04` | `cowrie.login.success` |
| `2026-06-19 22:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25b8dd50ef4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-19 22:40 |
| **Last Seen** | 2026-06-19 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:40:04` | `cowrie.session.connect` |
| `2026-06-19 22:40:04` | `cowrie.client.version` |
| `2026-06-19 22:40:04` | `cowrie.client.kex` |
| `2026-06-19 22:40:05` | `cowrie.login.success` |
| `2026-06-19 22:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe88cfa0ea2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-19 22:40 |
| **Last Seen** | 2026-06-19 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:40:09` | `cowrie.session.connect` |
| `2026-06-19 22:40:09` | `cowrie.client.version` |
| `2026-06-19 22:40:09` | `cowrie.client.kex` |
| `2026-06-19 22:40:10` | `cowrie.login.success` |
| `2026-06-19 22:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bfeca6beecf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-19 22:40 |
| **Last Seen** | 2026-06-19 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:40:10` | `cowrie.session.connect` |
| `2026-06-19 22:40:10` | `cowrie.client.version` |
| `2026-06-19 22:40:10` | `cowrie.client.kex` |
| `2026-06-19 22:40:10` | `cowrie.login.success` |
| `2026-06-19 22:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c43eb9d67022

| Field | Detail |
|---|---|
| **Source IP** | `167.233.68[.]137` |
| **First Seen** | 2026-06-19 22:44 |
| **Last Seen** | 2026-06-19 22:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:44:10` | `cowrie.session.connect` |
| `2026-06-19 22:44:11` | `cowrie.telnet.option` |
| `2026-06-19 22:44:11` | `cowrie.telnet.option` |
| `2026-06-19 22:45:11` | `cowrie.login.success` |
| `2026-06-19 22:45:11` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `167.233.68[.]137` to AbuseIPDB if not already reported
- [ ] Block `167.233.68[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda437e7ffc8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-19 22:51 |
| **Last Seen** | 2026-06-19 22:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-19 22:51:47` | `cowrie.session.connect` |
| `2026-06-19 22:51:50` | `cowrie.client.version` |
| `2026-06-19 22:51:50` | `cowrie.client.kex` |
| `2026-06-19 22:52:13` | `cowrie.login.success` |
| `2026-06-19 22:52:21` | `cowrie.session.params` |
| `2026-06-19 22:52:21` | `cowrie.command.input` |
| `2026-06-19 22:52:25` | `cowrie.log.closed` |
| `2026-06-19 22:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.68.100[.]228` | **546** | 2026-06-19 20:55 | 2026-06-19 22:54 | 616m | 0 | `T1592` | 🟠 MEDIUM |
| `203.151.27[.]181` | **19** | 2026-06-19 22:06 | 2026-06-19 22:10 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `72.167.37[.]165` | **15** | 2026-06-19 20:55 | 2026-06-19 22:44 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.117[.]219` | **4** | 2026-06-19 21:32 | 2026-06-19 21:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.91.11[.]226` | **3** | 2026-06-19 21:58 | 2026-06-19 22:30 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | **3** | 2026-06-19 21:25 | 2026-06-19 22:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.166.64[.]94` | **3** | 2026-06-19 21:49 | 2026-06-19 21:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.116.247[.]163` | 1 | 2026-06-19 22:33 | 2026-06-19 22:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-06-19 22:50 | 2026-06-19 22:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.202.41[.]161` | 1 | 2026-06-19 21:06 | 2026-06-19 21:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-06-19 21:35 | 2026-06-19 21:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-19 22:22 | 2026-06-19 22:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-19 22:46 | 2026-06-19 22:46 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `122.202.41[.]161` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `49.166.64[.]94` | KR | LG POWERCOMM | **100** ⚠️ | 1 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 2 |
| `183.91.11[.]226` | VN | CMC Telecom Infrastructure Company | **100** ⚠️ | 4 |
| `103.116.247[.]163` | HK | I LAYER LIMITED | **100** ⚠️ | 1 |
| `137.131.9[.]65` | US | Oracle Corporation | **100** ⚠️ | 4 |
| `203.151.27[.]181` | TH | Internet Thailand Company Limited | **100** ⚠️ | 8 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 652 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (4.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 13 recon entry/entries in table (7 group(s) consolidating 593 session(s)).

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
_Report time: 2026-06-19T23:02:16Z_

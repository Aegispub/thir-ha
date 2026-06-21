# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-21 |
| **Generated At** | 2026-06-21T12:12:50Z |
| **Shift Time** | 12:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **92** |
| Confirmed Threats | **75** |
| False Positives Filtered | **17** (18.5%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **10** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **8** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `ubuntu` | 2 |
| `admin` | 2 |
| `telecomadmin` | 1 |
| `confluence4` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 4 |
| `123@@@` | 2 |
| `LeitboGi0ro` | 2 |
| `admin` | 2 |
| `Rcs_1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 4 |
| `root` | `123@@@` | 2 |
| `root` | `LeitboGi0ro` | 2 |
| `admin` | `admin` | 2 |
| `root` | `Rcs_1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Rcs_1234` | `45.198.224.120` | 2026-06-21T08:57:08 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-21T09:13:55 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-21T09:13:56 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-21T09:14:03 |
| `telecomadmin` | `admintelecom` | `195.178.110.42` | 2026-06-21T09:14:04 |
| `confluence4` | `confluence4` | `45.198.224.120` | 2026-06-21T09:21:35 |
| `vnc` | `123` | `45.198.224.120` | 2026-06-21T09:29:31 |
| `root` | `Pw$$w0rd` | `45.198.224.120` | 2026-06-21T09:37:57 |
| `root` | `202020` | `45.198.224.120` | 2026-06-21T09:46:12 |
| `test` | `shadow` | `45.198.224.120` | 2026-06-21T09:54:36 |
| `ubuntu` | `upload123456789` | `45.198.224.120` | 2026-06-21T10:02:40 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `47.88.6.39` | 2026-06-21T10:20:28 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-21T10:23:27 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-21T10:23:27 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-21T10:23:28 |
| `root` | `ROOT` | `45.198.224.120` | 2026-06-21T10:27:03 |
| `root` | `Ubuntu$Root1234!` | `45.198.224.120` | 2026-06-21T10:43:24 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-21T10:50:10 |
| `ubuntu` | `asdf123` | `45.198.224.120` | 2026-06-21T10:51:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **92** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 29 |
| Paramiko (Python) | 8 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 10 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Go SSH scanner | 15 | 5 | — |
| `16443846184e...` | Go SSH scanner | 10 | 1 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
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
Source IPs: `195.178.110.42`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS0` |  | 1 | LOW |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS4811` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1264b026633d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 08:56 |
| **Last Seen** | 2026-06-21 08:57 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 08:56:47` | `cowrie.session.connect` |
| `2026-06-21 08:56:51` | `cowrie.client.version` |
| `2026-06-21 08:56:51` | `cowrie.client.kex` |
| `2026-06-21 08:57:08` | `cowrie.login.success` |
| `2026-06-21 08:57:25` | `cowrie.session.params` |
| `2026-06-21 08:57:25` | `cowrie.command.input` |
| `2026-06-21 08:57:28` | `cowrie.log.closed` |
| `2026-06-21 08:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065698bfb429

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-21 09:13 |
| **Last Seen** | 2026-06-21 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:13:55` | `cowrie.session.connect` |
| `2026-06-21 09:13:55` | `cowrie.client.version` |
| `2026-06-21 09:13:55` | `cowrie.client.kex` |
| `2026-06-21 09:13:55` | `cowrie.login.success` |
| `2026-06-21 09:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b80d3691725

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-21 09:13 |
| **Last Seen** | 2026-06-21 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:13:55` | `cowrie.session.connect` |
| `2026-06-21 09:13:55` | `cowrie.client.version` |
| `2026-06-21 09:13:55` | `cowrie.client.kex` |
| `2026-06-21 09:13:56` | `cowrie.login.success` |
| `2026-06-21 09:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452289e8bdcf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]42` |
| **First Seen** | 2026-06-21 09:14 |
| **Last Seen** | 2026-06-21 09:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:14:00` | `cowrie.session.connect` |
| `2026-06-21 09:14:04` | `cowrie.login.success` |
| `2026-06-21 09:14:05` | `cowrie.session.params` |
| `2026-06-21 09:14:05` | `cowrie.command.input` |
| `2026-06-21 09:14:06` | `cowrie.command.input` |
| `2026-06-21 09:14:06` | `cowrie.command.input` |
| `2026-06-21 09:14:07` | `cowrie.command.input` |
| `2026-06-21 09:14:07` | `cowrie.command.failed` |
| `2026-06-21 09:14:07` | `cowrie.log.closed` |
| `2026-06-21 09:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]42` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dffc1bf385b9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-21 09:14 |
| **Last Seen** | 2026-06-21 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:14:02` | `cowrie.session.connect` |
| `2026-06-21 09:14:02` | `cowrie.client.version` |
| `2026-06-21 09:14:02` | `cowrie.client.kex` |
| `2026-06-21 09:14:03` | `cowrie.login.success` |
| `2026-06-21 09:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ab8bf08432d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-21 09:14 |
| **Last Seen** | 2026-06-21 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:14:03` | `cowrie.session.connect` |
| `2026-06-21 09:14:03` | `cowrie.client.version` |
| `2026-06-21 09:14:03` | `cowrie.client.kex` |
| `2026-06-21 09:14:04` | `cowrie.login.success` |
| `2026-06-21 09:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-397056f7f016

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 09:21 |
| **Last Seen** | 2026-06-21 09:21 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:21:17` | `cowrie.session.connect` |
| `2026-06-21 09:21:19` | `cowrie.client.version` |
| `2026-06-21 09:21:19` | `cowrie.client.kex` |
| `2026-06-21 09:21:35` | `cowrie.login.success` |
| `2026-06-21 09:21:44` | `cowrie.session.params` |
| `2026-06-21 09:21:44` | `cowrie.command.input` |
| `2026-06-21 09:21:47` | `cowrie.log.closed` |
| `2026-06-21 09:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d900bf9e573

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 09:29 |
| **Last Seen** | 2026-06-21 09:29 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:29:11` | `cowrie.session.connect` |
| `2026-06-21 09:29:14` | `cowrie.client.version` |
| `2026-06-21 09:29:14` | `cowrie.client.kex` |
| `2026-06-21 09:29:31` | `cowrie.login.success` |
| `2026-06-21 09:29:41` | `cowrie.session.params` |
| `2026-06-21 09:29:41` | `cowrie.command.input` |
| `2026-06-21 09:29:44` | `cowrie.log.closed` |
| `2026-06-21 09:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb83c35f5dba

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 09:37 |
| **Last Seen** | 2026-06-21 09:38 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:37:36` | `cowrie.session.connect` |
| `2026-06-21 09:37:39` | `cowrie.client.version` |
| `2026-06-21 09:37:39` | `cowrie.client.kex` |
| `2026-06-21 09:37:57` | `cowrie.login.success` |
| `2026-06-21 09:38:05` | `cowrie.session.params` |
| `2026-06-21 09:38:05` | `cowrie.command.input` |
| `2026-06-21 09:38:10` | `cowrie.log.closed` |
| `2026-06-21 09:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869c2715cdf7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 09:45 |
| **Last Seen** | 2026-06-21 09:46 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:45:54` | `cowrie.session.connect` |
| `2026-06-21 09:45:57` | `cowrie.client.version` |
| `2026-06-21 09:45:57` | `cowrie.client.kex` |
| `2026-06-21 09:46:12` | `cowrie.login.success` |
| `2026-06-21 09:46:22` | `cowrie.session.params` |
| `2026-06-21 09:46:22` | `cowrie.command.input` |
| `2026-06-21 09:46:25` | `cowrie.log.closed` |
| `2026-06-21 09:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a944e6cb034d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 09:54 |
| **Last Seen** | 2026-06-21 09:54 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 09:54:16` | `cowrie.session.connect` |
| `2026-06-21 09:54:20` | `cowrie.client.version` |
| `2026-06-21 09:54:20` | `cowrie.client.kex` |
| `2026-06-21 09:54:36` | `cowrie.login.success` |
| `2026-06-21 09:54:44` | `cowrie.session.params` |
| `2026-06-21 09:54:44` | `cowrie.command.input` |
| `2026-06-21 09:54:49` | `cowrie.log.closed` |
| `2026-06-21 09:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88e0294a4c1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 10:02 |
| **Last Seen** | 2026-06-21 10:02 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:02:19` | `cowrie.session.connect` |
| `2026-06-21 10:02:23` | `cowrie.client.version` |
| `2026-06-21 10:02:23` | `cowrie.client.kex` |
| `2026-06-21 10:02:40` | `cowrie.login.success` |
| `2026-06-21 10:02:54` | `cowrie.session.params` |
| `2026-06-21 10:02:54` | `cowrie.command.input` |
| `2026-06-21 10:02:59` | `cowrie.log.closed` |
| `2026-06-21 10:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639bdea7e24f

| Field | Detail |
|---|---|
| **Source IP** | `47.88.6[.]39` |
| **First Seen** | 2026-06-21 10:20 |
| **Last Seen** | 2026-06-21 10:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:20:28` | `cowrie.session.connect` |
| `2026-06-21 10:20:28` | `cowrie.login.success` |
| `2026-06-21 10:20:29` | `cowrie.session.params` |
| `2026-06-21 10:20:29` | `cowrie.command.input` |
| `2026-06-21 10:20:29` | `cowrie.command.failed` |
| `2026-06-21 10:20:29` | `cowrie.command.input` |
| `2026-06-21 10:20:29` | `cowrie.command.failed` |
| `2026-06-21 10:20:29` | `cowrie.command.input` |
| `2026-06-21 10:20:31` | `cowrie.log.closed` |
| `2026-06-21 10:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.88.6[.]39` to AbuseIPDB if not already reported
- [ ] Block `47.88.6[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0bb0ccac7b4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-21 10:23 |
| **Last Seen** | 2026-06-21 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:23:27` | `cowrie.session.connect` |
| `2026-06-21 10:23:27` | `cowrie.client.version` |
| `2026-06-21 10:23:27` | `cowrie.client.kex` |
| `2026-06-21 10:23:27` | `cowrie.login.success` |
| `2026-06-21 10:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b577e0864995

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-21 10:23 |
| **Last Seen** | 2026-06-21 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:23:27` | `cowrie.session.connect` |
| `2026-06-21 10:23:27` | `cowrie.client.version` |
| `2026-06-21 10:23:27` | `cowrie.client.kex` |
| `2026-06-21 10:23:27` | `cowrie.login.success` |
| `2026-06-21 10:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb99d45c80b9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-21 10:23 |
| **Last Seen** | 2026-06-21 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:23:28` | `cowrie.session.connect` |
| `2026-06-21 10:23:28` | `cowrie.client.version` |
| `2026-06-21 10:23:28` | `cowrie.client.kex` |
| `2026-06-21 10:23:28` | `cowrie.login.success` |
| `2026-06-21 10:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e11ed383c5e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-21 10:23 |
| **Last Seen** | 2026-06-21 10:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:23:28` | `cowrie.session.connect` |
| `2026-06-21 10:23:28` | `cowrie.client.version` |
| `2026-06-21 10:23:28` | `cowrie.client.kex` |
| `2026-06-21 10:23:28` | `cowrie.login.success` |
| `2026-06-21 10:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f861a9251a3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 10:26 |
| **Last Seen** | 2026-06-21 10:27 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:26:37` | `cowrie.session.connect` |
| `2026-06-21 10:26:40` | `cowrie.client.version` |
| `2026-06-21 10:26:40` | `cowrie.client.kex` |
| `2026-06-21 10:27:03` | `cowrie.login.success` |
| `2026-06-21 10:27:11` | `cowrie.session.params` |
| `2026-06-21 10:27:11` | `cowrie.command.input` |
| `2026-06-21 10:27:16` | `cowrie.log.closed` |
| `2026-06-21 10:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9497c65e71a2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 10:43 |
| **Last Seen** | 2026-06-21 10:43 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:43:04` | `cowrie.session.connect` |
| `2026-06-21 10:43:07` | `cowrie.client.version` |
| `2026-06-21 10:43:07` | `cowrie.client.kex` |
| `2026-06-21 10:43:24` | `cowrie.login.success` |
| `2026-06-21 10:43:32` | `cowrie.session.params` |
| `2026-06-21 10:43:32` | `cowrie.command.input` |
| `2026-06-21 10:43:37` | `cowrie.log.closed` |
| `2026-06-21 10:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dbcfef4cbd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-21 10:50 |
| **Last Seen** | 2026-06-21 10:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:50:10` | `cowrie.session.connect` |
| `2026-06-21 10:50:10` | `cowrie.client.version` |
| `2026-06-21 10:50:10` | `cowrie.client.kex` |
| `2026-06-21 10:50:10` | `cowrie.login.success` |
| `2026-06-21 10:50:10` | `cowrie.direct-tcpip.request` |
| `2026-06-21 10:50:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-21 10:50:10` | `cowrie.direct-tcpip.data` |
| `2026-06-21 10:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1beeb99686fa

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-21 10:50 |
| **Last Seen** | 2026-06-21 10:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:50:10` | `cowrie.session.connect` |
| `2026-06-21 10:50:10` | `cowrie.client.version` |
| `2026-06-21 10:50:10` | `cowrie.client.kex` |
| `2026-06-21 10:50:11` | `cowrie.login.success` |
| `2026-06-21 10:50:11` | `cowrie.direct-tcpip.request` |
| `2026-06-21 10:50:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-21 10:50:11` | `cowrie.direct-tcpip.data` |
| `2026-06-21 10:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef919007f9a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-21 10:51 |
| **Last Seen** | 2026-06-21 10:51 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-21 10:51:20` | `cowrie.session.connect` |
| `2026-06-21 10:51:24` | `cowrie.client.version` |
| `2026-06-21 10:51:24` | `cowrie.client.kex` |
| `2026-06-21 10:51:43` | `cowrie.login.success` |
| `2026-06-21 10:51:52` | `cowrie.session.params` |
| `2026-06-21 10:51:52` | `cowrie.command.input` |
| `2026-06-21 10:51:57` | `cowrie.log.closed` |
| `2026-06-21 10:51:57` | `cowrie.session.closed` |

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
| `69.11.71[.]166` | **18** | 2026-06-21 08:59 | 2026-06-21 10:44 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `195.178.110[.]42` | **10** | 2026-06-21 09:13 | 2026-06-21 09:14 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `45.198.224[.]120` | **5** | 2026-06-21 09:04 | 2026-06-21 10:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `138.68.100[.]228` | **3** | 2026-06-21 09:15 | 2026-06-21 10:47 | 4m | 0 | `T1592` | 🟢 LOW |
| `47.88.6[.]39` | **3** | 2026-06-21 10:20 | 2026-06-21 10:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.15[.]218` | **2** | 2026-06-21 10:24 | 2026-06-21 10:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-06-21 10:05 | 2026-06-21 10:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.41.186[.]9` | **2** | 2026-06-21 10:02 | 2026-06-21 10:04 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-21 10:32 | 2026-06-21 10:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-06-21 09:41 | 2026-06-21 09:45 | 3m | 0 | `T1592` | 🟢 LOW |
| `14.103.230[.]55` | 1 | 2026-06-21 10:35 | 2026-06-21 10:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-06-21 09:07 | 2026-06-21 09:07 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-21 10:05 | 2026-06-21 10:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.231.149[.]154` | 1 | 2026-06-21 09:00 | 2026-06-21 09:01 | 31s | 0 | `T1592` | 🟢 LOW |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `47.88.6[.]39` | US | Alibaba Cloud - US | **100** ⚠️ | 25 |
| `69.11.71[.]166` | CA | SaskTel Wide Area Network Engineering Center | **100** ⚠️ | 2 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 3 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `49.231.149[.]154` | TH | Khaosod | **100** ⚠️ | 5 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `14.103.230[.]55` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 24 |
| `20.163.15[.]218` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `195.178.110[.]42` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 47 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 40 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 92 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 14 recon entry/entries in table (10 group(s) consolidating 49 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json auto-generated from pipeline.yml each run |
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
_Report time: 2026-06-21T12:12:50Z_

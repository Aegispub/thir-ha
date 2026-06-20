# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T19:43:09Z |
| **Shift Time** | 19:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **230** |
| Confirmed Threats | **217** |
| False Positives Filtered | **13** (5.7%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **9** |
| High Severity Cases | **30** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **200** |
| Malware Samples Analyzed | **1** HIGH · **15** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **7** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **28** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `admin` | 2 |
| `dongshuowu` | 1 |
| `solor` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `smo@@kkklss` | 4 |
| `123@@@` | 3 |
| `LeitboGi0ro` | 3 |
| `admin` | 2 |
| `p@ssw0rd123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `smo@@kkklss` | 4 |
| `root` | `123@@@` | 3 |
| `root` | `LeitboGi0ro` | 3 |
| `admin` | `admin` | 2 |
| `root` | `p@ssw0rd123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `p@ssw0rd123` | `45.205.1.42` | 2026-06-20T16:58:55 |
| `dongshuowu` | `dongshuowu` | `45.198.224.120` | 2026-06-20T17:01:37 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-20T17:02:38 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-20T17:02:38 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-20T17:02:41 |
| `admin` | `admin` | `8.136.189.162` | 2026-06-20T17:03:59 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-20T17:04:00 |
| `root` | `qwe!@#qwe` | `45.198.224.120` | 2026-06-20T17:18:21 |
| `root` | `P@ssword1234567` | `45.205.1.42` | 2026-06-20T17:18:31 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-20T17:25:50 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-20T17:25:50 |
| `root` | `P@ssw0rd2010` | `45.198.224.120` | 2026-06-20T17:35:18 |
| `root` | `﻿------fuck------` | `218.8.139.114` | 2026-06-20T17:37:21 |
| `root` | `qwaszx!@` | `45.205.1.42` | 2026-06-20T17:38:43 |
| `root` | `` | `91.92.40.15` | 2026-06-20T17:41:47 |
| `solor` | `solor` | `45.198.224.120` | 2026-06-20T17:43:34 |
| `root` | `---fuck_you----` | `117.50.213.145` | 2026-06-20T17:45:39 |
| `root` | `L1nux@Passw0rd!` | `45.198.224.120` | 2026-06-20T17:52:04 |
| `root` | `P@$$W0RD@2020` | `45.205.1.42` | 2026-06-20T17:58:29 |
| `user` | `1` | `45.198.224.120` | 2026-06-20T18:08:37 |
| `nagios` | `nagios123456` | `45.198.224.120` | 2026-06-20T18:16:12 |
| `ubuntu` | `Pass12345` | `45.205.1.42` | 2026-06-20T18:18:20 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-20T18:26:02 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-20T18:26:02 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-20T18:26:08 |
| `root` | `qwerty21` | `45.198.224.120` | 2026-06-20T18:32:16 |
| `root` | `112233` | `45.205.1.42` | 2026-06-20T18:38:14 |
| `root` | `qaz123#@!` | `45.198.224.120` | 2026-06-20T18:48:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **230** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 21 |
| libssh | 12 |
| Paramiko (Python) | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 16 | 3 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `5f904648ee89...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 16 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
Source IPs: `91.92.40.15`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **20** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS197170` | TechTies Inc. | 1 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS20473` | The Constant Company, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-74e1cfe2acf0

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 16:58 |
| **Last Seen** | 2026-06-20 16:59 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 16:58:44` | `cowrie.session.connect` |
| `2026-06-20 16:58:45` | `cowrie.client.version` |
| `2026-06-20 16:58:45` | `cowrie.client.kex` |
| `2026-06-20 16:58:55` | `cowrie.login.success` |
| `2026-06-20 16:58:59` | `cowrie.session.params` |
| `2026-06-20 16:58:59` | `cowrie.command.input` |
| `2026-06-20 16:59:02` | `cowrie.log.closed` |
| `2026-06-20 16:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e05a772f74

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 17:01 |
| **Last Seen** | 2026-06-20 17:01 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:01:15` | `cowrie.session.connect` |
| `2026-06-20 17:01:19` | `cowrie.client.version` |
| `2026-06-20 17:01:19` | `cowrie.client.kex` |
| `2026-06-20 17:01:37` | `cowrie.login.success` |
| `2026-06-20 17:01:47` | `cowrie.session.params` |
| `2026-06-20 17:01:47` | `cowrie.command.input` |
| `2026-06-20 17:01:51` | `cowrie.log.closed` |
| `2026-06-20 17:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f93ac33a83f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 17:02 |
| **Last Seen** | 2026-06-20 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:02:37` | `cowrie.session.connect` |
| `2026-06-20 17:02:37` | `cowrie.client.version` |
| `2026-06-20 17:02:37` | `cowrie.client.kex` |
| `2026-06-20 17:02:38` | `cowrie.login.success` |
| `2026-06-20 17:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-277d11cd38d1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 17:02 |
| **Last Seen** | 2026-06-20 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:02:37` | `cowrie.session.connect` |
| `2026-06-20 17:02:37` | `cowrie.client.version` |
| `2026-06-20 17:02:37` | `cowrie.client.kex` |
| `2026-06-20 17:02:38` | `cowrie.login.success` |
| `2026-06-20 17:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c64c1b2335b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 17:02 |
| **Last Seen** | 2026-06-20 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:02:40` | `cowrie.session.connect` |
| `2026-06-20 17:02:40` | `cowrie.client.version` |
| `2026-06-20 17:02:40` | `cowrie.client.kex` |
| `2026-06-20 17:02:41` | `cowrie.login.success` |
| `2026-06-20 17:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804869039017

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-20 17:02 |
| **Last Seen** | 2026-06-20 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:02:41` | `cowrie.session.connect` |
| `2026-06-20 17:02:41` | `cowrie.client.version` |
| `2026-06-20 17:02:41` | `cowrie.client.kex` |
| `2026-06-20 17:02:42` | `cowrie.login.success` |
| `2026-06-20 17:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55981354de97

| Field | Detail |
|---|---|
| **Source IP** | `8.136.189[.]162` |
| **First Seen** | 2026-06-20 17:03 |
| **Last Seen** | 2026-06-20 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:03:58` | `cowrie.session.connect` |
| `2026-06-20 17:03:58` | `cowrie.client.version` |
| `2026-06-20 17:03:58` | `cowrie.client.kex` |
| `2026-06-20 17:03:59` | `cowrie.login.success` |
| `2026-06-20 17:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.136.189[.]162` to AbuseIPDB if not already reported
- [ ] Block `8.136.189[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a06215c891

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-20 17:04 |
| **Last Seen** | 2026-06-20 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:04:00` | `cowrie.session.connect` |
| `2026-06-20 17:04:00` | `cowrie.client.version` |
| `2026-06-20 17:04:00` | `cowrie.client.kex` |
| `2026-06-20 17:04:00` | `cowrie.login.success` |
| `2026-06-20 17:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979c3ecf430f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 17:18 |
| **Last Seen** | 2026-06-20 17:18 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:18:02` | `cowrie.session.connect` |
| `2026-06-20 17:18:06` | `cowrie.client.version` |
| `2026-06-20 17:18:06` | `cowrie.client.kex` |
| `2026-06-20 17:18:21` | `cowrie.login.success` |
| `2026-06-20 17:18:29` | `cowrie.session.params` |
| `2026-06-20 17:18:29` | `cowrie.command.input` |
| `2026-06-20 17:18:33` | `cowrie.log.closed` |
| `2026-06-20 17:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a1bad6f2bf

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 17:18 |
| **Last Seen** | 2026-06-20 17:18 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:18:19` | `cowrie.session.connect` |
| `2026-06-20 17:18:21` | `cowrie.client.version` |
| `2026-06-20 17:18:21` | `cowrie.client.kex` |
| `2026-06-20 17:18:31` | `cowrie.login.success` |
| `2026-06-20 17:18:34` | `cowrie.session.params` |
| `2026-06-20 17:18:34` | `cowrie.command.input` |
| `2026-06-20 17:18:37` | `cowrie.log.closed` |
| `2026-06-20 17:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c85fb78bc6c

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-20 17:25 |
| **Last Seen** | 2026-06-20 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:25:49` | `cowrie.session.connect` |
| `2026-06-20 17:25:49` | `cowrie.client.version` |
| `2026-06-20 17:25:49` | `cowrie.client.kex` |
| `2026-06-20 17:25:50` | `cowrie.login.success` |
| `2026-06-20 17:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d132529ba7d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-20 17:25 |
| **Last Seen** | 2026-06-20 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:25:49` | `cowrie.session.connect` |
| `2026-06-20 17:25:49` | `cowrie.client.version` |
| `2026-06-20 17:25:50` | `cowrie.client.kex` |
| `2026-06-20 17:25:50` | `cowrie.login.success` |
| `2026-06-20 17:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04751f736b01

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 17:35 |
| **Last Seen** | 2026-06-20 17:35 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:35:02` | `cowrie.session.connect` |
| `2026-06-20 17:35:05` | `cowrie.client.version` |
| `2026-06-20 17:35:05` | `cowrie.client.kex` |
| `2026-06-20 17:35:18` | `cowrie.login.success` |
| `2026-06-20 17:35:26` | `cowrie.session.params` |
| `2026-06-20 17:35:26` | `cowrie.command.input` |
| `2026-06-20 17:35:29` | `cowrie.log.closed` |
| `2026-06-20 17:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cd1994f416

| Field | Detail |
|---|---|
| **Source IP** | `218.8.139[.]114` |
| **First Seen** | 2026-06-20 17:37 |
| **Last Seen** | 2026-06-20 17:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:37:19` | `cowrie.session.connect` |
| `2026-06-20 17:37:19` | `cowrie.client.version` |
| `2026-06-20 17:37:20` | `cowrie.client.kex` |
| `2026-06-20 17:37:21` | `cowrie.login.success` |
| `2026-06-20 17:37:22` | `cowrie.session.params` |
| `2026-06-20 17:37:22` | `cowrie.command.input` |
| `2026-06-20 17:37:22` | `cowrie.log.closed` |
| `2026-06-20 17:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.8.139[.]114` to AbuseIPDB if not already reported
- [ ] Block `218.8.139[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990a54458ed6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 17:38 |
| **Last Seen** | 2026-06-20 17:38 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:38:28` | `cowrie.session.connect` |
| `2026-06-20 17:38:30` | `cowrie.client.version` |
| `2026-06-20 17:38:30` | `cowrie.client.kex` |
| `2026-06-20 17:38:43` | `cowrie.login.success` |
| `2026-06-20 17:38:50` | `cowrie.session.params` |
| `2026-06-20 17:38:50` | `cowrie.command.input` |
| `2026-06-20 17:38:51` | `cowrie.log.closed` |
| `2026-06-20 17:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571831f25f5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]15` |
| **First Seen** | 2026-06-20 17:41 |
| **Last Seen** | 2026-06-20 17:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:41:47` | `cowrie.session.connect` |
| `2026-06-20 17:41:47` | `cowrie.login.success` |
| `2026-06-20 17:41:48` | `cowrie.session.params` |
| `2026-06-20 17:41:48` | `cowrie.command.input` |
| `2026-06-20 17:41:49` | `cowrie.command.input` |
| `2026-06-20 17:41:49` | `cowrie.command.input` |
| `2026-06-20 17:41:50` | `cowrie.command.input` |
| `2026-06-20 17:41:50` | `cowrie.command.failed` |
| `2026-06-20 17:41:50` | `cowrie.log.closed` |
| `2026-06-20 17:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]15` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0c5f3b5baf

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 17:43 |
| **Last Seen** | 2026-06-20 17:43 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:43:18` | `cowrie.session.connect` |
| `2026-06-20 17:43:21` | `cowrie.client.version` |
| `2026-06-20 17:43:21` | `cowrie.client.kex` |
| `2026-06-20 17:43:34` | `cowrie.login.success` |
| `2026-06-20 17:43:42` | `cowrie.session.params` |
| `2026-06-20 17:43:42` | `cowrie.command.input` |
| `2026-06-20 17:43:45` | `cowrie.log.closed` |
| `2026-06-20 17:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3870d1ad40

| Field | Detail |
|---|---|
| **Source IP** | `117.50.213[.]145` |
| **First Seen** | 2026-06-20 17:45 |
| **Last Seen** | 2026-06-20 17:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:45:36` | `cowrie.session.connect` |
| `2026-06-20 17:45:36` | `cowrie.client.version` |
| `2026-06-20 17:45:37` | `cowrie.client.kex` |
| `2026-06-20 17:45:39` | `cowrie.login.success` |
| `2026-06-20 17:45:40` | `cowrie.session.params` |
| `2026-06-20 17:45:40` | `cowrie.command.input` |
| `2026-06-20 17:45:40` | `cowrie.log.closed` |
| `2026-06-20 17:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.213[.]145` to AbuseIPDB if not already reported
- [ ] Block `117.50.213[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335c861b77c8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 17:51 |
| **Last Seen** | 2026-06-20 17:52 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:51:46` | `cowrie.session.connect` |
| `2026-06-20 17:51:50` | `cowrie.client.version` |
| `2026-06-20 17:51:50` | `cowrie.client.kex` |
| `2026-06-20 17:52:04` | `cowrie.login.success` |
| `2026-06-20 17:52:14` | `cowrie.session.params` |
| `2026-06-20 17:52:14` | `cowrie.command.input` |
| `2026-06-20 17:52:17` | `cowrie.log.closed` |
| `2026-06-20 17:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d685f5930bc8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 17:58 |
| **Last Seen** | 2026-06-20 17:58 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 17:58:17` | `cowrie.session.connect` |
| `2026-06-20 17:58:20` | `cowrie.client.version` |
| `2026-06-20 17:58:20` | `cowrie.client.kex` |
| `2026-06-20 17:58:29` | `cowrie.login.success` |
| `2026-06-20 17:58:35` | `cowrie.session.params` |
| `2026-06-20 17:58:35` | `cowrie.command.input` |
| `2026-06-20 17:58:37` | `cowrie.log.closed` |
| `2026-06-20 17:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2e207b2d95e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 18:08 |
| **Last Seen** | 2026-06-20 18:08 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:08:16` | `cowrie.session.connect` |
| `2026-06-20 18:08:19` | `cowrie.client.version` |
| `2026-06-20 18:08:19` | `cowrie.client.kex` |
| `2026-06-20 18:08:37` | `cowrie.login.success` |
| `2026-06-20 18:08:52` | `cowrie.session.params` |
| `2026-06-20 18:08:52` | `cowrie.command.input` |
| `2026-06-20 18:08:58` | `cowrie.log.closed` |
| `2026-06-20 18:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a064966b821

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 18:15 |
| **Last Seen** | 2026-06-20 18:16 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:15:50` | `cowrie.session.connect` |
| `2026-06-20 18:15:54` | `cowrie.client.version` |
| `2026-06-20 18:15:54` | `cowrie.client.kex` |
| `2026-06-20 18:16:12` | `cowrie.login.success` |
| `2026-06-20 18:16:22` | `cowrie.session.params` |
| `2026-06-20 18:16:22` | `cowrie.command.input` |
| `2026-06-20 18:16:26` | `cowrie.log.closed` |
| `2026-06-20 18:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc84e1a91f2a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 18:18 |
| **Last Seen** | 2026-06-20 18:18 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:18:07` | `cowrie.session.connect` |
| `2026-06-20 18:18:09` | `cowrie.client.version` |
| `2026-06-20 18:18:09` | `cowrie.client.kex` |
| `2026-06-20 18:18:20` | `cowrie.login.success` |
| `2026-06-20 18:18:24` | `cowrie.session.params` |
| `2026-06-20 18:18:24` | `cowrie.command.input` |
| `2026-06-20 18:18:27` | `cowrie.log.closed` |
| `2026-06-20 18:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985651448f7c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 18:26 |
| **Last Seen** | 2026-06-20 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:26:02` | `cowrie.session.connect` |
| `2026-06-20 18:26:02` | `cowrie.client.version` |
| `2026-06-20 18:26:02` | `cowrie.client.kex` |
| `2026-06-20 18:26:02` | `cowrie.login.success` |
| `2026-06-20 18:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6882cac80a59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 18:26 |
| **Last Seen** | 2026-06-20 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:26:02` | `cowrie.session.connect` |
| `2026-06-20 18:26:02` | `cowrie.client.version` |
| `2026-06-20 18:26:02` | `cowrie.client.kex` |
| `2026-06-20 18:26:02` | `cowrie.login.success` |
| `2026-06-20 18:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02774276d3a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 18:26 |
| **Last Seen** | 2026-06-20 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:26:08` | `cowrie.session.connect` |
| `2026-06-20 18:26:08` | `cowrie.client.version` |
| `2026-06-20 18:26:08` | `cowrie.client.kex` |
| `2026-06-20 18:26:08` | `cowrie.login.success` |
| `2026-06-20 18:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5cf56b6d9b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-20 18:26 |
| **Last Seen** | 2026-06-20 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:26:08` | `cowrie.session.connect` |
| `2026-06-20 18:26:08` | `cowrie.client.version` |
| `2026-06-20 18:26:08` | `cowrie.client.kex` |
| `2026-06-20 18:26:08` | `cowrie.login.success` |
| `2026-06-20 18:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c797a5d5a6b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 18:31 |
| **Last Seen** | 2026-06-20 18:32 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:31:56` | `cowrie.session.connect` |
| `2026-06-20 18:31:59` | `cowrie.client.version` |
| `2026-06-20 18:31:59` | `cowrie.client.kex` |
| `2026-06-20 18:32:16` | `cowrie.login.success` |
| `2026-06-20 18:32:24` | `cowrie.session.params` |
| `2026-06-20 18:32:24` | `cowrie.command.input` |
| `2026-06-20 18:32:30` | `cowrie.log.closed` |
| `2026-06-20 18:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db4ea398d16

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-20 18:38 |
| **Last Seen** | 2026-06-20 18:38 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:38:02` | `cowrie.session.connect` |
| `2026-06-20 18:38:04` | `cowrie.client.version` |
| `2026-06-20 18:38:04` | `cowrie.client.kex` |
| `2026-06-20 18:38:14` | `cowrie.login.success` |
| `2026-06-20 18:38:18` | `cowrie.session.params` |
| `2026-06-20 18:38:18` | `cowrie.command.input` |
| `2026-06-20 18:38:21` | `cowrie.log.closed` |
| `2026-06-20 18:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59705b04ceae

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-20 18:48 |
| **Last Seen** | 2026-06-20 18:49 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:48:32` | `cowrie.session.connect` |
| `2026-06-20 18:48:35` | `cowrie.client.version` |
| `2026-06-20 18:48:35` | `cowrie.client.kex` |
| `2026-06-20 18:48:49` | `cowrie.login.success` |
| `2026-06-20 18:48:58` | `cowrie.session.params` |
| `2026-06-20 18:48:58` | `cowrie.command.input` |
| `2026-06-20 18:49:01` | `cowrie.log.closed` |
| `2026-06-20 18:49:01` | `cowrie.session.closed` |

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
| `138.68.100[.]228` | **166** | 2026-06-20 16:55 | 2026-06-20 18:54 | 182m | 0 | `T1592` | 🟠 MEDIUM |
| `45.198.224[.]120` | **5** | 2026-06-20 17:09 | 2026-06-20 18:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.91.11[.]226` | **3** | 2026-06-20 17:14 | 2026-06-20 17:24 | 2m | 0 | `T1592` | 🟢 LOW |
| `124.225.4[.]88` | **2** | 2026-06-20 18:14 | 2026-06-20 18:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]53` | **2** | 2026-06-20 18:33 | 2026-06-20 18:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.197.71[.]254` | 1 | 2026-06-20 17:15 | 2026-06-20 17:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.50.213[.]145` | 1 | 2026-06-20 17:45 | 2026-06-20 17:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.162.112[.]209` | 1 | 2026-06-20 18:20 | 2026-06-20 18:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `20.171.46[.]137` | 1 | 2026-06-20 17:40 | 2026-06-20 17:41 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.8.139[.]114` | 1 | 2026-06-20 17:37 | 2026-06-20 17:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-06-20 17:24 | 2026-06-20 17:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]71` | 1 | 2026-06-20 18:54 | 2026-06-20 18:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]168` | 1 | 2026-06-20 17:08 | 2026-06-20 17:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]15` | 1 | 2026-06-20 17:41 | 2026-06-20 17:41 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `195.96.139[.]53` | GB | Driftnet Ltd | **100** ⚠️ | 5 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `18.162.112[.]209` | HK | Amazon Data Services Hong Kong | **100** ⚠️ | 3 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 3 |
| `91.92.40[.]15` | NL | TechTies Inc. | **100** ⚠️ | 21 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `20.171.46[.]137` | US | Microsoft Corporation | **100** ⚠️ | 5 |
| `8.136.189[.]162` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 30 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 230 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 17 files |
| Tool 33  | YARA Classifier             | ✅ 13 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 178 session(s)).

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
_Report time: 2026-06-20T19:43:09Z_

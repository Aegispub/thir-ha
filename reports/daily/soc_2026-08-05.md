# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-05 |
| **Generated At** | 2026-08-05T19:40:35Z |
| **Shift Time** | 19:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **169** |
| Confirmed Threats | **140** |
| False Positives Filtered | **29** (17.2%) |
| Unique Attacker IPs | **76** |
| Countries of Origin | **30** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **60** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **14** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **49** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `admin` | 18 |
| `operator` | 4 |
| `test1` | 3 |
| `support` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `7` | 6 |
| `root` | 5 |
| `qwerty` | 4 |
| `1234` | 4 |
| `654321` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `7` | 6 |
| `root` | `root` | 4 |
| `admin` | `qwerty` | 4 |
| `operator` | `1234` | 4 |
| `admin` | `654321` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `www` | `root` | `45.153.34.226` | 2026-08-05T16:56:44 |
| `admin` | `654321` | `10.0.0.73` | 2026-08-05T16:56:52 |
| `admin` | `password` | `130.12.182.225` | 2026-08-05T16:58:38 |
| `supervisor` | `6` | `189.56.0.19` | 2026-08-05T16:59:54 |
| `root` | `ui` | `45.154.244.193` | 2026-08-05T17:01:46 |
| `root` | `Passw0rdzxc` | `130.12.182.224` | 2026-08-05T17:04:25 |
| `ubuntu` | `secret` | `45.156.87.165` | 2026-08-05T17:08:40 |
| `admin` | `Admin` | `213.33.204.130` | 2026-08-05T17:13:15 |
| `admin` | `Admin` | `223.107.146.186` | 2026-08-05T17:13:24 |
| `admin` | `654321` | `42.248.129.234` | 2026-08-05T17:15:12 |
| `admin` | `654321` | `117.2.123.19` | 2026-08-05T17:15:21 |
| `admin` | `admin01` | `64.89.162.146` | 2026-08-05T17:27:08 |
| `admin` | `p@ssw0rd` | `64.89.162.146` | 2026-08-05T17:27:43 |
| `admin` | `qwerty` | `10.0.0.73` | 2026-08-05T17:28:41 |
| `root` | `david09` | `45.156.87.192` | 2026-08-05T17:30:03 |
| `operator` | `1234` | `10.0.0.73` | 2026-08-05T17:31:42 |
| `admin` | `admin01` | `130.12.182.224` | 2026-08-05T17:31:48 |
| `operator` | `1234` | `192.34.128.202` | 2026-08-05T17:33:21 |
| `operator` | `1234` | `210.245.95.11` | 2026-08-05T17:33:29 |
| `root` | `ui` | `10.0.0.73` | 2026-08-05T17:43:19 |
| `root` | `bootie` | `130.12.181.21` | 2026-08-05T17:44:27 |
| `config` | `config66` | `10.0.0.73` | 2026-08-05T17:46:18 |
| `admin` | `qwerty` | `211.247.127.250` | 2026-08-05T17:47:38 |
| `root` | `!!qaz2wsx!@#` | `45.153.34.226` | 2026-08-05T17:47:53 |
| `support` | `support` | `10.0.0.73` | 2026-08-05T17:47:56 |
| `admin` | `qwerty` | `103.111.6.121` | 2026-08-05T17:48:01 |
| `telecomadmin` | `admintelecom` | `93.152.221.206` | 2026-08-05T17:50:04 |
| `root` | `7` | `10.0.0.73` | 2026-08-05T18:03:15 |
| `test1` | `test1` | `10.0.0.73` | 2026-08-05T18:06:23 |
| `root` | `marketing` | `190.57.233.133` | 2026-08-05T18:09:10 |
| `root` | `tony24` | `102.220.160.47` | 2026-08-05T18:09:36 |
| `root` | `ZAQ!2011` | `130.12.182.224` | 2026-08-05T18:10:19 |
| `root` | `Admin654321!` | `64.89.162.146` | 2026-08-05T18:11:36 |
| `root` | `7` | `36.92.35.211` | 2026-08-05T18:21:58 |
| `root` | `7` | `213.130.207.177` | 2026-08-05T18:22:06 |
| `root` | `7` | `121.128.84.224` | 2026-08-05T18:22:11 |
| `root` | `7` | `49.206.194.29` | 2026-08-05T18:22:25 |
| `admin` | `switch` | `193.24.211.204` | 2026-08-05T18:23:11 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-05T18:24:12 |
| `test1` | `test1` | `195.222.57.190` | 2026-08-05T18:24:31 |
| `user` | `user` | `102.220.160.29` | 2026-08-05T18:30:51 |
| `123qweASD` | `123qweASD` | `10.0.0.73` | 2026-08-05T18:41:00 |
| `root` | `tyrell` | `64.89.162.146` | 2026-08-05T18:43:16 |
| `admin` | `123456789` | `130.12.182.225` | 2026-08-05T18:46:44 |
| `niggaballs` | `nigg@b@lls2015@` | `93.152.221.206` | 2026-08-05T18:47:47 |
| `root` | `﻿------fuck------` | `180.92.231.10` | 2026-08-05T18:48:34 |
| `AdminGPON` | `ALC#FGU` | `130.12.182.223` | 2026-08-05T18:50:29 |
| `root` | `qwer1234!` | `130.12.182.231` | 2026-08-05T18:53:42 |
| `admin` | `12345678` | `130.12.182.225` | 2026-08-05T18:53:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **169** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 28 |
| OpenSSH | 15 |
| Go SSH scanner | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a591c4ddccc9...` | Mirai/variant | 26 | 14 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `14b2ddda386a...` | Mirai/variant | 2 | 2 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a591c4ddccc9...` | libssh | 26 | 14 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 9 | 6 | — |
| `14b2ddda386a...` | libssh | 2 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **76** |
| Unique ASNs | **57** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS197769` | VPS Dedicated LLC | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS197170` | TechTies Inc. | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 2 | HIGH |
| `AS272030` | SMARTNET S.R.L. | 2 | LOW |
| `AS48721` | Flyservers S.A. | 1 | HIGH |
| `AS7738` | V tal | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (41)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e2864a3a4f75

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 16:56 |
| **Last Seen** | 2026-08-05 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:56:44` | `cowrie.session.connect` |
| `2026-08-05 16:56:44` | `cowrie.client.version` |
| `2026-08-05 16:56:44` | `cowrie.client.kex` |
| `2026-08-05 16:56:44` | `cowrie.login.success` |
| `2026-08-05 16:56:44` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:56:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da2e471d333

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 16:58 |
| **Last Seen** | 2026-08-05 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:58:38` | `cowrie.session.connect` |
| `2026-08-05 16:58:38` | `cowrie.client.version` |
| `2026-08-05 16:58:38` | `cowrie.client.kex` |
| `2026-08-05 16:58:38` | `cowrie.login.success` |
| `2026-08-05 16:58:39` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:58:39` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c326b6beab2e

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-05 16:59 |
| **Last Seen** | 2026-08-05 17:00 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:59:50` | `cowrie.session.connect` |
| `2026-08-05 16:59:51` | `cowrie.client.version` |
| `2026-08-05 16:59:51` | `cowrie.client.kex` |
| `2026-08-05 16:59:54` | `cowrie.login.success` |
| `2026-08-05 16:59:55` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68a48feddcf

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-05 17:01 |
| **Last Seen** | 2026-08-05 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:01:45` | `cowrie.session.connect` |
| `2026-08-05 17:01:45` | `cowrie.client.version` |
| `2026-08-05 17:01:45` | `cowrie.client.kex` |
| `2026-08-05 17:01:46` | `cowrie.login.success` |
| `2026-08-05 17:01:46` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:01:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-05 17:01:46` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa9d1a23cd4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 17:04 |
| **Last Seen** | 2026-08-05 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:04:24` | `cowrie.session.connect` |
| `2026-08-05 17:04:24` | `cowrie.client.version` |
| `2026-08-05 17:04:24` | `cowrie.client.kex` |
| `2026-08-05 17:04:25` | `cowrie.login.success` |
| `2026-08-05 17:04:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:04:25` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56080d8e342e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]165` |
| **First Seen** | 2026-08-05 17:08 |
| **Last Seen** | 2026-08-05 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:08:40` | `cowrie.session.connect` |
| `2026-08-05 17:08:40` | `cowrie.client.version` |
| `2026-08-05 17:08:40` | `cowrie.client.kex` |
| `2026-08-05 17:08:40` | `cowrie.login.success` |
| `2026-08-05 17:08:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:08:40` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c6a6ddd1aa

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-05 17:13 |
| **Last Seen** | 2026-08-05 17:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:13:13` | `cowrie.session.connect` |
| `2026-08-05 17:13:14` | `cowrie.client.version` |
| `2026-08-05 17:13:14` | `cowrie.client.kex` |
| `2026-08-05 17:13:15` | `cowrie.login.success` |
| `2026-08-05 17:13:15` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56444eb056f5

| Field | Detail |
|---|---|
| **Source IP** | `223.107.146[.]186` |
| **First Seen** | 2026-08-05 17:13 |
| **Last Seen** | 2026-08-05 17:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:13:20` | `cowrie.session.connect` |
| `2026-08-05 17:13:21` | `cowrie.client.version` |
| `2026-08-05 17:13:21` | `cowrie.client.kex` |
| `2026-08-05 17:13:24` | `cowrie.login.success` |
| `2026-08-05 17:13:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.146[.]186` to AbuseIPDB if not already reported
- [ ] Block `223.107.146[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f78fd9500b1

| Field | Detail |
|---|---|
| **Source IP** | `42.248.129[.]234` |
| **First Seen** | 2026-08-05 17:15 |
| **Last Seen** | 2026-08-05 17:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:15:08` | `cowrie.session.connect` |
| `2026-08-05 17:15:09` | `cowrie.client.version` |
| `2026-08-05 17:15:09` | `cowrie.client.kex` |
| `2026-08-05 17:15:12` | `cowrie.login.success` |
| `2026-08-05 17:15:13` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.248.129[.]234` to AbuseIPDB if not already reported
- [ ] Block `42.248.129[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d214e72079

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-08-05 17:15 |
| **Last Seen** | 2026-08-05 17:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:15:18` | `cowrie.session.connect` |
| `2026-08-05 17:15:19` | `cowrie.client.version` |
| `2026-08-05 17:15:19` | `cowrie.client.kex` |
| `2026-08-05 17:15:21` | `cowrie.login.success` |
| `2026-08-05 17:15:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22474f3b925d

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-05 17:27 |
| **Last Seen** | 2026-08-05 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:27:07` | `cowrie.session.connect` |
| `2026-08-05 17:27:07` | `cowrie.client.version` |
| `2026-08-05 17:27:07` | `cowrie.client.kex` |
| `2026-08-05 17:27:08` | `cowrie.login.success` |
| `2026-08-05 17:27:08` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:27:08` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ea5a5f02d02

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-05 17:27 |
| **Last Seen** | 2026-08-05 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:27:43` | `cowrie.session.connect` |
| `2026-08-05 17:27:43` | `cowrie.client.version` |
| `2026-08-05 17:27:43` | `cowrie.client.kex` |
| `2026-08-05 17:27:43` | `cowrie.login.success` |
| `2026-08-05 17:27:43` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:27:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a0abbd2503

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 17:30 |
| **Last Seen** | 2026-08-05 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:30:03` | `cowrie.session.connect` |
| `2026-08-05 17:30:03` | `cowrie.client.version` |
| `2026-08-05 17:30:03` | `cowrie.client.kex` |
| `2026-08-05 17:30:03` | `cowrie.login.success` |
| `2026-08-05 17:30:03` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:30:03` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78209a3aff55

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 17:31 |
| **Last Seen** | 2026-08-05 17:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:31:47` | `cowrie.session.connect` |
| `2026-08-05 17:31:47` | `cowrie.client.version` |
| `2026-08-05 17:31:47` | `cowrie.client.kex` |
| `2026-08-05 17:31:48` | `cowrie.login.success` |
| `2026-08-05 17:31:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:31:49` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4989bd512d8

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-08-05 17:33 |
| **Last Seen** | 2026-08-05 17:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:33:20` | `cowrie.session.connect` |
| `2026-08-05 17:33:20` | `cowrie.client.version` |
| `2026-08-05 17:33:20` | `cowrie.client.kex` |
| `2026-08-05 17:33:21` | `cowrie.login.success` |
| `2026-08-05 17:33:22` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71dae0b39f3

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-08-05 17:33 |
| **Last Seen** | 2026-08-05 17:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:33:27` | `cowrie.session.connect` |
| `2026-08-05 17:33:27` | `cowrie.client.version` |
| `2026-08-05 17:33:27` | `cowrie.client.kex` |
| `2026-08-05 17:33:29` | `cowrie.login.success` |
| `2026-08-05 17:33:30` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e82f0548c57

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 17:44 |
| **Last Seen** | 2026-08-05 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:44:26` | `cowrie.session.connect` |
| `2026-08-05 17:44:26` | `cowrie.client.version` |
| `2026-08-05 17:44:26` | `cowrie.client.kex` |
| `2026-08-05 17:44:27` | `cowrie.login.success` |
| `2026-08-05 17:44:27` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:44:27` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0008b4b831c

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-08-05 17:47 |
| **Last Seen** | 2026-08-05 17:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:47:35` | `cowrie.session.connect` |
| `2026-08-05 17:47:36` | `cowrie.client.version` |
| `2026-08-05 17:47:36` | `cowrie.client.kex` |
| `2026-08-05 17:47:38` | `cowrie.login.success` |
| `2026-08-05 17:47:39` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d348d048e504

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 17:47 |
| **Last Seen** | 2026-08-05 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:47:52` | `cowrie.session.connect` |
| `2026-08-05 17:47:52` | `cowrie.client.version` |
| `2026-08-05 17:47:52` | `cowrie.client.kex` |
| `2026-08-05 17:47:53` | `cowrie.login.success` |
| `2026-08-05 17:47:53` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:47:53` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736dc8cb1871

| Field | Detail |
|---|---|
| **Source IP** | `103.111.6[.]121` |
| **First Seen** | 2026-08-05 17:47 |
| **Last Seen** | 2026-08-05 17:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:47:58` | `cowrie.session.connect` |
| `2026-08-05 17:47:59` | `cowrie.client.version` |
| `2026-08-05 17:47:59` | `cowrie.client.kex` |
| `2026-08-05 17:48:01` | `cowrie.login.success` |
| `2026-08-05 17:48:01` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.111.6[.]121` to AbuseIPDB if not already reported
- [ ] Block `103.111.6[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc229436f3a

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-05 17:50 |
| **Last Seen** | 2026-08-05 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 17:50:04` | `cowrie.session.connect` |
| `2026-08-05 17:50:04` | `cowrie.client.version` |
| `2026-08-05 17:50:04` | `cowrie.client.kex` |
| `2026-08-05 17:50:04` | `cowrie.login.success` |
| `2026-08-05 17:50:05` | `cowrie.direct-tcpip.request` |
| `2026-08-05 17:50:05` | `cowrie.direct-tcpip.data` |
| `2026-08-05 17:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fca8e7cc93

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-05 18:09 |
| **Last Seen** | 2026-08-05 18:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:09:07` | `cowrie.session.connect` |
| `2026-08-05 18:09:08` | `cowrie.client.version` |
| `2026-08-05 18:09:08` | `cowrie.client.kex` |
| `2026-08-05 18:09:10` | `cowrie.login.success` |
| `2026-08-05 18:09:11` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9108e2920f3

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 18:09 |
| **Last Seen** | 2026-08-05 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:09:35` | `cowrie.session.connect` |
| `2026-08-05 18:09:35` | `cowrie.client.version` |
| `2026-08-05 18:09:35` | `cowrie.client.kex` |
| `2026-08-05 18:09:36` | `cowrie.login.success` |
| `2026-08-05 18:09:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:09:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5bf8503cf86

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 18:10 |
| **Last Seen** | 2026-08-05 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:10:18` | `cowrie.session.connect` |
| `2026-08-05 18:10:18` | `cowrie.client.version` |
| `2026-08-05 18:10:18` | `cowrie.client.kex` |
| `2026-08-05 18:10:19` | `cowrie.login.success` |
| `2026-08-05 18:10:19` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:10:19` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0732c85e26b0

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-05 18:11 |
| **Last Seen** | 2026-08-05 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:11:36` | `cowrie.session.connect` |
| `2026-08-05 18:11:36` | `cowrie.client.version` |
| `2026-08-05 18:11:36` | `cowrie.client.kex` |
| `2026-08-05 18:11:36` | `cowrie.login.success` |
| `2026-08-05 18:11:36` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:11:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7df29c97221

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 18:13 |
| **Last Seen** | 2026-08-05 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:13:11` | `cowrie.session.connect` |
| `2026-08-05 18:13:11` | `cowrie.client.version` |
| `2026-08-05 18:13:11` | `cowrie.client.kex` |
| `2026-08-05 18:13:11` | `cowrie.login.success` |
| `2026-08-05 18:13:11` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:13:12` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5be5457331

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-08-05 18:21 |
| **Last Seen** | 2026-08-05 18:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:21:55` | `cowrie.session.connect` |
| `2026-08-05 18:21:56` | `cowrie.client.version` |
| `2026-08-05 18:21:56` | `cowrie.client.kex` |
| `2026-08-05 18:21:58` | `cowrie.login.success` |
| `2026-08-05 18:21:59` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb2de681120

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-08-05 18:22 |
| **Last Seen** | 2026-08-05 18:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:22:04` | `cowrie.session.connect` |
| `2026-08-05 18:22:05` | `cowrie.client.version` |
| `2026-08-05 18:22:05` | `cowrie.client.kex` |
| `2026-08-05 18:22:06` | `cowrie.login.success` |
| `2026-08-05 18:22:06` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cd535bf23da

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-08-05 18:22 |
| **Last Seen** | 2026-08-05 18:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:22:08` | `cowrie.session.connect` |
| `2026-08-05 18:22:09` | `cowrie.client.version` |
| `2026-08-05 18:22:09` | `cowrie.client.kex` |
| `2026-08-05 18:22:11` | `cowrie.login.success` |
| `2026-08-05 18:22:12` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95cce906d5cc

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-08-05 18:22 |
| **Last Seen** | 2026-08-05 18:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:22:21` | `cowrie.session.connect` |
| `2026-08-05 18:22:22` | `cowrie.client.version` |
| `2026-08-05 18:22:22` | `cowrie.client.kex` |
| `2026-08-05 18:22:25` | `cowrie.login.success` |
| `2026-08-05 18:22:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9137c672d89d

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]204` |
| **First Seen** | 2026-08-05 18:23 |
| **Last Seen** | 2026-08-05 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:23:10` | `cowrie.session.connect` |
| `2026-08-05 18:23:10` | `cowrie.client.version` |
| `2026-08-05 18:23:10` | `cowrie.client.kex` |
| `2026-08-05 18:23:11` | `cowrie.login.success` |
| `2026-08-05 18:23:11` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:23:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-05 18:23:11` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d84cab0d3b2

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-05 18:23 |
| **Last Seen** | 2026-08-05 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:23:12` | `cowrie.session.connect` |
| `2026-08-05 18:23:12` | `cowrie.telnet.option` |
| `2026-08-05 18:23:12` | `cowrie.telnet.option` |
| `2026-08-05 18:24:12` | `cowrie.login.success` |
| `2026-08-05 18:24:13` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5f8a9d4786

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-05 18:24 |
| **Last Seen** | 2026-08-05 18:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:24:29` | `cowrie.session.connect` |
| `2026-08-05 18:24:30` | `cowrie.client.version` |
| `2026-08-05 18:24:30` | `cowrie.client.kex` |
| `2026-08-05 18:24:31` | `cowrie.login.success` |
| `2026-08-05 18:24:31` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d2186f5488

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 18:30 |
| **Last Seen** | 2026-08-05 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:30:50` | `cowrie.session.connect` |
| `2026-08-05 18:30:50` | `cowrie.client.version` |
| `2026-08-05 18:30:50` | `cowrie.client.kex` |
| `2026-08-05 18:30:51` | `cowrie.login.success` |
| `2026-08-05 18:30:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:30:51` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f712239295f

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-05 18:43 |
| **Last Seen** | 2026-08-05 18:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:43:16` | `cowrie.session.connect` |
| `2026-08-05 18:43:16` | `cowrie.client.version` |
| `2026-08-05 18:43:16` | `cowrie.client.kex` |
| `2026-08-05 18:43:16` | `cowrie.login.success` |
| `2026-08-05 18:43:16` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:43:16` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07bfc3e8d97

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 18:46 |
| **Last Seen** | 2026-08-05 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:46:43` | `cowrie.session.connect` |
| `2026-08-05 18:46:43` | `cowrie.client.version` |
| `2026-08-05 18:46:44` | `cowrie.client.kex` |
| `2026-08-05 18:46:44` | `cowrie.login.success` |
| `2026-08-05 18:46:44` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:46:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ad544e3ff1

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-05 18:47 |
| **Last Seen** | 2026-08-05 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:47:47` | `cowrie.session.connect` |
| `2026-08-05 18:47:47` | `cowrie.client.version` |
| `2026-08-05 18:47:47` | `cowrie.client.kex` |
| `2026-08-05 18:47:47` | `cowrie.login.success` |
| `2026-08-05 18:47:48` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:47:48` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81eef74d2575

| Field | Detail |
|---|---|
| **Source IP** | `180.92.231[.]10` |
| **First Seen** | 2026-08-05 18:48 |
| **Last Seen** | 2026-08-05 18:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:48:33` | `cowrie.session.connect` |
| `2026-08-05 18:48:33` | `cowrie.client.version` |
| `2026-08-05 18:48:33` | `cowrie.client.kex` |
| `2026-08-05 18:48:34` | `cowrie.login.success` |
| `2026-08-05 18:48:35` | `cowrie.session.params` |
| `2026-08-05 18:48:35` | `cowrie.command.input` |
| `2026-08-05 18:48:35` | `cowrie.log.closed` |
| `2026-08-05 18:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.92.231[.]10` to AbuseIPDB if not already reported
- [ ] Block `180.92.231[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3dd9587ce1e

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-05 18:50 |
| **Last Seen** | 2026-08-05 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:50:29` | `cowrie.session.connect` |
| `2026-08-05 18:50:29` | `cowrie.client.version` |
| `2026-08-05 18:50:29` | `cowrie.client.kex` |
| `2026-08-05 18:50:29` | `cowrie.login.success` |
| `2026-08-05 18:50:29` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:50:30` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02f86bda03f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]231` |
| **First Seen** | 2026-08-05 18:53 |
| **Last Seen** | 2026-08-05 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:53:42` | `cowrie.session.connect` |
| `2026-08-05 18:53:42` | `cowrie.client.version` |
| `2026-08-05 18:53:42` | `cowrie.client.kex` |
| `2026-08-05 18:53:42` | `cowrie.login.success` |
| `2026-08-05 18:53:42` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:53:42` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]231` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7244a2d9299a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 18:53 |
| **Last Seen** | 2026-08-05 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 18:53:48` | `cowrie.session.connect` |
| `2026-08-05 18:53:48` | `cowrie.client.version` |
| `2026-08-05 18:53:48` | `cowrie.client.kex` |
| `2026-08-05 18:53:49` | `cowrie.login.success` |
| `2026-08-05 18:53:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 18:53:49` | `cowrie.direct-tcpip.data` |
| `2026-08-05 18:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]58` | **53** | 2026-08-05 16:55 | 2026-08-05 18:47 | 28m | 0 | `T1592` | 🟠 MEDIUM |
| `102.220.160[.]67` | **4** | 2026-08-05 17:24 | 2026-08-05 17:24 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `130.12.182[.]224` | **4** | 2026-08-05 18:15 | 2026-08-05 18:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `130.12.182[.]227` | **4** | 2026-08-05 17:35 | 2026-08-05 17:35 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-05 17:12 | 2026-08-05 18:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `208.109.242[.]255` | **4** | 2026-08-05 17:52 | 2026-08-05 18:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.153.34[.]226` | **4** | 2026-08-05 18:14 | 2026-08-05 18:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-05 18:07 | 2026-08-05 18:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-08-05 17:37 | 2026-08-05 17:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.12.154[.]61` | **2** | 2026-08-05 18:34 | 2026-08-05 18:36 | 2m | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-08-05 17:25 | 2026-08-05 17:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.17[.]184` | 1 | 2026-08-05 17:43 | 2026-08-05 17:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | 1 | 2026-08-05 16:58 | 2026-08-05 16:58 | 41s | 0 | `T1592` | 🟢 LOW |
| `180.92.231[.]10` | 1 | 2026-08-05 18:48 | 2026-08-05 18:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.242.99[.]140` | 1 | 2026-08-05 18:42 | 2026-08-05 18:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-05 18:10 | 2026-08-05 18:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.199.32[.]174` | 1 | 2026-08-05 17:47 | 2026-08-05 17:48 | 33s | 0 | `T1592` | 🟢 LOW |
| `222.76.248[.]54` | 1 | 2026-08-05 17:32 | 2026-08-05 17:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.229.156[.]173` | 1 | 2026-08-05 18:52 | 2026-08-05 18:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]36` | 1 | 2026-08-05 17:16 | 2026-08-05 17:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-08-05 17:57 | 2026-08-05 17:59 | 96s | 0 | `T1592` | 🟢 LOW |
| `58.208.84[.]103` | 1 | 2026-08-05 17:54 | 2026-08-05 17:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-08-05 18:10 | 2026-08-05 18:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-05 17:47 | 2026-08-05 17:49 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 44/100 | 🟡 MEDIUM | **34/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260719-133120-1bcffc78eeca-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260801-061430-edcaf401de58-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `130.12.182[.]223` | DE | Netiface LLC | **100** ⚠️ | 13 |
| `92.204.138[.]58` | US | Host Europe GmbH | **100** ⚠️ | 15 |
| `192.34.128[.]202` | US | Zito Media | **100** ⚠️ | 50 |
| `190.57.233[.]133` | AR | Gigared S.A. | **100** ⚠️ | 50 |
| `93.152.221[.]206` | DE | TechTies Inc. | **100** ⚠️ | 11 |
| `45.156.87[.]192` | NL | TechTies Inc. | **100** ⚠️ | 29 |
| `210.245.95[.]11` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `103.111.6[.]121` | IN | NIKKI INTERNET SERVICES | **100** ⚠️ | 18 |
| `106.12.154[.]61` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 2 |
| `194.165.16[.]163` | PL | Flyservers S.A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 169 cases |
| Tool 34  | Credential Extractor        | ✅ 60 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 76 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 57 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 41 priority case(s) shown individually · 24 recon entry/entries in table (10 group(s) consolidating 85 session(s)).

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
| CIS-1 | Asset Inventory | ACTIVE | assets.json updated every pipeline run by Tool 05 — covers VM2 directly and VM1 via SSH relay |
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json auto-generated from pipeline.yml each run — tracks all active tools, languages, and I/O paths |
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
_Report time: 2026-08-05T19:40:35Z_

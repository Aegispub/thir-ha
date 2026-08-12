# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-12 |
| **Generated At** | 2026-08-12T11:02:27Z |
| **Shift Time** | 11:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **83** |
| Confirmed Threats | **68** |
| False Positives Filtered | **15** (18.1%) |
| Unique Attacker IPs | **57** |
| Countries of Origin | **23** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **3** HIGH · **22** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **10** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `debian` | 6 |
| `Admin` | 5 |
| `root` | 4 |
| `admin` | 4 |
| `centos` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123.com` | 5 |
| `112233` | 4 |
| `` | 4 |
| `admin123` | 4 |
| `passwd` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Admin` | `123.com` | 5 |
| `debian` | `112233` | 4 |
| `admin` | `` | 4 |
| `centos` | `admin123` | 4 |
| `test` | `passwd` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `debian` | `112233` | `182.75.197.174` | 2026-08-12T08:55:09 |
| `debian` | `112233` | `197.155.225.93` | 2026-08-12T08:55:21 |
| `debian` | `112233` | `179.185.227.77` | 2026-08-12T08:55:29 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-12T09:00:11 |
| `ftpuser` | `1234` | `39.164.91.67` | 2026-08-12T09:00:53 |
| `nobody` | `123456` | `124.239.169.52` | 2026-08-12T09:06:02 |
| `root` | `66666` | `10.0.0.73` | 2026-08-12T09:11:00 |
| `centos` | `admin123` | `10.0.0.73` | 2026-08-12T09:13:52 |
| `centos` | `admin123` | `180.188.253.150` | 2026-08-12T09:15:30 |
| `support` | `support` | `10.0.0.73` | 2026-08-12T09:23:03 |
| `root` | `66666` | `211.53.58.10` | 2026-08-12T09:29:39 |
| `root` | `66666` | `138.118.213.68` | 2026-08-12T09:30:00 |
| `centos` | `admin123` | `151.237.170.49` | 2026-08-12T09:31:50 |
| `test` | `passwd` | `200.232.114.71` | 2026-08-12T09:40:23 |
| `test` | `passwd` | `85.152.57.60` | 2026-08-12T09:40:30 |
| `Admin` | `123.com` | `10.0.0.73` | 2026-08-12T09:48:14 |
| `Admin` | `123.com` | `122.170.100.253` | 2026-08-12T09:49:53 |
| `test` | `passwd` | `10.0.0.73` | 2026-08-12T09:51:52 |
| `support` | `support` | `176.53.159.196` | 2026-08-12T10:04:04 |
| `Admin` | `123.com` | `111.70.7.189` | 2026-08-12T10:06:09 |
| `Admin` | `123.com` | `178.178.222.53` | 2026-08-12T10:06:17 |
| `test` | `passwd` | `112.28.73.142` | 2026-08-12T10:09:28 |
| `debian` | `administrator` | `117.211.15.106` | 2026-08-12T10:14:32 |
| `unknown` | `qwer1234` | `178.178.222.59` | 2026-08-12T10:38:06 |
| `unknown` | `qwer1234` | `103.121.27.218` | 2026-08-12T10:38:14 |
| `debian` | `administrator` | `182.75.197.174` | 2026-08-12T10:43:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **83** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 22 |
| libssh | 7 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 22 | 19 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 22 | 19 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **57** |
| Unique ASNs | **48** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS211298` | Driftnet Ltd | 2 | HIGH |
| `AS25159` | PJSC MegaFon | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS30844` | Liquid Telecommunications Ltd | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-adb88007e211

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-12 08:55 |
| **Last Seen** | 2026-08-12 08:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:55:06` | `cowrie.session.connect` |
| `2026-08-12 08:55:07` | `cowrie.client.version` |
| `2026-08-12 08:55:07` | `cowrie.client.kex` |
| `2026-08-12 08:55:09` | `cowrie.login.success` |
| `2026-08-12 08:55:10` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a1db9dac3d

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-12 08:55 |
| **Last Seen** | 2026-08-12 08:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:55:15` | `cowrie.session.connect` |
| `2026-08-12 08:55:16` | `cowrie.client.version` |
| `2026-08-12 08:55:16` | `cowrie.client.kex` |
| `2026-08-12 08:55:17` | `cowrie.login.success` |
| `2026-08-12 08:55:18` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:55:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99d95e939a0

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-08-12 08:55 |
| **Last Seen** | 2026-08-12 08:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:55:19` | `cowrie.session.connect` |
| `2026-08-12 08:55:19` | `cowrie.client.version` |
| `2026-08-12 08:55:19` | `cowrie.client.kex` |
| `2026-08-12 08:55:21` | `cowrie.login.success` |
| `2026-08-12 08:55:22` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fed93f11775

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-08-12 08:55 |
| **Last Seen** | 2026-08-12 08:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 08:55:27` | `cowrie.session.connect` |
| `2026-08-12 08:55:28` | `cowrie.client.version` |
| `2026-08-12 08:55:28` | `cowrie.client.kex` |
| `2026-08-12 08:55:29` | `cowrie.login.success` |
| `2026-08-12 08:55:30` | `cowrie.direct-tcpip.request` |
| `2026-08-12 08:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a262e4f2e6fe

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-08-12 09:00 |
| **Last Seen** | 2026-08-12 09:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:00:50` | `cowrie.session.connect` |
| `2026-08-12 09:00:51` | `cowrie.client.version` |
| `2026-08-12 09:00:51` | `cowrie.client.kex` |
| `2026-08-12 09:00:53` | `cowrie.login.success` |
| `2026-08-12 09:00:53` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe6796c9dc4

| Field | Detail |
|---|---|
| **Source IP** | `39.164.91[.]67` |
| **First Seen** | 2026-08-12 09:01 |
| **Last Seen** | 2026-08-12 09:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:01:03` | `cowrie.session.connect` |
| `2026-08-12 09:01:04` | `cowrie.client.version` |
| `2026-08-12 09:01:04` | `cowrie.client.kex` |
| `2026-08-12 09:01:06` | `cowrie.login.success` |
| `2026-08-12 09:01:07` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.91[.]67` to AbuseIPDB if not already reported
- [ ] Block `39.164.91[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f2244810ce

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-12 09:05 |
| **Last Seen** | 2026-08-12 09:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:05:56` | `cowrie.session.connect` |
| `2026-08-12 09:05:58` | `cowrie.client.version` |
| `2026-08-12 09:05:58` | `cowrie.client.kex` |
| `2026-08-12 09:06:02` | `cowrie.login.success` |
| `2026-08-12 09:06:03` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94d2a7d0a70

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-08-12 09:15 |
| **Last Seen** | 2026-08-12 09:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:15:27` | `cowrie.session.connect` |
| `2026-08-12 09:15:28` | `cowrie.client.version` |
| `2026-08-12 09:15:28` | `cowrie.client.kex` |
| `2026-08-12 09:15:30` | `cowrie.login.success` |
| `2026-08-12 09:15:31` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a42e934493

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-08-12 09:29 |
| **Last Seen** | 2026-08-12 09:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:29:37` | `cowrie.session.connect` |
| `2026-08-12 09:29:37` | `cowrie.client.version` |
| `2026-08-12 09:29:37` | `cowrie.client.kex` |
| `2026-08-12 09:29:39` | `cowrie.login.success` |
| `2026-08-12 09:29:40` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-141b8201fdff

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-12 09:29 |
| **Last Seen** | 2026-08-12 09:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:29:57` | `cowrie.session.connect` |
| `2026-08-12 09:29:57` | `cowrie.client.version` |
| `2026-08-12 09:29:57` | `cowrie.client.kex` |
| `2026-08-12 09:30:00` | `cowrie.login.success` |
| `2026-08-12 09:30:00` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eea646742c6

| Field | Detail |
|---|---|
| **Source IP** | `151.237.170[.]49` |
| **First Seen** | 2026-08-12 09:31 |
| **Last Seen** | 2026-08-12 09:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:31:47` | `cowrie.session.connect` |
| `2026-08-12 09:31:48` | `cowrie.client.version` |
| `2026-08-12 09:31:48` | `cowrie.client.kex` |
| `2026-08-12 09:31:50` | `cowrie.login.success` |
| `2026-08-12 09:31:50` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.237.170[.]49` to AbuseIPDB if not already reported
- [ ] Block `151.237.170[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2708ab7b29

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-12 09:40 |
| **Last Seen** | 2026-08-12 09:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:40:20` | `cowrie.session.connect` |
| `2026-08-12 09:40:21` | `cowrie.client.version` |
| `2026-08-12 09:40:21` | `cowrie.client.kex` |
| `2026-08-12 09:40:23` | `cowrie.login.success` |
| `2026-08-12 09:40:23` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fec9e04a448

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-12 09:40 |
| **Last Seen** | 2026-08-12 09:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:40:28` | `cowrie.session.connect` |
| `2026-08-12 09:40:29` | `cowrie.client.version` |
| `2026-08-12 09:40:29` | `cowrie.client.kex` |
| `2026-08-12 09:40:30` | `cowrie.login.success` |
| `2026-08-12 09:40:30` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d5fa6412b88

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-12 09:49 |
| **Last Seen** | 2026-08-12 09:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 09:49:51` | `cowrie.session.connect` |
| `2026-08-12 09:49:51` | `cowrie.client.version` |
| `2026-08-12 09:49:51` | `cowrie.client.kex` |
| `2026-08-12 09:49:53` | `cowrie.login.success` |
| `2026-08-12 09:49:54` | `cowrie.direct-tcpip.request` |
| `2026-08-12 09:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922bec46dec1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-12 10:04 |
| **Last Seen** | 2026-08-12 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:04:04` | `cowrie.session.connect` |
| `2026-08-12 10:04:04` | `cowrie.client.version` |
| `2026-08-12 10:04:04` | `cowrie.client.kex` |
| `2026-08-12 10:04:04` | `cowrie.login.success` |
| `2026-08-12 10:04:04` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:04:04` | `cowrie.direct-tcpip.data` |
| `2026-08-12 10:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f37ed0d234

| Field | Detail |
|---|---|
| **Source IP** | `111.70.7[.]189` |
| **First Seen** | 2026-08-12 10:06 |
| **Last Seen** | 2026-08-12 10:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:06:07` | `cowrie.session.connect` |
| `2026-08-12 10:06:07` | `cowrie.client.version` |
| `2026-08-12 10:06:07` | `cowrie.client.kex` |
| `2026-08-12 10:06:09` | `cowrie.login.success` |
| `2026-08-12 10:06:10` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.7[.]189` to AbuseIPDB if not already reported
- [ ] Block `111.70.7[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add61e56d6de

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-08-12 10:06 |
| **Last Seen** | 2026-08-12 10:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:06:15` | `cowrie.session.connect` |
| `2026-08-12 10:06:16` | `cowrie.client.version` |
| `2026-08-12 10:06:16` | `cowrie.client.kex` |
| `2026-08-12 10:06:17` | `cowrie.login.success` |
| `2026-08-12 10:06:17` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e4d9360472

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-08-12 10:09 |
| **Last Seen** | 2026-08-12 10:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:09:25` | `cowrie.session.connect` |
| `2026-08-12 10:09:25` | `cowrie.client.version` |
| `2026-08-12 10:09:25` | `cowrie.client.kex` |
| `2026-08-12 10:09:28` | `cowrie.login.success` |
| `2026-08-12 10:09:28` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee418da1308a

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-12 10:14 |
| **Last Seen** | 2026-08-12 10:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:14:29` | `cowrie.session.connect` |
| `2026-08-12 10:14:30` | `cowrie.client.version` |
| `2026-08-12 10:14:30` | `cowrie.client.kex` |
| `2026-08-12 10:14:32` | `cowrie.login.success` |
| `2026-08-12 10:14:33` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c5975f6441

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-12 10:38 |
| **Last Seen** | 2026-08-12 10:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:38:05` | `cowrie.session.connect` |
| `2026-08-12 10:38:06` | `cowrie.client.version` |
| `2026-08-12 10:38:06` | `cowrie.client.kex` |
| `2026-08-12 10:38:06` | `cowrie.login.success` |
| `2026-08-12 10:38:07` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af4f59793da

| Field | Detail |
|---|---|
| **Source IP** | `103.121.27[.]218` |
| **First Seen** | 2026-08-12 10:38 |
| **Last Seen** | 2026-08-12 10:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:38:12` | `cowrie.session.connect` |
| `2026-08-12 10:38:12` | `cowrie.client.version` |
| `2026-08-12 10:38:12` | `cowrie.client.kex` |
| `2026-08-12 10:38:14` | `cowrie.login.success` |
| `2026-08-12 10:38:14` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.121.27[.]218` to AbuseIPDB if not already reported
- [ ] Block `103.121.27[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ffb5ad67e6

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-12 10:43 |
| **Last Seen** | 2026-08-12 10:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-12 10:43:23` | `cowrie.session.connect` |
| `2026-08-12 10:43:24` | `cowrie.client.version` |
| `2026-08-12 10:43:24` | `cowrie.client.kex` |
| `2026-08-12 10:43:26` | `cowrie.login.success` |
| `2026-08-12 10:43:26` | `cowrie.direct-tcpip.request` |
| `2026-08-12 10:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **8** | 2026-08-12 08:57 | 2026-08-12 10:51 | 8m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-12 08:56 | 2026-08-12 10:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-12 09:47 | 2026-08-12 09:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-12 09:07 | 2026-08-12 09:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-12 10:41 | 2026-08-12 10:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-12 09:06 | 2026-08-12 10:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `146.158.99[.]226` | **2** | 2026-08-12 10:21 | 2026-08-12 10:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | **2** | 2026-08-12 08:55 | 2026-08-12 10:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `181.167.54[.]6` | **2** | 2026-08-12 09:28 | 2026-08-12 09:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]173` | **2** | 2026-08-12 10:20 | 2026-08-12 10:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.80.39[.]74` | 1 | 2026-08-12 10:09 | 2026-08-12 10:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.117.219[.]87` | 1 | 2026-08-12 10:39 | 2026-08-12 10:39 | 11s | 0 | `T1592` | 🟢 LOW |
| `124.152.90[.]68` | 1 | 2026-08-12 10:06 | 2026-08-12 10:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `125.227.240[.]43` | 1 | 2026-08-12 09:29 | 2026-08-12 09:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.220.244[.]134` | 1 | 2026-08-12 10:40 | 2026-08-12 10:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.154.172[.]19` | 1 | 2026-08-12 09:16 | 2026-08-12 09:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.44.26[.]41` | 1 | 2026-08-12 09:37 | 2026-08-12 09:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]202` | 1 | 2026-08-12 09:51 | 2026-08-12 09:51 | 2s | 0 | `T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-08-12 09:06 | 2026-08-12 09:06 | 6s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-08-12 09:29 | 2026-08-12 09:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.123.124[.]176` | 1 | 2026-08-12 09:31 | 2026-08-12 09:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.87.200[.]141` | 1 | 2026-08-12 09:29 | 2026-08-12 09:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-08-12 09:35 | 2026-08-12 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-12 09:10 | 2026-08-12 09:11 | 53s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |

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

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `125.227.240[.]43` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 4 |
| `117.211.15[.]106` | IN | O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `194.44.26[.]41` | UA | TzOV Biznes i Technologii | **100** ⚠️ | 1 |
| `41.87.200[.]141` | ZA | CipherWave | **100** ⚠️ | 0 |
| `112.28.73[.]142` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `124.152.90[.]68` | CN | China Unicom Gansu province network | **100** ⚠️ | 50 |
| `181.167.54[.]6` | AR | Telecom Argentina S.A. | **100** ⚠️ | 0 |
| `211.220.156[.]232` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `122.170.100[.]253` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `103.121.27[.]218` | IN | HiPOINT Connect Private Limited | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 83 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 57 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (18.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 24 recon entry/entries in table (10 group(s) consolidating 32 session(s)).

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
_Report time: 2026-08-12T11:02:27Z_

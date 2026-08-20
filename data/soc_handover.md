# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-20 |
| **Generated At** | 2026-08-20T16:40:44Z |
| **Shift Time** | 16:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **128** |
| Confirmed Threats | **125** |
| False Positives Filtered | **3** (2.3%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **22** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **3** HIGH · **21** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **85** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **9** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 26 |
| `unknown` | 13 |
| `admin` | 12 |
| `ubuntu` | 11 |
| `blank` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `blank2016` | 6 |
| `user2019` | 6 |
| `LeitboGi0ro` | 5 |
| `techsupport` | 5 |
| `unknown2006` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `blank2016` | 6 |
| `user` | `user2019` | 6 |
| `root` | `LeitboGi0ro` | 5 |
| `unknown` | `techsupport` | 5 |
| `unknown` | `unknown2006` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `Dd@2024` | `217.60.255.130` | 2026-08-20T12:57:16 |
| `centos` | `centos2009` | `187.115.144.103` | 2026-08-20T12:57:49 |
| `support` | `support` | `10.0.0.73` | 2026-08-20T12:58:47 |
| `root` | `2014` | `217.60.255.130` | 2026-08-20T13:01:23 |
| `support` | `support2015` | `117.70.94.155` | 2026-08-20T13:03:13 |
| `blank` | `blank2016` | `27.223.98.117` | 2026-08-20T13:08:05 |
| `blank` | `blank2016` | `103.31.39.188` | 2026-08-20T13:08:18 |
| `ubuntu` | `Welcome@123` | `217.60.255.130` | 2026-08-20T13:08:37 |
| `admin` | `admin` | `193.23.218.86` | 2026-08-20T13:09:15 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-20T13:09:19 |
| `test` | `test2015` | `69.172.79.198` | 2026-08-20T13:12:13 |
| `test` | `test2015` | `14.97.77.182` | 2026-08-20T13:12:21 |
| `test` | `test2015` | `210.13.99.66` | 2026-08-20T13:12:27 |
| `root` | `2016` | `217.60.255.130` | 2026-08-20T13:12:35 |
| `test` | `test2015` | `125.139.124.120` | 2026-08-20T13:12:36 |
| `root` | `root2005` | `10.0.0.73` | 2026-08-20T13:14:04 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-20T13:15:26 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-20T13:15:28 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-20T13:15:32 |
| `root` | `root2005` | `196.219.75.143` | 2026-08-20T13:15:33 |
| `blank` | `blank2016` | `10.0.0.73` | 2026-08-20T13:19:40 |
| `ubuntu` | `Huawei@123` | `217.60.255.130` | 2026-08-20T13:19:50 |
| `root` | `2222` | `217.60.255.130` | 2026-08-20T13:23:35 |
| `blank` | `blank2024` | `10.0.0.73` | 2026-08-20T13:27:38 |
| `ubuntu` | `Abcd1234` | `217.60.255.130` | 2026-08-20T13:31:01 |
| `root` | `root2005` | `121.202.206.119` | 2026-08-20T13:31:48 |
| `root` | `root2005` | `188.219.104.210` | 2026-08-20T13:31:56 |
| `root` | `2233` | `217.60.255.130` | 2026-08-20T13:34:35 |
| `blank` | `blank2016` | `82.193.122.91` | 2026-08-20T13:36:29 |
| `blank` | `blank2016` | `116.113.241.82` | 2026-08-20T13:36:39 |
| `unknown` | `techsupport` | `122.187.229.220` | 2026-08-20T13:41:44 |
| `unknown` | `techsupport` | `121.159.71.249` | 2026-08-20T13:41:53 |
| `ubuntu` | `admin!@#123` | `217.60.255.130` | 2026-08-20T13:41:58 |
| `root` | `3333` | `217.60.255.130` | 2026-08-20T13:45:25 |
| `blank` | `blank2024` | `186.239.41.74` | 2026-08-20T13:45:57 |
| `blank` | `blank2024` | `43.248.213.232` | 2026-08-20T13:46:02 |
| `blank` | `blank2024` | `182.75.197.174` | 2026-08-20T13:46:12 |
| `unknown` | `unknown2019` | `117.211.15.106` | 2026-08-20T13:49:31 |
| `unknown` | `unknown2019` | `59.11.202.38` | 2026-08-20T13:49:43 |
| `ubuntu` | `P@ssw0rd123!` | `217.60.255.130` | 2026-08-20T13:52:56 |
| `unknown` | `techsupport` | `10.0.0.73` | 2026-08-20T13:53:15 |
| `root` | `4321` | `217.60.255.130` | 2026-08-20T13:56:17 |
| `admin` | `admin2022` | `10.0.0.73` | 2026-08-20T14:01:10 |
| `ubuntu` | `anonymous@123` | `217.60.255.130` | 2026-08-20T14:03:54 |
| `unknown` | `unknown2019` | `117.247.77.115` | 2026-08-20T14:05:44 |
| `root` | `5555` | `217.60.255.130` | 2026-08-20T14:06:55 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-20T14:09:55 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-20T14:09:55 |
| `unknown` | `techsupport` | `210.206.24.237` | 2026-08-20T14:10:21 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-20T14:11:20 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-20T14:11:20 |
| `ubuntu` | `Anonymous@123` | `217.60.255.130` | 2026-08-20T14:14:41 |
| `root` | `8520` | `217.60.255.130` | 2026-08-20T14:17:37 |
| `admin` | `admin2022` | `65.20.187.47` | 2026-08-20T14:19:38 |
| `admin` | `admin2022` | `14.99.61.248` | 2026-08-20T14:19:47 |
| `unknown` | `unknown2006` | `10.0.0.73` | 2026-08-20T14:21:56 |
| `unknown` | `unknown2006` | `62.182.132.94` | 2026-08-20T14:23:27 |
| `unknown` | `unknown2006` | `24.207.66.154` | 2026-08-20T14:23:35 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-20T14:24:09 |
| `ubuntu` | `It123` | `217.60.255.130` | 2026-08-20T14:26:23 |
| `admin` | `admin2008` | `10.0.0.73` | 2026-08-20T14:26:55 |
| `root` | `8888` | `217.60.255.130` | 2026-08-20T14:28:24 |
| `user` | `user2019` | `10.0.0.73` | 2026-08-20T14:34:54 |
| `ubuntu` | `Welcome1234!` | `217.60.255.130` | 2026-08-20T14:36:30 |
| `root` | `﻿------fuck------` | `219.140.105.152` | 2026-08-20T14:38:48 |
| `root` | `9090` | `217.60.255.130` | 2026-08-20T14:39:20 |
| `unknown` | `unknown2006` | `125.69.76.148` | 2026-08-20T14:39:32 |
| `admin` | `admin2008` | `49.124.151.23` | 2026-08-20T14:43:55 |
| `admin` | `admin2008` | `171.217.70.151` | 2026-08-20T14:44:08 |
| `ubuntu` | `fuck` | `217.60.255.130` | 2026-08-20T14:47:31 |
| `root` | `9999` | `217.60.255.130` | 2026-08-20T14:50:04 |
| `user` | `user2019` | `81.195.152.14` | 2026-08-20T14:53:12 |
| `user` | `user2019` | `185.2.228.48` | 2026-08-20T14:53:24 |
| `user` | `user2019` | `117.2.123.19` | 2026-08-20T14:53:26 |
| `user` | `user2019` | `201.63.52.54` | 2026-08-20T14:53:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **128** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 34 |
| libssh | 27 |
| Paramiko (Python) | 10 |
| Go SSH scanner | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 34 | 34 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 34 | 34 | Mirai/variant |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **44** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS45820` | Tata Teleservices ISP AS | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (68)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f19f71c0d5c9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 12:57 |
| **Last Seen** | 2026-08-20 12:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:57:12` | `cowrie.session.connect` |
| `2026-08-20 12:57:12` | `cowrie.client.version` |
| `2026-08-20 12:57:13` | `cowrie.client.kex` |
| `2026-08-20 12:57:16` | `cowrie.login.success` |
| `2026-08-20 12:57:18` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:57:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 12:57:19` | `cowrie.direct-tcpip.data` |
| `2026-08-20 12:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b23dae35196

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-20 12:57 |
| **Last Seen** | 2026-08-20 12:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 12:57:44` | `cowrie.session.connect` |
| `2026-08-20 12:57:46` | `cowrie.client.version` |
| `2026-08-20 12:57:46` | `cowrie.client.kex` |
| `2026-08-20 12:57:49` | `cowrie.login.success` |
| `2026-08-20 12:57:50` | `cowrie.direct-tcpip.request` |
| `2026-08-20 12:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca68d1c9ceb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:01 |
| **Last Seen** | 2026-08-20 13:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:01:22` | `cowrie.session.connect` |
| `2026-08-20 13:01:22` | `cowrie.client.version` |
| `2026-08-20 13:01:23` | `cowrie.client.kex` |
| `2026-08-20 13:01:23` | `cowrie.login.success` |
| `2026-08-20 13:01:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:01:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:01:25` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9f19340c07

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-08-20 13:03 |
| **Last Seen** | 2026-08-20 13:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:03:02` | `cowrie.session.connect` |
| `2026-08-20 13:03:05` | `cowrie.client.version` |
| `2026-08-20 13:03:05` | `cowrie.client.kex` |
| `2026-08-20 13:03:13` | `cowrie.login.success` |
| `2026-08-20 13:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df83f358e0f

| Field | Detail |
|---|---|
| **Source IP** | `27.223.98[.]117` |
| **First Seen** | 2026-08-20 13:08 |
| **Last Seen** | 2026-08-20 13:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:08:03` | `cowrie.session.connect` |
| `2026-08-20 13:08:03` | `cowrie.client.version` |
| `2026-08-20 13:08:03` | `cowrie.client.kex` |
| `2026-08-20 13:08:05` | `cowrie.login.success` |
| `2026-08-20 13:08:06` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.223.98[.]117` to AbuseIPDB if not already reported
- [ ] Block `27.223.98[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1850ce17ee0

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-08-20 13:08 |
| **Last Seen** | 2026-08-20 13:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:08:12` | `cowrie.session.connect` |
| `2026-08-20 13:08:14` | `cowrie.client.version` |
| `2026-08-20 13:08:14` | `cowrie.client.kex` |
| `2026-08-20 13:08:18` | `cowrie.login.success` |
| `2026-08-20 13:08:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351674651719

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:08 |
| **Last Seen** | 2026-08-20 13:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:08:33` | `cowrie.session.connect` |
| `2026-08-20 13:08:34` | `cowrie.client.version` |
| `2026-08-20 13:08:34` | `cowrie.client.kex` |
| `2026-08-20 13:08:37` | `cowrie.login.success` |
| `2026-08-20 13:08:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:08:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:08:39` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4fe7f442f4

| Field | Detail |
|---|---|
| **Source IP** | `193.23.218[.]86` |
| **First Seen** | 2026-08-20 13:09 |
| **Last Seen** | 2026-08-20 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:09:14` | `cowrie.session.connect` |
| `2026-08-20 13:09:15` | `cowrie.client.version` |
| `2026-08-20 13:09:15` | `cowrie.client.kex` |
| `2026-08-20 13:09:15` | `cowrie.login.success` |
| `2026-08-20 13:09:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.23.218[.]86` to AbuseIPDB if not already reported
- [ ] Block `193.23.218[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7738582d292f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-20 13:09 |
| **Last Seen** | 2026-08-20 13:09 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:09:16` | `cowrie.session.connect` |
| `2026-08-20 13:09:16` | `cowrie.client.version` |
| `2026-08-20 13:09:16` | `cowrie.client.kex` |
| `2026-08-20 13:09:19` | `cowrie.login.success` |
| `2026-08-20 13:09:22` | `cowrie.session.params` |
| `2026-08-20 13:09:22` | `cowrie.command.input` |
| `2026-08-20 13:09:22` | `cowrie.session.file_download` |
| `2026-08-20 13:09:22` | `cowrie.session.file_download` |
| `2026-08-20 13:09:22` | `cowrie.log.closed` |
| `2026-08-20 13:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922e062a86e4

| Field | Detail |
|---|---|
| **Source IP** | `69.172.79[.]198` |
| **First Seen** | 2026-08-20 13:12 |
| **Last Seen** | 2026-08-20 13:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:12:10` | `cowrie.session.connect` |
| `2026-08-20 13:12:10` | `cowrie.client.version` |
| `2026-08-20 13:12:10` | `cowrie.client.kex` |
| `2026-08-20 13:12:13` | `cowrie.login.success` |
| `2026-08-20 13:12:14` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.172.79[.]198` to AbuseIPDB if not already reported
- [ ] Block `69.172.79[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8651d8ede1c8

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-08-20 13:12 |
| **Last Seen** | 2026-08-20 13:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:12:19` | `cowrie.session.connect` |
| `2026-08-20 13:12:19` | `cowrie.client.version` |
| `2026-08-20 13:12:19` | `cowrie.client.kex` |
| `2026-08-20 13:12:21` | `cowrie.login.success` |
| `2026-08-20 13:12:22` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3fcc5e89a09

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-08-20 13:12 |
| **Last Seen** | 2026-08-20 13:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:12:24` | `cowrie.session.connect` |
| `2026-08-20 13:12:24` | `cowrie.client.version` |
| `2026-08-20 13:12:24` | `cowrie.client.kex` |
| `2026-08-20 13:12:27` | `cowrie.login.success` |
| `2026-08-20 13:12:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10ad83812d0c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:12 |
| **Last Seen** | 2026-08-20 13:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:12:32` | `cowrie.session.connect` |
| `2026-08-20 13:12:32` | `cowrie.client.version` |
| `2026-08-20 13:12:32` | `cowrie.client.kex` |
| `2026-08-20 13:12:35` | `cowrie.login.success` |
| `2026-08-20 13:12:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:12:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:12:44` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf961e7fafd0

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-08-20 13:12 |
| **Last Seen** | 2026-08-20 13:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:12:33` | `cowrie.session.connect` |
| `2026-08-20 13:12:34` | `cowrie.client.version` |
| `2026-08-20 13:12:34` | `cowrie.client.kex` |
| `2026-08-20 13:12:36` | `cowrie.login.success` |
| `2026-08-20 13:12:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7369e13da067

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-20 13:15 |
| **Last Seen** | 2026-08-20 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:15:26` | `cowrie.session.connect` |
| `2026-08-20 13:15:26` | `cowrie.client.version` |
| `2026-08-20 13:15:26` | `cowrie.client.kex` |
| `2026-08-20 13:15:26` | `cowrie.login.success` |
| `2026-08-20 13:15:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72664e04af0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-20 13:15 |
| **Last Seen** | 2026-08-20 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:15:28` | `cowrie.session.connect` |
| `2026-08-20 13:15:28` | `cowrie.client.version` |
| `2026-08-20 13:15:28` | `cowrie.client.kex` |
| `2026-08-20 13:15:28` | `cowrie.login.success` |
| `2026-08-20 13:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97a30b65ac7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-20 13:15 |
| **Last Seen** | 2026-08-20 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:15:31` | `cowrie.session.connect` |
| `2026-08-20 13:15:31` | `cowrie.client.version` |
| `2026-08-20 13:15:31` | `cowrie.client.kex` |
| `2026-08-20 13:15:32` | `cowrie.login.success` |
| `2026-08-20 13:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5a1dd79aae

| Field | Detail |
|---|---|
| **Source IP** | `196.219.75[.]143` |
| **First Seen** | 2026-08-20 13:15 |
| **Last Seen** | 2026-08-20 13:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:15:32` | `cowrie.session.connect` |
| `2026-08-20 13:15:32` | `cowrie.client.version` |
| `2026-08-20 13:15:32` | `cowrie.client.kex` |
| `2026-08-20 13:15:33` | `cowrie.login.success` |
| `2026-08-20 13:15:34` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.75[.]143` to AbuseIPDB if not already reported
- [ ] Block `196.219.75[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7926f94847c7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-20 13:15 |
| **Last Seen** | 2026-08-20 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:15:32` | `cowrie.session.connect` |
| `2026-08-20 13:15:32` | `cowrie.client.version` |
| `2026-08-20 13:15:32` | `cowrie.client.kex` |
| `2026-08-20 13:15:33` | `cowrie.login.success` |
| `2026-08-20 13:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c355b3af958

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:19 |
| **Last Seen** | 2026-08-20 13:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:19:48` | `cowrie.session.connect` |
| `2026-08-20 13:19:48` | `cowrie.client.version` |
| `2026-08-20 13:19:48` | `cowrie.client.kex` |
| `2026-08-20 13:19:50` | `cowrie.login.success` |
| `2026-08-20 13:19:51` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:19:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:19:53` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5835ab77df

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:23 |
| **Last Seen** | 2026-08-20 13:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:23:31` | `cowrie.session.connect` |
| `2026-08-20 13:23:31` | `cowrie.client.version` |
| `2026-08-20 13:23:31` | `cowrie.client.kex` |
| `2026-08-20 13:23:35` | `cowrie.login.success` |
| `2026-08-20 13:23:41` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105443232608

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:30 |
| **Last Seen** | 2026-08-20 13:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:30:58` | `cowrie.session.connect` |
| `2026-08-20 13:30:58` | `cowrie.client.version` |
| `2026-08-20 13:30:58` | `cowrie.client.kex` |
| `2026-08-20 13:31:01` | `cowrie.login.success` |
| `2026-08-20 13:31:01` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:31:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:31:02` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404184fb596a

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-08-20 13:31 |
| **Last Seen** | 2026-08-20 13:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:31:44` | `cowrie.session.connect` |
| `2026-08-20 13:31:45` | `cowrie.client.version` |
| `2026-08-20 13:31:45` | `cowrie.client.kex` |
| `2026-08-20 13:31:48` | `cowrie.login.success` |
| `2026-08-20 13:31:49` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c130e51adf

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-08-20 13:31 |
| **Last Seen** | 2026-08-20 13:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:31:55` | `cowrie.session.connect` |
| `2026-08-20 13:31:55` | `cowrie.client.version` |
| `2026-08-20 13:31:55` | `cowrie.client.kex` |
| `2026-08-20 13:31:56` | `cowrie.login.success` |
| `2026-08-20 13:31:57` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7007aaba7f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:34 |
| **Last Seen** | 2026-08-20 13:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:34:30` | `cowrie.session.connect` |
| `2026-08-20 13:34:31` | `cowrie.client.version` |
| `2026-08-20 13:34:31` | `cowrie.client.kex` |
| `2026-08-20 13:34:35` | `cowrie.login.success` |
| `2026-08-20 13:34:35` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:34:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:34:42` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e15281f2ef32

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-08-20 13:36 |
| **Last Seen** | 2026-08-20 13:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:36:27` | `cowrie.session.connect` |
| `2026-08-20 13:36:28` | `cowrie.client.version` |
| `2026-08-20 13:36:28` | `cowrie.client.kex` |
| `2026-08-20 13:36:29` | `cowrie.login.success` |
| `2026-08-20 13:36:29` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89f1daeeea5

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-08-20 13:36 |
| **Last Seen** | 2026-08-20 13:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:36:36` | `cowrie.session.connect` |
| `2026-08-20 13:36:37` | `cowrie.client.version` |
| `2026-08-20 13:36:37` | `cowrie.client.kex` |
| `2026-08-20 13:36:39` | `cowrie.login.success` |
| `2026-08-20 13:36:40` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d7e47ed004

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]220` |
| **First Seen** | 2026-08-20 13:41 |
| **Last Seen** | 2026-08-20 13:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:41:41` | `cowrie.session.connect` |
| `2026-08-20 13:41:42` | `cowrie.client.version` |
| `2026-08-20 13:41:42` | `cowrie.client.kex` |
| `2026-08-20 13:41:44` | `cowrie.login.success` |
| `2026-08-20 13:41:45` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b35ea319d72c

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-08-20 13:41 |
| **Last Seen** | 2026-08-20 13:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:41:50` | `cowrie.session.connect` |
| `2026-08-20 13:41:51` | `cowrie.client.version` |
| `2026-08-20 13:41:51` | `cowrie.client.kex` |
| `2026-08-20 13:41:53` | `cowrie.login.success` |
| `2026-08-20 13:41:54` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dbff65deb3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:41 |
| **Last Seen** | 2026-08-20 13:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:41:56` | `cowrie.session.connect` |
| `2026-08-20 13:41:56` | `cowrie.client.version` |
| `2026-08-20 13:41:56` | `cowrie.client.kex` |
| `2026-08-20 13:41:58` | `cowrie.login.success` |
| `2026-08-20 13:41:58` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:42:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:42:00` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e480c4ee48

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:45 |
| **Last Seen** | 2026-08-20 13:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:45:23` | `cowrie.session.connect` |
| `2026-08-20 13:45:23` | `cowrie.client.version` |
| `2026-08-20 13:45:23` | `cowrie.client.kex` |
| `2026-08-20 13:45:25` | `cowrie.login.success` |
| `2026-08-20 13:45:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:45:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:45:26` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8c33d8106c

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-20 13:45 |
| **Last Seen** | 2026-08-20 13:46 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:45:50` | `cowrie.session.connect` |
| `2026-08-20 13:45:53` | `cowrie.client.version` |
| `2026-08-20 13:45:53` | `cowrie.client.kex` |
| `2026-08-20 13:45:57` | `cowrie.login.success` |
| `2026-08-20 13:45:59` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-444b710937fe

| Field | Detail |
|---|---|
| **Source IP** | `43.248.213[.]232` |
| **First Seen** | 2026-08-20 13:46 |
| **Last Seen** | 2026-08-20 13:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:46:00` | `cowrie.session.connect` |
| `2026-08-20 13:46:00` | `cowrie.client.version` |
| `2026-08-20 13:46:00` | `cowrie.client.kex` |
| `2026-08-20 13:46:02` | `cowrie.login.success` |
| `2026-08-20 13:46:03` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.213[.]232` to AbuseIPDB if not already reported
- [ ] Block `43.248.213[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-820f958550bf

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-20 13:46 |
| **Last Seen** | 2026-08-20 13:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:46:09` | `cowrie.session.connect` |
| `2026-08-20 13:46:10` | `cowrie.client.version` |
| `2026-08-20 13:46:10` | `cowrie.client.kex` |
| `2026-08-20 13:46:12` | `cowrie.login.success` |
| `2026-08-20 13:46:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b771ce29e692

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-20 13:49 |
| **Last Seen** | 2026-08-20 13:49 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:49:27` | `cowrie.session.connect` |
| `2026-08-20 13:49:29` | `cowrie.client.version` |
| `2026-08-20 13:49:29` | `cowrie.client.kex` |
| `2026-08-20 13:49:31` | `cowrie.login.success` |
| `2026-08-20 13:49:32` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdbd63d5a832

| Field | Detail |
|---|---|
| **Source IP** | `59.11.202[.]38` |
| **First Seen** | 2026-08-20 13:49 |
| **Last Seen** | 2026-08-20 13:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:49:39` | `cowrie.session.connect` |
| `2026-08-20 13:49:40` | `cowrie.client.version` |
| `2026-08-20 13:49:40` | `cowrie.client.kex` |
| `2026-08-20 13:49:43` | `cowrie.login.success` |
| `2026-08-20 13:49:44` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.11.202[.]38` to AbuseIPDB if not already reported
- [ ] Block `59.11.202[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2bf1e0cd7b7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:52 |
| **Last Seen** | 2026-08-20 13:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:52:53` | `cowrie.session.connect` |
| `2026-08-20 13:52:53` | `cowrie.client.version` |
| `2026-08-20 13:52:53` | `cowrie.client.kex` |
| `2026-08-20 13:52:56` | `cowrie.login.success` |
| `2026-08-20 13:52:56` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:52:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:52:56` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc53f1f319c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 13:56 |
| **Last Seen** | 2026-08-20 13:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 13:56:14` | `cowrie.session.connect` |
| `2026-08-20 13:56:14` | `cowrie.client.version` |
| `2026-08-20 13:56:14` | `cowrie.client.kex` |
| `2026-08-20 13:56:17` | `cowrie.login.success` |
| `2026-08-20 13:56:19` | `cowrie.direct-tcpip.request` |
| `2026-08-20 13:56:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 13:56:19` | `cowrie.direct-tcpip.data` |
| `2026-08-20 13:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51fc78f646ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:03 |
| **Last Seen** | 2026-08-20 14:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:03:51` | `cowrie.session.connect` |
| `2026-08-20 14:03:51` | `cowrie.client.version` |
| `2026-08-20 14:03:52` | `cowrie.client.kex` |
| `2026-08-20 14:03:54` | `cowrie.login.success` |
| `2026-08-20 14:03:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:03:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:03:55` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9ed7311cef

| Field | Detail |
|---|---|
| **Source IP** | `117.247.77[.]115` |
| **First Seen** | 2026-08-20 14:05 |
| **Last Seen** | 2026-08-20 14:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:05:42` | `cowrie.session.connect` |
| `2026-08-20 14:05:42` | `cowrie.client.version` |
| `2026-08-20 14:05:42` | `cowrie.client.kex` |
| `2026-08-20 14:05:44` | `cowrie.login.success` |
| `2026-08-20 14:05:45` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.77[.]115` to AbuseIPDB if not already reported
- [ ] Block `117.247.77[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f3f947db7bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:06 |
| **Last Seen** | 2026-08-20 14:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:06:51` | `cowrie.session.connect` |
| `2026-08-20 14:06:51` | `cowrie.client.version` |
| `2026-08-20 14:06:52` | `cowrie.client.kex` |
| `2026-08-20 14:06:55` | `cowrie.login.success` |
| `2026-08-20 14:06:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:06:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:06:56` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc8261b0dee

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-20 14:09 |
| **Last Seen** | 2026-08-20 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:09:55` | `cowrie.session.connect` |
| `2026-08-20 14:09:55` | `cowrie.client.version` |
| `2026-08-20 14:09:55` | `cowrie.client.kex` |
| `2026-08-20 14:09:55` | `cowrie.login.success` |
| `2026-08-20 14:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cfca7b80fc

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-20 14:09 |
| **Last Seen** | 2026-08-20 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:09:55` | `cowrie.session.connect` |
| `2026-08-20 14:09:55` | `cowrie.client.version` |
| `2026-08-20 14:09:55` | `cowrie.client.kex` |
| `2026-08-20 14:09:55` | `cowrie.login.success` |
| `2026-08-20 14:09:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fc05262bf3

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-20 14:09 |
| **Last Seen** | 2026-08-20 14:12 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:09:58` | `cowrie.session.connect` |
| `2026-08-20 14:09:58` | `cowrie.client.version` |
| `2026-08-20 14:09:58` | `cowrie.client.kex` |
| `2026-08-20 14:09:58` | `cowrie.login.success` |
| `2026-08-20 14:09:59` | `cowrie.session.file_upload` |
| `2026-08-20 14:10:00` | `cowrie.session.params` |
| `2026-08-20 14:10:00` | `cowrie.command.input` |
| `2026-08-20 14:10:00` | `cowrie.command.input` |
| `2026-08-20 14:10:00` | `cowrie.command.input` |
| `2026-08-20 14:10:00` | `cowrie.command.failed` |
| `2026-08-20 14:10:00` | `cowrie.log.closed` |
| `2026-08-20 14:10:01` | `cowrie.session.params` |
| `2026-08-20 14:10:01` | `cowrie.command.input` |
| `2026-08-20 14:10:01` | `cowrie.log.closed` |
| `2026-08-20 14:10:02` | `cowrie.session.params` |
| `2026-08-20 14:10:02` | `cowrie.command.input` |
| `2026-08-20 14:10:02` | `cowrie.log.closed` |
| `2026-08-20 14:10:03` | `cowrie.session.params` |
| `2026-08-20 14:10:03` | `cowrie.command.input` |
| `2026-08-20 14:10:03` | `cowrie.command.failed` |
| `2026-08-20 14:10:03` | `cowrie.command.failed` |
| `2026-08-20 14:11:03` | `cowrie.session.params` |
| `2026-08-20 14:11:03` | `cowrie.command.input` |
| `2026-08-20 14:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d847d9b6004a

| Field | Detail |
|---|---|
| **Source IP** | `210.206.24[.]237` |
| **First Seen** | 2026-08-20 14:10 |
| **Last Seen** | 2026-08-20 14:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:10:18` | `cowrie.session.connect` |
| `2026-08-20 14:10:19` | `cowrie.client.version` |
| `2026-08-20 14:10:19` | `cowrie.client.kex` |
| `2026-08-20 14:10:21` | `cowrie.login.success` |
| `2026-08-20 14:10:21` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.206.24[.]237` to AbuseIPDB if not already reported
- [ ] Block `210.206.24[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e5499825e4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 14:11 |
| **Last Seen** | 2026-08-20 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:11:19` | `cowrie.session.connect` |
| `2026-08-20 14:11:19` | `cowrie.client.version` |
| `2026-08-20 14:11:19` | `cowrie.client.kex` |
| `2026-08-20 14:11:20` | `cowrie.login.success` |
| `2026-08-20 14:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbee0c8b8350

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-20 14:11 |
| **Last Seen** | 2026-08-20 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:11:19` | `cowrie.session.connect` |
| `2026-08-20 14:11:19` | `cowrie.client.version` |
| `2026-08-20 14:11:20` | `cowrie.client.kex` |
| `2026-08-20 14:11:20` | `cowrie.login.success` |
| `2026-08-20 14:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42fc5c9cc67

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-20 14:12 |
| **Last Seen** | 2026-08-20 14:14 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:12:05` | `cowrie.session.connect` |
| `2026-08-20 14:12:05` | `cowrie.client.version` |
| `2026-08-20 14:12:05` | `cowrie.client.kex` |
| `2026-08-20 14:12:05` | `cowrie.login.success` |
| `2026-08-20 14:12:06` | `cowrie.session.file_upload` |
| `2026-08-20 14:12:07` | `cowrie.session.params` |
| `2026-08-20 14:12:07` | `cowrie.command.input` |
| `2026-08-20 14:12:07` | `cowrie.command.input` |
| `2026-08-20 14:12:07` | `cowrie.command.input` |
| `2026-08-20 14:12:07` | `cowrie.command.failed` |
| `2026-08-20 14:12:07` | `cowrie.log.closed` |
| `2026-08-20 14:12:08` | `cowrie.session.params` |
| `2026-08-20 14:12:08` | `cowrie.command.input` |
| `2026-08-20 14:12:08` | `cowrie.log.closed` |
| `2026-08-20 14:12:09` | `cowrie.session.params` |
| `2026-08-20 14:12:09` | `cowrie.command.input` |
| `2026-08-20 14:12:09` | `cowrie.log.closed` |
| `2026-08-20 14:12:09` | `cowrie.session.params` |
| `2026-08-20 14:12:09` | `cowrie.command.input` |
| `2026-08-20 14:12:09` | `cowrie.command.failed` |
| `2026-08-20 14:12:09` | `cowrie.command.failed` |
| `2026-08-20 14:13:10` | `cowrie.session.params` |
| `2026-08-20 14:13:10` | `cowrie.command.input` |
| `2026-08-20 14:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d93e34c7d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:14 |
| **Last Seen** | 2026-08-20 14:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:14:38` | `cowrie.session.connect` |
| `2026-08-20 14:14:39` | `cowrie.client.version` |
| `2026-08-20 14:14:39` | `cowrie.client.kex` |
| `2026-08-20 14:14:41` | `cowrie.login.success` |
| `2026-08-20 14:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:14:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:14:43` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e52dfd4d00

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:17 |
| **Last Seen** | 2026-08-20 14:17 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:17:35` | `cowrie.session.connect` |
| `2026-08-20 14:17:35` | `cowrie.client.version` |
| `2026-08-20 14:17:36` | `cowrie.client.kex` |
| `2026-08-20 14:17:37` | `cowrie.login.success` |
| `2026-08-20 14:17:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:17:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:17:52` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a737361844e1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-08-20 14:19 |
| **Last Seen** | 2026-08-20 14:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:19:34` | `cowrie.session.connect` |
| `2026-08-20 14:19:35` | `cowrie.client.version` |
| `2026-08-20 14:19:35` | `cowrie.client.kex` |
| `2026-08-20 14:19:38` | `cowrie.login.success` |
| `2026-08-20 14:19:39` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c06cda533964

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-08-20 14:19 |
| **Last Seen** | 2026-08-20 14:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:19:44` | `cowrie.session.connect` |
| `2026-08-20 14:19:45` | `cowrie.client.version` |
| `2026-08-20 14:19:45` | `cowrie.client.kex` |
| `2026-08-20 14:19:47` | `cowrie.login.success` |
| `2026-08-20 14:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde1f99673de

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-08-20 14:23 |
| **Last Seen** | 2026-08-20 14:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:23:26` | `cowrie.session.connect` |
| `2026-08-20 14:23:26` | `cowrie.client.version` |
| `2026-08-20 14:23:26` | `cowrie.client.kex` |
| `2026-08-20 14:23:27` | `cowrie.login.success` |
| `2026-08-20 14:23:28` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1137ccf6f04

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-20 14:23 |
| **Last Seen** | 2026-08-20 14:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:23:33` | `cowrie.session.connect` |
| `2026-08-20 14:23:34` | `cowrie.client.version` |
| `2026-08-20 14:23:34` | `cowrie.client.kex` |
| `2026-08-20 14:23:35` | `cowrie.login.success` |
| `2026-08-20 14:23:36` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f639f4878efd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:25 |
| **Last Seen** | 2026-08-20 14:26 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:25:30` | `cowrie.session.connect` |
| `2026-08-20 14:25:30` | `cowrie.client.version` |
| `2026-08-20 14:25:31` | `cowrie.client.kex` |
| `2026-08-20 14:26:23` | `cowrie.login.success` |
| `2026-08-20 14:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50cc20a110ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:28 |
| **Last Seen** | 2026-08-20 14:28 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:28:22` | `cowrie.session.connect` |
| `2026-08-20 14:28:22` | `cowrie.client.version` |
| `2026-08-20 14:28:22` | `cowrie.client.kex` |
| `2026-08-20 14:28:24` | `cowrie.login.success` |
| `2026-08-20 14:28:26` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:28:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:28:39` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f42dd6309296

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:36 |
| **Last Seen** | 2026-08-20 14:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:36:26` | `cowrie.session.connect` |
| `2026-08-20 14:36:26` | `cowrie.client.version` |
| `2026-08-20 14:36:28` | `cowrie.client.kex` |
| `2026-08-20 14:36:30` | `cowrie.login.success` |
| `2026-08-20 14:36:30` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:36:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:36:31` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67a0b30acfa

| Field | Detail |
|---|---|
| **Source IP** | `219.140.105[.]152` |
| **First Seen** | 2026-08-20 14:38 |
| **Last Seen** | 2026-08-20 14:39 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:38:15` | `cowrie.session.connect` |
| `2026-08-20 14:38:20` | `cowrie.client.version` |
| `2026-08-20 14:38:20` | `cowrie.client.kex` |
| `2026-08-20 14:38:48` | `cowrie.login.success` |
| `2026-08-20 14:39:00` | `cowrie.session.params` |
| `2026-08-20 14:39:00` | `cowrie.command.input` |
| `2026-08-20 14:39:05` | `cowrie.log.closed` |
| `2026-08-20 14:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.140.105[.]152` to AbuseIPDB if not already reported
- [ ] Block `219.140.105[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2311b3458c70

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:39 |
| **Last Seen** | 2026-08-20 14:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:39:05` | `cowrie.session.connect` |
| `2026-08-20 14:39:05` | `cowrie.client.version` |
| `2026-08-20 14:39:05` | `cowrie.client.kex` |
| `2026-08-20 14:39:20` | `cowrie.login.success` |
| `2026-08-20 14:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c3b425145f

| Field | Detail |
|---|---|
| **Source IP** | `125.69.76[.]148` |
| **First Seen** | 2026-08-20 14:39 |
| **Last Seen** | 2026-08-20 14:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:39:29` | `cowrie.session.connect` |
| `2026-08-20 14:39:30` | `cowrie.client.version` |
| `2026-08-20 14:39:30` | `cowrie.client.kex` |
| `2026-08-20 14:39:32` | `cowrie.login.success` |
| `2026-08-20 14:39:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.69.76[.]148` to AbuseIPDB if not already reported
- [ ] Block `125.69.76[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcebb307399c

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]23` |
| **First Seen** | 2026-08-20 14:43 |
| **Last Seen** | 2026-08-20 14:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:43:52` | `cowrie.session.connect` |
| `2026-08-20 14:43:52` | `cowrie.client.version` |
| `2026-08-20 14:43:52` | `cowrie.client.kex` |
| `2026-08-20 14:43:55` | `cowrie.login.success` |
| `2026-08-20 14:43:55` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]23` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7c7504daca

| Field | Detail |
|---|---|
| **Source IP** | `171.217.70[.]151` |
| **First Seen** | 2026-08-20 14:44 |
| **Last Seen** | 2026-08-20 14:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:44:02` | `cowrie.session.connect` |
| `2026-08-20 14:44:04` | `cowrie.client.version` |
| `2026-08-20 14:44:04` | `cowrie.client.kex` |
| `2026-08-20 14:44:08` | `cowrie.login.success` |
| `2026-08-20 14:44:10` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.70[.]151` to AbuseIPDB if not already reported
- [ ] Block `171.217.70[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2934d9578399

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:47 |
| **Last Seen** | 2026-08-20 14:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:47:28` | `cowrie.session.connect` |
| `2026-08-20 14:47:28` | `cowrie.client.version` |
| `2026-08-20 14:47:29` | `cowrie.client.kex` |
| `2026-08-20 14:47:31` | `cowrie.login.success` |
| `2026-08-20 14:47:33` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:47:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:47:35` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e447765b5bb8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-20 14:50 |
| **Last Seen** | 2026-08-20 14:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:50:01` | `cowrie.session.connect` |
| `2026-08-20 14:50:01` | `cowrie.client.version` |
| `2026-08-20 14:50:01` | `cowrie.client.kex` |
| `2026-08-20 14:50:04` | `cowrie.login.success` |
| `2026-08-20 14:50:06` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:50:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-20 14:50:07` | `cowrie.direct-tcpip.data` |
| `2026-08-20 14:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38061ca0e5c7

| Field | Detail |
|---|---|
| **Source IP** | `81.195.152[.]14` |
| **First Seen** | 2026-08-20 14:53 |
| **Last Seen** | 2026-08-20 14:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:53:10` | `cowrie.session.connect` |
| `2026-08-20 14:53:10` | `cowrie.client.version` |
| `2026-08-20 14:53:10` | `cowrie.client.kex` |
| `2026-08-20 14:53:12` | `cowrie.login.success` |
| `2026-08-20 14:53:13` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.195.152[.]14` to AbuseIPDB if not already reported
- [ ] Block `81.195.152[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff44aa6a3925

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-08-20 14:53 |
| **Last Seen** | 2026-08-20 14:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:53:22` | `cowrie.session.connect` |
| `2026-08-20 14:53:23` | `cowrie.client.version` |
| `2026-08-20 14:53:23` | `cowrie.client.kex` |
| `2026-08-20 14:53:24` | `cowrie.login.success` |
| `2026-08-20 14:53:24` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2572e7a18f

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-08-20 14:53 |
| **Last Seen** | 2026-08-20 14:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:53:23` | `cowrie.session.connect` |
| `2026-08-20 14:53:24` | `cowrie.client.version` |
| `2026-08-20 14:53:24` | `cowrie.client.kex` |
| `2026-08-20 14:53:26` | `cowrie.login.success` |
| `2026-08-20 14:53:27` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4024489f59fb

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-08-20 14:53 |
| **Last Seen** | 2026-08-20 14:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-20 14:53:34` | `cowrie.session.connect` |
| `2026-08-20 14:53:35` | `cowrie.client.version` |
| `2026-08-20 14:53:35` | `cowrie.client.kex` |
| `2026-08-20 14:53:36` | `cowrie.login.success` |
| `2026-08-20 14:53:37` | `cowrie.direct-tcpip.request` |
| `2026-08-20 14:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **31** | 2026-08-20 12:56 | 2026-08-20 14:53 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-20 13:19 | 2026-08-20 14:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `98.199.111[.]73` | **4** | 2026-08-20 13:16 | 2026-08-20 13:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.55.47[.]66` | **3** | 2026-08-20 14:43 | 2026-08-20 14:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | **2** | 2026-08-20 14:17 | 2026-08-20 14:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `219.140.105[.]152` | **2** | 2026-08-20 14:38 | 2026-08-20 14:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-08-20 12:57 | 2026-08-20 12:58 | 3s | 0 | `T1592` | 🟢 LOW |
| `117.198.99[.]18` | 1 | 2026-08-20 13:03 | 2026-08-20 13:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]23` | 1 | 2026-08-20 13:15 | 2026-08-20 13:15 | 8s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]26` | 1 | 2026-08-20 14:19 | 2026-08-20 14:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `20.115.99[.]68` | 1 | 2026-08-20 14:11 | 2026-08-20 14:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `200.81.165[.]59` | 1 | 2026-08-20 14:20 | 2026-08-20 14:20 | 11s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]89` | 1 | 2026-08-20 13:52 | 2026-08-20 13:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-08-20 13:41 | 2026-08-20 13:41 | 1s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]130` | 1 | 2026-08-20 14:37 | 2026-08-20 14:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]84` | 1 | 2026-08-20 13:57 | 2026-08-20 13:58 | 17s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-20 14:05 | 2026-08-20 14:07 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |

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
| `69.172.79[.]198` | HK | SkyExchange Internet Access | **100** ⚠️ | 50 |
| `185.2.228[.]48` | LT | Tele2 Lithuania | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `37.55.47[.]66` | UA | JSC Ukrtelecom | **100** ⚠️ | 1 |
| `62.182.132[.]94` | RU | Net By Net Holding LLC | **100** ⚠️ | 50 |
| `117.211.15[.]106` | IN | O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `183.171.236[.]23` | MY | Celcom Axiata Berhad | **100** ⚠️ | 38 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `27.223.98[.]117` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `49.124.151[.]23` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 68 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 1 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 128 cases |
| Tool 34  | Credential Extractor        | ✅ 85 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 68 priority case(s) shown individually · 17 recon entry/entries in table (6 group(s) consolidating 46 session(s)).

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
_Report time: 2026-08-20T16:40:44Z_

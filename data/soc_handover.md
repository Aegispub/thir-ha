# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-22 |
| **Generated At** | 2026-08-22T08:34:17Z |
| **Shift Time** | 08:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **123** |
| Confirmed Threats | **101** |
| False Positives Filtered | **22** (17.9%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **25** |
| High Severity Cases | **69** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **3** HIGH · **17** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **89** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **13** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **78** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `ubuntu` | 13 |
| `guest` | 10 |
| `config` | 10 |
| `ubnt` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `config2014` | 6 |
| `ubnt2016` | 6 |
| `root2005` | 6 |
| `supervisor2000` | 6 |
| `guest2002` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `config2014` | 6 |
| `ubnt` | `ubnt2016` | 6 |
| `root` | `root2005` | 6 |
| `supervisor` | `supervisor2000` | 6 |
| `guest` | `guest2002` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `P@ssw0rd2003` | `217.60.255.130` | 2026-08-22T04:58:13 |
| `root` | `123!@#qwe` | `217.60.255.130` | 2026-08-22T04:58:16 |
| `root` | `root2019` | `10.0.0.73` | 2026-08-22T04:58:43 |
| `default` | `default2004` | `223.210.27.53` | 2026-08-22T05:07:20 |
| `default` | `default2004` | `222.120.176.6` | 2026-08-22T05:07:29 |
| `ubuntu` | `Kian123` | `217.60.255.130` | 2026-08-22T05:07:39 |
| `root` | `Aa@12345` | `217.60.255.130` | 2026-08-22T05:07:43 |
| `guest` | `guest2010` | `213.101.138.172` | 2026-08-22T05:09:01 |
| `blank` | `blank12345` | `196.188.93.169` | 2026-08-22T05:14:05 |
| `root` | `root2019` | `65.20.251.170` | 2026-08-22T05:16:43 |
| `root` | `root2019` | `223.107.72.234` | 2026-08-22T05:16:51 |
| `root` | `root2019` | `65.20.141.202` | 2026-08-22T05:16:56 |
| `ubuntu` | `Pasargad@123` | `217.60.255.130` | 2026-08-22T05:17:11 |
| `root` | `Root123` | `217.60.255.130` | 2026-08-22T05:17:15 |
| `support` | `support` | `176.53.159.196` | 2026-08-22T05:19:42 |
| `config` | `config2014` | `10.0.0.73` | 2026-08-22T05:22:45 |
| `config` | `config2014` | `65.20.134.97` | 2026-08-22T05:24:16 |
| `config` | `config2014` | `103.67.152.201` | 2026-08-22T05:24:24 |
| `ubuntu` | `Pasargad123` | `217.60.255.130` | 2026-08-22T05:26:43 |
| `root` | `Aa123456` | `217.60.255.130` | 2026-08-22T05:26:47 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `47.250.119.197` | 2026-08-22T05:29:28 |
| `config` | `config2001` | `10.0.0.73` | 2026-08-22T05:31:34 |
| `ubuntu` | `Iran@2025` | `217.60.255.130` | 2026-08-22T05:36:11 |
| `root` | `12qw!@QW` | `217.60.255.130` | 2026-08-22T05:36:15 |
| `config` | `config2014` | `95.79.57.221` | 2026-08-22T05:39:47 |
| `config` | `config2014` | `211.221.158.216` | 2026-08-22T05:39:55 |
| `blank` | `blank12345` | `218.146.255.221` | 2026-08-22T05:41:48 |
| `support` | `support` | `10.0.0.73` | 2026-08-22T05:43:17 |
| `ubuntu` | `sina1234` | `217.60.255.130` | 2026-08-22T05:45:36 |
| `root` | `Abc@123` | `217.60.255.130` | 2026-08-22T05:45:40 |
| `nobody` | `nobody2015` | `125.59.204.176` | 2026-08-22T05:46:41 |
| `root` | `KX76bmNNOk` | `47.113.219.102` | 2026-08-22T05:48:47 |
| `config` | `config2001` | `186.238.242.194` | 2026-08-22T05:49:23 |
| `config` | `config2001` | `201.28.176.31` | 2026-08-22T05:49:31 |
| `ubuntu` | `Mm123456` | `217.60.255.130` | 2026-08-22T05:55:12 |
| `root` | `QAZwsx123` | `217.60.255.130` | 2026-08-22T05:55:16 |
| `ubnt` | `ubnt2016` | `10.0.0.73` | 2026-08-22T05:55:21 |
| `ubnt` | `ubnt2016` | `103.230.176.152` | 2026-08-22T05:56:54 |
| `ubnt` | `ubnt2016` | `111.70.32.53` | 2026-08-22T05:57:03 |
| `nobody` | `nobody2015` | `10.0.0.73` | 2026-08-22T05:57:48 |
| `root` | `root2005` | `10.0.0.73` | 2026-08-22T06:04:29 |
| `ubuntu` | `Dana@123` | `217.60.255.130` | 2026-08-22T06:04:36 |
| `root` | `admin1` | `217.60.255.130` | 2026-08-22T06:04:40 |
| `ubnt` | `ubnt2016` | `121.202.138.181` | 2026-08-22T06:12:19 |
| `ubnt` | `ubnt2016` | `95.35.29.192` | 2026-08-22T06:12:27 |
| `ubuntu` | `omid1234` | `217.60.255.130` | 2026-08-22T06:14:15 |
| `root` | `!QAZ1qaz` | `217.60.255.130` | 2026-08-22T06:14:19 |
| `nobody` | `nobody2015` | `220.93.167.144` | 2026-08-22T06:14:30 |
| `nobody` | `nobody2015` | `175.101.14.77` | 2026-08-22T06:14:42 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-22T06:15:12 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-22T06:15:13 |
| `supervisor` | `supervisor2000` | `103.224.19.186` | 2026-08-22T06:19:22 |
| `supervisor` | `supervisor2000` | `187.115.144.103` | 2026-08-22T06:19:31 |
| `root` | `root2005` | `65.20.204.108` | 2026-08-22T06:22:15 |
| `root` | `root2005` | `71.229.1.186` | 2026-08-22T06:22:22 |
| `root` | `root2005` | `2.55.122.202` | 2026-08-22T06:22:28 |
| `root` | `root2005` | `2.184.237.250` | 2026-08-22T06:22:38 |
| `ubuntu` | `deployer1234` | `217.60.255.130` | 2026-08-22T06:23:48 |
| `root` | `Q!w2e3r4t5y6` | `217.60.255.130` | 2026-08-22T06:23:52 |
| `guest` | `guest2002` | `10.0.0.73` | 2026-08-22T06:27:58 |
| `guest` | `guest2002` | `175.101.14.77` | 2026-08-22T06:29:38 |
| `guest` | `guest2002` | `90.230.168.26` | 2026-08-22T06:29:46 |
| `supervisor` | `supervisor2000` | `10.0.0.73` | 2026-08-22T06:30:31 |
| `admin` | `admin` | `43.110.37.217` | 2026-08-22T06:30:50 |
| `ubuntu` | `Pars@1234` | `217.60.255.130` | 2026-08-22T06:33:17 |
| `root` | `123QWEqwe` | `217.60.255.130` | 2026-08-22T06:33:21 |
| `guest` | `guest2007` | `10.0.0.73` | 2026-08-22T06:37:10 |
| `ubuntu` | `Reza@1234` | `217.60.255.130` | 2026-08-22T06:42:49 |
| `root` | `!@#QWE123qwe` | `217.60.255.130` | 2026-08-22T06:42:52 |
| `guest` | `guest2002` | `45.26.184.5` | 2026-08-22T06:44:55 |
| `guest` | `guest2002` | `37.28.177.141` | 2026-08-22T06:45:03 |
| `supervisor` | `supervisor2000` | `65.20.133.56` | 2026-08-22T06:47:02 |
| `supervisor` | `supervisor2000` | `96.52.164.34` | 2026-08-22T06:47:09 |
| `unknown` | `unknown2017` | `172.114.43.219` | 2026-08-22T06:52:08 |
| `unknown` | `unknown2017` | `116.114.94.242` | 2026-08-22T06:52:17 |
| `ubuntu` | `Arash@123` | `217.60.255.130` | 2026-08-22T06:52:26 |
| `root` | `admin@12345` | `217.60.255.130` | 2026-08-22T06:52:30 |
| `guest` | `guest2007` | `179.185.227.77` | 2026-08-22T06:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **123** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 37 |
| libssh | 32 |
| Go SSH scanner | 4 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 37 | 36 |
| `419da4c91ddb...` | Modern SSH client | 26 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 37 | 36 | Mirai/variant |
| `419da4c91ddb...` | libssh | 26 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **55** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS1257` | Tele2 Sverige AB | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS8473` | Bahnhof AB | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (69)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4d3913e639ac

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:58 |
| **Last Seen** | 2026-08-22 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:58:12` | `cowrie.session.connect` |
| `2026-08-22 04:58:12` | `cowrie.client.version` |
| `2026-08-22 04:58:12` | `cowrie.client.kex` |
| `2026-08-22 04:58:13` | `cowrie.login.success` |
| `2026-08-22 04:58:13` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:58:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:58:14` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fadbf2bcc11

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 04:58 |
| **Last Seen** | 2026-08-22 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 04:58:15` | `cowrie.session.connect` |
| `2026-08-22 04:58:15` | `cowrie.client.version` |
| `2026-08-22 04:58:15` | `cowrie.client.kex` |
| `2026-08-22 04:58:16` | `cowrie.login.success` |
| `2026-08-22 04:58:16` | `cowrie.direct-tcpip.request` |
| `2026-08-22 04:58:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 04:58:17` | `cowrie.direct-tcpip.data` |
| `2026-08-22 04:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51de30c8fa9b

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-08-22 05:07 |
| **Last Seen** | 2026-08-22 05:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:07:16` | `cowrie.session.connect` |
| `2026-08-22 05:07:17` | `cowrie.client.version` |
| `2026-08-22 05:07:17` | `cowrie.client.kex` |
| `2026-08-22 05:07:20` | `cowrie.login.success` |
| `2026-08-22 05:07:21` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655062753722

| Field | Detail |
|---|---|
| **Source IP** | `222.120.176[.]6` |
| **First Seen** | 2026-08-22 05:07 |
| **Last Seen** | 2026-08-22 05:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:07:26` | `cowrie.session.connect` |
| `2026-08-22 05:07:27` | `cowrie.client.version` |
| `2026-08-22 05:07:27` | `cowrie.client.kex` |
| `2026-08-22 05:07:29` | `cowrie.login.success` |
| `2026-08-22 05:07:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.120.176[.]6` to AbuseIPDB if not already reported
- [ ] Block `222.120.176[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c7016f9d2e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:07 |
| **Last Seen** | 2026-08-22 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:07:38` | `cowrie.session.connect` |
| `2026-08-22 05:07:38` | `cowrie.client.version` |
| `2026-08-22 05:07:39` | `cowrie.client.kex` |
| `2026-08-22 05:07:39` | `cowrie.login.success` |
| `2026-08-22 05:07:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:07:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:07:40` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b705d50e24be

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:07 |
| **Last Seen** | 2026-08-22 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:07:42` | `cowrie.session.connect` |
| `2026-08-22 05:07:42` | `cowrie.client.version` |
| `2026-08-22 05:07:43` | `cowrie.client.kex` |
| `2026-08-22 05:07:43` | `cowrie.login.success` |
| `2026-08-22 05:07:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:07:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:07:44` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d63717986af

| Field | Detail |
|---|---|
| **Source IP** | `213.101.138[.]172` |
| **First Seen** | 2026-08-22 05:08 |
| **Last Seen** | 2026-08-22 05:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:08:59` | `cowrie.session.connect` |
| `2026-08-22 05:09:00` | `cowrie.client.version` |
| `2026-08-22 05:09:00` | `cowrie.client.kex` |
| `2026-08-22 05:09:01` | `cowrie.login.success` |
| `2026-08-22 05:09:01` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.101.138[.]172` to AbuseIPDB if not already reported
- [ ] Block `213.101.138[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04ff8f109da

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-22 05:14 |
| **Last Seen** | 2026-08-22 05:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:14:03` | `cowrie.session.connect` |
| `2026-08-22 05:14:03` | `cowrie.client.version` |
| `2026-08-22 05:14:03` | `cowrie.client.kex` |
| `2026-08-22 05:14:05` | `cowrie.login.success` |
| `2026-08-22 05:14:05` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39c115ddf97d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]170` |
| **First Seen** | 2026-08-22 05:16 |
| **Last Seen** | 2026-08-22 05:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:16:42` | `cowrie.session.connect` |
| `2026-08-22 05:16:42` | `cowrie.client.version` |
| `2026-08-22 05:16:42` | `cowrie.client.kex` |
| `2026-08-22 05:16:43` | `cowrie.login.success` |
| `2026-08-22 05:16:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]170` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea4626271241

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-08-22 05:16 |
| **Last Seen** | 2026-08-22 05:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:16:49` | `cowrie.session.connect` |
| `2026-08-22 05:16:50` | `cowrie.client.version` |
| `2026-08-22 05:16:50` | `cowrie.client.kex` |
| `2026-08-22 05:16:51` | `cowrie.login.success` |
| `2026-08-22 05:16:52` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6ef940d5bf

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-08-22 05:16 |
| **Last Seen** | 2026-08-22 05:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:16:55` | `cowrie.session.connect` |
| `2026-08-22 05:16:55` | `cowrie.client.version` |
| `2026-08-22 05:16:55` | `cowrie.client.kex` |
| `2026-08-22 05:16:56` | `cowrie.login.success` |
| `2026-08-22 05:16:57` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1575479bdba3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:17 |
| **Last Seen** | 2026-08-22 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:17:10` | `cowrie.session.connect` |
| `2026-08-22 05:17:10` | `cowrie.client.version` |
| `2026-08-22 05:17:10` | `cowrie.client.kex` |
| `2026-08-22 05:17:11` | `cowrie.login.success` |
| `2026-08-22 05:17:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:17:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:17:11` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9722843ad59

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:17 |
| **Last Seen** | 2026-08-22 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:17:14` | `cowrie.session.connect` |
| `2026-08-22 05:17:14` | `cowrie.client.version` |
| `2026-08-22 05:17:14` | `cowrie.client.kex` |
| `2026-08-22 05:17:15` | `cowrie.login.success` |
| `2026-08-22 05:17:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:17:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:17:15` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e0692ca51c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 05:19 |
| **Last Seen** | 2026-08-22 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:19:41` | `cowrie.session.connect` |
| `2026-08-22 05:19:41` | `cowrie.client.version` |
| `2026-08-22 05:19:42` | `cowrie.client.kex` |
| `2026-08-22 05:19:42` | `cowrie.login.success` |
| `2026-08-22 05:19:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:19:42` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20f13dd5e3e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.134[.]97` |
| **First Seen** | 2026-08-22 05:24 |
| **Last Seen** | 2026-08-22 05:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:24:15` | `cowrie.session.connect` |
| `2026-08-22 05:24:15` | `cowrie.client.version` |
| `2026-08-22 05:24:15` | `cowrie.client.kex` |
| `2026-08-22 05:24:16` | `cowrie.login.success` |
| `2026-08-22 05:24:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.134[.]97` to AbuseIPDB if not already reported
- [ ] Block `65.20.134[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ca1425a74c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-08-22 05:24 |
| **Last Seen** | 2026-08-22 05:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:24:22` | `cowrie.session.connect` |
| `2026-08-22 05:24:22` | `cowrie.client.version` |
| `2026-08-22 05:24:22` | `cowrie.client.kex` |
| `2026-08-22 05:24:24` | `cowrie.login.success` |
| `2026-08-22 05:24:25` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622192da94ec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:26 |
| **Last Seen** | 2026-08-22 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:26:42` | `cowrie.session.connect` |
| `2026-08-22 05:26:42` | `cowrie.client.version` |
| `2026-08-22 05:26:42` | `cowrie.client.kex` |
| `2026-08-22 05:26:43` | `cowrie.login.success` |
| `2026-08-22 05:26:44` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:26:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:26:44` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b633317e91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:26 |
| **Last Seen** | 2026-08-22 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:26:46` | `cowrie.session.connect` |
| `2026-08-22 05:26:46` | `cowrie.client.version` |
| `2026-08-22 05:26:46` | `cowrie.client.kex` |
| `2026-08-22 05:26:47` | `cowrie.login.success` |
| `2026-08-22 05:26:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:26:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:26:47` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f60bf8fd54

| Field | Detail |
|---|---|
| **Source IP** | `47.250.119[.]197` |
| **First Seen** | 2026-08-22 05:29 |
| **Last Seen** | 2026-08-22 05:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: curl/7.64.1, Accept: */*` |
| **TTPs (MITRE)** | T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:29:28` | `cowrie.session.connect` |
| `2026-08-22 05:29:28` | `cowrie.login.success` |
| `2026-08-22 05:29:28` | `cowrie.session.params` |
| `2026-08-22 05:29:28` | `cowrie.command.input` |
| `2026-08-22 05:29:28` | `cowrie.command.failed` |
| `2026-08-22 05:29:28` | `cowrie.command.input` |
| `2026-08-22 05:29:28` | `cowrie.command.failed` |
| `2026-08-22 05:29:28` | `cowrie.command.input` |
| `2026-08-22 05:29:31` | `cowrie.log.closed` |
| `2026-08-22 05:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.250.119[.]197` to AbuseIPDB if not already reported
- [ ] Block `47.250.119[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7971b2b518

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:36 |
| **Last Seen** | 2026-08-22 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:36:10` | `cowrie.session.connect` |
| `2026-08-22 05:36:10` | `cowrie.client.version` |
| `2026-08-22 05:36:10` | `cowrie.client.kex` |
| `2026-08-22 05:36:11` | `cowrie.login.success` |
| `2026-08-22 05:36:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:36:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:36:11` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f24fc24d9cf4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:36 |
| **Last Seen** | 2026-08-22 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:36:14` | `cowrie.session.connect` |
| `2026-08-22 05:36:14` | `cowrie.client.version` |
| `2026-08-22 05:36:14` | `cowrie.client.kex` |
| `2026-08-22 05:36:15` | `cowrie.login.success` |
| `2026-08-22 05:36:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:36:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:36:15` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd065d11b3ee

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-08-22 05:39 |
| **Last Seen** | 2026-08-22 05:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:39:45` | `cowrie.session.connect` |
| `2026-08-22 05:39:46` | `cowrie.client.version` |
| `2026-08-22 05:39:46` | `cowrie.client.kex` |
| `2026-08-22 05:39:47` | `cowrie.login.success` |
| `2026-08-22 05:39:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476a1b290d9d

| Field | Detail |
|---|---|
| **Source IP** | `211.221.158[.]216` |
| **First Seen** | 2026-08-22 05:39 |
| **Last Seen** | 2026-08-22 05:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:39:52` | `cowrie.session.connect` |
| `2026-08-22 05:39:53` | `cowrie.client.version` |
| `2026-08-22 05:39:53` | `cowrie.client.kex` |
| `2026-08-22 05:39:55` | `cowrie.login.success` |
| `2026-08-22 05:39:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.221.158[.]216` to AbuseIPDB if not already reported
- [ ] Block `211.221.158[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6734c33f0f9

| Field | Detail |
|---|---|
| **Source IP** | `218.146.255[.]221` |
| **First Seen** | 2026-08-22 05:41 |
| **Last Seen** | 2026-08-22 05:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:41:44` | `cowrie.session.connect` |
| `2026-08-22 05:41:45` | `cowrie.client.version` |
| `2026-08-22 05:41:45` | `cowrie.client.kex` |
| `2026-08-22 05:41:48` | `cowrie.login.success` |
| `2026-08-22 05:41:49` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.146.255[.]221` to AbuseIPDB if not already reported
- [ ] Block `218.146.255[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4236f41fddc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:45 |
| **Last Seen** | 2026-08-22 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:45:35` | `cowrie.session.connect` |
| `2026-08-22 05:45:35` | `cowrie.client.version` |
| `2026-08-22 05:45:35` | `cowrie.client.kex` |
| `2026-08-22 05:45:36` | `cowrie.login.success` |
| `2026-08-22 05:45:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:45:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:45:36` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761a9a5a1077

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:45 |
| **Last Seen** | 2026-08-22 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:45:39` | `cowrie.session.connect` |
| `2026-08-22 05:45:39` | `cowrie.client.version` |
| `2026-08-22 05:45:39` | `cowrie.client.kex` |
| `2026-08-22 05:45:40` | `cowrie.login.success` |
| `2026-08-22 05:45:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:45:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:45:40` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834369107641

| Field | Detail |
|---|---|
| **Source IP** | `125.59.204[.]176` |
| **First Seen** | 2026-08-22 05:46 |
| **Last Seen** | 2026-08-22 05:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:46:39` | `cowrie.session.connect` |
| `2026-08-22 05:46:39` | `cowrie.client.version` |
| `2026-08-22 05:46:39` | `cowrie.client.kex` |
| `2026-08-22 05:46:41` | `cowrie.login.success` |
| `2026-08-22 05:46:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.59.204[.]176` to AbuseIPDB if not already reported
- [ ] Block `125.59.204[.]176` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7a17afeb52

| Field | Detail |
|---|---|
| **Source IP** | `47.113.219[.]102` |
| **First Seen** | 2026-08-22 05:48 |
| **Last Seen** | 2026-08-22 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:48:46` | `cowrie.session.connect` |
| `2026-08-22 05:48:46` | `cowrie.client.version` |
| `2026-08-22 05:48:46` | `cowrie.client.kex` |
| `2026-08-22 05:48:47` | `cowrie.login.success` |
| `2026-08-22 05:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.113.219[.]102` to AbuseIPDB if not already reported
- [ ] Block `47.113.219[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a56aba1a1b

| Field | Detail |
|---|---|
| **Source IP** | `186.238.242[.]194` |
| **First Seen** | 2026-08-22 05:49 |
| **Last Seen** | 2026-08-22 05:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:49:20` | `cowrie.session.connect` |
| `2026-08-22 05:49:21` | `cowrie.client.version` |
| `2026-08-22 05:49:21` | `cowrie.client.kex` |
| `2026-08-22 05:49:23` | `cowrie.login.success` |
| `2026-08-22 05:49:24` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.242[.]194` to AbuseIPDB if not already reported
- [ ] Block `186.238.242[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54b0e03284c9

| Field | Detail |
|---|---|
| **Source IP** | `201.28.176[.]31` |
| **First Seen** | 2026-08-22 05:49 |
| **Last Seen** | 2026-08-22 05:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:49:28` | `cowrie.session.connect` |
| `2026-08-22 05:49:29` | `cowrie.client.version` |
| `2026-08-22 05:49:29` | `cowrie.client.kex` |
| `2026-08-22 05:49:31` | `cowrie.login.success` |
| `2026-08-22 05:49:31` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.176[.]31` to AbuseIPDB if not already reported
- [ ] Block `201.28.176[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b94736fb0f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:55 |
| **Last Seen** | 2026-08-22 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:55:11` | `cowrie.session.connect` |
| `2026-08-22 05:55:11` | `cowrie.client.version` |
| `2026-08-22 05:55:11` | `cowrie.client.kex` |
| `2026-08-22 05:55:12` | `cowrie.login.success` |
| `2026-08-22 05:55:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:55:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:55:12` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bc0cc3ea00

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 05:55 |
| **Last Seen** | 2026-08-22 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:55:15` | `cowrie.session.connect` |
| `2026-08-22 05:55:15` | `cowrie.client.version` |
| `2026-08-22 05:55:15` | `cowrie.client.kex` |
| `2026-08-22 05:55:16` | `cowrie.login.success` |
| `2026-08-22 05:55:16` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:55:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 05:55:16` | `cowrie.direct-tcpip.data` |
| `2026-08-22 05:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58c8763604f

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-08-22 05:56 |
| **Last Seen** | 2026-08-22 05:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:56:51` | `cowrie.session.connect` |
| `2026-08-22 05:56:52` | `cowrie.client.version` |
| `2026-08-22 05:56:52` | `cowrie.client.kex` |
| `2026-08-22 05:56:54` | `cowrie.login.success` |
| `2026-08-22 05:56:55` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8850b5b5f83d

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-08-22 05:57 |
| **Last Seen** | 2026-08-22 05:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 05:57:01` | `cowrie.session.connect` |
| `2026-08-22 05:57:01` | `cowrie.client.version` |
| `2026-08-22 05:57:01` | `cowrie.client.kex` |
| `2026-08-22 05:57:03` | `cowrie.login.success` |
| `2026-08-22 05:57:04` | `cowrie.direct-tcpip.request` |
| `2026-08-22 05:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db4a504a1c5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:04 |
| **Last Seen** | 2026-08-22 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:04:35` | `cowrie.session.connect` |
| `2026-08-22 06:04:35` | `cowrie.client.version` |
| `2026-08-22 06:04:35` | `cowrie.client.kex` |
| `2026-08-22 06:04:36` | `cowrie.login.success` |
| `2026-08-22 06:04:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:04:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:04:37` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45020de339c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:04 |
| **Last Seen** | 2026-08-22 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:04:39` | `cowrie.session.connect` |
| `2026-08-22 06:04:39` | `cowrie.client.version` |
| `2026-08-22 06:04:39` | `cowrie.client.kex` |
| `2026-08-22 06:04:40` | `cowrie.login.success` |
| `2026-08-22 06:04:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:04:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:04:40` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19bef0e7582

| Field | Detail |
|---|---|
| **Source IP** | `121.202.138[.]181` |
| **First Seen** | 2026-08-22 06:12 |
| **Last Seen** | 2026-08-22 06:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:12:14` | `cowrie.session.connect` |
| `2026-08-22 06:12:15` | `cowrie.client.version` |
| `2026-08-22 06:12:15` | `cowrie.client.kex` |
| `2026-08-22 06:12:19` | `cowrie.login.success` |
| `2026-08-22 06:12:20` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.138[.]181` to AbuseIPDB if not already reported
- [ ] Block `121.202.138[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d11cd9445a6

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-08-22 06:12 |
| **Last Seen** | 2026-08-22 06:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:12:25` | `cowrie.session.connect` |
| `2026-08-22 06:12:26` | `cowrie.client.version` |
| `2026-08-22 06:12:26` | `cowrie.client.kex` |
| `2026-08-22 06:12:27` | `cowrie.login.success` |
| `2026-08-22 06:12:27` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8610bc140aa2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:14 |
| **Last Seen** | 2026-08-22 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:14:14` | `cowrie.session.connect` |
| `2026-08-22 06:14:14` | `cowrie.client.version` |
| `2026-08-22 06:14:14` | `cowrie.client.kex` |
| `2026-08-22 06:14:15` | `cowrie.login.success` |
| `2026-08-22 06:14:15` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:14:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:14:16` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc767eccd457

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:14 |
| **Last Seen** | 2026-08-22 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:14:18` | `cowrie.session.connect` |
| `2026-08-22 06:14:18` | `cowrie.client.version` |
| `2026-08-22 06:14:18` | `cowrie.client.kex` |
| `2026-08-22 06:14:19` | `cowrie.login.success` |
| `2026-08-22 06:14:19` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:14:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:14:20` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7ced8b71a6

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-22 06:14 |
| **Last Seen** | 2026-08-22 06:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:14:26` | `cowrie.session.connect` |
| `2026-08-22 06:14:28` | `cowrie.client.version` |
| `2026-08-22 06:14:28` | `cowrie.client.kex` |
| `2026-08-22 06:14:30` | `cowrie.login.success` |
| `2026-08-22 06:14:31` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa033f66fe9

| Field | Detail |
|---|---|
| **Source IP** | `175.101.14[.]77` |
| **First Seen** | 2026-08-22 06:14 |
| **Last Seen** | 2026-08-22 06:14 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:14:36` | `cowrie.session.connect` |
| `2026-08-22 06:14:39` | `cowrie.client.version` |
| `2026-08-22 06:14:39` | `cowrie.client.kex` |
| `2026-08-22 06:14:42` | `cowrie.login.success` |
| `2026-08-22 06:14:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.101.14[.]77` to AbuseIPDB if not already reported
- [ ] Block `175.101.14[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d86204d534

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-22 06:15 |
| **Last Seen** | 2026-08-22 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:15:11` | `cowrie.session.connect` |
| `2026-08-22 06:15:11` | `cowrie.client.version` |
| `2026-08-22 06:15:11` | `cowrie.client.kex` |
| `2026-08-22 06:15:12` | `cowrie.login.success` |
| `2026-08-22 06:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1661de83ca27

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-22 06:15 |
| **Last Seen** | 2026-08-22 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:15:12` | `cowrie.session.connect` |
| `2026-08-22 06:15:12` | `cowrie.client.version` |
| `2026-08-22 06:15:12` | `cowrie.client.kex` |
| `2026-08-22 06:15:13` | `cowrie.login.success` |
| `2026-08-22 06:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dec1be4ae30

| Field | Detail |
|---|---|
| **Source IP** | `103.224.19[.]186` |
| **First Seen** | 2026-08-22 06:19 |
| **Last Seen** | 2026-08-22 06:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:19:19` | `cowrie.session.connect` |
| `2026-08-22 06:19:20` | `cowrie.client.version` |
| `2026-08-22 06:19:20` | `cowrie.client.kex` |
| `2026-08-22 06:19:22` | `cowrie.login.success` |
| `2026-08-22 06:19:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.224.19[.]186` to AbuseIPDB if not already reported
- [ ] Block `103.224.19[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ba428fac52

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-22 06:19 |
| **Last Seen** | 2026-08-22 06:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:19:28` | `cowrie.session.connect` |
| `2026-08-22 06:19:29` | `cowrie.client.version` |
| `2026-08-22 06:19:29` | `cowrie.client.kex` |
| `2026-08-22 06:19:31` | `cowrie.login.success` |
| `2026-08-22 06:19:32` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9761b9829e5c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]108` |
| **First Seen** | 2026-08-22 06:22 |
| **Last Seen** | 2026-08-22 06:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:22:14` | `cowrie.session.connect` |
| `2026-08-22 06:22:14` | `cowrie.client.version` |
| `2026-08-22 06:22:14` | `cowrie.client.kex` |
| `2026-08-22 06:22:15` | `cowrie.login.success` |
| `2026-08-22 06:22:16` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]108` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc3698ebce4

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-08-22 06:22 |
| **Last Seen** | 2026-08-22 06:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:22:21` | `cowrie.session.connect` |
| `2026-08-22 06:22:21` | `cowrie.client.version` |
| `2026-08-22 06:22:21` | `cowrie.client.kex` |
| `2026-08-22 06:22:22` | `cowrie.login.success` |
| `2026-08-22 06:22:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389e0ffe7df2

| Field | Detail |
|---|---|
| **Source IP** | `2.55.122[.]202` |
| **First Seen** | 2026-08-22 06:22 |
| **Last Seen** | 2026-08-22 06:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:22:26` | `cowrie.session.connect` |
| `2026-08-22 06:22:27` | `cowrie.client.version` |
| `2026-08-22 06:22:27` | `cowrie.client.kex` |
| `2026-08-22 06:22:28` | `cowrie.login.success` |
| `2026-08-22 06:22:29` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.122[.]202` to AbuseIPDB if not already reported
- [ ] Block `2.55.122[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da7cc16cccfa

| Field | Detail |
|---|---|
| **Source IP** | `2.184.237[.]250` |
| **First Seen** | 2026-08-22 06:22 |
| **Last Seen** | 2026-08-22 06:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:22:35` | `cowrie.session.connect` |
| `2026-08-22 06:22:36` | `cowrie.client.version` |
| `2026-08-22 06:22:36` | `cowrie.client.kex` |
| `2026-08-22 06:22:38` | `cowrie.login.success` |
| `2026-08-22 06:22:38` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.184.237[.]250` to AbuseIPDB if not already reported
- [ ] Block `2.184.237[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2774963a25e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:23 |
| **Last Seen** | 2026-08-22 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:23:47` | `cowrie.session.connect` |
| `2026-08-22 06:23:47` | `cowrie.client.version` |
| `2026-08-22 06:23:47` | `cowrie.client.kex` |
| `2026-08-22 06:23:48` | `cowrie.login.success` |
| `2026-08-22 06:23:48` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:23:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:23:48` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b742ff66fcec

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:23 |
| **Last Seen** | 2026-08-22 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:23:51` | `cowrie.session.connect` |
| `2026-08-22 06:23:51` | `cowrie.client.version` |
| `2026-08-22 06:23:51` | `cowrie.client.kex` |
| `2026-08-22 06:23:52` | `cowrie.login.success` |
| `2026-08-22 06:23:52` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:23:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:23:52` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b113facaad60

| Field | Detail |
|---|---|
| **Source IP** | `175.101.14[.]77` |
| **First Seen** | 2026-08-22 06:29 |
| **Last Seen** | 2026-08-22 06:29 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:29:30` | `cowrie.session.connect` |
| `2026-08-22 06:29:34` | `cowrie.client.version` |
| `2026-08-22 06:29:34` | `cowrie.client.kex` |
| `2026-08-22 06:29:38` | `cowrie.login.success` |
| `2026-08-22 06:29:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.101.14[.]77` to AbuseIPDB if not already reported
- [ ] Block `175.101.14[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd47442df63

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-08-22 06:29 |
| **Last Seen** | 2026-08-22 06:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:29:45` | `cowrie.session.connect` |
| `2026-08-22 06:29:45` | `cowrie.client.version` |
| `2026-08-22 06:29:45` | `cowrie.client.kex` |
| `2026-08-22 06:29:46` | `cowrie.login.success` |
| `2026-08-22 06:29:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ffa0285559e

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-08-22 06:29 |
| **Last Seen** | 2026-08-22 06:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:29:49` | `cowrie.session.connect` |
| `2026-08-22 06:29:50` | `cowrie.telnet.option` |
| `2026-08-22 06:29:50` | `cowrie.telnet.option` |
| `2026-08-22 06:30:50` | `cowrie.login.success` |
| `2026-08-22 06:30:50` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb31bbb0695

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:33 |
| **Last Seen** | 2026-08-22 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:33:16` | `cowrie.session.connect` |
| `2026-08-22 06:33:16` | `cowrie.client.version` |
| `2026-08-22 06:33:17` | `cowrie.client.kex` |
| `2026-08-22 06:33:17` | `cowrie.login.success` |
| `2026-08-22 06:33:18` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:33:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:33:18` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86246f49ea26

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:33 |
| **Last Seen** | 2026-08-22 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:33:20` | `cowrie.session.connect` |
| `2026-08-22 06:33:20` | `cowrie.client.version` |
| `2026-08-22 06:33:20` | `cowrie.client.kex` |
| `2026-08-22 06:33:21` | `cowrie.login.success` |
| `2026-08-22 06:33:21` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:33:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:33:21` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6cf20ece56f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 06:39 |
| **Last Seen** | 2026-08-22 06:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:39:20` | `cowrie.session.connect` |
| `2026-08-22 06:39:20` | `cowrie.client.version` |
| `2026-08-22 06:39:20` | `cowrie.client.kex` |
| `2026-08-22 06:39:21` | `cowrie.login.success` |
| `2026-08-22 06:39:21` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:39:21` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0e7dedc2b5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:42 |
| **Last Seen** | 2026-08-22 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:42:47` | `cowrie.session.connect` |
| `2026-08-22 06:42:47` | `cowrie.client.version` |
| `2026-08-22 06:42:48` | `cowrie.client.kex` |
| `2026-08-22 06:42:49` | `cowrie.login.success` |
| `2026-08-22 06:42:49` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:42:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:42:49` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796d1a00aad8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:42 |
| **Last Seen** | 2026-08-22 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:42:51` | `cowrie.session.connect` |
| `2026-08-22 06:42:51` | `cowrie.client.version` |
| `2026-08-22 06:42:51` | `cowrie.client.kex` |
| `2026-08-22 06:42:52` | `cowrie.login.success` |
| `2026-08-22 06:42:52` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:42:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:42:52` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15024c179255

| Field | Detail |
|---|---|
| **Source IP** | `45.26.184[.]5` |
| **First Seen** | 2026-08-22 06:44 |
| **Last Seen** | 2026-08-22 06:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:44:54` | `cowrie.session.connect` |
| `2026-08-22 06:44:54` | `cowrie.client.version` |
| `2026-08-22 06:44:54` | `cowrie.client.kex` |
| `2026-08-22 06:44:55` | `cowrie.login.success` |
| `2026-08-22 06:44:55` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.26.184[.]5` to AbuseIPDB if not already reported
- [ ] Block `45.26.184[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf644bae9513

| Field | Detail |
|---|---|
| **Source IP** | `37.28.177[.]141` |
| **First Seen** | 2026-08-22 06:45 |
| **Last Seen** | 2026-08-22 06:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:45:01` | `cowrie.session.connect` |
| `2026-08-22 06:45:01` | `cowrie.client.version` |
| `2026-08-22 06:45:01` | `cowrie.client.kex` |
| `2026-08-22 06:45:03` | `cowrie.login.success` |
| `2026-08-22 06:45:03` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.28.177[.]141` to AbuseIPDB if not already reported
- [ ] Block `37.28.177[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc6cfd6a0b5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-22 06:47 |
| **Last Seen** | 2026-08-22 06:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:47:01` | `cowrie.session.connect` |
| `2026-08-22 06:47:01` | `cowrie.client.version` |
| `2026-08-22 06:47:01` | `cowrie.client.kex` |
| `2026-08-22 06:47:02` | `cowrie.login.success` |
| `2026-08-22 06:47:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e5c348592e

| Field | Detail |
|---|---|
| **Source IP** | `96.52.164[.]34` |
| **First Seen** | 2026-08-22 06:47 |
| **Last Seen** | 2026-08-22 06:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:47:07` | `cowrie.session.connect` |
| `2026-08-22 06:47:08` | `cowrie.client.version` |
| `2026-08-22 06:47:08` | `cowrie.client.kex` |
| `2026-08-22 06:47:09` | `cowrie.login.success` |
| `2026-08-22 06:47:10` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.52.164[.]34` to AbuseIPDB if not already reported
- [ ] Block `96.52.164[.]34` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e372aaca24

| Field | Detail |
|---|---|
| **Source IP** | `172.114.43[.]219` |
| **First Seen** | 2026-08-22 06:52 |
| **Last Seen** | 2026-08-22 06:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:52:06` | `cowrie.session.connect` |
| `2026-08-22 06:52:07` | `cowrie.client.version` |
| `2026-08-22 06:52:07` | `cowrie.client.kex` |
| `2026-08-22 06:52:08` | `cowrie.login.success` |
| `2026-08-22 06:52:08` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.114.43[.]219` to AbuseIPDB if not already reported
- [ ] Block `172.114.43[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9371a3c0a6cb

| Field | Detail |
|---|---|
| **Source IP** | `116.114.94[.]242` |
| **First Seen** | 2026-08-22 06:52 |
| **Last Seen** | 2026-08-22 06:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:52:14` | `cowrie.session.connect` |
| `2026-08-22 06:52:14` | `cowrie.client.version` |
| `2026-08-22 06:52:14` | `cowrie.client.kex` |
| `2026-08-22 06:52:17` | `cowrie.login.success` |
| `2026-08-22 06:52:18` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.94[.]242` to AbuseIPDB if not already reported
- [ ] Block `116.114.94[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f760c2da29

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:52 |
| **Last Seen** | 2026-08-22 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:52:25` | `cowrie.session.connect` |
| `2026-08-22 06:52:25` | `cowrie.client.version` |
| `2026-08-22 06:52:25` | `cowrie.client.kex` |
| `2026-08-22 06:52:26` | `cowrie.login.success` |
| `2026-08-22 06:52:26` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:52:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:52:26` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc89577fadc1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 06:52 |
| **Last Seen** | 2026-08-22 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:52:29` | `cowrie.session.connect` |
| `2026-08-22 06:52:29` | `cowrie.client.version` |
| `2026-08-22 06:52:29` | `cowrie.client.kex` |
| `2026-08-22 06:52:30` | `cowrie.login.success` |
| `2026-08-22 06:52:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 06:52:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 06:52:31` | `cowrie.direct-tcpip.data` |
| `2026-08-22 06:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e5a828d673

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-08-22 06:54 |
| **Last Seen** | 2026-08-22 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 06:54:59` | `cowrie.session.connect` |
| `2026-08-22 06:55:00` | `cowrie.client.version` |
| `2026-08-22 06:55:00` | `cowrie.client.kex` |
| `2026-08-22 06:55:02` | `cowrie.login.success` |
| `2026-08-22 06:55:02` | `cowrie.direct-tcpip.request` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-08-22 04:59 | 2026-08-22 06:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.250.119[.]197` | **3** | 2026-08-22 05:29 | 2026-08-22 05:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-22 05:41 | 2026-08-22 06:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | **2** | 2026-08-22 05:51 | 2026-08-22 05:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]105` | **2** | 2026-08-22 05:52 | 2026-08-22 05:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | **2** | 2026-08-22 06:35 | 2026-08-22 06:41 | 1m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-22 05:19 | 2026-08-22 05:19 | 38s | 0 | `T1592` | 🟢 LOW |
| `158.174.70[.]215` | 1 | 2026-08-22 05:09 | 2026-08-22 05:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.255.112[.]183` | 1 | 2026-08-22 06:36 | 2026-08-22 06:36 | 11s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-22 06:37 | 2026-08-22 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.36.252[.]218` | 1 | 2026-08-22 05:33 | 2026-08-22 05:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-08-22 05:49 | 2026-08-22 05:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.139.229[.]71` | 1 | 2026-08-22 04:59 | 2026-08-22 05:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.239.200[.]103` | 1 | 2026-08-22 05:41 | 2026-08-22 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]174` | 1 | 2026-08-22 05:46 | 2026-08-22 05:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `50.217.40[.]11` | 1 | 2026-08-22 05:17 | 2026-08-22 05:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]92` | 1 | 2026-08-22 05:47 | 2026-08-22 05:47 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | 1 | 2026-08-22 05:53 | 2026-08-22 05:53 | 16s | 0 | `T1592` | 🟢 LOW |
| `83.191.179[.]185` | 1 | 2026-08-22 05:49 | 2026-08-22 05:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]9` | 1 | 2026-08-22 06:10 | 2026-08-22 06:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.204.87[.]4` | 1 | 2026-08-22 05:55 | 2026-08-22 05:55 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `46.59.108[.]174` | SE | Bahnhof AB | **100** ⚠️ | 1 |
| `125.59.204[.]176` | HK | HK Cable TV Ltd | **100** ⚠️ | 1 |
| `71.229.1[.]186` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `176.36.252[.]218` | UA | Lanet Network Ltd | **100** ⚠️ | 2 |
| `65.20.133[.]56` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `43.239.200[.]103` | IN | Gtpl Broadband Pvt. Ltd. | **100** ⚠️ | 1 |
| `43.110.37[.]217` | US | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `223.210.27[.]53` | CN | BeiJing Guoxin bilin Telecom Technology Co.,Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 69 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 123 cases |
| Tool 34  | Credential Extractor        | ✅ 89 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (17.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 55 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 69 priority case(s) shown individually · 21 recon entry/entries in table (6 group(s) consolidating 17 session(s)).

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
_Report time: 2026-08-22T08:34:17Z_

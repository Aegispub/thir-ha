# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-04 |
| **Generated At** | 2026-08-04T23:06:37Z |
| **Shift Time** | 23:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **154** |
| Confirmed Threats | **132** |
| False Positives Filtered | **22** (14.3%) |
| Unique Attacker IPs | **98** |
| Countries of Origin | **29** |
| High Severity Cases | **77** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **85** |
| Unique Credential Pairs | **55** |
| Unique Usernames | **24** |
| Unique Passwords | **52** |
| Successful Auth Pairs | **79** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `admin` | 13 |
| `support` | 4 |
| `tcpdump` | 4 |
| `default` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 6 |
| `support` | 4 |
| `password` | 4 |
| `1111` | 4 |
| `123@@@` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 6 |
| `support` | `support` | 4 |
| `root` | `123@@@` | 4 |
| `tcpdump` | `tcpdump` | 4 |
| `admin` | `qwerty12` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `130.12.182.224` | 2026-08-04T20:56:15 |
| `root` | `violate` | `130.12.182.223` | 2026-08-04T20:56:52 |
| `root` | `Password1` | `58.34.174.90` | 2026-08-04T20:57:46 |
| `admin` | `Admin@123` | `130.12.182.107` | 2026-08-04T20:57:56 |
| `root` | `international` | `102.220.160.39` | 2026-08-04T20:59:37 |
| `root` | `R1512hashish@` | `130.12.182.223` | 2026-08-04T21:00:35 |
| `root` | `redhat123` | `93.152.221.206` | 2026-08-04T21:00:44 |
| `user3` | `1234` | `45.153.34.226` | 2026-08-04T21:00:47 |
| `root` | `debian` | `14.116.184.171` | 2026-08-04T21:01:16 |
| `default` | `administrator` | `59.34.17.130` | 2026-08-04T21:03:52 |
| `support` | `support` | `10.0.0.73` | 2026-08-04T21:03:57 |
| `default` | `administrator` | `178.178.222.59` | 2026-08-04T21:04:06 |
| `default` | `administrator` | `195.222.57.190` | 2026-08-04T21:04:18 |
| `root` | `` | `93.152.221.210` | 2026-08-04T21:04:39 |
| `username` | `password` | `64.89.161.90` | 2026-08-04T21:06:18 |
| `postgres` | `postgres123456` | `45.156.87.192` | 2026-08-04T21:07:32 |
| `root` | `monster0` | `45.156.87.182` | 2026-08-04T21:14:44 |
| `ubnt` | `1111` | `202.72.196.75` | 2026-08-04T21:14:47 |
| `ubnt` | `1111` | `116.48.150.115` | 2026-08-04T21:14:56 |
| `root` | `99` | `116.72.9.151` | 2026-08-04T21:15:51 |
| `root` | `99` | `195.158.26.59` | 2026-08-04T21:16:03 |
| `test` | `1111` | `10.0.0.73` | 2026-08-04T21:19:31 |
| `ubuntu` | `data@123` | `94.26.106.19` | 2026-08-04T21:19:43 |
| `username` | `password` | `93.152.221.210` | 2026-08-04T21:20:35 |
| `scott` | `password` | `64.89.162.146` | 2026-08-04T21:24:39 |
| `root` | `jiaqun@001` | `130.12.182.107` | 2026-08-04T21:25:07 |
| `guayaquil` | `guayaquil` | `130.12.181.21` | 2026-08-04T21:27:29 |
| `root` | `benito1` | `130.12.182.107` | 2026-08-04T21:31:59 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-04T21:36:59 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-04T21:36:59 |
| `root` | `jjjjjj1` | `130.12.182.107` | 2026-08-04T21:37:07 |
| `test` | `1111` | `178.178.222.59` | 2026-08-04T21:38:01 |
| `squid` | `squid` | `130.12.182.227` | 2026-08-04T21:41:18 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-04T21:48:09 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-04T21:48:09 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-04T21:48:15 |
| `admin` | `admin6` | `10.0.0.73` | 2026-08-04T21:49:00 |
| `CONNECT 130.12.182.231:80 HTTP/1.0` | `Host: 130.12.182.231:80` | `130.12.182.231` | 2026-08-04T21:49:28 |
| `root` | `monkey02` | `45.156.87.192` | 2026-08-04T21:51:09 |
| `admin` | `123456789` | `45.153.34.226` | 2026-08-04T21:51:23 |
| `laurent` | `laurent123!` | `102.220.160.39` | 2026-08-04T21:55:39 |
| `admin` | `admin@1234` | `93.152.221.50` | 2026-08-04T21:57:11 |
| `tcpdump` | `tcpdump` | `10.0.0.73` | 2026-08-04T22:00:57 |
| `sanjay` | `sanjay123` | `93.152.221.50` | 2026-08-04T22:05:53 |
| `ubnt` | `ubnt` | `93.152.221.210` | 2026-08-04T22:06:23 |
| `support` | `support` | `176.53.159.196` | 2026-08-04T22:06:40 |
| `admin` | `admin6` | `60.18.139.82` | 2026-08-04T22:06:51 |
| `admin` | `admin6` | `65.20.149.239` | 2026-08-04T22:07:00 |
| `root` | `Qwer@2025` | `102.220.160.41` | 2026-08-04T22:09:39 |
| `root` | `kaylin1` | `64.89.161.90` | 2026-08-04T22:11:17 |
| `admin` | `Huawei@123` | `110.25.109.54` | 2026-08-04T22:12:30 |
| `username` | `password` | `102.220.160.42` | 2026-08-04T22:14:03 |
| `root` | `051281` | `130.12.182.227` | 2026-08-04T22:16:44 |
| `proxyuser` | `proxyuser` | `130.12.182.224` | 2026-08-04T22:17:54 |
| `tcpdump` | `tcpdump` | `218.59.235.170` | 2026-08-04T22:18:20 |
| `tcpdump` | `tcpdump` | `211.238.237.254` | 2026-08-04T22:18:29 |
| `root` | `fa` | `94.26.106.33` | 2026-08-04T22:22:05 |
| `supervisor` | `supervisor10` | `10.0.0.73` | 2026-08-04T22:23:22 |
| `admin` | `qwerty12` | `218.13.214.18` | 2026-08-04T22:23:27 |
| `admin` | `qwerty12` | `103.29.185.162` | 2026-08-04T22:23:39 |
| `supervisor` | `supervisor10` | `62.201.212.54` | 2026-08-04T22:24:47 |
| `root` | `1r2o3o4t` | `130.12.182.227` | 2026-08-04T22:25:18 |
| `operator` | `operator` | `64.89.162.146` | 2026-08-04T22:26:30 |
| `debian1` | `debian` | `93.152.221.206` | 2026-08-04T22:27:21 |
| `admin` | `admin01` | `93.152.221.50` | 2026-08-04T22:28:12 |
| `root` | `1q2w3e4` | `93.152.221.50` | 2026-08-04T22:33:04 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-08-04T22:35:13 |
| `root` | `123@@@` | `165.1.75.106` | 2026-08-04T22:35:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-04T22:35:42 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-04T22:35:42 |
| `root` | `crazyfrog1` | `130.12.181.23` | 2026-08-04T22:38:29 |
| `root` | `Dilip@123` | `93.152.221.50` | 2026-08-04T22:43:03 |
| `user` | `123456` | `49.124.152.229` | 2026-08-04T22:46:39 |
| `ganesh` | `ganesh123` | `94.26.106.19` | 2026-08-04T22:46:46 |
| `user` | `123456` | `65.20.179.251` | 2026-08-04T22:46:50 |
| `Ubuntu` | `Mor@2025` | `130.12.182.230` | 2026-08-04T22:47:29 |
| `support` | `support` | `45.154.244.193` | 2026-08-04T22:49:54 |
| `admin` | `qwerty12` | `96.1.40.151` | 2026-08-04T22:52:35 |
| `admin` | `qwerty12` | `200.159.14.187` | 2026-08-04T22:52:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **154** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 47 |
| OpenSSH | 23 |
| Paramiko (Python) | 12 |
| Go SSH scanner | 7 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `a591c4ddccc9...` | Mirai/variant | 40 | 20 |
| `acaa53e0a7d7...` | Mirai/variant | 22 | 21 |
| `a2de0f306611...` | Mirai/variant | 12 | 4 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `a591c4ddccc9...` | libssh | 40 | 20 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 22 | 21 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 12 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **98** |
| Unique ASNs | **61** |
| High-Risk ASNs | **43** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS197769` | VPS Dedicated LLC | 11 | HIGH |
| `AS197170` | TechTies Inc. | 8 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS25229` | Limited Liability Company KYIVSKI TELEKOMUNIKATSIYNI MEREZHI | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (77)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fa8250a9da97

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-04 20:56 |
| **Last Seen** | 2026-08-04 20:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 20:56:15` | `cowrie.session.connect` |
| `2026-08-04 20:56:15` | `cowrie.client.version` |
| `2026-08-04 20:56:15` | `cowrie.client.kex` |
| `2026-08-04 20:56:15` | `cowrie.login.success` |
| `2026-08-04 20:56:15` | `cowrie.direct-tcpip.request` |
| `2026-08-04 20:56:15` | `cowrie.direct-tcpip.data` |
| `2026-08-04 20:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c15478c7bf

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-04 20:56 |
| **Last Seen** | 2026-08-04 20:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 20:56:52` | `cowrie.session.connect` |
| `2026-08-04 20:56:52` | `cowrie.client.version` |
| `2026-08-04 20:56:52` | `cowrie.client.kex` |
| `2026-08-04 20:56:52` | `cowrie.login.success` |
| `2026-08-04 20:56:52` | `cowrie.direct-tcpip.request` |
| `2026-08-04 20:56:53` | `cowrie.direct-tcpip.data` |
| `2026-08-04 20:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97331f2ce6e4

| Field | Detail |
|---|---|
| **Source IP** | `58.34.174[.]90` |
| **First Seen** | 2026-08-04 20:57 |
| **Last Seen** | 2026-08-04 20:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 20:57:43` | `cowrie.session.connect` |
| `2026-08-04 20:57:43` | `cowrie.client.version` |
| `2026-08-04 20:57:43` | `cowrie.client.kex` |
| `2026-08-04 20:57:46` | `cowrie.login.success` |
| `2026-08-04 20:57:46` | `cowrie.direct-tcpip.request` |
| `2026-08-04 20:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.34.174[.]90` to AbuseIPDB if not already reported
- [ ] Block `58.34.174[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38a7827ec46b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 20:57 |
| **Last Seen** | 2026-08-04 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 20:57:55` | `cowrie.session.connect` |
| `2026-08-04 20:57:55` | `cowrie.client.version` |
| `2026-08-04 20:57:55` | `cowrie.client.kex` |
| `2026-08-04 20:57:56` | `cowrie.login.success` |
| `2026-08-04 20:57:56` | `cowrie.direct-tcpip.request` |
| `2026-08-04 20:57:56` | `cowrie.direct-tcpip.data` |
| `2026-08-04 20:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d13ba21beb

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-08-04 20:59 |
| **Last Seen** | 2026-08-04 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 20:59:36` | `cowrie.session.connect` |
| `2026-08-04 20:59:36` | `cowrie.client.version` |
| `2026-08-04 20:59:37` | `cowrie.client.kex` |
| `2026-08-04 20:59:37` | `cowrie.login.success` |
| `2026-08-04 20:59:37` | `cowrie.direct-tcpip.request` |
| `2026-08-04 20:59:37` | `cowrie.direct-tcpip.data` |
| `2026-08-04 20:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d697aa5ea1f

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-04 21:00 |
| **Last Seen** | 2026-08-04 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:00:35` | `cowrie.session.connect` |
| `2026-08-04 21:00:35` | `cowrie.client.version` |
| `2026-08-04 21:00:35` | `cowrie.client.kex` |
| `2026-08-04 21:00:35` | `cowrie.login.success` |
| `2026-08-04 21:00:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:00:35` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c931d9a8afe8

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-04 21:00 |
| **Last Seen** | 2026-08-04 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:00:43` | `cowrie.session.connect` |
| `2026-08-04 21:00:43` | `cowrie.client.version` |
| `2026-08-04 21:00:43` | `cowrie.client.kex` |
| `2026-08-04 21:00:44` | `cowrie.login.success` |
| `2026-08-04 21:00:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:00:44` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c721745c9bf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-04 21:00 |
| **Last Seen** | 2026-08-04 21:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:00:47` | `cowrie.session.connect` |
| `2026-08-04 21:00:47` | `cowrie.client.version` |
| `2026-08-04 21:00:47` | `cowrie.client.kex` |
| `2026-08-04 21:00:47` | `cowrie.login.success` |
| `2026-08-04 21:00:47` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:00:47` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd0fff4fe2a

| Field | Detail |
|---|---|
| **Source IP** | `14.116.184[.]171` |
| **First Seen** | 2026-08-04 21:01 |
| **Last Seen** | 2026-08-04 21:02 |
| **Session Duration** | 93s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:01:15` | `cowrie.session.connect` |
| `2026-08-04 21:01:15` | `cowrie.client.version` |
| `2026-08-04 21:01:15` | `cowrie.client.kex` |
| `2026-08-04 21:01:16` | `cowrie.login.success` |
| `2026-08-04 21:02:48` | `cowrie.session.file_upload` |
| `2026-08-04 21:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.116.184[.]171` to AbuseIPDB if not already reported
- [ ] Block `14.116.184[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a0dffd27a0

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-08-04 21:03 |
| **Last Seen** | 2026-08-04 21:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:03:49` | `cowrie.session.connect` |
| `2026-08-04 21:03:50` | `cowrie.client.version` |
| `2026-08-04 21:03:50` | `cowrie.client.kex` |
| `2026-08-04 21:03:52` | `cowrie.login.success` |
| `2026-08-04 21:03:53` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-648a82a44cd8

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-04 21:04 |
| **Last Seen** | 2026-08-04 21:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:04:03` | `cowrie.session.connect` |
| `2026-08-04 21:04:03` | `cowrie.client.version` |
| `2026-08-04 21:04:03` | `cowrie.client.kex` |
| `2026-08-04 21:04:06` | `cowrie.login.success` |
| `2026-08-04 21:04:08` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32af95a16f9

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-04 21:04 |
| **Last Seen** | 2026-08-04 21:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:04:17` | `cowrie.session.connect` |
| `2026-08-04 21:04:17` | `cowrie.client.version` |
| `2026-08-04 21:04:17` | `cowrie.client.kex` |
| `2026-08-04 21:04:18` | `cowrie.login.success` |
| `2026-08-04 21:04:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824d6ccf4e51

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-04 21:04 |
| **Last Seen** | 2026-08-04 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:04:39` | `cowrie.session.connect` |
| `2026-08-04 21:04:39` | `cowrie.client.version` |
| `2026-08-04 21:04:39` | `cowrie.client.kex` |
| `2026-08-04 21:04:39` | `cowrie.login.success` |
| `2026-08-04 21:04:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:04:39` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa01dd485aef

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-04 21:06 |
| **Last Seen** | 2026-08-04 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:06:18` | `cowrie.session.connect` |
| `2026-08-04 21:06:18` | `cowrie.client.version` |
| `2026-08-04 21:06:18` | `cowrie.client.kex` |
| `2026-08-04 21:06:18` | `cowrie.login.success` |
| `2026-08-04 21:06:19` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:06:19` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b7888120ede

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 21:07 |
| **Last Seen** | 2026-08-04 21:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:07:31` | `cowrie.session.connect` |
| `2026-08-04 21:07:31` | `cowrie.client.version` |
| `2026-08-04 21:07:31` | `cowrie.client.kex` |
| `2026-08-04 21:07:32` | `cowrie.login.success` |
| `2026-08-04 21:07:32` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:07:32` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0dfe1528522

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-04 21:14 |
| **Last Seen** | 2026-08-04 21:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:14:43` | `cowrie.session.connect` |
| `2026-08-04 21:14:43` | `cowrie.client.version` |
| `2026-08-04 21:14:43` | `cowrie.client.kex` |
| `2026-08-04 21:14:44` | `cowrie.login.success` |
| `2026-08-04 21:14:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:14:44` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb60f2e27676

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-04 21:14 |
| **Last Seen** | 2026-08-04 21:19 |
| **Session Duration** | 278s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:14:45` | `cowrie.session.connect` |
| `2026-08-04 21:14:45` | `cowrie.client.version` |
| `2026-08-04 21:14:45` | `cowrie.client.kex` |
| `2026-08-04 21:14:47` | `cowrie.login.success` |
| `2026-08-04 21:14:48` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aea676de283

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-08-04 21:14 |
| **Last Seen** | 2026-08-04 21:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:14:53` | `cowrie.session.connect` |
| `2026-08-04 21:14:54` | `cowrie.client.version` |
| `2026-08-04 21:14:54` | `cowrie.client.kex` |
| `2026-08-04 21:14:56` | `cowrie.login.success` |
| `2026-08-04 21:14:57` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b3751ac6f5

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-04 21:15 |
| **Last Seen** | 2026-08-04 21:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:15:48` | `cowrie.session.connect` |
| `2026-08-04 21:15:49` | `cowrie.client.version` |
| `2026-08-04 21:15:49` | `cowrie.client.kex` |
| `2026-08-04 21:15:51` | `cowrie.login.success` |
| `2026-08-04 21:15:52` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9094731eb69a

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-08-04 21:16 |
| **Last Seen** | 2026-08-04 21:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:16:01` | `cowrie.session.connect` |
| `2026-08-04 21:16:02` | `cowrie.client.version` |
| `2026-08-04 21:16:02` | `cowrie.client.kex` |
| `2026-08-04 21:16:03` | `cowrie.login.success` |
| `2026-08-04 21:16:03` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4e82228861

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-04 21:19 |
| **Last Seen** | 2026-08-04 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:19:43` | `cowrie.session.connect` |
| `2026-08-04 21:19:43` | `cowrie.client.version` |
| `2026-08-04 21:19:43` | `cowrie.client.kex` |
| `2026-08-04 21:19:43` | `cowrie.login.success` |
| `2026-08-04 21:19:43` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:19:43` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e73913c615

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-04 21:20 |
| **Last Seen** | 2026-08-04 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:20:34` | `cowrie.session.connect` |
| `2026-08-04 21:20:34` | `cowrie.client.version` |
| `2026-08-04 21:20:34` | `cowrie.client.kex` |
| `2026-08-04 21:20:35` | `cowrie.login.success` |
| `2026-08-04 21:20:35` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:20:35` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:20:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-753fa0ba1694

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-04 21:24 |
| **Last Seen** | 2026-08-04 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:24:38` | `cowrie.session.connect` |
| `2026-08-04 21:24:38` | `cowrie.client.version` |
| `2026-08-04 21:24:38` | `cowrie.client.kex` |
| `2026-08-04 21:24:39` | `cowrie.login.success` |
| `2026-08-04 21:24:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:24:39` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-780187cc7fdb

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 21:25 |
| **Last Seen** | 2026-08-04 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:25:06` | `cowrie.session.connect` |
| `2026-08-04 21:25:06` | `cowrie.client.version` |
| `2026-08-04 21:25:07` | `cowrie.client.kex` |
| `2026-08-04 21:25:07` | `cowrie.login.success` |
| `2026-08-04 21:25:07` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:25:07` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9891d98428ff

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-04 21:27 |
| **Last Seen** | 2026-08-04 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:27:28` | `cowrie.session.connect` |
| `2026-08-04 21:27:28` | `cowrie.client.version` |
| `2026-08-04 21:27:28` | `cowrie.client.kex` |
| `2026-08-04 21:27:29` | `cowrie.login.success` |
| `2026-08-04 21:27:29` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:27:29` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aec3a47090a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 21:31 |
| **Last Seen** | 2026-08-04 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:31:58` | `cowrie.session.connect` |
| `2026-08-04 21:31:58` | `cowrie.client.version` |
| `2026-08-04 21:31:58` | `cowrie.client.kex` |
| `2026-08-04 21:31:59` | `cowrie.login.success` |
| `2026-08-04 21:31:59` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:31:59` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03fa37f922f3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 21:36 |
| **Last Seen** | 2026-08-04 21:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:36:59` | `cowrie.session.connect` |
| `2026-08-04 21:36:59` | `cowrie.client.version` |
| `2026-08-04 21:36:59` | `cowrie.client.kex` |
| `2026-08-04 21:36:59` | `cowrie.login.success` |
| `2026-08-04 21:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54b18e10b43

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-04 21:36 |
| **Last Seen** | 2026-08-04 21:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:36:59` | `cowrie.session.connect` |
| `2026-08-04 21:36:59` | `cowrie.client.version` |
| `2026-08-04 21:36:59` | `cowrie.client.kex` |
| `2026-08-04 21:36:59` | `cowrie.login.success` |
| `2026-08-04 21:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e8e1e55bcd

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-04 21:37 |
| **Last Seen** | 2026-08-04 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:37:06` | `cowrie.session.connect` |
| `2026-08-04 21:37:06` | `cowrie.client.version` |
| `2026-08-04 21:37:06` | `cowrie.client.kex` |
| `2026-08-04 21:37:07` | `cowrie.login.success` |
| `2026-08-04 21:37:07` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:37:07` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd40e04b9398

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-04 21:37 |
| **Last Seen** | 2026-08-04 21:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:37:59` | `cowrie.session.connect` |
| `2026-08-04 21:37:59` | `cowrie.client.version` |
| `2026-08-04 21:37:59` | `cowrie.client.kex` |
| `2026-08-04 21:38:01` | `cowrie.login.success` |
| `2026-08-04 21:38:02` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56768d0cf425

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-04 21:41 |
| **Last Seen** | 2026-08-04 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:41:17` | `cowrie.session.connect` |
| `2026-08-04 21:41:17` | `cowrie.client.version` |
| `2026-08-04 21:41:17` | `cowrie.client.kex` |
| `2026-08-04 21:41:18` | `cowrie.login.success` |
| `2026-08-04 21:41:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:41:18` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7648cce1c60

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 21:48 |
| **Last Seen** | 2026-08-04 21:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:48:08` | `cowrie.session.connect` |
| `2026-08-04 21:48:08` | `cowrie.client.version` |
| `2026-08-04 21:48:08` | `cowrie.client.kex` |
| `2026-08-04 21:48:09` | `cowrie.login.success` |
| `2026-08-04 21:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1229c1a4959f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 21:48 |
| **Last Seen** | 2026-08-04 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:48:08` | `cowrie.session.connect` |
| `2026-08-04 21:48:08` | `cowrie.client.version` |
| `2026-08-04 21:48:08` | `cowrie.client.kex` |
| `2026-08-04 21:48:09` | `cowrie.login.success` |
| `2026-08-04 21:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3bf4278aefd

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 21:48 |
| **Last Seen** | 2026-08-04 21:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:48:14` | `cowrie.session.connect` |
| `2026-08-04 21:48:14` | `cowrie.client.version` |
| `2026-08-04 21:48:14` | `cowrie.client.kex` |
| `2026-08-04 21:48:15` | `cowrie.login.success` |
| `2026-08-04 21:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbf861dae4cb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-04 21:48 |
| **Last Seen** | 2026-08-04 21:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:48:15` | `cowrie.session.connect` |
| `2026-08-04 21:48:15` | `cowrie.client.version` |
| `2026-08-04 21:48:15` | `cowrie.client.kex` |
| `2026-08-04 21:48:16` | `cowrie.login.success` |
| `2026-08-04 21:48:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff05d2a1ca37

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]231` |
| **First Seen** | 2026-08-04 21:49 |
| **Last Seen** | 2026-08-04 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:49:28` | `cowrie.session.connect` |
| `2026-08-04 21:49:28` | `cowrie.login.success` |
| `2026-08-04 21:49:28` | `cowrie.session.params` |
| `2026-08-04 21:49:28` | `cowrie.command.input` |
| `2026-08-04 21:49:29` | `cowrie.log.closed` |
| `2026-08-04 21:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]231` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8934185847d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-04 21:51 |
| **Last Seen** | 2026-08-04 21:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:51:09` | `cowrie.session.connect` |
| `2026-08-04 21:51:09` | `cowrie.client.version` |
| `2026-08-04 21:51:09` | `cowrie.client.kex` |
| `2026-08-04 21:51:09` | `cowrie.login.success` |
| `2026-08-04 21:51:09` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:51:09` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f631f64f2b26

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-04 21:51 |
| **Last Seen** | 2026-08-04 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:51:22` | `cowrie.session.connect` |
| `2026-08-04 21:51:22` | `cowrie.client.version` |
| `2026-08-04 21:51:22` | `cowrie.client.kex` |
| `2026-08-04 21:51:23` | `cowrie.login.success` |
| `2026-08-04 21:51:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:51:23` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb9455d48c2

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-08-04 21:55 |
| **Last Seen** | 2026-08-04 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:55:38` | `cowrie.session.connect` |
| `2026-08-04 21:55:38` | `cowrie.client.version` |
| `2026-08-04 21:55:38` | `cowrie.client.kex` |
| `2026-08-04 21:55:39` | `cowrie.login.success` |
| `2026-08-04 21:55:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:55:39` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ec7304ff14

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-04 21:57 |
| **Last Seen** | 2026-08-04 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 21:57:11` | `cowrie.session.connect` |
| `2026-08-04 21:57:11` | `cowrie.client.version` |
| `2026-08-04 21:57:11` | `cowrie.client.kex` |
| `2026-08-04 21:57:11` | `cowrie.login.success` |
| `2026-08-04 21:57:11` | `cowrie.direct-tcpip.request` |
| `2026-08-04 21:57:11` | `cowrie.direct-tcpip.data` |
| `2026-08-04 21:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36eef5d68f90

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-04 22:05 |
| **Last Seen** | 2026-08-04 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:05:53` | `cowrie.session.connect` |
| `2026-08-04 22:05:53` | `cowrie.client.version` |
| `2026-08-04 22:05:53` | `cowrie.client.kex` |
| `2026-08-04 22:05:53` | `cowrie.login.success` |
| `2026-08-04 22:05:53` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:05:53` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca298354d14

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]210` |
| **First Seen** | 2026-08-04 22:06 |
| **Last Seen** | 2026-08-04 22:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:06:23` | `cowrie.session.connect` |
| `2026-08-04 22:06:23` | `cowrie.client.version` |
| `2026-08-04 22:06:23` | `cowrie.client.kex` |
| `2026-08-04 22:06:23` | `cowrie.login.success` |
| `2026-08-04 22:06:23` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:06:23` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]210` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e79823f48ec

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-04 22:06 |
| **Last Seen** | 2026-08-04 22:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:06:40` | `cowrie.session.connect` |
| `2026-08-04 22:06:40` | `cowrie.client.version` |
| `2026-08-04 22:06:40` | `cowrie.client.kex` |
| `2026-08-04 22:06:40` | `cowrie.login.success` |
| `2026-08-04 22:06:40` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:06:40` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81515ca69c1

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-08-04 22:06 |
| **Last Seen** | 2026-08-04 22:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:06:48` | `cowrie.session.connect` |
| `2026-08-04 22:06:49` | `cowrie.client.version` |
| `2026-08-04 22:06:49` | `cowrie.client.kex` |
| `2026-08-04 22:06:51` | `cowrie.login.success` |
| `2026-08-04 22:06:52` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3bb562bd37b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]239` |
| **First Seen** | 2026-08-04 22:06 |
| **Last Seen** | 2026-08-04 22:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:06:58` | `cowrie.session.connect` |
| `2026-08-04 22:06:58` | `cowrie.client.version` |
| `2026-08-04 22:06:58` | `cowrie.client.kex` |
| `2026-08-04 22:07:00` | `cowrie.login.success` |
| `2026-08-04 22:07:00` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]239` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747ef709140d

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]41` |
| **First Seen** | 2026-08-04 22:09 |
| **Last Seen** | 2026-08-04 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:09:38` | `cowrie.session.connect` |
| `2026-08-04 22:09:38` | `cowrie.client.version` |
| `2026-08-04 22:09:39` | `cowrie.client.kex` |
| `2026-08-04 22:09:39` | `cowrie.login.success` |
| `2026-08-04 22:09:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:09:39` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]41` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50dbd276d0b4

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]90` |
| **First Seen** | 2026-08-04 22:11 |
| **Last Seen** | 2026-08-04 22:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:11:17` | `cowrie.session.connect` |
| `2026-08-04 22:11:17` | `cowrie.client.version` |
| `2026-08-04 22:11:17` | `cowrie.client.kex` |
| `2026-08-04 22:11:17` | `cowrie.login.success` |
| `2026-08-04 22:11:17` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:11:18` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]90` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20992b2579af

| Field | Detail |
|---|---|
| **Source IP** | `110.25.109[.]54` |
| **First Seen** | 2026-08-04 22:12 |
| **Last Seen** | 2026-08-04 22:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:12:27` | `cowrie.session.connect` |
| `2026-08-04 22:12:28` | `cowrie.client.version` |
| `2026-08-04 22:12:28` | `cowrie.client.kex` |
| `2026-08-04 22:12:30` | `cowrie.login.success` |
| `2026-08-04 22:12:30` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.109[.]54` to AbuseIPDB if not already reported
- [ ] Block `110.25.109[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b190902259

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-04 22:14 |
| **Last Seen** | 2026-08-04 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:14:02` | `cowrie.session.connect` |
| `2026-08-04 22:14:02` | `cowrie.client.version` |
| `2026-08-04 22:14:03` | `cowrie.client.kex` |
| `2026-08-04 22:14:03` | `cowrie.login.success` |
| `2026-08-04 22:14:03` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:14:03` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f8d774a35a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-04 22:16 |
| **Last Seen** | 2026-08-04 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:16:43` | `cowrie.session.connect` |
| `2026-08-04 22:16:43` | `cowrie.client.version` |
| `2026-08-04 22:16:43` | `cowrie.client.kex` |
| `2026-08-04 22:16:44` | `cowrie.login.success` |
| `2026-08-04 22:16:44` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:16:44` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f4f4465d64

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-04 22:17 |
| **Last Seen** | 2026-08-04 22:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:17:54` | `cowrie.session.connect` |
| `2026-08-04 22:17:54` | `cowrie.client.version` |
| `2026-08-04 22:17:54` | `cowrie.client.kex` |
| `2026-08-04 22:17:54` | `cowrie.login.success` |
| `2026-08-04 22:17:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:17:54` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85bdad997509

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-08-04 22:18 |
| **Last Seen** | 2026-08-04 22:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:18:16` | `cowrie.session.connect` |
| `2026-08-04 22:18:17` | `cowrie.client.version` |
| `2026-08-04 22:18:17` | `cowrie.client.kex` |
| `2026-08-04 22:18:20` | `cowrie.login.success` |
| `2026-08-04 22:18:21` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8befe31cada

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-08-04 22:18 |
| **Last Seen** | 2026-08-04 22:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:18:26` | `cowrie.session.connect` |
| `2026-08-04 22:18:27` | `cowrie.client.version` |
| `2026-08-04 22:18:27` | `cowrie.client.kex` |
| `2026-08-04 22:18:29` | `cowrie.login.success` |
| `2026-08-04 22:18:30` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76cf835b53b9

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]33` |
| **First Seen** | 2026-08-04 22:22 |
| **Last Seen** | 2026-08-04 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:22:04` | `cowrie.session.connect` |
| `2026-08-04 22:22:04` | `cowrie.client.version` |
| `2026-08-04 22:22:04` | `cowrie.client.kex` |
| `2026-08-04 22:22:05` | `cowrie.login.success` |
| `2026-08-04 22:22:05` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:22:05` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]33` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f15e6437c762

| Field | Detail |
|---|---|
| **Source IP** | `218.13.214[.]18` |
| **First Seen** | 2026-08-04 22:23 |
| **Last Seen** | 2026-08-04 22:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:23:25` | `cowrie.session.connect` |
| `2026-08-04 22:23:25` | `cowrie.client.version` |
| `2026-08-04 22:23:25` | `cowrie.client.kex` |
| `2026-08-04 22:23:27` | `cowrie.login.success` |
| `2026-08-04 22:23:28` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.13.214[.]18` to AbuseIPDB if not already reported
- [ ] Block `218.13.214[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d26d2ac2f2

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-04 22:23 |
| **Last Seen** | 2026-08-04 22:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:23:34` | `cowrie.session.connect` |
| `2026-08-04 22:23:36` | `cowrie.client.version` |
| `2026-08-04 22:23:36` | `cowrie.client.kex` |
| `2026-08-04 22:23:39` | `cowrie.login.success` |
| `2026-08-04 22:23:40` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642ce0d065c2

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-04 22:24 |
| **Last Seen** | 2026-08-04 22:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:24:45` | `cowrie.session.connect` |
| `2026-08-04 22:24:46` | `cowrie.client.version` |
| `2026-08-04 22:24:46` | `cowrie.client.kex` |
| `2026-08-04 22:24:47` | `cowrie.login.success` |
| `2026-08-04 22:24:47` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28e127c4614

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-04 22:25 |
| **Last Seen** | 2026-08-04 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:25:17` | `cowrie.session.connect` |
| `2026-08-04 22:25:17` | `cowrie.client.version` |
| `2026-08-04 22:25:17` | `cowrie.client.kex` |
| `2026-08-04 22:25:18` | `cowrie.login.success` |
| `2026-08-04 22:25:18` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:25:18` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c72e8bc8f8

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-04 22:26 |
| **Last Seen** | 2026-08-04 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:26:30` | `cowrie.session.connect` |
| `2026-08-04 22:26:30` | `cowrie.client.version` |
| `2026-08-04 22:26:30` | `cowrie.client.kex` |
| `2026-08-04 22:26:30` | `cowrie.login.success` |
| `2026-08-04 22:26:31` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:26:31` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6c8e7e1712

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]206` |
| **First Seen** | 2026-08-04 22:27 |
| **Last Seen** | 2026-08-04 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:27:21` | `cowrie.session.connect` |
| `2026-08-04 22:27:21` | `cowrie.client.version` |
| `2026-08-04 22:27:21` | `cowrie.client.kex` |
| `2026-08-04 22:27:21` | `cowrie.login.success` |
| `2026-08-04 22:27:22` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:27:22` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]206` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2273018bb8

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-04 22:28 |
| **Last Seen** | 2026-08-04 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:28:11` | `cowrie.session.connect` |
| `2026-08-04 22:28:11` | `cowrie.client.version` |
| `2026-08-04 22:28:11` | `cowrie.client.kex` |
| `2026-08-04 22:28:12` | `cowrie.login.success` |
| `2026-08-04 22:28:12` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:28:12` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651f60f7294f

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-04 22:33 |
| **Last Seen** | 2026-08-04 22:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:33:04` | `cowrie.session.connect` |
| `2026-08-04 22:33:04` | `cowrie.client.version` |
| `2026-08-04 22:33:04` | `cowrie.client.kex` |
| `2026-08-04 22:33:04` | `cowrie.login.success` |
| `2026-08-04 22:33:04` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:33:04` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fd9a716b84

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-04 22:35 |
| **Last Seen** | 2026-08-04 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:35:13` | `cowrie.session.connect` |
| `2026-08-04 22:35:13` | `cowrie.client.version` |
| `2026-08-04 22:35:13` | `cowrie.client.kex` |
| `2026-08-04 22:35:13` | `cowrie.login.success` |
| `2026-08-04 22:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d5605c12a8

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-04 22:35 |
| **Last Seen** | 2026-08-04 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:35:13` | `cowrie.session.connect` |
| `2026-08-04 22:35:13` | `cowrie.client.version` |
| `2026-08-04 22:35:13` | `cowrie.client.kex` |
| `2026-08-04 22:35:13` | `cowrie.login.success` |
| `2026-08-04 22:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ec2fdad5f5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-04 22:35 |
| **Last Seen** | 2026-08-04 22:37 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:35:37` | `cowrie.session.connect` |
| `2026-08-04 22:35:37` | `cowrie.client.version` |
| `2026-08-04 22:35:37` | `cowrie.client.kex` |
| `2026-08-04 22:35:37` | `cowrie.login.success` |
| `2026-08-04 22:35:38` | `cowrie.session.file_upload` |
| `2026-08-04 22:35:39` | `cowrie.session.params` |
| `2026-08-04 22:35:39` | `cowrie.command.input` |
| `2026-08-04 22:35:39` | `cowrie.command.input` |
| `2026-08-04 22:35:39` | `cowrie.command.input` |
| `2026-08-04 22:35:39` | `cowrie.command.failed` |
| `2026-08-04 22:35:39` | `cowrie.log.closed` |
| `2026-08-04 22:35:40` | `cowrie.session.params` |
| `2026-08-04 22:35:40` | `cowrie.command.input` |
| `2026-08-04 22:35:40` | `cowrie.log.closed` |
| `2026-08-04 22:35:40` | `cowrie.session.params` |
| `2026-08-04 22:35:40` | `cowrie.command.input` |
| `2026-08-04 22:35:41` | `cowrie.log.closed` |
| `2026-08-04 22:35:41` | `cowrie.session.params` |
| `2026-08-04 22:35:41` | `cowrie.command.input` |
| `2026-08-04 22:35:41` | `cowrie.command.failed` |
| `2026-08-04 22:35:41` | `cowrie.command.failed` |
| `2026-08-04 22:36:42` | `cowrie.session.params` |
| `2026-08-04 22:36:42` | `cowrie.command.input` |
| `2026-08-04 22:37:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59290cdf495e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 22:35 |
| **Last Seen** | 2026-08-04 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:35:40` | `cowrie.session.connect` |
| `2026-08-04 22:35:40` | `cowrie.client.version` |
| `2026-08-04 22:35:41` | `cowrie.client.kex` |
| `2026-08-04 22:35:42` | `cowrie.login.success` |
| `2026-08-04 22:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-888a011cc499

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-04 22:35 |
| **Last Seen** | 2026-08-04 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:35:40` | `cowrie.session.connect` |
| `2026-08-04 22:35:40` | `cowrie.client.version` |
| `2026-08-04 22:35:41` | `cowrie.client.kex` |
| `2026-08-04 22:35:42` | `cowrie.login.success` |
| `2026-08-04 22:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77496d0b4c2a

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-08-04 22:37 |
| **Last Seen** | 2026-08-04 22:40 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:37:58` | `cowrie.session.connect` |
| `2026-08-04 22:37:58` | `cowrie.client.version` |
| `2026-08-04 22:37:58` | `cowrie.client.kex` |
| `2026-08-04 22:37:58` | `cowrie.login.success` |
| `2026-08-04 22:37:59` | `cowrie.session.file_upload` |
| `2026-08-04 22:38:00` | `cowrie.session.params` |
| `2026-08-04 22:38:00` | `cowrie.command.input` |
| `2026-08-04 22:38:00` | `cowrie.command.input` |
| `2026-08-04 22:38:00` | `cowrie.command.input` |
| `2026-08-04 22:38:00` | `cowrie.command.failed` |
| `2026-08-04 22:38:00` | `cowrie.log.closed` |
| `2026-08-04 22:38:01` | `cowrie.session.params` |
| `2026-08-04 22:38:01` | `cowrie.command.input` |
| `2026-08-04 22:38:01` | `cowrie.log.closed` |
| `2026-08-04 22:38:02` | `cowrie.session.params` |
| `2026-08-04 22:38:02` | `cowrie.command.input` |
| `2026-08-04 22:38:02` | `cowrie.log.closed` |
| `2026-08-04 22:38:03` | `cowrie.session.params` |
| `2026-08-04 22:38:03` | `cowrie.command.input` |
| `2026-08-04 22:38:03` | `cowrie.command.failed` |
| `2026-08-04 22:38:03` | `cowrie.command.failed` |
| `2026-08-04 22:39:03` | `cowrie.session.params` |
| `2026-08-04 22:39:03` | `cowrie.command.input` |
| `2026-08-04 22:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46208a2bea8e

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-04 22:38 |
| **Last Seen** | 2026-08-04 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:38:28` | `cowrie.session.connect` |
| `2026-08-04 22:38:28` | `cowrie.client.version` |
| `2026-08-04 22:38:28` | `cowrie.client.kex` |
| `2026-08-04 22:38:29` | `cowrie.login.success` |
| `2026-08-04 22:38:29` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:38:29` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c4364f715c

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]50` |
| **First Seen** | 2026-08-04 22:43 |
| **Last Seen** | 2026-08-04 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:43:03` | `cowrie.session.connect` |
| `2026-08-04 22:43:03` | `cowrie.client.version` |
| `2026-08-04 22:43:03` | `cowrie.client.kex` |
| `2026-08-04 22:43:03` | `cowrie.login.success` |
| `2026-08-04 22:43:04` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:43:04` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]50` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4edf57660301

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]229` |
| **First Seen** | 2026-08-04 22:46 |
| **Last Seen** | 2026-08-04 22:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:46:36` | `cowrie.session.connect` |
| `2026-08-04 22:46:37` | `cowrie.client.version` |
| `2026-08-04 22:46:37` | `cowrie.client.kex` |
| `2026-08-04 22:46:39` | `cowrie.login.success` |
| `2026-08-04 22:46:39` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]229` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ebf0c15e1a

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-04 22:46 |
| **Last Seen** | 2026-08-04 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:46:46` | `cowrie.session.connect` |
| `2026-08-04 22:46:46` | `cowrie.client.version` |
| `2026-08-04 22:46:46` | `cowrie.client.kex` |
| `2026-08-04 22:46:46` | `cowrie.login.success` |
| `2026-08-04 22:46:47` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:46:47` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b05dbd54b24b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-08-04 22:46 |
| **Last Seen** | 2026-08-04 22:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:46:49` | `cowrie.session.connect` |
| `2026-08-04 22:46:49` | `cowrie.client.version` |
| `2026-08-04 22:46:49` | `cowrie.client.kex` |
| `2026-08-04 22:46:50` | `cowrie.login.success` |
| `2026-08-04 22:46:51` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6be5c9e0f9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-04 22:47 |
| **Last Seen** | 2026-08-04 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:47:29` | `cowrie.session.connect` |
| `2026-08-04 22:47:29` | `cowrie.client.version` |
| `2026-08-04 22:47:29` | `cowrie.client.kex` |
| `2026-08-04 22:47:29` | `cowrie.login.success` |
| `2026-08-04 22:47:30` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:47:30` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27dd50ee0f57

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-04 22:49 |
| **Last Seen** | 2026-08-04 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:49:54` | `cowrie.session.connect` |
| `2026-08-04 22:49:54` | `cowrie.client.version` |
| `2026-08-04 22:49:54` | `cowrie.client.kex` |
| `2026-08-04 22:49:54` | `cowrie.login.success` |
| `2026-08-04 22:49:54` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:49:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-04 22:49:55` | `cowrie.direct-tcpip.data` |
| `2026-08-04 22:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c1e1200bc0f

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-08-04 22:52 |
| **Last Seen** | 2026-08-04 22:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:52:34` | `cowrie.session.connect` |
| `2026-08-04 22:52:34` | `cowrie.client.version` |
| `2026-08-04 22:52:34` | `cowrie.client.kex` |
| `2026-08-04 22:52:35` | `cowrie.login.success` |
| `2026-08-04 22:52:36` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6896f0718b2d

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-08-04 22:52 |
| **Last Seen** | 2026-08-04 22:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-04 22:52:46` | `cowrie.session.connect` |
| `2026-08-04 22:52:46` | `cowrie.client.version` |
| `2026-08-04 22:52:46` | `cowrie.client.kex` |
| `2026-08-04 22:52:48` | `cowrie.login.success` |
| `2026-08-04 22:52:49` | `cowrie.direct-tcpip.request` |
| `2026-08-04 22:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-08-04 21:11 | 2026-08-04 22:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]139` | **4** | 2026-08-04 21:52 | 2026-08-04 22:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **4** | 2026-08-04 20:56 | 2026-08-04 22:08 | 3m | 0 | `T1592` | 🟢 LOW |
| `130.12.182[.]231` | **3** | 2026-08-04 21:49 | 2026-08-04 21:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]227` | **3** | 2026-08-04 21:35 | 2026-08-04 21:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-04 21:33 | 2026-08-04 21:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]181` | **3** | 2026-08-04 21:51 | 2026-08-04 21:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]199` | **3** | 2026-08-04 21:52 | 2026-08-04 21:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-04 22:42 | 2026-08-04 22:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-04 21:49 | 2026-08-04 21:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-08-04 21:24 | 2026-08-04 21:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | **2** | 2026-08-04 21:18 | 2026-08-04 21:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.68.22[.]115` | 1 | 2026-08-04 21:04 | 2026-08-04 21:04 | 7s | 0 | `T1592` | 🟢 LOW |
| `154.16.44[.]75` | 1 | 2026-08-04 21:52 | 2026-08-04 21:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `162.255.112[.]183` | 1 | 2026-08-04 22:04 | 2026-08-04 22:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-08-04 22:12 | 2026-08-04 22:12 | 32s | 0 | `T1592` | 🟢 LOW |
| `185.112.148[.]66` | 1 | 2026-08-04 22:24 | 2026-08-04 22:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.162.237[.]61` | 1 | 2026-08-04 21:56 | 2026-08-04 21:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]243` | 1 | 2026-08-04 21:53 | 2026-08-04 21:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-08-04 21:00 | 2026-08-04 21:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.55.69[.]224` | 1 | 2026-08-04 21:14 | 2026-08-04 21:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.29.231[.]106` | 1 | 2026-08-04 22:52 | 2026-08-04 22:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-04 22:06 | 2026-08-04 22:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-08-04 21:05 | 2026-08-04 21:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-04 21:33 | 2026-08-04 21:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.9.231[.]123` | 1 | 2026-08-04 21:46 | 2026-08-04 21:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `46.150.82[.]109` | 1 | 2026-08-04 22:03 | 2026-08-04 22:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `83.226.181[.]38` | 1 | 2026-08-04 20:57 | 2026-08-04 20:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]10` | 1 | 2026-08-04 21:40 | 2026-08-04 21:40 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `130.12.182[.]223` | DE | Netiface LLC | **100** ⚠️ | 13 |
| `103.29.185[.]162` | ID | PT Pascal Indonesia | **100** ⚠️ | 50 |
| `62.201.212[.]54` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `195.222.57[.]190` | BA | Public Enterprise BH Telecom DD | **100** ⚠️ | 50 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `195.158.26[.]59` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `65.20.179[.]251` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `103.68.22[.]115` | IN | Anonet Network Private Limited | **100** ⚠️ | 16 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 77 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 154 cases |
| Tool 34  | Credential Extractor        | ✅ 85 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 98 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (14.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 77 priority case(s) shown individually · 29 recon entry/entries in table (12 group(s) consolidating 38 session(s)).

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
_Report time: 2026-08-04T23:06:37Z_

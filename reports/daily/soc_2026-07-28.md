# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-28 |
| **Generated At** | 2026-07-28T21:11:46Z |
| **Shift Time** | 21:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **100** |
| False Positives Filtered | **15** (13.0%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **26** |
| High Severity Cases | **39** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **76** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **60** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **14** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **47** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 17 |
| `ubnt` | 12 |
| `support` | 7 |
| `nobody` | 5 |
| `guest` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `555` | 5 |
| `5` | 4 |
| `4444` | 4 |
| `smo@@kkklss` | 4 |
| `333` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `555` | 5 |
| `ubnt` | `5` | 4 |
| `ubnt` | `4444` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `ubnt` | `333` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubnt` | `5` | `124.167.20.113` | 2026-07-28T18:59:51 |
| `ubnt` | `5` | `182.75.197.174` | 2026-07-28T19:00:04 |
| `ubnt` | `5` | `195.158.26.59` | 2026-07-28T19:03:15 |
| `ubnt` | `5` | `61.37.150.6` | 2026-07-28T19:03:27 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-07-28T19:09:36 |
| `test` | `11` | `10.0.0.73` | 2026-07-28T19:16:22 |
| `ubnt` | `4444` | `61.184.128.210` | 2026-07-28T19:17:22 |
| `ubnt` | `4444` | `103.120.116.162` | 2026-07-28T19:17:34 |
| `ubnt` | `4444` | `10.0.0.73` | 2026-07-28T19:17:45 |
| `oracle` | `abcd1234` | `178.178.194.135` | 2026-07-28T19:24:16 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-28T19:27:20 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-28T19:27:21 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-28T19:27:28 |
| `oracle` | `abcd1234` | `65.20.205.197` | 2026-07-28T19:27:44 |
| `oracle` | `abcd1234` | `10.0.0.73` | 2026-07-28T19:28:02 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.210.100` | 2026-07-28T19:34:40 |
| `support` | `support` | `10.0.0.73` | 2026-07-28T19:36:11 |
| `ubnt` | `333` | `61.185.30.170` | 2026-07-28T19:38:19 |
| `config` | `config55` | `211.238.237.254` | 2026-07-28T19:40:14 |
| `config` | `config55` | `177.72.87.7` | 2026-07-28T19:40:22 |
| `ubnt` | `333` | `175.206.1.60` | 2026-07-28T19:41:41 |
| `ubnt` | `333` | `103.174.145.35` | 2026-07-28T19:41:49 |
| `ubnt` | `333` | `10.0.0.73` | 2026-07-28T19:42:21 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-28T19:43:48 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-28T19:43:48 |
| `Centos` | `ubuntu` | `10.0.0.73` | 2026-07-28T19:52:13 |
| `support` | `777777` | `65.20.131.63` | 2026-07-28T20:01:00 |
| `support` | `777777` | `183.233.85.194` | 2026-07-28T20:01:08 |
| `centos` | `8` | `217.24.185.98` | 2026-07-28T20:02:30 |
| `support` | `777777` | `60.18.139.82` | 2026-07-28T20:04:15 |
| `root` | `---fuck_you----` | `111.228.24.134` | 2026-07-28T20:04:21 |
| `support` | `777777` | `218.4.156.254` | 2026-07-28T20:04:25 |
| `root` | `DNLMBPB6JV` | `10.0.0.73` | 2026-07-28T20:07:05 |
| `guest` | `7777` | `27.107.102.154` | 2026-07-28T20:12:50 |
| `guest` | `7777` | `41.178.230.115` | 2026-07-28T20:12:56 |
| `guest` | `7777` | `10.0.0.73` | 2026-07-28T20:16:36 |
| `support` | `support` | `176.53.159.196` | 2026-07-28T20:17:10 |
| `admin` | `444444` | `10.0.0.73` | 2026-07-28T20:28:46 |
| `pi` | `qwer1234` | `10.0.0.73` | 2026-07-28T20:30:24 |
| `root` | `666` | `210.177.143.61` | 2026-07-28T20:37:08 |
| `root` | `666` | `65.20.211.96` | 2026-07-28T20:37:16 |
| `root` | `666` | `10.0.0.73` | 2026-07-28T20:40:47 |
| `GET /..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd HTTP/1.1` | `Host: 129.80.119.236:2323` | `192.161.49.2` | 2026-07-28T20:40:55 |
| `nobody` | `555` | `121.128.84.224` | 2026-07-28T20:51:05 |
| `nobody` | `555` | `211.238.237.254` | 2026-07-28T20:54:36 |
| `nobody` | `555` | `218.29.196.162` | 2026-07-28T20:54:44 |
| `nobody` | `555` | `10.0.0.73` | 2026-07-28T20:54:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **115** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 25 |
| Paramiko (Python) | 10 |
| libssh | 6 |
| Go SSH scanner | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 25 | 24 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `5bd26477da54...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 25 | 24 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `5bd26477da54...` | PuTTY | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **47** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (37)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8cba27b872d3

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]113` |
| **First Seen** | 2026-07-28 18:59 |
| **Last Seen** | 2026-07-28 18:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 18:59:49` | `cowrie.session.connect` |
| `2026-07-28 18:59:49` | `cowrie.client.version` |
| `2026-07-28 18:59:49` | `cowrie.client.kex` |
| `2026-07-28 18:59:51` | `cowrie.login.success` |
| `2026-07-28 18:59:52` | `cowrie.direct-tcpip.request` |
| `2026-07-28 18:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]113` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38410cf1408b

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-28 19:00 |
| **Last Seen** | 2026-07-28 19:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:00:02` | `cowrie.session.connect` |
| `2026-07-28 19:00:02` | `cowrie.client.version` |
| `2026-07-28 19:00:02` | `cowrie.client.kex` |
| `2026-07-28 19:00:04` | `cowrie.login.success` |
| `2026-07-28 19:00:05` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d5f8f10150

| Field | Detail |
|---|---|
| **Source IP** | `195.158.26[.]59` |
| **First Seen** | 2026-07-28 19:03 |
| **Last Seen** | 2026-07-28 19:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:03:12` | `cowrie.session.connect` |
| `2026-07-28 19:03:13` | `cowrie.client.version` |
| `2026-07-28 19:03:13` | `cowrie.client.kex` |
| `2026-07-28 19:03:15` | `cowrie.login.success` |
| `2026-07-28 19:03:17` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.158.26[.]59` to AbuseIPDB if not already reported
- [ ] Block `195.158.26[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c01ea477f1b6

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-28 19:03 |
| **Last Seen** | 2026-07-28 19:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:03:24` | `cowrie.session.connect` |
| `2026-07-28 19:03:24` | `cowrie.client.version` |
| `2026-07-28 19:03:24` | `cowrie.client.kex` |
| `2026-07-28 19:03:27` | `cowrie.login.success` |
| `2026-07-28 19:03:27` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:03:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1db049e5338

| Field | Detail |
|---|---|
| **Source IP** | `61.184.128[.]210` |
| **First Seen** | 2026-07-28 19:17 |
| **Last Seen** | 2026-07-28 19:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:17:19` | `cowrie.session.connect` |
| `2026-07-28 19:17:19` | `cowrie.client.version` |
| `2026-07-28 19:17:19` | `cowrie.client.kex` |
| `2026-07-28 19:17:22` | `cowrie.login.success` |
| `2026-07-28 19:17:22` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.184.128[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.184.128[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9db09b6bdd07

| Field | Detail |
|---|---|
| **Source IP** | `103.120.116[.]162` |
| **First Seen** | 2026-07-28 19:17 |
| **Last Seen** | 2026-07-28 19:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:17:32` | `cowrie.session.connect` |
| `2026-07-28 19:17:33` | `cowrie.client.version` |
| `2026-07-28 19:17:33` | `cowrie.client.kex` |
| `2026-07-28 19:17:34` | `cowrie.login.success` |
| `2026-07-28 19:17:35` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.120.116[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.120.116[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d59d366ed7db

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-07-28 19:24 |
| **Last Seen** | 2026-07-28 19:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:24:14` | `cowrie.session.connect` |
| `2026-07-28 19:24:14` | `cowrie.client.version` |
| `2026-07-28 19:24:14` | `cowrie.client.kex` |
| `2026-07-28 19:24:16` | `cowrie.login.success` |
| `2026-07-28 19:24:17` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54e7f613a70

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 19:27 |
| **Last Seen** | 2026-07-28 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:27:19` | `cowrie.session.connect` |
| `2026-07-28 19:27:19` | `cowrie.client.version` |
| `2026-07-28 19:27:19` | `cowrie.client.kex` |
| `2026-07-28 19:27:20` | `cowrie.login.success` |
| `2026-07-28 19:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec10576d544c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 19:27 |
| **Last Seen** | 2026-07-28 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:27:20` | `cowrie.session.connect` |
| `2026-07-28 19:27:20` | `cowrie.client.version` |
| `2026-07-28 19:27:21` | `cowrie.client.kex` |
| `2026-07-28 19:27:21` | `cowrie.login.success` |
| `2026-07-28 19:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75dc366084ca

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 19:27 |
| **Last Seen** | 2026-07-28 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:27:27` | `cowrie.session.connect` |
| `2026-07-28 19:27:27` | `cowrie.client.version` |
| `2026-07-28 19:27:27` | `cowrie.client.kex` |
| `2026-07-28 19:27:28` | `cowrie.login.success` |
| `2026-07-28 19:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f87fcacffab

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 19:27 |
| **Last Seen** | 2026-07-28 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:27:28` | `cowrie.session.connect` |
| `2026-07-28 19:27:28` | `cowrie.client.version` |
| `2026-07-28 19:27:28` | `cowrie.client.kex` |
| `2026-07-28 19:27:28` | `cowrie.login.success` |
| `2026-07-28 19:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d9b0167682

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-07-28 19:27 |
| **Last Seen** | 2026-07-28 19:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:27:42` | `cowrie.session.connect` |
| `2026-07-28 19:27:42` | `cowrie.client.version` |
| `2026-07-28 19:27:42` | `cowrie.client.kex` |
| `2026-07-28 19:27:44` | `cowrie.login.success` |
| `2026-07-28 19:27:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b541df8ed6

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-07-28 19:38 |
| **Last Seen** | 2026-07-28 19:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:38:16` | `cowrie.session.connect` |
| `2026-07-28 19:38:17` | `cowrie.client.version` |
| `2026-07-28 19:38:17` | `cowrie.client.kex` |
| `2026-07-28 19:38:19` | `cowrie.login.success` |
| `2026-07-28 19:38:19` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b632c0502d

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-28 19:40 |
| **Last Seen** | 2026-07-28 19:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:40:11` | `cowrie.session.connect` |
| `2026-07-28 19:40:11` | `cowrie.client.version` |
| `2026-07-28 19:40:11` | `cowrie.client.kex` |
| `2026-07-28 19:40:14` | `cowrie.login.success` |
| `2026-07-28 19:40:15` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fb0e34bb3d

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-07-28 19:40 |
| **Last Seen** | 2026-07-28 19:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:40:20` | `cowrie.session.connect` |
| `2026-07-28 19:40:21` | `cowrie.client.version` |
| `2026-07-28 19:40:21` | `cowrie.client.kex` |
| `2026-07-28 19:40:22` | `cowrie.login.success` |
| `2026-07-28 19:40:23` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e9384fb9bd

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-07-28 19:41 |
| **Last Seen** | 2026-07-28 19:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:41:39` | `cowrie.session.connect` |
| `2026-07-28 19:41:39` | `cowrie.client.version` |
| `2026-07-28 19:41:39` | `cowrie.client.kex` |
| `2026-07-28 19:41:41` | `cowrie.login.success` |
| `2026-07-28 19:41:42` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3be2e3678fc0

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-07-28 19:41 |
| **Last Seen** | 2026-07-28 19:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:41:47` | `cowrie.session.connect` |
| `2026-07-28 19:41:47` | `cowrie.client.version` |
| `2026-07-28 19:41:47` | `cowrie.client.kex` |
| `2026-07-28 19:41:49` | `cowrie.login.success` |
| `2026-07-28 19:41:49` | `cowrie.direct-tcpip.request` |
| `2026-07-28 19:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ea79745ea6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 19:43 |
| **Last Seen** | 2026-07-28 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:43:47` | `cowrie.session.connect` |
| `2026-07-28 19:43:47` | `cowrie.client.version` |
| `2026-07-28 19:43:47` | `cowrie.client.kex` |
| `2026-07-28 19:43:48` | `cowrie.login.success` |
| `2026-07-28 19:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d18d292ea7d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-28 19:43 |
| **Last Seen** | 2026-07-28 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 19:43:47` | `cowrie.session.connect` |
| `2026-07-28 19:43:47` | `cowrie.client.version` |
| `2026-07-28 19:43:48` | `cowrie.client.kex` |
| `2026-07-28 19:43:48` | `cowrie.login.success` |
| `2026-07-28 19:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb26a60b6f1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.131[.]63` |
| **First Seen** | 2026-07-28 20:00 |
| **Last Seen** | 2026-07-28 20:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:00:58` | `cowrie.session.connect` |
| `2026-07-28 20:00:59` | `cowrie.client.version` |
| `2026-07-28 20:00:59` | `cowrie.client.kex` |
| `2026-07-28 20:01:00` | `cowrie.login.success` |
| `2026-07-28 20:01:00` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.131[.]63` to AbuseIPDB if not already reported
- [ ] Block `65.20.131[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b4a84e2753

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-07-28 20:01 |
| **Last Seen** | 2026-07-28 20:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:01:05` | `cowrie.session.connect` |
| `2026-07-28 20:01:06` | `cowrie.client.version` |
| `2026-07-28 20:01:06` | `cowrie.client.kex` |
| `2026-07-28 20:01:08` | `cowrie.login.success` |
| `2026-07-28 20:01:09` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2781328300b

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-07-28 20:02 |
| **Last Seen** | 2026-07-28 20:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:02:28` | `cowrie.session.connect` |
| `2026-07-28 20:02:29` | `cowrie.client.version` |
| `2026-07-28 20:02:29` | `cowrie.client.kex` |
| `2026-07-28 20:02:30` | `cowrie.login.success` |
| `2026-07-28 20:02:30` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfa2ead3e3d

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-07-28 20:04 |
| **Last Seen** | 2026-07-28 20:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:04:12` | `cowrie.session.connect` |
| `2026-07-28 20:04:13` | `cowrie.client.version` |
| `2026-07-28 20:04:13` | `cowrie.client.kex` |
| `2026-07-28 20:04:15` | `cowrie.login.success` |
| `2026-07-28 20:04:16` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb40f870ab80

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-28 20:04 |
| **Last Seen** | 2026-07-28 20:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:04:22` | `cowrie.session.connect` |
| `2026-07-28 20:04:23` | `cowrie.client.version` |
| `2026-07-28 20:04:23` | `cowrie.client.kex` |
| `2026-07-28 20:04:25` | `cowrie.login.success` |
| `2026-07-28 20:04:25` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb7e36e00c2

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-28 20:12 |
| **Last Seen** | 2026-07-28 20:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:12:47` | `cowrie.session.connect` |
| `2026-07-28 20:12:48` | `cowrie.client.version` |
| `2026-07-28 20:12:48` | `cowrie.client.kex` |
| `2026-07-28 20:12:50` | `cowrie.login.success` |
| `2026-07-28 20:12:50` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c507769783

| Field | Detail |
|---|---|
| **Source IP** | `41.178.230[.]115` |
| **First Seen** | 2026-07-28 20:12 |
| **Last Seen** | 2026-07-28 20:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:12:55` | `cowrie.session.connect` |
| `2026-07-28 20:12:56` | `cowrie.client.version` |
| `2026-07-28 20:12:56` | `cowrie.client.kex` |
| `2026-07-28 20:12:56` | `cowrie.login.success` |
| `2026-07-28 20:12:57` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.178.230[.]115` to AbuseIPDB if not already reported
- [ ] Block `41.178.230[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dbeac2b5fe2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-28 20:17 |
| **Last Seen** | 2026-07-28 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:17:09` | `cowrie.session.connect` |
| `2026-07-28 20:17:09` | `cowrie.client.version` |
| `2026-07-28 20:17:09` | `cowrie.client.kex` |
| `2026-07-28 20:17:10` | `cowrie.login.success` |
| `2026-07-28 20:17:10` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:17:10` | `cowrie.direct-tcpip.data` |
| `2026-07-28 20:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dacbaf825e72

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-28 20:37 |
| **Last Seen** | 2026-07-28 20:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:37:05` | `cowrie.session.connect` |
| `2026-07-28 20:37:06` | `cowrie.client.version` |
| `2026-07-28 20:37:06` | `cowrie.client.kex` |
| `2026-07-28 20:37:08` | `cowrie.login.success` |
| `2026-07-28 20:37:08` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12727751861

| Field | Detail |
|---|---|
| **Source IP** | `65.20.211[.]96` |
| **First Seen** | 2026-07-28 20:37 |
| **Last Seen** | 2026-07-28 20:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:37:14` | `cowrie.session.connect` |
| `2026-07-28 20:37:14` | `cowrie.client.version` |
| `2026-07-28 20:37:14` | `cowrie.client.kex` |
| `2026-07-28 20:37:16` | `cowrie.login.success` |
| `2026-07-28 20:37:18` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.211[.]96` to AbuseIPDB if not already reported
- [ ] Block `65.20.211[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5ace5db326

| Field | Detail |
|---|---|
| **Source IP** | `192.161.49[.]2` |
| **First Seen** | 2026-07-28 20:40 |
| **Last Seen** | 2026-07-28 20:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0, Accept: */*, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:40:55` | `cowrie.session.connect` |
| `2026-07-28 20:40:55` | `cowrie.login.success` |
| `2026-07-28 20:40:55` | `cowrie.session.params` |
| `2026-07-28 20:40:55` | `cowrie.command.input` |
| `2026-07-28 20:40:55` | `cowrie.command.input` |
| `2026-07-28 20:40:55` | `cowrie.command.failed` |
| `2026-07-28 20:40:55` | `cowrie.command.input` |
| `2026-07-28 20:40:55` | `cowrie.command.failed` |
| `2026-07-28 20:40:55` | `cowrie.command.input` |
| `2026-07-28 20:40:55` | `cowrie.log.closed` |
| `2026-07-28 20:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.161.49[.]2` to AbuseIPDB if not already reported
- [ ] Block `192.161.49[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c956c6780a0

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-07-28 20:51 |
| **Last Seen** | 2026-07-28 20:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:51:02` | `cowrie.session.connect` |
| `2026-07-28 20:51:03` | `cowrie.client.version` |
| `2026-07-28 20:51:03` | `cowrie.client.kex` |
| `2026-07-28 20:51:05` | `cowrie.login.success` |
| `2026-07-28 20:51:05` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec807d444540

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 20:54 |
| **Last Seen** | 2026-07-28 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:54:04` | `cowrie.session.connect` |
| `2026-07-28 20:54:04` | `cowrie.client.version` |
| `2026-07-28 20:54:04` | `cowrie.client.kex` |
| `2026-07-28 20:54:05` | `cowrie.login.success` |
| `2026-07-28 20:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a4a46e3de6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 20:54 |
| **Last Seen** | 2026-07-28 20:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:54:04` | `cowrie.session.connect` |
| `2026-07-28 20:54:04` | `cowrie.client.version` |
| `2026-07-28 20:54:04` | `cowrie.client.kex` |
| `2026-07-28 20:54:05` | `cowrie.login.success` |
| `2026-07-28 20:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf7847b91160

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 20:54 |
| **Last Seen** | 2026-07-28 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:54:09` | `cowrie.session.connect` |
| `2026-07-28 20:54:09` | `cowrie.client.version` |
| `2026-07-28 20:54:10` | `cowrie.client.kex` |
| `2026-07-28 20:54:10` | `cowrie.login.success` |
| `2026-07-28 20:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6ade2954e9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-28 20:54 |
| **Last Seen** | 2026-07-28 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:54:11` | `cowrie.session.connect` |
| `2026-07-28 20:54:11` | `cowrie.client.version` |
| `2026-07-28 20:54:11` | `cowrie.client.kex` |
| `2026-07-28 20:54:11` | `cowrie.login.success` |
| `2026-07-28 20:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733c5f4aa16e

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-28 20:54 |
| **Last Seen** | 2026-07-28 20:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:54:32` | `cowrie.session.connect` |
| `2026-07-28 20:54:33` | `cowrie.client.version` |
| `2026-07-28 20:54:33` | `cowrie.client.kex` |
| `2026-07-28 20:54:36` | `cowrie.login.success` |
| `2026-07-28 20:54:36` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b4d5eb375cd

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-07-28 20:54 |
| **Last Seen** | 2026-07-28 20:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-28 20:54:41` | `cowrie.session.connect` |
| `2026-07-28 20:54:42` | `cowrie.client.version` |
| `2026-07-28 20:54:42` | `cowrie.client.kex` |
| `2026-07-28 20:54:44` | `cowrie.login.success` |
| `2026-07-28 20:54:44` | `cowrie.direct-tcpip.request` |
| `2026-07-28 20:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **25** | 2026-07-28 18:55 | 2026-07-28 20:54 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-28 19:07 | 2026-07-28 20:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **4** | 2026-07-28 20:01 | 2026-07-28 20:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-28 19:35 | 2026-07-28 19:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-28 19:12 | 2026-07-28 19:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]208` | **3** | 2026-07-28 20:01 | 2026-07-28 20:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-28 20:29 | 2026-07-28 20:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-07-28 19:42 | 2026-07-28 20:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.15[.]174` | **2** | 2026-07-28 20:04 | 2026-07-28 20:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `150.95.66[.]172` | 1 | 2026-07-28 20:37 | 2026-07-28 20:38 | 38s | 0 | `T1592` | 🟢 LOW |
| `183.89.248[.]224` | 1 | 2026-07-28 20:05 | 2026-07-28 20:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]245` | 1 | 2026-07-28 19:58 | 2026-07-28 19:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]72` | 1 | 2026-07-28 20:31 | 2026-07-28 20:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `190.103.198[.]143` | 1 | 2026-07-28 19:59 | 2026-07-28 19:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-07-28 19:04 | 2026-07-28 19:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-07-28 20:53 | 2026-07-28 20:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-28 20:39 | 2026-07-28 20:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | 1 | 2026-07-28 19:02 | 2026-07-28 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-07-28 19:50 | 2026-07-28 19:50 | 2s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-07-28 20:39 | 2026-07-28 20:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.87.248[.]223` | 1 | 2026-07-28 19:13 | 2026-07-28 19:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `99.238.166[.]78` | 1 | 2026-07-28 19:54 | 2026-07-28 19:54 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `190.103.198[.]143` | AR | Cooperativa de Huanguelén Ltda. | **100** ⚠️ | 1 |
| `45.198.224[.]26` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 5 |
| `72.14.178[.]148` | US | Linode | **100** ⚠️ | 50 |
| `185.247.137[.]245` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `95.87.248[.]223` | BG | Vivacom Bulgaria EAD | **100** ⚠️ | 50 |
| `195.158.26[.]59` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `132.148.30[.]167` | US | GoDaddy.com, LLC | **100** ⚠️ | 24 |
| `124.167.20[.]113` | CN | China Unicom Shan1xi province network | **100** ⚠️ | 50 |
| `121.128.84[.]224` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 45 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 39 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 115 cases |
| Tool 34  | Credential Extractor        | ✅ 60 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (13.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 37 priority case(s) shown individually · 22 recon entry/entries in table (9 group(s) consolidating 50 session(s)).

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
_Report time: 2026-07-28T21:11:46Z_

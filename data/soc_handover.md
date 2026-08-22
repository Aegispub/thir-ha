# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-22 |
| **Generated At** | 2026-08-22T22:25:49Z |
| **Shift Time** | 22:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **99** |
| Confirmed Threats | **87** |
| False Positives Filtered | **12** (12.1%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **29** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **33** |
| Malware Samples Analyzed | **2** HIGH · **18** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **89** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **12** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **76** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `ubuntu` | 12 |
| `unknown` | 11 |
| `config` | 10 |
| `guest` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root2006` | 6 |
| `guest2005` | 6 |
| `nobody2014` | 6 |
| `unknown2012` | 6 |
| `root2024` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root2006` | 6 |
| `guest` | `guest2005` | 6 |
| `nobody` | `nobody2014` | 6 |
| `unknown` | `unknown2012` | 6 |
| `root` | `root2024` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-08-22T18:56:19 |
| `root` | `root2024` | `10.0.0.73` | 2026-08-22T18:57:21 |
| `root` | `root2024` | `45.170.50.2` | 2026-08-22T18:58:56 |
| `root` | `root2024` | `199.7.163.33` | 2026-08-22T18:59:03 |
| `config` | `config2003` | `93.118.128.115` | 2026-08-22T18:59:09 |
| `ubuntu` | `Abcd123!` | `217.60.255.130` | 2026-08-22T18:59:10 |
| `config` | `config2003` | `120.234.232.184` | 2026-08-22T18:59:17 |
| `config` | `config2003` | `186.97.203.162` | 2026-08-22T18:59:26 |
| `config` | `config2003` | `110.25.109.48` | 2026-08-22T18:59:35 |
| `root` | `Boy@123` | `217.60.255.130` | 2026-08-22T18:59:43 |
| `config` | `config1234567` | `10.0.0.73` | 2026-08-22T19:00:08 |
| `ubuntu` | `Hitech@123` | `217.60.255.130` | 2026-08-22T19:09:09 |
| `root` | `vV123456` | `217.60.255.130` | 2026-08-22T19:09:48 |
| `operator` | `operator2013` | `10.0.0.73` | 2026-08-22T19:13:55 |
| `ubuntu` | `Password123456` | `217.60.255.130` | 2026-08-22T19:18:54 |
| `root` | `Cc@1234` | `217.60.255.130` | 2026-08-22T19:19:36 |
| `support` | `support` | `10.0.0.73` | 2026-08-22T19:19:48 |
| `test` | `test2006` | `108.234.110.202` | 2026-08-22T19:21:31 |
| `test` | `test2006` | `77.38.132.161` | 2026-08-22T19:21:40 |
| `ubuntu` | `Admin123!@#` | `217.60.255.130` | 2026-08-22T19:28:37 |
| `root` | `Aa@123` | `217.60.255.130` | 2026-08-22T19:29:24 |
| `unknown` | `unknown2004` | `10.0.0.73` | 2026-08-22T19:30:23 |
| `operator` | `operator2013` | `181.87.154.121` | 2026-08-22T19:31:17 |
| `operator` | `operator2013` | `78.72.168.178` | 2026-08-22T19:31:24 |
| `operator` | `operator2013` | `115.246.242.2` | 2026-08-22T19:31:31 |
| `unknown` | `unknown2004` | `66.175.138.122` | 2026-08-22T19:31:54 |
| `unknown` | `unknown2004` | `222.76.248.54` | 2026-08-22T19:32:03 |
| `test` | `test2006` | `10.0.0.73` | 2026-08-22T19:32:25 |
| `ubuntu` | `!Qaz@Wsx#Edc` | `217.60.255.130` | 2026-08-22T19:38:30 |
| `root` | `Aa@1234` | `217.60.255.130` | 2026-08-22T19:39:18 |
| `unknown` | `unknown2004` | `218.94.115.164` | 2026-08-22T19:47:19 |
| `ubuntu` | `Abc12345@` | `217.60.255.130` | 2026-08-22T19:48:28 |
| `test` | `test2006` | `58.57.154.146` | 2026-08-22T19:48:39 |
| `test` | `test2006` | `107.135.117.245` | 2026-08-22T19:48:47 |
| `root` | `Ahmad@123` | `217.60.255.130` | 2026-08-22T19:49:17 |
| `root` | `root2006` | `91.92.133.195` | 2026-08-22T19:53:52 |
| `root` | `root2006` | `104.248.83.99` | 2026-08-22T19:53:59 |
| `admin` | `admin` | `118.145.104.105` | 2026-08-22T19:58:07 |
| `ubuntu` | `Server12345@` | `217.60.255.130` | 2026-08-22T19:58:22 |
| `root` | `Ahmad@1234` | `217.60.255.130` | 2026-08-22T19:59:11 |
| `guest` | `guest2005` | `10.0.0.73` | 2026-08-22T20:03:02 |
| `default` | `123` | `65.20.165.78` | 2026-08-22T20:03:30 |
| `default` | `123` | `63.47.149.59` | 2026-08-22T20:03:39 |
| `default` | `123` | `121.135.47.141` | 2026-08-22T20:03:40 |
| `default` | `123` | `121.99.190.167` | 2026-08-22T20:03:50 |
| `guest` | `guest2005` | `65.20.189.52` | 2026-08-22T20:04:36 |
| `guest` | `guest2005` | `61.185.30.170` | 2026-08-22T20:04:45 |
| `root` | `root2006` | `10.0.0.73` | 2026-08-22T20:04:48 |
| `ubuntu` | `Password1234@` | `217.60.255.130` | 2026-08-22T20:08:33 |
| `root` | `Admin@2023` | `217.60.255.130` | 2026-08-22T20:09:22 |
| `nobody` | `nobody2014` | `10.0.0.73` | 2026-08-22T20:18:03 |
| `ubuntu` | `qq123123` | `217.60.255.130` | 2026-08-22T20:18:42 |
| `root` | `Hh2024` | `217.60.255.130` | 2026-08-22T20:19:28 |
| `guest` | `guest2005` | `122.187.229.220` | 2026-08-22T20:20:21 |
| `guest` | `guest2005` | `46.201.247.21` | 2026-08-22T20:20:28 |
| `root` | `root2006` | `122.170.100.253` | 2026-08-22T20:21:08 |
| `root` | `root2006` | `116.114.84.246` | 2026-08-22T20:21:17 |
| `ubuntu` | `P@ssw0rd2025` | `217.60.255.130` | 2026-08-22T20:28:51 |
| `root` | `Qq2025` | `217.60.255.130` | 2026-08-22T20:29:34 |
| `nobody` | `nobody2014` | `83.150.16.254` | 2026-08-22T20:35:26 |
| `nobody` | `nobody2014` | `178.178.194.131` | 2026-08-22T20:35:34 |
| `nobody` | `nobody2014` | `179.181.133.153` | 2026-08-22T20:35:34 |
| `nobody` | `nobody2014` | `103.93.37.178` | 2026-08-22T20:35:42 |
| `unknown` | `unknown2012` | `10.0.0.73` | 2026-08-22T20:36:00 |
| `config` | `config2010` | `10.0.0.73` | 2026-08-22T20:37:16 |
| `unknown` | `unknown2012` | `70.89.116.5` | 2026-08-22T20:37:27 |
| `unknown` | `unknown2012` | `101.13.5.26` | 2026-08-22T20:37:41 |
| `ubuntu` | `VPS@123456` | `217.60.255.130` | 2026-08-22T20:38:55 |
| `root` | `Dd@2024` | `217.60.255.130` | 2026-08-22T20:39:43 |
| `ubuntu` | `@Dmin123` | `217.60.255.130` | 2026-08-22T20:48:51 |
| `root` | `Welcome@123` | `217.60.255.130` | 2026-08-22T20:49:34 |
| `ubnt` | `ubnt2023` | `10.0.0.73` | 2026-08-22T20:50:08 |
| `unknown` | `unknown2012` | `183.167.234.154` | 2026-08-22T20:53:03 |
| `unknown` | `unknown2012` | `187.115.144.103` | 2026-08-22T20:53:11 |
| `config` | `config2010` | `182.60.128.241` | 2026-08-22T20:54:12 |
| `config` | `config2010` | `90.230.22.194` | 2026-08-22T20:54:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **99** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 39 |
| libssh | 32 |
| Go SSH scanner | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 39 | 38 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `bc3aee897af7...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 39 | 38 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 4 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `bc3aee897af7...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **54** |
| High-Risk ASNs | **44** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS58224` | Iran Telecommunication Company PJS | 2 | HIGH |
| `AS6167` | Verizon Business | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6782c5d429e4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 18:56 |
| **Last Seen** | 2026-08-22 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:56:19` | `cowrie.session.connect` |
| `2026-08-22 18:56:19` | `cowrie.client.version` |
| `2026-08-22 18:56:19` | `cowrie.client.kex` |
| `2026-08-22 18:56:19` | `cowrie.login.success` |
| `2026-08-22 18:56:19` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:56:19` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8fe90c9632

| Field | Detail |
|---|---|
| **Source IP** | `45.170.50[.]2` |
| **First Seen** | 2026-08-22 18:58 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:58:54` | `cowrie.session.connect` |
| `2026-08-22 18:58:54` | `cowrie.client.version` |
| `2026-08-22 18:58:54` | `cowrie.client.kex` |
| `2026-08-22 18:58:56` | `cowrie.login.success` |
| `2026-08-22 18:58:56` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.50[.]2` to AbuseIPDB if not already reported
- [ ] Block `45.170.50[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8926a5ab869c

| Field | Detail |
|---|---|
| **Source IP** | `199.7.163[.]33` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:01` | `cowrie.session.connect` |
| `2026-08-22 18:59:02` | `cowrie.client.version` |
| `2026-08-22 18:59:02` | `cowrie.client.kex` |
| `2026-08-22 18:59:03` | `cowrie.login.success` |
| `2026-08-22 18:59:03` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.7.163[.]33` to AbuseIPDB if not already reported
- [ ] Block `199.7.163[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78ace84782b

| Field | Detail |
|---|---|
| **Source IP** | `93.118.128[.]115` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:07` | `cowrie.session.connect` |
| `2026-08-22 18:59:07` | `cowrie.client.version` |
| `2026-08-22 18:59:07` | `cowrie.client.kex` |
| `2026-08-22 18:59:09` | `cowrie.login.success` |
| `2026-08-22 18:59:09` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.118.128[.]115` to AbuseIPDB if not already reported
- [ ] Block `93.118.128[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a5dddb2b72

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:09` | `cowrie.session.connect` |
| `2026-08-22 18:59:09` | `cowrie.client.version` |
| `2026-08-22 18:59:09` | `cowrie.client.kex` |
| `2026-08-22 18:59:10` | `cowrie.login.success` |
| `2026-08-22 18:59:10` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:59:10` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac06288a150

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:14` | `cowrie.session.connect` |
| `2026-08-22 18:59:15` | `cowrie.client.version` |
| `2026-08-22 18:59:15` | `cowrie.client.kex` |
| `2026-08-22 18:59:17` | `cowrie.login.success` |
| `2026-08-22 18:59:18` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367ee28fd7ee

| Field | Detail |
|---|---|
| **Source IP** | `186.97.203[.]162` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:21` | `cowrie.session.connect` |
| `2026-08-22 18:59:22` | `cowrie.client.version` |
| `2026-08-22 18:59:22` | `cowrie.client.kex` |
| `2026-08-22 18:59:26` | `cowrie.login.success` |
| `2026-08-22 18:59:27` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.97.203[.]162` to AbuseIPDB if not already reported
- [ ] Block `186.97.203[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-550f0ec71543

| Field | Detail |
|---|---|
| **Source IP** | `110.25.109[.]48` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:33` | `cowrie.session.connect` |
| `2026-08-22 18:59:34` | `cowrie.client.version` |
| `2026-08-22 18:59:34` | `cowrie.client.kex` |
| `2026-08-22 18:59:35` | `cowrie.login.success` |
| `2026-08-22 18:59:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.109[.]48` to AbuseIPDB if not already reported
- [ ] Block `110.25.109[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7416f95b13

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 18:59 |
| **Last Seen** | 2026-08-22 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 18:59:42` | `cowrie.session.connect` |
| `2026-08-22 18:59:42` | `cowrie.client.version` |
| `2026-08-22 18:59:42` | `cowrie.client.kex` |
| `2026-08-22 18:59:43` | `cowrie.login.success` |
| `2026-08-22 18:59:43` | `cowrie.direct-tcpip.request` |
| `2026-08-22 18:59:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 18:59:43` | `cowrie.direct-tcpip.data` |
| `2026-08-22 18:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6998b70e855

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:09 |
| **Last Seen** | 2026-08-22 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:09:08` | `cowrie.session.connect` |
| `2026-08-22 19:09:09` | `cowrie.client.version` |
| `2026-08-22 19:09:09` | `cowrie.client.kex` |
| `2026-08-22 19:09:09` | `cowrie.login.success` |
| `2026-08-22 19:09:10` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:09:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:09:10` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1094f8de5c38

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:09 |
| **Last Seen** | 2026-08-22 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:09:47` | `cowrie.session.connect` |
| `2026-08-22 19:09:47` | `cowrie.client.version` |
| `2026-08-22 19:09:47` | `cowrie.client.kex` |
| `2026-08-22 19:09:48` | `cowrie.login.success` |
| `2026-08-22 19:09:48` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:09:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:09:49` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f330922b5d7d

| Field | Detail |
|---|---|
| **Source IP** | `199.7.163[.]33` |
| **First Seen** | 2026-08-22 19:14 |
| **Last Seen** | 2026-08-22 19:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:14:28` | `cowrie.session.connect` |
| `2026-08-22 19:14:28` | `cowrie.client.version` |
| `2026-08-22 19:14:28` | `cowrie.client.kex` |
| `2026-08-22 19:14:29` | `cowrie.login.success` |
| `2026-08-22 19:14:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `199.7.163[.]33` to AbuseIPDB if not already reported
- [ ] Block `199.7.163[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fd10e0e213

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:18 |
| **Last Seen** | 2026-08-22 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:18:52` | `cowrie.session.connect` |
| `2026-08-22 19:18:52` | `cowrie.client.version` |
| `2026-08-22 19:18:53` | `cowrie.client.kex` |
| `2026-08-22 19:18:54` | `cowrie.login.success` |
| `2026-08-22 19:18:54` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:18:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:18:54` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a1ac1d028f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:19 |
| **Last Seen** | 2026-08-22 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:19:35` | `cowrie.session.connect` |
| `2026-08-22 19:19:35` | `cowrie.client.version` |
| `2026-08-22 19:19:35` | `cowrie.client.kex` |
| `2026-08-22 19:19:36` | `cowrie.login.success` |
| `2026-08-22 19:19:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:19:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:19:36` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba7aa16e3fe

| Field | Detail |
|---|---|
| **Source IP** | `108.234.110[.]202` |
| **First Seen** | 2026-08-22 19:21 |
| **Last Seen** | 2026-08-22 19:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:21:24` | `cowrie.session.connect` |
| `2026-08-22 19:21:26` | `cowrie.client.version` |
| `2026-08-22 19:21:26` | `cowrie.client.kex` |
| `2026-08-22 19:21:31` | `cowrie.login.success` |
| `2026-08-22 19:21:32` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.234.110[.]202` to AbuseIPDB if not already reported
- [ ] Block `108.234.110[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e653894bac3

| Field | Detail |
|---|---|
| **Source IP** | `77.38.132[.]161` |
| **First Seen** | 2026-08-22 19:21 |
| **Last Seen** | 2026-08-22 19:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:21:38` | `cowrie.session.connect` |
| `2026-08-22 19:21:39` | `cowrie.client.version` |
| `2026-08-22 19:21:39` | `cowrie.client.kex` |
| `2026-08-22 19:21:40` | `cowrie.login.success` |
| `2026-08-22 19:21:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.38.132[.]161` to AbuseIPDB if not already reported
- [ ] Block `77.38.132[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b546b1cc382

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:28 |
| **Last Seen** | 2026-08-22 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:28:36` | `cowrie.session.connect` |
| `2026-08-22 19:28:36` | `cowrie.client.version` |
| `2026-08-22 19:28:36` | `cowrie.client.kex` |
| `2026-08-22 19:28:37` | `cowrie.login.success` |
| `2026-08-22 19:28:37` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:28:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:28:37` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5cb82c62eb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:29 |
| **Last Seen** | 2026-08-22 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:29:23` | `cowrie.session.connect` |
| `2026-08-22 19:29:23` | `cowrie.client.version` |
| `2026-08-22 19:29:23` | `cowrie.client.kex` |
| `2026-08-22 19:29:24` | `cowrie.login.success` |
| `2026-08-22 19:29:24` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:29:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:29:24` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc4d75847c8

| Field | Detail |
|---|---|
| **Source IP** | `181.87.154[.]121` |
| **First Seen** | 2026-08-22 19:31 |
| **Last Seen** | 2026-08-22 19:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:31:14` | `cowrie.session.connect` |
| `2026-08-22 19:31:15` | `cowrie.client.version` |
| `2026-08-22 19:31:15` | `cowrie.client.kex` |
| `2026-08-22 19:31:17` | `cowrie.login.success` |
| `2026-08-22 19:31:18` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.87.154[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.87.154[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a4f3b6083c

| Field | Detail |
|---|---|
| **Source IP** | `78.72.168[.]178` |
| **First Seen** | 2026-08-22 19:31 |
| **Last Seen** | 2026-08-22 19:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:31:22` | `cowrie.session.connect` |
| `2026-08-22 19:31:23` | `cowrie.client.version` |
| `2026-08-22 19:31:23` | `cowrie.client.kex` |
| `2026-08-22 19:31:24` | `cowrie.login.success` |
| `2026-08-22 19:31:24` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.72.168[.]178` to AbuseIPDB if not already reported
- [ ] Block `78.72.168[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad28fbc550f

| Field | Detail |
|---|---|
| **Source IP** | `115.246.242[.]2` |
| **First Seen** | 2026-08-22 19:31 |
| **Last Seen** | 2026-08-22 19:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:31:28` | `cowrie.session.connect` |
| `2026-08-22 19:31:29` | `cowrie.client.version` |
| `2026-08-22 19:31:29` | `cowrie.client.kex` |
| `2026-08-22 19:31:31` | `cowrie.login.success` |
| `2026-08-22 19:31:32` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.246.242[.]2` to AbuseIPDB if not already reported
- [ ] Block `115.246.242[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f987bdd0ee5

| Field | Detail |
|---|---|
| **Source IP** | `66.175.138[.]122` |
| **First Seen** | 2026-08-22 19:31 |
| **Last Seen** | 2026-08-22 19:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:31:53` | `cowrie.session.connect` |
| `2026-08-22 19:31:53` | `cowrie.client.version` |
| `2026-08-22 19:31:53` | `cowrie.client.kex` |
| `2026-08-22 19:31:54` | `cowrie.login.success` |
| `2026-08-22 19:31:55` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.175.138[.]122` to AbuseIPDB if not already reported
- [ ] Block `66.175.138[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3c1cf88db2

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-22 19:32 |
| **Last Seen** | 2026-08-22 19:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:32:00` | `cowrie.session.connect` |
| `2026-08-22 19:32:01` | `cowrie.client.version` |
| `2026-08-22 19:32:01` | `cowrie.client.kex` |
| `2026-08-22 19:32:03` | `cowrie.login.success` |
| `2026-08-22 19:32:04` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9dabdf9ab6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:38 |
| **Last Seen** | 2026-08-22 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:38:29` | `cowrie.session.connect` |
| `2026-08-22 19:38:29` | `cowrie.client.version` |
| `2026-08-22 19:38:29` | `cowrie.client.kex` |
| `2026-08-22 19:38:30` | `cowrie.login.success` |
| `2026-08-22 19:38:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:38:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:38:30` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee54ef12e9a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:39 |
| **Last Seen** | 2026-08-22 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:39:16` | `cowrie.session.connect` |
| `2026-08-22 19:39:16` | `cowrie.client.version` |
| `2026-08-22 19:39:17` | `cowrie.client.kex` |
| `2026-08-22 19:39:18` | `cowrie.login.success` |
| `2026-08-22 19:39:18` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:39:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:39:18` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79dae01d9ad

| Field | Detail |
|---|---|
| **Source IP** | `218.94.115[.]164` |
| **First Seen** | 2026-08-22 19:47 |
| **Last Seen** | 2026-08-22 19:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:47:17` | `cowrie.session.connect` |
| `2026-08-22 19:47:17` | `cowrie.client.version` |
| `2026-08-22 19:47:17` | `cowrie.client.kex` |
| `2026-08-22 19:47:19` | `cowrie.login.success` |
| `2026-08-22 19:47:20` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.94.115[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.94.115[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb8ddf4dd50

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:48 |
| **Last Seen** | 2026-08-22 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:48:27` | `cowrie.session.connect` |
| `2026-08-22 19:48:27` | `cowrie.client.version` |
| `2026-08-22 19:48:27` | `cowrie.client.kex` |
| `2026-08-22 19:48:28` | `cowrie.login.success` |
| `2026-08-22 19:48:28` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:48:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:48:28` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a5a1baddfe

| Field | Detail |
|---|---|
| **Source IP** | `58.57.154[.]146` |
| **First Seen** | 2026-08-22 19:48 |
| **Last Seen** | 2026-08-22 19:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:48:37` | `cowrie.session.connect` |
| `2026-08-22 19:48:37` | `cowrie.client.version` |
| `2026-08-22 19:48:37` | `cowrie.client.kex` |
| `2026-08-22 19:48:39` | `cowrie.login.success` |
| `2026-08-22 19:48:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.57.154[.]146` to AbuseIPDB if not already reported
- [ ] Block `58.57.154[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0dd70f1923b

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-22 19:48 |
| **Last Seen** | 2026-08-22 19:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:48:45` | `cowrie.session.connect` |
| `2026-08-22 19:48:45` | `cowrie.client.version` |
| `2026-08-22 19:48:45` | `cowrie.client.kex` |
| `2026-08-22 19:48:47` | `cowrie.login.success` |
| `2026-08-22 19:48:47` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd1687b2f59

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:49 |
| **Last Seen** | 2026-08-22 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:49:16` | `cowrie.session.connect` |
| `2026-08-22 19:49:16` | `cowrie.client.version` |
| `2026-08-22 19:49:16` | `cowrie.client.kex` |
| `2026-08-22 19:49:17` | `cowrie.login.success` |
| `2026-08-22 19:49:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:49:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:49:18` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d17951bad72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.133[.]195` |
| **First Seen** | 2026-08-22 19:53 |
| **Last Seen** | 2026-08-22 19:54 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:53:44` | `cowrie.session.connect` |
| `2026-08-22 19:53:47` | `cowrie.client.version` |
| `2026-08-22 19:53:47` | `cowrie.client.kex` |
| `2026-08-22 19:53:52` | `cowrie.login.success` |
| `2026-08-22 19:53:53` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.133[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.133[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3699ff4de3

| Field | Detail |
|---|---|
| **Source IP** | `104.248.83[.]99` |
| **First Seen** | 2026-08-22 19:53 |
| **Last Seen** | 2026-08-22 19:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:53:59` | `cowrie.session.connect` |
| `2026-08-22 19:53:59` | `cowrie.client.version` |
| `2026-08-22 19:53:59` | `cowrie.client.kex` |
| `2026-08-22 19:53:59` | `cowrie.login.success` |
| `2026-08-22 19:54:00` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.248.83[.]99` to AbuseIPDB if not already reported
- [ ] Block `104.248.83[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8aacb1fa755

| Field | Detail |
|---|---|
| **Source IP** | `118.145.104[.]105` |
| **First Seen** | 2026-08-22 19:57 |
| **Last Seen** | 2026-08-22 19:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:57:06` | `cowrie.session.connect` |
| `2026-08-22 19:57:07` | `cowrie.telnet.option` |
| `2026-08-22 19:57:07` | `cowrie.telnet.option` |
| `2026-08-22 19:58:07` | `cowrie.login.success` |
| `2026-08-22 19:58:08` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `118.145.104[.]105` to AbuseIPDB if not already reported
- [ ] Block `118.145.104[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f881b87c8a96

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:58 |
| **Last Seen** | 2026-08-22 19:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:58:21` | `cowrie.session.connect` |
| `2026-08-22 19:58:21` | `cowrie.client.version` |
| `2026-08-22 19:58:21` | `cowrie.client.kex` |
| `2026-08-22 19:58:22` | `cowrie.login.success` |
| `2026-08-22 19:58:23` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:58:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:58:23` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b740f4928024

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 19:59 |
| **Last Seen** | 2026-08-22 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 19:59:10` | `cowrie.session.connect` |
| `2026-08-22 19:59:10` | `cowrie.client.version` |
| `2026-08-22 19:59:10` | `cowrie.client.kex` |
| `2026-08-22 19:59:11` | `cowrie.login.success` |
| `2026-08-22 19:59:11` | `cowrie.direct-tcpip.request` |
| `2026-08-22 19:59:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 19:59:11` | `cowrie.direct-tcpip.data` |
| `2026-08-22 19:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572cf2f88028

| Field | Detail |
|---|---|
| **Source IP** | `65.20.165[.]78` |
| **First Seen** | 2026-08-22 20:03 |
| **Last Seen** | 2026-08-22 20:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:03:29` | `cowrie.session.connect` |
| `2026-08-22 20:03:29` | `cowrie.client.version` |
| `2026-08-22 20:03:29` | `cowrie.client.kex` |
| `2026-08-22 20:03:30` | `cowrie.login.success` |
| `2026-08-22 20:03:30` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.165[.]78` to AbuseIPDB if not already reported
- [ ] Block `65.20.165[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64eb8800a1f

| Field | Detail |
|---|---|
| **Source IP** | `63.47.149[.]59` |
| **First Seen** | 2026-08-22 20:03 |
| **Last Seen** | 2026-08-22 20:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:03:36` | `cowrie.session.connect` |
| `2026-08-22 20:03:37` | `cowrie.client.version` |
| `2026-08-22 20:03:37` | `cowrie.client.kex` |
| `2026-08-22 20:03:39` | `cowrie.login.success` |
| `2026-08-22 20:03:40` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:03:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.47.149[.]59` to AbuseIPDB if not already reported
- [ ] Block `63.47.149[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c872ae2e096f

| Field | Detail |
|---|---|
| **Source IP** | `121.135.47[.]141` |
| **First Seen** | 2026-08-22 20:03 |
| **Last Seen** | 2026-08-22 20:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:03:37` | `cowrie.session.connect` |
| `2026-08-22 20:03:38` | `cowrie.client.version` |
| `2026-08-22 20:03:38` | `cowrie.client.kex` |
| `2026-08-22 20:03:40` | `cowrie.login.success` |
| `2026-08-22 20:03:41` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.135.47[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.135.47[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de36012c4997

| Field | Detail |
|---|---|
| **Source IP** | `121.99.190[.]167` |
| **First Seen** | 2026-08-22 20:03 |
| **Last Seen** | 2026-08-22 20:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:03:47` | `cowrie.session.connect` |
| `2026-08-22 20:03:48` | `cowrie.client.version` |
| `2026-08-22 20:03:48` | `cowrie.client.kex` |
| `2026-08-22 20:03:50` | `cowrie.login.success` |
| `2026-08-22 20:03:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.99.190[.]167` to AbuseIPDB if not already reported
- [ ] Block `121.99.190[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d400f78d10bb

| Field | Detail |
|---|---|
| **Source IP** | `65.20.189[.]52` |
| **First Seen** | 2026-08-22 20:04 |
| **Last Seen** | 2026-08-22 20:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:04:34` | `cowrie.session.connect` |
| `2026-08-22 20:04:34` | `cowrie.client.version` |
| `2026-08-22 20:04:34` | `cowrie.client.kex` |
| `2026-08-22 20:04:36` | `cowrie.login.success` |
| `2026-08-22 20:04:36` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.189[.]52` to AbuseIPDB if not already reported
- [ ] Block `65.20.189[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9839e07ed0ff

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-08-22 20:04 |
| **Last Seen** | 2026-08-22 20:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:04:42` | `cowrie.session.connect` |
| `2026-08-22 20:04:43` | `cowrie.client.version` |
| `2026-08-22 20:04:43` | `cowrie.client.kex` |
| `2026-08-22 20:04:45` | `cowrie.login.success` |
| `2026-08-22 20:04:45` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4719a810f09c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:08 |
| **Last Seen** | 2026-08-22 20:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:08:32` | `cowrie.session.connect` |
| `2026-08-22 20:08:32` | `cowrie.client.version` |
| `2026-08-22 20:08:32` | `cowrie.client.kex` |
| `2026-08-22 20:08:33` | `cowrie.login.success` |
| `2026-08-22 20:08:33` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:08:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:08:34` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338340a8b9e5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:09 |
| **Last Seen** | 2026-08-22 20:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:09:19` | `cowrie.session.connect` |
| `2026-08-22 20:09:19` | `cowrie.client.version` |
| `2026-08-22 20:09:19` | `cowrie.client.kex` |
| `2026-08-22 20:09:22` | `cowrie.login.success` |
| `2026-08-22 20:09:22` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:09:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:09:23` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186b61325bf9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:18 |
| **Last Seen** | 2026-08-22 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:18:41` | `cowrie.session.connect` |
| `2026-08-22 20:18:41` | `cowrie.client.version` |
| `2026-08-22 20:18:41` | `cowrie.client.kex` |
| `2026-08-22 20:18:42` | `cowrie.login.success` |
| `2026-08-22 20:18:42` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:18:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:18:42` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7cb30d1f04

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:19 |
| **Last Seen** | 2026-08-22 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:19:27` | `cowrie.session.connect` |
| `2026-08-22 20:19:27` | `cowrie.client.version` |
| `2026-08-22 20:19:27` | `cowrie.client.kex` |
| `2026-08-22 20:19:28` | `cowrie.login.success` |
| `2026-08-22 20:19:28` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:19:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:19:28` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452e5faadbf1

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]220` |
| **First Seen** | 2026-08-22 20:20 |
| **Last Seen** | 2026-08-22 20:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:20:18` | `cowrie.session.connect` |
| `2026-08-22 20:20:19` | `cowrie.client.version` |
| `2026-08-22 20:20:19` | `cowrie.client.kex` |
| `2026-08-22 20:20:21` | `cowrie.login.success` |
| `2026-08-22 20:20:22` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6863850aede1

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-08-22 20:20 |
| **Last Seen** | 2026-08-22 20:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:20:27` | `cowrie.session.connect` |
| `2026-08-22 20:20:27` | `cowrie.client.version` |
| `2026-08-22 20:20:27` | `cowrie.client.kex` |
| `2026-08-22 20:20:28` | `cowrie.login.success` |
| `2026-08-22 20:20:28` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe6b55b6a3f

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-22 20:21 |
| **Last Seen** | 2026-08-22 20:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:21:06` | `cowrie.session.connect` |
| `2026-08-22 20:21:07` | `cowrie.client.version` |
| `2026-08-22 20:21:07` | `cowrie.client.kex` |
| `2026-08-22 20:21:08` | `cowrie.login.success` |
| `2026-08-22 20:21:09` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3000897a0f16

| Field | Detail |
|---|---|
| **Source IP** | `116.114.84[.]246` |
| **First Seen** | 2026-08-22 20:21 |
| **Last Seen** | 2026-08-22 20:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:21:14` | `cowrie.session.connect` |
| `2026-08-22 20:21:15` | `cowrie.client.version` |
| `2026-08-22 20:21:15` | `cowrie.client.kex` |
| `2026-08-22 20:21:17` | `cowrie.login.success` |
| `2026-08-22 20:21:17` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.114.84[.]246` to AbuseIPDB if not already reported
- [ ] Block `116.114.84[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b0ad059250

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-22 20:23 |
| **Last Seen** | 2026-08-22 20:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:23:01` | `cowrie.session.connect` |
| `2026-08-22 20:23:01` | `cowrie.client.version` |
| `2026-08-22 20:23:01` | `cowrie.client.kex` |
| `2026-08-22 20:23:01` | `cowrie.login.success` |
| `2026-08-22 20:23:02` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:23:02` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e66b6ee77b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:28 |
| **Last Seen** | 2026-08-22 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:28:50` | `cowrie.session.connect` |
| `2026-08-22 20:28:50` | `cowrie.client.version` |
| `2026-08-22 20:28:50` | `cowrie.client.kex` |
| `2026-08-22 20:28:51` | `cowrie.login.success` |
| `2026-08-22 20:28:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:28:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:28:52` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c297d33772

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:29 |
| **Last Seen** | 2026-08-22 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:29:33` | `cowrie.session.connect` |
| `2026-08-22 20:29:33` | `cowrie.client.version` |
| `2026-08-22 20:29:34` | `cowrie.client.kex` |
| `2026-08-22 20:29:34` | `cowrie.login.success` |
| `2026-08-22 20:29:35` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:29:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:29:35` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c399aff1e63a

| Field | Detail |
|---|---|
| **Source IP** | `83.150.16[.]254` |
| **First Seen** | 2026-08-22 20:35 |
| **Last Seen** | 2026-08-22 20:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:35:24` | `cowrie.session.connect` |
| `2026-08-22 20:35:25` | `cowrie.client.version` |
| `2026-08-22 20:35:25` | `cowrie.client.kex` |
| `2026-08-22 20:35:26` | `cowrie.login.success` |
| `2026-08-22 20:35:26` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.150.16[.]254` to AbuseIPDB if not already reported
- [ ] Block `83.150.16[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6032bb0dd14

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-22 20:35 |
| **Last Seen** | 2026-08-22 20:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:35:31` | `cowrie.session.connect` |
| `2026-08-22 20:35:32` | `cowrie.client.version` |
| `2026-08-22 20:35:32` | `cowrie.client.kex` |
| `2026-08-22 20:35:34` | `cowrie.login.success` |
| `2026-08-22 20:35:34` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff016bd8d48

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-22 20:35 |
| **Last Seen** | 2026-08-22 20:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:35:32` | `cowrie.session.connect` |
| `2026-08-22 20:35:32` | `cowrie.client.version` |
| `2026-08-22 20:35:32` | `cowrie.client.kex` |
| `2026-08-22 20:35:34` | `cowrie.login.success` |
| `2026-08-22 20:35:34` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f3e52dbbfb

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-22 20:35 |
| **Last Seen** | 2026-08-22 20:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:35:39` | `cowrie.session.connect` |
| `2026-08-22 20:35:40` | `cowrie.client.version` |
| `2026-08-22 20:35:40` | `cowrie.client.kex` |
| `2026-08-22 20:35:42` | `cowrie.login.success` |
| `2026-08-22 20:35:43` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072016b65691

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-08-22 20:37 |
| **Last Seen** | 2026-08-22 20:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:37:25` | `cowrie.session.connect` |
| `2026-08-22 20:37:26` | `cowrie.client.version` |
| `2026-08-22 20:37:26` | `cowrie.client.kex` |
| `2026-08-22 20:37:27` | `cowrie.login.success` |
| `2026-08-22 20:37:28` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38f3796428b

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-22 20:37 |
| **Last Seen** | 2026-08-22 20:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:37:38` | `cowrie.session.connect` |
| `2026-08-22 20:37:38` | `cowrie.client.version` |
| `2026-08-22 20:37:38` | `cowrie.client.kex` |
| `2026-08-22 20:37:41` | `cowrie.login.success` |
| `2026-08-22 20:37:41` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a90503c9c24

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:38 |
| **Last Seen** | 2026-08-22 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:38:54` | `cowrie.session.connect` |
| `2026-08-22 20:38:54` | `cowrie.client.version` |
| `2026-08-22 20:38:54` | `cowrie.client.kex` |
| `2026-08-22 20:38:55` | `cowrie.login.success` |
| `2026-08-22 20:38:55` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:38:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:38:55` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dc3b7a1e37

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:39 |
| **Last Seen** | 2026-08-22 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:39:42` | `cowrie.session.connect` |
| `2026-08-22 20:39:42` | `cowrie.client.version` |
| `2026-08-22 20:39:42` | `cowrie.client.kex` |
| `2026-08-22 20:39:43` | `cowrie.login.success` |
| `2026-08-22 20:39:43` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:39:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:39:43` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf838d444650

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:48 |
| **Last Seen** | 2026-08-22 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:48:50` | `cowrie.session.connect` |
| `2026-08-22 20:48:50` | `cowrie.client.version` |
| `2026-08-22 20:48:50` | `cowrie.client.kex` |
| `2026-08-22 20:48:51` | `cowrie.login.success` |
| `2026-08-22 20:48:51` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:48:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:48:51` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebd8268359d3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-22 20:49 |
| **Last Seen** | 2026-08-22 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:49:32` | `cowrie.session.connect` |
| `2026-08-22 20:49:32` | `cowrie.client.version` |
| `2026-08-22 20:49:33` | `cowrie.client.kex` |
| `2026-08-22 20:49:34` | `cowrie.login.success` |
| `2026-08-22 20:49:34` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:49:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-22 20:49:34` | `cowrie.direct-tcpip.data` |
| `2026-08-22 20:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a470e5a6d92a

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-22 20:53 |
| **Last Seen** | 2026-08-22 20:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:53:00` | `cowrie.session.connect` |
| `2026-08-22 20:53:01` | `cowrie.client.version` |
| `2026-08-22 20:53:01` | `cowrie.client.kex` |
| `2026-08-22 20:53:03` | `cowrie.login.success` |
| `2026-08-22 20:53:03` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87c31602651

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-22 20:53 |
| **Last Seen** | 2026-08-22 20:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:53:09` | `cowrie.session.connect` |
| `2026-08-22 20:53:10` | `cowrie.client.version` |
| `2026-08-22 20:53:10` | `cowrie.client.kex` |
| `2026-08-22 20:53:11` | `cowrie.login.success` |
| `2026-08-22 20:53:12` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15b549ce866

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-22 20:54 |
| **Last Seen** | 2026-08-22 20:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:54:10` | `cowrie.session.connect` |
| `2026-08-22 20:54:10` | `cowrie.client.version` |
| `2026-08-22 20:54:10` | `cowrie.client.kex` |
| `2026-08-22 20:54:12` | `cowrie.login.success` |
| `2026-08-22 20:54:13` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1faaf0a60d

| Field | Detail |
|---|---|
| **Source IP** | `90.230.22[.]194` |
| **First Seen** | 2026-08-22 20:54 |
| **Last Seen** | 2026-08-22 20:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-22 20:54:18` | `cowrie.session.connect` |
| `2026-08-22 20:54:18` | `cowrie.client.version` |
| `2026-08-22 20:54:18` | `cowrie.client.kex` |
| `2026-08-22 20:54:19` | `cowrie.login.success` |
| `2026-08-22 20:54:19` | `cowrie.direct-tcpip.request` |
| `2026-08-22 20:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.22[.]194` to AbuseIPDB if not already reported
- [ ] Block `90.230.22[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **4** | 2026-08-22 19:19 | 2026-08-22 20:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.209.95[.]251` | **2** | 2026-08-22 20:38 | 2026-08-22 20:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.161.50[.]108` | **2** | 2026-08-22 20:37 | 2026-08-22 20:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]200` | **2** | 2026-08-22 19:20 | 2026-08-22 19:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.99.190[.]167` | 1 | 2026-08-22 20:03 | 2026-08-22 20:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-08-22 20:37 | 2026-08-22 20:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | 1 | 2026-08-22 20:12 | 2026-08-22 20:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.244.214[.]60` | 1 | 2026-08-22 19:04 | 2026-08-22 19:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `38.211.32[.]124` | 1 | 2026-08-22 19:50 | 2026-08-22 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-22 19:46 | 2026-08-22 19:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.10.74[.]2` | 1 | 2026-08-22 19:21 | 2026-08-22 19:21 | 12s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]134` | 1 | 2026-08-22 19:19 | 2026-08-22 19:20 | 22s | 0 | `T1592` | 🟢 LOW |
| `71.187.203[.]185` | 1 | 2026-08-22 20:41 | 2026-08-22 20:41 | 11s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-08-22 18:59 | 2026-08-22 18:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.203.165[.]140` | 1 | 2026-08-22 20:04 | 2026-08-22 20:06 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `65.20.165[.]78` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 1 |
| `46.10.74[.]2` | BG | BTC Broadband Service | **100** ⚠️ | 9 |
| `66.175.138[.]122` | US | C Spire Fiber | **100** ⚠️ | 1 |
| `77.38.132[.]161` | LV | SIA BITE Latvija | **100** ⚠️ | 1 |
| `110.25.109[.]48` | TW | Far EasTone Telecommunication Co., Ltd. | **100** ⚠️ | 6 |
| `179.181.133[.]153` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `120.234.232[.]184` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `78.72.168[.]178` | SE | Telia Network Services | **100** ⚠️ | 1 |
| `176.32.193[.]16` | AM | Ucom CJSC | **100** ⚠️ | 50 |
| `118.145.104[.]105` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 76 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 99 cases |
| Tool 34  | Credential Extractor        | ✅ 89 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (12.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 54 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 15 recon entry/entries in table (4 group(s) consolidating 10 session(s)).

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
_Report time: 2026-08-22T22:25:49Z_

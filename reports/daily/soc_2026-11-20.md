# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-11-20 |
| **Generated At** | 2026-11-20T19:27:52Z |
| **Shift Time** | 19:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **535** |
| Confirmed Threats | **451** |
| False Positives Filtered | **84** (15.7%) |
| Unique Attacker IPs | **194** |
| Countries of Origin | **46** |
| High Severity Cases | **339** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **195** |
| Malware Samples Analyzed | **9** HIGH · **26** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3613** |
| Unique Credential Pairs | **1538** |
| Unique Usernames | **528** |
| Unique Passwords | **1065** |
| Successful Auth Pairs | **3306** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1347 |
| `admin` | 159 |
| `ubuntu` | 99 |
| `user` | 65 |
| `support` | 53 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 178 |
| `123` | 97 |
| `root` | 83 |
| `admin` | 75 |
| `1234` | 69 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `rootssssss23424123123` | `rootssssss23424123123` | 52 |
| `admin` | `admin` | 51 |
| `root` | `root3245gs5662d34111111111` | 46 |
| `root` | `root` | 43 |
| `support` | `support` | 31 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `sec` | `109.160.32.161` | 2026-11-20T02:55:07 |
| `drcomadmin` | `drcomadmin123` | `109.160.32.161` | 2026-11-20T02:55:16 |
| `user` | `111111` | `109.160.32.161` | 2026-11-20T02:55:21 |
| `admin` | `E4IuG88G` | `109.160.32.161` | 2026-11-20T02:55:26 |
| `quai` | `quai` | `45.148.10.61` | 2026-11-20T02:55:29 |
| `term2` | `term2` | `109.160.32.161` | 2026-11-20T02:55:34 |
| `root` | `1qazxsw2` | `109.160.32.161` | 2026-11-20T02:55:39 |
| `cloud` | `Wangsu@2017` | `109.160.32.161` | 2026-11-20T02:55:46 |
| `deploy` | `dev` | `109.160.32.161` | 2026-11-20T02:55:54 |
| `jayalakshmi` | `jayalakshmi` | `109.160.32.161` | 2026-11-20T02:56:01 |
| `kailin` | `esearch` | `109.160.32.161` | 2026-11-20T02:56:08 |
| `deploy` | `123456789` | `109.160.32.161` | 2026-11-20T02:56:16 |
| `root` | `Test1234` | `109.160.32.161` | 2026-11-20T02:56:23 |
| `yzb` | `yzb@123456` | `109.160.32.161` | 2026-11-20T02:56:29 |
| `root` | `root1234` | `109.160.32.161` | 2026-11-20T02:56:35 |
| `root` | `12345123` | `109.160.32.161` | 2026-11-20T02:56:41 |
| `haruto` | `haruto` | `45.148.10.61` | 2026-11-20T02:56:47 |
| `devops` | `123456` | `109.160.32.161` | 2026-11-20T02:56:48 |
| `root` | `a123456A` | `109.160.32.161` | 2026-11-20T02:56:55 |
| `newuser` | `123456` | `109.160.32.161` | 2026-11-20T02:57:03 |
_… 3286 more successful pair(s) in credentials.json_

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **535** |
| Sessions with Fingerprint | **28** |
| Unique HASSH Fingerprints | **28** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 239 |
| libssh | 62 |
| OpenSSH | 10 |
| Unknown | 5 |
| Perl Net::SSH | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 165 | 3 |
| `f555226df196...` | Mirai/variant | 57 | 29 |
| `7d01d047ace6...` | Mirai/variant | 29 | 4 |
| `16443846184e...` | Generic scanner | 12 | 6 |
| `eff4c24daffc...` | Modern SSH client | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 165 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 57 | 29 | Mirai/variant |
| `7d01d047ace6...` | Go SSH scanner | 29 | 4 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 12 | 6 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 8 | 1 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 7 | 3 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 7 | 7 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 3 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **188** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 4 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 54 | 28 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1140, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
ping; sh
```
Source IPs: `85.130.237.235`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox HDEEG
```
Source IPs: `138.255.14.38`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **194** |
| Unique ASNs | **96** |
| High-Risk ASNs | **68** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 41 | HIGH |
| `AS14061` | DigitalOcean, LLC | 10 | HIGH |
| `AS213412` | ONYPHE SAS | 9 | LOW |
| `AS396982` | Google LLC | 7 | HIGH |
| `AS15169` | Google LLC | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (325)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2c10ca5aee00

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]161` |
| **First Seen** | 2026-11-20 02:55 |
| **Last Seen** | 2026-11-20 02:55 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 02:55:08` | `cowrie.session.connect` |
| `2026-11-20 02:55:09` | `cowrie.client.version` |
| `2026-11-20 02:55:09` | `cowrie.client.kex` |
| `2026-11-20 02:55:16` | `cowrie.login.success` |
| `2026-11-20 02:55:20` | `cowrie.session.params` |
| `2026-11-20 02:55:20` | `cowrie.command.input` |
| `2026-11-20 02:55:21` | `cowrie.log.closed` |
| `2026-11-20 02:55:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]161` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0266e529b77

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-11-20 02:55 |
| **Last Seen** | 2026-11-20 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 02:55:29` | `cowrie.session.connect` |
| `2026-11-20 02:55:29` | `cowrie.client.version` |
| `2026-11-20 02:55:29` | `cowrie.client.kex` |
| `2026-11-20 02:55:29` | `cowrie.login.success` |
| `2026-11-20 02:55:30` | `cowrie.session.params` |
| `2026-11-20 02:55:30` | `cowrie.command.input` |
| `2026-11-20 02:55:30` | `cowrie.log.closed` |
| `2026-11-20 02:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308c76c38117

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-20 02:59 |
| **Last Seen** | 2026-11-20 02:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 02:59:09` | `cowrie.session.connect` |
| `2026-11-20 02:59:09` | `cowrie.client.version` |
| `2026-11-20 02:59:09` | `cowrie.client.kex` |
| `2026-11-20 02:59:09` | `cowrie.login.success` |
| `2026-11-20 02:59:09` | `cowrie.direct-tcpip.request` |
| `2026-11-20 02:59:09` | `cowrie.direct-tcpip.data` |
| `2026-11-20 02:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5dafafc045f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-20 03:24 |
| **Last Seen** | 2026-11-20 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:24:42` | `cowrie.session.connect` |
| `2026-11-20 03:24:43` | `cowrie.login.success` |
| `2026-11-20 03:24:44` | `cowrie.session.params` |
| `2026-11-20 03:24:44` | `cowrie.log.closed` |
| `2026-11-20 03:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d71761b79f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-20 03:27 |
| **Last Seen** | 2026-11-20 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:27:29` | `cowrie.session.connect` |
| `2026-11-20 03:27:29` | `cowrie.login.success` |
| `2026-11-20 03:27:30` | `cowrie.session.params` |
| `2026-11-20 03:27:30` | `cowrie.log.closed` |
| `2026-11-20 03:27:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a19aa988b9d

| Field | Detail |
|---|---|
| **Source IP** | `36.255.97[.]232` |
| **First Seen** | 2026-11-20 03:42 |
| **Last Seen** | 2026-11-20 03:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:42:55` | `cowrie.session.connect` |
| `2026-11-20 03:42:55` | `cowrie.client.version` |
| `2026-11-20 03:42:55` | `cowrie.client.kex` |
| `2026-11-20 03:42:55` | `cowrie.login.success` |
| `2026-11-20 03:42:55` | `cowrie.direct-tcpip.request` |
| `2026-11-20 03:42:55` | `cowrie.direct-tcpip.data` |
| `2026-11-20 03:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.97[.]232` to AbuseIPDB if not already reported
- [ ] Block `36.255.97[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca34166ee77

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]200` |
| **First Seen** | 2026-11-20 03:52 |
| **Last Seen** | 2026-11-20 03:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:52:13` | `cowrie.session.connect` |
| `2026-11-20 03:52:13` | `cowrie.client.version` |
| `2026-11-20 03:52:13` | `cowrie.client.kex` |
| `2026-11-20 03:52:15` | `cowrie.login.success` |
| `2026-11-20 03:52:16` | `cowrie.session.params` |
| `2026-11-20 03:52:16` | `cowrie.command.input` |
| `2026-11-20 03:52:16` | `cowrie.log.closed` |
| `2026-11-20 03:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]200` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fbfd18aba4

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-11-20 03:58 |
| **Last Seen** | 2026-11-20 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:58:21` | `cowrie.session.connect` |
| `2026-11-20 03:58:21` | `cowrie.client.version` |
| `2026-11-20 03:58:21` | `cowrie.client.kex` |
| `2026-11-20 03:58:22` | `cowrie.login.success` |
| `2026-11-20 03:58:22` | `cowrie.direct-tcpip.request` |
| `2026-11-20 03:58:22` | `cowrie.direct-tcpip.ja4` |
| `2026-11-20 03:58:22` | `cowrie.direct-tcpip.data` |
| `2026-11-20 03:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b4e29c8bdb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-20 03:58 |
| **Last Seen** | 2026-11-20 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:58:32` | `cowrie.session.connect` |
| `2026-11-20 03:58:32` | `cowrie.client.version` |
| `2026-11-20 03:58:32` | `cowrie.client.kex` |
| `2026-11-20 03:58:32` | `cowrie.login.success` |
| `2026-11-20 03:58:32` | `cowrie.direct-tcpip.request` |
| `2026-11-20 03:58:32` | `cowrie.direct-tcpip.ja4` |
| `2026-11-20 03:58:32` | `cowrie.direct-tcpip.data` |
| `2026-11-20 03:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3692a373b7

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-20 03:58 |
| **Last Seen** | 2026-11-20 03:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 03:58:33` | `cowrie.session.connect` |
| `2026-11-20 03:58:33` | `cowrie.client.version` |
| `2026-11-20 03:58:33` | `cowrie.client.kex` |
| `2026-11-20 03:58:33` | `cowrie.login.success` |
| `2026-11-20 03:58:33` | `cowrie.direct-tcpip.request` |
| `2026-11-20 03:58:33` | `cowrie.direct-tcpip.ja4` |
| `2026-11-20 03:58:33` | `cowrie.direct-tcpip.data` |
| `2026-11-20 03:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2dffee62da

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]200` |
| **First Seen** | 2026-11-20 04:00 |
| **Last Seen** | 2026-11-20 04:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:00:03` | `cowrie.session.connect` |
| `2026-11-20 04:00:03` | `cowrie.client.version` |
| `2026-11-20 04:00:03` | `cowrie.client.kex` |
| `2026-11-20 04:00:05` | `cowrie.login.success` |
| `2026-11-20 04:00:06` | `cowrie.session.params` |
| `2026-11-20 04:00:06` | `cowrie.command.input` |
| `2026-11-20 04:00:06` | `cowrie.log.closed` |
| `2026-11-20 04:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]200` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad4c9dde5b2

| Field | Detail |
|---|---|
| **Source IP** | `109.160.32[.]161` |
| **First Seen** | 2026-11-20 04:00 |
| **Last Seen** | 2026-11-20 04:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:00:05` | `cowrie.session.connect` |
| `2026-11-20 04:00:06` | `cowrie.client.version` |
| `2026-11-20 04:00:06` | `cowrie.client.kex` |
| `2026-11-20 04:00:10` | `cowrie.login.success` |
| `2026-11-20 04:00:13` | `cowrie.session.params` |
| `2026-11-20 04:00:13` | `cowrie.command.input` |
| `2026-11-20 04:00:15` | `cowrie.log.closed` |
| `2026-11-20 04:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.160.32[.]161` to AbuseIPDB if not already reported
- [ ] Block `109.160.32[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394568a8fe7c

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]29` |
| **First Seen** | 2026-11-20 04:00 |
| **Last Seen** | 2026-11-20 04:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:00:38` | `cowrie.session.connect` |
| `2026-11-20 04:00:38` | `cowrie.client.version` |
| `2026-11-20 04:00:38` | `cowrie.client.kex` |
| `2026-11-20 04:00:39` | `cowrie.login.success` |
| `2026-11-20 04:00:39` | `cowrie.direct-tcpip.request` |
| `2026-11-20 04:00:39` | `cowrie.direct-tcpip.ja4` |
| `2026-11-20 04:00:39` | `cowrie.direct-tcpip.data` |
| `2026-11-20 04:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]29` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d185ca4e176a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]61` |
| **First Seen** | 2026-11-20 04:01 |
| **Last Seen** | 2026-11-20 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:01:10` | `cowrie.session.connect` |
| `2026-11-20 04:01:10` | `cowrie.client.version` |
| `2026-11-20 04:01:10` | `cowrie.client.kex` |
| `2026-11-20 04:01:10` | `cowrie.login.success` |
| `2026-11-20 04:01:11` | `cowrie.session.params` |
| `2026-11-20 04:01:11` | `cowrie.command.input` |
| `2026-11-20 04:01:11` | `cowrie.log.closed` |
| `2026-11-20 04:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9550185ec2a

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-11-20 04:01 |
| **Last Seen** | 2026-11-20 04:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:01:50` | `cowrie.session.connect` |
| `2026-11-20 04:01:50` | `cowrie.client.version` |
| `2026-11-20 04:01:50` | `cowrie.client.kex` |
| `2026-11-20 04:01:51` | `cowrie.login.success` |
| `2026-11-20 04:01:51` | `cowrie.direct-tcpip.request` |
| `2026-11-20 04:01:51` | `cowrie.direct-tcpip.ja4` |
| `2026-11-20 04:01:51` | `cowrie.direct-tcpip.data` |
| `2026-11-20 04:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17ca48c3bca

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-11-20 04:02 |
| **Last Seen** | 2026-11-20 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:02:16` | `cowrie.session.connect` |
| `2026-11-20 04:02:16` | `cowrie.client.version` |
| `2026-11-20 04:02:16` | `cowrie.client.kex` |
| `2026-11-20 04:02:16` | `cowrie.login.success` |
| `2026-11-20 04:02:16` | `cowrie.direct-tcpip.request` |
| `2026-11-20 04:02:16` | `cowrie.direct-tcpip.ja4` |
| `2026-11-20 04:02:16` | `cowrie.direct-tcpip.data` |
| `2026-11-20 04:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448e8345d847

| Field | Detail |
|---|---|
| **Source IP** | `93.152.221[.]108` |
| **First Seen** | 2026-11-20 04:04 |
| **Last Seen** | 2026-11-20 04:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:04:15` | `cowrie.session.connect` |
| `2026-11-20 04:04:15` | `cowrie.client.version` |
| `2026-11-20 04:04:15` | `cowrie.client.kex` |
| `2026-11-20 04:04:15` | `cowrie.login.success` |
| `2026-11-20 04:04:15` | `cowrie.direct-tcpip.request` |
| `2026-11-20 04:04:15` | `cowrie.direct-tcpip.data` |
| `2026-11-20 04:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.152.221[.]108` to AbuseIPDB if not already reported
- [ ] Block `93.152.221[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e379543d901

| Field | Detail |
|---|---|
| **Source IP** | `163.7.4[.]109` |
| **First Seen** | 2026-11-20 04:06 |
| **Last Seen** | 2026-11-20 04:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:06:07` | `cowrie.session.connect` |
| `2026-11-20 04:06:07` | `cowrie.client.version` |
| `2026-11-20 04:06:07` | `cowrie.client.kex` |
| `2026-11-20 04:06:08` | `cowrie.login.success` |
| `2026-11-20 04:06:09` | `cowrie.session.params` |
| `2026-11-20 04:06:09` | `cowrie.command.input` |
| `2026-11-20 04:06:09` | `cowrie.command.failed` |
| `2026-11-20 04:06:10` | `cowrie.log.closed` |
| `2026-11-20 04:06:11` | `cowrie.session.params` |
| `2026-11-20 04:06:11` | `cowrie.command.input` |
| `2026-11-20 04:06:11` | `cowrie.session.file_download` |
| `2026-11-20 04:06:11` | `cowrie.log.closed` |
| `2026-11-20 04:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.4[.]109` to AbuseIPDB if not already reported
- [ ] Block `163.7.4[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e098e80ab3

| Field | Detail |
|---|---|
| **Source IP** | `163.7.4[.]109` |
| **First Seen** | 2026-11-20 04:06 |
| **Last Seen** | 2026-11-20 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:06:11` | `cowrie.session.connect` |
| `2026-11-20 04:06:11` | `cowrie.client.version` |
| `2026-11-20 04:06:12` | `cowrie.client.kex` |
| `2026-11-20 04:06:13` | `cowrie.login.success` |
| `2026-11-20 04:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.4[.]109` to AbuseIPDB if not already reported
- [ ] Block `163.7.4[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3bb821d311

| Field | Detail |
|---|---|
| **Source IP** | `34.1.233[.]70` |
| **First Seen** | 2026-11-20 04:06 |
| **Last Seen** | 2026-11-20 04:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:06:19` | `cowrie.session.connect` |
| `2026-11-20 04:06:19` | `cowrie.client.version` |
| `2026-11-20 04:06:19` | `cowrie.client.kex` |
| `2026-11-20 04:06:23` | `cowrie.login.success` |
| `2026-11-20 04:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.1.233[.]70` to AbuseIPDB if not already reported
- [ ] Block `34.1.233[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cdc6a7b49b

| Field | Detail |
|---|---|
| **Source IP** | `122.180.242[.]27` |
| **First Seen** | 2026-11-20 04:08 |
| **Last Seen** | 2026-11-20 04:08 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:08:37` | `cowrie.session.connect` |
| `2026-11-20 04:08:37` | `cowrie.client.version` |
| `2026-11-20 04:08:37` | `cowrie.client.kex` |
| `2026-11-20 04:08:38` | `cowrie.login.success` |
| `2026-11-20 04:08:40` | `cowrie.session.params` |
| `2026-11-20 04:08:40` | `cowrie.command.input` |
| `2026-11-20 04:08:40` | `cowrie.command.failed` |
| `2026-11-20 04:08:40` | `cowrie.log.closed` |
| `2026-11-20 04:08:41` | `cowrie.session.params` |
| `2026-11-20 04:08:41` | `cowrie.command.input` |
| `2026-11-20 04:08:42` | `cowrie.session.file_download` |
| `2026-11-20 04:08:42` | `cowrie.log.closed` |
| `2026-11-20 04:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.180.242[.]27` to AbuseIPDB if not already reported
- [ ] Block `122.180.242[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c762a217147

| Field | Detail |
|---|---|
| **Source IP** | `122.180.242[.]27` |
| **First Seen** | 2026-11-20 04:08 |
| **Last Seen** | 2026-11-20 04:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:08:42` | `cowrie.session.connect` |
| `2026-11-20 04:08:42` | `cowrie.client.version` |
| `2026-11-20 04:08:42` | `cowrie.client.kex` |
| `2026-11-20 04:08:44` | `cowrie.login.success` |
| `2026-11-20 04:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.180.242[.]27` to AbuseIPDB if not already reported
- [ ] Block `122.180.242[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e39e1ff313f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-11-20 04:19 |
| **Last Seen** | 2026-11-20 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:19:53` | `cowrie.session.connect` |
| `2026-11-20 04:19:53` | `cowrie.client.version` |
| `2026-11-20 04:19:53` | `cowrie.client.kex` |
| `2026-11-20 04:19:54` | `cowrie.login.success` |
| `2026-11-20 04:19:54` | `cowrie.direct-tcpip.request` |
| `2026-11-20 04:19:54` | `cowrie.direct-tcpip.data` |
| `2026-11-20 04:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e2cda95bfe

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]252` |
| **First Seen** | 2026-11-20 04:30 |
| **Last Seen** | 2026-11-20 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:30:38` | `cowrie.session.connect` |
| `2026-11-20 04:30:39` | `cowrie.login.success` |
| `2026-11-20 04:30:40` | `cowrie.session.params` |
| `2026-11-20 04:30:40` | `cowrie.log.closed` |
| `2026-11-20 04:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]252` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e140fa708f9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]78` |
| **First Seen** | 2026-11-20 04:35 |
| **Last Seen** | 2026-11-20 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-11-20 04:35:34` | `cowrie.session.connect` |
| `2026-11-20 04:35:35` | `cowrie.login.success` |
| `2026-11-20 04:35:35` | `cowrie.session.params` |
| `2026-11-20 04:35:36` | `cowrie.log.closed` |
| `2026-11-20 04:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]78` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### Additional priority cases (300) — compact view

| Case | Severity | Source IP | First Seen | Auth | Cmds | DL | TTPs |
|---|---|---|---|---|---|---|---|
| IR-7747264b42b7 | HIGH | `23.132.164[.]185` | 2026-11-20 05:20 | Y | 1 | 0 | `T1078 · T1592` |
| IR-0ee8f64bf208 | HIGH | `200.77.172[.]159` | 2026-11-20 05:30 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-87e834370e36 | HIGH | `200.77.172[.]159` | 2026-11-20 05:30 | Y | 0 | 0 | `T1078 · T1592` |
| IR-50b254a2b8c7 | HIGH | `54.38.109[.]115` | 2026-11-20 05:32 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d40f2ca9edba | HIGH | `54.38.109[.]115` | 2026-11-20 05:32 | Y | 0 | 0 | `T1078 · T1592` |
| IR-573a3890c431 | HIGH | `35.214.207[.]68` | 2026-11-20 05:34 | Y | 0 | 0 | `T1078 · T1592` |
| IR-0d28ed4c37e5 | HIGH | `193.32.162[.]15` | 2026-11-20 05:36 | Y | 0 | 0 | `T1078 · T1592` |
| IR-2494d9935366 | HIGH | `35.214.136[.]216` | 2026-11-20 05:53 | Y | 3 | 0 | `T1078` |
| IR-d0f37b4d1647 | HIGH | `103.155.47[.]50` | 2026-11-20 05:53 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-390f0f52355d | HIGH | `103.155.47[.]50` | 2026-11-20 05:53 | Y | 0 | 0 | `T1078 · T1592` |
| IR-1cd33afaeb3f | HIGH | `45.121.25[.]115` | 2026-11-20 05:57 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-6177a91cacf0 | HIGH | `45.121.25[.]115` | 2026-11-20 05:57 | Y | 0 | 0 | `T1078 · T1592` |
| IR-6d6b19abfbae | HIGH | `169.128.70[.]53` | 2026-11-20 05:59 | Y | 4 | 0 | `T1078 · T1083` |
| IR-d3a3334d758a | HIGH | `78.135.111[.]47` | 2026-11-20 05:59 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-d3092141e8ed | HIGH | `78.135.111[.]47` | 2026-11-20 05:59 | Y | 0 | 0 | `T1078 · T1592` |
| IR-f48eca1e5462 | HIGH | `77.90.185[.]29` | 2026-11-20 06:00 | Y | 0 | 0 | `T1078 · T1592` |
| IR-732bfeab4ec0 | HIGH | `80.94.95[.]118` | 2026-11-20 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-9af262b38362 | HIGH | `78.128.112[.]74` | 2026-11-20 06:01 | Y | 1 | 0 | `T1078 · T1592` |
| IR-add2061f532f | HIGH | `138.226.239[.]233` | 2026-11-20 06:01 | Y | 0 | 0 | `T1078 · T1592` |
| IR-d419e1bc7a8c | HIGH | `35.214.209[.]95` | 2026-11-20 06:03 | Y | 3 | 0 | `T1078` |
| IR-c70cbfb395c7 | HIGH | `195.178.110[.]78` | 2026-11-20 06:08 | Y | 0 | 0 | `T1078` |
| IR-88440da25217 | HIGH | `35.214.136[.]216` | 2026-11-20 06:27 | Y | 3 | 0 | `T1078` |
| IR-f69a26b4460a | HIGH | `77.239.124[.]252` | 2026-11-20 06:34 | Y | 0 | 0 | `T1078` |
| IR-8a8bf7c7b3aa | HIGH | `176.53.159[.]196` | 2026-11-20 06:39 | Y | 0 | 0 | `T1078 · T1592` |
| IR-da36ddffc8f4 | HIGH | `163.7.5[.]228` | 2026-11-20 06:54 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-3bad6a9e2320 | HIGH | `163.7.5[.]228` | 2026-11-20 06:54 | Y | 0 | 0 | `T1078 · T1592` |
| IR-7b9cdae3e509 | HIGH | `172.191.178[.]196` | 2026-11-20 06:55 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-5b36cab605ee | HIGH | `172.191.178[.]196` | 2026-11-20 06:55 | Y | 0 | 0 | `T1078 · T1592` |
| IR-3034133811c8 | HIGH | `111.33.61[.]254` | 2026-11-20 07:02 | Y | 1 | 0 | `T1078 · T1592` |
| IR-745be0db98de | HIGH | `185.227.152[.]135` | 2026-11-20 07:37 | Y | 2 | 1 | `T1021.004 · T1078 · T1105` |
| IR-52ea6396874d | HIGH | `185.227.152[.]135` | 2026-11-20 07:37 | Y | 0 | 0 | `T1078 · T1592` |
| IR-99dcca42654c | HIGH | `92.118.39[.]71` | 2026-11-20 07:48 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fcd03daca073 | HIGH | `92.118.39[.]71` | 2026-11-20 07:50 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-18407a6a804a | HIGH | `92.118.39[.]71` | 2026-11-20 07:52 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-3e17e31215da | HIGH | `92.118.39[.]71` | 2026-11-20 07:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-30a182e3637e | HIGH | `92.118.39[.]71` | 2026-11-20 07:57 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-24b80577193c | HIGH | `92.118.39[.]71` | 2026-11-20 07:59 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-95ff22ee63b5 | HIGH | `92.118.39[.]71` | 2026-11-20 08:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-72def0fa008b | HIGH | `77.90.185[.]29` | 2026-11-20 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-57b842bd3d65 | HIGH | `80.94.95[.]118` | 2026-11-20 08:04 | Y | 0 | 0 | `T1078 · T1592` |
| IR-bbcdb5bbf724 | HIGH | `138.226.239[.]234` | 2026-11-20 08:06 | Y | 0 | 0 | `T1078 · T1592` |
| IR-87f5e3d3faf9 | HIGH | `92.118.39[.]71` | 2026-11-20 08:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ffd230fda98e | HIGH | `92.118.39[.]71` | 2026-11-20 08:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-36a2a8e82365 | HIGH | `92.118.39[.]71` | 2026-11-20 08:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-9cc2ae1d3226 | HIGH | `77.239.124[.]252` | 2026-11-20 08:12 | Y | 0 | 0 | `T1078` |
| IR-7a849123c9c5 | HIGH | `92.118.39[.]71` | 2026-11-20 08:12 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-85a2eea84465 | HIGH | `92.118.39[.]71` | 2026-11-20 08:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-37e574f5ec3f | HIGH | `92.118.39[.]71` | 2026-11-20 08:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f1e0a251afb5 | HIGH | `92.118.39[.]71` | 2026-11-20 08:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f74e6c24a68 | HIGH | `176.53.159[.]196` | 2026-11-20 08:20 | Y | 0 | 0 | `T1078 · T1592` |
| IR-b60ce71c797a | HIGH | `92.118.39[.]71` | 2026-11-20 08:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-47c240d60e77 | HIGH | `92.118.39[.]71` | 2026-11-20 08:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-d381e07ee36b | HIGH | `92.118.39[.]71` | 2026-11-20 08:25 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b5f54d44e03b | HIGH | `92.118.39[.]71` | 2026-11-20 08:27 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7678a0f377f1 | HIGH | `92.118.39[.]71` | 2026-11-20 08:30 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-a8d1dea2c781 | HIGH | `92.118.39[.]71` | 2026-11-20 08:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ad7b3ffe047c | HIGH | `195.178.110[.]78` | 2026-11-20 08:34 | Y | 0 | 0 | `T1078` |
| IR-1afa040f2b87 | HIGH | `92.118.39[.]71` | 2026-11-20 08:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-86f2c5dd5480 | HIGH | `92.118.39[.]71` | 2026-11-20 08:36 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4327336d4703 | HIGH | `92.118.39[.]71` | 2026-11-20 08:38 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f62b22e5d9b | HIGH | `92.118.39[.]71` | 2026-11-20 08:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-fe4f3c31f359 | HIGH | `92.118.39[.]71` | 2026-11-20 08:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cf8fdfbb9aad | HIGH | `92.118.39[.]71` | 2026-11-20 08:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-4062ca90c0b0 | HIGH | `92.118.39[.]71` | 2026-11-20 08:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-e5c1e41bc2af | HIGH | `92.118.39[.]71` | 2026-11-20 08:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-08971d7805ba | HIGH | `92.118.39[.]71` | 2026-11-20 08:51 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-53473c09e389 | HIGH | `92.118.39[.]71` | 2026-11-20 08:53 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-769aa3212be0 | HIGH | `92.118.39[.]71` | 2026-11-20 08:55 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de323e6ca492 | HIGH | `92.118.39[.]71` | 2026-11-20 08:58 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-27a4b2dcebbb | HIGH | `193.46.255[.]155` | 2026-11-20 08:58 | Y | 0 | 0 | `T1078` |
| IR-11f106cfa1be | HIGH | `92.118.39[.]71` | 2026-11-20 09:00 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-40bdabb17c4a | HIGH | `92.118.39[.]71` | 2026-11-20 09:02 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-37707343d7a7 | HIGH | `92.118.39[.]71` | 2026-11-20 09:04 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ea4968255af1 | HIGH | `92.118.39[.]71` | 2026-11-20 09:06 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-de44b4ae734e | HIGH | `92.118.39[.]71` | 2026-11-20 09:08 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-ec46f3966300 | HIGH | `92.118.39[.]71` | 2026-11-20 09:10 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-43143c26183f | HIGH | `92.118.39[.]71` | 2026-11-20 09:13 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-377c3c8c1d0a | HIGH | `92.118.39[.]71` | 2026-11-20 09:15 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b25c0d71dff3 | HIGH | `92.118.39[.]71` | 2026-11-20 09:17 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-c347ecf84b83 | HIGH | `92.118.39[.]71` | 2026-11-20 09:19 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-bf225446f0b1 | HIGH | `92.118.39[.]71` | 2026-11-20 09:21 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-27026bea6478 | HIGH | `92.118.39[.]71` | 2026-11-20 09:23 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-1e575ea7df7c | HIGH | `92.118.39[.]71` | 2026-11-20 09:26 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-13db13c59d8d | HIGH | `92.118.39[.]71` | 2026-11-20 09:28 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b44d3b909e63 | HIGH | `120.26.176[.]233` | 2026-11-20 09:29 | Y | 1 | 0 | `T1078 · T1592` |
| IR-649200026146 | HIGH | `92.118.39[.]71` | 2026-11-20 09:32 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-5bb4a914e6ec | HIGH | `92.118.39[.]71` | 2026-11-20 09:34 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-cf25cb651380 | HIGH | `92.118.39[.]71` | 2026-11-20 09:37 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-7f6066645184 | HIGH | `92.118.39[.]71` | 2026-11-20 09:39 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-b88a50a50d95 | HIGH | `92.118.39[.]71` | 2026-11-20 09:41 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f1f4d822f560 | HIGH | `45.156.128[.]68` | 2026-11-20 09:42 | Y | 3 | 0 | `T1078` |
| IR-245c295f7a43 | HIGH | `156.236.74[.]136` | 2026-11-20 09:42 | Y | 1 | 0 | `T1078 · T1592` |
| IR-e3d7d833482b | HIGH | `92.118.39[.]71` | 2026-11-20 09:43 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-0c3941ff0a81 | HIGH | `194.147.58[.]39` | 2026-11-20 09:44 | Y | 4 | 0 | `T1078 · T1083` |
| IR-fa014cffd533 | HIGH | `92.118.39[.]71` | 2026-11-20 09:45 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-f5753a304491 | HIGH | `92.118.39[.]71` | 2026-11-20 09:47 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-8ca78ff94060 | HIGH | `92.118.39[.]71` | 2026-11-20 09:49 | Y | 42 | 0 | `T1059.004 · T1078 · T1592` |
| IR-584075e60b9f | HIGH | `77.239.124[.]252` | 2026-11-20 10:02 | Y | 0 | 0 | `T1078` |
| IR-5b3c8b5a8895 | HIGH | `193.32.162[.]15` | 2026-11-20 10:03 | Y | 0 | 0 | `T1078 · T1592` |
| IR-801fc75fa870 | HIGH | `160.119.66[.]206` | 2026-11-20 10:03 | Y | 6 | 3 | `T1059.004 · T1078 · T1105` |
_… 200 more priority case(s) in ir_cases.json_

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `195.178.110[.]78` | **3** | 2026-11-20 03:24 | 2026-11-20 06:08 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **3** | 2026-11-20 06:34 | 2026-11-20 10:02 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `77.239.124[.]252` | **3** | 2026-11-20 12:38 | 2026-11-20 16:05 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `109.160.32[.]200` | **2** | 2026-11-20 03:51 | 2026-11-20 05:21 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-20 08:34 | 2026-11-20 10:06 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-20 12:55 | 2026-11-20 14:13 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `195.178.110[.]78` | **2** | 2026-11-20 16:32 | 2026-11-20 18:01 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `210.208.110[.]4` | **2** | 2026-11-20 17:19 | 2026-11-20 18:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.214.136[.]216` | **2** | 2026-11-20 05:52 | 2026-11-20 06:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.32.92[.]140` | **2** | 2026-11-20 03:01 | 2026-11-20 04:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-20 10:50 | 2026-11-20 12:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | **2** | 2026-11-20 15:03 | 2026-11-20 16:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | **2** | 2026-11-20 03:27 | 2026-11-20 04:30 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `92.118.39[.]63` | **2** | 2026-11-20 15:34 | 2026-11-20 16:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-11-20 07:42 | 2026-11-20 08:02 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.171.24[.]29` | 1 | 2026-11-20 08:06 | 2026-11-20 08:06 | 24s | 0 | `T1592` | 🟢 LOW |
| `108.59.221[.]60` | 1 | 2026-11-20 12:30 | 2026-11-20 12:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]109` | 1 | 2026-11-20 18:09 | 2026-11-20 18:09 | 8s | 0 | `T1592` | 🟢 LOW |
| `109.160.32[.]161` | 1 | 2026-11-20 04:23 | 2026-11-20 04:23 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.33.61[.]254` | 1 | 2026-11-20 07:02 | 2026-11-20 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-20 06:31 | 2026-11-20 06:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.33.71[.]238` | 1 | 2026-11-20 10:28 | 2026-11-20 10:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.26.176[.]233` | 1 | 2026-11-20 09:29 | 2026-11-20 09:29 | 1s | 0 | `T1592` | 🟢 LOW |
| `121.181.38[.]96` | 1 | 2026-11-20 05:53 | 2026-11-20 05:53 | 17s | 0 | `T1592` | 🟢 LOW |
| `123.57.94[.]58` | 1 | 2026-11-20 11:43 | 2026-11-20 11:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-20 03:50 | 2026-11-20 03:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-20 08:22 | 2026-11-20 08:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `137.184.5[.]188` | 1 | 2026-11-20 12:21 | 2026-11-20 12:21 | 11s | 0 | `T1592` | 🟢 LOW |
| `14.46.100[.]121` | 1 | 2026-11-20 06:53 | 2026-11-20 06:53 | 20s | 0 | `T1592` | 🟢 LOW |
| `142.93.96[.]190` | 1 | 2026-11-20 10:18 | 2026-11-20 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `143.198.208[.]150` | 1 | 2026-11-20 10:12 | 2026-11-20 10:13 | 36s | 0 | `T1592` | 🟢 LOW |
| `152.32.197[.]166` | 1 | 2026-11-20 18:52 | 2026-11-20 18:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `156.236.74[.]136` | 1 | 2026-11-20 09:42 | 2026-11-20 09:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `157.230.126[.]70` | 1 | 2026-11-20 10:18 | 2026-11-20 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.92.129[.]167` | 1 | 2026-11-20 10:18 | 2026-11-20 10:18 | 20s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-20 05:59 | 2026-11-20 05:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-20 13:23 | 2026-11-20 13:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `169.128.70[.]53` | 1 | 2026-11-20 18:17 | 2026-11-20 18:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `170.150.156[.]20` | 1 | 2026-11-20 07:16 | 2026-11-20 07:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `173.48.231[.]252` | 1 | 2026-11-20 09:54 | 2026-11-20 09:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.149.215[.]44` | 1 | 2026-11-20 09:09 | 2026-11-20 09:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `177.242.137[.]118` | 1 | 2026-11-20 12:18 | 2026-11-20 12:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.236.132[.]185` | 1 | 2026-11-20 16:49 | 2026-11-20 16:50 | 21s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]73` | 1 | 2026-11-20 06:00 | 2026-11-20 06:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.97.242[.]200` | 1 | 2026-11-20 14:46 | 2026-11-20 14:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.97.242[.]202` | 1 | 2026-11-20 14:46 | 2026-11-20 14:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-11-20 03:34 | 2026-11-20 03:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-20 05:36 | 2026-11-20 05:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-20 10:03 | 2026-11-20 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]15` | 1 | 2026-11-20 16:33 | 2026-11-20 16:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.46.255[.]155` | 1 | 2026-11-20 03:00 | 2026-11-20 03:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `194.147.58[.]39` | 1 | 2026-11-20 09:44 | 2026-11-20 09:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | 1 | 2026-11-20 13:07 | 2026-11-20 13:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]18` | 1 | 2026-11-20 05:33 | 2026-11-20 05:33 | 1s | 0 | `T1592` | 🟢 LOW |
| `20.163.3[.]122` | 1 | 2026-11-20 05:13 | 2026-11-20 05:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.169.85[.]54` | 1 | 2026-11-20 16:07 | 2026-11-20 16:07 | 9s | 0 | `T1592` | 🟢 LOW |
| `201.79.94[.]103` | 1 | 2026-11-20 10:17 | 2026-11-20 10:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.248.0[.]34` | 1 | 2026-11-20 09:58 | 2026-11-20 09:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.61.59[.]5` | 1 | 2026-11-20 12:05 | 2026-11-20 12:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.190.96[.]11` | 1 | 2026-11-20 18:21 | 2026-11-20 18:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `220.93.200[.]5` | 1 | 2026-11-20 09:31 | 2026-11-20 09:31 | 18s | 0 | `T1592` | 🟢 LOW |
| `221.152.136[.]35` | 1 | 2026-11-20 11:30 | 2026-11-20 11:30 | 27s | 0 | `T1592` | 🟢 LOW |
| `23.132.164[.]185` | 1 | 2026-11-20 05:20 | 2026-11-20 05:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | 1 | 2026-11-20 05:26 | 2026-11-20 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.15.179[.]241` | 1 | 2026-11-20 10:09 | 2026-11-20 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.1.224[.]172` | 1 | 2026-11-20 04:08 | 2026-11-20 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.1.233[.]70` | 1 | 2026-11-20 04:06 | 2026-11-20 04:06 | 4s | 0 | `T1592` | 🟢 LOW |
| `34.1.235[.]134` | 1 | 2026-11-20 05:40 | 2026-11-20 05:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.187.231[.]181` | 1 | 2026-11-20 12:39 | 2026-11-20 12:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.214.207[.]68` | 1 | 2026-11-20 05:34 | 2026-11-20 05:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `35.214.209[.]95` | 1 | 2026-11-20 06:03 | 2026-11-20 06:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `4.150.203[.]30` | 1 | 2026-11-20 13:17 | 2026-11-20 13:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]61` | 1 | 2026-11-20 18:30 | 2026-11-20 18:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]66` | 1 | 2026-11-20 09:42 | 2026-11-20 09:42 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]68` | 1 | 2026-11-20 09:43 | 2026-11-20 09:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]69` | 1 | 2026-11-20 09:43 | 2026-11-20 09:43 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.33.80[.]243` | 1 | 2026-11-20 13:08 | 2026-11-20 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-11-20 07:49 | 2026-11-20 07:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.98.62[.]166` | 1 | 2026-11-20 04:36 | 2026-11-20 04:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | 1 | 2026-11-20 11:08 | 2026-11-20 11:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]219` | 1 | 2026-11-20 10:07 | 2026-11-20 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.226.68[.]51` | 1 | 2026-11-20 10:18 | 2026-11-20 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-11-20 05:06 | 2026-11-20 05:06 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]39` | 1 | 2026-11-20 03:53 | 2026-11-20 03:53 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]48` | 1 | 2026-11-20 04:42 | 2026-11-20 04:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]142` | 1 | 2026-11-20 04:13 | 2026-11-20 04:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.159[.]18` | 1 | 2026-11-20 05:32 | 2026-11-20 05:33 | 14s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]32` | 1 | 2026-11-20 11:33 | 2026-11-20 11:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]204` | 1 | 2026-11-20 05:33 | 2026-11-20 05:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]44` | 1 | 2026-11-20 14:15 | 2026-11-20 14:16 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]64` | 1 | 2026-11-20 05:32 | 2026-11-20 05:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]130` | 1 | 2026-11-20 11:11 | 2026-11-20 11:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `73.116.146[.]186` | 1 | 2026-11-20 08:05 | 2026-11-20 08:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.108.251[.]51` | 1 | 2026-11-20 06:14 | 2026-11-20 06:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-20 08:20 | 2026-11-20 08:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-11-20 12:01 | 2026-11-20 12:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]132` | 1 | 2026-11-20 08:31 | 2026-11-20 08:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]252` | 1 | 2026-11-20 18:23 | 2026-11-20 18:23 | 1s | 1 | `T1110.001` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-20 06:01 | 2026-11-20 06:01 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-20 10:34 | 2026-11-20 10:34 | 6s | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | 1 | 2026-11-20 15:07 | 2026-11-20 15:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.124.56[.]242` | 1 | 2026-11-20 03:32 | 2026-11-20 03:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.219.222[.]66` | 1 | 2026-11-20 03:53 | 2026-11-20 03:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]53` | 1 | 2026-11-20 06:15 | 2026-11-20 06:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.38.187[.]154` | 1 | 2026-11-20 17:09 | 2026-11-20 17:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.222.77[.]1` | 1 | 2026-11-20 11:07 | 2026-11-20 11:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.115.71[.]93` | 1 | 2026-11-20 12:37 | 2026-11-20 12:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.158.115[.]115` | 1 | 2026-11-20 14:37 | 2026-11-20 14:37 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `0056cc09cf81211b753d79839e3399935a2aa6dd0217232a294f3953b9a7fc26` | ELF Binary (Linux executable) (AArch64 64-bit) | `0056cc09cf81211b...` | 30/100 | 🟢 LOW | **2/75** 🔴 |
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `026cc4f630776e0c9d42905bf3e9b048fda4da68d58c66e4a2e5bb3d8a9d787c` | ELF Binary (Linux executable) (x86-64 64-bit) | `026cc4f630776e0c...` | 31/100 | 🟢 LOW | **4/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` | Shell Script | `0583d9e18684b629...` | 70/100 | 🔴 HIGH | **2/75** 🔴 |
| `05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `05af569c3595b01e...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `0886e17b38d09ef7b0855a2394dd33454939edb3f33a43096c93e0dccfe6a81c` | ELF Binary (Linux executable) (x86-64 64-bit) | `0886e17b38d09ef7...` | 34/100 | 🟢 LOW | **10/75** 🔴 |
| `094d2147548839ba5ed36d884983aaf14bd7ae650095dec96a1cf537d3b23b48` | ELF Binary (Linux executable) (x86-64 64-bit) | `094d2147548839ba...` | 45/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0c99433c7d433d65ab890dcee20b330f262379d532bc76f91e18f09ecfa5fb54` | Shell Script | `0c99433c7d433d65...` | 30/100 | 🟢 LOW | 0/75 ✅ |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0de787cffbec4dcc42e0ecd9491795c7dfe8fe4a955cb67a87544d5c36070982` | ELF Binary (Linux executable) (x86-64 64-bit) | `0de787cffbec4dcc...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` | Bash Script | `0fad00ddec16b67f...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `107a9bfb3d0bb71a33ae17a9eac844a7a7562270a09b5ccce608a78316df0222` | ELF Binary (Linux executable) (x86 32-bit) | `107a9bfb3d0bb71a...` | 35/100 | 🟢 LOW | **13/75** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16254f69dc7011bdd51beb489af5e9825959e4098e565332da99f8cb58b7a76e` | ELF Binary (Linux executable) (x86 32-bit) | `16254f69dc7011bd...` | 30/100 | 🟢 LOW | **1/75** 🔴 |
| `163cb287fd8f81c13901eb4ddaea2db326213f4d2095e0e64321b9afd8300480` | ELF Binary (Linux executable) (x86 32-bit) | `163cb287fd8f81c1...` | 36/100 | 🟢 LOW | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `187b67e5e2116293144f4009b1f224ed09eea924dd4ade00741a66792a63b45a` | ELF Binary (Linux executable) (x86-64 64-bit) | `187b67e5e2116293...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` | ELF Binary (Linux executable) (MIPS 32-bit) | `1913ed2ad175632b...` | 86/100 | 🔴 HIGH | **42/75** 🔴 |
| `1946ee7ec655de32199ce87390699db1e18d80438bdf01f3b813a929e5cce4e6` | ELF Binary (Linux executable) (MIPS 32-bit) | `1946ee7ec655de32...` | 58/100 | 🟡 MEDIUM | **45/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `19e78c00d07f011fcb708ffb12f8dd2fd0f1e57faaf21129b53c7f68ae611e60` | ELF Binary (Linux executable) (x86-64 64-bit) | `19e78c00d07f011f...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1c847d3bd3ef4bf7e21a7091f1479e0e2ca432585ebea996653845b9adfb150e` | ELF Binary (Linux executable) (x86-64 64-bit) | `1c847d3bd3ef4bf7...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e5e56d2ffc990b1dd966e12a02d89d7dcad92c2f23c34834fbfa8c792d56520` | Unknown binary | `1e5e56d2ffc990b1...` | 22/100 | 🟢 LOW | **30/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ec20680994f17b88492809aa5d135fb463c04ec5868639c5515126e2149a240` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ec20680994f17b8...` | 34/100 | 🟢 LOW | **10/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`0583d9e18684b6297a1219d34dd99c1045658f58c3e9a74ca060d8499a5a0439` (0583d9e18684b6297a1219d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Hardware recon` — `cat /proc/cpuinfo`

_`05af569c3595b01e0724bc96c989105467952fd22a8681a716cfa22ec070d78c` (05af569c3595b01e0724bc96...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/.kworker`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.161[.]96:55487`

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`0fad00ddec16b67f3131aa4efffbe32d78fca178407895920b7549667d7bbfbf` (0fad00ddec16b67f3131aa4e...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

_`183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` (183fb8e38eeb1160f392f6d3...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `chmod +x (make executable)` — `chmod +x`

_`1913ed2ad175632b1b75e99bf5e291f551302b16dea51df318379e77a36f1ce9` (1913ed2ad175632b1b75e99b...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`
- `Crypto miner binary` — `xmrig`

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `78.128.112[.]74` | BG | Lir.bg EOOD | **100** ⚠️ | 50 |
| `111.33.61[.]254` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `142.93.96[.]190` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `123.57.94[.]58` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `169.128.70[.]53` | US | Fusiora Hosting | **100** ⚠️ | 10 |
| `3.15.179[.]241` | US | Amazon Technologies Inc. | **100** ⚠️ | 19 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `175.149.215[.]44` | CN | CHINA UNICOM Liaoning province network | **100** ⚠️ | 0 |
| `178.253.95[.]34` | SY | Tarassul Inetnet Service Provider | **100** ⚠️ | 21 |
| `34.1.224[.]172` | NL | Google LLC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 339 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 321 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 165 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |

---

## 🔕 False Positive Summary (84 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| AbuseIPDB score 11 below threshold 25 | 4 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 6 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 6 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 8 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 535 cases |
| Tool 34  | Credential Extractor        | ✅ 3613 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 28 fingerprints |
| Tool 36  | Command Clustering          | ✅ 188 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 194 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 84 filtered (15.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 96 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 39 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 325 priority case(s) shown individually · 108 recon entry/entries in table (15 group(s) consolidating 33 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-11-20T19:27:52Z_

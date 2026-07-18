# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-18 |
| **Generated At** | 2026-07-18T17:02:21Z |
| **Shift Time** | 17:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **137** |
| Confirmed Threats | **113** |
| False Positives Filtered | **24** (17.5%) |
| Unique Attacker IPs | **86** |
| Countries of Origin | **25** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **71** |
| Malware Samples Analyzed | **2** HIGH · **32** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **88** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **17** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **75** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `admin` | 13 |
| `support` | 10 |
| `default` | 5 |
| `solana` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 8 |
| `123456` | 4 |
| `777777` | 4 |
| `0l0ctyQh243O63uD` | 4 |
| `LeitboGi0ro` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `support` | `777777` | 4 |
| `admin` | `0l0ctyQh243O63uD` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `user1` | `test` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `admin` | `43.110.37.217` | 2026-07-18T14:55:49 |
| `admin` | `8888` | `10.0.0.73` | 2026-07-18T14:56:45 |
| `sales` | `123456` | `185.242.3.195` | 2026-07-18T14:58:36 |
| `unknown` | `12345` | `59.95.139.4` | 2026-07-18T15:01:17 |
| `unknown` | `12345` | `182.75.197.174` | 2026-07-18T15:01:27 |
| `root` | `!QAZ2wsx#EDC` | `61.169.54.150` | 2026-07-18T15:02:03 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-18T15:04:48 |
| `root` | `!QAZ2wsx#EDC` | `10.0.0.73` | 2026-07-18T15:05:54 |
| `Admin` | `Password1` | `122.186.249.6` | 2026-07-18T15:06:38 |
| `Admin` | `Password1` | `182.53.55.252` | 2026-07-18T15:06:48 |
| `ubnt` | `ubnt3` | `192.34.128.202` | 2026-07-18T15:21:48 |
| `default` | `default123` | `111.70.32.8` | 2026-07-18T15:22:50 |
| `default` | `default123` | `218.29.196.162` | 2026-07-18T15:22:59 |
| `sales` | `123456` | `10.0.0.73` | 2026-07-18T15:24:24 |
| `support` | `777777` | `195.222.57.183` | 2026-07-18T15:28:23 |
| `admin` | `0l0ctyQh243O63uD` | `64.72.74.162` | 2026-07-18T15:30:47 |
| `admin` | `0l0ctyQh243O63uD` | `219.248.65.30` | 2026-07-18T15:30:59 |
| `admin` | `0l0ctyQh243O63uD` | `10.0.0.73` | 2026-07-18T15:31:11 |
| `support` | `777777` | `81.214.75.248` | 2026-07-18T15:31:50 |
| `support` | `777777` | `103.67.152.201` | 2026-07-18T15:31:59 |
| `support` | `777777` | `10.0.0.73` | 2026-07-18T15:32:22 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-18T15:36:32 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-18T15:36:34 |
| `support` | `123456789` | `82.193.122.91` | 2026-07-18T15:43:19 |
| `root` | `﻿------fuck------` | `118.145.240.6` | 2026-07-18T15:44:02 |
| `support` | `123456789` | `65.20.143.45` | 2026-07-18T15:47:03 |
| `support` | `123456789` | `153.37.177.219` | 2026-07-18T15:47:16 |
| `root` | `root2011` | `10.0.0.73` | 2026-07-18T15:50:08 |
| `root` | `Indya123` | `185.242.3.195` | 2026-07-18T15:52:17 |
| `user` | `admin` | `186.239.41.74` | 2026-07-18T15:52:38 |
| `user` | `admin` | `10.0.0.73` | 2026-07-18T15:56:31 |
| `admin` | `444444` | `181.212.174.164` | 2026-07-18T15:57:05 |
| `admin` | `444444` | `46.101.9.55` | 2026-07-18T15:57:12 |
| `supervisor` | `supervisor2014` | `103.174.80.40` | 2026-07-18T16:15:04 |
| `supervisor` | `supervisor2014` | `83.239.84.130` | 2026-07-18T16:15:16 |
| `root` | `Indya123` | `10.0.0.73` | 2026-07-18T16:17:51 |
| `user1` | `test` | `92.84.21.186` | 2026-07-18T16:18:51 |
| `video` | `video` | `112.26.99.93` | 2026-07-18T16:21:24 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-18T16:21:28 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-18T16:21:28 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-18T16:21:32 |
| `video` | `video` | `180.188.253.150` | 2026-07-18T16:21:37 |
| `video` | `video` | `10.0.0.73` | 2026-07-18T16:21:48 |
| `user1` | `test` | `196.189.124.229` | 2026-07-18T16:22:17 |
| `user1` | `test` | `179.184.85.167` | 2026-07-18T16:22:24 |
| `user1` | `test` | `10.0.0.73` | 2026-07-18T16:22:41 |
| `ts3` | `ts3` | `220.132.170.64` | 2026-07-18T16:33:51 |
| `ts3` | `ts3` | `211.22.222.251` | 2026-07-18T16:34:01 |
| `root` | `111111` | `80.94.92.234` | 2026-07-18T16:34:18 |
| `default` | `password` | `59.93.36.136` | 2026-07-18T16:35:15 |
| `sol` | `sol` | `45.148.10.183` | 2026-07-18T16:36:33 |
| `root` | `123` | `80.94.92.234` | 2026-07-18T16:36:47 |
| `ts3` | `ts3` | `43.248.213.232` | 2026-07-18T16:37:18 |
| `default` | `password` | `85.105.2.51` | 2026-07-18T16:38:19 |
| `default` | `password` | `10.0.0.73` | 2026-07-18T16:38:48 |
| `solana` | `solana` | `45.148.10.183` | 2026-07-18T16:38:53 |
| `root` | `123123` | `80.94.92.234` | 2026-07-18T16:39:31 |
| `solana` | `1234` | `45.148.10.183` | 2026-07-18T16:41:10 |
| `root` | `123321` | `80.94.92.234` | 2026-07-18T16:42:15 |
| `sol` | `1234` | `45.148.10.183` | 2026-07-18T16:43:23 |
| `root` | `1234` | `80.94.92.234` | 2026-07-18T16:44:50 |
| `sol` | `123` | `45.148.10.183` | 2026-07-18T16:45:29 |
| `pruebas` | `pruebas` | `185.242.3.195` | 2026-07-18T16:45:48 |
| `User` | `1` | `122.187.147.13` | 2026-07-18T16:46:14 |
| `User` | `1` | `106.89.50.210` | 2026-07-18T16:46:24 |
| `support` | `support` | `176.53.159.196` | 2026-07-18T16:46:25 |
| `User` | `1` | `10.0.0.73` | 2026-07-18T16:46:37 |
| `root` | `12345` | `80.94.92.234` | 2026-07-18T16:47:31 |
| `sol` | `Solana` | `45.148.10.183` | 2026-07-18T16:47:32 |
| `support` | `test12345` | `183.239.20.236` | 2026-07-18T16:47:33 |
| `support` | `support` | `10.0.0.73` | 2026-07-18T16:47:46 |
| `solana` | `123456789` | `45.148.10.183` | 2026-07-18T16:49:34 |
| `solana` | `12345678` | `45.148.10.183` | 2026-07-18T16:51:37 |
| `root` | `1234567` | `80.94.92.234` | 2026-07-18T16:52:33 |
| `solana` | `1234567` | `45.148.10.183` | 2026-07-18T16:53:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **137** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 36 |
| Go SSH scanner | 26 |
| Paramiko (Python) | 8 |
| libssh | 7 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 36 |
| `16443846184e...` | Generic scanner | 14 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 8 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 36 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 14 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 3 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 7 | 1 | `T1082, T1592, T1078, T1083` |

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una
```
```
uname -s -v -n -m 2 > /dev/null
```
```
/bin/uname -s -v -n -m 2 > /dev/null
```
```
/usr/bin/uname -s -v -n -m 2 > /dev/null
```
```
busybox uname -s -v -n -m 2 > /dev/null
```
Source IPs: `80.94.92.234`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **86** |
| Unique ASNs | **59** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0b4f3f6312cc

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-07-18 14:55 |
| **Last Seen** | 2026-07-18 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 14:55:49` | `cowrie.login.success` |
| `2026-07-18 14:55:50` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f38ab79147

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-18 14:58 |
| **Last Seen** | 2026-07-18 14:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 14:58:36` | `cowrie.session.connect` |
| `2026-07-18 14:58:36` | `cowrie.client.version` |
| `2026-07-18 14:58:36` | `cowrie.client.kex` |
| `2026-07-18 14:58:36` | `cowrie.login.success` |
| `2026-07-18 14:58:37` | `cowrie.session.params` |
| `2026-07-18 14:58:37` | `cowrie.command.input` |
| `2026-07-18 14:58:38` | `cowrie.log.closed` |
| `2026-07-18 14:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-853b44f68371

| Field | Detail |
|---|---|
| **Source IP** | `59.95.139[.]4` |
| **First Seen** | 2026-07-18 15:01 |
| **Last Seen** | 2026-07-18 15:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:01:12` | `cowrie.session.connect` |
| `2026-07-18 15:01:14` | `cowrie.client.version` |
| `2026-07-18 15:01:14` | `cowrie.client.kex` |
| `2026-07-18 15:01:17` | `cowrie.login.success` |
| `2026-07-18 15:01:17` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.95.139[.]4` to AbuseIPDB if not already reported
- [ ] Block `59.95.139[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb6715d970c3

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-18 15:01 |
| **Last Seen** | 2026-07-18 15:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:01:23` | `cowrie.session.connect` |
| `2026-07-18 15:01:25` | `cowrie.client.version` |
| `2026-07-18 15:01:25` | `cowrie.client.kex` |
| `2026-07-18 15:01:27` | `cowrie.login.success` |
| `2026-07-18 15:01:28` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b6ce0094c5

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-07-18 15:02 |
| **Last Seen** | 2026-07-18 15:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:02:00` | `cowrie.session.connect` |
| `2026-07-18 15:02:02` | `cowrie.client.version` |
| `2026-07-18 15:02:02` | `cowrie.client.kex` |
| `2026-07-18 15:02:03` | `cowrie.login.success` |
| `2026-07-18 15:02:04` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dab18266d23

| Field | Detail |
|---|---|
| **Source IP** | `122.186.249[.]6` |
| **First Seen** | 2026-07-18 15:06 |
| **Last Seen** | 2026-07-18 15:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:06:33` | `cowrie.session.connect` |
| `2026-07-18 15:06:35` | `cowrie.client.version` |
| `2026-07-18 15:06:35` | `cowrie.client.kex` |
| `2026-07-18 15:06:38` | `cowrie.login.success` |
| `2026-07-18 15:06:39` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.186.249[.]6` to AbuseIPDB if not already reported
- [ ] Block `122.186.249[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8604ec62e4

| Field | Detail |
|---|---|
| **Source IP** | `182.53.55[.]252` |
| **First Seen** | 2026-07-18 15:06 |
| **Last Seen** | 2026-07-18 15:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:06:45` | `cowrie.session.connect` |
| `2026-07-18 15:06:46` | `cowrie.client.version` |
| `2026-07-18 15:06:46` | `cowrie.client.kex` |
| `2026-07-18 15:06:48` | `cowrie.login.success` |
| `2026-07-18 15:06:49` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.55[.]252` to AbuseIPDB if not already reported
- [ ] Block `182.53.55[.]252` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44377a44acf5

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-18 15:21 |
| **Last Seen** | 2026-07-18 15:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:21:46` | `cowrie.session.connect` |
| `2026-07-18 15:21:47` | `cowrie.client.version` |
| `2026-07-18 15:21:47` | `cowrie.client.kex` |
| `2026-07-18 15:21:48` | `cowrie.login.success` |
| `2026-07-18 15:21:48` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50fb7cc2afa5

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]8` |
| **First Seen** | 2026-07-18 15:22 |
| **Last Seen** | 2026-07-18 15:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:22:47` | `cowrie.session.connect` |
| `2026-07-18 15:22:48` | `cowrie.client.version` |
| `2026-07-18 15:22:48` | `cowrie.client.kex` |
| `2026-07-18 15:22:50` | `cowrie.login.success` |
| `2026-07-18 15:22:50` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]8` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b211d4ebdc

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-07-18 15:22 |
| **Last Seen** | 2026-07-18 15:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:22:55` | `cowrie.session.connect` |
| `2026-07-18 15:22:56` | `cowrie.client.version` |
| `2026-07-18 15:22:56` | `cowrie.client.kex` |
| `2026-07-18 15:22:59` | `cowrie.login.success` |
| `2026-07-18 15:22:59` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbbe20b3d1d

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-07-18 15:28 |
| **Last Seen** | 2026-07-18 15:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:28:21` | `cowrie.session.connect` |
| `2026-07-18 15:28:22` | `cowrie.client.version` |
| `2026-07-18 15:28:22` | `cowrie.client.kex` |
| `2026-07-18 15:28:23` | `cowrie.login.success` |
| `2026-07-18 15:28:23` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d5ceceb529

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-18 15:30 |
| **Last Seen** | 2026-07-18 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:30:23` | `cowrie.session.connect` |
| `2026-07-18 15:30:23` | `cowrie.client.version` |
| `2026-07-18 15:30:23` | `cowrie.client.kex` |
| `2026-07-18 15:30:23` | `cowrie.login.success` |
| `2026-07-18 15:30:24` | `cowrie.session.params` |
| `2026-07-18 15:30:24` | `cowrie.command.input` |
| `2026-07-18 15:30:24` | `cowrie.log.closed` |
| `2026-07-18 15:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819a0b900779

| Field | Detail |
|---|---|
| **Source IP** | `64.72.74[.]162` |
| **First Seen** | 2026-07-18 15:30 |
| **Last Seen** | 2026-07-18 15:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:30:45` | `cowrie.session.connect` |
| `2026-07-18 15:30:46` | `cowrie.client.version` |
| `2026-07-18 15:30:46` | `cowrie.client.kex` |
| `2026-07-18 15:30:47` | `cowrie.login.success` |
| `2026-07-18 15:30:47` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.72.74[.]162` to AbuseIPDB if not already reported
- [ ] Block `64.72.74[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb1bbce7a87

| Field | Detail |
|---|---|
| **Source IP** | `219.248.65[.]30` |
| **First Seen** | 2026-07-18 15:30 |
| **Last Seen** | 2026-07-18 15:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:30:56` | `cowrie.session.connect` |
| `2026-07-18 15:30:57` | `cowrie.client.version` |
| `2026-07-18 15:30:57` | `cowrie.client.kex` |
| `2026-07-18 15:30:59` | `cowrie.login.success` |
| `2026-07-18 15:31:00` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.248.65[.]30` to AbuseIPDB if not already reported
- [ ] Block `219.248.65[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e80bb004d82e

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-07-18 15:31 |
| **Last Seen** | 2026-07-18 15:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:31:48` | `cowrie.session.connect` |
| `2026-07-18 15:31:49` | `cowrie.client.version` |
| `2026-07-18 15:31:49` | `cowrie.client.kex` |
| `2026-07-18 15:31:50` | `cowrie.login.success` |
| `2026-07-18 15:31:50` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f0b2cafe69

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-18 15:31 |
| **Last Seen** | 2026-07-18 15:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:31:55` | `cowrie.session.connect` |
| `2026-07-18 15:31:56` | `cowrie.client.version` |
| `2026-07-18 15:31:56` | `cowrie.client.kex` |
| `2026-07-18 15:31:59` | `cowrie.login.success` |
| `2026-07-18 15:32:00` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b86855d308

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-18 15:36 |
| **Last Seen** | 2026-07-18 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:36:31` | `cowrie.session.connect` |
| `2026-07-18 15:36:31` | `cowrie.client.version` |
| `2026-07-18 15:36:31` | `cowrie.client.kex` |
| `2026-07-18 15:36:32` | `cowrie.login.success` |
| `2026-07-18 15:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21e034b72a3

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-18 15:36 |
| **Last Seen** | 2026-07-18 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:36:33` | `cowrie.session.connect` |
| `2026-07-18 15:36:33` | `cowrie.client.version` |
| `2026-07-18 15:36:33` | `cowrie.client.kex` |
| `2026-07-18 15:36:34` | `cowrie.login.success` |
| `2026-07-18 15:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6587891cf5cc

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-18 15:36 |
| **Last Seen** | 2026-07-18 15:38 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:36:49` | `cowrie.session.connect` |
| `2026-07-18 15:36:49` | `cowrie.client.version` |
| `2026-07-18 15:36:49` | `cowrie.client.kex` |
| `2026-07-18 15:36:50` | `cowrie.login.success` |
| `2026-07-18 15:36:52` | `cowrie.session.file_upload` |
| `2026-07-18 15:36:53` | `cowrie.session.params` |
| `2026-07-18 15:36:53` | `cowrie.command.input` |
| `2026-07-18 15:36:53` | `cowrie.command.input` |
| `2026-07-18 15:36:53` | `cowrie.command.input` |
| `2026-07-18 15:36:53` | `cowrie.command.failed` |
| `2026-07-18 15:36:53` | `cowrie.log.closed` |
| `2026-07-18 15:36:54` | `cowrie.session.params` |
| `2026-07-18 15:36:54` | `cowrie.command.input` |
| `2026-07-18 15:36:54` | `cowrie.log.closed` |
| `2026-07-18 15:36:55` | `cowrie.session.params` |
| `2026-07-18 15:36:55` | `cowrie.command.input` |
| `2026-07-18 15:36:55` | `cowrie.log.closed` |
| `2026-07-18 15:36:57` | `cowrie.session.params` |
| `2026-07-18 15:36:57` | `cowrie.command.input` |
| `2026-07-18 15:36:57` | `cowrie.command.failed` |
| `2026-07-18 15:36:57` | `cowrie.command.failed` |
| `2026-07-18 15:37:58` | `cowrie.session.params` |
| `2026-07-18 15:37:58` | `cowrie.command.input` |
| `2026-07-18 15:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f1b22f819e

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-18 15:39 |
| **Last Seen** | 2026-07-18 15:41 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:39:24` | `cowrie.session.connect` |
| `2026-07-18 15:39:24` | `cowrie.client.version` |
| `2026-07-18 15:39:24` | `cowrie.client.kex` |
| `2026-07-18 15:39:25` | `cowrie.login.success` |
| `2026-07-18 15:39:27` | `cowrie.session.file_upload` |
| `2026-07-18 15:39:28` | `cowrie.session.params` |
| `2026-07-18 15:39:28` | `cowrie.command.input` |
| `2026-07-18 15:39:28` | `cowrie.command.input` |
| `2026-07-18 15:39:28` | `cowrie.command.input` |
| `2026-07-18 15:39:28` | `cowrie.command.failed` |
| `2026-07-18 15:39:28` | `cowrie.log.closed` |
| `2026-07-18 15:39:29` | `cowrie.session.params` |
| `2026-07-18 15:39:29` | `cowrie.command.input` |
| `2026-07-18 15:39:29` | `cowrie.log.closed` |
| `2026-07-18 15:39:31` | `cowrie.session.params` |
| `2026-07-18 15:39:31` | `cowrie.command.input` |
| `2026-07-18 15:39:31` | `cowrie.log.closed` |
| `2026-07-18 15:39:32` | `cowrie.session.params` |
| `2026-07-18 15:39:32` | `cowrie.command.input` |
| `2026-07-18 15:39:32` | `cowrie.command.failed` |
| `2026-07-18 15:39:32` | `cowrie.command.failed` |
| `2026-07-18 15:40:33` | `cowrie.session.params` |
| `2026-07-18 15:40:33` | `cowrie.command.input` |
| `2026-07-18 15:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585de769333b

| Field | Detail |
|---|---|
| **Source IP** | `82.193.122[.]91` |
| **First Seen** | 2026-07-18 15:43 |
| **Last Seen** | 2026-07-18 15:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:43:18` | `cowrie.session.connect` |
| `2026-07-18 15:43:18` | `cowrie.client.version` |
| `2026-07-18 15:43:18` | `cowrie.client.kex` |
| `2026-07-18 15:43:19` | `cowrie.login.success` |
| `2026-07-18 15:43:19` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.193.122[.]91` to AbuseIPDB if not already reported
- [ ] Block `82.193.122[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4de30e62ca5

| Field | Detail |
|---|---|
| **Source IP** | `118.145.240[.]6` |
| **First Seen** | 2026-07-18 15:44 |
| **Last Seen** | 2026-07-18 15:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:44:00` | `cowrie.session.connect` |
| `2026-07-18 15:44:00` | `cowrie.client.version` |
| `2026-07-18 15:44:01` | `cowrie.client.kex` |
| `2026-07-18 15:44:02` | `cowrie.login.success` |
| `2026-07-18 15:44:03` | `cowrie.session.params` |
| `2026-07-18 15:44:03` | `cowrie.command.input` |
| `2026-07-18 15:44:04` | `cowrie.log.closed` |
| `2026-07-18 15:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.240[.]6` to AbuseIPDB if not already reported
- [ ] Block `118.145.240[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2fac4786b2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]45` |
| **First Seen** | 2026-07-18 15:47 |
| **Last Seen** | 2026-07-18 15:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:47:01` | `cowrie.session.connect` |
| `2026-07-18 15:47:01` | `cowrie.client.version` |
| `2026-07-18 15:47:01` | `cowrie.client.kex` |
| `2026-07-18 15:47:03` | `cowrie.login.success` |
| `2026-07-18 15:47:04` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]45` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2abba46ef1

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-18 15:47 |
| **Last Seen** | 2026-07-18 15:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:47:14` | `cowrie.session.connect` |
| `2026-07-18 15:47:14` | `cowrie.client.version` |
| `2026-07-18 15:47:14` | `cowrie.client.kex` |
| `2026-07-18 15:47:16` | `cowrie.login.success` |
| `2026-07-18 15:47:18` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c295ded54280

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-18 15:52 |
| **Last Seen** | 2026-07-18 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:52:16` | `cowrie.session.connect` |
| `2026-07-18 15:52:16` | `cowrie.client.version` |
| `2026-07-18 15:52:16` | `cowrie.client.kex` |
| `2026-07-18 15:52:17` | `cowrie.login.success` |
| `2026-07-18 15:52:18` | `cowrie.session.params` |
| `2026-07-18 15:52:18` | `cowrie.command.input` |
| `2026-07-18 15:52:18` | `cowrie.log.closed` |
| `2026-07-18 15:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f599e04e72

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-07-18 15:52 |
| **Last Seen** | 2026-07-18 15:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:52:36` | `cowrie.session.connect` |
| `2026-07-18 15:52:36` | `cowrie.client.version` |
| `2026-07-18 15:52:36` | `cowrie.client.kex` |
| `2026-07-18 15:52:38` | `cowrie.login.success` |
| `2026-07-18 15:52:39` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ccaa39f9a2f

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-07-18 15:57 |
| **Last Seen** | 2026-07-18 15:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:57:03` | `cowrie.session.connect` |
| `2026-07-18 15:57:04` | `cowrie.client.version` |
| `2026-07-18 15:57:04` | `cowrie.client.kex` |
| `2026-07-18 15:57:05` | `cowrie.login.success` |
| `2026-07-18 15:57:06` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ebcb352ddf6

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-07-18 15:57 |
| **Last Seen** | 2026-07-18 15:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 15:57:11` | `cowrie.session.connect` |
| `2026-07-18 15:57:11` | `cowrie.client.version` |
| `2026-07-18 15:57:11` | `cowrie.client.kex` |
| `2026-07-18 15:57:12` | `cowrie.login.success` |
| `2026-07-18 15:57:12` | `cowrie.direct-tcpip.request` |
| `2026-07-18 15:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e32d7b1512b

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-18 16:15 |
| **Last Seen** | 2026-07-18 16:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:15:01` | `cowrie.session.connect` |
| `2026-07-18 16:15:02` | `cowrie.client.version` |
| `2026-07-18 16:15:02` | `cowrie.client.kex` |
| `2026-07-18 16:15:04` | `cowrie.login.success` |
| `2026-07-18 16:15:05` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fbd2760c84b

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-07-18 16:15 |
| **Last Seen** | 2026-07-18 16:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:15:15` | `cowrie.session.connect` |
| `2026-07-18 16:15:15` | `cowrie.client.version` |
| `2026-07-18 16:15:15` | `cowrie.client.kex` |
| `2026-07-18 16:15:16` | `cowrie.login.success` |
| `2026-07-18 16:15:17` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cce00172eb1

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-18 16:18 |
| **Last Seen** | 2026-07-18 16:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:18:50` | `cowrie.session.connect` |
| `2026-07-18 16:18:50` | `cowrie.client.version` |
| `2026-07-18 16:18:50` | `cowrie.client.kex` |
| `2026-07-18 16:18:51` | `cowrie.login.success` |
| `2026-07-18 16:18:51` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370e2f802611

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-07-18 16:21 |
| **Last Seen** | 2026-07-18 16:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:21:20` | `cowrie.session.connect` |
| `2026-07-18 16:21:21` | `cowrie.client.version` |
| `2026-07-18 16:21:21` | `cowrie.client.kex` |
| `2026-07-18 16:21:24` | `cowrie.login.success` |
| `2026-07-18 16:21:26` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d80aceedbf

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-18 16:21 |
| **Last Seen** | 2026-07-18 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:21:28` | `cowrie.session.connect` |
| `2026-07-18 16:21:28` | `cowrie.client.version` |
| `2026-07-18 16:21:28` | `cowrie.client.kex` |
| `2026-07-18 16:21:28` | `cowrie.login.success` |
| `2026-07-18 16:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248986424de4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-18 16:21 |
| **Last Seen** | 2026-07-18 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:21:28` | `cowrie.session.connect` |
| `2026-07-18 16:21:28` | `cowrie.client.version` |
| `2026-07-18 16:21:28` | `cowrie.client.kex` |
| `2026-07-18 16:21:28` | `cowrie.login.success` |
| `2026-07-18 16:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f28ba11afe6e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-18 16:21 |
| **Last Seen** | 2026-07-18 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:21:32` | `cowrie.session.connect` |
| `2026-07-18 16:21:32` | `cowrie.client.version` |
| `2026-07-18 16:21:32` | `cowrie.client.kex` |
| `2026-07-18 16:21:32` | `cowrie.login.success` |
| `2026-07-18 16:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389b77cae146

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-18 16:21 |
| **Last Seen** | 2026-07-18 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:21:32` | `cowrie.session.connect` |
| `2026-07-18 16:21:32` | `cowrie.client.version` |
| `2026-07-18 16:21:32` | `cowrie.client.kex` |
| `2026-07-18 16:21:32` | `cowrie.login.success` |
| `2026-07-18 16:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-399dda51d48a

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-18 16:21 |
| **Last Seen** | 2026-07-18 16:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:21:32` | `cowrie.session.connect` |
| `2026-07-18 16:21:33` | `cowrie.client.version` |
| `2026-07-18 16:21:33` | `cowrie.client.kex` |
| `2026-07-18 16:21:37` | `cowrie.login.success` |
| `2026-07-18 16:21:38` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bead815789a

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-18 16:22 |
| **Last Seen** | 2026-07-18 16:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:22:14` | `cowrie.session.connect` |
| `2026-07-18 16:22:14` | `cowrie.client.version` |
| `2026-07-18 16:22:14` | `cowrie.client.kex` |
| `2026-07-18 16:22:17` | `cowrie.login.success` |
| `2026-07-18 16:22:17` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a3fcd4465a0

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-18 16:22 |
| **Last Seen** | 2026-07-18 16:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:22:22` | `cowrie.session.connect` |
| `2026-07-18 16:22:23` | `cowrie.client.version` |
| `2026-07-18 16:22:23` | `cowrie.client.kex` |
| `2026-07-18 16:22:24` | `cowrie.login.success` |
| `2026-07-18 16:22:25` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1d01fd7a0c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-18 16:23 |
| **Last Seen** | 2026-07-18 16:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:23:50` | `cowrie.session.connect` |
| `2026-07-18 16:23:50` | `cowrie.client.version` |
| `2026-07-18 16:23:50` | `cowrie.client.kex` |
| `2026-07-18 16:23:52` | `cowrie.login.success` |
| `2026-07-18 16:23:53` | `cowrie.session.params` |
| `2026-07-18 16:23:53` | `cowrie.command.input` |
| `2026-07-18 16:23:54` | `cowrie.log.closed` |
| `2026-07-18 16:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358894307704

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-07-18 16:33 |
| **Last Seen** | 2026-07-18 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:33:48` | `cowrie.session.connect` |
| `2026-07-18 16:33:49` | `cowrie.client.version` |
| `2026-07-18 16:33:49` | `cowrie.client.kex` |
| `2026-07-18 16:33:51` | `cowrie.login.success` |
| `2026-07-18 16:33:52` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bad3790516b

| Field | Detail |
|---|---|
| **Source IP** | `211.22.222[.]251` |
| **First Seen** | 2026-07-18 16:33 |
| **Last Seen** | 2026-07-18 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:33:58` | `cowrie.session.connect` |
| `2026-07-18 16:33:58` | `cowrie.client.version` |
| `2026-07-18 16:33:58` | `cowrie.client.kex` |
| `2026-07-18 16:34:01` | `cowrie.login.success` |
| `2026-07-18 16:34:02` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.222[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.22.222[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ab590516fb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:34 |
| **Last Seen** | 2026-07-18 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:34:14` | `cowrie.session.connect` |
| `2026-07-18 16:34:14` | `cowrie.client.version` |
| `2026-07-18 16:34:14` | `cowrie.client.kex` |
| `2026-07-18 16:34:18` | `cowrie.login.success` |
| `2026-07-18 16:34:20` | `cowrie.session.params` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.success` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:20` | `cowrie.command.input` |
| `2026-07-18 16:34:21` | `cowrie.log.closed` |
| `2026-07-18 16:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3ef02426b9f

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-18 16:35 |
| **Last Seen** | 2026-07-18 16:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:35:12` | `cowrie.session.connect` |
| `2026-07-18 16:35:13` | `cowrie.client.version` |
| `2026-07-18 16:35:13` | `cowrie.client.kex` |
| `2026-07-18 16:35:15` | `cowrie.login.success` |
| `2026-07-18 16:35:16` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b23f557d8f2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:36 |
| **Last Seen** | 2026-07-18 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:36:33` | `cowrie.session.connect` |
| `2026-07-18 16:36:33` | `cowrie.client.version` |
| `2026-07-18 16:36:33` | `cowrie.client.kex` |
| `2026-07-18 16:36:33` | `cowrie.login.success` |
| `2026-07-18 16:36:34` | `cowrie.session.params` |
| `2026-07-18 16:36:34` | `cowrie.command.input` |
| `2026-07-18 16:36:34` | `cowrie.log.closed` |
| `2026-07-18 16:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1402a79261

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:36 |
| **Last Seen** | 2026-07-18 16:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:36:43` | `cowrie.session.connect` |
| `2026-07-18 16:36:44` | `cowrie.client.version` |
| `2026-07-18 16:36:44` | `cowrie.client.kex` |
| `2026-07-18 16:36:47` | `cowrie.login.success` |
| `2026-07-18 16:36:49` | `cowrie.session.params` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.success` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:49` | `cowrie.command.input` |
| `2026-07-18 16:36:50` | `cowrie.log.closed` |
| `2026-07-18 16:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01a596fdc18d

| Field | Detail |
|---|---|
| **Source IP** | `43.248.213[.]232` |
| **First Seen** | 2026-07-18 16:37 |
| **Last Seen** | 2026-07-18 16:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:37:16` | `cowrie.session.connect` |
| `2026-07-18 16:37:17` | `cowrie.client.version` |
| `2026-07-18 16:37:17` | `cowrie.client.kex` |
| `2026-07-18 16:37:18` | `cowrie.login.success` |
| `2026-07-18 16:37:19` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.248.213[.]232` to AbuseIPDB if not already reported
- [ ] Block `43.248.213[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23aad3f98a15

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-07-18 16:38 |
| **Last Seen** | 2026-07-18 16:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:38:18` | `cowrie.session.connect` |
| `2026-07-18 16:38:19` | `cowrie.client.version` |
| `2026-07-18 16:38:19` | `cowrie.client.kex` |
| `2026-07-18 16:38:19` | `cowrie.login.success` |
| `2026-07-18 16:38:19` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560dd4dc391e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:38 |
| **Last Seen** | 2026-07-18 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:38:52` | `cowrie.session.connect` |
| `2026-07-18 16:38:52` | `cowrie.client.version` |
| `2026-07-18 16:38:52` | `cowrie.client.kex` |
| `2026-07-18 16:38:53` | `cowrie.login.success` |
| `2026-07-18 16:38:53` | `cowrie.session.params` |
| `2026-07-18 16:38:53` | `cowrie.command.input` |
| `2026-07-18 16:38:54` | `cowrie.log.closed` |
| `2026-07-18 16:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e8e9d5ad3e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:39 |
| **Last Seen** | 2026-07-18 16:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:39:27` | `cowrie.session.connect` |
| `2026-07-18 16:39:27` | `cowrie.client.version` |
| `2026-07-18 16:39:27` | `cowrie.client.kex` |
| `2026-07-18 16:39:31` | `cowrie.login.success` |
| `2026-07-18 16:39:34` | `cowrie.session.params` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.success` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:34` | `cowrie.command.input` |
| `2026-07-18 16:39:35` | `cowrie.log.closed` |
| `2026-07-18 16:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279e1a3cab47

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:41 |
| **Last Seen** | 2026-07-18 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:41:09` | `cowrie.session.connect` |
| `2026-07-18 16:41:09` | `cowrie.client.version` |
| `2026-07-18 16:41:09` | `cowrie.client.kex` |
| `2026-07-18 16:41:10` | `cowrie.login.success` |
| `2026-07-18 16:41:10` | `cowrie.session.params` |
| `2026-07-18 16:41:10` | `cowrie.command.input` |
| `2026-07-18 16:41:10` | `cowrie.log.closed` |
| `2026-07-18 16:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f58fd93f4e78

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:42 |
| **Last Seen** | 2026-07-18 16:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:42:10` | `cowrie.session.connect` |
| `2026-07-18 16:42:11` | `cowrie.client.version` |
| `2026-07-18 16:42:11` | `cowrie.client.kex` |
| `2026-07-18 16:42:15` | `cowrie.login.success` |
| `2026-07-18 16:42:17` | `cowrie.session.params` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.success` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:17` | `cowrie.command.input` |
| `2026-07-18 16:42:18` | `cowrie.log.closed` |
| `2026-07-18 16:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c6250f3ef8b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:43 |
| **Last Seen** | 2026-07-18 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:43:22` | `cowrie.session.connect` |
| `2026-07-18 16:43:22` | `cowrie.client.version` |
| `2026-07-18 16:43:23` | `cowrie.client.kex` |
| `2026-07-18 16:43:23` | `cowrie.login.success` |
| `2026-07-18 16:43:24` | `cowrie.session.params` |
| `2026-07-18 16:43:24` | `cowrie.command.input` |
| `2026-07-18 16:43:24` | `cowrie.log.closed` |
| `2026-07-18 16:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7dfdb4318a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:44 |
| **Last Seen** | 2026-07-18 16:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:44:46` | `cowrie.session.connect` |
| `2026-07-18 16:44:47` | `cowrie.client.version` |
| `2026-07-18 16:44:47` | `cowrie.client.kex` |
| `2026-07-18 16:44:50` | `cowrie.login.success` |
| `2026-07-18 16:44:53` | `cowrie.session.params` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.success` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:53` | `cowrie.command.input` |
| `2026-07-18 16:44:54` | `cowrie.log.closed` |
| `2026-07-18 16:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd73246d7fee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:45 |
| **Last Seen** | 2026-07-18 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:45:28` | `cowrie.session.connect` |
| `2026-07-18 16:45:28` | `cowrie.client.version` |
| `2026-07-18 16:45:28` | `cowrie.client.kex` |
| `2026-07-18 16:45:29` | `cowrie.login.success` |
| `2026-07-18 16:45:29` | `cowrie.session.params` |
| `2026-07-18 16:45:29` | `cowrie.command.input` |
| `2026-07-18 16:45:29` | `cowrie.log.closed` |
| `2026-07-18 16:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb8b17e2b5d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-18 16:45 |
| **Last Seen** | 2026-07-18 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:45:47` | `cowrie.session.connect` |
| `2026-07-18 16:45:47` | `cowrie.client.version` |
| `2026-07-18 16:45:48` | `cowrie.client.kex` |
| `2026-07-18 16:45:48` | `cowrie.login.success` |
| `2026-07-18 16:45:49` | `cowrie.session.params` |
| `2026-07-18 16:45:49` | `cowrie.command.input` |
| `2026-07-18 16:45:49` | `cowrie.log.closed` |
| `2026-07-18 16:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb19648b4f6b

| Field | Detail |
|---|---|
| **Source IP** | `122.187.147[.]13` |
| **First Seen** | 2026-07-18 16:46 |
| **Last Seen** | 2026-07-18 16:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:46:12` | `cowrie.session.connect` |
| `2026-07-18 16:46:12` | `cowrie.client.version` |
| `2026-07-18 16:46:12` | `cowrie.client.kex` |
| `2026-07-18 16:46:14` | `cowrie.login.success` |
| `2026-07-18 16:46:15` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.147[.]13` to AbuseIPDB if not already reported
- [ ] Block `122.187.147[.]13` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9130a6c052d0

| Field | Detail |
|---|---|
| **Source IP** | `106.89.50[.]210` |
| **First Seen** | 2026-07-18 16:46 |
| **Last Seen** | 2026-07-18 16:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:46:21` | `cowrie.session.connect` |
| `2026-07-18 16:46:21` | `cowrie.client.version` |
| `2026-07-18 16:46:21` | `cowrie.client.kex` |
| `2026-07-18 16:46:24` | `cowrie.login.success` |
| `2026-07-18 16:46:24` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.50[.]210` to AbuseIPDB if not already reported
- [ ] Block `106.89.50[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d12af4835722

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-18 16:46 |
| **Last Seen** | 2026-07-18 16:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:46:24` | `cowrie.session.connect` |
| `2026-07-18 16:46:24` | `cowrie.client.version` |
| `2026-07-18 16:46:24` | `cowrie.client.kex` |
| `2026-07-18 16:46:25` | `cowrie.login.success` |
| `2026-07-18 16:46:25` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:46:25` | `cowrie.direct-tcpip.data` |
| `2026-07-18 16:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f43418328f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:47 |
| **Last Seen** | 2026-07-18 16:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:47:27` | `cowrie.session.connect` |
| `2026-07-18 16:47:27` | `cowrie.client.version` |
| `2026-07-18 16:47:27` | `cowrie.client.kex` |
| `2026-07-18 16:47:31` | `cowrie.login.success` |
| `2026-07-18 16:47:33` | `cowrie.session.params` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.success` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.command.input` |
| `2026-07-18 16:47:34` | `cowrie.log.closed` |
| `2026-07-18 16:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09df9377c62a

| Field | Detail |
|---|---|
| **Source IP** | `183.239.20[.]236` |
| **First Seen** | 2026-07-18 16:47 |
| **Last Seen** | 2026-07-18 16:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:47:29` | `cowrie.session.connect` |
| `2026-07-18 16:47:30` | `cowrie.client.version` |
| `2026-07-18 16:47:30` | `cowrie.client.kex` |
| `2026-07-18 16:47:33` | `cowrie.login.success` |
| `2026-07-18 16:47:34` | `cowrie.direct-tcpip.request` |
| `2026-07-18 16:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.239.20[.]236` to AbuseIPDB if not already reported
- [ ] Block `183.239.20[.]236` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32dd7b2ae469

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:47 |
| **Last Seen** | 2026-07-18 16:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:47:31` | `cowrie.session.connect` |
| `2026-07-18 16:47:31` | `cowrie.client.version` |
| `2026-07-18 16:47:31` | `cowrie.client.kex` |
| `2026-07-18 16:47:32` | `cowrie.login.success` |
| `2026-07-18 16:47:32` | `cowrie.session.params` |
| `2026-07-18 16:47:32` | `cowrie.command.input` |
| `2026-07-18 16:47:33` | `cowrie.log.closed` |
| `2026-07-18 16:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809c83344ed9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:49 |
| **Last Seen** | 2026-07-18 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:49:33` | `cowrie.session.connect` |
| `2026-07-18 16:49:33` | `cowrie.client.version` |
| `2026-07-18 16:49:34` | `cowrie.client.kex` |
| `2026-07-18 16:49:34` | `cowrie.login.success` |
| `2026-07-18 16:49:35` | `cowrie.session.params` |
| `2026-07-18 16:49:35` | `cowrie.command.input` |
| `2026-07-18 16:49:35` | `cowrie.log.closed` |
| `2026-07-18 16:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a598458a687

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:51 |
| **Last Seen** | 2026-07-18 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:51:37` | `cowrie.session.connect` |
| `2026-07-18 16:51:37` | `cowrie.client.version` |
| `2026-07-18 16:51:37` | `cowrie.client.kex` |
| `2026-07-18 16:51:37` | `cowrie.login.success` |
| `2026-07-18 16:51:38` | `cowrie.session.params` |
| `2026-07-18 16:51:38` | `cowrie.command.input` |
| `2026-07-18 16:51:38` | `cowrie.log.closed` |
| `2026-07-18 16:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a400243dc0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-07-18 16:52 |
| **Last Seen** | 2026-07-18 16:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:52:30` | `cowrie.session.connect` |
| `2026-07-18 16:52:30` | `cowrie.client.version` |
| `2026-07-18 16:52:30` | `cowrie.client.kex` |
| `2026-07-18 16:52:33` | `cowrie.login.success` |
| `2026-07-18 16:52:35` | `cowrie.session.params` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.success` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:35` | `cowrie.command.input` |
| `2026-07-18 16:52:36` | `cowrie.log.closed` |
| `2026-07-18 16:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19357132e083

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]183` |
| **First Seen** | 2026-07-18 16:53 |
| **Last Seen** | 2026-07-18 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-18 16:53:42` | `cowrie.session.connect` |
| `2026-07-18 16:53:42` | `cowrie.client.version` |
| `2026-07-18 16:53:43` | `cowrie.client.kex` |
| `2026-07-18 16:53:43` | `cowrie.login.success` |
| `2026-07-18 16:53:44` | `cowrie.session.params` |
| `2026-07-18 16:53:44` | `cowrie.command.input` |
| `2026-07-18 16:53:44` | `cowrie.log.closed` |
| `2026-07-18 16:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]183` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-18 15:07 | 2026-07-18 16:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-18 15:58 | 2026-07-18 15:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]99` | **3** | 2026-07-18 15:51 | 2026-07-18 15:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]112` | **3** | 2026-07-18 15:52 | 2026-07-18 15:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]50` | **3** | 2026-07-18 15:51 | 2026-07-18 15:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-07-18 15:30 | 2026-07-18 15:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.192[.]88` | **2** | 2026-07-18 15:02 | 2026-07-18 15:04 | 2m | 0 | `T1592` | 🟢 LOW |
| `161.35.8[.]0` | **2** | 2026-07-18 14:56 | 2026-07-18 15:04 | 1m | 0 | `T1592` | 🟢 LOW |
| `167.172.172[.]63` | **2** | 2026-07-18 15:19 | 2026-07-18 15:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `4.150.190[.]180` | **2** | 2026-07-18 16:34 | 2026-07-18 16:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-07-18 16:28 | 2026-07-18 16:50 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]234` | 1 | 2026-07-18 15:21 | 2026-07-18 15:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.7.248[.]50` | 1 | 2026-07-18 16:11 | 2026-07-18 16:11 | 5s | 0 | `T1592` | 🟢 LOW |
| `118.145.240[.]6` | 1 | 2026-07-18 15:43 | 2026-07-18 15:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.52.92[.]197` | 1 | 2026-07-18 15:55 | 2026-07-18 15:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-07-18 16:47 | 2026-07-18 16:47 | 14s | 0 | `T1592` | 🟢 LOW |
| `171.217.70[.]151` | 1 | 2026-07-18 15:49 | 2026-07-18 15:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-07-18 16:38 | 2026-07-18 16:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-07-18 14:59 | 2026-07-18 15:00 | 55s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | 1 | 2026-07-18 14:55 | 2026-07-18 14:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-07-18 15:34 | 2026-07-18 15:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-07-18 15:28 | 2026-07-18 15:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `23.95.122[.]93` | 1 | 2026-07-18 16:41 | 2026-07-18 16:42 | 42s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-07-18 16:05 | 2026-07-18 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]183` | 1 | 2026-07-18 16:33 | 2026-07-18 16:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-18 16:10 | 2026-07-18 16:12 | 96s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-07-18 16:48 | 2026-07-18 16:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-18 16:11 | 2026-07-18 16:13 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 37/100 | 🟢 LOW | **18/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59b756899825573563cd53ae62bcd1f703a765f85797c352964e5246f04a85c0` | ELF Binary (Linux executable) (MIPS 32-bit) | `59b7568998255735...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5ea3509f840f6cc8b36e4930c7f6514253c3be358c7f83683c021d51fe6a2b97` | ELF Binary (Linux executable) (x86 32-bit) | `5ea3509f840f6cc8...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` (09591253a95411d60c2b0d53...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

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
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `121.66.63[.]186` | KR | LG Uplus | **100** ⚠️ | 50 |
| `211.22.222[.]251` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `61.169.54[.]150` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `59.93.36[.]136` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `203.110.233[.]225` | CN | CHINANET FUJIAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `192.34.128[.]202` | US | Zito Media | **100** ⚠️ | 50 |
| `83.239.84[.]130` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `182.75.197[.]174` | IN | Devbhumi Broadcast Pvt Ltd | **100** ⚠️ | 50 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 79 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 7 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 7 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 137 cases |
| Tool 34  | Credential Extractor        | ✅ 88 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 86 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (17.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 32 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 28 recon entry/entries in table (11 group(s) consolidating 30 session(s)).

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
_Report time: 2026-07-18T17:02:21Z_

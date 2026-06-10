# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-10 |
| **Generated At** | 2026-06-10T15:46:45Z |
| **Shift Time** | 15:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222f |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1146** |
| Confirmed Threats | **1103** |
| False Positives Filtered | **43** (3.8%) |
| Unique Attacker IPs | **52** |
| Countries of Origin | **21** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1078** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **69** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **25** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **62** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `admin` | 6 |
| `ubuntu` | 6 |
| `sol` | 6 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `LeitboGi0ro` | 7 |
| `admin` | 7 |
| `123@@@` | 6 |
| `smo@@kkklss` | 4 |
| `﻿------fuck------` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 7 |
| `root` | `123@@@` | 6 |
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `﻿------fuck------` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `caiden` | `caiden` | `213.209.159.56` | 2026-06-10T09:03:54 |
| `user` | `jobs` | `2.57.121.25` | 2026-06-10T09:21:52 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-10T09:27:25 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-10T09:27:25 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-10T09:29:34 |
| `root` | `LeitboGi0ro` | `138.2.98.41` | 2026-06-10T09:30:27 |
| `root` | `123@@@` | `138.2.98.41` | 2026-06-10T09:30:27 |
| `ftp` | `ftp` | `2.57.121.112` | 2026-06-10T09:36:28 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-10T09:41:16 |
| `alannah` | `alannah` | `213.209.159.56` | 2026-06-10T10:12:03 |
| `root` | `﻿------fuck------` | `42.49.97.250` | 2026-06-10T10:21:07 |
| `user` | `jerrys` | `2.57.121.25` | 2026-06-10T10:35:50 |
| `guest` | `guest` | `2.57.121.112` | 2026-06-10T10:50:42 |
| `ananda` | `ananda` | `213.209.159.56` | 2026-06-10T11:19:48 |
| `admin` | `admin` | `202.60.229.130` | 2026-06-10T11:27:15 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-10T11:27:31 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-10T11:35:42 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-10T11:35:42 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-10T11:35:50 |
| `root` | `---fuck_you----` | `183.129.249.4` | 2026-06-10T11:48:42 |
| `user` | `jazzy1` | `2.57.121.25` | 2026-06-10T11:49:57 |
| `oracle` | `oracle` | `2.57.121.112` | 2026-06-10T12:05:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.172` | 2026-06-10T12:10:07 |
| `root` | `admin` | `83.177.240.110` | 2026-06-10T12:11:25 |
| `madelin` | `madelin` | `213.209.159.56` | 2026-06-10T12:26:52 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-10T12:51:12 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-10T12:51:52 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-10T12:51:52 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-10T12:52:01 |
| `user` | `islands` | `2.57.121.25` | 2026-06-10T13:03:31 |
| `root` | `` | `45.205.1.36` | 2026-06-10T13:06:01 |
| `moth3r` | `fuck.3r` | `2.57.121.112` | 2026-06-10T13:19:21 |
| `ubuntu` | `ubuntu` | `80.94.92.182` | 2026-06-10T13:30:07 |
| `madilynn` | `madilynn` | `213.209.159.56` | 2026-06-10T13:33:41 |
| `ubuntu` | `ubuntu123` | `80.94.92.182` | 2026-06-10T13:34:21 |
| `sol` | `sol` | `80.94.92.182` | 2026-06-10T13:38:39 |
| `solana` | `solana` | `80.94.92.182` | 2026-06-10T13:42:39 |
| `solana` | `12345678` | `80.94.92.182` | 2026-06-10T13:46:32 |
| `sol` | `1234` | `80.94.92.182` | 2026-06-10T13:50:20 |
| `sol` | `123` | `80.94.92.182` | 2026-06-10T13:54:17 |
| `root` | `LeitboGi0ro` | `140.245.67.111` | 2026-06-10T13:54:50 |
| `root` | `123@@@` | `140.245.67.111` | 2026-06-10T13:54:50 |
| `sol` | `321` | `80.94.92.182` | 2026-06-10T13:58:11 |
| `solana` | `validator` | `80.94.92.182` | 2026-06-10T14:02:16 |
| `validator` | `validator` | `80.94.92.182` | 2026-06-10T14:06:00 |
| `node` | `node` | `80.94.92.182` | 2026-06-10T14:09:48 |
| `firedancer` | `firedancer` | `80.94.92.182` | 2026-06-10T14:13:42 |
| `root` | `LeitboGi0ro` | `188.64.139.147` | 2026-06-10T14:16:14 |
| `root` | `MoeClub.org` | `188.64.139.147` | 2026-06-10T14:16:17 |
| `user` | `interpol` | `2.57.121.25` | 2026-06-10T14:17:08 |
| `ubuntu` | `firedancer` | `80.94.92.182` | 2026-06-10T14:17:31 |
| `ubuntu` | `solana` | `80.94.92.182` | 2026-06-10T14:21:26 |
| `raydium` | `raydium` | `80.94.92.182` | 2026-06-10T14:25:11 |
| `jibs` | `jibs` | `80.94.92.182` | 2026-06-10T14:28:55 |
| `3d` | `3d` | `80.94.92.182` | 2026-06-10T14:32:43 |
| `test` | `test` | `2.57.121.112` | 2026-06-10T14:32:49 |
| `ps` | `123456` | `80.94.92.182` | 2026-06-10T14:36:36 |
| `nicolle` | `nicolle` | `213.209.159.56` | 2026-06-10T14:40:00 |
| `sol` | `sol@123` | `80.94.92.182` | 2026-06-10T14:40:17 |
| `sol` | `qwer1234` | `80.94.92.182` | 2026-06-10T14:44:03 |
| `ubuntu` | `qwer1234` | `80.94.92.182` | 2026-06-10T14:47:54 |
| `ubuntu` | `1234qwer` | `80.94.92.182` | 2026-06-10T14:51:51 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1146** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 39 |
| libssh | 19 |
| PuTTY | 17 |
| Paramiko (Python) | 16 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 25 | 3 |
| `57446c12547a...` | Mirai/variant | 16 | 3 |
| `a2de0f306611...` | Mirai/variant | 16 | 5 |
| `bf7dbf67fa9b...` | Mirai/variant | 4 | 2 |
| `98f63c4d9c87...` | Generic scanner | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 25 | 3 | Generic scanner |
| `57446c12547a...` | PuTTY | 16 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 16 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 16 | 5 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 4 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 4 | 4 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/busybox TEST
```
Source IPs: `45.205.1.36`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **52** |
| Unique ASNs | **35** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS6939` | Hurricane Electric LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (65)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2b79e6204f9e

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 09:03 |
| **Last Seen** | 2026-06-10 09:04 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:03:53` | `cowrie.session.connect` |
| `2026-06-10 09:03:53` | `cowrie.client.version` |
| `2026-06-10 09:03:54` | `cowrie.client.kex` |
| `2026-06-10 09:03:54` | `cowrie.login.success` |
| `2026-06-10 09:03:55` | `cowrie.direct-tcpip.request` |
| `2026-06-10 09:03:55` | `cowrie.direct-tcpip.data` |
| `2026-06-10 09:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7830a0495f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 09:21 |
| **Last Seen** | 2026-06-10 09:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:21:51` | `cowrie.session.connect` |
| `2026-06-10 09:21:51` | `cowrie.client.version` |
| `2026-06-10 09:21:51` | `cowrie.client.kex` |
| `2026-06-10 09:21:52` | `cowrie.login.success` |
| `2026-06-10 09:21:52` | `cowrie.direct-tcpip.request` |
| `2026-06-10 09:21:52` | `cowrie.direct-tcpip.data` |
| `2026-06-10 09:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2a3b4290a6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 09:27 |
| **Last Seen** | 2026-06-10 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:27:24` | `cowrie.session.connect` |
| `2026-06-10 09:27:24` | `cowrie.client.version` |
| `2026-06-10 09:27:24` | `cowrie.client.kex` |
| `2026-06-10 09:27:25` | `cowrie.login.success` |
| `2026-06-10 09:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676af55b1e83

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-10 09:27 |
| **Last Seen** | 2026-06-10 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:27:24` | `cowrie.session.connect` |
| `2026-06-10 09:27:24` | `cowrie.client.version` |
| `2026-06-10 09:27:24` | `cowrie.client.kex` |
| `2026-06-10 09:27:25` | `cowrie.login.success` |
| `2026-06-10 09:27:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15da963e4acc

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 09:30 |
| **Last Seen** | 2026-06-10 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:30:25` | `cowrie.session.connect` |
| `2026-06-10 09:30:25` | `cowrie.client.version` |
| `2026-06-10 09:30:26` | `cowrie.client.kex` |
| `2026-06-10 09:30:27` | `cowrie.login.success` |
| `2026-06-10 09:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e57b13f0dc

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 09:30 |
| **Last Seen** | 2026-06-10 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:30:26` | `cowrie.session.connect` |
| `2026-06-10 09:30:26` | `cowrie.client.version` |
| `2026-06-10 09:30:26` | `cowrie.client.kex` |
| `2026-06-10 09:30:27` | `cowrie.login.success` |
| `2026-06-10 09:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b86057fad74c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 09:36 |
| **Last Seen** | 2026-06-10 09:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:36:27` | `cowrie.session.connect` |
| `2026-06-10 09:36:27` | `cowrie.client.version` |
| `2026-06-10 09:36:27` | `cowrie.client.kex` |
| `2026-06-10 09:36:28` | `cowrie.login.success` |
| `2026-06-10 09:36:28` | `cowrie.direct-tcpip.request` |
| `2026-06-10 09:36:28` | `cowrie.direct-tcpip.data` |
| `2026-06-10 09:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc204ecd22fd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-10 09:41 |
| **Last Seen** | 2026-06-10 09:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:41:15` | `cowrie.session.connect` |
| `2026-06-10 09:41:15` | `cowrie.client.version` |
| `2026-06-10 09:41:15` | `cowrie.client.kex` |
| `2026-06-10 09:41:16` | `cowrie.login.success` |
| `2026-06-10 09:41:16` | `cowrie.direct-tcpip.request` |
| `2026-06-10 09:41:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-10 09:41:16` | `cowrie.direct-tcpip.data` |
| `2026-06-10 09:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beab6ee3ae6c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-10 09:41 |
| **Last Seen** | 2026-06-10 09:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 09:41:16` | `cowrie.session.connect` |
| `2026-06-10 09:41:16` | `cowrie.client.version` |
| `2026-06-10 09:41:16` | `cowrie.client.kex` |
| `2026-06-10 09:41:16` | `cowrie.login.success` |
| `2026-06-10 09:41:16` | `cowrie.direct-tcpip.request` |
| `2026-06-10 09:41:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-10 09:41:17` | `cowrie.direct-tcpip.data` |
| `2026-06-10 09:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd954b87f928

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 10:12 |
| **Last Seen** | 2026-06-10 10:12 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:12:03` | `cowrie.session.connect` |
| `2026-06-10 10:12:03` | `cowrie.client.version` |
| `2026-06-10 10:12:03` | `cowrie.client.kex` |
| `2026-06-10 10:12:03` | `cowrie.login.success` |
| `2026-06-10 10:12:03` | `cowrie.direct-tcpip.request` |
| `2026-06-10 10:12:03` | `cowrie.direct-tcpip.data` |
| `2026-06-10 10:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78007bf67708

| Field | Detail |
|---|---|
| **Source IP** | `42.49.97[.]250` |
| **First Seen** | 2026-06-10 10:21 |
| **Last Seen** | 2026-06-10 10:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:21:06` | `cowrie.session.connect` |
| `2026-06-10 10:21:06` | `cowrie.client.version` |
| `2026-06-10 10:21:06` | `cowrie.client.kex` |
| `2026-06-10 10:21:07` | `cowrie.login.success` |
| `2026-06-10 10:21:08` | `cowrie.session.params` |
| `2026-06-10 10:21:08` | `cowrie.command.input` |
| `2026-06-10 10:21:08` | `cowrie.log.closed` |
| `2026-06-10 10:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.49.97[.]250` to AbuseIPDB if not already reported
- [ ] Block `42.49.97[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff4f163c40d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 10:35 |
| **Last Seen** | 2026-06-10 10:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:35:49` | `cowrie.session.connect` |
| `2026-06-10 10:35:49` | `cowrie.client.version` |
| `2026-06-10 10:35:49` | `cowrie.client.kex` |
| `2026-06-10 10:35:50` | `cowrie.login.success` |
| `2026-06-10 10:35:50` | `cowrie.direct-tcpip.request` |
| `2026-06-10 10:35:50` | `cowrie.direct-tcpip.data` |
| `2026-06-10 10:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cab3307428d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 10:50 |
| **Last Seen** | 2026-06-10 10:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:50:41` | `cowrie.session.connect` |
| `2026-06-10 10:50:41` | `cowrie.client.version` |
| `2026-06-10 10:50:41` | `cowrie.client.kex` |
| `2026-06-10 10:50:42` | `cowrie.login.success` |
| `2026-06-10 10:50:42` | `cowrie.direct-tcpip.request` |
| `2026-06-10 10:50:42` | `cowrie.direct-tcpip.data` |
| `2026-06-10 10:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a314c58ff64

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 11:19 |
| **Last Seen** | 2026-06-10 11:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:19:47` | `cowrie.session.connect` |
| `2026-06-10 11:19:47` | `cowrie.client.version` |
| `2026-06-10 11:19:47` | `cowrie.client.kex` |
| `2026-06-10 11:19:48` | `cowrie.login.success` |
| `2026-06-10 11:19:48` | `cowrie.direct-tcpip.request` |
| `2026-06-10 11:19:48` | `cowrie.direct-tcpip.data` |
| `2026-06-10 11:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d392e241c9f

| Field | Detail |
|---|---|
| **Source IP** | `202.60.229[.]130` |
| **First Seen** | 2026-06-10 11:26 |
| **Last Seen** | 2026-06-10 11:27 |
| **Session Duration** | 73s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:26:02` | `cowrie.session.connect` |
| `2026-06-10 11:26:14` | `cowrie.client.version` |
| `2026-06-10 11:27:13` | `cowrie.client.kex` |
| `2026-06-10 11:27:15` | `cowrie.login.success` |
| `2026-06-10 11:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.60.229[.]130` to AbuseIPDB if not already reported
- [ ] Block `202.60.229[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1ebe7fff1a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-10 11:27 |
| **Last Seen** | 2026-06-10 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:27:31` | `cowrie.session.connect` |
| `2026-06-10 11:27:31` | `cowrie.client.version` |
| `2026-06-10 11:27:31` | `cowrie.client.kex` |
| `2026-06-10 11:27:31` | `cowrie.login.success` |
| `2026-06-10 11:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a811f9affc2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 11:35 |
| **Last Seen** | 2026-06-10 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:35:42` | `cowrie.session.connect` |
| `2026-06-10 11:35:42` | `cowrie.client.version` |
| `2026-06-10 11:35:42` | `cowrie.client.kex` |
| `2026-06-10 11:35:42` | `cowrie.login.success` |
| `2026-06-10 11:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892ec0276aa1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 11:35 |
| **Last Seen** | 2026-06-10 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:35:42` | `cowrie.session.connect` |
| `2026-06-10 11:35:42` | `cowrie.client.version` |
| `2026-06-10 11:35:42` | `cowrie.client.kex` |
| `2026-06-10 11:35:42` | `cowrie.login.success` |
| `2026-06-10 11:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b75a6b6835

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 11:35 |
| **Last Seen** | 2026-06-10 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:35:50` | `cowrie.session.connect` |
| `2026-06-10 11:35:50` | `cowrie.client.version` |
| `2026-06-10 11:35:50` | `cowrie.client.kex` |
| `2026-06-10 11:35:50` | `cowrie.login.success` |
| `2026-06-10 11:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f913bfd3d69

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-10 11:35 |
| **Last Seen** | 2026-06-10 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:35:50` | `cowrie.session.connect` |
| `2026-06-10 11:35:50` | `cowrie.client.version` |
| `2026-06-10 11:35:50` | `cowrie.client.kex` |
| `2026-06-10 11:35:50` | `cowrie.login.success` |
| `2026-06-10 11:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102fdcac3938

| Field | Detail |
|---|---|
| **Source IP** | `183.129.249[.]4` |
| **First Seen** | 2026-06-10 11:48 |
| **Last Seen** | 2026-06-10 11:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:48:42` | `cowrie.session.connect` |
| `2026-06-10 11:48:42` | `cowrie.client.version` |
| `2026-06-10 11:48:42` | `cowrie.client.kex` |
| `2026-06-10 11:48:42` | `cowrie.login.success` |
| `2026-06-10 11:48:44` | `cowrie.session.params` |
| `2026-06-10 11:48:44` | `cowrie.command.input` |
| `2026-06-10 11:48:44` | `cowrie.log.closed` |
| `2026-06-10 11:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.129.249[.]4` to AbuseIPDB if not already reported
- [ ] Block `183.129.249[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c378d5540758

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 11:49 |
| **Last Seen** | 2026-06-10 11:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:49:57` | `cowrie.session.connect` |
| `2026-06-10 11:49:57` | `cowrie.client.version` |
| `2026-06-10 11:49:57` | `cowrie.client.kex` |
| `2026-06-10 11:49:57` | `cowrie.login.success` |
| `2026-06-10 11:49:57` | `cowrie.direct-tcpip.request` |
| `2026-06-10 11:49:58` | `cowrie.direct-tcpip.data` |
| `2026-06-10 11:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b10e206d51

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 12:05 |
| **Last Seen** | 2026-06-10 12:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:05:04` | `cowrie.session.connect` |
| `2026-06-10 12:05:04` | `cowrie.client.version` |
| `2026-06-10 12:05:04` | `cowrie.client.kex` |
| `2026-06-10 12:05:05` | `cowrie.login.success` |
| `2026-06-10 12:05:05` | `cowrie.direct-tcpip.request` |
| `2026-06-10 12:05:05` | `cowrie.direct-tcpip.data` |
| `2026-06-10 12:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f8b6a4d957

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]172` |
| **First Seen** | 2026-06-10 12:10 |
| **Last Seen** | 2026-06-10 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:10:07` | `cowrie.session.connect` |
| `2026-06-10 12:10:07` | `cowrie.login.success` |
| `2026-06-10 12:10:08` | `cowrie.session.params` |
| `2026-06-10 12:10:08` | `cowrie.command.input` |
| `2026-06-10 12:10:08` | `cowrie.command.input` |
| `2026-06-10 12:10:08` | `cowrie.command.failed` |
| `2026-06-10 12:10:08` | `cowrie.command.input` |
| `2026-06-10 12:10:08` | `cowrie.command.failed` |
| `2026-06-10 12:10:08` | `cowrie.command.input` |
| `2026-06-10 12:10:08` | `cowrie.log.closed` |
| `2026-06-10 12:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]172` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-533f63cfa2a0

| Field | Detail |
|---|---|
| **Source IP** | `83.177.240[.]110` |
| **First Seen** | 2026-06-10 12:11 |
| **Last Seen** | 2026-06-10 12:12 |
| **Session Duration** | 47s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:11:23` | `cowrie.session.connect` |
| `2026-06-10 12:11:23` | `cowrie.client.version` |
| `2026-06-10 12:11:24` | `cowrie.client.kex` |
| `2026-06-10 12:11:24` | `cowrie.login.failed` |
| `2026-06-10 12:11:25` | `cowrie.login.success` |
| `2026-06-10 12:11:26` | `cowrie.session.params` |
| `2026-06-10 12:11:26` | `cowrie.command.input` |
| `2026-06-10 12:11:26` | `cowrie.command.failed` |
| `2026-06-10 12:11:26` | `cowrie.log.closed` |
| `2026-06-10 12:11:27` | `cowrie.session.params` |
| `2026-06-10 12:11:27` | `cowrie.command.input` |
| `2026-06-10 12:11:27` | `cowrie.log.closed` |
| `2026-06-10 12:11:28` | `cowrie.session.params` |
| `2026-06-10 12:11:28` | `cowrie.command.input` |
| `2026-06-10 12:11:28` | `cowrie.log.closed` |
| `2026-06-10 12:11:28` | `cowrie.session.params` |
| `2026-06-10 12:11:28` | `cowrie.command.input` |
| `2026-06-10 12:11:29` | `cowrie.log.closed` |
| `2026-06-10 12:11:29` | `cowrie.session.params` |
| `2026-06-10 12:11:29` | `cowrie.command.input` |
| `2026-06-10 12:11:29` | `cowrie.log.closed` |
| `2026-06-10 12:11:30` | `cowrie.session.params` |
| `2026-06-10 12:11:30` | `cowrie.command.input` |
| `2026-06-10 12:11:30` | `cowrie.log.closed` |
| `2026-06-10 12:11:31` | `cowrie.session.params` |
| `2026-06-10 12:11:31` | `cowrie.command.input` |
| `2026-06-10 12:11:31` | `cowrie.log.closed` |
| `2026-06-10 12:11:32` | `cowrie.session.params` |
| `2026-06-10 12:11:32` | `cowrie.command.input` |
| `2026-06-10 12:11:32` | `cowrie.log.closed` |
| `2026-06-10 12:11:33` | `cowrie.session.params` |
| `2026-06-10 12:11:33` | `cowrie.command.input` |
| `2026-06-10 12:11:33` | `cowrie.log.closed` |
| `2026-06-10 12:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.177.240[.]110` to AbuseIPDB if not already reported
- [ ] Block `83.177.240[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b49bde39f2c

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 12:26 |
| **Last Seen** | 2026-06-10 12:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:26:51` | `cowrie.session.connect` |
| `2026-06-10 12:26:51` | `cowrie.client.version` |
| `2026-06-10 12:26:51` | `cowrie.client.kex` |
| `2026-06-10 12:26:52` | `cowrie.login.success` |
| `2026-06-10 12:26:52` | `cowrie.direct-tcpip.request` |
| `2026-06-10 12:26:52` | `cowrie.direct-tcpip.data` |
| `2026-06-10 12:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ce5efc2809

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 12:51 |
| **Last Seen** | 2026-06-10 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:51:52` | `cowrie.session.connect` |
| `2026-06-10 12:51:52` | `cowrie.client.version` |
| `2026-06-10 12:51:52` | `cowrie.client.kex` |
| `2026-06-10 12:51:52` | `cowrie.login.success` |
| `2026-06-10 12:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1298108dac

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 12:51 |
| **Last Seen** | 2026-06-10 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:51:52` | `cowrie.session.connect` |
| `2026-06-10 12:51:52` | `cowrie.client.version` |
| `2026-06-10 12:51:52` | `cowrie.client.kex` |
| `2026-06-10 12:51:52` | `cowrie.login.success` |
| `2026-06-10 12:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3fa64c54ff

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 12:52 |
| **Last Seen** | 2026-06-10 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:52:00` | `cowrie.session.connect` |
| `2026-06-10 12:52:00` | `cowrie.client.version` |
| `2026-06-10 12:52:01` | `cowrie.client.kex` |
| `2026-06-10 12:52:01` | `cowrie.login.success` |
| `2026-06-10 12:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3355a3da7d62

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-10 12:52 |
| **Last Seen** | 2026-06-10 12:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:52:02` | `cowrie.session.connect` |
| `2026-06-10 12:52:02` | `cowrie.client.version` |
| `2026-06-10 12:52:02` | `cowrie.client.kex` |
| `2026-06-10 12:52:02` | `cowrie.login.success` |
| `2026-06-10 12:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7335ed7354

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 13:03 |
| **Last Seen** | 2026-06-10 13:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:03:30` | `cowrie.session.connect` |
| `2026-06-10 13:03:30` | `cowrie.client.version` |
| `2026-06-10 13:03:31` | `cowrie.client.kex` |
| `2026-06-10 13:03:31` | `cowrie.login.success` |
| `2026-06-10 13:03:31` | `cowrie.direct-tcpip.request` |
| `2026-06-10 13:03:31` | `cowrie.direct-tcpip.data` |
| `2026-06-10 13:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886059ac69a8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]36` |
| **First Seen** | 2026-06-10 13:05 |
| **Last Seen** | 2026-06-10 13:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /busybox TEST` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:05:59` | `cowrie.session.connect` |
| `2026-06-10 13:06:01` | `cowrie.login.success` |
| `2026-06-10 13:06:02` | `cowrie.session.params` |
| `2026-06-10 13:06:02` | `cowrie.command.input` |
| `2026-06-10 13:06:03` | `cowrie.command.input` |
| `2026-06-10 13:06:03` | `cowrie.command.failed` |
| `2026-06-10 13:06:04` | `cowrie.log.closed` |
| `2026-06-10 13:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]36` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3a97bcd12a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 13:19 |
| **Last Seen** | 2026-06-10 13:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:19:20` | `cowrie.session.connect` |
| `2026-06-10 13:19:20` | `cowrie.client.version` |
| `2026-06-10 13:19:20` | `cowrie.client.kex` |
| `2026-06-10 13:19:21` | `cowrie.login.success` |
| `2026-06-10 13:19:21` | `cowrie.direct-tcpip.request` |
| `2026-06-10 13:19:21` | `cowrie.direct-tcpip.data` |
| `2026-06-10 13:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb7250280b9

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:30 |
| **Last Seen** | 2026-06-10 13:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:30:06` | `cowrie.session.connect` |
| `2026-06-10 13:30:06` | `cowrie.client.version` |
| `2026-06-10 13:30:06` | `cowrie.client.kex` |
| `2026-06-10 13:30:07` | `cowrie.login.success` |
| `2026-06-10 13:30:08` | `cowrie.session.params` |
| `2026-06-10 13:30:08` | `cowrie.command.input` |
| `2026-06-10 13:30:09` | `cowrie.log.closed` |
| `2026-06-10 13:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f849141cb688

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 13:33 |
| **Last Seen** | 2026-06-10 13:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:33:40` | `cowrie.session.connect` |
| `2026-06-10 13:33:40` | `cowrie.client.version` |
| `2026-06-10 13:33:41` | `cowrie.client.kex` |
| `2026-06-10 13:33:41` | `cowrie.login.success` |
| `2026-06-10 13:33:41` | `cowrie.direct-tcpip.request` |
| `2026-06-10 13:33:41` | `cowrie.direct-tcpip.data` |
| `2026-06-10 13:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5551e153e06

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:34 |
| **Last Seen** | 2026-06-10 13:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:34:19` | `cowrie.session.connect` |
| `2026-06-10 13:34:19` | `cowrie.client.version` |
| `2026-06-10 13:34:19` | `cowrie.client.kex` |
| `2026-06-10 13:34:21` | `cowrie.login.success` |
| `2026-06-10 13:34:22` | `cowrie.session.params` |
| `2026-06-10 13:34:22` | `cowrie.command.input` |
| `2026-06-10 13:34:22` | `cowrie.log.closed` |
| `2026-06-10 13:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eec611cf0d0

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:38 |
| **Last Seen** | 2026-06-10 13:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:38:35` | `cowrie.session.connect` |
| `2026-06-10 13:38:35` | `cowrie.client.version` |
| `2026-06-10 13:38:35` | `cowrie.client.kex` |
| `2026-06-10 13:38:39` | `cowrie.login.success` |
| `2026-06-10 13:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584a8ac4e0a1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:42 |
| **Last Seen** | 2026-06-10 13:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:42:36` | `cowrie.session.connect` |
| `2026-06-10 13:42:37` | `cowrie.client.version` |
| `2026-06-10 13:42:37` | `cowrie.client.kex` |
| `2026-06-10 13:42:39` | `cowrie.login.success` |
| `2026-06-10 13:42:40` | `cowrie.session.params` |
| `2026-06-10 13:42:40` | `cowrie.command.input` |
| `2026-06-10 13:42:42` | `cowrie.log.closed` |
| `2026-06-10 13:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16887f7340d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:46 |
| **Last Seen** | 2026-06-10 13:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:46:29` | `cowrie.session.connect` |
| `2026-06-10 13:46:29` | `cowrie.client.version` |
| `2026-06-10 13:46:29` | `cowrie.client.kex` |
| `2026-06-10 13:46:32` | `cowrie.login.success` |
| `2026-06-10 13:46:33` | `cowrie.session.params` |
| `2026-06-10 13:46:33` | `cowrie.command.input` |
| `2026-06-10 13:46:33` | `cowrie.log.closed` |
| `2026-06-10 13:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29fffbe37d89

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:50 |
| **Last Seen** | 2026-06-10 13:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:50:18` | `cowrie.session.connect` |
| `2026-06-10 13:50:18` | `cowrie.client.version` |
| `2026-06-10 13:50:18` | `cowrie.client.kex` |
| `2026-06-10 13:50:20` | `cowrie.login.success` |
| `2026-06-10 13:50:21` | `cowrie.session.params` |
| `2026-06-10 13:50:21` | `cowrie.command.input` |
| `2026-06-10 13:50:22` | `cowrie.log.closed` |
| `2026-06-10 13:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac26b22aae3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:54 |
| **Last Seen** | 2026-06-10 13:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:54:16` | `cowrie.session.connect` |
| `2026-06-10 13:54:16` | `cowrie.client.version` |
| `2026-06-10 13:54:17` | `cowrie.client.kex` |
| `2026-06-10 13:54:17` | `cowrie.login.success` |
| `2026-06-10 13:54:19` | `cowrie.session.params` |
| `2026-06-10 13:54:19` | `cowrie.command.input` |
| `2026-06-10 13:54:19` | `cowrie.log.closed` |
| `2026-06-10 13:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace32d1ee3fa

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-10 13:54 |
| **Last Seen** | 2026-06-10 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:54:49` | `cowrie.session.connect` |
| `2026-06-10 13:54:49` | `cowrie.client.version` |
| `2026-06-10 13:54:49` | `cowrie.client.kex` |
| `2026-06-10 13:54:50` | `cowrie.login.success` |
| `2026-06-10 13:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a8b1c6a89a

| Field | Detail |
|---|---|
| **Source IP** | `140.245.67[.]111` |
| **First Seen** | 2026-06-10 13:54 |
| **Last Seen** | 2026-06-10 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:54:49` | `cowrie.session.connect` |
| `2026-06-10 13:54:49` | `cowrie.client.version` |
| `2026-06-10 13:54:49` | `cowrie.client.kex` |
| `2026-06-10 13:54:50` | `cowrie.login.success` |
| `2026-06-10 13:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.67[.]111` to AbuseIPDB if not already reported
- [ ] Block `140.245.67[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d6781e1c234

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 13:58 |
| **Last Seen** | 2026-06-10 13:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:58:09` | `cowrie.session.connect` |
| `2026-06-10 13:58:09` | `cowrie.client.version` |
| `2026-06-10 13:58:09` | `cowrie.client.kex` |
| `2026-06-10 13:58:11` | `cowrie.login.success` |
| `2026-06-10 13:58:12` | `cowrie.session.params` |
| `2026-06-10 13:58:12` | `cowrie.command.input` |
| `2026-06-10 13:58:13` | `cowrie.log.closed` |
| `2026-06-10 13:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65ecbba51c2

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 14:00 |
| **Last Seen** | 2026-06-10 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:00:29` | `cowrie.session.connect` |
| `2026-06-10 14:00:29` | `cowrie.client.version` |
| `2026-06-10 14:00:29` | `cowrie.client.kex` |
| `2026-06-10 14:00:30` | `cowrie.login.success` |
| `2026-06-10 14:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638881d399fc

| Field | Detail |
|---|---|
| **Source IP** | `138.2.98[.]41` |
| **First Seen** | 2026-06-10 14:00 |
| **Last Seen** | 2026-06-10 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:00:29` | `cowrie.session.connect` |
| `2026-06-10 14:00:29` | `cowrie.client.version` |
| `2026-06-10 14:00:30` | `cowrie.client.kex` |
| `2026-06-10 14:00:31` | `cowrie.login.success` |
| `2026-06-10 14:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.2.98[.]41` to AbuseIPDB if not already reported
- [ ] Block `138.2.98[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497973a4bc4d

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:02 |
| **Last Seen** | 2026-06-10 14:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:02:14` | `cowrie.session.connect` |
| `2026-06-10 14:02:15` | `cowrie.client.version` |
| `2026-06-10 14:02:15` | `cowrie.client.kex` |
| `2026-06-10 14:02:16` | `cowrie.login.success` |
| `2026-06-10 14:02:18` | `cowrie.session.params` |
| `2026-06-10 14:02:18` | `cowrie.command.input` |
| `2026-06-10 14:02:18` | `cowrie.log.closed` |
| `2026-06-10 14:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21e52fec886

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:05 |
| **Last Seen** | 2026-06-10 14:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:05:58` | `cowrie.session.connect` |
| `2026-06-10 14:05:58` | `cowrie.client.version` |
| `2026-06-10 14:05:58` | `cowrie.client.kex` |
| `2026-06-10 14:06:00` | `cowrie.login.success` |
| `2026-06-10 14:06:02` | `cowrie.session.params` |
| `2026-06-10 14:06:02` | `cowrie.command.input` |
| `2026-06-10 14:06:02` | `cowrie.log.closed` |
| `2026-06-10 14:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8469461f12f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:09 |
| **Last Seen** | 2026-06-10 14:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:09:45` | `cowrie.session.connect` |
| `2026-06-10 14:09:45` | `cowrie.client.version` |
| `2026-06-10 14:09:45` | `cowrie.client.kex` |
| `2026-06-10 14:09:48` | `cowrie.login.success` |
| `2026-06-10 14:09:49` | `cowrie.session.params` |
| `2026-06-10 14:09:49` | `cowrie.command.input` |
| `2026-06-10 14:09:49` | `cowrie.log.closed` |
| `2026-06-10 14:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233529b4b17f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:13 |
| **Last Seen** | 2026-06-10 14:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:13:40` | `cowrie.session.connect` |
| `2026-06-10 14:13:40` | `cowrie.client.version` |
| `2026-06-10 14:13:41` | `cowrie.client.kex` |
| `2026-06-10 14:13:42` | `cowrie.login.success` |
| `2026-06-10 14:13:46` | `cowrie.session.params` |
| `2026-06-10 14:13:46` | `cowrie.command.input` |
| `2026-06-10 14:13:46` | `cowrie.log.closed` |
| `2026-06-10 14:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69cfa2e34cbc

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-10 14:16 |
| **Last Seen** | 2026-06-10 14:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:16:12` | `cowrie.session.connect` |
| `2026-06-10 14:16:12` | `cowrie.client.version` |
| `2026-06-10 14:16:12` | `cowrie.client.kex` |
| `2026-06-10 14:16:14` | `cowrie.login.success` |
| `2026-06-10 14:16:15` | `cowrie.session.params` |
| `2026-06-10 14:16:15` | `cowrie.command.input` |
| `2026-06-10 14:16:16` | `cowrie.log.closed` |
| `2026-06-10 14:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b12c95197d

| Field | Detail |
|---|---|
| **Source IP** | `188.64.139[.]147` |
| **First Seen** | 2026-06-10 14:16 |
| **Last Seen** | 2026-06-10 14:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -m 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d'=' -f2 | tr -d '"' | tr -d '\n\r' || echo 'Linux'; echo '---SEP---'; hostname 2>/dev/null | tr -d '\n\r' || echo 'unknown'; echo '---SEP---'; curl -s --connect-timeout 2 ipinfo.io/country 2>/dev/null | tr -d '\n\r' || echo 'N/A'; echo '---SEP---'; nproc 2>/dev/null | tr -d '\n\r' || echo '1'; echo '---SEP---'; free -h 2>/dev/null | awk '/^Mem:/ {print $2}' | tr -d '\n\r' || echo ` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:16:16` | `cowrie.session.connect` |
| `2026-06-10 14:16:16` | `cowrie.client.version` |
| `2026-06-10 14:16:16` | `cowrie.client.kex` |
| `2026-06-10 14:16:17` | `cowrie.login.success` |
| `2026-06-10 14:16:18` | `cowrie.session.params` |
| `2026-06-10 14:16:18` | `cowrie.command.input` |
| `2026-06-10 14:16:19` | `cowrie.log.closed` |
| `2026-06-10 14:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.64.139[.]147` to AbuseIPDB if not already reported
- [ ] Block `188.64.139[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6ccf99c8cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]25` |
| **First Seen** | 2026-06-10 14:17 |
| **Last Seen** | 2026-06-10 14:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:17:08` | `cowrie.session.connect` |
| `2026-06-10 14:17:08` | `cowrie.client.version` |
| `2026-06-10 14:17:08` | `cowrie.client.kex` |
| `2026-06-10 14:17:08` | `cowrie.login.success` |
| `2026-06-10 14:17:09` | `cowrie.direct-tcpip.request` |
| `2026-06-10 14:17:09` | `cowrie.direct-tcpip.data` |
| `2026-06-10 14:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]25` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6e90f5682b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:17 |
| **Last Seen** | 2026-06-10 14:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:17:27` | `cowrie.session.connect` |
| `2026-06-10 14:17:28` | `cowrie.client.version` |
| `2026-06-10 14:17:28` | `cowrie.client.kex` |
| `2026-06-10 14:17:31` | `cowrie.login.success` |
| `2026-06-10 14:17:32` | `cowrie.session.params` |
| `2026-06-10 14:17:32` | `cowrie.command.input` |
| `2026-06-10 14:17:33` | `cowrie.log.closed` |
| `2026-06-10 14:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5a1dcd77cc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:21 |
| **Last Seen** | 2026-06-10 14:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:21:24` | `cowrie.session.connect` |
| `2026-06-10 14:21:25` | `cowrie.client.version` |
| `2026-06-10 14:21:25` | `cowrie.client.kex` |
| `2026-06-10 14:21:26` | `cowrie.login.success` |
| `2026-06-10 14:21:27` | `cowrie.session.params` |
| `2026-06-10 14:21:27` | `cowrie.command.input` |
| `2026-06-10 14:21:28` | `cowrie.log.closed` |
| `2026-06-10 14:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b24db14f751

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:25 |
| **Last Seen** | 2026-06-10 14:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:25:10` | `cowrie.session.connect` |
| `2026-06-10 14:25:10` | `cowrie.client.version` |
| `2026-06-10 14:25:10` | `cowrie.client.kex` |
| `2026-06-10 14:25:11` | `cowrie.login.success` |
| `2026-06-10 14:25:12` | `cowrie.session.params` |
| `2026-06-10 14:25:12` | `cowrie.command.input` |
| `2026-06-10 14:25:13` | `cowrie.log.closed` |
| `2026-06-10 14:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0d449e69fe

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:28 |
| **Last Seen** | 2026-06-10 14:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:28:54` | `cowrie.session.connect` |
| `2026-06-10 14:28:54` | `cowrie.client.version` |
| `2026-06-10 14:28:54` | `cowrie.client.kex` |
| `2026-06-10 14:28:55` | `cowrie.login.success` |
| `2026-06-10 14:28:56` | `cowrie.session.params` |
| `2026-06-10 14:28:56` | `cowrie.command.input` |
| `2026-06-10 14:28:57` | `cowrie.log.closed` |
| `2026-06-10 14:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360e1aee6479

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:32 |
| **Last Seen** | 2026-06-10 14:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:32:42` | `cowrie.session.connect` |
| `2026-06-10 14:32:43` | `cowrie.client.version` |
| `2026-06-10 14:32:43` | `cowrie.client.kex` |
| `2026-06-10 14:32:43` | `cowrie.login.success` |
| `2026-06-10 14:32:45` | `cowrie.session.params` |
| `2026-06-10 14:32:45` | `cowrie.command.input` |
| `2026-06-10 14:32:45` | `cowrie.log.closed` |
| `2026-06-10 14:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76ad337be648

| Field | Detail |
|---|---|
| **Source IP** | `2.57.121[.]112` |
| **First Seen** | 2026-06-10 14:32 |
| **Last Seen** | 2026-06-10 14:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:32:49` | `cowrie.session.connect` |
| `2026-06-10 14:32:49` | `cowrie.client.version` |
| `2026-06-10 14:32:49` | `cowrie.client.kex` |
| `2026-06-10 14:32:49` | `cowrie.login.success` |
| `2026-06-10 14:32:50` | `cowrie.direct-tcpip.request` |
| `2026-06-10 14:32:50` | `cowrie.direct-tcpip.data` |
| `2026-06-10 14:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.121[.]112` to AbuseIPDB if not already reported
- [ ] Block `2.57.121[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b8fb648b35

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:36 |
| **Last Seen** | 2026-06-10 14:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:36:34` | `cowrie.session.connect` |
| `2026-06-10 14:36:35` | `cowrie.client.version` |
| `2026-06-10 14:36:35` | `cowrie.client.kex` |
| `2026-06-10 14:36:36` | `cowrie.login.success` |
| `2026-06-10 14:36:37` | `cowrie.session.params` |
| `2026-06-10 14:36:37` | `cowrie.command.input` |
| `2026-06-10 14:36:38` | `cowrie.log.closed` |
| `2026-06-10 14:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1283ec1df42d

| Field | Detail |
|---|---|
| **Source IP** | `213.209.159[.]56` |
| **First Seen** | 2026-06-10 14:40 |
| **Last Seen** | 2026-06-10 14:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:40:00` | `cowrie.session.connect` |
| `2026-06-10 14:40:00` | `cowrie.client.version` |
| `2026-06-10 14:40:00` | `cowrie.client.kex` |
| `2026-06-10 14:40:00` | `cowrie.login.success` |
| `2026-06-10 14:40:00` | `cowrie.direct-tcpip.request` |
| `2026-06-10 14:40:00` | `cowrie.direct-tcpip.data` |
| `2026-06-10 14:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.209.159[.]56` to AbuseIPDB if not already reported
- [ ] Block `213.209.159[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8efd4bbf8340

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:40 |
| **Last Seen** | 2026-06-10 14:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:40:16` | `cowrie.session.connect` |
| `2026-06-10 14:40:16` | `cowrie.client.version` |
| `2026-06-10 14:40:16` | `cowrie.client.kex` |
| `2026-06-10 14:40:17` | `cowrie.login.success` |
| `2026-06-10 14:40:19` | `cowrie.session.params` |
| `2026-06-10 14:40:19` | `cowrie.command.input` |
| `2026-06-10 14:40:20` | `cowrie.log.closed` |
| `2026-06-10 14:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc657ebf05e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:44 |
| **Last Seen** | 2026-06-10 14:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:44:01` | `cowrie.session.connect` |
| `2026-06-10 14:44:01` | `cowrie.client.version` |
| `2026-06-10 14:44:01` | `cowrie.client.kex` |
| `2026-06-10 14:44:03` | `cowrie.login.success` |
| `2026-06-10 14:44:04` | `cowrie.session.params` |
| `2026-06-10 14:44:04` | `cowrie.command.input` |
| `2026-06-10 14:44:05` | `cowrie.log.closed` |
| `2026-06-10 14:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2b618cedd8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:47 |
| **Last Seen** | 2026-06-10 14:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:47:51` | `cowrie.session.connect` |
| `2026-06-10 14:47:53` | `cowrie.client.version` |
| `2026-06-10 14:47:53` | `cowrie.client.kex` |
| `2026-06-10 14:47:54` | `cowrie.login.success` |
| `2026-06-10 14:47:56` | `cowrie.session.params` |
| `2026-06-10 14:47:56` | `cowrie.command.input` |
| `2026-06-10 14:47:56` | `cowrie.log.closed` |
| `2026-06-10 14:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7052bd28d688

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]182` |
| **First Seen** | 2026-06-10 14:51 |
| **Last Seen** | 2026-06-10 14:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:51:50` | `cowrie.session.connect` |
| `2026-06-10 14:51:50` | `cowrie.client.version` |
| `2026-06-10 14:51:50` | `cowrie.client.kex` |
| `2026-06-10 14:51:51` | `cowrie.login.success` |
| `2026-06-10 14:51:52` | `cowrie.session.params` |
| `2026-06-10 14:51:52` | `cowrie.command.input` |
| `2026-06-10 14:51:53` | `cowrie.log.closed` |
| `2026-06-10 14:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]182` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.150[.]219` | **980** | 2026-06-10 08:55 | 2026-06-10 14:54 | 921m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **25** | 2026-06-10 08:58 | 2026-06-10 14:24 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `106.75.166[.]71` | **2** | 2026-06-10 14:40 | 2026-06-10 14:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.48.53[.]174` | **2** | 2026-06-10 12:27 | 2026-06-10 12:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-10 12:24 | 2026-06-10 13:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.217.149[.]46` | **2** | 2026-06-10 10:49 | 2026-06-10 10:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `182.92.202[.]149` | **2** | 2026-06-10 13:35 | 2026-06-10 13:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]29` | **2** | 2026-06-10 09:58 | 2026-06-10 09:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]132` | **2** | 2026-06-10 12:41 | 2026-06-10 12:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.23.63[.]217` | **2** | 2026-06-10 09:08 | 2026-06-10 09:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-10 09:15 | 2026-06-10 09:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.73.112[.]214` | **2** | 2026-06-10 13:25 | 2026-06-10 13:25 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]180` | **2** | 2026-06-10 10:44 | 2026-06-10 10:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.227.180[.]176` | 1 | 2026-06-10 09:41 | 2026-06-10 09:41 | 8s | 0 | `T1592` | 🟢 LOW |
| `183.129.249[.]4` | 1 | 2026-06-10 11:48 | 2026-06-10 11:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.115.189[.]194` | 1 | 2026-06-10 13:29 | 2026-06-10 13:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `42.49.97[.]250` | 1 | 2026-06-10 10:21 | 2026-06-10 10:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-06-10 14:31 | 2026-06-10 14:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-06-10 10:09 | 2026-06-10 10:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]36` | 1 | 2026-06-10 13:05 | 2026-06-10 13:05 | 1s | 0 | `T1592` | 🟢 LOW |
| `47.236.26[.]203` | 1 | 2026-06-10 10:50 | 2026-06-10 10:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]108` | 1 | 2026-06-10 11:33 | 2026-06-10 11:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.222.138[.]87` | 1 | 2026-06-10 11:23 | 2026-06-10 11:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]182` | 1 | 2026-06-10 13:20 | 2026-06-10 13:20 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `199.45.154[.]132` | HK | Censys, Inc. | **100** ⚠️ | 50 |
| `213.209.159[.]56` | DE | Feo Prest SRL | **100** ⚠️ | 50 |
| `45.205.1[.]36` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 32 |
| `83.177.240[.]110` | SE | Tele2 Sverige AB | **100** ⚠️ | 1 |
| `66.132.186[.]180` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `120.48.53[.]174` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 17 |
| `182.92.202[.]149` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 2 |
| `80.94.92[.]182` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 93 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 68 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (43 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 31 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1146 cases |
| Tool 34  | Credential Extractor        | ✅ 69 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 52 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 43 filtered (3.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 65 priority case(s) shown individually · 24 recon entry/entries in table (13 group(s) consolidating 1027 session(s)).

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
_Report time: 2026-06-10T15:46:45Z_

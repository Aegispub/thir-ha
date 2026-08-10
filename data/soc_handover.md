# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-10 |
| **Generated At** | 2026-08-10T15:01:52Z |
| **Shift Time** | 15:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **173** |
| Confirmed Threats | **152** |
| False Positives Filtered | **21** (12.1%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **24** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **128** |
| Malware Samples Analyzed | **2** HIGH · **24** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **52** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **9** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `admin` | 7 |
| `support` | 3 |
| `centos` | 3 |
| `odoo` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `changeme` | 4 |
| `smo@@kkklss` | 4 |
| `123456789` | 3 |
| `rootroot` | 3 |
| `Centos2013` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `changeme` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `rootroot` | 3 |
| `centos` | `Centos2013` | 3 |
| `odoo` | `odoo` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `changeme` | `220.122.115.9` | 2026-08-10T12:59:22 |
| `admin` | `changeme` | `111.70.42.37` | 2026-08-10T12:59:35 |
| `admin` | `changeme` | `31.173.2.182` | 2026-08-10T12:59:35 |
| `admin` | `changeme` | `31.41.81.65` | 2026-08-10T12:59:47 |
| `support` | `123456789` | `50.188.204.213` | 2026-08-10T13:04:23 |
| `support` | `123456789` | `219.129.236.174` | 2026-08-10T13:04:39 |
| `support` | `support` | `176.53.159.196` | 2026-08-10T13:10:37 |
| `supervisor` | `1234567890` | `45.170.50.2` | 2026-08-10T13:12:50 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-10T13:16:04 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-10T13:16:05 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-10T13:16:10 |
| `root` | `rootroot` | `10.0.0.73` | 2026-08-10T13:21:38 |
| `admin` | `admin` | `47.16.106.54` | 2026-08-10T13:30:47 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-10T13:30:48 |
| `centos` | `Centos2013` | `65.20.163.103` | 2026-08-10T13:33:40 |
| `centos` | `Centos2013` | `45.55.133.80` | 2026-08-10T13:33:53 |
| `centos` | `Centos2013` | `200.232.114.71` | 2026-08-10T13:34:00 |
| `root` | `---fuck_you----` | `43.106.81.238` | 2026-08-10T13:36:59 |
| `root` | `rootroot` | `62.201.212.54` | 2026-08-10T13:39:12 |
| `root` | `rootroot` | `68.7.114.69` | 2026-08-10T13:39:24 |
| `odoo` | `odoo` | `211.253.10.61` | 2026-08-10T13:44:25 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-10T13:44:30 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-10T13:44:30 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-10T13:44:32 |
| `odoo` | `odoo` | `10.0.0.73` | 2026-08-10T13:56:08 |
| `ubnt` | `ubntubnt` | `45.154.244.193` | 2026-08-10T14:01:54 |
| `root` | `2022` | `202.138.229.190` | 2026-08-10T14:04:01 |
| `root` | `2022` | `125.36.68.227` | 2026-08-10T14:04:10 |
| `admin` | `1q2w3e4r!` | `124.67.120.106` | 2026-08-10T14:08:19 |
| `root` | `﻿------fuck------` | `183.56.192.210` | 2026-08-10T14:11:42 |
| `blank` | `blank123456` | `23.30.11.253` | 2026-08-10T14:18:52 |
| `root` | `Passw@rd` | `10.0.0.73` | 2026-08-10T14:20:28 |
| `root` | `Passw@rd` | `31.173.29.136` | 2026-08-10T14:22:07 |
| `root` | `1` | `92.118.39.14` | 2026-08-10T14:33:53 |
| `root` | `12` | `92.118.39.14` | 2026-08-10T14:36:03 |
| `root` | `123` | `92.118.39.14` | 2026-08-10T14:38:10 |
| `root` | `Passw@rd` | `81.214.75.248` | 2026-08-10T14:38:29 |
| `root` | `1234` | `92.118.39.14` | 2026-08-10T14:40:17 |
| `root` | `12345` | `92.118.39.14` | 2026-08-10T14:42:23 |
| `oracle` | `oracle` | `96.56.228.149` | 2026-08-10T14:43:07 |
| `oracle` | `oracle` | `200.222.71.218` | 2026-08-10T14:43:19 |
| `root` | `1234567` | `92.118.39.14` | 2026-08-10T14:46:34 |
| `ubnt` | `ubntubnt` | `10.0.0.73` | 2026-08-10T14:47:10 |
| `blank` | `blank123456` | `178.216.165.187` | 2026-08-10T14:48:01 |
| `root` | `12345678` | `92.118.39.14` | 2026-08-10T14:48:40 |
| `root` | `123456789` | `92.118.39.14` | 2026-08-10T14:50:46 |
| `root` | `CtrDByNlv1` | `10.0.0.73` | 2026-08-10T14:52:16 |
| `root` | `1234567890` | `92.118.39.14` | 2026-08-10T14:52:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **173** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 23 |
| Go SSH scanner | 17 |
| libssh | 10 |
| Paramiko (Python) | 8 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 23 | 23 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |
| `eff4c24daffc...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 23 | 23 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 9 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.14`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **48** |
| High-Risk ASNs | **37** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | LOW |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (45)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8ed46354ad14

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-08-10 12:59 |
| **Last Seen** | 2026-08-10 12:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:59:20` | `cowrie.session.connect` |
| `2026-08-10 12:59:20` | `cowrie.client.version` |
| `2026-08-10 12:59:20` | `cowrie.client.kex` |
| `2026-08-10 12:59:22` | `cowrie.login.success` |
| `2026-08-10 12:59:23` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c9e6b0eb53

| Field | Detail |
|---|---|
| **Source IP** | `111.70.42[.]37` |
| **First Seen** | 2026-08-10 12:59 |
| **Last Seen** | 2026-08-10 12:59 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:59:29` | `cowrie.session.connect` |
| `2026-08-10 12:59:30` | `cowrie.client.version` |
| `2026-08-10 12:59:30` | `cowrie.client.kex` |
| `2026-08-10 12:59:35` | `cowrie.login.success` |
| `2026-08-10 12:59:36` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.42[.]37` to AbuseIPDB if not already reported
- [ ] Block `111.70.42[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b38317805e

| Field | Detail |
|---|---|
| **Source IP** | `31.173.2[.]182` |
| **First Seen** | 2026-08-10 12:59 |
| **Last Seen** | 2026-08-10 12:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:59:33` | `cowrie.session.connect` |
| `2026-08-10 12:59:34` | `cowrie.client.version` |
| `2026-08-10 12:59:34` | `cowrie.client.kex` |
| `2026-08-10 12:59:35` | `cowrie.login.success` |
| `2026-08-10 12:59:36` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.2[.]182` to AbuseIPDB if not already reported
- [ ] Block `31.173.2[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0405d06082cb

| Field | Detail |
|---|---|
| **Source IP** | `31.41.81[.]65` |
| **First Seen** | 2026-08-10 12:59 |
| **Last Seen** | 2026-08-10 12:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 12:59:46` | `cowrie.session.connect` |
| `2026-08-10 12:59:46` | `cowrie.client.version` |
| `2026-08-10 12:59:46` | `cowrie.client.kex` |
| `2026-08-10 12:59:47` | `cowrie.login.success` |
| `2026-08-10 12:59:47` | `cowrie.direct-tcpip.request` |
| `2026-08-10 12:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.81[.]65` to AbuseIPDB if not already reported
- [ ] Block `31.41.81[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e7328dc4e7

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-10 13:04 |
| **Last Seen** | 2026-08-10 13:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:04:21` | `cowrie.session.connect` |
| `2026-08-10 13:04:22` | `cowrie.client.version` |
| `2026-08-10 13:04:22` | `cowrie.client.kex` |
| `2026-08-10 13:04:23` | `cowrie.login.success` |
| `2026-08-10 13:04:24` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7ba0dbe155

| Field | Detail |
|---|---|
| **Source IP** | `219.129.236[.]174` |
| **First Seen** | 2026-08-10 13:04 |
| **Last Seen** | 2026-08-10 13:04 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:04:34` | `cowrie.session.connect` |
| `2026-08-10 13:04:36` | `cowrie.client.version` |
| `2026-08-10 13:04:36` | `cowrie.client.kex` |
| `2026-08-10 13:04:39` | `cowrie.login.success` |
| `2026-08-10 13:04:41` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.236[.]174` to AbuseIPDB if not already reported
- [ ] Block `219.129.236[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5648877bfe1

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-10 13:10 |
| **Last Seen** | 2026-08-10 13:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:10:37` | `cowrie.session.connect` |
| `2026-08-10 13:10:37` | `cowrie.client.version` |
| `2026-08-10 13:10:37` | `cowrie.client.kex` |
| `2026-08-10 13:10:37` | `cowrie.login.success` |
| `2026-08-10 13:10:37` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:10:37` | `cowrie.direct-tcpip.data` |
| `2026-08-10 13:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df128ef86a8

| Field | Detail |
|---|---|
| **Source IP** | `45.170.50[.]2` |
| **First Seen** | 2026-08-10 13:12 |
| **Last Seen** | 2026-08-10 13:12 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:12:48` | `cowrie.session.connect` |
| `2026-08-10 13:12:48` | `cowrie.client.version` |
| `2026-08-10 13:12:48` | `cowrie.client.kex` |
| `2026-08-10 13:12:50` | `cowrie.login.success` |
| `2026-08-10 13:12:51` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.170.50[.]2` to AbuseIPDB if not already reported
- [ ] Block `45.170.50[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404a1742b344

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 13:16 |
| **Last Seen** | 2026-08-10 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:16:03` | `cowrie.session.connect` |
| `2026-08-10 13:16:03` | `cowrie.client.version` |
| `2026-08-10 13:16:03` | `cowrie.client.kex` |
| `2026-08-10 13:16:04` | `cowrie.login.success` |
| `2026-08-10 13:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73235859ee8

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 13:16 |
| **Last Seen** | 2026-08-10 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:16:03` | `cowrie.session.connect` |
| `2026-08-10 13:16:03` | `cowrie.client.version` |
| `2026-08-10 13:16:04` | `cowrie.client.kex` |
| `2026-08-10 13:16:05` | `cowrie.login.success` |
| `2026-08-10 13:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9926314aa12f

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 13:16 |
| **Last Seen** | 2026-08-10 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:16:09` | `cowrie.session.connect` |
| `2026-08-10 13:16:09` | `cowrie.client.version` |
| `2026-08-10 13:16:09` | `cowrie.client.kex` |
| `2026-08-10 13:16:10` | `cowrie.login.success` |
| `2026-08-10 13:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bacc9848235

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-10 13:16 |
| **Last Seen** | 2026-08-10 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:16:11` | `cowrie.session.connect` |
| `2026-08-10 13:16:11` | `cowrie.client.version` |
| `2026-08-10 13:16:11` | `cowrie.client.kex` |
| `2026-08-10 13:16:12` | `cowrie.login.success` |
| `2026-08-10 13:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd087799132e

| Field | Detail |
|---|---|
| **Source IP** | `47.16.106[.]54` |
| **First Seen** | 2026-08-10 13:30 |
| **Last Seen** | 2026-08-10 13:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:30:45` | `cowrie.session.connect` |
| `2026-08-10 13:30:45` | `cowrie.client.version` |
| `2026-08-10 13:30:45` | `cowrie.client.kex` |
| `2026-08-10 13:30:47` | `cowrie.login.success` |
| `2026-08-10 13:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.16.106[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.16.106[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdecc00b21c3

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-10 13:30 |
| **Last Seen** | 2026-08-10 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:30:48` | `cowrie.session.connect` |
| `2026-08-10 13:30:48` | `cowrie.client.version` |
| `2026-08-10 13:30:48` | `cowrie.client.kex` |
| `2026-08-10 13:30:48` | `cowrie.login.success` |
| `2026-08-10 13:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54056cca44b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.163[.]103` |
| **First Seen** | 2026-08-10 13:33 |
| **Last Seen** | 2026-08-10 13:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:33:38` | `cowrie.session.connect` |
| `2026-08-10 13:33:39` | `cowrie.client.version` |
| `2026-08-10 13:33:39` | `cowrie.client.kex` |
| `2026-08-10 13:33:40` | `cowrie.login.success` |
| `2026-08-10 13:33:40` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.163[.]103` to AbuseIPDB if not already reported
- [ ] Block `65.20.163[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e877bb46000

| Field | Detail |
|---|---|
| **Source IP** | `45.55.133[.]80` |
| **First Seen** | 2026-08-10 13:33 |
| **Last Seen** | 2026-08-10 13:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:33:52` | `cowrie.session.connect` |
| `2026-08-10 13:33:52` | `cowrie.client.version` |
| `2026-08-10 13:33:52` | `cowrie.client.kex` |
| `2026-08-10 13:33:53` | `cowrie.login.success` |
| `2026-08-10 13:33:53` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.55.133[.]80` to AbuseIPDB if not already reported
- [ ] Block `45.55.133[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba81c143e93d

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-10 13:33 |
| **Last Seen** | 2026-08-10 13:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:33:58` | `cowrie.session.connect` |
| `2026-08-10 13:33:59` | `cowrie.client.version` |
| `2026-08-10 13:33:59` | `cowrie.client.kex` |
| `2026-08-10 13:34:00` | `cowrie.login.success` |
| `2026-08-10 13:34:01` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456141b052db

| Field | Detail |
|---|---|
| **Source IP** | `43.106.81[.]238` |
| **First Seen** | 2026-08-10 13:36 |
| **Last Seen** | 2026-08-10 13:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:36:58` | `cowrie.session.connect` |
| `2026-08-10 13:36:58` | `cowrie.client.version` |
| `2026-08-10 13:36:58` | `cowrie.client.kex` |
| `2026-08-10 13:36:59` | `cowrie.login.success` |
| `2026-08-10 13:37:00` | `cowrie.session.params` |
| `2026-08-10 13:37:00` | `cowrie.command.input` |
| `2026-08-10 13:37:00` | `cowrie.log.closed` |
| `2026-08-10 13:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.106.81[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.106.81[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2224c157fc4

| Field | Detail |
|---|---|
| **Source IP** | `62.201.212[.]54` |
| **First Seen** | 2026-08-10 13:39 |
| **Last Seen** | 2026-08-10 13:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:39:10` | `cowrie.session.connect` |
| `2026-08-10 13:39:11` | `cowrie.client.version` |
| `2026-08-10 13:39:11` | `cowrie.client.kex` |
| `2026-08-10 13:39:12` | `cowrie.login.success` |
| `2026-08-10 13:39:12` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.212[.]54` to AbuseIPDB if not already reported
- [ ] Block `62.201.212[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9c3ab96bc65

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-08-10 13:39 |
| **Last Seen** | 2026-08-10 13:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:39:22` | `cowrie.session.connect` |
| `2026-08-10 13:39:22` | `cowrie.client.version` |
| `2026-08-10 13:39:22` | `cowrie.client.kex` |
| `2026-08-10 13:39:24` | `cowrie.login.success` |
| `2026-08-10 13:39:24` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ef5e5516dd

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-08-10 13:44 |
| **Last Seen** | 2026-08-10 13:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:44:22` | `cowrie.session.connect` |
| `2026-08-10 13:44:23` | `cowrie.client.version` |
| `2026-08-10 13:44:23` | `cowrie.client.kex` |
| `2026-08-10 13:44:25` | `cowrie.login.success` |
| `2026-08-10 13:44:26` | `cowrie.direct-tcpip.request` |
| `2026-08-10 13:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b05f54f771f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 13:44 |
| **Last Seen** | 2026-08-10 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:44:30` | `cowrie.session.connect` |
| `2026-08-10 13:44:30` | `cowrie.client.version` |
| `2026-08-10 13:44:30` | `cowrie.client.kex` |
| `2026-08-10 13:44:30` | `cowrie.login.success` |
| `2026-08-10 13:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1ed4f2d803

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 13:44 |
| **Last Seen** | 2026-08-10 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:44:30` | `cowrie.session.connect` |
| `2026-08-10 13:44:30` | `cowrie.client.version` |
| `2026-08-10 13:44:30` | `cowrie.client.kex` |
| `2026-08-10 13:44:30` | `cowrie.login.success` |
| `2026-08-10 13:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a37e12ca5276

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 13:44 |
| **Last Seen** | 2026-08-10 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:44:32` | `cowrie.session.connect` |
| `2026-08-10 13:44:32` | `cowrie.client.version` |
| `2026-08-10 13:44:32` | `cowrie.client.kex` |
| `2026-08-10 13:44:32` | `cowrie.login.success` |
| `2026-08-10 13:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16a79659d92

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-10 13:44 |
| **Last Seen** | 2026-08-10 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 13:44:32` | `cowrie.session.connect` |
| `2026-08-10 13:44:32` | `cowrie.client.version` |
| `2026-08-10 13:44:32` | `cowrie.client.kex` |
| `2026-08-10 13:44:32` | `cowrie.login.success` |
| `2026-08-10 13:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e70f65c9a99

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-10 14:01 |
| **Last Seen** | 2026-08-10 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:01:53` | `cowrie.session.connect` |
| `2026-08-10 14:01:53` | `cowrie.client.version` |
| `2026-08-10 14:01:53` | `cowrie.client.kex` |
| `2026-08-10 14:01:54` | `cowrie.login.success` |
| `2026-08-10 14:01:54` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:01:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-10 14:01:54` | `cowrie.direct-tcpip.data` |
| `2026-08-10 14:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85967de50c8

| Field | Detail |
|---|---|
| **Source IP** | `202.138.229[.]190` |
| **First Seen** | 2026-08-10 14:03 |
| **Last Seen** | 2026-08-10 14:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:03:58` | `cowrie.session.connect` |
| `2026-08-10 14:03:59` | `cowrie.client.version` |
| `2026-08-10 14:03:59` | `cowrie.client.kex` |
| `2026-08-10 14:04:01` | `cowrie.login.success` |
| `2026-08-10 14:04:02` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.138.229[.]190` to AbuseIPDB if not already reported
- [ ] Block `202.138.229[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94c3a4ac9ad

| Field | Detail |
|---|---|
| **Source IP** | `125.36.68[.]227` |
| **First Seen** | 2026-08-10 14:04 |
| **Last Seen** | 2026-08-10 14:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:04:07` | `cowrie.session.connect` |
| `2026-08-10 14:04:08` | `cowrie.client.version` |
| `2026-08-10 14:04:08` | `cowrie.client.kex` |
| `2026-08-10 14:04:10` | `cowrie.login.success` |
| `2026-08-10 14:04:12` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.36.68[.]227` to AbuseIPDB if not already reported
- [ ] Block `125.36.68[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbac6ba9b8ee

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-08-10 14:08 |
| **Last Seen** | 2026-08-10 14:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:08:16` | `cowrie.session.connect` |
| `2026-08-10 14:08:17` | `cowrie.client.version` |
| `2026-08-10 14:08:17` | `cowrie.client.kex` |
| `2026-08-10 14:08:19` | `cowrie.login.success` |
| `2026-08-10 14:08:20` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec40f87a72e7

| Field | Detail |
|---|---|
| **Source IP** | `183.56.192[.]210` |
| **First Seen** | 2026-08-10 14:11 |
| **Last Seen** | 2026-08-10 14:11 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:11:19` | `cowrie.session.connect` |
| `2026-08-10 14:11:19` | `cowrie.client.version` |
| `2026-08-10 14:11:19` | `cowrie.client.kex` |
| `2026-08-10 14:11:42` | `cowrie.login.success` |
| `2026-08-10 14:11:44` | `cowrie.session.params` |
| `2026-08-10 14:11:44` | `cowrie.command.input` |
| `2026-08-10 14:11:44` | `cowrie.log.closed` |
| `2026-08-10 14:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.56.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `183.56.192[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7faf8bd509f

| Field | Detail |
|---|---|
| **Source IP** | `23.30.11[.]253` |
| **First Seen** | 2026-08-10 14:18 |
| **Last Seen** | 2026-08-10 14:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:18:50` | `cowrie.session.connect` |
| `2026-08-10 14:18:51` | `cowrie.client.version` |
| `2026-08-10 14:18:51` | `cowrie.client.kex` |
| `2026-08-10 14:18:52` | `cowrie.login.success` |
| `2026-08-10 14:18:52` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.30.11[.]253` to AbuseIPDB if not already reported
- [ ] Block `23.30.11[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e4a44d075b

| Field | Detail |
|---|---|
| **Source IP** | `31.173.29[.]136` |
| **First Seen** | 2026-08-10 14:22 |
| **Last Seen** | 2026-08-10 14:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:22:05` | `cowrie.session.connect` |
| `2026-08-10 14:22:05` | `cowrie.client.version` |
| `2026-08-10 14:22:05` | `cowrie.client.kex` |
| `2026-08-10 14:22:07` | `cowrie.login.success` |
| `2026-08-10 14:22:07` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.29[.]136` to AbuseIPDB if not already reported
- [ ] Block `31.173.29[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57eebc1d1c29

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:33 |
| **Last Seen** | 2026-08-10 14:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:33:49` | `cowrie.session.connect` |
| `2026-08-10 14:33:49` | `cowrie.client.version` |
| `2026-08-10 14:33:49` | `cowrie.client.kex` |
| `2026-08-10 14:33:53` | `cowrie.login.success` |
| `2026-08-10 14:33:55` | `cowrie.session.params` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.success` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.command.input` |
| `2026-08-10 14:33:55` | `cowrie.log.closed` |
| `2026-08-10 14:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c55a295caa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:36 |
| **Last Seen** | 2026-08-10 14:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:36:00` | `cowrie.session.connect` |
| `2026-08-10 14:36:00` | `cowrie.client.version` |
| `2026-08-10 14:36:00` | `cowrie.client.kex` |
| `2026-08-10 14:36:03` | `cowrie.login.success` |
| `2026-08-10 14:36:04` | `cowrie.session.params` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.success` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:04` | `cowrie.command.input` |
| `2026-08-10 14:36:05` | `cowrie.log.closed` |
| `2026-08-10 14:36:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6bb158d5c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:38 |
| **Last Seen** | 2026-08-10 14:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:38:08` | `cowrie.session.connect` |
| `2026-08-10 14:38:08` | `cowrie.client.version` |
| `2026-08-10 14:38:08` | `cowrie.client.kex` |
| `2026-08-10 14:38:10` | `cowrie.login.success` |
| `2026-08-10 14:38:12` | `cowrie.session.params` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.success` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.command.input` |
| `2026-08-10 14:38:12` | `cowrie.log.closed` |
| `2026-08-10 14:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66aba4f09a02

| Field | Detail |
|---|---|
| **Source IP** | `81.214.75[.]248` |
| **First Seen** | 2026-08-10 14:38 |
| **Last Seen** | 2026-08-10 14:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:38:28` | `cowrie.session.connect` |
| `2026-08-10 14:38:28` | `cowrie.client.version` |
| `2026-08-10 14:38:28` | `cowrie.client.kex` |
| `2026-08-10 14:38:29` | `cowrie.login.success` |
| `2026-08-10 14:38:29` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.214.75[.]248` to AbuseIPDB if not already reported
- [ ] Block `81.214.75[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c7f419f036c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:40 |
| **Last Seen** | 2026-08-10 14:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:40:15` | `cowrie.session.connect` |
| `2026-08-10 14:40:15` | `cowrie.client.version` |
| `2026-08-10 14:40:15` | `cowrie.client.kex` |
| `2026-08-10 14:40:17` | `cowrie.login.success` |
| `2026-08-10 14:40:18` | `cowrie.session.params` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.success` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:18` | `cowrie.command.input` |
| `2026-08-10 14:40:19` | `cowrie.log.closed` |
| `2026-08-10 14:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b26a688991a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:42 |
| **Last Seen** | 2026-08-10 14:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:42:21` | `cowrie.session.connect` |
| `2026-08-10 14:42:22` | `cowrie.client.version` |
| `2026-08-10 14:42:22` | `cowrie.client.kex` |
| `2026-08-10 14:42:23` | `cowrie.login.success` |
| `2026-08-10 14:42:25` | `cowrie.session.params` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.success` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.command.input` |
| `2026-08-10 14:42:25` | `cowrie.log.closed` |
| `2026-08-10 14:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b682591b9d

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-08-10 14:43 |
| **Last Seen** | 2026-08-10 14:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:43:06` | `cowrie.session.connect` |
| `2026-08-10 14:43:06` | `cowrie.client.version` |
| `2026-08-10 14:43:06` | `cowrie.client.kex` |
| `2026-08-10 14:43:07` | `cowrie.login.success` |
| `2026-08-10 14:43:07` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c96ed43e20b

| Field | Detail |
|---|---|
| **Source IP** | `200.222.71[.]218` |
| **First Seen** | 2026-08-10 14:43 |
| **Last Seen** | 2026-08-10 14:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:43:17` | `cowrie.session.connect` |
| `2026-08-10 14:43:17` | `cowrie.client.version` |
| `2026-08-10 14:43:17` | `cowrie.client.kex` |
| `2026-08-10 14:43:19` | `cowrie.login.success` |
| `2026-08-10 14:43:19` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.222.71[.]218` to AbuseIPDB if not already reported
- [ ] Block `200.222.71[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1697b23efe09

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:46 |
| **Last Seen** | 2026-08-10 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:46:32` | `cowrie.session.connect` |
| `2026-08-10 14:46:33` | `cowrie.client.version` |
| `2026-08-10 14:46:33` | `cowrie.client.kex` |
| `2026-08-10 14:46:34` | `cowrie.login.success` |
| `2026-08-10 14:46:35` | `cowrie.session.params` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.success` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.command.input` |
| `2026-08-10 14:46:35` | `cowrie.log.closed` |
| `2026-08-10 14:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cbcf047a87b

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-08-10 14:48 |
| **Last Seen** | 2026-08-10 14:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:48:00` | `cowrie.session.connect` |
| `2026-08-10 14:48:00` | `cowrie.client.version` |
| `2026-08-10 14:48:00` | `cowrie.client.kex` |
| `2026-08-10 14:48:01` | `cowrie.login.success` |
| `2026-08-10 14:48:01` | `cowrie.direct-tcpip.request` |
| `2026-08-10 14:48:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b09b1fa450a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:48 |
| **Last Seen** | 2026-08-10 14:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:48:39` | `cowrie.session.connect` |
| `2026-08-10 14:48:39` | `cowrie.client.version` |
| `2026-08-10 14:48:39` | `cowrie.client.kex` |
| `2026-08-10 14:48:40` | `cowrie.login.success` |
| `2026-08-10 14:48:41` | `cowrie.session.params` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.success` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.command.input` |
| `2026-08-10 14:48:41` | `cowrie.log.closed` |
| `2026-08-10 14:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb7f4db0de9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:50 |
| **Last Seen** | 2026-08-10 14:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:50:45` | `cowrie.session.connect` |
| `2026-08-10 14:50:45` | `cowrie.client.version` |
| `2026-08-10 14:50:45` | `cowrie.client.kex` |
| `2026-08-10 14:50:46` | `cowrie.login.success` |
| `2026-08-10 14:50:48` | `cowrie.session.params` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.success` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.command.input` |
| `2026-08-10 14:50:48` | `cowrie.log.closed` |
| `2026-08-10 14:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6157349e3f0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-10 14:52 |
| **Last Seen** | 2026-08-10 14:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-10 14:52:53` | `cowrie.session.connect` |
| `2026-08-10 14:52:53` | `cowrie.client.version` |
| `2026-08-10 14:52:53` | `cowrie.client.kex` |
| `2026-08-10 14:52:54` | `cowrie.login.success` |
| `2026-08-10 14:52:55` | `cowrie.session.params` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.success` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.command.input` |
| `2026-08-10 14:52:55` | `cowrie.log.closed` |
| `2026-08-10 14:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **43** | 2026-08-10 13:00 | 2026-08-10 14:54 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **20** | 2026-08-10 12:57 | 2026-08-10 14:50 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-10 13:12 | 2026-08-10 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **3** | 2026-08-10 13:10 | 2026-08-10 14:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-10 14:40 | 2026-08-10 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-10 14:16 | 2026-08-10 14:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]132` | **3** | 2026-08-10 12:57 | 2026-08-10 12:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]205` | **3** | 2026-08-10 12:58 | 2026-08-10 12:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]89` | **3** | 2026-08-10 12:57 | 2026-08-10 12:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-10 13:16 | 2026-08-10 13:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.89.125[.]252` | **2** | 2026-08-10 14:03 | 2026-08-10 14:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.46.231[.]114` | **2** | 2026-08-10 14:29 | 2026-08-10 14:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.189.81[.]101` | **2** | 2026-08-10 14:27 | 2026-08-10 14:29 | 2m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-08-10 14:27 | 2026-08-10 14:44 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.49[.]182` | 1 | 2026-08-10 14:08 | 2026-08-10 14:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `183.56.192[.]210` | 1 | 2026-08-10 14:11 | 2026-08-10 14:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.242.97[.]72` | 1 | 2026-08-10 13:00 | 2026-08-10 13:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `194.88.220[.]23` | 1 | 2026-08-10 13:12 | 2026-08-10 13:12 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.134.195[.]155` | 1 | 2026-08-10 14:32 | 2026-08-10 14:32 | 11s | 0 | `T1592` | 🟢 LOW |
| `24.125.88[.]192` | 1 | 2026-08-10 13:01 | 2026-08-10 13:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `43.106.81[.]238` | 1 | 2026-08-10 13:36 | 2026-08-10 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.14.28[.]30` | 1 | 2026-08-10 14:00 | 2026-08-10 14:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]38` | 1 | 2026-08-10 13:03 | 2026-08-10 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]209` | 1 | 2026-08-10 14:48 | 2026-08-10 14:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-10 14:36 | 2026-08-10 14:37 | 63s | 0 | `T1592` | 🟢 LOW |

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
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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
| `66.132.172[.]209` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `124.67.120[.]106` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `62.201.212[.]54` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `220.122.115[.]9` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `200.222.71[.]218` | BR | V tal | **100** ⚠️ | 50 |
| `88.214.25[.]123` | DE | VDS&VPN services | **100** ⚠️ | 50 |
| `31.41.81[.]65` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `66.132.172[.]205` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `194.165.16[.]123` | LT | Flyservers S.A. | **100** ⚠️ | 11 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 45 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 9 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 9 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 9 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 173 cases |
| Tool 34  | Credential Extractor        | ✅ 52 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (12.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 45 priority case(s) shown individually · 25 recon entry/entries in table (14 group(s) consolidating 96 session(s)).

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
_Report time: 2026-08-10T15:01:52Z_

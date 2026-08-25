# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-25 |
| **Generated At** | 2026-08-25T10:37:19Z |
| **Shift Time** | 10:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **182** |
| Confirmed Threats | **169** |
| False Positives Filtered | **13** (7.1%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **17** |
| High Severity Cases | **132** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **2** HIGH · **20** MED · 22 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **141** |
| Unique Credential Pairs | **131** |
| Unique Usernames | **11** |
| Unique Passwords | **96** |
| Successful Auth Pairs | **134** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `ubuntu` | 21 |
| `admin` | 17 |
| `user` | 14 |
| `test` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 9 |
| `123456` | 9 |
| `qwerty` | 8 |
| `admin` | 4 |
| `support` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 4 |
| `root` | `` | 4 |
| `admin` | `admin` | 3 |
| `root` | `﻿------fuck------` | 2 |
| `pi` | `abcd1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root123` | `2.57.122.150` | 2026-08-25T06:55:33 |
| `root` | `alpine` | `2.57.122.150` | 2026-08-25T06:56:44 |
| `root` | `changeme` | `2.57.122.150` | 2026-08-25T06:57:55 |
| `root` | `default` | `2.57.122.150` | 2026-08-25T06:59:05 |
| `root` | `r00t` | `2.57.122.150` | 2026-08-25T07:00:16 |
| `root` | `root@123` | `2.57.122.150` | 2026-08-25T07:01:23 |
| `ubuntu` | `it@2024` | `217.60.255.130` | 2026-08-25T07:02:10 |
| `root` | `P@$$w0rd2025` | `217.60.255.130` | 2026-08-25T07:02:14 |
| `root` | `Root123` | `2.57.122.150` | 2026-08-25T07:02:30 |
| `root` | `!root` | `2.57.122.150` | 2026-08-25T07:03:37 |
| `root` | `rootme` | `2.57.122.150` | 2026-08-25T07:04:44 |
| `admin` | `admin` | `2.57.122.150` | 2026-08-25T07:05:47 |
| `admin` | `password` | `2.57.122.150` | 2026-08-25T07:06:53 |
| `admin` | `123456` | `2.57.122.150` | 2026-08-25T07:08:02 |
| `admin` | `admin123` | `2.57.122.150` | 2026-08-25T07:09:10 |
| `admin` | `letmein` | `2.57.122.150` | 2026-08-25T07:10:24 |
| `admin` | `qwerty` | `2.57.122.150` | 2026-08-25T07:11:39 |
| `ubuntu` | `odoo@123` | `217.60.255.130` | 2026-08-25T07:11:51 |
| `root` | `!qaz2w` | `217.60.255.130` | 2026-08-25T07:11:55 |
| `admin` | `12345` | `2.57.122.150` | 2026-08-25T07:12:44 |
| `admin` | `admin@123` | `2.57.122.150` | 2026-08-25T07:13:47 |
| `admin` | `Admin123` | `2.57.122.150` | 2026-08-25T07:14:50 |
| `admin` | `P@ssw0rd` | `2.57.122.150` | 2026-08-25T07:15:52 |
| `support` | `support` | `176.53.159.196` | 2026-08-25T07:16:32 |
| `admin` | `welcome` | `2.57.122.150` | 2026-08-25T07:16:52 |
| `admin` | `passw0rd` | `2.57.122.150` | 2026-08-25T07:17:55 |
| `admin` | `administrator` | `2.57.122.150` | 2026-08-25T07:19:02 |
| `admin` | `adminroot` | `2.57.122.150` | 2026-08-25T07:20:10 |
| `admin` | `adminadmin` | `2.57.122.150` | 2026-08-25T07:21:24 |
| `ubuntu` | `Temp@1234` | `217.60.255.130` | 2026-08-25T07:21:41 |
| `root` | `ubnt@123` | `217.60.255.130` | 2026-08-25T07:21:48 |
| `user` | `user` | `2.57.122.150` | 2026-08-25T07:22:37 |
| `user` | `password` | `2.57.122.150` | 2026-08-25T07:23:41 |
| `user` | `123456` | `2.57.122.150` | 2026-08-25T07:24:45 |
| `user` | `qwerty` | `2.57.122.150` | 2026-08-25T07:25:48 |
| `user` | `12345` | `2.57.122.150` | 2026-08-25T07:26:53 |
| `user` | `letmein` | `2.57.122.150` | 2026-08-25T07:28:00 |
| `user` | `welcome` | `2.57.122.150` | 2026-08-25T07:29:14 |
| `user` | `passw0rd` | `2.57.122.150` | 2026-08-25T07:30:30 |
| `ubuntu` | `P@$$w0rd1234` | `217.60.255.130` | 2026-08-25T07:31:13 |
| `root` | `P@ssw0rd#1234` | `217.60.255.130` | 2026-08-25T07:31:20 |
| `user` | `user123` | `2.57.122.150` | 2026-08-25T07:31:42 |
| `user` | `user1` | `2.57.122.150` | 2026-08-25T07:32:44 |
| `user` | `userpass` | `2.57.122.150` | 2026-08-25T07:33:45 |
| `user` | `user@123` | `2.57.122.150` | 2026-08-25T07:34:45 |
| `user` | `User123` | `2.57.122.150` | 2026-08-25T07:35:45 |
| `admin` | `admin` | `8.215.69.55` | 2026-08-25T07:36:36 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-25T07:36:40 |
| `user` | `guest` | `2.57.122.150` | 2026-08-25T07:36:46 |
| `test` | `test` | `2.57.122.150` | 2026-08-25T07:37:52 |
| `test` | `password` | `2.57.122.150` | 2026-08-25T07:39:00 |
| `test` | `123456` | `2.57.122.150` | 2026-08-25T07:40:11 |
| `ubuntu` | `Pa$$w0rd12345` | `217.60.255.130` | 2026-08-25T07:40:51 |
| `root` | `ok123` | `217.60.255.130` | 2026-08-25T07:40:56 |
| `support` | `support` | `10.0.0.73` | 2026-08-25T07:41:24 |
| `test` | `test123` | `2.57.122.150` | 2026-08-25T07:41:25 |
| `test` | `qwerty` | `2.57.122.150` | 2026-08-25T07:42:47 |
| `test` | `12345` | `2.57.122.150` | 2026-08-25T07:43:56 |
| `test` | `test@123` | `2.57.122.150` | 2026-08-25T07:44:58 |
| `test` | `Test123` | `2.57.122.150` | 2026-08-25T07:45:57 |
| `test` | `testing` | `2.57.122.150` | 2026-08-25T07:46:55 |
| `test` | `tester` | `2.57.122.150` | 2026-08-25T07:47:55 |
| `test` | `testpass` | `2.57.122.150` | 2026-08-25T07:48:56 |
| `guest` | `guest` | `2.57.122.150` | 2026-08-25T07:49:59 |
| `ubuntu` | `Test@123!` | `217.60.255.130` | 2026-08-25T07:50:24 |
| `root` | `P@ssword@2025` | `217.60.255.130` | 2026-08-25T07:50:27 |
| `guest` | `password` | `2.57.122.150` | 2026-08-25T07:51:07 |
| `guest` | `123456` | `2.57.122.150` | 2026-08-25T07:52:17 |
| `guest` | `qwerty` | `2.57.122.150` | 2026-08-25T07:53:29 |
| `guest` | `welcome` | `2.57.122.150` | 2026-08-25T07:54:42 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-25T07:55:48 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-25T07:55:48 |
| `guest` | `guest123` | `2.57.122.150` | 2026-08-25T07:55:59 |
| `guest` | `guestpass` | `2.57.122.150` | 2026-08-25T07:57:14 |
| `guest` | `guest@123` | `2.57.122.150` | 2026-08-25T07:58:16 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-25T07:59:12 |
| `guest` | `Guest123` | `2.57.122.150` | 2026-08-25T07:59:14 |
| `ubuntu` | `Zxcvbnm@1234` | `217.60.255.130` | 2026-08-25T07:59:53 |
| `root` | `Power@123` | `217.60.255.130` | 2026-08-25T07:59:57 |
| `guest` | `anonymous` | `2.57.122.150` | 2026-08-25T08:00:11 |
| `ubuntu` | `ubuntu` | `2.57.122.150` | 2026-08-25T08:01:11 |
| `ubuntu` | `password` | `2.57.122.150` | 2026-08-25T08:02:12 |
| `ubuntu` | `ubuntu123` | `2.57.122.150` | 2026-08-25T08:03:15 |
| `ubuntu` | `ubuntu1` | `2.57.122.150` | 2026-08-25T08:04:19 |
| `ubuntu` | `ubuntu@123` | `2.57.122.150` | 2026-08-25T08:05:23 |
| `ubuntu` | `Ubuntu123` | `2.57.122.150` | 2026-08-25T08:06:27 |
| `ubuntu` | `changeme` | `2.57.122.150` | 2026-08-25T08:07:34 |
| `ubuntu` | `123456` | `2.57.122.150` | 2026-08-25T08:08:44 |
| `ubuntu` | `weblogic@123` | `217.60.255.130` | 2026-08-25T08:09:32 |
| `root` | `ABC123abc` | `217.60.255.130` | 2026-08-25T08:09:36 |
| `ubuntu` | `qwerty` | `2.57.122.150` | 2026-08-25T08:09:54 |
| `pi` | `raspberry` | `2.57.122.150` | 2026-08-25T08:11:06 |
| `pi` | `password` | `2.57.122.150` | 2026-08-25T08:12:16 |
| `pi` | `raspberrypi` | `2.57.122.150` | 2026-08-25T08:13:29 |
| `pi` | `123456` | `2.57.122.150` | 2026-08-25T08:14:41 |
| `pi` | `qwerty` | `2.57.122.150` | 2026-08-25T08:15:49 |
| `pi` | `pi123` | `2.57.122.150` | 2026-08-25T08:16:56 |
| `pi` | `rasp` | `2.57.122.150` | 2026-08-25T08:18:05 |
| `ubuntu` | `jenkins#123` | `217.60.255.130` | 2026-08-25T08:19:01 |
| `root` | `1234.abcd` | `217.60.255.130` | 2026-08-25T08:19:05 |
| `pi` | `pihole` | `2.57.122.150` | 2026-08-25T08:19:14 |
| `pi` | `p@ssw0rd` | `2.57.122.150` | 2026-08-25T08:20:28 |
| `oracle` | `oracle` | `2.57.122.150` | 2026-08-25T08:21:46 |
| `oracle` | `password` | `2.57.122.150` | 2026-08-25T08:23:05 |
| `oracle` | `123456` | `2.57.122.150` | 2026-08-25T08:24:25 |
| `oracle` | `oracle123` | `2.57.122.150` | 2026-08-25T08:25:40 |
| `root` | `﻿------fuck------` | `222.88.163.202` | 2026-08-25T08:25:48 |
| `oracle` | `oracle1` | `2.57.122.150` | 2026-08-25T08:26:43 |
| `oracle` | `oracle@123` | `2.57.122.150` | 2026-08-25T08:27:45 |
| `ubuntu` | `appuser@123` | `217.60.255.130` | 2026-08-25T08:28:29 |
| `root` | `guest123` | `217.60.255.130` | 2026-08-25T08:28:33 |
| `oracle` | `Oracle123` | `2.57.122.150` | 2026-08-25T08:28:49 |
| `oracle` | `welcome` | `2.57.122.150` | 2026-08-25T08:29:55 |
| `oracle` | `qwerty` | `2.57.122.150` | 2026-08-25T08:31:05 |
| `postgres` | `postgres` | `2.57.122.150` | 2026-08-25T08:32:18 |
| `postgres` | `password` | `2.57.122.150` | 2026-08-25T08:33:33 |
| `postgres` | `123456` | `2.57.122.150` | 2026-08-25T08:34:52 |
| `postgres` | `postgres123` | `2.57.122.150` | 2026-08-25T08:36:10 |
| `postgres` | `postgres1` | `2.57.122.150` | 2026-08-25T08:37:26 |
| `ubuntu` | `P@$$w0rd12345` | `217.60.255.130` | 2026-08-25T08:38:18 |
| `root` | `steam@2024` | `217.60.255.130` | 2026-08-25T08:38:22 |
| `postgres` | `postgres@123` | `2.57.122.150` | 2026-08-25T08:38:38 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-25T08:38:40 |
| `postgres` | `Postgres123` | `2.57.122.150` | 2026-08-25T08:39:52 |
| `postgres` | `qwerty` | `2.57.122.150` | 2026-08-25T08:41:09 |
| `postgres` | `admin` | `2.57.122.150` | 2026-08-25T08:42:27 |
| `ftp` | `ftp` | `2.57.122.150` | 2026-08-25T08:43:44 |
| `ftp` | `password` | `2.57.122.150` | 2026-08-25T08:45:00 |
| `ftp` | `123456` | `2.57.122.150` | 2026-08-25T08:46:18 |
| `ftp` | `ftp123` | `2.57.122.150` | 2026-08-25T08:47:36 |
| `ubuntu` | `debian@123` | `217.60.255.130` | 2026-08-25T08:48:03 |
| `root` | `kafka@2024` | `217.60.255.130` | 2026-08-25T08:48:05 |
| `ftp` | `ftpuser` | `2.57.122.150` | 2026-08-25T08:48:52 |
| `ftp` | `anonymous` | `2.57.122.150` | 2026-08-25T08:50:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **182** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 107 |
| libssh | 32 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 101 | 1 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 101 | 1 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 101 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `2.57.122.150`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **28** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS13188` | CONTENT DELIVERY NETWORK LTD | 1 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | HIGH |
| `AS50392` | CAMPUS RV | 1 | LOW |
| `AS396982` | Google LLC | 1 | LOW |
| `AS262958` | JG CARRARO TELECOM LTDA | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (132)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-42d386e1ea0d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:55 |
| **Last Seen** | 2026-08-25 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:55:32` | `cowrie.session.connect` |
| `2026-08-25 06:55:32` | `cowrie.client.version` |
| `2026-08-25 06:55:32` | `cowrie.client.kex` |
| `2026-08-25 06:55:33` | `cowrie.login.success` |
| `2026-08-25 06:55:34` | `cowrie.session.params` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.success` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:34` | `cowrie.command.input` |
| `2026-08-25 06:55:35` | `cowrie.log.closed` |
| `2026-08-25 06:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c22df6fd9a7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:56 |
| **Last Seen** | 2026-08-25 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:56:43` | `cowrie.session.connect` |
| `2026-08-25 06:56:43` | `cowrie.client.version` |
| `2026-08-25 06:56:43` | `cowrie.client.kex` |
| `2026-08-25 06:56:44` | `cowrie.login.success` |
| `2026-08-25 06:56:45` | `cowrie.session.params` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.success` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:45` | `cowrie.command.input` |
| `2026-08-25 06:56:46` | `cowrie.log.closed` |
| `2026-08-25 06:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d1fcab3bb7e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:57 |
| **Last Seen** | 2026-08-25 06:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:57:54` | `cowrie.session.connect` |
| `2026-08-25 06:57:54` | `cowrie.client.version` |
| `2026-08-25 06:57:54` | `cowrie.client.kex` |
| `2026-08-25 06:57:55` | `cowrie.login.success` |
| `2026-08-25 06:57:57` | `cowrie.session.params` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.success` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.command.input` |
| `2026-08-25 06:57:57` | `cowrie.log.closed` |
| `2026-08-25 06:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c54472fcc4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 06:59 |
| **Last Seen** | 2026-08-25 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 06:59:04` | `cowrie.session.connect` |
| `2026-08-25 06:59:05` | `cowrie.client.version` |
| `2026-08-25 06:59:05` | `cowrie.client.kex` |
| `2026-08-25 06:59:05` | `cowrie.login.success` |
| `2026-08-25 06:59:07` | `cowrie.session.params` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.success` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.command.input` |
| `2026-08-25 06:59:07` | `cowrie.log.closed` |
| `2026-08-25 06:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fda02e58e3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:00 |
| **Last Seen** | 2026-08-25 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:00:15` | `cowrie.session.connect` |
| `2026-08-25 07:00:15` | `cowrie.client.version` |
| `2026-08-25 07:00:15` | `cowrie.client.kex` |
| `2026-08-25 07:00:16` | `cowrie.login.success` |
| `2026-08-25 07:00:18` | `cowrie.session.params` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.success` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.command.input` |
| `2026-08-25 07:00:18` | `cowrie.log.closed` |
| `2026-08-25 07:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c894c3e6072

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:01 |
| **Last Seen** | 2026-08-25 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:01:22` | `cowrie.session.connect` |
| `2026-08-25 07:01:22` | `cowrie.client.version` |
| `2026-08-25 07:01:22` | `cowrie.client.kex` |
| `2026-08-25 07:01:23` | `cowrie.login.success` |
| `2026-08-25 07:01:24` | `cowrie.session.params` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.success` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:24` | `cowrie.command.input` |
| `2026-08-25 07:01:25` | `cowrie.log.closed` |
| `2026-08-25 07:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa7438385ba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:02 |
| **Last Seen** | 2026-08-25 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:02:09` | `cowrie.session.connect` |
| `2026-08-25 07:02:09` | `cowrie.client.version` |
| `2026-08-25 07:02:09` | `cowrie.client.kex` |
| `2026-08-25 07:02:10` | `cowrie.login.success` |
| `2026-08-25 07:02:10` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:02:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:02:10` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52358378771

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:02 |
| **Last Seen** | 2026-08-25 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:02:13` | `cowrie.session.connect` |
| `2026-08-25 07:02:13` | `cowrie.client.version` |
| `2026-08-25 07:02:13` | `cowrie.client.kex` |
| `2026-08-25 07:02:14` | `cowrie.login.success` |
| `2026-08-25 07:02:14` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:02:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:02:14` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1207bc21e9b1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:02 |
| **Last Seen** | 2026-08-25 07:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:02:28` | `cowrie.session.connect` |
| `2026-08-25 07:02:29` | `cowrie.client.version` |
| `2026-08-25 07:02:29` | `cowrie.client.kex` |
| `2026-08-25 07:02:30` | `cowrie.login.success` |
| `2026-08-25 07:02:31` | `cowrie.session.params` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.success` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:31` | `cowrie.command.input` |
| `2026-08-25 07:02:32` | `cowrie.log.closed` |
| `2026-08-25 07:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50493458553c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:03 |
| **Last Seen** | 2026-08-25 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:03:36` | `cowrie.session.connect` |
| `2026-08-25 07:03:36` | `cowrie.client.version` |
| `2026-08-25 07:03:36` | `cowrie.client.kex` |
| `2026-08-25 07:03:37` | `cowrie.login.success` |
| `2026-08-25 07:03:38` | `cowrie.session.params` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.success` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:38` | `cowrie.command.input` |
| `2026-08-25 07:03:39` | `cowrie.log.closed` |
| `2026-08-25 07:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f7ccd87f0b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:04 |
| **Last Seen** | 2026-08-25 07:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:04:42` | `cowrie.session.connect` |
| `2026-08-25 07:04:42` | `cowrie.client.version` |
| `2026-08-25 07:04:42` | `cowrie.client.kex` |
| `2026-08-25 07:04:44` | `cowrie.login.success` |
| `2026-08-25 07:04:45` | `cowrie.session.params` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.success` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.command.input` |
| `2026-08-25 07:04:45` | `cowrie.log.closed` |
| `2026-08-25 07:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5499c12f74a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:05 |
| **Last Seen** | 2026-08-25 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:05:46` | `cowrie.session.connect` |
| `2026-08-25 07:05:46` | `cowrie.client.version` |
| `2026-08-25 07:05:46` | `cowrie.client.kex` |
| `2026-08-25 07:05:47` | `cowrie.login.success` |
| `2026-08-25 07:05:49` | `cowrie.session.params` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.success` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.command.input` |
| `2026-08-25 07:05:49` | `cowrie.log.closed` |
| `2026-08-25 07:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7cd2bfa35e8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:06 |
| **Last Seen** | 2026-08-25 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:06:52` | `cowrie.session.connect` |
| `2026-08-25 07:06:52` | `cowrie.client.version` |
| `2026-08-25 07:06:52` | `cowrie.client.kex` |
| `2026-08-25 07:06:53` | `cowrie.login.success` |
| `2026-08-25 07:06:54` | `cowrie.session.params` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.success` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:54` | `cowrie.command.input` |
| `2026-08-25 07:06:55` | `cowrie.log.closed` |
| `2026-08-25 07:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454cfb7b3e9a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:08 |
| **Last Seen** | 2026-08-25 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:08:01` | `cowrie.session.connect` |
| `2026-08-25 07:08:01` | `cowrie.client.version` |
| `2026-08-25 07:08:01` | `cowrie.client.kex` |
| `2026-08-25 07:08:02` | `cowrie.login.success` |
| `2026-08-25 07:08:03` | `cowrie.session.params` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.success` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.command.input` |
| `2026-08-25 07:08:03` | `cowrie.log.closed` |
| `2026-08-25 07:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b33ede2bba

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:09 |
| **Last Seen** | 2026-08-25 07:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:09:09` | `cowrie.session.connect` |
| `2026-08-25 07:09:09` | `cowrie.client.version` |
| `2026-08-25 07:09:09` | `cowrie.client.kex` |
| `2026-08-25 07:09:10` | `cowrie.login.success` |
| `2026-08-25 07:09:12` | `cowrie.session.params` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.success` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.command.input` |
| `2026-08-25 07:09:12` | `cowrie.log.closed` |
| `2026-08-25 07:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3de4ac5d3dd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:10 |
| **Last Seen** | 2026-08-25 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:10:23` | `cowrie.session.connect` |
| `2026-08-25 07:10:24` | `cowrie.client.version` |
| `2026-08-25 07:10:24` | `cowrie.client.kex` |
| `2026-08-25 07:10:24` | `cowrie.login.success` |
| `2026-08-25 07:10:25` | `cowrie.session.params` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.success` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.command.input` |
| `2026-08-25 07:10:25` | `cowrie.log.closed` |
| `2026-08-25 07:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5425d033ead1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:11 |
| **Last Seen** | 2026-08-25 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:11:38` | `cowrie.session.connect` |
| `2026-08-25 07:11:38` | `cowrie.client.version` |
| `2026-08-25 07:11:39` | `cowrie.client.kex` |
| `2026-08-25 07:11:39` | `cowrie.login.success` |
| `2026-08-25 07:11:40` | `cowrie.session.params` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.success` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.command.input` |
| `2026-08-25 07:11:40` | `cowrie.log.closed` |
| `2026-08-25 07:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b24daf83f5d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:11 |
| **Last Seen** | 2026-08-25 07:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:11:50` | `cowrie.session.connect` |
| `2026-08-25 07:11:51` | `cowrie.client.version` |
| `2026-08-25 07:11:51` | `cowrie.client.kex` |
| `2026-08-25 07:11:51` | `cowrie.login.success` |
| `2026-08-25 07:11:52` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:11:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:11:53` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807e38342eb9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:11 |
| **Last Seen** | 2026-08-25 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:11:54` | `cowrie.session.connect` |
| `2026-08-25 07:11:54` | `cowrie.client.version` |
| `2026-08-25 07:11:54` | `cowrie.client.kex` |
| `2026-08-25 07:11:55` | `cowrie.login.success` |
| `2026-08-25 07:11:55` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:11:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:11:55` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:11:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9832faba69d4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:12 |
| **Last Seen** | 2026-08-25 07:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:12:42` | `cowrie.session.connect` |
| `2026-08-25 07:12:43` | `cowrie.client.version` |
| `2026-08-25 07:12:43` | `cowrie.client.kex` |
| `2026-08-25 07:12:44` | `cowrie.login.success` |
| `2026-08-25 07:12:45` | `cowrie.session.params` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.success` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:45` | `cowrie.command.input` |
| `2026-08-25 07:12:46` | `cowrie.log.closed` |
| `2026-08-25 07:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacb95088f47

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:13 |
| **Last Seen** | 2026-08-25 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:13:45` | `cowrie.session.connect` |
| `2026-08-25 07:13:45` | `cowrie.client.version` |
| `2026-08-25 07:13:45` | `cowrie.client.kex` |
| `2026-08-25 07:13:47` | `cowrie.login.success` |
| `2026-08-25 07:13:48` | `cowrie.session.params` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.success` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.command.input` |
| `2026-08-25 07:13:48` | `cowrie.log.closed` |
| `2026-08-25 07:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4e0806054b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:14 |
| **Last Seen** | 2026-08-25 07:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:14:48` | `cowrie.session.connect` |
| `2026-08-25 07:14:48` | `cowrie.client.version` |
| `2026-08-25 07:14:48` | `cowrie.client.kex` |
| `2026-08-25 07:14:50` | `cowrie.login.success` |
| `2026-08-25 07:14:51` | `cowrie.session.params` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.success` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.command.input` |
| `2026-08-25 07:14:51` | `cowrie.log.closed` |
| `2026-08-25 07:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9693a2054d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:15 |
| **Last Seen** | 2026-08-25 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:15:50` | `cowrie.session.connect` |
| `2026-08-25 07:15:51` | `cowrie.client.version` |
| `2026-08-25 07:15:51` | `cowrie.client.kex` |
| `2026-08-25 07:15:52` | `cowrie.login.success` |
| `2026-08-25 07:15:53` | `cowrie.session.params` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.success` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:53` | `cowrie.command.input` |
| `2026-08-25 07:15:54` | `cowrie.log.closed` |
| `2026-08-25 07:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9944d74c69ce

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 07:16 |
| **Last Seen** | 2026-08-25 07:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:16:32` | `cowrie.session.connect` |
| `2026-08-25 07:16:32` | `cowrie.client.version` |
| `2026-08-25 07:16:32` | `cowrie.client.kex` |
| `2026-08-25 07:16:32` | `cowrie.login.success` |
| `2026-08-25 07:16:33` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:16:33` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594c624fcd9f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:16 |
| **Last Seen** | 2026-08-25 07:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:16:51` | `cowrie.session.connect` |
| `2026-08-25 07:16:51` | `cowrie.client.version` |
| `2026-08-25 07:16:51` | `cowrie.client.kex` |
| `2026-08-25 07:16:52` | `cowrie.login.success` |
| `2026-08-25 07:16:53` | `cowrie.session.params` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.success` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:53` | `cowrie.command.input` |
| `2026-08-25 07:16:54` | `cowrie.log.closed` |
| `2026-08-25 07:16:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516afcabe563

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:17 |
| **Last Seen** | 2026-08-25 07:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:17:54` | `cowrie.session.connect` |
| `2026-08-25 07:17:54` | `cowrie.client.version` |
| `2026-08-25 07:17:54` | `cowrie.client.kex` |
| `2026-08-25 07:17:55` | `cowrie.login.success` |
| `2026-08-25 07:17:56` | `cowrie.session.params` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.success` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.command.input` |
| `2026-08-25 07:17:56` | `cowrie.log.closed` |
| `2026-08-25 07:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1a7ac754e6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:19 |
| **Last Seen** | 2026-08-25 07:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:19:01` | `cowrie.session.connect` |
| `2026-08-25 07:19:01` | `cowrie.client.version` |
| `2026-08-25 07:19:01` | `cowrie.client.kex` |
| `2026-08-25 07:19:02` | `cowrie.login.success` |
| `2026-08-25 07:19:03` | `cowrie.session.params` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.success` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.command.input` |
| `2026-08-25 07:19:03` | `cowrie.log.closed` |
| `2026-08-25 07:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9717889c57e2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:20 |
| **Last Seen** | 2026-08-25 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:20:10` | `cowrie.session.connect` |
| `2026-08-25 07:20:10` | `cowrie.client.version` |
| `2026-08-25 07:20:10` | `cowrie.client.kex` |
| `2026-08-25 07:20:10` | `cowrie.login.success` |
| `2026-08-25 07:20:11` | `cowrie.session.params` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.success` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.command.input` |
| `2026-08-25 07:20:11` | `cowrie.log.closed` |
| `2026-08-25 07:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a6a0a55608

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:21 |
| **Last Seen** | 2026-08-25 07:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:21:23` | `cowrie.session.connect` |
| `2026-08-25 07:21:23` | `cowrie.client.version` |
| `2026-08-25 07:21:23` | `cowrie.client.kex` |
| `2026-08-25 07:21:24` | `cowrie.login.success` |
| `2026-08-25 07:21:25` | `cowrie.session.params` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.success` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.command.input` |
| `2026-08-25 07:21:25` | `cowrie.log.closed` |
| `2026-08-25 07:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb57a09b2562

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:21 |
| **Last Seen** | 2026-08-25 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:21:40` | `cowrie.session.connect` |
| `2026-08-25 07:21:40` | `cowrie.client.version` |
| `2026-08-25 07:21:40` | `cowrie.client.kex` |
| `2026-08-25 07:21:41` | `cowrie.login.success` |
| `2026-08-25 07:21:41` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:21:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:21:41` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60420ffb0bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:21 |
| **Last Seen** | 2026-08-25 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:21:47` | `cowrie.session.connect` |
| `2026-08-25 07:21:47` | `cowrie.client.version` |
| `2026-08-25 07:21:47` | `cowrie.client.kex` |
| `2026-08-25 07:21:48` | `cowrie.login.success` |
| `2026-08-25 07:21:48` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:21:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:21:49` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c4c2751ba6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:22 |
| **Last Seen** | 2026-08-25 07:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:22:36` | `cowrie.session.connect` |
| `2026-08-25 07:22:37` | `cowrie.client.version` |
| `2026-08-25 07:22:37` | `cowrie.client.kex` |
| `2026-08-25 07:22:37` | `cowrie.login.success` |
| `2026-08-25 07:22:39` | `cowrie.session.params` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.success` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.command.input` |
| `2026-08-25 07:22:39` | `cowrie.log.closed` |
| `2026-08-25 07:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805e5a9d68da

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:23 |
| **Last Seen** | 2026-08-25 07:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:23:40` | `cowrie.session.connect` |
| `2026-08-25 07:23:40` | `cowrie.client.version` |
| `2026-08-25 07:23:40` | `cowrie.client.kex` |
| `2026-08-25 07:23:41` | `cowrie.login.success` |
| `2026-08-25 07:23:42` | `cowrie.session.params` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.success` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:42` | `cowrie.command.input` |
| `2026-08-25 07:23:43` | `cowrie.log.closed` |
| `2026-08-25 07:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4213df38f00

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:24 |
| **Last Seen** | 2026-08-25 07:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:24:44` | `cowrie.session.connect` |
| `2026-08-25 07:24:44` | `cowrie.client.version` |
| `2026-08-25 07:24:44` | `cowrie.client.kex` |
| `2026-08-25 07:24:45` | `cowrie.login.success` |
| `2026-08-25 07:24:46` | `cowrie.session.params` |
| `2026-08-25 07:24:46` | `cowrie.command.input` |
| `2026-08-25 07:24:46` | `cowrie.command.input` |
| `2026-08-25 07:24:46` | `cowrie.command.input` |
| `2026-08-25 07:24:46` | `cowrie.command.input` |
| `2026-08-25 07:24:46` | `cowrie.command.input` |
| `2026-08-25 07:24:46` | `cowrie.command.success` |
| `2026-08-25 07:24:47` | `cowrie.command.input` |
| `2026-08-25 07:24:47` | `cowrie.command.input` |
| `2026-08-25 07:24:47` | `cowrie.command.input` |
| `2026-08-25 07:24:47` | `cowrie.command.input` |
| `2026-08-25 07:24:47` | `cowrie.log.closed` |
| `2026-08-25 07:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db64752c2ae5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:25 |
| **Last Seen** | 2026-08-25 07:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:25:47` | `cowrie.session.connect` |
| `2026-08-25 07:25:47` | `cowrie.client.version` |
| `2026-08-25 07:25:47` | `cowrie.client.kex` |
| `2026-08-25 07:25:48` | `cowrie.login.success` |
| `2026-08-25 07:25:49` | `cowrie.session.params` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.success` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:49` | `cowrie.command.input` |
| `2026-08-25 07:25:50` | `cowrie.log.closed` |
| `2026-08-25 07:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3815dff08756

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:26 |
| **Last Seen** | 2026-08-25 07:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:26:52` | `cowrie.session.connect` |
| `2026-08-25 07:26:52` | `cowrie.client.version` |
| `2026-08-25 07:26:52` | `cowrie.client.kex` |
| `2026-08-25 07:26:53` | `cowrie.login.success` |
| `2026-08-25 07:26:54` | `cowrie.session.params` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.success` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:54` | `cowrie.command.input` |
| `2026-08-25 07:26:55` | `cowrie.log.closed` |
| `2026-08-25 07:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e23ab26f7a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:28 |
| **Last Seen** | 2026-08-25 07:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:28:00` | `cowrie.session.connect` |
| `2026-08-25 07:28:00` | `cowrie.client.version` |
| `2026-08-25 07:28:00` | `cowrie.client.kex` |
| `2026-08-25 07:28:00` | `cowrie.login.success` |
| `2026-08-25 07:28:02` | `cowrie.session.params` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.success` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.command.input` |
| `2026-08-25 07:28:02` | `cowrie.log.closed` |
| `2026-08-25 07:28:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24af3f51bf04

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:29 |
| **Last Seen** | 2026-08-25 07:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:29:13` | `cowrie.session.connect` |
| `2026-08-25 07:29:13` | `cowrie.client.version` |
| `2026-08-25 07:29:13` | `cowrie.client.kex` |
| `2026-08-25 07:29:14` | `cowrie.login.success` |
| `2026-08-25 07:29:14` | `cowrie.session.params` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.success` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:14` | `cowrie.command.input` |
| `2026-08-25 07:29:15` | `cowrie.log.closed` |
| `2026-08-25 07:29:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9fe5ca64c86

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:30 |
| **Last Seen** | 2026-08-25 07:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:30:29` | `cowrie.session.connect` |
| `2026-08-25 07:30:29` | `cowrie.client.version` |
| `2026-08-25 07:30:29` | `cowrie.client.kex` |
| `2026-08-25 07:30:30` | `cowrie.login.success` |
| `2026-08-25 07:30:31` | `cowrie.session.params` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.success` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.command.input` |
| `2026-08-25 07:30:31` | `cowrie.log.closed` |
| `2026-08-25 07:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2493b30e965

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:31 |
| **Last Seen** | 2026-08-25 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:31:11` | `cowrie.session.connect` |
| `2026-08-25 07:31:11` | `cowrie.client.version` |
| `2026-08-25 07:31:12` | `cowrie.client.kex` |
| `2026-08-25 07:31:13` | `cowrie.login.success` |
| `2026-08-25 07:31:13` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:31:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:31:13` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4cb1870933

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:31 |
| **Last Seen** | 2026-08-25 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:31:19` | `cowrie.session.connect` |
| `2026-08-25 07:31:19` | `cowrie.client.version` |
| `2026-08-25 07:31:19` | `cowrie.client.kex` |
| `2026-08-25 07:31:20` | `cowrie.login.success` |
| `2026-08-25 07:31:20` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:31:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:31:21` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b26c1fa472

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:31 |
| **Last Seen** | 2026-08-25 07:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:31:41` | `cowrie.session.connect` |
| `2026-08-25 07:31:41` | `cowrie.client.version` |
| `2026-08-25 07:31:41` | `cowrie.client.kex` |
| `2026-08-25 07:31:42` | `cowrie.login.success` |
| `2026-08-25 07:31:43` | `cowrie.session.params` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.success` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.command.input` |
| `2026-08-25 07:31:43` | `cowrie.log.closed` |
| `2026-08-25 07:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6c329be54d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:32 |
| **Last Seen** | 2026-08-25 07:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:32:43` | `cowrie.session.connect` |
| `2026-08-25 07:32:43` | `cowrie.client.version` |
| `2026-08-25 07:32:43` | `cowrie.client.kex` |
| `2026-08-25 07:32:44` | `cowrie.login.success` |
| `2026-08-25 07:32:45` | `cowrie.session.params` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.success` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:45` | `cowrie.command.input` |
| `2026-08-25 07:32:46` | `cowrie.log.closed` |
| `2026-08-25 07:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b84f4b6cb68

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:33 |
| **Last Seen** | 2026-08-25 07:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:33:44` | `cowrie.session.connect` |
| `2026-08-25 07:33:44` | `cowrie.client.version` |
| `2026-08-25 07:33:44` | `cowrie.client.kex` |
| `2026-08-25 07:33:45` | `cowrie.login.success` |
| `2026-08-25 07:33:46` | `cowrie.session.params` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.success` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:46` | `cowrie.command.input` |
| `2026-08-25 07:33:47` | `cowrie.log.closed` |
| `2026-08-25 07:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44a24208ddc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:34 |
| **Last Seen** | 2026-08-25 07:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:34:44` | `cowrie.session.connect` |
| `2026-08-25 07:34:44` | `cowrie.client.version` |
| `2026-08-25 07:34:44` | `cowrie.client.kex` |
| `2026-08-25 07:34:45` | `cowrie.login.success` |
| `2026-08-25 07:34:46` | `cowrie.session.params` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.success` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:46` | `cowrie.command.input` |
| `2026-08-25 07:34:47` | `cowrie.command.input` |
| `2026-08-25 07:34:47` | `cowrie.log.closed` |
| `2026-08-25 07:34:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5301afc779b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:35 |
| **Last Seen** | 2026-08-25 07:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:35:43` | `cowrie.session.connect` |
| `2026-08-25 07:35:43` | `cowrie.client.version` |
| `2026-08-25 07:35:43` | `cowrie.client.kex` |
| `2026-08-25 07:35:45` | `cowrie.login.success` |
| `2026-08-25 07:35:47` | `cowrie.session.params` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.success` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.command.input` |
| `2026-08-25 07:35:47` | `cowrie.log.closed` |
| `2026-08-25 07:35:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958cb47b066c

| Field | Detail |
|---|---|
| **Source IP** | `8.215.69[.]55` |
| **First Seen** | 2026-08-25 07:36 |
| **Last Seen** | 2026-08-25 07:36 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:36:23` | `cowrie.session.connect` |
| `2026-08-25 07:36:25` | `cowrie.client.version` |
| `2026-08-25 07:36:27` | `cowrie.client.kex` |
| `2026-08-25 07:36:36` | `cowrie.login.success` |
| `2026-08-25 07:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.215.69[.]55` to AbuseIPDB if not already reported
- [ ] Block `8.215.69[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0500388b60

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-25 07:36 |
| **Last Seen** | 2026-08-25 07:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:36:39` | `cowrie.session.connect` |
| `2026-08-25 07:36:39` | `cowrie.client.version` |
| `2026-08-25 07:36:39` | `cowrie.client.kex` |
| `2026-08-25 07:36:40` | `cowrie.login.success` |
| `2026-08-25 07:36:41` | `cowrie.session.params` |
| `2026-08-25 07:36:41` | `cowrie.command.input` |
| `2026-08-25 07:36:41` | `cowrie.session.file_download` |
| `2026-08-25 07:36:41` | `cowrie.session.file_download` |
| `2026-08-25 07:36:41` | `cowrie.log.closed` |
| `2026-08-25 07:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274d2459b35e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:36 |
| **Last Seen** | 2026-08-25 07:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:36:45` | `cowrie.session.connect` |
| `2026-08-25 07:36:45` | `cowrie.client.version` |
| `2026-08-25 07:36:45` | `cowrie.client.kex` |
| `2026-08-25 07:36:46` | `cowrie.login.success` |
| `2026-08-25 07:36:47` | `cowrie.session.params` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.success` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:47` | `cowrie.command.input` |
| `2026-08-25 07:36:48` | `cowrie.log.closed` |
| `2026-08-25 07:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c2f9ab8759

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:37 |
| **Last Seen** | 2026-08-25 07:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:37:51` | `cowrie.session.connect` |
| `2026-08-25 07:37:51` | `cowrie.client.version` |
| `2026-08-25 07:37:51` | `cowrie.client.kex` |
| `2026-08-25 07:37:52` | `cowrie.login.success` |
| `2026-08-25 07:37:53` | `cowrie.session.params` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.success` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.command.input` |
| `2026-08-25 07:37:53` | `cowrie.log.closed` |
| `2026-08-25 07:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-422e17a26c3f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:38 |
| **Last Seen** | 2026-08-25 07:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:38:59` | `cowrie.session.connect` |
| `2026-08-25 07:38:59` | `cowrie.client.version` |
| `2026-08-25 07:38:59` | `cowrie.client.kex` |
| `2026-08-25 07:39:00` | `cowrie.login.success` |
| `2026-08-25 07:39:01` | `cowrie.session.params` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.success` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.command.input` |
| `2026-08-25 07:39:01` | `cowrie.log.closed` |
| `2026-08-25 07:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa122a225469

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:40 |
| **Last Seen** | 2026-08-25 07:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:40:10` | `cowrie.session.connect` |
| `2026-08-25 07:40:10` | `cowrie.client.version` |
| `2026-08-25 07:40:10` | `cowrie.client.kex` |
| `2026-08-25 07:40:11` | `cowrie.login.success` |
| `2026-08-25 07:40:12` | `cowrie.session.params` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.success` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.command.input` |
| `2026-08-25 07:40:12` | `cowrie.log.closed` |
| `2026-08-25 07:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1315cc7c163

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:40 |
| **Last Seen** | 2026-08-25 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:40:50` | `cowrie.session.connect` |
| `2026-08-25 07:40:50` | `cowrie.client.version` |
| `2026-08-25 07:40:50` | `cowrie.client.kex` |
| `2026-08-25 07:40:51` | `cowrie.login.success` |
| `2026-08-25 07:40:51` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:40:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:40:52` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf745577590

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:40 |
| **Last Seen** | 2026-08-25 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:40:55` | `cowrie.session.connect` |
| `2026-08-25 07:40:55` | `cowrie.client.version` |
| `2026-08-25 07:40:55` | `cowrie.client.kex` |
| `2026-08-25 07:40:56` | `cowrie.login.success` |
| `2026-08-25 07:40:56` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:40:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:40:56` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c86063f89445

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:41 |
| **Last Seen** | 2026-08-25 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:41:24` | `cowrie.session.connect` |
| `2026-08-25 07:41:24` | `cowrie.client.version` |
| `2026-08-25 07:41:24` | `cowrie.client.kex` |
| `2026-08-25 07:41:25` | `cowrie.login.success` |
| `2026-08-25 07:41:26` | `cowrie.session.params` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.success` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.command.input` |
| `2026-08-25 07:41:26` | `cowrie.log.closed` |
| `2026-08-25 07:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171477f114d4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:42 |
| **Last Seen** | 2026-08-25 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:42:46` | `cowrie.session.connect` |
| `2026-08-25 07:42:46` | `cowrie.client.version` |
| `2026-08-25 07:42:46` | `cowrie.client.kex` |
| `2026-08-25 07:42:47` | `cowrie.login.success` |
| `2026-08-25 07:42:47` | `cowrie.session.params` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.success` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:47` | `cowrie.command.input` |
| `2026-08-25 07:42:48` | `cowrie.log.closed` |
| `2026-08-25 07:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a087a2a3cea

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:43 |
| **Last Seen** | 2026-08-25 07:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:43:55` | `cowrie.session.connect` |
| `2026-08-25 07:43:55` | `cowrie.client.version` |
| `2026-08-25 07:43:55` | `cowrie.client.kex` |
| `2026-08-25 07:43:56` | `cowrie.login.success` |
| `2026-08-25 07:43:58` | `cowrie.session.params` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.success` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.command.input` |
| `2026-08-25 07:43:58` | `cowrie.log.closed` |
| `2026-08-25 07:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fb3558fe313

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:44 |
| **Last Seen** | 2026-08-25 07:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:44:56` | `cowrie.session.connect` |
| `2026-08-25 07:44:56` | `cowrie.client.version` |
| `2026-08-25 07:44:56` | `cowrie.client.kex` |
| `2026-08-25 07:44:58` | `cowrie.login.success` |
| `2026-08-25 07:44:59` | `cowrie.session.params` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.success` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.command.input` |
| `2026-08-25 07:45:00` | `cowrie.log.closed` |
| `2026-08-25 07:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51ce6368fd4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:45 |
| **Last Seen** | 2026-08-25 07:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:45:55` | `cowrie.session.connect` |
| `2026-08-25 07:45:55` | `cowrie.client.version` |
| `2026-08-25 07:45:55` | `cowrie.client.kex` |
| `2026-08-25 07:45:57` | `cowrie.login.success` |
| `2026-08-25 07:45:58` | `cowrie.session.params` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.success` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:58` | `cowrie.command.input` |
| `2026-08-25 07:45:59` | `cowrie.log.closed` |
| `2026-08-25 07:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc077f94e2f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:46 |
| **Last Seen** | 2026-08-25 07:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:46:54` | `cowrie.session.connect` |
| `2026-08-25 07:46:54` | `cowrie.client.version` |
| `2026-08-25 07:46:54` | `cowrie.client.kex` |
| `2026-08-25 07:46:55` | `cowrie.login.success` |
| `2026-08-25 07:46:56` | `cowrie.session.params` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.success` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:56` | `cowrie.command.input` |
| `2026-08-25 07:46:57` | `cowrie.log.closed` |
| `2026-08-25 07:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59716c02d6ab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:47 |
| **Last Seen** | 2026-08-25 07:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:47:53` | `cowrie.session.connect` |
| `2026-08-25 07:47:54` | `cowrie.client.version` |
| `2026-08-25 07:47:54` | `cowrie.client.kex` |
| `2026-08-25 07:47:55` | `cowrie.login.success` |
| `2026-08-25 07:47:56` | `cowrie.session.params` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.success` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.command.input` |
| `2026-08-25 07:47:56` | `cowrie.log.closed` |
| `2026-08-25 07:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b11e6db00e0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:48 |
| **Last Seen** | 2026-08-25 07:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:48:55` | `cowrie.session.connect` |
| `2026-08-25 07:48:55` | `cowrie.client.version` |
| `2026-08-25 07:48:55` | `cowrie.client.kex` |
| `2026-08-25 07:48:56` | `cowrie.login.success` |
| `2026-08-25 07:48:57` | `cowrie.session.params` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.success` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.command.input` |
| `2026-08-25 07:48:57` | `cowrie.log.closed` |
| `2026-08-25 07:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c00e3683a4d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:49 |
| **Last Seen** | 2026-08-25 07:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:49:58` | `cowrie.session.connect` |
| `2026-08-25 07:49:58` | `cowrie.client.version` |
| `2026-08-25 07:49:58` | `cowrie.client.kex` |
| `2026-08-25 07:49:59` | `cowrie.login.success` |
| `2026-08-25 07:50:00` | `cowrie.session.params` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.success` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:00` | `cowrie.command.input` |
| `2026-08-25 07:50:01` | `cowrie.log.closed` |
| `2026-08-25 07:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e21b5000e05

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:50 |
| **Last Seen** | 2026-08-25 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:50:23` | `cowrie.session.connect` |
| `2026-08-25 07:50:23` | `cowrie.client.version` |
| `2026-08-25 07:50:23` | `cowrie.client.kex` |
| `2026-08-25 07:50:24` | `cowrie.login.success` |
| `2026-08-25 07:50:24` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:50:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:50:24` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8829a24077

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:50 |
| **Last Seen** | 2026-08-25 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:50:26` | `cowrie.session.connect` |
| `2026-08-25 07:50:26` | `cowrie.client.version` |
| `2026-08-25 07:50:26` | `cowrie.client.kex` |
| `2026-08-25 07:50:27` | `cowrie.login.success` |
| `2026-08-25 07:50:27` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:50:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:50:28` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d1379cd928

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:51 |
| **Last Seen** | 2026-08-25 07:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:51:06` | `cowrie.session.connect` |
| `2026-08-25 07:51:06` | `cowrie.client.version` |
| `2026-08-25 07:51:06` | `cowrie.client.kex` |
| `2026-08-25 07:51:07` | `cowrie.login.success` |
| `2026-08-25 07:51:08` | `cowrie.session.params` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.success` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.command.input` |
| `2026-08-25 07:51:08` | `cowrie.log.closed` |
| `2026-08-25 07:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed302b761aab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:52 |
| **Last Seen** | 2026-08-25 07:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:52:17` | `cowrie.session.connect` |
| `2026-08-25 07:52:17` | `cowrie.client.version` |
| `2026-08-25 07:52:17` | `cowrie.client.kex` |
| `2026-08-25 07:52:17` | `cowrie.login.success` |
| `2026-08-25 07:52:18` | `cowrie.session.params` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.success` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.command.input` |
| `2026-08-25 07:52:18` | `cowrie.log.closed` |
| `2026-08-25 07:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09df82ffd7c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:53 |
| **Last Seen** | 2026-08-25 07:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:53:28` | `cowrie.session.connect` |
| `2026-08-25 07:53:28` | `cowrie.client.version` |
| `2026-08-25 07:53:28` | `cowrie.client.kex` |
| `2026-08-25 07:53:29` | `cowrie.login.success` |
| `2026-08-25 07:53:30` | `cowrie.session.params` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.success` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.command.input` |
| `2026-08-25 07:53:30` | `cowrie.log.closed` |
| `2026-08-25 07:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38bbdceec0b8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:54 |
| **Last Seen** | 2026-08-25 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:54:41` | `cowrie.session.connect` |
| `2026-08-25 07:54:41` | `cowrie.client.version` |
| `2026-08-25 07:54:41` | `cowrie.client.kex` |
| `2026-08-25 07:54:42` | `cowrie.login.success` |
| `2026-08-25 07:54:43` | `cowrie.session.params` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.success` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.command.input` |
| `2026-08-25 07:54:43` | `cowrie.log.closed` |
| `2026-08-25 07:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fa8cc5d79d0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 07:55 |
| **Last Seen** | 2026-08-25 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:55:47` | `cowrie.session.connect` |
| `2026-08-25 07:55:47` | `cowrie.client.version` |
| `2026-08-25 07:55:47` | `cowrie.client.kex` |
| `2026-08-25 07:55:48` | `cowrie.login.success` |
| `2026-08-25 07:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ea4508ab27

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-25 07:55 |
| **Last Seen** | 2026-08-25 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:55:47` | `cowrie.session.connect` |
| `2026-08-25 07:55:47` | `cowrie.client.version` |
| `2026-08-25 07:55:47` | `cowrie.client.kex` |
| `2026-08-25 07:55:48` | `cowrie.login.success` |
| `2026-08-25 07:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afbddba730b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:55 |
| **Last Seen** | 2026-08-25 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:55:58` | `cowrie.session.connect` |
| `2026-08-25 07:55:58` | `cowrie.client.version` |
| `2026-08-25 07:55:59` | `cowrie.client.kex` |
| `2026-08-25 07:55:59` | `cowrie.login.success` |
| `2026-08-25 07:56:00` | `cowrie.session.params` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.success` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.command.input` |
| `2026-08-25 07:56:00` | `cowrie.log.closed` |
| `2026-08-25 07:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c9b9b02d0a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:57 |
| **Last Seen** | 2026-08-25 07:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:57:13` | `cowrie.session.connect` |
| `2026-08-25 07:57:13` | `cowrie.client.version` |
| `2026-08-25 07:57:13` | `cowrie.client.kex` |
| `2026-08-25 07:57:14` | `cowrie.login.success` |
| `2026-08-25 07:57:15` | `cowrie.session.params` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.success` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:15` | `cowrie.command.input` |
| `2026-08-25 07:57:16` | `cowrie.log.closed` |
| `2026-08-25 07:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9a23b6cef8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:58 |
| **Last Seen** | 2026-08-25 07:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:58:15` | `cowrie.session.connect` |
| `2026-08-25 07:58:15` | `cowrie.client.version` |
| `2026-08-25 07:58:15` | `cowrie.client.kex` |
| `2026-08-25 07:58:16` | `cowrie.login.success` |
| `2026-08-25 07:58:17` | `cowrie.session.params` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.success` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.command.input` |
| `2026-08-25 07:58:17` | `cowrie.log.closed` |
| `2026-08-25 07:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbbe6fb0b50

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 07:59 |
| **Last Seen** | 2026-08-25 07:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:59:12` | `cowrie.session.connect` |
| `2026-08-25 07:59:12` | `cowrie.client.version` |
| `2026-08-25 07:59:12` | `cowrie.client.kex` |
| `2026-08-25 07:59:14` | `cowrie.login.success` |
| `2026-08-25 07:59:15` | `cowrie.session.params` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.success` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.command.input` |
| `2026-08-25 07:59:15` | `cowrie.log.closed` |
| `2026-08-25 07:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29dad8b4a7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:59 |
| **Last Seen** | 2026-08-25 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:59:52` | `cowrie.session.connect` |
| `2026-08-25 07:59:52` | `cowrie.client.version` |
| `2026-08-25 07:59:52` | `cowrie.client.kex` |
| `2026-08-25 07:59:53` | `cowrie.login.success` |
| `2026-08-25 07:59:53` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:59:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:59:54` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa30406c614

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 07:59 |
| **Last Seen** | 2026-08-25 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 07:59:56` | `cowrie.session.connect` |
| `2026-08-25 07:59:56` | `cowrie.client.version` |
| `2026-08-25 07:59:56` | `cowrie.client.kex` |
| `2026-08-25 07:59:57` | `cowrie.login.success` |
| `2026-08-25 07:59:57` | `cowrie.direct-tcpip.request` |
| `2026-08-25 07:59:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 07:59:57` | `cowrie.direct-tcpip.data` |
| `2026-08-25 07:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ccd1ced4d31

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:00 |
| **Last Seen** | 2026-08-25 08:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:00:10` | `cowrie.session.connect` |
| `2026-08-25 08:00:10` | `cowrie.client.version` |
| `2026-08-25 08:00:10` | `cowrie.client.kex` |
| `2026-08-25 08:00:11` | `cowrie.login.success` |
| `2026-08-25 08:00:13` | `cowrie.session.params` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.success` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.command.input` |
| `2026-08-25 08:00:13` | `cowrie.log.closed` |
| `2026-08-25 08:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c699866c4a5b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:01 |
| **Last Seen** | 2026-08-25 08:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:01:09` | `cowrie.session.connect` |
| `2026-08-25 08:01:09` | `cowrie.client.version` |
| `2026-08-25 08:01:09` | `cowrie.client.kex` |
| `2026-08-25 08:01:11` | `cowrie.login.success` |
| `2026-08-25 08:01:12` | `cowrie.session.params` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.success` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.command.input` |
| `2026-08-25 08:01:12` | `cowrie.log.closed` |
| `2026-08-25 08:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8e463760275

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:02 |
| **Last Seen** | 2026-08-25 08:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:02:11` | `cowrie.session.connect` |
| `2026-08-25 08:02:11` | `cowrie.client.version` |
| `2026-08-25 08:02:11` | `cowrie.client.kex` |
| `2026-08-25 08:02:12` | `cowrie.login.success` |
| `2026-08-25 08:02:13` | `cowrie.session.params` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.success` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:13` | `cowrie.command.input` |
| `2026-08-25 08:02:14` | `cowrie.log.closed` |
| `2026-08-25 08:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-850aa517c3bc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-25 08:03 |
| **Last Seen** | 2026-08-25 08:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:03:00` | `cowrie.session.connect` |
| `2026-08-25 08:03:00` | `cowrie.client.version` |
| `2026-08-25 08:03:00` | `cowrie.client.kex` |
| `2026-08-25 08:03:01` | `cowrie.login.success` |
| `2026-08-25 08:03:01` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:03:01` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46605b70f7d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:03 |
| **Last Seen** | 2026-08-25 08:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:03:14` | `cowrie.session.connect` |
| `2026-08-25 08:03:14` | `cowrie.client.version` |
| `2026-08-25 08:03:14` | `cowrie.client.kex` |
| `2026-08-25 08:03:15` | `cowrie.login.success` |
| `2026-08-25 08:03:16` | `cowrie.session.params` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.success` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:16` | `cowrie.command.input` |
| `2026-08-25 08:03:17` | `cowrie.log.closed` |
| `2026-08-25 08:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ab45c61f7e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:04 |
| **Last Seen** | 2026-08-25 08:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:04:17` | `cowrie.session.connect` |
| `2026-08-25 08:04:18` | `cowrie.client.version` |
| `2026-08-25 08:04:18` | `cowrie.client.kex` |
| `2026-08-25 08:04:19` | `cowrie.login.success` |
| `2026-08-25 08:04:20` | `cowrie.session.params` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.success` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.command.input` |
| `2026-08-25 08:04:20` | `cowrie.log.closed` |
| `2026-08-25 08:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c095c44e3314

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:05 |
| **Last Seen** | 2026-08-25 08:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:05:22` | `cowrie.session.connect` |
| `2026-08-25 08:05:22` | `cowrie.client.version` |
| `2026-08-25 08:05:22` | `cowrie.client.kex` |
| `2026-08-25 08:05:23` | `cowrie.login.success` |
| `2026-08-25 08:05:24` | `cowrie.session.params` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.success` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.command.input` |
| `2026-08-25 08:05:24` | `cowrie.log.closed` |
| `2026-08-25 08:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77253d4ca357

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:06 |
| **Last Seen** | 2026-08-25 08:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:06:26` | `cowrie.session.connect` |
| `2026-08-25 08:06:26` | `cowrie.client.version` |
| `2026-08-25 08:06:26` | `cowrie.client.kex` |
| `2026-08-25 08:06:27` | `cowrie.login.success` |
| `2026-08-25 08:06:29` | `cowrie.session.params` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.success` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.command.input` |
| `2026-08-25 08:06:29` | `cowrie.log.closed` |
| `2026-08-25 08:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09c8c597523

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:07 |
| **Last Seen** | 2026-08-25 08:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:07:33` | `cowrie.session.connect` |
| `2026-08-25 08:07:33` | `cowrie.client.version` |
| `2026-08-25 08:07:33` | `cowrie.client.kex` |
| `2026-08-25 08:07:34` | `cowrie.login.success` |
| `2026-08-25 08:07:35` | `cowrie.session.params` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.success` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.command.input` |
| `2026-08-25 08:07:35` | `cowrie.log.closed` |
| `2026-08-25 08:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-040c317576e1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:08 |
| **Last Seen** | 2026-08-25 08:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:08:43` | `cowrie.session.connect` |
| `2026-08-25 08:08:43` | `cowrie.client.version` |
| `2026-08-25 08:08:43` | `cowrie.client.kex` |
| `2026-08-25 08:08:44` | `cowrie.login.success` |
| `2026-08-25 08:08:45` | `cowrie.session.params` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.success` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.command.input` |
| `2026-08-25 08:08:45` | `cowrie.log.closed` |
| `2026-08-25 08:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b01ac18b98

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:09 |
| **Last Seen** | 2026-08-25 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:09:31` | `cowrie.session.connect` |
| `2026-08-25 08:09:31` | `cowrie.client.version` |
| `2026-08-25 08:09:31` | `cowrie.client.kex` |
| `2026-08-25 08:09:32` | `cowrie.login.success` |
| `2026-08-25 08:09:32` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:09:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:09:33` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e4d810ff4b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:09 |
| **Last Seen** | 2026-08-25 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:09:35` | `cowrie.session.connect` |
| `2026-08-25 08:09:35` | `cowrie.client.version` |
| `2026-08-25 08:09:35` | `cowrie.client.kex` |
| `2026-08-25 08:09:36` | `cowrie.login.success` |
| `2026-08-25 08:09:36` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:09:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:09:36` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdd6e98f110a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:09 |
| **Last Seen** | 2026-08-25 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:09:54` | `cowrie.session.connect` |
| `2026-08-25 08:09:54` | `cowrie.client.version` |
| `2026-08-25 08:09:54` | `cowrie.client.kex` |
| `2026-08-25 08:09:54` | `cowrie.login.success` |
| `2026-08-25 08:09:56` | `cowrie.session.params` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.success` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.command.input` |
| `2026-08-25 08:09:56` | `cowrie.log.closed` |
| `2026-08-25 08:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93ea634ebc1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:11 |
| **Last Seen** | 2026-08-25 08:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:11:05` | `cowrie.session.connect` |
| `2026-08-25 08:11:05` | `cowrie.client.version` |
| `2026-08-25 08:11:05` | `cowrie.client.kex` |
| `2026-08-25 08:11:06` | `cowrie.login.success` |
| `2026-08-25 08:11:07` | `cowrie.session.params` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.success` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.command.input` |
| `2026-08-25 08:11:07` | `cowrie.log.closed` |
| `2026-08-25 08:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80590a9fdee8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:12 |
| **Last Seen** | 2026-08-25 08:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:12:16` | `cowrie.session.connect` |
| `2026-08-25 08:12:16` | `cowrie.client.version` |
| `2026-08-25 08:12:16` | `cowrie.client.kex` |
| `2026-08-25 08:12:16` | `cowrie.login.success` |
| `2026-08-25 08:12:18` | `cowrie.session.params` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.success` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.command.input` |
| `2026-08-25 08:12:18` | `cowrie.log.closed` |
| `2026-08-25 08:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73b7ac0331d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:13 |
| **Last Seen** | 2026-08-25 08:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:13:28` | `cowrie.session.connect` |
| `2026-08-25 08:13:28` | `cowrie.client.version` |
| `2026-08-25 08:13:28` | `cowrie.client.kex` |
| `2026-08-25 08:13:29` | `cowrie.login.success` |
| `2026-08-25 08:13:30` | `cowrie.session.params` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.success` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.command.input` |
| `2026-08-25 08:13:30` | `cowrie.log.closed` |
| `2026-08-25 08:13:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ece2d1053a9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:14 |
| **Last Seen** | 2026-08-25 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:14:40` | `cowrie.session.connect` |
| `2026-08-25 08:14:40` | `cowrie.client.version` |
| `2026-08-25 08:14:40` | `cowrie.client.kex` |
| `2026-08-25 08:14:41` | `cowrie.login.success` |
| `2026-08-25 08:14:42` | `cowrie.session.params` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.success` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.command.input` |
| `2026-08-25 08:14:42` | `cowrie.log.closed` |
| `2026-08-25 08:14:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da10c23f429f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:15 |
| **Last Seen** | 2026-08-25 08:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:15:48` | `cowrie.session.connect` |
| `2026-08-25 08:15:48` | `cowrie.client.version` |
| `2026-08-25 08:15:48` | `cowrie.client.kex` |
| `2026-08-25 08:15:49` | `cowrie.login.success` |
| `2026-08-25 08:15:50` | `cowrie.session.params` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.success` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.command.input` |
| `2026-08-25 08:15:50` | `cowrie.log.closed` |
| `2026-08-25 08:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4a187480f53

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:16 |
| **Last Seen** | 2026-08-25 08:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:16:55` | `cowrie.session.connect` |
| `2026-08-25 08:16:55` | `cowrie.client.version` |
| `2026-08-25 08:16:55` | `cowrie.client.kex` |
| `2026-08-25 08:16:56` | `cowrie.login.success` |
| `2026-08-25 08:16:57` | `cowrie.session.params` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.success` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.command.input` |
| `2026-08-25 08:16:57` | `cowrie.log.closed` |
| `2026-08-25 08:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1c1bf90a01

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:18 |
| **Last Seen** | 2026-08-25 08:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:18:04` | `cowrie.session.connect` |
| `2026-08-25 08:18:04` | `cowrie.client.version` |
| `2026-08-25 08:18:04` | `cowrie.client.kex` |
| `2026-08-25 08:18:05` | `cowrie.login.success` |
| `2026-08-25 08:18:06` | `cowrie.session.params` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.success` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.command.input` |
| `2026-08-25 08:18:06` | `cowrie.log.closed` |
| `2026-08-25 08:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d172e431fd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:19 |
| **Last Seen** | 2026-08-25 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:19:00` | `cowrie.session.connect` |
| `2026-08-25 08:19:00` | `cowrie.client.version` |
| `2026-08-25 08:19:01` | `cowrie.client.kex` |
| `2026-08-25 08:19:01` | `cowrie.login.success` |
| `2026-08-25 08:19:02` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:19:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:19:02` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60bebd790ae8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:19 |
| **Last Seen** | 2026-08-25 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:19:04` | `cowrie.session.connect` |
| `2026-08-25 08:19:04` | `cowrie.client.version` |
| `2026-08-25 08:19:04` | `cowrie.client.kex` |
| `2026-08-25 08:19:05` | `cowrie.login.success` |
| `2026-08-25 08:19:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:19:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:19:05` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed4592bec6de

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:19 |
| **Last Seen** | 2026-08-25 08:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:19:13` | `cowrie.session.connect` |
| `2026-08-25 08:19:13` | `cowrie.client.version` |
| `2026-08-25 08:19:13` | `cowrie.client.kex` |
| `2026-08-25 08:19:14` | `cowrie.login.success` |
| `2026-08-25 08:19:15` | `cowrie.session.params` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.success` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.command.input` |
| `2026-08-25 08:19:15` | `cowrie.log.closed` |
| `2026-08-25 08:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ddef8a4898

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:20 |
| **Last Seen** | 2026-08-25 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:20:28` | `cowrie.session.connect` |
| `2026-08-25 08:20:28` | `cowrie.client.version` |
| `2026-08-25 08:20:28` | `cowrie.client.kex` |
| `2026-08-25 08:20:28` | `cowrie.login.success` |
| `2026-08-25 08:20:29` | `cowrie.session.params` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.success` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.command.input` |
| `2026-08-25 08:20:29` | `cowrie.log.closed` |
| `2026-08-25 08:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54b80b9116c0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:21 |
| **Last Seen** | 2026-08-25 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:21:46` | `cowrie.session.connect` |
| `2026-08-25 08:21:46` | `cowrie.client.version` |
| `2026-08-25 08:21:46` | `cowrie.client.kex` |
| `2026-08-25 08:21:46` | `cowrie.login.success` |
| `2026-08-25 08:21:47` | `cowrie.session.params` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.success` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.command.input` |
| `2026-08-25 08:21:47` | `cowrie.log.closed` |
| `2026-08-25 08:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d00b94e5f9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:23 |
| **Last Seen** | 2026-08-25 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:23:05` | `cowrie.session.connect` |
| `2026-08-25 08:23:05` | `cowrie.client.version` |
| `2026-08-25 08:23:05` | `cowrie.client.kex` |
| `2026-08-25 08:23:05` | `cowrie.login.success` |
| `2026-08-25 08:23:06` | `cowrie.session.params` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.success` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.command.input` |
| `2026-08-25 08:23:06` | `cowrie.log.closed` |
| `2026-08-25 08:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a415b38e3ef4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:24 |
| **Last Seen** | 2026-08-25 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:24:25` | `cowrie.session.connect` |
| `2026-08-25 08:24:25` | `cowrie.client.version` |
| `2026-08-25 08:24:25` | `cowrie.client.kex` |
| `2026-08-25 08:24:25` | `cowrie.login.success` |
| `2026-08-25 08:24:26` | `cowrie.session.params` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.success` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.command.input` |
| `2026-08-25 08:24:26` | `cowrie.log.closed` |
| `2026-08-25 08:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64ee24ffdde

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:25 |
| **Last Seen** | 2026-08-25 08:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:25:40` | `cowrie.session.connect` |
| `2026-08-25 08:25:40` | `cowrie.client.version` |
| `2026-08-25 08:25:40` | `cowrie.client.kex` |
| `2026-08-25 08:25:40` | `cowrie.login.success` |
| `2026-08-25 08:25:41` | `cowrie.session.params` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.success` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.command.input` |
| `2026-08-25 08:25:41` | `cowrie.log.closed` |
| `2026-08-25 08:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4ab49602546

| Field | Detail |
|---|---|
| **Source IP** | `222.88.163[.]202` |
| **First Seen** | 2026-08-25 08:25 |
| **Last Seen** | 2026-08-25 08:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:25:47` | `cowrie.session.connect` |
| `2026-08-25 08:25:47` | `cowrie.client.version` |
| `2026-08-25 08:25:47` | `cowrie.client.kex` |
| `2026-08-25 08:25:48` | `cowrie.login.success` |
| `2026-08-25 08:25:49` | `cowrie.session.params` |
| `2026-08-25 08:25:49` | `cowrie.command.input` |
| `2026-08-25 08:25:49` | `cowrie.log.closed` |
| `2026-08-25 08:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.88.163[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.88.163[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebfd3814ec9e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:26 |
| **Last Seen** | 2026-08-25 08:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:26:42` | `cowrie.session.connect` |
| `2026-08-25 08:26:42` | `cowrie.client.version` |
| `2026-08-25 08:26:42` | `cowrie.client.kex` |
| `2026-08-25 08:26:43` | `cowrie.login.success` |
| `2026-08-25 08:26:44` | `cowrie.session.params` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.success` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:44` | `cowrie.command.input` |
| `2026-08-25 08:26:45` | `cowrie.log.closed` |
| `2026-08-25 08:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4c6923a89e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:27 |
| **Last Seen** | 2026-08-25 08:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:27:44` | `cowrie.session.connect` |
| `2026-08-25 08:27:44` | `cowrie.client.version` |
| `2026-08-25 08:27:44` | `cowrie.client.kex` |
| `2026-08-25 08:27:45` | `cowrie.login.success` |
| `2026-08-25 08:27:46` | `cowrie.session.params` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.success` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.command.input` |
| `2026-08-25 08:27:46` | `cowrie.log.closed` |
| `2026-08-25 08:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7b04a7e859

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:28 |
| **Last Seen** | 2026-08-25 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:28:27` | `cowrie.session.connect` |
| `2026-08-25 08:28:28` | `cowrie.client.version` |
| `2026-08-25 08:28:28` | `cowrie.client.kex` |
| `2026-08-25 08:28:29` | `cowrie.login.success` |
| `2026-08-25 08:28:29` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:28:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:28:29` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137006af5a4c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:28 |
| **Last Seen** | 2026-08-25 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:28:32` | `cowrie.session.connect` |
| `2026-08-25 08:28:32` | `cowrie.client.version` |
| `2026-08-25 08:28:32` | `cowrie.client.kex` |
| `2026-08-25 08:28:33` | `cowrie.login.success` |
| `2026-08-25 08:28:33` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:28:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:28:34` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f8d9763f32

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:28 |
| **Last Seen** | 2026-08-25 08:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:28:48` | `cowrie.session.connect` |
| `2026-08-25 08:28:48` | `cowrie.client.version` |
| `2026-08-25 08:28:48` | `cowrie.client.kex` |
| `2026-08-25 08:28:49` | `cowrie.login.success` |
| `2026-08-25 08:28:50` | `cowrie.session.params` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.success` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.command.input` |
| `2026-08-25 08:28:50` | `cowrie.log.closed` |
| `2026-08-25 08:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b07a198b04e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:29 |
| **Last Seen** | 2026-08-25 08:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:29:54` | `cowrie.session.connect` |
| `2026-08-25 08:29:54` | `cowrie.client.version` |
| `2026-08-25 08:29:54` | `cowrie.client.kex` |
| `2026-08-25 08:29:55` | `cowrie.login.success` |
| `2026-08-25 08:29:56` | `cowrie.session.params` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.success` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.command.input` |
| `2026-08-25 08:29:56` | `cowrie.log.closed` |
| `2026-08-25 08:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47634ba5ad13

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:31 |
| **Last Seen** | 2026-08-25 08:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:31:04` | `cowrie.session.connect` |
| `2026-08-25 08:31:04` | `cowrie.client.version` |
| `2026-08-25 08:31:04` | `cowrie.client.kex` |
| `2026-08-25 08:31:05` | `cowrie.login.success` |
| `2026-08-25 08:31:06` | `cowrie.session.params` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.success` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.command.input` |
| `2026-08-25 08:31:06` | `cowrie.log.closed` |
| `2026-08-25 08:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57f009c39fa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:32 |
| **Last Seen** | 2026-08-25 08:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:32:17` | `cowrie.session.connect` |
| `2026-08-25 08:32:17` | `cowrie.client.version` |
| `2026-08-25 08:32:17` | `cowrie.client.kex` |
| `2026-08-25 08:32:18` | `cowrie.login.success` |
| `2026-08-25 08:32:19` | `cowrie.session.params` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.success` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.command.input` |
| `2026-08-25 08:32:19` | `cowrie.log.closed` |
| `2026-08-25 08:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc54f21d93db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:33 |
| **Last Seen** | 2026-08-25 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:33:32` | `cowrie.session.connect` |
| `2026-08-25 08:33:32` | `cowrie.client.version` |
| `2026-08-25 08:33:32` | `cowrie.client.kex` |
| `2026-08-25 08:33:33` | `cowrie.login.success` |
| `2026-08-25 08:33:34` | `cowrie.session.params` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.success` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.command.input` |
| `2026-08-25 08:33:34` | `cowrie.log.closed` |
| `2026-08-25 08:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869fd5332b9f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:34 |
| **Last Seen** | 2026-08-25 08:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:34:51` | `cowrie.session.connect` |
| `2026-08-25 08:34:51` | `cowrie.client.version` |
| `2026-08-25 08:34:51` | `cowrie.client.kex` |
| `2026-08-25 08:34:52` | `cowrie.login.success` |
| `2026-08-25 08:34:53` | `cowrie.session.params` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.success` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.command.input` |
| `2026-08-25 08:34:53` | `cowrie.log.closed` |
| `2026-08-25 08:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8efbcfb20ddc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:36 |
| **Last Seen** | 2026-08-25 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:36:10` | `cowrie.session.connect` |
| `2026-08-25 08:36:10` | `cowrie.client.version` |
| `2026-08-25 08:36:10` | `cowrie.client.kex` |
| `2026-08-25 08:36:10` | `cowrie.login.success` |
| `2026-08-25 08:36:11` | `cowrie.session.params` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.success` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:11` | `cowrie.command.input` |
| `2026-08-25 08:36:12` | `cowrie.log.closed` |
| `2026-08-25 08:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a826bf204c4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:37 |
| **Last Seen** | 2026-08-25 08:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:37:25` | `cowrie.session.connect` |
| `2026-08-25 08:37:25` | `cowrie.client.version` |
| `2026-08-25 08:37:25` | `cowrie.client.kex` |
| `2026-08-25 08:37:26` | `cowrie.login.success` |
| `2026-08-25 08:37:27` | `cowrie.session.params` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.success` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.command.input` |
| `2026-08-25 08:37:27` | `cowrie.log.closed` |
| `2026-08-25 08:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c972093c8b4a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:38 |
| **Last Seen** | 2026-08-25 08:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:38:16` | `cowrie.session.connect` |
| `2026-08-25 08:38:16` | `cowrie.client.version` |
| `2026-08-25 08:38:17` | `cowrie.client.kex` |
| `2026-08-25 08:38:18` | `cowrie.login.success` |
| `2026-08-25 08:38:18` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:38:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:38:19` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a84ba87ef9c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:38 |
| **Last Seen** | 2026-08-25 08:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:38:20` | `cowrie.session.connect` |
| `2026-08-25 08:38:20` | `cowrie.client.version` |
| `2026-08-25 08:38:20` | `cowrie.client.kex` |
| `2026-08-25 08:38:22` | `cowrie.login.success` |
| `2026-08-25 08:38:22` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:38:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:38:22` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b938738607

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:38 |
| **Last Seen** | 2026-08-25 08:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:38:37` | `cowrie.session.connect` |
| `2026-08-25 08:38:37` | `cowrie.client.version` |
| `2026-08-25 08:38:37` | `cowrie.client.kex` |
| `2026-08-25 08:38:38` | `cowrie.login.success` |
| `2026-08-25 08:38:39` | `cowrie.session.params` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.success` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.command.input` |
| `2026-08-25 08:38:39` | `cowrie.log.closed` |
| `2026-08-25 08:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70f1eac5d2e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:39 |
| **Last Seen** | 2026-08-25 08:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:39:51` | `cowrie.session.connect` |
| `2026-08-25 08:39:51` | `cowrie.client.version` |
| `2026-08-25 08:39:51` | `cowrie.client.kex` |
| `2026-08-25 08:39:52` | `cowrie.login.success` |
| `2026-08-25 08:39:53` | `cowrie.session.params` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.success` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.command.input` |
| `2026-08-25 08:39:53` | `cowrie.log.closed` |
| `2026-08-25 08:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946be245d056

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:41 |
| **Last Seen** | 2026-08-25 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:41:09` | `cowrie.session.connect` |
| `2026-08-25 08:41:09` | `cowrie.client.version` |
| `2026-08-25 08:41:09` | `cowrie.client.kex` |
| `2026-08-25 08:41:09` | `cowrie.login.success` |
| `2026-08-25 08:41:10` | `cowrie.session.params` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.success` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.command.input` |
| `2026-08-25 08:41:10` | `cowrie.log.closed` |
| `2026-08-25 08:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703f0ebea384

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:42 |
| **Last Seen** | 2026-08-25 08:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:42:26` | `cowrie.session.connect` |
| `2026-08-25 08:42:26` | `cowrie.client.version` |
| `2026-08-25 08:42:26` | `cowrie.client.kex` |
| `2026-08-25 08:42:27` | `cowrie.login.success` |
| `2026-08-25 08:42:28` | `cowrie.session.params` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.success` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.command.input` |
| `2026-08-25 08:42:28` | `cowrie.log.closed` |
| `2026-08-25 08:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309726974c98

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:43 |
| **Last Seen** | 2026-08-25 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:43:44` | `cowrie.session.connect` |
| `2026-08-25 08:43:44` | `cowrie.client.version` |
| `2026-08-25 08:43:44` | `cowrie.client.kex` |
| `2026-08-25 08:43:44` | `cowrie.login.success` |
| `2026-08-25 08:43:45` | `cowrie.session.params` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.success` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.command.input` |
| `2026-08-25 08:43:45` | `cowrie.log.closed` |
| `2026-08-25 08:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a93ba074cf2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:45 |
| **Last Seen** | 2026-08-25 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:45:00` | `cowrie.session.connect` |
| `2026-08-25 08:45:00` | `cowrie.client.version` |
| `2026-08-25 08:45:00` | `cowrie.client.kex` |
| `2026-08-25 08:45:00` | `cowrie.login.success` |
| `2026-08-25 08:45:01` | `cowrie.session.params` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.success` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.command.input` |
| `2026-08-25 08:45:01` | `cowrie.log.closed` |
| `2026-08-25 08:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972d20ed7760

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:46 |
| **Last Seen** | 2026-08-25 08:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:46:18` | `cowrie.session.connect` |
| `2026-08-25 08:46:18` | `cowrie.client.version` |
| `2026-08-25 08:46:18` | `cowrie.client.kex` |
| `2026-08-25 08:46:18` | `cowrie.login.success` |
| `2026-08-25 08:46:19` | `cowrie.session.params` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.success` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:19` | `cowrie.command.input` |
| `2026-08-25 08:46:20` | `cowrie.log.closed` |
| `2026-08-25 08:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc02efa01f0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:47 |
| **Last Seen** | 2026-08-25 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:47:36` | `cowrie.session.connect` |
| `2026-08-25 08:47:36` | `cowrie.client.version` |
| `2026-08-25 08:47:36` | `cowrie.client.kex` |
| `2026-08-25 08:47:36` | `cowrie.login.success` |
| `2026-08-25 08:47:37` | `cowrie.session.params` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.success` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:37` | `cowrie.command.input` |
| `2026-08-25 08:47:38` | `cowrie.log.closed` |
| `2026-08-25 08:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5618a96fefea

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:48 |
| **Last Seen** | 2026-08-25 08:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:48:01` | `cowrie.session.connect` |
| `2026-08-25 08:48:01` | `cowrie.client.version` |
| `2026-08-25 08:48:01` | `cowrie.client.kex` |
| `2026-08-25 08:48:03` | `cowrie.login.success` |
| `2026-08-25 08:48:03` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:48:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:48:03` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a8983cfbba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-25 08:48 |
| **Last Seen** | 2026-08-25 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:48:04` | `cowrie.session.connect` |
| `2026-08-25 08:48:04` | `cowrie.client.version` |
| `2026-08-25 08:48:04` | `cowrie.client.kex` |
| `2026-08-25 08:48:05` | `cowrie.login.success` |
| `2026-08-25 08:48:05` | `cowrie.direct-tcpip.request` |
| `2026-08-25 08:48:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-25 08:48:06` | `cowrie.direct-tcpip.data` |
| `2026-08-25 08:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d5ae6ff38b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:48 |
| **Last Seen** | 2026-08-25 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:48:51` | `cowrie.session.connect` |
| `2026-08-25 08:48:51` | `cowrie.client.version` |
| `2026-08-25 08:48:51` | `cowrie.client.kex` |
| `2026-08-25 08:48:52` | `cowrie.login.success` |
| `2026-08-25 08:48:53` | `cowrie.session.params` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.success` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.command.input` |
| `2026-08-25 08:48:53` | `cowrie.log.closed` |
| `2026-08-25 08:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c15347616e54

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-08-25 08:50 |
| **Last Seen** | 2026-08-25 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-25 08:50:06` | `cowrie.session.connect` |
| `2026-08-25 08:50:06` | `cowrie.client.version` |
| `2026-08-25 08:50:06` | `cowrie.client.kex` |
| `2026-08-25 08:50:07` | `cowrie.login.success` |
| `2026-08-25 08:50:08` | `cowrie.session.params` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.success` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.command.input` |
| `2026-08-25 08:50:08` | `cowrie.log.closed` |
| `2026-08-25 08:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]191` | **7** | 2026-08-25 06:55 | 2026-08-25 08:14 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-25 07:07 | 2026-08-25 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `134.209.229[.]23` | **4** | 2026-08-25 07:07 | 2026-08-25 08:34 | 3m | 0 | `T1592` | 🟢 LOW |
| `91.203.63[.]71` | **4** | 2026-08-25 08:07 | 2026-08-25 08:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-08-25 07:25 | 2026-08-25 08:26 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `151.243.11[.]8` | **2** | 2026-08-25 08:31 | 2026-08-25 08:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.59.114[.]78` | **2** | 2026-08-25 08:13 | 2026-08-25 08:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.62[.]150` | **2** | 2026-08-25 07:37 | 2026-08-25 07:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.87.80[.]62` | 1 | 2026-08-25 08:32 | 2026-08-25 08:32 | 13s | 0 | `T1592` | 🟢 LOW |
| `111.53.8[.]101` | 1 | 2026-08-25 08:39 | 2026-08-25 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.233.207[.]57` | 1 | 2026-08-25 08:11 | 2026-08-25 08:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]139` | 1 | 2026-08-25 08:44 | 2026-08-25 08:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.230.86[.]205` | 1 | 2026-08-25 07:10 | 2026-08-25 07:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `222.88.163[.]202` | 1 | 2026-08-25 08:25 | 2026-08-25 08:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-08-25 08:35 | 2026-08-25 08:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `5.44.170[.]92` | 1 | 2026-08-25 07:52 | 2026-08-25 07:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | 1 | 2026-08-25 08:17 | 2026-08-25 08:18 | 87s | 0 | `T1592` | 🟢 LOW |

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
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `109.87.80[.]62` | UA | CONTENT DELIVERY NETWORK LTD | **100** ⚠️ | 0 |
| `200.59.127[.]139` | AR | Sinectis S.A. | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `213.230.86[.]205` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 6 |
| `45.79.207[.]252` | US | Linode | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `91.203.63[.]71` | UA | Ukrchermetavtomatika LLC | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 142 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 132 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 102 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 102 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 101 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 182 cases |
| Tool 34  | Credential Extractor        | ✅ 141 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (7.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 18 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 132 priority case(s) shown individually · 17 recon entry/entries in table (8 group(s) consolidating 28 session(s)).

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
_Report time: 2026-08-25T10:37:19Z_

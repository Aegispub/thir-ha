# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-24 |
| **Generated At** | 2026-06-24T23:08:33Z |
| **Shift Time** | 23:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **698** |
| Confirmed Threats | **681** |
| False Positives Filtered | **17** (2.4%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **13** |
| High Severity Cases | **308** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **390** |
| Malware Samples Analyzed | **4** HIGH · **26** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **325** |
| Unique Credential Pairs | **297** |
| Unique Usernames | **160** |
| Unique Passwords | **245** |
| Successful Auth Pairs | **305** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 120 |
| `admin` | 22 |
| `ubuntu` | 12 |
| `dell` | 5 |
| `oracle` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 29 |
| `admin` | 12 |
| `` | 6 |
| `123` | 5 |
| `1234` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 12 |
| `admin` | `` | 6 |
| `root` | `123@@@` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `plmoknijbuhvygctfxrdz` | `209.99.185.59` | 2026-06-24T18:55:47 |
| `sumin` | `1234` | `209.99.185.59` | 2026-06-24T18:56:42 |
| `adm` | `adm123` | `45.205.1.42` | 2026-06-24T18:57:12 |
| `steam` | `123` | `209.99.185.59` | 2026-06-24T18:57:36 |
| `inspur` | `123456` | `209.99.185.59` | 2026-06-24T18:58:30 |
| `chengjj2` | `yppasswd` | `209.99.185.59` | 2026-06-24T18:59:24 |
| `ubuntu` | `user123456` | `209.99.185.59` | 2026-06-24T19:00:19 |
| `caoxt` | `QUktyzysWd` | `209.99.185.59` | 2026-06-24T19:01:15 |
| `alice` | `123456` | `209.99.185.59` | 2026-06-24T19:02:11 |
| `office` | `office` | `209.99.185.59` | 2026-06-24T19:03:07 |
| `root` | `321456` | `209.99.185.59` | 2026-06-24T19:04:01 |
| `lanyun` | `admin123456` | `209.99.185.59` | 2026-06-24T19:04:55 |
| `ftp` | `111111` | `209.99.185.59` | 2026-06-24T19:05:48 |
| `jiafenglin` | `jiafenglin` | `209.99.185.59` | 2026-06-24T19:06:44 |
| `admin` | `admin` | `10.0.0.73` | 2026-06-24T19:07:25 |
| `aaa` | `aaa123` | `209.99.185.59` | 2026-06-24T19:07:39 |
| `ts3` | `ts3` | `209.99.185.59` | 2026-06-24T19:08:37 |
| `mbb` | `mbb` | `209.99.185.59` | 2026-06-24T19:09:33 |
| `nvidia` | `123456` | `209.99.185.59` | 2026-06-24T19:10:30 |
| `ubuntu` | `user123456` | `45.205.1.42` | 2026-06-24T19:11:24 |
| `ul` | `666666` | `209.99.185.59` | 2026-06-24T19:11:25 |
| `root` | `shenhua` | `209.99.185.59` | 2026-06-24T19:12:23 |
| `root` | `pass123` | `209.99.185.59` | 2026-06-24T19:13:21 |
| `dell` | `dell1234` | `209.99.185.59` | 2026-06-24T19:14:20 |
| `root` | `mobile1` | `209.99.185.59` | 2026-06-24T19:15:19 |
| `root` | `b` | `209.99.185.59` | 2026-06-24T19:16:18 |
| `admin` | `admin123456` | `209.99.185.59` | 2026-06-24T19:17:15 |
| `zhangsan` | `666666` | `209.99.185.59` | 2026-06-24T19:18:12 |
| `yaoye` | `yaoye` | `209.99.185.59` | 2026-06-24T19:19:08 |
| `root` | `mobcb@xinyuehui2020` | `209.99.185.59` | 2026-06-24T19:20:07 |
| `loose` | `666666` | `209.99.185.59` | 2026-06-24T19:21:06 |
| `srun` | `srun` | `209.99.185.59` | 2026-06-24T19:22:05 |
| `sadri` | `123456` | `209.99.185.59` | 2026-06-24T19:23:04 |
| `ntpo` | `o9p0ku98jokmn.k` | `209.99.185.59` | 2026-06-24T19:24:03 |
| `ftpuser` | `123qwe` | `209.99.185.59` | 2026-06-24T19:25:02 |
| `root` | `123@@@` | `64.110.90.250` | 2026-06-24T19:25:16 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-06-24T19:25:16 |
| `ubuntu` | `deploy123456789` | `45.205.1.42` | 2026-06-24T19:25:36 |
| `docker` | `tcuser` | `209.99.185.59` | 2026-06-24T19:26:03 |
| `admin` | `1` | `209.99.185.59` | 2026-06-24T19:27:06 |
| `root` | `123@@@` | `144.22.238.238` | 2026-06-24T19:27:52 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-06-24T19:27:53 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-06-24T19:28:03 |
| `wc21` | `wc131619` | `209.99.185.59` | 2026-06-24T19:28:10 |
| `usuario` | `usuario1` | `209.99.185.59` | 2026-06-24T19:29:12 |
| `newuser` | `1234` | `209.99.185.59` | 2026-06-24T19:30:14 |
| `root` | `olivia` | `209.99.185.59` | 2026-06-24T19:31:16 |
| `root` | `admin!QAZ@#$` | `209.99.185.59` | 2026-06-24T19:32:18 |
| `srudent` | `srudent` | `209.99.185.59` | 2026-06-24T19:33:22 |
| `nagios` | `test123` | `209.99.185.59` | 2026-06-24T19:34:27 |
| `devuser` | `12345` | `209.99.185.59` | 2026-06-24T19:35:30 |
| `root` | `1,d0b.2s,1g11` | `209.99.185.59` | 2026-06-24T19:36:31 |
| `root` | `1qaSW@3ed` | `209.99.185.59` | 2026-06-24T19:37:32 |
| `chenml` | `chenml123` | `209.99.185.59` | 2026-06-24T19:38:35 |
| `cjw` | `cjw` | `209.99.185.59` | 2026-06-24T19:39:39 |
| `databse` | `database` | `45.205.1.42` | 2026-06-24T19:39:41 |
| `zhanglei` | `zhanglei` | `209.99.185.59` | 2026-06-24T19:40:45 |
| `user` | `6Eeaf913e9551d93c10A` | `209.99.185.59` | 2026-06-24T19:41:49 |
| `root` | `admin@#$%` | `209.99.185.59` | 2026-06-24T19:42:53 |
| `kim` | `kim` | `209.99.185.59` | 2026-06-24T19:43:56 |
| `root` | `q1w2e3` | `209.99.185.59` | 2026-06-24T19:45:01 |
| `users5` | `users5` | `209.99.185.59` | 2026-06-24T19:46:10 |
| `root` | `qazxcvp-0!@#` | `209.99.185.59` | 2026-06-24T19:47:19 |
| `root` | `123` | `91.92.40.233` | 2026-06-24T19:47:27 |
| `oracle` | `oracle!1` | `209.99.185.59` | 2026-06-24T19:48:27 |
| `root` | `1234` | `91.92.40.233` | 2026-06-24T19:49:15 |
| `wkl` | `ygjjhnbdxz` | `209.99.185.59` | 2026-06-24T19:49:32 |
| `root` | `12345abc` | `209.99.185.59` | 2026-06-24T19:50:38 |
| `root` | `12345` | `91.92.40.233` | 2026-06-24T19:51:22 |
| `ubuntu` | `qwerty` | `209.99.185.59` | 2026-06-24T19:51:43 |
| `root` | `!@#$123` | `209.99.185.59` | 2026-06-24T19:52:50 |
| `root` | `qwe12#` | `45.205.1.42` | 2026-06-24T19:53:30 |
| `ndlabs` | `123` | `209.99.185.59` | 2026-06-24T19:53:58 |
| `root` | `1234567` | `91.92.40.233` | 2026-06-24T19:54:50 |
| `turnserver` | `1` | `209.99.185.59` | 2026-06-24T19:55:03 |
| `student` | `student1` | `209.99.185.59` | 2026-06-24T19:56:08 |
| `root` | `12345678` | `91.92.40.233` | 2026-06-24T19:56:32 |
| `sjb` | `korea2016` | `209.99.185.59` | 2026-06-24T19:57:12 |
| `root` | `123456789` | `91.92.40.233` | 2026-06-24T19:58:12 |
| `root` | `ROsLNa1O&#039;ZHGNOI` | `209.99.185.59` | 2026-06-24T19:58:19 |
| `postgres` | `pas1sword` | `209.99.185.59` | 2026-06-24T19:59:27 |
| `root` | `1234567890` | `91.92.40.233` | 2026-06-24T19:59:53 |
| `re` | `re` | `209.99.185.59` | 2026-06-24T20:00:29 |
| `es` | `es123!@#` | `209.99.185.59` | 2026-06-24T20:01:13 |
| `root` | `123abc` | `91.92.40.233` | 2026-06-24T20:01:32 |
| `www-data` | `l3tm31n` | `209.99.185.59` | 2026-06-24T20:01:58 |
| `guest` | `000000` | `209.99.185.59` | 2026-06-24T20:02:42 |
| `root` | `1q2w3e4r` | `91.92.40.233` | 2026-06-24T20:03:13 |
| `root` | `barcelona` | `209.99.185.59` | 2026-06-24T20:03:28 |
| `yyxue` | `502181795` | `209.99.185.59` | 2026-06-24T20:04:15 |
| `root` | `Admin@2021` | `209.99.185.59` | 2026-06-24T20:05:01 |
| `ashish` | `ashish` | `209.99.185.59` | 2026-06-24T20:05:48 |
| `root` | `1q@w#e$r` | `209.99.185.59` | 2026-06-24T20:06:35 |
| `reebee` | `123456` | `209.99.185.59` | 2026-06-24T20:07:21 |
| `root` | `web1` | `45.205.1.42` | 2026-06-24T20:07:54 |
| `root` | `Aa@123456` | `209.99.185.59` | 2026-06-24T20:08:07 |
| `root` | `P@55w0rd!` | `209.99.185.59` | 2026-06-24T20:08:51 |
| `weblogic` | `weblogic123` | `209.99.185.59` | 2026-06-24T20:09:35 |
| `root` | `qhy123456` | `209.99.185.59` | 2026-06-24T20:10:20 |
| `lzc` | `lzc` | `209.99.185.59` | 2026-06-24T20:11:05 |
| `solr` | `123456` | `209.99.185.59` | 2026-06-24T20:11:51 |
| `root` | `qq7758521` | `209.99.185.59` | 2026-06-24T20:12:37 |
| `root` | `Pass@word!@#456` | `209.99.185.59` | 2026-06-24T20:13:23 |
| `root` | `Dandy@123` | `209.99.185.59` | 2026-06-24T20:14:08 |
| `root` | `Admin@222` | `209.99.185.59` | 2026-06-24T20:14:53 |
| `root` | `Sugon@2022` | `209.99.185.59` | 2026-06-24T20:15:38 |
| `yangliusha9` | `yangliusha9` | `209.99.185.59` | 2026-06-24T20:16:24 |
| `www-data` | `1q2w3e` | `209.99.185.59` | 2026-06-24T20:17:11 |
| `user` | `changeme` | `209.99.185.59` | 2026-06-24T20:17:59 |
| `root` | `root@2222` | `209.99.185.59` | 2026-06-24T20:18:48 |
| `zhaoxz` | `Zhao6393003` | `209.99.185.59` | 2026-06-24T20:19:36 |
| `hengshi` | `hengshi` | `209.99.185.59` | 2026-06-24T20:20:24 |
| `kyt` | `123456` | `209.99.185.59` | 2026-06-24T20:21:10 |
| `root` | `PASS123456` | `209.99.185.59` | 2026-06-24T20:21:56 |
| `web` | `web` | `45.205.1.42` | 2026-06-24T20:22:10 |
| `pul` | `passwd` | `209.99.185.59` | 2026-06-24T20:22:42 |
| `ora_root` | `123456` | `209.99.185.59` | 2026-06-24T20:23:29 |
| `ceiling` | `caicaicai` | `209.99.185.59` | 2026-06-24T20:24:16 |
| `root` | `s198364mply` | `209.99.185.59` | 2026-06-24T20:25:05 |
| `root` | `P@ssw0rd!@#` | `209.99.185.59` | 2026-06-24T20:25:52 |
| `dxc22` | `20218123` | `209.99.185.59` | 2026-06-24T20:26:39 |
| `zq` | `qz` | `209.99.185.59` | 2026-06-24T20:27:26 |
| `root` | `PASS1` | `209.99.185.59` | 2026-06-24T20:28:13 |
| `longzr` | `lzrlab602` | `209.99.185.59` | 2026-06-24T20:29:00 |
| `root` | `qwertyuio` | `209.99.185.59` | 2026-06-24T20:29:48 |
| `root` | `playboy2` | `209.99.185.59` | 2026-06-24T20:30:38 |
| `wpyan` | `P@ssw0rd` | `209.99.185.59` | 2026-06-24T20:31:28 |
| `tomcat` | `tomcat` | `209.99.185.59` | 2026-06-24T20:32:17 |
| `admin` | `admin1` | `209.99.185.59` | 2026-06-24T20:33:08 |
| `phj` | `123456` | `209.99.185.59` | 2026-06-24T20:33:57 |
| `root` | `wsxedcrfvtgb` | `209.99.185.59` | 2026-06-24T20:34:45 |
| `deploy` | `test` | `209.99.185.59` | 2026-06-24T20:35:35 |
| `test1` | `password` | `209.99.185.59` | 2026-06-24T20:36:24 |
| `root` | `Pass!@` | `45.205.1.42` | 2026-06-24T20:36:49 |
| `hai` | `123456` | `209.99.185.59` | 2026-06-24T20:37:16 |
| `xuyusheng` | `hrh4h8r4` | `209.99.185.59` | 2026-06-24T20:38:08 |
| `dasco` | `dasco` | `209.99.185.59` | 2026-06-24T20:39:00 |
| `root` | `friends` | `209.99.185.59` | 2026-06-24T20:39:50 |
| `dell` | `Admin@2021` | `209.99.185.59` | 2026-06-24T20:40:41 |
| `ubuntu` | `123123123` | `209.99.185.59` | 2026-06-24T20:41:32 |
| `stratos` | `123456` | `209.99.185.59` | 2026-06-24T20:42:24 |
| `root` | `123qwerty` | `92.118.39.77` | 2026-06-24T20:42:26 |
| `root` | `worldclass` | `209.99.185.59` | 2026-06-24T20:45:51 |
| `maru` | `1234` | `209.99.185.59` | 2026-06-24T20:46:41 |
| `yeh` | `yeh` | `209.99.185.59` | 2026-06-24T20:47:31 |
| `dell` | `dell@3333` | `209.99.185.59` | 2026-06-24T20:48:21 |
| `pzy` | `pzy123` | `209.99.185.59` | 2026-06-24T20:49:13 |
| `dell` | `Admin@999` | `209.99.185.59` | 2026-06-24T20:50:06 |
| `dyl` | `123456` | `209.99.185.59` | 2026-06-24T20:50:59 |
| `root` | `mediaexcel` | `45.205.1.42` | 2026-06-24T20:51:18 |
| `amandabackup` | `amandabackup` | `209.99.185.59` | 2026-06-24T20:51:53 |
| `download` | `download` | `209.99.185.59` | 2026-06-24T20:52:45 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-06-24T20:53:29 |
| `root` | `123@@@` | `129.153.145.135` | 2026-06-24T20:53:29 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-06-24T20:53:38 |
| `ypt` | `ypt` | `209.99.185.59` | 2026-06-24T20:53:38 |
| `root` | `3333333` | `209.99.185.59` | 2026-06-24T20:54:31 |
| `hubeizhe` | `hubeizhenb` | `209.99.185.59` | 2026-06-24T20:55:26 |
| `proxy` | `proxy` | `209.99.185.59` | 2026-06-24T20:56:20 |
| `yifeng` | `123456` | `209.99.185.59` | 2026-06-24T20:57:15 |
| `peer` | `333333` | `209.99.185.59` | 2026-06-24T20:58:09 |
| `ubuntu` | `qwerty123456789` | `209.99.185.59` | 2026-06-24T20:59:01 |
| `srz` | `srz` | `209.99.185.59` | 2026-06-24T20:59:53 |
| `root` | `P5ssw0rd` | `209.99.185.59` | 2026-06-24T21:00:46 |
| `cym` | `123456` | `209.99.185.59` | 2026-06-24T21:01:40 |
| `admin` | `admin` | `45.148.10.121` | 2026-06-24T21:01:54 |
| `papercut` | `papercut` | `209.99.185.59` | 2026-06-24T21:02:35 |
| `root` | `owner` | `209.99.185.59` | 2026-06-24T21:03:30 |
| `ubuntu` | `qazzxc` | `209.99.185.59` | 2026-06-24T21:04:26 |
| `root` | `bigboss` | `209.99.185.59` | 2026-06-24T21:05:21 |
| `root` | `Qwsx333999Qwsx1111#` | `45.205.1.42` | 2026-06-24T21:05:37 |
| `jingluoxi` | `jingluoxi` | `209.99.185.59` | 2026-06-24T21:06:16 |
| `libsys` | `123456` | `209.99.185.59` | 2026-06-24T21:07:10 |
| `root` | `futurelight@wuzhen2021` | `209.99.185.59` | 2026-06-24T21:08:06 |
| `root` | `as1QxERJVY` | `10.0.0.73` | 2026-06-24T21:08:24 |
| `hadoop` | `12345678` | `209.99.185.59` | 2026-06-24T21:09:03 |
| `claudia` | `claudia` | `209.99.185.59` | 2026-06-24T21:10:00 |
| `fzz` | `Fzz123456` | `209.99.185.59` | 2026-06-24T21:10:55 |
| `wangtao` | `wangtao` | `209.99.185.59` | 2026-06-24T21:11:50 |
| `ub` | `111111` | `209.99.185.59` | 2026-06-24T21:12:45 |
| `huxiao` | `123456` | `209.99.185.59` | 2026-06-24T21:13:41 |
| `dqj` | `123` | `209.99.185.59` | 2026-06-24T21:14:37 |
| `root` | `guest` | `209.99.185.59` | 2026-06-24T21:15:36 |
| `pms` | `123456` | `209.99.185.59` | 2026-06-24T21:16:35 |
| `root` | `!@#$QWER` | `209.99.185.59` | 2026-06-24T21:17:33 |
| `john` | `password` | `209.99.185.59` | 2026-06-24T21:18:30 |
| `mysql` | `1q2w3e` | `209.99.185.59` | 2026-06-24T21:19:27 |
| `postmaster` | `password` | `45.205.1.42` | 2026-06-24T21:20:07 |
| `testuser2` | `123456` | `209.99.185.59` | 2026-06-24T21:20:26 |
| `fw` | `fw` | `209.99.185.59` | 2026-06-24T21:21:26 |
| `tem_common` | `tem_common` | `209.99.185.59` | 2026-06-24T21:22:27 |
| `root` | `Password!1` | `209.99.185.59` | 2026-06-24T21:23:27 |
| `root` | `senha` | `209.99.185.59` | 2026-06-24T21:24:26 |
| `ela` | `ela` | `209.99.185.59` | 2026-06-24T21:25:23 |
| `max` | `max` | `209.99.185.59` | 2026-06-24T21:26:22 |
| `root` | `password` | `209.99.185.59` | 2026-06-24T21:27:22 |
| `yuanwd` | `password123` | `209.99.185.59` | 2026-06-24T21:28:23 |
| `Xroot` | `Xroot` | `209.99.185.59` | 2026-06-24T21:29:24 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.137` | 2026-06-24T21:29:32 |
| `d302` | `d302` | `209.99.185.59` | 2026-06-24T21:30:25 |
| `ansible` | `123` | `209.99.185.59` | 2026-06-24T21:31:26 |
| `oracle` | `qazwsxedc123` | `209.99.185.59` | 2026-06-24T21:32:29 |
| `yansq` | `ysq123` | `209.99.185.59` | 2026-06-24T21:33:32 |
| `root` | `P@ssword` | `45.205.1.42` | 2026-06-24T21:34:23 |
| `hiyan` | `123456` | `209.99.185.59` | 2026-06-24T21:34:37 |
| `root` | `asd123!!@#Ad23` | `209.99.185.59` | 2026-06-24T21:35:42 |
| `hadoop` | `1234qwer` | `209.99.185.59` | 2026-06-24T21:36:46 |
| `huzhihao` | `z1Jvv2fL4m4Il@y8` | `209.99.185.59` | 2026-06-24T21:37:49 |
| `tianlixu` | `tianlixu2021` | `209.99.185.59` | 2026-06-24T21:38:54 |
| `dingy` | `123qwe` | `209.99.185.59` | 2026-06-24T21:40:01 |
| `all` | `all123` | `209.99.185.59` | 2026-06-24T21:41:10 |
| `july` | `july` | `209.99.185.59` | 2026-06-24T21:42:18 |
| `root` | `c` | `209.99.185.59` | 2026-06-24T21:43:27 |
| `root` | `cde3XSW@zaq1` | `209.99.185.59` | 2026-06-24T21:44:34 |
| `root` | `444` | `209.99.185.59` | 2026-06-24T21:45:45 |
| `root` | `cdnadmin` | `10.0.0.73` | 2026-06-24T21:46:49 |
| `root` | `Baidu` | `209.99.185.59` | 2026-06-24T21:46:55 |
| `gmy` | `123456` | `209.99.185.59` | 2026-06-24T21:48:06 |
| `ubuntu` | `12345qwert` | `45.205.1.42` | 2026-06-24T21:48:52 |
| `root` | `pokemon` | `209.99.185.59` | 2026-06-24T21:49:14 |
| `root` | `Aa123456!` | `209.99.185.59` | 2026-06-24T21:50:20 |
| `gpu02` | `gpu02123` | `209.99.185.59` | 2026-06-24T21:51:24 |
| `ubuntu` | `rootadmin` | `209.99.185.59` | 2026-06-24T21:52:31 |
| `scsc` | `fxl@2022` | `209.99.185.59` | 2026-06-24T21:53:38 |
| `kgma` | `kgma` | `209.99.185.59` | 2026-06-24T21:54:45 |
| `hy` | `123456` | `209.99.185.59` | 2026-06-24T21:55:52 |
| `root` | `Oc49m3sY` | `209.99.185.59` | 2026-06-24T21:56:59 |
| `root` | `Hekou@2020` | `209.99.185.59` | 2026-06-24T21:58:06 |
| `root` | `123654789` | `209.99.185.59` | 2026-06-24T21:59:15 |
| `deploy` | `q1w2e3r4` | `209.99.185.59` | 2026-06-24T22:00:22 |
| `web1` | `p@55w0rd` | `209.99.185.59` | 2026-06-24T22:01:07 |
| `aaaaaa` | `aaaaaa` | `209.99.185.59` | 2026-06-24T22:01:51 |
| `root` | `qwe!@#$` | `209.99.185.59` | 2026-06-24T22:02:35 |
| `root` | `11111111` | `45.205.1.42` | 2026-06-24T22:03:11 |
| `dev` | `12345678` | `209.99.185.59` | 2026-06-24T22:03:19 |
| `sander` | `sander1234` | `209.99.185.59` | 2026-06-24T22:04:02 |
| `aminuosi` | `qazplm74` | `209.99.185.59` | 2026-06-24T22:04:46 |
| `datacenter` | `abc123` | `209.99.185.59` | 2026-06-24T22:05:31 |
| `root` | `Password1!` | `209.99.185.59` | 2026-06-24T22:06:18 |
| `root` | `dragon` | `209.99.185.59` | 2026-06-24T22:07:04 |
| `root` | `Pass!` | `209.99.185.59` | 2026-06-24T22:07:49 |
| `azim` | `7890uiop` | `209.99.185.59` | 2026-06-24T22:08:34 |
| `zhl` | `123456` | `209.99.185.59` | 2026-06-24T22:09:19 |
| `emily` | `emily` | `209.99.185.59` | 2026-06-24T22:10:04 |
| `yuany` | `111111` | `209.99.185.59` | 2026-06-24T22:10:50 |
| `oracle` | `baseball` | `209.99.185.59` | 2026-06-24T22:11:35 |
| `root` | `88888888` | `209.99.185.59` | 2026-06-24T22:12:23 |
| `ts3` | `123456` | `209.99.185.59` | 2026-06-24T22:13:10 |
| `root` | `---fuck_you----` | `120.26.240.78` | 2026-06-24T22:13:35 |
| `root` | `j` | `209.99.185.59` | 2026-06-24T22:13:58 |
| `admin` | `admin` | `47.85.8.171` | 2026-06-24T22:14:21 |
| `admin` | `admin` | `130.12.180.51` | 2026-06-24T22:14:22 |
| `server` | `p@ssw0rd` | `209.99.185.59` | 2026-06-24T22:14:45 |
| `root` | `7` | `209.99.185.59` | 2026-06-24T22:15:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `185.226.196.15` | 2026-06-24T22:15:37 |
| `ubuntu` | `basketball` | `209.99.185.59` | 2026-06-24T22:16:17 |
| `ghost` | `ghost1` | `209.99.185.59` | 2026-06-24T22:17:03 |
| `ubuntu` | `pass123456789` | `45.205.1.42` | 2026-06-24T22:17:34 |
| `wangdui` | `wangdui` | `209.99.185.59` | 2026-06-24T22:17:50 |
| `ec2-user` | `123456` | `209.99.185.59` | 2026-06-24T22:18:39 |
| `root` | `TRyjt_2019_tjyRT` | `209.99.185.59` | 2026-06-24T22:19:29 |
| `admin` | `admin` | `144.31.220.41` | 2026-06-24T22:19:38 |
| `xiongza` | `Xzaxza992992` | `209.99.185.59` | 2026-06-24T22:20:17 |
| `agrant` | `vagrant` | `209.99.185.59` | 2026-06-24T22:21:04 |
| `root` | `zaq1xsw2cde3vfr4` | `209.99.185.59` | 2026-06-24T22:21:52 |
| `root` | `skinny` | `209.99.185.59` | 2026-06-24T22:22:40 |
| `root` | `qwedsa` | `209.99.185.59` | 2026-06-24T22:23:29 |
| `admin` | `1qaz!QAZ` | `209.99.185.59` | 2026-06-24T22:24:19 |
| `monica` | `monica` | `209.99.185.59` | 2026-06-24T22:25:08 |
| `wangzixi` | `wangzixi` | `209.99.185.59` | 2026-06-24T22:25:57 |
| `ltm19` | `Zn19970321` | `209.99.185.59` | 2026-06-24T22:26:47 |
| `aaaaaa` | `333333` | `209.99.185.59` | 2026-06-24T22:27:36 |
| `root` | `fudan0905ABC` | `209.99.185.59` | 2026-06-24T22:28:24 |
| `root` | `root.123` | `209.99.185.59` | 2026-06-24T22:29:12 |
| `anaconda` | `123456` | `209.99.185.59` | 2026-06-24T22:30:01 |
| `root` | `d3b1an` | `209.99.185.59` | 2026-06-24T22:30:51 |
| `my` | `my123` | `209.99.185.59` | 2026-06-24T22:31:42 |
| `root` | `P@sswd!@#` | `45.205.1.42` | 2026-06-24T22:31:58 |
| `taow` | `taowei2333` | `209.99.185.59` | 2026-06-24T22:32:33 |
| `root` | `0ok9ij` | `209.99.185.59` | 2026-06-24T22:33:24 |
| `test` | `abc123` | `209.99.185.59` | 2026-06-24T22:34:14 |
| `root` | `qaz123` | `209.99.185.59` | 2026-06-24T22:35:03 |
| `root` | `utility` | `209.99.185.59` | 2026-06-24T22:35:54 |
| `lighthouse` | `lighthouse123` | `209.99.185.59` | 2026-06-24T22:36:45 |
| `dell` | `dell@6000` | `209.99.185.59` | 2026-06-24T22:37:37 |
| `db2inst1` | `db2pass` | `209.99.185.59` | 2026-06-24T22:38:31 |
| `ryan` | `123456` | `209.99.185.59` | 2026-06-24T22:39:25 |
| `root` | `55o4nR1><` | `209.99.185.59` | 2026-06-24T22:40:19 |
| `hadoop` | `111111` | `209.99.185.59` | 2026-06-24T22:41:11 |
| `michelle` | `michelle` | `209.99.185.59` | 2026-06-24T22:42:02 |
| `ubuntu` | `asd12345678` | `209.99.185.59` | 2026-06-24T22:42:55 |
| `root` | `k_nzrwibuvss0nb9` | `209.99.185.59` | 2026-06-24T22:43:53 |
| `mz` | `123456` | `209.99.185.59` | 2026-06-24T22:44:46 |
| `buero3` | `buero3` | `209.99.185.59` | 2026-06-24T22:45:38 |
| `root` | `131313` | `45.205.1.42` | 2026-06-24T22:46:08 |
| `zabbix` | `zabbix@123` | `209.99.185.59` | 2026-06-24T22:46:30 |
| `root` | `555` | `209.99.185.59` | 2026-06-24T22:47:21 |
| `root` | `user123456789` | `209.99.185.59` | 2026-06-24T22:48:12 |
| `personal` | `personal` | `209.99.185.59` | 2026-06-24T22:49:04 |
| `root` | `Qq12345678` | `209.99.185.59` | 2026-06-24T22:49:59 |
| `root` | `admin03` | `209.99.185.59` | 2026-06-24T22:50:54 |
| `root` | `demo0123456789` | `209.99.185.59` | 2026-06-24T22:51:48 |
| `tangziqiang` | `tangziqiang` | `209.99.185.59` | 2026-06-24T22:52:40 |
| `root` | `1234561` | `209.99.185.59` | 2026-06-24T22:53:34 |
| `hadi` | `hadi` | `209.99.185.59` | 2026-06-24T22:54:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **698** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 299 |
| libssh | 19 |
| Paramiko (Python) | 12 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 277 | 2 |
| `a2de0f306611...` | Mirai/variant | 12 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 12 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 3 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 277 | 2 | Generic scanner |
| `95420f9d932d...` | libssh | 14 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 12 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 12 | 2 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `e37f354a101a...` | libssh | 2 | 2 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 10 | 2 | `T1082, T1592, T1078, T1083` |

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
echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'
```
Source IPs: `92.118.39.77`, `91.92.40.233`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **29** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS21859` | Zenlayer Inc | 4 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS31898` | Oracle Corporation | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (307)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7ab4f5b68add

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:55 |
| **Last Seen** | 2026-06-24 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:55:47` | `cowrie.session.connect` |
| `2026-06-24 18:55:47` | `cowrie.client.version` |
| `2026-06-24 18:55:47` | `cowrie.client.kex` |
| `2026-06-24 18:55:47` | `cowrie.login.success` |
| `2026-06-24 18:55:48` | `cowrie.session.params` |
| `2026-06-24 18:55:48` | `cowrie.command.input` |
| `2026-06-24 18:55:48` | `cowrie.log.closed` |
| `2026-06-24 18:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5562247414e3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:56 |
| **Last Seen** | 2026-06-24 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:56:42` | `cowrie.session.connect` |
| `2026-06-24 18:56:42` | `cowrie.client.version` |
| `2026-06-24 18:56:42` | `cowrie.client.kex` |
| `2026-06-24 18:56:42` | `cowrie.login.success` |
| `2026-06-24 18:56:43` | `cowrie.session.params` |
| `2026-06-24 18:56:43` | `cowrie.command.input` |
| `2026-06-24 18:56:43` | `cowrie.log.closed` |
| `2026-06-24 18:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-147245c1c1dc

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 18:57 |
| **Last Seen** | 2026-06-24 18:57 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:57:04` | `cowrie.session.connect` |
| `2026-06-24 18:57:06` | `cowrie.client.version` |
| `2026-06-24 18:57:06` | `cowrie.client.kex` |
| `2026-06-24 18:57:12` | `cowrie.login.success` |
| `2026-06-24 18:57:16` | `cowrie.session.params` |
| `2026-06-24 18:57:16` | `cowrie.command.input` |
| `2026-06-24 18:57:18` | `cowrie.log.closed` |
| `2026-06-24 18:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beb1dd714416

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:57 |
| **Last Seen** | 2026-06-24 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:57:36` | `cowrie.session.connect` |
| `2026-06-24 18:57:36` | `cowrie.client.version` |
| `2026-06-24 18:57:36` | `cowrie.client.kex` |
| `2026-06-24 18:57:36` | `cowrie.login.success` |
| `2026-06-24 18:57:37` | `cowrie.session.params` |
| `2026-06-24 18:57:37` | `cowrie.command.input` |
| `2026-06-24 18:57:37` | `cowrie.log.closed` |
| `2026-06-24 18:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4133ca2d9dd3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:58 |
| **Last Seen** | 2026-06-24 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:58:30` | `cowrie.session.connect` |
| `2026-06-24 18:58:30` | `cowrie.client.version` |
| `2026-06-24 18:58:30` | `cowrie.client.kex` |
| `2026-06-24 18:58:30` | `cowrie.login.success` |
| `2026-06-24 18:58:31` | `cowrie.session.params` |
| `2026-06-24 18:58:31` | `cowrie.command.input` |
| `2026-06-24 18:58:31` | `cowrie.log.closed` |
| `2026-06-24 18:58:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d7bda5bfbd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 18:59 |
| **Last Seen** | 2026-06-24 18:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 18:59:23` | `cowrie.session.connect` |
| `2026-06-24 18:59:23` | `cowrie.client.version` |
| `2026-06-24 18:59:24` | `cowrie.client.kex` |
| `2026-06-24 18:59:24` | `cowrie.login.success` |
| `2026-06-24 18:59:25` | `cowrie.session.params` |
| `2026-06-24 18:59:25` | `cowrie.command.input` |
| `2026-06-24 18:59:26` | `cowrie.log.closed` |
| `2026-06-24 18:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d70847235615

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:00 |
| **Last Seen** | 2026-06-24 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:00:19` | `cowrie.session.connect` |
| `2026-06-24 19:00:19` | `cowrie.client.version` |
| `2026-06-24 19:00:19` | `cowrie.client.kex` |
| `2026-06-24 19:00:19` | `cowrie.login.success` |
| `2026-06-24 19:00:20` | `cowrie.session.params` |
| `2026-06-24 19:00:20` | `cowrie.command.input` |
| `2026-06-24 19:00:20` | `cowrie.log.closed` |
| `2026-06-24 19:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1144f6990a89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:01 |
| **Last Seen** | 2026-06-24 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:01:15` | `cowrie.session.connect` |
| `2026-06-24 19:01:15` | `cowrie.client.version` |
| `2026-06-24 19:01:15` | `cowrie.client.kex` |
| `2026-06-24 19:01:15` | `cowrie.login.success` |
| `2026-06-24 19:01:16` | `cowrie.session.params` |
| `2026-06-24 19:01:16` | `cowrie.command.input` |
| `2026-06-24 19:01:16` | `cowrie.log.closed` |
| `2026-06-24 19:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6b2ebb0c5ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:02 |
| **Last Seen** | 2026-06-24 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:02:11` | `cowrie.session.connect` |
| `2026-06-24 19:02:11` | `cowrie.client.version` |
| `2026-06-24 19:02:11` | `cowrie.client.kex` |
| `2026-06-24 19:02:11` | `cowrie.login.success` |
| `2026-06-24 19:02:12` | `cowrie.session.params` |
| `2026-06-24 19:02:12` | `cowrie.command.input` |
| `2026-06-24 19:02:12` | `cowrie.log.closed` |
| `2026-06-24 19:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910ea42e34ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:03 |
| **Last Seen** | 2026-06-24 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:03:06` | `cowrie.session.connect` |
| `2026-06-24 19:03:06` | `cowrie.client.version` |
| `2026-06-24 19:03:06` | `cowrie.client.kex` |
| `2026-06-24 19:03:07` | `cowrie.login.success` |
| `2026-06-24 19:03:08` | `cowrie.session.params` |
| `2026-06-24 19:03:08` | `cowrie.command.input` |
| `2026-06-24 19:03:08` | `cowrie.log.closed` |
| `2026-06-24 19:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-676c4f1d82af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:04 |
| **Last Seen** | 2026-06-24 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:04:01` | `cowrie.session.connect` |
| `2026-06-24 19:04:01` | `cowrie.client.version` |
| `2026-06-24 19:04:01` | `cowrie.client.kex` |
| `2026-06-24 19:04:01` | `cowrie.login.success` |
| `2026-06-24 19:04:02` | `cowrie.session.params` |
| `2026-06-24 19:04:02` | `cowrie.command.input` |
| `2026-06-24 19:04:02` | `cowrie.log.closed` |
| `2026-06-24 19:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cad035fa1e7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:04 |
| **Last Seen** | 2026-06-24 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:04:54` | `cowrie.session.connect` |
| `2026-06-24 19:04:54` | `cowrie.client.version` |
| `2026-06-24 19:04:55` | `cowrie.client.kex` |
| `2026-06-24 19:04:55` | `cowrie.login.success` |
| `2026-06-24 19:04:56` | `cowrie.session.params` |
| `2026-06-24 19:04:56` | `cowrie.command.input` |
| `2026-06-24 19:04:56` | `cowrie.log.closed` |
| `2026-06-24 19:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0b82ef0832

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:05 |
| **Last Seen** | 2026-06-24 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:05:48` | `cowrie.session.connect` |
| `2026-06-24 19:05:48` | `cowrie.client.version` |
| `2026-06-24 19:05:48` | `cowrie.client.kex` |
| `2026-06-24 19:05:48` | `cowrie.login.success` |
| `2026-06-24 19:05:49` | `cowrie.session.params` |
| `2026-06-24 19:05:49` | `cowrie.command.input` |
| `2026-06-24 19:05:49` | `cowrie.log.closed` |
| `2026-06-24 19:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e022acc5afd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:06 |
| **Last Seen** | 2026-06-24 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:06:43` | `cowrie.session.connect` |
| `2026-06-24 19:06:43` | `cowrie.client.version` |
| `2026-06-24 19:06:43` | `cowrie.client.kex` |
| `2026-06-24 19:06:44` | `cowrie.login.success` |
| `2026-06-24 19:06:44` | `cowrie.session.params` |
| `2026-06-24 19:06:44` | `cowrie.command.input` |
| `2026-06-24 19:06:44` | `cowrie.log.closed` |
| `2026-06-24 19:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51806bce299e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:07 |
| **Last Seen** | 2026-06-24 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:07:39` | `cowrie.session.connect` |
| `2026-06-24 19:07:39` | `cowrie.client.version` |
| `2026-06-24 19:07:39` | `cowrie.client.kex` |
| `2026-06-24 19:07:39` | `cowrie.login.success` |
| `2026-06-24 19:07:40` | `cowrie.session.params` |
| `2026-06-24 19:07:40` | `cowrie.command.input` |
| `2026-06-24 19:07:40` | `cowrie.log.closed` |
| `2026-06-24 19:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de4abffa6ab8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:08 |
| **Last Seen** | 2026-06-24 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:08:36` | `cowrie.session.connect` |
| `2026-06-24 19:08:36` | `cowrie.client.version` |
| `2026-06-24 19:08:37` | `cowrie.client.kex` |
| `2026-06-24 19:08:37` | `cowrie.login.success` |
| `2026-06-24 19:08:38` | `cowrie.session.params` |
| `2026-06-24 19:08:38` | `cowrie.command.input` |
| `2026-06-24 19:08:38` | `cowrie.log.closed` |
| `2026-06-24 19:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2004d6c6569

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:09 |
| **Last Seen** | 2026-06-24 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:09:33` | `cowrie.session.connect` |
| `2026-06-24 19:09:33` | `cowrie.client.version` |
| `2026-06-24 19:09:33` | `cowrie.client.kex` |
| `2026-06-24 19:09:33` | `cowrie.login.success` |
| `2026-06-24 19:09:34` | `cowrie.session.params` |
| `2026-06-24 19:09:34` | `cowrie.command.input` |
| `2026-06-24 19:09:34` | `cowrie.log.closed` |
| `2026-06-24 19:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4795790ea2bc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:10 |
| **Last Seen** | 2026-06-24 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:10:29` | `cowrie.session.connect` |
| `2026-06-24 19:10:29` | `cowrie.client.version` |
| `2026-06-24 19:10:29` | `cowrie.client.kex` |
| `2026-06-24 19:10:30` | `cowrie.login.success` |
| `2026-06-24 19:10:30` | `cowrie.session.params` |
| `2026-06-24 19:10:30` | `cowrie.command.input` |
| `2026-06-24 19:10:30` | `cowrie.log.closed` |
| `2026-06-24 19:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3c713e357b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 19:11 |
| **Last Seen** | 2026-06-24 19:11 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:11:17` | `cowrie.session.connect` |
| `2026-06-24 19:11:18` | `cowrie.client.version` |
| `2026-06-24 19:11:18` | `cowrie.client.kex` |
| `2026-06-24 19:11:24` | `cowrie.login.success` |
| `2026-06-24 19:11:28` | `cowrie.session.params` |
| `2026-06-24 19:11:28` | `cowrie.command.input` |
| `2026-06-24 19:11:30` | `cowrie.log.closed` |
| `2026-06-24 19:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6fb1b2e7d9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:11 |
| **Last Seen** | 2026-06-24 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:11:25` | `cowrie.session.connect` |
| `2026-06-24 19:11:25` | `cowrie.client.version` |
| `2026-06-24 19:11:25` | `cowrie.client.kex` |
| `2026-06-24 19:11:25` | `cowrie.login.success` |
| `2026-06-24 19:11:26` | `cowrie.session.params` |
| `2026-06-24 19:11:26` | `cowrie.command.input` |
| `2026-06-24 19:11:26` | `cowrie.log.closed` |
| `2026-06-24 19:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f148e0a54640

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:12 |
| **Last Seen** | 2026-06-24 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:12:22` | `cowrie.session.connect` |
| `2026-06-24 19:12:22` | `cowrie.client.version` |
| `2026-06-24 19:12:22` | `cowrie.client.kex` |
| `2026-06-24 19:12:23` | `cowrie.login.success` |
| `2026-06-24 19:12:23` | `cowrie.session.params` |
| `2026-06-24 19:12:23` | `cowrie.command.input` |
| `2026-06-24 19:12:23` | `cowrie.log.closed` |
| `2026-06-24 19:12:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c07b50f6a8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:13 |
| **Last Seen** | 2026-06-24 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:13:20` | `cowrie.session.connect` |
| `2026-06-24 19:13:20` | `cowrie.client.version` |
| `2026-06-24 19:13:21` | `cowrie.client.kex` |
| `2026-06-24 19:13:21` | `cowrie.login.success` |
| `2026-06-24 19:13:22` | `cowrie.session.params` |
| `2026-06-24 19:13:22` | `cowrie.command.input` |
| `2026-06-24 19:13:22` | `cowrie.log.closed` |
| `2026-06-24 19:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4201a12f607a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:14 |
| **Last Seen** | 2026-06-24 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:14:19` | `cowrie.session.connect` |
| `2026-06-24 19:14:19` | `cowrie.client.version` |
| `2026-06-24 19:14:19` | `cowrie.client.kex` |
| `2026-06-24 19:14:20` | `cowrie.login.success` |
| `2026-06-24 19:14:20` | `cowrie.session.params` |
| `2026-06-24 19:14:20` | `cowrie.command.input` |
| `2026-06-24 19:14:20` | `cowrie.log.closed` |
| `2026-06-24 19:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07bbd7f7407

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:15 |
| **Last Seen** | 2026-06-24 19:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:15:19` | `cowrie.session.connect` |
| `2026-06-24 19:15:19` | `cowrie.client.version` |
| `2026-06-24 19:15:19` | `cowrie.client.kex` |
| `2026-06-24 19:15:19` | `cowrie.login.success` |
| `2026-06-24 19:15:20` | `cowrie.session.params` |
| `2026-06-24 19:15:20` | `cowrie.command.input` |
| `2026-06-24 19:15:20` | `cowrie.log.closed` |
| `2026-06-24 19:15:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88eadc68155

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:16 |
| **Last Seen** | 2026-06-24 19:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:16:17` | `cowrie.session.connect` |
| `2026-06-24 19:16:17` | `cowrie.client.version` |
| `2026-06-24 19:16:17` | `cowrie.client.kex` |
| `2026-06-24 19:16:18` | `cowrie.login.success` |
| `2026-06-24 19:16:19` | `cowrie.session.params` |
| `2026-06-24 19:16:19` | `cowrie.command.input` |
| `2026-06-24 19:16:19` | `cowrie.log.closed` |
| `2026-06-24 19:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c72e4e2ef1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:17 |
| **Last Seen** | 2026-06-24 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:17:15` | `cowrie.session.connect` |
| `2026-06-24 19:17:15` | `cowrie.client.version` |
| `2026-06-24 19:17:15` | `cowrie.client.kex` |
| `2026-06-24 19:17:15` | `cowrie.login.success` |
| `2026-06-24 19:17:16` | `cowrie.session.params` |
| `2026-06-24 19:17:16` | `cowrie.command.input` |
| `2026-06-24 19:17:16` | `cowrie.log.closed` |
| `2026-06-24 19:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e848fc587bb9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:18 |
| **Last Seen** | 2026-06-24 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:18:11` | `cowrie.session.connect` |
| `2026-06-24 19:18:11` | `cowrie.client.version` |
| `2026-06-24 19:18:12` | `cowrie.client.kex` |
| `2026-06-24 19:18:12` | `cowrie.login.success` |
| `2026-06-24 19:18:13` | `cowrie.session.params` |
| `2026-06-24 19:18:13` | `cowrie.command.input` |
| `2026-06-24 19:18:13` | `cowrie.log.closed` |
| `2026-06-24 19:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ffad7a034d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:19 |
| **Last Seen** | 2026-06-24 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:19:07` | `cowrie.session.connect` |
| `2026-06-24 19:19:07` | `cowrie.client.version` |
| `2026-06-24 19:19:07` | `cowrie.client.kex` |
| `2026-06-24 19:19:08` | `cowrie.login.success` |
| `2026-06-24 19:19:08` | `cowrie.session.params` |
| `2026-06-24 19:19:08` | `cowrie.command.input` |
| `2026-06-24 19:19:09` | `cowrie.log.closed` |
| `2026-06-24 19:19:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25e00567db5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:20 |
| **Last Seen** | 2026-06-24 19:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:20:06` | `cowrie.session.connect` |
| `2026-06-24 19:20:06` | `cowrie.client.version` |
| `2026-06-24 19:20:06` | `cowrie.client.kex` |
| `2026-06-24 19:20:07` | `cowrie.login.success` |
| `2026-06-24 19:20:08` | `cowrie.session.params` |
| `2026-06-24 19:20:08` | `cowrie.command.input` |
| `2026-06-24 19:20:08` | `cowrie.log.closed` |
| `2026-06-24 19:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c762bbde6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:21 |
| **Last Seen** | 2026-06-24 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:21:06` | `cowrie.session.connect` |
| `2026-06-24 19:21:06` | `cowrie.client.version` |
| `2026-06-24 19:21:06` | `cowrie.client.kex` |
| `2026-06-24 19:21:06` | `cowrie.login.success` |
| `2026-06-24 19:21:07` | `cowrie.session.params` |
| `2026-06-24 19:21:07` | `cowrie.command.input` |
| `2026-06-24 19:21:07` | `cowrie.log.closed` |
| `2026-06-24 19:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4227f23a8ff9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:22 |
| **Last Seen** | 2026-06-24 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:22:05` | `cowrie.session.connect` |
| `2026-06-24 19:22:05` | `cowrie.client.version` |
| `2026-06-24 19:22:05` | `cowrie.client.kex` |
| `2026-06-24 19:22:05` | `cowrie.login.success` |
| `2026-06-24 19:22:06` | `cowrie.session.params` |
| `2026-06-24 19:22:06` | `cowrie.command.input` |
| `2026-06-24 19:22:06` | `cowrie.log.closed` |
| `2026-06-24 19:22:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c79501ce2ea

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:23 |
| **Last Seen** | 2026-06-24 19:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:23:04` | `cowrie.session.connect` |
| `2026-06-24 19:23:04` | `cowrie.client.version` |
| `2026-06-24 19:23:04` | `cowrie.client.kex` |
| `2026-06-24 19:23:04` | `cowrie.login.success` |
| `2026-06-24 19:23:05` | `cowrie.session.params` |
| `2026-06-24 19:23:05` | `cowrie.command.input` |
| `2026-06-24 19:23:05` | `cowrie.log.closed` |
| `2026-06-24 19:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f8360da398

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:24 |
| **Last Seen** | 2026-06-24 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:24:02` | `cowrie.session.connect` |
| `2026-06-24 19:24:02` | `cowrie.client.version` |
| `2026-06-24 19:24:02` | `cowrie.client.kex` |
| `2026-06-24 19:24:03` | `cowrie.login.success` |
| `2026-06-24 19:24:03` | `cowrie.session.params` |
| `2026-06-24 19:24:03` | `cowrie.command.input` |
| `2026-06-24 19:24:03` | `cowrie.log.closed` |
| `2026-06-24 19:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989b8ab07507

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:25 |
| **Last Seen** | 2026-06-24 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:25:01` | `cowrie.session.connect` |
| `2026-06-24 19:25:01` | `cowrie.client.version` |
| `2026-06-24 19:25:01` | `cowrie.client.kex` |
| `2026-06-24 19:25:02` | `cowrie.login.success` |
| `2026-06-24 19:25:02` | `cowrie.session.params` |
| `2026-06-24 19:25:02` | `cowrie.command.input` |
| `2026-06-24 19:25:03` | `cowrie.log.closed` |
| `2026-06-24 19:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ecfe1a57d2a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-24 19:25 |
| **Last Seen** | 2026-06-24 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:25:15` | `cowrie.session.connect` |
| `2026-06-24 19:25:15` | `cowrie.client.version` |
| `2026-06-24 19:25:15` | `cowrie.client.kex` |
| `2026-06-24 19:25:16` | `cowrie.login.success` |
| `2026-06-24 19:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61814454590d

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-24 19:25 |
| **Last Seen** | 2026-06-24 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:25:15` | `cowrie.session.connect` |
| `2026-06-24 19:25:15` | `cowrie.client.version` |
| `2026-06-24 19:25:15` | `cowrie.client.kex` |
| `2026-06-24 19:25:16` | `cowrie.login.success` |
| `2026-06-24 19:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871d3d086524

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 19:25 |
| **Last Seen** | 2026-06-24 19:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:25:28` | `cowrie.session.connect` |
| `2026-06-24 19:25:30` | `cowrie.client.version` |
| `2026-06-24 19:25:30` | `cowrie.client.kex` |
| `2026-06-24 19:25:36` | `cowrie.login.success` |
| `2026-06-24 19:25:41` | `cowrie.session.params` |
| `2026-06-24 19:25:41` | `cowrie.command.input` |
| `2026-06-24 19:25:42` | `cowrie.log.closed` |
| `2026-06-24 19:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51bf77171882

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:26 |
| **Last Seen** | 2026-06-24 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:26:02` | `cowrie.session.connect` |
| `2026-06-24 19:26:02` | `cowrie.client.version` |
| `2026-06-24 19:26:02` | `cowrie.client.kex` |
| `2026-06-24 19:26:03` | `cowrie.login.success` |
| `2026-06-24 19:26:03` | `cowrie.session.params` |
| `2026-06-24 19:26:03` | `cowrie.command.input` |
| `2026-06-24 19:26:03` | `cowrie.log.closed` |
| `2026-06-24 19:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615e37901af2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:27 |
| **Last Seen** | 2026-06-24 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:27:06` | `cowrie.session.connect` |
| `2026-06-24 19:27:06` | `cowrie.client.version` |
| `2026-06-24 19:27:06` | `cowrie.client.kex` |
| `2026-06-24 19:27:06` | `cowrie.login.success` |
| `2026-06-24 19:27:07` | `cowrie.session.params` |
| `2026-06-24 19:27:07` | `cowrie.command.input` |
| `2026-06-24 19:27:07` | `cowrie.log.closed` |
| `2026-06-24 19:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f06a4a0aa5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 19:27 |
| **Last Seen** | 2026-06-24 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:27:52` | `cowrie.session.connect` |
| `2026-06-24 19:27:52` | `cowrie.client.version` |
| `2026-06-24 19:27:52` | `cowrie.client.kex` |
| `2026-06-24 19:27:52` | `cowrie.login.success` |
| `2026-06-24 19:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94920d53bc5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 19:27 |
| **Last Seen** | 2026-06-24 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:27:52` | `cowrie.session.connect` |
| `2026-06-24 19:27:52` | `cowrie.client.version` |
| `2026-06-24 19:27:52` | `cowrie.client.kex` |
| `2026-06-24 19:27:53` | `cowrie.login.success` |
| `2026-06-24 19:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-974f5eeb2d8a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 19:28 |
| **Last Seen** | 2026-06-24 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:28:02` | `cowrie.session.connect` |
| `2026-06-24 19:28:02` | `cowrie.client.version` |
| `2026-06-24 19:28:02` | `cowrie.client.kex` |
| `2026-06-24 19:28:03` | `cowrie.login.success` |
| `2026-06-24 19:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfde8a7e760

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-06-24 19:28 |
| **Last Seen** | 2026-06-24 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:28:03` | `cowrie.session.connect` |
| `2026-06-24 19:28:03` | `cowrie.client.version` |
| `2026-06-24 19:28:03` | `cowrie.client.kex` |
| `2026-06-24 19:28:04` | `cowrie.login.success` |
| `2026-06-24 19:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb9e359c715

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:28 |
| **Last Seen** | 2026-06-24 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:28:10` | `cowrie.session.connect` |
| `2026-06-24 19:28:10` | `cowrie.client.version` |
| `2026-06-24 19:28:10` | `cowrie.client.kex` |
| `2026-06-24 19:28:10` | `cowrie.login.success` |
| `2026-06-24 19:28:11` | `cowrie.session.params` |
| `2026-06-24 19:28:11` | `cowrie.command.input` |
| `2026-06-24 19:28:11` | `cowrie.log.closed` |
| `2026-06-24 19:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49cc4baf4507

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:29 |
| **Last Seen** | 2026-06-24 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:29:12` | `cowrie.session.connect` |
| `2026-06-24 19:29:12` | `cowrie.client.version` |
| `2026-06-24 19:29:12` | `cowrie.client.kex` |
| `2026-06-24 19:29:12` | `cowrie.login.success` |
| `2026-06-24 19:29:13` | `cowrie.session.params` |
| `2026-06-24 19:29:13` | `cowrie.command.input` |
| `2026-06-24 19:29:13` | `cowrie.log.closed` |
| `2026-06-24 19:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5046e7e451

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:30 |
| **Last Seen** | 2026-06-24 19:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:30:13` | `cowrie.session.connect` |
| `2026-06-24 19:30:13` | `cowrie.client.version` |
| `2026-06-24 19:30:13` | `cowrie.client.kex` |
| `2026-06-24 19:30:14` | `cowrie.login.success` |
| `2026-06-24 19:30:15` | `cowrie.session.params` |
| `2026-06-24 19:30:15` | `cowrie.command.input` |
| `2026-06-24 19:30:15` | `cowrie.log.closed` |
| `2026-06-24 19:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f31b8857dcf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:31 |
| **Last Seen** | 2026-06-24 19:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:31:15` | `cowrie.session.connect` |
| `2026-06-24 19:31:15` | `cowrie.client.version` |
| `2026-06-24 19:31:16` | `cowrie.client.kex` |
| `2026-06-24 19:31:16` | `cowrie.login.success` |
| `2026-06-24 19:31:16` | `cowrie.session.params` |
| `2026-06-24 19:31:16` | `cowrie.command.input` |
| `2026-06-24 19:31:17` | `cowrie.log.closed` |
| `2026-06-24 19:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5cea63bacd1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:32 |
| **Last Seen** | 2026-06-24 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:32:18` | `cowrie.session.connect` |
| `2026-06-24 19:32:18` | `cowrie.client.version` |
| `2026-06-24 19:32:18` | `cowrie.client.kex` |
| `2026-06-24 19:32:18` | `cowrie.login.success` |
| `2026-06-24 19:32:19` | `cowrie.session.params` |
| `2026-06-24 19:32:19` | `cowrie.command.input` |
| `2026-06-24 19:32:19` | `cowrie.log.closed` |
| `2026-06-24 19:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc56309fcf7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:33 |
| **Last Seen** | 2026-06-24 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:33:22` | `cowrie.session.connect` |
| `2026-06-24 19:33:22` | `cowrie.client.version` |
| `2026-06-24 19:33:22` | `cowrie.client.kex` |
| `2026-06-24 19:33:22` | `cowrie.login.success` |
| `2026-06-24 19:33:23` | `cowrie.session.params` |
| `2026-06-24 19:33:23` | `cowrie.command.input` |
| `2026-06-24 19:33:23` | `cowrie.log.closed` |
| `2026-06-24 19:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3cb0660515

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:34 |
| **Last Seen** | 2026-06-24 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:34:26` | `cowrie.session.connect` |
| `2026-06-24 19:34:26` | `cowrie.client.version` |
| `2026-06-24 19:34:26` | `cowrie.client.kex` |
| `2026-06-24 19:34:27` | `cowrie.login.success` |
| `2026-06-24 19:34:27` | `cowrie.session.params` |
| `2026-06-24 19:34:27` | `cowrie.command.input` |
| `2026-06-24 19:34:28` | `cowrie.log.closed` |
| `2026-06-24 19:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26caf9ec0f57

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:35 |
| **Last Seen** | 2026-06-24 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:35:29` | `cowrie.session.connect` |
| `2026-06-24 19:35:29` | `cowrie.client.version` |
| `2026-06-24 19:35:29` | `cowrie.client.kex` |
| `2026-06-24 19:35:30` | `cowrie.login.success` |
| `2026-06-24 19:35:31` | `cowrie.session.params` |
| `2026-06-24 19:35:31` | `cowrie.command.input` |
| `2026-06-24 19:35:31` | `cowrie.log.closed` |
| `2026-06-24 19:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a006203e52

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:36 |
| **Last Seen** | 2026-06-24 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:36:30` | `cowrie.session.connect` |
| `2026-06-24 19:36:30` | `cowrie.client.version` |
| `2026-06-24 19:36:30` | `cowrie.client.kex` |
| `2026-06-24 19:36:31` | `cowrie.login.success` |
| `2026-06-24 19:36:32` | `cowrie.session.params` |
| `2026-06-24 19:36:32` | `cowrie.command.input` |
| `2026-06-24 19:36:32` | `cowrie.log.closed` |
| `2026-06-24 19:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad07e5dfdffc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:37 |
| **Last Seen** | 2026-06-24 19:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:37:32` | `cowrie.session.connect` |
| `2026-06-24 19:37:32` | `cowrie.client.version` |
| `2026-06-24 19:37:32` | `cowrie.client.kex` |
| `2026-06-24 19:37:32` | `cowrie.login.success` |
| `2026-06-24 19:37:33` | `cowrie.session.params` |
| `2026-06-24 19:37:33` | `cowrie.command.input` |
| `2026-06-24 19:37:33` | `cowrie.log.closed` |
| `2026-06-24 19:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea3ec004d9cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:38 |
| **Last Seen** | 2026-06-24 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:38:34` | `cowrie.session.connect` |
| `2026-06-24 19:38:34` | `cowrie.client.version` |
| `2026-06-24 19:38:35` | `cowrie.client.kex` |
| `2026-06-24 19:38:35` | `cowrie.login.success` |
| `2026-06-24 19:38:36` | `cowrie.session.params` |
| `2026-06-24 19:38:36` | `cowrie.command.input` |
| `2026-06-24 19:38:36` | `cowrie.log.closed` |
| `2026-06-24 19:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0c0e53ec82

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 19:39 |
| **Last Seen** | 2026-06-24 19:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:39:33` | `cowrie.session.connect` |
| `2026-06-24 19:39:34` | `cowrie.client.version` |
| `2026-06-24 19:39:34` | `cowrie.client.kex` |
| `2026-06-24 19:39:41` | `cowrie.login.success` |
| `2026-06-24 19:39:45` | `cowrie.session.params` |
| `2026-06-24 19:39:45` | `cowrie.command.input` |
| `2026-06-24 19:39:47` | `cowrie.log.closed` |
| `2026-06-24 19:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e75012369fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:39 |
| **Last Seen** | 2026-06-24 19:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:39:39` | `cowrie.session.connect` |
| `2026-06-24 19:39:39` | `cowrie.client.version` |
| `2026-06-24 19:39:39` | `cowrie.client.kex` |
| `2026-06-24 19:39:39` | `cowrie.login.success` |
| `2026-06-24 19:39:40` | `cowrie.session.params` |
| `2026-06-24 19:39:40` | `cowrie.command.input` |
| `2026-06-24 19:39:40` | `cowrie.log.closed` |
| `2026-06-24 19:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b6962365983

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:40 |
| **Last Seen** | 2026-06-24 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:40:44` | `cowrie.session.connect` |
| `2026-06-24 19:40:44` | `cowrie.client.version` |
| `2026-06-24 19:40:44` | `cowrie.client.kex` |
| `2026-06-24 19:40:45` | `cowrie.login.success` |
| `2026-06-24 19:40:45` | `cowrie.session.params` |
| `2026-06-24 19:40:45` | `cowrie.command.input` |
| `2026-06-24 19:40:45` | `cowrie.log.closed` |
| `2026-06-24 19:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbcaaf1bf8b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:41 |
| **Last Seen** | 2026-06-24 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:41:49` | `cowrie.session.connect` |
| `2026-06-24 19:41:49` | `cowrie.client.version` |
| `2026-06-24 19:41:49` | `cowrie.client.kex` |
| `2026-06-24 19:41:49` | `cowrie.login.success` |
| `2026-06-24 19:41:50` | `cowrie.session.params` |
| `2026-06-24 19:41:50` | `cowrie.command.input` |
| `2026-06-24 19:41:50` | `cowrie.log.closed` |
| `2026-06-24 19:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e99ede8954fe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:42 |
| **Last Seen** | 2026-06-24 19:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:42:53` | `cowrie.session.connect` |
| `2026-06-24 19:42:53` | `cowrie.client.version` |
| `2026-06-24 19:42:53` | `cowrie.client.kex` |
| `2026-06-24 19:42:53` | `cowrie.login.success` |
| `2026-06-24 19:42:54` | `cowrie.session.params` |
| `2026-06-24 19:42:54` | `cowrie.command.input` |
| `2026-06-24 19:42:54` | `cowrie.log.closed` |
| `2026-06-24 19:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569cc473a08b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:43 |
| **Last Seen** | 2026-06-24 19:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:43:56` | `cowrie.session.connect` |
| `2026-06-24 19:43:56` | `cowrie.client.version` |
| `2026-06-24 19:43:56` | `cowrie.client.kex` |
| `2026-06-24 19:43:56` | `cowrie.login.success` |
| `2026-06-24 19:43:57` | `cowrie.session.params` |
| `2026-06-24 19:43:57` | `cowrie.command.input` |
| `2026-06-24 19:43:57` | `cowrie.log.closed` |
| `2026-06-24 19:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06add7f462c4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:45 |
| **Last Seen** | 2026-06-24 19:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:45:01` | `cowrie.session.connect` |
| `2026-06-24 19:45:01` | `cowrie.client.version` |
| `2026-06-24 19:45:01` | `cowrie.client.kex` |
| `2026-06-24 19:45:01` | `cowrie.login.success` |
| `2026-06-24 19:45:02` | `cowrie.session.params` |
| `2026-06-24 19:45:02` | `cowrie.command.input` |
| `2026-06-24 19:45:02` | `cowrie.log.closed` |
| `2026-06-24 19:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caad609d3c49

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:46 |
| **Last Seen** | 2026-06-24 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:46:09` | `cowrie.session.connect` |
| `2026-06-24 19:46:09` | `cowrie.client.version` |
| `2026-06-24 19:46:09` | `cowrie.client.kex` |
| `2026-06-24 19:46:10` | `cowrie.login.success` |
| `2026-06-24 19:46:11` | `cowrie.session.params` |
| `2026-06-24 19:46:11` | `cowrie.command.input` |
| `2026-06-24 19:46:11` | `cowrie.log.closed` |
| `2026-06-24 19:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ef4692a95d9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:47 |
| **Last Seen** | 2026-06-24 19:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:47:18` | `cowrie.session.connect` |
| `2026-06-24 19:47:18` | `cowrie.client.version` |
| `2026-06-24 19:47:18` | `cowrie.client.kex` |
| `2026-06-24 19:47:19` | `cowrie.login.success` |
| `2026-06-24 19:47:20` | `cowrie.session.params` |
| `2026-06-24 19:47:20` | `cowrie.command.input` |
| `2026-06-24 19:47:20` | `cowrie.log.closed` |
| `2026-06-24 19:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da8be1295cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:47 |
| **Last Seen** | 2026-06-24 19:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:47:25` | `cowrie.session.connect` |
| `2026-06-24 19:47:25` | `cowrie.client.version` |
| `2026-06-24 19:47:25` | `cowrie.client.kex` |
| `2026-06-24 19:47:27` | `cowrie.login.success` |
| `2026-06-24 19:47:28` | `cowrie.session.params` |
| `2026-06-24 19:47:28` | `cowrie.command.input` |
| `2026-06-24 19:47:28` | `cowrie.command.input` |
| `2026-06-24 19:47:28` | `cowrie.command.input` |
| `2026-06-24 19:47:28` | `cowrie.command.input` |
| `2026-06-24 19:47:29` | `cowrie.log.closed` |
| `2026-06-24 19:47:30` | `cowrie.session.params` |
| `2026-06-24 19:47:30` | `cowrie.command.input` |
| `2026-06-24 19:47:30` | `cowrie.command.input` |
| `2026-06-24 19:47:30` | `cowrie.command.failed` |
| `2026-06-24 19:47:30` | `cowrie.command.failed` |
| `2026-06-24 19:47:30` | `cowrie.command.failed` |
| `2026-06-24 19:47:30` | `cowrie.command.failed` |
| `2026-06-24 19:47:30` | `cowrie.log.closed` |
| `2026-06-24 19:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2855b33a3292

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:48 |
| **Last Seen** | 2026-06-24 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:48:26` | `cowrie.session.connect` |
| `2026-06-24 19:48:26` | `cowrie.client.version` |
| `2026-06-24 19:48:27` | `cowrie.client.kex` |
| `2026-06-24 19:48:27` | `cowrie.login.success` |
| `2026-06-24 19:48:28` | `cowrie.session.params` |
| `2026-06-24 19:48:28` | `cowrie.command.input` |
| `2026-06-24 19:48:28` | `cowrie.log.closed` |
| `2026-06-24 19:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca43478ead9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:49 |
| **Last Seen** | 2026-06-24 19:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:49:14` | `cowrie.session.connect` |
| `2026-06-24 19:49:14` | `cowrie.client.version` |
| `2026-06-24 19:49:14` | `cowrie.client.kex` |
| `2026-06-24 19:49:15` | `cowrie.login.success` |
| `2026-06-24 19:49:17` | `cowrie.session.params` |
| `2026-06-24 19:49:17` | `cowrie.command.input` |
| `2026-06-24 19:49:17` | `cowrie.command.input` |
| `2026-06-24 19:49:17` | `cowrie.command.input` |
| `2026-06-24 19:49:17` | `cowrie.command.input` |
| `2026-06-24 19:49:18` | `cowrie.log.closed` |
| `2026-06-24 19:49:19` | `cowrie.session.params` |
| `2026-06-24 19:49:19` | `cowrie.command.input` |
| `2026-06-24 19:49:19` | `cowrie.command.input` |
| `2026-06-24 19:49:19` | `cowrie.command.failed` |
| `2026-06-24 19:49:19` | `cowrie.command.failed` |
| `2026-06-24 19:49:19` | `cowrie.command.failed` |
| `2026-06-24 19:49:19` | `cowrie.command.failed` |
| `2026-06-24 19:49:20` | `cowrie.log.closed` |
| `2026-06-24 19:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a6c0b3d075

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:49 |
| **Last Seen** | 2026-06-24 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:49:32` | `cowrie.session.connect` |
| `2026-06-24 19:49:32` | `cowrie.client.version` |
| `2026-06-24 19:49:32` | `cowrie.client.kex` |
| `2026-06-24 19:49:32` | `cowrie.login.success` |
| `2026-06-24 19:49:33` | `cowrie.session.params` |
| `2026-06-24 19:49:33` | `cowrie.command.input` |
| `2026-06-24 19:49:33` | `cowrie.log.closed` |
| `2026-06-24 19:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c4c26b6e7a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:50 |
| **Last Seen** | 2026-06-24 19:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:50:37` | `cowrie.session.connect` |
| `2026-06-24 19:50:37` | `cowrie.client.version` |
| `2026-06-24 19:50:38` | `cowrie.client.kex` |
| `2026-06-24 19:50:38` | `cowrie.login.success` |
| `2026-06-24 19:50:39` | `cowrie.session.params` |
| `2026-06-24 19:50:39` | `cowrie.command.input` |
| `2026-06-24 19:50:39` | `cowrie.log.closed` |
| `2026-06-24 19:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1185ac44a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:51 |
| **Last Seen** | 2026-06-24 19:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:51:19` | `cowrie.session.connect` |
| `2026-06-24 19:51:19` | `cowrie.client.version` |
| `2026-06-24 19:51:19` | `cowrie.client.kex` |
| `2026-06-24 19:51:22` | `cowrie.login.success` |
| `2026-06-24 19:51:24` | `cowrie.session.params` |
| `2026-06-24 19:51:24` | `cowrie.command.input` |
| `2026-06-24 19:51:24` | `cowrie.command.input` |
| `2026-06-24 19:51:24` | `cowrie.command.input` |
| `2026-06-24 19:51:24` | `cowrie.command.input` |
| `2026-06-24 19:51:25` | `cowrie.log.closed` |
| `2026-06-24 19:51:27` | `cowrie.session.params` |
| `2026-06-24 19:51:27` | `cowrie.command.input` |
| `2026-06-24 19:51:27` | `cowrie.command.input` |
| `2026-06-24 19:51:27` | `cowrie.command.failed` |
| `2026-06-24 19:51:27` | `cowrie.command.failed` |
| `2026-06-24 19:51:27` | `cowrie.command.failed` |
| `2026-06-24 19:51:27` | `cowrie.command.failed` |
| `2026-06-24 19:51:29` | `cowrie.log.closed` |
| `2026-06-24 19:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cad8b73a983

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:51 |
| **Last Seen** | 2026-06-24 19:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:51:43` | `cowrie.session.connect` |
| `2026-06-24 19:51:43` | `cowrie.client.version` |
| `2026-06-24 19:51:43` | `cowrie.client.kex` |
| `2026-06-24 19:51:43` | `cowrie.login.success` |
| `2026-06-24 19:51:44` | `cowrie.session.params` |
| `2026-06-24 19:51:44` | `cowrie.command.input` |
| `2026-06-24 19:51:44` | `cowrie.log.closed` |
| `2026-06-24 19:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71efbcb357af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:52 |
| **Last Seen** | 2026-06-24 19:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:52:50` | `cowrie.session.connect` |
| `2026-06-24 19:52:50` | `cowrie.client.version` |
| `2026-06-24 19:52:50` | `cowrie.client.kex` |
| `2026-06-24 19:52:50` | `cowrie.login.success` |
| `2026-06-24 19:52:51` | `cowrie.session.params` |
| `2026-06-24 19:52:51` | `cowrie.command.input` |
| `2026-06-24 19:52:51` | `cowrie.log.closed` |
| `2026-06-24 19:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8642e517c8ed

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 19:53 |
| **Last Seen** | 2026-06-24 19:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:53:23` | `cowrie.session.connect` |
| `2026-06-24 19:53:24` | `cowrie.client.version` |
| `2026-06-24 19:53:24` | `cowrie.client.kex` |
| `2026-06-24 19:53:30` | `cowrie.login.success` |
| `2026-06-24 19:53:34` | `cowrie.session.params` |
| `2026-06-24 19:53:34` | `cowrie.command.input` |
| `2026-06-24 19:53:36` | `cowrie.log.closed` |
| `2026-06-24 19:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7944f0fa535

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:53 |
| **Last Seen** | 2026-06-24 19:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:53:58` | `cowrie.session.connect` |
| `2026-06-24 19:53:58` | `cowrie.client.version` |
| `2026-06-24 19:53:58` | `cowrie.client.kex` |
| `2026-06-24 19:53:58` | `cowrie.login.success` |
| `2026-06-24 19:53:59` | `cowrie.session.params` |
| `2026-06-24 19:53:59` | `cowrie.command.input` |
| `2026-06-24 19:53:59` | `cowrie.log.closed` |
| `2026-06-24 19:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3dfc46df3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:54 |
| **Last Seen** | 2026-06-24 19:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:54:47` | `cowrie.session.connect` |
| `2026-06-24 19:54:48` | `cowrie.client.version` |
| `2026-06-24 19:54:48` | `cowrie.client.kex` |
| `2026-06-24 19:54:50` | `cowrie.login.success` |
| `2026-06-24 19:54:51` | `cowrie.session.params` |
| `2026-06-24 19:54:51` | `cowrie.command.input` |
| `2026-06-24 19:54:51` | `cowrie.command.input` |
| `2026-06-24 19:54:51` | `cowrie.command.input` |
| `2026-06-24 19:54:51` | `cowrie.command.input` |
| `2026-06-24 19:54:52` | `cowrie.log.closed` |
| `2026-06-24 19:54:54` | `cowrie.session.params` |
| `2026-06-24 19:54:54` | `cowrie.command.input` |
| `2026-06-24 19:54:54` | `cowrie.command.input` |
| `2026-06-24 19:54:54` | `cowrie.command.failed` |
| `2026-06-24 19:54:54` | `cowrie.command.failed` |
| `2026-06-24 19:54:54` | `cowrie.command.failed` |
| `2026-06-24 19:54:54` | `cowrie.command.failed` |
| `2026-06-24 19:54:55` | `cowrie.log.closed` |
| `2026-06-24 19:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3f1a83e2cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:55 |
| **Last Seen** | 2026-06-24 19:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:55:03` | `cowrie.session.connect` |
| `2026-06-24 19:55:03` | `cowrie.client.version` |
| `2026-06-24 19:55:03` | `cowrie.client.kex` |
| `2026-06-24 19:55:03` | `cowrie.login.success` |
| `2026-06-24 19:55:04` | `cowrie.session.params` |
| `2026-06-24 19:55:04` | `cowrie.command.input` |
| `2026-06-24 19:55:04` | `cowrie.log.closed` |
| `2026-06-24 19:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537a3eef21a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:56 |
| **Last Seen** | 2026-06-24 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:56:07` | `cowrie.session.connect` |
| `2026-06-24 19:56:07` | `cowrie.client.version` |
| `2026-06-24 19:56:07` | `cowrie.client.kex` |
| `2026-06-24 19:56:08` | `cowrie.login.success` |
| `2026-06-24 19:56:08` | `cowrie.session.params` |
| `2026-06-24 19:56:08` | `cowrie.command.input` |
| `2026-06-24 19:56:08` | `cowrie.log.closed` |
| `2026-06-24 19:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ff1d090dd59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:56 |
| **Last Seen** | 2026-06-24 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '12345678' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:56:30` | `cowrie.session.connect` |
| `2026-06-24 19:56:31` | `cowrie.client.version` |
| `2026-06-24 19:56:31` | `cowrie.client.kex` |
| `2026-06-24 19:56:32` | `cowrie.login.success` |
| `2026-06-24 19:56:33` | `cowrie.session.params` |
| `2026-06-24 19:56:33` | `cowrie.command.input` |
| `2026-06-24 19:56:33` | `cowrie.command.input` |
| `2026-06-24 19:56:33` | `cowrie.command.input` |
| `2026-06-24 19:56:33` | `cowrie.command.input` |
| `2026-06-24 19:56:34` | `cowrie.log.closed` |
| `2026-06-24 19:56:35` | `cowrie.session.params` |
| `2026-06-24 19:56:35` | `cowrie.command.input` |
| `2026-06-24 19:56:35` | `cowrie.command.input` |
| `2026-06-24 19:56:35` | `cowrie.command.failed` |
| `2026-06-24 19:56:35` | `cowrie.command.failed` |
| `2026-06-24 19:56:35` | `cowrie.command.failed` |
| `2026-06-24 19:56:35` | `cowrie.command.failed` |
| `2026-06-24 19:56:36` | `cowrie.log.closed` |
| `2026-06-24 19:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553f60b8105d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:57 |
| **Last Seen** | 2026-06-24 19:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:57:12` | `cowrie.session.connect` |
| `2026-06-24 19:57:12` | `cowrie.client.version` |
| `2026-06-24 19:57:12` | `cowrie.client.kex` |
| `2026-06-24 19:57:12` | `cowrie.login.success` |
| `2026-06-24 19:57:13` | `cowrie.session.params` |
| `2026-06-24 19:57:13` | `cowrie.command.input` |
| `2026-06-24 19:57:13` | `cowrie.log.closed` |
| `2026-06-24 19:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4325ddeaeab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:58 |
| **Last Seen** | 2026-06-24 19:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123456789' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:58:11` | `cowrie.session.connect` |
| `2026-06-24 19:58:11` | `cowrie.client.version` |
| `2026-06-24 19:58:11` | `cowrie.client.kex` |
| `2026-06-24 19:58:12` | `cowrie.login.success` |
| `2026-06-24 19:58:14` | `cowrie.session.params` |
| `2026-06-24 19:58:14` | `cowrie.command.input` |
| `2026-06-24 19:58:14` | `cowrie.command.input` |
| `2026-06-24 19:58:14` | `cowrie.command.input` |
| `2026-06-24 19:58:14` | `cowrie.command.input` |
| `2026-06-24 19:58:15` | `cowrie.log.closed` |
| `2026-06-24 19:58:17` | `cowrie.session.params` |
| `2026-06-24 19:58:17` | `cowrie.command.input` |
| `2026-06-24 19:58:17` | `cowrie.command.input` |
| `2026-06-24 19:58:17` | `cowrie.command.failed` |
| `2026-06-24 19:58:17` | `cowrie.command.failed` |
| `2026-06-24 19:58:17` | `cowrie.command.failed` |
| `2026-06-24 19:58:17` | `cowrie.command.failed` |
| `2026-06-24 19:58:17` | `cowrie.log.closed` |
| `2026-06-24 19:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86476d725238

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:58 |
| **Last Seen** | 2026-06-24 19:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:58:18` | `cowrie.session.connect` |
| `2026-06-24 19:58:18` | `cowrie.client.version` |
| `2026-06-24 19:58:18` | `cowrie.client.kex` |
| `2026-06-24 19:58:19` | `cowrie.login.success` |
| `2026-06-24 19:58:20` | `cowrie.session.params` |
| `2026-06-24 19:58:20` | `cowrie.command.input` |
| `2026-06-24 19:58:20` | `cowrie.log.closed` |
| `2026-06-24 19:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e578d15985

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 19:59 |
| **Last Seen** | 2026-06-24 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:59:26` | `cowrie.session.connect` |
| `2026-06-24 19:59:26` | `cowrie.client.version` |
| `2026-06-24 19:59:26` | `cowrie.client.kex` |
| `2026-06-24 19:59:27` | `cowrie.login.success` |
| `2026-06-24 19:59:28` | `cowrie.session.params` |
| `2026-06-24 19:59:28` | `cowrie.command.input` |
| `2026-06-24 19:59:28` | `cowrie.log.closed` |
| `2026-06-24 19:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4c9cd03ea6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 19:59 |
| **Last Seen** | 2026-06-24 19:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1234567890' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 19:59:51` | `cowrie.session.connect` |
| `2026-06-24 19:59:51` | `cowrie.client.version` |
| `2026-06-24 19:59:51` | `cowrie.client.kex` |
| `2026-06-24 19:59:53` | `cowrie.login.success` |
| `2026-06-24 19:59:55` | `cowrie.session.params` |
| `2026-06-24 19:59:55` | `cowrie.command.input` |
| `2026-06-24 19:59:55` | `cowrie.command.input` |
| `2026-06-24 19:59:55` | `cowrie.command.input` |
| `2026-06-24 19:59:55` | `cowrie.command.input` |
| `2026-06-24 19:59:56` | `cowrie.log.closed` |
| `2026-06-24 19:59:58` | `cowrie.session.params` |
| `2026-06-24 19:59:58` | `cowrie.command.input` |
| `2026-06-24 19:59:58` | `cowrie.command.input` |
| `2026-06-24 19:59:58` | `cowrie.command.failed` |
| `2026-06-24 19:59:58` | `cowrie.command.failed` |
| `2026-06-24 19:59:58` | `cowrie.command.failed` |
| `2026-06-24 19:59:58` | `cowrie.command.failed` |
| `2026-06-24 19:59:58` | `cowrie.log.closed` |
| `2026-06-24 19:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d0e6fe02c9a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:00 |
| **Last Seen** | 2026-06-24 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:00:28` | `cowrie.session.connect` |
| `2026-06-24 20:00:28` | `cowrie.client.version` |
| `2026-06-24 20:00:28` | `cowrie.client.kex` |
| `2026-06-24 20:00:29` | `cowrie.login.success` |
| `2026-06-24 20:00:29` | `cowrie.session.params` |
| `2026-06-24 20:00:29` | `cowrie.command.input` |
| `2026-06-24 20:00:29` | `cowrie.log.closed` |
| `2026-06-24 20:00:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff9f563c40b1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:01 |
| **Last Seen** | 2026-06-24 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:01:13` | `cowrie.session.connect` |
| `2026-06-24 20:01:13` | `cowrie.client.version` |
| `2026-06-24 20:01:13` | `cowrie.client.kex` |
| `2026-06-24 20:01:13` | `cowrie.login.success` |
| `2026-06-24 20:01:14` | `cowrie.session.params` |
| `2026-06-24 20:01:14` | `cowrie.command.input` |
| `2026-06-24 20:01:14` | `cowrie.log.closed` |
| `2026-06-24 20:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c8d67f4794

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 20:01 |
| **Last Seen** | 2026-06-24 20:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123abc' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:01:30` | `cowrie.session.connect` |
| `2026-06-24 20:01:31` | `cowrie.client.version` |
| `2026-06-24 20:01:31` | `cowrie.client.kex` |
| `2026-06-24 20:01:32` | `cowrie.login.success` |
| `2026-06-24 20:01:34` | `cowrie.session.params` |
| `2026-06-24 20:01:34` | `cowrie.command.input` |
| `2026-06-24 20:01:34` | `cowrie.command.input` |
| `2026-06-24 20:01:34` | `cowrie.command.input` |
| `2026-06-24 20:01:34` | `cowrie.command.input` |
| `2026-06-24 20:01:35` | `cowrie.log.closed` |
| `2026-06-24 20:01:37` | `cowrie.session.params` |
| `2026-06-24 20:01:37` | `cowrie.command.input` |
| `2026-06-24 20:01:37` | `cowrie.command.input` |
| `2026-06-24 20:01:37` | `cowrie.command.failed` |
| `2026-06-24 20:01:37` | `cowrie.command.failed` |
| `2026-06-24 20:01:37` | `cowrie.command.failed` |
| `2026-06-24 20:01:37` | `cowrie.command.failed` |
| `2026-06-24 20:01:37` | `cowrie.log.closed` |
| `2026-06-24 20:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fcafefe2e31

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:01 |
| **Last Seen** | 2026-06-24 20:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:01:58` | `cowrie.session.connect` |
| `2026-06-24 20:01:58` | `cowrie.client.version` |
| `2026-06-24 20:01:58` | `cowrie.client.kex` |
| `2026-06-24 20:01:58` | `cowrie.login.success` |
| `2026-06-24 20:01:59` | `cowrie.session.params` |
| `2026-06-24 20:01:59` | `cowrie.command.input` |
| `2026-06-24 20:01:59` | `cowrie.log.closed` |
| `2026-06-24 20:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9543003c86f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:02 |
| **Last Seen** | 2026-06-24 20:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:02:42` | `cowrie.session.connect` |
| `2026-06-24 20:02:42` | `cowrie.client.version` |
| `2026-06-24 20:02:42` | `cowrie.client.kex` |
| `2026-06-24 20:02:42` | `cowrie.login.success` |
| `2026-06-24 20:02:43` | `cowrie.session.params` |
| `2026-06-24 20:02:43` | `cowrie.command.input` |
| `2026-06-24 20:02:43` | `cowrie.log.closed` |
| `2026-06-24 20:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13a9e071f22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-06-24 20:03 |
| **Last Seen** | 2026-06-24 20:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '1q2w3e4r' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:03:11` | `cowrie.session.connect` |
| `2026-06-24 20:03:11` | `cowrie.client.version` |
| `2026-06-24 20:03:11` | `cowrie.client.kex` |
| `2026-06-24 20:03:13` | `cowrie.login.success` |
| `2026-06-24 20:03:15` | `cowrie.session.params` |
| `2026-06-24 20:03:15` | `cowrie.command.input` |
| `2026-06-24 20:03:15` | `cowrie.command.input` |
| `2026-06-24 20:03:15` | `cowrie.command.input` |
| `2026-06-24 20:03:15` | `cowrie.command.input` |
| `2026-06-24 20:03:15` | `cowrie.log.closed` |
| `2026-06-24 20:03:17` | `cowrie.session.params` |
| `2026-06-24 20:03:17` | `cowrie.command.input` |
| `2026-06-24 20:03:17` | `cowrie.command.input` |
| `2026-06-24 20:03:17` | `cowrie.command.failed` |
| `2026-06-24 20:03:17` | `cowrie.command.failed` |
| `2026-06-24 20:03:17` | `cowrie.command.failed` |
| `2026-06-24 20:03:17` | `cowrie.command.failed` |
| `2026-06-24 20:03:18` | `cowrie.log.closed` |
| `2026-06-24 20:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d11bea25ef

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:03 |
| **Last Seen** | 2026-06-24 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:03:28` | `cowrie.session.connect` |
| `2026-06-24 20:03:28` | `cowrie.client.version` |
| `2026-06-24 20:03:28` | `cowrie.client.kex` |
| `2026-06-24 20:03:28` | `cowrie.login.success` |
| `2026-06-24 20:03:29` | `cowrie.session.params` |
| `2026-06-24 20:03:29` | `cowrie.command.input` |
| `2026-06-24 20:03:29` | `cowrie.log.closed` |
| `2026-06-24 20:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84869e156fce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:04 |
| **Last Seen** | 2026-06-24 20:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:04:14` | `cowrie.session.connect` |
| `2026-06-24 20:04:14` | `cowrie.client.version` |
| `2026-06-24 20:04:15` | `cowrie.client.kex` |
| `2026-06-24 20:04:15` | `cowrie.login.success` |
| `2026-06-24 20:04:16` | `cowrie.session.params` |
| `2026-06-24 20:04:16` | `cowrie.command.input` |
| `2026-06-24 20:04:16` | `cowrie.log.closed` |
| `2026-06-24 20:04:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-856b6d8a1a62

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:05 |
| **Last Seen** | 2026-06-24 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:05:01` | `cowrie.session.connect` |
| `2026-06-24 20:05:01` | `cowrie.client.version` |
| `2026-06-24 20:05:01` | `cowrie.client.kex` |
| `2026-06-24 20:05:01` | `cowrie.login.success` |
| `2026-06-24 20:05:02` | `cowrie.session.params` |
| `2026-06-24 20:05:02` | `cowrie.command.input` |
| `2026-06-24 20:05:02` | `cowrie.log.closed` |
| `2026-06-24 20:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecd9bf70362

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:05 |
| **Last Seen** | 2026-06-24 20:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:05:48` | `cowrie.session.connect` |
| `2026-06-24 20:05:48` | `cowrie.client.version` |
| `2026-06-24 20:05:48` | `cowrie.client.kex` |
| `2026-06-24 20:05:48` | `cowrie.login.success` |
| `2026-06-24 20:05:49` | `cowrie.session.params` |
| `2026-06-24 20:05:49` | `cowrie.command.input` |
| `2026-06-24 20:05:49` | `cowrie.log.closed` |
| `2026-06-24 20:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9321f4469847

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:06 |
| **Last Seen** | 2026-06-24 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:06:35` | `cowrie.session.connect` |
| `2026-06-24 20:06:35` | `cowrie.client.version` |
| `2026-06-24 20:06:35` | `cowrie.client.kex` |
| `2026-06-24 20:06:35` | `cowrie.login.success` |
| `2026-06-24 20:06:36` | `cowrie.session.params` |
| `2026-06-24 20:06:36` | `cowrie.command.input` |
| `2026-06-24 20:06:36` | `cowrie.log.closed` |
| `2026-06-24 20:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93bf63933222

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:07 |
| **Last Seen** | 2026-06-24 20:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:07:21` | `cowrie.session.connect` |
| `2026-06-24 20:07:21` | `cowrie.client.version` |
| `2026-06-24 20:07:21` | `cowrie.client.kex` |
| `2026-06-24 20:07:21` | `cowrie.login.success` |
| `2026-06-24 20:07:22` | `cowrie.session.params` |
| `2026-06-24 20:07:22` | `cowrie.command.input` |
| `2026-06-24 20:07:22` | `cowrie.log.closed` |
| `2026-06-24 20:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03afb407b87b

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 20:07 |
| **Last Seen** | 2026-06-24 20:08 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:07:46` | `cowrie.session.connect` |
| `2026-06-24 20:07:47` | `cowrie.client.version` |
| `2026-06-24 20:07:47` | `cowrie.client.kex` |
| `2026-06-24 20:07:54` | `cowrie.login.success` |
| `2026-06-24 20:07:58` | `cowrie.session.params` |
| `2026-06-24 20:07:58` | `cowrie.command.input` |
| `2026-06-24 20:08:00` | `cowrie.log.closed` |
| `2026-06-24 20:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc92e27bebb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:08 |
| **Last Seen** | 2026-06-24 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:08:06` | `cowrie.session.connect` |
| `2026-06-24 20:08:06` | `cowrie.client.version` |
| `2026-06-24 20:08:06` | `cowrie.client.kex` |
| `2026-06-24 20:08:07` | `cowrie.login.success` |
| `2026-06-24 20:08:08` | `cowrie.session.params` |
| `2026-06-24 20:08:08` | `cowrie.command.input` |
| `2026-06-24 20:08:08` | `cowrie.log.closed` |
| `2026-06-24 20:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17b7603374e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:08 |
| **Last Seen** | 2026-06-24 20:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:08:51` | `cowrie.session.connect` |
| `2026-06-24 20:08:51` | `cowrie.client.version` |
| `2026-06-24 20:08:51` | `cowrie.client.kex` |
| `2026-06-24 20:08:51` | `cowrie.login.success` |
| `2026-06-24 20:08:52` | `cowrie.session.params` |
| `2026-06-24 20:08:52` | `cowrie.command.input` |
| `2026-06-24 20:08:52` | `cowrie.log.closed` |
| `2026-06-24 20:08:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3902624d689d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:09 |
| **Last Seen** | 2026-06-24 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:09:35` | `cowrie.session.connect` |
| `2026-06-24 20:09:35` | `cowrie.client.version` |
| `2026-06-24 20:09:35` | `cowrie.client.kex` |
| `2026-06-24 20:09:35` | `cowrie.login.success` |
| `2026-06-24 20:09:36` | `cowrie.session.params` |
| `2026-06-24 20:09:36` | `cowrie.command.input` |
| `2026-06-24 20:09:36` | `cowrie.log.closed` |
| `2026-06-24 20:09:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144bb237ef95

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:10 |
| **Last Seen** | 2026-06-24 20:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:10:20` | `cowrie.session.connect` |
| `2026-06-24 20:10:20` | `cowrie.client.version` |
| `2026-06-24 20:10:20` | `cowrie.client.kex` |
| `2026-06-24 20:10:20` | `cowrie.login.success` |
| `2026-06-24 20:10:21` | `cowrie.session.params` |
| `2026-06-24 20:10:21` | `cowrie.command.input` |
| `2026-06-24 20:10:21` | `cowrie.log.closed` |
| `2026-06-24 20:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b0a4dbcccd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:11 |
| **Last Seen** | 2026-06-24 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:11:05` | `cowrie.session.connect` |
| `2026-06-24 20:11:05` | `cowrie.client.version` |
| `2026-06-24 20:11:05` | `cowrie.client.kex` |
| `2026-06-24 20:11:05` | `cowrie.login.success` |
| `2026-06-24 20:11:06` | `cowrie.session.params` |
| `2026-06-24 20:11:06` | `cowrie.command.input` |
| `2026-06-24 20:11:06` | `cowrie.log.closed` |
| `2026-06-24 20:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1215ad3f6bf8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:11 |
| **Last Seen** | 2026-06-24 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:11:51` | `cowrie.session.connect` |
| `2026-06-24 20:11:51` | `cowrie.client.version` |
| `2026-06-24 20:11:51` | `cowrie.client.kex` |
| `2026-06-24 20:11:51` | `cowrie.login.success` |
| `2026-06-24 20:11:52` | `cowrie.session.params` |
| `2026-06-24 20:11:52` | `cowrie.command.input` |
| `2026-06-24 20:11:52` | `cowrie.log.closed` |
| `2026-06-24 20:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ccdac7c1af0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:12 |
| **Last Seen** | 2026-06-24 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:12:37` | `cowrie.session.connect` |
| `2026-06-24 20:12:37` | `cowrie.client.version` |
| `2026-06-24 20:12:37` | `cowrie.client.kex` |
| `2026-06-24 20:12:37` | `cowrie.login.success` |
| `2026-06-24 20:12:38` | `cowrie.session.params` |
| `2026-06-24 20:12:38` | `cowrie.command.input` |
| `2026-06-24 20:12:38` | `cowrie.log.closed` |
| `2026-06-24 20:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fb1299be51

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:13 |
| **Last Seen** | 2026-06-24 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:13:22` | `cowrie.session.connect` |
| `2026-06-24 20:13:22` | `cowrie.client.version` |
| `2026-06-24 20:13:22` | `cowrie.client.kex` |
| `2026-06-24 20:13:23` | `cowrie.login.success` |
| `2026-06-24 20:13:23` | `cowrie.session.params` |
| `2026-06-24 20:13:23` | `cowrie.command.input` |
| `2026-06-24 20:13:24` | `cowrie.log.closed` |
| `2026-06-24 20:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafaa6d99da8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:14 |
| **Last Seen** | 2026-06-24 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:14:08` | `cowrie.session.connect` |
| `2026-06-24 20:14:08` | `cowrie.client.version` |
| `2026-06-24 20:14:08` | `cowrie.client.kex` |
| `2026-06-24 20:14:08` | `cowrie.login.success` |
| `2026-06-24 20:14:09` | `cowrie.session.params` |
| `2026-06-24 20:14:09` | `cowrie.command.input` |
| `2026-06-24 20:14:09` | `cowrie.log.closed` |
| `2026-06-24 20:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49efd376bd6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:14 |
| **Last Seen** | 2026-06-24 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:14:53` | `cowrie.session.connect` |
| `2026-06-24 20:14:53` | `cowrie.client.version` |
| `2026-06-24 20:14:53` | `cowrie.client.kex` |
| `2026-06-24 20:14:53` | `cowrie.login.success` |
| `2026-06-24 20:14:54` | `cowrie.session.params` |
| `2026-06-24 20:14:54` | `cowrie.command.input` |
| `2026-06-24 20:14:54` | `cowrie.log.closed` |
| `2026-06-24 20:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e8765f0cbf

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:15 |
| **Last Seen** | 2026-06-24 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:15:37` | `cowrie.session.connect` |
| `2026-06-24 20:15:37` | `cowrie.client.version` |
| `2026-06-24 20:15:37` | `cowrie.client.kex` |
| `2026-06-24 20:15:38` | `cowrie.login.success` |
| `2026-06-24 20:15:38` | `cowrie.session.params` |
| `2026-06-24 20:15:38` | `cowrie.command.input` |
| `2026-06-24 20:15:38` | `cowrie.log.closed` |
| `2026-06-24 20:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8f0a45b3cd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:16 |
| **Last Seen** | 2026-06-24 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:16:23` | `cowrie.session.connect` |
| `2026-06-24 20:16:23` | `cowrie.client.version` |
| `2026-06-24 20:16:24` | `cowrie.client.kex` |
| `2026-06-24 20:16:24` | `cowrie.login.success` |
| `2026-06-24 20:16:25` | `cowrie.session.params` |
| `2026-06-24 20:16:25` | `cowrie.command.input` |
| `2026-06-24 20:16:25` | `cowrie.log.closed` |
| `2026-06-24 20:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28292f4126e8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:17 |
| **Last Seen** | 2026-06-24 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:17:11` | `cowrie.session.connect` |
| `2026-06-24 20:17:11` | `cowrie.client.version` |
| `2026-06-24 20:17:11` | `cowrie.client.kex` |
| `2026-06-24 20:17:11` | `cowrie.login.success` |
| `2026-06-24 20:17:12` | `cowrie.session.params` |
| `2026-06-24 20:17:12` | `cowrie.command.input` |
| `2026-06-24 20:17:12` | `cowrie.log.closed` |
| `2026-06-24 20:17:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4917459e54f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:17 |
| **Last Seen** | 2026-06-24 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:17:59` | `cowrie.session.connect` |
| `2026-06-24 20:17:59` | `cowrie.client.version` |
| `2026-06-24 20:17:59` | `cowrie.client.kex` |
| `2026-06-24 20:17:59` | `cowrie.login.success` |
| `2026-06-24 20:18:00` | `cowrie.session.params` |
| `2026-06-24 20:18:00` | `cowrie.command.input` |
| `2026-06-24 20:18:00` | `cowrie.log.closed` |
| `2026-06-24 20:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7feab52c4ee3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:18 |
| **Last Seen** | 2026-06-24 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:18:48` | `cowrie.session.connect` |
| `2026-06-24 20:18:48` | `cowrie.client.version` |
| `2026-06-24 20:18:48` | `cowrie.client.kex` |
| `2026-06-24 20:18:48` | `cowrie.login.success` |
| `2026-06-24 20:18:49` | `cowrie.session.params` |
| `2026-06-24 20:18:49` | `cowrie.command.input` |
| `2026-06-24 20:18:49` | `cowrie.log.closed` |
| `2026-06-24 20:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8fd7b8fbe42

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:19 |
| **Last Seen** | 2026-06-24 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:19:36` | `cowrie.session.connect` |
| `2026-06-24 20:19:36` | `cowrie.client.version` |
| `2026-06-24 20:19:36` | `cowrie.client.kex` |
| `2026-06-24 20:19:36` | `cowrie.login.success` |
| `2026-06-24 20:19:37` | `cowrie.session.params` |
| `2026-06-24 20:19:37` | `cowrie.command.input` |
| `2026-06-24 20:19:37` | `cowrie.log.closed` |
| `2026-06-24 20:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7854321b2211

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:20 |
| **Last Seen** | 2026-06-24 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:20:24` | `cowrie.session.connect` |
| `2026-06-24 20:20:24` | `cowrie.client.version` |
| `2026-06-24 20:20:24` | `cowrie.client.kex` |
| `2026-06-24 20:20:24` | `cowrie.login.success` |
| `2026-06-24 20:20:25` | `cowrie.session.params` |
| `2026-06-24 20:20:25` | `cowrie.command.input` |
| `2026-06-24 20:20:25` | `cowrie.log.closed` |
| `2026-06-24 20:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7582c3ad7f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:21 |
| **Last Seen** | 2026-06-24 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:21:10` | `cowrie.session.connect` |
| `2026-06-24 20:21:10` | `cowrie.client.version` |
| `2026-06-24 20:21:10` | `cowrie.client.kex` |
| `2026-06-24 20:21:10` | `cowrie.login.success` |
| `2026-06-24 20:21:11` | `cowrie.session.params` |
| `2026-06-24 20:21:11` | `cowrie.command.input` |
| `2026-06-24 20:21:11` | `cowrie.log.closed` |
| `2026-06-24 20:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d265425253c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:21 |
| **Last Seen** | 2026-06-24 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:21:55` | `cowrie.session.connect` |
| `2026-06-24 20:21:55` | `cowrie.client.version` |
| `2026-06-24 20:21:56` | `cowrie.client.kex` |
| `2026-06-24 20:21:56` | `cowrie.login.success` |
| `2026-06-24 20:21:57` | `cowrie.session.params` |
| `2026-06-24 20:21:57` | `cowrie.command.input` |
| `2026-06-24 20:21:57` | `cowrie.log.closed` |
| `2026-06-24 20:21:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e380c1cd36d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 20:22 |
| **Last Seen** | 2026-06-24 20:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:22:03` | `cowrie.session.connect` |
| `2026-06-24 20:22:04` | `cowrie.client.version` |
| `2026-06-24 20:22:04` | `cowrie.client.kex` |
| `2026-06-24 20:22:10` | `cowrie.login.success` |
| `2026-06-24 20:22:15` | `cowrie.session.params` |
| `2026-06-24 20:22:15` | `cowrie.command.input` |
| `2026-06-24 20:22:16` | `cowrie.log.closed` |
| `2026-06-24 20:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026270185338

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:22 |
| **Last Seen** | 2026-06-24 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:22:42` | `cowrie.session.connect` |
| `2026-06-24 20:22:42` | `cowrie.client.version` |
| `2026-06-24 20:22:42` | `cowrie.client.kex` |
| `2026-06-24 20:22:42` | `cowrie.login.success` |
| `2026-06-24 20:22:43` | `cowrie.session.params` |
| `2026-06-24 20:22:43` | `cowrie.command.input` |
| `2026-06-24 20:22:43` | `cowrie.log.closed` |
| `2026-06-24 20:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6162a90b13dd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:23 |
| **Last Seen** | 2026-06-24 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:23:28` | `cowrie.session.connect` |
| `2026-06-24 20:23:28` | `cowrie.client.version` |
| `2026-06-24 20:23:28` | `cowrie.client.kex` |
| `2026-06-24 20:23:29` | `cowrie.login.success` |
| `2026-06-24 20:23:29` | `cowrie.session.params` |
| `2026-06-24 20:23:29` | `cowrie.command.input` |
| `2026-06-24 20:23:30` | `cowrie.log.closed` |
| `2026-06-24 20:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b3ae56df8c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:24 |
| **Last Seen** | 2026-06-24 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:24:16` | `cowrie.session.connect` |
| `2026-06-24 20:24:16` | `cowrie.client.version` |
| `2026-06-24 20:24:16` | `cowrie.client.kex` |
| `2026-06-24 20:24:16` | `cowrie.login.success` |
| `2026-06-24 20:24:17` | `cowrie.session.params` |
| `2026-06-24 20:24:17` | `cowrie.command.input` |
| `2026-06-24 20:24:17` | `cowrie.log.closed` |
| `2026-06-24 20:24:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bdb3487c9b5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:25 |
| **Last Seen** | 2026-06-24 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:25:04` | `cowrie.session.connect` |
| `2026-06-24 20:25:04` | `cowrie.client.version` |
| `2026-06-24 20:25:04` | `cowrie.client.kex` |
| `2026-06-24 20:25:05` | `cowrie.login.success` |
| `2026-06-24 20:25:05` | `cowrie.session.params` |
| `2026-06-24 20:25:05` | `cowrie.command.input` |
| `2026-06-24 20:25:05` | `cowrie.log.closed` |
| `2026-06-24 20:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d1bcbbabe0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:25 |
| **Last Seen** | 2026-06-24 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:25:52` | `cowrie.session.connect` |
| `2026-06-24 20:25:52` | `cowrie.client.version` |
| `2026-06-24 20:25:52` | `cowrie.client.kex` |
| `2026-06-24 20:25:52` | `cowrie.login.success` |
| `2026-06-24 20:25:53` | `cowrie.session.params` |
| `2026-06-24 20:25:53` | `cowrie.command.input` |
| `2026-06-24 20:25:53` | `cowrie.log.closed` |
| `2026-06-24 20:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e922c02fb0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:26 |
| **Last Seen** | 2026-06-24 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:26:39` | `cowrie.session.connect` |
| `2026-06-24 20:26:39` | `cowrie.client.version` |
| `2026-06-24 20:26:39` | `cowrie.client.kex` |
| `2026-06-24 20:26:39` | `cowrie.login.success` |
| `2026-06-24 20:26:40` | `cowrie.session.params` |
| `2026-06-24 20:26:40` | `cowrie.command.input` |
| `2026-06-24 20:26:40` | `cowrie.log.closed` |
| `2026-06-24 20:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b33680f8dba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:27 |
| **Last Seen** | 2026-06-24 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:27:26` | `cowrie.session.connect` |
| `2026-06-24 20:27:26` | `cowrie.client.version` |
| `2026-06-24 20:27:26` | `cowrie.client.kex` |
| `2026-06-24 20:27:26` | `cowrie.login.success` |
| `2026-06-24 20:27:27` | `cowrie.session.params` |
| `2026-06-24 20:27:27` | `cowrie.command.input` |
| `2026-06-24 20:27:27` | `cowrie.log.closed` |
| `2026-06-24 20:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91dbe3cacc10

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:28 |
| **Last Seen** | 2026-06-24 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:28:13` | `cowrie.session.connect` |
| `2026-06-24 20:28:13` | `cowrie.client.version` |
| `2026-06-24 20:28:13` | `cowrie.client.kex` |
| `2026-06-24 20:28:13` | `cowrie.login.success` |
| `2026-06-24 20:28:14` | `cowrie.session.params` |
| `2026-06-24 20:28:14` | `cowrie.command.input` |
| `2026-06-24 20:28:14` | `cowrie.log.closed` |
| `2026-06-24 20:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5992580aa9cc

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:29 |
| **Last Seen** | 2026-06-24 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:29:00` | `cowrie.session.connect` |
| `2026-06-24 20:29:00` | `cowrie.client.version` |
| `2026-06-24 20:29:00` | `cowrie.client.kex` |
| `2026-06-24 20:29:00` | `cowrie.login.success` |
| `2026-06-24 20:29:01` | `cowrie.session.params` |
| `2026-06-24 20:29:01` | `cowrie.command.input` |
| `2026-06-24 20:29:01` | `cowrie.log.closed` |
| `2026-06-24 20:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5098023c194

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:29 |
| **Last Seen** | 2026-06-24 20:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:29:48` | `cowrie.session.connect` |
| `2026-06-24 20:29:48` | `cowrie.client.version` |
| `2026-06-24 20:29:48` | `cowrie.client.kex` |
| `2026-06-24 20:29:48` | `cowrie.login.success` |
| `2026-06-24 20:29:49` | `cowrie.session.params` |
| `2026-06-24 20:29:49` | `cowrie.command.input` |
| `2026-06-24 20:29:49` | `cowrie.log.closed` |
| `2026-06-24 20:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4fb80f9c9f5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:30 |
| **Last Seen** | 2026-06-24 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:30:38` | `cowrie.session.connect` |
| `2026-06-24 20:30:38` | `cowrie.client.version` |
| `2026-06-24 20:30:38` | `cowrie.client.kex` |
| `2026-06-24 20:30:38` | `cowrie.login.success` |
| `2026-06-24 20:30:39` | `cowrie.session.params` |
| `2026-06-24 20:30:39` | `cowrie.command.input` |
| `2026-06-24 20:30:39` | `cowrie.log.closed` |
| `2026-06-24 20:30:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1b11f40d44

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:31 |
| **Last Seen** | 2026-06-24 20:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:31:27` | `cowrie.session.connect` |
| `2026-06-24 20:31:27` | `cowrie.client.version` |
| `2026-06-24 20:31:27` | `cowrie.client.kex` |
| `2026-06-24 20:31:28` | `cowrie.login.success` |
| `2026-06-24 20:31:28` | `cowrie.session.params` |
| `2026-06-24 20:31:28` | `cowrie.command.input` |
| `2026-06-24 20:31:29` | `cowrie.log.closed` |
| `2026-06-24 20:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a97d9df80ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:32 |
| **Last Seen** | 2026-06-24 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:32:17` | `cowrie.session.connect` |
| `2026-06-24 20:32:17` | `cowrie.client.version` |
| `2026-06-24 20:32:17` | `cowrie.client.kex` |
| `2026-06-24 20:32:17` | `cowrie.login.success` |
| `2026-06-24 20:32:18` | `cowrie.session.params` |
| `2026-06-24 20:32:18` | `cowrie.command.input` |
| `2026-06-24 20:32:18` | `cowrie.log.closed` |
| `2026-06-24 20:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81316f32276

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:33 |
| **Last Seen** | 2026-06-24 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:33:07` | `cowrie.session.connect` |
| `2026-06-24 20:33:07` | `cowrie.client.version` |
| `2026-06-24 20:33:07` | `cowrie.client.kex` |
| `2026-06-24 20:33:08` | `cowrie.login.success` |
| `2026-06-24 20:33:09` | `cowrie.session.params` |
| `2026-06-24 20:33:09` | `cowrie.command.input` |
| `2026-06-24 20:33:09` | `cowrie.log.closed` |
| `2026-06-24 20:33:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00d439a4ec2

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:33 |
| **Last Seen** | 2026-06-24 20:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:33:57` | `cowrie.session.connect` |
| `2026-06-24 20:33:57` | `cowrie.client.version` |
| `2026-06-24 20:33:57` | `cowrie.client.kex` |
| `2026-06-24 20:33:57` | `cowrie.login.success` |
| `2026-06-24 20:33:58` | `cowrie.session.params` |
| `2026-06-24 20:33:58` | `cowrie.command.input` |
| `2026-06-24 20:33:58` | `cowrie.log.closed` |
| `2026-06-24 20:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c746c04ec5a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:34 |
| **Last Seen** | 2026-06-24 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:34:45` | `cowrie.session.connect` |
| `2026-06-24 20:34:45` | `cowrie.client.version` |
| `2026-06-24 20:34:45` | `cowrie.client.kex` |
| `2026-06-24 20:34:45` | `cowrie.login.success` |
| `2026-06-24 20:34:46` | `cowrie.session.params` |
| `2026-06-24 20:34:46` | `cowrie.command.input` |
| `2026-06-24 20:34:46` | `cowrie.log.closed` |
| `2026-06-24 20:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac1cc07f98ff

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:35 |
| **Last Seen** | 2026-06-24 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:35:35` | `cowrie.session.connect` |
| `2026-06-24 20:35:35` | `cowrie.client.version` |
| `2026-06-24 20:35:35` | `cowrie.client.kex` |
| `2026-06-24 20:35:35` | `cowrie.login.success` |
| `2026-06-24 20:35:36` | `cowrie.session.params` |
| `2026-06-24 20:35:36` | `cowrie.command.input` |
| `2026-06-24 20:35:36` | `cowrie.log.closed` |
| `2026-06-24 20:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0048f2824840

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:36 |
| **Last Seen** | 2026-06-24 20:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:36:24` | `cowrie.session.connect` |
| `2026-06-24 20:36:24` | `cowrie.client.version` |
| `2026-06-24 20:36:24` | `cowrie.client.kex` |
| `2026-06-24 20:36:24` | `cowrie.login.success` |
| `2026-06-24 20:36:25` | `cowrie.session.params` |
| `2026-06-24 20:36:25` | `cowrie.command.input` |
| `2026-06-24 20:36:25` | `cowrie.log.closed` |
| `2026-06-24 20:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdc42954d88f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 20:36 |
| **Last Seen** | 2026-06-24 20:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:36:41` | `cowrie.session.connect` |
| `2026-06-24 20:36:42` | `cowrie.client.version` |
| `2026-06-24 20:36:42` | `cowrie.client.kex` |
| `2026-06-24 20:36:49` | `cowrie.login.success` |
| `2026-06-24 20:36:52` | `cowrie.session.params` |
| `2026-06-24 20:36:52` | `cowrie.command.input` |
| `2026-06-24 20:36:54` | `cowrie.log.closed` |
| `2026-06-24 20:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d7fb06ef6f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:37 |
| **Last Seen** | 2026-06-24 20:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:37:16` | `cowrie.session.connect` |
| `2026-06-24 20:37:16` | `cowrie.client.version` |
| `2026-06-24 20:37:16` | `cowrie.client.kex` |
| `2026-06-24 20:37:16` | `cowrie.login.success` |
| `2026-06-24 20:37:17` | `cowrie.session.params` |
| `2026-06-24 20:37:17` | `cowrie.command.input` |
| `2026-06-24 20:37:17` | `cowrie.log.closed` |
| `2026-06-24 20:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a950bf8ed6c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:38 |
| **Last Seen** | 2026-06-24 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:38:08` | `cowrie.session.connect` |
| `2026-06-24 20:38:08` | `cowrie.client.version` |
| `2026-06-24 20:38:08` | `cowrie.client.kex` |
| `2026-06-24 20:38:08` | `cowrie.login.success` |
| `2026-06-24 20:38:09` | `cowrie.session.params` |
| `2026-06-24 20:38:09` | `cowrie.command.input` |
| `2026-06-24 20:38:09` | `cowrie.log.closed` |
| `2026-06-24 20:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4615654299ed

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:39 |
| **Last Seen** | 2026-06-24 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:39:00` | `cowrie.session.connect` |
| `2026-06-24 20:39:00` | `cowrie.client.version` |
| `2026-06-24 20:39:00` | `cowrie.client.kex` |
| `2026-06-24 20:39:00` | `cowrie.login.success` |
| `2026-06-24 20:39:01` | `cowrie.session.params` |
| `2026-06-24 20:39:01` | `cowrie.command.input` |
| `2026-06-24 20:39:01` | `cowrie.log.closed` |
| `2026-06-24 20:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc1edb7b3ca

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:39 |
| **Last Seen** | 2026-06-24 20:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:39:50` | `cowrie.session.connect` |
| `2026-06-24 20:39:50` | `cowrie.client.version` |
| `2026-06-24 20:39:50` | `cowrie.client.kex` |
| `2026-06-24 20:39:50` | `cowrie.login.success` |
| `2026-06-24 20:39:51` | `cowrie.session.params` |
| `2026-06-24 20:39:51` | `cowrie.command.input` |
| `2026-06-24 20:39:51` | `cowrie.log.closed` |
| `2026-06-24 20:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ddb9c07c5f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:40 |
| **Last Seen** | 2026-06-24 20:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:40:41` | `cowrie.session.connect` |
| `2026-06-24 20:40:41` | `cowrie.client.version` |
| `2026-06-24 20:40:41` | `cowrie.client.kex` |
| `2026-06-24 20:40:41` | `cowrie.login.success` |
| `2026-06-24 20:40:42` | `cowrie.session.params` |
| `2026-06-24 20:40:42` | `cowrie.command.input` |
| `2026-06-24 20:40:42` | `cowrie.log.closed` |
| `2026-06-24 20:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f76ffd6585f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:41 |
| **Last Seen** | 2026-06-24 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:41:32` | `cowrie.session.connect` |
| `2026-06-24 20:41:32` | `cowrie.client.version` |
| `2026-06-24 20:41:32` | `cowrie.client.kex` |
| `2026-06-24 20:41:32` | `cowrie.login.success` |
| `2026-06-24 20:41:33` | `cowrie.session.params` |
| `2026-06-24 20:41:33` | `cowrie.command.input` |
| `2026-06-24 20:41:33` | `cowrie.log.closed` |
| `2026-06-24 20:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a1790831e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-06-24 20:42 |
| **Last Seen** | 2026-06-24 20:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1, echo '123qwerty' | sudo -S bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0' || bash -c 'm=0; while read k v r; do [ "$k" = MemTotal: ] && { m=$v; break; }; done < /proc/meminfo 2>/dev/null; [ "$m" -gt 1048576 ] 2>/dev/null && echo 1 || echo 0'` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:42:22` | `cowrie.session.connect` |
| `2026-06-24 20:42:23` | `cowrie.client.version` |
| `2026-06-24 20:42:23` | `cowrie.client.kex` |
| `2026-06-24 20:42:26` | `cowrie.login.success` |
| `2026-06-24 20:42:28` | `cowrie.session.params` |
| `2026-06-24 20:42:28` | `cowrie.command.input` |
| `2026-06-24 20:42:28` | `cowrie.command.input` |
| `2026-06-24 20:42:28` | `cowrie.command.input` |
| `2026-06-24 20:42:28` | `cowrie.command.input` |
| `2026-06-24 20:42:28` | `cowrie.log.closed` |
| `2026-06-24 20:42:30` | `cowrie.session.params` |
| `2026-06-24 20:42:30` | `cowrie.command.input` |
| `2026-06-24 20:42:30` | `cowrie.command.input` |
| `2026-06-24 20:42:30` | `cowrie.command.failed` |
| `2026-06-24 20:42:30` | `cowrie.command.failed` |
| `2026-06-24 20:42:30` | `cowrie.command.failed` |
| `2026-06-24 20:42:30` | `cowrie.command.failed` |
| `2026-06-24 20:42:30` | `cowrie.log.closed` |
| `2026-06-24 20:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2a5cf1814a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:42 |
| **Last Seen** | 2026-06-24 20:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:42:24` | `cowrie.session.connect` |
| `2026-06-24 20:42:24` | `cowrie.client.version` |
| `2026-06-24 20:42:24` | `cowrie.client.kex` |
| `2026-06-24 20:42:24` | `cowrie.login.success` |
| `2026-06-24 20:42:25` | `cowrie.session.params` |
| `2026-06-24 20:42:25` | `cowrie.command.input` |
| `2026-06-24 20:42:25` | `cowrie.log.closed` |
| `2026-06-24 20:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97ffa9180332

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:45 |
| **Last Seen** | 2026-06-24 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:45:51` | `cowrie.session.connect` |
| `2026-06-24 20:45:51` | `cowrie.client.version` |
| `2026-06-24 20:45:51` | `cowrie.client.kex` |
| `2026-06-24 20:45:51` | `cowrie.login.success` |
| `2026-06-24 20:45:52` | `cowrie.session.params` |
| `2026-06-24 20:45:52` | `cowrie.command.input` |
| `2026-06-24 20:45:52` | `cowrie.log.closed` |
| `2026-06-24 20:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b3bc64a440

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:46 |
| **Last Seen** | 2026-06-24 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:46:41` | `cowrie.session.connect` |
| `2026-06-24 20:46:41` | `cowrie.client.version` |
| `2026-06-24 20:46:41` | `cowrie.client.kex` |
| `2026-06-24 20:46:41` | `cowrie.login.success` |
| `2026-06-24 20:46:42` | `cowrie.session.params` |
| `2026-06-24 20:46:42` | `cowrie.command.input` |
| `2026-06-24 20:46:42` | `cowrie.log.closed` |
| `2026-06-24 20:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c5c74132a9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:47 |
| **Last Seen** | 2026-06-24 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:47:30` | `cowrie.session.connect` |
| `2026-06-24 20:47:30` | `cowrie.client.version` |
| `2026-06-24 20:47:30` | `cowrie.client.kex` |
| `2026-06-24 20:47:31` | `cowrie.login.success` |
| `2026-06-24 20:47:31` | `cowrie.session.params` |
| `2026-06-24 20:47:31` | `cowrie.command.input` |
| `2026-06-24 20:47:31` | `cowrie.log.closed` |
| `2026-06-24 20:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41c8a7e7e03

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:48 |
| **Last Seen** | 2026-06-24 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:48:21` | `cowrie.session.connect` |
| `2026-06-24 20:48:21` | `cowrie.client.version` |
| `2026-06-24 20:48:21` | `cowrie.client.kex` |
| `2026-06-24 20:48:21` | `cowrie.login.success` |
| `2026-06-24 20:48:22` | `cowrie.session.params` |
| `2026-06-24 20:48:22` | `cowrie.command.input` |
| `2026-06-24 20:48:22` | `cowrie.log.closed` |
| `2026-06-24 20:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4d4c508523

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:49 |
| **Last Seen** | 2026-06-24 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:49:13` | `cowrie.session.connect` |
| `2026-06-24 20:49:13` | `cowrie.client.version` |
| `2026-06-24 20:49:13` | `cowrie.client.kex` |
| `2026-06-24 20:49:13` | `cowrie.login.success` |
| `2026-06-24 20:49:14` | `cowrie.session.params` |
| `2026-06-24 20:49:14` | `cowrie.command.input` |
| `2026-06-24 20:49:14` | `cowrie.log.closed` |
| `2026-06-24 20:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4858b206a4d7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:50 |
| **Last Seen** | 2026-06-24 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:50:05` | `cowrie.session.connect` |
| `2026-06-24 20:50:05` | `cowrie.client.version` |
| `2026-06-24 20:50:05` | `cowrie.client.kex` |
| `2026-06-24 20:50:06` | `cowrie.login.success` |
| `2026-06-24 20:50:06` | `cowrie.session.params` |
| `2026-06-24 20:50:06` | `cowrie.command.input` |
| `2026-06-24 20:50:06` | `cowrie.log.closed` |
| `2026-06-24 20:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae401e3b6ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:50 |
| **Last Seen** | 2026-06-24 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:50:58` | `cowrie.session.connect` |
| `2026-06-24 20:50:58` | `cowrie.client.version` |
| `2026-06-24 20:50:59` | `cowrie.client.kex` |
| `2026-06-24 20:50:59` | `cowrie.login.success` |
| `2026-06-24 20:51:00` | `cowrie.session.params` |
| `2026-06-24 20:51:00` | `cowrie.command.input` |
| `2026-06-24 20:51:00` | `cowrie.log.closed` |
| `2026-06-24 20:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90eb39400bdd

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 20:51 |
| **Last Seen** | 2026-06-24 20:51 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:51:10` | `cowrie.session.connect` |
| `2026-06-24 20:51:12` | `cowrie.client.version` |
| `2026-06-24 20:51:12` | `cowrie.client.kex` |
| `2026-06-24 20:51:18` | `cowrie.login.success` |
| `2026-06-24 20:51:22` | `cowrie.session.params` |
| `2026-06-24 20:51:22` | `cowrie.command.input` |
| `2026-06-24 20:51:23` | `cowrie.log.closed` |
| `2026-06-24 20:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4532849b704d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:51 |
| **Last Seen** | 2026-06-24 20:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:51:52` | `cowrie.session.connect` |
| `2026-06-24 20:51:52` | `cowrie.client.version` |
| `2026-06-24 20:51:52` | `cowrie.client.kex` |
| `2026-06-24 20:51:53` | `cowrie.login.success` |
| `2026-06-24 20:51:53` | `cowrie.session.params` |
| `2026-06-24 20:51:53` | `cowrie.command.input` |
| `2026-06-24 20:51:53` | `cowrie.log.closed` |
| `2026-06-24 20:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6ef0a5500f0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:52 |
| **Last Seen** | 2026-06-24 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:52:45` | `cowrie.session.connect` |
| `2026-06-24 20:52:45` | `cowrie.client.version` |
| `2026-06-24 20:52:45` | `cowrie.client.kex` |
| `2026-06-24 20:52:45` | `cowrie.login.success` |
| `2026-06-24 20:52:46` | `cowrie.session.params` |
| `2026-06-24 20:52:46` | `cowrie.command.input` |
| `2026-06-24 20:52:46` | `cowrie.log.closed` |
| `2026-06-24 20:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c197bac2ab

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 20:53 |
| **Last Seen** | 2026-06-24 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:53:29` | `cowrie.session.connect` |
| `2026-06-24 20:53:29` | `cowrie.client.version` |
| `2026-06-24 20:53:29` | `cowrie.client.kex` |
| `2026-06-24 20:53:29` | `cowrie.login.success` |
| `2026-06-24 20:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3880973a366

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 20:53 |
| **Last Seen** | 2026-06-24 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:53:29` | `cowrie.session.connect` |
| `2026-06-24 20:53:29` | `cowrie.client.version` |
| `2026-06-24 20:53:29` | `cowrie.client.kex` |
| `2026-06-24 20:53:29` | `cowrie.login.success` |
| `2026-06-24 20:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171266339a57

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:53 |
| **Last Seen** | 2026-06-24 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:53:38` | `cowrie.session.connect` |
| `2026-06-24 20:53:38` | `cowrie.client.version` |
| `2026-06-24 20:53:38` | `cowrie.client.kex` |
| `2026-06-24 20:53:38` | `cowrie.login.success` |
| `2026-06-24 20:53:39` | `cowrie.session.params` |
| `2026-06-24 20:53:39` | `cowrie.command.input` |
| `2026-06-24 20:53:39` | `cowrie.log.closed` |
| `2026-06-24 20:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3de7c2c6c69

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 20:53 |
| **Last Seen** | 2026-06-24 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:53:38` | `cowrie.session.connect` |
| `2026-06-24 20:53:38` | `cowrie.client.version` |
| `2026-06-24 20:53:38` | `cowrie.client.kex` |
| `2026-06-24 20:53:38` | `cowrie.login.success` |
| `2026-06-24 20:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edfd77245ef6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-06-24 20:53 |
| **Last Seen** | 2026-06-24 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:53:38` | `cowrie.session.connect` |
| `2026-06-24 20:53:38` | `cowrie.client.version` |
| `2026-06-24 20:53:38` | `cowrie.client.kex` |
| `2026-06-24 20:53:38` | `cowrie.login.success` |
| `2026-06-24 20:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4197e5e51d8d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:54 |
| **Last Seen** | 2026-06-24 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:54:31` | `cowrie.session.connect` |
| `2026-06-24 20:54:31` | `cowrie.client.version` |
| `2026-06-24 20:54:31` | `cowrie.client.kex` |
| `2026-06-24 20:54:31` | `cowrie.login.success` |
| `2026-06-24 20:54:32` | `cowrie.session.params` |
| `2026-06-24 20:54:32` | `cowrie.command.input` |
| `2026-06-24 20:54:32` | `cowrie.log.closed` |
| `2026-06-24 20:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50659371b8db

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:55 |
| **Last Seen** | 2026-06-24 20:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:55:25` | `cowrie.session.connect` |
| `2026-06-24 20:55:25` | `cowrie.client.version` |
| `2026-06-24 20:55:25` | `cowrie.client.kex` |
| `2026-06-24 20:55:26` | `cowrie.login.success` |
| `2026-06-24 20:55:26` | `cowrie.session.params` |
| `2026-06-24 20:55:26` | `cowrie.command.input` |
| `2026-06-24 20:55:27` | `cowrie.log.closed` |
| `2026-06-24 20:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9656b84b7f23

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:56 |
| **Last Seen** | 2026-06-24 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:56:20` | `cowrie.session.connect` |
| `2026-06-24 20:56:20` | `cowrie.client.version` |
| `2026-06-24 20:56:20` | `cowrie.client.kex` |
| `2026-06-24 20:56:20` | `cowrie.login.success` |
| `2026-06-24 20:56:21` | `cowrie.session.params` |
| `2026-06-24 20:56:21` | `cowrie.command.input` |
| `2026-06-24 20:56:21` | `cowrie.log.closed` |
| `2026-06-24 20:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb015dea33ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:57 |
| **Last Seen** | 2026-06-24 20:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:57:14` | `cowrie.session.connect` |
| `2026-06-24 20:57:14` | `cowrie.client.version` |
| `2026-06-24 20:57:15` | `cowrie.client.kex` |
| `2026-06-24 20:57:15` | `cowrie.login.success` |
| `2026-06-24 20:57:16` | `cowrie.session.params` |
| `2026-06-24 20:57:16` | `cowrie.command.input` |
| `2026-06-24 20:57:16` | `cowrie.log.closed` |
| `2026-06-24 20:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb4940f031b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:58 |
| **Last Seen** | 2026-06-24 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:58:08` | `cowrie.session.connect` |
| `2026-06-24 20:58:08` | `cowrie.client.version` |
| `2026-06-24 20:58:08` | `cowrie.client.kex` |
| `2026-06-24 20:58:09` | `cowrie.login.success` |
| `2026-06-24 20:58:10` | `cowrie.session.params` |
| `2026-06-24 20:58:10` | `cowrie.command.input` |
| `2026-06-24 20:58:10` | `cowrie.log.closed` |
| `2026-06-24 20:58:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb17e5ecf1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:59 |
| **Last Seen** | 2026-06-24 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:59:01` | `cowrie.session.connect` |
| `2026-06-24 20:59:01` | `cowrie.client.version` |
| `2026-06-24 20:59:01` | `cowrie.client.kex` |
| `2026-06-24 20:59:01` | `cowrie.login.success` |
| `2026-06-24 20:59:02` | `cowrie.session.params` |
| `2026-06-24 20:59:02` | `cowrie.command.input` |
| `2026-06-24 20:59:02` | `cowrie.log.closed` |
| `2026-06-24 20:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a6098fc3b9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 20:59 |
| **Last Seen** | 2026-06-24 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 20:59:53` | `cowrie.session.connect` |
| `2026-06-24 20:59:53` | `cowrie.client.version` |
| `2026-06-24 20:59:53` | `cowrie.client.kex` |
| `2026-06-24 20:59:53` | `cowrie.login.success` |
| `2026-06-24 20:59:54` | `cowrie.session.params` |
| `2026-06-24 20:59:54` | `cowrie.command.input` |
| `2026-06-24 20:59:54` | `cowrie.log.closed` |
| `2026-06-24 20:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24b0f9a8e746

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:00 |
| **Last Seen** | 2026-06-24 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:00:46` | `cowrie.session.connect` |
| `2026-06-24 21:00:46` | `cowrie.client.version` |
| `2026-06-24 21:00:46` | `cowrie.client.kex` |
| `2026-06-24 21:00:46` | `cowrie.login.success` |
| `2026-06-24 21:00:47` | `cowrie.session.params` |
| `2026-06-24 21:00:47` | `cowrie.command.input` |
| `2026-06-24 21:00:47` | `cowrie.log.closed` |
| `2026-06-24 21:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ee7192f0f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:01 |
| **Last Seen** | 2026-06-24 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:01:40` | `cowrie.session.connect` |
| `2026-06-24 21:01:40` | `cowrie.client.version` |
| `2026-06-24 21:01:40` | `cowrie.client.kex` |
| `2026-06-24 21:01:40` | `cowrie.login.success` |
| `2026-06-24 21:01:41` | `cowrie.session.params` |
| `2026-06-24 21:01:41` | `cowrie.command.input` |
| `2026-06-24 21:01:41` | `cowrie.log.closed` |
| `2026-06-24 21:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46e32c2e5c8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-24 21:01 |
| **Last Seen** | 2026-06-24 21:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:01:53` | `cowrie.session.connect` |
| `2026-06-24 21:01:53` | `cowrie.client.version` |
| `2026-06-24 21:01:53` | `cowrie.client.kex` |
| `2026-06-24 21:01:54` | `cowrie.login.success` |
| `2026-06-24 21:01:54` | `cowrie.direct-tcpip.request` |
| `2026-06-24 21:01:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-24 21:01:54` | `cowrie.direct-tcpip.data` |
| `2026-06-24 21:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61723e743a04

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-06-24 21:01 |
| **Last Seen** | 2026-06-24 21:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:01:54` | `cowrie.session.connect` |
| `2026-06-24 21:01:54` | `cowrie.client.version` |
| `2026-06-24 21:01:54` | `cowrie.client.kex` |
| `2026-06-24 21:01:54` | `cowrie.login.success` |
| `2026-06-24 21:01:54` | `cowrie.direct-tcpip.request` |
| `2026-06-24 21:01:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-06-24 21:01:54` | `cowrie.direct-tcpip.data` |
| `2026-06-24 21:01:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7998b2445c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:02 |
| **Last Seen** | 2026-06-24 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:02:35` | `cowrie.session.connect` |
| `2026-06-24 21:02:35` | `cowrie.client.version` |
| `2026-06-24 21:02:35` | `cowrie.client.kex` |
| `2026-06-24 21:02:35` | `cowrie.login.success` |
| `2026-06-24 21:02:36` | `cowrie.session.params` |
| `2026-06-24 21:02:36` | `cowrie.command.input` |
| `2026-06-24 21:02:36` | `cowrie.log.closed` |
| `2026-06-24 21:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44d2b9276039

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:03 |
| **Last Seen** | 2026-06-24 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:03:30` | `cowrie.session.connect` |
| `2026-06-24 21:03:30` | `cowrie.client.version` |
| `2026-06-24 21:03:30` | `cowrie.client.kex` |
| `2026-06-24 21:03:30` | `cowrie.login.success` |
| `2026-06-24 21:03:31` | `cowrie.session.params` |
| `2026-06-24 21:03:31` | `cowrie.command.input` |
| `2026-06-24 21:03:31` | `cowrie.log.closed` |
| `2026-06-24 21:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5395d92e029

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-24 21:03 |
| **Last Seen** | 2026-06-24 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:03:52` | `cowrie.session.connect` |
| `2026-06-24 21:03:52` | `cowrie.client.version` |
| `2026-06-24 21:03:52` | `cowrie.client.kex` |
| `2026-06-24 21:03:53` | `cowrie.login.success` |
| `2026-06-24 21:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e3c9ee0ec90

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-06-24 21:03 |
| **Last Seen** | 2026-06-24 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:03:53` | `cowrie.session.connect` |
| `2026-06-24 21:03:53` | `cowrie.client.version` |
| `2026-06-24 21:03:53` | `cowrie.client.kex` |
| `2026-06-24 21:03:54` | `cowrie.login.success` |
| `2026-06-24 21:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fec6e92ab849

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:04 |
| **Last Seen** | 2026-06-24 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:04:25` | `cowrie.session.connect` |
| `2026-06-24 21:04:25` | `cowrie.client.version` |
| `2026-06-24 21:04:25` | `cowrie.client.kex` |
| `2026-06-24 21:04:26` | `cowrie.login.success` |
| `2026-06-24 21:04:26` | `cowrie.session.params` |
| `2026-06-24 21:04:26` | `cowrie.command.input` |
| `2026-06-24 21:04:27` | `cowrie.log.closed` |
| `2026-06-24 21:04:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13c56c98d15

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:05 |
| **Last Seen** | 2026-06-24 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:05:20` | `cowrie.session.connect` |
| `2026-06-24 21:05:20` | `cowrie.client.version` |
| `2026-06-24 21:05:21` | `cowrie.client.kex` |
| `2026-06-24 21:05:21` | `cowrie.login.success` |
| `2026-06-24 21:05:22` | `cowrie.session.params` |
| `2026-06-24 21:05:22` | `cowrie.command.input` |
| `2026-06-24 21:05:22` | `cowrie.log.closed` |
| `2026-06-24 21:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2efa04aa7af8

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 21:05 |
| **Last Seen** | 2026-06-24 21:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:05:29` | `cowrie.session.connect` |
| `2026-06-24 21:05:31` | `cowrie.client.version` |
| `2026-06-24 21:05:31` | `cowrie.client.kex` |
| `2026-06-24 21:05:37` | `cowrie.login.success` |
| `2026-06-24 21:05:40` | `cowrie.session.params` |
| `2026-06-24 21:05:40` | `cowrie.command.input` |
| `2026-06-24 21:05:42` | `cowrie.log.closed` |
| `2026-06-24 21:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281df50479fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:06 |
| **Last Seen** | 2026-06-24 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:06:15` | `cowrie.session.connect` |
| `2026-06-24 21:06:15` | `cowrie.client.version` |
| `2026-06-24 21:06:15` | `cowrie.client.kex` |
| `2026-06-24 21:06:16` | `cowrie.login.success` |
| `2026-06-24 21:06:16` | `cowrie.session.params` |
| `2026-06-24 21:06:16` | `cowrie.command.input` |
| `2026-06-24 21:06:17` | `cowrie.log.closed` |
| `2026-06-24 21:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7654379b2dc3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:07 |
| **Last Seen** | 2026-06-24 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:07:10` | `cowrie.session.connect` |
| `2026-06-24 21:07:10` | `cowrie.client.version` |
| `2026-06-24 21:07:10` | `cowrie.client.kex` |
| `2026-06-24 21:07:10` | `cowrie.login.success` |
| `2026-06-24 21:07:11` | `cowrie.session.params` |
| `2026-06-24 21:07:11` | `cowrie.command.input` |
| `2026-06-24 21:07:11` | `cowrie.log.closed` |
| `2026-06-24 21:07:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a918ead019ec

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:08 |
| **Last Seen** | 2026-06-24 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:08:06` | `cowrie.session.connect` |
| `2026-06-24 21:08:06` | `cowrie.client.version` |
| `2026-06-24 21:08:06` | `cowrie.client.kex` |
| `2026-06-24 21:08:06` | `cowrie.login.success` |
| `2026-06-24 21:08:07` | `cowrie.session.params` |
| `2026-06-24 21:08:07` | `cowrie.command.input` |
| `2026-06-24 21:08:07` | `cowrie.log.closed` |
| `2026-06-24 21:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-627ae5ff0dc7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:09 |
| **Last Seen** | 2026-06-24 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:09:03` | `cowrie.session.connect` |
| `2026-06-24 21:09:03` | `cowrie.client.version` |
| `2026-06-24 21:09:03` | `cowrie.client.kex` |
| `2026-06-24 21:09:03` | `cowrie.login.success` |
| `2026-06-24 21:09:04` | `cowrie.session.params` |
| `2026-06-24 21:09:04` | `cowrie.command.input` |
| `2026-06-24 21:09:04` | `cowrie.log.closed` |
| `2026-06-24 21:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df13ded0c43

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:09 |
| **Last Seen** | 2026-06-24 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:09:59` | `cowrie.session.connect` |
| `2026-06-24 21:09:59` | `cowrie.client.version` |
| `2026-06-24 21:09:59` | `cowrie.client.kex` |
| `2026-06-24 21:10:00` | `cowrie.login.success` |
| `2026-06-24 21:10:00` | `cowrie.session.params` |
| `2026-06-24 21:10:00` | `cowrie.command.input` |
| `2026-06-24 21:10:01` | `cowrie.log.closed` |
| `2026-06-24 21:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339c3b33f1d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:10 |
| **Last Seen** | 2026-06-24 21:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:10:55` | `cowrie.session.connect` |
| `2026-06-24 21:10:55` | `cowrie.client.version` |
| `2026-06-24 21:10:55` | `cowrie.client.kex` |
| `2026-06-24 21:10:55` | `cowrie.login.success` |
| `2026-06-24 21:10:56` | `cowrie.session.params` |
| `2026-06-24 21:10:56` | `cowrie.command.input` |
| `2026-06-24 21:10:56` | `cowrie.log.closed` |
| `2026-06-24 21:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20b89fbc56ce

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:11 |
| **Last Seen** | 2026-06-24 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:11:50` | `cowrie.session.connect` |
| `2026-06-24 21:11:50` | `cowrie.client.version` |
| `2026-06-24 21:11:50` | `cowrie.client.kex` |
| `2026-06-24 21:11:50` | `cowrie.login.success` |
| `2026-06-24 21:11:51` | `cowrie.session.params` |
| `2026-06-24 21:11:51` | `cowrie.command.input` |
| `2026-06-24 21:11:51` | `cowrie.log.closed` |
| `2026-06-24 21:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294be9e3eb09

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:12 |
| **Last Seen** | 2026-06-24 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:12:45` | `cowrie.session.connect` |
| `2026-06-24 21:12:45` | `cowrie.client.version` |
| `2026-06-24 21:12:45` | `cowrie.client.kex` |
| `2026-06-24 21:12:45` | `cowrie.login.success` |
| `2026-06-24 21:12:46` | `cowrie.session.params` |
| `2026-06-24 21:12:46` | `cowrie.command.input` |
| `2026-06-24 21:12:46` | `cowrie.log.closed` |
| `2026-06-24 21:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06127dc396b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:13 |
| **Last Seen** | 2026-06-24 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:13:40` | `cowrie.session.connect` |
| `2026-06-24 21:13:40` | `cowrie.client.version` |
| `2026-06-24 21:13:40` | `cowrie.client.kex` |
| `2026-06-24 21:13:41` | `cowrie.login.success` |
| `2026-06-24 21:13:41` | `cowrie.session.params` |
| `2026-06-24 21:13:41` | `cowrie.command.input` |
| `2026-06-24 21:13:42` | `cowrie.log.closed` |
| `2026-06-24 21:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3706a234b459

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:14 |
| **Last Seen** | 2026-06-24 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:14:37` | `cowrie.session.connect` |
| `2026-06-24 21:14:37` | `cowrie.client.version` |
| `2026-06-24 21:14:37` | `cowrie.client.kex` |
| `2026-06-24 21:14:37` | `cowrie.login.success` |
| `2026-06-24 21:14:38` | `cowrie.session.params` |
| `2026-06-24 21:14:38` | `cowrie.command.input` |
| `2026-06-24 21:14:38` | `cowrie.log.closed` |
| `2026-06-24 21:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a8763c6c1d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:15 |
| **Last Seen** | 2026-06-24 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:15:36` | `cowrie.session.connect` |
| `2026-06-24 21:15:36` | `cowrie.client.version` |
| `2026-06-24 21:15:36` | `cowrie.client.kex` |
| `2026-06-24 21:15:36` | `cowrie.login.success` |
| `2026-06-24 21:15:37` | `cowrie.session.params` |
| `2026-06-24 21:15:37` | `cowrie.command.input` |
| `2026-06-24 21:15:37` | `cowrie.log.closed` |
| `2026-06-24 21:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15e48b1eac76

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:16 |
| **Last Seen** | 2026-06-24 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:16:34` | `cowrie.session.connect` |
| `2026-06-24 21:16:34` | `cowrie.client.version` |
| `2026-06-24 21:16:34` | `cowrie.client.kex` |
| `2026-06-24 21:16:35` | `cowrie.login.success` |
| `2026-06-24 21:16:35` | `cowrie.session.params` |
| `2026-06-24 21:16:35` | `cowrie.command.input` |
| `2026-06-24 21:16:36` | `cowrie.log.closed` |
| `2026-06-24 21:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba79c24bed5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:17 |
| **Last Seen** | 2026-06-24 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:17:33` | `cowrie.session.connect` |
| `2026-06-24 21:17:33` | `cowrie.client.version` |
| `2026-06-24 21:17:33` | `cowrie.client.kex` |
| `2026-06-24 21:17:33` | `cowrie.login.success` |
| `2026-06-24 21:17:34` | `cowrie.session.params` |
| `2026-06-24 21:17:34` | `cowrie.command.input` |
| `2026-06-24 21:17:34` | `cowrie.log.closed` |
| `2026-06-24 21:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04de5513f7fb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:18 |
| **Last Seen** | 2026-06-24 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:18:30` | `cowrie.session.connect` |
| `2026-06-24 21:18:30` | `cowrie.client.version` |
| `2026-06-24 21:18:30` | `cowrie.client.kex` |
| `2026-06-24 21:18:30` | `cowrie.login.success` |
| `2026-06-24 21:18:31` | `cowrie.session.params` |
| `2026-06-24 21:18:31` | `cowrie.command.input` |
| `2026-06-24 21:18:31` | `cowrie.log.closed` |
| `2026-06-24 21:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146856ad07f3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:19 |
| **Last Seen** | 2026-06-24 21:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:19:27` | `cowrie.session.connect` |
| `2026-06-24 21:19:27` | `cowrie.client.version` |
| `2026-06-24 21:19:27` | `cowrie.client.kex` |
| `2026-06-24 21:19:27` | `cowrie.login.success` |
| `2026-06-24 21:19:28` | `cowrie.session.params` |
| `2026-06-24 21:19:28` | `cowrie.command.input` |
| `2026-06-24 21:19:28` | `cowrie.log.closed` |
| `2026-06-24 21:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a0d82db74c6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 21:19 |
| **Last Seen** | 2026-06-24 21:20 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:19:59` | `cowrie.session.connect` |
| `2026-06-24 21:20:01` | `cowrie.client.version` |
| `2026-06-24 21:20:01` | `cowrie.client.kex` |
| `2026-06-24 21:20:07` | `cowrie.login.success` |
| `2026-06-24 21:20:12` | `cowrie.session.params` |
| `2026-06-24 21:20:12` | `cowrie.command.input` |
| `2026-06-24 21:20:14` | `cowrie.log.closed` |
| `2026-06-24 21:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72fd346eb1c0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:20 |
| **Last Seen** | 2026-06-24 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:20:26` | `cowrie.session.connect` |
| `2026-06-24 21:20:26` | `cowrie.client.version` |
| `2026-06-24 21:20:26` | `cowrie.client.kex` |
| `2026-06-24 21:20:26` | `cowrie.login.success` |
| `2026-06-24 21:20:27` | `cowrie.session.params` |
| `2026-06-24 21:20:27` | `cowrie.command.input` |
| `2026-06-24 21:20:27` | `cowrie.log.closed` |
| `2026-06-24 21:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079cc8845352

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:21 |
| **Last Seen** | 2026-06-24 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:21:25` | `cowrie.session.connect` |
| `2026-06-24 21:21:25` | `cowrie.client.version` |
| `2026-06-24 21:21:25` | `cowrie.client.kex` |
| `2026-06-24 21:21:26` | `cowrie.login.success` |
| `2026-06-24 21:21:27` | `cowrie.session.params` |
| `2026-06-24 21:21:27` | `cowrie.command.input` |
| `2026-06-24 21:21:27` | `cowrie.log.closed` |
| `2026-06-24 21:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8fae674b725

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:22 |
| **Last Seen** | 2026-06-24 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:22:26` | `cowrie.session.connect` |
| `2026-06-24 21:22:26` | `cowrie.client.version` |
| `2026-06-24 21:22:26` | `cowrie.client.kex` |
| `2026-06-24 21:22:27` | `cowrie.login.success` |
| `2026-06-24 21:22:27` | `cowrie.session.params` |
| `2026-06-24 21:22:27` | `cowrie.command.input` |
| `2026-06-24 21:22:27` | `cowrie.log.closed` |
| `2026-06-24 21:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39d72c36cc0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:23 |
| **Last Seen** | 2026-06-24 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:23:27` | `cowrie.session.connect` |
| `2026-06-24 21:23:27` | `cowrie.client.version` |
| `2026-06-24 21:23:27` | `cowrie.client.kex` |
| `2026-06-24 21:23:27` | `cowrie.login.success` |
| `2026-06-24 21:23:28` | `cowrie.session.params` |
| `2026-06-24 21:23:28` | `cowrie.command.input` |
| `2026-06-24 21:23:28` | `cowrie.log.closed` |
| `2026-06-24 21:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f6c2715c480

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:24 |
| **Last Seen** | 2026-06-24 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:24:25` | `cowrie.session.connect` |
| `2026-06-24 21:24:25` | `cowrie.client.version` |
| `2026-06-24 21:24:26` | `cowrie.client.kex` |
| `2026-06-24 21:24:26` | `cowrie.login.success` |
| `2026-06-24 21:24:27` | `cowrie.session.params` |
| `2026-06-24 21:24:27` | `cowrie.command.input` |
| `2026-06-24 21:24:27` | `cowrie.log.closed` |
| `2026-06-24 21:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d130344cc9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:25 |
| **Last Seen** | 2026-06-24 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:25:23` | `cowrie.session.connect` |
| `2026-06-24 21:25:23` | `cowrie.client.version` |
| `2026-06-24 21:25:23` | `cowrie.client.kex` |
| `2026-06-24 21:25:23` | `cowrie.login.success` |
| `2026-06-24 21:25:24` | `cowrie.session.params` |
| `2026-06-24 21:25:24` | `cowrie.command.input` |
| `2026-06-24 21:25:24` | `cowrie.log.closed` |
| `2026-06-24 21:25:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad5525ba135

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:26 |
| **Last Seen** | 2026-06-24 21:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:26:21` | `cowrie.session.connect` |
| `2026-06-24 21:26:21` | `cowrie.client.version` |
| `2026-06-24 21:26:22` | `cowrie.client.kex` |
| `2026-06-24 21:26:22` | `cowrie.login.success` |
| `2026-06-24 21:26:23` | `cowrie.session.params` |
| `2026-06-24 21:26:23` | `cowrie.command.input` |
| `2026-06-24 21:26:23` | `cowrie.log.closed` |
| `2026-06-24 21:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cf4cb75b879

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:27 |
| **Last Seen** | 2026-06-24 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:27:22` | `cowrie.session.connect` |
| `2026-06-24 21:27:22` | `cowrie.client.version` |
| `2026-06-24 21:27:22` | `cowrie.client.kex` |
| `2026-06-24 21:27:22` | `cowrie.login.success` |
| `2026-06-24 21:27:23` | `cowrie.session.params` |
| `2026-06-24 21:27:23` | `cowrie.command.input` |
| `2026-06-24 21:27:23` | `cowrie.log.closed` |
| `2026-06-24 21:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e33f41c234d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:28 |
| **Last Seen** | 2026-06-24 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:28:23` | `cowrie.session.connect` |
| `2026-06-24 21:28:23` | `cowrie.client.version` |
| `2026-06-24 21:28:23` | `cowrie.client.kex` |
| `2026-06-24 21:28:23` | `cowrie.login.success` |
| `2026-06-24 21:28:24` | `cowrie.session.params` |
| `2026-06-24 21:28:24` | `cowrie.command.input` |
| `2026-06-24 21:28:24` | `cowrie.log.closed` |
| `2026-06-24 21:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22bf8b165b4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:29 |
| **Last Seen** | 2026-06-24 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:29:23` | `cowrie.session.connect` |
| `2026-06-24 21:29:23` | `cowrie.client.version` |
| `2026-06-24 21:29:23` | `cowrie.client.kex` |
| `2026-06-24 21:29:24` | `cowrie.login.success` |
| `2026-06-24 21:29:25` | `cowrie.session.params` |
| `2026-06-24 21:29:25` | `cowrie.command.input` |
| `2026-06-24 21:29:25` | `cowrie.log.closed` |
| `2026-06-24 21:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e416ad67e4f6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:30 |
| **Last Seen** | 2026-06-24 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:30:24` | `cowrie.session.connect` |
| `2026-06-24 21:30:24` | `cowrie.client.version` |
| `2026-06-24 21:30:25` | `cowrie.client.kex` |
| `2026-06-24 21:30:25` | `cowrie.login.success` |
| `2026-06-24 21:30:26` | `cowrie.session.params` |
| `2026-06-24 21:30:26` | `cowrie.command.input` |
| `2026-06-24 21:30:26` | `cowrie.log.closed` |
| `2026-06-24 21:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5ee4acb41a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:31 |
| **Last Seen** | 2026-06-24 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:31:26` | `cowrie.session.connect` |
| `2026-06-24 21:31:26` | `cowrie.client.version` |
| `2026-06-24 21:31:26` | `cowrie.client.kex` |
| `2026-06-24 21:31:26` | `cowrie.login.success` |
| `2026-06-24 21:31:27` | `cowrie.session.params` |
| `2026-06-24 21:31:27` | `cowrie.command.input` |
| `2026-06-24 21:31:27` | `cowrie.log.closed` |
| `2026-06-24 21:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c7c7ef9f27e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:32 |
| **Last Seen** | 2026-06-24 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:32:28` | `cowrie.session.connect` |
| `2026-06-24 21:32:28` | `cowrie.client.version` |
| `2026-06-24 21:32:28` | `cowrie.client.kex` |
| `2026-06-24 21:32:29` | `cowrie.login.success` |
| `2026-06-24 21:32:29` | `cowrie.session.params` |
| `2026-06-24 21:32:29` | `cowrie.command.input` |
| `2026-06-24 21:32:29` | `cowrie.log.closed` |
| `2026-06-24 21:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1386ee676850

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:33 |
| **Last Seen** | 2026-06-24 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:33:32` | `cowrie.session.connect` |
| `2026-06-24 21:33:32` | `cowrie.client.version` |
| `2026-06-24 21:33:32` | `cowrie.client.kex` |
| `2026-06-24 21:33:32` | `cowrie.login.success` |
| `2026-06-24 21:33:33` | `cowrie.session.params` |
| `2026-06-24 21:33:33` | `cowrie.command.input` |
| `2026-06-24 21:33:33` | `cowrie.log.closed` |
| `2026-06-24 21:33:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a984febfd30a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 21:34 |
| **Last Seen** | 2026-06-24 21:34 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:34:14` | `cowrie.session.connect` |
| `2026-06-24 21:34:16` | `cowrie.client.version` |
| `2026-06-24 21:34:16` | `cowrie.client.kex` |
| `2026-06-24 21:34:23` | `cowrie.login.success` |
| `2026-06-24 21:34:27` | `cowrie.session.params` |
| `2026-06-24 21:34:27` | `cowrie.command.input` |
| `2026-06-24 21:34:29` | `cowrie.log.closed` |
| `2026-06-24 21:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe6e5e97125

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:34 |
| **Last Seen** | 2026-06-24 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:34:37` | `cowrie.session.connect` |
| `2026-06-24 21:34:37` | `cowrie.client.version` |
| `2026-06-24 21:34:37` | `cowrie.client.kex` |
| `2026-06-24 21:34:37` | `cowrie.login.success` |
| `2026-06-24 21:34:38` | `cowrie.session.params` |
| `2026-06-24 21:34:38` | `cowrie.command.input` |
| `2026-06-24 21:34:38` | `cowrie.log.closed` |
| `2026-06-24 21:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f504d9d21fc5

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:35 |
| **Last Seen** | 2026-06-24 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:35:42` | `cowrie.session.connect` |
| `2026-06-24 21:35:42` | `cowrie.client.version` |
| `2026-06-24 21:35:42` | `cowrie.client.kex` |
| `2026-06-24 21:35:42` | `cowrie.login.success` |
| `2026-06-24 21:35:43` | `cowrie.session.params` |
| `2026-06-24 21:35:43` | `cowrie.command.input` |
| `2026-06-24 21:35:43` | `cowrie.log.closed` |
| `2026-06-24 21:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e84c18c5b2b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:36 |
| **Last Seen** | 2026-06-24 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:36:46` | `cowrie.session.connect` |
| `2026-06-24 21:36:46` | `cowrie.client.version` |
| `2026-06-24 21:36:46` | `cowrie.client.kex` |
| `2026-06-24 21:36:46` | `cowrie.login.success` |
| `2026-06-24 21:36:47` | `cowrie.session.params` |
| `2026-06-24 21:36:47` | `cowrie.command.input` |
| `2026-06-24 21:36:47` | `cowrie.log.closed` |
| `2026-06-24 21:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25c0b8bfd09c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:37 |
| **Last Seen** | 2026-06-24 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:37:49` | `cowrie.session.connect` |
| `2026-06-24 21:37:49` | `cowrie.client.version` |
| `2026-06-24 21:37:49` | `cowrie.client.kex` |
| `2026-06-24 21:37:49` | `cowrie.login.success` |
| `2026-06-24 21:37:50` | `cowrie.session.params` |
| `2026-06-24 21:37:50` | `cowrie.command.input` |
| `2026-06-24 21:37:50` | `cowrie.log.closed` |
| `2026-06-24 21:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160530c34e89

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:38 |
| **Last Seen** | 2026-06-24 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:38:53` | `cowrie.session.connect` |
| `2026-06-24 21:38:53` | `cowrie.client.version` |
| `2026-06-24 21:38:53` | `cowrie.client.kex` |
| `2026-06-24 21:38:54` | `cowrie.login.success` |
| `2026-06-24 21:38:55` | `cowrie.session.params` |
| `2026-06-24 21:38:55` | `cowrie.command.input` |
| `2026-06-24 21:38:55` | `cowrie.log.closed` |
| `2026-06-24 21:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ed05643049

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:40 |
| **Last Seen** | 2026-06-24 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:40:00` | `cowrie.session.connect` |
| `2026-06-24 21:40:00` | `cowrie.client.version` |
| `2026-06-24 21:40:00` | `cowrie.client.kex` |
| `2026-06-24 21:40:01` | `cowrie.login.success` |
| `2026-06-24 21:40:01` | `cowrie.session.params` |
| `2026-06-24 21:40:01` | `cowrie.command.input` |
| `2026-06-24 21:40:01` | `cowrie.log.closed` |
| `2026-06-24 21:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-458d2899c231

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:41 |
| **Last Seen** | 2026-06-24 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:41:10` | `cowrie.session.connect` |
| `2026-06-24 21:41:10` | `cowrie.client.version` |
| `2026-06-24 21:41:10` | `cowrie.client.kex` |
| `2026-06-24 21:41:10` | `cowrie.login.success` |
| `2026-06-24 21:41:11` | `cowrie.session.params` |
| `2026-06-24 21:41:11` | `cowrie.command.input` |
| `2026-06-24 21:41:11` | `cowrie.log.closed` |
| `2026-06-24 21:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad13d7d75b47

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:42 |
| **Last Seen** | 2026-06-24 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:42:18` | `cowrie.session.connect` |
| `2026-06-24 21:42:18` | `cowrie.client.version` |
| `2026-06-24 21:42:18` | `cowrie.client.kex` |
| `2026-06-24 21:42:18` | `cowrie.login.success` |
| `2026-06-24 21:42:19` | `cowrie.session.params` |
| `2026-06-24 21:42:19` | `cowrie.command.input` |
| `2026-06-24 21:42:19` | `cowrie.log.closed` |
| `2026-06-24 21:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ace163bcf01

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:43 |
| **Last Seen** | 2026-06-24 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:43:26` | `cowrie.session.connect` |
| `2026-06-24 21:43:26` | `cowrie.client.version` |
| `2026-06-24 21:43:26` | `cowrie.client.kex` |
| `2026-06-24 21:43:27` | `cowrie.login.success` |
| `2026-06-24 21:43:27` | `cowrie.session.params` |
| `2026-06-24 21:43:27` | `cowrie.command.input` |
| `2026-06-24 21:43:28` | `cowrie.log.closed` |
| `2026-06-24 21:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5ad4b74754

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:44 |
| **Last Seen** | 2026-06-24 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:44:33` | `cowrie.session.connect` |
| `2026-06-24 21:44:33` | `cowrie.client.version` |
| `2026-06-24 21:44:33` | `cowrie.client.kex` |
| `2026-06-24 21:44:34` | `cowrie.login.success` |
| `2026-06-24 21:44:35` | `cowrie.session.params` |
| `2026-06-24 21:44:35` | `cowrie.command.input` |
| `2026-06-24 21:44:35` | `cowrie.log.closed` |
| `2026-06-24 21:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e72aae2b1b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:45 |
| **Last Seen** | 2026-06-24 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:45:44` | `cowrie.session.connect` |
| `2026-06-24 21:45:44` | `cowrie.client.version` |
| `2026-06-24 21:45:44` | `cowrie.client.kex` |
| `2026-06-24 21:45:45` | `cowrie.login.success` |
| `2026-06-24 21:45:45` | `cowrie.session.params` |
| `2026-06-24 21:45:45` | `cowrie.command.input` |
| `2026-06-24 21:45:45` | `cowrie.log.closed` |
| `2026-06-24 21:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e79eed51ba

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:46 |
| **Last Seen** | 2026-06-24 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:46:54` | `cowrie.session.connect` |
| `2026-06-24 21:46:54` | `cowrie.client.version` |
| `2026-06-24 21:46:54` | `cowrie.client.kex` |
| `2026-06-24 21:46:55` | `cowrie.login.success` |
| `2026-06-24 21:46:56` | `cowrie.session.params` |
| `2026-06-24 21:46:56` | `cowrie.command.input` |
| `2026-06-24 21:46:56` | `cowrie.log.closed` |
| `2026-06-24 21:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff832c1feb6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:48 |
| **Last Seen** | 2026-06-24 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:48:06` | `cowrie.session.connect` |
| `2026-06-24 21:48:06` | `cowrie.client.version` |
| `2026-06-24 21:48:06` | `cowrie.client.kex` |
| `2026-06-24 21:48:06` | `cowrie.login.success` |
| `2026-06-24 21:48:07` | `cowrie.session.params` |
| `2026-06-24 21:48:07` | `cowrie.command.input` |
| `2026-06-24 21:48:07` | `cowrie.log.closed` |
| `2026-06-24 21:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7f1cb57a1f1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 21:48 |
| **Last Seen** | 2026-06-24 21:48 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:48:45` | `cowrie.session.connect` |
| `2026-06-24 21:48:46` | `cowrie.client.version` |
| `2026-06-24 21:48:46` | `cowrie.client.kex` |
| `2026-06-24 21:48:52` | `cowrie.login.success` |
| `2026-06-24 21:48:56` | `cowrie.session.params` |
| `2026-06-24 21:48:56` | `cowrie.command.input` |
| `2026-06-24 21:48:58` | `cowrie.log.closed` |
| `2026-06-24 21:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d92266b0d6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:49 |
| **Last Seen** | 2026-06-24 21:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:49:14` | `cowrie.session.connect` |
| `2026-06-24 21:49:14` | `cowrie.client.version` |
| `2026-06-24 21:49:14` | `cowrie.client.kex` |
| `2026-06-24 21:49:14` | `cowrie.login.success` |
| `2026-06-24 21:49:15` | `cowrie.session.params` |
| `2026-06-24 21:49:15` | `cowrie.command.input` |
| `2026-06-24 21:49:15` | `cowrie.log.closed` |
| `2026-06-24 21:49:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-718dcc23ae77

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:50 |
| **Last Seen** | 2026-06-24 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:50:20` | `cowrie.session.connect` |
| `2026-06-24 21:50:20` | `cowrie.client.version` |
| `2026-06-24 21:50:20` | `cowrie.client.kex` |
| `2026-06-24 21:50:20` | `cowrie.login.success` |
| `2026-06-24 21:50:21` | `cowrie.session.params` |
| `2026-06-24 21:50:21` | `cowrie.command.input` |
| `2026-06-24 21:50:21` | `cowrie.log.closed` |
| `2026-06-24 21:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dab3f332cf8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:51 |
| **Last Seen** | 2026-06-24 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:51:24` | `cowrie.session.connect` |
| `2026-06-24 21:51:24` | `cowrie.client.version` |
| `2026-06-24 21:51:24` | `cowrie.client.kex` |
| `2026-06-24 21:51:24` | `cowrie.login.success` |
| `2026-06-24 21:51:25` | `cowrie.session.params` |
| `2026-06-24 21:51:25` | `cowrie.command.input` |
| `2026-06-24 21:51:25` | `cowrie.log.closed` |
| `2026-06-24 21:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b16419e11f1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:52 |
| **Last Seen** | 2026-06-24 21:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:52:30` | `cowrie.session.connect` |
| `2026-06-24 21:52:30` | `cowrie.client.version` |
| `2026-06-24 21:52:30` | `cowrie.client.kex` |
| `2026-06-24 21:52:31` | `cowrie.login.success` |
| `2026-06-24 21:52:31` | `cowrie.session.params` |
| `2026-06-24 21:52:31` | `cowrie.command.input` |
| `2026-06-24 21:52:32` | `cowrie.log.closed` |
| `2026-06-24 21:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b2e7f0849c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:53 |
| **Last Seen** | 2026-06-24 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:53:37` | `cowrie.session.connect` |
| `2026-06-24 21:53:37` | `cowrie.client.version` |
| `2026-06-24 21:53:37` | `cowrie.client.kex` |
| `2026-06-24 21:53:38` | `cowrie.login.success` |
| `2026-06-24 21:53:39` | `cowrie.session.params` |
| `2026-06-24 21:53:39` | `cowrie.command.input` |
| `2026-06-24 21:53:39` | `cowrie.log.closed` |
| `2026-06-24 21:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e106e919c34

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:54 |
| **Last Seen** | 2026-06-24 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:54:45` | `cowrie.session.connect` |
| `2026-06-24 21:54:45` | `cowrie.client.version` |
| `2026-06-24 21:54:45` | `cowrie.client.kex` |
| `2026-06-24 21:54:45` | `cowrie.login.success` |
| `2026-06-24 21:54:46` | `cowrie.session.params` |
| `2026-06-24 21:54:46` | `cowrie.command.input` |
| `2026-06-24 21:54:46` | `cowrie.log.closed` |
| `2026-06-24 21:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee641ef0456

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:55 |
| **Last Seen** | 2026-06-24 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:55:51` | `cowrie.session.connect` |
| `2026-06-24 21:55:51` | `cowrie.client.version` |
| `2026-06-24 21:55:52` | `cowrie.client.kex` |
| `2026-06-24 21:55:52` | `cowrie.login.success` |
| `2026-06-24 21:55:53` | `cowrie.session.params` |
| `2026-06-24 21:55:53` | `cowrie.command.input` |
| `2026-06-24 21:55:53` | `cowrie.log.closed` |
| `2026-06-24 21:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9363570cb120

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:56 |
| **Last Seen** | 2026-06-24 21:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:56:58` | `cowrie.session.connect` |
| `2026-06-24 21:56:58` | `cowrie.client.version` |
| `2026-06-24 21:56:58` | `cowrie.client.kex` |
| `2026-06-24 21:56:59` | `cowrie.login.success` |
| `2026-06-24 21:57:00` | `cowrie.session.params` |
| `2026-06-24 21:57:00` | `cowrie.command.input` |
| `2026-06-24 21:57:00` | `cowrie.log.closed` |
| `2026-06-24 21:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd736563987

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:58 |
| **Last Seen** | 2026-06-24 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:58:06` | `cowrie.session.connect` |
| `2026-06-24 21:58:06` | `cowrie.client.version` |
| `2026-06-24 21:58:06` | `cowrie.client.kex` |
| `2026-06-24 21:58:06` | `cowrie.login.success` |
| `2026-06-24 21:58:07` | `cowrie.session.params` |
| `2026-06-24 21:58:07` | `cowrie.command.input` |
| `2026-06-24 21:58:07` | `cowrie.log.closed` |
| `2026-06-24 21:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37221eda952

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 21:59 |
| **Last Seen** | 2026-06-24 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 21:59:15` | `cowrie.session.connect` |
| `2026-06-24 21:59:15` | `cowrie.client.version` |
| `2026-06-24 21:59:15` | `cowrie.client.kex` |
| `2026-06-24 21:59:15` | `cowrie.login.success` |
| `2026-06-24 21:59:16` | `cowrie.session.params` |
| `2026-06-24 21:59:16` | `cowrie.command.input` |
| `2026-06-24 21:59:16` | `cowrie.log.closed` |
| `2026-06-24 21:59:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e1c8a2e28e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:00 |
| **Last Seen** | 2026-06-24 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:00:22` | `cowrie.session.connect` |
| `2026-06-24 22:00:22` | `cowrie.client.version` |
| `2026-06-24 22:00:22` | `cowrie.client.kex` |
| `2026-06-24 22:00:22` | `cowrie.login.success` |
| `2026-06-24 22:00:23` | `cowrie.session.params` |
| `2026-06-24 22:00:23` | `cowrie.command.input` |
| `2026-06-24 22:00:23` | `cowrie.log.closed` |
| `2026-06-24 22:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c550a1c101e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:01 |
| **Last Seen** | 2026-06-24 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:01:07` | `cowrie.session.connect` |
| `2026-06-24 22:01:07` | `cowrie.client.version` |
| `2026-06-24 22:01:07` | `cowrie.client.kex` |
| `2026-06-24 22:01:07` | `cowrie.login.success` |
| `2026-06-24 22:01:08` | `cowrie.session.params` |
| `2026-06-24 22:01:08` | `cowrie.command.input` |
| `2026-06-24 22:01:08` | `cowrie.log.closed` |
| `2026-06-24 22:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62862eea815

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:01 |
| **Last Seen** | 2026-06-24 22:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:01:51` | `cowrie.session.connect` |
| `2026-06-24 22:01:51` | `cowrie.client.version` |
| `2026-06-24 22:01:51` | `cowrie.client.kex` |
| `2026-06-24 22:01:51` | `cowrie.login.success` |
| `2026-06-24 22:01:52` | `cowrie.session.params` |
| `2026-06-24 22:01:52` | `cowrie.command.input` |
| `2026-06-24 22:01:53` | `cowrie.log.closed` |
| `2026-06-24 22:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9aec6ceee3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:02 |
| **Last Seen** | 2026-06-24 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:02:35` | `cowrie.session.connect` |
| `2026-06-24 22:02:35` | `cowrie.client.version` |
| `2026-06-24 22:02:35` | `cowrie.client.kex` |
| `2026-06-24 22:02:35` | `cowrie.login.success` |
| `2026-06-24 22:02:36` | `cowrie.session.params` |
| `2026-06-24 22:02:36` | `cowrie.command.input` |
| `2026-06-24 22:02:36` | `cowrie.log.closed` |
| `2026-06-24 22:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ed92ffad35

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 22:03 |
| **Last Seen** | 2026-06-24 22:03 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:03:04` | `cowrie.session.connect` |
| `2026-06-24 22:03:06` | `cowrie.client.version` |
| `2026-06-24 22:03:06` | `cowrie.client.kex` |
| `2026-06-24 22:03:11` | `cowrie.login.success` |
| `2026-06-24 22:03:15` | `cowrie.session.params` |
| `2026-06-24 22:03:15` | `cowrie.command.input` |
| `2026-06-24 22:03:17` | `cowrie.log.closed` |
| `2026-06-24 22:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536b679fcce8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:03 |
| **Last Seen** | 2026-06-24 22:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:03:18` | `cowrie.session.connect` |
| `2026-06-24 22:03:18` | `cowrie.client.version` |
| `2026-06-24 22:03:18` | `cowrie.client.kex` |
| `2026-06-24 22:03:19` | `cowrie.login.success` |
| `2026-06-24 22:03:20` | `cowrie.session.params` |
| `2026-06-24 22:03:20` | `cowrie.command.input` |
| `2026-06-24 22:03:20` | `cowrie.log.closed` |
| `2026-06-24 22:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf1c06a928c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:04 |
| **Last Seen** | 2026-06-24 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:04:02` | `cowrie.session.connect` |
| `2026-06-24 22:04:02` | `cowrie.client.version` |
| `2026-06-24 22:04:02` | `cowrie.client.kex` |
| `2026-06-24 22:04:02` | `cowrie.login.success` |
| `2026-06-24 22:04:03` | `cowrie.session.params` |
| `2026-06-24 22:04:03` | `cowrie.command.input` |
| `2026-06-24 22:04:03` | `cowrie.log.closed` |
| `2026-06-24 22:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fcd2b2e2f41

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:04 |
| **Last Seen** | 2026-06-24 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:04:45` | `cowrie.session.connect` |
| `2026-06-24 22:04:45` | `cowrie.client.version` |
| `2026-06-24 22:04:46` | `cowrie.client.kex` |
| `2026-06-24 22:04:46` | `cowrie.login.success` |
| `2026-06-24 22:04:47` | `cowrie.session.params` |
| `2026-06-24 22:04:47` | `cowrie.command.input` |
| `2026-06-24 22:04:47` | `cowrie.log.closed` |
| `2026-06-24 22:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cf94427c60

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:05 |
| **Last Seen** | 2026-06-24 22:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:05:31` | `cowrie.session.connect` |
| `2026-06-24 22:05:31` | `cowrie.client.version` |
| `2026-06-24 22:05:31` | `cowrie.client.kex` |
| `2026-06-24 22:05:31` | `cowrie.login.success` |
| `2026-06-24 22:05:32` | `cowrie.session.params` |
| `2026-06-24 22:05:32` | `cowrie.command.input` |
| `2026-06-24 22:05:32` | `cowrie.log.closed` |
| `2026-06-24 22:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c85775a176

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:06 |
| **Last Seen** | 2026-06-24 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:06:17` | `cowrie.session.connect` |
| `2026-06-24 22:06:17` | `cowrie.client.version` |
| `2026-06-24 22:06:17` | `cowrie.client.kex` |
| `2026-06-24 22:06:18` | `cowrie.login.success` |
| `2026-06-24 22:06:18` | `cowrie.session.params` |
| `2026-06-24 22:06:18` | `cowrie.command.input` |
| `2026-06-24 22:06:19` | `cowrie.log.closed` |
| `2026-06-24 22:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f71cd7cde99c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:07 |
| **Last Seen** | 2026-06-24 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:07:03` | `cowrie.session.connect` |
| `2026-06-24 22:07:03` | `cowrie.client.version` |
| `2026-06-24 22:07:03` | `cowrie.client.kex` |
| `2026-06-24 22:07:04` | `cowrie.login.success` |
| `2026-06-24 22:07:04` | `cowrie.session.params` |
| `2026-06-24 22:07:04` | `cowrie.command.input` |
| `2026-06-24 22:07:05` | `cowrie.log.closed` |
| `2026-06-24 22:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7904e30a580e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:07 |
| **Last Seen** | 2026-06-24 22:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:07:49` | `cowrie.session.connect` |
| `2026-06-24 22:07:49` | `cowrie.client.version` |
| `2026-06-24 22:07:49` | `cowrie.client.kex` |
| `2026-06-24 22:07:49` | `cowrie.login.success` |
| `2026-06-24 22:07:50` | `cowrie.session.params` |
| `2026-06-24 22:07:50` | `cowrie.command.input` |
| `2026-06-24 22:07:50` | `cowrie.log.closed` |
| `2026-06-24 22:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d56d5aa2494

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:08 |
| **Last Seen** | 2026-06-24 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:08:34` | `cowrie.session.connect` |
| `2026-06-24 22:08:34` | `cowrie.client.version` |
| `2026-06-24 22:08:34` | `cowrie.client.kex` |
| `2026-06-24 22:08:34` | `cowrie.login.success` |
| `2026-06-24 22:08:35` | `cowrie.session.params` |
| `2026-06-24 22:08:35` | `cowrie.command.input` |
| `2026-06-24 22:08:35` | `cowrie.log.closed` |
| `2026-06-24 22:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15505a859bfd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:09 |
| **Last Seen** | 2026-06-24 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:09:18` | `cowrie.session.connect` |
| `2026-06-24 22:09:18` | `cowrie.client.version` |
| `2026-06-24 22:09:18` | `cowrie.client.kex` |
| `2026-06-24 22:09:19` | `cowrie.login.success` |
| `2026-06-24 22:09:20` | `cowrie.session.params` |
| `2026-06-24 22:09:20` | `cowrie.command.input` |
| `2026-06-24 22:09:20` | `cowrie.log.closed` |
| `2026-06-24 22:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee61d1f4220c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:10 |
| **Last Seen** | 2026-06-24 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:10:04` | `cowrie.session.connect` |
| `2026-06-24 22:10:04` | `cowrie.client.version` |
| `2026-06-24 22:10:04` | `cowrie.client.kex` |
| `2026-06-24 22:10:04` | `cowrie.login.success` |
| `2026-06-24 22:10:05` | `cowrie.session.params` |
| `2026-06-24 22:10:05` | `cowrie.command.input` |
| `2026-06-24 22:10:05` | `cowrie.log.closed` |
| `2026-06-24 22:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfee7576b28c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:10 |
| **Last Seen** | 2026-06-24 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:10:49` | `cowrie.session.connect` |
| `2026-06-24 22:10:49` | `cowrie.client.version` |
| `2026-06-24 22:10:50` | `cowrie.client.kex` |
| `2026-06-24 22:10:50` | `cowrie.login.success` |
| `2026-06-24 22:10:51` | `cowrie.session.params` |
| `2026-06-24 22:10:51` | `cowrie.command.input` |
| `2026-06-24 22:10:51` | `cowrie.log.closed` |
| `2026-06-24 22:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a02fc0966d9c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:11 |
| **Last Seen** | 2026-06-24 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:11:35` | `cowrie.session.connect` |
| `2026-06-24 22:11:35` | `cowrie.client.version` |
| `2026-06-24 22:11:35` | `cowrie.client.kex` |
| `2026-06-24 22:11:35` | `cowrie.login.success` |
| `2026-06-24 22:11:36` | `cowrie.session.params` |
| `2026-06-24 22:11:36` | `cowrie.command.input` |
| `2026-06-24 22:11:36` | `cowrie.log.closed` |
| `2026-06-24 22:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e35e830b96c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:12 |
| **Last Seen** | 2026-06-24 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:12:22` | `cowrie.session.connect` |
| `2026-06-24 22:12:22` | `cowrie.client.version` |
| `2026-06-24 22:12:22` | `cowrie.client.kex` |
| `2026-06-24 22:12:23` | `cowrie.login.success` |
| `2026-06-24 22:12:23` | `cowrie.session.params` |
| `2026-06-24 22:12:23` | `cowrie.command.input` |
| `2026-06-24 22:12:24` | `cowrie.log.closed` |
| `2026-06-24 22:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f23ac58e6e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:13 |
| **Last Seen** | 2026-06-24 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:13:10` | `cowrie.session.connect` |
| `2026-06-24 22:13:10` | `cowrie.client.version` |
| `2026-06-24 22:13:10` | `cowrie.client.kex` |
| `2026-06-24 22:13:10` | `cowrie.login.success` |
| `2026-06-24 22:13:11` | `cowrie.session.params` |
| `2026-06-24 22:13:11` | `cowrie.command.input` |
| `2026-06-24 22:13:11` | `cowrie.log.closed` |
| `2026-06-24 22:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea0828741c57

| Field | Detail |
|---|---|
| **Source IP** | `120.26.240[.]78` |
| **First Seen** | 2026-06-24 22:13 |
| **Last Seen** | 2026-06-24 22:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:13:34` | `cowrie.session.connect` |
| `2026-06-24 22:13:34` | `cowrie.client.version` |
| `2026-06-24 22:13:34` | `cowrie.client.kex` |
| `2026-06-24 22:13:35` | `cowrie.login.success` |
| `2026-06-24 22:13:36` | `cowrie.session.params` |
| `2026-06-24 22:13:36` | `cowrie.command.input` |
| `2026-06-24 22:13:36` | `cowrie.log.closed` |
| `2026-06-24 22:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.240[.]78` to AbuseIPDB if not already reported
- [ ] Block `120.26.240[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b14b828dd7a1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:13 |
| **Last Seen** | 2026-06-24 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:13:57` | `cowrie.session.connect` |
| `2026-06-24 22:13:57` | `cowrie.client.version` |
| `2026-06-24 22:13:57` | `cowrie.client.kex` |
| `2026-06-24 22:13:58` | `cowrie.login.success` |
| `2026-06-24 22:13:59` | `cowrie.session.params` |
| `2026-06-24 22:13:59` | `cowrie.command.input` |
| `2026-06-24 22:13:59` | `cowrie.log.closed` |
| `2026-06-24 22:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4738d7c2a9

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-06-24 22:14 |
| **Last Seen** | 2026-06-24 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:14:21` | `cowrie.session.connect` |
| `2026-06-24 22:14:21` | `cowrie.client.version` |
| `2026-06-24 22:14:21` | `cowrie.client.kex` |
| `2026-06-24 22:14:21` | `cowrie.login.success` |
| `2026-06-24 22:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db586f1940dd

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-24 22:14 |
| **Last Seen** | 2026-06-24 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:14:21` | `cowrie.session.connect` |
| `2026-06-24 22:14:21` | `cowrie.client.version` |
| `2026-06-24 22:14:22` | `cowrie.client.kex` |
| `2026-06-24 22:14:22` | `cowrie.login.success` |
| `2026-06-24 22:14:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f876d60c16

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:14 |
| **Last Seen** | 2026-06-24 22:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:14:44` | `cowrie.session.connect` |
| `2026-06-24 22:14:44` | `cowrie.client.version` |
| `2026-06-24 22:14:44` | `cowrie.client.kex` |
| `2026-06-24 22:14:45` | `cowrie.login.success` |
| `2026-06-24 22:14:45` | `cowrie.session.params` |
| `2026-06-24 22:14:45` | `cowrie.command.input` |
| `2026-06-24 22:14:45` | `cowrie.log.closed` |
| `2026-06-24 22:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8be2d91c4b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:15 |
| **Last Seen** | 2026-06-24 22:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:15:30` | `cowrie.session.connect` |
| `2026-06-24 22:15:30` | `cowrie.client.version` |
| `2026-06-24 22:15:30` | `cowrie.client.kex` |
| `2026-06-24 22:15:31` | `cowrie.login.success` |
| `2026-06-24 22:15:32` | `cowrie.session.params` |
| `2026-06-24 22:15:32` | `cowrie.command.input` |
| `2026-06-24 22:15:32` | `cowrie.log.closed` |
| `2026-06-24 22:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-891f8063a394

| Field | Detail |
|---|---|
| **Source IP** | `185.226.196[.]15` |
| **First Seen** | 2026-06-24 22:15 |
| **Last Seen** | 2026-06-24 22:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:15:37` | `cowrie.session.connect` |
| `2026-06-24 22:15:37` | `cowrie.login.success` |
| `2026-06-24 22:15:37` | `cowrie.session.params` |
| `2026-06-24 22:15:37` | `cowrie.command.input` |
| `2026-06-24 22:15:37` | `cowrie.command.input` |
| `2026-06-24 22:15:37` | `cowrie.command.failed` |
| `2026-06-24 22:15:37` | `cowrie.command.input` |
| `2026-06-24 22:15:37` | `cowrie.command.failed` |
| `2026-06-24 22:15:37` | `cowrie.command.input` |
| `2026-06-24 22:15:38` | `cowrie.log.closed` |
| `2026-06-24 22:15:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.226.196[.]15` to AbuseIPDB if not already reported
- [ ] Block `185.226.196[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6506552178

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:16 |
| **Last Seen** | 2026-06-24 22:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:16:16` | `cowrie.session.connect` |
| `2026-06-24 22:16:16` | `cowrie.client.version` |
| `2026-06-24 22:16:16` | `cowrie.client.kex` |
| `2026-06-24 22:16:17` | `cowrie.login.success` |
| `2026-06-24 22:16:17` | `cowrie.session.params` |
| `2026-06-24 22:16:17` | `cowrie.command.input` |
| `2026-06-24 22:16:17` | `cowrie.log.closed` |
| `2026-06-24 22:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1ad6e5b8f8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:17 |
| **Last Seen** | 2026-06-24 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:17:02` | `cowrie.session.connect` |
| `2026-06-24 22:17:02` | `cowrie.client.version` |
| `2026-06-24 22:17:03` | `cowrie.client.kex` |
| `2026-06-24 22:17:03` | `cowrie.login.success` |
| `2026-06-24 22:17:04` | `cowrie.session.params` |
| `2026-06-24 22:17:04` | `cowrie.command.input` |
| `2026-06-24 22:17:04` | `cowrie.log.closed` |
| `2026-06-24 22:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a9aba26007

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 22:17 |
| **Last Seen** | 2026-06-24 22:17 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:17:26` | `cowrie.session.connect` |
| `2026-06-24 22:17:27` | `cowrie.client.version` |
| `2026-06-24 22:17:27` | `cowrie.client.kex` |
| `2026-06-24 22:17:34` | `cowrie.login.success` |
| `2026-06-24 22:17:37` | `cowrie.session.params` |
| `2026-06-24 22:17:37` | `cowrie.command.input` |
| `2026-06-24 22:17:39` | `cowrie.log.closed` |
| `2026-06-24 22:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88aaf3345646

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:17 |
| **Last Seen** | 2026-06-24 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:17:50` | `cowrie.session.connect` |
| `2026-06-24 22:17:50` | `cowrie.client.version` |
| `2026-06-24 22:17:50` | `cowrie.client.kex` |
| `2026-06-24 22:17:50` | `cowrie.login.success` |
| `2026-06-24 22:17:51` | `cowrie.session.params` |
| `2026-06-24 22:17:51` | `cowrie.command.input` |
| `2026-06-24 22:17:51` | `cowrie.log.closed` |
| `2026-06-24 22:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166c56d82a40

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:18 |
| **Last Seen** | 2026-06-24 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:18:39` | `cowrie.session.connect` |
| `2026-06-24 22:18:39` | `cowrie.client.version` |
| `2026-06-24 22:18:39` | `cowrie.client.kex` |
| `2026-06-24 22:18:39` | `cowrie.login.success` |
| `2026-06-24 22:18:40` | `cowrie.session.params` |
| `2026-06-24 22:18:40` | `cowrie.command.input` |
| `2026-06-24 22:18:40` | `cowrie.log.closed` |
| `2026-06-24 22:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-523b7b1e5921

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:19 |
| **Last Seen** | 2026-06-24 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:19:28` | `cowrie.session.connect` |
| `2026-06-24 22:19:28` | `cowrie.client.version` |
| `2026-06-24 22:19:28` | `cowrie.client.kex` |
| `2026-06-24 22:19:29` | `cowrie.login.success` |
| `2026-06-24 22:19:29` | `cowrie.session.params` |
| `2026-06-24 22:19:29` | `cowrie.command.input` |
| `2026-06-24 22:19:29` | `cowrie.log.closed` |
| `2026-06-24 22:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54548673b282

| Field | Detail |
|---|---|
| **Source IP** | `144.31.220[.]41` |
| **First Seen** | 2026-06-24 22:19 |
| **Last Seen** | 2026-06-24 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:19:37` | `cowrie.session.connect` |
| `2026-06-24 22:19:37` | `cowrie.client.version` |
| `2026-06-24 22:19:37` | `cowrie.client.kex` |
| `2026-06-24 22:19:38` | `cowrie.login.success` |
| `2026-06-24 22:19:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.31.220[.]41` to AbuseIPDB if not already reported
- [ ] Block `144.31.220[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d918c424011

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-06-24 22:19 |
| **Last Seen** | 2026-06-24 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:19:38` | `cowrie.session.connect` |
| `2026-06-24 22:19:38` | `cowrie.client.version` |
| `2026-06-24 22:19:39` | `cowrie.client.kex` |
| `2026-06-24 22:19:39` | `cowrie.login.success` |
| `2026-06-24 22:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5cecd522a21

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:20 |
| **Last Seen** | 2026-06-24 22:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:20:16` | `cowrie.session.connect` |
| `2026-06-24 22:20:16` | `cowrie.client.version` |
| `2026-06-24 22:20:16` | `cowrie.client.kex` |
| `2026-06-24 22:20:17` | `cowrie.login.success` |
| `2026-06-24 22:20:18` | `cowrie.session.params` |
| `2026-06-24 22:20:18` | `cowrie.command.input` |
| `2026-06-24 22:20:18` | `cowrie.log.closed` |
| `2026-06-24 22:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a63791681d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:21 |
| **Last Seen** | 2026-06-24 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:21:04` | `cowrie.session.connect` |
| `2026-06-24 22:21:04` | `cowrie.client.version` |
| `2026-06-24 22:21:04` | `cowrie.client.kex` |
| `2026-06-24 22:21:04` | `cowrie.login.success` |
| `2026-06-24 22:21:05` | `cowrie.session.params` |
| `2026-06-24 22:21:05` | `cowrie.command.input` |
| `2026-06-24 22:21:05` | `cowrie.log.closed` |
| `2026-06-24 22:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61dedab71f97

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:21 |
| **Last Seen** | 2026-06-24 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:21:51` | `cowrie.session.connect` |
| `2026-06-24 22:21:51` | `cowrie.client.version` |
| `2026-06-24 22:21:51` | `cowrie.client.kex` |
| `2026-06-24 22:21:52` | `cowrie.login.success` |
| `2026-06-24 22:21:53` | `cowrie.session.params` |
| `2026-06-24 22:21:53` | `cowrie.command.input` |
| `2026-06-24 22:21:53` | `cowrie.log.closed` |
| `2026-06-24 22:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d1d7f88d1e

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:22 |
| **Last Seen** | 2026-06-24 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:22:40` | `cowrie.session.connect` |
| `2026-06-24 22:22:40` | `cowrie.client.version` |
| `2026-06-24 22:22:40` | `cowrie.client.kex` |
| `2026-06-24 22:22:40` | `cowrie.login.success` |
| `2026-06-24 22:22:41` | `cowrie.session.params` |
| `2026-06-24 22:22:41` | `cowrie.command.input` |
| `2026-06-24 22:22:41` | `cowrie.log.closed` |
| `2026-06-24 22:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903e53d36624

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:23 |
| **Last Seen** | 2026-06-24 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:23:29` | `cowrie.session.connect` |
| `2026-06-24 22:23:29` | `cowrie.client.version` |
| `2026-06-24 22:23:29` | `cowrie.client.kex` |
| `2026-06-24 22:23:29` | `cowrie.login.success` |
| `2026-06-24 22:23:30` | `cowrie.session.params` |
| `2026-06-24 22:23:30` | `cowrie.command.input` |
| `2026-06-24 22:23:30` | `cowrie.log.closed` |
| `2026-06-24 22:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be2884e5a01a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:24 |
| **Last Seen** | 2026-06-24 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:24:18` | `cowrie.session.connect` |
| `2026-06-24 22:24:18` | `cowrie.client.version` |
| `2026-06-24 22:24:18` | `cowrie.client.kex` |
| `2026-06-24 22:24:19` | `cowrie.login.success` |
| `2026-06-24 22:24:19` | `cowrie.session.params` |
| `2026-06-24 22:24:19` | `cowrie.command.input` |
| `2026-06-24 22:24:20` | `cowrie.log.closed` |
| `2026-06-24 22:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34114480650

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:25 |
| **Last Seen** | 2026-06-24 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:25:08` | `cowrie.session.connect` |
| `2026-06-24 22:25:08` | `cowrie.client.version` |
| `2026-06-24 22:25:08` | `cowrie.client.kex` |
| `2026-06-24 22:25:08` | `cowrie.login.success` |
| `2026-06-24 22:25:09` | `cowrie.session.params` |
| `2026-06-24 22:25:09` | `cowrie.command.input` |
| `2026-06-24 22:25:09` | `cowrie.log.closed` |
| `2026-06-24 22:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2ed2beb0af

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:25 |
| **Last Seen** | 2026-06-24 22:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:25:57` | `cowrie.session.connect` |
| `2026-06-24 22:25:57` | `cowrie.client.version` |
| `2026-06-24 22:25:57` | `cowrie.client.kex` |
| `2026-06-24 22:25:57` | `cowrie.login.success` |
| `2026-06-24 22:25:58` | `cowrie.session.params` |
| `2026-06-24 22:25:58` | `cowrie.command.input` |
| `2026-06-24 22:25:58` | `cowrie.log.closed` |
| `2026-06-24 22:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3eba0cc2bd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:26 |
| **Last Seen** | 2026-06-24 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:26:46` | `cowrie.session.connect` |
| `2026-06-24 22:26:46` | `cowrie.client.version` |
| `2026-06-24 22:26:46` | `cowrie.client.kex` |
| `2026-06-24 22:26:47` | `cowrie.login.success` |
| `2026-06-24 22:26:47` | `cowrie.session.params` |
| `2026-06-24 22:26:47` | `cowrie.command.input` |
| `2026-06-24 22:26:48` | `cowrie.log.closed` |
| `2026-06-24 22:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed622263c30

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:27 |
| **Last Seen** | 2026-06-24 22:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:27:35` | `cowrie.session.connect` |
| `2026-06-24 22:27:35` | `cowrie.client.version` |
| `2026-06-24 22:27:35` | `cowrie.client.kex` |
| `2026-06-24 22:27:36` | `cowrie.login.success` |
| `2026-06-24 22:27:36` | `cowrie.session.params` |
| `2026-06-24 22:27:36` | `cowrie.command.input` |
| `2026-06-24 22:27:36` | `cowrie.log.closed` |
| `2026-06-24 22:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f805c626c96b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:28 |
| **Last Seen** | 2026-06-24 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:28:23` | `cowrie.session.connect` |
| `2026-06-24 22:28:23` | `cowrie.client.version` |
| `2026-06-24 22:28:23` | `cowrie.client.kex` |
| `2026-06-24 22:28:24` | `cowrie.login.success` |
| `2026-06-24 22:28:24` | `cowrie.session.params` |
| `2026-06-24 22:28:24` | `cowrie.command.input` |
| `2026-06-24 22:28:25` | `cowrie.log.closed` |
| `2026-06-24 22:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f4d6b9d51f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:29 |
| **Last Seen** | 2026-06-24 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:29:12` | `cowrie.session.connect` |
| `2026-06-24 22:29:12` | `cowrie.client.version` |
| `2026-06-24 22:29:12` | `cowrie.client.kex` |
| `2026-06-24 22:29:12` | `cowrie.login.success` |
| `2026-06-24 22:29:13` | `cowrie.session.params` |
| `2026-06-24 22:29:13` | `cowrie.command.input` |
| `2026-06-24 22:29:13` | `cowrie.log.closed` |
| `2026-06-24 22:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b71f76fcbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:30 |
| **Last Seen** | 2026-06-24 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:30:01` | `cowrie.session.connect` |
| `2026-06-24 22:30:01` | `cowrie.client.version` |
| `2026-06-24 22:30:01` | `cowrie.client.kex` |
| `2026-06-24 22:30:01` | `cowrie.login.success` |
| `2026-06-24 22:30:02` | `cowrie.session.params` |
| `2026-06-24 22:30:02` | `cowrie.command.input` |
| `2026-06-24 22:30:02` | `cowrie.log.closed` |
| `2026-06-24 22:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df082705af83

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:30 |
| **Last Seen** | 2026-06-24 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:30:51` | `cowrie.session.connect` |
| `2026-06-24 22:30:51` | `cowrie.client.version` |
| `2026-06-24 22:30:51` | `cowrie.client.kex` |
| `2026-06-24 22:30:51` | `cowrie.login.success` |
| `2026-06-24 22:30:52` | `cowrie.session.params` |
| `2026-06-24 22:30:52` | `cowrie.command.input` |
| `2026-06-24 22:30:52` | `cowrie.log.closed` |
| `2026-06-24 22:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a79062c65a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:31 |
| **Last Seen** | 2026-06-24 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:31:42` | `cowrie.session.connect` |
| `2026-06-24 22:31:42` | `cowrie.client.version` |
| `2026-06-24 22:31:42` | `cowrie.client.kex` |
| `2026-06-24 22:31:42` | `cowrie.login.success` |
| `2026-06-24 22:31:43` | `cowrie.session.params` |
| `2026-06-24 22:31:43` | `cowrie.command.input` |
| `2026-06-24 22:31:43` | `cowrie.log.closed` |
| `2026-06-24 22:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94cb15e1dcc9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 22:31 |
| **Last Seen** | 2026-06-24 22:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:31:51` | `cowrie.session.connect` |
| `2026-06-24 22:31:52` | `cowrie.client.version` |
| `2026-06-24 22:31:52` | `cowrie.client.kex` |
| `2026-06-24 22:31:58` | `cowrie.login.success` |
| `2026-06-24 22:32:02` | `cowrie.session.params` |
| `2026-06-24 22:32:02` | `cowrie.command.input` |
| `2026-06-24 22:32:03` | `cowrie.log.closed` |
| `2026-06-24 22:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-187848e1c4f7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:32 |
| **Last Seen** | 2026-06-24 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:32:33` | `cowrie.session.connect` |
| `2026-06-24 22:32:33` | `cowrie.client.version` |
| `2026-06-24 22:32:33` | `cowrie.client.kex` |
| `2026-06-24 22:32:33` | `cowrie.login.success` |
| `2026-06-24 22:32:34` | `cowrie.session.params` |
| `2026-06-24 22:32:34` | `cowrie.command.input` |
| `2026-06-24 22:32:34` | `cowrie.log.closed` |
| `2026-06-24 22:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5992ad865cbe

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:33 |
| **Last Seen** | 2026-06-24 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:33:24` | `cowrie.session.connect` |
| `2026-06-24 22:33:24` | `cowrie.client.version` |
| `2026-06-24 22:33:24` | `cowrie.client.kex` |
| `2026-06-24 22:33:24` | `cowrie.login.success` |
| `2026-06-24 22:33:25` | `cowrie.session.params` |
| `2026-06-24 22:33:25` | `cowrie.command.input` |
| `2026-06-24 22:33:25` | `cowrie.log.closed` |
| `2026-06-24 22:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a278ff7efbeb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:34 |
| **Last Seen** | 2026-06-24 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:34:13` | `cowrie.session.connect` |
| `2026-06-24 22:34:13` | `cowrie.client.version` |
| `2026-06-24 22:34:13` | `cowrie.client.kex` |
| `2026-06-24 22:34:14` | `cowrie.login.success` |
| `2026-06-24 22:34:15` | `cowrie.session.params` |
| `2026-06-24 22:34:15` | `cowrie.command.input` |
| `2026-06-24 22:34:15` | `cowrie.log.closed` |
| `2026-06-24 22:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9665e41c611

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:35 |
| **Last Seen** | 2026-06-24 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:35:03` | `cowrie.session.connect` |
| `2026-06-24 22:35:03` | `cowrie.client.version` |
| `2026-06-24 22:35:03` | `cowrie.client.kex` |
| `2026-06-24 22:35:03` | `cowrie.login.success` |
| `2026-06-24 22:35:04` | `cowrie.session.params` |
| `2026-06-24 22:35:04` | `cowrie.command.input` |
| `2026-06-24 22:35:04` | `cowrie.log.closed` |
| `2026-06-24 22:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df218eb0486b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:35 |
| **Last Seen** | 2026-06-24 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:35:53` | `cowrie.session.connect` |
| `2026-06-24 22:35:53` | `cowrie.client.version` |
| `2026-06-24 22:35:53` | `cowrie.client.kex` |
| `2026-06-24 22:35:54` | `cowrie.login.success` |
| `2026-06-24 22:35:54` | `cowrie.session.params` |
| `2026-06-24 22:35:54` | `cowrie.command.input` |
| `2026-06-24 22:35:54` | `cowrie.log.closed` |
| `2026-06-24 22:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32df9cb1e4eb

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:36 |
| **Last Seen** | 2026-06-24 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:36:44` | `cowrie.session.connect` |
| `2026-06-24 22:36:44` | `cowrie.client.version` |
| `2026-06-24 22:36:45` | `cowrie.client.kex` |
| `2026-06-24 22:36:45` | `cowrie.login.success` |
| `2026-06-24 22:36:46` | `cowrie.session.params` |
| `2026-06-24 22:36:46` | `cowrie.command.input` |
| `2026-06-24 22:36:46` | `cowrie.log.closed` |
| `2026-06-24 22:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e56243d2eff8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:37 |
| **Last Seen** | 2026-06-24 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:37:37` | `cowrie.session.connect` |
| `2026-06-24 22:37:37` | `cowrie.client.version` |
| `2026-06-24 22:37:37` | `cowrie.client.kex` |
| `2026-06-24 22:37:37` | `cowrie.login.success` |
| `2026-06-24 22:37:38` | `cowrie.session.params` |
| `2026-06-24 22:37:38` | `cowrie.command.input` |
| `2026-06-24 22:37:38` | `cowrie.log.closed` |
| `2026-06-24 22:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06874289fc6c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:38 |
| **Last Seen** | 2026-06-24 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:38:31` | `cowrie.session.connect` |
| `2026-06-24 22:38:31` | `cowrie.client.version` |
| `2026-06-24 22:38:31` | `cowrie.client.kex` |
| `2026-06-24 22:38:31` | `cowrie.login.success` |
| `2026-06-24 22:38:32` | `cowrie.session.params` |
| `2026-06-24 22:38:32` | `cowrie.command.input` |
| `2026-06-24 22:38:32` | `cowrie.log.closed` |
| `2026-06-24 22:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015b6c6d3da3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:39 |
| **Last Seen** | 2026-06-24 22:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:39:24` | `cowrie.session.connect` |
| `2026-06-24 22:39:24` | `cowrie.client.version` |
| `2026-06-24 22:39:24` | `cowrie.client.kex` |
| `2026-06-24 22:39:25` | `cowrie.login.success` |
| `2026-06-24 22:39:26` | `cowrie.session.params` |
| `2026-06-24 22:39:26` | `cowrie.command.input` |
| `2026-06-24 22:39:26` | `cowrie.log.closed` |
| `2026-06-24 22:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5374d9b841a7

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:40 |
| **Last Seen** | 2026-06-24 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:40:18` | `cowrie.session.connect` |
| `2026-06-24 22:40:18` | `cowrie.client.version` |
| `2026-06-24 22:40:18` | `cowrie.client.kex` |
| `2026-06-24 22:40:19` | `cowrie.login.success` |
| `2026-06-24 22:40:19` | `cowrie.session.params` |
| `2026-06-24 22:40:19` | `cowrie.command.input` |
| `2026-06-24 22:40:19` | `cowrie.log.closed` |
| `2026-06-24 22:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e908795077

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:41 |
| **Last Seen** | 2026-06-24 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:41:10` | `cowrie.session.connect` |
| `2026-06-24 22:41:10` | `cowrie.client.version` |
| `2026-06-24 22:41:10` | `cowrie.client.kex` |
| `2026-06-24 22:41:11` | `cowrie.login.success` |
| `2026-06-24 22:41:12` | `cowrie.session.params` |
| `2026-06-24 22:41:12` | `cowrie.command.input` |
| `2026-06-24 22:41:12` | `cowrie.log.closed` |
| `2026-06-24 22:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07deed6d40a3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:42 |
| **Last Seen** | 2026-06-24 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:42:02` | `cowrie.session.connect` |
| `2026-06-24 22:42:02` | `cowrie.client.version` |
| `2026-06-24 22:42:02` | `cowrie.client.kex` |
| `2026-06-24 22:42:02` | `cowrie.login.success` |
| `2026-06-24 22:42:03` | `cowrie.session.params` |
| `2026-06-24 22:42:03` | `cowrie.command.input` |
| `2026-06-24 22:42:03` | `cowrie.log.closed` |
| `2026-06-24 22:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e39c0b9302

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:42 |
| **Last Seen** | 2026-06-24 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:42:55` | `cowrie.session.connect` |
| `2026-06-24 22:42:55` | `cowrie.client.version` |
| `2026-06-24 22:42:55` | `cowrie.client.kex` |
| `2026-06-24 22:42:55` | `cowrie.login.success` |
| `2026-06-24 22:42:56` | `cowrie.session.params` |
| `2026-06-24 22:42:56` | `cowrie.command.input` |
| `2026-06-24 22:42:56` | `cowrie.log.closed` |
| `2026-06-24 22:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c16b04bfd85a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:43 |
| **Last Seen** | 2026-06-24 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:43:52` | `cowrie.session.connect` |
| `2026-06-24 22:43:52` | `cowrie.client.version` |
| `2026-06-24 22:43:52` | `cowrie.client.kex` |
| `2026-06-24 22:43:53` | `cowrie.login.success` |
| `2026-06-24 22:43:53` | `cowrie.session.params` |
| `2026-06-24 22:43:53` | `cowrie.command.input` |
| `2026-06-24 22:43:54` | `cowrie.log.closed` |
| `2026-06-24 22:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce8d537c00c

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:44 |
| **Last Seen** | 2026-06-24 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:44:45` | `cowrie.session.connect` |
| `2026-06-24 22:44:45` | `cowrie.client.version` |
| `2026-06-24 22:44:45` | `cowrie.client.kex` |
| `2026-06-24 22:44:46` | `cowrie.login.success` |
| `2026-06-24 22:44:46` | `cowrie.session.params` |
| `2026-06-24 22:44:46` | `cowrie.command.input` |
| `2026-06-24 22:44:47` | `cowrie.log.closed` |
| `2026-06-24 22:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a36e16aa80a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:45 |
| **Last Seen** | 2026-06-24 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:45:37` | `cowrie.session.connect` |
| `2026-06-24 22:45:37` | `cowrie.client.version` |
| `2026-06-24 22:45:38` | `cowrie.client.kex` |
| `2026-06-24 22:45:38` | `cowrie.login.success` |
| `2026-06-24 22:45:39` | `cowrie.session.params` |
| `2026-06-24 22:45:39` | `cowrie.command.input` |
| `2026-06-24 22:45:39` | `cowrie.log.closed` |
| `2026-06-24 22:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46e554b9ac05

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-06-24 22:46 |
| **Last Seen** | 2026-06-24 22:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:46:01` | `cowrie.session.connect` |
| `2026-06-24 22:46:02` | `cowrie.client.version` |
| `2026-06-24 22:46:02` | `cowrie.client.kex` |
| `2026-06-24 22:46:08` | `cowrie.login.success` |
| `2026-06-24 22:46:12` | `cowrie.session.params` |
| `2026-06-24 22:46:12` | `cowrie.command.input` |
| `2026-06-24 22:46:13` | `cowrie.log.closed` |
| `2026-06-24 22:46:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fd3068f26b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:46 |
| **Last Seen** | 2026-06-24 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:46:29` | `cowrie.session.connect` |
| `2026-06-24 22:46:29` | `cowrie.client.version` |
| `2026-06-24 22:46:29` | `cowrie.client.kex` |
| `2026-06-24 22:46:30` | `cowrie.login.success` |
| `2026-06-24 22:46:30` | `cowrie.session.params` |
| `2026-06-24 22:46:30` | `cowrie.command.input` |
| `2026-06-24 22:46:31` | `cowrie.log.closed` |
| `2026-06-24 22:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca7d96382c6

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:47 |
| **Last Seen** | 2026-06-24 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:47:20` | `cowrie.session.connect` |
| `2026-06-24 22:47:20` | `cowrie.client.version` |
| `2026-06-24 22:47:20` | `cowrie.client.kex` |
| `2026-06-24 22:47:21` | `cowrie.login.success` |
| `2026-06-24 22:47:21` | `cowrie.session.params` |
| `2026-06-24 22:47:21` | `cowrie.command.input` |
| `2026-06-24 22:47:22` | `cowrie.log.closed` |
| `2026-06-24 22:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aefef4e84c9

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:48 |
| **Last Seen** | 2026-06-24 22:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:48:12` | `cowrie.session.connect` |
| `2026-06-24 22:48:12` | `cowrie.client.version` |
| `2026-06-24 22:48:12` | `cowrie.client.kex` |
| `2026-06-24 22:48:12` | `cowrie.login.success` |
| `2026-06-24 22:48:13` | `cowrie.session.params` |
| `2026-06-24 22:48:13` | `cowrie.command.input` |
| `2026-06-24 22:48:13` | `cowrie.log.closed` |
| `2026-06-24 22:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad838bdaa0e1

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:49 |
| **Last Seen** | 2026-06-24 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:49:04` | `cowrie.session.connect` |
| `2026-06-24 22:49:04` | `cowrie.client.version` |
| `2026-06-24 22:49:04` | `cowrie.client.kex` |
| `2026-06-24 22:49:04` | `cowrie.login.success` |
| `2026-06-24 22:49:05` | `cowrie.session.params` |
| `2026-06-24 22:49:05` | `cowrie.command.input` |
| `2026-06-24 22:49:05` | `cowrie.log.closed` |
| `2026-06-24 22:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c69253c836

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:49 |
| **Last Seen** | 2026-06-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:49:58` | `cowrie.session.connect` |
| `2026-06-24 22:49:58` | `cowrie.client.version` |
| `2026-06-24 22:49:58` | `cowrie.client.kex` |
| `2026-06-24 22:49:59` | `cowrie.login.success` |
| `2026-06-24 22:49:59` | `cowrie.session.params` |
| `2026-06-24 22:49:59` | `cowrie.command.input` |
| `2026-06-24 22:50:00` | `cowrie.log.closed` |
| `2026-06-24 22:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085881d44946

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:50 |
| **Last Seen** | 2026-06-24 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:50:53` | `cowrie.session.connect` |
| `2026-06-24 22:50:53` | `cowrie.client.version` |
| `2026-06-24 22:50:53` | `cowrie.client.kex` |
| `2026-06-24 22:50:54` | `cowrie.login.success` |
| `2026-06-24 22:50:54` | `cowrie.session.params` |
| `2026-06-24 22:50:54` | `cowrie.command.input` |
| `2026-06-24 22:50:55` | `cowrie.log.closed` |
| `2026-06-24 22:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af2c711d9f4

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:51 |
| **Last Seen** | 2026-06-24 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:51:47` | `cowrie.session.connect` |
| `2026-06-24 22:51:47` | `cowrie.client.version` |
| `2026-06-24 22:51:47` | `cowrie.client.kex` |
| `2026-06-24 22:51:48` | `cowrie.login.success` |
| `2026-06-24 22:51:48` | `cowrie.session.params` |
| `2026-06-24 22:51:48` | `cowrie.command.input` |
| `2026-06-24 22:51:48` | `cowrie.log.closed` |
| `2026-06-24 22:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c54236304ab

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:52 |
| **Last Seen** | 2026-06-24 22:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:52:40` | `cowrie.session.connect` |
| `2026-06-24 22:52:40` | `cowrie.client.version` |
| `2026-06-24 22:52:40` | `cowrie.client.kex` |
| `2026-06-24 22:52:40` | `cowrie.login.success` |
| `2026-06-24 22:52:41` | `cowrie.session.params` |
| `2026-06-24 22:52:41` | `cowrie.command.input` |
| `2026-06-24 22:52:41` | `cowrie.log.closed` |
| `2026-06-24 22:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52efdc22ca51

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:53 |
| **Last Seen** | 2026-06-24 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:53:33` | `cowrie.session.connect` |
| `2026-06-24 22:53:33` | `cowrie.client.version` |
| `2026-06-24 22:53:33` | `cowrie.client.kex` |
| `2026-06-24 22:53:34` | `cowrie.login.success` |
| `2026-06-24 22:53:34` | `cowrie.session.params` |
| `2026-06-24 22:53:34` | `cowrie.command.input` |
| `2026-06-24 22:53:35` | `cowrie.log.closed` |
| `2026-06-24 22:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.185[.]59` to AbuseIPDB if not already reported
- [ ] Block `209.99.185[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-572b40e2e37b

| Field | Detail |
|---|---|
| **Source IP** | `209.99.185[.]59` |
| **First Seen** | 2026-06-24 22:54 |
| **Last Seen** | 2026-06-24 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 22:54:25` | `cowrie.session.connect` |
| `2026-06-24 22:54:25` | `cowrie.client.version` |
| `2026-06-24 22:54:25` | `cowrie.client.kex` |
| `2026-06-24 22:54:26` | `cowrie.login.success` |
| `2026-06-24 22:54:26` | `cowrie.session.params` |
| `2026-06-24 22:54:26` | `cowrie.command.input` |
| `2026-06-24 22:54:26` | `cowrie.log.closed` |
| `2026-06-24 22:54:26` | `cowrie.session.closed` |

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
| `209.99.185[.]59` | **260** | 2026-06-24 18:55 | 2026-06-24 22:54 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `92.204.138[.]142` | **61** | 2026-06-24 19:06 | 2026-06-24 22:54 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `185.226.196[.]12` | **4** | 2026-06-24 22:15 | 2026-06-24 22:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-06-24 19:12 | 2026-06-24 22:08 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `185.226.196[.]14` | **3** | 2026-06-24 22:16 | 2026-06-24 22:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]43` | **3** | 2026-06-24 21:31 | 2026-06-24 21:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]37` | **3** | 2026-06-24 21:30 | 2026-06-24 21:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]86` | **3** | 2026-06-24 21:31 | 2026-06-24 21:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.181[.]68` | **2** | 2026-06-24 19:08 | 2026-06-24 19:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]15` | **2** | 2026-06-24 22:15 | 2026-06-24 22:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]88` | **2** | 2026-06-24 19:36 | 2026-06-24 19:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `36.134.211[.]199` | **2** | 2026-06-24 19:40 | 2026-06-24 19:42 | 2m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-06-24 20:39 | 2026-06-24 20:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.74.213[.]140` | **2** | 2026-06-24 20:40 | 2026-06-24 20:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.222.86[.]210` | **2** | 2026-06-24 21:23 | 2026-06-24 21:25 | 2m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]233` | **2** | 2026-06-24 19:42 | 2026-06-24 19:53 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]77` | **2** | 2026-06-24 20:36 | 2026-06-24 20:40 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.29.34[.]90` | 1 | 2026-06-24 19:34 | 2026-06-24 19:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-06-24 20:38 | 2026-06-24 20:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `172.104.210[.]105` | 1 | 2026-06-24 20:58 | 2026-06-24 20:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.107.80[.]93` | 1 | 2026-06-24 19:19 | 2026-06-24 19:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]13` | 1 | 2026-06-24 22:16 | 2026-06-24 22:16 | 5s | 0 | `T1592` | 🟢 LOW |
| `188.113.80[.]177` | 1 | 2026-06-24 21:12 | 2026-06-24 21:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]101` | 1 | 2026-06-24 22:51 | 2026-06-24 22:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `218.15.121[.]54` | 1 | 2026-06-24 21:04 | 2026-06-24 21:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-06-24 19:57 | 2026-06-24 19:57 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.79.5[.]11` | 1 | 2026-06-24 21:01 | 2026-06-24 21:01 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]63` | 1 | 2026-06-24 20:36 | 2026-06-24 20:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `71.31.179[.]88` | 1 | 2026-06-24 19:39 | 2026-06-24 19:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-06-24 20:33 | 2026-06-24 20:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.134.124[.]8` | 1 | 2026-06-24 19:18 | 2026-06-24 19:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]1` | 1 | 2026-06-24 22:20 | 2026-06-24 22:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-06-24 19:15 | 2026-06-24 19:15 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (31 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 61/100 | 🟡 MEDIUM | **3/75** 🔴 |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **21/73** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **42/74** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 60/100 | 🟡 MEDIUM | 0/76 ✅ |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `ce3cb467257e402122e4ab5f3f40fefcbdb4a662664659672a38967ee8aaaad0` | ELF Binary (Linux executable) (x86-64 64-bit) | `ce3cb467257e4021...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `d46555af1173d22f07c37ef9c1e0e74fd68db022f2b6fb3ab5388d2c5bc6a98e` | Bash Script | `d46555af1173d22f...` | 70/100 | 🔴 HIGH | **26/75** 🔴 |
| `dbb7ebb960dc0d5a480f97ddde3a227a2d83fcaca7d37ae672e6a0a6785631e9` | ELF Binary (Linux executable) (AArch64 64-bit) | `dbb7ebb960dc0d5a...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
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
| `144.22.238[.]238` | BR | Oracle Corporation | **100** ⚠️ | 3 |
| `144.31.220[.]41` | DE | aurorix networks | **100** ⚠️ | 1 |
| `36.134.211[.]199` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `185.226.196[.]14` | US | ICG-3-ZEN-LAX | **100** ⚠️ | 50 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `45.33.14[.]5` | US | Linode | **100** ⚠️ | 50 |
| `91.92.40[.]233` | NL | TechTies Inc. | **100** ⚠️ | 9 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `85.217.149[.]1` | CA | NL MODAT | **100** ⚠️ | 50 |
| `8.134.124[.]8` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 332 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 308 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 11 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Known scanner ISP: University of Illinois Chicago | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 698 cases |
| Tool 34  | Credential Extractor        | ✅ 325 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 31 files |
| Tool 33  | YARA Classifier             | ✅ 26 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 307 priority case(s) shown individually · 33 recon entry/entries in table (17 group(s) consolidating 358 session(s)).

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
_Report time: 2026-06-24T23:08:33Z_
